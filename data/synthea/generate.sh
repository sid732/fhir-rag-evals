#!/usr/bin/env bash
# Regenerate the synthetic eval cohort in data/cohort/ from a pinned Synthea release.
#
# Synthea documents that the same version and seed produce the same population,
# so every input that affects the output is fixed below. Raw output goes to a
# temp directory; only gzipped bundles and a manifest land in data/cohort/.
set -euo pipefail
export LC_ALL=C # stable sort order for globs and the manifest

SYNTHEA_VERSION="v4.0.0"
JAR_URL="https://github.com/synthetichealth/synthea/releases/download/${SYNTHEA_VERSION}/synthea-with-dependencies.jar"
JAR_SHA256="ed43c20ad40ba5c3bc724503a5af032715fe3c491620b766148e7c2361e6ecc1" # GitHub's digest for the asset

# Synthea defaults all four of these to the current time.
SEED=20261020           # -s: population seed
CLINICIAN_SEED=20261020 # -cs: clinician assignment seed
REFERENCE_DATE=20261001 # -r: date ages (-a) are measured at, YYYYMMDD
END_DATE=20261001       # -e: date the simulation stops, YYYYMMDD

POPULATION=15   # -p: living patients
AGE_RANGE=35-85 # -a: adults, whose records have chronic conditions, labs and medications
STATE=Massachusetts

REPO_ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/../.." && pwd)"
COHORT_DIR="${REPO_ROOT}/data/cohort"
CACHE_DIR="${XDG_CACHE_HOME:-$HOME/.cache}/fhir-rag-evals"
JAR="${CACHE_DIR}/synthea-${SYNTHEA_VERSION}.jar"

command -v java >/dev/null || { echo "java not found; Synthea ${SYNTHEA_VERSION} needs JDK 17+" >&2; exit 1; }

mkdir -p "$CACHE_DIR"
if [[ ! -f "$JAR" ]]; then
  echo "Downloading Synthea ${SYNTHEA_VERSION} (about 200 MB) to ${CACHE_DIR}"
  curl --fail --location --silent --show-error --output "${JAR}.part" "$JAR_URL"
  mv "${JAR}.part" "$JAR"
fi
echo "${JAR_SHA256}  ${JAR}" | shasum -a 256 --check --status ||
  { echo "checksum mismatch for ${JAR}; delete it and rerun" >&2; exit 1; }

WORK_DIR="$(mktemp -d)"
trap 'rm -rf "$WORK_DIR"' EXIT

# Settings we rely on are passed even where they match the default, so a
# Synthea upgrade can't change them silently. US Core also turns on the
# per-encounter clinical notes. When a simulated person dies early, Synthea
# retries with a new one; only_alive_patients drops the dead attempts, whose
# records end decades ago.
echo "Running Synthea (its log is printed only if it fails)"
if ! java -jar "$JAR" \
  -s "$SEED" -cs "$CLINICIAN_SEED" -r "$REFERENCE_DATE" -e "$END_DATE" \
  -p "$POPULATION" -a "$AGE_RANGE" \
  --generate.only_alive_patients true \
  --exporter.baseDirectory "${WORK_DIR}/out" \
  --exporter.use_uuid_filenames true \
  --exporter.years_of_history 10 \
  --exporter.fhir.export true \
  --exporter.fhir.use_us_core_ig true \
  --exporter.fhir.transaction_bundle true \
  "$STATE" >"${WORK_DIR}/synthea.log" 2>&1; then
  tail -n 30 "${WORK_DIR}/synthea.log" >&2
  exit 1
fi

rm -rf "${COHORT_DIR:?}"
mkdir -p "$COHORT_DIR"
for src in "${WORK_DIR}"/out/fhir/*.json; do
  name="$(basename "$src")"
  case "$name" in # these two carry a run timestamp in their names
    hospitalInformation*) name="hospitalInformation.json" ;;
    practitionerInformation*) name="practitionerInformation.json" ;;
  esac
  gzip -n -c "$src" >"${COHORT_DIR}/${name}.gz" # -n: no timestamp in the gzip header
done

# Hash the JSON inside each file, not the .gz bytes, so the manifest doesn't
# depend on which gzip implementation compressed it.
for gz in "${COHORT_DIR}"/*.json.gz; do
  printf '%s  %s\n' "$(gzip -dc "$gz" | shasum -a 256 | cut -d ' ' -f 1)" "$(basename "${gz%.gz}")"
done >"${COHORT_DIR}/MANIFEST.sha256"

count="$(find "$COHORT_DIR" -name '*.json.gz' ! -name '*Information.json.gz' | wc -l | tr -d ' ')"
echo "Wrote ${count} patient bundles to data/cohort/ ($(du -sh "$COHORT_DIR" | awk '{print $1}'))"
