# fhir-rag-evals: design

What the service does, the decisions behind it, what changed while it was built, and what comes next. Results are in the [README](../README.md); how the evals work is in [evals.md](evals.md).

## Summary

- **What it is.** A FastAPI service that answers a clinician's question about one synthetic patient. Every sentence in the answer cites the FHIR R4 resources it relies on, and every citation resolves to an endpoint that returns that resource. An evaluation harness measures retrieval and answer quality and runs in CI.
- **Data.** A pinned Synthea v4.0.0 cohort: 15 adult patients, FHIR R4 with US Core 6.1.0 profiles, Massachusetts. Synthetic only. No real or de-identified patient data anywhere in the project.
- **Retrieval.** Filtered to one patient before ranking. BM25 plus local embeddings, fused with Reciprocal Rank Fusion, with series expansion and a pinned patient summary. SQLite and numpy, no vector database.
- **Generation.** Claude with structured output: sentences with cited resource references, or an explicit "not in record". Code checks every citation against what the model was shown.
- **Evals.** 275 labeled questions with gold labels computed from the raw FHIR bundles by code, split into dev and a held-out test set. Metrics: retrieval hit rate, recall and MRR; citation validity, precision and recall; faithfulness (an LLM judge checked against blind reference labels, plus a deterministic check on numbers and dates); abstention; latency and cost. Confidence intervals on every number.
- **CI.** The retrieval eval is deterministic and free, so it gates every push and pull request. The answer eval costs money and varies run to run, so it runs on demand, with a spend cap.

## Scope

In scope: ingest, a question-answering endpoint for one patient at a time, the eval harness, CI, Docker.

Out of scope, with the reason:

- Real PHI, or de-identified real data such as MIMIC: the project is synthetic-only by rule.
- Authentication and authorization: described in the README (SMART on FHIR scopes), not built. It would take a week and isn't what the project is meant to show.
- Questions across patients (cohort queries): a different retrieval problem. It is the point where a vector index would earn its place.
- Writing back to a FHIR server, agents, fine-tuning.
- A UI beyond the OpenAPI docs page.

## Architecture

```
Synthea v4.0.0 (pinned jar, seed, clinician seed, reference date, end date)
  |  one FHIR R4 transaction Bundle per patient (US Core 6.1.0)
  v
ingest
  parse an allowlist of resource types into typed views
  render one text "card" per resource (notes split into sections)
  build the pinned summary, embed the cards
  v
SQLite: resources, cards, summary, embeddings
  v
FastAPI
  GET  /health
  GET  /patients
  GET  /patients/{id}
  GET  /patients/{id}/resources/{type}/{rid}    every citation resolves here
  POST /patients/{id}/ask   {"question": "..."}
         1. retrieve   filter to the patient, BM25 + dense, fuse with RRF,
                       series expansion, pinned summary in front
         2. generate   Claude, structured output: sentences with cited refs,
                       or status "not_in_record"
         3. validate   remove and count citations to cards the model wasn't shown
         4. respond    answer, citations, retrieved refs, usage, cost, latency

evals/
  questions/questions.jsonl   built from the cohort by make questions
  run_retrieval               no API key; runs on every push
  run_answers, rejudge        call Claude; on demand
  reports/*.md                one per run, plus per-question rows in runs/<name>/
```

## Design decisions

Each entry gives the decision, why, what else was considered, and what would change it.

### D1. Synthetic data from Synthea, pinned and committed

