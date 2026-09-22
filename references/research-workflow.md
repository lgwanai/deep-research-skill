# Research Workflow

Use this file for Standard, Pro, and Ultra research. The goal is to produce useful conclusions, not just a pile of links.

## Phase 0: Research Contract

Before writing the research contract, perform a retrieval tool audit when the task needs external information. Use `references/retrieval-tool-planning.md` for platform-specific, social, video, finance, JavaScript-heavy, or scraping-heavy tasks.

For Pro/Ultra or resumable/auditable work, initialize the state described in `references/research-state-schema.md`. Update branches, sources, claims, calculations, coverage, and the retrieval log as work progresses. Keep this state internal unless the user requests an export.

Establish the contract in one short internal note or visible plan:

```text
Goal:
Decision/output:
Scope:
Time window:
Required source types:
Best retrieval tools:
Likely risks/unknowns:
```

Ask one clarifying question only when a missing boundary would materially change the work. Otherwise state assumptions and proceed.

## Phase 1: Broad Exploration

Purpose: map the terrain.

Run 2-4 broad searches using different phrasings:

- `<topic> overview <current year>`
- `<topic> latest <month/year>`
- `<topic> official docs OR announcement OR filing`
- `<topic> market analysis OR case study OR limitations`

Use the retrieval tools selected in Phase 0. If search engines block or degrade generic websearch/webfetch, switch to Agent Reach, Brave, Tavily, Exa, Lightpanda/rendered browser, or platform-native tools before treating the dimension as uncovered.

Capture recurring:

- Entities, products, people, organizations
- Dates, versions, releases, regulations
- Metrics, benchmarks, market numbers
- Disagreements or surprising claims
- Sources that appear original rather than derivative

Do not conclude yet.

After the broad pass, create the research queue described in `references/depth-and-followup.md`. Broad exploration maps the terrain; it does not satisfy a decision-critical question by itself.

### Query Auto-Expansion

After the first round of broad searches, extract seed terms from results to generate follow-up queries automatically. This prevents the agent from overlooking important sub-topics.

Extract from page titles, headings, and key paragraphs:

- **Entities**: products, companies, people, organizations mentioned
- **Technical terms**: acronyms, APIs, protocols, model names, version identifiers
- **Controversy signals**: "however", "limitation", "criticism", "issue", "concern"
- **Temporal markers**: dates, release versions, announcement months

Generate the second round of queries by combining the original topic with extracted terms:

```text
Original: <topic>
Expanded:
- <topic> + <extracted entity> + comparison
- <topic> + <extracted term> + limitations
- <topic> + <extracted entity> + <current year>
- <extracted controversy> + <topic>
```

This replaces ad-hoc "what else should I search" decision-making with a mechanical step.

Auto-expansion must not become a list of near-duplicate keyword searches. Convert useful discoveries into follow-up branches: trace the original source, inspect the method behind a number, test an alternative explanation, resolve a scope mismatch, or search for evidence that would overturn the emerging conclusion. Use `references/depth-and-followup.md`.

### Query Diversity Check

Before moving to deep dive, verify the query set covers:

- At least one query targeting official/primary sources
- At least one query targeting criticism or limitations
- At least one query with a time anchor (year, month, or `after:` filter)
- Queries with different phrasings, not just keyword variants
- If the topic has a Chinese/international dimension, at least one query in the relevant language

### Retrieval Fallback Chain

When a search yields no useful results, follow this chain before declaring the dimension uncovered:

```text
1. Exact query (specific terms, quotes, filters)
2. Relax query (remove quotes, broaden terms, drop year anchor)
3. Synonym rewrite (use alternative terminology, related concepts)
4. Change search source (if the host supports multiple search backends)
5. Search for adjacent topics that imply the target information
6. Declare gap with a note of what was attempted
```

Track fallback steps internally. Include them in the final report only when they affect confidence, leave an important gap, or the user asks for auditability.

## Phase 2: Dimension Mapping

Turn the exploration into a research map. Typical dimensions:

