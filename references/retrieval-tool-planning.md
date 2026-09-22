# Retrieval Tool Planning

Use this reference before external research. The goal is to choose the best available retrieval tools for the user's task, not to default to generic web search and web fetch.

Default assumption: search engines and many modern sites may block, degrade, or rate-limit generic websearch/webfetch. For search-heavy tasks, prefer Agent Reach, platform-native tools, dedicated search providers, or rendered-browser tools first. Treat generic websearch/webfetch as a convenience fallback, not the default best path.

This skill is host-agnostic. Tool names differ by environment. Inspect the active tool list, plugin/MCP availability, installed CLIs, and local skills before deciding.

## Required Pre-Search Audit

Before searching, answer internally:

```text
Task target:
Information types needed:
Platforms likely to contain the answer:
Available search tools:
Available fetch/read tools:
Available rendered browser/scraping tools:
Available platform-specific tools:
Available finance/market-data tools:
Fallback path (retry chain, see Retrieval Failure Handling):
Limitations to disclose if retrieval fails:
```

If the host supports tool discovery, use it first because host-native tools and MCP servers may not have local executables. When shell access is available, run the bundled local probe as a second signal:

```bash
python3 scripts/detect_retrieval_capabilities.py
```

The probe reports installed CLIs and discoverable local skills without reading credentials or making network requests. Its `host_discovery_required` field is intentional: absence from `PATH` does not prove that an equivalent host tool is unavailable.

If the Agent Reach CLI is actually installed, `agent-reach doctor --json` can identify working channels. If only the Agent Reach skill, MCP backends, `opencli`, or `mcporter` are present, follow those interfaces instead of requiring the CLI wrapper.

## Retrieval Failure Handling: Retry Chain, Never Skip

A tool returning an error, timeout, empty body, rate-limit, or login wall is **not** permission to skip that information dimension. Silent skipping degrades the whole report and reads to the user as "covered it." Exhaust the fallback chain before treating a fact as unretrievable, then surface the gap explicitly.

This is the default behavior for every retrieval step, not an opt-in. It supersedes the convenience of moving on.

### Select The Primary Path First

There is no universal first tool. Choose the primary path from the information type:

- Broad discovery: dedicated search provider or Agent Reach search channel.
- Platform content: platform-native or Agent Reach channel.
- Known static URL, filing, document, or API: native fetch/reader or official API.
- JavaScript application: rendered browser.
- Multi-page corpus: crawler/scraper.
- Current quote or security metadata: finance/market-data tool, then exchange/issuer source.

This selection rule takes precedence over the fallback tiers below. Generic WebSearch/WebFetch is not the default search path merely because it is inexpensive.

### Failure-Cause Fallback

After the selected primary path fails, route by failure cause instead of blindly following one fixed sequence:

| Failure | Next path |
|---|---|
| Search blocked, low recall, or SEO noise | Agent Reach/Exa, Brave, Tavily, another dedicated provider, then site-specific search |
| Platform page inaccessible | Platform-native/Agent Reach channel, then rendered browser, then external discovery snippets with caveat |
| Static fetch is empty because of JavaScript | Rendered/headless browser, then full browser automation |
| Reader output is noisy | Alternate reader, structured extraction, or markitdown |
| Multi-page discovery is incomplete | Firecrawl/crawler, sitemap/API, then targeted page retrieval |
| Login wall | Existing authorized session/tool; otherwise stop and disclose rather than bypass access controls |
| Rate limit or transient timeout | Retry once with backoff or alternate provider, then switch path |
| Paywall | Original public document, issuer/regulator copy, library/public abstract, or disclose the limitation |

Within a path, escalate from the least costly sufficient tool to more interactive retrieval. A tool class that is unavailable should be recorded as unavailable, not treated as a failed evidence source.

### Retry Rules

- On failure, **do not** continue without the data and **do not** fabricate from priors.
- Re-attempt at least once with a rephrased query, a different URL, or a different tool before stepping down the chain.
- Track per dimension which tools were tried and failed, so retries are targeted — not blind repeats of the same failed call.
- Only declare a fact unretrievable after reasonable paths for that information type have been attempted, or the remaining paths are unavailable, unauthorized, or disproportionate to the task. Note which paths were unavailable, not just which failed.

