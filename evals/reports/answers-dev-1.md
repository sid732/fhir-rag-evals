# Answer eval: dev-1

commit: `248b54a`, cohort: `57e36fe7e8f2`, mode: `real`, generator: `claude-opus-5-5`, effort: `medium`, judge: `claude-sonnet-5-5`, retrieval: `hybrid, k=10, series=3, summary=True`, split: `dev`

164 graded cases, 0 failed attempts (not scored).

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
| Citation precision | 140 | 0.568 [0.531, 0.602] |
| Citation recall | 140 | 0.957 [0.931, 0.985] |
| Numbers and dates in cited cards | 140 | 0.979 [0.957, 0.996] |
| Key facts present | 87 | 1.000 [1.000, 1.000] |
| Faithfulness (judge: supported) | 140 | 0.635 [0.582, 0.690] |
| Judge: partially supported | 140 | 0.362 [0.307, 0.417] |
| Gold evidence in context | 140 | 0.957 [0.931, 0.985] |

## By category

| Category | n | Citation recall | Key facts | Faithfulness |
|---|---|---|---|---|
| fact_lookup | 34 | 0.824 | - | 0.750 |
| values_dates | 59 | 1.000 | 1.000 | 0.432 |
| lay_terms | 18 | 1.000 | 1.000 | 0.894 |
| multi_step | 29 | 1.000 | 1.000 | 0.753 |

## Cost and latency

|  | Value |
|---|---|
| Total cost (generator + judge) | $5.14 |
| Generator cost per case | $0.0275 |
| Judge cost per case | $0.0038 |
| Input tokens per case (mean) | 5353 |
| Output tokens per case (mean) | 307 |
| Latency p50 / p95, whole request | 3.78 s / 8.37 s |
| Latency p50 / p95, model call | 3.71 s / 8.35 s |

## Lowest-scoring answers

| Question | Faithfulness | Citation recall | Answer |
|---|---|---|---|
| last-colonoscopy:0eeb6aa3 | 0.0 | 1.00 | The patient's most recent colonoscopy was on 2023-10-29, with status completed, performed at a check-up encounter for colon cancer screening at HOLY FAMILY HOSP |
| last-colonoscopy:8446fe54 | 0.0 | 1.00 | The patient's most recent colonoscopy in the record was on 2018-04-18, with status completed, performed during a check-up encounter for colon cancer screening a |
| last-er-visit:0e6e0d73 | 0.0 | 1.00 | The most recent emergency encounter in the record was an obstetric emergency hospital admission on 2024-06-03 at ALLIANCE HEALTH AT BRAINTREE, with the reason l |
| last-visit:3ab4eeae | 0.0 | 1.00 | The patient's most recent visit in the record was on 2026-02-17, an ambulatory (AMB) encounter for problem (procedure) at TUFTS MEDICAL CENTER, INC, with the re |
| last-visit:530b9289 | 0.0 | 1.00 | The most recent visit in the record was on 2025-03-12, an ambulatory (AMB) encounter for check up at NORTH SHORE MEDICAL CENTER INC, with the reason listed as G |
| last-visit:760e0542 | 0.0 | 1.00 | The patient's most recent visit was on 2026-09-09, an ambulatory (class AMB) urgent care clinic encounter at MIDDLETON FAMILY MEDICINE URGENT CARE, LLC. |
| last-visit:8446fe54 | 0.0 | 1.00 | The patient's most recent visit was on 2026-04-10, an ambulatory (class AMB) ophthalmic examination and evaluation at MILFORD REGIONAL MEDICAL CENTER. |
| latest-bp:760e0542 | 0.0 | 1.00 | The most recent blood pressure reading, on 2026-09-09, was Systolic Blood Pressure 97 mm[Hg] and Diastolic Blood Pressure 68 mm[Hg]. |
| latest-bp:772fc930 | 0.0 | 1.00 | The most recent blood pressure reading was on 2026-07-09: Systolic Blood Pressure 129 mm[Hg] and Diastolic Blood Pressure 89 mm[Hg]. |
| latest-bp:0e6e0d73 | 0.0 | 1.00 | The most recent blood pressure reading, on 2026-05-25, was Systolic Blood Pressure 109 mm[Hg] and Diastolic Blood Pressure 73 mm[Hg]. |
| latest-bp:8ff46e01 | 0.0 | 1.00 | The most recent blood pressure reading was on 2025-12-31, with a systolic blood pressure of 109 mm[Hg] and a diastolic blood pressure of 48 mm[Hg]. |
| latest-bp:9292c3d5 | 0.0 | 1.00 | The most recent blood pressure reading was on 2026-04-26, with a systolic blood pressure of 133 mm[Hg] and a diastolic blood pressure of 76 mm[Hg]. |
| latest-bp:e56a8cde | 0.0 | 1.00 | The most recent blood pressure reading, on 2025-12-25, was Systolic Blood Pressure 106 mm[Hg] and Diastolic Blood Pressure 75 mm[Hg]. |
| latest-lab-18262-6:d14e9292 | 0.0 | 1.00 | The most recent LDL cholesterol (direct assay) result was 73.93 mg/dL, measured on 2025-05-15. The prior result was 81.28 mg/dL on 2022-05-12. |
| latest-lab-2093-3:3ab4eeae | 0.0 | 1.00 | The most recent total cholesterol result was 202.13 mg/dL, measured on 2025-10-22. |
