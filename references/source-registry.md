# Structured Source Registry

`source-registry.json` is the machine-readable companion to `authoritative-sources.md`. Use it to select source targets by domain, geography, evidence role, access level, and format before broad discovery.

The registry is intentionally selective. It identifies stable high-value starting points, not every possible source and not a whitelist. The prose directory remains useful for wider discovery and caveats.

Query it with:

```bash
python3 scripts/query_source_registry.py --domain equity --region CN
python3 scripts/query_source_registry.py --domain healthcare --authority primary
python3 scripts/query_source_registry.py --format json --domain macro
```

Fields:

- `id`: stable registry identifier
- `name`, `domains`: source identity
- `research_domains`: research modes where the source is useful
- `regions`: geographic coverage
- `evidence_roles`: facts, filings, policy, datasets, standards, trials, and similar roles
- `authority`: primary or expert secondary
- `access`: public, registration, subscription, or mixed
- `formats`: HTML, PDF, API, XBRL, dataset, or other usable forms
- `freshness`: expected update pattern
- `query_patterns`: source-specific discovery patterns
- `limitations`: caveats that should affect use

When a source changes access policy or domain, update the registry and add a behavioral evaluation case if the change affects routing.
