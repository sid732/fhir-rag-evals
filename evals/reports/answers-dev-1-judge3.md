# Answer eval: dev-1-judge3

commit: `daac303+dirty`, cohort: `57e36fe7e8f2`, mode: `real`, generator: `claude-opus-5-5`, effort: `medium`, judge: `claude-sonnet-5-5`, retrieval: `hybrid, k=10, series=3, summary=True`, split: `dev`, answers_from: `dev-1`, judge_prompt: `judge_v3-d86cce01`

Commit `daac303` became `3cac2c7` when this repo's history was rewritten on 2026-11-01. `+dirty` means the run included changes that weren't committed yet.

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
| Citation precision | 140 | 0.568 [0.532, 0.603] |
| Citation recall | 140 | 0.957 [0.930, 0.984] |
| Numbers and dates in cited cards | 140 | 0.979 [0.957, 0.996] |
| Key facts present | 87 | 1.000 [1.000, 1.000] |
| Faithfulness (judge: supported) | 140 | 0.993 [0.985, 1.000] |
| Judge: partially supported | 140 | 0.007 [0.000, 0.015] |
| Gold evidence in context | 140 | 0.957 [0.930, 0.984] |

## By category

| Category | n | Citation recall | Key facts | Faithfulness |
|---|---|---|---|---|
| fact_lookup | 34 | 0.824 | - | 0.990 |
| values_dates | 59 | 1.000 | 1.000 | 1.000 |
| lay_terms | 18 | 1.000 | 1.000 | 1.000 |
| multi_step | 29 | 1.000 | 1.000 | 0.977 |

## Cost and latency

|  | Value |
|---|---|
| Total cost (generator + judge) | $6.59 |
| Generator cost per case | $0.0275 |
| Judge cost per case | $0.0126 |
| Input tokens per case (mean) | 5353 |
| Output tokens per case (mean) | 307 |
| Latency p50 / p95, whole request | 3.78 s / 8.37 s |
| Latency p50 / p95, model call | 3.71 s / 8.35 s |

## Lowest-scoring answers

| Question | Faithfulness | Citation recall | Answer |
|---|---|---|---|
| current-meds:0e6e0d73 | 0.6666666666666666 | 1.00 | The only medication with an active status is Levora 0.15/30 28 Day (21 ethinyl estradiol 0.03 MG / levonorgestrel 0.15 MG Oral Tablet / 7 inert ingredients 1 MG |
| prescribed-for-diabetes-mellitus-type-2:0eeb6aa3 | 0.6666666666666666 | 1.00 | The only medication prescribed for diabetes mellitus type 2 is 24 HR Metformin hydrochloride 500 MG Extended Release Oral Tablet, with an active prescription da |
| prescribed-for-hyperlipidemia:8446fe54 | 0.6666666666666666 | 1.00 | Simvastatin 10 MG Oral Tablet is the medication prescribed with hyperlipidemia as the stated reason, first noted in a 2002-06-14 clinical note alongside a hyper |
| smoking-status:760e0542 | 1.0 | 0.00 | No, the patient's clinical notes state that the patient has never smoked, most recently in the note dated 2024-08-14. |
| smoking-status:772fc930 | 1.0 | 0.00 | No; the clinical notes consistently state that the patient has never smoked, most recently in the note dated 2019-01-10. |
| smoking-status:8446fe54 | 1.0 | 0.00 | No, the patient does not smoke; the most recent clinical note dated 2026-04-10 states "Patient has never smoked." This never-smoker status is documented consist |
| smoking-status:9292c3d5 | 1.0 | 0.00 | No; the clinical notes consistently state that the patient quit smoking at age 17, including the most recent note dated 2021-04-04. |
| smoking-status:ef5e136c | 1.0 | 0.00 | No, the clinical notes state that the patient has never smoked, most recently in the note dated 2026-05-27. |
| smoking-status:d14e9292 | 1.0 | 0.00 | No, the patient does not smoke; her clinical notes consistently state that she has never smoked, including the most recent note on 2026-07-15. |
| active-problems:0e6e0d73 | 1.0 | 1.00 | The patient's active clinical diagnoses are sepsis and septic shock (both onset 2017-09-23), unhealthy alcohol drinking behavior (onset 2021-08-16), and past pr |
| a1c-trend:8d945e28 | 1.0 | 1.00 | The last three hemoglobin A1c results were 3.14 % on 2026-06-22, 3.37 % on 2026-07-13, and 3.14 % on 2026-09-07. The value rose briefly in July and then fell ba |
| a1c-trend:8ff46e01 | 1.0 | 1.00 | The patient's last three hemoglobin A1c results were 6.27 % on 2023-12-27, 5.84 % on 2025-11-10, and 6.11 % on 2025-12-31. The A1c fell from 6.27 % to 5.84 %, t |
| a1c-trend:530b9289 | 1.0 | 1.00 | The patient's hemoglobin A1c was 5.92 % on 2021-06-30, 5.9 % on 2023-02-22, and 6.07 % on 2025-02-26. The value was essentially stable between 2021 and 2023, th |
| active-problems:530b9289 | 1.0 | 1.00 | The patient's active diagnoses are prediabetes (onset 2005-04-20), body mass index 30+ - obesity (onset 2017-05-03), and chronic sinusitis (onset 1996-04-03). O |
| active-problems:8d945e28 | 1.0 | 1.00 | Active diagnoses include chronic kidney disease stage 4 (onset 2020-11-09) with awaiting kidney transplantation, as well as chronic kidney disease stages 1, 2 a |
