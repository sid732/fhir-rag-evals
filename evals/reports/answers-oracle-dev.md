# Answer eval: oracle-dev

commit: `e529634`, cohort: `57e36fe7e8f2`, card_version: `1`, mode: `oracle`, backend: `None`, generator: `oracle`, effort: `medium`, judge: `None`, judge_prompt: `None`, retrieval: `hybrid, k=10, series=3, summary=True`, split: `dev`

166 graded cases, 0 failed attempts (not scored).

## Abstention

|  | Answered | Said not in record |
|---|---|---|
| Answerable | 143 | 0 |
| Not in record | 0 | 23 |

'Not in record' precision 1.000, recall 1.000.

## Answered, answerable cases (143)

| Metric | n | Mean [95% CI] |
|---|---|---|
| Citation validity | 143 | 0.822 [0.766, 0.880] |
| Citation precision | 143 | 0.951 [0.926, 0.976] |
| Citation recall | 143 | 0.951 [0.926, 0.976] |
| Numbers and dates in cited cards | 90 | 0.989 [0.966, 1.000] |
| Key facts present | 90 | 1.000 [1.000, 1.000] |
| Gold evidence in context | 143 | 0.951 [0.926, 0.976] |

## By category

| Category | n | Citation recall | Key facts | Faithfulness |
|---|---|---|---|---|
| fact_lookup | 34 | 0.824 | - | - |
| values_dates | 60 | 0.983 | 1.000 | - |
| lay_terms | 18 | 1.000 | 1.000 | - |
| multi_step | 31 | 1.000 | 1.000 | - |

## Cost and latency

|  | Value |
|---|---|
| Total cost (generator + judge) | $0.00 |
| Generator cost per case | $0.0000 |
| Judge cost per case | $0.0000 |
| Input tokens per case (mean) | 2390 |
| Output tokens per case (mean) | 50 |
| Latency p50 / p95, whole request | 0.01 s / 0.19 s |
| Latency p50 / p95, model call | 0.00 s / 0.00 s |

## Lowest-scoring answers

| Question | Faithfulness | Citation recall | Answer |
|---|---|---|---|
| latest-lipid-panel:8d945e28 | - | 0.00 | Recorded: 201.61, 2025-10-20. |
| smoking-status:772fc930 | - | 0.00 | Recorded: see cited records. |
| smoking-status:760e0542 | - | 0.00 | Recorded: see cited records. |
| smoking-status:9292c3d5 | - | 0.00 | Recorded: see cited records. |
| smoking-status:8446fe54 | - | 0.00 | Recorded: see cited records. |
| smoking-status:d14e9292 | - | 0.00 | Recorded: see cited records. |
| smoking-status:ef5e136c | - | 0.00 | Recorded: see cited records. |
| a1c-trend:530b9289 | - | 1.00 | Recorded: 5.92, 5.9, 6.07. |
| a1c-trend:8d945e28 | - | 1.00 | Recorded: 3.14, 3.37, 3.14. |
| a1c-trend:8ff46e01 | - | 1.00 | Recorded: 6.27, 5.84, 6.11. |
| active-problems:0e6e0d73 | - | 1.00 | Recorded: see cited records. |
| active-problems:0eeb6aa3 | - | 1.00 | Recorded: see cited records. |
| active-problems:530b9289 | - | 1.00 | Recorded: see cited records. |
| active-problems:8446fe54 | - | 1.00 | Recorded: see cited records. |
| active-problems:8d945e28 | - | 1.00 | Recorded: see cited records. |
