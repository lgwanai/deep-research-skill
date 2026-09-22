# Research Depth And Follow-Up

Use this reference for Standard, Pro, and Ultra work when the first search results are not enough to support the user's decision. The goal is not to run more searches mechanically. The goal is to keep asking the next evidence-driven question until each decision-critical branch is resolved, bounded, or explicitly left open.

## Why Research Stops Too Early

Shallow research usually has one of these patterns:

- The agent finds several relevant pages and mistakes topical relevance for an answer.
- Query expansion repeats synonyms but does not investigate the missing evidence.
- A secondary article is cited without following its source.
- A number is collected without its definition, method, period, or denominator.
- Conflicting sources are listed but not investigated.
- The emerging conclusion is supported repeatedly while contrary evidence is never sought.
- The agent summarizes before checking whether every decision-critical question is actually answerable.

## Build A Question Tree

Translate the task into a small tree before deep retrieval:

```text
Decision or deliverable
├── Critical question A
│   ├── Fact or metric required
│   ├── Preferred original source
│   └── What could change the answer
├── Critical question B
│   ├── Fact or metric required
│   ├── Preferred original source
│   └── What could change the answer
└── Critical question C
    ├── Fact or metric required
    ├── Preferred original source
    └── What could change the answer
```

Keep the tree proportional. A Standard task may need three to five branches. Pro and Ultra tasks may need sub-branches by entity, period, geography, or competing explanation.

## Maintain A Research Queue

After each retrieval round, update a compact internal queue:

```markdown
| Branch | Current answer | Best evidence | Unresolved reason | Next action | Status |
|---|---|---|---|---|---|
| A | ... | ... | Original dataset not found | Trace citation upstream | open |
| B | ... | ... | Two definitions differ | Find methodologies | conflicting |
| C | ... | ... | One company claim only | Seek independent evidence | partial |
```

Statuses:

- **Open**: no usable answer yet
- **Partial**: some evidence, but a required field or angle is missing
- **Conflicting**: credible evidence disagrees
- **Resolved**: sufficient evidence supports a bounded answer
- **Missing**: reasonable retrieval paths were exhausted and the gap is documented
- **Blocked**: access, paywall, unavailable data, or tool limits prevent verification

The next query must come from the unresolved reason, not from a generic request for "more information."

## Adaptive Follow-Up Triggers

| Retrieval result | Required follow-up |
|---|---|
| Secondary article cites a report | Locate and read the original report |
| Report cites a dataset | Find the dataset, table, or methodology page |
| Number has no scope or denominator | Search the metric definition and calculation method |
| Two values differ | Search both sources' periods, geography, versions, and methods |
| Company or vendor makes a favorable claim | Seek filing, customer, regulator, benchmark, or independent evidence |
| Source says "studies show" | Identify the named study and inspect its design |
| Policy summary describes a rule | Open the official text and check effective date, scope, and later amendments |
| A conclusion depends on causality | Search for alternative explanations and temporal evidence |
| Only supporting evidence appears | Run an explicit criticism, failure, limitation, or bear-case search |
| Evidence is old | Search for later updates, revisions, or superseding publications |
| Search results repeat each other | Trace the common origin or switch source/tool/query structure |
| A branch has many sources but no answer | Restate the exact missing fact and search by source type or field |

## Multi-Hop Source Tracing

Follow important claims through their source chain:

```text
Search result or media article
→ cited report, filing, announcement, paper, or dataset
→ exact table, passage, chart, or record
→ methodology, definitions, sample, and calculation notes
→ later correction, revision, amendment, or update
```

Do not stop at every hop. Continue when the claim is decision-critical and the current hop does not expose enough detail to validate it. Record a gap when the chain ends behind an inaccessible source or missing methodology.

## Five Deepening Passes

Use only the passes needed by the task, but do not skip a pass that can materially change the conclusion.

### 1. Foundation Pass

Establish official facts, identities, dates, definitions, and the main source landscape.

### 2. Source-Chain Pass

Trace important claims and numbers to their original documents, data, or methods.

### 3. Gap And Conflict Pass

Target missing fields, weak branches, scope mismatches, and contradictory evidence.

### 4. Challenge Pass

Try to disprove or weaken the emerging conclusion. Search for limitations, failed cases, alternative explanations, contrary data, and stakeholder incentives.

### 5. Freshness And Change Pass

Check whether later events, revisions, new filings, policy changes, or corrected data alter the answer.

## Query Construction From Evidence

Generate precise follow-ups from what was found:

```text
<named report> methodology
<dataset name> definition <metric>
<issuer> filing <period> <segment>
<claim phrase> original source
<metric A> vs <metric B> definition
<event> alternative explanation
<topic> limitation OR failure OR criticism
<document title> revision OR amendment OR correction
```

Prefer entity names, document titles, table names, authors, dataset names, policy numbers, metric names, and dates extracted from retrieved evidence. These are stronger anchors than broad topical synonyms.

## Depth By Mode

### Standard

- Build a compact question tree.
- Complete an initial search and at least one evidence-driven follow-up round for partial or conflicting critical branches.
- Trace material secondary claims to an original source when available.
- Run a compact counter-evidence check.

