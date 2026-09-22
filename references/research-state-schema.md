# Research State And Package Schema

Use this reference for Pro/Ultra work, audit-sensitive research, numerical comparisons, or any task that may be resumed or independently checked. Keep the state internal unless the user requests the package or methodology.

The purpose is to preserve decisions and evidence across retrieval rounds. Markdown tables remain acceptable for presentation; this schema is the canonical machine-readable form.

## Package Shape

```json
{
  "schema_version": "1.0",
  "status": "working",
  "research_contract": {},
  "capability_profile": {},
  "branches": [],
  "sources": [],
  "claims": [],
  "calculations": [],
  "coverage": [],
  "retrieval_log": [],
  "final_assessment": {}
}
```

Allowed package statuses: `working`, `final`, `blocked`.

## Research Contract

Required fields:

```json
{
  "question": "Decision or deliverable to support",
  "mode": "quick | standard | pro | ultra",
  "as_of_date": "YYYY-MM-DD",
  "geography": ["US", "China"],
  "time_window": "2024-2026",
  "audience": "Who will use the answer",
  "decision_context": "What decision changes",
  "included": [],
  "excluded": [],
  "assumptions": []
}
```

For market-sensitive work, `as_of_date` is the information cutoff. Do not merge observations published after that date into a point-in-time analysis.

## Branches

Each decision-critical question is a branch:

```json
{
  "id": "B01",
  "question": "What must be learned?",
  "critical": true,
  "status": "open | partial | conflicting | resolved | missing | blocked",
  "unresolved_reason": "Why another action is needed",
  "next_action": "Evidence-driven next step",
  "claim_ids": ["C01"]
}
```

A final package must not contain an `open` critical branch. It may contain `partial`, `conflicting`, `missing`, or `blocked` critical branches only when the final conclusion and confidence visibly reflect the limitation.

## Sources

```json
{
  "id": "S01",
  "title": "Source title",
  "url": "https://example.com",
  "publisher": "Organization",
  "source_type": "primary | expert_secondary | practitioner | community | aggregator",
  "published_or_updated": "YYYY-MM-DD or unknown",
  "accessed_at": "ISO-8601 timestamp",
  "exact_location": "page, table, section, paragraph, or anchor",
  "origin_id": "S01",
  "authority": "high | medium | low",
  "limitations": []
}
```

Use the same `origin_id` for syndications, translations, and articles that repeat one underlying report. They do not count as independent confirmation.

## Claims

```json
{
  "id": "C01",
  "text": "Smallest independently checkable statement",
  "claim_type": "fact | attributed_view | synthesis | estimate | assumption",
  "critical": true,
  "status": "supported | supported_by_synthesis | partial | conflicting | unsupported | not_verifiable",
  "source_ids": ["S01"],
  "entity": "Entity",
  "period_or_version": "Period/version",
  "geography": "Geography",
  "metric_definition": "Definition or n/a",
  "scope_or_denominator": "Scope or n/a",
  "unit_or_currency": "Unit or n/a",
  "reasoning": "Required for synthesis and estimates"
}
```

Critical factual claims marked `supported` require at least one source. `supported_by_synthesis` should normally use at least two independent `origin_id` values unless one primary source plus transparent reasoning is sufficient.

## Calculations

```json
{
  "id": "K01",
  "claim_id": "C02",
  "raw_inputs": [{"name": "revenue_2025", "value": 100, "unit": "USDm", "source_id": "S02"}],
  "formula": "(revenue_2025 / revenue_2024) - 1",
  "result": 0.25,
  "result_unit": "percent",
  "period": "FY2025 vs FY2024",
  "scope": "consolidated",
  "status": "passed | needs_review"
}
```

Store raw values before formatting. State FX dates, inflation basis, annualization, split adjustment, and other transformations when relevant.

## Coverage And Retrieval Log

```json
{
  "dimension": "official facts",
  "status": "covered | partial | missing | blocked",
  "source_ids": ["S01"],
  "confidence": "high | medium | low",
  "notes": "Why this status is justified"
}
```

```json
{
  "timestamp": "ISO-8601 timestamp",
  "branch_id": "B01",
  "query_or_target": "Exact query or URL",
  "tool_class": "dedicated_search | platform_native | fetch | rendered_browser | crawler | finance",
  "tool_name": "Host-visible tool name",
  "outcome": "used | duplicate | empty | blocked | rate_limited | failed",
  "source_ids": ["S01"],
  "notes": "Material failure or routing decision"
}
```

## Final Assessment

```json
{
  "confidence": "high | medium | low",
  "bottom_line": "Bounded conclusion",
  "critical_gaps": [],
  "unresolved_conflicts": [],
  "what_would_change_the_view": [],
  "stopping_reason": "Why additional retrieval is unlikely to change the decision"
}
```

Validate a saved package with:

```bash
python3 scripts/validate_research_package.py research-package.json --strict
```

The validator checks structural and provenance invariants. It cannot determine whether a passage semantically entails a claim; the agent must still perform claim-to-evidence review.
