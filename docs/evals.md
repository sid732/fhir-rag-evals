# Evals

How the evaluation harness works, what each number means, and what hasn't been measured yet.

## The question set

`evals/questions/questions.jsonl` holds 274 questions over the 15 patients, built by `make questions`. Each question has a patient, a category, gold evidence, optional key facts, a source, and a split.

| Category | Dev | Test | Examples |
|---|---:|---:|---|
| fact_lookup | 34 | 23 | current medications, active diagnoses, allergies, smoking status, vaccines in the last year |
| values_dates | 60 | 40 | latest lab result and date, latest blood pressure, latest lipid panel, last flu shot, last visit, last colonoscopy |
| lay_terms | 18 | 12 | "Has the patient ever been diagnosed with high blood pressure?" |
| multi_step | 29 | 19 | medications prescribed for a condition, HbA1c trend over three results, reason for the last ER visit |
| not_in_record | 23 | 16 | labs never measured, conditions never diagnosed, tests Synthea never generates (blood type, HIV viral load), colonoscopy never done |

**Gold labels are computed from the raw bundles** by `src/fhir_rag/evals/templates.py`, which parses FHIR with plain dict access and shares nothing with the service except the bundle loader. A parsing bug in the service's views or cards can't hide in the labels too. `build_questions` checks that every gold ref exists in that patient's record and that every "not in record" question has no gold.

**Gold evidence is a list of groups.** Each group holds interchangeable refs: retrieving or citing any one of them counts for the group. "Latest HbA1c" has one group with one ref, the newest result. "What was prescribed for hypertension?" has one group per drug, holding every prescription of that drug for that reason. Recall counts groups, not refs.

**The split** is 60/40 dev/test within each category, decided by a hash of the question id. It was fixed before any tuning, and a question's split doesn't change when others are added. Design decisions were made on dev; test was scored after.

**Hand-written questions** go in `evals/questions/drafted.jsonl` (same format, `source: "human"`), and `make questions` merges them in. None exist yet.

## Retrieval metrics

`make eval-retrieval` (no API key, deterministic). For answerable questions:

- **hit@k**: some gold group has a member in the context.
- **recall@k**: share of gold groups with a member in the context.
- **MRR@k**: 1 / rank of the first gold card among the *ranked* cards. The pinned summary isn't ranked, so it's left out of MRR.
- **Leaked cards**: retrieved cards that belong to another patient. Checked on every question; CI fails on any.

"Context" is everything the model would see: the pinned summary (when on) plus the first k ranked cards. Summary cards don't count against k, so the report also gives the average context size and a no-summary configuration at the same budget.

Intervals are 95% cluster-bootstrap CIs that resample patients rather than questions, because questions about one patient are correlated.

## Answer metrics

`make eval-answers` runs the real pipeline. For answered, answerable cases:

- **Citation validity**: share of the model's citations that name a card it was shown. Measured before invalid citations are removed. Undefined, and left out, when an answer cites nothing.
- **Citation precision and recall**: overlap of the valid citations with the gold groups. Precision undercounts when the model cites a relevant card that isn't gold, such as an older result in a trend answer; the judge covers that case.
- **Numbers and dates in cited cards**: of the sentences that state a number or date, the share whose numbers and dates all appear in the cards that sentence cites. Deterministic and free, and aimed at the most harmful error: a wrong value or date.
- **Key facts present**: for questions with key facts (values and dates), the share that appear in the answer. Numbers compare as numbers, so 6.80 matches 6.8.
- **Faithfulness**: share of sentences the judge (claude-sonnet-5-5) marks fully supported. Facts about specific entries (values, dates, statuses) must be in the cards the sentence cites. Claims about the record as a whole ("most recent", "only", counts, "no record of") are checked against the whole context the model saw, because no single card can show that nothing later exists. Partial support is reported separately.
- **Gold evidence in context**: whether retrieval gave the model what it needed. It separates retrieval misses from generation misses.

