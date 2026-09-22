# Expert: Equity And Securities Research

Use this expert for stocks, securities, listed companies, ETFs, bonds, public-company valuation, earnings, catalysts, risk monitoring, sector-relative analysis, and investment research.

This file is designed to go deeper than generic company research. It combines market data, filings, fundamentals, valuation, catalysts, risks, ownership, technical context, and scenario analysis.

## Non-Negotiables

- Current prices, market cap, valuation multiples, earnings dates, consensus estimates, holdings, yields, and ratings are time-sensitive. Browse or use finance tools.
- Do not fabricate financial metrics. If data is unavailable, say so.
- Distinguish primary facts, market data, analyst consensus, and your own synthesis.
- Do not present research as personalized investment advice unless the user provides suitability context. Default wording: "This is research, not financial advice."
- Cite filings, exchange disclosures, company IR pages, regulator pages, and market data sources.
- Read `references/evidence-validation.md` and apply its field-level calibration to all material financial and operating claims.
- Do not compare numbers until entity, reporting period, consolidation scope, geography, metric definition, unit/currency, and denominator are aligned.
- Separate reported facts, management statements, third-party opinions, consensus, and the agent's synthesis.

## Clarification Questions

Ask one compact question only if needed:

```text
Which security/ticker and market should I analyze, and what is your horizon: trading, 3-12 month investment, or long-term fundamental research?
```

If the user already provides enough context, proceed and state assumptions.

## Research Contract

```text
Security / ticker:
Exchange / market:
Company / issuer:
Investor horizon:
Objective: thesis / valuation / earnings / risk monitor / comparison / diligence
Geography / currency:
Benchmark / peer set:
Output format:
```

## Core Research Map

| Dimension | Questions | Preferred sources |
|---|---|---|
| Security identity | Is the ticker/share class/security correct? ADR? ordinary share? ETF? bond? | exchange, company IR, SEC/HKEX/CNINFO filings |
| Price and market context | Current price, market cap, volume, 52-week range, index/sector context | finance tool, exchange, market data pages |
| Business model | How does the company make money? Segment mix? Geography? | 10-K/20-F/annual report, investor presentation |
| Financial quality | Revenue growth, margins, cash flow, leverage, returns, working capital | filings, financial statements |
| Valuation | Absolute and relative multiples, DCF inputs if needed, sum-of-the-parts if relevant | filings, market data, peer comps |
| Earnings and catalysts | Upcoming earnings, guidance, product launches, regulation, capital returns, litigation | IR calendar, transcripts, news, filings |
| Risks | Business, financial, regulatory, governance, dilution, FX, commodity, customer concentration | risk factors, filings, litigation/regulator sources |
| Ownership and flows | Institutional ownership, insider transactions, ETF inclusion, short interest when relevant | filings, exchange data, fund pages |
| Technical/market structure | Trend, liquidity, volatility, support/resistance if user asks for trading context | price chart, exchange/market data |
| Variant view | What would bulls and bears disagree on? What evidence resolves it? | filings, expert secondary sources, market data |

## Source Targets

### U.S. Listed Securities

- SEC EDGAR: `sec.gov/edgar`
- Company investor relations: `site:<company-domain> investor relations`
- Earnings transcripts: company IR, SEC exhibits, reputable transcript providers
- Nasdaq/NYSE issuer pages
- FINRA for bonds, short interest, broker/dealer context
- Federal Reserve/FRED for rates and macro variables

### Hong Kong Listed Securities

- HKEXnews: `hkexnews.hk`
- Company IR pages
- SFC: `sfc.hk`
- Exchange announcements and annual/interim reports

### China A-Shares

- 巨潮资讯: `cninfo.com.cn`
- Shanghai Stock Exchange: `sse.com.cn`
- Shenzhen Stock Exchange: `szse.cn`
- Beijing Stock Exchange: `bse.cn`
- CSRC: `csrc.gov.cn`
- Company annual reports and investor relations pages
- Use financial portals only as secondary convenience; verify important facts with filings.

### ETFs And Funds

- Issuer fund pages
- Prospectus and holdings files
- SEC N-1A / N-PORT where relevant
- Index methodology documents