### When Everything Fails

Surface the gap — never paper over it:

- Mark the claim as unverified / unknown in the evidence ledger.
- State in the final output which dimension could not be sourced and why (tool failures, logins required, paywalls, region blocks, channel unavailable).
- Offer the user a path forward: provide a source, authorize an existing session, enable a channel, or verify the item manually. Do not assume the `agent-reach` CLI exists.

## Tool Classes

| Tool class | Use for | Examples |
|---|---|---|
| Dedicated search providers | Broad discovery and source finding with better search coverage | Brave, Tavily, Exa, host-native provider tools |
| Generic web search | Convenience fallback when dedicated providers are unavailable or sufficient | host websearch, Google/Bing-like tools |
| Web fetch / reader | Static pages, docs, articles, PDFs when supported | host fetch, Jina Reader, markitdown |
| Rendered browser | JavaScript-heavy pages, search result pages, login/session pages, pages needing interaction | Lightpanda, Browserless, Playwright/Chrome, browser tools |
| Crawlers / scrapers | Multi-page sites, docs, structured extraction, sitemap-like tasks | Firecrawl, Browserless, custom scraper tools |
| Platform-specific social tools | Social posts, comments, feeds, creator content, platform search | Agent Reach channels, native APIs, platform MCPs |
| Video/podcast tools | YouTube/Bilibili/Douyin/Xiaoyuzhou transcripts and metadata | yt-dlp, Agent Reach, transcript tools |
| Finance/market-data tools | Quotes, indices, ETFs, securities, crypto, financial market snapshots | host finance tools, Xueqiu, exchange/issuer data |
| Code/repo tools | GitHub repositories, issues, commits, releases | GitHub CLI/API/MCP, code search |
| RSS/feed tools | Monitoring, news feeds, repeated sources | feedparser, RSS readers |

## Dynamic Routing

Choose retrieval by information type.

| User need | Preferred retrieval path | Fallback |
|---|---|---|
| Official facts, docs, laws, filings | Official site search + fetch; regulator/filing database | Generic search with `site:` queries |
| Broad web research | Agent Reach Exa, Brave, Tavily, or other dedicated providers; fetch top sources | Host search only, then query expansion |
| JavaScript-heavy pages | Rendered browser / Browserless / Playwright | Jina Reader, markitdown, cached snippets |
| Search engine result pages blocked by default tools | Agent Reach search/Exa, Brave/Tavily, Lightpanda/rendered browser | Host search with caveat, site-specific queries |
| Multi-page crawl | Firecrawl or crawler service | Search specific pages and fetch manually |
| XiaoHongShu / RED | Agent Reach XiaoHongShu channel | Search engine snippets, user-provided links |
| Douyin / short video | Agent Reach Douyin parser or video tool | Search web for mirrored summaries |
| WeChat articles | Agent Reach WeChat reader / Camoufox path | Search title/author externally; snippets only with caveat |
| Weibo | Agent Reach Weibo channel | Search engine `site:weibo.com` |
| X/Twitter | Agent Reach bird channel or platform tool | Search snippets, official reposts |
| Reddit / forums | Reddit API/search or Agent Reach; V2EX API for V2EX | Exa/web search with `site:` |
| YouTube / Bilibili | yt-dlp metadata/subtitles or Agent Reach | Page fetch, search summaries |
| Podcasts | Xiaoyuzhou/Whisper/transcript tools | Episode notes only |
| GitHub | GitHub API/CLI/MCP | Web search + repo fetch |
| Stock/security quotes | Finance tool or Xueqiu quote channel | Exchange/company IR, market-data pages |
| China market sentiment | Xueqiu, Weibo, XiaoHongShu, WeChat, V2EX depending topic | Chinese search + site-specific queries |

## Agent Reach Routing

If Agent Reach is installed/available, prefer it for platform-native retrieval across:

