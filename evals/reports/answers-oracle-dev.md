# Answer eval: oracle-dev

commit: `dca8c0a`, cohort: `57e36fe7e8f2`, card_version: `1`, mode: `oracle`, backend: `None`, generator: `oracle`, effort: `medium`, judge: `None`, judge_prompt: `None`, retrieval: `hybrid, k=10, series=3, summary=True`, split: `dev`, category: `None`

181 graded cases, 0 failed attempts (not scored).

## Abstention

|  | Answered | Said not in record |
|---|---|---|
| Answerable | 158 | 0 |
| Not in record | 0 | 23 |

'Not in record' precision 1.000, recall 1.000.

## Answered, answerable cases (158)

| Metric | n | Mean [95% CI] |
|---|---|---|
| Citation validity | 158 | 0.832 [0.783, 0.883] |
| Citation precision | 158 | 0.956 [0.933, 0.979] |
| Citation recall | 158 | 0.956 [0.933, 0.979] |
| Numbers and dates in cited cards | 105 | 0.990 [0.970, 1.000] |
| Key facts present | 105 | 1.000 [1.000, 1.000] |
| Gold evidence in context | 158 | 0.956 [0.933, 0.979] |

## By category

| Category | n | Citation recall | Key facts | Faithfulness |
|---|---|---|---|---|
| fact_lookup | 34 | 0.824 | - | - |
| values_dates | 60 | 0.983 | 1.000 | - |
| lay_terms | 18 | 1.000 | 1.000 | - |
| multi_step | 31 | 1.000 | 1.000 | - |
| rare_history | 15 | 1.000 | 1.000 | - |

## Cost and latency

|  | Value |
|---|---|
| Total cost (generator + judge) | $0.00 |
| Generator cost per case | $0.0000 |
| Judge cost per case | $0.0000 |
| Input tokens per case (mean) | 2436 |
| Output tokens per case (mean) | 50 |
| Latency p50 / p95, whole request | 0.01 s / 0.15 s |
| Latency p50 / p95, model call | 0.00 s / 0.00 s |

## Lowest-scoring answers

| Question | Faithfulness | Citation recall | Answer |
|---|---|---|---|
| latest-lipid-panel:8d945e28 | - | 0.00 | Recorded: 201.61, 2025-10-20. |
| smoking-status:760e0542 | - | 0.00 | Recorded: see cited records. |
| smoking-status:772fc930 | - | 0.00 | Recorded: see cited records. |
| smoking-status:8446fe54 | - | 0.00 | Recorded: see cited records. |
| smoking-status:d14e9292 | - | 0.00 | Recorded: see cited records. |
| smoking-status:9292c3d5 | - | 0.00 | Recorded: see cited records. |
| smoking-status:ef5e136c | - | 0.00 | Recorded: see cited records. |
| a1c-trend:530b9289 | - | 1.00 | Recorded: 5.92, 5.9, 6.07. |
| a1c-trend:8d945e28 | - | 1.00 | Recorded: 3.14, 3.37, 3.14. |
| a1c-trend:8ff46e01 | - | 1.00 | Recorded: 6.27, 5.84, 6.11. |
| active-problems:0e6e0d73 | - | 1.00 | Recorded: see cited records. |
| active-problems:0eeb6aa3 | - | 1.00 | Recorded: see cited records. |
| active-problems:530b9289 | - | 1.00 | Recorded: see cited records. |
| active-problems:8446fe54 | - | 1.00 | Recorded: see cited records. |
| active-problems:8d945e28 | - | 1.00 | Recorded: see cited records. |
