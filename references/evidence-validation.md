# Evidence Validation

Use this reference when a research result must be correct enough to support a report, decision, comparison, policy interpretation, financial analysis, or other auditable deliverable. It complements source-quality checks: a strong source is necessary, but it does not guarantee that the agent interpreted or applied the source correctly.

## When To Load

Load this file for:

- Pro or Ultra research containing decision-critical claims
- Securities, company financials, policy, regulation, market data, benchmarks, or numerical comparisons
- Multiple sources that may use different periods, versions, scopes, or metric definitions
- Reports requiring traceability from conclusion back to the exact source passage
- Requests to verify, validate, reconcile, fact-check, or build a reusable evidence package

For a machine-readable package, also load `references/research-state-schema.md` and validate the saved JSON with `scripts/validate_research_package.py`.

For a simple definition or small fact lookup, use a proportionate check rather than producing the full appendix.

## Validation Model

Run validation in four layers. Passing an earlier layer does not imply that later layers pass.

| Layer | Question | Typical problem |
|---|---|---|
| Source | Is this the original, authoritative, current source? | A news article repeats a filing but changes the wording |
| Field | Are the compared facts defined on the same basis? | Global shipments are compared with domestic installations |
| Claim | Does the cited passage support the exact sentence? | The source says revenue increased; the report says demand increased |
| Calculation | Can the derived number be reproduced? | Percent change is reported as percentage-point change |

## Field-Level Calibration

Before comparing or combining evidence, capture the fields that matter. Use the full set for numerical work and the relevant subset for qualitative work.

| Field | Check |
|---|---|
| Entity | Company, subsidiary, product, market, population, or object is the same |
| Time | Reporting period, event date, publication date, and effective date are not confused |
| Version | Document, policy, product, dataset, or methodology version is pinned |
| Geography | Global, national, regional, and site-level data are not mixed |
| Metric definition | Revenue, bookings, shipments, installations, production, users, or other measures are distinguished |
| Scope / denominator | Consolidated vs parent, total vs segment, gross vs net, sample size, and denominator are explicit |
| Unit / currency | Unit, scale, currency, exchange rate, nominal/real basis, and tax basis are retained |
| Method | Reported, surveyed, estimated, modeled, adjusted, forecast, or calculated is identified |

If a decision-critical field is unknown, do not silently assume equivalence. Mark the comparison as partial or blocked.

## Content Type Separation

Label evidence and output using these categories or equivalent visible wording:

| Type | Meaning | Allowed wording |
|---|---|---|
| Source fact | Directly stated or shown in a reliable source | "The filing reports..." |
| Attributed view | A company's, expert's, analyst's, or author's interpretation | "Management stated..." |
| Synthesis | The agent's conclusion from multiple pieces of evidence | "Taken together, the evidence suggests..." |
| Estimate | A calculated or modeled result using stated assumptions | "Based on X and Y, the estimate is..." |
| Assumption | An unverified condition used to continue analysis | "Assuming the reporting scope is unchanged..." |

Never rewrite an attributed view as a fact. Never present synthesis or an estimate without the supporting evidence and reasoning.

## Claim-To-Evidence Validation

For each decision-critical claim:

1. Write the claim in its smallest checkable form. Split sentences containing multiple factual assertions.
2. Open the full source and locate the exact page, section, table, chart, or paragraph.
3. Decide whether the passage supports the claim directly, supports only part of it, conflicts with it, or does not support it.
4. Check qualifiers such as time, geography, product, population, uncertainty, and exceptions.
5. Check whether the report's wording is stronger than the source. Words such as "caused", "proved", "leading", "all", and "will" require stronger evidence than "associated", "reported", "among", "some", and "may".
6. Rewrite, downgrade, or remove unsupported content. Do not keep a stronger sentence merely because a citation is attached.

Use these statuses:

- **Supported**: the exact claim is directly supported under aligned fields
- **Supported by synthesis**: multiple sources support a clearly identified analytical conclusion
- **Partial**: only part of the claim is supported, or a qualifier is missing
- **Conflicting**: credible evidence disagrees and the difference is unresolved
- **Unsupported**: the cited evidence does not establish the claim
- **Not verifiable**: the source is inaccessible, incomplete, or lacks the required detail

## Numerical Validation

For each number that affects a conclusion:

1. Preserve the raw value, original unit, period, scope, and source location.
2. Record every conversion, including currency, scale, unit, annualization, and inflation adjustment.
3. Show the formula for growth, ratio, share, per-unit, or derived values.
4. Recalculate with a deterministic calculator or code tool when available.
5. Distinguish:
   - percent change from percentage-point change
   - current-period value from cumulative value
   - reported value from adjusted value
   - actual value from forecast or consensus
   - consolidated data from parent-company or segment data
6. If the result cannot be reproduced, mark it for review and do not use it as decisive evidence.

Compact record:

```markdown
| Result | Raw inputs | Period/scope/unit | Formula or conversion | Status | Source |
|---|---|---|---|---|---|
| ... | ... | ... | ... | passed / needs review | ... |
```

## Conflict Resolution

Do not resolve conflicts by choosing the newest or most convenient number automatically.

1. State the exact conflict.
2. Normalize the field set: entity, time, version, geography, metric definition, scope/denominator, unit, and method.
3. Trace derivative reports back to the original source.
4. Determine whether the conflict disappears after normalization.
5. If both values remain credible, show both, explain the difference, and state how it affects the conclusion.
6. If the user's decision depends on the unresolved difference, stop short of a final recommendation and identify the required direct verification.

## Expanded Evidence Ledger

Use this schema for auditable Pro/Ultra work:

```markdown
| ID | Claim | Type | Entity | Time/version | Metric/scope/unit | Source and exact location | Support | Conflict | Validation |
|---|---|---|---|---|---|---|---|---|---|
| C01 | ... | fact / view / synthesis / estimate / assumption | ... | ... | ... | URL, page/section/table | direct / multi-source / inferred | none / resolved / unresolved | supported / partial / conflicting / unsupported / not verifiable |
```

The exact source location is required for material claims when the source provides stable pages, sections, tables, headings, or paragraph anchors.

## Delivery Rules

- Keep the main report readable. Put the full ledger in an appendix when it would interrupt the narrative.
- Surface material conflicts, unsupported claims, and information gaps in the main conclusion, not only in an appendix.
- State what changed after validation: claims weakened, removed, separated by scope, or left unresolved.
- Do not equate a high source-quality score with a supported claim.
- Retrieval confidence and claim validity are separate judgments: broad retrieval can still produce a misapplied conclusion.

## Completion Check

Before delivery, confirm:

- Material claims have exact supporting passages or are visibly labeled synthesis/estimate
- Compared values align on entity, time, version, geography, definition, scope, and unit
- Facts, attributed views, synthesis, estimates, and assumptions are separated
- Decision-critical calculations are reproducible
- Conflicts are resolved, bounded, or explicitly left open
- Missing evidence changes the confidence or conclusion rather than being hidden
