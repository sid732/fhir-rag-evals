# Answer eval: rare-1

commit: `619b66f+dirty`, cohort: `57e36fe7e8f2`, card_version: `1`, mode: `real`, backend: `cli`, generator: `claude-opus-5-5`, effort: `medium`, judge: `claude-sonnet-5-5`, judge_prompt: `judge_v3-d86cce01`, retrieval: `hybrid, k=10, series=3, summary=True`, split: `all`, category: `rare_history`

`+dirty`: the run included the rare_history template and questions before they were committed; they were committed together with this report.

20 graded cases, 0 failed attempts (not scored).
Calls made through the Claude Code CLI (backend `cli`) ran on a subscription and weren't billed: their cost below is the list price of the tokens they used, and their model-call latency is the CLI's time in API calls.

## Abstention

|  | Answered | Said not in record |
|---|---|---|
| Answerable | 20 | 0 |
| Not in record | 0 | 0 |

'Not in record' precision 0.000, recall 0.000.

## Answered, answerable cases (20)

| Metric | n | Mean [95% CI] |
|---|---|---|
| Citation validity | 20 | 1.000 [1.000, 1.000] |
| Citation precision | 20 | 0.287 [0.247, 0.342] |
| Citation recall | 20 | 1.000 [1.000, 1.000] |
| Numbers and dates in cited cards | 20 | 1.000 [1.000, 1.000] |
| Key facts present | 20 | 1.000 [1.000, 1.000] |
| Faithfulness (judge: supported) | 20 | 0.958 [0.889, 1.000] |
| Judge: partially supported | 20 | 0.042 [0.000, 0.111] |
| Gold evidence in context | 20 | 1.000 [1.000, 1.000] |

## By category

| Category | n | Citation recall | Key facts | Faithfulness |
|---|---|---|---|---|
| rare_history | 20 | 1.000 | 1.000 | 0.958 |

## Cost and latency

|  | Value |
|---|---|
| Total cost (generator + judge) | $1.13 |
| Generator cost per case | $0.0369 |
| Judge cost per case | $0.0197 |
| Input tokens per case (mean) | 7104 |
| Output tokens per case (mean) | 426 |
| Latency p50 / p95, whole request | 5.36 s / 8.33 s |
| Latency p50 / p95, model call | 5.23 s / 8.12 s |

## Lowest-scoring answers

| Question | Faithfulness | Citation recall | Answer |
|---|---|---|---|
| rare-injury-of-neck:8446fe54 | 0.5 | 1.00 | Yes, the patient was diagnosed with injury of neck with onset 2026-01-11, along with whiplash injury to neck on the same date. Both conditions are listed as res |
| rare-streptococcal-sore-throat:d4f2a6f8 | 0.6666666666666666 | 1.00 | Yes, the patient was diagnosed with streptococcal sore throat with onset 2025-03-13, and it is recorded as resolved on 2025-03-27. The diagnosis was made at a s |
| rare-concussion-with-no-loss-of-consciousness:3ab4eeae | 1.0 | 1.00 | Yes. The patient was diagnosed with concussion with no loss of consciousness, with onset on 2019-12-04. The condition is marked resolved as of 2020-02-22, which |
| rare-disease-caused-by-severe-acute-respiratory-syndrome-coronavirus-2:7280f7f8 | 1.0 | 1.00 | Yes, the patient was diagnosed with disease caused by severe acute respiratory syndrome coronavirus 2, with onset 2020-12-21; it is recorded as resolved on 2021 |
| rare-concussion-injury-of-brain:9292c3d5 | 1.0 | 1.00 | Yes. The patient was diagnosed with concussion injury of brain, with onset on 2023-10-07, during an emergency room admission at CRANEVILLE PLACE REHABILITATION  |
| rare-eclampsia-in-pregnancy:0e6e0d73 | 1.0 | 1.00 | Yes. The patient was diagnosed with eclampsia in pregnancy with onset on 2024-04-22, and it is recorded as resolved on 2024-06-03. The clinical note from 2024-0 |
| rare-injury-of-tendon-of-the-rotator-cuff-of-shoulder:ef5e136c | 1.0 | 1.00 | Yes. The patient was diagnosed with injury of tendon of the rotator cuff of shoulder with onset 2024-12-18, and it was marked resolved on 2025-04-02. The diagno |
| rare-fracture-of-bone:d4f2a6f8 | 1.0 | 1.00 | Yes. The patient was diagnosed with fracture of bone with onset 2025-03-03, and it is recorded as resolved on 2025-06-19. The specific fracture was a fracture o |
| rare-epidermal-burn-of-skin:d14e9292 | 1.0 | 1.00 | Yes. The patient was diagnosed with epidermal burn of skin with onset 2026-01-31, at an emergency room visit for a burn injury on that date. She was prescribed  |
| rare-laceration---injury:0eeb6aa3 | 1.0 | 1.00 | Yes. The patient was diagnosed with laceration - injury with onset 2021-10-01, and it was resolved on 2021-10-25. It was diagnosed during an emergency room admi |
| rare-laceration-of-hand:d14e9292 | 1.0 | 1.00 | Yes. The patient was diagnosed with laceration of hand with onset 2018-09-29, and it resolved on 2018-10-25. At that visit on 2018-09-29, the open wound was sut |
| rare-miscarriage-in-first-trimester:0e6e0d73 | 1.0 | 1.00 | Yes. The patient was diagnosed with miscarriage in first trimester, with onset on 2018-04-16, and the condition is recorded as resolved on 2018-04-30. A clinica |
| rare-otitis-media:9292c3d5 | 1.0 | 1.00 | Yes, the patient was diagnosed with otitis media on 2022-06-08 during a symptom visit at Pittsfield Outpatient Clinic. At that visit, he was also diagnosed with |
| rare-polyp-of-colon:3ab4eeae | 1.0 | 1.00 | Yes. The patient was diagnosed with polyp of colon with onset 2024-09-24, and the condition is marked resolved as of 2025-11-17. It was found at a colon cancer  |
| rare-polyp-of-colon:ef5e136c | 1.0 | 1.00 | Yes, the patient was diagnosed with polyp of colon with an onset date of 2022-11-29, and the condition is marked resolved as of 2024-04-17. On 2022-11-29 the pa |
