# AGENTS.md — Genius-Code

## Buildkite execution

Expected Buildkite pipeline slug: `genius-code`.

When Buildkite tools are available, use Buildkite's official remote MCP server at `https://mcp.buildkite.com/mcp` and inspect live pipeline/build state before making CI claims.

Primary Buildkite evidence lanes:

- contract validation;
- contract unit tests;
- Hypothesis property-based verification in `verification/properties/test_sort_properties.py`.

Useful commands:

```sh
bk pipeline validate --file .buildkite/pipeline.yml
bk pipeline view genius-code --json
bk build view --pipeline genius-code --summary
```

For failures, inspect Buildkite jobs/logs and preserve the distinction between a committed pipeline definition and an executed build result.