| Dimension | What to look for |
|---|---|
| Definition/scope | What exactly is included/excluded |
| Official facts | Docs, release notes, filings, standards, laws |
| Data/metrics | Market size, price, performance, adoption, benchmarks |
| Use cases/examples | Concrete implementations or case studies |
| Competitive context | Alternatives, substitutes, tradeoffs |
| Risk/criticism | Limits, failures, controversies, compliance |
| Time line | What changed, when, and why it matters |

For comparisons, create a matrix before deep diving:

```text
Objects: A, B, C
Dimensions: capability, cost, maturity, ecosystem, risk, best fit
Must verify: current pricing, release status, known limitations
```

## Phase 3: Deep Dive

Search each important dimension separately. Good query patterns:

Run deep dive as an adaptive loop rather than a single batch. After every round, update each critical branch as resolved, partial, conflicting, or missing; generate the next query from the unresolved reason. Do not move to synthesis while a decision-critical branch is merely "relevant results found."

- Official: `<entity> official docs`, `<entity> release notes <year>`, `<entity> pricing <year>`
- Data: `<topic> statistics <year>`, `<topic> market size <year>`, `<topic> benchmark`
- Cases: `<topic> case study`, `<entity> customer story`, `<technology> production use`
- Criticism: `<topic> limitations`, `<topic> risks`, `<topic> controversy`, `<topic> security concerns`
- Comparison: `<A> vs <B> <year>`, `<A> alternatives`, `<category> buyer guide`
- Academic: `<topic> paper`, `<topic> systematic review`, `<topic> arxiv`
- Chinese ecosystem: `<topic> 知乎`, `<topic> 微信公众号`, `<topic> 研究报告 PDF`, `<topic> 白皮书`, `<topic> site:gov.cn`

Fetch full pages for sources that support key claims. When a page references a more primary source, follow it.

### Parallel Fetch Strategy

For Standard mode and above, fetch multiple candidate pages in parallel rather than sequentially. This reduces wall-clock time and prevents anchoring on the first source read.

```text
1. Identify candidate URLs from search results (top 3-5 per dimension)
2. Fetch all candidates in parallel
3. Skim each for: publication date, author/organization, data presence, primary-source links
4. Prioritize deep reading of the strongest 1-2 per dimension
5. If none meet the quality bar, trigger the fallback chain
```

### Retrieval Budget Management

Allocate search and fetch capacity by dimension importance, not evenly:

| Priority | Dimension type | Budget share |
|---|---|---|
| High | Core facts, official data, pricing/specs | 40% of searches + fetches |
| Medium | Independent analysis, use cases, comparisons | 35% |
| Low | Background context, historical timeline, community sentiment | 25% |

**Early stopping rule**: If two consecutive searches in a dimension return no new facts (only restatements of already-collected information), stop that dimension and reallocate budget to others.

Apply early stopping only after checking whether the branch still lacks an original source, method, scope, counter-evidence, or conflict resolution. Repeated summaries are a reason to change retrieval strategy, not automatically a reason to abandon a critical branch.

### Structured Data Extraction

When fetching pages, actively extract structured information instead of treating all content as flat text:

- **Tables**: Extract `<table>` elements as markdown tables. If markitdown flattens them, note the data loss and try alternative extraction.
- **Dates and versions**: Pull from `<meta>` tags, headings, and first paragraphs. Record in `YYYY-MM-DD` format for comparison.
- **Numbers and metrics**: Extract with units and context (e.g., "$12.5B (2025 revenue, GAAP)"), not as bare digits.
- **Author/organization**: Extract from bylines, `<meta name="author">`, schema.org `author` properties, or page footers.

Use `scripts/markitdown_readable.py` when native fetch returns noisy HTML or the input is a local document. If markitdown is not installed, skip it and work with raw fetch output. Mention installation only if extraction quality was a blocker.

## Phase 4: Evidence Ledger

For Pro/Ultra tasks, keep a compact evidence ledger. It can stay internal unless useful to show.

```markdown
| Claim | Source | Type | Date | Confidence | Notes |
|---|---|---|---|---|---|
| ... | ... | primary / secondary / community | ... | high / medium / low | ... |
```

For finance, policy, metrics, comparisons, or other correctness-sensitive work, use the expanded ledger and calibration rules in `references/evidence-validation.md`. A source is not accepted merely because it is authoritative: the exact passage must support the exact claim under the same entity, period, scope, version, metric definition, and unit.

