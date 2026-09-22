# Deep Research Agent

A zero-configuration core skill for evidence-backed web research, expert-domain analysis, and auditable reports.

It brings DeerFlow-inspired research behavior into native agent hosts without requiring a custom runtime or model provider layer. The core works with retrieval tools already exposed by the host; Agent Reach, dedicated search providers, rendered browsers, crawlers, social channels, and finance tools are optional capability upgrades.

## Why This Skill

Most research failures are not caused by weak prose. They come from stopping after one search, citing snippets, mixing incompatible numbers, counting syndicated articles as independent evidence, or hiding gaps behind a polished answer.

Deep Research Agent provides:

- capability-aware retrieval planning and failure-specific fallback
- broad-to-narrow discovery with adaptive follow-up questions
- source-chain tracing from summaries to original evidence
- authority, freshness, independence, and contradiction checks
- field-level validation for entity, period, version, geography, definition, scope, unit, and method
- reproducible calculations and point-in-time discipline
- expert modes for securities, companies, industries, macro/policy, technology, healthcare, and energy
- one-file-per-deliverable export specifications
- a machine-readable research package and deterministic validator
- behavioral evaluation cases for regression testing

## Quick Start

Install the skill, then invoke it explicitly in an agent prompt:

```text
Use $deep-research-agent in Pro mode to research the China industrial robotics market. Define the market boundary, compare market-size methodologies, map the value chain and competitors, identify demand drivers and risks, and produce an industry expert brief with citations.
```

The skill can also be selected automatically by hosts that support implicit skill discovery.

- [Detailed usage guide](docs/USAGE.md)
- [Copy-ready example prompts](examples/PROMPTS.md)

## Research Modes

| Mode | Best for | Quality bar |
|---|---|---|
| Quick | One bounded current fact | Read an authoritative source and cite the answer |
| Standard | Overview, comparison, current explanation | Multiple angles, key pages read, risks and gaps visible |
| Pro | Reports, diligence, strategy, investment research | Research queue, evidence ledger, validation, structured recommendation |
| Ultra | Broad or high-stakes research | Independent workstreams, adversarial review, convergence, reproducible package |

## How It Works

~~~text
User decision
  -> mode + expert routing
  -> host capability audit
  -> question tree and retrieval plan
  -> broad discovery
  -> gap/conflict/source-chain follow-ups
  -> claim and calculation validation
  -> expert-specific export
  -> confidence, gaps, and sources
~~~

Search-engine discovery does not automatically begin with generic WebSearch/WebFetch. The skill prefers dedicated search or Agent Reach when available, platform-native tools for platform content, official APIs/fetch for known primary pages, rendered browsers for JavaScript, and crawlers for multi-page corpora. Fallbacks are selected from the actual failure cause.

## Expert Modes And Exports

| Expert | Typical questions | Primary exports |
|---|---|---|
| Equity and securities | Thesis, valuation, earnings, catalysts, security risk | Research note, earnings review, comparison, risk monitor |
| Company financials | Business model, statements, unit economics, diligence | Company diligence memo |
| Industry and market | Market size, value chain, competition, entry strategy | Industry expert brief |
| Macro and policy | Rates, inflation, FX, fiscal/regulatory transmission | Macro policy brief |
| Technology and product | Capability, architecture, benchmark, security, cost | Technology/product evaluation |
| Healthcare and life sciences | Trials, efficacy, safety, approval, reimbursement | Healthcare research brief |
| Energy and commodities | Supply/demand, infrastructure, policy, project economics | Energy/commodity brief |

The expert file defines how to research. The export file defines how to present the result. Only the selected expert and export need to be loaded.

The securities expert includes:

- information-cutoff and market-data timestamps
- share class, ADR ratio, diluted shares, splits, dividends, issuance, and buybacks
- GAAP, IFRS, PRC GAAP, adjusted metrics, restatements, and reporting-scope reconciliation
- actual, guidance, consensus, and agent-estimate separation
- business-specific valuation methods for banks, insurers, REITs, commodities, biotech, funds, and credit
- reproducible bear/base/bull valuation inputs
- probability, time-window, and impact assessment for catalysts

## Capability Audit

The skill first inspects host-native tools, MCP/apps/plugins, browser sessions, local skills, and CLIs. A bundled local probe provides an additional signal without network access or credential reads:

~~~bash
python3 scripts/detect_retrieval_capabilities.py
~~~

The result deliberately distinguishes local executables from host-only capabilities. For example, an Agent Reach skill or MCP backend may be available even when an agent-reach executable is absent.

## Structured Sources