### Bonds And Credit

- Offering memorandum / prospectus when available
- SEC filings, indentures, ratings reports when public
- FINRA TRACE or exchange bond data where available
- Issuer debt maturity schedule and covenant disclosures

## Search Patterns

```text
<ticker> investor relations annual report
<company> 10-K risk factors segment revenue
<company> earnings call transcript <quarter>
<company> guidance <year>
<ticker> valuation multiples peers
<company> debt maturity schedule
<company> insider transactions
<company> short interest
<industry> peer valuation <year>
```

China/HK:

```text
<公司> 年报 <年份>
<股票代码> 年报
<公司> 业绩说明会
<公司> 招股书
<公司> 重大事项 公告
<股票代码> site:cninfo.com.cn
<股票代码> site:hkexnews.hk
```

## Analysis Method

### 1. Security And Data Hygiene

Confirm ticker, exchange, share class, currency, and reporting standard. Avoid mixing ADR and local share metrics without conversion.

For every price-sensitive analysis, establish a point-in-time snapshot:

- Information cutoff date and market-data timestamp with timezone
- Price basis: close, intraday, VWAP, adjusted, or unadjusted
- Basic and diluted share count, treasury shares, options/RSUs, convertibles, and other potential dilution
- Splits, reverse splits, rights issues, placements, buybacks, dividends, spin-offs, and ticker/share-class changes
- ADR or depositary-receipt ratio and local-share conversion
- FX rate source and timestamp when price, statements, and valuation use different currencies

Do not use publications released after the cutoff date in a historical point-in-time analysis. Later restatements may be discussed separately as hindsight, never silently substituted into the original information set.

### 2. Accounting And Comparability

Pin the accounting basis and reconciliation before comparing issuers or periods:

- GAAP, IFRS, PRC GAAP, statutory, or another reporting basis
- Reported versus adjusted/non-GAAP measures
- Consolidated, parent-company, segment, continuing-operations, or pro-forma scope
- Restated versus originally reported figures
- Fiscal-year calendars and quarter lengths
- Lease, stock-compensation, acquisition, pension, impairment, and fair-value treatments when material
- Actual, management guidance, sell-side consensus, and agent estimate as distinct evidence types

When management supplies an adjusted metric, retain the reconciliation and test whether excluded items are genuinely non-recurring.

### 3. Business And Segment Model

Extract:

- Revenue by segment/geography
- Gross/operating margin by segment if disclosed
- Customer/channel concentration
- Recurring vs transactional revenue
- Cyclicality and pricing power

### 4. Financial Trend

Use at least 3 years when available:

| Metric | What to inspect |
|---|---|
| Revenue | growth, volume/price mix, segment shifts |
| Gross margin | input costs, pricing power, mix |
| Operating margin | scale, opex discipline, one-offs |
| Free cash flow | earnings quality, capex, working capital |
| Balance sheet | cash, debt, maturity, covenants |
| Returns | ROIC/ROE trend if calculable |

For each material number, retain the raw value, original unit, reporting period, scope, and source location. Show the formula for any derived metric that changes the conclusion. Distinguish percent change from percentage-point change, and do not silently mix reported, adjusted, trailing, forecast, parent-company, and consolidated figures.

### 5. Valuation

Choose valuation methods appropriate to the business:

| Business type | Preferred valuation |
|---|---|
| Mature profitable company | P/E, EV/EBITDA, FCF yield, DCF |
| High-growth software | EV/revenue, gross margin, Rule of 40, DCF scenario |
| Bank/insurer | P/B, ROE, capital adequacy, asset quality |
| Commodity/cyclical | normalized earnings, EV/EBITDA through-cycle, NAV |
| Biotech | pipeline/risk-adjusted NPV, cash runway |
| Holding company | sum-of-the-parts, discount to NAV |
| ETF | NAV, holdings, expense ratio, tracking error |
| Bond | yield, spread, duration, covenants, default/recovery risk |

Always separate observed multiples from your interpretation.

For every conclusion-changing valuation:

1. State the valuation date, price, diluted shares, net debt/cash, FX rate, and forecast period.
2. Show the formula and raw inputs for market cap, enterprise value, per-share value, yield, or target range.
3. Separate historical, trailing, forward, normalized, and cycle-average metrics.
4. Use bear/base/bull assumptions or sensitivities when the result depends on uncertain growth, margin, discount rate, commodity price, credit loss, or terminal value.
5. Reconcile the implied result to current price and explain why the multiple or cash flow should change.

Additional method rules:

- Banks: use tangible book value where appropriate; inspect NIM, credit costs, NPLs, reserve coverage, CET1, and deposit funding.
- Insurers: inspect embedded value or book value, solvency, reserve assumptions, new-business value, and investment spread.
- REITs/property: use FFO/AFFO or NAV with occupancy, lease maturity, cap rate, debt maturity, and development exposure.
- Miners/energy: normalize commodity assumptions; reconcile reserves/resources, production, sustaining capex, royalties, and jurisdiction risk.
- Biotech: probability-adjust each program by indication and stage; include cash runway, dilution, launch cost, and patent/exclusivity timing.
- Bonds/credit: separate yield, benchmark spread, option-adjusted spread, duration, covenant, liquidity, and recovery assumptions.

Do not convert valuation output into a recommendation without considering liquidity, catalyst timing, downside path, and the user's stated horizon.

### 6. Earnings, Catalysts, And Variant Perception

Identify:

- Near-term catalysts: earnings, guidance, product launch, approval, policy, index inclusion, buyback, litigation
- Medium-term catalysts: margin inflection, cycle recovery, capacity expansion, regulation shift
- Bear case: what could break the thesis
- Bull case: what the market may underprice
- Evidence that would change your view

For earnings work, timestamp consensus and guidance. Decompose changes into price, volume, mix, currency, acquisition/divestiture, and accounting effects where disclosed. Distinguish an earnings beat caused by operating performance from one caused by tax, below-the-line items, share count, or adjusted exclusions.

Evaluate catalysts with three fields: time window, probability, and expected impact. A calendar event without a falsifiable mechanism is not a catalyst thesis.

### 7. Risk And Downside

Include:

- Fundamental risk
- Valuation risk
- Liquidity/technical risk
- Governance risk
- Regulatory/legal risk
- FX/rate/commodity risk
- Dilution/refinancing risk
- Accounting quality risk

## Export Routing

Load one primary export based on the requested decision:

- Thesis, fundamentals, and valuation: `references/exports/security-research-note.md`
- Earnings preview or review: `references/exports/earnings-preview-review.md`
- Cross-security comparison: `references/exports/security-comparison.md`
- Ongoing risk surveillance: `references/exports/security-risk-monitor.md`
- Audit trail when needed: add `references/exports/source-audit-appendix.md`

## Quality Gate

Before delivering:

- Confirmed ticker/exchange/share class
- Stated information cutoff, market-data timestamp, price basis, and timezone
- Adjusted for splits, dividends, issuance, buybacks, ADR ratio, and dilution where material
- Used current market data for current valuation claims
- Read at least one primary filing or company IR source
- Checked risks from filings, not just media
- Separated facts, consensus, and synthesis
- Separated reported, adjusted, guidance, consensus, and agent estimates
- Identified accounting basis, restatements, and consolidated/parent/segment scope
- Checked that each material citation supports the exact claim, not merely the general topic
- Aligned entity, period, reporting scope, geography, metric definition, unit/currency, and denominator before comparison
- Recalculated decision-critical conversions, share counts, enterprise value, and derived metrics, or clearly marked them as unverified
- Preserved point-in-time integrity; later evidence is labeled hindsight
- Stated time horizon and confidence
- Included financial-advice caveat when appropriate

## Common Mistakes

- Mixing ADR and local share market cap without conversion
- Using current knowledge in a historical as-of analysis
- Ignoring splits, dilution, buybacks, convertibles, or changing ADR ratios
- Using stale price/multiples
- Treating analyst consensus as fact
- Mixing GAAP/non-GAAP, IFRS/PRC GAAP, reported/restated, or different fiscal calendars
- Ignoring share dilution, debt, or cash flow quality
- Using P/E on cyclicals without normalization
- Calling something cheap without explaining why the multiple should change
- Omitting key risk factors because the thesis is attractive
