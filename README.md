# Genius-Code

[![Buildkite](https://badge.buildkite.com/963583c73f3cd364adfafef25db4d5f68e794b3d545450003e.svg)](https://buildkite.com/casey-1/genius-code)

Flagship domain repository for **code mastery**.

Identity: `Genius-Code` (hyphenated only; no colon-form dual identity).

## What this is

Not a skill pile or tutorial curriculum. An executable, continuously growing mastery system covering:

- language semantics & memory models
- algorithms & data structures
- compilers & IR
- systems programming
- databases (storage, WAL, concurrency control)
- distributed systems primitives (from the code side)
- verification (property tests, fuzzing, sanitizers)
- performance engineering
- reliability patterns
- production engineering & supply chain

## Doctrine reminder

| Aspirational | Verified |
|---|---|
| Enormous domain map | Only claims with evidence receipts |
| Frontier questions | Challenge tiers actually passed |

Scaffold ≠ mastery.

## Anatomy (required planes)

```text
mastery/          knowledge targets + vector + retention
claims/           falsifiable claims
sources/          provenance-aware registry
challenges/       foundation → frontier ladder
evidence/         ledger + receipts + counterevidence
implementations/  reference / production / competing
experiments/
benchmarks/
verification/
operations/
synthesis/
teaching/
original-work/
frontier/
interfaces/       COMPOSITION.yaml
tools/
tests/
```

## Kernel dependency

Schemas and family protocol live in [Genius-Mastery](https://github.com/GlacierEQ/Genius-Mastery).

```bash
pip install pyyaml
python tools/validate.py .
```

## Status (truthful)

| Surface | State |
|---|---|
| GENIUS.yaml v2 | Implemented |
| Domain map seed | Present |
| Claims (example set) | Mapped |
| Source registry (high-authority nucleus) | Present |
| Challenge ladder skeleton | Present |
| Evidence ledger | Empty (no executed receipts yet) |
| Implementations / benchmarks | Not yet populated |
| Buildkite CI (`casey-1/genius-code`) | Observed PASS on [build #1](https://buildkite.com/casey-1/genius-code/builds/1) @ `16e11cc4db97f3319d7843f6e75a84693a973e83` including Hypothesis property-sort |

## License

MIT — see LICENSE.
