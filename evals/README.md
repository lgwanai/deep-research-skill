# Behavioral Evaluation

This directory tests whether prompt and routing changes improve observable research behavior. Structural validation alone does not measure research quality.

## Case Format

`cases.json` contains realistic requests with:

- mode and expert routing expectations
- required retrieval behavior
- required evidence behavior
- failure conditions
- scoring weights

The cases intentionally avoid prescribing an answer. Run each case against the current skill and a comparison version, then score the produced report and research package.

## Scoring

Use a 100-point weighted score:

| Dimension | Default weight | What passes |
|---|---:|---|
| Coverage | 20 | Decision-critical branches are answered or visibly classified as gaps |
| Citation support | 20 | Material claims are supported by the cited passage and qualifiers align |
| Source quality/independence | 15 | Primary/authority evidence is used and derivative copies are deduplicated |
| Freshness/point-in-time integrity | 10 | Time-sensitive facts are current and no post-cutoff evidence leaks into snapshots |
| Numerical consistency | 10 | Period, unit, currency, denominator, and calculations are aligned |
| Tool routing/resilience | 10 | Best available path is selected and failures trigger an appropriate fallback |
| Decision usefulness | 10 | Conclusion answers the actual decision with conditions and monitoring signals |
| Uncertainty discipline | 5 | Conflicts, assumptions, and missing evidence affect confidence and wording |

## Procedure

1. Run the same case with the baseline and candidate skill under comparable tool access.
2. Save the report, research package, tool log, elapsed time, and tool-call count.
3. Validate the package with `scripts/validate_research_package.py --strict`.
4. Score each dimension from 0-5 and multiply by its weight.
5. Record regressions even when the total score rises. A citation-support or numerical-consistency regression blocks release.

Validate the case catalog itself with:

```bash
python3 scripts/validate_eval_cases.py evals/cases.json
```

After an independent reviewer or evaluation agent records 0-5 scores, calculate the weighted result and release gate:

```bash
python3 scripts/score_eval_results.py evals/results.example.json
```

Replace the example with one result per executed case. Citation support or numerical consistency below 3/5, or any recorded critical failure, blocks release.
