# Expert Mode Router

Use this file when the user asks for expert-level research, industry research, market/stock/security analysis, strategic advice, diligence, policy analysis, technology research, healthcare research, or energy/commodity research.

The router decides which expert method and export contract to load. Load one primary expert, no more than two supporting experts, and exactly one primary export. Add the source audit appendix only when justified.

## Routing Rule

Prefer one primary expert and at most two supporting experts.

| User intent | Primary expert file | Supporting expert files |
|---|---|---|
| Stock, listed company, ETF, bond, security, valuation, catalyst, earnings, portfolio watch | `references/expert-equity-securities.md` | company financials, macro policy, industry market |
| Company deep dive, business model, unit economics, filings, due diligence | `references/expert-company-financials.md` | industry market, equity securities |
| Industry, market size, competitive landscape, value chain, strategic entry | `references/expert-industry-market.md` | macro policy, company financials |
| Macro, rates, inflation, FX, trade, fiscal/monetary policy, country outlook | `references/expert-macro-policy.md` | equity securities, industry market |
| AI, software, cloud, semiconductor, technical product, benchmark, ecosystem | `references/expert-technology-product.md` | industry market, company financials |
| Healthcare, pharma, biotech, medtech, clinical trial, approval, safety | `references/expert-healthcare-life-sciences.md` | company financials, macro policy |
| Energy, power, oil/gas, renewables, grid, commodities, climate | `references/expert-energy-climate.md` | macro policy, company financials |

If the user asks for "industry expert" without a domain, start with `references/expert-industry-market.md`.

## Clarification Policy

Ask at most one compact clarification question before researching, and only when the missing information changes the research design. If the user asks for speed, proceed with assumptions.

### Universal Questions

Use these only if missing:

```text
What is the geography, time horizon, and decision context for this research?
```

### Expert-Specific Questions

| Expert | Ask when needed |
|---|---|
| Equity/securities | Ticker/security, market, time horizon, investor type, output depth |
| Company financials | Company/entity, period, peer set, diligence objective |
| Industry market | Geography, market boundary, target customer, output decision |
| Macro policy | Country/region, time horizon, policy variable, affected asset/sector |
| Technology product | Product/category, user segment, benchmark criteria, deployment context |
| Healthcare | Disease/product/device, geography, clinical/regulatory question |
| Energy | Commodity/asset/market, geography, time horizon, project or trading/investment context |

## Matching Workflow

1. Read the user's request and choose a primary expert.
2. If the request involves stocks/securities, always load `references/expert-equity-securities.md`.
3. If the request depends on current market data, browse or use finance tools; do not rely on memory.
4. If the request requires source discovery, load `references/authoritative-sources.md` or query the structured registry.
5. If the request asks for a formal report, load one matching export from `references/exports/README.md`.
6. Ask one clarification question only if needed; otherwise state assumptions and proceed.

## Output Selection

Choose the smallest export that satisfies the user:

| Need | Export file |
|---|---|
| Quick answer or general report | `references/report-template.md` |
| Security thesis/valuation | `references/exports/security-research-note.md` |
| Earnings event | `references/exports/earnings-preview-review.md` |
| Security comparison | `references/exports/security-comparison.md` |
| Security monitoring | `references/exports/security-risk-monitor.md` |
| Industry strategy | `references/exports/industry-expert-brief.md` |
| Company diligence | `references/exports/company-diligence-memo.md` |
| Macro/policy | `references/exports/macro-policy-brief.md` |
| Technology/product | `references/exports/technology-product-evaluation.md` |
| Healthcare/life sciences | `references/exports/healthcare-research-brief.md` |
| Energy/commodity | `references/exports/energy-commodity-brief.md` |
| Auditability | Add `references/exports/source-audit-appendix.md` |

Do not load every export. The export controls presentation; the expert file controls research method.

## Safety

For financial, legal, medical, and safety topics:

- Use primary and regulator sources where possible.
- State uncertainty and scope.
- Avoid personalized advice unless the user explicitly provides suitability context.
- For securities, provide research and risk framing, not a guaranteed buy/sell outcome.