For every case: a confusion matrix of answered vs "not in record" against answerable vs not, with precision and recall for "not in record". Cost comes from recorded usage and list prices (`src/fhir_rag/llm/pricing.py`); latency is reported at p50 and p95.

## Harness checks

- `make eval-selftest` runs **oracle** answers (built from the gold labels) and **null** answers ("I don't know", no citations) through the whole pipeline. On dev, the oracle gets key facts 1.000, precision 0.950 and recall 0.950 (the same as the context recall, its true ceiling), and abstains correctly on every "not in record" question. Null gets 0 on precision, recall and key facts, and never abstains. Two bugs were caught this way and fixed: precision and recall were counting citations that had already been removed, and two metrics passed empty answers vacuously.
- Failed attempts (timeouts, API errors, refusals, unparseable output) go to `errors.jsonl` with a failure class and are never scored as wrong answers. Every case is written as it finishes, and an interrupted run resumes.
- The model that served each answer is recorded. If a refusal fallback answered instead of the requested model, the row is flagged.
- Each report records the commit, cohort hash, card version, models, effort and retrieval settings.

## Judge calibration

The faithfulness number means little until the judge is checked against independent labels:

```bash
uv run python -m fhir_rag.evals.calibrate sample --run <run-name> --n 50
# label every line of evals/labels/judge_calibration.jsonl by hand
uv run python -m fhir_rag.evals.calibrate score
```

`sample` keeps the judge's verdicts in a separate file, so labeling is blind. `score` prints agreement, Cohen's kappa (three classes, and supported-vs-not), and a confusion table. The target is at least 90% agreement on clear cases; revise `src/fhir_rag/evals/prompts/judge_v2.txt` until it's met. `make eval-rejudge FROM=<run> RUN=<new-run>` re-grades a finished run's answers with the current judge, so a prompt change costs only judge calls (about $2 for dev).

## Judge v1 and v2

The first full dev run ([report](../evals/reports/answers-dev-1.md)) used judge v1, which saw only the cards each sentence cited. It scored faithfulness 0.635 while every deterministic check was near perfect. Of the 85 sentences it didn't mark supported, 74 were flagged only for a claim about the whole record, such as "the most recent reading was ..." with one reading cited. v1 couldn't check those claims, because the evidence for "most recent" is the absence of anything later. Key facts were 1.000 against gold computed from the raw bundles, so those claims were right.

Judge v2 (`prompts/judge_v2.txt`) checks such claims against the whole context, and it also judges sentences that cite nothing (one answer said, correctly, that no low red cell count diagnosis was recorded). The same 290 sentences, re-judged ([report](../evals/reports/answers-dev-1-judge2.md)):

| v1 verdict | v2: supported | v2: partially supported |
|---|---:|---:|
| supported | 201 | 4 |
| partially supported | 80 | 4 |
| not supported | 1 | 0 |

Faithfulness went from 0.635 to 0.976 [0.960, 0.991]. v2 is not simply more lenient, but it isn't clean either. Reading all 8 of its flags and its 81 upgrades:

- Two flags are judge errors. One marks "the active prescriptions are A to E" as incomplete although the next sentence adds F; v2 still judges each sentence alone. The other gives a reason that says the sentence is supported, then marks it partial.
- One real catch was lost. v1 noticed that an answer folded a separate "awaiting kidney transplant" condition into the CKD stage 4 entry; v2 passed it.
- The other flags are defensible strictness: a flu shot said to be given "at that visit" when the immunization isn't linked to the encounter, and a "stated reason" that comes from an uncited entry.

These are notes from one read-through, not a measurement. The hand-labeled calibration set decides whether v2 needs another revision. Re-judging cost $1.97 ($0.014 per answer; v2 reads about 6,200 input tokens, v1 about 1,400).

## Not measured yet

- Judge agreement with hand labels. Until then, faithfulness is the judge's opinion.
- Run-to-run noise: three repetitions of the dev answer eval (`--reps 3`). The answer-eval CI gate waits on this number.
- The answer eval on the test split.
