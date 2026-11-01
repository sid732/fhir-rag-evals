# Answer eval: dev-1-judge2

commit: `248b54a+dirty`, cohort: `57e36fe7e8f2`, mode: `real`, generator: `claude-opus-5-5`, effort: `medium`, judge: `claude-sonnet-5-5`, retrieval: `hybrid, k=10, series=3, summary=True`, split: `dev`, answers_from: `dev-1`, judge_prompt: `judge_v2-9a419bb8`

Commit `248b54a` became `5a379c9` when this repo's history was rewritten on 2026-11-01. `+dirty` means the run included changes that weren't committed yet.

164 graded cases, 0 failed attempts (not scored).
Answers reused from run dev-1 and judged again; the generator cost below was spent there.

## Abstention

|  | Answered | Said not in record |
|---|---|---|
| Answerable | 140 | 1 |
| Not in record | 0 | 23 |

'Not in record' precision 0.958, recall 1.000.

## Answered, answerable cases (140)

| Metric | n | Mean [95% CI] |
|---|---|---|
| Citation validity | 140 | 1.000 [1.000, 1.000] |
| Citation precision | 140 | 0.568 [0.531, 0.600] |
| Citation recall | 140 | 0.957 [0.931, 0.981] |
| Numbers and dates in cited cards | 140 | 0.979 [0.956, 0.996] |
| Key facts present | 87 | 1.000 [1.000, 1.000] |
| Faithfulness (judge: supported) | 140 | 0.976 [0.960, 0.991] |
| Judge: partially supported | 140 | 0.024 [0.009, 0.040] |
| Gold evidence in context | 140 | 0.957 [0.931, 0.981] |

## By category

| Category | n | Citation recall | Key facts | Faithfulness |
|---|---|---|---|---|
| fact_lookup | 34 | 0.824 | - | 0.966 |
| values_dates | 59 | 1.000 | 1.000 | 0.983 |
| lay_terms | 18 | 1.000 | 1.000 | 1.000 |
| multi_step | 29 | 1.000 | 1.000 | 0.960 |

## Cost and latency

|  | Value |
|---|---|
| Total cost (generator + judge) | $6.49 |
| Generator cost per case | $0.0275 |
| Judge cost per case | $0.0120 |
| Input tokens per case (mean) | 5353 |
| Output tokens per case (mean) | 307 |
| Latency p50 / p95, whole request | 3.78 s / 8.37 s |
| Latency p50 / p95, model call | 3.71 s / 8.35 s |

## Lowest-scoring answers

| Question | Faithfulness | Citation recall | Answer |
|---|---|---|---|
| current-meds:8ff46e01 | 0.5 | 1.00 | The patient's active prescriptions are aspirin 81 MG Oral Tablet, rosuvastatin calcium 10 MG Oral Tablet, atenolol 50 MG Oral Tablet, prasugrel 10 MG Oral Table |
| last-visit:9292c3d5 | 0.5 | 1.00 | The patient's most recent visit was on 2026-04-26, an ambulatory (class AMB) encounter for General examination of patient (procedure) at COMMUNITY HEALTH PROGRA |
| latest-lipid-panel:d4f2a6f8 | 0.5 | 1.00 | The most recent lipid panel with direct LDL, dated 2026-04-02, showed total cholesterol 166.31 mg/dL, triglycerides 117.76 mg/dL, LDL cholesterol (direct assay) |
| prescribed-for-diabetes-mellitus-type-2:ef5e136c | 0.5 | 1.00 | The only medication with diabetes mellitus type 2 listed as its reason is insulin isophane, human 70 UNT/ML / insulin, regular, human 30 UNT/ML Injectable Suspe |
| current-meds:0e6e0d73 | 0.6666666666666666 | 1.00 | The only medication with an active status is Levora 0.15/30 28 Day (21 ethinyl estradiol 0.03 MG / levonorgestrel 0.15 MG Oral Tablet / 7 inert ingredients 1 MG |
| current-meds:d4f2a6f8 | 0.6666666666666666 | 1.00 | The patient's active prescriptions for essential hypertension are hydrochlorothiazide 25 MG oral tablet, lisinopril 10 MG oral tablet, and amLODIPine 2.5 MG ora |
| prescribed-for-essential-hypertension:8446fe54 | 0.6666666666666666 | 1.00 | Lisinopril 10 MG Oral Tablet is the medication prescribed with essential hypertension as the reason, with a currently active prescription dated 2025-10-03. Earl |
| prescribed-for-hyperlipidemia:8446fe54 | 0.6666666666666666 | 1.00 | Simvastatin 10 MG Oral Tablet is the medication prescribed with hyperlipidemia as the stated reason, first noted in a 2002-06-14 clinical note alongside a hyper |
| smoking-status:760e0542 | 1.0 | 0.00 | No, the patient's clinical notes state that the patient has never smoked, most recently in the note dated 2024-08-14. |
| smoking-status:9292c3d5 | 1.0 | 0.00 | No; the clinical notes consistently state that the patient quit smoking at age 17, including the most recent note dated 2021-04-04. |
| smoking-status:8446fe54 | 1.0 | 0.00 | No, the patient does not smoke; the most recent clinical note dated 2026-04-10 states "Patient has never smoked." This never-smoker status is documented consist |
| smoking-status:772fc930 | 1.0 | 0.00 | No; the clinical notes consistently state that the patient has never smoked, most recently in the note dated 2019-01-10. |
| smoking-status:ef5e136c | 1.0 | 0.00 | No, the clinical notes state that the patient has never smoked, most recently in the note dated 2026-05-27. |
| smoking-status:d14e9292 | 1.0 | 0.00 | No, the patient does not smoke; her clinical notes consistently state that she has never smoked, including the most recent note on 2026-07-15. |
| a1c-trend:8ff46e01 | 1.0 | 1.00 | The patient's last three hemoglobin A1c results were 6.27 % on 2023-12-27, 5.84 % on 2025-11-10, and 6.11 % on 2025-12-31. The A1c fell from 6.27 % to 5.84 %, t |
