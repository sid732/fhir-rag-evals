# Answer eval: test-2

commit: `61bfd3d+dirty`, cohort: `57e36fe7e8f2`, card_version: `1`, mode: `real`, backend: `cli`, generator: `claude-opus-5-5`, effort: `medium`, judge: `claude-sonnet-5-5`, judge_prompt: `judge_v3-d86cce01`, retrieval: `hybrid, k=10, series=3, summary=True`, split: `test`

109 graded cases, 0 failed attempts (not scored).
Calls made through the Claude Code CLI (backend `cli`) ran on a subscription and weren't billed: their cost below is the list price of the tokens they used, and their model-call latency is the CLI's time in API calls.

## Abstention

|  | Answered | Said not in record |
|---|---|---|
| Answerable | 93 | 1 |
| Not in record | 0 | 15 |

'Not in record' precision 0.938, recall 1.000.

## Answered, answerable cases (93)

| Metric | n | Mean [95% CI] |
|---|---|---|
| Citation validity | 93 | 1.000 [0.999, 1.000] |
| Citation precision | 93 | 0.456 [0.409, 0.506] |
| Citation recall | 93 | 0.925 [0.887, 0.964] |
| Numbers and dates in cited cards | 93 | 0.968 [0.935, 0.995] |
| Key facts present | 64 | 1.000 [1.000, 1.000] |
| Faithfulness (judge: supported) | 93 | 0.986 [0.958, 1.000] |
| Judge: partially supported | 93 | 0.014 [0.000, 0.042] |
| Gold evidence in context | 93 | 0.925 [0.887, 0.964] |

## By category

| Category | n | Citation recall | Key facts | Faithfulness |
|---|---|---|---|---|
| fact_lookup | 23 | 0.696 | - | 0.957 |
| values_dates | 39 | 1.000 | 1.000 | 0.991 |
| lay_terms | 12 | 1.000 | 1.000 | 1.000 |
| multi_step | 19 | 1.000 | 1.000 | 1.000 |

## Cost and latency

|  | Value |
|---|---|
| Total cost (generator + judge) | $5.44 |
| Generator cost per case | $0.0348 |
| Judge cost per case | $0.0151 |
| Input tokens per case (mean) | 6657 |
| Output tokens per case (mean) | 409 |
| Latency p50 / p95, whole request | 5.12 s / 17.28 s |
| Latency p50 / p95, model call | 4.90 s / 17.26 s |

## Lowest-scoring answers

| Question | Faithfulness | Citation recall | Answer |
|---|---|---|---|
| current-meds:530b9289 | 0.0 | 1.00 | The patient's only active prescription is ferrous sulfate 325 MG Oral Tablet, prescribed 2003-11-14. |
| latest-lipid-panel:8446fe54 | 0.6666666666666666 | 1.00 | The patient's most recent lipid panel, done on 2025-10-04, showed total cholesterol 150.12 mg/dL, triglycerides 160.16 mg/dL, direct LDL cholesterol 109.14 mg/d |
| smoking-status:0e6e0d73 | 1.0 | 0.00 | No. The clinical notes say she is a former smoker who quit at age 16. The most recent note that mentions smoking is dated 2024-04-22, and it still says she quit |
| smoking-status:3ab4eeae | 1.0 | 0.00 | No, the patient doesn't smoke: the clinical notes always say "Patient has never smoked." The latest note to say this is from 2025-12-19. Notes going back to 197 |
| smoking-status:530b9289 | 1.0 | 0.00 | No, the record shows the patient has never smoked. Every clinical note from 1995-09-07 to 2020-05-06 lists her as a never-smoker. None of the excerpts records h |
| smoking-status:7280f7f8 | 1.0 | 0.00 | No, the patient doesn't smoke: every clinical note says he has never smoked, from the first one on 1964-12-20 to the latest one on 2024-12-01. The same notes al |
| smoking-status:8ff46e01 | 1.0 | 0.00 | No, the patient does not smoke: clinical notes as recent as 2025-12-31 say "Patient has never smoked." Earlier notes going back to 1980-04-22 record the same ne |
| smoking-status:d4f2a6f8 | 1.0 | 0.00 | No, the social history in the clinical notes says the patient has never smoked. The most recent of these notes is dated 2024-12-30, and earlier notes going back |
| smoking-status:e56a8cde | 1.0 | 0.00 | No. Every clinical note in the excerpts says "Patient has never smoked," from 1963-07-18 through the most recent note on 2016-11-17. |
| a1c-trend:760e0542 | 1.0 | 1.00 | The patient's last three hemoglobin A1c results haven't changed: each one is 3.08 %, on 2026-05-13, 2026-08-05 and 2026-09-09. |
| a1c-trend:0eeb6aa3 | 1.0 | 1.00 | The last three hemoglobin A1c results haven't changed: each one was 6.04 %. The tests were done on 2025-07-20, 2025-12-14 and 2026-08-09, the most recent. |
| a1c-trend:772fc930 | 1.0 | 1.00 | The last three hemoglobin A1c results went down and then partly back up: 3.35 % on 2026-07-02, 2.96 % on 2026-07-09, and 3.11 % on 2026-07-16. The most recent v |
| a1c-trend:7280f7f8 | 1.0 | 1.00 | The patient's last three hemoglobin A1c results were 6.22 % on 2024-11-24, 5.82 % on 2025-04-06, and 5.88 % on 2026-04-12. So the value dropped from 6.22 % to 5 |
| a1c-trend:8446fe54 | 1.0 | 1.00 | The patient's last three hemoglobin A1c results have not changed: each one was 6.91 %. The tests were done on 2023-09-22, 2024-09-27 and 2025-10-03, and the mos |
| a1c-trend:d4f2a6f8 | 1.0 | 1.00 | The patient's last three hemoglobin A1c results went up a little each time: 3.05 % on 2026-03-05, 3.09 % on 2026-04-02, and 3.33 % on 2026-04-09. Before these,  |
