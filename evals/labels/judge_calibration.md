# Judge calibration: dev-1-judge2

Labeled on 2026-10-30 by Claude Opus 5.5 in five batches of 10, blind to the judge's
verdicts (each batch saw only the rubric and its own items). Each `note:` line is the
labeler's reason.

50 answer sentences. Label each one by the rubric below, then run
`uv run python -m fhir_rag.evals.calibrate score --set judge_calibration`. Don't open
`judge_calibration.verdicts.jsonl` or the run's report until you're done.

On each `label:` line write `s` (supported), `p` (partially supported) or `n`
(not supported). Add `?` after the letter (`s?`) when the case is unclear to
you; unclear cases are reported apart from clear ones. The sentence being
labeled is in bold inside its whole answer.

The judge is given the same rubric:

- Facts about specific entries (names, numbers, units, dates, statuses,
  reasons, how entries relate) must be stated in the cards the sentence cites.
- Claims about the whole record (most recent, latest, first or only one of its
  kind, counts, a complete list, something absent or never done) are checked
  against everything the model saw.
- `s`: every claim passes its check. `p`: the main claim passes, but a detail
  is missing from its evidence or goes beyond it. `n`: the main claim fails or
  the evidence contradicts it; a fact about an entry fails when the sentence
  cites nothing.

## 1. `prescribed-for-diabetes-mellitus-type-2:ef5e136c#0#0`

Question: Which medications have been prescribed for the patient's diabetes mellitus type 2?

Answer: **The only medication with diabetes mellitus type 2 listed as its reason is insulin isophane, human 70 UNT/ML / insulin, regular, human 30 UNT/ML Injectable Suspension [Humulin], prescribed 2026-09-30 with status active.** Separately, tropicamide 5 mg/ml ophthalmic solution was prescribed at visits that included a diabetic retinal eye exam, most recently on 2022-12-10, but no reason is stated for it.

Cards this sentence cites:

- `[MedicationRequest/ef5e136c-ff1e-0695-6804-cf31640a9491]` MedicationRequest | prescribed 2026-09-30 | insulin isophane, human 70 UNT/ML / insulin, regular, human 30 UNT/ML Injectable Suspension [Humulin] | status active | reason: Diabetes mellitus type 2 (disorder) | RxNorm 106892

<details><summary>Everything the model saw (47 cards)</summary>

```text
[Condition/ef5e136c-ff1e-0695-1f8c-935a12106cac] Condition | onset 2026-09-30 | Medication review due (situation) | clinical status active | SNOMED 314529007
[Condition/ef5e136c-ff1e-0695-7e5d-470b95f60db2] Condition | onset 2026-09-23 | Social isolation (finding) | clinical status active | SNOMED 422650009
[Condition/ef5e136c-ff1e-0695-9d2d-c4be459bc9f4] Condition | onset 2026-09-09 | Unemployed (finding) | clinical status active | SNOMED 73438004
[Condition/ef5e136c-ff1e-0695-7b9c-f43e5ca3f6c6] Condition | onset 2026-08-12 | Stress (finding) | clinical status active | SNOMED 73595000
[Condition/ef5e136c-ff1e-0695-aa04-94486c99258f] Condition | onset 2025-08-27 | End-stage renal disease (disorder) | clinical status active | SNOMED 46177005
[Condition/ef5e136c-ff1e-0695-423f-ed71d76e81e3] Condition | onset 2025-03-30 | Awaiting transplantation of kidney (situation) | clinical status active | SNOMED 698306007
[Condition/ef5e136c-ff1e-0695-71df-3a96389b0a39] Condition | onset 2025-02-05 | Chronic kidney disease stage 4 (disorder) | clinical status active | SNOMED 431857002
[Condition/ef5e136c-ff1e-0695-5331-2d63eb213c34] Condition | onset 2024-05-15 | Proteinuria due to type 2 diabetes mellitus (disorder) | clinical status active | SNOMED 157141000119108
[Condition/ef5e136c-ff1e-0695-3834-fa6cb282a475] Condition | onset 2024-05-15 | Chronic kidney disease stage 3 (disorder) | clinical status active | SNOMED 433144002
[Condition/ef5e136c-ff1e-0695-68fe-9e2010333061] Condition | onset 2023-08-16 | Microalbuminuria due to type 2 diabetes mellitus (disorder) | clinical status active | SNOMED 90781000119102
[Condition/ef5e136c-ff1e-0695-65f5-8d04f278a661] Condition | onset 2023-08-16 | Chronic kidney disease stage 2 (disorder) | clinical status active | SNOMED 431856006
[Condition/ef5e136c-ff1e-0695-aac2-46a0ff462178] Condition | onset 2023-04-19 | Gingivitis (disorder) | clinical status active | SNOMED 66383009
[Condition/ef5e136c-ff1e-0695-fda2-40e12f6b17a7] Condition | onset 2017-11-15 | Chronic kidney disease stage 1 (disorder) | clinical status active | SNOMED 431855005
[Condition/ef5e136c-ff1e-0695-bf3f-30946ad3f8b4] Condition | onset 2017-11-15 | Disorder of kidney due to diabetes mellitus (disorder) | clinical status active | SNOMED 127013003
[Condition/ef5e136c-ff1e-0695-eac4-d545a0296998] Condition | onset 2011-07-27 | Essential hypertension (disorder) | clinical status active | SNOMED 59621000
[Condition/ef5e136c-ff1e-0695-b228-2f5ff5bb47cb] Condition | onset 2010-05-19 | Metabolic syndrome X (disorder) | clinical status active | SNOMED 237602007
[Condition/ef5e136c-ff1e-0695-af16-82f03f777ba8] Condition | onset 2010-05-19 | Hypertriglyceridemia (disorder) | clinical status active | SNOMED 302870006
[Condition/ef5e136c-ff1e-0695-5ca5-51bfdc51320e] Condition | onset 2010-05-12 | Diabetes mellitus type 2 (disorder) | clinical status active | SNOMED 44054006
[Condition/ef5e136c-ff1e-0695-f7ec-ceae0c2566bc] Condition | onset 2004-06-16 | Body mass index 30+ - obesity (finding) | clinical status active | SNOMED 162864005
[Condition/ef5e136c-ff1e-0695-c94a-5d81ddd88117] Condition | onset 1997-05-07 | Has a criminal record (finding) | clinical status active | SNOMED 266948004
[Condition/ef5e136c-ff1e-0695-6efc-9f7d5e6b04ef] Condition | onset 1993-09-01 | Anemia (disorder) | clinical status active | SNOMED 271737000
[Condition/ef5e136c-ff1e-0695-1f68-dac24351dbaa] Condition | onset 1993-04-14 | Prediabetes (finding) | clinical status active | SNOMED 714628002
[Condition/ef5e136c-ff1e-0695-2d8d-328849698529] Condition | onset 1993-01-22 | History of tubal ligation (situation) | clinical status active | SNOMED 267020005
[Condition/ef5e136c-ff1e-0695-0825-c31e8b252683] Condition | onset 1983-11-14 | Past pregnancy history of miscarriage (situation) | clinical status active | SNOMED 161744009
[Condition/ef5e136c-ff1e-0695-cb16-3a98eeb2de7a] Condition | onset 1976-01-07 | Received higher education (finding) | clinical status active | SNOMED 224299000
[Condition/ef5e136c-ff1e-0695-3278-6a86eaf1fb5d] Condition | onset 1975-06-27 | Chronic sinusitis (disorder) | clinical status active | SNOMED 40055000
[Condition/ef5e136c-ff1e-0695-337f-d12087c8dbb5] Condition | onset 1975-01-01 | Risk activity involvement (finding) | clinical status active | SNOMED 160968000
[MedicationRequest/ef5e136c-ff1e-0695-ffec-2ea7ac772a27] MedicationRequest | prescribed 2026-09-30 | Hydrochlorothiazide 25 MG Oral Tablet | status active | reason: Essential hypertension (disorder) | RxNorm 310798
[MedicationRequest/ef5e136c-ff1e-0695-b3ba-a1ec7bcfb9f4] MedicationRequest | prescribed 2026-09-30 | albuterol 0.83 MG/ML Inhalation Solution | status active | RxNorm 630208
[MedicationRequest/ef5e136c-ff1e-0695-901e-2e1f9afb0cca] MedicationRequest | prescribed 2026-09-30 | lisinopril 10 MG Oral Tablet | status active | reason: Essential hypertension (disorder) | RxNorm 314076
[MedicationRequest/ef5e136c-ff1e-0695-76a6-8eeb54f8a75e] MedicationRequest | prescribed 2026-09-30 | 120 ACTUAT fluticasone propionate 0.044 MG/ACTUAT Metered Dose Inhaler [Flovent] | status active | RxNorm 895996
[MedicationRequest/ef5e136c-ff1e-0695-6c6d-182c3b9c47c1] MedicationRequest | prescribed 2026-09-30 | amLODIPine 2.5 MG Oral Tablet | status active | reason: Essential hypertension (disorder) | RxNorm 308136
[MedicationRequest/ef5e136c-ff1e-0695-6804-cf31640a9491] MedicationRequest | prescribed 2026-09-30 | insulin isophane, human 70 UNT/ML / insulin, regular, human 30 UNT/ML Injectable Suspension [Humulin] | status active | reason: Diabetes mellitus type 2 (disorder) | RxNorm 106892
[Encounter/ef5e136c-ff1e-0695-08ba-2471a16a6570] Encounter | 2026-09-30 | Emergency room admission (procedure) | class EMER | at APPLE VALLEY CENTER
[Encounter/ef5e136c-ff1e-0695-aea4-11055569fd51] Encounter | 2026-09-23 | Urgent care clinic (environment) | class AMB | at URGENT HELP CHELMSFORD PC
[Encounter/ef5e136c-ff1e-0695-4a41-6fca58c80cb7] Encounter | 2026-09-16 | Urgent care clinic (environment) | class AMB | at URGENT HELP CHELMSFORD PC
[Immunization/ef5e136c-ff1e-0695-6beb-93901776b619] Immunization | 2026-05-13 | Influenza, split virus, trivalent, PF | status completed | CVX 140
[DocumentReference/e66e01ce-8a8a-57d5-9bf6-52c4d40ac8d2#2] Clinical note | 2021-01-19 | part 2 of 2 | # Medications lisinopril 10 mg oral tablet; tropicamide 5 mg/ml ophthalmic solution; hydrochlorothiazide 25 mg oral tablet; amoxicillin 250 mg oral capsule; acetaminophen 325 mg / oxycodone hydrochloride 5 mg oral tablet; 120 actuat fluticasone propionate 0.044 mg/actuat metered dose inhaler [flovent]; amlodipine 2.5 mg oral tablet; insulin isophane, human 70 unt/ml / insulin, regular, human 30 unt/ml injectable suspension [humulin]; albuterol 0.83 mg/ml inhalation solution; naproxen sodium 220 mg oral tablet # Assessment and Plan ## Plan The following procedures were conducted: - visual acuity testing (procedure) - intraocular pressure test (procedure) - ocular slit lamp examination (procedure) - indirect gonioscopy (procedure) - camera fundoscopy (procedure) - diabetic retinal eye exam (procedure) The patient was prescribed the following medications: - tropicamide 5 mg/ml ophthalmic solution
[DocumentReference/db48b326-95ec-6012-24c9-24234b74b109#2] Clinical note | 2020-01-25 | part 2 of 2 | # Medications lisinopril 10 mg oral tablet; tropicamide 5 mg/ml ophthalmic solution; hydrochlorothiazide 25 mg oral tablet; amoxicillin 250 mg oral capsule; acetaminophen 325 mg / oxycodone hydrochloride 5 mg oral tablet; 120 actuat fluticasone propionate 0.044 mg/actuat metered dose inhaler [flovent]; amlodipine 2.5 mg oral tablet; insulin isophane, human 70 unt/ml / insulin, regular, human 30 unt/ml injectable suspension [humulin]; albuterol 0.83 mg/ml inhalation solution; naproxen sodium 220 mg oral tablet # Assessment and Plan ## Plan The following procedures were conducted: - visual acuity testing (procedure) - intraocular pressure test (procedure) - ocular slit lamp examination (procedure) - indirect gonioscopy (procedure) - camera fundoscopy (procedure) - diabetic retinal eye exam (procedure) The patient was prescribed the following medications: - tropicamide 5 mg/ml ophthalmic solution
[Procedure/ef5e136c-ff1e-0695-f6b2-4d72c75dfa7f] Procedure | 2024-12-11 | Indirect gonioscopy (procedure) | status completed | reason: Diabetes mellitus type 2 (disorder) | SNOMED 389153003
[Procedure/ef5e136c-ff1e-0695-de5f-91cf8475a486] Procedure | 2023-12-05 | Indirect gonioscopy (procedure) | status completed | reason: Diabetes mellitus type 2 (disorder) | SNOMED 389153003
[Procedure/ef5e136c-ff1e-0695-00d9-98012c068d6a] Procedure | 2022-12-10 | Indirect gonioscopy (procedure) | status completed | reason: Diabetes mellitus type 2 (disorder) | SNOMED 389153003
[DocumentReference/2267fd18-9da9-a4fa-aa4d-a95b255bf0fd#2] Clinical note | 2021-12-15 | part 2 of 2 | # Medications lisinopril 10 mg oral tablet; tropicamide 5 mg/ml ophthalmic solution; hydrochlorothiazide 25 mg oral tablet; amoxicillin 250 mg oral capsule; acetaminophen 325 mg / oxycodone hydrochloride 5 mg oral tablet; 120 actuat fluticasone propionate 0.044 mg/actuat metered dose inhaler [flovent]; amlodipine 2.5 mg oral tablet; insulin isophane, human 70 unt/ml / insulin, regular, human 30 unt/ml injectable suspension [humulin]; albuterol 0.83 mg/ml inhalation solution; naproxen sodium 220 mg oral tablet # Assessment and Plan ## Plan The following procedures were conducted: - visual acuity testing (procedure) - intraocular pressure test (procedure) - ocular slit lamp examination (procedure) - indirect gonioscopy (procedure) - camera fundoscopy (procedure) - diabetic retinal eye exam (procedure) The patient was prescribed the following medications: - tropicamide 5 mg/ml ophthalmic solution
[DocumentReference/266eae94-47a1-e383-dbf6-ff8a9122547f#2] Clinical note | 2022-12-10 | part 2 of 2 | # Medications lisinopril 10 mg oral tablet; tropicamide 5 mg/ml ophthalmic solution; hydrochlorothiazide 25 mg oral tablet; amoxicillin 250 mg oral capsule; acetaminophen 325 mg / oxycodone hydrochloride 5 mg oral tablet; 120 actuat fluticasone propionate 0.044 mg/actuat metered dose inhaler [flovent]; amlodipine 2.5 mg oral tablet; insulin isophane, human 70 unt/ml / insulin, regular, human 30 unt/ml injectable suspension [humulin]; albuterol 0.83 mg/ml inhalation solution; naproxen sodium 220 mg oral tablet # Assessment and Plan ## Plan The following procedures were conducted: - visual acuity testing (procedure) - intraocular pressure test (procedure) - ocular slit lamp examination (procedure) - indirect gonioscopy (procedure) - camera fundoscopy (procedure) - diabetic retinal eye exam (procedure) The patient was prescribed the following medications: - tropicamide 5 mg/ml ophthalmic solution
[DocumentReference/f60e4bd7-409f-c1e9-7e5f-4220c110be9f#2] Clinical note | 2019-12-04 | part 2 of 3 | # Medications lisinopril 10 mg oral tablet; tropicamide 5 mg/ml ophthalmic solution; hydrochlorothiazide 25 mg oral tablet; amoxicillin 250 mg oral capsule; acetaminophen 325 mg / oxycodone hydrochloride 5 mg oral tablet; 120 actuat fluticasone propionate 0.044 mg/actuat metered dose inhaler [flovent]; amlodipine 2.5 mg oral tablet; insulin isophane, human 70 unt/ml / insulin, regular, human 30 unt/ml injectable suspension [humulin]; albuterol 0.83 mg/ml inhalation solution; naproxen sodium 220 mg oral tablet
[DocumentReference/26c615dc-db73-72f4-2a4d-fb891dfb2540#2] Clinical note | 2019-03-01 | part 2 of 2 | # Medications lisinopril 10 mg oral tablet; tropicamide 5 mg/ml ophthalmic solution; hydrochlorothiazide 25 mg oral tablet; 120 actuat fluticasone propionate 0.044 mg/actuat metered dose inhaler [flovent]; amlodipine 2.5 mg oral tablet; insulin isophane, human 70 unt/ml / insulin, regular, human 30 unt/ml injectable suspension [humulin]; albuterol 0.83 mg/ml inhalation solution # Assessment and Plan ## Plan The following procedures were conducted: - visual acuity testing (procedure) - intraocular pressure test (procedure) - ocular slit lamp examination (procedure) - indirect gonioscopy (procedure) - camera fundoscopy (procedure) - diabetic retinal eye exam (procedure) The patient was prescribed the following medications: - tropicamide 5 mg/ml ophthalmic solution
[DocumentReference/4d0d0889-f360-8c5c-b81d-aa7686616e55#2] Clinical note | 2016-10-19 | part 2 of 2 | # Assessment and Plan ## Plan The patient was prescribed the following medications: - hydrochlorothiazide 25 mg oral tablet - 120 actuat fluticasone propionate 0.044 mg/actuat metered dose inhaler [flovent] - lisinopril 10 mg oral tablet - amlodipine 2.5 mg oral tablet - albuterol 0.83 mg/ml inhalation solution
```

</details>

label: s
note: Cited card shows Humulin 70/30 prescribed 2026-09-30, status active, reason Diabetes mellitus type 2; of the six MedicationRequests seen, the others have reason Essential hypertension or none, so 'only' holds.

## 2. `last-visit:d4f2a6f8#0#0`

Question: When was the patient's most recent visit, and what kind of visit was it?

Answer: **The patient's most recent visit was on 2026-09-23, an ambulatory (class AMB) encounter for problem at TEWKSBURY HOSPITAL, with the reason listed as chronic kidney disease stage 4.**

Cards this sentence cites:

- `[Encounter/d4f2a6f8-e358-6b1b-1745-afd1215948c6]` Encounter | 2026-09-23 | Encounter for problem (procedure) | class AMB | reason: Chronic kidney disease stage 4 (disorder) | at TEWKSBURY HOSPITAL

<details><summary>Everything the model saw (42 cards)</summary>

```text
[Condition/d4f2a6f8-e358-6b1b-a870-7578fc115ba3] Condition | onset 2026-04-02 | Stress (finding) | clinical status active | SNOMED 73595000
[Condition/d4f2a6f8-e358-6b1b-37cc-cacad982df8c] Condition | onset 2026-04-02 | Reports of violence in the environment (finding) | clinical status active | SNOMED 424393004
[Condition/d4f2a6f8-e358-6b1b-c78d-1b6bc447e34a] Condition | onset 2025-12-04 | Full-time employment (finding) | clinical status active | SNOMED 160903007
[Condition/d4f2a6f8-e358-6b1b-29d8-fc1e6a15e60d] Condition | onset 2025-12-04 | Medication review due (situation) | clinical status active | SNOMED 314529007
[Condition/d4f2a6f8-e358-6b1b-f1ac-92593f6454e7] Condition | onset 2025-03-20 | Chronic kidney disease stage 4 (disorder) | clinical status active | SNOMED 431857002
[Condition/d4f2a6f8-e358-6b1b-4959-9b97d2d3536d] Condition | onset 2025-02-03 | Awaiting transplantation of kidney (situation) | clinical status active | SNOMED 698306007
[Condition/d4f2a6f8-e358-6b1b-76dc-8902de051de4] Condition | onset 2022-10-20 | Microalbuminuria due to type 2 diabetes mellitus (disorder) | clinical status active | SNOMED 90781000119102
[Condition/d4f2a6f8-e358-6b1b-1e8b-4beeba77ed82] Condition | onset 2022-10-20 | Proteinuria due to type 2 diabetes mellitus (disorder) | clinical status active | SNOMED 157141000119108
[Condition/d4f2a6f8-e358-6b1b-042a-23b17f3aef58] Condition | onset 2022-10-20 | Chronic kidney disease stage 3 (disorder) | clinical status active | SNOMED 433144002
[Condition/d4f2a6f8-e358-6b1b-7e47-2334f6b84c0f] Condition | onset 2020-05-28 | History of coronary artery bypass grafting (situation) | clinical status active | SNOMED 399261000
[Condition/d4f2a6f8-e358-6b1b-ebe7-54c5d38117fc] Condition | onset 2020-03-19 | Abnormal findings diagnostic imaging heart+coronary circulat (finding) | clinical status active | SNOMED 274531002
[Condition/d4f2a6f8-e358-6b1b-e1e3-648cc0a38c11] Condition | onset 2020-03-05 | Chronic kidney disease stage 1 (disorder) | clinical status active | SNOMED 431855005
[Condition/d4f2a6f8-e358-6b1b-7f62-e48c3798c8b1] Condition | onset 2020-03-05 | Disorder of kidney due to diabetes mellitus (disorder) | clinical status active | SNOMED 127013003
[Condition/d4f2a6f8-e358-6b1b-6866-45937dfd6387] Condition | onset 2020-03-05 | Ischemic heart disease (disorder) | clinical status active | SNOMED 414545008
[Condition/d4f2a6f8-e358-6b1b-9d41-102804feed92] Condition | onset 2004-12-09 | Metabolic syndrome X (disorder) | clinical status active | SNOMED 237602007
[Condition/d4f2a6f8-e358-6b1b-4dab-6274d2854b00] Condition | onset 2002-11-28 | Anemia (disorder) | clinical status active | SNOMED 271737000
[Condition/d4f2a6f8-e358-6b1b-c5c9-83d1526dc404] Condition | onset 2001-11-22 | Essential hypertension (disorder) | clinical status active | SNOMED 59621000
[Condition/d4f2a6f8-e358-6b1b-d3db-555b40b7ebe5] Condition | onset 2000-05-04 | Prediabetes (finding) | clinical status active | SNOMED 714628002
[Condition/d4f2a6f8-e358-6b1b-4a76-ae3dfbf47144] Condition | onset 1986-11-06 | Body mass index 30+ - obesity (finding) | clinical status active | SNOMED 162864005
[Condition/d4f2a6f8-e358-6b1b-c732-3e05c6bfa924] Condition | onset 1982-10-28 | Only received primary school education (finding) | clinical status active | SNOMED 224295006
[MedicationRequest/d4f2a6f8-e358-6b1b-da40-22bfe510e33d] MedicationRequest | prescribed 2026-04-09 | Hydrochlorothiazide 25 MG Oral Tablet | status active | reason: Essential hypertension (disorder) | RxNorm 310798
[MedicationRequest/d4f2a6f8-e358-6b1b-b1c3-dd4b80a73ea4] MedicationRequest | prescribed 2026-04-09 | insulin isophane, human 70 UNT/ML / insulin, regular, human 30 UNT/ML Injectable Suspension [Humulin] | status active | reason: Prediabetes (finding) | RxNorm 106892
[MedicationRequest/d4f2a6f8-e358-6b1b-875e-3c108c25914e] MedicationRequest | prescribed 2026-04-09 | lisinopril 10 MG Oral Tablet | status active | reason: Essential hypertension (disorder) | RxNorm 314076
[MedicationRequest/d4f2a6f8-e358-6b1b-6913-a3ea2279b298] MedicationRequest | prescribed 2026-04-09 | amLODIPine 2.5 MG Oral Tablet | status active | reason: Essential hypertension (disorder) | RxNorm 308136
[MedicationRequest/d4f2a6f8-e358-6b1b-f33b-aeabe5d3ea2a] MedicationRequest | prescribed 2020-03-12 | Simvastatin 20 MG Oral Tablet | status active | RxNorm 312961
[MedicationRequest/d4f2a6f8-e358-6b1b-da7b-92b61020d936] MedicationRequest | prescribed 2020-03-12 | Nitroglycerin 0.4 MG/ACTUAT Mucosal Spray | status active | RxNorm 705129
[MedicationRequest/d4f2a6f8-e358-6b1b-c7c5-6dd35faf2d76] MedicationRequest | prescribed 2020-03-12 | 24 HR metoprolol succinate 100 MG Extended Release Oral Tablet | status active | RxNorm 866412
[MedicationRequest/d4f2a6f8-e358-6b1b-102e-595eecaa5a85] MedicationRequest | prescribed 2020-03-12 | Clopidogrel 75 MG Oral Tablet | status active | RxNorm 309362
[Encounter/d4f2a6f8-e358-6b1b-1745-afd1215948c6] Encounter | 2026-09-23 | Encounter for problem (procedure) | class AMB | reason: Chronic kidney disease stage 4 (disorder) | at TEWKSBURY HOSPITAL
[Encounter/d4f2a6f8-e358-6b1b-3133-f32329c08d3e] Encounter | 2026-09-20 | Encounter for problem (procedure) | class AMB | reason: Chronic kidney disease stage 4 (disorder) | at TEWKSBURY HOSPITAL
[Encounter/d4f2a6f8-e358-6b1b-0f9b-7fe2ad9bcba8] Encounter | 2026-09-20 | Encounter for problem (procedure) | class AMB | reason: Chronic kidney disease stage 4 (disorder) | at TEWKSBURY HOSPITAL
[Immunization/d4f2a6f8-e358-6b1b-d852-5d7c3a4a2175] Immunization | 2026-03-05 | Influenza, split virus, trivalent, PF | status completed | CVX 140
[Condition/d4f2a6f8-e358-6b1b-682c-89c53ae93d73] Condition | onset 2017-02-16 | Medication review due (situation) | clinical status resolved | resolved 2017-02-16 | SNOMED 314529007
[Condition/d4f2a6f8-e358-6b1b-f66d-d5a922c47210] Condition | onset 2025-09-18 | Medication review due (situation) | clinical status resolved | resolved 2025-09-25 | SNOMED 314529007
[Condition/d4f2a6f8-e358-6b1b-56d2-679e490aba62] Condition | onset 2025-08-21 | Medication review due (situation) | clinical status resolved | resolved 2025-08-21 | SNOMED 314529007
[Procedure/d4f2a6f8-e358-6b1b-6620-b14f01ad313b] Procedure | 2023-04-06 | periodic orthodontic treatment visit | status completed | http://www.ada.org/cdt D8670
[DocumentReference/89ed1698-d0b7-3d7b-a65f-b4ec656372df#2] Clinical note | 2023-04-06 | part 2 of 2 | # Assessment and Plan ## Plan The following procedures were conducted: - periodic orthodontic treatment visit
[Observation/d4f2a6f8-e358-6b1b-f589-fc6dd6ddb437] Observation (laboratory) | 2020-05-29 | Prothrombin time (PT) = 11.318 s | status final | LOINC 5902-2
[Observation/d4f2a6f8-e358-6b1b-9d2f-acf3992aecba] Observation (laboratory) | 2020-05-28 | Prothrombin time (PT) = 9.8251 s | status final | LOINC 5902-2
[Observation/d4f2a6f8-e358-6b1b-8bfa-b85630de3a60] Observation (laboratory) | 2020-04-27 | Prothrombin time (PT) = 11.608 s | status final | LOINC 5902-2
[Observation/d4f2a6f8-e358-6b1b-7f59-7babc37f6fac] Observation (laboratory) | 2020-05-29 | aPTT in Blood by Coagulation assay = 33.795 s | status final | LOINC 3173-2
[Observation/d4f2a6f8-e358-6b1b-9e16-230f4fc10cff] Observation (laboratory) | 2020-05-28 | aPTT in Blood by Coagulation assay = 25.702 s | status final | LOINC 3173-2
```

</details>

label: s
note: Cited encounter is 2026-09-23, Encounter for problem, class AMB, reason CKD stage 4, at TEWKSBURY HOSPITAL; the other encounters are 2026-09-20 and the other dated cards are older, so it is the most recent.

## 3. `current-meds:7280f7f8#0#2`

Question: What medications is the patient currently prescribed?

Answer: The patient's active prescriptions from 2026-04-12 to 2026-04-13 are Simvastatin 10 MG Oral Tablet (for hyperlipidemia), Ibuprofen 400 MG Oral Tablet [Ibu], Acetaminophen 325 MG / Oxycodone Hydrochloride 10 MG Oral Tablet [Percocet], Galantamine 4 MG Oral Tablet (for Alzheimer's disease), and Acetaminophen 325 MG Oral Tablet [Tylenol]. Also still listed as active from 2018-11-11 are Simvastatin 20 MG Oral Tablet, Nitroglycerin 0.4 MG/ACTUAT Mucosal Spray, Clopidogrel 75 MG Oral Tablet, and 24 HR metoprolol succinate 100 MG Extended Release Oral Tablet. **Two simvastatin prescriptions are active at the same time: 20 MG from 2018-11-11 and 10 MG from 2026-04-13.**

Cards this sentence cites:

- `[MedicationRequest/7280f7f8-315d-7c6a-e1ca-6672a64e96d6]` MedicationRequest | prescribed 2018-11-11 | Simvastatin 20 MG Oral Tablet | status active | RxNorm 312961
- `[MedicationRequest/7280f7f8-315d-7c6a-d103-5f5cf25ace53]` MedicationRequest | prescribed 2026-04-13 | Simvastatin 10 MG Oral Tablet | status active | reason: Hyperlipidemia (disorder) | RxNorm 314231

<details><summary>Everything the model saw (43 cards)</summary>

```text
[Condition/7280f7f8-315d-7c6a-5183-1fc53612d856] Condition | onset 2026-04-12 | Alzheimer's disease (disorder) | clinical status active | SNOMED 26929004
[Condition/7280f7f8-315d-7c6a-069f-25fdb34e3e53] Condition | onset 2025-04-06 | Stress (finding) | clinical status active | SNOMED 73595000
[Condition/7280f7f8-315d-7c6a-06ae-a26712c6cfb7] Condition | onset 2024-03-31 | Full-time employment (finding) | clinical status active | SNOMED 160903007
[Condition/7280f7f8-315d-7c6a-84b2-d6045a9b8deb] Condition | onset 2018-11-12 | Abnormal findings diagnostic imaging heart+coronary circulat (finding) | clinical status active | SNOMED 274531002
[Condition/7280f7f8-315d-7c6a-60b8-1b2b3b190d66] Condition | onset 2018-11-04 | Ischemic heart disease (disorder) | clinical status active | SNOMED 414545008
[Condition/7280f7f8-315d-7c6a-eee1-33d3eda16b26] Condition | onset 2014-02-16 | Chronic low back pain (finding) | clinical status active | SNOMED 278860009
[Condition/7280f7f8-315d-7c6a-23b9-2a24d0c43093] Condition | onset 2014-02-16 | Chronic neck pain (finding) | clinical status active | SNOMED 1121000119107
[Condition/7280f7f8-315d-7c6a-f371-666500850eb4] Condition | onset 2014-02-02 | Gingivitis (disorder) | clinical status active | SNOMED 66383009
[Condition/7280f7f8-315d-7c6a-b5ea-aa0955ebc2c7] Condition | onset 2010-01-10 | Hyperlipidemia (disorder) | clinical status active | SNOMED 55822004
[Condition/7280f7f8-315d-7c6a-929f-e845c91bba18] Condition | onset 1993-02-06 | Dependent drug abuse (disorder) | clinical status active | SNOMED 6525002
[Condition/7280f7f8-315d-7c6a-6159-244929402415] Condition | onset 1991-07-09 | Chronic pain (finding) | clinical status active | SNOMED 82423001
[Condition/7280f7f8-315d-7c6a-7561-551dd4fb980c] Condition | onset 1990-11-11 | Has a criminal record (finding) | clinical status active | SNOMED 266948004
[Condition/7280f7f8-315d-7c6a-69cb-9f6bde195716] Condition | onset 1990-10-25 | Impacted molars (disorder) | clinical status active | SNOMED 196416002
[Condition/7280f7f8-315d-7c6a-e183-7fc41f06abde] Condition | onset 1990-02-06 | Chronic intractable migraine without aura (disorder) | clinical status active | SNOMED 124171000119105
[Condition/7280f7f8-315d-7c6a-57cd-16215a141add] Condition | onset 1988-11-06 | Body mass index 30+ - obesity (finding) | clinical status active | SNOMED 162864005
[Condition/7280f7f8-315d-7c6a-7c25-7a247f43e721] Condition | onset 1981-01-18 | Anemia (disorder) | clinical status active | SNOMED 271737000
[Condition/7280f7f8-315d-7c6a-50ac-70390520f5d8] Condition | onset 1981-01-18 | Prediabetes (finding) | clinical status active | SNOMED 714628002
[Condition/7280f7f8-315d-7c6a-a35c-5f2c4404e1cd] Condition | onset 1971-02-18 | Chronic sinusitis (disorder) | clinical status active | SNOMED 40055000
[Condition/7280f7f8-315d-7c6a-cf3c-1559c1e270a8] Condition | onset 1964-12-20 | Housing unsatisfactory (finding) | clinical status active | SNOMED 105531004
[Condition/7280f7f8-315d-7c6a-3735-89103641aea2] Condition | onset 1964-12-20 | Only received primary school education (finding) | clinical status active | SNOMED 224295006
[MedicationRequest/7280f7f8-315d-7c6a-d103-5f5cf25ace53] MedicationRequest | prescribed 2026-04-13 | Simvastatin 10 MG Oral Tablet | status active | reason: Hyperlipidemia (disorder) | RxNorm 314231
[MedicationRequest/7280f7f8-315d-7c6a-dd3c-435b565b36d4] MedicationRequest | prescribed 2026-04-12 | Ibuprofen 400 MG Oral Tablet [Ibu] | status active | RxNorm 206905
[MedicationRequest/7280f7f8-315d-7c6a-698d-8c3f4a330263] MedicationRequest | prescribed 2026-04-12 | Acetaminophen 325 MG / Oxycodone Hydrochloride 10 MG Oral Tablet [Percocet] | status active | RxNorm 1049625
[MedicationRequest/7280f7f8-315d-7c6a-53dc-677516ba315e] MedicationRequest | prescribed 2026-04-12 | Galantamine 4 MG Oral Tablet | status active | reason: Alzheimer's disease (disorder) | RxNorm 310436
[MedicationRequest/7280f7f8-315d-7c6a-21fd-127361ce4eae] MedicationRequest | prescribed 2026-04-12 | Acetaminophen 325 MG Oral Tablet [Tylenol] | status active | RxNorm 209387
[MedicationRequest/7280f7f8-315d-7c6a-e1ca-6672a64e96d6] MedicationRequest | prescribed 2018-11-11 | Simvastatin 20 MG Oral Tablet | status active | RxNorm 312961
[MedicationRequest/7280f7f8-315d-7c6a-d3dc-bf227b26b9de] MedicationRequest | prescribed 2018-11-11 | Nitroglycerin 0.4 MG/ACTUAT Mucosal Spray | status active | RxNorm 705129
[MedicationRequest/7280f7f8-315d-7c6a-40f0-094ac0d35606] MedicationRequest | prescribed 2018-11-11 | Clopidogrel 75 MG Oral Tablet | status active | RxNorm 309362
[MedicationRequest/7280f7f8-315d-7c6a-344e-7b21fe48818f] MedicationRequest | prescribed 2018-11-11 | 24 HR metoprolol succinate 100 MG Extended Release Oral Tablet | status active | RxNorm 866412
[Encounter/7280f7f8-315d-7c6a-ddbc-56619e72a429] Encounter | 2026-04-26 | Encounter for check up (procedure) | class AMB | at LAWRENCE GENERAL HOSPITAL
[Encounter/7280f7f8-315d-7c6a-e49f-7858d34e1916] Encounter | 2026-04-13 | Follow-up encounter (procedure) | class AMB | reason: Hyperlipidemia (disorder) | at LAWRENCE GENERAL HOSPITAL
[Encounter/7280f7f8-315d-7c6a-79c7-b2135168eae6] Encounter | 2026-04-12 | General examination of patient (procedure) | class AMB | at HOLY FAMILY MEDICAL SPECIALTY PRACTICE PLLC
[Immunization/7280f7f8-315d-7c6a-89f5-f28321d6dbe8] Immunization | 2026-04-12 | Influenza, split virus, trivalent, PF | status completed | CVX 140
[MedicationRequest/7280f7f8-315d-7c6a-bff4-e18d95f7f79b] MedicationRequest | prescribed 2021-03-14 | Acetaminophen 325 MG Oral Tablet [Tylenol] | status completed | RxNorm 209387
[MedicationRequest/7280f7f8-315d-7c6a-bbcd-ae9102946cec] MedicationRequest | prescribed 2025-04-06 | Acetaminophen 325 MG Oral Tablet [Tylenol] | status completed | RxNorm 209387
[MedicationRequest/7280f7f8-315d-7c6a-4c3e-27b79818327b] MedicationRequest | prescribed 2024-11-24 | Acetaminophen 325 MG Oral Tablet [Tylenol] | status completed | RxNorm 209387
[MedicationRequest/7280f7f8-315d-7c6a-1656-a49c2a84baae] MedicationRequest | prescribed 2021-03-14 | Ibuprofen 400 MG Oral Tablet [Ibu] | status completed | RxNorm 206905
[MedicationRequest/7280f7f8-315d-7c6a-9203-04a436d5611e] MedicationRequest | prescribed 2025-04-06 | Ibuprofen 400 MG Oral Tablet [Ibu] | status completed | RxNorm 206905
[MedicationRequest/7280f7f8-315d-7c6a-12d1-81b620daaf62] MedicationRequest | prescribed 2024-11-24 | Ibuprofen 400 MG Oral Tablet [Ibu] | status completed | RxNorm 206905
[DocumentReference/750cb41b-d9ad-3c1d-b6d7-fadb5db1236e#1] Clinical note | 2010-01-31 | part 1 of 1 | 2010-01-31 # Chief Complaint - Memory Loss - Decreased in Judgement # History of Present Illness Neil122 is a 63 year-old nonhispanic white male. Patient has a history of victim of intimate partner abuse (finding). # Social History Patient is married. Patient has a documented history of opioid addiction. Patient has never smoked. Patient identifies as heterosexual. Patient comes from a low socioeconomic background. Patient did not finish high school. Patient currently has Cigna Health. # Allergies No Known Allergies. # Medications No Active Medications. # Assessment and Plan ## Plan The patient was prescribed the following medications: - simvastatin 10 mg oral tablet The patient was placed on a careplan: - hyperlipidemia clinical management plan (record artifact)
[DocumentReference/ae41b370-e3ce-e406-ac51-c30e28d61121#2] Clinical note | 2018-02-25 | part 2 of 2 | # Assessment and Plan Patient is presenting with medication review due (situation). ## Plan Patient was given the following immunizations: influenza, split virus, trivalent, pf, td (adult), 5 lf tetanus toxoid, preservative free, adsorbed. The following procedures were conducted: - medication reconciliation (procedure) - assessment of health and social care needs (procedure) - assessment of anxiety (procedure) - assessment using morse fall scale (procedure) - depression screening (procedure) - depression screening (procedure) - patient referral for dental care (procedure) The following lab reports were completed: - basic metabolic panel - blood - lipid panel with direct ldl - serum or plasma - generalized anxiety disorder 7 item (gad-7) - morse fall scale panel - patient health questionnaire 2 item (phq-2) [reported] The patient was prescribed the following medications: - acetaminophen 325 mg / oxycodone hydrochloride 10 mg oral tablet [percocet] - acetaminophen 325 mg oral tablet [tylenol] - ibuprofen 400 mg oral tablet [ibu]
[DocumentReference/6b0d0857-4700-f6ee-c3e4-f8d7c3eb1f27#2] Clinical note | 2026-04-13 | part 2 of 2 | # Assessment and Plan ## Plan The following lab reports were completed: - comprehensive metabolic 2000 panel - serum or plasma - lipid panel with direct ldl - serum or plasma The patient was prescribed the following medications: - simvastatin 10 mg oral tablet
[DocumentReference/d33f5325-2f82-5aa9-5d4d-a95b2ba279e4#2] Clinical note | 2017-02-19 | part 2 of 2 | # Assessment and Plan Patient is presenting with full-time employment (finding). ## Plan Patient was given the following immunizations: influenza, split virus, trivalent, pf. The following procedures were conducted: - medication reconciliation (procedure) - assessment of health and social care needs (procedure) - assessment of anxiety (procedure) - screening for domestic abuse (procedure) - depression screening (procedure) - depression screening (procedure) - patient referral for dental care (procedure) The following lab reports were completed: - basic metabolic panel - blood - generalized anxiety disorder 7 item (gad-7) - humiliation, afraid, rape, and kick questionnaire [hark] - patient health questionnaire 2 item (phq-2) [reported] The patient was prescribed the following medications: - acetaminophen 325 mg / oxycodone hydrochloride 10 mg oral tablet [percocet] - acetaminophen 325 mg oral tablet [tylenol] - ibuprofen 400 mg oral tablet [ibu]
```

</details>

label: s
note: Cited cards show Simvastatin 20 MG prescribed 2018-11-11 status active and Simvastatin 10 MG prescribed 2026-04-13 status active; these are the only simvastatin MedicationRequests seen, so 'two' is correct.

## 4. `current-meds:8d945e28#0#0`

Question: What medications is the patient currently prescribed?

Answer: **The patient's active prescriptions are Humulin (insulin isophane, human 70 UNT/ML / insulin, regular, human 30 UNT/ML Injectable Suspension), prescribed 2026-09-07 for prediabetes, and Hydrochlorothiazide 25 MG Oral Tablet, prescribed 2026-09-07 for essential hypertension.** Vitamin B12 5 MG/ML Injectable Solution, prescribed 1981-07-27, is also active. Clinical notes through 2026-01-19 also list epoetin alfa 4000 unt/ml injection [epogen], acetaminophen, acetaminophen/oxycodone, ibuprofen and naproxen sodium among the medications, but these notes do not state an active status.

Cards this sentence cites:

- `[MedicationRequest/8d945e28-1d8a-bd72-ff5c-41daf21d65a9]` MedicationRequest | prescribed 2026-09-07 | insulin isophane, human 70 UNT/ML / insulin, regular, human 30 UNT/ML Injectable Suspension [Humulin] | status active | reason: Prediabetes (finding) | RxNorm 106892
- `[MedicationRequest/8d945e28-1d8a-bd72-d409-38c0124f2c47]` MedicationRequest | prescribed 2026-09-07 | Hydrochlorothiazide 25 MG Oral Tablet | status active | reason: Essential hypertension (disorder) | RxNorm 310798

<details><summary>Everything the model saw (39 cards)</summary>

```text
[Condition/8d945e28-1d8a-bd72-9d6c-259e17157c55] Condition | onset 2026-09-07 | Full-time employment (finding) | clinical status active | SNOMED 160903007
[Condition/8d945e28-1d8a-bd72-3102-64b703ba601c] Condition | onset 2026-07-13 | Medication review due (situation) | clinical status active | SNOMED 314529007
[Condition/8d945e28-1d8a-bd72-6b51-0718e8cd7a5e] Condition | onset 2021-01-01 | Awaiting transplantation of kidney (situation) | clinical status active | SNOMED 698306007
[Condition/8d945e28-1d8a-bd72-db4c-2552d073039a] Condition | onset 2020-11-09 | Chronic kidney disease stage 4 (disorder) | clinical status active | SNOMED 431857002
[Condition/8d945e28-1d8a-bd72-ed26-25aa62be033c] Condition | onset 2020-08-18 | Dependent drug abuse (disorder) | clinical status active | SNOMED 6525002
[Condition/8d945e28-1d8a-bd72-05bf-4b4b02b03fe9] Condition | onset 2018-01-22 | Has a criminal record (finding) | clinical status active | SNOMED 266948004
[Condition/8d945e28-1d8a-bd72-38fb-c4bf927332c6] Condition | onset 2013-09-16 | Proteinuria due to type 2 diabetes mellitus (disorder) | clinical status active | SNOMED 157141000119108
[Condition/8d945e28-1d8a-bd72-1379-82140e2d1648] Condition | onset 2013-09-16 | Chronic kidney disease stage 3 (disorder) | clinical status active | SNOMED 433144002
[Condition/8d945e28-1d8a-bd72-cd47-b95fb1e4464b] Condition | onset 2009-07-06 | Microalbuminuria due to type 2 diabetes mellitus (disorder) | clinical status active | SNOMED 90781000119102
[Condition/8d945e28-1d8a-bd72-be1a-fb710d842e34] Condition | onset 2009-07-06 | Chronic kidney disease stage 2 (disorder) | clinical status active | SNOMED 431856006
[Condition/8d945e28-1d8a-bd72-2a55-0f3c986db8dd] Condition | onset 2009-07-06 | Gingivitis (disorder) | clinical status active | SNOMED 66383009
[Condition/8d945e28-1d8a-bd72-4277-241d976b7354] Condition | onset 2007-06-25 | Metabolic syndrome X (disorder) | clinical status active | SNOMED 237602007
[Condition/8d945e28-1d8a-bd72-e0ac-a99a0168ad8a] Condition | onset 2004-06-07 | Disorder of kidney due to diabetes mellitus (disorder) | clinical status active | SNOMED 127013003
[Condition/8d945e28-1d8a-bd72-a508-e7d1553f7f62] Condition | onset 2004-06-07 | Chronic kidney disease stage 1 (disorder) | clinical status active | SNOMED 431855005
[Condition/8d945e28-1d8a-bd72-2622-8fe0a1a30909] Condition | onset 2003-06-02 | Essential hypertension (disorder) | clinical status active | SNOMED 59621000
[Condition/8d945e28-1d8a-bd72-12e3-17db162c8f0b] Condition | onset 2001-06-04 | Obstructive sleep apnea syndrome (disorder) | clinical status active | SNOMED 78275009
[Condition/8d945e28-1d8a-bd72-d01e-086bb9d1d22f] Condition | onset 2001-05-07 | Sleep disorder (disorder) | clinical status active | SNOMED 39898005
[Condition/8d945e28-1d8a-bd72-f5fa-42692b5be159] Condition | onset 1996-08-05 | Body mass index 30+ - obesity (finding) | clinical status active | SNOMED 162864005
[Condition/8d945e28-1d8a-bd72-e601-8e5493910aec] Condition | onset 1981-07-20 | Prediabetes (finding) | clinical status active | SNOMED 714628002
[Condition/8d945e28-1d8a-bd72-52ca-256d6584412c] Condition | onset 1981-07-20 | Anemia (disorder) | clinical status active | SNOMED 271737000
[Condition/8d945e28-1d8a-bd72-d644-66738e889d91] Condition | onset 1977-07-11 | Received higher education (finding) | clinical status active | SNOMED 224299000
[Condition/8d945e28-1d8a-bd72-fbf9-3e6f6bd97f57] Condition | onset 1977-03-07 | Risk activity involvement (finding) | clinical status active | SNOMED 160968000
[MedicationRequest/8d945e28-1d8a-bd72-ff5c-41daf21d65a9] MedicationRequest | prescribed 2026-09-07 | insulin isophane, human 70 UNT/ML / insulin, regular, human 30 UNT/ML Injectable Suspension [Humulin] | status active | reason: Prediabetes (finding) | RxNorm 106892
[MedicationRequest/8d945e28-1d8a-bd72-d409-38c0124f2c47] MedicationRequest | prescribed 2026-09-07 | Hydrochlorothiazide 25 MG Oral Tablet | status active | reason: Essential hypertension (disorder) | RxNorm 310798
[MedicationRequest/8d945e28-1d8a-bd72-bcd6-3304c42dca58] MedicationRequest | prescribed 1981-07-27 | Vitamin B12 5 MG/ML Injectable Solution | status active | RxNorm 2001499
[Encounter/8d945e28-1d8a-bd72-016c-9af67d7199fd] Encounter | 2026-09-27 | Encounter for problem (procedure) | class AMB | reason: Chronic kidney disease stage 4 (disorder) | at NEW ENGLAND REHABILITATION SERVICES OF CENTRAL MASSACHUSETTS INC
[Encounter/8d945e28-1d8a-bd72-3f01-7946bd8f2be1] Encounter | 2026-09-26 | Encounter for problem (procedure) | class AMB | reason: Chronic kidney disease stage 4 (disorder) | at NEW ENGLAND REHABILITATION SERVICES OF CENTRAL MASSACHUSETTS INC
[Encounter/8d945e28-1d8a-bd72-9dbd-785d1f0e4915] Encounter | 2026-09-23 | Encounter for problem (procedure) | class AMB | reason: Chronic kidney disease stage 4 (disorder) | at NEW ENGLAND REHABILITATION SERVICES OF CENTRAL MASSACHUSETTS INC
[Immunization/8d945e28-1d8a-bd72-6a94-32775be2d4e6] Immunization | 2026-01-12 | Influenza, split virus, trivalent, PF | status completed | CVX 140
[DocumentReference/198dc0c0-ac2a-f381-c815-204a8135294a#2] Clinical note | 2025-12-19 | part 2 of 2 | # Medications 1 ml epoetin alfa 4000 unt/ml injection [epogen]; acetaminophen 325 mg oral tablet; hydrochlorothiazide 25 mg oral tablet; acetaminophen 325 mg / oxycodone hydrochloride 5 mg oral tablet; insulin isophane, human 70 unt/ml / insulin, regular, human 30 unt/ml injectable suspension [humulin]; ibuprofen 200 mg oral tablet; naproxen sodium 220 mg oral tablet # Assessment and Plan ## Plan The following procedures were conducted: - renal dialysis (procedure) The patient was prescribed the following medications: - 1 ml epoetin alfa 4000 unt/ml injection [epogen]
[DocumentReference/ed2accc3-f181-6c76-019e-602100408021#1] Clinical note | 1981-07-27 | part 1 of 1 | 1981-07-27 # Chief Complaint - Thirst - Fatigue - Hunger # History of Present Illness Tien590 Marcela739 is a 22 year-old nonhispanic white female. # Social History Patient is married. Patient has a documented history of opioid addiction. Patient has never smoked. Patient identifies as heterosexual. Patient comes from a middle socioeconomic background. Patient has completed some college courses. Patient currently has Cigna Health. # Allergies No Known Allergies. # Medications No Active Medications. # Assessment and Plan ## Plan The patient was prescribed the following medications: - vitamin b12 5 mg/ml injectable solution
[DocumentReference/46621701-ca2a-cb98-5521-2aabde9e5ef5#1] Clinical note | 2016-08-15 | part 1 of 1 | 2016-08-15 # Chief Complaint - Thirst - Fatigue - Hunger # History of Present Illness Tien590 Marcela739 is a 57 year-old nonhispanic white female. Patient has a history of acute apical periodontitis of pulpal origin, medication review due (situation), chronic periodontitis, generalized, full-time employment (finding), victim of intimate partner abuse (finding), stress (finding). # Social History Patient is married. Patient has a documented history of opioid addiction. Patient has never smoked. Patient identifies as heterosexual. Patient comes from a middle socioeconomic background. Patient has completed some college courses. Patient currently has Medicare. # Allergies No Known Allergies. # Medications No Active Medications. # Assessment and Plan ## Plan The patient was prescribed the following medications: - insulin isophane, human 70 unt/ml / insulin, regular, human 30 unt/ml injectable suspension [humulin] - hydrochlorothiazide 25 mg oral tablet
[DocumentReference/80a3c86e-df5b-b958-28f5-96bc5396b5a7#2] Clinical note | 2024-12-19 | part 2 of 2 | # Medications 1 ml epoetin alfa 4000 unt/ml injection [epogen]; acetaminophen 325 mg oral tablet; hydrochlorothiazide 25 mg oral tablet; acetaminophen 325 mg / oxycodone hydrochloride 5 mg oral tablet; insulin isophane, human 70 unt/ml / insulin, regular, human 30 unt/ml injectable suspension [humulin]; ibuprofen 200 mg oral tablet; naproxen sodium 220 mg oral tablet # Assessment and Plan ## Plan The following procedures were conducted: - renal dialysis (procedure) The patient was prescribed the following medications: - 1 ml epoetin alfa 4000 unt/ml injection [epogen]
[DocumentReference/0404ad4f-552b-33c0-8dd9-b7851ed9bb1f#2] Clinical note | 2024-09-19 | part 2 of 2 | # Medications 1 ml epoetin alfa 4000 unt/ml injection [epogen]; acetaminophen 325 mg oral tablet; hydrochlorothiazide 25 mg oral tablet; acetaminophen 325 mg / oxycodone hydrochloride 5 mg oral tablet; insulin isophane, human 70 unt/ml / insulin, regular, human 30 unt/ml injectable suspension [humulin]; ibuprofen 200 mg oral tablet; naproxen sodium 220 mg oral tablet # Assessment and Plan ## Plan The following procedures were conducted: - renal dialysis (procedure) The patient was prescribed the following medications: - 1 ml epoetin alfa 4000 unt/ml injection [epogen]
[DocumentReference/f4d1a4ab-164b-5c81-a496-8f30333033c5#2] Clinical note | 2021-05-16 | part 2 of 2 | # Assessment and Plan ## Plan The following procedures were conducted: - renal dialysis (procedure) The patient was prescribed the following medications: - 1 ml epoetin alfa 4000 unt/ml injection [epogen]
[DocumentReference/722b463c-e306-97a2-0f7b-e9997def0d9b#2] Clinical note | 2026-01-19 | part 2 of 2 | # Medications 1 ml epoetin alfa 4000 unt/ml injection [epogen]; acetaminophen 325 mg oral tablet; hydrochlorothiazide 25 mg oral tablet; acetaminophen 325 mg / oxycodone hydrochloride 5 mg oral tablet; insulin isophane, human 70 unt/ml / insulin, regular, human 30 unt/ml injectable suspension [humulin]; ibuprofen 200 mg oral tablet; naproxen sodium 220 mg oral tablet # Assessment and Plan ## Plan The following procedures were conducted: - renal dialysis (procedure) The patient was prescribed the following medications: - 1 ml epoetin alfa 4000 unt/ml injection [epogen]
[DocumentReference/90a6e575-11cc-9dfb-2b8f-5b6daf1d4158#2] Clinical note | 2021-05-13 | part 2 of 2 | # Assessment and Plan ## Plan The following procedures were conducted: - renal dialysis (procedure) The patient was prescribed the following medications: - 1 ml epoetin alfa 4000 unt/ml injection [epogen]
[DocumentReference/9dcc0331-09a7-627c-75ae-78739719ce1e#2] Clinical note | 2025-12-16 | part 2 of 2 | # Medications 1 ml epoetin alfa 4000 unt/ml injection [epogen]; acetaminophen 325 mg oral tablet; hydrochlorothiazide 25 mg oral tablet; acetaminophen 325 mg / oxycodone hydrochloride 5 mg oral tablet; insulin isophane, human 70 unt/ml / insulin, regular, human 30 unt/ml injectable suspension [humulin]; ibuprofen 200 mg oral tablet; naproxen sodium 220 mg oral tablet # Assessment and Plan ## Plan The following procedures were conducted: - renal dialysis (procedure) The patient was prescribed the following medications: - 1 ml epoetin alfa 4000 unt/ml injection [epogen]
[DocumentReference/af9a9175-6ec4-7dfb-4a83-076e0c152158#2] Clinical note | 2021-04-25 | part 2 of 2 | # Assessment and Plan ## Plan The following procedures were conducted: - renal dialysis (procedure) The patient was prescribed the following medications: - 1 ml epoetin alfa 4000 unt/ml injection [epogen]
```

</details>

label: s?
note: Both cited cards match (Humulin 2026-09-07 active, reason Prediabetes; HCTZ 25 MG 2026-09-07 active, reason Essential hypertension). Read alone the sentence sounds like the complete active list, which misses the active Vitamin B12, but the next sentence adds it as 'also active', so the full answer is complete.

## 5. `current-meds:ef5e136c#0#1`

Question: What medications is the patient currently prescribed?

Answer: The patient has six active medication prescriptions, all prescribed 2026-09-30: hydrochlorothiazide 25 MG Oral Tablet, lisinopril 10 MG Oral Tablet, and amLODIPine 2.5 MG Oral Tablet (each for essential hypertension); insulin isophane, human 70 UNT/ML / insulin, regular, human 30 UNT/ML Injectable Suspension [Humulin] (for type 2 diabetes mellitus); 120 ACTUAT fluticasone propionate 0.044 MG/ACTUAT Metered Dose Inhaler [Flovent]; and albuterol 0.83 MG/ML Inhalation Solution. **The 2026-09-30 clinical note's plan lists the same six medications as prescribed.**

Cards this sentence cites:

- `[DocumentReference/55bd2590-6cf6-db02-b7d1-6322cd131a2f#2]` Clinical note | 2026-09-30 | part 2 of 2 | # Social History Patient is single. Patient has never smoked. Patient identifies as heterosexual. Patient comes from a high socioeconomic background. Patient is a college graduate. Patient currently has Medicare. # Allergies No Known Allergies. # Medications lisinopril 10 mg oral tablet; tropicamide 5 mg/ml ophthalmic solution; 1 ml epoetin alfa 4000 unt/ml injection [epogen]; hydrochlorothiazide 25 mg oral tablet; amoxicillin 250 mg oral capsule; acetaminophen 325 mg / oxycodone hydrochloride 5 mg oral tablet; 120 actuat fluticasone propionate 0.044 mg/actuat metered dose inhaler [flovent]; amlodipine 2.5 mg oral tablet; insulin isophane, human 70 unt/ml / insulin, regular, human 30 unt/ml injectable suspension [humulin]; albuterol 0.83 mg/ml inhalation solution; naproxen sodium 220 mg oral tablet # Assessment and Plan Patient is presenting with medication review due (situation). ## Plan The patient was prescribed the following medications: - insulin isophane, human 70 unt/ml / insulin, regular, human 30 unt/ml injectable suspension [humulin] - hydrochlorothiazide 25 mg oral tablet - 120 actuat fluticasone propionate 0.044 mg/actuat metered dose inhaler [flovent] - lisinopril 10 mg oral tablet - amlodipine 2.5 mg oral tablet - albuterol 0.83 mg/ml inhalation solution

<details><summary>Everything the model saw (47 cards)</summary>

```text
[Condition/ef5e136c-ff1e-0695-1f8c-935a12106cac] Condition | onset 2026-09-30 | Medication review due (situation) | clinical status active | SNOMED 314529007
[Condition/ef5e136c-ff1e-0695-7e5d-470b95f60db2] Condition | onset 2026-09-23 | Social isolation (finding) | clinical status active | SNOMED 422650009
[Condition/ef5e136c-ff1e-0695-9d2d-c4be459bc9f4] Condition | onset 2026-09-09 | Unemployed (finding) | clinical status active | SNOMED 73438004
[Condition/ef5e136c-ff1e-0695-7b9c-f43e5ca3f6c6] Condition | onset 2026-08-12 | Stress (finding) | clinical status active | SNOMED 73595000
[Condition/ef5e136c-ff1e-0695-aa04-94486c99258f] Condition | onset 2025-08-27 | End-stage renal disease (disorder) | clinical status active | SNOMED 46177005
[Condition/ef5e136c-ff1e-0695-423f-ed71d76e81e3] Condition | onset 2025-03-30 | Awaiting transplantation of kidney (situation) | clinical status active | SNOMED 698306007
[Condition/ef5e136c-ff1e-0695-71df-3a96389b0a39] Condition | onset 2025-02-05 | Chronic kidney disease stage 4 (disorder) | clinical status active | SNOMED 431857002
[Condition/ef5e136c-ff1e-0695-5331-2d63eb213c34] Condition | onset 2024-05-15 | Proteinuria due to type 2 diabetes mellitus (disorder) | clinical status active | SNOMED 157141000119108
[Condition/ef5e136c-ff1e-0695-3834-fa6cb282a475] Condition | onset 2024-05-15 | Chronic kidney disease stage 3 (disorder) | clinical status active | SNOMED 433144002
[Condition/ef5e136c-ff1e-0695-68fe-9e2010333061] Condition | onset 2023-08-16 | Microalbuminuria due to type 2 diabetes mellitus (disorder) | clinical status active | SNOMED 90781000119102
[Condition/ef5e136c-ff1e-0695-65f5-8d04f278a661] Condition | onset 2023-08-16 | Chronic kidney disease stage 2 (disorder) | clinical status active | SNOMED 431856006
[Condition/ef5e136c-ff1e-0695-aac2-46a0ff462178] Condition | onset 2023-04-19 | Gingivitis (disorder) | clinical status active | SNOMED 66383009
[Condition/ef5e136c-ff1e-0695-fda2-40e12f6b17a7] Condition | onset 2017-11-15 | Chronic kidney disease stage 1 (disorder) | clinical status active | SNOMED 431855005
[Condition/ef5e136c-ff1e-0695-bf3f-30946ad3f8b4] Condition | onset 2017-11-15 | Disorder of kidney due to diabetes mellitus (disorder) | clinical status active | SNOMED 127013003
[Condition/ef5e136c-ff1e-0695-eac4-d545a0296998] Condition | onset 2011-07-27 | Essential hypertension (disorder) | clinical status active | SNOMED 59621000
[Condition/ef5e136c-ff1e-0695-b228-2f5ff5bb47cb] Condition | onset 2010-05-19 | Metabolic syndrome X (disorder) | clinical status active | SNOMED 237602007
[Condition/ef5e136c-ff1e-0695-af16-82f03f777ba8] Condition | onset 2010-05-19 | Hypertriglyceridemia (disorder) | clinical status active | SNOMED 302870006
[Condition/ef5e136c-ff1e-0695-5ca5-51bfdc51320e] Condition | onset 2010-05-12 | Diabetes mellitus type 2 (disorder) | clinical status active | SNOMED 44054006
[Condition/ef5e136c-ff1e-0695-f7ec-ceae0c2566bc] Condition | onset 2004-06-16 | Body mass index 30+ - obesity (finding) | clinical status active | SNOMED 162864005
[Condition/ef5e136c-ff1e-0695-c94a-5d81ddd88117] Condition | onset 1997-05-07 | Has a criminal record (finding) | clinical status active | SNOMED 266948004
[Condition/ef5e136c-ff1e-0695-6efc-9f7d5e6b04ef] Condition | onset 1993-09-01 | Anemia (disorder) | clinical status active | SNOMED 271737000
[Condition/ef5e136c-ff1e-0695-1f68-dac24351dbaa] Condition | onset 1993-04-14 | Prediabetes (finding) | clinical status active | SNOMED 714628002
[Condition/ef5e136c-ff1e-0695-2d8d-328849698529] Condition | onset 1993-01-22 | History of tubal ligation (situation) | clinical status active | SNOMED 267020005
[Condition/ef5e136c-ff1e-0695-0825-c31e8b252683] Condition | onset 1983-11-14 | Past pregnancy history of miscarriage (situation) | clinical status active | SNOMED 161744009
[Condition/ef5e136c-ff1e-0695-cb16-3a98eeb2de7a] Condition | onset 1976-01-07 | Received higher education (finding) | clinical status active | SNOMED 224299000
[Condition/ef5e136c-ff1e-0695-3278-6a86eaf1fb5d] Condition | onset 1975-06-27 | Chronic sinusitis (disorder) | clinical status active | SNOMED 40055000
[Condition/ef5e136c-ff1e-0695-337f-d12087c8dbb5] Condition | onset 1975-01-01 | Risk activity involvement (finding) | clinical status active | SNOMED 160968000
[MedicationRequest/ef5e136c-ff1e-0695-ffec-2ea7ac772a27] MedicationRequest | prescribed 2026-09-30 | Hydrochlorothiazide 25 MG Oral Tablet | status active | reason: Essential hypertension (disorder) | RxNorm 310798
[MedicationRequest/ef5e136c-ff1e-0695-b3ba-a1ec7bcfb9f4] MedicationRequest | prescribed 2026-09-30 | albuterol 0.83 MG/ML Inhalation Solution | status active | RxNorm 630208
[MedicationRequest/ef5e136c-ff1e-0695-901e-2e1f9afb0cca] MedicationRequest | prescribed 2026-09-30 | lisinopril 10 MG Oral Tablet | status active | reason: Essential hypertension (disorder) | RxNorm 314076
[MedicationRequest/ef5e136c-ff1e-0695-76a6-8eeb54f8a75e] MedicationRequest | prescribed 2026-09-30 | 120 ACTUAT fluticasone propionate 0.044 MG/ACTUAT Metered Dose Inhaler [Flovent] | status active | RxNorm 895996
[MedicationRequest/ef5e136c-ff1e-0695-6c6d-182c3b9c47c1] MedicationRequest | prescribed 2026-09-30 | amLODIPine 2.5 MG Oral Tablet | status active | reason: Essential hypertension (disorder) | RxNorm 308136
[MedicationRequest/ef5e136c-ff1e-0695-6804-cf31640a9491] MedicationRequest | prescribed 2026-09-30 | insulin isophane, human 70 UNT/ML / insulin, regular, human 30 UNT/ML Injectable Suspension [Humulin] | status active | reason: Diabetes mellitus type 2 (disorder) | RxNorm 106892
[Encounter/ef5e136c-ff1e-0695-08ba-2471a16a6570] Encounter | 2026-09-30 | Emergency room admission (procedure) | class EMER | at APPLE VALLEY CENTER
[Encounter/ef5e136c-ff1e-0695-aea4-11055569fd51] Encounter | 2026-09-23 | Urgent care clinic (environment) | class AMB | at URGENT HELP CHELMSFORD PC
[Encounter/ef5e136c-ff1e-0695-4a41-6fca58c80cb7] Encounter | 2026-09-16 | Urgent care clinic (environment) | class AMB | at URGENT HELP CHELMSFORD PC
[Immunization/ef5e136c-ff1e-0695-6beb-93901776b619] Immunization | 2026-05-13 | Influenza, split virus, trivalent, PF | status completed | CVX 140
[DocumentReference/4d0d0889-f360-8c5c-b81d-aa7686616e55#2] Clinical note | 2016-10-19 | part 2 of 2 | # Assessment and Plan ## Plan The patient was prescribed the following medications: - hydrochlorothiazide 25 mg oral tablet - 120 actuat fluticasone propionate 0.044 mg/actuat metered dose inhaler [flovent] - lisinopril 10 mg oral tablet - amlodipine 2.5 mg oral tablet - albuterol 0.83 mg/ml inhalation solution
[DocumentReference/8d12e732-8cec-c2d2-a952-1494a12a5532#2] Clinical note | 2026-06-10 | part 2 of 2 | # Social History Patient is single. Patient has never smoked. Patient identifies as heterosexual. Patient comes from a high socioeconomic background. Patient is a college graduate. Patient currently has Medicare. # Allergies No Known Allergies. # Medications lisinopril 10 mg oral tablet; tropicamide 5 mg/ml ophthalmic solution; 1 ml epoetin alfa 4000 unt/ml injection [epogen]; hydrochlorothiazide 25 mg oral tablet; amoxicillin 250 mg oral capsule; acetaminophen 325 mg / oxycodone hydrochloride 5 mg oral tablet; 120 actuat fluticasone propionate 0.044 mg/actuat metered dose inhaler [flovent]; amlodipine 2.5 mg oral tablet; insulin isophane, human 70 unt/ml / insulin, regular, human 30 unt/ml injectable suspension [humulin]; albuterol 0.83 mg/ml inhalation solution; naproxen sodium 220 mg oral tablet # Assessment and Plan Patient is presenting with medication review due (situation). ## Plan The patient was prescribed the following medications: - insulin isophane, human 70 unt/ml / insulin, regular, human 30 unt/ml injectable suspension [humulin] - hydrochlorothiazide 25 mg oral tablet - 120 actuat fluticasone propionate 0.044 mg/actuat metered dose inhaler [flovent] - lisinopril 10 mg oral tablet - amlodipine 2.5 mg oral tablet - albuterol 0.83 mg/ml inhalation solution
[DocumentReference/1e45e0e7-f85b-c7ac-e99e-65f75cf3cebb#2] Clinical note | 2026-06-24 | part 2 of 2 | # Social History Patient is single. Patient has never smoked. Patient identifies as heterosexual. Patient comes from a high socioeconomic background. Patient is a college graduate. Patient currently has Medicare. # Allergies No Known Allergies. # Medications lisinopril 10 mg oral tablet; tropicamide 5 mg/ml ophthalmic solution; 1 ml epoetin alfa 4000 unt/ml injection [epogen]; hydrochlorothiazide 25 mg oral tablet; amoxicillin 250 mg oral capsule; acetaminophen 325 mg / oxycodone hydrochloride 5 mg oral tablet; 120 actuat fluticasone propionate 0.044 mg/actuat metered dose inhaler [flovent]; amlodipine 2.5 mg oral tablet; insulin isophane, human 70 unt/ml / insulin, regular, human 30 unt/ml injectable suspension [humulin]; albuterol 0.83 mg/ml inhalation solution; naproxen sodium 220 mg oral tablet # Assessment and Plan Patient is presenting with medication review due (situation). ## Plan The patient was prescribed the following medications: - insulin isophane, human 70 unt/ml / insulin, regular, human 30 unt/ml injectable suspension [humulin] - hydrochlorothiazide 25 mg oral tablet - 120 actuat fluticasone propionate 0.044 mg/actuat metered dose inhaler [flovent] - lisinopril 10 mg oral tablet - amlodipine 2.5 mg oral tablet - albuterol 0.83 mg/ml inhalation solution
[DocumentReference/55bd2590-6cf6-db02-b7d1-6322cd131a2f#2] Clinical note | 2026-09-30 | part 2 of 2 | # Social History Patient is single. Patient has never smoked. Patient identifies as heterosexual. Patient comes from a high socioeconomic background. Patient is a college graduate. Patient currently has Medicare. # Allergies No Known Allergies. # Medications lisinopril 10 mg oral tablet; tropicamide 5 mg/ml ophthalmic solution; 1 ml epoetin alfa 4000 unt/ml injection [epogen]; hydrochlorothiazide 25 mg oral tablet; amoxicillin 250 mg oral capsule; acetaminophen 325 mg / oxycodone hydrochloride 5 mg oral tablet; 120 actuat fluticasone propionate 0.044 mg/actuat metered dose inhaler [flovent]; amlodipine 2.5 mg oral tablet; insulin isophane, human 70 unt/ml / insulin, regular, human 30 unt/ml injectable suspension [humulin]; albuterol 0.83 mg/ml inhalation solution; naproxen sodium 220 mg oral tablet # Assessment and Plan Patient is presenting with medication review due (situation). ## Plan The patient was prescribed the following medications: - insulin isophane, human 70 unt/ml / insulin, regular, human 30 unt/ml injectable suspension [humulin] - hydrochlorothiazide 25 mg oral tablet - 120 actuat fluticasone propionate 0.044 mg/actuat metered dose inhaler [flovent] - lisinopril 10 mg oral tablet - amlodipine 2.5 mg oral tablet - albuterol 0.83 mg/ml inhalation solution
[DocumentReference/3a57cf52-e968-196f-5696-fcb4fda5abcf#2] Clinical note | 2025-12-10 | part 2 of 2 | # Social History Patient is single. Patient has never smoked. Patient identifies as heterosexual. Patient comes from a high socioeconomic background. Patient is a college graduate. Patient currently has Medicare. # Allergies No Known Allergies. # Medications lisinopril 10 mg oral tablet; tropicamide 5 mg/ml ophthalmic solution; 1 ml epoetin alfa 4000 unt/ml injection [epogen]; hydrochlorothiazide 25 mg oral tablet; amoxicillin 250 mg oral capsule; acetaminophen 325 mg / oxycodone hydrochloride 5 mg oral tablet; 120 actuat fluticasone propionate 0.044 mg/actuat metered dose inhaler [flovent]; amlodipine 2.5 mg oral tablet; insulin isophane, human 70 unt/ml / insulin, regular, human 30 unt/ml injectable suspension [humulin]; albuterol 0.83 mg/ml inhalation solution; naproxen sodium 220 mg oral tablet # Assessment and Plan Patient is presenting with medication review due (situation). ## Plan The patient was prescribed the following medications: - insulin isophane, human 70 unt/ml / insulin, regular, human 30 unt/ml injectable suspension [humulin] - hydrochlorothiazide 25 mg oral tablet - 120 actuat fluticasone propionate 0.044 mg/actuat metered dose inhaler [flovent] - lisinopril 10 mg oral tablet - amlodipine 2.5 mg oral tablet - albuterol 0.83 mg/ml inhalation solution
[DocumentReference/88f70ab4-f37e-aefe-89d9-041f04209b91#2] Clinical note | 2025-11-12 | part 2 of 2 | # Social History Patient is single. Patient has never smoked. Patient identifies as heterosexual. Patient comes from a high socioeconomic background. Patient is a college graduate. Patient currently has Medicare. # Allergies No Known Allergies. # Medications lisinopril 10 mg oral tablet; tropicamide 5 mg/ml ophthalmic solution; 1 ml epoetin alfa 4000 unt/ml injection [epogen]; hydrochlorothiazide 25 mg oral tablet; amoxicillin 250 mg oral capsule; acetaminophen 325 mg / oxycodone hydrochloride 5 mg oral tablet; 120 actuat fluticasone propionate 0.044 mg/actuat metered dose inhaler [flovent]; amlodipine 2.5 mg oral tablet; insulin isophane, human 70 unt/ml / insulin, regular, human 30 unt/ml injectable suspension [humulin]; albuterol 0.83 mg/ml inhalation solution; naproxen sodium 220 mg oral tablet # Assessment and Plan Patient is presenting with medication review due (situation). ## Plan The patient was prescribed the following medications: - insulin isophane, human 70 unt/ml / insulin, regular, human 30 unt/ml injectable suspension [humulin] - hydrochlorothiazide 25 mg oral tablet - 120 actuat fluticasone propionate 0.044 mg/actuat metered dose inhaler [flovent] - lisinopril 10 mg oral tablet - amlodipine 2.5 mg oral tablet - albuterol 0.83 mg/ml inhalation solution
[DocumentReference/12d16d0b-f49d-b245-c3db-8bd524abd1db#2] Clinical note | 2026-05-27 | part 2 of 2 | # Social History Patient is single. Patient has never smoked. Patient identifies as heterosexual. Patient comes from a high socioeconomic background. Patient is a college graduate. Patient currently has Medicare. # Allergies No Known Allergies. # Medications lisinopril 10 mg oral tablet; tropicamide 5 mg/ml ophthalmic solution; 1 ml epoetin alfa 4000 unt/ml injection [epogen]; hydrochlorothiazide 25 mg oral tablet; amoxicillin 250 mg oral capsule; acetaminophen 325 mg / oxycodone hydrochloride 5 mg oral tablet; 120 actuat fluticasone propionate 0.044 mg/actuat metered dose inhaler [flovent]; amlodipine 2.5 mg oral tablet; insulin isophane, human 70 unt/ml / insulin, regular, human 30 unt/ml injectable suspension [humulin]; albuterol 0.83 mg/ml inhalation solution; naproxen sodium 220 mg oral tablet # Assessment and Plan Patient is presenting with medication review due (situation). ## Plan The patient was prescribed the following medications: - insulin isophane, human 70 unt/ml / insulin, regular, human 30 unt/ml injectable suspension [humulin] - hydrochlorothiazide 25 mg oral tablet - 120 actuat fluticasone propionate 0.044 mg/actuat metered dose inhaler [flovent] - lisinopril 10 mg oral tablet - amlodipine 2.5 mg oral tablet - albuterol 0.83 mg/ml inhalation solution
[DocumentReference/bb47a9b7-15ec-a25f-04c8-1ab3cb74f356#2] Clinical note | 2026-04-29 | part 2 of 2 | # Social History Patient is single. Patient has never smoked. Patient identifies as heterosexual. Patient comes from a high socioeconomic background. Patient is a college graduate. Patient currently has Medicare. # Allergies No Known Allergies. # Medications lisinopril 10 mg oral tablet; tropicamide 5 mg/ml ophthalmic solution; 1 ml epoetin alfa 4000 unt/ml injection [epogen]; hydrochlorothiazide 25 mg oral tablet; amoxicillin 250 mg oral capsule; acetaminophen 325 mg / oxycodone hydrochloride 5 mg oral tablet; 120 actuat fluticasone propionate 0.044 mg/actuat metered dose inhaler [flovent]; amlodipine 2.5 mg oral tablet; insulin isophane, human 70 unt/ml / insulin, regular, human 30 unt/ml injectable suspension [humulin]; albuterol 0.83 mg/ml inhalation solution; naproxen sodium 220 mg oral tablet # Assessment and Plan Patient is presenting with medication review due (situation). ## Plan The patient was prescribed the following medications: - insulin isophane, human 70 unt/ml / insulin, regular, human 30 unt/ml injectable suspension [humulin] - hydrochlorothiazide 25 mg oral tablet - 120 actuat fluticasone propionate 0.044 mg/actuat metered dose inhaler [flovent] - lisinopril 10 mg oral tablet - amlodipine 2.5 mg oral tablet - albuterol 0.83 mg/ml inhalation solution
[DocumentReference/780c6791-75b5-9812-862b-fe427fd46142#2] Clinical note | 2026-04-01 | part 2 of 2 | # Social History Patient is single. Patient has never smoked. Patient identifies as heterosexual. Patient comes from a high socioeconomic background. Patient is a college graduate. Patient currently has Medicare. # Allergies No Known Allergies. # Medications lisinopril 10 mg oral tablet; tropicamide 5 mg/ml ophthalmic solution; 1 ml epoetin alfa 4000 unt/ml injection [epogen]; hydrochlorothiazide 25 mg oral tablet; amoxicillin 250 mg oral capsule; acetaminophen 325 mg / oxycodone hydrochloride 5 mg oral tablet; 120 actuat fluticasone propionate 0.044 mg/actuat metered dose inhaler [flovent]; amlodipine 2.5 mg oral tablet; insulin isophane, human 70 unt/ml / insulin, regular, human 30 unt/ml injectable suspension [humulin]; albuterol 0.83 mg/ml inhalation solution; naproxen sodium 220 mg oral tablet # Assessment and Plan Patient is presenting with medication review due (situation). ## Plan The patient was prescribed the following medications: - insulin isophane, human 70 unt/ml / insulin, regular, human 30 unt/ml injectable suspension [humulin] - hydrochlorothiazide 25 mg oral tablet - 120 actuat fluticasone propionate 0.044 mg/actuat metered dose inhaler [flovent] - lisinopril 10 mg oral tablet - amlodipine 2.5 mg oral tablet - albuterol 0.83 mg/ml inhalation solution
[DocumentReference/6bdffe30-6826-064d-7bab-56b5778a9e54#2] Clinical note | 2025-09-03 | part 2 of 2 | # Social History Patient is single. Patient has never smoked. Patient identifies as heterosexual. Patient comes from a high socioeconomic background. Patient is a college graduate. Patient currently has Medicare. # Allergies No Known Allergies. # Medications lisinopril 10 mg oral tablet; tropicamide 5 mg/ml ophthalmic solution; 1 ml epoetin alfa 4000 unt/ml injection [epogen]; hydrochlorothiazide 25 mg oral tablet; amoxicillin 250 mg oral capsule; acetaminophen 325 mg / oxycodone hydrochloride 5 mg oral tablet; 120 actuat fluticasone propionate 0.044 mg/actuat metered dose inhaler [flovent]; amlodipine 2.5 mg oral tablet; insulin isophane, human 70 unt/ml / insulin, regular, human 30 unt/ml injectable suspension [humulin]; albuterol 0.83 mg/ml inhalation solution; naproxen sodium 220 mg oral tablet # Assessment and Plan Patient is presenting with medication review due (situation). ## Plan The patient was prescribed the following medications: - insulin isophane, human 70 unt/ml / insulin, regular, human 30 unt/ml injectable suspension [humulin] - hydrochlorothiazide 25 mg oral tablet - 120 actuat fluticasone propionate 0.044 mg/actuat metered dose inhaler [flovent] - lisinopril 10 mg oral tablet - amlodipine 2.5 mg oral tablet - albuterol 0.83 mg/ml inhalation solution
```

</details>

label: s
note: The cited 2026-09-30 note's Plan lists as prescribed Humulin, hydrochlorothiazide, Flovent, lisinopril, amlodipine and albuterol, the same six drugs as the six active 2026-09-30 MedicationRequests.

## 6. `last-visit:0e6e0d73#0#1`

Question: When was the patient's most recent visit, and what kind of visit was it?

Answer: The patient's most recent visit was on 2026-07-12, an ambulatory Consultation for treatment (procedure) for contraception care (regime/therapy) at NEW ENGLAND SINAI HOSPITAL. **At that visit, Levora 0.15/30 28 Day (ethinyl estradiol 0.03 MG / levonorgestrel 0.15 MG) was prescribed, and the prescription is listed as active.**

Cards this sentence cites:

- `[MedicationRequest/0e6e0d73-619d-15c3-e363-3a1afa521a17]` MedicationRequest | prescribed 2026-07-12 | {21 (ethinyl estradiol 0.03 MG / levonorgestrel 0.15 MG Oral Tablet) / 7 (inert ingredients 1 MG Oral Tablet) } Pack [Levora 0.15/30 28 Day] | status active | RxNorm 748879

<details><summary>Everything the model saw (26 cards)</summary>

```text
[Condition/0e6e0d73-619d-15c3-1198-27a3f1e6671d] Condition | onset 2026-05-25 | Full-time employment (finding) | clinical status active | SNOMED 160903007
[Condition/0e6e0d73-619d-15c3-73bb-c4435e198a52] Condition | onset 2021-08-16 | Unhealthy alcohol drinking behavior (finding) | clinical status active | SNOMED 10939881000119105
[Condition/0e6e0d73-619d-15c3-a2af-2198a3d15909] Condition | onset 2021-08-02 | Medication review due (situation) | clinical status active | SNOMED 314529007
[Condition/0e6e0d73-619d-15c3-7d75-d0dd94ac6175] Condition | onset 2018-04-30 | Past pregnancy history of miscarriage (situation) | clinical status active | SNOMED 161744009
[Condition/0e6e0d73-619d-15c3-dabb-3f18b4ab6eed] Condition | onset 2017-09-23 | Sepsis (disorder) | clinical status active | SNOMED 91302008
[Condition/0e6e0d73-619d-15c3-279b-bad1f131dc84] Condition | onset 2017-09-23 | Septic shock (disorder) | clinical status active | SNOMED 76571007
[Condition/0e6e0d73-619d-15c3-252c-3ec5aec72d7f] Condition | onset 2006-07-17 | Victim of intimate partner abuse (finding) | clinical status active | SNOMED 706893006
[Condition/0e6e0d73-619d-15c3-a3b6-7fc6f2b594a9] Condition | onset 2002-07-08 | Educated to high school level (finding) | clinical status active | SNOMED 473461003
[Condition/0e6e0d73-619d-15c3-a0ee-8e9994e38bf4] Condition | onset 2001-07-02 | Risk activity involvement (finding) | clinical status active | SNOMED 160968000
[MedicationRequest/0e6e0d73-619d-15c3-e363-3a1afa521a17] MedicationRequest | prescribed 2026-07-12 | {21 (ethinyl estradiol 0.03 MG / levonorgestrel 0.15 MG Oral Tablet) / 7 (inert ingredients 1 MG Oral Tablet) } Pack [Levora 0.15/30 28 Day] | status active | RxNorm 748879
[Encounter/0e6e0d73-619d-15c3-9366-052e1e643c56] Encounter | 2026-07-12 | Consultation for treatment (procedure) | class AMB | reason: Contraception care (regime/therapy) | at NEW ENGLAND SINAI HOSPITAL
[Encounter/0e6e0d73-619d-15c3-60c1-89e78f0afd63] Encounter | 2026-05-25 | General examination of patient (procedure) | class AMB | at ENRICH WELLNESS HEALTH CENTER LLC
[Encounter/0e6e0d73-619d-15c3-08dc-dd55aa3a67ea] Encounter | 2025-07-17 | Consultation for treatment (procedure) | class AMB | reason: Contraception care (regime/therapy) | at NEW ENGLAND SINAI HOSPITAL
[Immunization/0e6e0d73-619d-15c3-f93b-2cd3ab790ac4] Immunization | 2026-05-25 | Hep A, adult | status completed | CVX 52
[Immunization/0e6e0d73-619d-15c3-e4c7-db7a86392a05] Immunization | 2026-05-25 | Influenza, split virus, trivalent, PF | status completed | CVX 140
[Immunization/0e6e0d73-619d-15c3-8254-2b4f6f2ea96c] Immunization | 2026-05-25 | Td (adult), 5 Lf tetanus toxoid, preservative free, adsorbed | status completed | CVX 113
[Encounter/0e6e0d73-619d-15c3-1e47-5eaaf40f64fc] Encounter | 2001-07-02 | Well child visit (procedure) | class AMB | at ENRICH WELLNESS HEALTH CENTER LLC
[Encounter/0e6e0d73-619d-15c3-cf19-f83770d11355] Encounter | 2024-07-15 | Postnatal visit (regime/therapy) | class AMB | at NEW ENGLAND SINAI HOSPITAL
[Encounter/0e6e0d73-619d-15c3-cee9-5d4677ae3061] Encounter | 2024-05-13 | Prenatal visit (regime/therapy) | class AMB | reason: Normal pregnancy (finding) | at NEW ENGLAND SINAI HOSPITAL
[Encounter/0e6e0d73-619d-15c3-419a-775bf57ccccf] Encounter | 2024-05-06 | Prenatal visit (regime/therapy) | class AMB | reason: Normal pregnancy (finding) | at NEW ENGLAND SINAI HOSPITAL
[Encounter/0e6e0d73-619d-15c3-4fcb-c0b6a5c7e704] Encounter | 2023-12-04 | Prenatal visit (regime/therapy) | class AMB | reason: Normal pregnancy (finding) | at NEW ENGLAND SINAI HOSPITAL
[Encounter/0e6e0d73-619d-15c3-901e-799a89ef2329] Encounter | 2024-05-27 | Prenatal visit (regime/therapy) | class AMB | reason: Normal pregnancy (finding) | at NEW ENGLAND SINAI HOSPITAL
[Encounter/0e6e0d73-619d-15c3-e63c-aad9b351c11c] Encounter | 2024-04-22 | Prenatal visit (regime/therapy) | class AMB | reason: Normal pregnancy (finding) | at NEW ENGLAND SINAI HOSPITAL
[Encounter/0e6e0d73-619d-15c3-440e-fa98e2430730] Encounter | 2024-01-01 | Prenatal visit (regime/therapy) | class AMB | reason: Normal pregnancy (finding) | at NEW ENGLAND SINAI HOSPITAL
[Encounter/0e6e0d73-619d-15c3-7da9-b2f0ee46c986] Encounter | 2018-04-16 | Prenatal initial visit (regime/therapy) | class AMB | reason: Normal pregnancy (finding) | at NEW ENGLAND SINAI HOSPITAL
[Encounter/0e6e0d73-619d-15c3-94a4-5ffa7c240e31] Encounter | 2024-03-25 | Prenatal visit (regime/therapy) | class AMB | reason: Normal pregnancy (finding) | at NEW ENGLAND SINAI HOSPITAL
```

</details>

label: s
note: Cited card shows the Levora 0.15/30 28 Day pack (ethinyl estradiol 0.03 MG / levonorgestrel 0.15 MG) prescribed 2026-07-12 with status active, the same date as the most recent visit (the 2026-07-12 consultation).

## 7. `last-flu-shot:7280f7f8#0#0`

Question: When did the patient last get a flu shot?

Answer: **The patient's most recent flu shot was on 2026-04-12 (Influenza, split virus, trivalent, PF; status completed).** Earlier flu shots were given on 2024-11-24, 2024-03-31, and 2023-03-26.

Cards this sentence cites:

- `[Immunization/7280f7f8-315d-7c6a-89f5-f28321d6dbe8]` Immunization | 2026-04-12 | Influenza, split virus, trivalent, PF | status completed | CVX 140

<details><summary>Everything the model saw (43 cards)</summary>

```text
[Condition/7280f7f8-315d-7c6a-5183-1fc53612d856] Condition | onset 2026-04-12 | Alzheimer's disease (disorder) | clinical status active | SNOMED 26929004
[Condition/7280f7f8-315d-7c6a-069f-25fdb34e3e53] Condition | onset 2025-04-06 | Stress (finding) | clinical status active | SNOMED 73595000
[Condition/7280f7f8-315d-7c6a-06ae-a26712c6cfb7] Condition | onset 2024-03-31 | Full-time employment (finding) | clinical status active | SNOMED 160903007
[Condition/7280f7f8-315d-7c6a-84b2-d6045a9b8deb] Condition | onset 2018-11-12 | Abnormal findings diagnostic imaging heart+coronary circulat (finding) | clinical status active | SNOMED 274531002
[Condition/7280f7f8-315d-7c6a-60b8-1b2b3b190d66] Condition | onset 2018-11-04 | Ischemic heart disease (disorder) | clinical status active | SNOMED 414545008
[Condition/7280f7f8-315d-7c6a-eee1-33d3eda16b26] Condition | onset 2014-02-16 | Chronic low back pain (finding) | clinical status active | SNOMED 278860009
[Condition/7280f7f8-315d-7c6a-23b9-2a24d0c43093] Condition | onset 2014-02-16 | Chronic neck pain (finding) | clinical status active | SNOMED 1121000119107
[Condition/7280f7f8-315d-7c6a-f371-666500850eb4] Condition | onset 2014-02-02 | Gingivitis (disorder) | clinical status active | SNOMED 66383009
[Condition/7280f7f8-315d-7c6a-b5ea-aa0955ebc2c7] Condition | onset 2010-01-10 | Hyperlipidemia (disorder) | clinical status active | SNOMED 55822004
[Condition/7280f7f8-315d-7c6a-929f-e845c91bba18] Condition | onset 1993-02-06 | Dependent drug abuse (disorder) | clinical status active | SNOMED 6525002
[Condition/7280f7f8-315d-7c6a-6159-244929402415] Condition | onset 1991-07-09 | Chronic pain (finding) | clinical status active | SNOMED 82423001
[Condition/7280f7f8-315d-7c6a-7561-551dd4fb980c] Condition | onset 1990-11-11 | Has a criminal record (finding) | clinical status active | SNOMED 266948004
[Condition/7280f7f8-315d-7c6a-69cb-9f6bde195716] Condition | onset 1990-10-25 | Impacted molars (disorder) | clinical status active | SNOMED 196416002
[Condition/7280f7f8-315d-7c6a-e183-7fc41f06abde] Condition | onset 1990-02-06 | Chronic intractable migraine without aura (disorder) | clinical status active | SNOMED 124171000119105
[Condition/7280f7f8-315d-7c6a-57cd-16215a141add] Condition | onset 1988-11-06 | Body mass index 30+ - obesity (finding) | clinical status active | SNOMED 162864005
[Condition/7280f7f8-315d-7c6a-7c25-7a247f43e721] Condition | onset 1981-01-18 | Anemia (disorder) | clinical status active | SNOMED 271737000
[Condition/7280f7f8-315d-7c6a-50ac-70390520f5d8] Condition | onset 1981-01-18 | Prediabetes (finding) | clinical status active | SNOMED 714628002
[Condition/7280f7f8-315d-7c6a-a35c-5f2c4404e1cd] Condition | onset 1971-02-18 | Chronic sinusitis (disorder) | clinical status active | SNOMED 40055000
[Condition/7280f7f8-315d-7c6a-cf3c-1559c1e270a8] Condition | onset 1964-12-20 | Housing unsatisfactory (finding) | clinical status active | SNOMED 105531004
[Condition/7280f7f8-315d-7c6a-3735-89103641aea2] Condition | onset 1964-12-20 | Only received primary school education (finding) | clinical status active | SNOMED 224295006
[MedicationRequest/7280f7f8-315d-7c6a-d103-5f5cf25ace53] MedicationRequest | prescribed 2026-04-13 | Simvastatin 10 MG Oral Tablet | status active | reason: Hyperlipidemia (disorder) | RxNorm 314231
[MedicationRequest/7280f7f8-315d-7c6a-dd3c-435b565b36d4] MedicationRequest | prescribed 2026-04-12 | Ibuprofen 400 MG Oral Tablet [Ibu] | status active | RxNorm 206905
[MedicationRequest/7280f7f8-315d-7c6a-698d-8c3f4a330263] MedicationRequest | prescribed 2026-04-12 | Acetaminophen 325 MG / Oxycodone Hydrochloride 10 MG Oral Tablet [Percocet] | status active | RxNorm 1049625
[MedicationRequest/7280f7f8-315d-7c6a-53dc-677516ba315e] MedicationRequest | prescribed 2026-04-12 | Galantamine 4 MG Oral Tablet | status active | reason: Alzheimer's disease (disorder) | RxNorm 310436
[MedicationRequest/7280f7f8-315d-7c6a-21fd-127361ce4eae] MedicationRequest | prescribed 2026-04-12 | Acetaminophen 325 MG Oral Tablet [Tylenol] | status active | RxNorm 209387
[MedicationRequest/7280f7f8-315d-7c6a-e1ca-6672a64e96d6] MedicationRequest | prescribed 2018-11-11 | Simvastatin 20 MG Oral Tablet | status active | RxNorm 312961
[MedicationRequest/7280f7f8-315d-7c6a-d3dc-bf227b26b9de] MedicationRequest | prescribed 2018-11-11 | Nitroglycerin 0.4 MG/ACTUAT Mucosal Spray | status active | RxNorm 705129
[MedicationRequest/7280f7f8-315d-7c6a-40f0-094ac0d35606] MedicationRequest | prescribed 2018-11-11 | Clopidogrel 75 MG Oral Tablet | status active | RxNorm 309362
[MedicationRequest/7280f7f8-315d-7c6a-344e-7b21fe48818f] MedicationRequest | prescribed 2018-11-11 | 24 HR metoprolol succinate 100 MG Extended Release Oral Tablet | status active | RxNorm 866412
[Encounter/7280f7f8-315d-7c6a-ddbc-56619e72a429] Encounter | 2026-04-26 | Encounter for check up (procedure) | class AMB | at LAWRENCE GENERAL HOSPITAL
[Encounter/7280f7f8-315d-7c6a-e49f-7858d34e1916] Encounter | 2026-04-13 | Follow-up encounter (procedure) | class AMB | reason: Hyperlipidemia (disorder) | at LAWRENCE GENERAL HOSPITAL
[Encounter/7280f7f8-315d-7c6a-79c7-b2135168eae6] Encounter | 2026-04-12 | General examination of patient (procedure) | class AMB | at HOLY FAMILY MEDICAL SPECIALTY PRACTICE PLLC
[Immunization/7280f7f8-315d-7c6a-89f5-f28321d6dbe8] Immunization | 2026-04-12 | Influenza, split virus, trivalent, PF | status completed | CVX 140
[Observation/7280f7f8-315d-7c6a-2d11-a7126032c00a] Observation (laboratory) | 2020-12-21 | Influenza virus B Ag [Presence] in Upper respiratory specimen by Rapid immunoassay = Not detected (qualifier value) | status final | LOINC 80383-3
[Observation/7280f7f8-315d-7c6a-3bcf-660371c4df20] Observation (survey) | 2024-03-31 | Protocol for Responding to and Assessing Patients' Assets, Risks, and Experiences [PRAPARE] = Within the last year, have you been afraid of your partner or ex-partner No; Do you feel physically and emotionally safe where you currently live [PRAPARE] Yes; Are you a refugee No; Have you spent more than 2 nights in a row in a jail, prison, detention center, or juvenile correctional facility in past 1 year [PRAPARE] Yes; Stress level Somewhat; How often do you see or talk to people that you care about and feel close to [PRAPARE] 5 or more times a week; Has lack of transportation kept you from medical appointments, meetings, work, or from getting things needed for daily living No; Have you or any family members you live with been unable to get any of the following when it was really needed in past 1 year [PRAPARE] Food; What was your best estimate of the total income of all family members from all sources, before taxes, in last year [PhenX] 41074 /a; Primary insurance Medicare; Employment status - current Full-time work; Highest level of education Less than high school degree; Address 702 Parisian Flat; Are you worried about losing your housing [PRAPARE] Yes; Housing status I have housing; How many people are living or staying at this address [#] 8 {#}; Preferred language English; Discharged from the U.S. Armed Forces No; Has season or migrant farm work been your or your family's main source of income at any point in past 2 years [PRAPARE] No; Race White; Hispanic or Latino No | status final | LOINC 93025-5
[Observation/7280f7f8-315d-7c6a-17d4-3bde7faffa5a] Observation (survey) | 2026-04-12 | Protocol for Responding to and Assessing Patients' Assets, Risks, and Experiences [PRAPARE] = Within the last year, have you been afraid of your partner or ex-partner No; Do you feel physically and emotionally safe where you currently live [PRAPARE] Yes; Are you a refugee No; Have you spent more than 2 nights in a row in a jail, prison, detention center, or juvenile correctional facility in past 1 year [PRAPARE] Yes; Stress level A little bit; How often do you see or talk to people that you care about and feel close to [PRAPARE] 3 to 5 times a week; Has lack of transportation kept you from medical appointments, meetings, work, or from getting things needed for daily living No; Have you or any family members you live with been unable to get any of the following when it was really needed in past 1 year [PRAPARE] I choose not to answer this question; What was your best estimate of the total income of all family members from all sources, before taxes, in last year [PhenX] 41074 /a; Primary insurance Medicare; Employment status - current Full-time work; Highest level of education Less than high school degree; Address 702 Parisian Flat; Are you worried about losing your housing [PRAPARE] Yes; Housing status I have housing; How many people are living or staying at this address [#] 8 {#}; Preferred language English; Discharged from the U.S. Armed Forces No; Has season or migrant farm work been your or your family's main source of income at any point in past 2 years [PRAPARE] No; Race White; Hispanic or Latino No | status final | LOINC 93025-5
[Observation/7280f7f8-315d-7c6a-073a-b5db76259ffb] Observation (survey) | 2025-04-06 | Protocol for Responding to and Assessing Patients' Assets, Risks, and Experiences [PRAPARE] = Within the last year, have you been afraid of your partner or ex-partner No; Do you feel physically and emotionally safe where you currently live [PRAPARE] Yes; Are you a refugee No; Have you spent more than 2 nights in a row in a jail, prison, detention center, or juvenile correctional facility in past 1 year [PRAPARE] Yes; Stress level Quite a bit; How often do you see or talk to people that you care about and feel close to [PRAPARE] 3 to 5 times a week; Has lack of transportation kept you from medical appointments, meetings, work, or from getting things needed for daily living No; Have you or any family members you live with been unable to get any of the following when it was really needed in past 1 year [PRAPARE] Medicine or Any Health Care (Medical, Dental, Mental Health, Vision); What was your best estimate of the total income of all family members from all sources, before taxes, in last year [PhenX] 41074 /a; Primary insurance Medicare; Employment status - current Full-time work; Highest level of education Less than high school degree; Address 702 Parisian Flat; Are you worried about losing your housing [PRAPARE] Yes; Housing status I have housing; How many people are living or staying at this address [#] 8 {#}; Preferred language English; Discharged from the U.S. Armed Forces No; Has season or migrant farm work been your or your family's main source of income at any point in past 2 years [PRAPARE] No; Race White; Hispanic or Latino No | status final | LOINC 93025-5
[Observation/7280f7f8-315d-7c6a-f0b4-d6fc3b03db28] Observation (survey) | 2024-11-24 | Protocol for Responding to and Assessing Patients' Assets, Risks, and Experiences [PRAPARE] = Within the last year, have you been afraid of your partner or ex-partner No; Do you feel physically and emotionally safe where you currently live [PRAPARE] Yes; Are you a refugee No; Have you spent more than 2 nights in a row in a jail, prison, detention center, or juvenile correctional facility in past 1 year [PRAPARE] Yes; Stress level Not at all; How often do you see or talk to people that you care about and feel close to [PRAPARE] 5 or more times a week; Has lack of transportation kept you from medical appointments, meetings, work, or from getting things needed for daily living No; Have you or any family members you live with been unable to get any of the following when it was really needed in past 1 year [PRAPARE] Utilities; What was your best estimate of the total income of all family members from all sources, before taxes, in last year [PhenX] 41074 /a; Primary insurance Medicare; Employment status - current Full-time work; Highest level of education Less than high school degree; Address 702 Parisian Flat; Are you worried about losing your housing [PRAPARE] Yes; Housing status I have housing; How many people are living or staying at this address [#] 8 {#}; Preferred language English; Discharged from the U.S. Armed Forces No; Has season or migrant farm work been your or your family's main source of income at any point in past 2 years [PRAPARE] No; Race White; Hispanic or Latino No | status final | LOINC 93025-5
[Observation/7280f7f8-315d-7c6a-aa9b-12ba229b5de0] Observation (laboratory) | 2020-12-21 | Influenza virus A Ag [Presence] in Upper respiratory specimen by Rapid immunoassay = Not detected (qualifier value) | status final | LOINC 80382-5
[Immunization/7280f7f8-315d-7c6a-2836-354c2b85cb88] Immunization | 2023-03-26 | Influenza, split virus, trivalent, PF | status completed | CVX 140
[Immunization/7280f7f8-315d-7c6a-a994-7340336c5a95] Immunization | 2024-11-24 | Influenza, split virus, trivalent, PF | status completed | CVX 140
[Immunization/7280f7f8-315d-7c6a-5206-3912d1550e2d] Immunization | 2024-03-31 | Influenza, split virus, trivalent, PF | status completed | CVX 140
[DiagnosticReport/7280f7f8-315d-7c6a-a75e-da29d2a52425] DiagnosticReport | 2020-12-21 | Influenza virus A and B Ag panel - Upper respiratory specimen by Rapid immunoassay | results: Influenza virus A Ag [Presence] in Upper respiratory specimen by Rapid immunoassay Not detected (qualifier value); Influenza virus B Ag [Presence] in Upper respiratory specimen by Rapid immunoassay Not detected (qualifier value) | LOINC 80381-7
```

</details>

label: s
note: Cited immunization is Influenza, split virus, trivalent, PF on 2026-04-12, status completed; the other influenza immunizations seen are 2024-11-24, 2024-03-31 and 2023-03-26, so this one is the most recent.

## 8. `prescribed-for-anemia:8d945e28#0#0`

Question: Which medications have been prescribed for the patient's anemia?

Answer: **The record has several completed medication requests with the reason Anemia (disorder), prescribed 2021-02-18, 2021-04-22, 2021-08-18, 2021-10-18, 2021-12-19, 2026-09-20, 2026-09-23 and 2026-09-27, but these entries do not name the medication.** Clinical notes from 2021-04-19 and 2021-05-10 record prescriptions of 1 ml epoetin alfa 4000 unt/ml injection [epogen], though these notes do not state the reason for it. An active Vitamin B12 5 MG/ML Injectable Solution was prescribed 1981-07-27, but no reason is listed for it.

Cards this sentence cites:

- `[MedicationRequest/8d945e28-1d8a-bd72-b130-0ab0ae19f5ef]` MedicationRequest | prescribed 2021-02-18 | status completed | reason: Anemia (disorder)
- `[MedicationRequest/8d945e28-1d8a-bd72-9d0f-7f2bf255038a]` MedicationRequest | prescribed 2021-04-22 | status completed | reason: Anemia (disorder)
- `[MedicationRequest/8d945e28-1d8a-bd72-2310-7887f27830d3]` MedicationRequest | prescribed 2021-08-18 | status completed | reason: Anemia (disorder)
- `[MedicationRequest/8d945e28-1d8a-bd72-d1d1-ade610dfcc7f]` MedicationRequest | prescribed 2021-10-18 | status completed | reason: Anemia (disorder)
- `[MedicationRequest/8d945e28-1d8a-bd72-6a8e-71a80daaea46]` MedicationRequest | prescribed 2021-12-19 | status completed | reason: Anemia (disorder)
- `[MedicationRequest/8d945e28-1d8a-bd72-84b2-c9e1d128173c]` MedicationRequest | prescribed 2026-09-20 | status completed | reason: Anemia (disorder)
- `[MedicationRequest/8d945e28-1d8a-bd72-5f50-134a5a073f4d]` MedicationRequest | prescribed 2026-09-23 | status completed | reason: Anemia (disorder)
- `[MedicationRequest/8d945e28-1d8a-bd72-1c5f-e1356b8956dd]` MedicationRequest | prescribed 2026-09-27 | status completed | reason: Anemia (disorder)

<details><summary>Everything the model saw (39 cards)</summary>

```text
[Condition/8d945e28-1d8a-bd72-9d6c-259e17157c55] Condition | onset 2026-09-07 | Full-time employment (finding) | clinical status active | SNOMED 160903007
[Condition/8d945e28-1d8a-bd72-3102-64b703ba601c] Condition | onset 2026-07-13 | Medication review due (situation) | clinical status active | SNOMED 314529007
[Condition/8d945e28-1d8a-bd72-6b51-0718e8cd7a5e] Condition | onset 2021-01-01 | Awaiting transplantation of kidney (situation) | clinical status active | SNOMED 698306007
[Condition/8d945e28-1d8a-bd72-db4c-2552d073039a] Condition | onset 2020-11-09 | Chronic kidney disease stage 4 (disorder) | clinical status active | SNOMED 431857002
[Condition/8d945e28-1d8a-bd72-ed26-25aa62be033c] Condition | onset 2020-08-18 | Dependent drug abuse (disorder) | clinical status active | SNOMED 6525002
[Condition/8d945e28-1d8a-bd72-05bf-4b4b02b03fe9] Condition | onset 2018-01-22 | Has a criminal record (finding) | clinical status active | SNOMED 266948004
[Condition/8d945e28-1d8a-bd72-38fb-c4bf927332c6] Condition | onset 2013-09-16 | Proteinuria due to type 2 diabetes mellitus (disorder) | clinical status active | SNOMED 157141000119108
[Condition/8d945e28-1d8a-bd72-1379-82140e2d1648] Condition | onset 2013-09-16 | Chronic kidney disease stage 3 (disorder) | clinical status active | SNOMED 433144002
[Condition/8d945e28-1d8a-bd72-cd47-b95fb1e4464b] Condition | onset 2009-07-06 | Microalbuminuria due to type 2 diabetes mellitus (disorder) | clinical status active | SNOMED 90781000119102
[Condition/8d945e28-1d8a-bd72-be1a-fb710d842e34] Condition | onset 2009-07-06 | Chronic kidney disease stage 2 (disorder) | clinical status active | SNOMED 431856006
[Condition/8d945e28-1d8a-bd72-2a55-0f3c986db8dd] Condition | onset 2009-07-06 | Gingivitis (disorder) | clinical status active | SNOMED 66383009
[Condition/8d945e28-1d8a-bd72-4277-241d976b7354] Condition | onset 2007-06-25 | Metabolic syndrome X (disorder) | clinical status active | SNOMED 237602007
[Condition/8d945e28-1d8a-bd72-e0ac-a99a0168ad8a] Condition | onset 2004-06-07 | Disorder of kidney due to diabetes mellitus (disorder) | clinical status active | SNOMED 127013003
[Condition/8d945e28-1d8a-bd72-a508-e7d1553f7f62] Condition | onset 2004-06-07 | Chronic kidney disease stage 1 (disorder) | clinical status active | SNOMED 431855005
[Condition/8d945e28-1d8a-bd72-2622-8fe0a1a30909] Condition | onset 2003-06-02 | Essential hypertension (disorder) | clinical status active | SNOMED 59621000
[Condition/8d945e28-1d8a-bd72-12e3-17db162c8f0b] Condition | onset 2001-06-04 | Obstructive sleep apnea syndrome (disorder) | clinical status active | SNOMED 78275009
[Condition/8d945e28-1d8a-bd72-d01e-086bb9d1d22f] Condition | onset 2001-05-07 | Sleep disorder (disorder) | clinical status active | SNOMED 39898005
[Condition/8d945e28-1d8a-bd72-f5fa-42692b5be159] Condition | onset 1996-08-05 | Body mass index 30+ - obesity (finding) | clinical status active | SNOMED 162864005
[Condition/8d945e28-1d8a-bd72-e601-8e5493910aec] Condition | onset 1981-07-20 | Prediabetes (finding) | clinical status active | SNOMED 714628002
[Condition/8d945e28-1d8a-bd72-52ca-256d6584412c] Condition | onset 1981-07-20 | Anemia (disorder) | clinical status active | SNOMED 271737000
[Condition/8d945e28-1d8a-bd72-d644-66738e889d91] Condition | onset 1977-07-11 | Received higher education (finding) | clinical status active | SNOMED 224299000
[Condition/8d945e28-1d8a-bd72-fbf9-3e6f6bd97f57] Condition | onset 1977-03-07 | Risk activity involvement (finding) | clinical status active | SNOMED 160968000
[MedicationRequest/8d945e28-1d8a-bd72-ff5c-41daf21d65a9] MedicationRequest | prescribed 2026-09-07 | insulin isophane, human 70 UNT/ML / insulin, regular, human 30 UNT/ML Injectable Suspension [Humulin] | status active | reason: Prediabetes (finding) | RxNorm 106892
[MedicationRequest/8d945e28-1d8a-bd72-d409-38c0124f2c47] MedicationRequest | prescribed 2026-09-07 | Hydrochlorothiazide 25 MG Oral Tablet | status active | reason: Essential hypertension (disorder) | RxNorm 310798
[MedicationRequest/8d945e28-1d8a-bd72-bcd6-3304c42dca58] MedicationRequest | prescribed 1981-07-27 | Vitamin B12 5 MG/ML Injectable Solution | status active | RxNorm 2001499
[Encounter/8d945e28-1d8a-bd72-016c-9af67d7199fd] Encounter | 2026-09-27 | Encounter for problem (procedure) | class AMB | reason: Chronic kidney disease stage 4 (disorder) | at NEW ENGLAND REHABILITATION SERVICES OF CENTRAL MASSACHUSETTS INC
[Encounter/8d945e28-1d8a-bd72-3f01-7946bd8f2be1] Encounter | 2026-09-26 | Encounter for problem (procedure) | class AMB | reason: Chronic kidney disease stage 4 (disorder) | at NEW ENGLAND REHABILITATION SERVICES OF CENTRAL MASSACHUSETTS INC
[Encounter/8d945e28-1d8a-bd72-9dbd-785d1f0e4915] Encounter | 2026-09-23 | Encounter for problem (procedure) | class AMB | reason: Chronic kidney disease stage 4 (disorder) | at NEW ENGLAND REHABILITATION SERVICES OF CENTRAL MASSACHUSETTS INC
[Immunization/8d945e28-1d8a-bd72-6a94-32775be2d4e6] Immunization | 2026-01-12 | Influenza, split virus, trivalent, PF | status completed | CVX 140
[DocumentReference/39c3ccb8-f3ba-af45-7465-13f2298b9b36#2] Clinical note | 2021-05-10 | part 2 of 2 | # Assessment and Plan ## Plan Patient was given the following immunizations: covid-19, mrna, lnp-s, pf, 30 mcg/0.3 ml dose. The following procedures were conducted: - renal dialysis (procedure) The patient was prescribed the following medications: - 1 ml epoetin alfa 4000 unt/ml injection [epogen]
[MedicationRequest/8d945e28-1d8a-bd72-d1d1-ade610dfcc7f] MedicationRequest | prescribed 2021-10-18 | status completed | reason: Anemia (disorder)
[DocumentReference/3f628097-7433-7ecf-0911-07f6fe088905#2] Clinical note | 2021-04-19 | part 2 of 2 | # Assessment and Plan ## Plan Patient was given the following immunizations: covid-19, mrna, lnp-s, pf, 30 mcg/0.3 ml dose. The following procedures were conducted: - renal dialysis (procedure) The patient was prescribed the following medications: - 1 ml epoetin alfa 4000 unt/ml injection [epogen]
[MedicationRequest/8d945e28-1d8a-bd72-2310-7887f27830d3] MedicationRequest | prescribed 2021-08-18 | status completed | reason: Anemia (disorder)
[MedicationRequest/8d945e28-1d8a-bd72-1c5f-e1356b8956dd] MedicationRequest | prescribed 2026-09-27 | status completed | reason: Anemia (disorder)
[MedicationRequest/8d945e28-1d8a-bd72-b130-0ab0ae19f5ef] MedicationRequest | prescribed 2021-02-18 | status completed | reason: Anemia (disorder)
[MedicationRequest/8d945e28-1d8a-bd72-5f50-134a5a073f4d] MedicationRequest | prescribed 2026-09-23 | status completed | reason: Anemia (disorder)
[MedicationRequest/8d945e28-1d8a-bd72-6a8e-71a80daaea46] MedicationRequest | prescribed 2021-12-19 | status completed | reason: Anemia (disorder)
[MedicationRequest/8d945e28-1d8a-bd72-84b2-c9e1d128173c] MedicationRequest | prescribed 2026-09-20 | status completed | reason: Anemia (disorder)
[MedicationRequest/8d945e28-1d8a-bd72-9d0f-7f2bf255038a] MedicationRequest | prescribed 2021-04-22 | status completed | reason: Anemia (disorder)
```

</details>

label: s
note: All eight cited MedicationRequests are status completed, reason Anemia (disorder), with no drug named, on exactly the eight listed dates; no other anemia-reason MedicationRequest appears among the cards seen.

## 9. `vaccines-last-year:8446fe54#0#0`

Question: Which vaccines did the patient receive in the last year?

Answer: **In the last year, the only vaccine recorded is Influenza, split virus, trivalent, PF (CVX 140), given on 2025-10-03 with status completed.**

Cards this sentence cites:

- `[Immunization/8446fe54-5b2e-6a46-dae8-760a54add250]` Immunization | 2025-10-03 | Influenza, split virus, trivalent, PF | status completed | CVX 140

<details><summary>Everything the model saw (49 cards)</summary>

```text
[Condition/8446fe54-5b2e-6a46-c855-6376bf616037] Condition | onset 2025-10-03 | Stress (finding) | clinical status active | SNOMED 73595000
[Condition/8446fe54-5b2e-6a46-3883-408ea2da0a37] Condition | onset 2025-05-15 | Nonproliferative diabetic retinopathy due to type II diabetes mellitus | clinical status active | SNOMED 1551000119108
[Condition/8446fe54-5b2e-6a46-2283-ccf89bdfa001] Condition | onset 2024-09-27 | Medication review due (situation) | clinical status active | SNOMED 314529007
[Condition/8446fe54-5b2e-6a46-8ab7-b639a56aa55f] Condition | onset 2023-09-22 | Osteoporosis (disorder) | clinical status active | SNOMED 64859006
[Condition/8446fe54-5b2e-6a46-169f-475724b93b14] Condition | onset 2022-03-10 | History of myocardial infarction (situation) | clinical status active | SNOMED 399211009
[Condition/8446fe54-5b2e-6a46-7c5e-428350d41910] Condition | onset 2022-03-08 | Acute non-ST segment elevation myocardial infarction (disorder) | clinical status active | SNOMED 401314000
[Condition/8446fe54-5b2e-6a46-b854-dbfe1d5848d8] Condition | onset 2019-08-30 | Neuropathy due to type 2 diabetes mellitus (disorder) | clinical status active | SNOMED 368581000119106
[Condition/8446fe54-5b2e-6a46-9883-d3e4fb3c92c7] Condition | onset 2017-08-18 | Full-time employment (finding) | clinical status active | SNOMED 160903007
[Condition/8446fe54-5b2e-6a46-90ec-9d5bb7f4215c] Condition | onset 2015-08-07 | Limited social contact (finding) | clinical status active | SNOMED 423315002
[Condition/8446fe54-5b2e-6a46-ac98-749a48641300] Condition | onset 2009-07-27 | Abnormal findings diagnostic imaging heart+coronary circulat (finding) | clinical status active | SNOMED 274531002
[Condition/8446fe54-5b2e-6a46-ac45-606071904f4c] Condition | onset 2009-07-03 | Ischemic heart disease (disorder) | clinical status active | SNOMED 414545008
[Condition/8446fe54-5b2e-6a46-19e1-02a0cca64803] Condition | onset 2009-07-03 | Gingivitis (disorder) | clinical status active | SNOMED 66383009
[Condition/8446fe54-5b2e-6a46-9731-2ba07e7b3f8a] Condition | onset 2002-05-24 | Hyperlipidemia (disorder) | clinical status active | SNOMED 55822004
[Condition/8446fe54-5b2e-6a46-5645-a8fdbdfcefa0] Condition | onset 1997-04-25 | Essential hypertension (disorder) | clinical status active | SNOMED 59621000
[Condition/8446fe54-5b2e-6a46-6984-e3082708b597] Condition | onset 1997-01-20 | Localized, primary osteoarthritis of the hand (disorder) | clinical status active | SNOMED 201834006
[Condition/8446fe54-5b2e-6a46-918b-8a35802414ef] Condition | onset 1996-11-29 | Metabolic syndrome X (disorder) | clinical status active | SNOMED 237602007
[Condition/8446fe54-5b2e-6a46-8453-0b6ddcc40622] Condition | onset 1996-11-29 | Hypertriglyceridemia (disorder) | clinical status active | SNOMED 302870006
[Condition/8446fe54-5b2e-6a46-71d0-e1231acfc548] Condition | onset 1996-04-19 | Diabetes mellitus type 2 (disorder) | clinical status active | SNOMED 44054006
[Condition/8446fe54-5b2e-6a46-53e3-b8317bbea5b4] Condition | onset 1973-08-15 | Past pregnancy history of miscarriage (situation) | clinical status active | SNOMED 161744009
[Condition/8446fe54-5b2e-6a46-efe6-1830fbd69235] Condition | onset 1971-06-11 | Body mass index 30+ - obesity (finding) | clinical status active | SNOMED 162864005
[Condition/8446fe54-5b2e-6a46-a0b3-4dfcdfdaffac] Condition | onset 1965-06-04 | Anemia (disorder) | clinical status active | SNOMED 271737000
[Condition/8446fe54-5b2e-6a46-26e1-de3ad83381e7] Condition | onset 1965-06-04 | Prediabetes (finding) | clinical status active | SNOMED 714628002
[Condition/8446fe54-5b2e-6a46-3a03-f8734c3aad20] Condition | onset 1961-05-26 | Received higher education (finding) | clinical status active | SNOMED 224299000
[MedicationRequest/8446fe54-5b2e-6a46-659f-46ecea0cf5ef] MedicationRequest | prescribed 2025-10-04 | Simvastatin 10 MG Oral Tablet | status active | reason: Hyperlipidemia (disorder) | RxNorm 314231
[MedicationRequest/8446fe54-5b2e-6a46-88a0-c7dd9e8fc1a1] MedicationRequest | prescribed 2025-10-03 | lisinopril 10 MG Oral Tablet | status active | reason: Essential hypertension (disorder) | RxNorm 314076
[MedicationRequest/8446fe54-5b2e-6a46-7320-4ef7c8ad8f40] MedicationRequest | prescribed 2025-10-03 | Alendronic acid 10 MG Oral Tablet | status active | reason: Osteoporosis (disorder) | RxNorm 904419
[MedicationRequest/8446fe54-5b2e-6a46-bf69-9fef69e23979] MedicationRequest | prescribed 2022-03-10 | rosuvastatin calcium 10 MG Oral Tablet [Crestor] | status active | RxNorm 859749
[MedicationRequest/8446fe54-5b2e-6a46-4de5-bb23365c2bff] MedicationRequest | prescribed 2022-03-10 | carvedilol 25 MG Oral Tablet | status active | RxNorm 200033
[MedicationRequest/8446fe54-5b2e-6a46-49d9-f1a38344333d] MedicationRequest | prescribed 2022-03-10 | aspirin 81 MG Oral Tablet | status active | RxNorm 243670
[MedicationRequest/8446fe54-5b2e-6a46-3148-e44c765beb21] MedicationRequest | prescribed 2022-03-10 | prasugrel 10 MG Oral Tablet | status active | RxNorm 855812
[MedicationRequest/8446fe54-5b2e-6a46-2330-5a6c9a9f35f4] MedicationRequest | prescribed 2022-03-10 | losartan potassium 25 MG Oral Tablet | status active | RxNorm 979485
[MedicationRequest/8446fe54-5b2e-6a46-abfb-29ebed5ed8f5] MedicationRequest | prescribed 2009-07-10 | 24 HR metoprolol succinate 100 MG Extended Release Oral Tablet | status active | RxNorm 866412
[MedicationRequest/8446fe54-5b2e-6a46-a1b3-bc484b4b6e59] MedicationRequest | prescribed 2009-07-10 | Clopidogrel 75 MG Oral Tablet | status active | RxNorm 309362
[MedicationRequest/8446fe54-5b2e-6a46-31e7-0fab4c5ed076] MedicationRequest | prescribed 2009-07-10 | Nitroglycerin 0.4 MG/ACTUAT Mucosal Spray | status active | RxNorm 705129
[MedicationRequest/8446fe54-5b2e-6a46-2210-4b4518283f4c] MedicationRequest | prescribed 2009-07-10 | Simvastatin 20 MG Oral Tablet | status active | RxNorm 312961
[Encounter/8446fe54-5b2e-6a46-f799-ff1c9d688587] Encounter | 2026-04-10 | Ophthalmic examination and evaluation (procedure) | class AMB | at MILFORD REGIONAL MEDICAL CENTER
[Encounter/8446fe54-5b2e-6a46-7463-6a2732ff7cd0] Encounter | 2026-03-06 | Encounter for symptom (procedure) | class AMB | reason: Viral sinusitis (disorder) | at MILFORD REGIONAL MEDICAL CENTER
[Encounter/8446fe54-5b2e-6a46-f36c-8ce8c10cff85] Encounter | 2026-01-11 | Hospital admission (procedure) | class IMP | reason: Patient transfer to skilled nursing facility (procedure) | at CLAFLIN HILL CORPORATION
[Immunization/8446fe54-5b2e-6a46-dae8-760a54add250] Immunization | 2025-10-03 | Influenza, split virus, trivalent, PF | status completed | CVX 140
[DocumentReference/cbab290e-e4c7-b25f-2742-e49eff81ff79#1] Clinical note | 2020-09-04 | part 1 of 2 | 2020-09-04 # Chief Complaint - Tingling in Hands and Feet - Blurred Vision # History of Present Illness Elfrieda676 Agustina460 is a 77 year-old nonhispanic white female. Patient has a history of part-time employment (finding), medication review due (situation), exfoliation of teeth due to systemic causes, viral sinusitis (disorder), social isolation (finding), stress (finding). # Social History Patient is married. Patient has never smoked. Patient identifies as heterosexual. Patient comes from a middle socioeconomic background. Patient has completed some college courses. Patient currently has Medicare. # Allergies No Known Allergies. # Medications lisinopril 10 mg oral tablet; tropicamide 5 mg/ml ophthalmic solution; simvastatin 10 mg oral tablet; naproxen sodium 220 mg oral tablet
[DocumentReference/3f4646b0-9a43-31fc-f695-bdd0cfb7cc2e#1] Clinical note | 2017-09-01 | part 1 of 1 | 2017-09-01 # Chief Complaint - Tingling in Hands and Feet - Blurred Vision # History of Present Illness Elfrieda676 Agustina460 is a 74 year-old nonhispanic white female. Patient has a history of part-time employment (finding), medication review due (situation), exfoliation of teeth due to systemic causes, social isolation (finding), stress (finding). # Social History Patient is married. Patient has never smoked. Patient identifies as heterosexual. Patient comes from a middle socioeconomic background. Patient has completed some college courses. Patient currently has Medicare. # Allergies No Known Allergies. # Medications lisinopril 10 mg oral tablet; tropicamide 5 mg/ml ophthalmic solution; simvastatin 10 mg oral tablet; naproxen sodium 220 mg oral tablet # Assessment and Plan ## Plan The following procedures were conducted: - antigen testing for a public health related pathogen, including coronavirus
[DocumentReference/aadcfe32-4192-0ac3-104b-5d2081fcf3f8#1] Clinical note | 2017-08-18 | part 1 of 2 | 2017-08-18 # Chief Complaint - Tingling in Hands and Feet - Blurred Vision # History of Present Illness Elfrieda676 Agustina460 is a 74 year-old nonhispanic white female. Patient has a history of part-time employment (finding), medication review due (situation), exfoliation of teeth due to systemic causes, social isolation (finding), stress (finding). # Social History Patient is married. Patient has never smoked. Patient identifies as heterosexual. Patient comes from a middle socioeconomic background. Patient has completed some college courses. Patient currently has Medicare. # Allergies No Known Allergies. # Medications lisinopril 10 mg oral tablet; tropicamide 5 mg/ml ophthalmic solution; simvastatin 10 mg oral tablet; naproxen sodium 220 mg oral tablet
[DocumentReference/683ebf8d-8e75-bc00-b7b5-dfc3030feeb7#1] Clinical note | 2021-09-24 | part 1 of 1 | 2021-09-24 # Chief Complaint - Tingling in Hands and Feet - Blurred Vision # History of Present Illness Elfrieda676 Agustina460 is a 78 year-old nonhispanic white female. Patient has a history of part-time employment (finding), medication review due (situation), exfoliation of teeth due to systemic causes, viral sinusitis (disorder), social isolation (finding), stress (finding), dental caries, unspecified. # Social History Patient is married. Patient has never smoked. Patient identifies as heterosexual. Patient comes from a middle socioeconomic background. Patient has completed some college courses. Patient currently has Medicare. # Allergies No Known Allergies. # Medications lisinopril 10 mg oral tablet; tropicamide 5 mg/ml ophthalmic solution; simvastatin 10 mg oral tablet; naproxen sodium 220 mg oral tablet # Assessment and Plan ## Plan The following procedures were conducted: - antigen testing for a public health related pathogen, including coronavirus
[DocumentReference/0675a98c-4791-cf8e-7b0f-dc439708efc3#1] Clinical note | 2016-08-12 | part 1 of 1 | 2016-08-12 # Chief Complaint - Tingling in Hands and Feet - Blurred Vision # History of Present Illness Elfrieda676 Agustina460 is a 73 year-old nonhispanic white female. Patient has a history of medication review due (situation), exfoliation of teeth due to systemic causes. # Social History Patient is married. Patient has never smoked. Patient identifies as heterosexual. Patient comes from a middle socioeconomic background. Patient has completed some college courses. Patient currently has Medicare. # Allergies No Known Allergies. # Medications simvastatin 10 mg oral tablet; naproxen sodium 220 mg oral tablet # Assessment and Plan Patient is presenting with part-time employment (finding), social isolation (finding), stress (finding). ## Plan The patient was prescribed the following medications: - lisinopril 10 mg oral tablet
[DocumentReference/93f40204-2bac-1c39-974b-4ba7572113ab#1] Clinical note | 2020-04-24 | part 1 of 1 | 2020-04-24 # Chief Complaint - Tingling in Hands and Feet - Blurred Vision # History of Present Illness Elfrieda676 Agustina460 is a 77 year-old nonhispanic white female. Patient has a history of part-time employment (finding), medication review due (situation), exfoliation of teeth due to systemic causes, social isolation (finding), stress (finding). # Social History Patient is married. Patient has never smoked. Patient identifies as heterosexual. Patient comes from a middle socioeconomic background. Patient has completed some college courses. Patient currently has Medicare. # Allergies No Known Allergies. # Medications lisinopril 10 mg oral tablet; tropicamide 5 mg/ml ophthalmic solution; simvastatin 10 mg oral tablet; naproxen sodium 220 mg oral tablet # Assessment and Plan Patient is presenting with viral sinusitis (disorder). ## Plan
[DocumentReference/bda282be-bdf1-3246-771e-3bc0699603dc#1] Clinical note | 2021-01-29 | part 1 of 1 | 2021-01-29 # Chief Complaint - Tingling in Hands and Feet - Blurred Vision # History of Present Illness Elfrieda676 Agustina460 is a 77 year-old nonhispanic white female. Patient has a history of part-time employment (finding), medication review due (situation), exfoliation of teeth due to systemic causes, viral sinusitis (disorder), social isolation (finding), stress (finding), dental caries, unspecified. # Social History Patient is married. Patient has never smoked. Patient identifies as heterosexual. Patient comes from a middle socioeconomic background. Patient has completed some college courses. Patient currently has Medicare. # Allergies No Known Allergies. # Medications lisinopril 10 mg oral tablet; tropicamide 5 mg/ml ophthalmic solution; simvastatin 10 mg oral tablet; naproxen sodium 220 mg oral tablet # Assessment and Plan ## Plan Patient was given the following immunizations: covid-19, mrna, lnp-s, pf, 30 mcg/0.3 ml dose.
[DocumentReference/7c96b2a0-664a-c09a-3826-cd5ab3641c32#1] Clinical note | 2021-01-08 | part 1 of 1 | 2021-01-08 # Chief Complaint - Tingling in Hands and Feet - Blurred Vision # History of Present Illness Elfrieda676 Agustina460 is a 77 year-old nonhispanic white female. Patient has a history of part-time employment (finding), medication review due (situation), exfoliation of teeth due to systemic causes, viral sinusitis (disorder), social isolation (finding), stress (finding), dental caries, unspecified. # Social History Patient is married. Patient has never smoked. Patient identifies as heterosexual. Patient comes from a middle socioeconomic background. Patient has completed some college courses. Patient currently has Medicare. # Allergies No Known Allergies. # Medications lisinopril 10 mg oral tablet; tropicamide 5 mg/ml ophthalmic solution; simvastatin 10 mg oral tablet; naproxen sodium 220 mg oral tablet # Assessment and Plan ## Plan Patient was given the following immunizations: covid-19, mrna, lnp-s, pf, 30 mcg/0.3 ml dose.
[DocumentReference/84a2c66a-0342-4445-005b-c815a813d9ff#1] Clinical note | 2023-09-22 | part 1 of 2 | 2023-09-22 # Chief Complaint - Tingling in Hands and Feet - Blurred Vision # History of Present Illness Elfrieda676 Agustina460 is a 80 year-old nonhispanic white female. Patient has a history of part-time employment (finding), medication review due (situation), exfoliation of teeth due to systemic causes, viral sinusitis (disorder), myocardial infarction (disorder), social isolation (finding), stress (finding), dental caries, unspecified. # Social History Patient is married. Patient has never smoked. Patient identifies as heterosexual. Patient comes from a middle socioeconomic background. Patient has completed some college courses. Patient currently has Medicare. # Allergies No Known Allergies. # Medications lisinopril 10 mg oral tablet; tropicamide 5 mg/ml ophthalmic solution; simvastatin 10 mg oral tablet; heparin sodium, porcine 100 unt/ml injectable solution; nitroglycerin 0.4 mg sublingual tablet; aspirin 325 mg oral tablet; clopidogrel 300 mg oral tablet; naproxen sodium 220 mg oral tablet
[DocumentReference/e9e02006-0dcf-6144-6100-557aa8021894#1] Clinical note | 2024-09-27 | part 1 of 2 | 2024-09-27 # Chief Complaint - Tingling in Hands and Feet - Blurred Vision # History of Present Illness Elfrieda676 Agustina460 is a 81 year-old nonhispanic white female. Patient has a history of part-time employment (finding), medication review due (situation), exfoliation of teeth due to systemic causes, viral sinusitis (disorder), myocardial infarction (disorder), social isolation (finding), stress (finding), dental caries, unspecified. # Social History Patient is married. Patient has never smoked. Patient identifies as heterosexual. Patient comes from a middle socioeconomic background. Patient has completed some college courses. Patient currently has Medicare. # Allergies No Known Allergies. # Medications lisinopril 10 mg oral tablet; tropicamide 5 mg/ml ophthalmic solution; simvastatin 10 mg oral tablet; heparin sodium, porcine 100 unt/ml injectable solution; nitroglycerin 0.4 mg sublingual tablet; aspirin 325 mg oral tablet; clopidogrel 300 mg oral tablet; naproxen sodium 220 mg oral tablet; alendronic acid 10 mg oral tablet
```

</details>

label: s
note: The cited immunization (Influenza, split virus, trivalent, PF, CVX 140, 2025-10-03, completed) falls after 2025-10-01 and is the only Immunization card seen; the COVID doses in notes are from 2021.

## 10. `last-er-visit:8ff46e01#0#0`

Question: Why was the patient last seen in the emergency department, and when?

Answer: **The patient's most recent emergency department visit was an emergency room admission on 2025-11-10 at Fitchburg Outpatient Clinic, with the reason recorded as myocardial infarction (disorder).** An acute non-ST segment elevation myocardial infarction with onset 2025-11-10 is also recorded as active.

Cards this sentence cites:

- `[Encounter/8ff46e01-0333-fefb-bdb4-35663b36a4c8]` Encounter | 2025-11-10 | Emergency room admission (procedure) | class EMER | reason: Myocardial infarction (disorder) | at Fitchburg Outpatient Clinic

<details><summary>Everything the model saw (35 cards)</summary>

```text
[Condition/8ff46e01-0333-fefb-e078-a2c79f9b5570] Condition | onset 2025-11-10 | History of myocardial infarction (situation) | clinical status active | SNOMED 399211009
[Condition/8ff46e01-0333-fefb-ca9a-9c89d481d534] Condition | onset 2025-11-10 | Acute non-ST segment elevation myocardial infarction (disorder) | clinical status active | SNOMED 401314000
[Condition/8ff46e01-0333-fefb-f69f-b001b28f2b81] Condition | onset 2023-12-27 | Full-time employment (finding) | clinical status active | SNOMED 160903007
[Condition/8ff46e01-0333-fefb-d37b-fa17bc4619e6] Condition | onset 2023-12-27 | Hyperlipidemia (disorder) | clinical status active | SNOMED 55822004
[Condition/8ff46e01-0333-fefb-1085-7240f563162c] Condition | onset 2023-12-27 | Anemia (disorder) | clinical status active | SNOMED 271737000
[Condition/8ff46e01-0333-fefb-0d5f-96af345c8178] Condition | onset 2023-12-27 | Prediabetes (finding) | clinical status active | SNOMED 714628002
[Condition/8ff46e01-0333-fefb-a724-e7508612ceb2] Condition | onset 2015-12-19 | History of tubal ligation (situation) | clinical status active | SNOMED 267020005
[Condition/8ff46e01-0333-fefb-c4b8-0da5f4d9d6af] Condition | onset 2010-09-29 | Stress (finding) | clinical status active | SNOMED 73595000
[Condition/8ff46e01-0333-fefb-3eac-29a6b80382d5] Condition | onset 1998-06-27 | Recurrent urinary tract infection (disorder) | clinical status active | SNOMED 197927001
[Condition/8ff46e01-0333-fefb-1001-1cc553e61d65] Condition | onset 1998-02-04 | Only received primary school education (finding) | clinical status active | SNOMED 224295006
[Condition/8ff46e01-0333-fefb-2118-3da43e594952] Condition | onset 1995-01-18 | Risk activity involvement (finding) | clinical status active | SNOMED 160968000
[Condition/8ff46e01-0333-fefb-400e-c9db591e5ada] Condition | onset 1988-12-14 | Gingivitis (disorder) | clinical status active | SNOMED 66383009
[Condition/8ff46e01-0333-fefb-6f8d-08005729c21a] Condition | onset 1980-10-17 | History of seizure (situation) | clinical status active | SNOMED 1290882004
[Condition/8ff46e01-0333-fefb-334a-c4ab11856973] Condition | onset 1980-10-17 | Seizure disorder (disorder) | clinical status active | SNOMED 128613002
[Condition/8ff46e01-0333-fefb-493a-f8d458075b36] Condition | onset 1980-04-22 | Chronic sinusitis (disorder) | clinical status active | SNOMED 40055000
[MedicationRequest/8ff46e01-0333-fefb-081b-4d95e98b7814] MedicationRequest | prescribed 2026-01-16 | Simvastatin 10 MG Oral Tablet | status active | reason: Hyperlipidemia (disorder) | RxNorm 314231
[MedicationRequest/8ff46e01-0333-fefb-cca1-202b10a1b90d] MedicationRequest | prescribed 2025-11-10 | aspirin 81 MG Oral Tablet | status active | RxNorm 243670
[MedicationRequest/8ff46e01-0333-fefb-6306-60b207f6bcda] MedicationRequest | prescribed 2025-11-10 | rosuvastatin calcium 10 MG Oral Tablet | status active | RxNorm 859747
[MedicationRequest/8ff46e01-0333-fefb-5a32-7c872c74242b] MedicationRequest | prescribed 2025-11-10 | atenolol 50 MG Oral Tablet | status active | RxNorm 197381
[MedicationRequest/8ff46e01-0333-fefb-5632-79d28eb2f69d] MedicationRequest | prescribed 2025-11-10 | prasugrel 10 MG Oral Tablet | status active | RxNorm 855812
[MedicationRequest/8ff46e01-0333-fefb-0f09-741ffc0ecb79] MedicationRequest | prescribed 2025-11-10 | lisinopril 10 MG Oral Tablet | status active | RxNorm 314076
[Encounter/8ff46e01-0333-fefb-2842-108bae2a93b7] Encounter | 2026-01-16 | Follow-up encounter (procedure) | class AMB | reason: Hyperlipidemia (disorder) | at STEWARD HOLY FAMILY HOSPITAL INC
[Encounter/8ff46e01-0333-fefb-deac-7d54a2e717b0] Encounter | 2025-12-31 | General examination of patient (procedure) | class AMB | at GREATER LAWRENCE FAMILY HEALTH CENTER INC
[Encounter/8ff46e01-0333-fefb-bdb4-35663b36a4c8] Encounter | 2025-11-10 | Emergency room admission (procedure) | class EMER | reason: Myocardial infarction (disorder) | at Fitchburg Outpatient Clinic
[Immunization/8ff46e01-0333-fefb-0b35-b6fa97749e42] Immunization | 2025-12-31 | Influenza, split virus, trivalent, PF | status completed | CVX 140
[Encounter/8ff46e01-0333-fefb-cfd6-fbd730ce6fea] Encounter | 1980-10-17 | Emergency room admission (procedure) | class EMER | reason: Seizure disorder (disorder) | at LAKEVIEW HOUSE SKLD NRSG  AND RESIDENTIAL CARE FAC
[Encounter/8ff46e01-0333-fefb-2d65-6b97d180d22e] Encounter | 2019-02-22 | Emergency room admission (procedure) | class EMER | reason: Sprain (morphologic abnormality) | at LAKEVIEW HOUSE SKLD NRSG  AND RESIDENTIAL CARE FAC
[Encounter/8ff46e01-0333-fefb-f0e5-0204fb684bf9] Encounter | 2015-12-19 | Admission to surgical department (procedure) | class IMP | reason: Sterilization requested (situation) | at STEWARD HOLY FAMILY HOSPITAL INC
[Encounter/8ff46e01-0333-fefb-1dd1-2605caf4eb4e] Encounter | 2022-02-08 | Emergency room admission (procedure) | class EMER | reason: Sprain (morphologic abnormality) | at LAKEVIEW HOUSE SKLD NRSG  AND RESIDENTIAL CARE FAC
[Observation/8ff46e01-0333-fefb-816d-363218ace13b] Observation (survey) | 2025-12-31 | Protocol for Responding to and Assessing Patients' Assets, Risks, and Experiences [PRAPARE] = Within the last year, have you been afraid of your partner or ex-partner No; Do you feel physically and emotionally safe where you currently live [PRAPARE] Yes; Are you a refugee No; Have you spent more than 2 nights in a row in a jail, prison, detention center, or juvenile correctional facility in past 1 year [PRAPARE] No; Stress level Somewhat; How often do you see or talk to people that you care about and feel close to [PRAPARE] 5 or more times a week; Has lack of transportation kept you from medical appointments, meetings, work, or from getting things needed for daily living No; Have you or any family members you live with been unable to get any of the following when it was really needed in past 1 year [PRAPARE] I choose not to answer this question; What was your best estimate of the total income of all family members from all sources, before taxes, in last year [PhenX] 90342 /a; Primary insurance Medicare; Employment status - current Full-time work; Highest level of education Less than high school degree; Address 942 Herzog Highlands Suite 0; Are you worried about losing your housing [PRAPARE] No; Housing status I have housing; How many people are living or staying at this address [#] 1 {#}; Preferred language English; Discharged from the U.S. Armed Forces No; Has season or migrant farm work been your or your family's main source of income at any point in past 2 years [PRAPARE] No; Race White; Hispanic or Latino No | status final | LOINC 93025-5
[Observation/8ff46e01-0333-fefb-cb14-9f790999159d] Observation (survey) | 2023-12-27 | Protocol for Responding to and Assessing Patients' Assets, Risks, and Experiences [PRAPARE] = Within the last year, have you been afraid of your partner or ex-partner No; Do you feel physically and emotionally safe where you currently live [PRAPARE] Yes; Are you a refugee No; Have you spent more than 2 nights in a row in a jail, prison, detention center, or juvenile correctional facility in past 1 year [PRAPARE] No; Stress level Somewhat; How often do you see or talk to people that you care about and feel close to [PRAPARE] 5 or more times a week; Has lack of transportation kept you from medical appointments, meetings, work, or from getting things needed for daily living No; Have you or any family members you live with been unable to get any of the following when it was really needed in past 1 year [PRAPARE] I choose not to answer this question; What was your best estimate of the total income of all family members from all sources, before taxes, in last year [PhenX] 90342 /a; Primary insurance Medicare; Employment status - current Full-time work; Highest level of education Less than high school degree; Address 942 Herzog Highlands Suite 0; Are you worried about losing your housing [PRAPARE] No; Housing status I have housing; How many people are living or staying at this address [#] 1 {#}; Preferred language English; Discharged from the U.S. Armed Forces No; Has season or migrant farm work been your or your family's main source of income at any point in past 2 years [PRAPARE] No; Race White; Hispanic or Latino No | status final | LOINC 93025-5
[Observation/8ff46e01-0333-fefb-21a5-1c5b6786878d] Observation (survey) | 2021-12-22 | Protocol for Responding to and Assessing Patients' Assets, Risks, and Experiences [PRAPARE] = Within the last year, have you been afraid of your partner or ex-partner No; Do you feel physically and emotionally safe where you currently live [PRAPARE] Yes; Are you a refugee No; Have you spent more than 2 nights in a row in a jail, prison, detention center, or juvenile correctional facility in past 1 year [PRAPARE] No; Stress level A little bit; How often do you see or talk to people that you care about and feel close to [PRAPARE] 5 or more times a week; Has lack of transportation kept you from medical appointments, meetings, work, or from getting things needed for daily living No; Have you or any family members you live with been unable to get any of the following when it was really needed in past 1 year [PRAPARE] I choose not to answer this question; What was your best estimate of the total income of all family members from all sources, before taxes, in last year [PhenX] 90342 /a; Primary insurance Medicare; Employment status - current Part-time or temporary work; Highest level of education Less than high school degree; Address 942 Herzog Highlands Suite 0; Are you worried about losing your housing [PRAPARE] No; Housing status I have housing; How many people are living or staying at this address [#] 1 {#}; Preferred language English; Discharged from the U.S. Armed Forces No; Has season or migrant farm work been your or your family's main source of income at any point in past 2 years [PRAPARE] No; Race White; Hispanic or Latino No | status final | LOINC 93025-5
[Condition/8ff46e01-0333-fefb-c542-076c5124eeb2] Condition | onset 2017-03-01 | Medication review due (situation) | clinical status resolved | resolved 2023-12-27 | SNOMED 314529007
[Condition/8ff46e01-0333-fefb-312f-6e1ca711c649] Condition | onset 2025-12-31 | Medication review due (situation) | clinical status resolved | resolved 2025-12-31 | SNOMED 314529007
[Condition/8ff46e01-0333-fefb-3072-23b1a01874cb] Condition | onset 2010-07-28 | Full-time employment (finding) | clinical status resolved | resolved 2019-12-18 | SNOMED 160903007
```

</details>

label: s
note: Cited card is the 2025-11-10 Emergency room admission, class EMER, reason Myocardial infarction (disorder), at Fitchburg Outpatient Clinic; the other EMER encounters are 2022-02-08, 2019-02-22 and 1980-10-17, so it is the most recent.

## 11. `last-colonoscopy:7280f7f8#0#0`

Question: When was the patient's most recent colonoscopy?

Answer: **The patient's most recent colonoscopy was on 2021-11-28, completed during a check-up encounter for colon cancer screening at LAWRENCE GENERAL HOSPITAL.** A prior colonoscopy was done on 2016-11-02.

Cards this sentence cites:

- `[Procedure/7280f7f8-315d-7c6a-87ff-7a3e1aeca6bb]` Procedure | 2021-11-28 | Colonoscopy (procedure) | status completed | SNOMED 73761001
- `[Encounter/7280f7f8-315d-7c6a-e22e-84f402648ddf]` Encounter | 2021-11-28 | Encounter for check up (procedure) | class AMB | reason: Screening for malignant neoplasm of colon (procedure) | at LAWRENCE GENERAL HOSPITAL
- `[DocumentReference/39105fec-16a0-bb34-7fcf-e3effdf1fcff#1]` Clinical note | 2021-11-28 | part 1 of 1 | 2021-11-28 # Chief Complaint - Memory Loss - Decreased in Judgement # History of Present Illness Neil122 is a 75 year-old nonhispanic white male. Patient has a history of medication review due (situation), unemployed (finding), victim of intimate partner abuse (finding), viral sinusitis (disorder), dental caries, unspecified, part-time employment (finding), fever (finding), sputum finding (finding), full-time employment (finding), cough (finding), acute infective cystitis (disorder), suspected disease caused by severe acute respiratory coronavirus 2 (situation), disease caused by severe acute respiratory syndrome coronavirus 2 (disorder), stress (finding), social isolation (finding). # Social History Patient is married. Patient has a documented history of opioid addiction. Patient has never smoked. Patient identifies as heterosexual. Patient comes from a low socioeconomic background. Patient did not finish high school. Patient currently has Medicare. # Allergies No Known Allergies. # Medications simvastatin 10 mg oral tablet; acetaminophen 325 mg / oxycodone hydrochloride 10 mg oral tablet [percocet]; ibuprofen 400 mg oral tablet [ibu]; acetaminophen 325 mg oral tablet [tylenol]; ciprofloxacin 500 mg oral tablet # Assessment and Plan ## Plan The following procedures were conducted: - colonoscopy (procedure)

<details><summary>Everything the model saw (43 cards)</summary>

```text
[Condition/7280f7f8-315d-7c6a-5183-1fc53612d856] Condition | onset 2026-04-12 | Alzheimer's disease (disorder) | clinical status active | SNOMED 26929004
[Condition/7280f7f8-315d-7c6a-069f-25fdb34e3e53] Condition | onset 2025-04-06 | Stress (finding) | clinical status active | SNOMED 73595000
[Condition/7280f7f8-315d-7c6a-06ae-a26712c6cfb7] Condition | onset 2024-03-31 | Full-time employment (finding) | clinical status active | SNOMED 160903007
[Condition/7280f7f8-315d-7c6a-84b2-d6045a9b8deb] Condition | onset 2018-11-12 | Abnormal findings diagnostic imaging heart+coronary circulat (finding) | clinical status active | SNOMED 274531002
[Condition/7280f7f8-315d-7c6a-60b8-1b2b3b190d66] Condition | onset 2018-11-04 | Ischemic heart disease (disorder) | clinical status active | SNOMED 414545008
[Condition/7280f7f8-315d-7c6a-eee1-33d3eda16b26] Condition | onset 2014-02-16 | Chronic low back pain (finding) | clinical status active | SNOMED 278860009
[Condition/7280f7f8-315d-7c6a-23b9-2a24d0c43093] Condition | onset 2014-02-16 | Chronic neck pain (finding) | clinical status active | SNOMED 1121000119107
[Condition/7280f7f8-315d-7c6a-f371-666500850eb4] Condition | onset 2014-02-02 | Gingivitis (disorder) | clinical status active | SNOMED 66383009
[Condition/7280f7f8-315d-7c6a-b5ea-aa0955ebc2c7] Condition | onset 2010-01-10 | Hyperlipidemia (disorder) | clinical status active | SNOMED 55822004
[Condition/7280f7f8-315d-7c6a-929f-e845c91bba18] Condition | onset 1993-02-06 | Dependent drug abuse (disorder) | clinical status active | SNOMED 6525002
[Condition/7280f7f8-315d-7c6a-6159-244929402415] Condition | onset 1991-07-09 | Chronic pain (finding) | clinical status active | SNOMED 82423001
[Condition/7280f7f8-315d-7c6a-7561-551dd4fb980c] Condition | onset 1990-11-11 | Has a criminal record (finding) | clinical status active | SNOMED 266948004
[Condition/7280f7f8-315d-7c6a-69cb-9f6bde195716] Condition | onset 1990-10-25 | Impacted molars (disorder) | clinical status active | SNOMED 196416002
[Condition/7280f7f8-315d-7c6a-e183-7fc41f06abde] Condition | onset 1990-02-06 | Chronic intractable migraine without aura (disorder) | clinical status active | SNOMED 124171000119105
[Condition/7280f7f8-315d-7c6a-57cd-16215a141add] Condition | onset 1988-11-06 | Body mass index 30+ - obesity (finding) | clinical status active | SNOMED 162864005
[Condition/7280f7f8-315d-7c6a-7c25-7a247f43e721] Condition | onset 1981-01-18 | Anemia (disorder) | clinical status active | SNOMED 271737000
[Condition/7280f7f8-315d-7c6a-50ac-70390520f5d8] Condition | onset 1981-01-18 | Prediabetes (finding) | clinical status active | SNOMED 714628002
[Condition/7280f7f8-315d-7c6a-a35c-5f2c4404e1cd] Condition | onset 1971-02-18 | Chronic sinusitis (disorder) | clinical status active | SNOMED 40055000
[Condition/7280f7f8-315d-7c6a-cf3c-1559c1e270a8] Condition | onset 1964-12-20 | Housing unsatisfactory (finding) | clinical status active | SNOMED 105531004
[Condition/7280f7f8-315d-7c6a-3735-89103641aea2] Condition | onset 1964-12-20 | Only received primary school education (finding) | clinical status active | SNOMED 224295006
[MedicationRequest/7280f7f8-315d-7c6a-d103-5f5cf25ace53] MedicationRequest | prescribed 2026-04-13 | Simvastatin 10 MG Oral Tablet | status active | reason: Hyperlipidemia (disorder) | RxNorm 314231
[MedicationRequest/7280f7f8-315d-7c6a-dd3c-435b565b36d4] MedicationRequest | prescribed 2026-04-12 | Ibuprofen 400 MG Oral Tablet [Ibu] | status active | RxNorm 206905
[MedicationRequest/7280f7f8-315d-7c6a-698d-8c3f4a330263] MedicationRequest | prescribed 2026-04-12 | Acetaminophen 325 MG / Oxycodone Hydrochloride 10 MG Oral Tablet [Percocet] | status active | RxNorm 1049625
[MedicationRequest/7280f7f8-315d-7c6a-53dc-677516ba315e] MedicationRequest | prescribed 2026-04-12 | Galantamine 4 MG Oral Tablet | status active | reason: Alzheimer's disease (disorder) | RxNorm 310436
[MedicationRequest/7280f7f8-315d-7c6a-21fd-127361ce4eae] MedicationRequest | prescribed 2026-04-12 | Acetaminophen 325 MG Oral Tablet [Tylenol] | status active | RxNorm 209387
[MedicationRequest/7280f7f8-315d-7c6a-e1ca-6672a64e96d6] MedicationRequest | prescribed 2018-11-11 | Simvastatin 20 MG Oral Tablet | status active | RxNorm 312961
[MedicationRequest/7280f7f8-315d-7c6a-d3dc-bf227b26b9de] MedicationRequest | prescribed 2018-11-11 | Nitroglycerin 0.4 MG/ACTUAT Mucosal Spray | status active | RxNorm 705129
[MedicationRequest/7280f7f8-315d-7c6a-40f0-094ac0d35606] MedicationRequest | prescribed 2018-11-11 | Clopidogrel 75 MG Oral Tablet | status active | RxNorm 309362
[MedicationRequest/7280f7f8-315d-7c6a-344e-7b21fe48818f] MedicationRequest | prescribed 2018-11-11 | 24 HR metoprolol succinate 100 MG Extended Release Oral Tablet | status active | RxNorm 866412
[Encounter/7280f7f8-315d-7c6a-ddbc-56619e72a429] Encounter | 2026-04-26 | Encounter for check up (procedure) | class AMB | at LAWRENCE GENERAL HOSPITAL
[Encounter/7280f7f8-315d-7c6a-e49f-7858d34e1916] Encounter | 2026-04-13 | Follow-up encounter (procedure) | class AMB | reason: Hyperlipidemia (disorder) | at LAWRENCE GENERAL HOSPITAL
[Encounter/7280f7f8-315d-7c6a-79c7-b2135168eae6] Encounter | 2026-04-12 | General examination of patient (procedure) | class AMB | at HOLY FAMILY MEDICAL SPECIALTY PRACTICE PLLC
[Immunization/7280f7f8-315d-7c6a-89f5-f28321d6dbe8] Immunization | 2026-04-12 | Influenza, split virus, trivalent, PF | status completed | CVX 140
[Procedure/7280f7f8-315d-7c6a-6137-837ed6116ed6] Procedure | 2016-11-02 | Colonoscopy (procedure) | status completed | SNOMED 73761001
[Procedure/7280f7f8-315d-7c6a-87ff-7a3e1aeca6bb] Procedure | 2021-11-28 | Colonoscopy (procedure) | status completed | SNOMED 73761001
[DocumentReference/e6c70e5e-0f2d-6577-0601-986c65636198#1] Clinical note | 2016-11-02 | part 1 of 1 | 2016-11-02 # Chief Complaint - Memory Loss - Decreased in Judgement # History of Present Illness Neil122 is a 70 year-old nonhispanic white male. Patient has a history of medication review due (situation), unemployed (finding), victim of intimate partner abuse (finding), stress (finding). # Social History Patient is married. Patient has a documented history of opioid addiction. Patient has never smoked. Patient identifies as heterosexual. Patient comes from a low socioeconomic background. Patient did not finish high school. Patient currently has Medicare. # Allergies No Known Allergies. # Medications simvastatin 10 mg oral tablet; acetaminophen 325 mg / oxycodone hydrochloride 10 mg oral tablet [percocet]; ibuprofen 400 mg oral tablet [ibu]; acetaminophen 325 mg oral tablet [tylenol] # Assessment and Plan ## Plan The following procedures were conducted: - colonoscopy (procedure)
[DocumentReference/39105fec-16a0-bb34-7fcf-e3effdf1fcff#1] Clinical note | 2021-11-28 | part 1 of 1 | 2021-11-28 # Chief Complaint - Memory Loss - Decreased in Judgement # History of Present Illness Neil122 is a 75 year-old nonhispanic white male. Patient has a history of medication review due (situation), unemployed (finding), victim of intimate partner abuse (finding), viral sinusitis (disorder), dental caries, unspecified, part-time employment (finding), fever (finding), sputum finding (finding), full-time employment (finding), cough (finding), acute infective cystitis (disorder), suspected disease caused by severe acute respiratory coronavirus 2 (situation), disease caused by severe acute respiratory syndrome coronavirus 2 (disorder), stress (finding), social isolation (finding). # Social History Patient is married. Patient has a documented history of opioid addiction. Patient has never smoked. Patient identifies as heterosexual. Patient comes from a low socioeconomic background. Patient did not finish high school. Patient currently has Medicare. # Allergies No Known Allergies. # Medications simvastatin 10 mg oral tablet; acetaminophen 325 mg / oxycodone hydrochloride 10 mg oral tablet [percocet]; ibuprofen 400 mg oral tablet [ibu]; acetaminophen 325 mg oral tablet [tylenol]; ciprofloxacin 500 mg oral tablet # Assessment and Plan ## Plan The following procedures were conducted: - colonoscopy (procedure)
[Encounter/7280f7f8-315d-7c6a-e22e-84f402648ddf] Encounter | 2021-11-28 | Encounter for check up (procedure) | class AMB | reason: Screening for malignant neoplasm of colon (procedure) | at LAWRENCE GENERAL HOSPITAL
[Encounter/7280f7f8-315d-7c6a-88f9-9f28494785cd] Encounter | 2021-10-31 | Admission to hospice (procedure) | class HH | reason: Alzheimer's disease (disorder) | at ALL CARE HOSPICE INC.
[Encounter/7280f7f8-315d-7c6a-be52-abb22de90c9b] Encounter | 2016-11-02 | Encounter for check up (procedure) | class AMB | reason: Screening for malignant neoplasm of colon (procedure) | at LAWRENCE GENERAL HOSPITAL
[Immunization/7280f7f8-315d-7c6a-2c12-076f4ebe4a00] Immunization | 2021-04-11 | COVID-19, mRNA, LNP-S, PF, 30 mcg/0.3 mL dose | status completed | CVX 208
[Immunization/7280f7f8-315d-7c6a-03fb-59ac9d44c133] Immunization | 2021-03-21 | COVID-19, mRNA, LNP-S, PF, 30 mcg/0.3 mL dose | status completed | CVX 208
[Procedure/7280f7f8-315d-7c6a-c5ad-1c2513b2fb89] Procedure | 2021-11-20 | Patient discharge (procedure) | status completed | SNOMED 58000006
```

</details>

label: s
note: Only two colonoscopy procedures exist (2016-11-02, 2021-11-28), so 2021-11-28 is the most recent and is completed; the cited same-day encounter is a check-up for colon cancer screening at LAWRENCE GENERAL HOSPITAL, and the same-day note says a colonoscopy was conducted.

## 12. `vaccines-last-year:9292c3d5#0#0`

Question: Which vaccines did the patient receive in the last year?

Answer: **In the last year, the record shows one vaccine: Influenza, split virus, trivalent, PF (CVX 140), given on 2026-04-26 with status completed.**

Cards this sentence cites:

- `[Immunization/9292c3d5-3db6-f4f9-2e74-b2ab508532b8]` Immunization | 2026-04-26 | Influenza, split virus, trivalent, PF | status completed | CVX 140

<details><summary>Everything the model saw (31 cards)</summary>

```text
[Condition/9292c3d5-3db6-f4f9-b5ec-3a44e8649597] Condition | onset 2026-04-26 | Full-time employment (finding) | clinical status active | SNOMED 160903007
[Condition/9292c3d5-3db6-f4f9-861b-f7159312202f] Condition | onset 2026-04-26 | Medication review due (situation) | clinical status active | SNOMED 314529007
[Condition/9292c3d5-3db6-f4f9-483e-3d8d3b0f4690] Condition | onset 2026-04-26 | Social isolation (finding) | clinical status active | SNOMED 422650009
[Condition/9292c3d5-3db6-f4f9-38dc-147de4ac63a8] Condition | onset 2026-04-26 | Stress (finding) | clinical status active | SNOMED 73595000
[Condition/9292c3d5-3db6-f4f9-5b6c-1c0ed0fd0321] Condition | onset 2020-03-22 | Opioid abuse | clinical status active | SNOMED 5602001
[Condition/9292c3d5-3db6-f4f9-f835-25af6c77c701] Condition | onset 2011-08-22 | History of myocardial infarction (situation) | clinical status active | SNOMED 399211009
[Condition/9292c3d5-3db6-f4f9-54d1-d4b6d2666838] Condition | onset 2011-08-22 | Acute ST segment elevation myocardial infarction (disorder) | clinical status active | SNOMED 401303003
[Condition/9292c3d5-3db6-f4f9-2b48-fd31edda50b0] Condition | onset 2010-03-21 | Anemia (disorder) | clinical status active | SNOMED 271737000
[Condition/9292c3d5-3db6-f4f9-1b0c-65cb31846f75] Condition | onset 2005-05-29 | Prediabetes (finding) | clinical status active | SNOMED 714628002
[Condition/9292c3d5-3db6-f4f9-2a82-9615e45bb615] Condition | onset 1986-05-04 | Educated to high school level (finding) | clinical status active | SNOMED 473461003
[Condition/9292c3d5-3db6-f4f9-24a0-fe08e411b951] Condition | onset 1986-05-04 | Serving in military service (finding) | clinical status active | SNOMED 1187604002
[Condition/9292c3d5-3db6-f4f9-97fc-b779fe5ffdd4] Condition | onset 1985-04-28 | Risk activity involvement (finding) | clinical status active | SNOMED 160968000
[MedicationRequest/9292c3d5-3db6-f4f9-c2ad-ca0afa2369e8] MedicationRequest | prescribed 2011-08-22 | 24 HR metoprolol succinate 50 MG Extended Release Oral Tablet | status active | RxNorm 866436
[MedicationRequest/9292c3d5-3db6-f4f9-b955-8ddb9b72de69] MedicationRequest | prescribed 2011-08-22 | prasugrel 10 MG Oral Tablet | status active | RxNorm 855812
[MedicationRequest/9292c3d5-3db6-f4f9-8b49-28e15899c04a] MedicationRequest | prescribed 2011-08-22 | aspirin 81 MG Oral Tablet | status active | RxNorm 243670
[MedicationRequest/9292c3d5-3db6-f4f9-7675-f5ee99ae0c4e] MedicationRequest | prescribed 2011-08-22 | simvastatin 40 MG Oral Tablet | status active | RxNorm 198211
[MedicationRequest/9292c3d5-3db6-f4f9-2744-8b9a3e3302b8] MedicationRequest | prescribed 2011-08-22 | lisinopril 2.5 MG Oral Tablet | status active | RxNorm 311353
[Encounter/9292c3d5-3db6-f4f9-f8cd-08dfcc81ed12] Encounter | 2026-04-26 | General examination of patient (procedure) | class AMB | at COMMUNITY HEALTH PROGRAMS INC
[Encounter/9292c3d5-3db6-f4f9-2526-cf0c3fc1dcaa] Encounter | 2025-08-10 | Encounter for check up (procedure) | class AMB | reason: Gingivitis (disorder) | at Pittsfield Outpatient Clinic
[Encounter/9292c3d5-3db6-f4f9-d85c-7f88671a1881] Encounter | 2025-08-03 | Encounter for symptom (procedure) | class AMB | reason: Acute viral pharyngitis (disorder) | at Pittsfield Outpatient Clinic
[Immunization/9292c3d5-3db6-f4f9-2e74-b2ab508532b8] Immunization | 2026-04-26 | Influenza, split virus, trivalent, PF | status completed | CVX 140
[DocumentReference/960a81cd-5ce7-7531-422f-127dc3be48f4#1] Clinical note | 2021-04-04 | part 1 of 1 | 2021-04-04 # Chief Complaint No complaints. # History of Present Illness Arnold338 is a 53 year-old nonhispanic white male. Patient has a history of severe anxiety (panic) (finding), medication review due (situation), not in labor force (finding), limited social contact (finding), disorder of teeth and/or supporting structures, full-time employment (finding), social isolation (finding), stress (finding). # Social History Patient is single. Patient quit smoking at age 17. Patient identifies as heterosexual. Patient comes from a middle socioeconomic background. Patient has a high school education. Patient currently has Humana. # Allergies No Known Allergies. # Medications No Active Medications. # Assessment and Plan ## Plan Patient was given the following immunizations: covid-19, mrna, lnp-s, pf, 30 mcg/0.3 ml dose.
[DocumentReference/5922e550-66a0-0ffd-b471-f000f8e2d198#1] Clinical note | 2018-03-11 | part 1 of 1 | 2018-03-11 # Chief Complaint No complaints. # History of Present Illness Arnold338 is a 50 year-old nonhispanic white male. Patient has a history of medication review due (situation), disorder of teeth and/or supporting structures, full-time employment (finding), social isolation (finding). # Social History Patient is single. Patient quit smoking at age 17. Patient identifies as heterosexual. Patient comes from a middle socioeconomic background. Patient has a high school education. Patient currently has Humana. # Allergies No Known Allergies. # Medications No Active Medications. # Assessment and Plan Patient is presenting with stress (finding). ## Plan Patient was given the following immunizations: zoster vaccine, live, influenza, split virus, trivalent, pf. The following procedures were conducted: - assessment of health and social care needs (procedure) - depression screening (procedure) - depression screening (procedure) The following lab reports were completed: - basic metabolic panel - blood - lipid panel with direct ldl - serum or plasma - patient health questionnaire 2 item (phq-2) [reported]
[DocumentReference/b0afcae6-490b-fb11-b71d-382273ce441c#1] Clinical note | 2021-03-14 | part 1 of 1 | 2021-03-14 # Chief Complaint No complaints. # History of Present Illness Arnold338 is a 53 year-old nonhispanic white male. Patient has a history of severe anxiety (panic) (finding), medication review due (situation), not in labor force (finding), limited social contact (finding), disorder of teeth and/or supporting structures, full-time employment (finding), social isolation (finding), stress (finding). # Social History Patient is single. Patient quit smoking at age 17. Patient identifies as heterosexual. Patient comes from a middle socioeconomic background. Patient has a high school education. Patient currently has Humana. # Allergies No Known Allergies. # Medications No Active Medications. # Assessment and Plan ## Plan Patient was given the following immunizations: covid-19, mrna, lnp-s, pf, 30 mcg/0.3 ml dose.
[DocumentReference/97aefd74-bc89-27c6-4556-82cd05aa88b4#1] Clinical note | 2016-06-05 | part 1 of 1 | 2016-06-05 # Chief Complaint No complaints. # History of Present Illness Arnold338 is a 48 year-old nonhispanic white male. Patient has a history of medication review due (situation), disorder of teeth and/or supporting structures, full-time employment (finding). # Social History Patient is single. Patient quit smoking at age 17. Patient identifies as heterosexual. Patient comes from a middle socioeconomic background. Patient has a high school education. Patient currently has Humana. # Allergies No Known Allergies. # Medications No Active Medications. # Assessment and Plan Patient is presenting with social isolation (finding). ## Plan
[DocumentReference/2bc93ddb-a0c6-4817-5059-ee42779a0ac3#1] Clinical note | 2016-05-29 | part 1 of 1 | 2016-05-29 # Chief Complaint No complaints. # History of Present Illness Arnold338 is a 48 year-old nonhispanic white male. Patient has a history of medication review due (situation), disorder of teeth and/or supporting structures, full-time employment (finding). # Social History Patient is single. Patient quit smoking at age 17. Patient identifies as heterosexual. Patient comes from a middle socioeconomic background. Patient has a high school education. Patient currently has Humana. # Allergies No Known Allergies. # Medications No Active Medications. # Assessment and Plan ## Plan The patient was placed on a careplan: - respiratory therapy (procedure)
[DocumentReference/19e0c452-e4de-9759-abf6-d32dbf56ecdd#1] Clinical note | 1985-04-28 | part 1 of 1 | 1985-04-28 # Chief Complaint No complaints. # History of Present Illness Arnold338 is a 17 year-old nonhispanic white male. Patient has a history of disorder of teeth and/or supporting structures. # Social History Patient quit smoking at age 17. Patient identifies as heterosexual. Patient comes from a middle socioeconomic background. Patient currently has NO INSURANCE. # Allergies No Known Allergies. # Medications No Active Medications. # Assessment and Plan Patient is presenting with risk activity involvement (finding). ## Plan
[DocumentReference/10751b31-4607-0b97-c565-c63a6a33254c#1] Clinical note | 1986-05-04 | part 1 of 1 | 1986-05-04 # Chief Complaint No complaints. # History of Present Illness Arnold338 is a 18 year-old nonhispanic white male. Patient has a history of disorder of teeth and/or supporting structures. # Social History Patient quit smoking at age 17. Patient identifies as heterosexual. Patient comes from a middle socioeconomic background. Patient has a high school education. Patient currently has NO INSURANCE. # Allergies No Known Allergies. # Medications No Active Medications. # Assessment and Plan Patient is presenting with serving in military service (finding), educated to high school level (finding). ## Plan
[DocumentReference/43776b3d-60c3-c1e3-e18c-cc61e6477899#1] Clinical note | 2020-03-22 | part 1 of 2 | 2020-03-22 # Chief Complaint No complaints. # History of Present Illness Arnold338 is a 52 year-old nonhispanic white male. Patient has a history of medication review due (situation), not in labor force (finding), limited social contact (finding), disorder of teeth and/or supporting structures, full-time employment (finding), social isolation (finding), stress (finding). # Social History Patient is single. Patient quit smoking at age 17. Patient identifies as heterosexual. Patient comes from a middle socioeconomic background. Patient has a high school education. Patient currently has Humana. # Allergies No Known Allergies. # Medications No Active Medications.
[DocumentReference/94a94abd-5518-5d39-0216-86e817616840#1] Clinical note | 2022-04-03 | part 1 of 1 | 2022-04-03 # Chief Complaint No complaints. # History of Present Illness Arnold338 is a 54 year-old nonhispanic white male. Patient has a history of severe anxiety (panic) (finding), medication review due (situation), not in labor force (finding), limited social contact (finding), disorder of teeth and/or supporting structures, full-time employment (finding), social isolation (finding), stress (finding). # Social History Patient is single. Patient quit smoking at age 17. Patient identifies as heterosexual. Patient comes from a middle socioeconomic background. Patient has a high school education. Patient currently has Humana. # Allergies No Known Allergies. # Medications No Active Medications. # Assessment and Plan ## Plan Patient was given the following immunizations: influenza, split virus, trivalent, pf. The following procedures were conducted: - assessment of health and social care needs (procedure) - assessment of anxiety (procedure) The following lab reports were completed: - basic metabolic panel - blood - generalized anxiety disorder 7 item (gad-7)
[DocumentReference/62150bd0-ea5c-0b8b-1705-b6da0e882541#1] Clinical note | 2021-03-28 | part 1 of 1 | 2021-03-28 # Chief Complaint No complaints. # History of Present Illness Arnold338 is a 53 year-old nonhispanic white male. Patient has a history of severe anxiety (panic) (finding), medication review due (situation), not in labor force (finding), limited social contact (finding), disorder of teeth and/or supporting structures, full-time employment (finding), social isolation (finding), stress (finding). # Social History Patient is single. Patient quit smoking at age 17. Patient identifies as heterosexual. Patient comes from a middle socioeconomic background. Patient has a high school education. Patient currently has Humana. # Allergies No Known Allergies. # Medications No Active Medications. # Assessment and Plan Patient is presenting with full-time employment (finding). ## Plan Patient was given the following immunizations: influenza, split virus, trivalent, pf. The following procedures were conducted: - assessment of health and social care needs (procedure) - assessment of anxiety (procedure) - screening for domestic abuse (procedure) The following lab reports were completed: - basic metabolic panel - blood - lipid panel with direct ldl - serum or plasma - generalized anxiety disorder 7 item (gad-7) - humiliation, afraid, rape, and kick questionnaire [hark]
```

</details>

label: s
note: The only Immunization card is Influenza, split virus, trivalent, PF, CVX 140, 2026-04-26, completed; every other immunization the notes mention (2018, 2021, 2022) is before 2025-10-01, so 'one vaccine' holds.

## 13. `lay-a-heart-attack:8ff46e01#0#2`

Question: Has the patient ever been diagnosed with a heart attack? If so, when?

Answer: Yes, the patient was diagnosed with a myocardial infarction (heart attack) with onset 2025-11-10, specifically an acute non-ST segment elevation myocardial infarction. She presented to the emergency room on 2025-11-10 with myocardial infarction as the reason for admission. **The myocardial infarction (disorder) entry is marked resolved on 2025-11-10, while the acute NSTEMI and history of myocardial infarction entries remain listed as active.**

Cards this sentence cites:

- `[Condition/8ff46e01-0333-fefb-d46d-069e32dc10df]` Condition | onset 2025-11-10 | Myocardial infarction (disorder) | clinical status resolved | resolved 2025-11-10 | SNOMED 22298006
- `[Condition/8ff46e01-0333-fefb-ca9a-9c89d481d534]` Condition | onset 2025-11-10 | Acute non-ST segment elevation myocardial infarction (disorder) | clinical status active | SNOMED 401314000
- `[Condition/8ff46e01-0333-fefb-e078-a2c79f9b5570]` Condition | onset 2025-11-10 | History of myocardial infarction (situation) | clinical status active | SNOMED 399211009

<details><summary>Everything the model saw (35 cards)</summary>

```text
[Condition/8ff46e01-0333-fefb-e078-a2c79f9b5570] Condition | onset 2025-11-10 | History of myocardial infarction (situation) | clinical status active | SNOMED 399211009
[Condition/8ff46e01-0333-fefb-ca9a-9c89d481d534] Condition | onset 2025-11-10 | Acute non-ST segment elevation myocardial infarction (disorder) | clinical status active | SNOMED 401314000
[Condition/8ff46e01-0333-fefb-f69f-b001b28f2b81] Condition | onset 2023-12-27 | Full-time employment (finding) | clinical status active | SNOMED 160903007
[Condition/8ff46e01-0333-fefb-d37b-fa17bc4619e6] Condition | onset 2023-12-27 | Hyperlipidemia (disorder) | clinical status active | SNOMED 55822004
[Condition/8ff46e01-0333-fefb-1085-7240f563162c] Condition | onset 2023-12-27 | Anemia (disorder) | clinical status active | SNOMED 271737000
[Condition/8ff46e01-0333-fefb-0d5f-96af345c8178] Condition | onset 2023-12-27 | Prediabetes (finding) | clinical status active | SNOMED 714628002
[Condition/8ff46e01-0333-fefb-a724-e7508612ceb2] Condition | onset 2015-12-19 | History of tubal ligation (situation) | clinical status active | SNOMED 267020005
[Condition/8ff46e01-0333-fefb-c4b8-0da5f4d9d6af] Condition | onset 2010-09-29 | Stress (finding) | clinical status active | SNOMED 73595000
[Condition/8ff46e01-0333-fefb-3eac-29a6b80382d5] Condition | onset 1998-06-27 | Recurrent urinary tract infection (disorder) | clinical status active | SNOMED 197927001
[Condition/8ff46e01-0333-fefb-1001-1cc553e61d65] Condition | onset 1998-02-04 | Only received primary school education (finding) | clinical status active | SNOMED 224295006
[Condition/8ff46e01-0333-fefb-2118-3da43e594952] Condition | onset 1995-01-18 | Risk activity involvement (finding) | clinical status active | SNOMED 160968000
[Condition/8ff46e01-0333-fefb-400e-c9db591e5ada] Condition | onset 1988-12-14 | Gingivitis (disorder) | clinical status active | SNOMED 66383009
[Condition/8ff46e01-0333-fefb-6f8d-08005729c21a] Condition | onset 1980-10-17 | History of seizure (situation) | clinical status active | SNOMED 1290882004
[Condition/8ff46e01-0333-fefb-334a-c4ab11856973] Condition | onset 1980-10-17 | Seizure disorder (disorder) | clinical status active | SNOMED 128613002
[Condition/8ff46e01-0333-fefb-493a-f8d458075b36] Condition | onset 1980-04-22 | Chronic sinusitis (disorder) | clinical status active | SNOMED 40055000
[MedicationRequest/8ff46e01-0333-fefb-081b-4d95e98b7814] MedicationRequest | prescribed 2026-01-16 | Simvastatin 10 MG Oral Tablet | status active | reason: Hyperlipidemia (disorder) | RxNorm 314231
[MedicationRequest/8ff46e01-0333-fefb-cca1-202b10a1b90d] MedicationRequest | prescribed 2025-11-10 | aspirin 81 MG Oral Tablet | status active | RxNorm 243670
[MedicationRequest/8ff46e01-0333-fefb-6306-60b207f6bcda] MedicationRequest | prescribed 2025-11-10 | rosuvastatin calcium 10 MG Oral Tablet | status active | RxNorm 859747
[MedicationRequest/8ff46e01-0333-fefb-5a32-7c872c74242b] MedicationRequest | prescribed 2025-11-10 | atenolol 50 MG Oral Tablet | status active | RxNorm 197381
[MedicationRequest/8ff46e01-0333-fefb-5632-79d28eb2f69d] MedicationRequest | prescribed 2025-11-10 | prasugrel 10 MG Oral Tablet | status active | RxNorm 855812
[MedicationRequest/8ff46e01-0333-fefb-0f09-741ffc0ecb79] MedicationRequest | prescribed 2025-11-10 | lisinopril 10 MG Oral Tablet | status active | RxNorm 314076
[Encounter/8ff46e01-0333-fefb-2842-108bae2a93b7] Encounter | 2026-01-16 | Follow-up encounter (procedure) | class AMB | reason: Hyperlipidemia (disorder) | at STEWARD HOLY FAMILY HOSPITAL INC
[Encounter/8ff46e01-0333-fefb-deac-7d54a2e717b0] Encounter | 2025-12-31 | General examination of patient (procedure) | class AMB | at GREATER LAWRENCE FAMILY HEALTH CENTER INC
[Encounter/8ff46e01-0333-fefb-bdb4-35663b36a4c8] Encounter | 2025-11-10 | Emergency room admission (procedure) | class EMER | reason: Myocardial infarction (disorder) | at Fitchburg Outpatient Clinic
[Immunization/8ff46e01-0333-fefb-0b35-b6fa97749e42] Immunization | 2025-12-31 | Influenza, split virus, trivalent, PF | status completed | CVX 140
[Observation/8ff46e01-0333-fefb-4b4e-a188d7da0932] Observation (vital-signs) | 2021-12-22 | Heart rate = 96 /min | status final | LOINC 8867-4
[Observation/8ff46e01-0333-fefb-b74d-2a1428a26ad8] Observation (vital-signs) | 2025-12-31 | Heart rate = 71 /min | status final | LOINC 8867-4
[Observation/8ff46e01-0333-fefb-20c1-44871274df91] Observation (vital-signs) | 2023-12-27 | Heart rate = 69 /min | status final | LOINC 8867-4
[Condition/8ff46e01-0333-fefb-d46d-069e32dc10df] Condition | onset 2025-11-10 | Myocardial infarction (disorder) | clinical status resolved | resolved 2025-11-10 | SNOMED 22298006
[DocumentReference/6387cd8c-586a-c131-f37f-b3ec6096418d#2] Clinical note | 2025-11-10 | part 2 of 2 | # Assessment and Plan Patient is presenting with myocardial infarction (disorder), acute non-st segment elevation myocardial infarction (disorder). ## Plan The following procedures were conducted: - assessment of cardiac status using monitoring device (procedure) - electrocardiographic procedure (procedure) - oxygen administration by mask (procedure) - laboratory test (procedure) - plain x-ray of chest (procedure) - diagnostic assessment (procedure) - electrocardiographic procedure (procedure) The following lab reports were completed: - cbc panel - blood by automated count - comprehensive metabolic 2000 panel - serum or plasma - lipid panel with direct ldl - serum or plasma The patient was prescribed the following medications: - aspirin 325 mg oral tablet - nitroglycerin 0.4 mg sublingual tablet
[Condition/8ff46e01-0333-fefb-c542-076c5124eeb2] Condition | onset 2017-03-01 | Medication review due (situation) | clinical status resolved | resolved 2023-12-27 | SNOMED 314529007
[Condition/8ff46e01-0333-fefb-312f-6e1ca711c649] Condition | onset 2025-12-31 | Medication review due (situation) | clinical status resolved | resolved 2025-12-31 | SNOMED 314529007
[DocumentReference/1a8f2b39-faf7-54d2-7a97-56ba57874cb8#2] Clinical note | 2025-11-10 | part 2 of 2 | # Assessment and Plan Patient is presenting with history of myocardial infarction (situation). ## Plan The following procedures were conducted: - risk assessment (procedure) - cardiovascular stress testing (procedure) - angiography of coronary artery (procedure) - percutaneous coronary intervention - transthoracic echocardiography (procedure) The patient was prescribed the following medications: - heparin sodium, porcine 100 unt/ml injectable solution - clopidogrel 300 mg oral tablet - aspirin 81 mg oral tablet - atenolol 50 mg oral tablet - rosuvastatin calcium 10 mg oral tablet - lisinopril 10 mg oral tablet - prasugrel 10 mg oral tablet The patient was placed on a careplan: - discharge care plan (record artifact)
[Condition/8ff46e01-0333-fefb-3072-23b1a01874cb] Condition | onset 2010-07-28 | Full-time employment (finding) | clinical status resolved | resolved 2019-12-18 | SNOMED 160903007
[DocumentReference/9733939e-9ff2-9322-c737-a55ece3a8f15#1] Clinical note | 2019-02-22 | part 1 of 1 | 2019-02-22 # Chief Complaint No complaints. # History of Present Illness Lupe126 is a 39 year-old hispanic white female. Patient has a history of malignant neoplasm of head, face and neck, other specified diseases of jaws, medication review due (situation), full-time employment (finding), other specified disorders of teeth and supporting structures, dental caries, unspecified. # Social History Patient is single. Patient has never smoked. Patient identifies as heterosexual. Patient comes from a middle socioeconomic background. Patient did not finish high school. Patient currently has Medicare. # Allergies No Known Allergies. # Medications No Active Medications. # Assessment and Plan Patient is presenting with sprain (morphologic abnormality), sprain of wrist (disorder). ## Plan The patient was prescribed the following medications: - acetaminophen 325 mg oral tablet The patient was placed on a careplan: - physiotherapy care plan (record artifact)
```

</details>

label: s
note: The cited cards show Myocardial infarction (disorder) resolved 2025-11-10, and the acute NSTEMI and History of myocardial infarction entries both have clinical status active.

## 14. `smoking-status:9292c3d5#0#0`

Question: Does the patient smoke?

Answer: **No; the clinical notes consistently state that the patient quit smoking at age 17, including the most recent note dated 2021-04-04.**

Cards this sentence cites:

- `[DocumentReference/960a81cd-5ce7-7531-422f-127dc3be48f4#1]` Clinical note | 2021-04-04 | part 1 of 1 | 2021-04-04 # Chief Complaint No complaints. # History of Present Illness Arnold338 is a 53 year-old nonhispanic white male. Patient has a history of severe anxiety (panic) (finding), medication review due (situation), not in labor force (finding), limited social contact (finding), disorder of teeth and/or supporting structures, full-time employment (finding), social isolation (finding), stress (finding). # Social History Patient is single. Patient quit smoking at age 17. Patient identifies as heterosexual. Patient comes from a middle socioeconomic background. Patient has a high school education. Patient currently has Humana. # Allergies No Known Allergies. # Medications No Active Medications. # Assessment and Plan ## Plan Patient was given the following immunizations: covid-19, mrna, lnp-s, pf, 30 mcg/0.3 ml dose.
- `[DocumentReference/b0afcae6-490b-fb11-b71d-382273ce441c#1]` Clinical note | 2021-03-14 | part 1 of 1 | 2021-03-14 # Chief Complaint No complaints. # History of Present Illness Arnold338 is a 53 year-old nonhispanic white male. Patient has a history of severe anxiety (panic) (finding), medication review due (situation), not in labor force (finding), limited social contact (finding), disorder of teeth and/or supporting structures, full-time employment (finding), social isolation (finding), stress (finding). # Social History Patient is single. Patient quit smoking at age 17. Patient identifies as heterosexual. Patient comes from a middle socioeconomic background. Patient has a high school education. Patient currently has Humana. # Allergies No Known Allergies. # Medications No Active Medications. # Assessment and Plan ## Plan Patient was given the following immunizations: covid-19, mrna, lnp-s, pf, 30 mcg/0.3 ml dose.
- `[DocumentReference/2bc93ddb-a0c6-4817-5059-ee42779a0ac3#1]` Clinical note | 2016-05-29 | part 1 of 1 | 2016-05-29 # Chief Complaint No complaints. # History of Present Illness Arnold338 is a 48 year-old nonhispanic white male. Patient has a history of medication review due (situation), disorder of teeth and/or supporting structures, full-time employment (finding). # Social History Patient is single. Patient quit smoking at age 17. Patient identifies as heterosexual. Patient comes from a middle socioeconomic background. Patient has a high school education. Patient currently has Humana. # Allergies No Known Allergies. # Medications No Active Medications. # Assessment and Plan ## Plan The patient was placed on a careplan: - respiratory therapy (procedure)

<details><summary>Everything the model saw (31 cards)</summary>

```text
[Condition/9292c3d5-3db6-f4f9-b5ec-3a44e8649597] Condition | onset 2026-04-26 | Full-time employment (finding) | clinical status active | SNOMED 160903007
[Condition/9292c3d5-3db6-f4f9-861b-f7159312202f] Condition | onset 2026-04-26 | Medication review due (situation) | clinical status active | SNOMED 314529007
[Condition/9292c3d5-3db6-f4f9-483e-3d8d3b0f4690] Condition | onset 2026-04-26 | Social isolation (finding) | clinical status active | SNOMED 422650009
[Condition/9292c3d5-3db6-f4f9-38dc-147de4ac63a8] Condition | onset 2026-04-26 | Stress (finding) | clinical status active | SNOMED 73595000
[Condition/9292c3d5-3db6-f4f9-5b6c-1c0ed0fd0321] Condition | onset 2020-03-22 | Opioid abuse | clinical status active | SNOMED 5602001
[Condition/9292c3d5-3db6-f4f9-f835-25af6c77c701] Condition | onset 2011-08-22 | History of myocardial infarction (situation) | clinical status active | SNOMED 399211009
[Condition/9292c3d5-3db6-f4f9-54d1-d4b6d2666838] Condition | onset 2011-08-22 | Acute ST segment elevation myocardial infarction (disorder) | clinical status active | SNOMED 401303003
[Condition/9292c3d5-3db6-f4f9-2b48-fd31edda50b0] Condition | onset 2010-03-21 | Anemia (disorder) | clinical status active | SNOMED 271737000
[Condition/9292c3d5-3db6-f4f9-1b0c-65cb31846f75] Condition | onset 2005-05-29 | Prediabetes (finding) | clinical status active | SNOMED 714628002
[Condition/9292c3d5-3db6-f4f9-2a82-9615e45bb615] Condition | onset 1986-05-04 | Educated to high school level (finding) | clinical status active | SNOMED 473461003
[Condition/9292c3d5-3db6-f4f9-24a0-fe08e411b951] Condition | onset 1986-05-04 | Serving in military service (finding) | clinical status active | SNOMED 1187604002
[Condition/9292c3d5-3db6-f4f9-97fc-b779fe5ffdd4] Condition | onset 1985-04-28 | Risk activity involvement (finding) | clinical status active | SNOMED 160968000
[MedicationRequest/9292c3d5-3db6-f4f9-c2ad-ca0afa2369e8] MedicationRequest | prescribed 2011-08-22 | 24 HR metoprolol succinate 50 MG Extended Release Oral Tablet | status active | RxNorm 866436
[MedicationRequest/9292c3d5-3db6-f4f9-b955-8ddb9b72de69] MedicationRequest | prescribed 2011-08-22 | prasugrel 10 MG Oral Tablet | status active | RxNorm 855812
[MedicationRequest/9292c3d5-3db6-f4f9-8b49-28e15899c04a] MedicationRequest | prescribed 2011-08-22 | aspirin 81 MG Oral Tablet | status active | RxNorm 243670
[MedicationRequest/9292c3d5-3db6-f4f9-7675-f5ee99ae0c4e] MedicationRequest | prescribed 2011-08-22 | simvastatin 40 MG Oral Tablet | status active | RxNorm 198211
[MedicationRequest/9292c3d5-3db6-f4f9-2744-8b9a3e3302b8] MedicationRequest | prescribed 2011-08-22 | lisinopril 2.5 MG Oral Tablet | status active | RxNorm 311353
[Encounter/9292c3d5-3db6-f4f9-f8cd-08dfcc81ed12] Encounter | 2026-04-26 | General examination of patient (procedure) | class AMB | at COMMUNITY HEALTH PROGRAMS INC
[Encounter/9292c3d5-3db6-f4f9-2526-cf0c3fc1dcaa] Encounter | 2025-08-10 | Encounter for check up (procedure) | class AMB | reason: Gingivitis (disorder) | at Pittsfield Outpatient Clinic
[Encounter/9292c3d5-3db6-f4f9-d85c-7f88671a1881] Encounter | 2025-08-03 | Encounter for symptom (procedure) | class AMB | reason: Acute viral pharyngitis (disorder) | at Pittsfield Outpatient Clinic
[Immunization/9292c3d5-3db6-f4f9-2e74-b2ab508532b8] Immunization | 2026-04-26 | Influenza, split virus, trivalent, PF | status completed | CVX 140
[DocumentReference/2bc93ddb-a0c6-4817-5059-ee42779a0ac3#1] Clinical note | 2016-05-29 | part 1 of 1 | 2016-05-29 # Chief Complaint No complaints. # History of Present Illness Arnold338 is a 48 year-old nonhispanic white male. Patient has a history of medication review due (situation), disorder of teeth and/or supporting structures, full-time employment (finding). # Social History Patient is single. Patient quit smoking at age 17. Patient identifies as heterosexual. Patient comes from a middle socioeconomic background. Patient has a high school education. Patient currently has Humana. # Allergies No Known Allergies. # Medications No Active Medications. # Assessment and Plan ## Plan The patient was placed on a careplan: - respiratory therapy (procedure)
[DocumentReference/19e0c452-e4de-9759-abf6-d32dbf56ecdd#1] Clinical note | 1985-04-28 | part 1 of 1 | 1985-04-28 # Chief Complaint No complaints. # History of Present Illness Arnold338 is a 17 year-old nonhispanic white male. Patient has a history of disorder of teeth and/or supporting structures. # Social History Patient quit smoking at age 17. Patient identifies as heterosexual. Patient comes from a middle socioeconomic background. Patient currently has NO INSURANCE. # Allergies No Known Allergies. # Medications No Active Medications. # Assessment and Plan Patient is presenting with risk activity involvement (finding). ## Plan
[DocumentReference/d2523d84-8b02-2671-e861-185f0357ab03#1] Clinical note | 1970-08-23 | part 1 of 1 | 1970-08-23 # Chief Complaint No complaints. # History of Present Illness Arnold338 is a 2 year-old nonhispanic white male. # Social History Patient quit smoking at age 17. Patient comes from a middle socioeconomic background. Patient currently has NO INSURANCE. # Allergies No Known Allergies. # Medications No Active Medications. # Assessment and Plan Patient is presenting with disorder of teeth and/or supporting structures. ## Plan
[DocumentReference/10751b31-4607-0b97-c565-c63a6a33254c#1] Clinical note | 1986-05-04 | part 1 of 1 | 1986-05-04 # Chief Complaint No complaints. # History of Present Illness Arnold338 is a 18 year-old nonhispanic white male. Patient has a history of disorder of teeth and/or supporting structures. # Social History Patient quit smoking at age 17. Patient identifies as heterosexual. Patient comes from a middle socioeconomic background. Patient has a high school education. Patient currently has NO INSURANCE. # Allergies No Known Allergies. # Medications No Active Medications. # Assessment and Plan Patient is presenting with serving in military service (finding), educated to high school level (finding). ## Plan
[DocumentReference/5463d8b4-a00d-58eb-0a18-c95fa9318505#1] Clinical note | 2010-03-21 | part 1 of 1 | 2010-03-21 # Chief Complaint No complaints. # History of Present Illness Arnold338 is a 42 year-old nonhispanic white male. Patient has a history of disorder of teeth and/or supporting structures. # Social History Patient is single. Patient quit smoking at age 17. Patient identifies as heterosexual. Patient comes from a middle socioeconomic background. Patient has a high school education. Patient currently has Humana. # Allergies No Known Allergies. # Medications No Active Medications. # Assessment and Plan Patient is presenting with anemia (disorder), full-time employment (finding). ## Plan
[DocumentReference/b0afcae6-490b-fb11-b71d-382273ce441c#1] Clinical note | 2021-03-14 | part 1 of 1 | 2021-03-14 # Chief Complaint No complaints. # History of Present Illness Arnold338 is a 53 year-old nonhispanic white male. Patient has a history of severe anxiety (panic) (finding), medication review due (situation), not in labor force (finding), limited social contact (finding), disorder of teeth and/or supporting structures, full-time employment (finding), social isolation (finding), stress (finding). # Social History Patient is single. Patient quit smoking at age 17. Patient identifies as heterosexual. Patient comes from a middle socioeconomic background. Patient has a high school education. Patient currently has Humana. # Allergies No Known Allergies. # Medications No Active Medications. # Assessment and Plan ## Plan Patient was given the following immunizations: covid-19, mrna, lnp-s, pf, 30 mcg/0.3 ml dose.
[DocumentReference/960a81cd-5ce7-7531-422f-127dc3be48f4#1] Clinical note | 2021-04-04 | part 1 of 1 | 2021-04-04 # Chief Complaint No complaints. # History of Present Illness Arnold338 is a 53 year-old nonhispanic white male. Patient has a history of severe anxiety (panic) (finding), medication review due (situation), not in labor force (finding), limited social contact (finding), disorder of teeth and/or supporting structures, full-time employment (finding), social isolation (finding), stress (finding). # Social History Patient is single. Patient quit smoking at age 17. Patient identifies as heterosexual. Patient comes from a middle socioeconomic background. Patient has a high school education. Patient currently has Humana. # Allergies No Known Allergies. # Medications No Active Medications. # Assessment and Plan ## Plan Patient was given the following immunizations: covid-19, mrna, lnp-s, pf, 30 mcg/0.3 ml dose.
[DocumentReference/b17e486c-6db0-1b18-1b5f-9e7eb6085684#1] Clinical note | 2014-03-30 | part 1 of 1 | 2014-03-30 # Chief Complaint No complaints. # History of Present Illness Arnold338 is a 46 year-old nonhispanic white male. Patient has a history of disorder of teeth and/or supporting structures, full-time employment (finding). # Social History Patient is single. Patient quit smoking at age 17. Patient identifies as heterosexual. Patient comes from a middle socioeconomic background. Patient has a high school education. Patient currently has Humana. # Allergies No Known Allergies. # Medications No Active Medications. # Assessment and Plan Patient is presenting with medication review due (situation). ## Plan
[DocumentReference/f220eff2-c97c-79d3-4a6a-1153b72a2159#1] Clinical note | 2019-03-17 | part 1 of 2 | 2019-03-17 # Chief Complaint No complaints. # History of Present Illness Arnold338 is a 51 year-old nonhispanic white male. Patient has a history of medication review due (situation), disorder of teeth and/or supporting structures, full-time employment (finding), social isolation (finding), stress (finding). # Social History Patient is single. Patient quit smoking at age 17. Patient identifies as heterosexual. Patient comes from a middle socioeconomic background. Patient has a high school education. Patient currently has Humana. # Allergies No Known Allergies. # Medications No Active Medications.
[DocumentReference/43776b3d-60c3-c1e3-e18c-cc61e6477899#1] Clinical note | 2020-03-22 | part 1 of 2 | 2020-03-22 # Chief Complaint No complaints. # History of Present Illness Arnold338 is a 52 year-old nonhispanic white male. Patient has a history of medication review due (situation), not in labor force (finding), limited social contact (finding), disorder of teeth and/or supporting structures, full-time employment (finding), social isolation (finding), stress (finding). # Social History Patient is single. Patient quit smoking at age 17. Patient identifies as heterosexual. Patient comes from a middle socioeconomic background. Patient has a high school education. Patient currently has Humana. # Allergies No Known Allergies. # Medications No Active Medications.
```

</details>

label: s
note: All 10 notes the model saw say 'Patient quit smoking at age 17', and the latest of them is dated 2021-04-04 (others are 1970-2021-03-14), so both 'consistently' and 'most recent' check out.

## 15. `current-meds:8ff46e01#0#0`

Question: What medications is the patient currently prescribed?

Answer: **The patient's active prescriptions are aspirin 81 MG Oral Tablet, rosuvastatin calcium 10 MG Oral Tablet, atenolol 50 MG Oral Tablet, prasugrel 10 MG Oral Tablet, and lisinopril 10 MG Oral Tablet, all prescribed 2025-11-10.** Simvastatin 10 MG Oral Tablet, prescribed 2026-01-16 for hyperlipidemia, is also active.

Cards this sentence cites:

- `[MedicationRequest/8ff46e01-0333-fefb-cca1-202b10a1b90d]` MedicationRequest | prescribed 2025-11-10 | aspirin 81 MG Oral Tablet | status active | RxNorm 243670
- `[MedicationRequest/8ff46e01-0333-fefb-6306-60b207f6bcda]` MedicationRequest | prescribed 2025-11-10 | rosuvastatin calcium 10 MG Oral Tablet | status active | RxNorm 859747
- `[MedicationRequest/8ff46e01-0333-fefb-5a32-7c872c74242b]` MedicationRequest | prescribed 2025-11-10 | atenolol 50 MG Oral Tablet | status active | RxNorm 197381
- `[MedicationRequest/8ff46e01-0333-fefb-5632-79d28eb2f69d]` MedicationRequest | prescribed 2025-11-10 | prasugrel 10 MG Oral Tablet | status active | RxNorm 855812
- `[MedicationRequest/8ff46e01-0333-fefb-0f09-741ffc0ecb79]` MedicationRequest | prescribed 2025-11-10 | lisinopril 10 MG Oral Tablet | status active | RxNorm 314076

<details><summary>Everything the model saw (35 cards)</summary>

```text
[Condition/8ff46e01-0333-fefb-e078-a2c79f9b5570] Condition | onset 2025-11-10 | History of myocardial infarction (situation) | clinical status active | SNOMED 399211009
[Condition/8ff46e01-0333-fefb-ca9a-9c89d481d534] Condition | onset 2025-11-10 | Acute non-ST segment elevation myocardial infarction (disorder) | clinical status active | SNOMED 401314000
[Condition/8ff46e01-0333-fefb-f69f-b001b28f2b81] Condition | onset 2023-12-27 | Full-time employment (finding) | clinical status active | SNOMED 160903007
[Condition/8ff46e01-0333-fefb-d37b-fa17bc4619e6] Condition | onset 2023-12-27 | Hyperlipidemia (disorder) | clinical status active | SNOMED 55822004
[Condition/8ff46e01-0333-fefb-1085-7240f563162c] Condition | onset 2023-12-27 | Anemia (disorder) | clinical status active | SNOMED 271737000
[Condition/8ff46e01-0333-fefb-0d5f-96af345c8178] Condition | onset 2023-12-27 | Prediabetes (finding) | clinical status active | SNOMED 714628002
[Condition/8ff46e01-0333-fefb-a724-e7508612ceb2] Condition | onset 2015-12-19 | History of tubal ligation (situation) | clinical status active | SNOMED 267020005
[Condition/8ff46e01-0333-fefb-c4b8-0da5f4d9d6af] Condition | onset 2010-09-29 | Stress (finding) | clinical status active | SNOMED 73595000
[Condition/8ff46e01-0333-fefb-3eac-29a6b80382d5] Condition | onset 1998-06-27 | Recurrent urinary tract infection (disorder) | clinical status active | SNOMED 197927001
[Condition/8ff46e01-0333-fefb-1001-1cc553e61d65] Condition | onset 1998-02-04 | Only received primary school education (finding) | clinical status active | SNOMED 224295006
[Condition/8ff46e01-0333-fefb-2118-3da43e594952] Condition | onset 1995-01-18 | Risk activity involvement (finding) | clinical status active | SNOMED 160968000
[Condition/8ff46e01-0333-fefb-400e-c9db591e5ada] Condition | onset 1988-12-14 | Gingivitis (disorder) | clinical status active | SNOMED 66383009
[Condition/8ff46e01-0333-fefb-6f8d-08005729c21a] Condition | onset 1980-10-17 | History of seizure (situation) | clinical status active | SNOMED 1290882004
[Condition/8ff46e01-0333-fefb-334a-c4ab11856973] Condition | onset 1980-10-17 | Seizure disorder (disorder) | clinical status active | SNOMED 128613002
[Condition/8ff46e01-0333-fefb-493a-f8d458075b36] Condition | onset 1980-04-22 | Chronic sinusitis (disorder) | clinical status active | SNOMED 40055000
[MedicationRequest/8ff46e01-0333-fefb-081b-4d95e98b7814] MedicationRequest | prescribed 2026-01-16 | Simvastatin 10 MG Oral Tablet | status active | reason: Hyperlipidemia (disorder) | RxNorm 314231
[MedicationRequest/8ff46e01-0333-fefb-cca1-202b10a1b90d] MedicationRequest | prescribed 2025-11-10 | aspirin 81 MG Oral Tablet | status active | RxNorm 243670
[MedicationRequest/8ff46e01-0333-fefb-6306-60b207f6bcda] MedicationRequest | prescribed 2025-11-10 | rosuvastatin calcium 10 MG Oral Tablet | status active | RxNorm 859747
[MedicationRequest/8ff46e01-0333-fefb-5a32-7c872c74242b] MedicationRequest | prescribed 2025-11-10 | atenolol 50 MG Oral Tablet | status active | RxNorm 197381
[MedicationRequest/8ff46e01-0333-fefb-5632-79d28eb2f69d] MedicationRequest | prescribed 2025-11-10 | prasugrel 10 MG Oral Tablet | status active | RxNorm 855812
[MedicationRequest/8ff46e01-0333-fefb-0f09-741ffc0ecb79] MedicationRequest | prescribed 2025-11-10 | lisinopril 10 MG Oral Tablet | status active | RxNorm 314076
[Encounter/8ff46e01-0333-fefb-2842-108bae2a93b7] Encounter | 2026-01-16 | Follow-up encounter (procedure) | class AMB | reason: Hyperlipidemia (disorder) | at STEWARD HOLY FAMILY HOSPITAL INC
[Encounter/8ff46e01-0333-fefb-deac-7d54a2e717b0] Encounter | 2025-12-31 | General examination of patient (procedure) | class AMB | at GREATER LAWRENCE FAMILY HEALTH CENTER INC
[Encounter/8ff46e01-0333-fefb-bdb4-35663b36a4c8] Encounter | 2025-11-10 | Emergency room admission (procedure) | class EMER | reason: Myocardial infarction (disorder) | at Fitchburg Outpatient Clinic
[Immunization/8ff46e01-0333-fefb-0b35-b6fa97749e42] Immunization | 2025-12-31 | Influenza, split virus, trivalent, PF | status completed | CVX 140
[MedicationRequest/8ff46e01-0333-fefb-071f-4a32d7ee3611] MedicationRequest | prescribed 2025-11-10 | status completed
[MedicationRequest/8ff46e01-0333-fefb-6b5e-9f6740d55d90] MedicationRequest | prescribed 2025-11-10 | status completed
[MedicationRequest/8ff46e01-0333-fefb-881b-968118aa2f40] MedicationRequest | prescribed 2025-11-10 | status completed
[MedicationRequest/8ff46e01-0333-fefb-f0e1-cfc081e03b69] MedicationRequest | prescribed 2025-11-10 | status completed
[MedicationRequest/8ff46e01-0333-fefb-e5ec-bf946b3fdf85] MedicationRequest | prescribed 2019-02-22 | Acetaminophen 325 MG Oral Tablet | status completed | RxNorm 313782
[DocumentReference/9733939e-9ff2-9322-c737-a55ece3a8f15#1] Clinical note | 2019-02-22 | part 1 of 1 | 2019-02-22 # Chief Complaint No complaints. # History of Present Illness Lupe126 is a 39 year-old hispanic white female. Patient has a history of malignant neoplasm of head, face and neck, other specified diseases of jaws, medication review due (situation), full-time employment (finding), other specified disorders of teeth and supporting structures, dental caries, unspecified. # Social History Patient is single. Patient has never smoked. Patient identifies as heterosexual. Patient comes from a middle socioeconomic background. Patient did not finish high school. Patient currently has Medicare. # Allergies No Known Allergies. # Medications No Active Medications. # Assessment and Plan Patient is presenting with sprain (morphologic abnormality), sprain of wrist (disorder). ## Plan The patient was prescribed the following medications: - acetaminophen 325 mg oral tablet The patient was placed on a careplan: - physiotherapy care plan (record artifact)
[DocumentReference/2b583abb-ebce-d62b-2d63-1ad30fcccfc3#1] Clinical note | 2024-01-17 | part 1 of 1 | 2024-01-17 # Chief Complaint No complaints. # History of Present Illness Lupe126 is a 44 year-old hispanic white female. Patient has a history of part-time employment (finding), malignant neoplasm of head, face and neck, sprain (morphologic abnormality), other specified diseases of jaws, medication review due (situation), full-time employment (finding), sprain of ankle (disorder), sprain of wrist (disorder), viral sinusitis (disorder), other specified disorders of teeth and supporting structures, dental caries, unspecified. # Social History Patient is single. Patient has never smoked. Patient identifies as heterosexual. Patient comes from a middle socioeconomic background. Patient did not finish high school. Patient currently has Medicare. # Allergies No Known Allergies. # Medications acetaminophen 325 mg oral tablet; naproxen sodium 220 mg oral tablet # Assessment and Plan ## Plan The patient was prescribed the following medications: - simvastatin 10 mg oral tablet The patient was placed on a careplan: - hyperlipidemia clinical management plan (record artifact)
[DocumentReference/47fddcb0-4702-402b-2c7d-9be347439c2e#1] Clinical note | 2022-02-08 | part 1 of 1 | 2022-02-08 # Chief Complaint No complaints. # History of Present Illness Lupe126 is a 42 year-old hispanic white female. Patient has a history of part-time employment (finding), malignant neoplasm of head, face and neck, sprain (morphologic abnormality), other specified diseases of jaws, medication review due (situation), full-time employment (finding), sprain of wrist (disorder), viral sinusitis (disorder), other specified disorders of teeth and supporting structures, dental caries, unspecified. # Social History Patient is single. Patient has never smoked. Patient identifies as heterosexual. Patient comes from a middle socioeconomic background. Patient did not finish high school. Patient currently has Medicare. # Allergies No Known Allergies. # Medications acetaminophen 325 mg oral tablet # Assessment and Plan Patient is presenting with sprain (morphologic abnormality), sprain of ankle (disorder). ## Plan The patient was prescribed the following medications: - naproxen sodium 220 mg oral tablet The patient was placed on a careplan: - physiotherapy care plan (record artifact)
[MedicationRequest/8ff46e01-0333-fefb-8a46-b576798484c9] MedicationRequest | prescribed 2025-01-16 | Simvastatin 10 MG Oral Tablet | status completed | reason: Hyperlipidemia (disorder) | RxNorm 314231
[MedicationRequest/8ff46e01-0333-fefb-7f78-a97308c8b605] MedicationRequest | prescribed 2024-01-17 | Simvastatin 10 MG Oral Tablet | status completed | reason: Hyperlipidemia (disorder) | RxNorm 314231
```

</details>

label: s?
note: The five drugs are all active and prescribed 2025-11-10 per the cited cards; simvastatin 10 MG (2026-01-16) is the only other active request, and the next sentence adds it as 'also active'. Read alone, the bold sentence looks like an incomplete list, so some may label p.

## 16. `latest-lab-4548-4:8446fe54#0#0`

Question: What was the patient's most recent hemoglobin A1c result, and when was it measured?

Answer: **The most recent hemoglobin A1c was 6.91 %, measured on 2025-10-03.** Earlier results on 2024-09-27 and 2023-09-22 were also 6.91 %.

Cards this sentence cites:

- `[Observation/8446fe54-5b2e-6a46-a7d0-f74e09b33da1]` Observation (laboratory) | 2025-10-03 | Hemoglobin A1c/Hemoglobin.total in Blood = 6.91 % | status final | LOINC 4548-4

<details><summary>Everything the model saw (49 cards)</summary>

```text
[Condition/8446fe54-5b2e-6a46-c855-6376bf616037] Condition | onset 2025-10-03 | Stress (finding) | clinical status active | SNOMED 73595000
[Condition/8446fe54-5b2e-6a46-3883-408ea2da0a37] Condition | onset 2025-05-15 | Nonproliferative diabetic retinopathy due to type II diabetes mellitus | clinical status active | SNOMED 1551000119108
[Condition/8446fe54-5b2e-6a46-2283-ccf89bdfa001] Condition | onset 2024-09-27 | Medication review due (situation) | clinical status active | SNOMED 314529007
[Condition/8446fe54-5b2e-6a46-8ab7-b639a56aa55f] Condition | onset 2023-09-22 | Osteoporosis (disorder) | clinical status active | SNOMED 64859006
[Condition/8446fe54-5b2e-6a46-169f-475724b93b14] Condition | onset 2022-03-10 | History of myocardial infarction (situation) | clinical status active | SNOMED 399211009
[Condition/8446fe54-5b2e-6a46-7c5e-428350d41910] Condition | onset 2022-03-08 | Acute non-ST segment elevation myocardial infarction (disorder) | clinical status active | SNOMED 401314000
[Condition/8446fe54-5b2e-6a46-b854-dbfe1d5848d8] Condition | onset 2019-08-30 | Neuropathy due to type 2 diabetes mellitus (disorder) | clinical status active | SNOMED 368581000119106
[Condition/8446fe54-5b2e-6a46-9883-d3e4fb3c92c7] Condition | onset 2017-08-18 | Full-time employment (finding) | clinical status active | SNOMED 160903007
[Condition/8446fe54-5b2e-6a46-90ec-9d5bb7f4215c] Condition | onset 2015-08-07 | Limited social contact (finding) | clinical status active | SNOMED 423315002
[Condition/8446fe54-5b2e-6a46-ac98-749a48641300] Condition | onset 2009-07-27 | Abnormal findings diagnostic imaging heart+coronary circulat (finding) | clinical status active | SNOMED 274531002
[Condition/8446fe54-5b2e-6a46-ac45-606071904f4c] Condition | onset 2009-07-03 | Ischemic heart disease (disorder) | clinical status active | SNOMED 414545008
[Condition/8446fe54-5b2e-6a46-19e1-02a0cca64803] Condition | onset 2009-07-03 | Gingivitis (disorder) | clinical status active | SNOMED 66383009
[Condition/8446fe54-5b2e-6a46-9731-2ba07e7b3f8a] Condition | onset 2002-05-24 | Hyperlipidemia (disorder) | clinical status active | SNOMED 55822004
[Condition/8446fe54-5b2e-6a46-5645-a8fdbdfcefa0] Condition | onset 1997-04-25 | Essential hypertension (disorder) | clinical status active | SNOMED 59621000
[Condition/8446fe54-5b2e-6a46-6984-e3082708b597] Condition | onset 1997-01-20 | Localized, primary osteoarthritis of the hand (disorder) | clinical status active | SNOMED 201834006
[Condition/8446fe54-5b2e-6a46-918b-8a35802414ef] Condition | onset 1996-11-29 | Metabolic syndrome X (disorder) | clinical status active | SNOMED 237602007
[Condition/8446fe54-5b2e-6a46-8453-0b6ddcc40622] Condition | onset 1996-11-29 | Hypertriglyceridemia (disorder) | clinical status active | SNOMED 302870006
[Condition/8446fe54-5b2e-6a46-71d0-e1231acfc548] Condition | onset 1996-04-19 | Diabetes mellitus type 2 (disorder) | clinical status active | SNOMED 44054006
[Condition/8446fe54-5b2e-6a46-53e3-b8317bbea5b4] Condition | onset 1973-08-15 | Past pregnancy history of miscarriage (situation) | clinical status active | SNOMED 161744009
[Condition/8446fe54-5b2e-6a46-efe6-1830fbd69235] Condition | onset 1971-06-11 | Body mass index 30+ - obesity (finding) | clinical status active | SNOMED 162864005
[Condition/8446fe54-5b2e-6a46-a0b3-4dfcdfdaffac] Condition | onset 1965-06-04 | Anemia (disorder) | clinical status active | SNOMED 271737000
[Condition/8446fe54-5b2e-6a46-26e1-de3ad83381e7] Condition | onset 1965-06-04 | Prediabetes (finding) | clinical status active | SNOMED 714628002
[Condition/8446fe54-5b2e-6a46-3a03-f8734c3aad20] Condition | onset 1961-05-26 | Received higher education (finding) | clinical status active | SNOMED 224299000
[MedicationRequest/8446fe54-5b2e-6a46-659f-46ecea0cf5ef] MedicationRequest | prescribed 2025-10-04 | Simvastatin 10 MG Oral Tablet | status active | reason: Hyperlipidemia (disorder) | RxNorm 314231
[MedicationRequest/8446fe54-5b2e-6a46-88a0-c7dd9e8fc1a1] MedicationRequest | prescribed 2025-10-03 | lisinopril 10 MG Oral Tablet | status active | reason: Essential hypertension (disorder) | RxNorm 314076
[MedicationRequest/8446fe54-5b2e-6a46-7320-4ef7c8ad8f40] MedicationRequest | prescribed 2025-10-03 | Alendronic acid 10 MG Oral Tablet | status active | reason: Osteoporosis (disorder) | RxNorm 904419
[MedicationRequest/8446fe54-5b2e-6a46-bf69-9fef69e23979] MedicationRequest | prescribed 2022-03-10 | rosuvastatin calcium 10 MG Oral Tablet [Crestor] | status active | RxNorm 859749
[MedicationRequest/8446fe54-5b2e-6a46-4de5-bb23365c2bff] MedicationRequest | prescribed 2022-03-10 | carvedilol 25 MG Oral Tablet | status active | RxNorm 200033
[MedicationRequest/8446fe54-5b2e-6a46-49d9-f1a38344333d] MedicationRequest | prescribed 2022-03-10 | aspirin 81 MG Oral Tablet | status active | RxNorm 243670
[MedicationRequest/8446fe54-5b2e-6a46-3148-e44c765beb21] MedicationRequest | prescribed 2022-03-10 | prasugrel 10 MG Oral Tablet | status active | RxNorm 855812
[MedicationRequest/8446fe54-5b2e-6a46-2330-5a6c9a9f35f4] MedicationRequest | prescribed 2022-03-10 | losartan potassium 25 MG Oral Tablet | status active | RxNorm 979485
[MedicationRequest/8446fe54-5b2e-6a46-abfb-29ebed5ed8f5] MedicationRequest | prescribed 2009-07-10 | 24 HR metoprolol succinate 100 MG Extended Release Oral Tablet | status active | RxNorm 866412
[MedicationRequest/8446fe54-5b2e-6a46-a1b3-bc484b4b6e59] MedicationRequest | prescribed 2009-07-10 | Clopidogrel 75 MG Oral Tablet | status active | RxNorm 309362
[MedicationRequest/8446fe54-5b2e-6a46-31e7-0fab4c5ed076] MedicationRequest | prescribed 2009-07-10 | Nitroglycerin 0.4 MG/ACTUAT Mucosal Spray | status active | RxNorm 705129
[MedicationRequest/8446fe54-5b2e-6a46-2210-4b4518283f4c] MedicationRequest | prescribed 2009-07-10 | Simvastatin 20 MG Oral Tablet | status active | RxNorm 312961
[Encounter/8446fe54-5b2e-6a46-f799-ff1c9d688587] Encounter | 2026-04-10 | Ophthalmic examination and evaluation (procedure) | class AMB | at MILFORD REGIONAL MEDICAL CENTER
[Encounter/8446fe54-5b2e-6a46-7463-6a2732ff7cd0] Encounter | 2026-03-06 | Encounter for symptom (procedure) | class AMB | reason: Viral sinusitis (disorder) | at MILFORD REGIONAL MEDICAL CENTER
[Encounter/8446fe54-5b2e-6a46-f36c-8ce8c10cff85] Encounter | 2026-01-11 | Hospital admission (procedure) | class IMP | reason: Patient transfer to skilled nursing facility (procedure) | at CLAFLIN HILL CORPORATION
[Immunization/8446fe54-5b2e-6a46-dae8-760a54add250] Immunization | 2025-10-03 | Influenza, split virus, trivalent, PF | status completed | CVX 140
[Observation/8446fe54-5b2e-6a46-a7d0-f74e09b33da1] Observation (laboratory) | 2025-10-03 | Hemoglobin A1c/Hemoglobin.total in Blood = 6.91 % | status final | LOINC 4548-4
[Observation/8446fe54-5b2e-6a46-3f49-a8117f3d22df] Observation (laboratory) | 2024-09-27 | Hemoglobin A1c/Hemoglobin.total in Blood = 6.91 % | status final | LOINC 4548-4
[Observation/8446fe54-5b2e-6a46-2871-fec03332d8c9] Observation (laboratory) | 2023-09-22 | Hemoglobin A1c/Hemoglobin.total in Blood = 6.91 % | status final | LOINC 4548-4
[Observation/8446fe54-5b2e-6a46-9ac0-8f2331e3952d] Observation (laboratory) | 2020-09-04 | Hemoglobin [Mass/volume] in Blood = 14.51 g/dL | status final | LOINC 718-7
[Observation/8446fe54-5b2e-6a46-3004-2f2ac3a1a5ac] Observation (laboratory) | 2025-10-03 | Hemoglobin [Mass/volume] in Blood = 16.946 g/dL | status final | LOINC 718-7
[Observation/8446fe54-5b2e-6a46-c76a-da88e588c9ae] Observation (laboratory) | 2022-03-08 | Hemoglobin [Mass/volume] in Blood = 12.751 g/dL | status final | LOINC 718-7
[Observation/8446fe54-5b2e-6a46-a1f0-b97be4fc91f1] Observation (laboratory) | 2022-03-08 | aPTT in Blood by Coagulation assay = 28.597 s | status final | LOINC 3173-2
[Observation/8446fe54-5b2e-6a46-eb75-0e1bbcd98d97] Observation (laboratory) | 2020-09-11 | Glucose [Mass/volume] in Blood = 124.54 mg/dL | status final | LOINC 2339-0
[Observation/8446fe54-5b2e-6a46-2262-d649e8bf4cce] Observation (laboratory) | 2025-10-04 | Glucose [Mass/volume] in Blood = 100.31 mg/dL | status final | LOINC 2339-0
[Observation/8446fe54-5b2e-6a46-102b-35b203651829] Observation (laboratory) | 2025-10-03 | Glucose [Mass/volume] in Blood = 104.23 mg/dL | status final | LOINC 2339-0
```

</details>

label: s
note: There are three HbA1c (LOINC 4548-4) results, 2025-10-03, 2024-09-27 and 2023-09-22, so 2025-10-03 is the latest, and the cited card gives 6.91 %.

## 17. `current-meds:0eeb6aa3#0#2`

Question: What medications is the patient currently prescribed?

Answer: For essential hypertension, the patient has active prescriptions for amLODIPine 2.5 MG Oral Tablet, Hydrochlorothiazide 25 MG Oral Tablet, and lisinopril 10 MG Oral Tablet, all prescribed 2026-08-09. For diabetes mellitus type 2, 24 HR Metformin hydrochloride 500 MG Extended Release Oral Tablet is active, prescribed 2026-08-09. **Naproxen 500 MG Oral Tablet is active for primary fibromyalgia syndrome, prescribed 2026-07-29.** Naproxen sodium 220 MG Oral Tablet is active for osteoarthritis of knee, prescribed 2021-04-07. Ferrous sulfate 325 MG Oral Tablet is active, prescribed 1993-03-28.

Cards this sentence cites:

- `[MedicationRequest/0eeb6aa3-c249-0e46-48fb-484102ab7f68]` MedicationRequest | prescribed 2026-07-29 | Naproxen 500 MG Oral Tablet | status active | reason: Primary fibromyalgia syndrome (disorder) | RxNorm 198014

<details><summary>Everything the model saw (36 cards)</summary>

```text
[Condition/0eeb6aa3-c249-0e46-6f19-eb10a1f328db] Condition | onset 2026-07-29 | Primary fibromyalgia syndrome (disorder) | clinical status active | SNOMED 95417003
[Condition/0eeb6aa3-c249-0e46-44b4-3580330e81b7] Condition | onset 2025-12-14 | Misuses drugs (finding) | clinical status active | SNOMED 361055000
[Condition/0eeb6aa3-c249-0e46-2c95-28a9408c6896] Condition | onset 2025-12-14 | Full-time employment (finding) | clinical status active | SNOMED 160903007
[Condition/0eeb6aa3-c249-0e46-b1be-047f25b1022e] Condition | onset 2022-11-27 | Metabolic syndrome X (disorder) | clinical status active | SNOMED 237602007
[Condition/0eeb6aa3-c249-0e46-6def-33ad344a7a9b] Condition | onset 2022-11-27 | Hypertriglyceridemia (disorder) | clinical status active | SNOMED 302870006
[Condition/0eeb6aa3-c249-0e46-06a5-9d3ec2ee65d0] Condition | onset 2022-11-27 | Hyperglycemia (disorder) | clinical status active | SNOMED 80394007
[Condition/0eeb6aa3-c249-0e46-d84e-f3245ad02f8e] Condition | onset 2021-11-21 | Essential hypertension (disorder) | clinical status active | SNOMED 59621000
[Condition/0eeb6aa3-c249-0e46-ce58-8dd4753fcdb4] Condition | onset 2021-11-21 | Victim of intimate partner abuse (finding) | clinical status active | SNOMED 706893006
[Condition/0eeb6aa3-c249-0e46-8d5d-18bd4ff7c429] Condition | onset 2021-11-21 | Diabetes mellitus type 2 (disorder) | clinical status active | SNOMED 44054006
[Condition/0eeb6aa3-c249-0e46-0e2a-b4435a3e06d7] Condition | onset 2021-04-07 | Osteoarthritis of knee (disorder) | clinical status active | SNOMED 239873007
[Condition/0eeb6aa3-c249-0e46-c1e0-a1835f8dfe99] Condition | onset 2013-11-03 | Body mass index 30+ - obesity (finding) | clinical status active | SNOMED 162864005
[Condition/0eeb6aa3-c249-0e46-7e82-50da4e26d936] Condition | onset 2009-08-25 | History of tubal ligation (situation) | clinical status active | SNOMED 267020005
[Condition/0eeb6aa3-c249-0e46-05b2-ee89706489e7] Condition | onset 2008-01-13 | Prediabetes (finding) | clinical status active | SNOMED 714628002
[Condition/0eeb6aa3-c249-0e46-1bf9-48c5ad5ed3c4] Condition | onset 1991-12-22 | Received higher education (finding) | clinical status active | SNOMED 224299000
[Condition/0eeb6aa3-c249-0e46-7231-74f682325091] Condition | onset 1988-12-04 | Risk activity involvement (finding) | clinical status active | SNOMED 160968000
[MedicationRequest/0eeb6aa3-c249-0e46-d035-2af008a23544] MedicationRequest | prescribed 2026-08-09 | amLODIPine 2.5 MG Oral Tablet | status active | reason: Essential hypertension (disorder) | RxNorm 308136
[MedicationRequest/0eeb6aa3-c249-0e46-9e8f-3bc3a049dcd6] MedicationRequest | prescribed 2026-08-09 | Hydrochlorothiazide 25 MG Oral Tablet | status active | reason: Essential hypertension (disorder) | RxNorm 310798
[MedicationRequest/0eeb6aa3-c249-0e46-9979-087d4ecb9395] MedicationRequest | prescribed 2026-08-09 | lisinopril 10 MG Oral Tablet | status active | reason: Essential hypertension (disorder) | RxNorm 314076
[MedicationRequest/0eeb6aa3-c249-0e46-8801-c4efefa8fdf6] MedicationRequest | prescribed 2026-08-09 | 24 HR Metformin hydrochloride 500 MG Extended Release Oral Tablet | status active | reason: Diabetes mellitus type 2 (disorder) | RxNorm 860975
[MedicationRequest/0eeb6aa3-c249-0e46-48fb-484102ab7f68] MedicationRequest | prescribed 2026-07-29 | Naproxen 500 MG Oral Tablet | status active | reason: Primary fibromyalgia syndrome (disorder) | RxNorm 198014
[MedicationRequest/0eeb6aa3-c249-0e46-7cb4-1e0c24948d9a] MedicationRequest | prescribed 2021-04-07 | Naproxen sodium 220 MG Oral Tablet | status active | reason: Osteoarthritis of knee (disorder) | RxNorm 849574
[MedicationRequest/0eeb6aa3-c249-0e46-6749-08c77e3ff56d] MedicationRequest | prescribed 1993-03-28 | ferrous sulfate 325 MG Oral Tablet | status active | RxNorm 310325
[Encounter/0eeb6aa3-c249-0e46-4c0e-5bc7f2736fbd] Encounter | 2026-08-09 | Urgent care clinic (environment) | class AMB | at URGENT HELP CHELMSFORD PC
[Encounter/0eeb6aa3-c249-0e46-43a1-ecea1c0a2a61] Encounter | 2026-07-29 | Encounter for problem (procedure) | class AMB | reason: Primary fibromyalgia syndrome (disorder) | at HOLY FAMILY HOSPITAL
[Encounter/0eeb6aa3-c249-0e46-d415-7e8395059f69] Encounter | 2026-01-04 | Encounter for check up (procedure) | class AMB | reason: Patient referral for dental care (procedure) | at HOLY FAMILY HOSPITAL
[Immunization/0eeb6aa3-c249-0e46-99a3-4dae451772fe] Immunization | 2026-08-09 | Influenza, split virus, trivalent, PF | status completed | CVX 140
[DocumentReference/defee664-4d19-01ca-bbf7-70aefb37dd43#2] Clinical note | 2025-07-13 | part 2 of 2 | # Assessment and Plan Patient is presenting with medication review due (situation). ## Plan The patient was prescribed the following medications: - hydrochlorothiazide 25 mg oral tablet - 24 hr metformin hydrochloride 500 mg extended release oral tablet - lisinopril 10 mg oral tablet - amlodipine 2.5 mg oral tablet
[DocumentReference/bb53c693-35fa-1396-96c2-e2324743695a#2] Clinical note | 2024-08-25 | part 2 of 2 | # Assessment and Plan ## Plan The following procedures were conducted: - medication reconciliation (procedure) The patient was prescribed the following medications: - hydrochlorothiazide 25 mg oral tablet - 24 hr metformin hydrochloride 500 mg extended release oral tablet - lisinopril 10 mg oral tablet - amlodipine 2.5 mg oral tablet
[MedicationRequest/0eeb6aa3-c249-0e46-db02-9ad8292eeb53] MedicationRequest | prescribed 2021-12-12 | status completed
[MedicationRequest/0eeb6aa3-c249-0e46-bd5f-62c40576c607] MedicationRequest | prescribed 2024-12-15 | status completed
[MedicationRequest/0eeb6aa3-c249-0e46-ca8b-0ea8c0a9f16e] MedicationRequest | prescribed 2022-12-07 | status completed
[MedicationRequest/0eeb6aa3-c249-0e46-011e-821bb6b6dcd9] MedicationRequest | prescribed 2025-12-21 | status completed
[MedicationRequest/0eeb6aa3-c249-0e46-a5bb-3d602420d63d] MedicationRequest | prescribed 2023-12-10 | status completed
[MedicationRequest/0eeb6aa3-c249-0e46-13fc-e358f17e21e0] MedicationRequest | prescribed 2021-10-01 | Ibuprofen 200 MG Oral Tablet | status completed | RxNorm 310965
[MedicationRequest/0eeb6aa3-c249-0e46-2d85-7a741c19839d] MedicationRequest | prescribed 2025-12-14 | Hydrochlorothiazide 25 MG Oral Tablet | status completed | reason: Essential hypertension (disorder) | RxNorm 310798
[MedicationRequest/0eeb6aa3-c249-0e46-d71a-f406991eb66d] MedicationRequest | prescribed 2025-07-20 | Hydrochlorothiazide 25 MG Oral Tablet | status completed | reason: Essential hypertension (disorder) | RxNorm 310798
```

</details>

label: s
note: The cited card shows Naproxen 500 MG Oral Tablet, prescribed 2026-07-29, status active, reason Primary fibromyalgia syndrome.

## 18. `current-meds:0e6e0d73#0#1`

Question: What medications is the patient currently prescribed?

Answer: The only medication with an active status is Levora 0.15/30 28 Day (21 ethinyl estradiol 0.03 MG / levonorgestrel 0.15 MG Oral Tablet / 7 inert ingredients 1 MG Oral Tablet), prescribed 2026-07-12. **It was prescribed at a contraception care consultation on 2026-07-12.** Other medication requests in the record, such as acetaminophen 325 MG Oral Tablet, have status completed.

Cards this sentence cites:

- `[Encounter/0e6e0d73-619d-15c3-9366-052e1e643c56]` Encounter | 2026-07-12 | Consultation for treatment (procedure) | class AMB | reason: Contraception care (regime/therapy) | at NEW ENGLAND SINAI HOSPITAL

<details><summary>Everything the model saw (26 cards)</summary>

```text
[Condition/0e6e0d73-619d-15c3-1198-27a3f1e6671d] Condition | onset 2026-05-25 | Full-time employment (finding) | clinical status active | SNOMED 160903007
[Condition/0e6e0d73-619d-15c3-73bb-c4435e198a52] Condition | onset 2021-08-16 | Unhealthy alcohol drinking behavior (finding) | clinical status active | SNOMED 10939881000119105
[Condition/0e6e0d73-619d-15c3-a2af-2198a3d15909] Condition | onset 2021-08-02 | Medication review due (situation) | clinical status active | SNOMED 314529007
[Condition/0e6e0d73-619d-15c3-7d75-d0dd94ac6175] Condition | onset 2018-04-30 | Past pregnancy history of miscarriage (situation) | clinical status active | SNOMED 161744009
[Condition/0e6e0d73-619d-15c3-dabb-3f18b4ab6eed] Condition | onset 2017-09-23 | Sepsis (disorder) | clinical status active | SNOMED 91302008
[Condition/0e6e0d73-619d-15c3-279b-bad1f131dc84] Condition | onset 2017-09-23 | Septic shock (disorder) | clinical status active | SNOMED 76571007
[Condition/0e6e0d73-619d-15c3-252c-3ec5aec72d7f] Condition | onset 2006-07-17 | Victim of intimate partner abuse (finding) | clinical status active | SNOMED 706893006
[Condition/0e6e0d73-619d-15c3-a3b6-7fc6f2b594a9] Condition | onset 2002-07-08 | Educated to high school level (finding) | clinical status active | SNOMED 473461003
[Condition/0e6e0d73-619d-15c3-a0ee-8e9994e38bf4] Condition | onset 2001-07-02 | Risk activity involvement (finding) | clinical status active | SNOMED 160968000
[MedicationRequest/0e6e0d73-619d-15c3-e363-3a1afa521a17] MedicationRequest | prescribed 2026-07-12 | {21 (ethinyl estradiol 0.03 MG / levonorgestrel 0.15 MG Oral Tablet) / 7 (inert ingredients 1 MG Oral Tablet) } Pack [Levora 0.15/30 28 Day] | status active | RxNorm 748879
[Encounter/0e6e0d73-619d-15c3-9366-052e1e643c56] Encounter | 2026-07-12 | Consultation for treatment (procedure) | class AMB | reason: Contraception care (regime/therapy) | at NEW ENGLAND SINAI HOSPITAL
[Encounter/0e6e0d73-619d-15c3-60c1-89e78f0afd63] Encounter | 2026-05-25 | General examination of patient (procedure) | class AMB | at ENRICH WELLNESS HEALTH CENTER LLC
[Encounter/0e6e0d73-619d-15c3-08dc-dd55aa3a67ea] Encounter | 2025-07-17 | Consultation for treatment (procedure) | class AMB | reason: Contraception care (regime/therapy) | at NEW ENGLAND SINAI HOSPITAL
[Immunization/0e6e0d73-619d-15c3-f93b-2cd3ab790ac4] Immunization | 2026-05-25 | Hep A, adult | status completed | CVX 52
[Immunization/0e6e0d73-619d-15c3-e4c7-db7a86392a05] Immunization | 2026-05-25 | Influenza, split virus, trivalent, PF | status completed | CVX 140
[Immunization/0e6e0d73-619d-15c3-8254-2b4f6f2ea96c] Immunization | 2026-05-25 | Td (adult), 5 Lf tetanus toxoid, preservative free, adsorbed | status completed | CVX 113
[MedicationRequest/0e6e0d73-619d-15c3-53c7-cbba809d74d4] MedicationRequest | prescribed 2021-12-24 | status completed
[MedicationRequest/0e6e0d73-619d-15c3-13bd-a9b27df0c238] MedicationRequest | prescribed 2024-07-22 | status completed
[DocumentReference/1de68fee-45f3-6d87-010a-750782b94201#2] Clinical note | 2021-07-11 | part 2 of 2 | # Assessment and Plan Patient is presenting with acute bacterial sinusitis (disorder). ## Plan The patient was prescribed the following medications: - amoxicillin 250 mg / clavulanate 125 mg oral tablet
[DocumentReference/065f0a55-bf3e-9021-ff28-039c0e70053f#2] Clinical note | 2021-12-24 | part 2 of 2 | # Assessment and Plan ## Plan The following procedures were conducted: - intramuscular injection (procedure) The patient was prescribed the following medications: - 1 ml medroxyprogesterone acetate 150 mg/ml injection
[DocumentReference/a99414e6-fef2-4a1f-3b86-a18561dc8711#1] Clinical note | 2016-01-25 | part 1 of 1 | 2016-01-25 # Chief Complaint No complaints. # History of Present Illness Farah862 Beryl690 is a 31 year-old nonhispanic black female. Patient has a history of full-time employment (finding), stress (finding). # Social History Patient is married. Patient quit smoking at age 16. Patient identifies as heterosexual. Patient comes from a middle socioeconomic background. Patient has a high school education. Patient currently has Blue Cross Blue Shield. # Allergies No Known Allergies. # Medications No Active Medications. # Assessment and Plan ## Plan The patient was prescribed the following medications: - {5 (dienogest 2 mg / estradiol valerate 2 mg oral tablet) / 17 (dienogest 3 mg / estradiol valerate 2 mg oral tablet) / 2 (estradiol valerate 1 mg oral tablet) / 2 (estradiol valerate 3 mg oral tablet) / 2 (inert ingredients 1 mg oral tablet) } pack [natazia 28 day]
[DocumentReference/e798a7a8-625f-ec2b-0f31-62379ec468cf#2] Clinical note | 2021-08-07 | part 2 of 2 | # Assessment and Plan Patient is presenting with acute bronchitis (disorder). ## Plan The following procedures were conducted: - measurement of respiratory function (procedure) The patient was prescribed the following medications: - acetaminophen 325 mg oral tablet The patient was placed on a careplan: - respiratory therapy (procedure)
[MedicationRequest/0e6e0d73-619d-15c3-5bf9-7735ec346e03] MedicationRequest | prescribed 2021-08-07 | Acetaminophen 325 MG Oral Tablet | status completed | reason: Acute bronchitis (disorder) | RxNorm 313782
[MedicationRequest/0e6e0d73-619d-15c3-18ae-f182af13de87] MedicationRequest | prescribed 2017-09-23 | status completed | reason: Sepsis (disorder)
[MedicationRequest/0e6e0d73-619d-15c3-1e0d-46cb74202521] MedicationRequest | prescribed 2017-09-23 | status completed | reason: Sepsis (disorder)
[DocumentReference/a1166bcf-90d1-f82f-df67-ff9bee199661#2] Clinical note | 2025-07-17 | part 2 of 2 | # Medications acetaminophen 325 mg oral tablet; 21 day ethinyl estradiol 0.000625 mg/hr / etonogestrel 0.005 mg/hr vaginal system [nuvaring]; etonogestrel 68 mg drug implant; 150 ml vancomycin 5 mg/ml injection; {5 (dienogest 2 mg / estradiol valerate 2 mg oral tablet) / 17 (dienogest 3 mg / estradiol valerate 2 mg oral tablet) / 2 (estradiol valerate 1 mg oral tablet) / 2 (estradiol valerate 3 mg oral tablet) / 2 (inert ingredients 1 mg oral tablet) } pack [natazia 28 day]; 1 ml medroxyprogesterone acetate 150 mg/ml injection; piperacillin 2000 mg / tazobactam 250 mg injection; amoxicillin 250 mg / clavulanate 125 mg oral tablet # Assessment and Plan ## Plan The patient was prescribed the following medications: - {7 (ethinyl estradiol 0.035 mg / norgestimate 0.18 mg oral tablet) / 7 (ethinyl estradiol 0.035 mg / norgestimate 0.215 mg oral tablet) / 7 (ethinyl estradiol 0.035 mg / norgestimate 0.25 mg oral tablet) / 7 (inert ingredients 1 mg oral tablet) } pack [trinessa 28 day]
```

</details>

label: p?
note: The cited encounter supports a contraception care consultation on 2026-07-12, but it says nothing about the Levora prescription. The link is inferred from the matching date on the uncited MedicationRequest card, though a clinician would likely accept it.

## 19. `prescribed-for-essential-hypertension:772fc930#0#0`

Question: Which medications have been prescribed for the patient's essential hypertension?

Answer: **For essential hypertension, the patient has been prescribed Hydrochlorothiazide 25 MG Oral Tablet and lisinopril 10 MG Oral Tablet, both with active prescriptions dated 2026-07-16.** Earlier, now-completed prescriptions for Hydrochlorothiazide 25 MG Oral Tablet were dated 2026-07-02 and 2026-07-09. Earlier, now-completed prescriptions for lisinopril 10 MG Oral Tablet were dated 2021-08-26, 2026-07-02 and 2026-07-09.

Cards this sentence cites:

- `[MedicationRequest/772fc930-5418-0bfa-35ed-4b81c08cb46e]` MedicationRequest | prescribed 2026-07-16 | Hydrochlorothiazide 25 MG Oral Tablet | status active | reason: Essential hypertension (disorder) | RxNorm 310798
- `[MedicationRequest/772fc930-5418-0bfa-0d23-3b3c40dabcae]` MedicationRequest | prescribed 2026-07-16 | lisinopril 10 MG Oral Tablet | status active | reason: Essential hypertension (disorder) | RxNorm 314076

<details><summary>Everything the model saw (36 cards)</summary>

```text
[Condition/772fc930-5418-0bfa-5baf-97b1667a332f] Condition | onset 2026-07-09 | Part-time employment (finding) | clinical status active | SNOMED 160904001
[Condition/772fc930-5418-0bfa-446c-c28d224cff31] Condition | onset 2026-06-25 | Medication review due (situation) | clinical status active | SNOMED 314529007
[Condition/772fc930-5418-0bfa-33d9-881f0ecc07c1] Condition | onset 2026-06-11 | Stress (finding) | clinical status active | SNOMED 73595000
[Condition/772fc930-5418-0bfa-d3cc-a2daa4832199] Condition | onset 2026-02-19 | Chronic kidney disease stage 3 (disorder) | clinical status active | SNOMED 433144002
[Condition/772fc930-5418-0bfa-600b-5558ca66220a] Condition | onset 2026-02-19 | Proteinuria due to type 2 diabetes mellitus (disorder) | clinical status active | SNOMED 157141000119108
[Condition/772fc930-5418-0bfa-6352-6c3984966ef8] Condition | onset 2025-02-13 | Hyperlipidemia (disorder) | clinical status active | SNOMED 55822004
[Condition/772fc930-5418-0bfa-bb6d-8a0b90cf95e4] Condition | onset 2020-01-16 | Microalbuminuria due to type 2 diabetes mellitus (disorder) | clinical status active | SNOMED 90781000119102
[Condition/772fc930-5418-0bfa-ab71-24a74b1745fd] Condition | onset 2020-01-16 | Chronic kidney disease stage 2 (disorder) | clinical status active | SNOMED 431856006
[Condition/772fc930-5418-0bfa-beac-a103fe7f3fd2] Condition | onset 2019-01-10 | Disorder of kidney due to diabetes mellitus (disorder) | clinical status active | SNOMED 127013003
[Condition/772fc930-5418-0bfa-2c4f-3f5ed5953c36] Condition | onset 2019-01-10 | Chronic kidney disease stage 1 (disorder) | clinical status active | SNOMED 431855005
[Condition/772fc930-5418-0bfa-3873-02589386889d] Condition | onset 2004-06-19 | Osteoarthritis of hip (disorder) | clinical status active | SNOMED 239872002
[Condition/772fc930-5418-0bfa-a4a0-5eff492015a6] Condition | onset 1991-08-28 | History of coronary artery bypass grafting (situation) | clinical status active | SNOMED 399261000
[Condition/772fc930-5418-0bfa-01dc-3613408a83a6] Condition | onset 1991-08-22 | Abnormal findings diagnostic imaging heart+coronary circulat (finding) | clinical status active | SNOMED 274531002
[Condition/772fc930-5418-0bfa-35d2-44b4eb4fcccc] Condition | onset 1991-08-08 | Ischemic heart disease (disorder) | clinical status active | SNOMED 414545008
[Condition/772fc930-5418-0bfa-43ec-8fdd443cc6ce] Condition | onset 1988-07-21 | Gingivitis (disorder) | clinical status active | SNOMED 66383009
[Condition/772fc930-5418-0bfa-91e4-e46a214921b9] Condition | onset 1986-07-10 | Prediabetes (finding) | clinical status active | SNOMED 714628002
[Condition/772fc930-5418-0bfa-47df-a943ca27aa29] Condition | onset 1986-07-10 | Anemia (disorder) | clinical status active | SNOMED 271737000
[Condition/772fc930-5418-0bfa-7d09-0ea3ca1e93ba] Condition | onset 1986-03-30 | Obstructive sleep apnea syndrome (disorder) | clinical status active | SNOMED 78275009
[Condition/772fc930-5418-0bfa-1be5-06b5144b5817] Condition | onset 1986-03-01 | Sleep disorder (disorder) | clinical status active | SNOMED 39898005
[Condition/772fc930-5418-0bfa-0cdf-ac369e474ff3] Condition | onset 1977-05-19 | Essential hypertension (disorder) | clinical status active | SNOMED 59621000
[Condition/772fc930-5418-0bfa-f6df-7e2448081e0f] Condition | onset 1967-05-04 | Received higher education (finding) | clinical status active | SNOMED 224299000
[Condition/772fc930-5418-0bfa-ffbe-e3692c7542d7] Condition | onset 1964-01-15 | Chronic sinusitis (disorder) | clinical status active | SNOMED 40055000
[MedicationRequest/772fc930-5418-0bfa-d2b4-bc5609421614] MedicationRequest | prescribed 2026-07-16 | insulin isophane, human 70 UNT/ML / insulin, regular, human 30 UNT/ML Injectable Suspension [Humulin] | status active | reason: Prediabetes (finding) | RxNorm 106892
[MedicationRequest/772fc930-5418-0bfa-35ed-4b81c08cb46e] MedicationRequest | prescribed 2026-07-16 | Hydrochlorothiazide 25 MG Oral Tablet | status active | reason: Essential hypertension (disorder) | RxNorm 310798
[MedicationRequest/772fc930-5418-0bfa-0d23-3b3c40dabcae] MedicationRequest | prescribed 2026-07-16 | lisinopril 10 MG Oral Tablet | status active | reason: Essential hypertension (disorder) | RxNorm 314076
[MedicationRequest/772fc930-5418-0bfa-ac79-a5117bd68db1] MedicationRequest | prescribed 2026-03-06 | Simvastatin 10 MG Oral Tablet | status active | reason: Hyperlipidemia (disorder) | RxNorm 314231
[MedicationRequest/772fc930-5418-0bfa-dfc7-922f9300bced] MedicationRequest | prescribed 2004-06-19 | Naproxen sodium 220 MG Oral Tablet | status active | reason: Osteoarthritis of hip (disorder) | RxNorm 849574
[Encounter/772fc930-5418-0bfa-dd45-e4b82fc97e3d] Encounter | 2026-07-23 | Encounter for check up (procedure) | class AMB | at BOSTON MEDICAL CENTER CORPORATION-
[Encounter/772fc930-5418-0bfa-6606-662b1312d21c] Encounter | 2026-07-16 | Urgent care clinic (environment) | class AMB | at LYNN URGENT CARE LLC
[Encounter/772fc930-5418-0bfa-54c7-a3b13e8997b9] Encounter | 2026-07-09 | Emergency room admission (procedure) | class EMER | at LEONARD FLORENCE CENTER FOR LIVING
[Immunization/772fc930-5418-0bfa-fcca-2fca6db3fac3] Immunization | 2026-02-19 | Influenza, split virus, trivalent, PF | status completed | CVX 140
[MedicationRequest/772fc930-5418-0bfa-3648-8f2dee0d3e13] MedicationRequest | prescribed 2026-07-09 | Hydrochlorothiazide 25 MG Oral Tablet | status completed | reason: Essential hypertension (disorder) | RxNorm 310798
[MedicationRequest/772fc930-5418-0bfa-5a75-777528122cac] MedicationRequest | prescribed 2026-07-02 | Hydrochlorothiazide 25 MG Oral Tablet | status completed | reason: Essential hypertension (disorder) | RxNorm 310798
[MedicationRequest/772fc930-5418-0bfa-54d4-0d5c54ef37f9] MedicationRequest | prescribed 2021-08-26 | lisinopril 10 MG Oral Tablet | status completed | reason: Essential hypertension (disorder) | RxNorm 314076
[MedicationRequest/772fc930-5418-0bfa-92c6-1656ddca0b53] MedicationRequest | prescribed 2026-07-09 | lisinopril 10 MG Oral Tablet | status completed | reason: Essential hypertension (disorder) | RxNorm 314076
[MedicationRequest/772fc930-5418-0bfa-0876-1f10630a892a] MedicationRequest | prescribed 2026-07-02 | lisinopril 10 MG Oral Tablet | status completed | reason: Essential hypertension (disorder) | RxNorm 314076
```

</details>

label: s
note: The cited cards show HCTZ 25 MG and lisinopril 10 MG, both active, 2026-07-16, for essential hypertension; no other medication in the record has that reason, so the list is complete.

## 20. `last-colonoscopy:ef5e136c#0#1`

Question: When was the patient's most recent colonoscopy?

Answer: The patient's most recent colonoscopy was on 2024-04-17 (status completed). **Earlier colonoscopies were performed on 2022-11-29 and 2017-11-29.** A colon polyp found on 2022-11-29 was recorded as resolved on 2024-04-17.

Cards this sentence cites:

- `[Procedure/ef5e136c-ff1e-0695-f09f-74f1d600c1f4]` Procedure | 2022-11-29 | Colonoscopy (procedure) | status completed | SNOMED 73761001
- `[Procedure/ef5e136c-ff1e-0695-8a4e-a9576c900754]` Procedure | 2017-11-29 | Colonoscopy (procedure) | status completed | SNOMED 73761001

<details><summary>Everything the model saw (47 cards)</summary>

```text
[Condition/ef5e136c-ff1e-0695-1f8c-935a12106cac] Condition | onset 2026-09-30 | Medication review due (situation) | clinical status active | SNOMED 314529007
[Condition/ef5e136c-ff1e-0695-7e5d-470b95f60db2] Condition | onset 2026-09-23 | Social isolation (finding) | clinical status active | SNOMED 422650009
[Condition/ef5e136c-ff1e-0695-9d2d-c4be459bc9f4] Condition | onset 2026-09-09 | Unemployed (finding) | clinical status active | SNOMED 73438004
[Condition/ef5e136c-ff1e-0695-7b9c-f43e5ca3f6c6] Condition | onset 2026-08-12 | Stress (finding) | clinical status active | SNOMED 73595000
[Condition/ef5e136c-ff1e-0695-aa04-94486c99258f] Condition | onset 2025-08-27 | End-stage renal disease (disorder) | clinical status active | SNOMED 46177005
[Condition/ef5e136c-ff1e-0695-423f-ed71d76e81e3] Condition | onset 2025-03-30 | Awaiting transplantation of kidney (situation) | clinical status active | SNOMED 698306007
[Condition/ef5e136c-ff1e-0695-71df-3a96389b0a39] Condition | onset 2025-02-05 | Chronic kidney disease stage 4 (disorder) | clinical status active | SNOMED 431857002
[Condition/ef5e136c-ff1e-0695-5331-2d63eb213c34] Condition | onset 2024-05-15 | Proteinuria due to type 2 diabetes mellitus (disorder) | clinical status active | SNOMED 157141000119108
[Condition/ef5e136c-ff1e-0695-3834-fa6cb282a475] Condition | onset 2024-05-15 | Chronic kidney disease stage 3 (disorder) | clinical status active | SNOMED 433144002
[Condition/ef5e136c-ff1e-0695-68fe-9e2010333061] Condition | onset 2023-08-16 | Microalbuminuria due to type 2 diabetes mellitus (disorder) | clinical status active | SNOMED 90781000119102
[Condition/ef5e136c-ff1e-0695-65f5-8d04f278a661] Condition | onset 2023-08-16 | Chronic kidney disease stage 2 (disorder) | clinical status active | SNOMED 431856006
[Condition/ef5e136c-ff1e-0695-aac2-46a0ff462178] Condition | onset 2023-04-19 | Gingivitis (disorder) | clinical status active | SNOMED 66383009
[Condition/ef5e136c-ff1e-0695-fda2-40e12f6b17a7] Condition | onset 2017-11-15 | Chronic kidney disease stage 1 (disorder) | clinical status active | SNOMED 431855005
[Condition/ef5e136c-ff1e-0695-bf3f-30946ad3f8b4] Condition | onset 2017-11-15 | Disorder of kidney due to diabetes mellitus (disorder) | clinical status active | SNOMED 127013003
[Condition/ef5e136c-ff1e-0695-eac4-d545a0296998] Condition | onset 2011-07-27 | Essential hypertension (disorder) | clinical status active | SNOMED 59621000
[Condition/ef5e136c-ff1e-0695-b228-2f5ff5bb47cb] Condition | onset 2010-05-19 | Metabolic syndrome X (disorder) | clinical status active | SNOMED 237602007
[Condition/ef5e136c-ff1e-0695-af16-82f03f777ba8] Condition | onset 2010-05-19 | Hypertriglyceridemia (disorder) | clinical status active | SNOMED 302870006
[Condition/ef5e136c-ff1e-0695-5ca5-51bfdc51320e] Condition | onset 2010-05-12 | Diabetes mellitus type 2 (disorder) | clinical status active | SNOMED 44054006
[Condition/ef5e136c-ff1e-0695-f7ec-ceae0c2566bc] Condition | onset 2004-06-16 | Body mass index 30+ - obesity (finding) | clinical status active | SNOMED 162864005
[Condition/ef5e136c-ff1e-0695-c94a-5d81ddd88117] Condition | onset 1997-05-07 | Has a criminal record (finding) | clinical status active | SNOMED 266948004
[Condition/ef5e136c-ff1e-0695-6efc-9f7d5e6b04ef] Condition | onset 1993-09-01 | Anemia (disorder) | clinical status active | SNOMED 271737000
[Condition/ef5e136c-ff1e-0695-1f68-dac24351dbaa] Condition | onset 1993-04-14 | Prediabetes (finding) | clinical status active | SNOMED 714628002
[Condition/ef5e136c-ff1e-0695-2d8d-328849698529] Condition | onset 1993-01-22 | History of tubal ligation (situation) | clinical status active | SNOMED 267020005
[Condition/ef5e136c-ff1e-0695-0825-c31e8b252683] Condition | onset 1983-11-14 | Past pregnancy history of miscarriage (situation) | clinical status active | SNOMED 161744009
[Condition/ef5e136c-ff1e-0695-cb16-3a98eeb2de7a] Condition | onset 1976-01-07 | Received higher education (finding) | clinical status active | SNOMED 224299000
[Condition/ef5e136c-ff1e-0695-3278-6a86eaf1fb5d] Condition | onset 1975-06-27 | Chronic sinusitis (disorder) | clinical status active | SNOMED 40055000
[Condition/ef5e136c-ff1e-0695-337f-d12087c8dbb5] Condition | onset 1975-01-01 | Risk activity involvement (finding) | clinical status active | SNOMED 160968000
[MedicationRequest/ef5e136c-ff1e-0695-ffec-2ea7ac772a27] MedicationRequest | prescribed 2026-09-30 | Hydrochlorothiazide 25 MG Oral Tablet | status active | reason: Essential hypertension (disorder) | RxNorm 310798
[MedicationRequest/ef5e136c-ff1e-0695-b3ba-a1ec7bcfb9f4] MedicationRequest | prescribed 2026-09-30 | albuterol 0.83 MG/ML Inhalation Solution | status active | RxNorm 630208
[MedicationRequest/ef5e136c-ff1e-0695-901e-2e1f9afb0cca] MedicationRequest | prescribed 2026-09-30 | lisinopril 10 MG Oral Tablet | status active | reason: Essential hypertension (disorder) | RxNorm 314076
[MedicationRequest/ef5e136c-ff1e-0695-76a6-8eeb54f8a75e] MedicationRequest | prescribed 2026-09-30 | 120 ACTUAT fluticasone propionate 0.044 MG/ACTUAT Metered Dose Inhaler [Flovent] | status active | RxNorm 895996
[MedicationRequest/ef5e136c-ff1e-0695-6c6d-182c3b9c47c1] MedicationRequest | prescribed 2026-09-30 | amLODIPine 2.5 MG Oral Tablet | status active | reason: Essential hypertension (disorder) | RxNorm 308136
[MedicationRequest/ef5e136c-ff1e-0695-6804-cf31640a9491] MedicationRequest | prescribed 2026-09-30 | insulin isophane, human 70 UNT/ML / insulin, regular, human 30 UNT/ML Injectable Suspension [Humulin] | status active | reason: Diabetes mellitus type 2 (disorder) | RxNorm 106892
[Encounter/ef5e136c-ff1e-0695-08ba-2471a16a6570] Encounter | 2026-09-30 | Emergency room admission (procedure) | class EMER | at APPLE VALLEY CENTER
[Encounter/ef5e136c-ff1e-0695-aea4-11055569fd51] Encounter | 2026-09-23 | Urgent care clinic (environment) | class AMB | at URGENT HELP CHELMSFORD PC
[Encounter/ef5e136c-ff1e-0695-4a41-6fca58c80cb7] Encounter | 2026-09-16 | Urgent care clinic (environment) | class AMB | at URGENT HELP CHELMSFORD PC
[Immunization/ef5e136c-ff1e-0695-6beb-93901776b619] Immunization | 2026-05-13 | Influenza, split virus, trivalent, PF | status completed | CVX 140
[Procedure/ef5e136c-ff1e-0695-6492-376000eaabc8] Procedure | 2024-04-17 | Colonoscopy (procedure) | status completed | SNOMED 73761001
[Procedure/ef5e136c-ff1e-0695-f09f-74f1d600c1f4] Procedure | 2022-11-29 | Colonoscopy (procedure) | status completed | SNOMED 73761001
[Procedure/ef5e136c-ff1e-0695-8a4e-a9576c900754] Procedure | 2017-11-29 | Colonoscopy (procedure) | status completed | SNOMED 73761001
[Condition/ef5e136c-ff1e-0695-48e1-d64ec86cb18d] Condition | onset 2022-11-29 | Polyp of colon (disorder) | clinical status resolved | resolved 2024-04-17 | SNOMED 68496003
[Immunization/ef5e136c-ff1e-0695-358d-908aa385ad32] Immunization | 2021-07-28 | COVID-19, mRNA, LNP-S, PF, 100 mcg/0.5mL dose or 50 mcg/0.25mL dose | status completed | CVX 207
[Immunization/ef5e136c-ff1e-0695-43d1-1c013e357b6c] Immunization | 2021-06-30 | COVID-19, mRNA, LNP-S, PF, 100 mcg/0.5mL dose or 50 mcg/0.25mL dose | status completed | CVX 207
[Procedure/ef5e136c-ff1e-0695-a1b4-af5e716e7746] Procedure | 2022-11-29 | Screening for occult blood in feces (procedure) | status completed | reason: Polyp of colon (disorder) | SNOMED 104435004
[Condition/ef5e136c-ff1e-0695-fa1e-dadf939797f8] Condition | onset 2025-05-14 | Maxillary fracture, unspecified side, sequela | clinical status resolved | resolved 2025-07-23 | http://hl7.org/fhir/sid/icd-10 S02.401S
[Procedure/ef5e136c-ff1e-0695-e258-f6ce1deb890c] Procedure | 2022-11-29 | Rectal polypectomy (procedure) | status completed | reason: Polyp of colon (disorder) | SNOMED 274031008
[DocumentReference/ad64bd03-d904-8f43-8f5e-28147af12244#2] Clinical note | 2024-04-17 | part 2 of 2 | # Medications lisinopril 10 mg oral tablet; tropicamide 5 mg/ml ophthalmic solution; hydrochlorothiazide 25 mg oral tablet; amoxicillin 250 mg oral capsule; acetaminophen 325 mg / oxycodone hydrochloride 5 mg oral tablet; 120 actuat fluticasone propionate 0.044 mg/actuat metered dose inhaler [flovent]; amlodipine 2.5 mg oral tablet; insulin isophane, human 70 unt/ml / insulin, regular, human 30 unt/ml injectable suspension [humulin]; albuterol 0.83 mg/ml inhalation solution; naproxen sodium 220 mg oral tablet # Assessment and Plan ## Plan The following procedures were conducted: - colonoscopy (procedure)
```

</details>

label: s
note: There are three colonoscopy procedures (2024-04-17, 2022-11-29, 2017-11-29); the two earlier than the most recent are exactly the cited 2022-11-29 and 2017-11-29 completed entries.

## 21. `latest-bp:ef5e136c#0#0`

Question: What was the patient's most recent blood pressure reading?

Answer: **The most recent blood pressure reading was on 2026-09-23: Systolic Blood Pressure 115 mm[Hg] and Diastolic Blood Pressure 60 mm[Hg].**

Cards this sentence cites:

- `[Observation/ef5e136c-ff1e-0695-8150-2ef2105a3233]` Observation (vital-signs) | 2026-09-23 | Blood pressure panel with all children optional = Diastolic Blood Pressure 60 mm[Hg]; Systolic Blood Pressure 115 mm[Hg] | status final | LOINC 85354-9

<details><summary>Everything the model saw (41 cards)</summary>

```text
[Condition/ef5e136c-ff1e-0695-1f8c-935a12106cac] Condition | onset 2026-09-30 | Medication review due (situation) | clinical status active | SNOMED 314529007
[Condition/ef5e136c-ff1e-0695-7e5d-470b95f60db2] Condition | onset 2026-09-23 | Social isolation (finding) | clinical status active | SNOMED 422650009
[Condition/ef5e136c-ff1e-0695-9d2d-c4be459bc9f4] Condition | onset 2026-09-09 | Unemployed (finding) | clinical status active | SNOMED 73438004
[Condition/ef5e136c-ff1e-0695-7b9c-f43e5ca3f6c6] Condition | onset 2026-08-12 | Stress (finding) | clinical status active | SNOMED 73595000
[Condition/ef5e136c-ff1e-0695-aa04-94486c99258f] Condition | onset 2025-08-27 | End-stage renal disease (disorder) | clinical status active | SNOMED 46177005
[Condition/ef5e136c-ff1e-0695-423f-ed71d76e81e3] Condition | onset 2025-03-30 | Awaiting transplantation of kidney (situation) | clinical status active | SNOMED 698306007
[Condition/ef5e136c-ff1e-0695-71df-3a96389b0a39] Condition | onset 2025-02-05 | Chronic kidney disease stage 4 (disorder) | clinical status active | SNOMED 431857002
[Condition/ef5e136c-ff1e-0695-5331-2d63eb213c34] Condition | onset 2024-05-15 | Proteinuria due to type 2 diabetes mellitus (disorder) | clinical status active | SNOMED 157141000119108
[Condition/ef5e136c-ff1e-0695-3834-fa6cb282a475] Condition | onset 2024-05-15 | Chronic kidney disease stage 3 (disorder) | clinical status active | SNOMED 433144002
[Condition/ef5e136c-ff1e-0695-68fe-9e2010333061] Condition | onset 2023-08-16 | Microalbuminuria due to type 2 diabetes mellitus (disorder) | clinical status active | SNOMED 90781000119102
[Condition/ef5e136c-ff1e-0695-65f5-8d04f278a661] Condition | onset 2023-08-16 | Chronic kidney disease stage 2 (disorder) | clinical status active | SNOMED 431856006
[Condition/ef5e136c-ff1e-0695-aac2-46a0ff462178] Condition | onset 2023-04-19 | Gingivitis (disorder) | clinical status active | SNOMED 66383009
[Condition/ef5e136c-ff1e-0695-fda2-40e12f6b17a7] Condition | onset 2017-11-15 | Chronic kidney disease stage 1 (disorder) | clinical status active | SNOMED 431855005
[Condition/ef5e136c-ff1e-0695-bf3f-30946ad3f8b4] Condition | onset 2017-11-15 | Disorder of kidney due to diabetes mellitus (disorder) | clinical status active | SNOMED 127013003
[Condition/ef5e136c-ff1e-0695-eac4-d545a0296998] Condition | onset 2011-07-27 | Essential hypertension (disorder) | clinical status active | SNOMED 59621000
[Condition/ef5e136c-ff1e-0695-b228-2f5ff5bb47cb] Condition | onset 2010-05-19 | Metabolic syndrome X (disorder) | clinical status active | SNOMED 237602007
[Condition/ef5e136c-ff1e-0695-af16-82f03f777ba8] Condition | onset 2010-05-19 | Hypertriglyceridemia (disorder) | clinical status active | SNOMED 302870006
[Condition/ef5e136c-ff1e-0695-5ca5-51bfdc51320e] Condition | onset 2010-05-12 | Diabetes mellitus type 2 (disorder) | clinical status active | SNOMED 44054006
[Condition/ef5e136c-ff1e-0695-f7ec-ceae0c2566bc] Condition | onset 2004-06-16 | Body mass index 30+ - obesity (finding) | clinical status active | SNOMED 162864005
[Condition/ef5e136c-ff1e-0695-c94a-5d81ddd88117] Condition | onset 1997-05-07 | Has a criminal record (finding) | clinical status active | SNOMED 266948004
[Condition/ef5e136c-ff1e-0695-6efc-9f7d5e6b04ef] Condition | onset 1993-09-01 | Anemia (disorder) | clinical status active | SNOMED 271737000
[Condition/ef5e136c-ff1e-0695-1f68-dac24351dbaa] Condition | onset 1993-04-14 | Prediabetes (finding) | clinical status active | SNOMED 714628002
[Condition/ef5e136c-ff1e-0695-2d8d-328849698529] Condition | onset 1993-01-22 | History of tubal ligation (situation) | clinical status active | SNOMED 267020005
[Condition/ef5e136c-ff1e-0695-0825-c31e8b252683] Condition | onset 1983-11-14 | Past pregnancy history of miscarriage (situation) | clinical status active | SNOMED 161744009
[Condition/ef5e136c-ff1e-0695-cb16-3a98eeb2de7a] Condition | onset 1976-01-07 | Received higher education (finding) | clinical status active | SNOMED 224299000
[Condition/ef5e136c-ff1e-0695-3278-6a86eaf1fb5d] Condition | onset 1975-06-27 | Chronic sinusitis (disorder) | clinical status active | SNOMED 40055000
[Condition/ef5e136c-ff1e-0695-337f-d12087c8dbb5] Condition | onset 1975-01-01 | Risk activity involvement (finding) | clinical status active | SNOMED 160968000
[MedicationRequest/ef5e136c-ff1e-0695-ffec-2ea7ac772a27] MedicationRequest | prescribed 2026-09-30 | Hydrochlorothiazide 25 MG Oral Tablet | status active | reason: Essential hypertension (disorder) | RxNorm 310798
[MedicationRequest/ef5e136c-ff1e-0695-b3ba-a1ec7bcfb9f4] MedicationRequest | prescribed 2026-09-30 | albuterol 0.83 MG/ML Inhalation Solution | status active | RxNorm 630208
[MedicationRequest/ef5e136c-ff1e-0695-901e-2e1f9afb0cca] MedicationRequest | prescribed 2026-09-30 | lisinopril 10 MG Oral Tablet | status active | reason: Essential hypertension (disorder) | RxNorm 314076
[MedicationRequest/ef5e136c-ff1e-0695-76a6-8eeb54f8a75e] MedicationRequest | prescribed 2026-09-30 | 120 ACTUAT fluticasone propionate 0.044 MG/ACTUAT Metered Dose Inhaler [Flovent] | status active | RxNorm 895996
[MedicationRequest/ef5e136c-ff1e-0695-6c6d-182c3b9c47c1] MedicationRequest | prescribed 2026-09-30 | amLODIPine 2.5 MG Oral Tablet | status active | reason: Essential hypertension (disorder) | RxNorm 308136
[MedicationRequest/ef5e136c-ff1e-0695-6804-cf31640a9491] MedicationRequest | prescribed 2026-09-30 | insulin isophane, human 70 UNT/ML / insulin, regular, human 30 UNT/ML Injectable Suspension [Humulin] | status active | reason: Diabetes mellitus type 2 (disorder) | RxNorm 106892
[Encounter/ef5e136c-ff1e-0695-08ba-2471a16a6570] Encounter | 2026-09-30 | Emergency room admission (procedure) | class EMER | at APPLE VALLEY CENTER
[Encounter/ef5e136c-ff1e-0695-aea4-11055569fd51] Encounter | 2026-09-23 | Urgent care clinic (environment) | class AMB | at URGENT HELP CHELMSFORD PC
[Encounter/ef5e136c-ff1e-0695-4a41-6fca58c80cb7] Encounter | 2026-09-16 | Urgent care clinic (environment) | class AMB | at URGENT HELP CHELMSFORD PC
[Immunization/ef5e136c-ff1e-0695-6beb-93901776b619] Immunization | 2026-05-13 | Influenza, split virus, trivalent, PF | status completed | CVX 140
[Observation/ef5e136c-ff1e-0695-e97d-34c3c9cb7062] Observation (vital-signs) | 2026-07-01 | Blood pressure panel with all children optional = Diastolic Blood Pressure 67 mm[Hg]; Systolic Blood Pressure 116 mm[Hg] | status final | LOINC 85354-9
[Observation/ef5e136c-ff1e-0695-8150-2ef2105a3233] Observation (vital-signs) | 2026-09-23 | Blood pressure panel with all children optional = Diastolic Blood Pressure 60 mm[Hg]; Systolic Blood Pressure 115 mm[Hg] | status final | LOINC 85354-9
[Observation/ef5e136c-ff1e-0695-e1dc-2e5f1dd38840] Observation (vital-signs) | 2026-09-09 | Blood pressure panel with all children optional = Diastolic Blood Pressure 60 mm[Hg]; Systolic Blood Pressure 114 mm[Hg] | status final | LOINC 85354-9
[Observation/ef5e136c-ff1e-0695-eceb-e6bdd735d27d] Observation (vital-signs) | 2026-08-26 | Blood pressure panel with all children optional = Diastolic Blood Pressure 67 mm[Hg]; Systolic Blood Pressure 111 mm[Hg] | status final | LOINC 85354-9
```

</details>

label: s
note: Cited 2026-09-23 panel shows Systolic 115 / Diastolic 60 mm[Hg]; the other BP panels seen (2026-07-01, 2026-08-26, 2026-09-09) are all earlier, so it is the most recent.

## 22. `prescribed-for-acute-bacterial-sinusitis:0e6e0d73#0#1`

Question: Which medications have been prescribed for the patient's acute bacterial sinusitis?

Answer: For acute bacterial sinusitis (onset 2021-07-11, resolved 2021-08-03), the patient was prescribed Amoxicillin 250 MG / Clavulanate 125 MG Oral Tablet on 2021-07-11, and this prescription has status completed. **The same drug was also prescribed on 2019-01-08, but for viral sinusitis, not acute bacterial sinusitis.**

Cards this sentence cites:

- `[MedicationRequest/0e6e0d73-619d-15c3-a36c-70d5b764c793]` MedicationRequest | prescribed 2019-01-08 | Amoxicillin 250 MG / Clavulanate 125 MG Oral Tablet | status completed | reason: Viral sinusitis (disorder) | RxNorm 562251

<details><summary>Everything the model saw (26 cards)</summary>

```text
[Condition/0e6e0d73-619d-15c3-1198-27a3f1e6671d] Condition | onset 2026-05-25 | Full-time employment (finding) | clinical status active | SNOMED 160903007
[Condition/0e6e0d73-619d-15c3-73bb-c4435e198a52] Condition | onset 2021-08-16 | Unhealthy alcohol drinking behavior (finding) | clinical status active | SNOMED 10939881000119105
[Condition/0e6e0d73-619d-15c3-a2af-2198a3d15909] Condition | onset 2021-08-02 | Medication review due (situation) | clinical status active | SNOMED 314529007
[Condition/0e6e0d73-619d-15c3-7d75-d0dd94ac6175] Condition | onset 2018-04-30 | Past pregnancy history of miscarriage (situation) | clinical status active | SNOMED 161744009
[Condition/0e6e0d73-619d-15c3-dabb-3f18b4ab6eed] Condition | onset 2017-09-23 | Sepsis (disorder) | clinical status active | SNOMED 91302008
[Condition/0e6e0d73-619d-15c3-279b-bad1f131dc84] Condition | onset 2017-09-23 | Septic shock (disorder) | clinical status active | SNOMED 76571007
[Condition/0e6e0d73-619d-15c3-252c-3ec5aec72d7f] Condition | onset 2006-07-17 | Victim of intimate partner abuse (finding) | clinical status active | SNOMED 706893006
[Condition/0e6e0d73-619d-15c3-a3b6-7fc6f2b594a9] Condition | onset 2002-07-08 | Educated to high school level (finding) | clinical status active | SNOMED 473461003
[Condition/0e6e0d73-619d-15c3-a0ee-8e9994e38bf4] Condition | onset 2001-07-02 | Risk activity involvement (finding) | clinical status active | SNOMED 160968000
[MedicationRequest/0e6e0d73-619d-15c3-e363-3a1afa521a17] MedicationRequest | prescribed 2026-07-12 | {21 (ethinyl estradiol 0.03 MG / levonorgestrel 0.15 MG Oral Tablet) / 7 (inert ingredients 1 MG Oral Tablet) } Pack [Levora 0.15/30 28 Day] | status active | RxNorm 748879
[Encounter/0e6e0d73-619d-15c3-9366-052e1e643c56] Encounter | 2026-07-12 | Consultation for treatment (procedure) | class AMB | reason: Contraception care (regime/therapy) | at NEW ENGLAND SINAI HOSPITAL
[Encounter/0e6e0d73-619d-15c3-60c1-89e78f0afd63] Encounter | 2026-05-25 | General examination of patient (procedure) | class AMB | at ENRICH WELLNESS HEALTH CENTER LLC
[Encounter/0e6e0d73-619d-15c3-08dc-dd55aa3a67ea] Encounter | 2025-07-17 | Consultation for treatment (procedure) | class AMB | reason: Contraception care (regime/therapy) | at NEW ENGLAND SINAI HOSPITAL
[Immunization/0e6e0d73-619d-15c3-f93b-2cd3ab790ac4] Immunization | 2026-05-25 | Hep A, adult | status completed | CVX 52
[Immunization/0e6e0d73-619d-15c3-e4c7-db7a86392a05] Immunization | 2026-05-25 | Influenza, split virus, trivalent, PF | status completed | CVX 140
[Immunization/0e6e0d73-619d-15c3-8254-2b4f6f2ea96c] Immunization | 2026-05-25 | Td (adult), 5 Lf tetanus toxoid, preservative free, adsorbed | status completed | CVX 113
[DocumentReference/1de68fee-45f3-6d87-010a-750782b94201#2] Clinical note | 2021-07-11 | part 2 of 2 | # Assessment and Plan Patient is presenting with acute bacterial sinusitis (disorder). ## Plan The patient was prescribed the following medications: - amoxicillin 250 mg / clavulanate 125 mg oral tablet
[MedicationRequest/0e6e0d73-619d-15c3-711f-345ffccf4ca5] MedicationRequest | prescribed 2021-07-11 | Amoxicillin 250 MG / Clavulanate 125 MG Oral Tablet | status completed | reason: Acute bacterial sinusitis (disorder) | RxNorm 562251
[MedicationRequest/0e6e0d73-619d-15c3-a36c-70d5b764c793] MedicationRequest | prescribed 2019-01-08 | Amoxicillin 250 MG / Clavulanate 125 MG Oral Tablet | status completed | reason: Viral sinusitis (disorder) | RxNorm 562251
[Condition/0e6e0d73-619d-15c3-e56e-1a917dcb8dde] Condition | onset 2021-07-11 | Acute bacterial sinusitis (disorder) | clinical status resolved | resolved 2021-08-03 | SNOMED 75498004
[Encounter/0e6e0d73-619d-15c3-33f5-5ccf62390c23] Encounter | 2021-07-11 | Encounter for symptom (procedure) | class AMB | reason: Acute bacterial sinusitis (disorder) | at NEW ENGLAND SINAI HOSPITAL
[MedicationRequest/0e6e0d73-619d-15c3-5bf9-7735ec346e03] MedicationRequest | prescribed 2021-08-07 | Acetaminophen 325 MG Oral Tablet | status completed | reason: Acute bronchitis (disorder) | RxNorm 313782
[DocumentReference/e798a7a8-625f-ec2b-0f31-62379ec468cf#2] Clinical note | 2021-08-07 | part 2 of 2 | # Assessment and Plan Patient is presenting with acute bronchitis (disorder). ## Plan The following procedures were conducted: - measurement of respiratory function (procedure) The patient was prescribed the following medications: - acetaminophen 325 mg oral tablet The patient was placed on a careplan: - respiratory therapy (procedure)
[DocumentReference/76f78d5e-ac2c-3184-bec1-bfd837d5254a#1] Clinical note | 2024-04-22 | part 1 of 2 | 2024-04-22 # Chief Complaint No complaints. # History of Present Illness Farah862 Beryl690 is a 39 year-old nonhispanic black female. Patient has a history of acute bacterial sinusitis (disorder), acute bronchitis (disorder), medication review due (situation), full-time employment (finding), miscarriage in first trimester (disorder), unemployed (finding), viral sinusitis (disorder), complete miscarriage (disorder), stress (finding), normal pregnancy (finding). # Social History Patient is married. Patient quit smoking at age 16. Patient identifies as heterosexual. Patient comes from a middle socioeconomic background. Patient has a high school education. Patient currently has Blue Cross Blue Shield. # Allergies No Known Allergies. # Medications acetaminophen 325 mg oral tablet; 21 day ethinyl estradiol 0.000625 mg/hr / etonogestrel 0.005 mg/hr vaginal system [nuvaring]; 150 ml vancomycin 5 mg/ml injection; {5 (dienogest 2 mg / estradiol valerate 2 mg oral tablet) / 17 (dienogest 3 mg / estradiol valerate 2 mg oral tablet) / 2 (estradiol valerate 1 mg oral tablet) / 2 (estradiol valerate 3 mg oral tablet) / 2 (inert ingredients 1 mg oral tablet) } pack [natazia 28 day]; 1 ml medroxyprogesterone acetate 150 mg/ml injection; piperacillin 2000 mg / tazobactam 250 mg injection; amoxicillin 250 mg / clavulanate 125 mg oral tablet
[DocumentReference/fd7d64b9-19b2-61f7-1bf6-2db26001936d#1] Clinical note | 2023-12-04 | part 1 of 2 | 2023-12-04 # Chief Complaint No complaints. # History of Present Illness Farah862 Beryl690 is a 39 year-old nonhispanic black female. Patient has a history of acute bacterial sinusitis (disorder), acute bronchitis (disorder), medication review due (situation), full-time employment (finding), miscarriage in first trimester (disorder), unemployed (finding), viral sinusitis (disorder), complete miscarriage (disorder), stress (finding), normal pregnancy (finding). # Social History Patient is married. Patient quit smoking at age 16. Patient identifies as heterosexual. Patient comes from a middle socioeconomic background. Patient has a high school education. Patient currently has Blue Cross Blue Shield. # Allergies No Known Allergies. # Medications acetaminophen 325 mg oral tablet; 21 day ethinyl estradiol 0.000625 mg/hr / etonogestrel 0.005 mg/hr vaginal system [nuvaring]; 150 ml vancomycin 5 mg/ml injection; {5 (dienogest 2 mg / estradiol valerate 2 mg oral tablet) / 17 (dienogest 3 mg / estradiol valerate 2 mg oral tablet) / 2 (estradiol valerate 1 mg oral tablet) / 2 (estradiol valerate 3 mg oral tablet) / 2 (inert ingredients 1 mg oral tablet) } pack [natazia 28 day]; 1 ml medroxyprogesterone acetate 150 mg/ml injection; piperacillin 2000 mg / tazobactam 250 mg injection; amoxicillin 250 mg / clavulanate 125 mg oral tablet
[DocumentReference/6dd5703a-f87e-5aa8-16c9-3682c2b0d434#1] Clinical note | 2024-02-26 | part 1 of 2 | 2024-02-26 # Chief Complaint No complaints. # History of Present Illness Farah862 Beryl690 is a 39 year-old nonhispanic black female. Patient has a history of acute bacterial sinusitis (disorder), acute bronchitis (disorder), medication review due (situation), full-time employment (finding), miscarriage in first trimester (disorder), unemployed (finding), viral sinusitis (disorder), complete miscarriage (disorder), stress (finding), normal pregnancy (finding). # Social History Patient is married. Patient quit smoking at age 16. Patient identifies as heterosexual. Patient comes from a middle socioeconomic background. Patient has a high school education. Patient currently has Blue Cross Blue Shield. # Allergies No Known Allergies. # Medications acetaminophen 325 mg oral tablet; 21 day ethinyl estradiol 0.000625 mg/hr / etonogestrel 0.005 mg/hr vaginal system [nuvaring]; 150 ml vancomycin 5 mg/ml injection; {5 (dienogest 2 mg / estradiol valerate 2 mg oral tablet) / 17 (dienogest 3 mg / estradiol valerate 2 mg oral tablet) / 2 (estradiol valerate 1 mg oral tablet) / 2 (estradiol valerate 3 mg oral tablet) / 2 (inert ingredients 1 mg oral tablet) } pack [natazia 28 day]; 1 ml medroxyprogesterone acetate 150 mg/ml injection; piperacillin 2000 mg / tazobactam 250 mg injection; amoxicillin 250 mg / clavulanate 125 mg oral tablet
```

</details>

label: s
note: Cited MedicationRequest dated 2019-01-08 is the same Amoxicillin 250 MG / Clavulanate 125 MG tablet (RxNorm 562251) with reason Viral sinusitis.

## 23. `current-meds:d4f2a6f8#0#2`

Question: What medications is the patient currently prescribed?

Answer: The patient's active prescriptions for essential hypertension are hydrochlorothiazide 25 MG oral tablet, lisinopril 10 MG oral tablet, and amLODIPine 2.5 MG oral tablet, all prescribed 2026-04-09. Also active is Humulin (insulin isophane, human 70 UNT/ML / insulin, regular, human 30 UNT/ML injectable suspension), prescribed 2026-04-09 with prediabetes listed as the reason. **Additional active prescriptions from 2020-03-12 are simvastatin 20 MG oral tablet, nitroglycerin 0.4 MG/ACTUAT mucosal spray, 24 HR metoprolol succinate 100 MG extended release oral tablet, and clopidogrel 75 MG oral tablet.**

Cards this sentence cites:

- `[MedicationRequest/d4f2a6f8-e358-6b1b-f33b-aeabe5d3ea2a]` MedicationRequest | prescribed 2020-03-12 | Simvastatin 20 MG Oral Tablet | status active | RxNorm 312961
- `[MedicationRequest/d4f2a6f8-e358-6b1b-da7b-92b61020d936]` MedicationRequest | prescribed 2020-03-12 | Nitroglycerin 0.4 MG/ACTUAT Mucosal Spray | status active | RxNorm 705129
- `[MedicationRequest/d4f2a6f8-e358-6b1b-c7c5-6dd35faf2d76]` MedicationRequest | prescribed 2020-03-12 | 24 HR metoprolol succinate 100 MG Extended Release Oral Tablet | status active | RxNorm 866412
- `[MedicationRequest/d4f2a6f8-e358-6b1b-102e-595eecaa5a85]` MedicationRequest | prescribed 2020-03-12 | Clopidogrel 75 MG Oral Tablet | status active | RxNorm 309362

<details><summary>Everything the model saw (42 cards)</summary>

```text
[Condition/d4f2a6f8-e358-6b1b-a870-7578fc115ba3] Condition | onset 2026-04-02 | Stress (finding) | clinical status active | SNOMED 73595000
[Condition/d4f2a6f8-e358-6b1b-37cc-cacad982df8c] Condition | onset 2026-04-02 | Reports of violence in the environment (finding) | clinical status active | SNOMED 424393004
[Condition/d4f2a6f8-e358-6b1b-c78d-1b6bc447e34a] Condition | onset 2025-12-04 | Full-time employment (finding) | clinical status active | SNOMED 160903007
[Condition/d4f2a6f8-e358-6b1b-29d8-fc1e6a15e60d] Condition | onset 2025-12-04 | Medication review due (situation) | clinical status active | SNOMED 314529007
[Condition/d4f2a6f8-e358-6b1b-f1ac-92593f6454e7] Condition | onset 2025-03-20 | Chronic kidney disease stage 4 (disorder) | clinical status active | SNOMED 431857002
[Condition/d4f2a6f8-e358-6b1b-4959-9b97d2d3536d] Condition | onset 2025-02-03 | Awaiting transplantation of kidney (situation) | clinical status active | SNOMED 698306007
[Condition/d4f2a6f8-e358-6b1b-76dc-8902de051de4] Condition | onset 2022-10-20 | Microalbuminuria due to type 2 diabetes mellitus (disorder) | clinical status active | SNOMED 90781000119102
[Condition/d4f2a6f8-e358-6b1b-1e8b-4beeba77ed82] Condition | onset 2022-10-20 | Proteinuria due to type 2 diabetes mellitus (disorder) | clinical status active | SNOMED 157141000119108
[Condition/d4f2a6f8-e358-6b1b-042a-23b17f3aef58] Condition | onset 2022-10-20 | Chronic kidney disease stage 3 (disorder) | clinical status active | SNOMED 433144002
[Condition/d4f2a6f8-e358-6b1b-7e47-2334f6b84c0f] Condition | onset 2020-05-28 | History of coronary artery bypass grafting (situation) | clinical status active | SNOMED 399261000
[Condition/d4f2a6f8-e358-6b1b-ebe7-54c5d38117fc] Condition | onset 2020-03-19 | Abnormal findings diagnostic imaging heart+coronary circulat (finding) | clinical status active | SNOMED 274531002
[Condition/d4f2a6f8-e358-6b1b-e1e3-648cc0a38c11] Condition | onset 2020-03-05 | Chronic kidney disease stage 1 (disorder) | clinical status active | SNOMED 431855005
[Condition/d4f2a6f8-e358-6b1b-7f62-e48c3798c8b1] Condition | onset 2020-03-05 | Disorder of kidney due to diabetes mellitus (disorder) | clinical status active | SNOMED 127013003
[Condition/d4f2a6f8-e358-6b1b-6866-45937dfd6387] Condition | onset 2020-03-05 | Ischemic heart disease (disorder) | clinical status active | SNOMED 414545008
[Condition/d4f2a6f8-e358-6b1b-9d41-102804feed92] Condition | onset 2004-12-09 | Metabolic syndrome X (disorder) | clinical status active | SNOMED 237602007
[Condition/d4f2a6f8-e358-6b1b-4dab-6274d2854b00] Condition | onset 2002-11-28 | Anemia (disorder) | clinical status active | SNOMED 271737000
[Condition/d4f2a6f8-e358-6b1b-c5c9-83d1526dc404] Condition | onset 2001-11-22 | Essential hypertension (disorder) | clinical status active | SNOMED 59621000
[Condition/d4f2a6f8-e358-6b1b-d3db-555b40b7ebe5] Condition | onset 2000-05-04 | Prediabetes (finding) | clinical status active | SNOMED 714628002
[Condition/d4f2a6f8-e358-6b1b-4a76-ae3dfbf47144] Condition | onset 1986-11-06 | Body mass index 30+ - obesity (finding) | clinical status active | SNOMED 162864005
[Condition/d4f2a6f8-e358-6b1b-c732-3e05c6bfa924] Condition | onset 1982-10-28 | Only received primary school education (finding) | clinical status active | SNOMED 224295006
[MedicationRequest/d4f2a6f8-e358-6b1b-da40-22bfe510e33d] MedicationRequest | prescribed 2026-04-09 | Hydrochlorothiazide 25 MG Oral Tablet | status active | reason: Essential hypertension (disorder) | RxNorm 310798
[MedicationRequest/d4f2a6f8-e358-6b1b-b1c3-dd4b80a73ea4] MedicationRequest | prescribed 2026-04-09 | insulin isophane, human 70 UNT/ML / insulin, regular, human 30 UNT/ML Injectable Suspension [Humulin] | status active | reason: Prediabetes (finding) | RxNorm 106892
[MedicationRequest/d4f2a6f8-e358-6b1b-875e-3c108c25914e] MedicationRequest | prescribed 2026-04-09 | lisinopril 10 MG Oral Tablet | status active | reason: Essential hypertension (disorder) | RxNorm 314076
[MedicationRequest/d4f2a6f8-e358-6b1b-6913-a3ea2279b298] MedicationRequest | prescribed 2026-04-09 | amLODIPine 2.5 MG Oral Tablet | status active | reason: Essential hypertension (disorder) | RxNorm 308136
[MedicationRequest/d4f2a6f8-e358-6b1b-f33b-aeabe5d3ea2a] MedicationRequest | prescribed 2020-03-12 | Simvastatin 20 MG Oral Tablet | status active | RxNorm 312961
[MedicationRequest/d4f2a6f8-e358-6b1b-da7b-92b61020d936] MedicationRequest | prescribed 2020-03-12 | Nitroglycerin 0.4 MG/ACTUAT Mucosal Spray | status active | RxNorm 705129
[MedicationRequest/d4f2a6f8-e358-6b1b-c7c5-6dd35faf2d76] MedicationRequest | prescribed 2020-03-12 | 24 HR metoprolol succinate 100 MG Extended Release Oral Tablet | status active | RxNorm 866412
[MedicationRequest/d4f2a6f8-e358-6b1b-102e-595eecaa5a85] MedicationRequest | prescribed 2020-03-12 | Clopidogrel 75 MG Oral Tablet | status active | RxNorm 309362
[Encounter/d4f2a6f8-e358-6b1b-1745-afd1215948c6] Encounter | 2026-09-23 | Encounter for problem (procedure) | class AMB | reason: Chronic kidney disease stage 4 (disorder) | at TEWKSBURY HOSPITAL
[Encounter/d4f2a6f8-e358-6b1b-3133-f32329c08d3e] Encounter | 2026-09-20 | Encounter for problem (procedure) | class AMB | reason: Chronic kidney disease stage 4 (disorder) | at TEWKSBURY HOSPITAL
[Encounter/d4f2a6f8-e358-6b1b-0f9b-7fe2ad9bcba8] Encounter | 2026-09-20 | Encounter for problem (procedure) | class AMB | reason: Chronic kidney disease stage 4 (disorder) | at TEWKSBURY HOSPITAL
[Immunization/d4f2a6f8-e358-6b1b-d852-5d7c3a4a2175] Immunization | 2026-03-05 | Influenza, split virus, trivalent, PF | status completed | CVX 140
[MedicationRequest/d4f2a6f8-e358-6b1b-0d85-a40e01bf3261] MedicationRequest | prescribed 2020-05-28 | status completed
[MedicationRequest/d4f2a6f8-e358-6b1b-2bed-c64deadda479] MedicationRequest | prescribed 2020-05-28 | status completed
[MedicationRequest/d4f2a6f8-e358-6b1b-3758-30f5ce219846] MedicationRequest | prescribed 2020-05-28 | status completed
[MedicationRequest/d4f2a6f8-e358-6b1b-3f5e-7e6135d2c6f5] MedicationRequest | prescribed 2020-05-28 | status completed
[MedicationRequest/d4f2a6f8-e358-6b1b-51c2-18369a745aed] MedicationRequest | prescribed 2020-05-28 | status completed
[MedicationRequest/d4f2a6f8-e358-6b1b-66d4-84aa05c7a061] MedicationRequest | prescribed 2020-05-28 | status completed
[MedicationRequest/d4f2a6f8-e358-6b1b-8a18-260ddf353210] MedicationRequest | prescribed 2020-05-28 | status completed
[MedicationRequest/d4f2a6f8-e358-6b1b-b002-7ebb7e779147] MedicationRequest | prescribed 2020-05-28 | status completed
[MedicationRequest/d4f2a6f8-e358-6b1b-e554-c4539e720574] MedicationRequest | prescribed 2020-05-28 | status completed
[DocumentReference/9389ec5f-50b0-7626-f7a6-5efda445225b#1] Clinical note | 2016-02-11 | part 1 of 1 | 2016-02-11 # Chief Complaint - Thirst - Fatigue - Frequent Urination - Hunger # History of Present Illness Adolfo777 is a 51 year-old nonhispanic white male. Patient has a history of dental caries on smooth surface penetrating into pulp. # Social History Patient is married. Patient has never smoked. Patient identifies as heterosexual. Patient comes from a middle socioeconomic background. Patient did not finish high school. Patient currently has Aetna. # Allergies No Known Allergies. # Medications No Active Medications. # Assessment and Plan Patient is presenting with part-time employment (finding). ## Plan The patient was prescribed the following medications: - hydrochlorothiazide 25 mg oral tablet - lisinopril 10 mg oral tablet - amlodipine 2.5 mg oral tablet
```

</details>

label: s
note: All four cited 2020-03-12 MedicationRequests (simvastatin 20 MG, nitroglycerin 0.4 MG/ACTUAT spray, 24 HR metoprolol succinate 100 MG ER, clopidogrel 75 MG) are status active, and no other 2020-03-12 prescriptions appear in the record.

## 24. `prescribed-for-diabetes-mellitus-type-2:ef5e136c#0#1`

Question: Which medications have been prescribed for the patient's diabetes mellitus type 2?

Answer: The only medication with diabetes mellitus type 2 listed as its reason is insulin isophane, human 70 UNT/ML / insulin, regular, human 30 UNT/ML Injectable Suspension [Humulin], prescribed 2026-09-30 with status active. **Separately, tropicamide 5 mg/ml ophthalmic solution was prescribed at visits that included a diabetic retinal eye exam, most recently on 2022-12-10, but no reason is stated for it.**

Cards this sentence cites:

- `[DocumentReference/266eae94-47a1-e383-dbf6-ff8a9122547f#2]` Clinical note | 2022-12-10 | part 2 of 2 | # Medications lisinopril 10 mg oral tablet; tropicamide 5 mg/ml ophthalmic solution; hydrochlorothiazide 25 mg oral tablet; amoxicillin 250 mg oral capsule; acetaminophen 325 mg / oxycodone hydrochloride 5 mg oral tablet; 120 actuat fluticasone propionate 0.044 mg/actuat metered dose inhaler [flovent]; amlodipine 2.5 mg oral tablet; insulin isophane, human 70 unt/ml / insulin, regular, human 30 unt/ml injectable suspension [humulin]; albuterol 0.83 mg/ml inhalation solution; naproxen sodium 220 mg oral tablet # Assessment and Plan ## Plan The following procedures were conducted: - visual acuity testing (procedure) - intraocular pressure test (procedure) - ocular slit lamp examination (procedure) - indirect gonioscopy (procedure) - camera fundoscopy (procedure) - diabetic retinal eye exam (procedure) The patient was prescribed the following medications: - tropicamide 5 mg/ml ophthalmic solution
- `[DocumentReference/2267fd18-9da9-a4fa-aa4d-a95b255bf0fd#2]` Clinical note | 2021-12-15 | part 2 of 2 | # Medications lisinopril 10 mg oral tablet; tropicamide 5 mg/ml ophthalmic solution; hydrochlorothiazide 25 mg oral tablet; amoxicillin 250 mg oral capsule; acetaminophen 325 mg / oxycodone hydrochloride 5 mg oral tablet; 120 actuat fluticasone propionate 0.044 mg/actuat metered dose inhaler [flovent]; amlodipine 2.5 mg oral tablet; insulin isophane, human 70 unt/ml / insulin, regular, human 30 unt/ml injectable suspension [humulin]; albuterol 0.83 mg/ml inhalation solution; naproxen sodium 220 mg oral tablet # Assessment and Plan ## Plan The following procedures were conducted: - visual acuity testing (procedure) - intraocular pressure test (procedure) - ocular slit lamp examination (procedure) - indirect gonioscopy (procedure) - camera fundoscopy (procedure) - diabetic retinal eye exam (procedure) The patient was prescribed the following medications: - tropicamide 5 mg/ml ophthalmic solution
- `[DocumentReference/e66e01ce-8a8a-57d5-9bf6-52c4d40ac8d2#2]` Clinical note | 2021-01-19 | part 2 of 2 | # Medications lisinopril 10 mg oral tablet; tropicamide 5 mg/ml ophthalmic solution; hydrochlorothiazide 25 mg oral tablet; amoxicillin 250 mg oral capsule; acetaminophen 325 mg / oxycodone hydrochloride 5 mg oral tablet; 120 actuat fluticasone propionate 0.044 mg/actuat metered dose inhaler [flovent]; amlodipine 2.5 mg oral tablet; insulin isophane, human 70 unt/ml / insulin, regular, human 30 unt/ml injectable suspension [humulin]; albuterol 0.83 mg/ml inhalation solution; naproxen sodium 220 mg oral tablet # Assessment and Plan ## Plan The following procedures were conducted: - visual acuity testing (procedure) - intraocular pressure test (procedure) - ocular slit lamp examination (procedure) - indirect gonioscopy (procedure) - camera fundoscopy (procedure) - diabetic retinal eye exam (procedure) The patient was prescribed the following medications: - tropicamide 5 mg/ml ophthalmic solution

<details><summary>Everything the model saw (47 cards)</summary>

```text
[Condition/ef5e136c-ff1e-0695-1f8c-935a12106cac] Condition | onset 2026-09-30 | Medication review due (situation) | clinical status active | SNOMED 314529007
[Condition/ef5e136c-ff1e-0695-7e5d-470b95f60db2] Condition | onset 2026-09-23 | Social isolation (finding) | clinical status active | SNOMED 422650009
[Condition/ef5e136c-ff1e-0695-9d2d-c4be459bc9f4] Condition | onset 2026-09-09 | Unemployed (finding) | clinical status active | SNOMED 73438004
[Condition/ef5e136c-ff1e-0695-7b9c-f43e5ca3f6c6] Condition | onset 2026-08-12 | Stress (finding) | clinical status active | SNOMED 73595000
[Condition/ef5e136c-ff1e-0695-aa04-94486c99258f] Condition | onset 2025-08-27 | End-stage renal disease (disorder) | clinical status active | SNOMED 46177005
[Condition/ef5e136c-ff1e-0695-423f-ed71d76e81e3] Condition | onset 2025-03-30 | Awaiting transplantation of kidney (situation) | clinical status active | SNOMED 698306007
[Condition/ef5e136c-ff1e-0695-71df-3a96389b0a39] Condition | onset 2025-02-05 | Chronic kidney disease stage 4 (disorder) | clinical status active | SNOMED 431857002
[Condition/ef5e136c-ff1e-0695-5331-2d63eb213c34] Condition | onset 2024-05-15 | Proteinuria due to type 2 diabetes mellitus (disorder) | clinical status active | SNOMED 157141000119108
[Condition/ef5e136c-ff1e-0695-3834-fa6cb282a475] Condition | onset 2024-05-15 | Chronic kidney disease stage 3 (disorder) | clinical status active | SNOMED 433144002
[Condition/ef5e136c-ff1e-0695-68fe-9e2010333061] Condition | onset 2023-08-16 | Microalbuminuria due to type 2 diabetes mellitus (disorder) | clinical status active | SNOMED 90781000119102
[Condition/ef5e136c-ff1e-0695-65f5-8d04f278a661] Condition | onset 2023-08-16 | Chronic kidney disease stage 2 (disorder) | clinical status active | SNOMED 431856006
[Condition/ef5e136c-ff1e-0695-aac2-46a0ff462178] Condition | onset 2023-04-19 | Gingivitis (disorder) | clinical status active | SNOMED 66383009
[Condition/ef5e136c-ff1e-0695-fda2-40e12f6b17a7] Condition | onset 2017-11-15 | Chronic kidney disease stage 1 (disorder) | clinical status active | SNOMED 431855005
[Condition/ef5e136c-ff1e-0695-bf3f-30946ad3f8b4] Condition | onset 2017-11-15 | Disorder of kidney due to diabetes mellitus (disorder) | clinical status active | SNOMED 127013003
[Condition/ef5e136c-ff1e-0695-eac4-d545a0296998] Condition | onset 2011-07-27 | Essential hypertension (disorder) | clinical status active | SNOMED 59621000
[Condition/ef5e136c-ff1e-0695-b228-2f5ff5bb47cb] Condition | onset 2010-05-19 | Metabolic syndrome X (disorder) | clinical status active | SNOMED 237602007
[Condition/ef5e136c-ff1e-0695-af16-82f03f777ba8] Condition | onset 2010-05-19 | Hypertriglyceridemia (disorder) | clinical status active | SNOMED 302870006
[Condition/ef5e136c-ff1e-0695-5ca5-51bfdc51320e] Condition | onset 2010-05-12 | Diabetes mellitus type 2 (disorder) | clinical status active | SNOMED 44054006
[Condition/ef5e136c-ff1e-0695-f7ec-ceae0c2566bc] Condition | onset 2004-06-16 | Body mass index 30+ - obesity (finding) | clinical status active | SNOMED 162864005
[Condition/ef5e136c-ff1e-0695-c94a-5d81ddd88117] Condition | onset 1997-05-07 | Has a criminal record (finding) | clinical status active | SNOMED 266948004
[Condition/ef5e136c-ff1e-0695-6efc-9f7d5e6b04ef] Condition | onset 1993-09-01 | Anemia (disorder) | clinical status active | SNOMED 271737000
[Condition/ef5e136c-ff1e-0695-1f68-dac24351dbaa] Condition | onset 1993-04-14 | Prediabetes (finding) | clinical status active | SNOMED 714628002
[Condition/ef5e136c-ff1e-0695-2d8d-328849698529] Condition | onset 1993-01-22 | History of tubal ligation (situation) | clinical status active | SNOMED 267020005
[Condition/ef5e136c-ff1e-0695-0825-c31e8b252683] Condition | onset 1983-11-14 | Past pregnancy history of miscarriage (situation) | clinical status active | SNOMED 161744009
[Condition/ef5e136c-ff1e-0695-cb16-3a98eeb2de7a] Condition | onset 1976-01-07 | Received higher education (finding) | clinical status active | SNOMED 224299000
[Condition/ef5e136c-ff1e-0695-3278-6a86eaf1fb5d] Condition | onset 1975-06-27 | Chronic sinusitis (disorder) | clinical status active | SNOMED 40055000
[Condition/ef5e136c-ff1e-0695-337f-d12087c8dbb5] Condition | onset 1975-01-01 | Risk activity involvement (finding) | clinical status active | SNOMED 160968000
[MedicationRequest/ef5e136c-ff1e-0695-ffec-2ea7ac772a27] MedicationRequest | prescribed 2026-09-30 | Hydrochlorothiazide 25 MG Oral Tablet | status active | reason: Essential hypertension (disorder) | RxNorm 310798
[MedicationRequest/ef5e136c-ff1e-0695-b3ba-a1ec7bcfb9f4] MedicationRequest | prescribed 2026-09-30 | albuterol 0.83 MG/ML Inhalation Solution | status active | RxNorm 630208
[MedicationRequest/ef5e136c-ff1e-0695-901e-2e1f9afb0cca] MedicationRequest | prescribed 2026-09-30 | lisinopril 10 MG Oral Tablet | status active | reason: Essential hypertension (disorder) | RxNorm 314076
[MedicationRequest/ef5e136c-ff1e-0695-76a6-8eeb54f8a75e] MedicationRequest | prescribed 2026-09-30 | 120 ACTUAT fluticasone propionate 0.044 MG/ACTUAT Metered Dose Inhaler [Flovent] | status active | RxNorm 895996
[MedicationRequest/ef5e136c-ff1e-0695-6c6d-182c3b9c47c1] MedicationRequest | prescribed 2026-09-30 | amLODIPine 2.5 MG Oral Tablet | status active | reason: Essential hypertension (disorder) | RxNorm 308136
[MedicationRequest/ef5e136c-ff1e-0695-6804-cf31640a9491] MedicationRequest | prescribed 2026-09-30 | insulin isophane, human 70 UNT/ML / insulin, regular, human 30 UNT/ML Injectable Suspension [Humulin] | status active | reason: Diabetes mellitus type 2 (disorder) | RxNorm 106892
[Encounter/ef5e136c-ff1e-0695-08ba-2471a16a6570] Encounter | 2026-09-30 | Emergency room admission (procedure) | class EMER | at APPLE VALLEY CENTER
[Encounter/ef5e136c-ff1e-0695-aea4-11055569fd51] Encounter | 2026-09-23 | Urgent care clinic (environment) | class AMB | at URGENT HELP CHELMSFORD PC
[Encounter/ef5e136c-ff1e-0695-4a41-6fca58c80cb7] Encounter | 2026-09-16 | Urgent care clinic (environment) | class AMB | at URGENT HELP CHELMSFORD PC
[Immunization/ef5e136c-ff1e-0695-6beb-93901776b619] Immunization | 2026-05-13 | Influenza, split virus, trivalent, PF | status completed | CVX 140
[DocumentReference/e66e01ce-8a8a-57d5-9bf6-52c4d40ac8d2#2] Clinical note | 2021-01-19 | part 2 of 2 | # Medications lisinopril 10 mg oral tablet; tropicamide 5 mg/ml ophthalmic solution; hydrochlorothiazide 25 mg oral tablet; amoxicillin 250 mg oral capsule; acetaminophen 325 mg / oxycodone hydrochloride 5 mg oral tablet; 120 actuat fluticasone propionate 0.044 mg/actuat metered dose inhaler [flovent]; amlodipine 2.5 mg oral tablet; insulin isophane, human 70 unt/ml / insulin, regular, human 30 unt/ml injectable suspension [humulin]; albuterol 0.83 mg/ml inhalation solution; naproxen sodium 220 mg oral tablet # Assessment and Plan ## Plan The following procedures were conducted: - visual acuity testing (procedure) - intraocular pressure test (procedure) - ocular slit lamp examination (procedure) - indirect gonioscopy (procedure) - camera fundoscopy (procedure) - diabetic retinal eye exam (procedure) The patient was prescribed the following medications: - tropicamide 5 mg/ml ophthalmic solution
[DocumentReference/db48b326-95ec-6012-24c9-24234b74b109#2] Clinical note | 2020-01-25 | part 2 of 2 | # Medications lisinopril 10 mg oral tablet; tropicamide 5 mg/ml ophthalmic solution; hydrochlorothiazide 25 mg oral tablet; amoxicillin 250 mg oral capsule; acetaminophen 325 mg / oxycodone hydrochloride 5 mg oral tablet; 120 actuat fluticasone propionate 0.044 mg/actuat metered dose inhaler [flovent]; amlodipine 2.5 mg oral tablet; insulin isophane, human 70 unt/ml / insulin, regular, human 30 unt/ml injectable suspension [humulin]; albuterol 0.83 mg/ml inhalation solution; naproxen sodium 220 mg oral tablet # Assessment and Plan ## Plan The following procedures were conducted: - visual acuity testing (procedure) - intraocular pressure test (procedure) - ocular slit lamp examination (procedure) - indirect gonioscopy (procedure) - camera fundoscopy (procedure) - diabetic retinal eye exam (procedure) The patient was prescribed the following medications: - tropicamide 5 mg/ml ophthalmic solution
[Procedure/ef5e136c-ff1e-0695-f6b2-4d72c75dfa7f] Procedure | 2024-12-11 | Indirect gonioscopy (procedure) | status completed | reason: Diabetes mellitus type 2 (disorder) | SNOMED 389153003
[Procedure/ef5e136c-ff1e-0695-de5f-91cf8475a486] Procedure | 2023-12-05 | Indirect gonioscopy (procedure) | status completed | reason: Diabetes mellitus type 2 (disorder) | SNOMED 389153003
[Procedure/ef5e136c-ff1e-0695-00d9-98012c068d6a] Procedure | 2022-12-10 | Indirect gonioscopy (procedure) | status completed | reason: Diabetes mellitus type 2 (disorder) | SNOMED 389153003
[DocumentReference/2267fd18-9da9-a4fa-aa4d-a95b255bf0fd#2] Clinical note | 2021-12-15 | part 2 of 2 | # Medications lisinopril 10 mg oral tablet; tropicamide 5 mg/ml ophthalmic solution; hydrochlorothiazide 25 mg oral tablet; amoxicillin 250 mg oral capsule; acetaminophen 325 mg / oxycodone hydrochloride 5 mg oral tablet; 120 actuat fluticasone propionate 0.044 mg/actuat metered dose inhaler [flovent]; amlodipine 2.5 mg oral tablet; insulin isophane, human 70 unt/ml / insulin, regular, human 30 unt/ml injectable suspension [humulin]; albuterol 0.83 mg/ml inhalation solution; naproxen sodium 220 mg oral tablet # Assessment and Plan ## Plan The following procedures were conducted: - visual acuity testing (procedure) - intraocular pressure test (procedure) - ocular slit lamp examination (procedure) - indirect gonioscopy (procedure) - camera fundoscopy (procedure) - diabetic retinal eye exam (procedure) The patient was prescribed the following medications: - tropicamide 5 mg/ml ophthalmic solution
[DocumentReference/266eae94-47a1-e383-dbf6-ff8a9122547f#2] Clinical note | 2022-12-10 | part 2 of 2 | # Medications lisinopril 10 mg oral tablet; tropicamide 5 mg/ml ophthalmic solution; hydrochlorothiazide 25 mg oral tablet; amoxicillin 250 mg oral capsule; acetaminophen 325 mg / oxycodone hydrochloride 5 mg oral tablet; 120 actuat fluticasone propionate 0.044 mg/actuat metered dose inhaler [flovent]; amlodipine 2.5 mg oral tablet; insulin isophane, human 70 unt/ml / insulin, regular, human 30 unt/ml injectable suspension [humulin]; albuterol 0.83 mg/ml inhalation solution; naproxen sodium 220 mg oral tablet # Assessment and Plan ## Plan The following procedures were conducted: - visual acuity testing (procedure) - intraocular pressure test (procedure) - ocular slit lamp examination (procedure) - indirect gonioscopy (procedure) - camera fundoscopy (procedure) - diabetic retinal eye exam (procedure) The patient was prescribed the following medications: - tropicamide 5 mg/ml ophthalmic solution
[DocumentReference/f60e4bd7-409f-c1e9-7e5f-4220c110be9f#2] Clinical note | 2019-12-04 | part 2 of 3 | # Medications lisinopril 10 mg oral tablet; tropicamide 5 mg/ml ophthalmic solution; hydrochlorothiazide 25 mg oral tablet; amoxicillin 250 mg oral capsule; acetaminophen 325 mg / oxycodone hydrochloride 5 mg oral tablet; 120 actuat fluticasone propionate 0.044 mg/actuat metered dose inhaler [flovent]; amlodipine 2.5 mg oral tablet; insulin isophane, human 70 unt/ml / insulin, regular, human 30 unt/ml injectable suspension [humulin]; albuterol 0.83 mg/ml inhalation solution; naproxen sodium 220 mg oral tablet
[DocumentReference/26c615dc-db73-72f4-2a4d-fb891dfb2540#2] Clinical note | 2019-03-01 | part 2 of 2 | # Medications lisinopril 10 mg oral tablet; tropicamide 5 mg/ml ophthalmic solution; hydrochlorothiazide 25 mg oral tablet; 120 actuat fluticasone propionate 0.044 mg/actuat metered dose inhaler [flovent]; amlodipine 2.5 mg oral tablet; insulin isophane, human 70 unt/ml / insulin, regular, human 30 unt/ml injectable suspension [humulin]; albuterol 0.83 mg/ml inhalation solution # Assessment and Plan ## Plan The following procedures were conducted: - visual acuity testing (procedure) - intraocular pressure test (procedure) - ocular slit lamp examination (procedure) - indirect gonioscopy (procedure) - camera fundoscopy (procedure) - diabetic retinal eye exam (procedure) The patient was prescribed the following medications: - tropicamide 5 mg/ml ophthalmic solution
[DocumentReference/4d0d0889-f360-8c5c-b81d-aa7686616e55#2] Clinical note | 2016-10-19 | part 2 of 2 | # Assessment and Plan ## Plan The patient was prescribed the following medications: - hydrochlorothiazide 25 mg oral tablet - 120 actuat fluticasone propionate 0.044 mg/actuat metered dose inhaler [flovent] - lisinopril 10 mg oral tablet - amlodipine 2.5 mg oral tablet - albuterol 0.83 mg/ml inhalation solution
```

</details>

label: s
note: Cited notes list a diabetic retinal eye exam and tropicamide 5 mg/ml prescribed, with no reason given for the drug; the latest note showing tropicamide prescribed is 2022-12-10 (later 2023/2024 gonioscopy procedures do not mention tropicamide).

## 25. `active-problems:0eeb6aa3#0#2`

Question: What active diagnoses does the patient have?

Answer: Active diagnoses include primary fibromyalgia syndrome (onset 2026-07-29), metabolic syndrome X, hypertriglyceridemia, and hyperglycemia (all onset 2022-11-27). Also active are essential hypertension and diabetes mellitus type 2 (both onset 2021-11-21), osteoarthritis of knee (onset 2021-04-07), obesity with BMI 30+ (onset 2013-11-03), and prediabetes (onset 2008-01-13). **Other active findings include misuses drugs (onset 2025-12-14), victim of intimate partner abuse (onset 2021-11-21), history of tubal ligation, and risk activity involvement.**

Cards this sentence cites:

- `[Condition/0eeb6aa3-c249-0e46-44b4-3580330e81b7]` Condition | onset 2025-12-14 | Misuses drugs (finding) | clinical status active | SNOMED 361055000
- `[Condition/0eeb6aa3-c249-0e46-ce58-8dd4753fcdb4]` Condition | onset 2021-11-21 | Victim of intimate partner abuse (finding) | clinical status active | SNOMED 706893006
- `[Condition/0eeb6aa3-c249-0e46-7e82-50da4e26d936]` Condition | onset 2009-08-25 | History of tubal ligation (situation) | clinical status active | SNOMED 267020005
- `[Condition/0eeb6aa3-c249-0e46-7231-74f682325091]` Condition | onset 1988-12-04 | Risk activity involvement (finding) | clinical status active | SNOMED 160968000

<details><summary>Everything the model saw (36 cards)</summary>

```text
[Condition/0eeb6aa3-c249-0e46-6f19-eb10a1f328db] Condition | onset 2026-07-29 | Primary fibromyalgia syndrome (disorder) | clinical status active | SNOMED 95417003
[Condition/0eeb6aa3-c249-0e46-44b4-3580330e81b7] Condition | onset 2025-12-14 | Misuses drugs (finding) | clinical status active | SNOMED 361055000
[Condition/0eeb6aa3-c249-0e46-2c95-28a9408c6896] Condition | onset 2025-12-14 | Full-time employment (finding) | clinical status active | SNOMED 160903007
[Condition/0eeb6aa3-c249-0e46-b1be-047f25b1022e] Condition | onset 2022-11-27 | Metabolic syndrome X (disorder) | clinical status active | SNOMED 237602007
[Condition/0eeb6aa3-c249-0e46-6def-33ad344a7a9b] Condition | onset 2022-11-27 | Hypertriglyceridemia (disorder) | clinical status active | SNOMED 302870006
[Condition/0eeb6aa3-c249-0e46-06a5-9d3ec2ee65d0] Condition | onset 2022-11-27 | Hyperglycemia (disorder) | clinical status active | SNOMED 80394007
[Condition/0eeb6aa3-c249-0e46-d84e-f3245ad02f8e] Condition | onset 2021-11-21 | Essential hypertension (disorder) | clinical status active | SNOMED 59621000
[Condition/0eeb6aa3-c249-0e46-ce58-8dd4753fcdb4] Condition | onset 2021-11-21 | Victim of intimate partner abuse (finding) | clinical status active | SNOMED 706893006
[Condition/0eeb6aa3-c249-0e46-8d5d-18bd4ff7c429] Condition | onset 2021-11-21 | Diabetes mellitus type 2 (disorder) | clinical status active | SNOMED 44054006
[Condition/0eeb6aa3-c249-0e46-0e2a-b4435a3e06d7] Condition | onset 2021-04-07 | Osteoarthritis of knee (disorder) | clinical status active | SNOMED 239873007
[Condition/0eeb6aa3-c249-0e46-c1e0-a1835f8dfe99] Condition | onset 2013-11-03 | Body mass index 30+ - obesity (finding) | clinical status active | SNOMED 162864005
[Condition/0eeb6aa3-c249-0e46-7e82-50da4e26d936] Condition | onset 2009-08-25 | History of tubal ligation (situation) | clinical status active | SNOMED 267020005
[Condition/0eeb6aa3-c249-0e46-05b2-ee89706489e7] Condition | onset 2008-01-13 | Prediabetes (finding) | clinical status active | SNOMED 714628002
[Condition/0eeb6aa3-c249-0e46-1bf9-48c5ad5ed3c4] Condition | onset 1991-12-22 | Received higher education (finding) | clinical status active | SNOMED 224299000
[Condition/0eeb6aa3-c249-0e46-7231-74f682325091] Condition | onset 1988-12-04 | Risk activity involvement (finding) | clinical status active | SNOMED 160968000
[MedicationRequest/0eeb6aa3-c249-0e46-d035-2af008a23544] MedicationRequest | prescribed 2026-08-09 | amLODIPine 2.5 MG Oral Tablet | status active | reason: Essential hypertension (disorder) | RxNorm 308136
[MedicationRequest/0eeb6aa3-c249-0e46-9e8f-3bc3a049dcd6] MedicationRequest | prescribed 2026-08-09 | Hydrochlorothiazide 25 MG Oral Tablet | status active | reason: Essential hypertension (disorder) | RxNorm 310798
[MedicationRequest/0eeb6aa3-c249-0e46-9979-087d4ecb9395] MedicationRequest | prescribed 2026-08-09 | lisinopril 10 MG Oral Tablet | status active | reason: Essential hypertension (disorder) | RxNorm 314076
[MedicationRequest/0eeb6aa3-c249-0e46-8801-c4efefa8fdf6] MedicationRequest | prescribed 2026-08-09 | 24 HR Metformin hydrochloride 500 MG Extended Release Oral Tablet | status active | reason: Diabetes mellitus type 2 (disorder) | RxNorm 860975
[MedicationRequest/0eeb6aa3-c249-0e46-48fb-484102ab7f68] MedicationRequest | prescribed 2026-07-29 | Naproxen 500 MG Oral Tablet | status active | reason: Primary fibromyalgia syndrome (disorder) | RxNorm 198014
[MedicationRequest/0eeb6aa3-c249-0e46-7cb4-1e0c24948d9a] MedicationRequest | prescribed 2021-04-07 | Naproxen sodium 220 MG Oral Tablet | status active | reason: Osteoarthritis of knee (disorder) | RxNorm 849574
[MedicationRequest/0eeb6aa3-c249-0e46-6749-08c77e3ff56d] MedicationRequest | prescribed 1993-03-28 | ferrous sulfate 325 MG Oral Tablet | status active | RxNorm 310325
[Encounter/0eeb6aa3-c249-0e46-4c0e-5bc7f2736fbd] Encounter | 2026-08-09 | Urgent care clinic (environment) | class AMB | at URGENT HELP CHELMSFORD PC
[Encounter/0eeb6aa3-c249-0e46-43a1-ecea1c0a2a61] Encounter | 2026-07-29 | Encounter for problem (procedure) | class AMB | reason: Primary fibromyalgia syndrome (disorder) | at HOLY FAMILY HOSPITAL
[Encounter/0eeb6aa3-c249-0e46-d415-7e8395059f69] Encounter | 2026-01-04 | Encounter for check up (procedure) | class AMB | reason: Patient referral for dental care (procedure) | at HOLY FAMILY HOSPITAL
[Immunization/0eeb6aa3-c249-0e46-99a3-4dae451772fe] Immunization | 2026-08-09 | Influenza, split virus, trivalent, PF | status completed | CVX 140
[Condition/0eeb6aa3-c249-0e46-0893-f2e439b68154] Condition | onset 2019-11-17 | Full-time employment (finding) | clinical status resolved | resolved 2024-08-18 | SNOMED 160903007
[Condition/0eeb6aa3-c249-0e46-dbc8-2be40b51cb31] Condition | onset 2019-11-17 | Victim of intimate partner abuse (finding) | clinical status resolved | resolved 2021-11-21 | SNOMED 706893006
[DocumentReference/1fdd7223-94ae-8e9f-e6c5-3675ea1f857a#1] Clinical note | 2017-11-26 | part 1 of 1 | 2017-11-26 # Chief Complaint - Muscle Pain - Fatigue - Memory Loss - Stiffness - Decreased Communication - Decreased Visual Perception - Cognitive Difficulties # History of Present Illness Azucena377 Trina350 is a 44 year-old hispanic white female. Patient has a history of part-time employment (finding), medication review due (situation), dental caries on smooth surface penetrating into pulp, gingivitis (disorder), stress (finding). # Social History Patient is married. Patient has never smoked. Patient identifies as heterosexual. Patient comes from a middle socioeconomic background. Patient has completed some college courses. Patient currently has Medicaid. # Allergies No Known Allergies. # Medications No Active Medications. # Assessment and Plan ## Plan The following procedures were conducted: - periodic oral evaluation established patient - prophylaxis adult
[DocumentReference/075e821c-0beb-21ac-d6e7-26c6edd8d939#1] Clinical note | 2008-01-13 | part 1 of 1 | 2008-01-13 # Chief Complaint - Muscle Pain - Fatigue - Memory Loss - Stiffness - Decreased Communication - Decreased Visual Perception - Cognitive Difficulties # History of Present Illness Azucena377 Trina350 is a 34 year-old hispanic white female. Patient has a history of dental caries on smooth surface penetrating into pulp. # Social History Patient is married. Patient has never smoked. Patient identifies as heterosexual. Patient comes from a middle socioeconomic background. Patient has completed some college courses. Patient currently has Medicaid. # Allergies No Known Allergies. # Medications No Active Medications. # Assessment and Plan Patient is presenting with prediabetes (finding). ## Plan The patient was placed on a careplan: - diabetes self management plan (record artifact)
[DocumentReference/8ac58413-19f5-2021-b01c-9380d6639c66#1] Clinical note | 2020-08-30 | part 1 of 1 | 2020-08-30 # Chief Complaint - Muscle Pain - Fatigue - Memory Loss - Stiffness - Decreased Communication - Decreased Visual Perception - Cognitive Difficulties # History of Present Illness Azucena377 Trina350 is a 46 year-old hispanic white female. Patient has a history of part-time employment (finding), medication review due (situation), dental caries on smooth surface penetrating into pulp, full-time employment (finding), victim of intimate partner abuse (finding), gingivitis (disorder), stress (finding). # Social History Patient is married. Patient has never smoked. Patient identifies as heterosexual. Patient comes from a middle socioeconomic background. Patient has completed some college courses. Patient currently has Medicaid. # Allergies No Known Allergies. # Medications No Active Medications. # Assessment and Plan ## Plan The following procedures were conducted: - removal of subcutaneous contraceptive (procedure) - implantation of subcutaneous contraceptive (procedure)
[Procedure/0eeb6aa3-c249-0e46-cf7b-6369d6b532d1] Procedure | 2021-12-05 | periodic oral evaluation  established patient | status completed | http://www.ada.org/cdt D0120
[Procedure/0eeb6aa3-c249-0e46-944e-b28fcfb85439] Procedure | 2017-11-26 | periodic oral evaluation  established patient | status completed | http://www.ada.org/cdt D0120
[Condition/0eeb6aa3-c249-0e46-b1da-92adcad53df9] Condition | onset 2011-01-16 | Stress (finding) | clinical status resolved | resolved 2026-08-09 | SNOMED 73595000
[Device/0eeb6aa3-c249-0e46-7b11-493f6cf44aba] Device | Wheelchair accessory (physical object) | status active | manufactured 2021-03-17 | SNOMED 705417005
[Condition/0eeb6aa3-c249-0e46-12d1-e61940ee084a] Condition | onset 2025-07-06 | Unemployed (finding) | clinical status resolved | resolved 2025-12-14 | SNOMED 73438004
```

</details>

label: s
note: Cited Condition cards show misuses drugs (onset 2025-12-14), victim of intimate partner abuse (onset 2021-11-21), history of tubal ligation and risk activity involvement, all clinical status active; 'include' makes no completeness claim.

## 26. `latest-lab-2085-9:8d945e28#0#0`

Question: What was the patient's most recent HDL cholesterol result, and when was it measured?

Answer: **The most recent HDL cholesterol result was 52.86 mg/dL, measured on 2025-10-20.** Earlier HDL values were 54.33 mg/dL on 2022-09-12 and 59.23 mg/dL on 2019-08-26.

Cards this sentence cites:

- `[Observation/8d945e28-1d8a-bd72-e167-028828939847]` Observation (laboratory) | 2025-10-20 | Cholesterol in HDL [Mass/volume] in Serum or Plasma = 52.86 mg/dL | status final | LOINC 2085-9
- `[DiagnosticReport/8d945e28-1d8a-bd72-dbf0-308e6fd426b0]` DiagnosticReport | 2025-10-20 | Lipid panel with direct LDL - Serum or Plasma | results: Cholesterol [Mass/volume] in Serum or Plasma 201.61 mg/dL; Triglyceride [Mass/volume] in Serum or Plasma 122.44 mg/dL; Cholesterol in LDL [Mass/volume] in Serum or Plasma by Direct assay 124.27 mg/dL; Cholesterol in HDL [Mass/volume] in Serum or Plasma 52.86 mg/dL | LOINC 57698-3

<details><summary>Everything the model saw (39 cards)</summary>

```text
[Condition/8d945e28-1d8a-bd72-9d6c-259e17157c55] Condition | onset 2026-09-07 | Full-time employment (finding) | clinical status active | SNOMED 160903007
[Condition/8d945e28-1d8a-bd72-3102-64b703ba601c] Condition | onset 2026-07-13 | Medication review due (situation) | clinical status active | SNOMED 314529007
[Condition/8d945e28-1d8a-bd72-6b51-0718e8cd7a5e] Condition | onset 2021-01-01 | Awaiting transplantation of kidney (situation) | clinical status active | SNOMED 698306007
[Condition/8d945e28-1d8a-bd72-db4c-2552d073039a] Condition | onset 2020-11-09 | Chronic kidney disease stage 4 (disorder) | clinical status active | SNOMED 431857002
[Condition/8d945e28-1d8a-bd72-ed26-25aa62be033c] Condition | onset 2020-08-18 | Dependent drug abuse (disorder) | clinical status active | SNOMED 6525002
[Condition/8d945e28-1d8a-bd72-05bf-4b4b02b03fe9] Condition | onset 2018-01-22 | Has a criminal record (finding) | clinical status active | SNOMED 266948004
[Condition/8d945e28-1d8a-bd72-38fb-c4bf927332c6] Condition | onset 2013-09-16 | Proteinuria due to type 2 diabetes mellitus (disorder) | clinical status active | SNOMED 157141000119108
[Condition/8d945e28-1d8a-bd72-1379-82140e2d1648] Condition | onset 2013-09-16 | Chronic kidney disease stage 3 (disorder) | clinical status active | SNOMED 433144002
[Condition/8d945e28-1d8a-bd72-cd47-b95fb1e4464b] Condition | onset 2009-07-06 | Microalbuminuria due to type 2 diabetes mellitus (disorder) | clinical status active | SNOMED 90781000119102
[Condition/8d945e28-1d8a-bd72-be1a-fb710d842e34] Condition | onset 2009-07-06 | Chronic kidney disease stage 2 (disorder) | clinical status active | SNOMED 431856006
[Condition/8d945e28-1d8a-bd72-2a55-0f3c986db8dd] Condition | onset 2009-07-06 | Gingivitis (disorder) | clinical status active | SNOMED 66383009
[Condition/8d945e28-1d8a-bd72-4277-241d976b7354] Condition | onset 2007-06-25 | Metabolic syndrome X (disorder) | clinical status active | SNOMED 237602007
[Condition/8d945e28-1d8a-bd72-e0ac-a99a0168ad8a] Condition | onset 2004-06-07 | Disorder of kidney due to diabetes mellitus (disorder) | clinical status active | SNOMED 127013003
[Condition/8d945e28-1d8a-bd72-a508-e7d1553f7f62] Condition | onset 2004-06-07 | Chronic kidney disease stage 1 (disorder) | clinical status active | SNOMED 431855005
[Condition/8d945e28-1d8a-bd72-2622-8fe0a1a30909] Condition | onset 2003-06-02 | Essential hypertension (disorder) | clinical status active | SNOMED 59621000
[Condition/8d945e28-1d8a-bd72-12e3-17db162c8f0b] Condition | onset 2001-06-04 | Obstructive sleep apnea syndrome (disorder) | clinical status active | SNOMED 78275009
[Condition/8d945e28-1d8a-bd72-d01e-086bb9d1d22f] Condition | onset 2001-05-07 | Sleep disorder (disorder) | clinical status active | SNOMED 39898005
[Condition/8d945e28-1d8a-bd72-f5fa-42692b5be159] Condition | onset 1996-08-05 | Body mass index 30+ - obesity (finding) | clinical status active | SNOMED 162864005
[Condition/8d945e28-1d8a-bd72-e601-8e5493910aec] Condition | onset 1981-07-20 | Prediabetes (finding) | clinical status active | SNOMED 714628002
[Condition/8d945e28-1d8a-bd72-52ca-256d6584412c] Condition | onset 1981-07-20 | Anemia (disorder) | clinical status active | SNOMED 271737000
[Condition/8d945e28-1d8a-bd72-d644-66738e889d91] Condition | onset 1977-07-11 | Received higher education (finding) | clinical status active | SNOMED 224299000
[Condition/8d945e28-1d8a-bd72-fbf9-3e6f6bd97f57] Condition | onset 1977-03-07 | Risk activity involvement (finding) | clinical status active | SNOMED 160968000
[MedicationRequest/8d945e28-1d8a-bd72-ff5c-41daf21d65a9] MedicationRequest | prescribed 2026-09-07 | insulin isophane, human 70 UNT/ML / insulin, regular, human 30 UNT/ML Injectable Suspension [Humulin] | status active | reason: Prediabetes (finding) | RxNorm 106892
[MedicationRequest/8d945e28-1d8a-bd72-d409-38c0124f2c47] MedicationRequest | prescribed 2026-09-07 | Hydrochlorothiazide 25 MG Oral Tablet | status active | reason: Essential hypertension (disorder) | RxNorm 310798
[MedicationRequest/8d945e28-1d8a-bd72-bcd6-3304c42dca58] MedicationRequest | prescribed 1981-07-27 | Vitamin B12 5 MG/ML Injectable Solution | status active | RxNorm 2001499
[Encounter/8d945e28-1d8a-bd72-016c-9af67d7199fd] Encounter | 2026-09-27 | Encounter for problem (procedure) | class AMB | reason: Chronic kidney disease stage 4 (disorder) | at NEW ENGLAND REHABILITATION SERVICES OF CENTRAL MASSACHUSETTS INC
[Encounter/8d945e28-1d8a-bd72-3f01-7946bd8f2be1] Encounter | 2026-09-26 | Encounter for problem (procedure) | class AMB | reason: Chronic kidney disease stage 4 (disorder) | at NEW ENGLAND REHABILITATION SERVICES OF CENTRAL MASSACHUSETTS INC
[Encounter/8d945e28-1d8a-bd72-9dbd-785d1f0e4915] Encounter | 2026-09-23 | Encounter for problem (procedure) | class AMB | reason: Chronic kidney disease stage 4 (disorder) | at NEW ENGLAND REHABILITATION SERVICES OF CENTRAL MASSACHUSETTS INC
[Immunization/8d945e28-1d8a-bd72-6a94-32775be2d4e6] Immunization | 2026-01-12 | Influenza, split virus, trivalent, PF | status completed | CVX 140
[Observation/8d945e28-1d8a-bd72-e167-028828939847] Observation (laboratory) | 2025-10-20 | Cholesterol in HDL [Mass/volume] in Serum or Plasma = 52.86 mg/dL | status final | LOINC 2085-9
[Observation/8d945e28-1d8a-bd72-8170-de0dd31b67c6] Observation (laboratory) | 2022-09-12 | Cholesterol in HDL [Mass/volume] in Serum or Plasma = 54.33 mg/dL | status final | LOINC 2085-9
[Observation/8d945e28-1d8a-bd72-9493-f703b3ba8ff3] Observation (laboratory) | 2019-08-26 | Cholesterol in HDL [Mass/volume] in Serum or Plasma = 59.23 mg/dL | status final | LOINC 2085-9
[Observation/8d945e28-1d8a-bd72-d6e5-3ebe5fed8f1a] Observation (laboratory) | 2022-09-12 | Cholesterol [Mass/volume] in Serum or Plasma = 148.65 mg/dL | status final | LOINC 2093-3
[Observation/8d945e28-1d8a-bd72-64a2-d704939e5569] Observation (laboratory) | 2025-10-20 | Cholesterol [Mass/volume] in Serum or Plasma = 201.61 mg/dL | status final | LOINC 2093-3
[Observation/8d945e28-1d8a-bd72-8b12-08eb743b5705] Observation (laboratory) | 2019-08-26 | Cholesterol [Mass/volume] in Serum or Plasma = 142.1 mg/dL | status final | LOINC 2093-3
[Observation/8d945e28-1d8a-bd72-961c-17441972e819] Observation (laboratory) | 2022-09-12 | Cholesterol in LDL [Mass/volume] in Serum or Plasma by Direct assay = 68.79 mg/dL | status final | LOINC 18262-6
[Observation/8d945e28-1d8a-bd72-bb0b-ad8a47cf0e8b] Observation (laboratory) | 2025-10-20 | Cholesterol in LDL [Mass/volume] in Serum or Plasma by Direct assay = 124.27 mg/dL | status final | LOINC 18262-6
[Observation/8d945e28-1d8a-bd72-e3ba-330aae54bfd7] Observation (laboratory) | 2019-08-26 | Cholesterol in LDL [Mass/volume] in Serum or Plasma by Direct assay = 59.46 mg/dL | status final | LOINC 18262-6
[DiagnosticReport/8d945e28-1d8a-bd72-dbf0-308e6fd426b0] DiagnosticReport | 2025-10-20 | Lipid panel with direct LDL - Serum or Plasma | results: Cholesterol [Mass/volume] in Serum or Plasma 201.61 mg/dL; Triglyceride [Mass/volume] in Serum or Plasma 122.44 mg/dL; Cholesterol in LDL [Mass/volume] in Serum or Plasma by Direct assay 124.27 mg/dL; Cholesterol in HDL [Mass/volume] in Serum or Plasma 52.86 mg/dL | LOINC 57698-3
```

</details>

label: s
note: Cited HDL observation and lipid panel show 52.86 mg/dL on 2025-10-20; the only other HDL results (2022-09-12, 2019-08-26) are earlier.

## 27. `latest-lab-2339-0:e56a8cde#0#0`

Question: What was the patient's most recent blood glucose result, and when was it measured?

Answer: **The most recent blood glucose result was 68.84 mg/dL, measured on 2026-01-01 as part of a comprehensive metabolic panel.** Prior values were 69.59 mg/dL on 2024-12-20 and 72.42 mg/dL on 2023-12-21.

Cards this sentence cites:

- `[Observation/e56a8cde-8395-a37d-1b9c-9f8ffab8b485]` Observation (laboratory) | 2026-01-01 | Glucose [Mass/volume] in Blood = 68.84 mg/dL | status final | LOINC 2339-0
- `[DiagnosticReport/e56a8cde-8395-a37d-be96-8a833439e988]` DiagnosticReport | 2026-01-01 | Comprehensive metabolic 2000 panel - Serum or Plasma | results: Glucose [Mass/volume] in Blood 68.84 mg/dL; Urea nitrogen [Mass/volume] in Blood 9.95 mg/dL; Creatinine [Mass/volume] in Blood 2.5647 mg/dL; Calcium [Mass/volume] in Blood 8.64 mg/dL; Sodium [Moles/volume] in Blood 140.96 mmol/L; Potassium [Moles/volume] in Blood 3.79 mmol/L; Chloride [Moles/volume] in Blood 101.2 mmol/L; Carbon dioxide, total [Moles/volume] in Blood 26.33 mmol/L; Glomerular filtration rate [Volume Rate/Area] in Serum or Plasma by Creatinine-based formula (MDRD)/1.73 sq M 82.374 mL/min; Protein [Mass/volume] in Serum or Plasma 7.3929 g/dL; Albumin [Mass/volume] in Serum or Plasma 4.5646 g/dL; Globulin [Mass/volume] in Serum by calculation 2.9995 g/L; Bilirubin.total [Mass/volume] in Serum or Plasma 0.15192 mg/dL; Alkaline phosphatase [Enzymatic activity/volume] in Serum or Plasma 25.802 U/L; Alanine aminotransferase [Enzymatic activity/volume] in Serum or Plasma 29.499 U/L; Aspartate aminotransferase [Enzymatic activity/volume] in Serum or Plasma 6.8194 U/L | LOINC 24323-8

<details><summary>Everything the model saw (56 cards)</summary>

```text
[Condition/e56a8cde-8395-a37d-f7ae-15d35f13e9f0] Condition | onset 2025-12-25 | Victim of intimate partner abuse (finding) | clinical status active | SNOMED 706893006
[Condition/e56a8cde-8395-a37d-80d3-3984f14d8bb3] Condition | onset 2025-12-25 | Stress (finding) | clinical status active | SNOMED 73595000
[Condition/e56a8cde-8395-a37d-5c7c-75429c6f1e56] Condition | onset 2025-12-25 | Medication review due (situation) | clinical status active | SNOMED 314529007
[Condition/e56a8cde-8395-a37d-354e-df92238c35a7] Condition | onset 2025-12-25 | Unemployed (finding) | clinical status active | SNOMED 73438004
[Condition/e56a8cde-8395-a37d-6690-7ef5746552bd] Condition | onset 2017-11-09 | Hyperlipidemia (disorder) | clinical status active | SNOMED 55822004
[Condition/e56a8cde-8395-a37d-922a-d32061194c0b] Condition | onset 2016-11-03 | Gingivitis (disorder) | clinical status active | SNOMED 66383009
[Condition/e56a8cde-8395-a37d-e775-23849ffbe97b] Condition | onset 2014-02-01 | Chronic low back pain (finding) | clinical status active | SNOMED 278860009
[Condition/e56a8cde-8395-a37d-a82c-6129bc784139] Condition | onset 2014-02-01 | Chronic pain (finding) | clinical status active | SNOMED 82423001
[Condition/e56a8cde-8395-a37d-64b8-86023f198a46] Condition | onset 2014-02-01 | Chronic neck pain (finding) | clinical status active | SNOMED 1121000119107
[Condition/e56a8cde-8395-a37d-e547-8e085bacfa8e] Condition | onset 2007-09-13 | Has a criminal record (finding) | clinical status active | SNOMED 266948004
[Condition/e56a8cde-8395-a37d-37b4-500cf9e797e9] Condition | onset 2005-09-01 | Osteoporosis (disorder) | clinical status active | SNOMED 64859006
[Condition/e56a8cde-8395-a37d-d5cb-6239a28a0055] Condition | onset 2003-12-16 | History of myocardial infarction (situation) | clinical status active | SNOMED 399211009
[Condition/e56a8cde-8395-a37d-4d5f-670d3e1632bc] Condition | onset 2003-12-16 | Acute non-ST segment elevation myocardial infarction (disorder) | clinical status active | SNOMED 401314000
[Condition/e56a8cde-8395-a37d-1853-568436ee1ea2] Condition | onset 2001-08-20 | History of coronary artery bypass grafting (situation) | clinical status active | SNOMED 399261000
[Condition/e56a8cde-8395-a37d-810b-643d651149ba] Condition | onset 2001-08-18 | Abnormal findings diagnostic imaging heart+coronary circulat (finding) | clinical status active | SNOMED 274531002
[Condition/e56a8cde-8395-a37d-2761-7d0bfc799087] Condition | onset 2001-08-09 | Ischemic heart disease (disorder) | clinical status active | SNOMED 414545008
[Condition/e56a8cde-8395-a37d-ed31-c4144dbefb9e] Condition | onset 1996-05-17 | Osteoarthritis of knee (disorder) | clinical status active | SNOMED 239873007
[Condition/e56a8cde-8395-a37d-333f-0835bee4de98] Condition | onset 1991-06-13 | Essential hypertension (disorder) | clinical status active | SNOMED 59621000
[Condition/e56a8cde-8395-a37d-30cd-5f4f9de67da3] Condition | onset 1967-07-27 | Lack of access to transportation (finding) | clinical status active | SNOMED 713458007
[Condition/e56a8cde-8395-a37d-ac70-0b466edf16a1] Condition | onset 1963-07-18 | Transport problem (finding) | clinical status active | SNOMED 266934004
[Condition/e56a8cde-8395-a37d-99e6-93fe1e3f6036] Condition | onset 1963-07-18 | Only received primary school education (finding) | clinical status active | SNOMED 224295006
[MedicationRequest/e56a8cde-8395-a37d-0c1b-7da0b396a0c4] MedicationRequest | prescribed 2026-01-01 | Simvastatin 10 MG Oral Tablet | status active | reason: Hyperlipidemia (disorder) | RxNorm 314231
[MedicationRequest/e56a8cde-8395-a37d-f153-06ed5ef5b40a] MedicationRequest | prescribed 2025-12-25 | Alendronic acid 10 MG Oral Tablet | status active | reason: Osteoporosis (disorder) | RxNorm 904419
[MedicationRequest/e56a8cde-8395-a37d-b70b-d6ff9e66fb91] MedicationRequest | prescribed 2025-12-25 | Acetaminophen 325 MG Oral Tablet [Tylenol] | status active | RxNorm 209387
[MedicationRequest/e56a8cde-8395-a37d-1cff-386c29158923] MedicationRequest | prescribed 2025-12-25 | lisinopril 10 MG Oral Tablet | status active | reason: Essential hypertension (disorder) | RxNorm 314076
[MedicationRequest/e56a8cde-8395-a37d-f778-f1044e9a8316] MedicationRequest | prescribed 2003-12-16 | atorvastatin 10 MG Oral Tablet | status active | RxNorm 617312
[MedicationRequest/e56a8cde-8395-a37d-e36e-ab680e0ad841] MedicationRequest | prescribed 2003-12-16 | hydrochlorothiazide 25 MG / lisinopril 20 MG Oral Tablet | status active | RxNorm 197887
[MedicationRequest/e56a8cde-8395-a37d-d237-6e376bbcb9a6] MedicationRequest | prescribed 2003-12-16 | metoprolol tartrate 25 MG Oral Tablet | status active | RxNorm 866924
[MedicationRequest/e56a8cde-8395-a37d-2fb4-edeac8b69b00] MedicationRequest | prescribed 2003-12-16 | prasugrel 10 MG Oral Tablet | status active | RxNorm 855812
[MedicationRequest/e56a8cde-8395-a37d-228f-f6135c165caa] MedicationRequest | prescribed 2003-12-16 | aspirin 81 MG Oral Tablet | status active | RxNorm 243670
[MedicationRequest/e56a8cde-8395-a37d-eee1-8d05287f0e29] MedicationRequest | prescribed 2001-08-16 | Nitroglycerin 0.4 MG/ACTUAT Mucosal Spray | status active | RxNorm 705129
[MedicationRequest/e56a8cde-8395-a37d-d36b-2e3fc9df975e] MedicationRequest | prescribed 2001-08-16 | 24 HR metoprolol succinate 100 MG Extended Release Oral Tablet | status active | RxNorm 866412
[MedicationRequest/e56a8cde-8395-a37d-a8c0-f9ed9ed3ea83] MedicationRequest | prescribed 2001-08-16 | Clopidogrel 75 MG Oral Tablet | status active | RxNorm 309362
[MedicationRequest/e56a8cde-8395-a37d-321f-ecd1d25263ad] MedicationRequest | prescribed 2001-08-16 | Simvastatin 20 MG Oral Tablet | status active | RxNorm 312961
[MedicationRequest/e56a8cde-8395-a37d-9456-c58ec0c7de32] MedicationRequest | prescribed 1949-01-17 | diphenhydrAMINE Hydrochloride 25 MG Oral Tablet | status active | RxNorm 1049630
[AllergyIntolerance/e56a8cde-8395-a37d-b318-8f34a7d6b5f7] AllergyIntolerance | recorded 1946-06-09 | Animal dander (substance) | allergy, category environment, criticality low | clinical status active | reactions: Eruption of skin (disorder); Rhinoconjunctivitis (disorder) | SNOMED 264287008
[AllergyIntolerance/e56a8cde-8395-a37d-a098-9831a40ac85b] AllergyIntolerance | recorded 1946-06-09 | Mold (organism) | allergy, category environment, criticality low | clinical status active | SNOMED 84489001
[AllergyIntolerance/e56a8cde-8395-a37d-85d4-fe7519012219] AllergyIntolerance | recorded 1946-06-09 | House dust mite (organism) | allergy, category environment, criticality low | clinical status active | SNOMED 260147004
[AllergyIntolerance/e56a8cde-8395-a37d-60c2-b75e4a4d4513] AllergyIntolerance | recorded 1946-06-09 | Tree pollen (substance) | allergy, category environment, criticality low | clinical status active | SNOMED 782576004
[AllergyIntolerance/e56a8cde-8395-a37d-5834-224d1127b6f9] AllergyIntolerance | recorded 1946-06-09 | Grass pollen (substance) | allergy, category environment, criticality low | clinical status active | SNOMED 256277009
[AllergyIntolerance/e56a8cde-8395-a37d-2daa-dbe0dbcf6ecf] AllergyIntolerance | recorded 1946-06-09 | Shellfish (substance) | allergy, category food, criticality low | clinical status active | reactions: Dyspnea (finding); Allergic angioedema (disorder); Itching (finding); Cough (finding); Diarrhea (finding) | SNOMED 735029006
[AllergyIntolerance/e56a8cde-8395-a37d-1508-bdb84bdc4c5d] AllergyIntolerance | recorded 1946-06-09 | Allergic disposition (finding) | allergy, category environment, criticality low | clinical status active | SNOMED 609328004
[Encounter/e56a8cde-8395-a37d-9f47-5b69723a8690] Encounter | 2026-01-01 | Follow-up encounter (procedure) | class AMB | reason: Hyperlipidemia (disorder) | at DANA FARBER CANCER INSTITUTE
[Encounter/e56a8cde-8395-a37d-2450-250d53d64dc7] Encounter | 2025-12-25 | General examination of patient (procedure) | class AMB | at SOUTH SHORE PRIMARY CARE PC
[Encounter/e56a8cde-8395-a37d-20eb-f707e34a4164] Encounter | 2024-12-20 | Follow-up encounter (procedure) | class AMB | reason: Hyperlipidemia (disorder) | at DANA FARBER CANCER INSTITUTE
[Immunization/e56a8cde-8395-a37d-7cd1-bb3bac5572f3] Immunization | 2025-12-25 | Influenza, split virus, trivalent, PF | status completed | CVX 140
[Observation/e56a8cde-8395-a37d-1b9c-9f8ffab8b485] Observation (laboratory) | 2026-01-01 | Glucose [Mass/volume] in Blood = 68.84 mg/dL | status final | LOINC 2339-0
[Observation/e56a8cde-8395-a37d-86a6-60c7b0e163a5] Observation (laboratory) | 2024-12-20 | Glucose [Mass/volume] in Blood = 69.59 mg/dL | status final | LOINC 2339-0
[Observation/e56a8cde-8395-a37d-5037-60397fbc6883] Observation (laboratory) | 2023-12-21 | Glucose [Mass/volume] in Blood = 72.42 mg/dL | status final | LOINC 2339-0
[Observation/e56a8cde-8395-a37d-42e2-f0bd81342de7] Observation (laboratory) | 2021-11-03 | Glucose [Mass/volume] in Urine by Test strip = 13.324 mg/dL | status final | LOINC 5792-7
[DiagnosticReport/e56a8cde-8395-a37d-be96-8a833439e988] DiagnosticReport | 2026-01-01 | Comprehensive metabolic 2000 panel - Serum or Plasma | results: Glucose [Mass/volume] in Blood 68.84 mg/dL; Urea nitrogen [Mass/volume] in Blood 9.95 mg/dL; Creatinine [Mass/volume] in Blood 2.5647 mg/dL; Calcium [Mass/volume] in Blood 8.64 mg/dL; Sodium [Moles/volume] in Blood 140.96 mmol/L; Potassium [Moles/volume] in Blood 3.79 mmol/L; Chloride [Moles/volume] in Blood 101.2 mmol/L; Carbon dioxide, total [Moles/volume] in Blood 26.33 mmol/L; Glomerular filtration rate [Volume Rate/Area] in Serum or Plasma by Creatinine-based formula (MDRD)/1.73 sq M 82.374 mL/min; Protein [Mass/volume] in Serum or Plasma 7.3929 g/dL; Albumin [Mass/volume] in Serum or Plasma 4.5646 g/dL; Globulin [Mass/volume] in Serum by calculation 2.9995 g/L; Bilirubin.total [Mass/volume] in Serum or Plasma 0.15192 mg/dL; Alkaline phosphatase [Enzymatic activity/volume] in Serum or Plasma 25.802 U/L; Alanine aminotransferase [Enzymatic activity/volume] in Serum or Plasma 29.499 U/L; Aspartate aminotransferase [Enzymatic activity/volume] in Serum or Plasma 6.8194 U/L | LOINC 24323-8
[DiagnosticReport/e56a8cde-8395-a37d-8651-b20d134f2385] DiagnosticReport | 2024-12-20 | Comprehensive metabolic 2000 panel - Serum or Plasma | results: Glucose [Mass/volume] in Blood 69.59 mg/dL; Urea nitrogen [Mass/volume] in Blood 17.74 mg/dL; Creatinine [Mass/volume] in Blood 2.8562 mg/dL; Calcium [Mass/volume] in Blood 8.95 mg/dL; Sodium [Moles/volume] in Blood 137.69 mmol/L; Potassium [Moles/volume] in Blood 4.92 mmol/L; Chloride [Moles/volume] in Blood 101.27 mmol/L; Carbon dioxide, total [Moles/volume] in Blood 27 mmol/L; Glomerular filtration rate [Volume Rate/Area] in Serum or Plasma by Creatinine-based formula (MDRD)/1.73 sq M 69.58 mL/min; Protein [Mass/volume] in Serum or Plasma 7.544 g/dL; Albumin [Mass/volume] in Serum or Plasma 3.8181 g/dL; Globulin [Mass/volume] in Serum by calculation 3.0019 g/L; Bilirubin.total [Mass/volume] in Serum or Plasma 1.0233 mg/dL; Alkaline phosphatase [Enzymatic activity/volume] in Serum or Plasma 85.047 U/L; Alanine aminotransferase [Enzymatic activity/volume] in Serum or Plasma 36.367 U/L; Aspartate aminotransferase [Enzymatic activity/volume] in Serum or Plasma 24.965 U/L | LOINC 24323-8
[DiagnosticReport/e56a8cde-8395-a37d-303f-5c4d644ca8a5] DiagnosticReport | 2023-12-21 | Comprehensive metabolic 2000 panel - Serum or Plasma | results: Glucose [Mass/volume] in Blood 72.42 mg/dL; Urea nitrogen [Mass/volume] in Blood 15.43 mg/dL; Creatinine [Mass/volume] in Blood 2.9389 mg/dL; Calcium [Mass/volume] in Blood 9.76 mg/dL; Sodium [Moles/volume] in Blood 141.67 mmol/L; Potassium [Moles/volume] in Blood 4.2 mmol/L; Chloride [Moles/volume] in Blood 105.23 mmol/L; Carbon dioxide, total [Moles/volume] in Blood 22.8 mmol/L; Glomerular filtration rate [Volume Rate/Area] in Serum or Plasma by Creatinine-based formula (MDRD)/1.73 sq M 69.886 mL/min; Protein [Mass/volume] in Serum or Plasma 6.4274 g/dL; Albumin [Mass/volume] in Serum or Plasma 4.507 g/dL; Globulin [Mass/volume] in Serum by calculation 2.3948 g/L; Bilirubin.total [Mass/volume] in Serum or Plasma 0.94419 mg/dL; Alkaline phosphatase [Enzymatic activity/volume] in Serum or Plasma 57.249 U/L; Alanine aminotransferase [Enzymatic activity/volume] in Serum or Plasma 21.891 U/L; Aspartate aminotransferase [Enzymatic activity/volume] in Serum or Plasma 34.828 U/L | LOINC 24323-8
[Immunization/e56a8cde-8395-a37d-ded2-6b37ccc4ca99] Immunization | 2021-02-18 | COVID-19, mRNA, LNP-S, PF, 100 mcg/0.5mL dose or 50 mcg/0.25mL dose | status completed | CVX 207
[Immunization/e56a8cde-8395-a37d-7678-458aa2ed7c54] Immunization | 2021-01-21 | COVID-19, mRNA, LNP-S, PF, 100 mcg/0.5mL dose or 50 mcg/0.25mL dose | status completed | CVX 207
[Observation/e56a8cde-8395-a37d-bba5-0f6b9130005e] Observation (laboratory) | 2020-11-29 | Triglyceride [Mass/volume] in Serum or Plasma = 131.12 mg/dL | status final | LOINC 2571-8
```

</details>

label: s
note: Cited blood glucose 68.84 mg/dL on 2026-01-01 appears in the Comprehensive metabolic 2000 panel report; other blood glucose results (2024-12-20, 2023-12-21) are earlier.

## 28. `current-meds:d4f2a6f8#0#0`

Question: What medications is the patient currently prescribed?

Answer: **The patient's active prescriptions for essential hypertension are hydrochlorothiazide 25 MG oral tablet, lisinopril 10 MG oral tablet, and amLODIPine 2.5 MG oral tablet, all prescribed 2026-04-09.** Also active is Humulin (insulin isophane, human 70 UNT/ML / insulin, regular, human 30 UNT/ML injectable suspension), prescribed 2026-04-09 with prediabetes listed as the reason. Additional active prescriptions from 2020-03-12 are simvastatin 20 MG oral tablet, nitroglycerin 0.4 MG/ACTUAT mucosal spray, 24 HR metoprolol succinate 100 MG extended release oral tablet, and clopidogrel 75 MG oral tablet.

Cards this sentence cites:

- `[MedicationRequest/d4f2a6f8-e358-6b1b-da40-22bfe510e33d]` MedicationRequest | prescribed 2026-04-09 | Hydrochlorothiazide 25 MG Oral Tablet | status active | reason: Essential hypertension (disorder) | RxNorm 310798
- `[MedicationRequest/d4f2a6f8-e358-6b1b-875e-3c108c25914e]` MedicationRequest | prescribed 2026-04-09 | lisinopril 10 MG Oral Tablet | status active | reason: Essential hypertension (disorder) | RxNorm 314076
- `[MedicationRequest/d4f2a6f8-e358-6b1b-6913-a3ea2279b298]` MedicationRequest | prescribed 2026-04-09 | amLODIPine 2.5 MG Oral Tablet | status active | reason: Essential hypertension (disorder) | RxNorm 308136

<details><summary>Everything the model saw (42 cards)</summary>

```text
[Condition/d4f2a6f8-e358-6b1b-a870-7578fc115ba3] Condition | onset 2026-04-02 | Stress (finding) | clinical status active | SNOMED 73595000
[Condition/d4f2a6f8-e358-6b1b-37cc-cacad982df8c] Condition | onset 2026-04-02 | Reports of violence in the environment (finding) | clinical status active | SNOMED 424393004
[Condition/d4f2a6f8-e358-6b1b-c78d-1b6bc447e34a] Condition | onset 2025-12-04 | Full-time employment (finding) | clinical status active | SNOMED 160903007
[Condition/d4f2a6f8-e358-6b1b-29d8-fc1e6a15e60d] Condition | onset 2025-12-04 | Medication review due (situation) | clinical status active | SNOMED 314529007
[Condition/d4f2a6f8-e358-6b1b-f1ac-92593f6454e7] Condition | onset 2025-03-20 | Chronic kidney disease stage 4 (disorder) | clinical status active | SNOMED 431857002
[Condition/d4f2a6f8-e358-6b1b-4959-9b97d2d3536d] Condition | onset 2025-02-03 | Awaiting transplantation of kidney (situation) | clinical status active | SNOMED 698306007
[Condition/d4f2a6f8-e358-6b1b-76dc-8902de051de4] Condition | onset 2022-10-20 | Microalbuminuria due to type 2 diabetes mellitus (disorder) | clinical status active | SNOMED 90781000119102
[Condition/d4f2a6f8-e358-6b1b-1e8b-4beeba77ed82] Condition | onset 2022-10-20 | Proteinuria due to type 2 diabetes mellitus (disorder) | clinical status active | SNOMED 157141000119108
[Condition/d4f2a6f8-e358-6b1b-042a-23b17f3aef58] Condition | onset 2022-10-20 | Chronic kidney disease stage 3 (disorder) | clinical status active | SNOMED 433144002
[Condition/d4f2a6f8-e358-6b1b-7e47-2334f6b84c0f] Condition | onset 2020-05-28 | History of coronary artery bypass grafting (situation) | clinical status active | SNOMED 399261000
[Condition/d4f2a6f8-e358-6b1b-ebe7-54c5d38117fc] Condition | onset 2020-03-19 | Abnormal findings diagnostic imaging heart+coronary circulat (finding) | clinical status active | SNOMED 274531002
[Condition/d4f2a6f8-e358-6b1b-e1e3-648cc0a38c11] Condition | onset 2020-03-05 | Chronic kidney disease stage 1 (disorder) | clinical status active | SNOMED 431855005
[Condition/d4f2a6f8-e358-6b1b-7f62-e48c3798c8b1] Condition | onset 2020-03-05 | Disorder of kidney due to diabetes mellitus (disorder) | clinical status active | SNOMED 127013003
[Condition/d4f2a6f8-e358-6b1b-6866-45937dfd6387] Condition | onset 2020-03-05 | Ischemic heart disease (disorder) | clinical status active | SNOMED 414545008
[Condition/d4f2a6f8-e358-6b1b-9d41-102804feed92] Condition | onset 2004-12-09 | Metabolic syndrome X (disorder) | clinical status active | SNOMED 237602007
[Condition/d4f2a6f8-e358-6b1b-4dab-6274d2854b00] Condition | onset 2002-11-28 | Anemia (disorder) | clinical status active | SNOMED 271737000
[Condition/d4f2a6f8-e358-6b1b-c5c9-83d1526dc404] Condition | onset 2001-11-22 | Essential hypertension (disorder) | clinical status active | SNOMED 59621000
[Condition/d4f2a6f8-e358-6b1b-d3db-555b40b7ebe5] Condition | onset 2000-05-04 | Prediabetes (finding) | clinical status active | SNOMED 714628002
[Condition/d4f2a6f8-e358-6b1b-4a76-ae3dfbf47144] Condition | onset 1986-11-06 | Body mass index 30+ - obesity (finding) | clinical status active | SNOMED 162864005
[Condition/d4f2a6f8-e358-6b1b-c732-3e05c6bfa924] Condition | onset 1982-10-28 | Only received primary school education (finding) | clinical status active | SNOMED 224295006
[MedicationRequest/d4f2a6f8-e358-6b1b-da40-22bfe510e33d] MedicationRequest | prescribed 2026-04-09 | Hydrochlorothiazide 25 MG Oral Tablet | status active | reason: Essential hypertension (disorder) | RxNorm 310798
[MedicationRequest/d4f2a6f8-e358-6b1b-b1c3-dd4b80a73ea4] MedicationRequest | prescribed 2026-04-09 | insulin isophane, human 70 UNT/ML / insulin, regular, human 30 UNT/ML Injectable Suspension [Humulin] | status active | reason: Prediabetes (finding) | RxNorm 106892
[MedicationRequest/d4f2a6f8-e358-6b1b-875e-3c108c25914e] MedicationRequest | prescribed 2026-04-09 | lisinopril 10 MG Oral Tablet | status active | reason: Essential hypertension (disorder) | RxNorm 314076
[MedicationRequest/d4f2a6f8-e358-6b1b-6913-a3ea2279b298] MedicationRequest | prescribed 2026-04-09 | amLODIPine 2.5 MG Oral Tablet | status active | reason: Essential hypertension (disorder) | RxNorm 308136
[MedicationRequest/d4f2a6f8-e358-6b1b-f33b-aeabe5d3ea2a] MedicationRequest | prescribed 2020-03-12 | Simvastatin 20 MG Oral Tablet | status active | RxNorm 312961
[MedicationRequest/d4f2a6f8-e358-6b1b-da7b-92b61020d936] MedicationRequest | prescribed 2020-03-12 | Nitroglycerin 0.4 MG/ACTUAT Mucosal Spray | status active | RxNorm 705129
[MedicationRequest/d4f2a6f8-e358-6b1b-c7c5-6dd35faf2d76] MedicationRequest | prescribed 2020-03-12 | 24 HR metoprolol succinate 100 MG Extended Release Oral Tablet | status active | RxNorm 866412
[MedicationRequest/d4f2a6f8-e358-6b1b-102e-595eecaa5a85] MedicationRequest | prescribed 2020-03-12 | Clopidogrel 75 MG Oral Tablet | status active | RxNorm 309362
[Encounter/d4f2a6f8-e358-6b1b-1745-afd1215948c6] Encounter | 2026-09-23 | Encounter for problem (procedure) | class AMB | reason: Chronic kidney disease stage 4 (disorder) | at TEWKSBURY HOSPITAL
[Encounter/d4f2a6f8-e358-6b1b-3133-f32329c08d3e] Encounter | 2026-09-20 | Encounter for problem (procedure) | class AMB | reason: Chronic kidney disease stage 4 (disorder) | at TEWKSBURY HOSPITAL
[Encounter/d4f2a6f8-e358-6b1b-0f9b-7fe2ad9bcba8] Encounter | 2026-09-20 | Encounter for problem (procedure) | class AMB | reason: Chronic kidney disease stage 4 (disorder) | at TEWKSBURY HOSPITAL
[Immunization/d4f2a6f8-e358-6b1b-d852-5d7c3a4a2175] Immunization | 2026-03-05 | Influenza, split virus, trivalent, PF | status completed | CVX 140
[MedicationRequest/d4f2a6f8-e358-6b1b-0d85-a40e01bf3261] MedicationRequest | prescribed 2020-05-28 | status completed
[MedicationRequest/d4f2a6f8-e358-6b1b-2bed-c64deadda479] MedicationRequest | prescribed 2020-05-28 | status completed
[MedicationRequest/d4f2a6f8-e358-6b1b-3758-30f5ce219846] MedicationRequest | prescribed 2020-05-28 | status completed
[MedicationRequest/d4f2a6f8-e358-6b1b-3f5e-7e6135d2c6f5] MedicationRequest | prescribed 2020-05-28 | status completed
[MedicationRequest/d4f2a6f8-e358-6b1b-51c2-18369a745aed] MedicationRequest | prescribed 2020-05-28 | status completed
[MedicationRequest/d4f2a6f8-e358-6b1b-66d4-84aa05c7a061] MedicationRequest | prescribed 2020-05-28 | status completed
[MedicationRequest/d4f2a6f8-e358-6b1b-8a18-260ddf353210] MedicationRequest | prescribed 2020-05-28 | status completed
[MedicationRequest/d4f2a6f8-e358-6b1b-b002-7ebb7e779147] MedicationRequest | prescribed 2020-05-28 | status completed
[MedicationRequest/d4f2a6f8-e358-6b1b-e554-c4539e720574] MedicationRequest | prescribed 2020-05-28 | status completed
[DocumentReference/9389ec5f-50b0-7626-f7a6-5efda445225b#1] Clinical note | 2016-02-11 | part 1 of 1 | 2016-02-11 # Chief Complaint - Thirst - Fatigue - Frequent Urination - Hunger # History of Present Illness Adolfo777 is a 51 year-old nonhispanic white male. Patient has a history of dental caries on smooth surface penetrating into pulp. # Social History Patient is married. Patient has never smoked. Patient identifies as heterosexual. Patient comes from a middle socioeconomic background. Patient did not finish high school. Patient currently has Aetna. # Allergies No Known Allergies. # Medications No Active Medications. # Assessment and Plan Patient is presenting with part-time employment (finding). ## Plan The patient was prescribed the following medications: - hydrochlorothiazide 25 mg oral tablet - lisinopril 10 mg oral tablet - amlodipine 2.5 mg oral tablet
```

</details>

label: s
note: The three cited MedicationRequests (hydrochlorothiazide 25 MG, lisinopril 10 MG, amLODIPine 2.5 MG) are active, dated 2026-04-09, reason Essential hypertension; no other prescription in the record lists that reason.

## 29. `prescribed-for-hyperlipidemia:7280f7f8#0#0`

Question: Which medications have been prescribed for the patient's hyperlipidemia?

Answer: **Simvastatin 10 MG Oral Tablet is the medication prescribed for hyperlipidemia, with an active prescription dated 2026-04-13.** Earlier Simvastatin 10 MG prescriptions for hyperlipidemia, now completed, were dated 2021-03-21, 2024-04-01 and 2025-04-13. Clinical notes show simvastatin 10 mg first prescribed on 2010-01-31 alongside a hyperlipidemia clinical management plan, and prescribed again in later notes through 2026-04-13. Simvastatin 20 MG Oral Tablet, prescribed 2018-11-11, is also active, but the record does not list a reason for it.

Cards this sentence cites:

- `[MedicationRequest/7280f7f8-315d-7c6a-d103-5f5cf25ace53]` MedicationRequest | prescribed 2026-04-13 | Simvastatin 10 MG Oral Tablet | status active | reason: Hyperlipidemia (disorder) | RxNorm 314231

<details><summary>Everything the model saw (43 cards)</summary>

```text
[Condition/7280f7f8-315d-7c6a-5183-1fc53612d856] Condition | onset 2026-04-12 | Alzheimer's disease (disorder) | clinical status active | SNOMED 26929004
[Condition/7280f7f8-315d-7c6a-069f-25fdb34e3e53] Condition | onset 2025-04-06 | Stress (finding) | clinical status active | SNOMED 73595000
[Condition/7280f7f8-315d-7c6a-06ae-a26712c6cfb7] Condition | onset 2024-03-31 | Full-time employment (finding) | clinical status active | SNOMED 160903007
[Condition/7280f7f8-315d-7c6a-84b2-d6045a9b8deb] Condition | onset 2018-11-12 | Abnormal findings diagnostic imaging heart+coronary circulat (finding) | clinical status active | SNOMED 274531002
[Condition/7280f7f8-315d-7c6a-60b8-1b2b3b190d66] Condition | onset 2018-11-04 | Ischemic heart disease (disorder) | clinical status active | SNOMED 414545008
[Condition/7280f7f8-315d-7c6a-eee1-33d3eda16b26] Condition | onset 2014-02-16 | Chronic low back pain (finding) | clinical status active | SNOMED 278860009
[Condition/7280f7f8-315d-7c6a-23b9-2a24d0c43093] Condition | onset 2014-02-16 | Chronic neck pain (finding) | clinical status active | SNOMED 1121000119107
[Condition/7280f7f8-315d-7c6a-f371-666500850eb4] Condition | onset 2014-02-02 | Gingivitis (disorder) | clinical status active | SNOMED 66383009
[Condition/7280f7f8-315d-7c6a-b5ea-aa0955ebc2c7] Condition | onset 2010-01-10 | Hyperlipidemia (disorder) | clinical status active | SNOMED 55822004
[Condition/7280f7f8-315d-7c6a-929f-e845c91bba18] Condition | onset 1993-02-06 | Dependent drug abuse (disorder) | clinical status active | SNOMED 6525002
[Condition/7280f7f8-315d-7c6a-6159-244929402415] Condition | onset 1991-07-09 | Chronic pain (finding) | clinical status active | SNOMED 82423001
[Condition/7280f7f8-315d-7c6a-7561-551dd4fb980c] Condition | onset 1990-11-11 | Has a criminal record (finding) | clinical status active | SNOMED 266948004
[Condition/7280f7f8-315d-7c6a-69cb-9f6bde195716] Condition | onset 1990-10-25 | Impacted molars (disorder) | clinical status active | SNOMED 196416002
[Condition/7280f7f8-315d-7c6a-e183-7fc41f06abde] Condition | onset 1990-02-06 | Chronic intractable migraine without aura (disorder) | clinical status active | SNOMED 124171000119105
[Condition/7280f7f8-315d-7c6a-57cd-16215a141add] Condition | onset 1988-11-06 | Body mass index 30+ - obesity (finding) | clinical status active | SNOMED 162864005
[Condition/7280f7f8-315d-7c6a-7c25-7a247f43e721] Condition | onset 1981-01-18 | Anemia (disorder) | clinical status active | SNOMED 271737000
[Condition/7280f7f8-315d-7c6a-50ac-70390520f5d8] Condition | onset 1981-01-18 | Prediabetes (finding) | clinical status active | SNOMED 714628002
[Condition/7280f7f8-315d-7c6a-a35c-5f2c4404e1cd] Condition | onset 1971-02-18 | Chronic sinusitis (disorder) | clinical status active | SNOMED 40055000
[Condition/7280f7f8-315d-7c6a-cf3c-1559c1e270a8] Condition | onset 1964-12-20 | Housing unsatisfactory (finding) | clinical status active | SNOMED 105531004
[Condition/7280f7f8-315d-7c6a-3735-89103641aea2] Condition | onset 1964-12-20 | Only received primary school education (finding) | clinical status active | SNOMED 224295006
[MedicationRequest/7280f7f8-315d-7c6a-d103-5f5cf25ace53] MedicationRequest | prescribed 2026-04-13 | Simvastatin 10 MG Oral Tablet | status active | reason: Hyperlipidemia (disorder) | RxNorm 314231
[MedicationRequest/7280f7f8-315d-7c6a-dd3c-435b565b36d4] MedicationRequest | prescribed 2026-04-12 | Ibuprofen 400 MG Oral Tablet [Ibu] | status active | RxNorm 206905
[MedicationRequest/7280f7f8-315d-7c6a-698d-8c3f4a330263] MedicationRequest | prescribed 2026-04-12 | Acetaminophen 325 MG / Oxycodone Hydrochloride 10 MG Oral Tablet [Percocet] | status active | RxNorm 1049625
[MedicationRequest/7280f7f8-315d-7c6a-53dc-677516ba315e] MedicationRequest | prescribed 2026-04-12 | Galantamine 4 MG Oral Tablet | status active | reason: Alzheimer's disease (disorder) | RxNorm 310436
[MedicationRequest/7280f7f8-315d-7c6a-21fd-127361ce4eae] MedicationRequest | prescribed 2026-04-12 | Acetaminophen 325 MG Oral Tablet [Tylenol] | status active | RxNorm 209387
[MedicationRequest/7280f7f8-315d-7c6a-e1ca-6672a64e96d6] MedicationRequest | prescribed 2018-11-11 | Simvastatin 20 MG Oral Tablet | status active | RxNorm 312961
[MedicationRequest/7280f7f8-315d-7c6a-d3dc-bf227b26b9de] MedicationRequest | prescribed 2018-11-11 | Nitroglycerin 0.4 MG/ACTUAT Mucosal Spray | status active | RxNorm 705129
[MedicationRequest/7280f7f8-315d-7c6a-40f0-094ac0d35606] MedicationRequest | prescribed 2018-11-11 | Clopidogrel 75 MG Oral Tablet | status active | RxNorm 309362
[MedicationRequest/7280f7f8-315d-7c6a-344e-7b21fe48818f] MedicationRequest | prescribed 2018-11-11 | 24 HR metoprolol succinate 100 MG Extended Release Oral Tablet | status active | RxNorm 866412
[Encounter/7280f7f8-315d-7c6a-ddbc-56619e72a429] Encounter | 2026-04-26 | Encounter for check up (procedure) | class AMB | at LAWRENCE GENERAL HOSPITAL
[Encounter/7280f7f8-315d-7c6a-e49f-7858d34e1916] Encounter | 2026-04-13 | Follow-up encounter (procedure) | class AMB | reason: Hyperlipidemia (disorder) | at LAWRENCE GENERAL HOSPITAL
[Encounter/7280f7f8-315d-7c6a-79c7-b2135168eae6] Encounter | 2026-04-12 | General examination of patient (procedure) | class AMB | at HOLY FAMILY MEDICAL SPECIALTY PRACTICE PLLC
[Immunization/7280f7f8-315d-7c6a-89f5-f28321d6dbe8] Immunization | 2026-04-12 | Influenza, split virus, trivalent, PF | status completed | CVX 140
[MedicationRequest/7280f7f8-315d-7c6a-bb38-7fe5589f6bd1] MedicationRequest | prescribed 2021-03-21 | Simvastatin 10 MG Oral Tablet | status completed | reason: Hyperlipidemia (disorder) | RxNorm 314231
[MedicationRequest/7280f7f8-315d-7c6a-1229-8b8ac61b850c] MedicationRequest | prescribed 2025-04-13 | Simvastatin 10 MG Oral Tablet | status completed | reason: Hyperlipidemia (disorder) | RxNorm 314231
[MedicationRequest/7280f7f8-315d-7c6a-f259-2997c9221f42] MedicationRequest | prescribed 2024-04-01 | Simvastatin 10 MG Oral Tablet | status completed | reason: Hyperlipidemia (disorder) | RxNorm 314231
[DocumentReference/e6e9fc8c-b7e9-b73c-6766-e6b4f1428f2d#2] Clinical note | 2021-03-21 | part 2 of 2 | # Assessment and Plan ## Plan The following lab reports were completed: - comprehensive metabolic 2000 panel - serum or plasma - lipid panel with direct ldl - serum or plasma The patient was prescribed the following medications: - simvastatin 10 mg oral tablet
[DocumentReference/1bc417bc-1504-ce97-8e95-c79d15fea2e7#2] Clinical note | 2023-04-02 | part 2 of 2 | # Assessment and Plan ## Plan The following lab reports were completed: - comprehensive metabolic 2000 panel - serum or plasma - lipid panel with direct ldl - serum or plasma The patient was prescribed the following medications: - simvastatin 10 mg oral tablet
[DocumentReference/623620ec-1d91-d30a-5e56-4026a7a02940#2] Clinical note | 2024-04-01 | part 2 of 2 | # Assessment and Plan ## Plan The following lab reports were completed: - comprehensive metabolic 2000 panel - serum or plasma - lipid panel with direct ldl - serum or plasma The patient was prescribed the following medications: - simvastatin 10 mg oral tablet
[DocumentReference/6b0d0857-4700-f6ee-c3e4-f8d7c3eb1f27#2] Clinical note | 2026-04-13 | part 2 of 2 | # Assessment and Plan ## Plan The following lab reports were completed: - comprehensive metabolic 2000 panel - serum or plasma - lipid panel with direct ldl - serum or plasma The patient was prescribed the following medications: - simvastatin 10 mg oral tablet
[DocumentReference/e7f7d6a9-6472-c4c5-cd5b-366b66666d66#2] Clinical note | 2025-04-13 | part 2 of 2 | # Assessment and Plan ## Plan The following lab reports were completed: - comprehensive metabolic 2000 panel - serum or plasma - lipid panel with direct ldl - serum or plasma The patient was prescribed the following medications: - simvastatin 10 mg oral tablet
[DocumentReference/750cb41b-d9ad-3c1d-b6d7-fadb5db1236e#1] Clinical note | 2010-01-31 | part 1 of 1 | 2010-01-31 # Chief Complaint - Memory Loss - Decreased in Judgement # History of Present Illness Neil122 is a 63 year-old nonhispanic white male. Patient has a history of victim of intimate partner abuse (finding). # Social History Patient is married. Patient has a documented history of opioid addiction. Patient has never smoked. Patient identifies as heterosexual. Patient comes from a low socioeconomic background. Patient did not finish high school. Patient currently has Cigna Health. # Allergies No Known Allergies. # Medications No Active Medications. # Assessment and Plan ## Plan The patient was prescribed the following medications: - simvastatin 10 mg oral tablet The patient was placed on a careplan: - hyperlipidemia clinical management plan (record artifact)
[DocumentReference/53e3dee9-e8d4-88fd-c6b5-8ecae9ce5d4d#2] Clinical note | 2022-03-21 | part 2 of 2 | # Assessment and Plan ## Plan The following lab reports were completed: - comprehensive metabolic 2000 panel - serum or plasma - lipid panel with direct ldl - serum or plasma The patient was prescribed the following medications: - simvastatin 10 mg oral tablet
```

</details>

label: s
note: Cited MedicationRequest is Simvastatin 10 MG, active, 2026-04-13, reason Hyperlipidemia; every hyperlipidemia-linked prescription seen is Simvastatin 10 MG (simvastatin 20 MG has no reason, as the answer notes).

## 30. `last-flu-shot:0eeb6aa3#0#0`

Question: When did the patient last get a flu shot?

Answer: **The patient's most recent flu shot was on 2026-08-09 (Influenza, split virus, trivalent, PF; status completed).** Earlier influenza vaccinations were recorded on 2025-07-06, 2024-08-18, and 2023-12-03.

Cards this sentence cites:

- `[Immunization/0eeb6aa3-c249-0e46-99a3-4dae451772fe]` Immunization | 2026-08-09 | Influenza, split virus, trivalent, PF | status completed | CVX 140

<details><summary>Everything the model saw (36 cards)</summary>

```text
[Condition/0eeb6aa3-c249-0e46-6f19-eb10a1f328db] Condition | onset 2026-07-29 | Primary fibromyalgia syndrome (disorder) | clinical status active | SNOMED 95417003
[Condition/0eeb6aa3-c249-0e46-44b4-3580330e81b7] Condition | onset 2025-12-14 | Misuses drugs (finding) | clinical status active | SNOMED 361055000
[Condition/0eeb6aa3-c249-0e46-2c95-28a9408c6896] Condition | onset 2025-12-14 | Full-time employment (finding) | clinical status active | SNOMED 160903007
[Condition/0eeb6aa3-c249-0e46-b1be-047f25b1022e] Condition | onset 2022-11-27 | Metabolic syndrome X (disorder) | clinical status active | SNOMED 237602007
[Condition/0eeb6aa3-c249-0e46-6def-33ad344a7a9b] Condition | onset 2022-11-27 | Hypertriglyceridemia (disorder) | clinical status active | SNOMED 302870006
[Condition/0eeb6aa3-c249-0e46-06a5-9d3ec2ee65d0] Condition | onset 2022-11-27 | Hyperglycemia (disorder) | clinical status active | SNOMED 80394007
[Condition/0eeb6aa3-c249-0e46-d84e-f3245ad02f8e] Condition | onset 2021-11-21 | Essential hypertension (disorder) | clinical status active | SNOMED 59621000
[Condition/0eeb6aa3-c249-0e46-ce58-8dd4753fcdb4] Condition | onset 2021-11-21 | Victim of intimate partner abuse (finding) | clinical status active | SNOMED 706893006
[Condition/0eeb6aa3-c249-0e46-8d5d-18bd4ff7c429] Condition | onset 2021-11-21 | Diabetes mellitus type 2 (disorder) | clinical status active | SNOMED 44054006
[Condition/0eeb6aa3-c249-0e46-0e2a-b4435a3e06d7] Condition | onset 2021-04-07 | Osteoarthritis of knee (disorder) | clinical status active | SNOMED 239873007
[Condition/0eeb6aa3-c249-0e46-c1e0-a1835f8dfe99] Condition | onset 2013-11-03 | Body mass index 30+ - obesity (finding) | clinical status active | SNOMED 162864005
[Condition/0eeb6aa3-c249-0e46-7e82-50da4e26d936] Condition | onset 2009-08-25 | History of tubal ligation (situation) | clinical status active | SNOMED 267020005
[Condition/0eeb6aa3-c249-0e46-05b2-ee89706489e7] Condition | onset 2008-01-13 | Prediabetes (finding) | clinical status active | SNOMED 714628002
[Condition/0eeb6aa3-c249-0e46-1bf9-48c5ad5ed3c4] Condition | onset 1991-12-22 | Received higher education (finding) | clinical status active | SNOMED 224299000
[Condition/0eeb6aa3-c249-0e46-7231-74f682325091] Condition | onset 1988-12-04 | Risk activity involvement (finding) | clinical status active | SNOMED 160968000
[MedicationRequest/0eeb6aa3-c249-0e46-d035-2af008a23544] MedicationRequest | prescribed 2026-08-09 | amLODIPine 2.5 MG Oral Tablet | status active | reason: Essential hypertension (disorder) | RxNorm 308136
[MedicationRequest/0eeb6aa3-c249-0e46-9e8f-3bc3a049dcd6] MedicationRequest | prescribed 2026-08-09 | Hydrochlorothiazide 25 MG Oral Tablet | status active | reason: Essential hypertension (disorder) | RxNorm 310798
[MedicationRequest/0eeb6aa3-c249-0e46-9979-087d4ecb9395] MedicationRequest | prescribed 2026-08-09 | lisinopril 10 MG Oral Tablet | status active | reason: Essential hypertension (disorder) | RxNorm 314076
[MedicationRequest/0eeb6aa3-c249-0e46-8801-c4efefa8fdf6] MedicationRequest | prescribed 2026-08-09 | 24 HR Metformin hydrochloride 500 MG Extended Release Oral Tablet | status active | reason: Diabetes mellitus type 2 (disorder) | RxNorm 860975
[MedicationRequest/0eeb6aa3-c249-0e46-48fb-484102ab7f68] MedicationRequest | prescribed 2026-07-29 | Naproxen 500 MG Oral Tablet | status active | reason: Primary fibromyalgia syndrome (disorder) | RxNorm 198014
[MedicationRequest/0eeb6aa3-c249-0e46-7cb4-1e0c24948d9a] MedicationRequest | prescribed 2021-04-07 | Naproxen sodium 220 MG Oral Tablet | status active | reason: Osteoarthritis of knee (disorder) | RxNorm 849574
[MedicationRequest/0eeb6aa3-c249-0e46-6749-08c77e3ff56d] MedicationRequest | prescribed 1993-03-28 | ferrous sulfate 325 MG Oral Tablet | status active | RxNorm 310325
[Encounter/0eeb6aa3-c249-0e46-4c0e-5bc7f2736fbd] Encounter | 2026-08-09 | Urgent care clinic (environment) | class AMB | at URGENT HELP CHELMSFORD PC
[Encounter/0eeb6aa3-c249-0e46-43a1-ecea1c0a2a61] Encounter | 2026-07-29 | Encounter for problem (procedure) | class AMB | reason: Primary fibromyalgia syndrome (disorder) | at HOLY FAMILY HOSPITAL
[Encounter/0eeb6aa3-c249-0e46-d415-7e8395059f69] Encounter | 2026-01-04 | Encounter for check up (procedure) | class AMB | reason: Patient referral for dental care (procedure) | at HOLY FAMILY HOSPITAL
[Immunization/0eeb6aa3-c249-0e46-99a3-4dae451772fe] Immunization | 2026-08-09 | Influenza, split virus, trivalent, PF | status completed | CVX 140
[Immunization/0eeb6aa3-c249-0e46-0f8a-c753ad5d69d4] Immunization | 2023-12-03 | Influenza, split virus, trivalent, PF | status completed | CVX 140
[Immunization/0eeb6aa3-c249-0e46-1aef-3abca12a4341] Immunization | 2025-07-06 | Influenza, split virus, trivalent, PF | status completed | CVX 140
[Immunization/0eeb6aa3-c249-0e46-c2dc-a350191a6400] Immunization | 2024-08-18 | Influenza, split virus, trivalent, PF | status completed | CVX 140
[Observation/0eeb6aa3-c249-0e46-e893-745f1abe8454] Observation (survey) | 2025-07-06 | Protocol for Responding to and Assessing Patients' Assets, Risks, and Experiences [PRAPARE] = Within the last year, have you been afraid of your partner or ex-partner No; Do you feel physically and emotionally safe where you currently live [PRAPARE] Yes; Are you a refugee No; Have you spent more than 2 nights in a row in a jail, prison, detention center, or juvenile correctional facility in past 1 year [PRAPARE] No; Stress level Quite a bit; How often do you see or talk to people that you care about and feel close to [PRAPARE] 5 or more times a week; Has lack of transportation kept you from medical appointments, meetings, work, or from getting things needed for daily living No; Have you or any family members you live with been unable to get any of the following when it was really needed in past 1 year [PRAPARE] Food; What was your best estimate of the total income of all family members from all sources, before taxes, in last year [PhenX] 18408 /a; Primary insurance Medicaid; Employment status - current Unemployed; Highest level of education More than high school; Address 1026 Shanahan Street Unit 90; Are you worried about losing your housing [PRAPARE] No; Housing status I have housing; How many people are living or staying at this address [#] 7 {#}; Preferred language English; Discharged from the U.S. Armed Forces No; Has season or migrant farm work been your or your family's main source of income at any point in past 2 years [PRAPARE] No; Race White; Hispanic or Latino No | status final | LOINC 93025-5
[Observation/0eeb6aa3-c249-0e46-8cd1-1bb1f37f5764] Observation (survey) | 2026-08-09 | Protocol for Responding to and Assessing Patients' Assets, Risks, and Experiences [PRAPARE] = Within the last year, have you been afraid of your partner or ex-partner No; Do you feel physically and emotionally safe where you currently live [PRAPARE] Yes; Are you a refugee No; Have you spent more than 2 nights in a row in a jail, prison, detention center, or juvenile correctional facility in past 1 year [PRAPARE] No; Stress level Not at all; How often do you see or talk to people that you care about and feel close to [PRAPARE] 3 to 5 times a week; Has lack of transportation kept you from medical appointments, meetings, work, or from getting things needed for daily living No; Have you or any family members you live with been unable to get any of the following when it was really needed in past 1 year [PRAPARE] Food; What was your best estimate of the total income of all family members from all sources, before taxes, in last year [PhenX] 18408 /a; Primary insurance Medicaid; Employment status - current Full-time work; Highest level of education More than high school; Address 1026 Shanahan Street Unit 90; Are you worried about losing your housing [PRAPARE] No; Housing status I have housing; How many people are living or staying at this address [#] 7 {#}; Preferred language English; Discharged from the U.S. Armed Forces No; Has season or migrant farm work been your or your family's main source of income at any point in past 2 years [PRAPARE] No; Race White; Hispanic or Latino No | status final | LOINC 93025-5
[Observation/0eeb6aa3-c249-0e46-9a14-057ea96c115e] Observation (survey) | 2025-12-14 | Protocol for Responding to and Assessing Patients' Assets, Risks, and Experiences [PRAPARE] = Within the last year, have you been afraid of your partner or ex-partner No; Do you feel physically and emotionally safe where you currently live [PRAPARE] Yes; Are you a refugee No; Have you spent more than 2 nights in a row in a jail, prison, detention center, or juvenile correctional facility in past 1 year [PRAPARE] No; Stress level Somewhat; How often do you see or talk to people that you care about and feel close to [PRAPARE] 5 or more times a week; Has lack of transportation kept you from medical appointments, meetings, work, or from getting things needed for daily living No; Have you or any family members you live with been unable to get any of the following when it was really needed in past 1 year [PRAPARE] Other; What was your best estimate of the total income of all family members from all sources, before taxes, in last year [PhenX] 18408 /a; Primary insurance Medicaid; Employment status - current Full-time work; Highest level of education More than high school; Address 1026 Shanahan Street Unit 90; Are you worried about losing your housing [PRAPARE] No; Housing status I have housing; How many people are living or staying at this address [#] 7 {#}; Preferred language English; Discharged from the U.S. Armed Forces No; Has season or migrant farm work been your or your family's main source of income at any point in past 2 years [PRAPARE] No; Race White; Hispanic or Latino No | status final | LOINC 93025-5
[Observation/0eeb6aa3-c249-0e46-149f-504272d0666a] Observation (survey) | 2025-07-20 | Protocol for Responding to and Assessing Patients' Assets, Risks, and Experiences [PRAPARE] = Within the last year, have you been afraid of your partner or ex-partner No; Do you feel physically and emotionally safe where you currently live [PRAPARE] Yes; Are you a refugee No; Have you spent more than 2 nights in a row in a jail, prison, detention center, or juvenile correctional facility in past 1 year [PRAPARE] No; Stress level Quite a bit; How often do you see or talk to people that you care about and feel close to [PRAPARE] 5 or more times a week; Has lack of transportation kept you from medical appointments, meetings, work, or from getting things needed for daily living No; Have you or any family members you live with been unable to get any of the following when it was really needed in past 1 year [PRAPARE] I choose not to answer this question; What was your best estimate of the total income of all family members from all sources, before taxes, in last year [PhenX] 18408 /a; Primary insurance Medicaid; Employment status - current Unemployed; Highest level of education More than high school; Address 1026 Shanahan Street Unit 90; Are you worried about losing your housing [PRAPARE] No; Housing status I have housing; How many people are living or staying at this address [#] 7 {#}; Preferred language English; Discharged from the U.S. Armed Forces No; Has season or migrant farm work been your or your family's main source of income at any point in past 2 years [PRAPARE] Yes; Race White; Hispanic or Latino No | status final | LOINC 93025-5
[Procedure/0eeb6aa3-c249-0e46-7fba-df171b06549c] Procedure | 2021-12-12 | History taking (procedure) | status completed | reason: Diabetes mellitus type 2 (disorder) | SNOMED 84100007
[Immunization/0eeb6aa3-c249-0e46-7a2a-645241e28212] Immunization | 2021-04-11 | COVID-19, mRNA, LNP-S, PF, 30 mcg/0.3 mL dose | status completed | CVX 208
[Immunization/0eeb6aa3-c249-0e46-b7a5-0b7440de25ee] Immunization | 2021-03-21 | COVID-19, mRNA, LNP-S, PF, 30 mcg/0.3 mL dose | status completed | CVX 208
```

</details>

label: s
note: Cited immunization is Influenza, split virus, trivalent, PF on 2026-08-09, completed; the other flu shots seen (2025-07-06, 2024-08-18, 2023-12-03) are earlier.

## 31. `last-flu-shot:e56a8cde#0#1`

Question: When did the patient last get a flu shot?

Answer: The patient's most recent flu shot was on 2025-12-25 (Influenza, split virus, trivalent, PF; status completed). **Earlier influenza vaccinations were given on 2024-12-19, 2023-12-14, and 2016-11-03.**

Cards this sentence cites:

- `[Immunization/e56a8cde-8395-a37d-2679-541acde9ac04]` Immunization | 2024-12-19 | Influenza, split virus, trivalent, PF | status completed | CVX 140
- `[Immunization/e56a8cde-8395-a37d-55b4-0002692e8619]` Immunization | 2023-12-14 | Influenza, split virus, trivalent, PF | status completed | CVX 140
- `[Immunization/e56a8cde-8395-a37d-ff2c-7a583e1d9ddd]` Immunization | 2016-11-03 | Influenza, split virus, trivalent, PF | status completed | CVX 140

<details><summary>Everything the model saw (56 cards)</summary>

```text
[Condition/e56a8cde-8395-a37d-f7ae-15d35f13e9f0] Condition | onset 2025-12-25 | Victim of intimate partner abuse (finding) | clinical status active | SNOMED 706893006
[Condition/e56a8cde-8395-a37d-80d3-3984f14d8bb3] Condition | onset 2025-12-25 | Stress (finding) | clinical status active | SNOMED 73595000
[Condition/e56a8cde-8395-a37d-5c7c-75429c6f1e56] Condition | onset 2025-12-25 | Medication review due (situation) | clinical status active | SNOMED 314529007
[Condition/e56a8cde-8395-a37d-354e-df92238c35a7] Condition | onset 2025-12-25 | Unemployed (finding) | clinical status active | SNOMED 73438004
[Condition/e56a8cde-8395-a37d-6690-7ef5746552bd] Condition | onset 2017-11-09 | Hyperlipidemia (disorder) | clinical status active | SNOMED 55822004
[Condition/e56a8cde-8395-a37d-922a-d32061194c0b] Condition | onset 2016-11-03 | Gingivitis (disorder) | clinical status active | SNOMED 66383009
[Condition/e56a8cde-8395-a37d-e775-23849ffbe97b] Condition | onset 2014-02-01 | Chronic low back pain (finding) | clinical status active | SNOMED 278860009
[Condition/e56a8cde-8395-a37d-a82c-6129bc784139] Condition | onset 2014-02-01 | Chronic pain (finding) | clinical status active | SNOMED 82423001
[Condition/e56a8cde-8395-a37d-64b8-86023f198a46] Condition | onset 2014-02-01 | Chronic neck pain (finding) | clinical status active | SNOMED 1121000119107
[Condition/e56a8cde-8395-a37d-e547-8e085bacfa8e] Condition | onset 2007-09-13 | Has a criminal record (finding) | clinical status active | SNOMED 266948004
[Condition/e56a8cde-8395-a37d-37b4-500cf9e797e9] Condition | onset 2005-09-01 | Osteoporosis (disorder) | clinical status active | SNOMED 64859006
[Condition/e56a8cde-8395-a37d-d5cb-6239a28a0055] Condition | onset 2003-12-16 | History of myocardial infarction (situation) | clinical status active | SNOMED 399211009
[Condition/e56a8cde-8395-a37d-4d5f-670d3e1632bc] Condition | onset 2003-12-16 | Acute non-ST segment elevation myocardial infarction (disorder) | clinical status active | SNOMED 401314000
[Condition/e56a8cde-8395-a37d-1853-568436ee1ea2] Condition | onset 2001-08-20 | History of coronary artery bypass grafting (situation) | clinical status active | SNOMED 399261000
[Condition/e56a8cde-8395-a37d-810b-643d651149ba] Condition | onset 2001-08-18 | Abnormal findings diagnostic imaging heart+coronary circulat (finding) | clinical status active | SNOMED 274531002
[Condition/e56a8cde-8395-a37d-2761-7d0bfc799087] Condition | onset 2001-08-09 | Ischemic heart disease (disorder) | clinical status active | SNOMED 414545008
[Condition/e56a8cde-8395-a37d-ed31-c4144dbefb9e] Condition | onset 1996-05-17 | Osteoarthritis of knee (disorder) | clinical status active | SNOMED 239873007
[Condition/e56a8cde-8395-a37d-333f-0835bee4de98] Condition | onset 1991-06-13 | Essential hypertension (disorder) | clinical status active | SNOMED 59621000
[Condition/e56a8cde-8395-a37d-30cd-5f4f9de67da3] Condition | onset 1967-07-27 | Lack of access to transportation (finding) | clinical status active | SNOMED 713458007
[Condition/e56a8cde-8395-a37d-ac70-0b466edf16a1] Condition | onset 1963-07-18 | Transport problem (finding) | clinical status active | SNOMED 266934004
[Condition/e56a8cde-8395-a37d-99e6-93fe1e3f6036] Condition | onset 1963-07-18 | Only received primary school education (finding) | clinical status active | SNOMED 224295006
[MedicationRequest/e56a8cde-8395-a37d-0c1b-7da0b396a0c4] MedicationRequest | prescribed 2026-01-01 | Simvastatin 10 MG Oral Tablet | status active | reason: Hyperlipidemia (disorder) | RxNorm 314231
[MedicationRequest/e56a8cde-8395-a37d-f153-06ed5ef5b40a] MedicationRequest | prescribed 2025-12-25 | Alendronic acid 10 MG Oral Tablet | status active | reason: Osteoporosis (disorder) | RxNorm 904419
[MedicationRequest/e56a8cde-8395-a37d-b70b-d6ff9e66fb91] MedicationRequest | prescribed 2025-12-25 | Acetaminophen 325 MG Oral Tablet [Tylenol] | status active | RxNorm 209387
[MedicationRequest/e56a8cde-8395-a37d-1cff-386c29158923] MedicationRequest | prescribed 2025-12-25 | lisinopril 10 MG Oral Tablet | status active | reason: Essential hypertension (disorder) | RxNorm 314076
[MedicationRequest/e56a8cde-8395-a37d-f778-f1044e9a8316] MedicationRequest | prescribed 2003-12-16 | atorvastatin 10 MG Oral Tablet | status active | RxNorm 617312
[MedicationRequest/e56a8cde-8395-a37d-e36e-ab680e0ad841] MedicationRequest | prescribed 2003-12-16 | hydrochlorothiazide 25 MG / lisinopril 20 MG Oral Tablet | status active | RxNorm 197887
[MedicationRequest/e56a8cde-8395-a37d-d237-6e376bbcb9a6] MedicationRequest | prescribed 2003-12-16 | metoprolol tartrate 25 MG Oral Tablet | status active | RxNorm 866924
[MedicationRequest/e56a8cde-8395-a37d-2fb4-edeac8b69b00] MedicationRequest | prescribed 2003-12-16 | prasugrel 10 MG Oral Tablet | status active | RxNorm 855812
[MedicationRequest/e56a8cde-8395-a37d-228f-f6135c165caa] MedicationRequest | prescribed 2003-12-16 | aspirin 81 MG Oral Tablet | status active | RxNorm 243670
[MedicationRequest/e56a8cde-8395-a37d-eee1-8d05287f0e29] MedicationRequest | prescribed 2001-08-16 | Nitroglycerin 0.4 MG/ACTUAT Mucosal Spray | status active | RxNorm 705129
[MedicationRequest/e56a8cde-8395-a37d-d36b-2e3fc9df975e] MedicationRequest | prescribed 2001-08-16 | 24 HR metoprolol succinate 100 MG Extended Release Oral Tablet | status active | RxNorm 866412
[MedicationRequest/e56a8cde-8395-a37d-a8c0-f9ed9ed3ea83] MedicationRequest | prescribed 2001-08-16 | Clopidogrel 75 MG Oral Tablet | status active | RxNorm 309362
[MedicationRequest/e56a8cde-8395-a37d-321f-ecd1d25263ad] MedicationRequest | prescribed 2001-08-16 | Simvastatin 20 MG Oral Tablet | status active | RxNorm 312961
[MedicationRequest/e56a8cde-8395-a37d-9456-c58ec0c7de32] MedicationRequest | prescribed 1949-01-17 | diphenhydrAMINE Hydrochloride 25 MG Oral Tablet | status active | RxNorm 1049630
[AllergyIntolerance/e56a8cde-8395-a37d-b318-8f34a7d6b5f7] AllergyIntolerance | recorded 1946-06-09 | Animal dander (substance) | allergy, category environment, criticality low | clinical status active | reactions: Eruption of skin (disorder); Rhinoconjunctivitis (disorder) | SNOMED 264287008
[AllergyIntolerance/e56a8cde-8395-a37d-a098-9831a40ac85b] AllergyIntolerance | recorded 1946-06-09 | Mold (organism) | allergy, category environment, criticality low | clinical status active | SNOMED 84489001
[AllergyIntolerance/e56a8cde-8395-a37d-85d4-fe7519012219] AllergyIntolerance | recorded 1946-06-09 | House dust mite (organism) | allergy, category environment, criticality low | clinical status active | SNOMED 260147004
[AllergyIntolerance/e56a8cde-8395-a37d-60c2-b75e4a4d4513] AllergyIntolerance | recorded 1946-06-09 | Tree pollen (substance) | allergy, category environment, criticality low | clinical status active | SNOMED 782576004
[AllergyIntolerance/e56a8cde-8395-a37d-5834-224d1127b6f9] AllergyIntolerance | recorded 1946-06-09 | Grass pollen (substance) | allergy, category environment, criticality low | clinical status active | SNOMED 256277009
[AllergyIntolerance/e56a8cde-8395-a37d-2daa-dbe0dbcf6ecf] AllergyIntolerance | recorded 1946-06-09 | Shellfish (substance) | allergy, category food, criticality low | clinical status active | reactions: Dyspnea (finding); Allergic angioedema (disorder); Itching (finding); Cough (finding); Diarrhea (finding) | SNOMED 735029006
[AllergyIntolerance/e56a8cde-8395-a37d-1508-bdb84bdc4c5d] AllergyIntolerance | recorded 1946-06-09 | Allergic disposition (finding) | allergy, category environment, criticality low | clinical status active | SNOMED 609328004
[Encounter/e56a8cde-8395-a37d-9f47-5b69723a8690] Encounter | 2026-01-01 | Follow-up encounter (procedure) | class AMB | reason: Hyperlipidemia (disorder) | at DANA FARBER CANCER INSTITUTE
[Encounter/e56a8cde-8395-a37d-2450-250d53d64dc7] Encounter | 2025-12-25 | General examination of patient (procedure) | class AMB | at SOUTH SHORE PRIMARY CARE PC
[Encounter/e56a8cde-8395-a37d-20eb-f707e34a4164] Encounter | 2024-12-20 | Follow-up encounter (procedure) | class AMB | reason: Hyperlipidemia (disorder) | at DANA FARBER CANCER INSTITUTE
[Immunization/e56a8cde-8395-a37d-7cd1-bb3bac5572f3] Immunization | 2025-12-25 | Influenza, split virus, trivalent, PF | status completed | CVX 140
[Immunization/e56a8cde-8395-a37d-ff2c-7a583e1d9ddd] Immunization | 2016-11-03 | Influenza, split virus, trivalent, PF | status completed | CVX 140
[Immunization/e56a8cde-8395-a37d-2679-541acde9ac04] Immunization | 2024-12-19 | Influenza, split virus, trivalent, PF | status completed | CVX 140
[Immunization/e56a8cde-8395-a37d-55b4-0002692e8619] Immunization | 2023-12-14 | Influenza, split virus, trivalent, PF | status completed | CVX 140
[Observation/e56a8cde-8395-a37d-c2c3-7ecfb87783d5] Observation (survey) | 2017-11-09 | Protocol for Responding to and Assessing Patients' Assets, Risks, and Experiences [PRAPARE] = Within the last year, have you been afraid of your partner or ex-partner No; Do you feel physically and emotionally safe where you currently live [PRAPARE] Yes; Are you a refugee No; Have you spent more than 2 nights in a row in a jail, prison, detention center, or juvenile correctional facility in past 1 year [PRAPARE] Yes; Stress level Somewhat; How often do you see or talk to people that you care about and feel close to [PRAPARE] 5 or more times a week; Has lack of transportation kept you from medical appointments, meetings, work, or from getting things needed for daily living Yes, it has kept me from medical appointments or from getting my medications; Have you or any family members you live with been unable to get any of the following when it was really needed in past 1 year [PRAPARE] Other; What was your best estimate of the total income of all family members from all sources, before taxes, in last year [PhenX] 93343 /a; Primary insurance Medicare; Employment status - current Full-time work; Highest level of education Less than high school degree; Address 791 Wintheiser Club; Are you worried about losing your housing [PRAPARE] No; Housing status I have housing; How many people are living or staying at this address [#] 7 {#}; Preferred language English; Discharged from the U.S. Armed Forces No; Has season or migrant farm work been your or your family's main source of income at any point in past 2 years [PRAPARE] No; Race White; Hispanic or Latino No | status final | LOINC 93025-5
[Observation/e56a8cde-8395-a37d-26c2-3b03ace41dd6] Observation (survey) | 2025-12-25 | Protocol for Responding to and Assessing Patients' Assets, Risks, and Experiences [PRAPARE] = Within the last year, have you been afraid of your partner or ex-partner Yes; Do you feel physically and emotionally safe where you currently live [PRAPARE] Yes; Are you a refugee No; Have you spent more than 2 nights in a row in a jail, prison, detention center, or juvenile correctional facility in past 1 year [PRAPARE] Yes; Stress level A little bit; How often do you see or talk to people that you care about and feel close to [PRAPARE] 3 to 5 times a week; Has lack of transportation kept you from medical appointments, meetings, work, or from getting things needed for daily living Yes, it has kept me from non-medical meetings, appointments, work, or from getting things that I need; Have you or any family members you live with been unable to get any of the following when it was really needed in past 1 year [PRAPARE] I choose not to answer this question; What was your best estimate of the total income of all family members from all sources, before taxes, in last year [PhenX] 93343 /a; Primary insurance Medicare; Employment status - current Unemployed; Highest level of education Less than high school degree; Address 791 Wintheiser Club; Are you worried about losing your housing [PRAPARE] No; Housing status I have housing; How many people are living or staying at this address [#] 7 {#}; Preferred language English; Discharged from the U.S. Armed Forces No; Has season or migrant farm work been your or your family's main source of income at any point in past 2 years [PRAPARE] No; Race White; Hispanic or Latino No | status final | LOINC 93025-5
[Observation/e56a8cde-8395-a37d-93d2-c1eed5087fe3] Observation (survey) | 2024-12-19 | Protocol for Responding to and Assessing Patients' Assets, Risks, and Experiences [PRAPARE] = Within the last year, have you been afraid of your partner or ex-partner No; Do you feel physically and emotionally safe where you currently live [PRAPARE] Yes; Are you a refugee No; Have you spent more than 2 nights in a row in a jail, prison, detention center, or juvenile correctional facility in past 1 year [PRAPARE] Yes; Stress level Not at all; How often do you see or talk to people that you care about and feel close to [PRAPARE] 5 or more times a week; Has lack of transportation kept you from medical appointments, meetings, work, or from getting things needed for daily living Yes, it has kept me from non-medical meetings, appointments, work, or from getting things that I need; Have you or any family members you live with been unable to get any of the following when it was really needed in past 1 year [PRAPARE] I choose not to answer this question; What was your best estimate of the total income of all family members from all sources, before taxes, in last year [PhenX] 93343 /a; Primary insurance Medicare; Employment status - current Full-time work; Highest level of education Less than high school degree; Address 791 Wintheiser Club; Are you worried about losing your housing [PRAPARE] No; Housing status I have housing; How many people are living or staying at this address [#] 7 {#}; Preferred language English; Discharged from the U.S. Armed Forces No; Has season or migrant farm work been your or your family's main source of income at any point in past 2 years [PRAPARE] No; Race White; Hispanic or Latino No | status final | LOINC 93025-5
[Observation/e56a8cde-8395-a37d-4cfe-066ec7606c27] Observation (survey) | 2023-12-14 | Protocol for Responding to and Assessing Patients' Assets, Risks, and Experiences [PRAPARE] = Within the last year, have you been afraid of your partner or ex-partner No; Do you feel physically and emotionally safe where you currently live [PRAPARE] Yes; Are you a refugee No; Have you spent more than 2 nights in a row in a jail, prison, detention center, or juvenile correctional facility in past 1 year [PRAPARE] Yes; Stress level Not at all; How often do you see or talk to people that you care about and feel close to [PRAPARE] 3 to 5 times a week; Has lack of transportation kept you from medical appointments, meetings, work, or from getting things needed for daily living Yes, it has kept me from medical appointments or from getting my medications; Have you or any family members you live with been unable to get any of the following when it was really needed in past 1 year [PRAPARE] I choose not to answer this question; What was your best estimate of the total income of all family members from all sources, before taxes, in last year [PhenX] 93343 /a; Primary insurance Medicare; Employment status - current Full-time work; Highest level of education Less than high school degree; Address 791 Wintheiser Club; Are you worried about losing your housing [PRAPARE] No; Housing status I have housing; How many people are living or staying at this address [#] 7 {#}; Preferred language English; Discharged from the U.S. Armed Forces No; Has season or migrant farm work been your or your family's main source of income at any point in past 2 years [PRAPARE] No; Race White; Hispanic or Latino No | status final | LOINC 93025-5
[DocumentReference/b3013519-3000-7f68-7b32-de706218460e#2] Clinical note | 2018-11-15 | part 2 of 2 | # Assessment and Plan ## Plan Patient was given the following immunizations: influenza, split virus, trivalent, pf. The following procedures were conducted: - medication reconciliation (procedure) - assessment of health and social care needs (procedure) - assessment of anxiety (procedure) - depression screening (procedure) - depression screening (procedure) - assessment of substance use (procedure) - screening for drug abuse (procedure) - patient referral for dental care (procedure) The following lab reports were completed: - lipid panel with direct ldl - serum or plasma - generalized anxiety disorder 7 item (gad-7) - patient health questionnaire 2 item (phq-2) [reported] - drug abuse screening test-10 [dast-10] The patient was prescribed the following medications: - acetaminophen 325 mg oral tablet [tylenol] - lisinopril 10 mg oral tablet - alendronic acid 10 mg oral tablet
[Condition/e56a8cde-8395-a37d-69c0-a727f224eaed] Condition | onset 2023-12-14 | Medication review due (situation) | clinical status resolved | resolved 2023-12-14 | SNOMED 314529007
[Condition/e56a8cde-8395-a37d-c0ad-27ddea6d5687] Condition | onset 2024-12-19 | Medication review due (situation) | clinical status resolved | resolved 2024-12-19 | SNOMED 314529007
```

</details>

label: p?
note: The three dates (2024-12-19, 2023-12-14, 2016-11-03) match the cited Immunization cards, but the sentence reads as the full list of earlier flu shots and leaves out the 2018-11-15 clinical note (part 2), which records an influenza split virus trivalent PF immunization.

## 32. `latest-lab-2571-8:760e0542#0#0`

Question: What was the patient's most recent triglycerides result, and when was it measured?

Answer: **The patient's most recent triglyceride result was 142.92 mg/dL, measured on 2026-09-09.**

Cards this sentence cites:

- `[Observation/760e0542-9c61-9c1a-64b4-980543a63c85]` Observation (laboratory) | 2026-09-09 | Triglyceride [Mass/volume] in Serum or Plasma = 142.92 mg/dL | status final | LOINC 2571-8

<details><summary>Everything the model saw (44 cards)</summary>

```text
[Condition/760e0542-9c61-9c1a-f014-d96ecb52354b] Condition | onset 2026-09-09 | Full-time employment (finding) | clinical status active | SNOMED 160903007
[Condition/760e0542-9c61-9c1a-3909-ca43a58a2be0] Condition | onset 2023-02-08 | Social isolation (finding) | clinical status active | SNOMED 422650009
[Condition/760e0542-9c61-9c1a-0603-33ac04e928e9] Condition | onset 2017-07-26 | Has a criminal record (finding) | clinical status active | SNOMED 266948004
[Condition/760e0542-9c61-9c1a-7969-97405f2cda90] Condition | onset 2016-09-28 | Gingivitis (disorder) | clinical status active | SNOMED 66383009
[Condition/760e0542-9c61-9c1a-bc04-975a613f7bef] Condition | onset 2016-05-04 | Proteinuria due to type 2 diabetes mellitus (disorder) | clinical status active | SNOMED 157141000119108
[Condition/760e0542-9c61-9c1a-19fd-96240fc0e3b9] Condition | onset 2016-05-04 | Chronic kidney disease stage 3 (disorder) | clinical status active | SNOMED 433144002
[Condition/760e0542-9c61-9c1a-e1cf-d1bcca0d3b69] Condition | onset 2016-03-02 | Familial Alzheimer's disease of early onset (disorder) | clinical status active | SNOMED 230265002
[Condition/760e0542-9c61-9c1a-bf45-3800d10bb908] Condition | onset 2012-09-12 | Chronic sinusitis (disorder) | clinical status active | SNOMED 40055000
[Condition/760e0542-9c61-9c1a-6a42-9364f5d685e7] Condition | onset 2009-10-14 | Chronic kidney disease stage 2 (disorder) | clinical status active | SNOMED 431856006
[Condition/760e0542-9c61-9c1a-6844-45eca3bcbf32] Condition | onset 2009-10-14 | Microalbuminuria due to type 2 diabetes mellitus (disorder) | clinical status active | SNOMED 90781000119102
[Condition/760e0542-9c61-9c1a-c55b-b73483d412d5] Condition | onset 2004-09-01 | Disorder of kidney due to diabetes mellitus (disorder) | clinical status active | SNOMED 127013003
[Condition/760e0542-9c61-9c1a-8f20-42b2a944fe6e] Condition | onset 2004-09-01 | Chronic kidney disease stage 1 (disorder) | clinical status active | SNOMED 431855005
[Condition/760e0542-9c61-9c1a-426d-1b0e47f6ef3a] Condition | onset 2004-09-01 | Hyperglycemia (disorder) | clinical status active | SNOMED 80394007
[Condition/760e0542-9c61-9c1a-84cc-6ec1252b5c47] Condition | onset 1998-10-12 | History of tubal ligation (situation) | clinical status active | SNOMED 267020005
[Condition/760e0542-9c61-9c1a-d618-c814cd687574] Condition | onset 1998-01-07 | Hypertriglyceridemia (disorder) | clinical status active | SNOMED 302870006
[Condition/760e0542-9c61-9c1a-addb-545c11e2d54a] Condition | onset 1998-01-07 | Metabolic syndrome X (disorder) | clinical status active | SNOMED 237602007
[Condition/760e0542-9c61-9c1a-393d-4476d7ede869] Condition | onset 1995-01-04 | Diabetes mellitus type 2 (disorder) | clinical status active | SNOMED 44054006
[Condition/760e0542-9c61-9c1a-0e56-fe029b0a5419] Condition | onset 1990-08-12 | Past pregnancy history of miscarriage (situation) | clinical status active | SNOMED 161744009
[Condition/760e0542-9c61-9c1a-8747-2a2b77e88f89] Condition | onset 1988-12-28 | Anemia (disorder) | clinical status active | SNOMED 271737000
[Condition/760e0542-9c61-9c1a-4f0e-0a94437d4aaa] Condition | onset 1988-12-28 | Body mass index 30+ - obesity (finding) | clinical status active | SNOMED 162864005
[Condition/760e0542-9c61-9c1a-771f-54deeed066bf] Condition | onset 1982-12-22 | Prediabetes (finding) | clinical status active | SNOMED 714628002
[Condition/760e0542-9c61-9c1a-0604-679a8d525bc1] Condition | onset 1981-12-16 | Received higher education (finding) | clinical status active | SNOMED 224299000
[Condition/760e0542-9c61-9c1a-c792-3a8303530414] Condition | onset 1979-12-05 | Risk activity involvement (finding) | clinical status active | SNOMED 160968000
[Condition/760e0542-9c61-9c1a-1d06-faad5e8f657c] Condition | onset 1974-01-03 | Adolescent idiopathic scoliosis (disorder) | clinical status active | SNOMED 203646004
[MedicationRequest/760e0542-9c61-9c1a-c29f-4c3b83db674e] MedicationRequest | prescribed 2026-09-09 | 24 HR Metformin hydrochloride 500 MG Extended Release Oral Tablet | status active | reason: Diabetes mellitus type 2 (disorder) | RxNorm 860975
[MedicationRequest/760e0542-9c61-9c1a-096d-4868f9087e48] MedicationRequest | prescribed 2026-09-09 | insulin isophane, human 70 UNT/ML / insulin, regular, human 30 UNT/ML Injectable Suspension [Humulin] | status active | reason: Diabetes mellitus type 2 (disorder) | RxNorm 106892
[MedicationRequest/760e0542-9c61-9c1a-c259-531395abfaa1] MedicationRequest | prescribed 2023-01-14 | 24 HR Donepezil hydrochloride 10 MG / Memantine hydrochloride 28 MG Extended Release Oral Capsule | status active | reason: Familial Alzheimer's disease of early onset (disorder) | RxNorm 1599803
[MedicationRequest/760e0542-9c61-9c1a-fd81-acf11c1ddec0] MedicationRequest | prescribed 1967-04-25 | Chlorpheniramine Maleate 2 MG/ML Oral Solution | status active | RxNorm 477045
[AllergyIntolerance/760e0542-9c61-9c1a-3695-658972edefe5] AllergyIntolerance | recorded 1967-05-01 | Allergic disposition (finding) | allergy, category environment, criticality low | clinical status active | SNOMED 609328004
[AllergyIntolerance/760e0542-9c61-9c1a-1887-b0f58a6117f4] AllergyIntolerance | recorded 1967-05-01 | Lisinopril | intolerance, category medication, criticality low | clinical status active | RxNorm 29046
[Encounter/760e0542-9c61-9c1a-6caa-86123ce8fd48] Encounter | 2026-09-09 | Urgent care clinic (environment) | class AMB | at MIDDLETON FAMILY MEDICINE URGENT CARE, LLC
[Encounter/760e0542-9c61-9c1a-dbc8-3964b3a3c72f] Encounter | 2026-08-05 | Urgent care clinic (environment) | class AMB | at MIDDLETON FAMILY MEDICINE URGENT CARE, LLC
[Encounter/760e0542-9c61-9c1a-d9e8-129c4edf531b] Encounter | 2026-05-27 | Encounter for check up (procedure) | class AMB | at LAWRENCE GENERAL HOSPITAL
[Immunization/760e0542-9c61-9c1a-bb77-51bf2da7f927] Immunization | 2026-04-08 | Influenza, split virus, trivalent, PF | status completed | CVX 140
[Observation/760e0542-9c61-9c1a-a6c5-e0368436305f] Observation (laboratory) | 2020-12-23 | Triglyceride [Mass/volume] in Serum or Plasma = 121.81 mg/dL | status final | LOINC 2571-8
[Observation/760e0542-9c61-9c1a-64b4-980543a63c85] Observation (laboratory) | 2026-09-09 | Triglyceride [Mass/volume] in Serum or Plasma = 142.92 mg/dL | status final | LOINC 2571-8
[Observation/760e0542-9c61-9c1a-bdda-c4e20ca4aba5] Observation (laboratory) | 2026-08-05 | Triglyceride [Mass/volume] in Serum or Plasma = 140.68 mg/dL | status final | LOINC 2571-8
[Observation/760e0542-9c61-9c1a-68cc-2e0634bcede4] Observation (laboratory) | 2026-05-13 | Triglyceride [Mass/volume] in Serum or Plasma = 102.5 mg/dL | status final | LOINC 2571-8
[Immunization/760e0542-9c61-9c1a-bb55-2e74e1870df5] Immunization | 2021-05-05 | COVID-19, mRNA, LNP-S, PF, 30 mcg/0.3 mL dose | status completed | CVX 208
[Immunization/760e0542-9c61-9c1a-348d-850ee604a0a7] Immunization | 2021-04-14 | COVID-19, mRNA, LNP-S, PF, 30 mcg/0.3 mL dose | status completed | CVX 208
[Encounter/760e0542-9c61-9c1a-2861-bf73d649f457] Encounter | 2024-11-06 | Follow-up consultation (procedure) | class AMB | reason: Familial Alzheimer's disease of early onset (disorder) | at LAWRENCE GENERAL HOSPITAL
[Encounter/760e0542-9c61-9c1a-288d-f959733c1cc1] Encounter | 2023-01-14 | Follow-up consultation (procedure) | class VR | reason: Familial Alzheimer's disease of early onset (disorder) | at LAWRENCE GENERAL HOSPITAL
[MedicationRequest/760e0542-9c61-9c1a-6b3b-5b42378d77ac] MedicationRequest | prescribed 2016-03-02 | Galantamine 4 MG Oral Tablet | status completed | reason: Familial Alzheimer's disease of early onset (disorder) | RxNorm 310436
[DocumentReference/dea8e555-16a6-228a-ab25-b69355fdcefe#2] Clinical note | 2021-04-14 | part 2 of 2 | # Assessment and Plan ## Plan Patient was given the following immunizations: covid-19, mrna, lnp-s, pf, 30 mcg/0.3 ml dose. The following lab reports were completed: - basic metabolic 2000 panel - serum or plasma - urinalysis macro (dipstick) panel - urine The patient was prescribed the following medications: - insulin isophane, human 70 unt/ml / insulin, regular, human 30 unt/ml injectable suspension [humulin] - 24 hr metformin hydrochloride 500 mg extended release oral tablet
```

</details>

label: s
note: The record has four triglyceride results (2020-12-23, 2026-05-13, 2026-08-05, 2026-09-09). The latest is 2026-09-09 at 142.92 mg/dL, which matches the cited card exactly.

## 33. `active-problems:0eeb6aa3#0#1`

Question: What active diagnoses does the patient have?

Answer: Active diagnoses include primary fibromyalgia syndrome (onset 2026-07-29), metabolic syndrome X, hypertriglyceridemia, and hyperglycemia (all onset 2022-11-27). **Also active are essential hypertension and diabetes mellitus type 2 (both onset 2021-11-21), osteoarthritis of knee (onset 2021-04-07), obesity with BMI 30+ (onset 2013-11-03), and prediabetes (onset 2008-01-13).** Other active findings include misuses drugs (onset 2025-12-14), victim of intimate partner abuse (onset 2021-11-21), history of tubal ligation, and risk activity involvement.

Cards this sentence cites:

- `[Condition/0eeb6aa3-c249-0e46-d84e-f3245ad02f8e]` Condition | onset 2021-11-21 | Essential hypertension (disorder) | clinical status active | SNOMED 59621000
- `[Condition/0eeb6aa3-c249-0e46-8d5d-18bd4ff7c429]` Condition | onset 2021-11-21 | Diabetes mellitus type 2 (disorder) | clinical status active | SNOMED 44054006
- `[Condition/0eeb6aa3-c249-0e46-0e2a-b4435a3e06d7]` Condition | onset 2021-04-07 | Osteoarthritis of knee (disorder) | clinical status active | SNOMED 239873007
- `[Condition/0eeb6aa3-c249-0e46-c1e0-a1835f8dfe99]` Condition | onset 2013-11-03 | Body mass index 30+ - obesity (finding) | clinical status active | SNOMED 162864005
- `[Condition/0eeb6aa3-c249-0e46-05b2-ee89706489e7]` Condition | onset 2008-01-13 | Prediabetes (finding) | clinical status active | SNOMED 714628002

<details><summary>Everything the model saw (36 cards)</summary>

```text
[Condition/0eeb6aa3-c249-0e46-6f19-eb10a1f328db] Condition | onset 2026-07-29 | Primary fibromyalgia syndrome (disorder) | clinical status active | SNOMED 95417003
[Condition/0eeb6aa3-c249-0e46-44b4-3580330e81b7] Condition | onset 2025-12-14 | Misuses drugs (finding) | clinical status active | SNOMED 361055000
[Condition/0eeb6aa3-c249-0e46-2c95-28a9408c6896] Condition | onset 2025-12-14 | Full-time employment (finding) | clinical status active | SNOMED 160903007
[Condition/0eeb6aa3-c249-0e46-b1be-047f25b1022e] Condition | onset 2022-11-27 | Metabolic syndrome X (disorder) | clinical status active | SNOMED 237602007
[Condition/0eeb6aa3-c249-0e46-6def-33ad344a7a9b] Condition | onset 2022-11-27 | Hypertriglyceridemia (disorder) | clinical status active | SNOMED 302870006
[Condition/0eeb6aa3-c249-0e46-06a5-9d3ec2ee65d0] Condition | onset 2022-11-27 | Hyperglycemia (disorder) | clinical status active | SNOMED 80394007
[Condition/0eeb6aa3-c249-0e46-d84e-f3245ad02f8e] Condition | onset 2021-11-21 | Essential hypertension (disorder) | clinical status active | SNOMED 59621000
[Condition/0eeb6aa3-c249-0e46-ce58-8dd4753fcdb4] Condition | onset 2021-11-21 | Victim of intimate partner abuse (finding) | clinical status active | SNOMED 706893006
[Condition/0eeb6aa3-c249-0e46-8d5d-18bd4ff7c429] Condition | onset 2021-11-21 | Diabetes mellitus type 2 (disorder) | clinical status active | SNOMED 44054006
[Condition/0eeb6aa3-c249-0e46-0e2a-b4435a3e06d7] Condition | onset 2021-04-07 | Osteoarthritis of knee (disorder) | clinical status active | SNOMED 239873007
[Condition/0eeb6aa3-c249-0e46-c1e0-a1835f8dfe99] Condition | onset 2013-11-03 | Body mass index 30+ - obesity (finding) | clinical status active | SNOMED 162864005
[Condition/0eeb6aa3-c249-0e46-7e82-50da4e26d936] Condition | onset 2009-08-25 | History of tubal ligation (situation) | clinical status active | SNOMED 267020005
[Condition/0eeb6aa3-c249-0e46-05b2-ee89706489e7] Condition | onset 2008-01-13 | Prediabetes (finding) | clinical status active | SNOMED 714628002
[Condition/0eeb6aa3-c249-0e46-1bf9-48c5ad5ed3c4] Condition | onset 1991-12-22 | Received higher education (finding) | clinical status active | SNOMED 224299000
[Condition/0eeb6aa3-c249-0e46-7231-74f682325091] Condition | onset 1988-12-04 | Risk activity involvement (finding) | clinical status active | SNOMED 160968000
[MedicationRequest/0eeb6aa3-c249-0e46-d035-2af008a23544] MedicationRequest | prescribed 2026-08-09 | amLODIPine 2.5 MG Oral Tablet | status active | reason: Essential hypertension (disorder) | RxNorm 308136
[MedicationRequest/0eeb6aa3-c249-0e46-9e8f-3bc3a049dcd6] MedicationRequest | prescribed 2026-08-09 | Hydrochlorothiazide 25 MG Oral Tablet | status active | reason: Essential hypertension (disorder) | RxNorm 310798
[MedicationRequest/0eeb6aa3-c249-0e46-9979-087d4ecb9395] MedicationRequest | prescribed 2026-08-09 | lisinopril 10 MG Oral Tablet | status active | reason: Essential hypertension (disorder) | RxNorm 314076
[MedicationRequest/0eeb6aa3-c249-0e46-8801-c4efefa8fdf6] MedicationRequest | prescribed 2026-08-09 | 24 HR Metformin hydrochloride 500 MG Extended Release Oral Tablet | status active | reason: Diabetes mellitus type 2 (disorder) | RxNorm 860975
[MedicationRequest/0eeb6aa3-c249-0e46-48fb-484102ab7f68] MedicationRequest | prescribed 2026-07-29 | Naproxen 500 MG Oral Tablet | status active | reason: Primary fibromyalgia syndrome (disorder) | RxNorm 198014
[MedicationRequest/0eeb6aa3-c249-0e46-7cb4-1e0c24948d9a] MedicationRequest | prescribed 2021-04-07 | Naproxen sodium 220 MG Oral Tablet | status active | reason: Osteoarthritis of knee (disorder) | RxNorm 849574
[MedicationRequest/0eeb6aa3-c249-0e46-6749-08c77e3ff56d] MedicationRequest | prescribed 1993-03-28 | ferrous sulfate 325 MG Oral Tablet | status active | RxNorm 310325
[Encounter/0eeb6aa3-c249-0e46-4c0e-5bc7f2736fbd] Encounter | 2026-08-09 | Urgent care clinic (environment) | class AMB | at URGENT HELP CHELMSFORD PC
[Encounter/0eeb6aa3-c249-0e46-43a1-ecea1c0a2a61] Encounter | 2026-07-29 | Encounter for problem (procedure) | class AMB | reason: Primary fibromyalgia syndrome (disorder) | at HOLY FAMILY HOSPITAL
[Encounter/0eeb6aa3-c249-0e46-d415-7e8395059f69] Encounter | 2026-01-04 | Encounter for check up (procedure) | class AMB | reason: Patient referral for dental care (procedure) | at HOLY FAMILY HOSPITAL
[Immunization/0eeb6aa3-c249-0e46-99a3-4dae451772fe] Immunization | 2026-08-09 | Influenza, split virus, trivalent, PF | status completed | CVX 140
[Condition/0eeb6aa3-c249-0e46-0893-f2e439b68154] Condition | onset 2019-11-17 | Full-time employment (finding) | clinical status resolved | resolved 2024-08-18 | SNOMED 160903007
[Condition/0eeb6aa3-c249-0e46-dbc8-2be40b51cb31] Condition | onset 2019-11-17 | Victim of intimate partner abuse (finding) | clinical status resolved | resolved 2021-11-21 | SNOMED 706893006
[DocumentReference/1fdd7223-94ae-8e9f-e6c5-3675ea1f857a#1] Clinical note | 2017-11-26 | part 1 of 1 | 2017-11-26 # Chief Complaint - Muscle Pain - Fatigue - Memory Loss - Stiffness - Decreased Communication - Decreased Visual Perception - Cognitive Difficulties # History of Present Illness Azucena377 Trina350 is a 44 year-old hispanic white female. Patient has a history of part-time employment (finding), medication review due (situation), dental caries on smooth surface penetrating into pulp, gingivitis (disorder), stress (finding). # Social History Patient is married. Patient has never smoked. Patient identifies as heterosexual. Patient comes from a middle socioeconomic background. Patient has completed some college courses. Patient currently has Medicaid. # Allergies No Known Allergies. # Medications No Active Medications. # Assessment and Plan ## Plan The following procedures were conducted: - periodic oral evaluation established patient - prophylaxis adult
[DocumentReference/075e821c-0beb-21ac-d6e7-26c6edd8d939#1] Clinical note | 2008-01-13 | part 1 of 1 | 2008-01-13 # Chief Complaint - Muscle Pain - Fatigue - Memory Loss - Stiffness - Decreased Communication - Decreased Visual Perception - Cognitive Difficulties # History of Present Illness Azucena377 Trina350 is a 34 year-old hispanic white female. Patient has a history of dental caries on smooth surface penetrating into pulp. # Social History Patient is married. Patient has never smoked. Patient identifies as heterosexual. Patient comes from a middle socioeconomic background. Patient has completed some college courses. Patient currently has Medicaid. # Allergies No Known Allergies. # Medications No Active Medications. # Assessment and Plan Patient is presenting with prediabetes (finding). ## Plan The patient was placed on a careplan: - diabetes self management plan (record artifact)
[DocumentReference/8ac58413-19f5-2021-b01c-9380d6639c66#1] Clinical note | 2020-08-30 | part 1 of 1 | 2020-08-30 # Chief Complaint - Muscle Pain - Fatigue - Memory Loss - Stiffness - Decreased Communication - Decreased Visual Perception - Cognitive Difficulties # History of Present Illness Azucena377 Trina350 is a 46 year-old hispanic white female. Patient has a history of part-time employment (finding), medication review due (situation), dental caries on smooth surface penetrating into pulp, full-time employment (finding), victim of intimate partner abuse (finding), gingivitis (disorder), stress (finding). # Social History Patient is married. Patient has never smoked. Patient identifies as heterosexual. Patient comes from a middle socioeconomic background. Patient has completed some college courses. Patient currently has Medicaid. # Allergies No Known Allergies. # Medications No Active Medications. # Assessment and Plan ## Plan The following procedures were conducted: - removal of subcutaneous contraceptive (procedure) - implantation of subcutaneous contraceptive (procedure)
[Procedure/0eeb6aa3-c249-0e46-cf7b-6369d6b532d1] Procedure | 2021-12-05 | periodic oral evaluation  established patient | status completed | http://www.ada.org/cdt D0120
[Procedure/0eeb6aa3-c249-0e46-944e-b28fcfb85439] Procedure | 2017-11-26 | periodic oral evaluation  established patient | status completed | http://www.ada.org/cdt D0120
[Condition/0eeb6aa3-c249-0e46-b1da-92adcad53df9] Condition | onset 2011-01-16 | Stress (finding) | clinical status resolved | resolved 2026-08-09 | SNOMED 73595000
[Device/0eeb6aa3-c249-0e46-7b11-493f6cf44aba] Device | Wheelchair accessory (physical object) | status active | manufactured 2021-03-17 | SNOMED 705417005
[Condition/0eeb6aa3-c249-0e46-12d1-e61940ee084a] Condition | onset 2025-07-06 | Unemployed (finding) | clinical status resolved | resolved 2025-12-14 | SNOMED 73438004
```

</details>

label: s
note: Every condition and onset date (essential hypertension and DM2 2021-11-21, knee OA 2021-04-07, BMI 30+ obesity 2013-11-03, prediabetes 2008-01-13) matches a cited Condition card, and all are clinical status active.

## 34. `prescribed-for-essential-hypertension:8446fe54#0#0`

Question: Which medications have been prescribed for the patient's essential hypertension?

Answer: **Lisinopril 10 MG Oral Tablet is the medication prescribed with essential hypertension as the reason, with a currently active prescription dated 2025-10-03.** Earlier lisinopril 10 MG Oral Tablet prescriptions for essential hypertension, dated 2021-09-10, 2023-09-22 and 2024-09-27, have status completed. A lifestyle education care plan for hypertension, started 1997-04-25, is also active.

Cards this sentence cites:

- `[MedicationRequest/8446fe54-5b2e-6a46-88a0-c7dd9e8fc1a1]` MedicationRequest | prescribed 2025-10-03 | lisinopril 10 MG Oral Tablet | status active | reason: Essential hypertension (disorder) | RxNorm 314076

<details><summary>Everything the model saw (49 cards)</summary>

```text
[Condition/8446fe54-5b2e-6a46-c855-6376bf616037] Condition | onset 2025-10-03 | Stress (finding) | clinical status active | SNOMED 73595000
[Condition/8446fe54-5b2e-6a46-3883-408ea2da0a37] Condition | onset 2025-05-15 | Nonproliferative diabetic retinopathy due to type II diabetes mellitus | clinical status active | SNOMED 1551000119108
[Condition/8446fe54-5b2e-6a46-2283-ccf89bdfa001] Condition | onset 2024-09-27 | Medication review due (situation) | clinical status active | SNOMED 314529007
[Condition/8446fe54-5b2e-6a46-8ab7-b639a56aa55f] Condition | onset 2023-09-22 | Osteoporosis (disorder) | clinical status active | SNOMED 64859006
[Condition/8446fe54-5b2e-6a46-169f-475724b93b14] Condition | onset 2022-03-10 | History of myocardial infarction (situation) | clinical status active | SNOMED 399211009
[Condition/8446fe54-5b2e-6a46-7c5e-428350d41910] Condition | onset 2022-03-08 | Acute non-ST segment elevation myocardial infarction (disorder) | clinical status active | SNOMED 401314000
[Condition/8446fe54-5b2e-6a46-b854-dbfe1d5848d8] Condition | onset 2019-08-30 | Neuropathy due to type 2 diabetes mellitus (disorder) | clinical status active | SNOMED 368581000119106
[Condition/8446fe54-5b2e-6a46-9883-d3e4fb3c92c7] Condition | onset 2017-08-18 | Full-time employment (finding) | clinical status active | SNOMED 160903007
[Condition/8446fe54-5b2e-6a46-90ec-9d5bb7f4215c] Condition | onset 2015-08-07 | Limited social contact (finding) | clinical status active | SNOMED 423315002
[Condition/8446fe54-5b2e-6a46-ac98-749a48641300] Condition | onset 2009-07-27 | Abnormal findings diagnostic imaging heart+coronary circulat (finding) | clinical status active | SNOMED 274531002
[Condition/8446fe54-5b2e-6a46-ac45-606071904f4c] Condition | onset 2009-07-03 | Ischemic heart disease (disorder) | clinical status active | SNOMED 414545008
[Condition/8446fe54-5b2e-6a46-19e1-02a0cca64803] Condition | onset 2009-07-03 | Gingivitis (disorder) | clinical status active | SNOMED 66383009
[Condition/8446fe54-5b2e-6a46-9731-2ba07e7b3f8a] Condition | onset 2002-05-24 | Hyperlipidemia (disorder) | clinical status active | SNOMED 55822004
[Condition/8446fe54-5b2e-6a46-5645-a8fdbdfcefa0] Condition | onset 1997-04-25 | Essential hypertension (disorder) | clinical status active | SNOMED 59621000
[Condition/8446fe54-5b2e-6a46-6984-e3082708b597] Condition | onset 1997-01-20 | Localized, primary osteoarthritis of the hand (disorder) | clinical status active | SNOMED 201834006
[Condition/8446fe54-5b2e-6a46-918b-8a35802414ef] Condition | onset 1996-11-29 | Metabolic syndrome X (disorder) | clinical status active | SNOMED 237602007
[Condition/8446fe54-5b2e-6a46-8453-0b6ddcc40622] Condition | onset 1996-11-29 | Hypertriglyceridemia (disorder) | clinical status active | SNOMED 302870006
[Condition/8446fe54-5b2e-6a46-71d0-e1231acfc548] Condition | onset 1996-04-19 | Diabetes mellitus type 2 (disorder) | clinical status active | SNOMED 44054006
[Condition/8446fe54-5b2e-6a46-53e3-b8317bbea5b4] Condition | onset 1973-08-15 | Past pregnancy history of miscarriage (situation) | clinical status active | SNOMED 161744009
[Condition/8446fe54-5b2e-6a46-efe6-1830fbd69235] Condition | onset 1971-06-11 | Body mass index 30+ - obesity (finding) | clinical status active | SNOMED 162864005
[Condition/8446fe54-5b2e-6a46-a0b3-4dfcdfdaffac] Condition | onset 1965-06-04 | Anemia (disorder) | clinical status active | SNOMED 271737000
[Condition/8446fe54-5b2e-6a46-26e1-de3ad83381e7] Condition | onset 1965-06-04 | Prediabetes (finding) | clinical status active | SNOMED 714628002
[Condition/8446fe54-5b2e-6a46-3a03-f8734c3aad20] Condition | onset 1961-05-26 | Received higher education (finding) | clinical status active | SNOMED 224299000
[MedicationRequest/8446fe54-5b2e-6a46-659f-46ecea0cf5ef] MedicationRequest | prescribed 2025-10-04 | Simvastatin 10 MG Oral Tablet | status active | reason: Hyperlipidemia (disorder) | RxNorm 314231
[MedicationRequest/8446fe54-5b2e-6a46-88a0-c7dd9e8fc1a1] MedicationRequest | prescribed 2025-10-03 | lisinopril 10 MG Oral Tablet | status active | reason: Essential hypertension (disorder) | RxNorm 314076
[MedicationRequest/8446fe54-5b2e-6a46-7320-4ef7c8ad8f40] MedicationRequest | prescribed 2025-10-03 | Alendronic acid 10 MG Oral Tablet | status active | reason: Osteoporosis (disorder) | RxNorm 904419
[MedicationRequest/8446fe54-5b2e-6a46-bf69-9fef69e23979] MedicationRequest | prescribed 2022-03-10 | rosuvastatin calcium 10 MG Oral Tablet [Crestor] | status active | RxNorm 859749
[MedicationRequest/8446fe54-5b2e-6a46-4de5-bb23365c2bff] MedicationRequest | prescribed 2022-03-10 | carvedilol 25 MG Oral Tablet | status active | RxNorm 200033
[MedicationRequest/8446fe54-5b2e-6a46-49d9-f1a38344333d] MedicationRequest | prescribed 2022-03-10 | aspirin 81 MG Oral Tablet | status active | RxNorm 243670
[MedicationRequest/8446fe54-5b2e-6a46-3148-e44c765beb21] MedicationRequest | prescribed 2022-03-10 | prasugrel 10 MG Oral Tablet | status active | RxNorm 855812
[MedicationRequest/8446fe54-5b2e-6a46-2330-5a6c9a9f35f4] MedicationRequest | prescribed 2022-03-10 | losartan potassium 25 MG Oral Tablet | status active | RxNorm 979485
[MedicationRequest/8446fe54-5b2e-6a46-abfb-29ebed5ed8f5] MedicationRequest | prescribed 2009-07-10 | 24 HR metoprolol succinate 100 MG Extended Release Oral Tablet | status active | RxNorm 866412
[MedicationRequest/8446fe54-5b2e-6a46-a1b3-bc484b4b6e59] MedicationRequest | prescribed 2009-07-10 | Clopidogrel 75 MG Oral Tablet | status active | RxNorm 309362
[MedicationRequest/8446fe54-5b2e-6a46-31e7-0fab4c5ed076] MedicationRequest | prescribed 2009-07-10 | Nitroglycerin 0.4 MG/ACTUAT Mucosal Spray | status active | RxNorm 705129
[MedicationRequest/8446fe54-5b2e-6a46-2210-4b4518283f4c] MedicationRequest | prescribed 2009-07-10 | Simvastatin 20 MG Oral Tablet | status active | RxNorm 312961
[Encounter/8446fe54-5b2e-6a46-f799-ff1c9d688587] Encounter | 2026-04-10 | Ophthalmic examination and evaluation (procedure) | class AMB | at MILFORD REGIONAL MEDICAL CENTER
[Encounter/8446fe54-5b2e-6a46-7463-6a2732ff7cd0] Encounter | 2026-03-06 | Encounter for symptom (procedure) | class AMB | reason: Viral sinusitis (disorder) | at MILFORD REGIONAL MEDICAL CENTER
[Encounter/8446fe54-5b2e-6a46-f36c-8ce8c10cff85] Encounter | 2026-01-11 | Hospital admission (procedure) | class IMP | reason: Patient transfer to skilled nursing facility (procedure) | at CLAFLIN HILL CORPORATION
[Immunization/8446fe54-5b2e-6a46-dae8-760a54add250] Immunization | 2025-10-03 | Influenza, split virus, trivalent, PF | status completed | CVX 140
[MedicationRequest/8446fe54-5b2e-6a46-386f-9221c610c0f4] MedicationRequest | prescribed 2021-09-10 | lisinopril 10 MG Oral Tablet | status completed | reason: Essential hypertension (disorder) | RxNorm 314076
[MedicationRequest/8446fe54-5b2e-6a46-738a-d4c152c25a67] MedicationRequest | prescribed 2024-09-27 | lisinopril 10 MG Oral Tablet | status completed | reason: Essential hypertension (disorder) | RxNorm 314076
[MedicationRequest/8446fe54-5b2e-6a46-fbb9-e09c508bd3ef] MedicationRequest | prescribed 2023-09-22 | lisinopril 10 MG Oral Tablet | status completed | reason: Essential hypertension (disorder) | RxNorm 314076
[CarePlan/8446fe54-5b2e-6a46-a78b-87751e770c9f] CarePlan | started 1997-04-25 | Lifestyle education regarding hypertension (procedure) | status active | activities: Prescribed activity/exercise education (procedure); Counseling about alcohol consumption (procedure); Dietary Approaches to Stop Hypertension diet (regime/therapy); Smoking cessation education (procedure)
[DocumentReference/59779ffc-7e59-1b72-e992-5a4997b4b32d#2] Clinical note | 2025-10-04 | part 2 of 2 | # Assessment and Plan ## Plan The following lab reports were completed: - comprehensive metabolic 2000 panel - serum or plasma - lipid panel with direct ldl - serum or plasma The patient was prescribed the following medications: - simvastatin 10 mg oral tablet
[MedicationRequest/8446fe54-5b2e-6a46-cbe0-330eed1bd176] MedicationRequest | prescribed 2021-08-04 | status completed
[DocumentReference/28ab82c8-e34e-aee8-b559-56a6ab5c0c0e#1] Clinical note | 1997-04-25 | part 1 of 1 | 1997-04-25 # Chief Complaint - Tingling in Hands and Feet - Blurred Vision # History of Present Illness Elfrieda676 Agustina460 is a 54 year-old nonhispanic white female. # Social History Patient is married. Patient has never smoked. Patient identifies as heterosexual. Patient comes from a middle socioeconomic background. Patient has completed some college courses. Patient currently has NO INSURANCE. # Allergies No Known Allergies. # Medications naproxen sodium 220 mg oral tablet # Assessment and Plan Patient is presenting with essential hypertension (disorder). ## Plan The patient was placed on a careplan: - lifestyle education regarding hypertension (procedure)
[MedicationRequest/8446fe54-5b2e-6a46-3dfa-0a8aa3812f7d] MedicationRequest | prescribed 2018-11-18 | status completed
[MedicationRequest/8446fe54-5b2e-6a46-d1b0-886d1cae3bc3] MedicationRequest | prescribed 2022-03-08 | status completed
[MedicationRequest/8446fe54-5b2e-6a46-8d86-18f729728011] MedicationRequest | prescribed 2020-09-08 | status completed
```

</details>

label: s
note: Across all cards, the only MedicationRequests with reason Essential hypertension are lisinopril 10 MG. The cited 2025-10-03 request is status active, and the other three are completed.

## 35. `a1c-trend:530b9289#0#0`

Question: How have the patient's last three hemoglobin A1c results changed?

Answer: **The patient's hemoglobin A1c was 5.92 % on 2021-06-30, 5.9 % on 2023-02-22, and 6.07 % on 2025-02-26.** The value was essentially stable between 2021 and 2023, then rose to its highest level in the most recent result on 2025-02-26. The patient has an active prediabetes diagnosis, with onset 2005-04-20.

Cards this sentence cites:

- `[Observation/530b9289-dc96-576f-eaa7-2c1b033ef2bc]` Observation (laboratory) | 2021-06-30 | Hemoglobin A1c/Hemoglobin.total in Blood = 5.92 % | status final | LOINC 4548-4
- `[Observation/530b9289-dc96-576f-6199-9e688725841b]` Observation (laboratory) | 2023-02-22 | Hemoglobin A1c/Hemoglobin.total in Blood = 5.9 % | status final | LOINC 4548-4
- `[Observation/530b9289-dc96-576f-2b9c-5226874044a3]` Observation (laboratory) | 2025-02-26 | Hemoglobin A1c/Hemoglobin.total in Blood = 6.07 % | status final | LOINC 4548-4

<details><summary>Everything the model saw (22 cards)</summary>

```text
[Condition/530b9289-dc96-576f-f6fc-11015cce065e] Condition | onset 2025-02-26 | Part-time employment (finding) | clinical status active | SNOMED 160904001
[Condition/530b9289-dc96-576f-888a-14c459fcf894] Condition | onset 2020-05-06 | Medication review due (situation) | clinical status active | SNOMED 314529007
[Condition/530b9289-dc96-576f-1809-1246e2ec41d9] Condition | onset 2018-10-06 | History of tubal ligation (situation) | clinical status active | SNOMED 267020005
[Condition/530b9289-dc96-576f-8734-8c3a0a9992bf] Condition | onset 2017-05-03 | Body mass index 30+ - obesity (finding) | clinical status active | SNOMED 162864005
[Condition/530b9289-dc96-576f-bdaf-615dd0bc7cf7] Condition | onset 2005-04-20 | Prediabetes (finding) | clinical status active | SNOMED 714628002
[Condition/530b9289-dc96-576f-d54d-1d2b15a86dde] Condition | onset 2001-04-11 | Housing unsatisfactory (finding) | clinical status active | SNOMED 105531004
[Condition/530b9289-dc96-576f-6f01-b29a29894132] Condition | onset 2001-04-11 | Educated to high school level (finding) | clinical status active | SNOMED 473461003
[Condition/530b9289-dc96-576f-8fa7-f82a4cf5d127] Condition | onset 1996-04-03 | Chronic sinusitis (disorder) | clinical status active | SNOMED 40055000
[MedicationRequest/530b9289-dc96-576f-f948-ba67b946cdb9] MedicationRequest | prescribed 2003-11-14 | ferrous sulfate 325 MG Oral Tablet | status active | RxNorm 310325
[Encounter/530b9289-dc96-576f-fa45-0629d4ad3b09] Encounter | 2025-03-12 | Encounter for check up (procedure) | class AMB | reason: Gingivitis (disorder) | at NORTH SHORE MEDICAL CENTER INC
[Encounter/530b9289-dc96-576f-4652-29db662eb77f] Encounter | 2025-02-26 | General examination of patient (procedure) | class AMB | at SALEM FAMILY HEALTH CENTER
[Encounter/530b9289-dc96-576f-3573-1253261abd75] Encounter | 2024-01-10 | Encounter for symptom (procedure) | class AMB | reason: Viral sinusitis (disorder) | at NORTH SHORE MEDICAL CENTER INC
[Observation/530b9289-dc96-576f-6199-9e688725841b] Observation (laboratory) | 2023-02-22 | Hemoglobin A1c/Hemoglobin.total in Blood = 5.9 % | status final | LOINC 4548-4
[Observation/530b9289-dc96-576f-2b9c-5226874044a3] Observation (laboratory) | 2025-02-26 | Hemoglobin A1c/Hemoglobin.total in Blood = 6.07 % | status final | LOINC 4548-4
[Observation/530b9289-dc96-576f-eaa7-2c1b033ef2bc] Observation (laboratory) | 2021-06-30 | Hemoglobin A1c/Hemoglobin.total in Blood = 5.92 % | status final | LOINC 4548-4
[Observation/530b9289-dc96-576f-791f-13b0267dfce6] Observation (laboratory) | 2023-02-22 | Hemoglobin [Mass/volume] in Blood = 14.039 g/dL | status final | LOINC 718-7
[Observation/530b9289-dc96-576f-7c3c-99af5b2445c4] Observation (laboratory) | 2017-05-03 | Hemoglobin [Mass/volume] in Blood = 16.018 g/dL | status final | LOINC 718-7
[DiagnosticReport/530b9289-dc96-576f-9160-2d92d09aa9a2] DiagnosticReport | 2020-05-07 | Alcohol Use Disorder Identification Test - Consumption [AUDIT-C] | results: Total score [AUDIT-C] 1 {score} | LOINC 72109-2
[DiagnosticReport/530b9289-dc96-576f-c972-8fde6b371cd7] DiagnosticReport | 2025-02-27 | Alcohol Use Disorder Identification Test - Consumption [AUDIT-C] | results: Total score [AUDIT-C] 2 {score} | LOINC 72109-2
[DiagnosticReport/530b9289-dc96-576f-3d01-d7acffbfa875] DiagnosticReport | 2023-02-23 | Alcohol Use Disorder Identification Test - Consumption [AUDIT-C] | results: Total score [AUDIT-C] 1 {score} | LOINC 72109-2
[DiagnosticReport/530b9289-dc96-576f-7c87-194250f28ee4] DiagnosticReport | 2017-05-03 | CBC panel - Blood by Automated count | results: Leukocytes [#/volume] in Blood by Automated count 7.5833 10*3/uL; Erythrocytes [#/volume] in Blood by Automated count 4.165 10*6/uL; Hemoglobin [Mass/volume] in Blood 16.018 g/dL; Hematocrit [Volume Fraction] of Blood by Automated count 44.742 %; MCV [Entitic mean volume] in Red Blood Cells by Automated count 88.386 fL; MCH [Entitic mass] by Automated count 27.508 pg; MCHC [Entitic Mass/volume] in Red Blood Cells by Automated count 34.854 g/dL; Erythrocyte [DistWidth] in Blood by Automated count 45.506 fL; Platelets [#/volume] in Blood by Automated count 167.21 10*3/uL; Platelet distribution width [Entitic volume] in Blood by Automated count 343.87 fL; Platelet [Entitic mean volume] in Blood by Automated count 11.524 fL | LOINC 58410-2
[DiagnosticReport/530b9289-dc96-576f-2ab3-a7ec51c471a5] DiagnosticReport | 2023-02-22 | CBC panel - Blood by Automated count | results: Leukocytes [#/volume] in Blood by Automated count 6.6939 10*3/uL; Erythrocytes [#/volume] in Blood by Automated count 4.9191 10*6/uL; Hemoglobin [Mass/volume] in Blood 14.039 g/dL; Hematocrit [Volume Fraction] of Blood by Automated count 43.013 %; MCV [Entitic mean volume] in Red Blood Cells by Automated count 93.275 fL; MCH [Entitic mass] by Automated count 29.72 pg; MCHC [Entitic Mass/volume] in Red Blood Cells by Automated count 35.377 g/dL; Erythrocyte [DistWidth] in Blood by Automated count 45.773 fL; Platelets [#/volume] in Blood by Automated count 333.81 10*3/uL; Platelet distribution width [Entitic volume] in Blood by Automated count 480.92 fL; Platelet [Entitic mean volume] in Blood by Automated count 10.992 fL | LOINC 58410-2
```

</details>

label: s
note: The record holds exactly three HbA1c results: 5.92 % on 2021-06-30, 5.9 % on 2023-02-22 and 6.07 % on 2025-02-26. All three match the cited cards.

## 36. `prescribed-for-hyperlipidemia:8446fe54#0#0`

Question: Which medications have been prescribed for the patient's hyperlipidemia?

Answer: **Simvastatin 10 MG Oral Tablet is the medication prescribed with hyperlipidemia as the stated reason, first noted in a 2002-06-14 clinical note alongside a hyperlipidemia clinical management plan.** It was prescribed for hyperlipidemia on 2021-09-11, 2023-09-23 and 2024-10-04 (all status completed), and again on 2025-10-04, which is status active. The record also lists active prescriptions for Simvastatin 20 MG Oral Tablet (2009-07-10) and rosuvastatin calcium 10 MG Oral Tablet [Crestor] (2022-03-10), but no reason is stated for these.

Cards this sentence cites:

- `[DocumentReference/abb75d29-3fa5-fd07-94eb-c2979e943d72#1]` Clinical note | 2002-06-14 | part 1 of 1 | 2002-06-14 # Chief Complaint - Tingling in Hands and Feet - Blurred Vision # History of Present Illness Elfrieda676 Agustina460 is a 59 year-old nonhispanic white female. # Social History Patient is married. Patient has never smoked. Patient identifies as heterosexual. Patient comes from a middle socioeconomic background. Patient has completed some college courses. Patient currently has NO INSURANCE. # Allergies No Known Allergies. # Medications naproxen sodium 220 mg oral tablet # Assessment and Plan ## Plan The patient was prescribed the following medications: - simvastatin 10 mg oral tablet The patient was placed on a careplan: - hyperlipidemia clinical management plan (record artifact)
- `[CarePlan/8446fe54-5b2e-6a46-b046-cadc3fca49c8]` CarePlan | started 2002-06-14 | Hyperlipidemia clinical management plan (record artifact) | status active | activities: Low salt diet education (procedure); Physical exercises (regime/therapy)

<details><summary>Everything the model saw (49 cards)</summary>

```text
[Condition/8446fe54-5b2e-6a46-c855-6376bf616037] Condition | onset 2025-10-03 | Stress (finding) | clinical status active | SNOMED 73595000
[Condition/8446fe54-5b2e-6a46-3883-408ea2da0a37] Condition | onset 2025-05-15 | Nonproliferative diabetic retinopathy due to type II diabetes mellitus | clinical status active | SNOMED 1551000119108
[Condition/8446fe54-5b2e-6a46-2283-ccf89bdfa001] Condition | onset 2024-09-27 | Medication review due (situation) | clinical status active | SNOMED 314529007
[Condition/8446fe54-5b2e-6a46-8ab7-b639a56aa55f] Condition | onset 2023-09-22 | Osteoporosis (disorder) | clinical status active | SNOMED 64859006
[Condition/8446fe54-5b2e-6a46-169f-475724b93b14] Condition | onset 2022-03-10 | History of myocardial infarction (situation) | clinical status active | SNOMED 399211009
[Condition/8446fe54-5b2e-6a46-7c5e-428350d41910] Condition | onset 2022-03-08 | Acute non-ST segment elevation myocardial infarction (disorder) | clinical status active | SNOMED 401314000
[Condition/8446fe54-5b2e-6a46-b854-dbfe1d5848d8] Condition | onset 2019-08-30 | Neuropathy due to type 2 diabetes mellitus (disorder) | clinical status active | SNOMED 368581000119106
[Condition/8446fe54-5b2e-6a46-9883-d3e4fb3c92c7] Condition | onset 2017-08-18 | Full-time employment (finding) | clinical status active | SNOMED 160903007
[Condition/8446fe54-5b2e-6a46-90ec-9d5bb7f4215c] Condition | onset 2015-08-07 | Limited social contact (finding) | clinical status active | SNOMED 423315002
[Condition/8446fe54-5b2e-6a46-ac98-749a48641300] Condition | onset 2009-07-27 | Abnormal findings diagnostic imaging heart+coronary circulat (finding) | clinical status active | SNOMED 274531002
[Condition/8446fe54-5b2e-6a46-ac45-606071904f4c] Condition | onset 2009-07-03 | Ischemic heart disease (disorder) | clinical status active | SNOMED 414545008
[Condition/8446fe54-5b2e-6a46-19e1-02a0cca64803] Condition | onset 2009-07-03 | Gingivitis (disorder) | clinical status active | SNOMED 66383009
[Condition/8446fe54-5b2e-6a46-9731-2ba07e7b3f8a] Condition | onset 2002-05-24 | Hyperlipidemia (disorder) | clinical status active | SNOMED 55822004
[Condition/8446fe54-5b2e-6a46-5645-a8fdbdfcefa0] Condition | onset 1997-04-25 | Essential hypertension (disorder) | clinical status active | SNOMED 59621000
[Condition/8446fe54-5b2e-6a46-6984-e3082708b597] Condition | onset 1997-01-20 | Localized, primary osteoarthritis of the hand (disorder) | clinical status active | SNOMED 201834006
[Condition/8446fe54-5b2e-6a46-918b-8a35802414ef] Condition | onset 1996-11-29 | Metabolic syndrome X (disorder) | clinical status active | SNOMED 237602007
[Condition/8446fe54-5b2e-6a46-8453-0b6ddcc40622] Condition | onset 1996-11-29 | Hypertriglyceridemia (disorder) | clinical status active | SNOMED 302870006
[Condition/8446fe54-5b2e-6a46-71d0-e1231acfc548] Condition | onset 1996-04-19 | Diabetes mellitus type 2 (disorder) | clinical status active | SNOMED 44054006
[Condition/8446fe54-5b2e-6a46-53e3-b8317bbea5b4] Condition | onset 1973-08-15 | Past pregnancy history of miscarriage (situation) | clinical status active | SNOMED 161744009
[Condition/8446fe54-5b2e-6a46-efe6-1830fbd69235] Condition | onset 1971-06-11 | Body mass index 30+ - obesity (finding) | clinical status active | SNOMED 162864005
[Condition/8446fe54-5b2e-6a46-a0b3-4dfcdfdaffac] Condition | onset 1965-06-04 | Anemia (disorder) | clinical status active | SNOMED 271737000
[Condition/8446fe54-5b2e-6a46-26e1-de3ad83381e7] Condition | onset 1965-06-04 | Prediabetes (finding) | clinical status active | SNOMED 714628002
[Condition/8446fe54-5b2e-6a46-3a03-f8734c3aad20] Condition | onset 1961-05-26 | Received higher education (finding) | clinical status active | SNOMED 224299000
[MedicationRequest/8446fe54-5b2e-6a46-659f-46ecea0cf5ef] MedicationRequest | prescribed 2025-10-04 | Simvastatin 10 MG Oral Tablet | status active | reason: Hyperlipidemia (disorder) | RxNorm 314231
[MedicationRequest/8446fe54-5b2e-6a46-88a0-c7dd9e8fc1a1] MedicationRequest | prescribed 2025-10-03 | lisinopril 10 MG Oral Tablet | status active | reason: Essential hypertension (disorder) | RxNorm 314076
[MedicationRequest/8446fe54-5b2e-6a46-7320-4ef7c8ad8f40] MedicationRequest | prescribed 2025-10-03 | Alendronic acid 10 MG Oral Tablet | status active | reason: Osteoporosis (disorder) | RxNorm 904419
[MedicationRequest/8446fe54-5b2e-6a46-bf69-9fef69e23979] MedicationRequest | prescribed 2022-03-10 | rosuvastatin calcium 10 MG Oral Tablet [Crestor] | status active | RxNorm 859749
[MedicationRequest/8446fe54-5b2e-6a46-4de5-bb23365c2bff] MedicationRequest | prescribed 2022-03-10 | carvedilol 25 MG Oral Tablet | status active | RxNorm 200033
[MedicationRequest/8446fe54-5b2e-6a46-49d9-f1a38344333d] MedicationRequest | prescribed 2022-03-10 | aspirin 81 MG Oral Tablet | status active | RxNorm 243670
[MedicationRequest/8446fe54-5b2e-6a46-3148-e44c765beb21] MedicationRequest | prescribed 2022-03-10 | prasugrel 10 MG Oral Tablet | status active | RxNorm 855812
[MedicationRequest/8446fe54-5b2e-6a46-2330-5a6c9a9f35f4] MedicationRequest | prescribed 2022-03-10 | losartan potassium 25 MG Oral Tablet | status active | RxNorm 979485
[MedicationRequest/8446fe54-5b2e-6a46-abfb-29ebed5ed8f5] MedicationRequest | prescribed 2009-07-10 | 24 HR metoprolol succinate 100 MG Extended Release Oral Tablet | status active | RxNorm 866412
[MedicationRequest/8446fe54-5b2e-6a46-a1b3-bc484b4b6e59] MedicationRequest | prescribed 2009-07-10 | Clopidogrel 75 MG Oral Tablet | status active | RxNorm 309362
[MedicationRequest/8446fe54-5b2e-6a46-31e7-0fab4c5ed076] MedicationRequest | prescribed 2009-07-10 | Nitroglycerin 0.4 MG/ACTUAT Mucosal Spray | status active | RxNorm 705129
[MedicationRequest/8446fe54-5b2e-6a46-2210-4b4518283f4c] MedicationRequest | prescribed 2009-07-10 | Simvastatin 20 MG Oral Tablet | status active | RxNorm 312961
[Encounter/8446fe54-5b2e-6a46-f799-ff1c9d688587] Encounter | 2026-04-10 | Ophthalmic examination and evaluation (procedure) | class AMB | at MILFORD REGIONAL MEDICAL CENTER
[Encounter/8446fe54-5b2e-6a46-7463-6a2732ff7cd0] Encounter | 2026-03-06 | Encounter for symptom (procedure) | class AMB | reason: Viral sinusitis (disorder) | at MILFORD REGIONAL MEDICAL CENTER
[Encounter/8446fe54-5b2e-6a46-f36c-8ce8c10cff85] Encounter | 2026-01-11 | Hospital admission (procedure) | class IMP | reason: Patient transfer to skilled nursing facility (procedure) | at CLAFLIN HILL CORPORATION
[Immunization/8446fe54-5b2e-6a46-dae8-760a54add250] Immunization | 2025-10-03 | Influenza, split virus, trivalent, PF | status completed | CVX 140
[MedicationRequest/8446fe54-5b2e-6a46-b539-a391b5db365e] MedicationRequest | prescribed 2021-09-11 | Simvastatin 10 MG Oral Tablet | status completed | reason: Hyperlipidemia (disorder) | RxNorm 314231
[MedicationRequest/8446fe54-5b2e-6a46-d564-ed70bd7f8bcb] MedicationRequest | prescribed 2024-10-04 | Simvastatin 10 MG Oral Tablet | status completed | reason: Hyperlipidemia (disorder) | RxNorm 314231
[MedicationRequest/8446fe54-5b2e-6a46-ef39-55f150579ba6] MedicationRequest | prescribed 2023-09-23 | Simvastatin 10 MG Oral Tablet | status completed | reason: Hyperlipidemia (disorder) | RxNorm 314231
[DocumentReference/59779ffc-7e59-1b72-e992-5a4997b4b32d#2] Clinical note | 2025-10-04 | part 2 of 2 | # Assessment and Plan ## Plan The following lab reports were completed: - comprehensive metabolic 2000 panel - serum or plasma - lipid panel with direct ldl - serum or plasma The patient was prescribed the following medications: - simvastatin 10 mg oral tablet
[DocumentReference/abb75d29-3fa5-fd07-94eb-c2979e943d72#1] Clinical note | 2002-06-14 | part 1 of 1 | 2002-06-14 # Chief Complaint - Tingling in Hands and Feet - Blurred Vision # History of Present Illness Elfrieda676 Agustina460 is a 59 year-old nonhispanic white female. # Social History Patient is married. Patient has never smoked. Patient identifies as heterosexual. Patient comes from a middle socioeconomic background. Patient has completed some college courses. Patient currently has NO INSURANCE. # Allergies No Known Allergies. # Medications naproxen sodium 220 mg oral tablet # Assessment and Plan ## Plan The patient was prescribed the following medications: - simvastatin 10 mg oral tablet The patient was placed on a careplan: - hyperlipidemia clinical management plan (record artifact)
[Encounter/8446fe54-5b2e-6a46-b32c-b2a513e6d00e] Encounter | 2020-09-11 | Follow-up encounter (procedure) | class AMB | reason: Hyperlipidemia (disorder) | at MILFORD REGIONAL MEDICAL CENTER
[Encounter/8446fe54-5b2e-6a46-d8cd-08457feac47b] Encounter | 2021-09-11 | Follow-up encounter (procedure) | class AMB | reason: Hyperlipidemia (disorder) | at MILFORD REGIONAL MEDICAL CENTER
[Encounter/8446fe54-5b2e-6a46-575d-cbe9e384554d] Encounter | 2025-10-04 | Follow-up encounter (procedure) | class AMB | reason: Hyperlipidemia (disorder) | at MILFORD REGIONAL MEDICAL CENTER
[Encounter/8446fe54-5b2e-6a46-9035-250e11565743] Encounter | 2024-10-04 | Follow-up encounter (procedure) | class AMB | reason: Hyperlipidemia (disorder) | at MILFORD REGIONAL MEDICAL CENTER
[CarePlan/8446fe54-5b2e-6a46-b046-cadc3fca49c8] CarePlan | started 2002-06-14 | Hyperlipidemia clinical management plan (record artifact) | status active | activities: Low salt diet education (procedure); Physical exercises (regime/therapy)
```

</details>

label: p?
note: The cited 2002-06-14 note (earliest simvastatin mention) shows simvastatin 10 mg prescribed together with the hyperlipidemia management plan, and across the whole record it is the only drug with reason Hyperlipidemia. However, the 'stated reason' only appears in uncited MedicationRequest cards, since neither cited card states a reason.

## 37. `lay-a-sinus-infection:e56a8cde#0#0`

Question: Has the patient ever been diagnosed with a sinus infection? If so, when?

Answer: **Yes, the patient has been diagnosed with viral sinusitis on two occasions.** The first episode had onset 2017-12-07 at a symptom encounter at DANA FARBER CANCER INSTITUTE and resolved 2018-01-02. The second episode had onset 2020-03-01, was treated with amoxicillin 250 mg / clavulanate 125 mg oral tablet, and resolved 2020-03-18.

Cards this sentence cites:

- `[Condition/e56a8cde-8395-a37d-448b-343ff0888a14]` Condition | onset 2017-12-07 | Viral sinusitis (disorder) | clinical status resolved | resolved 2018-01-02 | SNOMED 444814009
- `[Condition/e56a8cde-8395-a37d-f660-3a080ceb9c43]` Condition | onset 2020-03-01 | Viral sinusitis (disorder) | clinical status resolved | resolved 2020-03-18 | SNOMED 444814009

<details><summary>Everything the model saw (56 cards)</summary>

```text
[Condition/e56a8cde-8395-a37d-f7ae-15d35f13e9f0] Condition | onset 2025-12-25 | Victim of intimate partner abuse (finding) | clinical status active | SNOMED 706893006
[Condition/e56a8cde-8395-a37d-80d3-3984f14d8bb3] Condition | onset 2025-12-25 | Stress (finding) | clinical status active | SNOMED 73595000
[Condition/e56a8cde-8395-a37d-5c7c-75429c6f1e56] Condition | onset 2025-12-25 | Medication review due (situation) | clinical status active | SNOMED 314529007
[Condition/e56a8cde-8395-a37d-354e-df92238c35a7] Condition | onset 2025-12-25 | Unemployed (finding) | clinical status active | SNOMED 73438004
[Condition/e56a8cde-8395-a37d-6690-7ef5746552bd] Condition | onset 2017-11-09 | Hyperlipidemia (disorder) | clinical status active | SNOMED 55822004
[Condition/e56a8cde-8395-a37d-922a-d32061194c0b] Condition | onset 2016-11-03 | Gingivitis (disorder) | clinical status active | SNOMED 66383009
[Condition/e56a8cde-8395-a37d-e775-23849ffbe97b] Condition | onset 2014-02-01 | Chronic low back pain (finding) | clinical status active | SNOMED 278860009
[Condition/e56a8cde-8395-a37d-a82c-6129bc784139] Condition | onset 2014-02-01 | Chronic pain (finding) | clinical status active | SNOMED 82423001
[Condition/e56a8cde-8395-a37d-64b8-86023f198a46] Condition | onset 2014-02-01 | Chronic neck pain (finding) | clinical status active | SNOMED 1121000119107
[Condition/e56a8cde-8395-a37d-e547-8e085bacfa8e] Condition | onset 2007-09-13 | Has a criminal record (finding) | clinical status active | SNOMED 266948004
[Condition/e56a8cde-8395-a37d-37b4-500cf9e797e9] Condition | onset 2005-09-01 | Osteoporosis (disorder) | clinical status active | SNOMED 64859006
[Condition/e56a8cde-8395-a37d-d5cb-6239a28a0055] Condition | onset 2003-12-16 | History of myocardial infarction (situation) | clinical status active | SNOMED 399211009
[Condition/e56a8cde-8395-a37d-4d5f-670d3e1632bc] Condition | onset 2003-12-16 | Acute non-ST segment elevation myocardial infarction (disorder) | clinical status active | SNOMED 401314000
[Condition/e56a8cde-8395-a37d-1853-568436ee1ea2] Condition | onset 2001-08-20 | History of coronary artery bypass grafting (situation) | clinical status active | SNOMED 399261000
[Condition/e56a8cde-8395-a37d-810b-643d651149ba] Condition | onset 2001-08-18 | Abnormal findings diagnostic imaging heart+coronary circulat (finding) | clinical status active | SNOMED 274531002
[Condition/e56a8cde-8395-a37d-2761-7d0bfc799087] Condition | onset 2001-08-09 | Ischemic heart disease (disorder) | clinical status active | SNOMED 414545008
[Condition/e56a8cde-8395-a37d-ed31-c4144dbefb9e] Condition | onset 1996-05-17 | Osteoarthritis of knee (disorder) | clinical status active | SNOMED 239873007
[Condition/e56a8cde-8395-a37d-333f-0835bee4de98] Condition | onset 1991-06-13 | Essential hypertension (disorder) | clinical status active | SNOMED 59621000
[Condition/e56a8cde-8395-a37d-30cd-5f4f9de67da3] Condition | onset 1967-07-27 | Lack of access to transportation (finding) | clinical status active | SNOMED 713458007
[Condition/e56a8cde-8395-a37d-ac70-0b466edf16a1] Condition | onset 1963-07-18 | Transport problem (finding) | clinical status active | SNOMED 266934004
[Condition/e56a8cde-8395-a37d-99e6-93fe1e3f6036] Condition | onset 1963-07-18 | Only received primary school education (finding) | clinical status active | SNOMED 224295006
[MedicationRequest/e56a8cde-8395-a37d-0c1b-7da0b396a0c4] MedicationRequest | prescribed 2026-01-01 | Simvastatin 10 MG Oral Tablet | status active | reason: Hyperlipidemia (disorder) | RxNorm 314231
[MedicationRequest/e56a8cde-8395-a37d-f153-06ed5ef5b40a] MedicationRequest | prescribed 2025-12-25 | Alendronic acid 10 MG Oral Tablet | status active | reason: Osteoporosis (disorder) | RxNorm 904419
[MedicationRequest/e56a8cde-8395-a37d-b70b-d6ff9e66fb91] MedicationRequest | prescribed 2025-12-25 | Acetaminophen 325 MG Oral Tablet [Tylenol] | status active | RxNorm 209387
[MedicationRequest/e56a8cde-8395-a37d-1cff-386c29158923] MedicationRequest | prescribed 2025-12-25 | lisinopril 10 MG Oral Tablet | status active | reason: Essential hypertension (disorder) | RxNorm 314076
[MedicationRequest/e56a8cde-8395-a37d-f778-f1044e9a8316] MedicationRequest | prescribed 2003-12-16 | atorvastatin 10 MG Oral Tablet | status active | RxNorm 617312
[MedicationRequest/e56a8cde-8395-a37d-e36e-ab680e0ad841] MedicationRequest | prescribed 2003-12-16 | hydrochlorothiazide 25 MG / lisinopril 20 MG Oral Tablet | status active | RxNorm 197887
[MedicationRequest/e56a8cde-8395-a37d-d237-6e376bbcb9a6] MedicationRequest | prescribed 2003-12-16 | metoprolol tartrate 25 MG Oral Tablet | status active | RxNorm 866924
[MedicationRequest/e56a8cde-8395-a37d-2fb4-edeac8b69b00] MedicationRequest | prescribed 2003-12-16 | prasugrel 10 MG Oral Tablet | status active | RxNorm 855812
[MedicationRequest/e56a8cde-8395-a37d-228f-f6135c165caa] MedicationRequest | prescribed 2003-12-16 | aspirin 81 MG Oral Tablet | status active | RxNorm 243670
[MedicationRequest/e56a8cde-8395-a37d-eee1-8d05287f0e29] MedicationRequest | prescribed 2001-08-16 | Nitroglycerin 0.4 MG/ACTUAT Mucosal Spray | status active | RxNorm 705129
[MedicationRequest/e56a8cde-8395-a37d-d36b-2e3fc9df975e] MedicationRequest | prescribed 2001-08-16 | 24 HR metoprolol succinate 100 MG Extended Release Oral Tablet | status active | RxNorm 866412
[MedicationRequest/e56a8cde-8395-a37d-a8c0-f9ed9ed3ea83] MedicationRequest | prescribed 2001-08-16 | Clopidogrel 75 MG Oral Tablet | status active | RxNorm 309362
[MedicationRequest/e56a8cde-8395-a37d-321f-ecd1d25263ad] MedicationRequest | prescribed 2001-08-16 | Simvastatin 20 MG Oral Tablet | status active | RxNorm 312961
[MedicationRequest/e56a8cde-8395-a37d-9456-c58ec0c7de32] MedicationRequest | prescribed 1949-01-17 | diphenhydrAMINE Hydrochloride 25 MG Oral Tablet | status active | RxNorm 1049630
[AllergyIntolerance/e56a8cde-8395-a37d-b318-8f34a7d6b5f7] AllergyIntolerance | recorded 1946-06-09 | Animal dander (substance) | allergy, category environment, criticality low | clinical status active | reactions: Eruption of skin (disorder); Rhinoconjunctivitis (disorder) | SNOMED 264287008
[AllergyIntolerance/e56a8cde-8395-a37d-a098-9831a40ac85b] AllergyIntolerance | recorded 1946-06-09 | Mold (organism) | allergy, category environment, criticality low | clinical status active | SNOMED 84489001
[AllergyIntolerance/e56a8cde-8395-a37d-85d4-fe7519012219] AllergyIntolerance | recorded 1946-06-09 | House dust mite (organism) | allergy, category environment, criticality low | clinical status active | SNOMED 260147004
[AllergyIntolerance/e56a8cde-8395-a37d-60c2-b75e4a4d4513] AllergyIntolerance | recorded 1946-06-09 | Tree pollen (substance) | allergy, category environment, criticality low | clinical status active | SNOMED 782576004
[AllergyIntolerance/e56a8cde-8395-a37d-5834-224d1127b6f9] AllergyIntolerance | recorded 1946-06-09 | Grass pollen (substance) | allergy, category environment, criticality low | clinical status active | SNOMED 256277009
[AllergyIntolerance/e56a8cde-8395-a37d-2daa-dbe0dbcf6ecf] AllergyIntolerance | recorded 1946-06-09 | Shellfish (substance) | allergy, category food, criticality low | clinical status active | reactions: Dyspnea (finding); Allergic angioedema (disorder); Itching (finding); Cough (finding); Diarrhea (finding) | SNOMED 735029006
[AllergyIntolerance/e56a8cde-8395-a37d-1508-bdb84bdc4c5d] AllergyIntolerance | recorded 1946-06-09 | Allergic disposition (finding) | allergy, category environment, criticality low | clinical status active | SNOMED 609328004
[Encounter/e56a8cde-8395-a37d-9f47-5b69723a8690] Encounter | 2026-01-01 | Follow-up encounter (procedure) | class AMB | reason: Hyperlipidemia (disorder) | at DANA FARBER CANCER INSTITUTE
[Encounter/e56a8cde-8395-a37d-2450-250d53d64dc7] Encounter | 2025-12-25 | General examination of patient (procedure) | class AMB | at SOUTH SHORE PRIMARY CARE PC
[Encounter/e56a8cde-8395-a37d-20eb-f707e34a4164] Encounter | 2024-12-20 | Follow-up encounter (procedure) | class AMB | reason: Hyperlipidemia (disorder) | at DANA FARBER CANCER INSTITUTE
[Immunization/e56a8cde-8395-a37d-7cd1-bb3bac5572f3] Immunization | 2025-12-25 | Influenza, split virus, trivalent, PF | status completed | CVX 140
[Condition/e56a8cde-8395-a37d-f660-3a080ceb9c43] Condition | onset 2020-03-01 | Viral sinusitis (disorder) | clinical status resolved | resolved 2020-03-18 | SNOMED 444814009
[Condition/e56a8cde-8395-a37d-448b-343ff0888a14] Condition | onset 2017-12-07 | Viral sinusitis (disorder) | clinical status resolved | resolved 2018-01-02 | SNOMED 444814009
[DocumentReference/53edf378-3bfc-fc8b-b070-0e0daf1e78f5#1] Clinical note | 2018-11-29 | part 1 of 1 | 2018-11-29 # Chief Complaint - Memory Loss - Decreased Communication - Decreased Visual Perception - Confusion - Decreased in Judgement # History of Present Illness Roosevelt595 is a 73 year-old nonhispanic white male. Patient has a history of severe anxiety (panic) (finding), sprain (morphologic abnormality), medication review due (situation), full-time employment (finding), sprain of wrist (disorder), viral sinusitis (disorder), stress (finding). # Social History Patient is married. Patient has never smoked. Patient identifies as heterosexual. Patient comes from a middle socioeconomic background. Patient did not finish high school. Patient currently has Medicare. # Allergies No Known Allergies. # Medications lisinopril 10 mg oral tablet; acetaminophen 325 mg oral tablet; simvastatin 10 mg oral tablet; acetaminophen 325 mg oral tablet [tylenol]; alendronic acid 10 mg oral tablet # Assessment and Plan ## Plan The following procedures were conducted: - extraction, erupted tooth or exposed root (elevation and/or forceps removal)
[Encounter/e56a8cde-8395-a37d-a174-6f2b8b9d9601] Encounter | 2020-03-01 | Encounter for symptom (procedure) | class AMB | reason: Viral sinusitis (disorder) | at DANA FARBER CANCER INSTITUTE
[DocumentReference/42753ae1-81eb-b0aa-5a3b-e0a9b39507dc#1] Clinical note | 2020-03-01 | part 1 of 1 | 2020-03-01 # Chief Complaint - Memory Loss - Decreased Communication - Decreased Visual Perception - Confusion - Decreased in Judgement # History of Present Illness Roosevelt595 is a 74 year-old nonhispanic white male. Patient has a history of severe anxiety (panic) (finding), sprain (morphologic abnormality), medication review due (situation), unhealthy alcohol drinking behavior (finding), full-time employment (finding), sprain of wrist (disorder), viral sinusitis (disorder), stress (finding). # Social History Patient is married. Patient has never smoked. Patient identifies as heterosexual. Patient comes from a middle socioeconomic background. Patient did not finish high school. Patient currently has Medicare. # Allergies No Known Allergies. # Medications lisinopril 10 mg oral tablet; acetaminophen 325 mg oral tablet; simvastatin 10 mg oral tablet; acetaminophen 325 mg oral tablet [tylenol]; alendronic acid 10 mg oral tablet # Assessment and Plan Patient is presenting with viral sinusitis (disorder). ## Plan The patient was prescribed the following medications: - amoxicillin 250 mg / clavulanate 125 mg oral tablet
[DocumentReference/e9da819c-9abe-a548-8fa2-b345f1f0bd0f#1] Clinical note | 2017-12-07 | part 1 of 1 | 2017-12-07 # Chief Complaint - Memory Loss - Decreased Communication - Decreased Visual Perception - Confusion - Decreased in Judgement # History of Present Illness Roosevelt595 is a 72 year-old nonhispanic white male. Patient has a history of severe anxiety (panic) (finding), sprain (morphologic abnormality), medication review due (situation), full-time employment (finding), sprain of wrist (disorder), stress (finding). # Social History Patient is married. Patient has never smoked. Patient identifies as heterosexual. Patient comes from a middle socioeconomic background. Patient did not finish high school. Patient currently has Medicare. # Allergies No Known Allergies. # Medications lisinopril 10 mg oral tablet; acetaminophen 325 mg oral tablet; simvastatin 10 mg oral tablet; acetaminophen 325 mg oral tablet [tylenol]; alendronic acid 10 mg oral tablet # Assessment and Plan Patient is presenting with viral sinusitis (disorder). ## Plan
[DocumentReference/a1179c6e-edc7-a264-ebd1-2d2d22f5e3f1#1] Clinical note | 2021-02-18 | part 1 of 1 | 2021-02-18 # Chief Complaint - Memory Loss - Decreased Communication - Decreased Visual Perception - Confusion - Decreased in Judgement # History of Present Illness Roosevelt595 is a 75 year-old nonhispanic white male. Patient has a history of severe anxiety (panic) (finding), sprain (morphologic abnormality), medication review due (situation), unhealthy alcohol drinking behavior (finding), full-time employment (finding), sprain of wrist (disorder), viral sinusitis (disorder), stress (finding). # Social History Patient is married. Patient has never smoked. Patient identifies as heterosexual. Patient comes from a middle socioeconomic background. Patient did not finish high school. Patient currently has Medicare. # Allergies No Known Allergies. # Medications lisinopril 10 mg oral tablet; acetaminophen 325 mg oral tablet; simvastatin 10 mg oral tablet; acetaminophen 325 mg oral tablet [tylenol]; alendronic acid 10 mg oral tablet; amoxicillin 250 mg / clavulanate 125 mg oral tablet # Assessment and Plan Patient is presenting with acute infective cystitis (disorder). ## Plan Patient was given the following immunizations: covid-19, mrna, lnp-s, pf, 100 mcg/0.5ml dose or 50 mcg/0.25ml dose.
[DocumentReference/b3013519-3000-7f68-7b32-de706218460e#1] Clinical note | 2018-11-15 | part 1 of 2 | 2018-11-15 # Chief Complaint - Memory Loss - Decreased Communication - Decreased Visual Perception - Confusion - Decreased in Judgement # History of Present Illness Roosevelt595 is a 73 year-old nonhispanic white male. Patient has a history of severe anxiety (panic) (finding), sprain (morphologic abnormality), medication review due (situation), full-time employment (finding), sprain of wrist (disorder), viral sinusitis (disorder), stress (finding). # Social History Patient is married. Patient has never smoked. Patient identifies as heterosexual. Patient comes from a middle socioeconomic background. Patient did not finish high school. Patient currently has Medicare. # Allergies No Known Allergies. # Medications lisinopril 10 mg oral tablet; acetaminophen 325 mg oral tablet; simvastatin 10 mg oral tablet; acetaminophen 325 mg oral tablet [tylenol]; alendronic acid 10 mg oral tablet
[Encounter/e56a8cde-8395-a37d-7593-7148468dba47] Encounter | 2017-12-07 | Encounter for symptom (procedure) | class AMB | reason: Viral sinusitis (disorder) | at DANA FARBER CANCER INSTITUTE
[DocumentReference/54e6f2f3-53b3-4254-8474-3e83b705f0b8#1] Clinical note | 2019-11-21 | part 1 of 2 | 2019-11-21 # Chief Complaint - Memory Loss - Decreased Communication - Decreased Visual Perception - Confusion - Decreased in Judgement # History of Present Illness Roosevelt595 is a 74 year-old nonhispanic white male. Patient has a history of severe anxiety (panic) (finding), sprain (morphologic abnormality), medication review due (situation), full-time employment (finding), sprain of wrist (disorder), viral sinusitis (disorder), stress (finding). # Social History Patient is married. Patient has never smoked. Patient identifies as heterosexual. Patient comes from a middle socioeconomic background. Patient did not finish high school. Patient currently has Medicare. # Allergies No Known Allergies. # Medications lisinopril 10 mg oral tablet; acetaminophen 325 mg oral tablet; simvastatin 10 mg oral tablet; acetaminophen 325 mg oral tablet [tylenol]; alendronic acid 10 mg oral tablet
```

</details>

label: s
note: The record has exactly two viral sinusitis Condition cards (onset 2017-12-07 and 2020-03-01), both cited, and no other sinusitis diagnosis, so 'two occasions' holds.

## 38. `last-flu-shot:7280f7f8#0#1`

Question: When did the patient last get a flu shot?

Answer: The patient's most recent flu shot was on 2026-04-12 (Influenza, split virus, trivalent, PF; status completed). **Earlier flu shots were given on 2024-11-24, 2024-03-31, and 2023-03-26.**

Cards this sentence cites:

- `[Immunization/7280f7f8-315d-7c6a-a994-7340336c5a95]` Immunization | 2024-11-24 | Influenza, split virus, trivalent, PF | status completed | CVX 140
- `[Immunization/7280f7f8-315d-7c6a-5206-3912d1550e2d]` Immunization | 2024-03-31 | Influenza, split virus, trivalent, PF | status completed | CVX 140
- `[Immunization/7280f7f8-315d-7c6a-2836-354c2b85cb88]` Immunization | 2023-03-26 | Influenza, split virus, trivalent, PF | status completed | CVX 140

<details><summary>Everything the model saw (43 cards)</summary>

```text
[Condition/7280f7f8-315d-7c6a-5183-1fc53612d856] Condition | onset 2026-04-12 | Alzheimer's disease (disorder) | clinical status active | SNOMED 26929004
[Condition/7280f7f8-315d-7c6a-069f-25fdb34e3e53] Condition | onset 2025-04-06 | Stress (finding) | clinical status active | SNOMED 73595000
[Condition/7280f7f8-315d-7c6a-06ae-a26712c6cfb7] Condition | onset 2024-03-31 | Full-time employment (finding) | clinical status active | SNOMED 160903007
[Condition/7280f7f8-315d-7c6a-84b2-d6045a9b8deb] Condition | onset 2018-11-12 | Abnormal findings diagnostic imaging heart+coronary circulat (finding) | clinical status active | SNOMED 274531002
[Condition/7280f7f8-315d-7c6a-60b8-1b2b3b190d66] Condition | onset 2018-11-04 | Ischemic heart disease (disorder) | clinical status active | SNOMED 414545008
[Condition/7280f7f8-315d-7c6a-eee1-33d3eda16b26] Condition | onset 2014-02-16 | Chronic low back pain (finding) | clinical status active | SNOMED 278860009
[Condition/7280f7f8-315d-7c6a-23b9-2a24d0c43093] Condition | onset 2014-02-16 | Chronic neck pain (finding) | clinical status active | SNOMED 1121000119107
[Condition/7280f7f8-315d-7c6a-f371-666500850eb4] Condition | onset 2014-02-02 | Gingivitis (disorder) | clinical status active | SNOMED 66383009
[Condition/7280f7f8-315d-7c6a-b5ea-aa0955ebc2c7] Condition | onset 2010-01-10 | Hyperlipidemia (disorder) | clinical status active | SNOMED 55822004
[Condition/7280f7f8-315d-7c6a-929f-e845c91bba18] Condition | onset 1993-02-06 | Dependent drug abuse (disorder) | clinical status active | SNOMED 6525002
[Condition/7280f7f8-315d-7c6a-6159-244929402415] Condition | onset 1991-07-09 | Chronic pain (finding) | clinical status active | SNOMED 82423001
[Condition/7280f7f8-315d-7c6a-7561-551dd4fb980c] Condition | onset 1990-11-11 | Has a criminal record (finding) | clinical status active | SNOMED 266948004
[Condition/7280f7f8-315d-7c6a-69cb-9f6bde195716] Condition | onset 1990-10-25 | Impacted molars (disorder) | clinical status active | SNOMED 196416002
[Condition/7280f7f8-315d-7c6a-e183-7fc41f06abde] Condition | onset 1990-02-06 | Chronic intractable migraine without aura (disorder) | clinical status active | SNOMED 124171000119105
[Condition/7280f7f8-315d-7c6a-57cd-16215a141add] Condition | onset 1988-11-06 | Body mass index 30+ - obesity (finding) | clinical status active | SNOMED 162864005
[Condition/7280f7f8-315d-7c6a-7c25-7a247f43e721] Condition | onset 1981-01-18 | Anemia (disorder) | clinical status active | SNOMED 271737000
[Condition/7280f7f8-315d-7c6a-50ac-70390520f5d8] Condition | onset 1981-01-18 | Prediabetes (finding) | clinical status active | SNOMED 714628002
[Condition/7280f7f8-315d-7c6a-a35c-5f2c4404e1cd] Condition | onset 1971-02-18 | Chronic sinusitis (disorder) | clinical status active | SNOMED 40055000
[Condition/7280f7f8-315d-7c6a-cf3c-1559c1e270a8] Condition | onset 1964-12-20 | Housing unsatisfactory (finding) | clinical status active | SNOMED 105531004
[Condition/7280f7f8-315d-7c6a-3735-89103641aea2] Condition | onset 1964-12-20 | Only received primary school education (finding) | clinical status active | SNOMED 224295006
[MedicationRequest/7280f7f8-315d-7c6a-d103-5f5cf25ace53] MedicationRequest | prescribed 2026-04-13 | Simvastatin 10 MG Oral Tablet | status active | reason: Hyperlipidemia (disorder) | RxNorm 314231
[MedicationRequest/7280f7f8-315d-7c6a-dd3c-435b565b36d4] MedicationRequest | prescribed 2026-04-12 | Ibuprofen 400 MG Oral Tablet [Ibu] | status active | RxNorm 206905
[MedicationRequest/7280f7f8-315d-7c6a-698d-8c3f4a330263] MedicationRequest | prescribed 2026-04-12 | Acetaminophen 325 MG / Oxycodone Hydrochloride 10 MG Oral Tablet [Percocet] | status active | RxNorm 1049625
[MedicationRequest/7280f7f8-315d-7c6a-53dc-677516ba315e] MedicationRequest | prescribed 2026-04-12 | Galantamine 4 MG Oral Tablet | status active | reason: Alzheimer's disease (disorder) | RxNorm 310436
[MedicationRequest/7280f7f8-315d-7c6a-21fd-127361ce4eae] MedicationRequest | prescribed 2026-04-12 | Acetaminophen 325 MG Oral Tablet [Tylenol] | status active | RxNorm 209387
[MedicationRequest/7280f7f8-315d-7c6a-e1ca-6672a64e96d6] MedicationRequest | prescribed 2018-11-11 | Simvastatin 20 MG Oral Tablet | status active | RxNorm 312961
[MedicationRequest/7280f7f8-315d-7c6a-d3dc-bf227b26b9de] MedicationRequest | prescribed 2018-11-11 | Nitroglycerin 0.4 MG/ACTUAT Mucosal Spray | status active | RxNorm 705129
[MedicationRequest/7280f7f8-315d-7c6a-40f0-094ac0d35606] MedicationRequest | prescribed 2018-11-11 | Clopidogrel 75 MG Oral Tablet | status active | RxNorm 309362
[MedicationRequest/7280f7f8-315d-7c6a-344e-7b21fe48818f] MedicationRequest | prescribed 2018-11-11 | 24 HR metoprolol succinate 100 MG Extended Release Oral Tablet | status active | RxNorm 866412
[Encounter/7280f7f8-315d-7c6a-ddbc-56619e72a429] Encounter | 2026-04-26 | Encounter for check up (procedure) | class AMB | at LAWRENCE GENERAL HOSPITAL
[Encounter/7280f7f8-315d-7c6a-e49f-7858d34e1916] Encounter | 2026-04-13 | Follow-up encounter (procedure) | class AMB | reason: Hyperlipidemia (disorder) | at LAWRENCE GENERAL HOSPITAL
[Encounter/7280f7f8-315d-7c6a-79c7-b2135168eae6] Encounter | 2026-04-12 | General examination of patient (procedure) | class AMB | at HOLY FAMILY MEDICAL SPECIALTY PRACTICE PLLC
[Immunization/7280f7f8-315d-7c6a-89f5-f28321d6dbe8] Immunization | 2026-04-12 | Influenza, split virus, trivalent, PF | status completed | CVX 140
[Observation/7280f7f8-315d-7c6a-2d11-a7126032c00a] Observation (laboratory) | 2020-12-21 | Influenza virus B Ag [Presence] in Upper respiratory specimen by Rapid immunoassay = Not detected (qualifier value) | status final | LOINC 80383-3
[Observation/7280f7f8-315d-7c6a-3bcf-660371c4df20] Observation (survey) | 2024-03-31 | Protocol for Responding to and Assessing Patients' Assets, Risks, and Experiences [PRAPARE] = Within the last year, have you been afraid of your partner or ex-partner No; Do you feel physically and emotionally safe where you currently live [PRAPARE] Yes; Are you a refugee No; Have you spent more than 2 nights in a row in a jail, prison, detention center, or juvenile correctional facility in past 1 year [PRAPARE] Yes; Stress level Somewhat; How often do you see or talk to people that you care about and feel close to [PRAPARE] 5 or more times a week; Has lack of transportation kept you from medical appointments, meetings, work, or from getting things needed for daily living No; Have you or any family members you live with been unable to get any of the following when it was really needed in past 1 year [PRAPARE] Food; What was your best estimate of the total income of all family members from all sources, before taxes, in last year [PhenX] 41074 /a; Primary insurance Medicare; Employment status - current Full-time work; Highest level of education Less than high school degree; Address 702 Parisian Flat; Are you worried about losing your housing [PRAPARE] Yes; Housing status I have housing; How many people are living or staying at this address [#] 8 {#}; Preferred language English; Discharged from the U.S. Armed Forces No; Has season or migrant farm work been your or your family's main source of income at any point in past 2 years [PRAPARE] No; Race White; Hispanic or Latino No | status final | LOINC 93025-5
[Observation/7280f7f8-315d-7c6a-17d4-3bde7faffa5a] Observation (survey) | 2026-04-12 | Protocol for Responding to and Assessing Patients' Assets, Risks, and Experiences [PRAPARE] = Within the last year, have you been afraid of your partner or ex-partner No; Do you feel physically and emotionally safe where you currently live [PRAPARE] Yes; Are you a refugee No; Have you spent more than 2 nights in a row in a jail, prison, detention center, or juvenile correctional facility in past 1 year [PRAPARE] Yes; Stress level A little bit; How often do you see or talk to people that you care about and feel close to [PRAPARE] 3 to 5 times a week; Has lack of transportation kept you from medical appointments, meetings, work, or from getting things needed for daily living No; Have you or any family members you live with been unable to get any of the following when it was really needed in past 1 year [PRAPARE] I choose not to answer this question; What was your best estimate of the total income of all family members from all sources, before taxes, in last year [PhenX] 41074 /a; Primary insurance Medicare; Employment status - current Full-time work; Highest level of education Less than high school degree; Address 702 Parisian Flat; Are you worried about losing your housing [PRAPARE] Yes; Housing status I have housing; How many people are living or staying at this address [#] 8 {#}; Preferred language English; Discharged from the U.S. Armed Forces No; Has season or migrant farm work been your or your family's main source of income at any point in past 2 years [PRAPARE] No; Race White; Hispanic or Latino No | status final | LOINC 93025-5
[Observation/7280f7f8-315d-7c6a-073a-b5db76259ffb] Observation (survey) | 2025-04-06 | Protocol for Responding to and Assessing Patients' Assets, Risks, and Experiences [PRAPARE] = Within the last year, have you been afraid of your partner or ex-partner No; Do you feel physically and emotionally safe where you currently live [PRAPARE] Yes; Are you a refugee No; Have you spent more than 2 nights in a row in a jail, prison, detention center, or juvenile correctional facility in past 1 year [PRAPARE] Yes; Stress level Quite a bit; How often do you see or talk to people that you care about and feel close to [PRAPARE] 3 to 5 times a week; Has lack of transportation kept you from medical appointments, meetings, work, or from getting things needed for daily living No; Have you or any family members you live with been unable to get any of the following when it was really needed in past 1 year [PRAPARE] Medicine or Any Health Care (Medical, Dental, Mental Health, Vision); What was your best estimate of the total income of all family members from all sources, before taxes, in last year [PhenX] 41074 /a; Primary insurance Medicare; Employment status - current Full-time work; Highest level of education Less than high school degree; Address 702 Parisian Flat; Are you worried about losing your housing [PRAPARE] Yes; Housing status I have housing; How many people are living or staying at this address [#] 8 {#}; Preferred language English; Discharged from the U.S. Armed Forces No; Has season or migrant farm work been your or your family's main source of income at any point in past 2 years [PRAPARE] No; Race White; Hispanic or Latino No | status final | LOINC 93025-5
[Observation/7280f7f8-315d-7c6a-f0b4-d6fc3b03db28] Observation (survey) | 2024-11-24 | Protocol for Responding to and Assessing Patients' Assets, Risks, and Experiences [PRAPARE] = Within the last year, have you been afraid of your partner or ex-partner No; Do you feel physically and emotionally safe where you currently live [PRAPARE] Yes; Are you a refugee No; Have you spent more than 2 nights in a row in a jail, prison, detention center, or juvenile correctional facility in past 1 year [PRAPARE] Yes; Stress level Not at all; How often do you see or talk to people that you care about and feel close to [PRAPARE] 5 or more times a week; Has lack of transportation kept you from medical appointments, meetings, work, or from getting things needed for daily living No; Have you or any family members you live with been unable to get any of the following when it was really needed in past 1 year [PRAPARE] Utilities; What was your best estimate of the total income of all family members from all sources, before taxes, in last year [PhenX] 41074 /a; Primary insurance Medicare; Employment status - current Full-time work; Highest level of education Less than high school degree; Address 702 Parisian Flat; Are you worried about losing your housing [PRAPARE] Yes; Housing status I have housing; How many people are living or staying at this address [#] 8 {#}; Preferred language English; Discharged from the U.S. Armed Forces No; Has season or migrant farm work been your or your family's main source of income at any point in past 2 years [PRAPARE] No; Race White; Hispanic or Latino No | status final | LOINC 93025-5
[Observation/7280f7f8-315d-7c6a-aa9b-12ba229b5de0] Observation (laboratory) | 2020-12-21 | Influenza virus A Ag [Presence] in Upper respiratory specimen by Rapid immunoassay = Not detected (qualifier value) | status final | LOINC 80382-5
[Immunization/7280f7f8-315d-7c6a-2836-354c2b85cb88] Immunization | 2023-03-26 | Influenza, split virus, trivalent, PF | status completed | CVX 140
[Immunization/7280f7f8-315d-7c6a-a994-7340336c5a95] Immunization | 2024-11-24 | Influenza, split virus, trivalent, PF | status completed | CVX 140
[Immunization/7280f7f8-315d-7c6a-5206-3912d1550e2d] Immunization | 2024-03-31 | Influenza, split virus, trivalent, PF | status completed | CVX 140
[DiagnosticReport/7280f7f8-315d-7c6a-a75e-da29d2a52425] DiagnosticReport | 2020-12-21 | Influenza virus A and B Ag panel - Upper respiratory specimen by Rapid immunoassay | results: Influenza virus A Ag [Presence] in Upper respiratory specimen by Rapid immunoassay Not detected (qualifier value); Influenza virus B Ag [Presence] in Upper respiratory specimen by Rapid immunoassay Not detected (qualifier value) | LOINC 80381-7
```

</details>

label: s
note: The record's flu immunizations are 2026-04-12, 2024-11-24, 2024-03-31 and 2023-03-26. The three earlier dates are cited and correct, and none are missing.

## 39. `last-visit:530b9289#0#0`

Question: When was the patient's most recent visit, and what kind of visit was it?

Answer: **The most recent visit in the record was on 2025-03-12, an ambulatory (AMB) encounter for check up at NORTH SHORE MEDICAL CENTER INC, with the reason listed as Gingivitis (disorder).**

Cards this sentence cites:

- `[Encounter/530b9289-dc96-576f-fa45-0629d4ad3b09]` Encounter | 2025-03-12 | Encounter for check up (procedure) | class AMB | reason: Gingivitis (disorder) | at NORTH SHORE MEDICAL CENTER INC

<details><summary>Everything the model saw (22 cards)</summary>

```text
[Condition/530b9289-dc96-576f-f6fc-11015cce065e] Condition | onset 2025-02-26 | Part-time employment (finding) | clinical status active | SNOMED 160904001
[Condition/530b9289-dc96-576f-888a-14c459fcf894] Condition | onset 2020-05-06 | Medication review due (situation) | clinical status active | SNOMED 314529007
[Condition/530b9289-dc96-576f-1809-1246e2ec41d9] Condition | onset 2018-10-06 | History of tubal ligation (situation) | clinical status active | SNOMED 267020005
[Condition/530b9289-dc96-576f-8734-8c3a0a9992bf] Condition | onset 2017-05-03 | Body mass index 30+ - obesity (finding) | clinical status active | SNOMED 162864005
[Condition/530b9289-dc96-576f-bdaf-615dd0bc7cf7] Condition | onset 2005-04-20 | Prediabetes (finding) | clinical status active | SNOMED 714628002
[Condition/530b9289-dc96-576f-d54d-1d2b15a86dde] Condition | onset 2001-04-11 | Housing unsatisfactory (finding) | clinical status active | SNOMED 105531004
[Condition/530b9289-dc96-576f-6f01-b29a29894132] Condition | onset 2001-04-11 | Educated to high school level (finding) | clinical status active | SNOMED 473461003
[Condition/530b9289-dc96-576f-8fa7-f82a4cf5d127] Condition | onset 1996-04-03 | Chronic sinusitis (disorder) | clinical status active | SNOMED 40055000
[MedicationRequest/530b9289-dc96-576f-f948-ba67b946cdb9] MedicationRequest | prescribed 2003-11-14 | ferrous sulfate 325 MG Oral Tablet | status active | RxNorm 310325
[Encounter/530b9289-dc96-576f-fa45-0629d4ad3b09] Encounter | 2025-03-12 | Encounter for check up (procedure) | class AMB | reason: Gingivitis (disorder) | at NORTH SHORE MEDICAL CENTER INC
[Encounter/530b9289-dc96-576f-4652-29db662eb77f] Encounter | 2025-02-26 | General examination of patient (procedure) | class AMB | at SALEM FAMILY HEALTH CENTER
[Encounter/530b9289-dc96-576f-3573-1253261abd75] Encounter | 2024-01-10 | Encounter for symptom (procedure) | class AMB | reason: Viral sinusitis (disorder) | at NORTH SHORE MEDICAL CENTER INC
[Observation/530b9289-dc96-576f-0c60-44566e4ae6e8] Observation (survey) | 2017-05-04 | Protocol for Responding to and Assessing Patients' Assets, Risks, and Experiences [PRAPARE] = Within the last year, have you been afraid of your partner or ex-partner No; Do you feel physically and emotionally safe where you currently live [PRAPARE] No; Are you a refugee No; Have you spent more than 2 nights in a row in a jail, prison, detention center, or juvenile correctional facility in past 1 year [PRAPARE] No; Stress level A little bit; How often do you see or talk to people that you care about and feel close to [PRAPARE] 3 to 5 times a week; Has lack of transportation kept you from medical appointments, meetings, work, or from getting things needed for daily living No; Have you or any family members you live with been unable to get any of the following when it was really needed in past 1 year [PRAPARE] I choose not to answer this question; What was your best estimate of the total income of all family members from all sources, before taxes, in last year [PhenX] 77618 /a; Primary insurance Private insurance; Employment status - current Otherwise unemployed but not seeking work (ex: student, retired, disabled, unpaid primary care giver); Highest level of education High school diploma or GED; Address 523 Hessel Parade Apt 49; Are you worried about losing your housing [PRAPARE] Yes; Housing status I have housing; How many people are living or staying at this address [#] 2 {#}; Preferred language English; Discharged from the U.S. Armed Forces No; Has season or migrant farm work been your or your family's main source of income at any point in past 2 years [PRAPARE] No; Race White; Hispanic or Latino No | status final | LOINC 93025-5
[Observation/530b9289-dc96-576f-e88b-b1435ded689b] Observation (survey) | 2025-02-26 | Protocol for Responding to and Assessing Patients' Assets, Risks, and Experiences [PRAPARE] = Within the last year, have you been afraid of your partner or ex-partner No; Do you feel physically and emotionally safe where you currently live [PRAPARE] Yes; Are you a refugee No; Have you spent more than 2 nights in a row in a jail, prison, detention center, or juvenile correctional facility in past 1 year [PRAPARE] No; Stress level Not at all; How often do you see or talk to people that you care about and feel close to [PRAPARE] 3 to 5 times a week; Has lack of transportation kept you from medical appointments, meetings, work, or from getting things needed for daily living No; Have you or any family members you live with been unable to get any of the following when it was really needed in past 1 year [PRAPARE] I choose not to answer this question; What was your best estimate of the total income of all family members from all sources, before taxes, in last year [PhenX] 77618 /a; Primary insurance Private insurance; Employment status - current Part-time or temporary work; Highest level of education High school diploma or GED; Address 523 Hessel Parade Apt 49; Are you worried about losing your housing [PRAPARE] Yes; Housing status I have housing; How many people are living or staying at this address [#] 2 {#}; Preferred language English; Discharged from the U.S. Armed Forces No; Has season or migrant farm work been your or your family's main source of income at any point in past 2 years [PRAPARE] No; Race White; Hispanic or Latino No | status final | LOINC 93025-5
[Observation/530b9289-dc96-576f-b895-83a4407cc3dd] Observation (survey) | 2023-02-22 | Protocol for Responding to and Assessing Patients' Assets, Risks, and Experiences [PRAPARE] = Within the last year, have you been afraid of your partner or ex-partner No; Do you feel physically and emotionally safe where you currently live [PRAPARE] Yes; Are you a refugee No; Have you spent more than 2 nights in a row in a jail, prison, detention center, or juvenile correctional facility in past 1 year [PRAPARE] No; Stress level Very much; How often do you see or talk to people that you care about and feel close to [PRAPARE] 5 or more times a week; Has lack of transportation kept you from medical appointments, meetings, work, or from getting things needed for daily living No; Have you or any family members you live with been unable to get any of the following when it was really needed in past 1 year [PRAPARE] I choose not to answer this question; What was your best estimate of the total income of all family members from all sources, before taxes, in last year [PhenX] 77618 /a; Primary insurance Private insurance; Employment status - current Full-time work; Highest level of education High school diploma or GED; Address 523 Hessel Parade Apt 49; Are you worried about losing your housing [PRAPARE] Yes; Housing status I have housing; How many people are living or staying at this address [#] 2 {#}; Preferred language English; Discharged from the U.S. Armed Forces No; Has season or migrant farm work been your or your family's main source of income at any point in past 2 years [PRAPARE] No; Race White; Hispanic or Latino No | status final | LOINC 93025-5
[Observation/530b9289-dc96-576f-e163-7a7fe69adbc5] Observation (survey) | 2021-06-30 | Protocol for Responding to and Assessing Patients' Assets, Risks, and Experiences [PRAPARE] = Within the last year, have you been afraid of your partner or ex-partner No; Do you feel physically and emotionally safe where you currently live [PRAPARE] Yes; Are you a refugee No; Have you spent more than 2 nights in a row in a jail, prison, detention center, or juvenile correctional facility in past 1 year [PRAPARE] No; Stress level Not at all; How often do you see or talk to people that you care about and feel close to [PRAPARE] 3 to 5 times a week; Has lack of transportation kept you from medical appointments, meetings, work, or from getting things needed for daily living No; Have you or any family members you live with been unable to get any of the following when it was really needed in past 1 year [PRAPARE] I choose not to answer this question; What was your best estimate of the total income of all family members from all sources, before taxes, in last year [PhenX] 77618 /a; Primary insurance Private insurance; Employment status - current Full-time work; Highest level of education High school diploma or GED; Address 523 Hessel Parade Apt 49; Are you worried about losing your housing [PRAPARE] Yes; Housing status I have housing; How many people are living or staying at this address [#] 2 {#}; Preferred language English; Discharged from the U.S. Armed Forces No; Has season or migrant farm work been your or your family's main source of income at any point in past 2 years [PRAPARE] No; Race White; Hispanic or Latino No | status final | LOINC 93025-5
[DocumentReference/67792a8e-57d6-d9db-8ae2-d31f04cb4751#1] Clinical note | 2021-04-14 | part 1 of 1 | 2021-04-14 # Chief Complaint No complaints. # History of Present Illness Carlee848 Anastasia959 is a 38 year-old nonhispanic white female. Patient has a history of dental caries, medication review due (situation), not in labor force (finding), cracked tooth, reports of violence in the environment (finding), full-time employment (finding), viral sinusitis (disorder), sterilization requested (situation), gingivitis (disorder), stress (finding). # Social History Patient is married. Patient has never smoked. Patient identifies as heterosexual. Patient comes from a middle socioeconomic background. Patient has a high school education. Patient currently has UnitedHealthcare. # Allergies No Known Allergies. # Medications {28 (norethindrone 0.35 mg oral tablet) } pack [jolivette 28 day]; levonorgestrel 0.000813 mg/hr intrauterine system [liletta] # Assessment and Plan ## Plan Patient was given the following immunizations: covid-19, mrna, lnp-s, pf, 30 mcg/0.3 ml dose.
[DocumentReference/567999a9-d576-ce2e-036e-071ff8e076bf#1] Clinical note | 2021-03-24 | part 1 of 1 | 2021-03-24 # Chief Complaint No complaints. # History of Present Illness Carlee848 Anastasia959 is a 38 year-old nonhispanic white female. Patient has a history of dental caries, medication review due (situation), not in labor force (finding), cracked tooth, reports of violence in the environment (finding), full-time employment (finding), viral sinusitis (disorder), sterilization requested (situation), gingivitis (disorder), stress (finding). # Social History Patient is married. Patient has never smoked. Patient identifies as heterosexual. Patient comes from a middle socioeconomic background. Patient has a high school education. Patient currently has UnitedHealthcare. # Allergies No Known Allergies. # Medications {28 (norethindrone 0.35 mg oral tablet) } pack [jolivette 28 day]; levonorgestrel 0.000813 mg/hr intrauterine system [liletta] # Assessment and Plan ## Plan Patient was given the following immunizations: covid-19, mrna, lnp-s, pf, 30 mcg/0.3 ml dose.
[Condition/530b9289-dc96-576f-06e5-5971d590051b] Condition | onset 2017-05-03 | Medication review due (situation) | clinical status resolved | resolved 2017-05-03 | SNOMED 314529007
[Immunization/530b9289-dc96-576f-2d9c-beb32f553ec9] Immunization | 2021-04-14 | COVID-19, mRNA, LNP-S, PF, 30 mcg/0.3 mL dose | status completed | CVX 208
[Immunization/530b9289-dc96-576f-e722-2d63e01309e8] Immunization | 2021-03-24 | COVID-19, mRNA, LNP-S, PF, 30 mcg/0.3 mL dose | status completed | CVX 208
[MedicationRequest/530b9289-dc96-576f-dddc-9fa798e0f1fb] MedicationRequest | prescribed 2016-09-25 | status completed
```

</details>

label: s
note: The record's encounters are 2025-03-12, 2025-02-26 and 2024-01-10. The latest is the cited 2025-03-12 AMB check-up at NORTH SHORE MEDICAL CENTER INC with reason Gingivitis, and every detail matches.

## 40. `vaccines-last-year:760e0542#0#0`

Question: Which vaccines did the patient receive in the last year?

Answer: **In the year before the record's as-of date of 2026-10-01, the patient received one vaccine: Influenza, split virus, trivalent, PF (CVX 140) on 2026-04-08.** The previous influenza dose, on 2025-03-12, falls outside that one-year window.

Cards this sentence cites:

- `[Immunization/760e0542-9c61-9c1a-bb77-51bf2da7f927]` Immunization | 2026-04-08 | Influenza, split virus, trivalent, PF | status completed | CVX 140

<details><summary>Everything the model saw (44 cards)</summary>

```text
[Condition/760e0542-9c61-9c1a-f014-d96ecb52354b] Condition | onset 2026-09-09 | Full-time employment (finding) | clinical status active | SNOMED 160903007
[Condition/760e0542-9c61-9c1a-3909-ca43a58a2be0] Condition | onset 2023-02-08 | Social isolation (finding) | clinical status active | SNOMED 422650009
[Condition/760e0542-9c61-9c1a-0603-33ac04e928e9] Condition | onset 2017-07-26 | Has a criminal record (finding) | clinical status active | SNOMED 266948004
[Condition/760e0542-9c61-9c1a-7969-97405f2cda90] Condition | onset 2016-09-28 | Gingivitis (disorder) | clinical status active | SNOMED 66383009
[Condition/760e0542-9c61-9c1a-bc04-975a613f7bef] Condition | onset 2016-05-04 | Proteinuria due to type 2 diabetes mellitus (disorder) | clinical status active | SNOMED 157141000119108
[Condition/760e0542-9c61-9c1a-19fd-96240fc0e3b9] Condition | onset 2016-05-04 | Chronic kidney disease stage 3 (disorder) | clinical status active | SNOMED 433144002
[Condition/760e0542-9c61-9c1a-e1cf-d1bcca0d3b69] Condition | onset 2016-03-02 | Familial Alzheimer's disease of early onset (disorder) | clinical status active | SNOMED 230265002
[Condition/760e0542-9c61-9c1a-bf45-3800d10bb908] Condition | onset 2012-09-12 | Chronic sinusitis (disorder) | clinical status active | SNOMED 40055000
[Condition/760e0542-9c61-9c1a-6a42-9364f5d685e7] Condition | onset 2009-10-14 | Chronic kidney disease stage 2 (disorder) | clinical status active | SNOMED 431856006
[Condition/760e0542-9c61-9c1a-6844-45eca3bcbf32] Condition | onset 2009-10-14 | Microalbuminuria due to type 2 diabetes mellitus (disorder) | clinical status active | SNOMED 90781000119102
[Condition/760e0542-9c61-9c1a-c55b-b73483d412d5] Condition | onset 2004-09-01 | Disorder of kidney due to diabetes mellitus (disorder) | clinical status active | SNOMED 127013003
[Condition/760e0542-9c61-9c1a-8f20-42b2a944fe6e] Condition | onset 2004-09-01 | Chronic kidney disease stage 1 (disorder) | clinical status active | SNOMED 431855005
[Condition/760e0542-9c61-9c1a-426d-1b0e47f6ef3a] Condition | onset 2004-09-01 | Hyperglycemia (disorder) | clinical status active | SNOMED 80394007
[Condition/760e0542-9c61-9c1a-84cc-6ec1252b5c47] Condition | onset 1998-10-12 | History of tubal ligation (situation) | clinical status active | SNOMED 267020005
[Condition/760e0542-9c61-9c1a-d618-c814cd687574] Condition | onset 1998-01-07 | Hypertriglyceridemia (disorder) | clinical status active | SNOMED 302870006
[Condition/760e0542-9c61-9c1a-addb-545c11e2d54a] Condition | onset 1998-01-07 | Metabolic syndrome X (disorder) | clinical status active | SNOMED 237602007
[Condition/760e0542-9c61-9c1a-393d-4476d7ede869] Condition | onset 1995-01-04 | Diabetes mellitus type 2 (disorder) | clinical status active | SNOMED 44054006
[Condition/760e0542-9c61-9c1a-0e56-fe029b0a5419] Condition | onset 1990-08-12 | Past pregnancy history of miscarriage (situation) | clinical status active | SNOMED 161744009
[Condition/760e0542-9c61-9c1a-8747-2a2b77e88f89] Condition | onset 1988-12-28 | Anemia (disorder) | clinical status active | SNOMED 271737000
[Condition/760e0542-9c61-9c1a-4f0e-0a94437d4aaa] Condition | onset 1988-12-28 | Body mass index 30+ - obesity (finding) | clinical status active | SNOMED 162864005
[Condition/760e0542-9c61-9c1a-771f-54deeed066bf] Condition | onset 1982-12-22 | Prediabetes (finding) | clinical status active | SNOMED 714628002
[Condition/760e0542-9c61-9c1a-0604-679a8d525bc1] Condition | onset 1981-12-16 | Received higher education (finding) | clinical status active | SNOMED 224299000
[Condition/760e0542-9c61-9c1a-c792-3a8303530414] Condition | onset 1979-12-05 | Risk activity involvement (finding) | clinical status active | SNOMED 160968000
[Condition/760e0542-9c61-9c1a-1d06-faad5e8f657c] Condition | onset 1974-01-03 | Adolescent idiopathic scoliosis (disorder) | clinical status active | SNOMED 203646004
[MedicationRequest/760e0542-9c61-9c1a-c29f-4c3b83db674e] MedicationRequest | prescribed 2026-09-09 | 24 HR Metformin hydrochloride 500 MG Extended Release Oral Tablet | status active | reason: Diabetes mellitus type 2 (disorder) | RxNorm 860975
[MedicationRequest/760e0542-9c61-9c1a-096d-4868f9087e48] MedicationRequest | prescribed 2026-09-09 | insulin isophane, human 70 UNT/ML / insulin, regular, human 30 UNT/ML Injectable Suspension [Humulin] | status active | reason: Diabetes mellitus type 2 (disorder) | RxNorm 106892
[MedicationRequest/760e0542-9c61-9c1a-c259-531395abfaa1] MedicationRequest | prescribed 2023-01-14 | 24 HR Donepezil hydrochloride 10 MG / Memantine hydrochloride 28 MG Extended Release Oral Capsule | status active | reason: Familial Alzheimer's disease of early onset (disorder) | RxNorm 1599803
[MedicationRequest/760e0542-9c61-9c1a-fd81-acf11c1ddec0] MedicationRequest | prescribed 1967-04-25 | Chlorpheniramine Maleate 2 MG/ML Oral Solution | status active | RxNorm 477045
[AllergyIntolerance/760e0542-9c61-9c1a-3695-658972edefe5] AllergyIntolerance | recorded 1967-05-01 | Allergic disposition (finding) | allergy, category environment, criticality low | clinical status active | SNOMED 609328004
[AllergyIntolerance/760e0542-9c61-9c1a-1887-b0f58a6117f4] AllergyIntolerance | recorded 1967-05-01 | Lisinopril | intolerance, category medication, criticality low | clinical status active | RxNorm 29046
[Encounter/760e0542-9c61-9c1a-6caa-86123ce8fd48] Encounter | 2026-09-09 | Urgent care clinic (environment) | class AMB | at MIDDLETON FAMILY MEDICINE URGENT CARE, LLC
[Encounter/760e0542-9c61-9c1a-dbc8-3964b3a3c72f] Encounter | 2026-08-05 | Urgent care clinic (environment) | class AMB | at MIDDLETON FAMILY MEDICINE URGENT CARE, LLC
[Encounter/760e0542-9c61-9c1a-d9e8-129c4edf531b] Encounter | 2026-05-27 | Encounter for check up (procedure) | class AMB | at LAWRENCE GENERAL HOSPITAL
[Immunization/760e0542-9c61-9c1a-bb77-51bf2da7f927] Immunization | 2026-04-08 | Influenza, split virus, trivalent, PF | status completed | CVX 140
[Immunization/760e0542-9c61-9c1a-929e-cafe8c3d1285] Immunization | 2021-04-07 | Influenza, split virus, trivalent, PF | status completed | CVX 140
[Immunization/760e0542-9c61-9c1a-56c8-3633420009aa] Immunization | 2025-03-12 | Influenza, split virus, trivalent, PF | status completed | CVX 140
[Immunization/760e0542-9c61-9c1a-7506-c0010ccbdeb9] Immunization | 2024-03-20 | Influenza, split virus, trivalent, PF | status completed | CVX 140
[Observation/760e0542-9c61-9c1a-4db9-5f8155d7a4a9] Observation (survey) | 2022-08-31 | Protocol for Responding to and Assessing Patients' Assets, Risks, and Experiences [PRAPARE] = Within the last year, have you been afraid of your partner or ex-partner No; Do you feel physically and emotionally safe where you currently live [PRAPARE] Yes; Are you a refugee No; Have you spent more than 2 nights in a row in a jail, prison, detention center, or juvenile correctional facility in past 1 year [PRAPARE] Yes; Stress level Somewhat; How often do you see or talk to people that you care about and feel close to [PRAPARE] 5 or more times a week; Has lack of transportation kept you from medical appointments, meetings, work, or from getting things needed for daily living No; Have you or any family members you live with been unable to get any of the following when it was really needed in past 1 year [PRAPARE] Phone; What was your best estimate of the total income of all family members from all sources, before taxes, in last year [PhenX] 34577 /a; Primary insurance Medicare; Employment status - current Full-time work; Highest level of education More than high school; Address 594 Johns Parade; Are you worried about losing your housing [PRAPARE] No; Housing status I have housing; How many people are living or staying at this address [#] 7 {#}; Preferred language English; Discharged from the U.S. Armed Forces No; Has season or migrant farm work been your or your family's main source of income at any point in past 2 years [PRAPARE] No; Race White; Hispanic or Latino No | status final | LOINC 93025-5
[Observation/760e0542-9c61-9c1a-5396-569000ad1810] Observation (survey) | 2026-09-09 | Protocol for Responding to and Assessing Patients' Assets, Risks, and Experiences [PRAPARE] = Within the last year, have you been afraid of your partner or ex-partner No; Do you feel physically and emotionally safe where you currently live [PRAPARE] Yes; Are you a refugee No; Have you spent more than 2 nights in a row in a jail, prison, detention center, or juvenile correctional facility in past 1 year [PRAPARE] Yes; Stress level Not at all; How often do you see or talk to people that you care about and feel close to [PRAPARE] 3 to 5 times a week; Has lack of transportation kept you from medical appointments, meetings, work, or from getting things needed for daily living No; Have you or any family members you live with been unable to get any of the following when it was really needed in past 1 year [PRAPARE] Food; What was your best estimate of the total income of all family members from all sources, before taxes, in last year [PhenX] 34577 /a; Primary insurance Medicare; Employment status - current Full-time work; Highest level of education More than high school; Address 594 Johns Parade; Are you worried about losing your housing [PRAPARE] No; Housing status I have housing; How many people are living or staying at this address [#] 7 {#}; Preferred language English; Discharged from the U.S. Armed Forces No; Has season or migrant farm work been your or your family's main source of income at any point in past 2 years [PRAPARE] No; Race White; Hispanic or Latino No | status final | LOINC 93025-5
[Observation/760e0542-9c61-9c1a-70b1-461a59a58d74] Observation (survey) | 2026-08-05 | Protocol for Responding to and Assessing Patients' Assets, Risks, and Experiences [PRAPARE] = Within the last year, have you been afraid of your partner or ex-partner No; Do you feel physically and emotionally safe where you currently live [PRAPARE] No; Are you a refugee No; Have you spent more than 2 nights in a row in a jail, prison, detention center, or juvenile correctional facility in past 1 year [PRAPARE] Yes; Stress level Quite a bit; How often do you see or talk to people that you care about and feel close to [PRAPARE] 3 to 5 times a week; Has lack of transportation kept you from medical appointments, meetings, work, or from getting things needed for daily living No; Have you or any family members you live with been unable to get any of the following when it was really needed in past 1 year [PRAPARE] I choose not to answer this question; What was your best estimate of the total income of all family members from all sources, before taxes, in last year [PhenX] 34577 /a; Primary insurance Medicare; Employment status - current Part-time or temporary work; Highest level of education More than high school; Address 594 Johns Parade; Are you worried about losing your housing [PRAPARE] No; Housing status I have housing; How many people are living or staying at this address [#] 7 {#}; Preferred language English; Discharged from the U.S. Armed Forces No; Has season or migrant farm work been your or your family's main source of income at any point in past 2 years [PRAPARE] No; Race White; Hispanic or Latino No | status final | LOINC 93025-5
[Observation/760e0542-9c61-9c1a-e7d2-cadcc2eca802] Observation (survey) | 2026-05-13 | Protocol for Responding to and Assessing Patients' Assets, Risks, and Experiences [PRAPARE] = Within the last year, have you been afraid of your partner or ex-partner No; Do you feel physically and emotionally safe where you currently live [PRAPARE] Yes; Are you a refugee No; Have you spent more than 2 nights in a row in a jail, prison, detention center, or juvenile correctional facility in past 1 year [PRAPARE] Yes; Stress level A little bit; How often do you see or talk to people that you care about and feel close to [PRAPARE] 3 to 5 times a week; Has lack of transportation kept you from medical appointments, meetings, work, or from getting things needed for daily living No; Have you or any family members you live with been unable to get any of the following when it was really needed in past 1 year [PRAPARE] Food; What was your best estimate of the total income of all family members from all sources, before taxes, in last year [PhenX] 34577 /a; Primary insurance Medicare; Employment status - current Full-time work; Highest level of education More than high school; Address 594 Johns Parade; Are you worried about losing your housing [PRAPARE] No; Housing status I have housing; How many people are living or staying at this address [#] 7 {#}; Preferred language English; Discharged from the U.S. Armed Forces No; Has season or migrant farm work been your or your family's main source of income at any point in past 2 years [PRAPARE] No; Race White; Hispanic or Latino No | status final | LOINC 93025-5
[Immunization/760e0542-9c61-9c1a-348d-850ee604a0a7] Immunization | 2021-04-14 | COVID-19, mRNA, LNP-S, PF, 30 mcg/0.3 mL dose | status completed | CVX 208
[Immunization/760e0542-9c61-9c1a-bb55-2e74e1870df5] Immunization | 2021-05-05 | COVID-19, mRNA, LNP-S, PF, 30 mcg/0.3 mL dose | status completed | CVX 208
[DocumentReference/dea8e555-16a6-228a-ab25-b69355fdcefe#2] Clinical note | 2021-04-14 | part 2 of 2 | # Assessment and Plan ## Plan Patient was given the following immunizations: covid-19, mrna, lnp-s, pf, 30 mcg/0.3 ml dose. The following lab reports were completed: - basic metabolic 2000 panel - serum or plasma - urinalysis macro (dipstick) panel - urine The patient was prescribed the following medications: - insulin isophane, human 70 unt/ml / insulin, regular, human 30 unt/ml injectable suspension [humulin] - 24 hr metformin hydrochloride 500 mg extended release oral tablet
```

</details>

label: s
note: The only immunization after 2025-10-01 is the cited influenza CVX 140 dose on 2026-04-08. The others (2025-03-12, 2024-03-20, 2021 doses) fall outside the window, so 'one vaccine' holds.

## 41. `last-flu-shot:8ff46e01#0#0`

Question: When did the patient last get a flu shot?

Answer: **The patient's most recent flu shot was on 2025-12-31 (Influenza, split virus, trivalent, PF; status completed).** Earlier influenza vaccinations of the same type were given on 2023-12-27 and 2021-12-22.

Cards this sentence cites:

- `[Immunization/8ff46e01-0333-fefb-0b35-b6fa97749e42]` Immunization | 2025-12-31 | Influenza, split virus, trivalent, PF | status completed | CVX 140

<details><summary>Everything the model saw (35 cards)</summary>

```text
[Condition/8ff46e01-0333-fefb-e078-a2c79f9b5570] Condition | onset 2025-11-10 | History of myocardial infarction (situation) | clinical status active | SNOMED 399211009
[Condition/8ff46e01-0333-fefb-ca9a-9c89d481d534] Condition | onset 2025-11-10 | Acute non-ST segment elevation myocardial infarction (disorder) | clinical status active | SNOMED 401314000
[Condition/8ff46e01-0333-fefb-f69f-b001b28f2b81] Condition | onset 2023-12-27 | Full-time employment (finding) | clinical status active | SNOMED 160903007
[Condition/8ff46e01-0333-fefb-d37b-fa17bc4619e6] Condition | onset 2023-12-27 | Hyperlipidemia (disorder) | clinical status active | SNOMED 55822004
[Condition/8ff46e01-0333-fefb-1085-7240f563162c] Condition | onset 2023-12-27 | Anemia (disorder) | clinical status active | SNOMED 271737000
[Condition/8ff46e01-0333-fefb-0d5f-96af345c8178] Condition | onset 2023-12-27 | Prediabetes (finding) | clinical status active | SNOMED 714628002
[Condition/8ff46e01-0333-fefb-a724-e7508612ceb2] Condition | onset 2015-12-19 | History of tubal ligation (situation) | clinical status active | SNOMED 267020005
[Condition/8ff46e01-0333-fefb-c4b8-0da5f4d9d6af] Condition | onset 2010-09-29 | Stress (finding) | clinical status active | SNOMED 73595000
[Condition/8ff46e01-0333-fefb-3eac-29a6b80382d5] Condition | onset 1998-06-27 | Recurrent urinary tract infection (disorder) | clinical status active | SNOMED 197927001
[Condition/8ff46e01-0333-fefb-1001-1cc553e61d65] Condition | onset 1998-02-04 | Only received primary school education (finding) | clinical status active | SNOMED 224295006
[Condition/8ff46e01-0333-fefb-2118-3da43e594952] Condition | onset 1995-01-18 | Risk activity involvement (finding) | clinical status active | SNOMED 160968000
[Condition/8ff46e01-0333-fefb-400e-c9db591e5ada] Condition | onset 1988-12-14 | Gingivitis (disorder) | clinical status active | SNOMED 66383009
[Condition/8ff46e01-0333-fefb-6f8d-08005729c21a] Condition | onset 1980-10-17 | History of seizure (situation) | clinical status active | SNOMED 1290882004
[Condition/8ff46e01-0333-fefb-334a-c4ab11856973] Condition | onset 1980-10-17 | Seizure disorder (disorder) | clinical status active | SNOMED 128613002
[Condition/8ff46e01-0333-fefb-493a-f8d458075b36] Condition | onset 1980-04-22 | Chronic sinusitis (disorder) | clinical status active | SNOMED 40055000
[MedicationRequest/8ff46e01-0333-fefb-081b-4d95e98b7814] MedicationRequest | prescribed 2026-01-16 | Simvastatin 10 MG Oral Tablet | status active | reason: Hyperlipidemia (disorder) | RxNorm 314231
[MedicationRequest/8ff46e01-0333-fefb-cca1-202b10a1b90d] MedicationRequest | prescribed 2025-11-10 | aspirin 81 MG Oral Tablet | status active | RxNorm 243670
[MedicationRequest/8ff46e01-0333-fefb-6306-60b207f6bcda] MedicationRequest | prescribed 2025-11-10 | rosuvastatin calcium 10 MG Oral Tablet | status active | RxNorm 859747
[MedicationRequest/8ff46e01-0333-fefb-5a32-7c872c74242b] MedicationRequest | prescribed 2025-11-10 | atenolol 50 MG Oral Tablet | status active | RxNorm 197381
[MedicationRequest/8ff46e01-0333-fefb-5632-79d28eb2f69d] MedicationRequest | prescribed 2025-11-10 | prasugrel 10 MG Oral Tablet | status active | RxNorm 855812
[MedicationRequest/8ff46e01-0333-fefb-0f09-741ffc0ecb79] MedicationRequest | prescribed 2025-11-10 | lisinopril 10 MG Oral Tablet | status active | RxNorm 314076
[Encounter/8ff46e01-0333-fefb-2842-108bae2a93b7] Encounter | 2026-01-16 | Follow-up encounter (procedure) | class AMB | reason: Hyperlipidemia (disorder) | at STEWARD HOLY FAMILY HOSPITAL INC
[Encounter/8ff46e01-0333-fefb-deac-7d54a2e717b0] Encounter | 2025-12-31 | General examination of patient (procedure) | class AMB | at GREATER LAWRENCE FAMILY HEALTH CENTER INC
[Encounter/8ff46e01-0333-fefb-bdb4-35663b36a4c8] Encounter | 2025-11-10 | Emergency room admission (procedure) | class EMER | reason: Myocardial infarction (disorder) | at Fitchburg Outpatient Clinic
[Immunization/8ff46e01-0333-fefb-0b35-b6fa97749e42] Immunization | 2025-12-31 | Influenza, split virus, trivalent, PF | status completed | CVX 140
[Immunization/8ff46e01-0333-fefb-9332-da69b2e28029] Immunization | 2021-12-22 | Hep A, adult | status completed | CVX 52
[Immunization/8ff46e01-0333-fefb-0ce7-a4c238a33f28] Immunization | 2019-12-18 | Hep A, adult | status completed | CVX 52
[Observation/8ff46e01-0333-fefb-816d-363218ace13b] Observation (survey) | 2025-12-31 | Protocol for Responding to and Assessing Patients' Assets, Risks, and Experiences [PRAPARE] = Within the last year, have you been afraid of your partner or ex-partner No; Do you feel physically and emotionally safe where you currently live [PRAPARE] Yes; Are you a refugee No; Have you spent more than 2 nights in a row in a jail, prison, detention center, or juvenile correctional facility in past 1 year [PRAPARE] No; Stress level Somewhat; How often do you see or talk to people that you care about and feel close to [PRAPARE] 5 or more times a week; Has lack of transportation kept you from medical appointments, meetings, work, or from getting things needed for daily living No; Have you or any family members you live with been unable to get any of the following when it was really needed in past 1 year [PRAPARE] I choose not to answer this question; What was your best estimate of the total income of all family members from all sources, before taxes, in last year [PhenX] 90342 /a; Primary insurance Medicare; Employment status - current Full-time work; Highest level of education Less than high school degree; Address 942 Herzog Highlands Suite 0; Are you worried about losing your housing [PRAPARE] No; Housing status I have housing; How many people are living or staying at this address [#] 1 {#}; Preferred language English; Discharged from the U.S. Armed Forces No; Has season or migrant farm work been your or your family's main source of income at any point in past 2 years [PRAPARE] No; Race White; Hispanic or Latino No | status final | LOINC 93025-5
[Observation/8ff46e01-0333-fefb-cb14-9f790999159d] Observation (survey) | 2023-12-27 | Protocol for Responding to and Assessing Patients' Assets, Risks, and Experiences [PRAPARE] = Within the last year, have you been afraid of your partner or ex-partner No; Do you feel physically and emotionally safe where you currently live [PRAPARE] Yes; Are you a refugee No; Have you spent more than 2 nights in a row in a jail, prison, detention center, or juvenile correctional facility in past 1 year [PRAPARE] No; Stress level Somewhat; How often do you see or talk to people that you care about and feel close to [PRAPARE] 5 or more times a week; Has lack of transportation kept you from medical appointments, meetings, work, or from getting things needed for daily living No; Have you or any family members you live with been unable to get any of the following when it was really needed in past 1 year [PRAPARE] I choose not to answer this question; What was your best estimate of the total income of all family members from all sources, before taxes, in last year [PhenX] 90342 /a; Primary insurance Medicare; Employment status - current Full-time work; Highest level of education Less than high school degree; Address 942 Herzog Highlands Suite 0; Are you worried about losing your housing [PRAPARE] No; Housing status I have housing; How many people are living or staying at this address [#] 1 {#}; Preferred language English; Discharged from the U.S. Armed Forces No; Has season or migrant farm work been your or your family's main source of income at any point in past 2 years [PRAPARE] No; Race White; Hispanic or Latino No | status final | LOINC 93025-5
[Observation/8ff46e01-0333-fefb-21a5-1c5b6786878d] Observation (survey) | 2021-12-22 | Protocol for Responding to and Assessing Patients' Assets, Risks, and Experiences [PRAPARE] = Within the last year, have you been afraid of your partner or ex-partner No; Do you feel physically and emotionally safe where you currently live [PRAPARE] Yes; Are you a refugee No; Have you spent more than 2 nights in a row in a jail, prison, detention center, or juvenile correctional facility in past 1 year [PRAPARE] No; Stress level A little bit; How often do you see or talk to people that you care about and feel close to [PRAPARE] 5 or more times a week; Has lack of transportation kept you from medical appointments, meetings, work, or from getting things needed for daily living No; Have you or any family members you live with been unable to get any of the following when it was really needed in past 1 year [PRAPARE] I choose not to answer this question; What was your best estimate of the total income of all family members from all sources, before taxes, in last year [PhenX] 90342 /a; Primary insurance Medicare; Employment status - current Part-time or temporary work; Highest level of education Less than high school degree; Address 942 Herzog Highlands Suite 0; Are you worried about losing your housing [PRAPARE] No; Housing status I have housing; How many people are living or staying at this address [#] 1 {#}; Preferred language English; Discharged from the U.S. Armed Forces No; Has season or migrant farm work been your or your family's main source of income at any point in past 2 years [PRAPARE] No; Race White; Hispanic or Latino No | status final | LOINC 93025-5
[Immunization/8ff46e01-0333-fefb-0036-64ca02117c5e] Immunization | 2023-12-27 | Influenza, split virus, trivalent, PF | status completed | CVX 140
[Immunization/8ff46e01-0333-fefb-e72e-ff49966cb353] Immunization | 2021-12-22 | Influenza, split virus, trivalent, PF | status completed | CVX 140
[DocumentReference/3b72f05e-b969-be57-439e-70bb4961a4b7#2] Clinical note | 2021-12-22 | part 2 of 2 | # Assessment and Plan ## Plan Patient was given the following immunizations: influenza, split virus, trivalent, pf, td (adult), 5 lf tetanus toxoid, preservative free, adsorbed, hep a, adult. The following procedures were conducted: - assessment of health and social care needs (procedure) - assessment of anxiety (procedure) - depression screening (procedure) - depression screening (procedure) - assessment of substance use (procedure) - assessment using alcohol use disorders identification test - consumption (procedure) The following lab reports were completed: - lipid panel with direct ldl - serum or plasma - generalized anxiety disorder 7 item (gad-7) - patient health questionnaire 2 item (phq-2) [reported] - alcohol use disorder identification test - consumption [audit-c]
[DocumentReference/463b0dd4-8c74-c01d-fe40-d6d40adac09f#1] Clinical note | 2017-03-01 | part 1 of 1 | 2017-03-01 # Chief Complaint No complaints. # History of Present Illness Lupe126 is a 37 year-old hispanic white female. Patient has a history of malignant neoplasm of head, face and neck, other specified diseases of jaws, full-time employment (finding), other specified disorders of teeth and supporting structures, dental caries, unspecified. # Social History Patient is single. Patient has never smoked. Patient identifies as heterosexual. Patient comes from a middle socioeconomic background. Patient did not finish high school. Patient currently has NO INSURANCE. # Allergies No Known Allergies. # Medications No Active Medications. # Assessment and Plan Patient is presenting with medication review due (situation). ## Plan Patient was given the following immunizations: influenza, split virus, trivalent, pf. The following procedures were conducted: - assessment of health and social care needs (procedure) - depression screening (procedure) - depression screening (procedure) - assessment of substance use (procedure) - screening for drug abuse (procedure) - patient referral for dental care (procedure) The following lab reports were completed: - lipid panel with direct ldl - serum or plasma - patient health questionnaire 2 item (phq-2) [reported] - drug abuse screening test-10 [dast-10]
[MedicationRequest/8ff46e01-0333-fefb-071f-4a32d7ee3611] MedicationRequest | prescribed 2025-11-10 | status completed
```

</details>

label: s
note: Cited Immunization card is Influenza, split virus, trivalent, PF, 2025-12-31, completed; the only other influenza entries seen (2023-12-27, 2021-12-22, 2017-03-01 note) are all earlier, so 'most recent' holds.

## 42. `last-visit:9292c3d5#0#0`

Question: When was the patient's most recent visit, and what kind of visit was it?

Answer: **The patient's most recent visit was on 2026-04-26, an ambulatory (class AMB) encounter for General examination of patient (procedure) at COMMUNITY HEALTH PROGRAMS INC.** At that visit, the patient received an Influenza, split virus, trivalent, PF immunization.

Cards this sentence cites:

- `[Encounter/9292c3d5-3db6-f4f9-f8cd-08dfcc81ed12]` Encounter | 2026-04-26 | General examination of patient (procedure) | class AMB | at COMMUNITY HEALTH PROGRAMS INC

<details><summary>Everything the model saw (31 cards)</summary>

```text
[Condition/9292c3d5-3db6-f4f9-b5ec-3a44e8649597] Condition | onset 2026-04-26 | Full-time employment (finding) | clinical status active | SNOMED 160903007
[Condition/9292c3d5-3db6-f4f9-861b-f7159312202f] Condition | onset 2026-04-26 | Medication review due (situation) | clinical status active | SNOMED 314529007
[Condition/9292c3d5-3db6-f4f9-483e-3d8d3b0f4690] Condition | onset 2026-04-26 | Social isolation (finding) | clinical status active | SNOMED 422650009
[Condition/9292c3d5-3db6-f4f9-38dc-147de4ac63a8] Condition | onset 2026-04-26 | Stress (finding) | clinical status active | SNOMED 73595000
[Condition/9292c3d5-3db6-f4f9-5b6c-1c0ed0fd0321] Condition | onset 2020-03-22 | Opioid abuse | clinical status active | SNOMED 5602001
[Condition/9292c3d5-3db6-f4f9-f835-25af6c77c701] Condition | onset 2011-08-22 | History of myocardial infarction (situation) | clinical status active | SNOMED 399211009
[Condition/9292c3d5-3db6-f4f9-54d1-d4b6d2666838] Condition | onset 2011-08-22 | Acute ST segment elevation myocardial infarction (disorder) | clinical status active | SNOMED 401303003
[Condition/9292c3d5-3db6-f4f9-2b48-fd31edda50b0] Condition | onset 2010-03-21 | Anemia (disorder) | clinical status active | SNOMED 271737000
[Condition/9292c3d5-3db6-f4f9-1b0c-65cb31846f75] Condition | onset 2005-05-29 | Prediabetes (finding) | clinical status active | SNOMED 714628002
[Condition/9292c3d5-3db6-f4f9-2a82-9615e45bb615] Condition | onset 1986-05-04 | Educated to high school level (finding) | clinical status active | SNOMED 473461003
[Condition/9292c3d5-3db6-f4f9-24a0-fe08e411b951] Condition | onset 1986-05-04 | Serving in military service (finding) | clinical status active | SNOMED 1187604002
[Condition/9292c3d5-3db6-f4f9-97fc-b779fe5ffdd4] Condition | onset 1985-04-28 | Risk activity involvement (finding) | clinical status active | SNOMED 160968000
[MedicationRequest/9292c3d5-3db6-f4f9-c2ad-ca0afa2369e8] MedicationRequest | prescribed 2011-08-22 | 24 HR metoprolol succinate 50 MG Extended Release Oral Tablet | status active | RxNorm 866436
[MedicationRequest/9292c3d5-3db6-f4f9-b955-8ddb9b72de69] MedicationRequest | prescribed 2011-08-22 | prasugrel 10 MG Oral Tablet | status active | RxNorm 855812
[MedicationRequest/9292c3d5-3db6-f4f9-8b49-28e15899c04a] MedicationRequest | prescribed 2011-08-22 | aspirin 81 MG Oral Tablet | status active | RxNorm 243670
[MedicationRequest/9292c3d5-3db6-f4f9-7675-f5ee99ae0c4e] MedicationRequest | prescribed 2011-08-22 | simvastatin 40 MG Oral Tablet | status active | RxNorm 198211
[MedicationRequest/9292c3d5-3db6-f4f9-2744-8b9a3e3302b8] MedicationRequest | prescribed 2011-08-22 | lisinopril 2.5 MG Oral Tablet | status active | RxNorm 311353
[Encounter/9292c3d5-3db6-f4f9-f8cd-08dfcc81ed12] Encounter | 2026-04-26 | General examination of patient (procedure) | class AMB | at COMMUNITY HEALTH PROGRAMS INC
[Encounter/9292c3d5-3db6-f4f9-2526-cf0c3fc1dcaa] Encounter | 2025-08-10 | Encounter for check up (procedure) | class AMB | reason: Gingivitis (disorder) | at Pittsfield Outpatient Clinic
[Encounter/9292c3d5-3db6-f4f9-d85c-7f88671a1881] Encounter | 2025-08-03 | Encounter for symptom (procedure) | class AMB | reason: Acute viral pharyngitis (disorder) | at Pittsfield Outpatient Clinic
[Immunization/9292c3d5-3db6-f4f9-2e74-b2ab508532b8] Immunization | 2026-04-26 | Influenza, split virus, trivalent, PF | status completed | CVX 140
[DocumentReference/90384e69-4cc2-2777-3c5c-df19b398fb3a#1] Clinical note | 2019-03-31 | part 1 of 1 | 2019-03-31 # Chief Complaint No complaints. # History of Present Illness Arnold338 is a 51 year-old nonhispanic white male. Patient has a history of medication review due (situation), not in labor force (finding), limited social contact (finding), disorder of teeth and/or supporting structures, full-time employment (finding), social isolation (finding), stress (finding). # Social History Patient is single. Patient quit smoking at age 17. Patient identifies as heterosexual. Patient comes from a middle socioeconomic background. Patient has a high school education. Patient currently has Humana. # Allergies No Known Allergies. # Medications No Active Medications. # Assessment and Plan ## Plan The following procedures were conducted: - periodic orthodontic treatment visit - periodic orthodontic treatment visit
[Encounter/9292c3d5-3db6-f4f9-a03b-3743d58b1c78] Encounter | 1985-04-28 | Well child visit (procedure) | class AMB | at COMMUNITY HEALTH PROGRAMS INC
[Procedure/9292c3d5-3db6-f4f9-1146-76d185c4ad5d] Procedure | 2019-03-31 | periodic orthodontic treatment visit | status completed | http://www.ada.org/cdt D8670
[Procedure/9292c3d5-3db6-f4f9-a726-7825263e1ace] Procedure | 2019-03-31 | periodic orthodontic treatment visit | status completed | http://www.ada.org/cdt D8670
[DocumentReference/b0afcae6-490b-fb11-b71d-382273ce441c#1] Clinical note | 2021-03-14 | part 1 of 1 | 2021-03-14 # Chief Complaint No complaints. # History of Present Illness Arnold338 is a 53 year-old nonhispanic white male. Patient has a history of severe anxiety (panic) (finding), medication review due (situation), not in labor force (finding), limited social contact (finding), disorder of teeth and/or supporting structures, full-time employment (finding), social isolation (finding), stress (finding). # Social History Patient is single. Patient quit smoking at age 17. Patient identifies as heterosexual. Patient comes from a middle socioeconomic background. Patient has a high school education. Patient currently has Humana. # Allergies No Known Allergies. # Medications No Active Medications. # Assessment and Plan ## Plan Patient was given the following immunizations: covid-19, mrna, lnp-s, pf, 30 mcg/0.3 ml dose.
[Condition/9292c3d5-3db6-f4f9-fbfb-cfc1d4cdf03c] Condition | onset 2014-03-30 | Medication review due (situation) | clinical status resolved | resolved 2025-04-20 | SNOMED 314529007
[Condition/9292c3d5-3db6-f4f9-dc28-5fba82169057] Condition | onset 2025-07-27 | Medication review due (situation) | clinical status resolved | resolved 2025-07-27 | SNOMED 314529007
[Encounter/9292c3d5-3db6-f4f9-71e0-c657f27fd422] Encounter | 1970-08-23 | Encounter for check up (procedure) | class AMB | reason: Patient referral for dental care (procedure) | at BERKSHIRE MEDICAL CENTER INC - 1
[Immunization/9292c3d5-3db6-f4f9-0e55-dcf5b05aeef5] Immunization | 2021-04-04 | COVID-19, mRNA, LNP-S, PF, 30 mcg/0.3 mL dose | status completed | CVX 208
[Immunization/9292c3d5-3db6-f4f9-0865-19e45ffab679] Immunization | 2021-03-14 | COVID-19, mRNA, LNP-S, PF, 30 mcg/0.3 mL dose | status completed | CVX 208
```

</details>

label: s
note: Cited Encounter is 2026-04-26, General examination of patient (procedure), class AMB, at COMMUNITY HEALTH PROGRAMS INC; all other encounters, notes and procedures seen are earlier (latest 2025-08-10), so it is the most recent visit.

## 43. `smoking-status:772fc930#0#0`

Question: Does the patient smoke?

Answer: **No; the clinical notes consistently state that the patient has never smoked, most recently in the note dated 2019-01-10.**

Cards this sentence cites:

- `[DocumentReference/d7c0c753-f1ba-0f21-189c-0603918a2545#1]` Clinical note | 2019-01-10 | part 1 of 2 | 2019-01-10 # Chief Complaint - Hunger - Thirst - Fatigue - Frequent Urination # History of Present Illness Jimmie93 is a 69 year-old nonhispanic black male. Patient has a history of cellulitis and abscess of mouth, inflammatory conditions of jaws, part-time employment (finding), medication review due (situation), not in labor force (finding), full-time employment (finding), viral sinusitis (disorder), social isolation (finding), stress (finding). # Social History Patient is married. Patient has never smoked. Patient identifies as heterosexual. Patient comes from a high socioeconomic background. Patient has completed some college courses. Patient currently has Medicare. # Allergies No Known Allergies. # Medications lisinopril 10 mg oral tablet; hydrochlorothiazide 25 mg oral tablet
- `[DocumentReference/f13bc7f0-cee1-04f7-02dc-359026b0ed03#1]` Clinical note | 2015-12-24 | part 1 of 1 | 2015-12-24 # Chief Complaint - Hunger - Thirst - Fatigue - Frequent Urination # History of Present Illness Jimmie93 is a 66 year-old nonhispanic black male. Patient has a history of cellulitis and abscess of mouth, inflammatory conditions of jaws, medication review due (situation). # Social History Patient is married. Patient has never smoked. Patient identifies as heterosexual. Patient comes from a high socioeconomic background. Patient has completed some college courses. Patient currently has Medicare. # Allergies No Known Allergies. # Medications No Active Medications. # Assessment and Plan Patient is presenting with not in labor force (finding), social isolation (finding). ## Plan The patient was prescribed the following medications: - hydrochlorothiazide 25 mg oral tablet - lisinopril 10 mg oral tablet
- `[DocumentReference/b7b727da-7f08-c2f6-639f-1be007d8f9c6#1]` Clinical note | 2014-12-18 | part 1 of 1 | 2014-12-18 # Chief Complaint - Hunger - Thirst - Fatigue - Frequent Urination # History of Present Illness Jimmie93 is a 65 year-old nonhispanic black male. Patient has a history of cellulitis and abscess of mouth. # Social History Patient is married. Patient has never smoked. Patient identifies as heterosexual. Patient comes from a high socioeconomic background. Patient has completed some college courses. Patient currently has Medicare. # Allergies No Known Allergies. # Medications No Active Medications. # Assessment and Plan Patient is presenting with medication review due (situation). ## Plan
- `[DocumentReference/898dce84-1e0a-27d9-1691-3b7edc896832#1]` Clinical note | 1986-03-01 | part 1 of 1 | 1986-03-01 # Chief Complaint - Hunger - Thirst - Fatigue - Frequent Urination # History of Present Illness Jimmie93 is a 36 year-old nonhispanic black male. # Social History Patient is married. Patient has never smoked. Patient identifies as heterosexual. Patient comes from a high socioeconomic background. Patient has completed some college courses. Patient currently has NO INSURANCE. # Allergies No Known Allergies. # Medications No Active Medications. # Assessment and Plan Patient is presenting with sleep disorder (disorder). ## Plan

<details><summary>Everything the model saw (41 cards)</summary>

```text
[Condition/772fc930-5418-0bfa-5baf-97b1667a332f] Condition | onset 2026-07-09 | Part-time employment (finding) | clinical status active | SNOMED 160904001
[Condition/772fc930-5418-0bfa-446c-c28d224cff31] Condition | onset 2026-06-25 | Medication review due (situation) | clinical status active | SNOMED 314529007
[Condition/772fc930-5418-0bfa-33d9-881f0ecc07c1] Condition | onset 2026-06-11 | Stress (finding) | clinical status active | SNOMED 73595000
[Condition/772fc930-5418-0bfa-d3cc-a2daa4832199] Condition | onset 2026-02-19 | Chronic kidney disease stage 3 (disorder) | clinical status active | SNOMED 433144002
[Condition/772fc930-5418-0bfa-600b-5558ca66220a] Condition | onset 2026-02-19 | Proteinuria due to type 2 diabetes mellitus (disorder) | clinical status active | SNOMED 157141000119108
[Condition/772fc930-5418-0bfa-6352-6c3984966ef8] Condition | onset 2025-02-13 | Hyperlipidemia (disorder) | clinical status active | SNOMED 55822004
[Condition/772fc930-5418-0bfa-bb6d-8a0b90cf95e4] Condition | onset 2020-01-16 | Microalbuminuria due to type 2 diabetes mellitus (disorder) | clinical status active | SNOMED 90781000119102
[Condition/772fc930-5418-0bfa-ab71-24a74b1745fd] Condition | onset 2020-01-16 | Chronic kidney disease stage 2 (disorder) | clinical status active | SNOMED 431856006
[Condition/772fc930-5418-0bfa-beac-a103fe7f3fd2] Condition | onset 2019-01-10 | Disorder of kidney due to diabetes mellitus (disorder) | clinical status active | SNOMED 127013003
[Condition/772fc930-5418-0bfa-2c4f-3f5ed5953c36] Condition | onset 2019-01-10 | Chronic kidney disease stage 1 (disorder) | clinical status active | SNOMED 431855005
[Condition/772fc930-5418-0bfa-3873-02589386889d] Condition | onset 2004-06-19 | Osteoarthritis of hip (disorder) | clinical status active | SNOMED 239872002
[Condition/772fc930-5418-0bfa-a4a0-5eff492015a6] Condition | onset 1991-08-28 | History of coronary artery bypass grafting (situation) | clinical status active | SNOMED 399261000
[Condition/772fc930-5418-0bfa-01dc-3613408a83a6] Condition | onset 1991-08-22 | Abnormal findings diagnostic imaging heart+coronary circulat (finding) | clinical status active | SNOMED 274531002
[Condition/772fc930-5418-0bfa-35d2-44b4eb4fcccc] Condition | onset 1991-08-08 | Ischemic heart disease (disorder) | clinical status active | SNOMED 414545008
[Condition/772fc930-5418-0bfa-43ec-8fdd443cc6ce] Condition | onset 1988-07-21 | Gingivitis (disorder) | clinical status active | SNOMED 66383009
[Condition/772fc930-5418-0bfa-91e4-e46a214921b9] Condition | onset 1986-07-10 | Prediabetes (finding) | clinical status active | SNOMED 714628002
[Condition/772fc930-5418-0bfa-47df-a943ca27aa29] Condition | onset 1986-07-10 | Anemia (disorder) | clinical status active | SNOMED 271737000
[Condition/772fc930-5418-0bfa-7d09-0ea3ca1e93ba] Condition | onset 1986-03-30 | Obstructive sleep apnea syndrome (disorder) | clinical status active | SNOMED 78275009
[Condition/772fc930-5418-0bfa-1be5-06b5144b5817] Condition | onset 1986-03-01 | Sleep disorder (disorder) | clinical status active | SNOMED 39898005
[Condition/772fc930-5418-0bfa-0cdf-ac369e474ff3] Condition | onset 1977-05-19 | Essential hypertension (disorder) | clinical status active | SNOMED 59621000
[Condition/772fc930-5418-0bfa-f6df-7e2448081e0f] Condition | onset 1967-05-04 | Received higher education (finding) | clinical status active | SNOMED 224299000
[Condition/772fc930-5418-0bfa-ffbe-e3692c7542d7] Condition | onset 1964-01-15 | Chronic sinusitis (disorder) | clinical status active | SNOMED 40055000
[MedicationRequest/772fc930-5418-0bfa-d2b4-bc5609421614] MedicationRequest | prescribed 2026-07-16 | insulin isophane, human 70 UNT/ML / insulin, regular, human 30 UNT/ML Injectable Suspension [Humulin] | status active | reason: Prediabetes (finding) | RxNorm 106892
[MedicationRequest/772fc930-5418-0bfa-35ed-4b81c08cb46e] MedicationRequest | prescribed 2026-07-16 | Hydrochlorothiazide 25 MG Oral Tablet | status active | reason: Essential hypertension (disorder) | RxNorm 310798
[MedicationRequest/772fc930-5418-0bfa-0d23-3b3c40dabcae] MedicationRequest | prescribed 2026-07-16 | lisinopril 10 MG Oral Tablet | status active | reason: Essential hypertension (disorder) | RxNorm 314076
[MedicationRequest/772fc930-5418-0bfa-ac79-a5117bd68db1] MedicationRequest | prescribed 2026-03-06 | Simvastatin 10 MG Oral Tablet | status active | reason: Hyperlipidemia (disorder) | RxNorm 314231
[MedicationRequest/772fc930-5418-0bfa-dfc7-922f9300bced] MedicationRequest | prescribed 2004-06-19 | Naproxen sodium 220 MG Oral Tablet | status active | reason: Osteoarthritis of hip (disorder) | RxNorm 849574
[Encounter/772fc930-5418-0bfa-dd45-e4b82fc97e3d] Encounter | 2026-07-23 | Encounter for check up (procedure) | class AMB | at BOSTON MEDICAL CENTER CORPORATION-
[Encounter/772fc930-5418-0bfa-6606-662b1312d21c] Encounter | 2026-07-16 | Urgent care clinic (environment) | class AMB | at LYNN URGENT CARE LLC
[Encounter/772fc930-5418-0bfa-54c7-a3b13e8997b9] Encounter | 2026-07-09 | Emergency room admission (procedure) | class EMER | at LEONARD FLORENCE CENTER FOR LIVING
[Immunization/772fc930-5418-0bfa-fcca-2fca6db3fac3] Immunization | 2026-02-19 | Influenza, split virus, trivalent, PF | status completed | CVX 140
[DocumentReference/aa9a00bd-5594-50a1-dee0-8273d2f39041#1] Clinical note | 1991-08-08 | part 1 of 1 | 1991-08-08 # Chief Complaint - Hunger - Thirst - Fatigue - Frequent Urination # History of Present Illness Jimmie93 is a 42 year-old nonhispanic black male. # Social History Patient is married. Patient has never smoked. Patient identifies as heterosexual. Patient comes from a high socioeconomic background. Patient has completed some college courses. Patient currently has Medicare. # Allergies No Known Allergies. # Medications No Active Medications. # Assessment and Plan Patient is presenting with ischemic heart disease (disorder). ## Plan
[DocumentReference/b7b727da-7f08-c2f6-639f-1be007d8f9c6#1] Clinical note | 2014-12-18 | part 1 of 1 | 2014-12-18 # Chief Complaint - Hunger - Thirst - Fatigue - Frequent Urination # History of Present Illness Jimmie93 is a 65 year-old nonhispanic black male. Patient has a history of cellulitis and abscess of mouth. # Social History Patient is married. Patient has never smoked. Patient identifies as heterosexual. Patient comes from a high socioeconomic background. Patient has completed some college courses. Patient currently has Medicare. # Allergies No Known Allergies. # Medications No Active Medications. # Assessment and Plan Patient is presenting with medication review due (situation). ## Plan
[DocumentReference/5c86cd72-f855-67ca-0c26-9d891b964309#1] Clinical note | 1991-08-22 | part 1 of 1 | 1991-08-22 # Chief Complaint - Hunger - Thirst - Fatigue - Frequent Urination # History of Present Illness Jimmie93 is a 42 year-old nonhispanic black male. # Social History Patient is married. Patient has never smoked. Patient identifies as heterosexual. Patient comes from a high socioeconomic background. Patient has completed some college courses. Patient currently has Medicare. # Allergies No Known Allergies. # Medications No Active Medications. # Assessment and Plan Patient is presenting with abnormal findings diagnostic imaging heart+coronary circulat (finding). ## Plan
[DocumentReference/e4967a2a-f9b1-faa2-f24a-6524f6b35cd6#1] Clinical note | 1991-08-28 | part 1 of 1 | 1991-08-28 # Chief Complaint - Hunger - Thirst - Fatigue - Frequent Urination # History of Present Illness Jimmie93 is a 42 year-old nonhispanic black male. # Social History Patient is married. Patient has never smoked. Patient identifies as heterosexual. Patient comes from a high socioeconomic background. Patient has completed some college courses. Patient currently has Medicare. # Allergies No Known Allergies. # Medications No Active Medications. # Assessment and Plan Patient is presenting with history of coronary artery bypass grafting (situation). ## Plan
[DocumentReference/d81b2a70-f84e-23e8-17bb-5eb77a04a148#1] Clinical note | 1986-03-29 | part 1 of 1 | 1986-03-29 # Chief Complaint - Hunger - Thirst - Fatigue - Frequent Urination # History of Present Illness Jimmie93 is a 37 year-old nonhispanic black male. # Social History Patient is married. Patient has never smoked. Patient identifies as heterosexual. Patient comes from a high socioeconomic background. Patient has completed some college courses. Patient currently has Medicare. # Allergies No Known Allergies. # Medications No Active Medications. # Assessment and Plan Patient is presenting with obstructive sleep apnea syndrome (disorder). ## Plan The patient was placed on a careplan: - care plan (record artifact)
[DocumentReference/f13bc7f0-cee1-04f7-02dc-359026b0ed03#1] Clinical note | 2015-12-24 | part 1 of 1 | 2015-12-24 # Chief Complaint - Hunger - Thirst - Fatigue - Frequent Urination # History of Present Illness Jimmie93 is a 66 year-old nonhispanic black male. Patient has a history of cellulitis and abscess of mouth, inflammatory conditions of jaws, medication review due (situation). # Social History Patient is married. Patient has never smoked. Patient identifies as heterosexual. Patient comes from a high socioeconomic background. Patient has completed some college courses. Patient currently has Medicare. # Allergies No Known Allergies. # Medications No Active Medications. # Assessment and Plan Patient is presenting with not in labor force (finding), social isolation (finding). ## Plan The patient was prescribed the following medications: - hydrochlorothiazide 25 mg oral tablet - lisinopril 10 mg oral tablet
[DocumentReference/d7c0c753-f1ba-0f21-189c-0603918a2545#1] Clinical note | 2019-01-10 | part 1 of 2 | 2019-01-10 # Chief Complaint - Hunger - Thirst - Fatigue - Frequent Urination # History of Present Illness Jimmie93 is a 69 year-old nonhispanic black male. Patient has a history of cellulitis and abscess of mouth, inflammatory conditions of jaws, part-time employment (finding), medication review due (situation), not in labor force (finding), full-time employment (finding), viral sinusitis (disorder), social isolation (finding), stress (finding). # Social History Patient is married. Patient has never smoked. Patient identifies as heterosexual. Patient comes from a high socioeconomic background. Patient has completed some college courses. Patient currently has Medicare. # Allergies No Known Allergies. # Medications lisinopril 10 mg oral tablet; hydrochlorothiazide 25 mg oral tablet
[DocumentReference/a6487051-167a-c18a-767f-3ffcfe6ec713#1] Clinical note | 2010-12-09 | part 1 of 1 | 2010-12-09 # Chief Complaint - Hunger - Thirst - Fatigue - Frequent Urination # History of Present Illness Jimmie93 is a 61 year-old nonhispanic black male. # Social History Patient is married. Patient has never smoked. Patient identifies as heterosexual. Patient comes from a high socioeconomic background. Patient has completed some college courses. Patient currently has Medicare. # Allergies No Known Allergies. # Medications No Active Medications. # Assessment and Plan Patient is presenting with cellulitis and abscess of mouth. ## Plan
[DocumentReference/898dce84-1e0a-27d9-1691-3b7edc896832#1] Clinical note | 1986-03-01 | part 1 of 1 | 1986-03-01 # Chief Complaint - Hunger - Thirst - Fatigue - Frequent Urination # History of Present Illness Jimmie93 is a 36 year-old nonhispanic black male. # Social History Patient is married. Patient has never smoked. Patient identifies as heterosexual. Patient comes from a high socioeconomic background. Patient has completed some college courses. Patient currently has NO INSURANCE. # Allergies No Known Allergies. # Medications No Active Medications. # Assessment and Plan Patient is presenting with sleep disorder (disorder). ## Plan
[DocumentReference/2221afb5-fe05-d0dc-79f1-97c10fa63e7b#1] Clinical note | 1988-07-21 | part 1 of 1 | 1988-07-21 # Chief Complaint - Hunger - Thirst - Fatigue - Frequent Urination # History of Present Illness Jimmie93 is a 39 year-old nonhispanic black male. # Social History Patient is married. Patient has never smoked. Patient identifies as heterosexual. Patient comes from a high socioeconomic background. Patient has completed some college courses. Patient currently has Medicare. # Allergies No Known Allergies. # Medications No Active Medications. # Assessment and Plan Patient is presenting with gingivitis (disorder). ## Plan
```

</details>

label: s
note: All ten clinical notes seen (1986-03-01 through 2019-01-10) say 'Patient has never smoked', and none is later than 2019-01-10, so both 'consistently' and 'most recently 2019-01-10' hold; no contradicting smoking observation was seen.

## 44. `latest-lipid-panel:e56a8cde#0#0`

Question: What did the patient's most recent lipid panel show?

Answer: **The most recent lipid panel with direct LDL, dated 2026-01-01, showed total cholesterol 159.93 mg/dL, triglycerides 199.6 mg/dL, direct LDL cholesterol 122.86 mg/dL, and HDL cholesterol 54.093 mg/dL.** It was drawn at a hyperlipidemia follow-up visit, after which simvastatin 10 mg oral tablet was prescribed.

Cards this sentence cites:

- `[DiagnosticReport/e56a8cde-8395-a37d-dec2-ff39cdb530e3]` DiagnosticReport | 2026-01-01 | Lipid panel with direct LDL - Serum or Plasma | results: Cholesterol [Mass/volume] in Serum or Plasma 159.93 mg/dL; Triglyceride [Mass/volume] in Serum or Plasma 199.6 mg/dL; Cholesterol in LDL [Mass/volume] in Serum or Plasma by Direct assay 122.86 mg/dL; Cholesterol in HDL [Mass/volume] in Serum or Plasma 54.093 mg/dL | LOINC 57698-3

<details><summary>Everything the model saw (56 cards)</summary>

```text
[Condition/e56a8cde-8395-a37d-f7ae-15d35f13e9f0] Condition | onset 2025-12-25 | Victim of intimate partner abuse (finding) | clinical status active | SNOMED 706893006
[Condition/e56a8cde-8395-a37d-80d3-3984f14d8bb3] Condition | onset 2025-12-25 | Stress (finding) | clinical status active | SNOMED 73595000
[Condition/e56a8cde-8395-a37d-5c7c-75429c6f1e56] Condition | onset 2025-12-25 | Medication review due (situation) | clinical status active | SNOMED 314529007
[Condition/e56a8cde-8395-a37d-354e-df92238c35a7] Condition | onset 2025-12-25 | Unemployed (finding) | clinical status active | SNOMED 73438004
[Condition/e56a8cde-8395-a37d-6690-7ef5746552bd] Condition | onset 2017-11-09 | Hyperlipidemia (disorder) | clinical status active | SNOMED 55822004
[Condition/e56a8cde-8395-a37d-922a-d32061194c0b] Condition | onset 2016-11-03 | Gingivitis (disorder) | clinical status active | SNOMED 66383009
[Condition/e56a8cde-8395-a37d-e775-23849ffbe97b] Condition | onset 2014-02-01 | Chronic low back pain (finding) | clinical status active | SNOMED 278860009
[Condition/e56a8cde-8395-a37d-a82c-6129bc784139] Condition | onset 2014-02-01 | Chronic pain (finding) | clinical status active | SNOMED 82423001
[Condition/e56a8cde-8395-a37d-64b8-86023f198a46] Condition | onset 2014-02-01 | Chronic neck pain (finding) | clinical status active | SNOMED 1121000119107
[Condition/e56a8cde-8395-a37d-e547-8e085bacfa8e] Condition | onset 2007-09-13 | Has a criminal record (finding) | clinical status active | SNOMED 266948004
[Condition/e56a8cde-8395-a37d-37b4-500cf9e797e9] Condition | onset 2005-09-01 | Osteoporosis (disorder) | clinical status active | SNOMED 64859006
[Condition/e56a8cde-8395-a37d-d5cb-6239a28a0055] Condition | onset 2003-12-16 | History of myocardial infarction (situation) | clinical status active | SNOMED 399211009
[Condition/e56a8cde-8395-a37d-4d5f-670d3e1632bc] Condition | onset 2003-12-16 | Acute non-ST segment elevation myocardial infarction (disorder) | clinical status active | SNOMED 401314000
[Condition/e56a8cde-8395-a37d-1853-568436ee1ea2] Condition | onset 2001-08-20 | History of coronary artery bypass grafting (situation) | clinical status active | SNOMED 399261000
[Condition/e56a8cde-8395-a37d-810b-643d651149ba] Condition | onset 2001-08-18 | Abnormal findings diagnostic imaging heart+coronary circulat (finding) | clinical status active | SNOMED 274531002
[Condition/e56a8cde-8395-a37d-2761-7d0bfc799087] Condition | onset 2001-08-09 | Ischemic heart disease (disorder) | clinical status active | SNOMED 414545008
[Condition/e56a8cde-8395-a37d-ed31-c4144dbefb9e] Condition | onset 1996-05-17 | Osteoarthritis of knee (disorder) | clinical status active | SNOMED 239873007
[Condition/e56a8cde-8395-a37d-333f-0835bee4de98] Condition | onset 1991-06-13 | Essential hypertension (disorder) | clinical status active | SNOMED 59621000
[Condition/e56a8cde-8395-a37d-30cd-5f4f9de67da3] Condition | onset 1967-07-27 | Lack of access to transportation (finding) | clinical status active | SNOMED 713458007
[Condition/e56a8cde-8395-a37d-ac70-0b466edf16a1] Condition | onset 1963-07-18 | Transport problem (finding) | clinical status active | SNOMED 266934004
[Condition/e56a8cde-8395-a37d-99e6-93fe1e3f6036] Condition | onset 1963-07-18 | Only received primary school education (finding) | clinical status active | SNOMED 224295006
[MedicationRequest/e56a8cde-8395-a37d-0c1b-7da0b396a0c4] MedicationRequest | prescribed 2026-01-01 | Simvastatin 10 MG Oral Tablet | status active | reason: Hyperlipidemia (disorder) | RxNorm 314231
[MedicationRequest/e56a8cde-8395-a37d-f153-06ed5ef5b40a] MedicationRequest | prescribed 2025-12-25 | Alendronic acid 10 MG Oral Tablet | status active | reason: Osteoporosis (disorder) | RxNorm 904419
[MedicationRequest/e56a8cde-8395-a37d-b70b-d6ff9e66fb91] MedicationRequest | prescribed 2025-12-25 | Acetaminophen 325 MG Oral Tablet [Tylenol] | status active | RxNorm 209387
[MedicationRequest/e56a8cde-8395-a37d-1cff-386c29158923] MedicationRequest | prescribed 2025-12-25 | lisinopril 10 MG Oral Tablet | status active | reason: Essential hypertension (disorder) | RxNorm 314076
[MedicationRequest/e56a8cde-8395-a37d-f778-f1044e9a8316] MedicationRequest | prescribed 2003-12-16 | atorvastatin 10 MG Oral Tablet | status active | RxNorm 617312
[MedicationRequest/e56a8cde-8395-a37d-e36e-ab680e0ad841] MedicationRequest | prescribed 2003-12-16 | hydrochlorothiazide 25 MG / lisinopril 20 MG Oral Tablet | status active | RxNorm 197887
[MedicationRequest/e56a8cde-8395-a37d-d237-6e376bbcb9a6] MedicationRequest | prescribed 2003-12-16 | metoprolol tartrate 25 MG Oral Tablet | status active | RxNorm 866924
[MedicationRequest/e56a8cde-8395-a37d-2fb4-edeac8b69b00] MedicationRequest | prescribed 2003-12-16 | prasugrel 10 MG Oral Tablet | status active | RxNorm 855812
[MedicationRequest/e56a8cde-8395-a37d-228f-f6135c165caa] MedicationRequest | prescribed 2003-12-16 | aspirin 81 MG Oral Tablet | status active | RxNorm 243670
[MedicationRequest/e56a8cde-8395-a37d-eee1-8d05287f0e29] MedicationRequest | prescribed 2001-08-16 | Nitroglycerin 0.4 MG/ACTUAT Mucosal Spray | status active | RxNorm 705129
[MedicationRequest/e56a8cde-8395-a37d-d36b-2e3fc9df975e] MedicationRequest | prescribed 2001-08-16 | 24 HR metoprolol succinate 100 MG Extended Release Oral Tablet | status active | RxNorm 866412
[MedicationRequest/e56a8cde-8395-a37d-a8c0-f9ed9ed3ea83] MedicationRequest | prescribed 2001-08-16 | Clopidogrel 75 MG Oral Tablet | status active | RxNorm 309362
[MedicationRequest/e56a8cde-8395-a37d-321f-ecd1d25263ad] MedicationRequest | prescribed 2001-08-16 | Simvastatin 20 MG Oral Tablet | status active | RxNorm 312961
[MedicationRequest/e56a8cde-8395-a37d-9456-c58ec0c7de32] MedicationRequest | prescribed 1949-01-17 | diphenhydrAMINE Hydrochloride 25 MG Oral Tablet | status active | RxNorm 1049630
[AllergyIntolerance/e56a8cde-8395-a37d-b318-8f34a7d6b5f7] AllergyIntolerance | recorded 1946-06-09 | Animal dander (substance) | allergy, category environment, criticality low | clinical status active | reactions: Eruption of skin (disorder); Rhinoconjunctivitis (disorder) | SNOMED 264287008
[AllergyIntolerance/e56a8cde-8395-a37d-a098-9831a40ac85b] AllergyIntolerance | recorded 1946-06-09 | Mold (organism) | allergy, category environment, criticality low | clinical status active | SNOMED 84489001
[AllergyIntolerance/e56a8cde-8395-a37d-85d4-fe7519012219] AllergyIntolerance | recorded 1946-06-09 | House dust mite (organism) | allergy, category environment, criticality low | clinical status active | SNOMED 260147004
[AllergyIntolerance/e56a8cde-8395-a37d-60c2-b75e4a4d4513] AllergyIntolerance | recorded 1946-06-09 | Tree pollen (substance) | allergy, category environment, criticality low | clinical status active | SNOMED 782576004
[AllergyIntolerance/e56a8cde-8395-a37d-5834-224d1127b6f9] AllergyIntolerance | recorded 1946-06-09 | Grass pollen (substance) | allergy, category environment, criticality low | clinical status active | SNOMED 256277009
[AllergyIntolerance/e56a8cde-8395-a37d-2daa-dbe0dbcf6ecf] AllergyIntolerance | recorded 1946-06-09 | Shellfish (substance) | allergy, category food, criticality low | clinical status active | reactions: Dyspnea (finding); Allergic angioedema (disorder); Itching (finding); Cough (finding); Diarrhea (finding) | SNOMED 735029006
[AllergyIntolerance/e56a8cde-8395-a37d-1508-bdb84bdc4c5d] AllergyIntolerance | recorded 1946-06-09 | Allergic disposition (finding) | allergy, category environment, criticality low | clinical status active | SNOMED 609328004
[Encounter/e56a8cde-8395-a37d-9f47-5b69723a8690] Encounter | 2026-01-01 | Follow-up encounter (procedure) | class AMB | reason: Hyperlipidemia (disorder) | at DANA FARBER CANCER INSTITUTE
[Encounter/e56a8cde-8395-a37d-2450-250d53d64dc7] Encounter | 2025-12-25 | General examination of patient (procedure) | class AMB | at SOUTH SHORE PRIMARY CARE PC
[Encounter/e56a8cde-8395-a37d-20eb-f707e34a4164] Encounter | 2024-12-20 | Follow-up encounter (procedure) | class AMB | reason: Hyperlipidemia (disorder) | at DANA FARBER CANCER INSTITUTE
[Immunization/e56a8cde-8395-a37d-7cd1-bb3bac5572f3] Immunization | 2025-12-25 | Influenza, split virus, trivalent, PF | status completed | CVX 140
[DocumentReference/494317a8-1900-de5b-7b5a-de4de13287b2#2] Clinical note | 2026-01-01 | part 2 of 2 | # Assessment and Plan ## Plan The following lab reports were completed: - comprehensive metabolic 2000 panel - serum or plasma - lipid panel with direct ldl - serum or plasma The patient was prescribed the following medications: - simvastatin 10 mg oral tablet
[DocumentReference/b90b3a01-6a64-0ced-e3f1-7cfa3f1d1322#2] Clinical note | 2024-12-20 | part 2 of 2 | # Assessment and Plan ## Plan The following lab reports were completed: - comprehensive metabolic 2000 panel - serum or plasma - lipid panel with direct ldl - serum or plasma The patient was prescribed the following medications: - simvastatin 10 mg oral tablet
[DocumentReference/776858d3-4a9b-c831-91ff-7999eff89090#2] Clinical note | 2021-12-09 | part 2 of 2 | # Assessment and Plan ## Plan The following lab reports were completed: - comprehensive metabolic 2000 panel - serum or plasma - lipid panel with direct ldl - serum or plasma The patient was prescribed the following medications: - simvastatin 10 mg oral tablet
[DocumentReference/2e83ca5b-0566-c4f8-c3f6-ebd76fc34712#2] Clinical note | 2023-12-21 | part 2 of 2 | # Assessment and Plan ## Plan The following lab reports were completed: - comprehensive metabolic 2000 panel - serum or plasma - lipid panel with direct ldl - serum or plasma The patient was prescribed the following medications: - simvastatin 10 mg oral tablet
[DocumentReference/67c3d2e5-fd00-fa7a-99db-998bc532a3d1#2] Clinical note | 2022-12-09 | part 2 of 2 | # Assessment and Plan ## Plan The following lab reports were completed: - comprehensive metabolic 2000 panel - serum or plasma - lipid panel with direct ldl - serum or plasma The patient was prescribed the following medications: - simvastatin 10 mg oral tablet
[DocumentReference/dd13e7d2-1a65-f255-e97e-3d9ea0579bc7#2] Clinical note | 2017-11-09 | part 2 of 2 | # Assessment and Plan Patient is presenting with hyperlipidemia (disorder), stress (finding). ## Plan Patient was given the following immunizations: influenza, split virus, trivalent, pf. The following procedures were conducted: - assessment of health and social care needs (procedure) - assessment using morse fall scale (procedure) - assessment of substance use (procedure) - assessment using alcohol use disorders identification test - consumption (procedure) - patient referral for dental care (procedure) The following lab reports were completed: - lipid panel with direct ldl - serum or plasma - comprehensive metabolic 2000 panel - serum or plasma - morse fall scale panel - alcohol use disorder identification test - consumption [audit-c] The patient was prescribed the following medications: - acetaminophen 325 mg oral tablet [tylenol] - lisinopril 10 mg oral tablet - alendronic acid 10 mg oral tablet
[DocumentReference/b3013519-3000-7f68-7b32-de706218460e#2] Clinical note | 2018-11-15 | part 2 of 2 | # Assessment and Plan ## Plan Patient was given the following immunizations: influenza, split virus, trivalent, pf. The following procedures were conducted: - medication reconciliation (procedure) - assessment of health and social care needs (procedure) - assessment of anxiety (procedure) - depression screening (procedure) - depression screening (procedure) - assessment of substance use (procedure) - screening for drug abuse (procedure) - patient referral for dental care (procedure) The following lab reports were completed: - lipid panel with direct ldl - serum or plasma - generalized anxiety disorder 7 item (gad-7) - patient health questionnaire 2 item (phq-2) [reported] - drug abuse screening test-10 [dast-10] The patient was prescribed the following medications: - acetaminophen 325 mg oral tablet [tylenol] - lisinopril 10 mg oral tablet - alendronic acid 10 mg oral tablet
[DiagnosticReport/e56a8cde-8395-a37d-51bd-ee35b4a49d60] DiagnosticReport | 2024-12-20 | Lipid panel with direct LDL - Serum or Plasma | results: Cholesterol [Mass/volume] in Serum or Plasma 189.46 mg/dL; Triglyceride [Mass/volume] in Serum or Plasma 188.45 mg/dL; Cholesterol in LDL [Mass/volume] in Serum or Plasma by Direct assay 108.08 mg/dL; Cholesterol in HDL [Mass/volume] in Serum or Plasma 35.169 mg/dL | LOINC 57698-3
[DiagnosticReport/e56a8cde-8395-a37d-dec2-ff39cdb530e3] DiagnosticReport | 2026-01-01 | Lipid panel with direct LDL - Serum or Plasma | results: Cholesterol [Mass/volume] in Serum or Plasma 159.93 mg/dL; Triglyceride [Mass/volume] in Serum or Plasma 199.6 mg/dL; Cholesterol in LDL [Mass/volume] in Serum or Plasma by Direct assay 122.86 mg/dL; Cholesterol in HDL [Mass/volume] in Serum or Plasma 54.093 mg/dL | LOINC 57698-3
[DiagnosticReport/e56a8cde-8395-a37d-f210-2a71df24d2fa] DiagnosticReport | 2024-12-19 | Lipid panel with direct LDL - Serum or Plasma | results: Cholesterol [Mass/volume] in Serum or Plasma 255.6 mg/dL; Triglyceride [Mass/volume] in Serum or Plasma 125.17 mg/dL; Cholesterol in LDL [Mass/volume] in Serum or Plasma by Direct assay 176.14 mg/dL; Cholesterol in HDL [Mass/volume] in Serum or Plasma 54.43 mg/dL | LOINC 57698-3
```

</details>

label: s
note: Cited 2026-01-01 lipid panel lists 159.93, 199.6, 122.86 (direct LDL) and 54.093 mg/dL exactly; the other lipid panel reports seen are 2024-12-19 and 2024-12-20, so it is the most recent.

## 45. `latest-lipid-panel:d4f2a6f8#0#1`

Question: What did the patient's most recent lipid panel show?

Answer: The most recent lipid panel with direct LDL, dated 2026-04-02, showed total cholesterol 166.31 mg/dL, triglycerides 117.76 mg/dL, LDL cholesterol (direct assay) 83 mg/dL, and HDL cholesterol 59.76 mg/dL. **For comparison, the prior panel on 2023-03-23 showed total cholesterol 115.36 mg/dL, triglycerides 139.57 mg/dL, LDL 30.05 mg/dL, and HDL 57.4 mg/dL.**

Cards this sentence cites:

- `[DiagnosticReport/d4f2a6f8-e358-6b1b-0b7b-12c321876a96]` DiagnosticReport | 2023-03-23 | Lipid panel with direct LDL - Serum or Plasma | results: Cholesterol [Mass/volume] in Serum or Plasma 115.36 mg/dL; Triglyceride [Mass/volume] in Serum or Plasma 139.57 mg/dL; Cholesterol in LDL [Mass/volume] in Serum or Plasma by Direct assay 30.05 mg/dL; Cholesterol in HDL [Mass/volume] in Serum or Plasma 57.4 mg/dL | LOINC 57698-3

<details><summary>Everything the model saw (42 cards)</summary>

```text
[Condition/d4f2a6f8-e358-6b1b-a870-7578fc115ba3] Condition | onset 2026-04-02 | Stress (finding) | clinical status active | SNOMED 73595000
[Condition/d4f2a6f8-e358-6b1b-37cc-cacad982df8c] Condition | onset 2026-04-02 | Reports of violence in the environment (finding) | clinical status active | SNOMED 424393004
[Condition/d4f2a6f8-e358-6b1b-c78d-1b6bc447e34a] Condition | onset 2025-12-04 | Full-time employment (finding) | clinical status active | SNOMED 160903007
[Condition/d4f2a6f8-e358-6b1b-29d8-fc1e6a15e60d] Condition | onset 2025-12-04 | Medication review due (situation) | clinical status active | SNOMED 314529007
[Condition/d4f2a6f8-e358-6b1b-f1ac-92593f6454e7] Condition | onset 2025-03-20 | Chronic kidney disease stage 4 (disorder) | clinical status active | SNOMED 431857002
[Condition/d4f2a6f8-e358-6b1b-4959-9b97d2d3536d] Condition | onset 2025-02-03 | Awaiting transplantation of kidney (situation) | clinical status active | SNOMED 698306007
[Condition/d4f2a6f8-e358-6b1b-76dc-8902de051de4] Condition | onset 2022-10-20 | Microalbuminuria due to type 2 diabetes mellitus (disorder) | clinical status active | SNOMED 90781000119102
[Condition/d4f2a6f8-e358-6b1b-1e8b-4beeba77ed82] Condition | onset 2022-10-20 | Proteinuria due to type 2 diabetes mellitus (disorder) | clinical status active | SNOMED 157141000119108
[Condition/d4f2a6f8-e358-6b1b-042a-23b17f3aef58] Condition | onset 2022-10-20 | Chronic kidney disease stage 3 (disorder) | clinical status active | SNOMED 433144002
[Condition/d4f2a6f8-e358-6b1b-7e47-2334f6b84c0f] Condition | onset 2020-05-28 | History of coronary artery bypass grafting (situation) | clinical status active | SNOMED 399261000
[Condition/d4f2a6f8-e358-6b1b-ebe7-54c5d38117fc] Condition | onset 2020-03-19 | Abnormal findings diagnostic imaging heart+coronary circulat (finding) | clinical status active | SNOMED 274531002
[Condition/d4f2a6f8-e358-6b1b-e1e3-648cc0a38c11] Condition | onset 2020-03-05 | Chronic kidney disease stage 1 (disorder) | clinical status active | SNOMED 431855005
[Condition/d4f2a6f8-e358-6b1b-7f62-e48c3798c8b1] Condition | onset 2020-03-05 | Disorder of kidney due to diabetes mellitus (disorder) | clinical status active | SNOMED 127013003
[Condition/d4f2a6f8-e358-6b1b-6866-45937dfd6387] Condition | onset 2020-03-05 | Ischemic heart disease (disorder) | clinical status active | SNOMED 414545008
[Condition/d4f2a6f8-e358-6b1b-9d41-102804feed92] Condition | onset 2004-12-09 | Metabolic syndrome X (disorder) | clinical status active | SNOMED 237602007
[Condition/d4f2a6f8-e358-6b1b-4dab-6274d2854b00] Condition | onset 2002-11-28 | Anemia (disorder) | clinical status active | SNOMED 271737000
[Condition/d4f2a6f8-e358-6b1b-c5c9-83d1526dc404] Condition | onset 2001-11-22 | Essential hypertension (disorder) | clinical status active | SNOMED 59621000
[Condition/d4f2a6f8-e358-6b1b-d3db-555b40b7ebe5] Condition | onset 2000-05-04 | Prediabetes (finding) | clinical status active | SNOMED 714628002
[Condition/d4f2a6f8-e358-6b1b-4a76-ae3dfbf47144] Condition | onset 1986-11-06 | Body mass index 30+ - obesity (finding) | clinical status active | SNOMED 162864005
[Condition/d4f2a6f8-e358-6b1b-c732-3e05c6bfa924] Condition | onset 1982-10-28 | Only received primary school education (finding) | clinical status active | SNOMED 224295006
[MedicationRequest/d4f2a6f8-e358-6b1b-da40-22bfe510e33d] MedicationRequest | prescribed 2026-04-09 | Hydrochlorothiazide 25 MG Oral Tablet | status active | reason: Essential hypertension (disorder) | RxNorm 310798
[MedicationRequest/d4f2a6f8-e358-6b1b-b1c3-dd4b80a73ea4] MedicationRequest | prescribed 2026-04-09 | insulin isophane, human 70 UNT/ML / insulin, regular, human 30 UNT/ML Injectable Suspension [Humulin] | status active | reason: Prediabetes (finding) | RxNorm 106892
[MedicationRequest/d4f2a6f8-e358-6b1b-875e-3c108c25914e] MedicationRequest | prescribed 2026-04-09 | lisinopril 10 MG Oral Tablet | status active | reason: Essential hypertension (disorder) | RxNorm 314076
[MedicationRequest/d4f2a6f8-e358-6b1b-6913-a3ea2279b298] MedicationRequest | prescribed 2026-04-09 | amLODIPine 2.5 MG Oral Tablet | status active | reason: Essential hypertension (disorder) | RxNorm 308136
[MedicationRequest/d4f2a6f8-e358-6b1b-f33b-aeabe5d3ea2a] MedicationRequest | prescribed 2020-03-12 | Simvastatin 20 MG Oral Tablet | status active | RxNorm 312961
[MedicationRequest/d4f2a6f8-e358-6b1b-da7b-92b61020d936] MedicationRequest | prescribed 2020-03-12 | Nitroglycerin 0.4 MG/ACTUAT Mucosal Spray | status active | RxNorm 705129
[MedicationRequest/d4f2a6f8-e358-6b1b-c7c5-6dd35faf2d76] MedicationRequest | prescribed 2020-03-12 | 24 HR metoprolol succinate 100 MG Extended Release Oral Tablet | status active | RxNorm 866412
[MedicationRequest/d4f2a6f8-e358-6b1b-102e-595eecaa5a85] MedicationRequest | prescribed 2020-03-12 | Clopidogrel 75 MG Oral Tablet | status active | RxNorm 309362
[Encounter/d4f2a6f8-e358-6b1b-1745-afd1215948c6] Encounter | 2026-09-23 | Encounter for problem (procedure) | class AMB | reason: Chronic kidney disease stage 4 (disorder) | at TEWKSBURY HOSPITAL
[Encounter/d4f2a6f8-e358-6b1b-3133-f32329c08d3e] Encounter | 2026-09-20 | Encounter for problem (procedure) | class AMB | reason: Chronic kidney disease stage 4 (disorder) | at TEWKSBURY HOSPITAL
[Encounter/d4f2a6f8-e358-6b1b-0f9b-7fe2ad9bcba8] Encounter | 2026-09-20 | Encounter for problem (procedure) | class AMB | reason: Chronic kidney disease stage 4 (disorder) | at TEWKSBURY HOSPITAL
[Immunization/d4f2a6f8-e358-6b1b-d852-5d7c3a4a2175] Immunization | 2026-03-05 | Influenza, split virus, trivalent, PF | status completed | CVX 140
[DocumentReference/f9a870be-7889-8e8d-72f6-c36f4e1a0058#2] Clinical note | 2020-04-27 | part 2 of 2 | # Assessment and Plan ## Plan The following procedures were conducted: - pre-surgery testing (procedure) - blood group typing (procedure) - electrocardiographic procedure (procedure) - plain x-ray of chest (procedure) - echocardiography (procedure) - notification of treatment plan (procedure) - scheduling (procedure) The following lab reports were completed: - cbc panel - blood by automated count - comprehensive metabolic 2000 panel - serum or plasma - pt panel - platelet poor plasma by coagulation assay - gas panel - arterial blood - lipid panel with direct ldl - serum or plasma - troponin i.cardiac panel - serum or plasma by high sensitivity method - urinalysis complete panel - urine - heart failure tracking panel
[DocumentReference/5ca19742-951a-484d-1ff7-d909beff8198#2] Clinical note | 2020-05-28 | part 2 of 2 | # Assessment and Plan ## Plan The following procedures were conducted: - removal of endotracheal tube (procedure) - electrocardiographic procedure (procedure) - plain x-ray of chest (procedure) - transfusion of packed red blood cells (procedure) - discharge to ward (procedure) The following lab reports were completed: - cbc panel - blood by automated count - comprehensive metabolic 2000 panel - serum or plasma - pt panel - platelet poor plasma by coagulation assay - gas panel - arterial blood - lipid panel with direct ldl - serum or plasma - cbc panel - blood by automated count - comprehensive metabolic 2000 panel - serum or plasma - pt panel - platelet poor plasma by coagulation assay - gas panel - arterial blood - lipid panel with direct ldl - serum or plasma
[DocumentReference/c0403aba-dae6-8e34-dce7-cf9f05f3e73b#2] Clinical note | 2020-03-05 | part 2 of 3 | # Assessment and Plan Patient is presenting with medication review due (situation), chronic kidney disease stage 1 (disorder), disorder of kidney due to diabetes mellitus (disorder), ischemic heart disease (disorder), not in labor force (finding). ## Plan Patient was given the following immunizations: influenza, split virus, trivalent, pf. The following procedures were conducted: - medication reconciliation (procedure) - assessment of health and social care needs (procedure) - assessment of anxiety (procedure) - depression screening (procedure) - depression screening (procedure) - assessment of substance use (procedure) - assessment using alcohol use disorders identification test - consumption (procedure) - patient referral for dental care (procedure) The following lab reports were completed: - basic metabolic 2000 panel - serum or plasma - urinalysis macro (dipstick) panel - urine - basic metabolic panel - blood - lipid panel with direct ldl - serum or plasma - generalized anxiety disorder 7 item (gad-7) - patient health questionnaire 2 item (phq-2) [reported] - alcohol use disorder identification test - consumption [audit-c] The patient was prescribed the following medications: - hydrochlorothiazide 25 mg oral tablet - lisinopril 10 mg oral tablet - amlodipine 2.5 mg oral tablet - insulin isophane, human 70 unt/ml / insulin, regular, human
[DocumentReference/5fb9f00e-8c42-cf29-899f-29594f9910f0#3] Clinical note | 2024-03-28 | part 3 of 3 | # Assessment and Plan Patient is presenting with medication review due (situation). ## Plan Patient was given the following immunizations: influenza, split virus, trivalent, pf. The following procedures were conducted: - assessment of health and social care needs (procedure) - assessment of substance use (procedure) - assessment using alcohol use disorders identification test - consumption (procedure) The following lab reports were completed: - basic metabolic 2000 panel - serum or plasma - urinalysis macro (dipstick) panel - urine - basic metabolic panel - blood - cbc panel - blood by automated count - alcohol use disorder identification test - consumption [audit-c] The patient was prescribed the following medications: - insulin isophane, human 70 unt/ml / insulin, regular, human 30 unt/ml injectable suspension [humulin] - hydrochlorothiazide 25 mg oral tablet - lisinopril 10 mg oral tablet - amlodipine 2.5 mg oral tablet
[DocumentReference/d591421c-a831-e41a-009e-9b23c4d978ff#2] Clinical note | 2017-02-16 | part 2 of 2 | # Assessment and Plan Patient is presenting with medication review due (situation), full-time employment (finding), stress (finding). ## Plan Patient was given the following immunizations: influenza, split virus, trivalent, pf. The following procedures were conducted: - medication reconciliation (procedure) - assessment of health and social care needs (procedure) - assessment of anxiety (procedure) - depression screening (procedure) - depression screening (procedure) - assessment of substance use (procedure) - screening for drug abuse (procedure) The following lab reports were completed: - basic metabolic panel - blood - lipid panel with direct ldl - serum or plasma - generalized anxiety disorder 7 item (gad-7) - patient health questionnaire 2 item (phq-2) [reported] - drug abuse screening test-10 [dast-10] The patient was prescribed the following medications: - hydrochlorothiazide 25 mg oral tablet - lisinopril 10 mg oral tablet - amlodipine 2.5 mg oral tablet
[DocumentReference/d14a00de-037c-a93e-2514-73738a292ccd#2] Clinical note | 2021-07-29 | part 2 of 2 | # Assessment and Plan Patient is presenting with medication review due (situation), part-time employment (finding). ## Plan The following procedures were conducted: - assessment of health and social care needs (procedure) - assessment of substance use (procedure) - assessment using alcohol use disorders identification test - consumption (procedure) The following lab reports were completed: - basic metabolic 2000 panel - serum or plasma - urinalysis macro (dipstick) panel - urine - basic metabolic panel - blood - alcohol use disorder identification test - consumption [audit-c] The patient was prescribed the following medications: - insulin isophane, human 70 unt/ml / insulin, regular, human 30 unt/ml injectable suspension [humulin] - hydrochlorothiazide 25 mg oral tablet - lisinopril 10 mg oral tablet - amlodipine 2.5 mg oral tablet
[DiagnosticReport/d4f2a6f8-e358-6b1b-429c-06ce628aa51e] DiagnosticReport | 2017-02-16 | Lipid panel with direct LDL - Serum or Plasma | results: Cholesterol [Mass/volume] in Serum or Plasma 209.81 mg/dL; Triglyceride [Mass/volume] in Serum or Plasma 121.95 mg/dL; Cholesterol in LDL [Mass/volume] in Serum or Plasma by Direct assay 126.98 mg/dL; Cholesterol in HDL [Mass/volume] in Serum or Plasma 58.44 mg/dL | LOINC 57698-3
[DiagnosticReport/d4f2a6f8-e358-6b1b-be08-0c4edd9933df] DiagnosticReport | 2026-04-02 | Lipid panel with direct LDL - Serum or Plasma | results: Cholesterol [Mass/volume] in Serum or Plasma 166.31 mg/dL; Triglyceride [Mass/volume] in Serum or Plasma 117.76 mg/dL; Cholesterol in LDL [Mass/volume] in Serum or Plasma by Direct assay 83 mg/dL; Cholesterol in HDL [Mass/volume] in Serum or Plasma 59.76 mg/dL | LOINC 57698-3
[DiagnosticReport/d4f2a6f8-e358-6b1b-0b7b-12c321876a96] DiagnosticReport | 2023-03-23 | Lipid panel with direct LDL - Serum or Plasma | results: Cholesterol [Mass/volume] in Serum or Plasma 115.36 mg/dL; Triglyceride [Mass/volume] in Serum or Plasma 139.57 mg/dL; Cholesterol in LDL [Mass/volume] in Serum or Plasma by Direct assay 30.05 mg/dL; Cholesterol in HDL [Mass/volume] in Serum or Plasma 57.4 mg/dL | LOINC 57698-3
[DiagnosticReport/d4f2a6f8-e358-6b1b-1152-52e4df07c94a] DiagnosticReport | 2020-05-29 | Lipid panel with direct LDL - Serum or Plasma | results: Cholesterol [Mass/volume] in Serum or Plasma 141.58 mg/dL; Triglyceride [Mass/volume] in Serum or Plasma 101.99 mg/dL; Cholesterol in LDL [Mass/volume] in Serum or Plasma by Direct assay 67.4 mg/dL; Cholesterol in HDL [Mass/volume] in Serum or Plasma 53.78 mg/dL | LOINC 57698-3
```

</details>

label: s
note: Cited 2023-03-23 panel shows 115.36, 139.57, 30.05 and 57.4 mg/dL exactly; lipid panels seen are 2017-02-16, 2020-05-29, 2023-03-23 and 2026-04-02, so 2023-03-23 is the panel just before the latest one.

## 46. `smoking-status:ef5e136c#0#0`

Question: Does the patient smoke?

Answer: **No, the clinical notes state that the patient has never smoked, most recently in the note dated 2026-05-27.**

Cards this sentence cites:

- `[DocumentReference/12d16d0b-f49d-b245-c3db-8bd524abd1db#2]` Clinical note | 2026-05-27 | part 2 of 2 | # Social History Patient is single. Patient has never smoked. Patient identifies as heterosexual. Patient comes from a high socioeconomic background. Patient is a college graduate. Patient currently has Medicare. # Allergies No Known Allergies. # Medications lisinopril 10 mg oral tablet; tropicamide 5 mg/ml ophthalmic solution; 1 ml epoetin alfa 4000 unt/ml injection [epogen]; hydrochlorothiazide 25 mg oral tablet; amoxicillin 250 mg oral capsule; acetaminophen 325 mg / oxycodone hydrochloride 5 mg oral tablet; 120 actuat fluticasone propionate 0.044 mg/actuat metered dose inhaler [flovent]; amlodipine 2.5 mg oral tablet; insulin isophane, human 70 unt/ml / insulin, regular, human 30 unt/ml injectable suspension [humulin]; albuterol 0.83 mg/ml inhalation solution; naproxen sodium 220 mg oral tablet # Assessment and Plan Patient is presenting with medication review due (situation). ## Plan The patient was prescribed the following medications: - insulin isophane, human 70 unt/ml / insulin, regular, human 30 unt/ml injectable suspension [humulin] - hydrochlorothiazide 25 mg oral tablet - 120 actuat fluticasone propionate 0.044 mg/actuat metered dose inhaler [flovent] - lisinopril 10 mg oral tablet - amlodipine 2.5 mg oral tablet - albuterol 0.83 mg/ml inhalation solution
- `[DocumentReference/88f70ab4-f37e-aefe-89d9-041f04209b91#2]` Clinical note | 2025-11-12 | part 2 of 2 | # Social History Patient is single. Patient has never smoked. Patient identifies as heterosexual. Patient comes from a high socioeconomic background. Patient is a college graduate. Patient currently has Medicare. # Allergies No Known Allergies. # Medications lisinopril 10 mg oral tablet; tropicamide 5 mg/ml ophthalmic solution; 1 ml epoetin alfa 4000 unt/ml injection [epogen]; hydrochlorothiazide 25 mg oral tablet; amoxicillin 250 mg oral capsule; acetaminophen 325 mg / oxycodone hydrochloride 5 mg oral tablet; 120 actuat fluticasone propionate 0.044 mg/actuat metered dose inhaler [flovent]; amlodipine 2.5 mg oral tablet; insulin isophane, human 70 unt/ml / insulin, regular, human 30 unt/ml injectable suspension [humulin]; albuterol 0.83 mg/ml inhalation solution; naproxen sodium 220 mg oral tablet # Assessment and Plan Patient is presenting with medication review due (situation). ## Plan The patient was prescribed the following medications: - insulin isophane, human 70 unt/ml / insulin, regular, human 30 unt/ml injectable suspension [humulin] - hydrochlorothiazide 25 mg oral tablet - 120 actuat fluticasone propionate 0.044 mg/actuat metered dose inhaler [flovent] - lisinopril 10 mg oral tablet - amlodipine 2.5 mg oral tablet - albuterol 0.83 mg/ml inhalation solution

<details><summary>Everything the model saw (47 cards)</summary>

```text
[Condition/ef5e136c-ff1e-0695-1f8c-935a12106cac] Condition | onset 2026-09-30 | Medication review due (situation) | clinical status active | SNOMED 314529007
[Condition/ef5e136c-ff1e-0695-7e5d-470b95f60db2] Condition | onset 2026-09-23 | Social isolation (finding) | clinical status active | SNOMED 422650009
[Condition/ef5e136c-ff1e-0695-9d2d-c4be459bc9f4] Condition | onset 2026-09-09 | Unemployed (finding) | clinical status active | SNOMED 73438004
[Condition/ef5e136c-ff1e-0695-7b9c-f43e5ca3f6c6] Condition | onset 2026-08-12 | Stress (finding) | clinical status active | SNOMED 73595000
[Condition/ef5e136c-ff1e-0695-aa04-94486c99258f] Condition | onset 2025-08-27 | End-stage renal disease (disorder) | clinical status active | SNOMED 46177005
[Condition/ef5e136c-ff1e-0695-423f-ed71d76e81e3] Condition | onset 2025-03-30 | Awaiting transplantation of kidney (situation) | clinical status active | SNOMED 698306007
[Condition/ef5e136c-ff1e-0695-71df-3a96389b0a39] Condition | onset 2025-02-05 | Chronic kidney disease stage 4 (disorder) | clinical status active | SNOMED 431857002
[Condition/ef5e136c-ff1e-0695-5331-2d63eb213c34] Condition | onset 2024-05-15 | Proteinuria due to type 2 diabetes mellitus (disorder) | clinical status active | SNOMED 157141000119108
[Condition/ef5e136c-ff1e-0695-3834-fa6cb282a475] Condition | onset 2024-05-15 | Chronic kidney disease stage 3 (disorder) | clinical status active | SNOMED 433144002
[Condition/ef5e136c-ff1e-0695-68fe-9e2010333061] Condition | onset 2023-08-16 | Microalbuminuria due to type 2 diabetes mellitus (disorder) | clinical status active | SNOMED 90781000119102
[Condition/ef5e136c-ff1e-0695-65f5-8d04f278a661] Condition | onset 2023-08-16 | Chronic kidney disease stage 2 (disorder) | clinical status active | SNOMED 431856006
[Condition/ef5e136c-ff1e-0695-aac2-46a0ff462178] Condition | onset 2023-04-19 | Gingivitis (disorder) | clinical status active | SNOMED 66383009
[Condition/ef5e136c-ff1e-0695-fda2-40e12f6b17a7] Condition | onset 2017-11-15 | Chronic kidney disease stage 1 (disorder) | clinical status active | SNOMED 431855005
[Condition/ef5e136c-ff1e-0695-bf3f-30946ad3f8b4] Condition | onset 2017-11-15 | Disorder of kidney due to diabetes mellitus (disorder) | clinical status active | SNOMED 127013003
[Condition/ef5e136c-ff1e-0695-eac4-d545a0296998] Condition | onset 2011-07-27 | Essential hypertension (disorder) | clinical status active | SNOMED 59621000
[Condition/ef5e136c-ff1e-0695-b228-2f5ff5bb47cb] Condition | onset 2010-05-19 | Metabolic syndrome X (disorder) | clinical status active | SNOMED 237602007
[Condition/ef5e136c-ff1e-0695-af16-82f03f777ba8] Condition | onset 2010-05-19 | Hypertriglyceridemia (disorder) | clinical status active | SNOMED 302870006
[Condition/ef5e136c-ff1e-0695-5ca5-51bfdc51320e] Condition | onset 2010-05-12 | Diabetes mellitus type 2 (disorder) | clinical status active | SNOMED 44054006
[Condition/ef5e136c-ff1e-0695-f7ec-ceae0c2566bc] Condition | onset 2004-06-16 | Body mass index 30+ - obesity (finding) | clinical status active | SNOMED 162864005
[Condition/ef5e136c-ff1e-0695-c94a-5d81ddd88117] Condition | onset 1997-05-07 | Has a criminal record (finding) | clinical status active | SNOMED 266948004
[Condition/ef5e136c-ff1e-0695-6efc-9f7d5e6b04ef] Condition | onset 1993-09-01 | Anemia (disorder) | clinical status active | SNOMED 271737000
[Condition/ef5e136c-ff1e-0695-1f68-dac24351dbaa] Condition | onset 1993-04-14 | Prediabetes (finding) | clinical status active | SNOMED 714628002
[Condition/ef5e136c-ff1e-0695-2d8d-328849698529] Condition | onset 1993-01-22 | History of tubal ligation (situation) | clinical status active | SNOMED 267020005
[Condition/ef5e136c-ff1e-0695-0825-c31e8b252683] Condition | onset 1983-11-14 | Past pregnancy history of miscarriage (situation) | clinical status active | SNOMED 161744009
[Condition/ef5e136c-ff1e-0695-cb16-3a98eeb2de7a] Condition | onset 1976-01-07 | Received higher education (finding) | clinical status active | SNOMED 224299000
[Condition/ef5e136c-ff1e-0695-3278-6a86eaf1fb5d] Condition | onset 1975-06-27 | Chronic sinusitis (disorder) | clinical status active | SNOMED 40055000
[Condition/ef5e136c-ff1e-0695-337f-d12087c8dbb5] Condition | onset 1975-01-01 | Risk activity involvement (finding) | clinical status active | SNOMED 160968000
[MedicationRequest/ef5e136c-ff1e-0695-ffec-2ea7ac772a27] MedicationRequest | prescribed 2026-09-30 | Hydrochlorothiazide 25 MG Oral Tablet | status active | reason: Essential hypertension (disorder) | RxNorm 310798
[MedicationRequest/ef5e136c-ff1e-0695-b3ba-a1ec7bcfb9f4] MedicationRequest | prescribed 2026-09-30 | albuterol 0.83 MG/ML Inhalation Solution | status active | RxNorm 630208
[MedicationRequest/ef5e136c-ff1e-0695-901e-2e1f9afb0cca] MedicationRequest | prescribed 2026-09-30 | lisinopril 10 MG Oral Tablet | status active | reason: Essential hypertension (disorder) | RxNorm 314076
[MedicationRequest/ef5e136c-ff1e-0695-76a6-8eeb54f8a75e] MedicationRequest | prescribed 2026-09-30 | 120 ACTUAT fluticasone propionate 0.044 MG/ACTUAT Metered Dose Inhaler [Flovent] | status active | RxNorm 895996
[MedicationRequest/ef5e136c-ff1e-0695-6c6d-182c3b9c47c1] MedicationRequest | prescribed 2026-09-30 | amLODIPine 2.5 MG Oral Tablet | status active | reason: Essential hypertension (disorder) | RxNorm 308136
[MedicationRequest/ef5e136c-ff1e-0695-6804-cf31640a9491] MedicationRequest | prescribed 2026-09-30 | insulin isophane, human 70 UNT/ML / insulin, regular, human 30 UNT/ML Injectable Suspension [Humulin] | status active | reason: Diabetes mellitus type 2 (disorder) | RxNorm 106892
[Encounter/ef5e136c-ff1e-0695-08ba-2471a16a6570] Encounter | 2026-09-30 | Emergency room admission (procedure) | class EMER | at APPLE VALLEY CENTER
[Encounter/ef5e136c-ff1e-0695-aea4-11055569fd51] Encounter | 2026-09-23 | Urgent care clinic (environment) | class AMB | at URGENT HELP CHELMSFORD PC
[Encounter/ef5e136c-ff1e-0695-4a41-6fca58c80cb7] Encounter | 2026-09-16 | Urgent care clinic (environment) | class AMB | at URGENT HELP CHELMSFORD PC
[Immunization/ef5e136c-ff1e-0695-6beb-93901776b619] Immunization | 2026-05-13 | Influenza, split virus, trivalent, PF | status completed | CVX 140
[DocumentReference/daf4cbbc-d83d-ad34-9f1d-46e198762b8f#2] Clinical note | 2025-06-28 | part 2 of 2 | # Social History Patient is single. Patient has never smoked. Patient identifies as heterosexual. Patient comes from a high socioeconomic background. Patient is a college graduate. Patient currently has Medicare. # Allergies No Known Allergies. # Medications lisinopril 10 mg oral tablet; tropicamide 5 mg/ml ophthalmic solution; 1 ml epoetin alfa 4000 unt/ml injection [epogen]; hydrochlorothiazide 25 mg oral tablet; amoxicillin 250 mg oral capsule; acetaminophen 325 mg / oxycodone hydrochloride 5 mg oral tablet; 120 actuat fluticasone propionate 0.044 mg/actuat metered dose inhaler [flovent]; amlodipine 2.5 mg oral tablet; insulin isophane, human 70 unt/ml / insulin, regular, human 30 unt/ml injectable suspension [humulin]; albuterol 0.83 mg/ml inhalation solution; naproxen sodium 220 mg oral tablet # Assessment and Plan ## Plan The following procedures were conducted: - renal dialysis (procedure) The patient was prescribed the following medications: - 1 ml epoetin alfa 4000 unt/ml injection [epogen]
[DocumentReference/7a6837ed-3b45-d320-df00-3efd069e582f#2] Clinical note | 2025-05-27 | part 2 of 2 | # Social History Patient is single. Patient has never smoked. Patient identifies as heterosexual. Patient comes from a high socioeconomic background. Patient is a college graduate. Patient currently has Medicare. # Allergies No Known Allergies. # Medications lisinopril 10 mg oral tablet; tropicamide 5 mg/ml ophthalmic solution; 1 ml epoetin alfa 4000 unt/ml injection [epogen]; hydrochlorothiazide 25 mg oral tablet; amoxicillin 250 mg oral capsule; acetaminophen 325 mg / oxycodone hydrochloride 5 mg oral tablet; 120 actuat fluticasone propionate 0.044 mg/actuat metered dose inhaler [flovent]; amlodipine 2.5 mg oral tablet; insulin isophane, human 70 unt/ml / insulin, regular, human 30 unt/ml injectable suspension [humulin]; albuterol 0.83 mg/ml inhalation solution; naproxen sodium 220 mg oral tablet # Assessment and Plan ## Plan The following procedures were conducted: - renal dialysis (procedure) The patient was prescribed the following medications: - 1 ml epoetin alfa 4000 unt/ml injection [epogen]
[DocumentReference/862383bd-b7a3-c7c6-8d33-4f163cb32c5e#2] Clinical note | 2025-07-30 | part 2 of 2 | # Social History Patient is single. Patient has never smoked. Patient identifies as heterosexual. Patient comes from a high socioeconomic background. Patient is a college graduate. Patient currently has Medicare. # Allergies No Known Allergies. # Medications lisinopril 10 mg oral tablet; tropicamide 5 mg/ml ophthalmic solution; 1 ml epoetin alfa 4000 unt/ml injection [epogen]; hydrochlorothiazide 25 mg oral tablet; amoxicillin 250 mg oral capsule; acetaminophen 325 mg / oxycodone hydrochloride 5 mg oral tablet; 120 actuat fluticasone propionate 0.044 mg/actuat metered dose inhaler [flovent]; amlodipine 2.5 mg oral tablet; insulin isophane, human 70 unt/ml / insulin, regular, human 30 unt/ml injectable suspension [humulin]; albuterol 0.83 mg/ml inhalation solution; naproxen sodium 220 mg oral tablet # Assessment and Plan ## Plan The following procedures were conducted: - renal dialysis (procedure) The patient was prescribed the following medications: - 1 ml epoetin alfa 4000 unt/ml injection [epogen]
[DocumentReference/f71ef622-751d-0109-7f6f-ec6bf58dfdbf#2] Clinical note | 2025-05-24 | part 2 of 2 | # Social History Patient is single. Patient has never smoked. Patient identifies as heterosexual. Patient comes from a high socioeconomic background. Patient is a college graduate. Patient currently has Medicare. # Allergies No Known Allergies. # Medications lisinopril 10 mg oral tablet; tropicamide 5 mg/ml ophthalmic solution; 1 ml epoetin alfa 4000 unt/ml injection [epogen]; hydrochlorothiazide 25 mg oral tablet; amoxicillin 250 mg oral capsule; acetaminophen 325 mg / oxycodone hydrochloride 5 mg oral tablet; 120 actuat fluticasone propionate 0.044 mg/actuat metered dose inhaler [flovent]; amlodipine 2.5 mg oral tablet; insulin isophane, human 70 unt/ml / insulin, regular, human 30 unt/ml injectable suspension [humulin]; albuterol 0.83 mg/ml inhalation solution; naproxen sodium 220 mg oral tablet # Assessment and Plan ## Plan The following procedures were conducted: - renal dialysis (procedure) The patient was prescribed the following medications: - 1 ml epoetin alfa 4000 unt/ml injection [epogen]
[DocumentReference/39309066-7a2d-f9a7-e573-1818c631818c#2] Clinical note | 2025-06-25 | part 2 of 2 | # Social History Patient is single. Patient has never smoked. Patient identifies as heterosexual. Patient comes from a high socioeconomic background. Patient is a college graduate. Patient currently has Medicare. # Allergies No Known Allergies. # Medications lisinopril 10 mg oral tablet; tropicamide 5 mg/ml ophthalmic solution; 1 ml epoetin alfa 4000 unt/ml injection [epogen]; hydrochlorothiazide 25 mg oral tablet; amoxicillin 250 mg oral capsule; acetaminophen 325 mg / oxycodone hydrochloride 5 mg oral tablet; 120 actuat fluticasone propionate 0.044 mg/actuat metered dose inhaler [flovent]; amlodipine 2.5 mg oral tablet; insulin isophane, human 70 unt/ml / insulin, regular, human 30 unt/ml injectable suspension [humulin]; albuterol 0.83 mg/ml inhalation solution; naproxen sodium 220 mg oral tablet # Assessment and Plan ## Plan The following procedures were conducted: - renal dialysis (procedure) The patient was prescribed the following medications: - 1 ml epoetin alfa 4000 unt/ml injection [epogen]
[DocumentReference/1d1baf68-c25c-474a-f33c-f341e85e0b3c#2] Clinical note | 2025-08-06 | part 2 of 2 | # Social History Patient is single. Patient has never smoked. Patient identifies as heterosexual. Patient comes from a high socioeconomic background. Patient is a college graduate. Patient currently has Medicare. # Allergies No Known Allergies. # Medications lisinopril 10 mg oral tablet; tropicamide 5 mg/ml ophthalmic solution; 1 ml epoetin alfa 4000 unt/ml injection [epogen]; hydrochlorothiazide 25 mg oral tablet; amoxicillin 250 mg oral capsule; acetaminophen 325 mg / oxycodone hydrochloride 5 mg oral tablet; 120 actuat fluticasone propionate 0.044 mg/actuat metered dose inhaler [flovent]; amlodipine 2.5 mg oral tablet; insulin isophane, human 70 unt/ml / insulin, regular, human 30 unt/ml injectable suspension [humulin]; albuterol 0.83 mg/ml inhalation solution; naproxen sodium 220 mg oral tablet # Assessment and Plan ## Plan The following procedures were conducted: - renal dialysis (procedure) The patient was prescribed the following medications: - 1 ml epoetin alfa 4000 unt/ml injection [epogen]
[DocumentReference/b04c555d-dfa3-4de7-0142-9ede50a00370#2] Clinical note | 2025-07-01 | part 2 of 2 | # Social History Patient is single. Patient has never smoked. Patient identifies as heterosexual. Patient comes from a high socioeconomic background. Patient is a college graduate. Patient currently has Medicare. # Allergies No Known Allergies. # Medications lisinopril 10 mg oral tablet; tropicamide 5 mg/ml ophthalmic solution; 1 ml epoetin alfa 4000 unt/ml injection [epogen]; hydrochlorothiazide 25 mg oral tablet; amoxicillin 250 mg oral capsule; acetaminophen 325 mg / oxycodone hydrochloride 5 mg oral tablet; 120 actuat fluticasone propionate 0.044 mg/actuat metered dose inhaler [flovent]; amlodipine 2.5 mg oral tablet; insulin isophane, human 70 unt/ml / insulin, regular, human 30 unt/ml injectable suspension [humulin]; albuterol 0.83 mg/ml inhalation solution; naproxen sodium 220 mg oral tablet # Assessment and Plan ## Plan The following procedures were conducted: - renal dialysis (procedure) The patient was prescribed the following medications: - 1 ml epoetin alfa 4000 unt/ml injection [epogen]
[DocumentReference/88f70ab4-f37e-aefe-89d9-041f04209b91#2] Clinical note | 2025-11-12 | part 2 of 2 | # Social History Patient is single. Patient has never smoked. Patient identifies as heterosexual. Patient comes from a high socioeconomic background. Patient is a college graduate. Patient currently has Medicare. # Allergies No Known Allergies. # Medications lisinopril 10 mg oral tablet; tropicamide 5 mg/ml ophthalmic solution; 1 ml epoetin alfa 4000 unt/ml injection [epogen]; hydrochlorothiazide 25 mg oral tablet; amoxicillin 250 mg oral capsule; acetaminophen 325 mg / oxycodone hydrochloride 5 mg oral tablet; 120 actuat fluticasone propionate 0.044 mg/actuat metered dose inhaler [flovent]; amlodipine 2.5 mg oral tablet; insulin isophane, human 70 unt/ml / insulin, regular, human 30 unt/ml injectable suspension [humulin]; albuterol 0.83 mg/ml inhalation solution; naproxen sodium 220 mg oral tablet # Assessment and Plan Patient is presenting with medication review due (situation). ## Plan The patient was prescribed the following medications: - insulin isophane, human 70 unt/ml / insulin, regular, human 30 unt/ml injectable suspension [humulin] - hydrochlorothiazide 25 mg oral tablet - 120 actuat fluticasone propionate 0.044 mg/actuat metered dose inhaler [flovent] - lisinopril 10 mg oral tablet - amlodipine 2.5 mg oral tablet - albuterol 0.83 mg/ml inhalation solution
[DocumentReference/879e468a-b533-0a0f-19fe-62c9e2951e4d#2] Clinical note | 2025-05-21 | part 2 of 2 | # Social History Patient is single. Patient has never smoked. Patient identifies as heterosexual. Patient comes from a high socioeconomic background. Patient is a college graduate. Patient currently has Medicare. # Allergies No Known Allergies. # Medications lisinopril 10 mg oral tablet; tropicamide 5 mg/ml ophthalmic solution; 1 ml epoetin alfa 4000 unt/ml injection [epogen]; hydrochlorothiazide 25 mg oral tablet; amoxicillin 250 mg oral capsule; acetaminophen 325 mg / oxycodone hydrochloride 5 mg oral tablet; 120 actuat fluticasone propionate 0.044 mg/actuat metered dose inhaler [flovent]; amlodipine 2.5 mg oral tablet; insulin isophane, human 70 unt/ml / insulin, regular, human 30 unt/ml injectable suspension [humulin]; albuterol 0.83 mg/ml inhalation solution; naproxen sodium 220 mg oral tablet # Assessment and Plan ## Plan The following procedures were conducted: - renal dialysis (procedure) The patient was prescribed the following medications: - 1 ml epoetin alfa 4000 unt/ml injection [epogen]
[DocumentReference/12d16d0b-f49d-b245-c3db-8bd524abd1db#2] Clinical note | 2026-05-27 | part 2 of 2 | # Social History Patient is single. Patient has never smoked. Patient identifies as heterosexual. Patient comes from a high socioeconomic background. Patient is a college graduate. Patient currently has Medicare. # Allergies No Known Allergies. # Medications lisinopril 10 mg oral tablet; tropicamide 5 mg/ml ophthalmic solution; 1 ml epoetin alfa 4000 unt/ml injection [epogen]; hydrochlorothiazide 25 mg oral tablet; amoxicillin 250 mg oral capsule; acetaminophen 325 mg / oxycodone hydrochloride 5 mg oral tablet; 120 actuat fluticasone propionate 0.044 mg/actuat metered dose inhaler [flovent]; amlodipine 2.5 mg oral tablet; insulin isophane, human 70 unt/ml / insulin, regular, human 30 unt/ml injectable suspension [humulin]; albuterol 0.83 mg/ml inhalation solution; naproxen sodium 220 mg oral tablet # Assessment and Plan Patient is presenting with medication review due (situation). ## Plan The patient was prescribed the following medications: - insulin isophane, human 70 unt/ml / insulin, regular, human 30 unt/ml injectable suspension [humulin] - hydrochlorothiazide 25 mg oral tablet - 120 actuat fluticasone propionate 0.044 mg/actuat metered dose inhaler [flovent] - lisinopril 10 mg oral tablet - amlodipine 2.5 mg oral tablet - albuterol 0.83 mg/ml inhalation solution
```

</details>

label: s
note: Cited 2026-05-27 and 2025-11-12 notes say 'Patient has never smoked'; all other notes seen (May-Aug 2025) say the same, and 2026-05-27 is the latest note seen.

## 47. `last-visit:8d945e28#0#0`

Question: When was the patient's most recent visit, and what kind of visit was it?

Answer: **The patient's most recent visit was on 2026-09-27, an ambulatory (AMB) encounter for problem with the reason listed as Chronic kidney disease stage 4, at NEW ENGLAND REHABILITATION SERVICES OF CENTRAL MASSACHUSETTS INC.**

Cards this sentence cites:

- `[Encounter/8d945e28-1d8a-bd72-016c-9af67d7199fd]` Encounter | 2026-09-27 | Encounter for problem (procedure) | class AMB | reason: Chronic kidney disease stage 4 (disorder) | at NEW ENGLAND REHABILITATION SERVICES OF CENTRAL MASSACHUSETTS INC

<details><summary>Everything the model saw (39 cards)</summary>

```text
[Condition/8d945e28-1d8a-bd72-9d6c-259e17157c55] Condition | onset 2026-09-07 | Full-time employment (finding) | clinical status active | SNOMED 160903007
[Condition/8d945e28-1d8a-bd72-3102-64b703ba601c] Condition | onset 2026-07-13 | Medication review due (situation) | clinical status active | SNOMED 314529007
[Condition/8d945e28-1d8a-bd72-6b51-0718e8cd7a5e] Condition | onset 2021-01-01 | Awaiting transplantation of kidney (situation) | clinical status active | SNOMED 698306007
[Condition/8d945e28-1d8a-bd72-db4c-2552d073039a] Condition | onset 2020-11-09 | Chronic kidney disease stage 4 (disorder) | clinical status active | SNOMED 431857002
[Condition/8d945e28-1d8a-bd72-ed26-25aa62be033c] Condition | onset 2020-08-18 | Dependent drug abuse (disorder) | clinical status active | SNOMED 6525002
[Condition/8d945e28-1d8a-bd72-05bf-4b4b02b03fe9] Condition | onset 2018-01-22 | Has a criminal record (finding) | clinical status active | SNOMED 266948004
[Condition/8d945e28-1d8a-bd72-38fb-c4bf927332c6] Condition | onset 2013-09-16 | Proteinuria due to type 2 diabetes mellitus (disorder) | clinical status active | SNOMED 157141000119108
[Condition/8d945e28-1d8a-bd72-1379-82140e2d1648] Condition | onset 2013-09-16 | Chronic kidney disease stage 3 (disorder) | clinical status active | SNOMED 433144002
[Condition/8d945e28-1d8a-bd72-cd47-b95fb1e4464b] Condition | onset 2009-07-06 | Microalbuminuria due to type 2 diabetes mellitus (disorder) | clinical status active | SNOMED 90781000119102
[Condition/8d945e28-1d8a-bd72-be1a-fb710d842e34] Condition | onset 2009-07-06 | Chronic kidney disease stage 2 (disorder) | clinical status active | SNOMED 431856006
[Condition/8d945e28-1d8a-bd72-2a55-0f3c986db8dd] Condition | onset 2009-07-06 | Gingivitis (disorder) | clinical status active | SNOMED 66383009
[Condition/8d945e28-1d8a-bd72-4277-241d976b7354] Condition | onset 2007-06-25 | Metabolic syndrome X (disorder) | clinical status active | SNOMED 237602007
[Condition/8d945e28-1d8a-bd72-e0ac-a99a0168ad8a] Condition | onset 2004-06-07 | Disorder of kidney due to diabetes mellitus (disorder) | clinical status active | SNOMED 127013003
[Condition/8d945e28-1d8a-bd72-a508-e7d1553f7f62] Condition | onset 2004-06-07 | Chronic kidney disease stage 1 (disorder) | clinical status active | SNOMED 431855005
[Condition/8d945e28-1d8a-bd72-2622-8fe0a1a30909] Condition | onset 2003-06-02 | Essential hypertension (disorder) | clinical status active | SNOMED 59621000
[Condition/8d945e28-1d8a-bd72-12e3-17db162c8f0b] Condition | onset 2001-06-04 | Obstructive sleep apnea syndrome (disorder) | clinical status active | SNOMED 78275009
[Condition/8d945e28-1d8a-bd72-d01e-086bb9d1d22f] Condition | onset 2001-05-07 | Sleep disorder (disorder) | clinical status active | SNOMED 39898005
[Condition/8d945e28-1d8a-bd72-f5fa-42692b5be159] Condition | onset 1996-08-05 | Body mass index 30+ - obesity (finding) | clinical status active | SNOMED 162864005
[Condition/8d945e28-1d8a-bd72-e601-8e5493910aec] Condition | onset 1981-07-20 | Prediabetes (finding) | clinical status active | SNOMED 714628002
[Condition/8d945e28-1d8a-bd72-52ca-256d6584412c] Condition | onset 1981-07-20 | Anemia (disorder) | clinical status active | SNOMED 271737000
[Condition/8d945e28-1d8a-bd72-d644-66738e889d91] Condition | onset 1977-07-11 | Received higher education (finding) | clinical status active | SNOMED 224299000
[Condition/8d945e28-1d8a-bd72-fbf9-3e6f6bd97f57] Condition | onset 1977-03-07 | Risk activity involvement (finding) | clinical status active | SNOMED 160968000
[MedicationRequest/8d945e28-1d8a-bd72-ff5c-41daf21d65a9] MedicationRequest | prescribed 2026-09-07 | insulin isophane, human 70 UNT/ML / insulin, regular, human 30 UNT/ML Injectable Suspension [Humulin] | status active | reason: Prediabetes (finding) | RxNorm 106892
[MedicationRequest/8d945e28-1d8a-bd72-d409-38c0124f2c47] MedicationRequest | prescribed 2026-09-07 | Hydrochlorothiazide 25 MG Oral Tablet | status active | reason: Essential hypertension (disorder) | RxNorm 310798
[MedicationRequest/8d945e28-1d8a-bd72-bcd6-3304c42dca58] MedicationRequest | prescribed 1981-07-27 | Vitamin B12 5 MG/ML Injectable Solution | status active | RxNorm 2001499
[Encounter/8d945e28-1d8a-bd72-016c-9af67d7199fd] Encounter | 2026-09-27 | Encounter for problem (procedure) | class AMB | reason: Chronic kidney disease stage 4 (disorder) | at NEW ENGLAND REHABILITATION SERVICES OF CENTRAL MASSACHUSETTS INC
[Encounter/8d945e28-1d8a-bd72-3f01-7946bd8f2be1] Encounter | 2026-09-26 | Encounter for problem (procedure) | class AMB | reason: Chronic kidney disease stage 4 (disorder) | at NEW ENGLAND REHABILITATION SERVICES OF CENTRAL MASSACHUSETTS INC
[Encounter/8d945e28-1d8a-bd72-9dbd-785d1f0e4915] Encounter | 2026-09-23 | Encounter for problem (procedure) | class AMB | reason: Chronic kidney disease stage 4 (disorder) | at NEW ENGLAND REHABILITATION SERVICES OF CENTRAL MASSACHUSETTS INC
[Immunization/8d945e28-1d8a-bd72-6a94-32775be2d4e6] Immunization | 2026-01-12 | Influenza, split virus, trivalent, PF | status completed | CVX 140
[Condition/8d945e28-1d8a-bd72-de85-e5a567dddc03] Condition | onset 2017-05-01 | Medication review due (situation) | clinical status resolved | resolved 2017-05-01 | SNOMED 314529007
[Condition/8d945e28-1d8a-bd72-a7e0-bc786c26dcac] Condition | onset 2025-10-20 | Medication review due (situation) | clinical status resolved | resolved 2026-06-22 | SNOMED 314529007
[Condition/8d945e28-1d8a-bd72-7a33-55af8cacbbe5] Condition | onset 2025-03-31 | Medication review due (situation) | clinical status resolved | resolved 2025-08-18 | SNOMED 314529007
[Procedure/8d945e28-1d8a-bd72-211a-721564ba2a16] Procedure | 2021-06-14 | office visit for observation (during regularly scheduled hours) - no other services performed | status completed | http://www.ada.org/cdt D9430
[Immunization/8d945e28-1d8a-bd72-28c7-936105552d76] Immunization | 2021-05-17 | COVID-19, mRNA, LNP-S, PF, 30 mcg/0.3 mL dose | status completed | CVX 208
[Immunization/8d945e28-1d8a-bd72-c212-27d34e4b0eef] Immunization | 2021-04-26 | COVID-19, mRNA, LNP-S, PF, 30 mcg/0.3 mL dose | status completed | CVX 208
[DocumentReference/2e0bb647-4d20-0072-1890-d32c2463b037#2] Clinical note | 2021-06-14 | part 2 of 2 | # Medications 1 ml epoetin alfa 4000 unt/ml injection [epogen]; acetaminophen 325 mg oral tablet; hydrochlorothiazide 25 mg oral tablet; acetaminophen 325 mg / oxycodone hydrochloride 5 mg oral tablet; insulin isophane, human 70 unt/ml / insulin, regular, human 30 unt/ml injectable suspension [humulin]; ibuprofen 200 mg oral tablet # Assessment and Plan Patient is presenting with dental caries, unspecified. ## Plan The following procedures were conducted: - office visit for observation (during regularly scheduled hours) - no other services performed
[DocumentReference/39c3ccb8-f3ba-af45-7465-13f2298b9b36#2] Clinical note | 2021-05-10 | part 2 of 2 | # Assessment and Plan ## Plan Patient was given the following immunizations: covid-19, mrna, lnp-s, pf, 30 mcg/0.3 ml dose. The following procedures were conducted: - renal dialysis (procedure) The patient was prescribed the following medications: - 1 ml epoetin alfa 4000 unt/ml injection [epogen]
[DocumentReference/3f628097-7433-7ecf-0911-07f6fe088905#2] Clinical note | 2021-04-19 | part 2 of 2 | # Assessment and Plan ## Plan Patient was given the following immunizations: covid-19, mrna, lnp-s, pf, 30 mcg/0.3 ml dose. The following procedures were conducted: - renal dialysis (procedure) The patient was prescribed the following medications: - 1 ml epoetin alfa 4000 unt/ml injection [epogen]
[Observation/8d945e28-1d8a-bd72-f73b-94561c535277] Observation (survey) | 2024-09-02 | Protocol for Responding to and Assessing Patients' Assets, Risks, and Experiences [PRAPARE] = Within the last year, have you been afraid of your partner or ex-partner No; Do you feel physically and emotionally safe where you currently live [PRAPARE] Yes; Are you a refugee No; Have you spent more than 2 nights in a row in a jail, prison, detention center, or juvenile correctional facility in past 1 year [PRAPARE] Yes; Stress level Somewhat; How often do you see or talk to people that you care about and feel close to [PRAPARE] 5 or more times a week; Has lack of transportation kept you from medical appointments, meetings, work, or from getting things needed for daily living No; Have you or any family members you live with been unable to get any of the following when it was really needed in past 1 year [PRAPARE] Clothing; What was your best estimate of the total income of all family members from all sources, before taxes, in last year [PhenX] 24465 /a; Primary insurance Medicare; Employment status - current Full-time work; Highest level of education More than high school; Address 965 Hintz Light; Are you worried about losing your housing [PRAPARE] No; Housing status I have housing; How many people are living or staying at this address [#] 2 {#}; Preferred language English; Discharged from the U.S. Armed Forces No; Has season or migrant farm work been your or your family's main source of income at any point in past 2 years [PRAPARE] No; Race White; Hispanic or Latino No | status final | LOINC 93025-5
```

</details>

label: s
note: Cited Encounter is 2026-09-27, Encounter for problem, class AMB, reason Chronic kidney disease stage 4, at NEW ENGLAND REHABILITATION SERVICES OF CENTRAL MASSACHUSETTS INC; the other encounters seen (2026-09-26, 2026-09-23) and the other entries are earlier.

## 48. `last-visit:9292c3d5#0#1`

Question: When was the patient's most recent visit, and what kind of visit was it?

Answer: The patient's most recent visit was on 2026-04-26, an ambulatory (class AMB) encounter for General examination of patient (procedure) at COMMUNITY HEALTH PROGRAMS INC. **At that visit, the patient received an Influenza, split virus, trivalent, PF immunization.**

Cards this sentence cites:

- `[Immunization/9292c3d5-3db6-f4f9-2e74-b2ab508532b8]` Immunization | 2026-04-26 | Influenza, split virus, trivalent, PF | status completed | CVX 140

<details><summary>Everything the model saw (31 cards)</summary>

```text
[Condition/9292c3d5-3db6-f4f9-b5ec-3a44e8649597] Condition | onset 2026-04-26 | Full-time employment (finding) | clinical status active | SNOMED 160903007
[Condition/9292c3d5-3db6-f4f9-861b-f7159312202f] Condition | onset 2026-04-26 | Medication review due (situation) | clinical status active | SNOMED 314529007
[Condition/9292c3d5-3db6-f4f9-483e-3d8d3b0f4690] Condition | onset 2026-04-26 | Social isolation (finding) | clinical status active | SNOMED 422650009
[Condition/9292c3d5-3db6-f4f9-38dc-147de4ac63a8] Condition | onset 2026-04-26 | Stress (finding) | clinical status active | SNOMED 73595000
[Condition/9292c3d5-3db6-f4f9-5b6c-1c0ed0fd0321] Condition | onset 2020-03-22 | Opioid abuse | clinical status active | SNOMED 5602001
[Condition/9292c3d5-3db6-f4f9-f835-25af6c77c701] Condition | onset 2011-08-22 | History of myocardial infarction (situation) | clinical status active | SNOMED 399211009
[Condition/9292c3d5-3db6-f4f9-54d1-d4b6d2666838] Condition | onset 2011-08-22 | Acute ST segment elevation myocardial infarction (disorder) | clinical status active | SNOMED 401303003
[Condition/9292c3d5-3db6-f4f9-2b48-fd31edda50b0] Condition | onset 2010-03-21 | Anemia (disorder) | clinical status active | SNOMED 271737000
[Condition/9292c3d5-3db6-f4f9-1b0c-65cb31846f75] Condition | onset 2005-05-29 | Prediabetes (finding) | clinical status active | SNOMED 714628002
[Condition/9292c3d5-3db6-f4f9-2a82-9615e45bb615] Condition | onset 1986-05-04 | Educated to high school level (finding) | clinical status active | SNOMED 473461003
[Condition/9292c3d5-3db6-f4f9-24a0-fe08e411b951] Condition | onset 1986-05-04 | Serving in military service (finding) | clinical status active | SNOMED 1187604002
[Condition/9292c3d5-3db6-f4f9-97fc-b779fe5ffdd4] Condition | onset 1985-04-28 | Risk activity involvement (finding) | clinical status active | SNOMED 160968000
[MedicationRequest/9292c3d5-3db6-f4f9-c2ad-ca0afa2369e8] MedicationRequest | prescribed 2011-08-22 | 24 HR metoprolol succinate 50 MG Extended Release Oral Tablet | status active | RxNorm 866436
[MedicationRequest/9292c3d5-3db6-f4f9-b955-8ddb9b72de69] MedicationRequest | prescribed 2011-08-22 | prasugrel 10 MG Oral Tablet | status active | RxNorm 855812
[MedicationRequest/9292c3d5-3db6-f4f9-8b49-28e15899c04a] MedicationRequest | prescribed 2011-08-22 | aspirin 81 MG Oral Tablet | status active | RxNorm 243670
[MedicationRequest/9292c3d5-3db6-f4f9-7675-f5ee99ae0c4e] MedicationRequest | prescribed 2011-08-22 | simvastatin 40 MG Oral Tablet | status active | RxNorm 198211
[MedicationRequest/9292c3d5-3db6-f4f9-2744-8b9a3e3302b8] MedicationRequest | prescribed 2011-08-22 | lisinopril 2.5 MG Oral Tablet | status active | RxNorm 311353
[Encounter/9292c3d5-3db6-f4f9-f8cd-08dfcc81ed12] Encounter | 2026-04-26 | General examination of patient (procedure) | class AMB | at COMMUNITY HEALTH PROGRAMS INC
[Encounter/9292c3d5-3db6-f4f9-2526-cf0c3fc1dcaa] Encounter | 2025-08-10 | Encounter for check up (procedure) | class AMB | reason: Gingivitis (disorder) | at Pittsfield Outpatient Clinic
[Encounter/9292c3d5-3db6-f4f9-d85c-7f88671a1881] Encounter | 2025-08-03 | Encounter for symptom (procedure) | class AMB | reason: Acute viral pharyngitis (disorder) | at Pittsfield Outpatient Clinic
[Immunization/9292c3d5-3db6-f4f9-2e74-b2ab508532b8] Immunization | 2026-04-26 | Influenza, split virus, trivalent, PF | status completed | CVX 140
[DocumentReference/90384e69-4cc2-2777-3c5c-df19b398fb3a#1] Clinical note | 2019-03-31 | part 1 of 1 | 2019-03-31 # Chief Complaint No complaints. # History of Present Illness Arnold338 is a 51 year-old nonhispanic white male. Patient has a history of medication review due (situation), not in labor force (finding), limited social contact (finding), disorder of teeth and/or supporting structures, full-time employment (finding), social isolation (finding), stress (finding). # Social History Patient is single. Patient quit smoking at age 17. Patient identifies as heterosexual. Patient comes from a middle socioeconomic background. Patient has a high school education. Patient currently has Humana. # Allergies No Known Allergies. # Medications No Active Medications. # Assessment and Plan ## Plan The following procedures were conducted: - periodic orthodontic treatment visit - periodic orthodontic treatment visit
[Encounter/9292c3d5-3db6-f4f9-a03b-3743d58b1c78] Encounter | 1985-04-28 | Well child visit (procedure) | class AMB | at COMMUNITY HEALTH PROGRAMS INC
[Procedure/9292c3d5-3db6-f4f9-1146-76d185c4ad5d] Procedure | 2019-03-31 | periodic orthodontic treatment visit | status completed | http://www.ada.org/cdt D8670
[Procedure/9292c3d5-3db6-f4f9-a726-7825263e1ace] Procedure | 2019-03-31 | periodic orthodontic treatment visit | status completed | http://www.ada.org/cdt D8670
[DocumentReference/b0afcae6-490b-fb11-b71d-382273ce441c#1] Clinical note | 2021-03-14 | part 1 of 1 | 2021-03-14 # Chief Complaint No complaints. # History of Present Illness Arnold338 is a 53 year-old nonhispanic white male. Patient has a history of severe anxiety (panic) (finding), medication review due (situation), not in labor force (finding), limited social contact (finding), disorder of teeth and/or supporting structures, full-time employment (finding), social isolation (finding), stress (finding). # Social History Patient is single. Patient quit smoking at age 17. Patient identifies as heterosexual. Patient comes from a middle socioeconomic background. Patient has a high school education. Patient currently has Humana. # Allergies No Known Allergies. # Medications No Active Medications. # Assessment and Plan ## Plan Patient was given the following immunizations: covid-19, mrna, lnp-s, pf, 30 mcg/0.3 ml dose.
[Condition/9292c3d5-3db6-f4f9-fbfb-cfc1d4cdf03c] Condition | onset 2014-03-30 | Medication review due (situation) | clinical status resolved | resolved 2025-04-20 | SNOMED 314529007
[Condition/9292c3d5-3db6-f4f9-dc28-5fba82169057] Condition | onset 2025-07-27 | Medication review due (situation) | clinical status resolved | resolved 2025-07-27 | SNOMED 314529007
[Encounter/9292c3d5-3db6-f4f9-71e0-c657f27fd422] Encounter | 1970-08-23 | Encounter for check up (procedure) | class AMB | reason: Patient referral for dental care (procedure) | at BERKSHIRE MEDICAL CENTER INC - 1
[Immunization/9292c3d5-3db6-f4f9-0e55-dcf5b05aeef5] Immunization | 2021-04-04 | COVID-19, mRNA, LNP-S, PF, 30 mcg/0.3 mL dose | status completed | CVX 208
[Immunization/9292c3d5-3db6-f4f9-0865-19e45ffab679] Immunization | 2021-03-14 | COVID-19, mRNA, LNP-S, PF, 30 mcg/0.3 mL dose | status completed | CVX 208
```

</details>

label: s?
note: Cited Immunization is Influenza, split virus, trivalent, PF on 2026-04-26, the same date as the only encounter that day, so the flu shot fits that visit. The card does not name the encounter, though, so a strict reader could call the 'at that visit' link a partial.

## 49. `vaccines-last-year:760e0542#0#1`

Question: Which vaccines did the patient receive in the last year?

Answer: In the year before the record's as-of date of 2026-10-01, the patient received one vaccine: Influenza, split virus, trivalent, PF (CVX 140) on 2026-04-08. **The previous influenza dose, on 2025-03-12, falls outside that one-year window.**

Cards this sentence cites:

- `[Immunization/760e0542-9c61-9c1a-56c8-3633420009aa]` Immunization | 2025-03-12 | Influenza, split virus, trivalent, PF | status completed | CVX 140

<details><summary>Everything the model saw (44 cards)</summary>

```text
[Condition/760e0542-9c61-9c1a-f014-d96ecb52354b] Condition | onset 2026-09-09 | Full-time employment (finding) | clinical status active | SNOMED 160903007
[Condition/760e0542-9c61-9c1a-3909-ca43a58a2be0] Condition | onset 2023-02-08 | Social isolation (finding) | clinical status active | SNOMED 422650009
[Condition/760e0542-9c61-9c1a-0603-33ac04e928e9] Condition | onset 2017-07-26 | Has a criminal record (finding) | clinical status active | SNOMED 266948004
[Condition/760e0542-9c61-9c1a-7969-97405f2cda90] Condition | onset 2016-09-28 | Gingivitis (disorder) | clinical status active | SNOMED 66383009
[Condition/760e0542-9c61-9c1a-bc04-975a613f7bef] Condition | onset 2016-05-04 | Proteinuria due to type 2 diabetes mellitus (disorder) | clinical status active | SNOMED 157141000119108
[Condition/760e0542-9c61-9c1a-19fd-96240fc0e3b9] Condition | onset 2016-05-04 | Chronic kidney disease stage 3 (disorder) | clinical status active | SNOMED 433144002
[Condition/760e0542-9c61-9c1a-e1cf-d1bcca0d3b69] Condition | onset 2016-03-02 | Familial Alzheimer's disease of early onset (disorder) | clinical status active | SNOMED 230265002
[Condition/760e0542-9c61-9c1a-bf45-3800d10bb908] Condition | onset 2012-09-12 | Chronic sinusitis (disorder) | clinical status active | SNOMED 40055000
[Condition/760e0542-9c61-9c1a-6a42-9364f5d685e7] Condition | onset 2009-10-14 | Chronic kidney disease stage 2 (disorder) | clinical status active | SNOMED 431856006
[Condition/760e0542-9c61-9c1a-6844-45eca3bcbf32] Condition | onset 2009-10-14 | Microalbuminuria due to type 2 diabetes mellitus (disorder) | clinical status active | SNOMED 90781000119102
[Condition/760e0542-9c61-9c1a-c55b-b73483d412d5] Condition | onset 2004-09-01 | Disorder of kidney due to diabetes mellitus (disorder) | clinical status active | SNOMED 127013003
[Condition/760e0542-9c61-9c1a-8f20-42b2a944fe6e] Condition | onset 2004-09-01 | Chronic kidney disease stage 1 (disorder) | clinical status active | SNOMED 431855005
[Condition/760e0542-9c61-9c1a-426d-1b0e47f6ef3a] Condition | onset 2004-09-01 | Hyperglycemia (disorder) | clinical status active | SNOMED 80394007
[Condition/760e0542-9c61-9c1a-84cc-6ec1252b5c47] Condition | onset 1998-10-12 | History of tubal ligation (situation) | clinical status active | SNOMED 267020005
[Condition/760e0542-9c61-9c1a-d618-c814cd687574] Condition | onset 1998-01-07 | Hypertriglyceridemia (disorder) | clinical status active | SNOMED 302870006
[Condition/760e0542-9c61-9c1a-addb-545c11e2d54a] Condition | onset 1998-01-07 | Metabolic syndrome X (disorder) | clinical status active | SNOMED 237602007
[Condition/760e0542-9c61-9c1a-393d-4476d7ede869] Condition | onset 1995-01-04 | Diabetes mellitus type 2 (disorder) | clinical status active | SNOMED 44054006
[Condition/760e0542-9c61-9c1a-0e56-fe029b0a5419] Condition | onset 1990-08-12 | Past pregnancy history of miscarriage (situation) | clinical status active | SNOMED 161744009
[Condition/760e0542-9c61-9c1a-8747-2a2b77e88f89] Condition | onset 1988-12-28 | Anemia (disorder) | clinical status active | SNOMED 271737000
[Condition/760e0542-9c61-9c1a-4f0e-0a94437d4aaa] Condition | onset 1988-12-28 | Body mass index 30+ - obesity (finding) | clinical status active | SNOMED 162864005
[Condition/760e0542-9c61-9c1a-771f-54deeed066bf] Condition | onset 1982-12-22 | Prediabetes (finding) | clinical status active | SNOMED 714628002
[Condition/760e0542-9c61-9c1a-0604-679a8d525bc1] Condition | onset 1981-12-16 | Received higher education (finding) | clinical status active | SNOMED 224299000
[Condition/760e0542-9c61-9c1a-c792-3a8303530414] Condition | onset 1979-12-05 | Risk activity involvement (finding) | clinical status active | SNOMED 160968000
[Condition/760e0542-9c61-9c1a-1d06-faad5e8f657c] Condition | onset 1974-01-03 | Adolescent idiopathic scoliosis (disorder) | clinical status active | SNOMED 203646004
[MedicationRequest/760e0542-9c61-9c1a-c29f-4c3b83db674e] MedicationRequest | prescribed 2026-09-09 | 24 HR Metformin hydrochloride 500 MG Extended Release Oral Tablet | status active | reason: Diabetes mellitus type 2 (disorder) | RxNorm 860975
[MedicationRequest/760e0542-9c61-9c1a-096d-4868f9087e48] MedicationRequest | prescribed 2026-09-09 | insulin isophane, human 70 UNT/ML / insulin, regular, human 30 UNT/ML Injectable Suspension [Humulin] | status active | reason: Diabetes mellitus type 2 (disorder) | RxNorm 106892
[MedicationRequest/760e0542-9c61-9c1a-c259-531395abfaa1] MedicationRequest | prescribed 2023-01-14 | 24 HR Donepezil hydrochloride 10 MG / Memantine hydrochloride 28 MG Extended Release Oral Capsule | status active | reason: Familial Alzheimer's disease of early onset (disorder) | RxNorm 1599803
[MedicationRequest/760e0542-9c61-9c1a-fd81-acf11c1ddec0] MedicationRequest | prescribed 1967-04-25 | Chlorpheniramine Maleate 2 MG/ML Oral Solution | status active | RxNorm 477045
[AllergyIntolerance/760e0542-9c61-9c1a-3695-658972edefe5] AllergyIntolerance | recorded 1967-05-01 | Allergic disposition (finding) | allergy, category environment, criticality low | clinical status active | SNOMED 609328004
[AllergyIntolerance/760e0542-9c61-9c1a-1887-b0f58a6117f4] AllergyIntolerance | recorded 1967-05-01 | Lisinopril | intolerance, category medication, criticality low | clinical status active | RxNorm 29046
[Encounter/760e0542-9c61-9c1a-6caa-86123ce8fd48] Encounter | 2026-09-09 | Urgent care clinic (environment) | class AMB | at MIDDLETON FAMILY MEDICINE URGENT CARE, LLC
[Encounter/760e0542-9c61-9c1a-dbc8-3964b3a3c72f] Encounter | 2026-08-05 | Urgent care clinic (environment) | class AMB | at MIDDLETON FAMILY MEDICINE URGENT CARE, LLC
[Encounter/760e0542-9c61-9c1a-d9e8-129c4edf531b] Encounter | 2026-05-27 | Encounter for check up (procedure) | class AMB | at LAWRENCE GENERAL HOSPITAL
[Immunization/760e0542-9c61-9c1a-bb77-51bf2da7f927] Immunization | 2026-04-08 | Influenza, split virus, trivalent, PF | status completed | CVX 140
[Immunization/760e0542-9c61-9c1a-929e-cafe8c3d1285] Immunization | 2021-04-07 | Influenza, split virus, trivalent, PF | status completed | CVX 140
[Immunization/760e0542-9c61-9c1a-56c8-3633420009aa] Immunization | 2025-03-12 | Influenza, split virus, trivalent, PF | status completed | CVX 140
[Immunization/760e0542-9c61-9c1a-7506-c0010ccbdeb9] Immunization | 2024-03-20 | Influenza, split virus, trivalent, PF | status completed | CVX 140
[Observation/760e0542-9c61-9c1a-4db9-5f8155d7a4a9] Observation (survey) | 2022-08-31 | Protocol for Responding to and Assessing Patients' Assets, Risks, and Experiences [PRAPARE] = Within the last year, have you been afraid of your partner or ex-partner No; Do you feel physically and emotionally safe where you currently live [PRAPARE] Yes; Are you a refugee No; Have you spent more than 2 nights in a row in a jail, prison, detention center, or juvenile correctional facility in past 1 year [PRAPARE] Yes; Stress level Somewhat; How often do you see or talk to people that you care about and feel close to [PRAPARE] 5 or more times a week; Has lack of transportation kept you from medical appointments, meetings, work, or from getting things needed for daily living No; Have you or any family members you live with been unable to get any of the following when it was really needed in past 1 year [PRAPARE] Phone; What was your best estimate of the total income of all family members from all sources, before taxes, in last year [PhenX] 34577 /a; Primary insurance Medicare; Employment status - current Full-time work; Highest level of education More than high school; Address 594 Johns Parade; Are you worried about losing your housing [PRAPARE] No; Housing status I have housing; How many people are living or staying at this address [#] 7 {#}; Preferred language English; Discharged from the U.S. Armed Forces No; Has season or migrant farm work been your or your family's main source of income at any point in past 2 years [PRAPARE] No; Race White; Hispanic or Latino No | status final | LOINC 93025-5
[Observation/760e0542-9c61-9c1a-5396-569000ad1810] Observation (survey) | 2026-09-09 | Protocol for Responding to and Assessing Patients' Assets, Risks, and Experiences [PRAPARE] = Within the last year, have you been afraid of your partner or ex-partner No; Do you feel physically and emotionally safe where you currently live [PRAPARE] Yes; Are you a refugee No; Have you spent more than 2 nights in a row in a jail, prison, detention center, or juvenile correctional facility in past 1 year [PRAPARE] Yes; Stress level Not at all; How often do you see or talk to people that you care about and feel close to [PRAPARE] 3 to 5 times a week; Has lack of transportation kept you from medical appointments, meetings, work, or from getting things needed for daily living No; Have you or any family members you live with been unable to get any of the following when it was really needed in past 1 year [PRAPARE] Food; What was your best estimate of the total income of all family members from all sources, before taxes, in last year [PhenX] 34577 /a; Primary insurance Medicare; Employment status - current Full-time work; Highest level of education More than high school; Address 594 Johns Parade; Are you worried about losing your housing [PRAPARE] No; Housing status I have housing; How many people are living or staying at this address [#] 7 {#}; Preferred language English; Discharged from the U.S. Armed Forces No; Has season or migrant farm work been your or your family's main source of income at any point in past 2 years [PRAPARE] No; Race White; Hispanic or Latino No | status final | LOINC 93025-5
[Observation/760e0542-9c61-9c1a-70b1-461a59a58d74] Observation (survey) | 2026-08-05 | Protocol for Responding to and Assessing Patients' Assets, Risks, and Experiences [PRAPARE] = Within the last year, have you been afraid of your partner or ex-partner No; Do you feel physically and emotionally safe where you currently live [PRAPARE] No; Are you a refugee No; Have you spent more than 2 nights in a row in a jail, prison, detention center, or juvenile correctional facility in past 1 year [PRAPARE] Yes; Stress level Quite a bit; How often do you see or talk to people that you care about and feel close to [PRAPARE] 3 to 5 times a week; Has lack of transportation kept you from medical appointments, meetings, work, or from getting things needed for daily living No; Have you or any family members you live with been unable to get any of the following when it was really needed in past 1 year [PRAPARE] I choose not to answer this question; What was your best estimate of the total income of all family members from all sources, before taxes, in last year [PhenX] 34577 /a; Primary insurance Medicare; Employment status - current Part-time or temporary work; Highest level of education More than high school; Address 594 Johns Parade; Are you worried about losing your housing [PRAPARE] No; Housing status I have housing; How many people are living or staying at this address [#] 7 {#}; Preferred language English; Discharged from the U.S. Armed Forces No; Has season or migrant farm work been your or your family's main source of income at any point in past 2 years [PRAPARE] No; Race White; Hispanic or Latino No | status final | LOINC 93025-5
[Observation/760e0542-9c61-9c1a-e7d2-cadcc2eca802] Observation (survey) | 2026-05-13 | Protocol for Responding to and Assessing Patients' Assets, Risks, and Experiences [PRAPARE] = Within the last year, have you been afraid of your partner or ex-partner No; Do you feel physically and emotionally safe where you currently live [PRAPARE] Yes; Are you a refugee No; Have you spent more than 2 nights in a row in a jail, prison, detention center, or juvenile correctional facility in past 1 year [PRAPARE] Yes; Stress level A little bit; How often do you see or talk to people that you care about and feel close to [PRAPARE] 3 to 5 times a week; Has lack of transportation kept you from medical appointments, meetings, work, or from getting things needed for daily living No; Have you or any family members you live with been unable to get any of the following when it was really needed in past 1 year [PRAPARE] Food; What was your best estimate of the total income of all family members from all sources, before taxes, in last year [PhenX] 34577 /a; Primary insurance Medicare; Employment status - current Full-time work; Highest level of education More than high school; Address 594 Johns Parade; Are you worried about losing your housing [PRAPARE] No; Housing status I have housing; How many people are living or staying at this address [#] 7 {#}; Preferred language English; Discharged from the U.S. Armed Forces No; Has season or migrant farm work been your or your family's main source of income at any point in past 2 years [PRAPARE] No; Race White; Hispanic or Latino No | status final | LOINC 93025-5
[Immunization/760e0542-9c61-9c1a-348d-850ee604a0a7] Immunization | 2021-04-14 | COVID-19, mRNA, LNP-S, PF, 30 mcg/0.3 mL dose | status completed | CVX 208
[Immunization/760e0542-9c61-9c1a-bb55-2e74e1870df5] Immunization | 2021-05-05 | COVID-19, mRNA, LNP-S, PF, 30 mcg/0.3 mL dose | status completed | CVX 208
[DocumentReference/dea8e555-16a6-228a-ab25-b69355fdcefe#2] Clinical note | 2021-04-14 | part 2 of 2 | # Assessment and Plan ## Plan Patient was given the following immunizations: covid-19, mrna, lnp-s, pf, 30 mcg/0.3 ml dose. The following lab reports were completed: - basic metabolic 2000 panel - serum or plasma - urinalysis macro (dipstick) panel - urine The patient was prescribed the following medications: - insulin isophane, human 70 unt/ml / insulin, regular, human 30 unt/ml injectable suspension [humulin] - 24 hr metformin hydrochloride 500 mg extended release oral tablet
```

</details>

label: s
note: Cited Immunization is influenza on 2025-03-12, which is before 2025-10-01 and so outside the window; the other influenza doses seen (2026-04-08, 2024-03-20, 2021-04-07) confirm it is the dose just before 2026-04-08.

## 50. `lay-a-sinus-infection:d4f2a6f8#0#1`

Question: Has the patient ever been diagnosed with a sinus infection? If so, when?

Answer: Yes, the patient was diagnosed with viral sinusitis with onset 2025-09-11, evaluated at an encounter for symptom at TEWKSBURY HOSPITAL that day. **The condition's clinical status is resolved, with a resolution date of 2025-09-22.**

Cards this sentence cites:

- `[Condition/d4f2a6f8-e358-6b1b-bfcd-a5b0b4460ce0]` Condition | onset 2025-09-11 | Viral sinusitis (disorder) | clinical status resolved | resolved 2025-09-22 | SNOMED 444814009

<details><summary>Everything the model saw (42 cards)</summary>

```text
[Condition/d4f2a6f8-e358-6b1b-a870-7578fc115ba3] Condition | onset 2026-04-02 | Stress (finding) | clinical status active | SNOMED 73595000
[Condition/d4f2a6f8-e358-6b1b-37cc-cacad982df8c] Condition | onset 2026-04-02 | Reports of violence in the environment (finding) | clinical status active | SNOMED 424393004
[Condition/d4f2a6f8-e358-6b1b-c78d-1b6bc447e34a] Condition | onset 2025-12-04 | Full-time employment (finding) | clinical status active | SNOMED 160903007
[Condition/d4f2a6f8-e358-6b1b-29d8-fc1e6a15e60d] Condition | onset 2025-12-04 | Medication review due (situation) | clinical status active | SNOMED 314529007
[Condition/d4f2a6f8-e358-6b1b-f1ac-92593f6454e7] Condition | onset 2025-03-20 | Chronic kidney disease stage 4 (disorder) | clinical status active | SNOMED 431857002
[Condition/d4f2a6f8-e358-6b1b-4959-9b97d2d3536d] Condition | onset 2025-02-03 | Awaiting transplantation of kidney (situation) | clinical status active | SNOMED 698306007
[Condition/d4f2a6f8-e358-6b1b-76dc-8902de051de4] Condition | onset 2022-10-20 | Microalbuminuria due to type 2 diabetes mellitus (disorder) | clinical status active | SNOMED 90781000119102
[Condition/d4f2a6f8-e358-6b1b-1e8b-4beeba77ed82] Condition | onset 2022-10-20 | Proteinuria due to type 2 diabetes mellitus (disorder) | clinical status active | SNOMED 157141000119108
[Condition/d4f2a6f8-e358-6b1b-042a-23b17f3aef58] Condition | onset 2022-10-20 | Chronic kidney disease stage 3 (disorder) | clinical status active | SNOMED 433144002
[Condition/d4f2a6f8-e358-6b1b-7e47-2334f6b84c0f] Condition | onset 2020-05-28 | History of coronary artery bypass grafting (situation) | clinical status active | SNOMED 399261000
[Condition/d4f2a6f8-e358-6b1b-ebe7-54c5d38117fc] Condition | onset 2020-03-19 | Abnormal findings diagnostic imaging heart+coronary circulat (finding) | clinical status active | SNOMED 274531002
[Condition/d4f2a6f8-e358-6b1b-e1e3-648cc0a38c11] Condition | onset 2020-03-05 | Chronic kidney disease stage 1 (disorder) | clinical status active | SNOMED 431855005
[Condition/d4f2a6f8-e358-6b1b-7f62-e48c3798c8b1] Condition | onset 2020-03-05 | Disorder of kidney due to diabetes mellitus (disorder) | clinical status active | SNOMED 127013003
[Condition/d4f2a6f8-e358-6b1b-6866-45937dfd6387] Condition | onset 2020-03-05 | Ischemic heart disease (disorder) | clinical status active | SNOMED 414545008
[Condition/d4f2a6f8-e358-6b1b-9d41-102804feed92] Condition | onset 2004-12-09 | Metabolic syndrome X (disorder) | clinical status active | SNOMED 237602007
[Condition/d4f2a6f8-e358-6b1b-4dab-6274d2854b00] Condition | onset 2002-11-28 | Anemia (disorder) | clinical status active | SNOMED 271737000
[Condition/d4f2a6f8-e358-6b1b-c5c9-83d1526dc404] Condition | onset 2001-11-22 | Essential hypertension (disorder) | clinical status active | SNOMED 59621000
[Condition/d4f2a6f8-e358-6b1b-d3db-555b40b7ebe5] Condition | onset 2000-05-04 | Prediabetes (finding) | clinical status active | SNOMED 714628002
[Condition/d4f2a6f8-e358-6b1b-4a76-ae3dfbf47144] Condition | onset 1986-11-06 | Body mass index 30+ - obesity (finding) | clinical status active | SNOMED 162864005
[Condition/d4f2a6f8-e358-6b1b-c732-3e05c6bfa924] Condition | onset 1982-10-28 | Only received primary school education (finding) | clinical status active | SNOMED 224295006
[MedicationRequest/d4f2a6f8-e358-6b1b-da40-22bfe510e33d] MedicationRequest | prescribed 2026-04-09 | Hydrochlorothiazide 25 MG Oral Tablet | status active | reason: Essential hypertension (disorder) | RxNorm 310798
[MedicationRequest/d4f2a6f8-e358-6b1b-b1c3-dd4b80a73ea4] MedicationRequest | prescribed 2026-04-09 | insulin isophane, human 70 UNT/ML / insulin, regular, human 30 UNT/ML Injectable Suspension [Humulin] | status active | reason: Prediabetes (finding) | RxNorm 106892
[MedicationRequest/d4f2a6f8-e358-6b1b-875e-3c108c25914e] MedicationRequest | prescribed 2026-04-09 | lisinopril 10 MG Oral Tablet | status active | reason: Essential hypertension (disorder) | RxNorm 314076
[MedicationRequest/d4f2a6f8-e358-6b1b-6913-a3ea2279b298] MedicationRequest | prescribed 2026-04-09 | amLODIPine 2.5 MG Oral Tablet | status active | reason: Essential hypertension (disorder) | RxNorm 308136
[MedicationRequest/d4f2a6f8-e358-6b1b-f33b-aeabe5d3ea2a] MedicationRequest | prescribed 2020-03-12 | Simvastatin 20 MG Oral Tablet | status active | RxNorm 312961
[MedicationRequest/d4f2a6f8-e358-6b1b-da7b-92b61020d936] MedicationRequest | prescribed 2020-03-12 | Nitroglycerin 0.4 MG/ACTUAT Mucosal Spray | status active | RxNorm 705129
[MedicationRequest/d4f2a6f8-e358-6b1b-c7c5-6dd35faf2d76] MedicationRequest | prescribed 2020-03-12 | 24 HR metoprolol succinate 100 MG Extended Release Oral Tablet | status active | RxNorm 866412
[MedicationRequest/d4f2a6f8-e358-6b1b-102e-595eecaa5a85] MedicationRequest | prescribed 2020-03-12 | Clopidogrel 75 MG Oral Tablet | status active | RxNorm 309362
[Encounter/d4f2a6f8-e358-6b1b-1745-afd1215948c6] Encounter | 2026-09-23 | Encounter for problem (procedure) | class AMB | reason: Chronic kidney disease stage 4 (disorder) | at TEWKSBURY HOSPITAL
[Encounter/d4f2a6f8-e358-6b1b-3133-f32329c08d3e] Encounter | 2026-09-20 | Encounter for problem (procedure) | class AMB | reason: Chronic kidney disease stage 4 (disorder) | at TEWKSBURY HOSPITAL
[Encounter/d4f2a6f8-e358-6b1b-0f9b-7fe2ad9bcba8] Encounter | 2026-09-20 | Encounter for problem (procedure) | class AMB | reason: Chronic kidney disease stage 4 (disorder) | at TEWKSBURY HOSPITAL
[Immunization/d4f2a6f8-e358-6b1b-d852-5d7c3a4a2175] Immunization | 2026-03-05 | Influenza, split virus, trivalent, PF | status completed | CVX 140
[Condition/d4f2a6f8-e358-6b1b-bfcd-a5b0b4460ce0] Condition | onset 2025-09-11 | Viral sinusitis (disorder) | clinical status resolved | resolved 2025-09-22 | SNOMED 444814009
[Encounter/d4f2a6f8-e358-6b1b-21e4-317a04f40f21] Encounter | 2025-09-11 | Encounter for symptom (procedure) | class AMB | reason: Viral sinusitis (disorder) | at TEWKSBURY HOSPITAL
[DocumentReference/ad9b4247-7496-f0cc-d6f3-ad0fad7c2d73#1] Clinical note | 2026-09-23 | part 1 of 2 | 2026-09-23 # Chief Complaint - Thirst - Fatigue - Frequent Urination - Hunger # History of Present Illness Adolfo777 is a 62 year-old nonhispanic white male. Patient has a history of streptococcal sore throat (disorder), accretion on tooth, medication review due (situation), dental caries on smooth surface penetrating into pulp, unemployed (finding), fracture of clavicle (disorder), fracture of bone (disorder), viral sinusitis (disorder), victim of intimate partner abuse (finding), part-time employment (finding), acute bronchitis (disorder), acute gingivitis, not in labor force (finding), limited social contact (finding), reports of violence in the environment (finding), full-time employment (finding), acute infective cystitis (disorder), gingivitis (disorder), stress (finding), social isolation (finding). # Social History Patient is married. Patient has never smoked. Patient identifies as heterosexual. Patient comes from a middle socioeconomic background. Patient did not finish high school. Patient currently has Aetna. # Allergies No Known Allergies.
[DocumentReference/52f1334b-6cb1-7d6d-371c-40a473ce2502#1] Clinical note | 2026-09-20 | part 1 of 2 | 2026-09-20 # Chief Complaint - Thirst - Fatigue - Frequent Urination - Hunger # History of Present Illness Adolfo777 is a 62 year-old nonhispanic white male. Patient has a history of streptococcal sore throat (disorder), accretion on tooth, medication review due (situation), dental caries on smooth surface penetrating into pulp, unemployed (finding), fracture of clavicle (disorder), fracture of bone (disorder), viral sinusitis (disorder), victim of intimate partner abuse (finding), part-time employment (finding), acute bronchitis (disorder), acute gingivitis, not in labor force (finding), limited social contact (finding), reports of violence in the environment (finding), full-time employment (finding), acute infective cystitis (disorder), gingivitis (disorder), stress (finding), social isolation (finding). # Social History Patient is married. Patient has never smoked. Patient identifies as heterosexual. Patient comes from a middle socioeconomic background. Patient did not finish high school. Patient currently has Aetna. # Allergies No Known Allergies.
[DocumentReference/81a1814c-c60f-ba46-a285-163f62b51bf1#1] Clinical note | 2026-09-20 | part 1 of 2 | 2026-09-20 # Chief Complaint - Thirst - Fatigue - Frequent Urination - Hunger # History of Present Illness Adolfo777 is a 62 year-old nonhispanic white male. Patient has a history of streptococcal sore throat (disorder), accretion on tooth, medication review due (situation), dental caries on smooth surface penetrating into pulp, unemployed (finding), fracture of clavicle (disorder), fracture of bone (disorder), viral sinusitis (disorder), victim of intimate partner abuse (finding), part-time employment (finding), acute bronchitis (disorder), acute gingivitis, not in labor force (finding), limited social contact (finding), reports of violence in the environment (finding), full-time employment (finding), acute infective cystitis (disorder), gingivitis (disorder), stress (finding), social isolation (finding). # Social History Patient is married. Patient has never smoked. Patient identifies as heterosexual. Patient comes from a middle socioeconomic background. Patient did not finish high school. Patient currently has Aetna. # Allergies No Known Allergies.
[DocumentReference/fa2b3a31-b56e-70b9-3310-76d8dec6db82#1] Clinical note | 2026-09-10 | part 1 of 2 | 2026-09-10 # Chief Complaint - Thirst - Fatigue - Frequent Urination - Hunger # History of Present Illness Adolfo777 is a 62 year-old nonhispanic white male. Patient has a history of streptococcal sore throat (disorder), accretion on tooth, medication review due (situation), dental caries on smooth surface penetrating into pulp, unemployed (finding), fracture of clavicle (disorder), fracture of bone (disorder), viral sinusitis (disorder), victim of intimate partner abuse (finding), part-time employment (finding), acute bronchitis (disorder), acute gingivitis, not in labor force (finding), limited social contact (finding), reports of violence in the environment (finding), full-time employment (finding), acute infective cystitis (disorder), gingivitis (disorder), stress (finding), social isolation (finding). # Social History Patient is married. Patient has never smoked. Patient identifies as heterosexual. Patient comes from a middle socioeconomic background. Patient did not finish high school. Patient currently has Aetna. # Allergies No Known Allergies.
[DocumentReference/1c4565d3-3557-a88e-e6b7-fb59e1db36e1#1] Clinical note | 2026-09-04 | part 1 of 2 | 2026-09-04 # Chief Complaint - Thirst - Fatigue - Frequent Urination - Hunger # History of Present Illness Adolfo777 is a 62 year-old nonhispanic white male. Patient has a history of streptococcal sore throat (disorder), accretion on tooth, medication review due (situation), dental caries on smooth surface penetrating into pulp, unemployed (finding), fracture of clavicle (disorder), fracture of bone (disorder), viral sinusitis (disorder), victim of intimate partner abuse (finding), part-time employment (finding), acute bronchitis (disorder), acute gingivitis, not in labor force (finding), limited social contact (finding), reports of violence in the environment (finding), full-time employment (finding), acute infective cystitis (disorder), gingivitis (disorder), stress (finding), social isolation (finding). # Social History Patient is married. Patient has never smoked. Patient identifies as heterosexual. Patient comes from a middle socioeconomic background. Patient did not finish high school. Patient currently has Aetna. # Allergies No Known Allergies.
[DocumentReference/e9a6b909-3e15-e2cc-7f2d-658ccc69ad3f#1] Clinical note | 2026-09-14 | part 1 of 2 | 2026-09-14 # Chief Complaint - Thirst - Fatigue - Frequent Urination - Hunger # History of Present Illness Adolfo777 is a 62 year-old nonhispanic white male. Patient has a history of streptococcal sore throat (disorder), accretion on tooth, medication review due (situation), dental caries on smooth surface penetrating into pulp, unemployed (finding), fracture of clavicle (disorder), fracture of bone (disorder), viral sinusitis (disorder), victim of intimate partner abuse (finding), part-time employment (finding), acute bronchitis (disorder), acute gingivitis, not in labor force (finding), limited social contact (finding), reports of violence in the environment (finding), full-time employment (finding), acute infective cystitis (disorder), gingivitis (disorder), stress (finding), social isolation (finding). # Social History Patient is married. Patient has never smoked. Patient identifies as heterosexual. Patient comes from a middle socioeconomic background. Patient did not finish high school. Patient currently has Aetna. # Allergies No Known Allergies.
[DocumentReference/61457bbc-e8e8-1121-b3f6-514d5ab28a6f#1] Clinical note | 2026-09-17 | part 1 of 2 | 2026-09-17 # Chief Complaint - Thirst - Fatigue - Frequent Urination - Hunger # History of Present Illness Adolfo777 is a 62 year-old nonhispanic white male. Patient has a history of streptococcal sore throat (disorder), accretion on tooth, medication review due (situation), dental caries on smooth surface penetrating into pulp, unemployed (finding), fracture of clavicle (disorder), fracture of bone (disorder), viral sinusitis (disorder), victim of intimate partner abuse (finding), part-time employment (finding), acute bronchitis (disorder), acute gingivitis, not in labor force (finding), limited social contact (finding), reports of violence in the environment (finding), full-time employment (finding), acute infective cystitis (disorder), gingivitis (disorder), stress (finding), social isolation (finding). # Social History Patient is married. Patient has never smoked. Patient identifies as heterosexual. Patient comes from a middle socioeconomic background. Patient did not finish high school. Patient currently has Aetna. # Allergies No Known Allergies.
[DocumentReference/80830ffd-f0d2-7053-5613-81c86a20c304#1] Clinical note | 2026-09-07 | part 1 of 2 | 2026-09-07 # Chief Complaint - Thirst - Fatigue - Frequent Urination - Hunger # History of Present Illness Adolfo777 is a 62 year-old nonhispanic white male. Patient has a history of streptococcal sore throat (disorder), accretion on tooth, medication review due (situation), dental caries on smooth surface penetrating into pulp, unemployed (finding), fracture of clavicle (disorder), fracture of bone (disorder), viral sinusitis (disorder), victim of intimate partner abuse (finding), part-time employment (finding), acute bronchitis (disorder), acute gingivitis, not in labor force (finding), limited social contact (finding), reports of violence in the environment (finding), full-time employment (finding), acute infective cystitis (disorder), gingivitis (disorder), stress (finding), social isolation (finding). # Social History Patient is married. Patient has never smoked. Patient identifies as heterosexual. Patient comes from a middle socioeconomic background. Patient did not finish high school. Patient currently has Aetna. # Allergies No Known Allergies.
```

</details>

label: s
note: Cited Condition card for Viral sinusitis shows clinical status resolved and resolved 2025-09-22, matching the sentence exactly.