- **Decision.** Generate the cohort with Synthea v4.0.0 (released 2026-03-05): a pinned jar with a recorded SHA-256, a fixed seed (`-s`), clinician seed (`-cs`), reference date (`-r`), end date (`-e`) and population size (`-p`), state Massachusetts, living patients only. Commit the generated cohort, filtered and gzipped, to the repo.
- **Why.** Synthea produces longitudinal FHIR R4 records coded with SNOMED CT, LOINC, RxNorm and CVX. In v4.0.0 the US Core 6.1.0 profiles are on by default, and each encounter gets a clinical note. The Synthea docs say the same seed and the same version should produce the same population. All four time-related flags matter: in Synthea's source, the seed, the clinician seed, the reference date and the end date all default to the current time, so leaving any of them out changes the output. The end date is where the simulation stops; without it a rerun next week adds a week of history. (The first test run caught this: with only `-r` pinned, records ran up to the day of the run.) Committing the data keeps the gold labels, which point at resource IDs, versioned together with the data they describe.
- **Alternatives.** MIMIC-IV demo on FHIR (real de-identified ICU data, ruled out by the synthetic-only rule). Public FHIR test servers (unlabeled, inconsistent, change without notice). Regenerating the cohort in CI (adds a Java step and relies on identical output across machines, which Synthea doesn't promise).
- **Revisit if.** The committed cohort grows past about 25 MB. Then use fewer patients or move the data to a release asset.

### D2. Our own typed views of FHIR, not a full FHIR model library

- **Decision.** Write small Pydantic models ("views") for the indexed resource types, covering only the fields we use (around 30) and ignoring the rest. Handle FHIR choice types (`effective[x]`, `value[x]`, `onset[x]`, `occurrence[x]`) explicitly.
- **Why.** The service reads a narrow slice of each resource: Reference, Coding and CodeableConcept (system, code, display), Quantity, Period, status fields and choice types, as US Core profiles constrain them. There is also a version-fit reason: `fhir.resources` 7 and later ship R5 and R4B models but no R4 (4.0.1) package, and Synthea writes R4. R4B is close to R4 for these resources, but strict validation against the wrong version can reject valid data or accept invalid data.
- **Alternatives.** `fhir.resources` 8.x with R4B models (full validation, heavier, the version mismatch above). Plain dicts (no type checking, so errors surface late).
- **Revisit if.** The project starts writing FHIR back to a server or needs full profile validation. Then use a tool built for that, such as the HL7 FHIR validator.

### D3. Index an allowlist of clinical resource types

- **Decision.** Index Patient, Condition, Observation, MedicationRequest, AllergyIntolerance, Immunization, Procedure, Encounter, DiagnosticReport (lab panels), DocumentReference (clinical notes) and CarePlan. Skip billing resources (Claim, ExplanationOfBenefit), Provenance, and directory resources (Organization, Practitioner, Location), which are only used to resolve display names. The list was set from measured counts ([data.md](data.md)).
- **Why.** Billing resources take up a large part of each bundle and don't answer clinical questions; indexing them would crowd the top results with noise. Synthea also writes each clinical note twice, once as `DiagnosticReport.presentedForm` and once as a `DocumentReference` attachment, so notes are indexed once, from DocumentReference, to avoid duplicate hits.
- **Alternatives.** Index everything and let ranking sort it out (likely noisier). Drop billing at generation time with Synthea's `exporter.fhir.excluded_resources` setting.
- **Revisit if.** Questions about coverage or costs come into scope. Synthea's Claim and ExplanationOfBenefit resources could support a payer-side question category (what was billed, what insurance paid).

### D4. One card per resource

- **Decision.** Render each resource as a short text card: type, date, display names with codes, values with units, status. For example:
  `Observation | 2026-03-04 | Hemoglobin A1c/Hemoglobin.total in Blood (LOINC 4548-4) = 6.8 % | final`
  Clinical notes are split into sections, with refs like `DocumentReference/<id>#2`.
- **Why.** A citation has to point at something a clinician can open, and resource boundaries are natural chunk boundaries. Cards also drop JSON noise (profile URLs, meta, identifiers) that hurts both BM25 and embeddings. The card text is what gets searched, embedded, and shown to the model.
- **Alternatives.** Fixed-size token windows over raw JSON (breaks the link between a chunk and its resource, and embeds JSON syntax). One summary document per patient (loses granularity). Grouping repeated Observations of the same code into one "series" card; series expansion at query time does that job instead (change 3 below).
- **Revisit if.** The per-category eval shows trend or "latest value" questions failing because the right card isn't in the context.

### D5. Retrieval is filtered to one patient before ranking

- **Decision.** The `/ask` endpoint takes a patient ID, and retrieval filters to that patient's cards before any scoring.
- **Why.** Correctness: the question is about this patient. Safety: another patient's data can't reach the prompt, and that is enforced in code rather than by asking the model. It also keeps the search space to a few thousand cards, which is what makes D8 possible. This mirrors how an app launched from an EHR gets its patient from the launch context, not from the question text.
- **Eval check.** Every question asserts that zero retrieved resources belong to another patient. Any leak fails CI.

### D6. Hybrid retrieval: BM25 and dense, fused with RRF

- **Decision.** BM25 as the baseline, then dense retrieval, then the two rankings combined with Reciprocal Rank Fusion: each card scores the sum of 1 / (60 + rank) across the two lists. The eval, read by category, picked hybrid retrieval with series expansion and the pinned summary (the README's retrieval table).
- **Why.** Clinical questions mix exact terms, where lexical matching wins (drug names, lab names, codes), and lay or paraphrased terms, where embeddings win ("blood sugar" for glucose, "heart attack" for myocardial infarction). RRF combines ranks, so BM25 scores and cosine similarities never have to be put on the same scale. The constant 60 keeps a single top-ranked hit from dominating; it is the usual default and can be tuned.
- **Implementation.** BM25 is written out in `retrieval/bm25.py` with numpy (change 4 below).
- **Alternatives.** Dense only. Weighted score blending (needs score normalization). A cross-encoder reranker over the fused top 50. LLM query rewriting (adds a model call to every question).

### D7. Local embeddings: bge-small-en-v1.5 through fastembed

- **Decision.** Embed cards and questions with `BAAI/bge-small-en-v1.5` (384 dimensions), run through `fastembed` on ONNX Runtime.
- **Why.** Free. Runs on a laptop CPU and in CI with no GPU and no PyTorch. The model files are pinned and their hash goes into every report, so vectors don't change underneath the eval. No record text leaves the machine to be embedded.
- **Alternatives.** Hosted embedding APIs (cost money, need a secret in CI, and the provider can update the model). Larger general models such as bge-base. Biomedical encoders such as MedCPT.
- **Revisit if.** The eval shows dense retrieval missing paraphrased clinical terms that a domain model would likely catch.

### D8. SQLite and numpy, no vector database

- **Decision.** Store resources, cards and embeddings in one SQLite file. Load vectors into memory at startup and compute cosine similarity for a patient with one matrix-vector product.
- **Why.** Retrieval always covers a single patient, so search runs over a few thousand vectors. Exact brute-force search at that size is fast, loses no recall to approximate search, and adds no service to run. SQLite ships with Python, and the file can be rebuilt from the cohort at any time.
- **Alternatives.** Postgres with pgvector. Chroma, Qdrant, FAISS.
- **Revisit if.** Questions span patients, or the corpus reaches hundreds of thousands of vectors. Then Postgres with pgvector and an HNSW index, keeping the same schema.

### D9. Claude through the Anthropic SDK, behind a small adapter

- **Decision.** Call Claude with the official `anthropic` Python SDK through a small `LLMClient` interface. Model ID, effort level and timeouts come from config. Generator `claude-opus-5-5`, judge `claude-sonnet-5-5` (D14). A second client makes the same calls through the Claude Code CLI on a Claude subscription (change 10 below).
- **Why.** The SDK's `messages.parse()` validates each response against a Pydantic schema (structured outputs), which D10 depends on. The same models and structured outputs are available on Amazon Bedrock through the SDK's `AnthropicBedrockMantle` client, with only the client class and model ID changing. Bedrock is on AWS's HIPAA Eligible Services list, so a real deployment could send PHI there under an AWS BAA. Eligibility is not compliance; the rest of the system would need the same care.
- **Note.** On Opus 5.5, thinking can't be turned off. Depth is set with `effort`, which defaults to `medium`. Config sets it explicitly.
- **Alternatives.** A local model through Ollama (free and private; whether a small local model follows the citation schema reliably is an open question). Other hosted providers.

### D10. Structured output with per-sentence citations

- **Decision.** The model returns JSON that matches a schema:

  ```json
  {
    "status": "answered",
    "sentences": [
      {"text": "The most recent HbA1c was 6.8% on 2026-03-04.",
       "citations": ["Observation/3f2c..."]}
    ]
  }
  ```

  `status` is `answered` or `not_in_record`. After the call, code checks every citation against the cards the model was shown; invalid ones are removed from the response and counted.
- **Why.** Per-sentence references make citation accuracy measurable without parsing free text, and the explicit status gives the model an allowed way to say the record doesn't contain the answer.
- **Alternatives.** Anthropic's Citations feature, which returns quoted spans tied to the documents passed in. It can't be combined with structured outputs (`output_config.format`) in one request, so "not in record" would need another mechanism. Free text with inline `[Observation/123]` markers parsed by regex (brittle).

### D11. "Not in record" is a feature

- **Decision.** When the retrieved context doesn't contain the answer, the service says so instead of answering. The question set includes questions the record can't answer.
- **Why.** In a clinical tool, a confident wrong answer is worse than "this isn't in the record". It has to be measured in both directions: a system that always abstains would score perfectly on unanswerable questions, so false abstentions on answerable questions are counted too.
- **Metrics.** A confusion matrix: correct answers, correct abstentions, false abstentions, and answers given to unanswerable questions (the worst cell).

### D12. Question set: gold labels computed from the record

- **Decision.** 275 questions over the cohort, in five categories, stored as JSONL. Each item has the patient ID, question, category, gold evidence, expected key facts, a source and a split.

  | Category | Example |
  |---|---|
  | Fact lookup | What allergies are documented for this patient? |
  | Values and dates | What was the patient's most recent hemoglobin A1c result, and when was it measured? |
  | Lay terms | Has the patient ever been diagnosed with high blood pressure? If so, when? |
  | Multi-step | Why was the patient last seen in the emergency department, and when? |
  | Not in record | What is the patient's blood type? |

- **How gold labels are made.** A script reads the raw bundles and computes the answer directly, for example: Observations with LOINC 4548-4, sorted by date, newest first. That script shares no code with the service except the bundle loader, so a parsing bug in the service can't also hide in the labels. `build_questions` checks that every gold ref exists in the patient's record and that "not in record" questions have no gold. Misses in the answer evals are read against the raw bundles; that is how four wrong labels were found on the test split (change 11 below).
- **Split.** About 60% dev and 40% held-out test, fixed before any tuning. A question keeps its split once assigned, and a new question's split depends only on a hash of its id. Design decisions were made on dev; test was scored after.
- **Why.** Code-derived labels are exact and cheap, which lets the set grow large enough to mean something. Reporting by category keeps easy questions from inflating the headline number. Hand-written questions would cover what templates can't, such as the words clinicians use; the builder merges them from `evals/questions/drafted.jsonl`, and none are in the set yet.
- **Alternatives.** Having an LLM write questions and answers (fast, but then the eval partly measures agreement with that model). All hand-written (too slow to reach a useful size).

### D13. Metrics, defined exactly

Retrieval, over answerable questions, at k = 5, 10 and 20:

- **Hit@k**: share of questions with at least one gold group in the context.
- **Recall@k**: share of gold groups with a member in the context, averaged over questions. This one matters for list questions, where Hit@k can look fine while most of the list is missing.
- **MRR@k**: average of 1 / (rank of the first gold card among the ranked cards), counting 0 when none is in the top k.
- **Leakage**: retrieved resources that belong to another patient. Must be 0.

Answers:

- **Citation validity**: share of cited refs that were actually in the context, measured before the validator removes bad ones. Shows how often the model invents or mangles references.
- **Citation precision and recall**: overlap between cited refs and gold groups. Precision undercounts when the model cites a relevant resource that isn't in the gold set (an older HbA1c in a trend answer, say); the judge's verdict covers that case.
- **Faithfulness**: share of answer sentences the LLM judge marks as fully supported. Facts about specific entries must be in the cards that sentence cites; claims about the record as a whole ("most recent", "only", counts, "no record of") are checked against the whole context the model saw (change 9 below).
- **Number and date check**: every number and date in the answer appears, after normalization, in a card that its sentence cites. Deterministic, free, and aimed at the most harmful kind of error: a wrong lab value or a wrong date.
- **Key-fact correctness**: the expected value, unit, date and name appear in the answer, after normalization.
- **Abstention**: the confusion matrix from D11, with precision and recall for `not_in_record`.

Operations: p50 and p95 latency for retrieval, the model call and the whole request; input and output tokens; cost per question from recorded usage and list prices.

Every metric is reported overall and by category with a 95% bootstrap confidence interval. The bootstrap resamples patients rather than single questions, because questions about the same patient are correlated.

### D14. The judge is checked before its numbers count

- **Decision.** The judge is a separate Claude call with a concrete rubric and structured output: for each sentence, `supported`, `partially_supported` or `not_supported`, with a one-line reason. One call per answer. The judge model differs from the generator, because a model tends to rate output that resembles its own more favorably.
- **Calibration.** Sentences from a real run are labeled blind, without the judge's verdicts, and the report gives agreement and Cohen's kappa. The judge flags few sentences, so samples are stratified and weighted back to the run. The target is at least 90% agreement on clear cases. The reference labels come from Claude Opus 5.5, a stronger model than the judge, labeling in small batches that see only the rubric and their items; every reason that decided a disagreement was checked against the cards. A second set drawn after a judge revision serves as the held-out check ([evals.md](evals.md#checking-the-judge-against-blind-reference-labels)).
- **Why.** An unchecked judge gives an opinion, not a measurement. The agreement number is what makes the faithfulness score defensible.
- **Alternatives.** RAGAS or DeepEval faithfulness metrics (the same claim-checking idea, with less control over the prompt and harder to explain line by line). NLI models (local and free, but untested on card-style text).

### D15. Harness hygiene

- Each question's full trace is saved: question, retrieved refs and scores, prompt version, raw model output, judge output, usage, latency, and the model that served the request.
- Infrastructure failures (timeouts, API errors after retries, unparseable output) go to `errors.jsonl` and are never scored as wrong answers. Responses cut off at `max_tokens` are flagged. Refusals are recorded as their own outcome.
- The served model is checked against the requested model on every call.
- Each result is written as soon as it finishes, and runs resume where they stopped, keyed by question and repetition.
- The harness itself is tested with an oracle run (gold answers formatted as model output, which should score near 100%) and a null run (empty answers, which should score near 0%).
- Each report records the commit, cohort hash, card version, models, effort, judge prompt version and retrieval settings, so any two reports can be compared.

### D16. Two CI workflows

- **`ci.yml`, on every push and pull request.** `uv sync --locked`, ruff, mypy, pytest (unit tests use a fake LLM client and never call a model), build the index (embeddings cached between runs), run the retrieval eval on the dev split, and compare with `evals/baselines/retrieval-dev.json`. Retrieval is deterministic apart from floating-point noise across machines, so the gate allows a drop of at most one question per metric and fails on anything larger, or on any leakage. A pull request that changes retrieval on purpose updates the baseline file in the same diff, where a reviewer can see the change.
- **`llm-eval.yml`, on demand and on pull requests labeled `llm-eval`.** Uses the `ANTHROPIC_API_KEY` repository secret, runs the answer eval, uploads the report as an artifact, writes a summary to the job page, and stops at a spend cap. It reports numbers without failing: a threshold has to sit above the run-to-run spread, which hasn't been measured yet.
- **Why two.** Free, deterministic checks can gate every change. Paid, noisy checks need to run less often, with thresholds that account for noise. With about 160 dev questions, a single run's pass rate carries several points of sampling noise either way, so a small change from one run means little on its own.

### D17. Service engineering

- Async endpoints, because the model call is network-bound and takes seconds; `AsyncAnthropic` lets one worker serve other requests while it waits.
- FastAPI dependency injection for settings, store, retriever and LLM client, so tests can swap in a fake client.
- Config through `pydantic-settings` and environment variables. `.env` is gitignored; `.env.example` documents every setting.
- Timeouts and bounded retries on the model call. Clear error responses: 404 for an unknown patient, 422 for invalid input, 503 or 504 when the model call fails or times out.
- A request ID on every request and response. JSON logs carry resource refs, timings and token counts, never question text or record text. With real PHI, an access audit log (who asked about which patient, and when) would go to a separate, access-controlled store.
- Retrieved record text is treated as data, not instructions. Real notes can contain patient-entered text, so the prompt marks the record as untrusted content, and structured output plus citation checks limit what a hostile note could do.
- A Docker image built with uv, running as a non-root user, with a health check, and `compose.yaml` for one-command startup.

### D18. Tooling

- **Python 3.13**, installed and managed by uv. The native dependencies here (numpy, onnxruntime) have shipped 3.13 wheels for longer than 3.14 ones.
- **uv** for dependencies and the lockfile (fast, reproducible installs in CI), **ruff** for lint and formatting, **mypy** in strict mode on `src/`, **pytest** for tests. Versions are pinned in `uv.lock`.

## Changes during the build

1. **Gold evidence is a list of groups** (D12, D13). Several questions have interchangeable evidence: any prescription of the right drug answers "what was prescribed for X?". Each group holds interchangeable refs, and recall and citation recall count groups.
2. **Pinned patient summary** (D6). The first retrieval run showed "current" lists and recency questions failing, because similarity can't see status or dates. Active problems, active medications, allergies, the last three visits and the past year's immunizations now go in front of every context (`retrieval/summary.py`). On dev, recall@10 is 0.735 without it, 0.844 with the same card budget but no summary, and 0.951 with it. On test: 0.708, 0.838, 0.915.
3. **Series expansion at query time** instead of series cards (D4). When a ranked card belongs to a series (every HbA1c result), its newest three members join the context and the series' other members are skipped. This lifts recall@10 from 0.616 to 0.735 on dev.
4. **BM25 written out in `retrieval/bm25.py`** instead of the `bm25s` library (D6). Per-patient corpora are at most ~14k cards, so plain numpy postings are fast enough, and every term of the formula is visible.
5. **Harder templates** were added after the summary saturated the first set: smoking status, latest lipid panel, HbA1c trend, last ER visit reason, last colonoscopy, and tests Synthea never generates.
6. **anthropic SDK 2.x** was current at install. Calls use `beta.messages.parse` with structured output and the server-side refusal fallback (`fallbacks="default"`); sampling parameters such as temperature no longer exist on these models.
7. **Embedding model files**: fastembed serves Qdrant's quantized ONNX export of bge-small-en-v1.5 (`Qdrant/bge-small-en-v1.5-onnx-Q`, revision `aa8f8b06`).
8. **Line length 100** instead of ruff's default 88: prompts, FHIR paths and SQL ran long.
9. **Judges v2 and v3** (D13, D14), 2026-10-30, after the first full dev run. Judge v1 saw only the cards each sentence cited, so it couldn't check "most recent", "only" or "no record of", and it scored faithfulness 0.635 on answers whose key facts were all correct. v2 checks claims about the whole record against the whole context and facts about entries against the cited cards; on the same answers it scores 0.976. `evals/rejudge.py` re-grades stored answers without calling the generator. v3 followed the same day, after blind reference labels showed most of v2's flags were wrong: it reads each sentence within its answer, counts only the excerpts shown, and writes its reason before its verdict. On a held-out label set it matches v2, and both miss answers that leave out entries found only in clinical notes. [evals.md](evals.md) has both comparisons.
10. **Claude Code CLI backend** (D9), 2026-10-31. `ClaudeCodeLLM` runs the same calls through `claude -p` on a Claude subscription, picked with `FHIR_RAG_LLM_BACKEND=cli`, so answer evals can run without API credits. The API client stays the default. On two dev questions the CLI gave the same answers and verdicts, with about 1,000 more input tokens per call and model calls two to four times slower. Reports say when a run used it, because its cost is list price rather than billed and its latency is the CLI's. [evals.md](evals.md#running-on-a-claude-subscription) has the details.
11. **Label fixes and sticky splits** (D12), 2026-10-31. The first test answer run found four wrong labels from two template rules: the last ER visit was taken from visits with a recorded reason, and labs were looked up under one LOINC code although Synthea uses a whole-blood and a serum-or-plasma code for four of them. Both rules are fixed for every patient. Rebuilding the set then showed that splits were assigned by rank within each category, so the two added questions would have moved a dev question to test. Splits are now read from the existing file, and a new question's split depends only on its id's hash. The set is 275 questions (166 dev, 109 test).

## Where to start reading

Smallest and most central first: `fhir/views.py`, `fhir/cards.py`, `retrieval/bm25.py`, `retrieval/fusion.py`, `retrieval/retriever.py`, `retrieval/summary.py`, `evals/metrics.py`, `evals/templates.py`, `llm/answer.py`, then the rest.

## Future work

- Hand-written questions in `evals/questions/drafted.jsonl`, especially paraphrases and multi-step questions.
- Run-to-run noise: three repetitions of the dev answer eval (`--reps 3`), then an llm-eval threshold above that spread.
- A clinician-labeled calibration set for the judge.
- Experiments: Opus 5.5, Sonnet 5.5 and Haiku 5.5 as the generator on quality, cost and latency; k = 5, 10 and 20; a larger or biomedical embedding model; structured output against the Citations feature; BM25 with stemming, for the smoking-status misses.
- Ingest from a FHIR server: load the bundles into HAPI FHIR running in Docker, then read each patient back with `Patient/$everything`.
- HL7 v2: convert one ORU^R01 lab message into FHIR Observations.
- A payer-side question category over Claim and ExplanationOfBenefit.
- A prompt-injection test: a synthetic note that contains instructions, checking that answers ignore them.

## References

- Synthea, Basic Setup and Running: https://github.com/synthetichealth/synthea/wiki/Basic-Setup-and-Running
- Synthea v4.0.0 release: https://github.com/synthetichealth/synthea/releases/tag/v4.0.0
- FHIR R4 specification: https://hl7.org/fhir/R4/
- US Core Implementation Guide: https://hl7.org/fhir/us/core/
- SMART App Launch, scopes and launch context: https://hl7.org/fhir/smart-app-launch/scopes-and-launch-context.html
- AWS HIPAA Eligible Services Reference: https://aws.amazon.com/compliance/hipaa-eligible-services-reference/
- Claude structured outputs: https://platform.claude.com/docs/en/build-with-claude/structured-outputs
- Claude citations: https://platform.claude.com/docs/en/build-with-claude/citations
- Claude pricing: https://platform.claude.com/docs/en/about-claude/pricing
- bm25s: https://github.com/xhluca/bm25s
- fastembed: https://github.com/qdrant/fastembed