When a machine-readable package is created, validate it before delivery:

```bash
python3 scripts/validate_research_package.py research-package.json --strict
```

Confidence guide:

- High: primary source, or multiple independent reliable sources agree
- Medium: one reliable secondary source, or primary source with ambiguity
- Low: community/social/marketing-only, old source, or unverified single-source claim

## Phase 5: Conflict And Gap Handling

If sources conflict:

1. Compare publication/update dates.
2. Prefer primary sources for direct facts.
3. Check whether geography, edition, version, or time window differs.
4. Report the conflict instead of forcing a false consensus.

**Contradiction detection**: When two or more sources provide different values for the same factual dimension (same market, same time window, same metric), flag them explicitly:

```markdown
Data conflict detected:
- Source A claims: $10B market size (2025, [citation])
- Source B claims: $15B market size (2025, [citation])
- Resolution attempt: Source A counts domestic only; Source B counts global. Reporting both with scope notes.
```

If data is missing:

- State what was searched.
- State the nearest available proxy if useful.
- Do not invent estimates unless explicitly asked to model assumptions; label estimates clearly.

Before synthesis, run a claim-level validation pass for decision-critical statements:

1. Classify each statement as source fact, attributed view, synthesis, estimate, or assumption.
2. Check the citation at passage level, not only page level.
3. Normalize entity, period, geography, version, metric definition, unit/currency, and denominator.
4. Recalculate conversions, growth rates, percentage-point changes, and totals when they affect the conclusion.
5. Downgrade, rewrite, or remove statements that are only partially supported.

Use `references/evidence-validation.md` for the full procedure and output statuses.

**Gap escalation log**: Track which dimensions required fallback. Show this table only for Pro/Ultra reports, disputed research, or when the retrieval gap affects the recommendation:

```markdown
| Dimension | Attempts | Highest fallback level | Outcome |
|---|---|---|---|
| Pricing | 3 searches | Level 4 (changed source) | Found 2025 data, 2026 not yet published |
| Security audit | 2 searches | Level 2 (relaxed query) | Found independent review |
| Competitor B revenue | 4 searches | Level 6 (declared gap) | Private company, no public filings |
```

## Phase 6: Synthesis

Synthesize by answering:

- What is the bottom line?
- What evidence most strongly supports it?
- What changes by segment, geography, time, or use case?
- What should the user do with this information?
- What remains uncertain?

Avoid source-by-source summaries unless the user asked for an annotated bibliography. Group facts into findings.

### Retrieval Coverage Self-Check

Before delivering the final answer, verify coverage against the research map. For normal answers, this can be an internal check. For Pro/Ultra reports, include a compact public version when it improves trust:

```markdown
## Coverage Checklist

| Dimension | Covered? | Source count | Best source type | Confidence |
|---|---|---|---|---|
| Official/primary facts | covered / partial / missing | N | primary / secondary / community | high / med / low |
| Data and metrics | | | | |
| Independent analysis | | | | |
| Examples/cases | | | | |
| Risks, limits, criticism | | | | |
| Implications for user goal | | | | |

Overall confidence: High / Medium / Low
```

**Red flags that demand more research before delivering**:

- Any decision-critical row marked missing
- Any row with only 1 source AND that source is low-quality
- Overall confidence rated Low
- Key user question cannot be answered from collected evidence

### Retrieval Reproducibility

Record the search queries and fetched URLs for auditability. Include this log only for Pro/Ultra reports, user-requested methodology, high-stakes topics, or materially weak/conflicting evidence:

```markdown
## Research Log

**Searches performed** (date: YYYY-MM-DD):
1. `<query>` — returned N results, used M
2. ...

**Pages fetched and read**:
- [Title](URL) — date, author, why used
- ...

**Pages considered but not used** (with reason):
- [Title](URL) — stale (2022), marketing-only, paywalled, etc.
```

## Mode Checklists

### Quick

- 1-2 targeted searches
- 1 fetched authoritative source
- Inline citation for the answer
- Mention uncertainty if source freshness is weak
- If the source is low-quality, state it and suggest a Standard search

### Standard