references/authoritative-sources.md is the broad human-readable source directory. references/source-registry.json is a selective machine-readable registry with region, research domain, evidence role, authority, access, format, freshness, query patterns, and limitations.

~~~bash
python3 scripts/query_source_registry.py --domain equity --region CN
python3 scripts/query_source_registry.py --domain healthcare --authority primary
~~~

The registry is a starting map, not a whitelist. Every source still requires identity, recency, methodology, and claim-support checks.

## Reproducible Research Packages

Pro/Ultra or audit-sensitive work can save a JSON research package containing:

- research contract and information cutoff
- retrieval capability profile
- question branches and resolution status
- source records and independent-origin identifiers
- atomic claims and validation status
- raw calculation inputs and formulas
- coverage matrix and retrieval log
- final confidence, gaps, conflicts, and stopping reason

Validate the package:

~~~bash
python3 scripts/validate_research_package.py research-package.json --strict
~~~

The validator checks structural and provenance invariants. Semantic entailment between a passage and a claim still requires agent review.

## Behavioral Evaluation

The repository includes ten regression cases covering current facts, bilingual China industry research, A-share point-in-time analysis, ADR/share-class normalization, conflicting market sizes, social sentiment, blocked-search fallback, paywalls, healthcare comparison, and duplicate news echoes.

~~~bash
python3 scripts/validate_eval_cases.py evals/cases.json
python3 scripts/validate_research_package.py evals/fixtures/valid-research-package.json --strict
python3 scripts/score_eval_results.py evals/results.example.json
~~~

The rubric scores coverage, citation support, source independence, freshness, numerical consistency, tool routing, decision usefulness, and uncertainty discipline. Citation-support and numerical-consistency regressions should block release even when the total score improves.

## Installation

Install this repository as deep-research-agent in the skill directory used by the target host. For Codex:

~~~bash
cp -R /path/to/DeepResearch ~/.codex/skills/deep-research-agent
~~~

No API key is required by the skill itself.

- Core profile: uses capabilities already present in the host.
- Enhanced profile: gains reach from Agent Reach, Exa/Brave/Tavily, browser rendering, Firecrawl, finance data, or authenticated platform tools when those are separately available and authorized.

## Repository Structure

~~~text
.
├── SKILL.md
├── agents/
│   └── openai.yaml
├── evals/
│   ├── README.md
│   ├── cases.json
│   ├── results.example.json
│   └── fixtures/
│       └── valid-research-package.json
├── docs/
│   └── USAGE.md
├── examples/
│   └── PROMPTS.md
├── references/
│   ├── authoritative-sources.md
│   ├── source-registry.md
│   ├── source-registry.json
│   ├── research-workflow.md
│   ├── depth-and-followup.md
│   ├── retrieval-tool-planning.md
│   ├── source-quality.md
│   ├── evidence-validation.md
│   ├── research-state-schema.md
│   ├── expert-router.md
│   ├── expert-*.md
│   ├── exports/
│   │   ├── README.md
│   │   └── <one file per deliverable>.md
│   └── report-template.md
└── scripts/
    ├── detect_retrieval_capabilities.py
    ├── markitdown_readable.py
    ├── query_source_registry.py
    ├── score_eval_results.py
    ├── validate_eval_cases.py
    └── validate_research_package.py
~~~

## Optional Document Extraction

scripts/markitdown_readable.py can convert noisy web pages or local PDF/Office files when the optional markitdown package is installed:

~~~bash
python3 scripts/markitdown_readable.py "https://example.com"
python3 scripts/markitdown_readable.py ./source.pdf -o source.md
~~~

This is a readability fallback, not a retrieval engine and not a core dependency.

## Design Principles

- Research before synthesis
- Capability-first retrieval
- Full sources over snippets
- Claims validated separately from source reputation
- One evidence origin counted once
- Point-in-time integrity for historical and market work
- Counter-evidence before confidence
- Visible uncertainty instead of invented precision
- Evidence-gain stopping rather than arbitrary search counts
- Progressive loading instead of one giant prompt

## Relationship To DeerFlow

This project adopts DeerFlow's strongest research ideas: staged investigation, broad-to-narrow search, mode selection, evidence discipline, structured synthesis, and specialized research paths.

It intentionally does not reproduce DeerFlow's runtime, model/provider configuration, sandbox, or executor. Native host tools remain responsible for retrieval and execution; this skill supplies the research protocol, expert methods, schemas, validators, and export contracts.

## Validation

Run the structural validator:

~~~bash
python3 /path/to/skill-creator/scripts/quick_validate.py /path/to/DeepResearch
~~~

Expected result:

~~~text
Skill is valid!
~~~