- X/Twitter: search, user timeline, threads, articles
- Reddit: search and community posts
- YouTube and Bilibili: metadata and subtitles
- GitHub: repository, issues, code search via `gh`
- XiaoHongShu: feed search, feed detail, comments when logged in
- Douyin: shared video metadata and download link
- Weibo: trends, users, feeds, content search, comments
- WeChat Articles: search and Camoufox reader for official-account articles
- Xiaoyuzhou: podcast transcription
- LinkedIn: people/profile search when available
- V2EX: public API topics, replies, users
- Xueqiu: quotes, stock search, hot posts, hot stocks
- RSS: feed parsing
- Exa: web search and code context

Run `agent-reach doctor` when a platform channel may be needed and status is uncertain. Some channels need cookies, proxy, ffmpeg, API keys, or browser support. If unavailable, use the fallback path and disclose limitations.

## Search Provider Strategy

When multiple search providers are available:

- Use Agent Reach search/Exa, Brave, or Tavily before generic websearch when search-engine blocking is likely.
- Use Brave or a strong host-native provider for general current web coverage.
- Use Tavily for research-oriented web snippets and topical discovery when available.
- Use Exa for semantic search, technical/code context, and finding high-signal pages.
- Use Lightpanda or another rendered-browser tool when search/result pages or target pages require JavaScript or block static fetch.
- Use site-specific queries for authoritative sources.
- Use more than one provider when the topic is controversial, fast-moving, SEO-polluted, or platform-specific.

Do not treat provider count as source count. Multiple search engines returning the same article is one evidence source.

## Scraping And Rendered-Page Strategy

Use rendered/crawler tools when:

- The page depends on JavaScript.
- Native fetch returns empty/noisy content.
- You need comments, pagination, product listings, tables, or multiple pages.
- You need a structured crawl of docs or a website section.

Preferred order:

1. Native fetch/reader for simple pages.
2. Lightpanda, rendered browser, or Browserless for dynamic pages and blocked search/result pages.
3. Firecrawl/crawler for multi-page extraction if available.
4. markitdown for local files, PDFs, Office docs, or noisy HTML fallback.
5. Manual extraction with caveats if no tool works.

## Social And Community Evidence Rules

Social platforms are useful for sentiment, adoption signals, emerging complaints, creator/customer language, and real-world use cases. They are usually weak evidence for hard facts.

Use them as:

- Leads for official verification
- Qualitative sentiment
- Examples of user pain
- Early-warning signals
- Distribution/channel insight

Do not use them as sole proof for:

- Market size
- Product capability
- Legal/regulatory status
- Financial performance
- Medical/safety claims

## Finance And Securities Tool Rules

For stocks, securities, ETFs, bonds, indices, and crypto:

- Use current finance/market tools when available.
- Verify issuer facts with filings, exchange disclosures, and investor relations.
- Use Xueqiu/finance portals as market snapshot or sentiment tools, not as final authority for filings.
- Timestamp all market-sensitive data.
- Separate price/market data from investment judgment.

## Retrieval Plan Output

For Pro/Ultra or audit-heavy tasks, include a compact retrieval plan:

```markdown
## Retrieval Plan

| Need | Tool / source path | Reason | Fallback |
|---|---|---|---|
| Official facts | SEC/company IR fetch | primary source | web search site query |
| Market data | finance tool | current quote | exchange page |
| Social sentiment | Agent Reach Xueqiu/Weibo | platform-native posts | search snippets with caveat |
```

For normal tasks, keep this internal and only mention material limitations.

## Common Mistakes

- Treating a tool failure (error, timeout, empty result, rate-limit, login wall) as a reason to skip a dimension instead of stepping through the retry chain. See Retrieval Failure Handling above.
- Using generic websearch/webfetch as the first choice for search tasks when Agent Reach, Brave, Tavily, Exa, Lightpanda, or another better retrieval path exists.
- Using web search when a platform-native tool exists.
- Treating social content as authoritative fact.
- Reading WeChat/Douyin/XiaoHongShu through generic fetch when a specialized channel is available.
- Using stale market data for securities.
- Crawling a site manually when Firecrawl/Browserless/browser tooling is available.
- Failing to disclose that a platform channel required login or was unavailable.