### Pro

- Maintain the research queue throughout the task.
- Follow decision-critical source chains to original evidence and methodology.
- Run gap, conflict, challenge, and freshness passes where relevant.
- Do not finalize while a critical branch remains open; classify it as resolved, partial, conflicting, missing, or blocked.
- Include a compact research log when auditability matters.

### Ultra

- Decompose the task into independent workstreams by entity, dimension, geography, period, or competing hypothesis. Give each workstream its own research contract, question tree, queue, evidence ledger, and closure status.
- Run workstreams in parallel where tools allow, but never merge their evidence trails prematurely.
- Build both a source graph and a claim graph. The source graph shows where evidence originated and how derivative sources connect; the claim graph shows which evidence supports, weakens, or conflicts with each conclusion.
- Run all relevant deepening passes inside each critical workstream: foundation, source-chain, gap/conflict, challenge, and freshness.
- After every batch, run a convergence review. Compare workstreams, identify shared assumptions, detect inconsistent definitions or dates, and create new follow-up branches for cross-workstream dependencies.
- Reallocate retrieval budget toward unresolved branches with the greatest potential to change the conclusion. Do not continue spending evenly on already-saturated branches.
- Assign an adversarial review pass that starts from the opposite conclusion, searches for disconfirming evidence, and checks whether an important stakeholder, geography, period, or failure mode was omitted.
- Use cross-workstream adjudication when two branches rely on different versions, definitions, samples, currencies, or causal explanations. Preserve both positions until normalization or stronger evidence resolves them.
- Do not close the overall task while any decision-critical workstream remains open. Convert it to resolved, partial, conflicting, missing, or blocked, and explain the effect on the final conclusion.
- Preserve a reproducibility package containing exact queries, retrieval tools/routes, fetched pages, rejected sources with reasons, source-chain paths, workstream status changes, calculations, and unresolved items.

## Ultra Execution Loop

Use this loop for broad or high-stakes research:

```text
1. Frame the decision and define the research boundary
2. Decompose into independent workstreams and competing hypotheses
3. Run parallel foundation searches
4. Build source and claim graphs
5. Deepen each workstream through source-chain and gap-driven follow-ups
6. Converge findings and generate cross-workstream questions
7. Reallocate budget to the branches most likely to change the answer
8. Run contradiction resolution and independent adversarial review
9. Validate claims, fields, and calculations
10. Check entity-by-dimension coverage
11. Close or explicitly classify every critical branch
12. Produce the final synthesis and reproducibility package
```

## Ultra Convergence Review

At each convergence point, answer:

- Which workstreams changed the emerging conclusion?
- Which conclusions depend on evidence shared by multiple workstreams rather than independent evidence?
- Do different workstreams use the same entity, time period, version, metric definition, geography, unit, and denominator?
- Has a local finding been incorrectly generalized to another market, segment, or period?
- What evidence would most likely reverse the current conclusion?
- Which unresolved branch now deserves more retrieval budget?

## Ultra Coverage Matrix

Use an entity-by-dimension matrix to prevent a large report from appearing complete while leaving specific entities or dimensions unresearched:

```markdown
| Entity / workstream | Official facts | Metrics | Independent evidence | Risks/counter-evidence | Freshness | Status |
|---|---|---|---|---|---|---|
| A | covered | covered | partial | covered | covered | partial |
| B | covered | missing | covered | partial | covered | missing |
```

The number of sources does not determine coverage. A cell is covered only when the evidence is adequate for the question and has passed the relevant validation checks.

## Ultra Stopping Rule

Ultra research may stop only when:

- Every decision-critical workstream has a non-open status.
- Source and claim graphs no longer reveal an untraced critical dependency.
- Cross-workstream conflicts are resolved, bounded, or explicitly left unresolved.
- The adversarial pass produces no new evidence likely to reverse the conclusion, or its evidence has been incorporated.
- Additional retrieval has reached an information-gain plateau across the remaining branches.
- The final confidence reflects partial, conflicting, missing, and blocked branches rather than averaging them away.

## Information Gain And Stopping

Measure progress by decision impact, not source count. A retrieval round adds value when it provides at least one of:

- A new decision-relevant fact
- An original source replacing a derivative source
- A missing definition, scope, period, version, unit, or methodology
- Independent confirmation
- A credible contradiction or alternative explanation
- Resolution of a conflict or gap
- Evidence that changes confidence or the recommendation

Stop a branch when:

- The bounded question is answered with adequate evidence and validation.
- Additional searches return only duplicates or restatements and no unresolved critical field remains.
- The remaining gap is inaccessible or unavailable after the fallback chain, and the limitation is documented.
- New evidence is unlikely to change the decision, wording, or confidence.

Do not stop merely because two searches returned no new facts if the branch still lacks its original source, methodology, counter-evidence, or conflict resolution. Change the retrieval path first.

## Delivery

Keep most of the queue internal. For Pro/Ultra or audit-sensitive work, summarize:

- Which critical branches were resolved
- Which remain partial, conflicting, missing, or blocked
- Which source chains reached original evidence
- Which conclusion changed after the challenge pass
- Why further searching was stopped
