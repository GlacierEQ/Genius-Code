# AGENTS.md — Genius-Code

## Buildkite execution contract

Expected pipeline: `casey-1/genius-code`.

APEX control is external: `GlacierEQ/apex-control-plane/scripts/reconcile_genius_buildkite.py` owns pipeline reconciliation and terminal family verification. This repository owns Code-domain execution only.

The Code verification job must preserve:

- contract validation;
- contract unit tests;
- Hypothesis property verification in `verification/properties/test_sort_properties.py`;
- JUnit + SHA-256 proof artifacts;
- a host-side terminal receipt bound to those artifacts.

Buildkite's base upload step owns dynamic pipeline parse/secret validation. Do not re-add a duplicate child-side upload preflight.

The Docker job may receive only the nonsecret identity variables it actually needs. Do not use `propagate-environment: true`.

Current production queue: `macos-self`. Do not route to `oracle-arm64` until that queue has live independent Buildkite proof.

A successful claim requires all of:

1. the exact GitHub head was checked out;
2. the Code verification job passed;
3. the terminal receipt was emitted with artifact digests;
4. Buildkite reported terminal PASS;
5. `buildkite/genius-code` projected success to that exact GitHub SHA.

Useful commands:

```sh
bk pipeline validate --file .buildkite/pipeline.yml
bk pipeline view casey-1/genius-code --json
bk build view --pipeline casey-1/genius-code --summary
```