- 3+ search angles (with query auto-expansion applied)
- 3+ relevant sources (with parallel fetch for efficiency)
- Fetch official/primary source when available
- Include limitations or counterpoint
- Sources section with why each source matters
- Run the coverage self-check before delivering; include it only if useful

### Pro

- Research contract and map
- Adaptive research queue with multi-hop source tracing and unresolved-question follow-ups
- Dimension-specific searches with query auto-expansion
- Parallel fetch with budget allocation
- Evidence ledger
- Field-level calibration and claim-to-evidence validation for correctness-sensitive claims
- Source quality and freshness check
- Contradiction auto-detection
- Counter-evidence pass against the emerging conclusion
- Gap escalation log
- Structured answer or report with recommendations
- Full coverage self-check; include a reproducibility log when trust/auditability matters

### Ultra

- Workstreams by dimension/entity
- Explicit question tree and source graph for each decision-critical workstream
- Assign each workstream its own research contract, question tree, queue, evidence ledger, and stopping decision
- Batch independent searches/fetches across workstreams while preserving separate evidence trails
- Run foundation, source-chain, gap/conflict, challenge, and freshness passes inside every critical workstream
- Reallocate search and fetch budget after each convergence review toward unresolved high-impact branches
- Perform interim synthesis after each batch, then generate new cross-workstream questions from dependencies and inconsistencies
- Run cross-workstream adjudication for shared entities, metrics, dates, causal claims, and conflicting conclusions
- Run an independent adversarial pass that attempts to overturn the emerging answer and identifies omitted explanations
- Iteratively close every critical branch as resolved, partial, conflicting, missing, or blocked
- Do not finalize while a decision-critical workstream remains merely open; explain any partial, conflicting, missing, or blocked result
- Explicit scope, methodology, confidence, gaps, and reasons for stopping
- Auditable claim register with normalized fields, evidence locations, conflict status, and validation result
- Entity-by-dimension coverage matrix and cross-workstream dependency map
- Consider tables, timelines, source graphs, and causal diagrams when they improve clarity
- Complete retrieval reproducibility package: exact queries, tools/routes, pages read, pages rejected with reasons, source-chain paths, workstream decisions, and unresolved items

## Chinese Ecosystem Search Strategy

When the topic involves China, or the user's context is Chinese, adapt the search strategy beyond English-web defaults:

### Platform-Specific Queries

| Platform | Query pattern | Best for |
|---|---|---|
| 微信公众号 | `<topic> 公众号` or `site:mp.weixin.qq.com <topic>` | Industry analysis, official announcements |
| 知乎 | `<topic> 知乎` or `site:zhihu.com <topic>` | Practitioner experience, in-depth discussion |
| 政府网站 | `<topic> site:gov.cn` | Policy, regulation, official data |
| 学术 | `<topic> site:cnki.net` or `<topic> 知网` | Academic papers, theses |
| 行业报告 | `<topic> 研究报告 PDF` or `<topic> 白皮书` | Industry reports, white papers |
| 36Kr / 虎嗅 | `<topic> site:36kr.com` or `<topic> site:huxiu.com` | Tech/business news and analysis |

### Bilingual Search

For topics with both Chinese and international dimensions:

1. Run parallel searches in Chinese and English
2. Cross-reference: Chinese-language sources often have better coverage of domestic policy, market data, and local use cases; English-language sources often lead on international standards, global market data, and technology trends
3. Flag when only one language's sources are found — the picture may be incomplete

### Chinese Source Quality Notes

- WeChat articles (微信公众号): Can be high-quality original analysis but verify author credentials; many are marketing-driven
- Zhihu (知乎): Good for practitioner insights and technical deep-dives; check author background, not all answers are expert
- Government sites (.gov.cn): Authoritative for policy/regulation but may lag on implementation details
- Industry reports from Chinese research firms (艾瑞, 易观, QuestMobile): Cite methodology when available; many are commissioned by vendors

## Stop Criteria

Research is sufficient when:

- Main dimensions are covered
- Key claims have citations
- You fetched full content for the most important sources
- You checked for currentness and contradiction
- Additional searches repeat the same facts or do not affect the answer

Continue researching when:

- A conclusion rests on snippets only
- The strongest source is undated or low quality
- Numbers differ materially across sources
- The user needs a decision and risks are not covered
