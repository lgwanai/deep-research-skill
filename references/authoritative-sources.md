# Authoritative Sources Directory

Use this directory to discover high-quality source targets before broad web search, especially for industry research, policy, finance, healthcare, energy, technology, standards, and China/international comparisons.

This is a starting map, not a whitelist. Always verify recency, scope, methodology, and whether a source is primary, secondary, or commercial.

For automatic filtering by research domain, region, evidence role, access, and format, use `references/source-registry.json` with `scripts/query_source_registry.py`. The structured registry is selective; this document remains the broader human-readable directory.

For stock and securities research, also read `references/expert-equity-securities.md` because source choice depends on exchange, instrument type, share class, and time horizon.

## How To Use

1. Identify the domain and geography.
2. Search official/authority sources first.
3. Use analyst, media, and community sources to interpret, not to replace primary evidence.
4. Prefer source-specific queries:

```text
site:<domain> <topic> <year>
site:<domain> <company> annual report
site:<domain> <industry> market size
site:<domain> <policy topic> regulation
```

5. When a paid report snippet appears, cite only what is publicly visible and clearly label limitations.

## Global Statistics And Macro

| Source | Site / query target | Best for |
|---|---|---|
| World Bank | `worldbank.org`, `data.worldbank.org` | macro indicators, development data |
| IMF | `imf.org` | macro outlook, financial stability, country data |
| OECD | `oecd.org`, `data.oecd.org` | developed economy indicators, policy analysis |
| UN Data | `data.un.org` | global official statistics |
| UNCTAD | `unctad.org` | trade, investment, digital economy |
| WTO | `wto.org` | trade rules, trade statistics |
| ILO | `ilo.org` | labor statistics and employment |
| BIS | `bis.org` | banking, monetary, financial stability |
| FRED | `fred.stlouisfed.org` | U.S. and global economic time series |

## China Statistics, Policy, And Industry

| Source | Site / query target | Best for |
|---|---|---|
| 国家统计局 | `stats.gov.cn` | official China statistics |
| 中国政府网 | `gov.cn` | national policy and State Council documents |
| 国家发改委 | `ndrc.gov.cn` | macro policy, pricing, industry policy |
| 工信部 | `miit.gov.cn` | technology, manufacturing, telecom, industrial policy |
| 商务部 | `mofcom.gov.cn` | trade, commerce, foreign investment |
| 央行 | `pbc.gov.cn` | monetary policy, finance statistics |
| 国家金融监督管理总局 | `nfsa.gov.cn` | banking and insurance regulation |
| 证监会 | `csrc.gov.cn` | securities regulation |
| 国家市场监督管理总局 | `samr.gov.cn` | market regulation, antitrust, product standards |
| 海关总署 | `customs.gov.cn` | import/export statistics |
| 国家能源局 | `nea.gov.cn` | energy policy and energy statistics |
| 国家药监局 | `nmpa.gov.cn` | drugs, medical devices, cosmetics approvals |
| 国家知识产权局 | `cnipa.gov.cn` | patents and intellectual property |
| 中国信通院 | `caict.ac.cn` | ICT, cloud, AI, digital economy reports |
| 中国汽车工业协会 | `caam.org.cn` | auto production/sales and industry data |

## Company, Finance, And Capital Markets

| Source | Site / query target | Best for |
|---|---|---|
| SEC EDGAR | `sec.gov/edgar` | U.S. public company filings, 10-K, 10-Q, S-1 |
| Companies House | `companieshouse.gov.uk` | UK company filings |
| ESMA | `esma.europa.eu` | EU securities regulation |
| HKEXnews | `hkexnews.hk` | Hong Kong listed company announcements |
| Shanghai Stock Exchange | `sse.com.cn` | Shanghai-listed filings |
| Shenzhen Stock Exchange | `szse.cn` | Shenzhen-listed filings |
| Beijing Stock Exchange | `bse.cn` | Beijing-listed filings |
| National Enterprise Credit Information Publicity System | `gsxt.gov.cn` | China company registration |
| Investor relations pages | `site:<company-domain> investor relations annual report` | company strategy, segment data, risk factors |

## Standards, Regulation, And Legal

| Source | Site / query target | Best for |
|---|---|---|
| ISO | `iso.org` | international standards |
| IEC | `iec.ch` | electrotechnical standards |
| IEEE Standards | `standards.ieee.org` | technical standards |
| IETF RFC | `rfc-editor.org`, `ietf.org` | internet standards |
| W3C | `w3.org` | web standards |
| NIST | `nist.gov` | cybersecurity, AI risk, measurement standards |
| FTC | `ftc.gov` | U.S. consumer protection, competition |
| FDA | `fda.gov` | U.S. drugs, devices, food |
| EMA | `ema.europa.eu` | EU medicines regulation |
| European Commission | `commission.europa.eu`, `digital-strategy.ec.europa.eu` | EU policy and regulation |
| EUR-Lex | `eur-lex.europa.eu` | EU legal text |
| GovInfo | `govinfo.gov` | U.S. federal legal/public documents |

## Technology, AI, And Open Source

| Source | Site / query target | Best for |
|---|---|---|
| Official product docs | `site:<vendor-domain> docs` | capabilities, APIs, limits |
| Official release notes | `site:<vendor-domain> release notes` | dates, changes, deprecations |
| GitHub | `github.com` | source code, releases, issues, adoption signals |
| arXiv | `arxiv.org` | preprints and technical research |
| Papers With Code | `paperswithcode.com` | ML benchmarks and paper implementations |
| Hugging Face | `huggingface.co` | models, datasets, model cards |
| OpenAI | `openai.com`, `platform.openai.com` | OpenAI product/API facts |
| Anthropic | `anthropic.com`, `docs.anthropic.com` | Claude product/API facts |
| Google AI / DeepMind | `ai.google`, `deepmind.google` | Google model and research updates |
| Microsoft Research | `microsoft.com/research` | research papers and technical reports |
| ACM Digital Library | `dl.acm.org` | computer science papers |
| IEEE Xplore | `ieeexplore.ieee.org` | engineering and technical papers |

