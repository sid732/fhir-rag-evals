# Answer eval: pilot

commit: `c782cd8`, cohort: `57e36fe7e8f2`, mode: `real`, generator: `claude-opus-5-5`, effort: `medium`, judge: `claude-sonnet-5-5`, retrieval: `hybrid, k=10, series=3, summary=True`, split: `dev`

Commit `c782cd8` became `72068d7` when this repo's history was rewritten on 2026-11-01.

10 graded cases, 0 failed attempts (not scored).

## Abstention

|  | Answered | Said not in record |
|---|---|---|
| Answerable | 10 | 0 |
| Not in record | 0 | 0 |

'Not in record' precision 0.000, recall 0.000.

## Answered, answerable cases (10)

| Metric | n | Mean [95% CI] |
|---|---|---|
| Citation validity | 10 | 0.988 [0.966, 1.000] |
| Citation precision | 10 | 0.508 [0.351, 0.653] |
| Citation recall | 10 | 1.000 [1.000, 1.000] |
| Numbers and dates in cited cards | 10 | 0.967 [0.909, 1.000] |
| Key facts present | 3 | 1.000 [1.000, 1.000] |
| Faithfulness (judge: supported) | 10 | 0.967 [0.909, 1.000] |
| Judge: partially supported | 10 | 0.033 [0.000, 0.091] |
| Gold evidence in context | 10 | 1.000 [1.000, 1.000] |

## By category

| Category | n | Citation recall | Key facts | Faithfulness |
|---|---|---|---|---|
| fact_lookup | 7 | 1.000 | - | 0.952 |
| multi_step | 3 | 1.000 | 1.000 | 1.000 |

## Cost and latency

|  | Value |
|---|---|
| Total cost (generator + judge) | $0.36 |
| Generator cost per case | $0.0311 |
| Judge cost per case | $0.0051 |
| Input tokens per case (mean) | 4469 |
| Output tokens per case (mean) | 660 |
| Latency p50 / p95, whole request | 5.86 s / 12.12 s |
| Latency p50 / p95, model call | 5.44 s / 11.95 s |

## Lowest-scoring answers

| Question | Faithfulness | Citation recall | Answer |
|---|---|---|---|
| active-problems:530b9289 | 0.6666666666666666 | 1.00 | The patient's active diagnoses are prediabetes (onset 2005-04-20), body mass index 30+ - obesity (onset 2017-05-03), and chronic sinusitis (onset 1996-04-03). O |
| a1c-trend:8ff46e01 | 1.0 | 1.00 | The patient's hemoglobin A1c was 6.27 % on 2023-12-27, decreased to 5.84 % on 2025-11-10, and then rose to 6.11 % on 2025-12-31. The patient has an active predi |
| active-problems:0e6e0d73 | 1.0 | 1.00 | The patient's active conditions are full-time employment (onset 2026-05-25), unhealthy alcohol drinking behavior (onset 2021-08-16), medication review due (onse |
| a1c-trend:8d945e28 | 1.0 | 1.00 | The patient's last three hemoglobin A1c results were 3.14 % on 2026-06-22, 3.37 % on 2026-07-13, and 3.14 % on 2026-09-07. The value rose from 3.14 % to 3.37 %, |
| a1c-trend:530b9289 | 1.0 | 1.00 | The patient's last three hemoglobin A1c results were 5.92 % on 2021-06-30, 5.9 % on 2023-02-22, and 6.07 % on 2025-02-26. The value was essentially stable betwe |
| active-problems:0eeb6aa3 | 1.0 | 1.00 | Active diagnoses include primary fibromyalgia syndrome (onset 2026-07-29), metabolic syndrome X, hypertriglyceridemia, and hyperglycemia (each onset 2022-11-27) |
| active-problems:8d945e28 | 1.0 | 1.00 | Active kidney-related diagnoses include chronic kidney disease stages 1, 2, 3 and 4, disorder of kidney due to diabetes mellitus, microalbuminuria due to type 2 |
| active-problems:8446fe54 | 1.0 | 1.00 | Active cardiometabolic diagnoses include diabetes mellitus type 2 with neuropathy and nonproliferative diabetic retinopathy, prediabetes, metabolic syndrome X,  |
| active-problems:9292c3d5 | 1.0 | 1.00 | The patient's active clinical diagnoses are opioid abuse (onset 2020-03-22), history of myocardial infarction and acute ST segment elevation myocardial infarcti |
| active-problems:d4f2a6f8 | 1.0 | 1.00 | Active kidney and diabetes-related diagnoses are chronic kidney disease stage 4 (onset 2025-03-20), stage 3 (onset 2022-10-20), and stage 1 (onset 2020-03-05),  |
