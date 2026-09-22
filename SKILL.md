---
name: "deep-research-agent"
description: "Research current or uncertain external facts, compare products/companies/markets, investigate industries or securities, and produce evidence-backed briefs or reports. Use when the answer requires web retrieval, multiple sources, source validation, or expert-domain synthesis; do not use for purely local edits or unsupported drafting."
---

# Deep Research Agent

Produce decision-useful research whose material claims can be traced to current, correctly interpreted evidence. The core workflow uses tools already available in the host; optional search, browser, platform, finance, and extraction capabilities improve reach but are not required for every task.

## Select Depth

Choose the smallest sufficient mode:

| Mode | Use | Required outcome |
|---|---|---|
| Quick | One bounded current fact | Read an authoritative source and cite the answer |
| Standard | Overview, comparison, current explanation | Cover multiple angles, read key pages, state risks/gaps |
| Pro | Report, diligence, strategy, investment research | Research map, adaptive queue, evidence ledger, validation, structured recommendation |
| Ultra | Broad/high-stakes work with interacting questions | Independent workstreams, convergence review, adversarial pass, reproducible package |

Ask one concise scope question only when geography, entity, time horizon, or decision context would materially change the method. Otherwise state reasonable assumptions and proceed.

## Route The Task

Before retrieval:

1. Define the user's decision or deliverable, entities, geography, time window, audience, exclusions, and information cutoff.
2. For expert-level industry, company, securities, macro, technology, healthcare, or energy work, read `references/expert-router.md`, then load one primary expert and no more than two supporting experts.
3. For any stock, bond, ETF, listed company valuation, earnings, catalyst, or investment-risk request, always load `references/expert-equity-securities.md`.
4. Select one primary export from `references/exports/README.md` only when a formal deliverable is needed.
5. Use `references/report-template.md` for general briefs, comparisons, or reports.

## Audit Retrieval Capabilities

For external research, inspect host-native tools, MCP/apps/plugins, local skills, browser sessions, and available CLIs before choosing a path. Read `references/retrieval-tool-planning.md` for broad search, blocked engines, social/video/forum content, JavaScript pages, scraping, or financial data.

When shell access exists, use this only as a local signal:

```bash
python3 scripts/detect_retrieval_capabilities.py
```

Tool selection is capability-first:

- Broad search: prefer Agent Reach search/Exa, Brave, Tavily, or another dedicated provider when available.
- Social, video, forums, repositories, and finance: prefer platform-native or specialized tools.
- Known official/static page: use official APIs, fetch, or a reader.
- JavaScript or interaction: use a rendered browser; use full automation only when needed and authorized.
- Multi-page corpus: use a crawler when available.
- Generic WebSearch/WebFetch: use when sufficient or as a fallback, not as an automatic first choice for search-engine discovery.

Choose fallbacks by failure cause. Do not bypass authentication, paywalls, access controls, or user authorization. A missing CLI does not prove that the host lacks the equivalent MCP or built-in tool.

## Research Loop

For Standard and above, use the detailed loop in `references/research-workflow.md` and `references/depth-and-followup.md`:

1. Build a bounded question tree around what could change the answer.
2. Search broadly enough to identify entities, terminology, original sources, controversy, and date/version signals.
3. Turn unresolved evidence needs into a queue; the next query must address a gap, conflict, missing method, source chain, or counter-hypothesis.
4. Fetch and read the strongest pages. Search snippets are discovery leads, not evidence.
5. Follow derivative claims to original filings, datasets, laws, papers, specifications, or methodology.
6. Stop a branch when it is resolved, reaches an information-gain plateau, or is explicitly classified as partial, conflicting, missing, or blocked.

For Chinese or China-related topics, search in Chinese and English and use domestic official, filing, industry, and platform sources where they are closer to the subject.

## Evidence Invariants

Read `references/source-quality.md` whenever external evidence determines the answer. Read `references/evidence-validation.md` for finance, policy, regulation, numerical comparisons, conflicting evidence, Pro/Ultra work, or auditability.

Do not deliver until these invariants hold:

- Material external claims have nearby citations to pages actually read.
- Important numbers preserve entity, period, version, geography, definition, scope/denominator, unit/currency, and method.
- Facts, attributed views, synthesis, estimates, and assumptions are distinguishable.
- One original report repeated across sites counts as one evidence origin.
- Supporting evidence and disconfirming evidence were both considered.
- Conflicts and missing evidence change the wording, confidence, or recommendation.
- Calculations that change the conclusion are reproducible from raw inputs and formulas.
- Current or point-in-time work states an as-of date; historical snapshots exclude later knowledge unless labeled hindsight.

For Pro/Ultra or resumable/auditable work, use `references/research-state-schema.md`. If a JSON research package is saved, validate it:

```bash
python3 scripts/validate_research_package.py research-package.json --strict
```

## Sources And Authority

Use `references/authoritative-sources.md` for broad source discovery. For structured filtering, query `references/source-registry.json`:

```bash
python3 scripts/query_source_registry.py --domain equity --region CN
```

The directory and registry are starting maps, not whitelists. Verify identity, recency, methodology, access, and relevance. Social/community material is useful for sentiment, complaints, language, and leads, but not as sole proof of market size, financial performance, regulatory status, or medical/safety claims.

## Delivery

Lead with the bounded answer, then the evidence, implication, risks/conflicts/gaps, and sources. Use the host's supported clickable citation format near the claim. Do not add a large methodology appendix to routine answers; use `references/exports/source-audit-appendix.md` for audit-heavy work.

Assign confidence from evidence and coverage, not prose quality:

- High: decision-critical dimensions are covered by strong, current, mostly primary or independent evidence.
- Medium: material conclusions are usable but rely on secondary evidence or contain bounded gaps.
- Low: sparse, stale, inaccessible, conflicting, or weak evidence materially limits the answer.

## Hard Stops

Stop, narrow the conclusion, or request user input when:

- Current external facts are required but no retrieval path is available.
- The requested cutoff cannot be respected or market-sensitive data cannot be timestamped.
- A decision-critical claim remains supported only by a weak source after reasonable alternatives.
- Credible sources conflict on a fact that controls the decision.
- Required data is paywalled, login-bound, unavailable, or not comparable and no authorized fallback works.
- A high-stakes conclusion would exceed the available legal, medical, financial, or safety evidence.

Never invent facts, quotations, prices, market sizes, consensus, calculations, sources, or access to unavailable content.

## Reference Routing

Load only what the task needs:

- Workflow/depth: `references/research-workflow.md`, `references/depth-and-followup.md`
- Retrieval: `references/retrieval-tool-planning.md`
- Evidence: `references/source-quality.md`, `references/evidence-validation.md`, `references/research-state-schema.md`
- Sources: `references/authoritative-sources.md`, `references/source-registry.md`
- Experts: `references/expert-router.md` and the selected `references/expert-*.md`
- Industry frame: `references/industry-expert-research.md`
- Output: `references/report-template.md` or one file under `references/exports/`

Use `scripts/markitdown_readable.py` only as an optional fallback for noisy pages or local documents when `markitdown` is installed.