## Healthcare, Pharma, And Life Sciences

| Source | Site / query target | Best for |
|---|---|---|
| WHO | `who.int` | global health guidance and statistics |
| CDC | `cdc.gov` | U.S. public health data |
| NIH | `nih.gov` | biomedical research |
| PubMed | `pubmed.ncbi.nlm.nih.gov` | peer-reviewed biomedical literature |
| ClinicalTrials.gov | `clinicaltrials.gov` | clinical trial registrations |
| FDA | `fda.gov` | U.S. drug/device approvals and safety |
| EMA | `ema.europa.eu` | EU medicines |
| NMPA | `nmpa.gov.cn` | China drug/device/cosmetics approvals |
| Drug labels | `accessdata.fda.gov`, regulator label pages | prescribing information and safety |

## Energy, Climate, And Commodities

| Source | Site / query target | Best for |
|---|---|---|
| IEA | `iea.org` | energy outlook, technology, demand/supply |
| EIA | `eia.gov` | U.S. and global energy statistics |
| IPCC | `ipcc.ch` | climate science assessments |
| IRENA | `irena.org` | renewable energy |
| OPEC | `opec.org` | oil market reports |
| World Nuclear Association | `world-nuclear.org` | nuclear energy data |
| National energy regulators | `site:<country regulator>` | local energy regulation and tariffs |

## Consumer, Internet, And Advertising

| Source | Site / query target | Best for |
|---|---|---|
| Company filings | `annual report`, `10-K`, `S-1` | revenue, users, risks, segments |
| Platform ads libraries | `facebook.com/ads/library`, `adstransparency.google.com` | ad activity and messaging |
| App stores | `apps.apple.com`, `play.google.com` | app positioning, reviews, release notes |
| Similarweb / Sensor Tower / data.ai | public pages only | traffic/app ranking clues; usually partial |
| QuestMobile | `questmobile.com.cn` | China mobile internet reports |
| CNNIC | `cnnic.cn` | China internet development reports |

## Consulting, Analyst, And Industry Research

These sources are useful but often commercial. Treat them as expert secondary sources, not primary facts unless methodology is visible.

| Source | Site / query target | Best for |
|---|---|---|
| McKinsey | `mckinsey.com` | strategy, industry trends |
| BCG | `bcg.com` | strategy, sector analysis |
| Bain | `bain.com` | consumer, private equity, strategy |
| Deloitte | `deloitte.com` | industry outlooks |
| PwC | `pwc.com` | tax, regulation, industry reports |
| EY | `ey.com` | industry and finance |
| KPMG | `kpmg.com` | audit, finance, industry |
| Gartner | `gartner.com` | enterprise technology categories |
| Forrester | `forrester.com` | technology buyers, customer experience |
| IDC | `idc.com` | technology market sizing |
| Counterpoint | `counterpointresearch.com` | smartphones, consumer electronics |
| Canalys | `canalys.com` | devices, channels, cloud |
| Omdia | `omdia.tech.informa.com` | technology and telecom markets |
| 艾瑞咨询 | `iresearch.com.cn` | China internet and consumer reports |
| 易观分析 | `analysys.cn` | China digital market analysis |
| 前瞻产业研究院 | `qianzhan.com` | China industry overviews; verify methodology |

## Academic And Patent Research

| Source | Site / query target | Best for |
|---|---|---|
| Google Scholar | `scholar.google.com` | broad scholarly discovery |
| Semantic Scholar | `semanticscholar.org` | paper graph and citation context |
| PubMed | `pubmed.ncbi.nlm.nih.gov` | biomedical papers |
| arXiv | `arxiv.org` | preprints |
| SSRN | `ssrn.com` | social science and law preprints |
| CNKI | `cnki.net` | Chinese academic literature |
| Google Patents | `patents.google.com` | patent search |
| USPTO | `uspto.gov` | U.S. patent and trademark data |
| EPO Espacenet | `worldwide.espacenet.com` | international patents |
| WIPO Patentscope | `patentscope.wipo.int` | international patent applications |

## News And Trade Media

Use news for chronology, context, and leads. Verify major claims against primary sources.

| Source type | Examples / query target | Best for |
|---|---|---|
| Global business media | Reuters, Bloomberg, Financial Times, Wall Street Journal | events, markets, company news |
| Technology media | The Verge, TechCrunch, Wired, The Information | product and startup news |
| China business media | 财新, 36氪, 晚点, 虎嗅, 第一财经 | China market and company context |
| Trade media | industry-specific publications | niche operational details |

## Source Selection Rules

- For market size: prefer official statistics, trade associations, filings, or named analyst methodology.
- For company performance: prefer filings, audited reports, earnings transcripts, and investor presentations.
- For regulation: prefer regulator or legal text, then law firm summaries for interpretation.
- For technology capability: prefer official docs, release notes, benchmarks with methodology, and reproducible papers/code.
- For sentiment: use reviews, forums, and social media only as qualitative signals.
- For China topics: search Chinese and English. Domestic sources often cover policy and local market structure better; English sources may cover global comparables better.

## Citation Caveats

Use caveats when:

- The source is commercial and methodology is not visible.
- The report is paywalled and only snippets are visible.
- The data uses a different geography, year, or category definition.
- The page is a vendor white paper or sponsored content.
- Multiple sources appear to repeat the same original report.
