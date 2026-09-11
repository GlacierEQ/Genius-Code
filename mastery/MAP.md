# Mastery Map — Genius-Code

## Epistemic foundation

All domain work is governed by [`EPISTEMOLOGY.md`](EPISTEMOLOGY.md).

The core rule is claim-specific proof burden: semantic, functional, algorithmic, systems, performance, reliability, security, architectural, and empirical claims are not interchangeable and must be supported by evidence appropriate to the proposition.

```text
DEFINE → MODEL → IMPLEMENT → ANALYZE → CHALLENGE → MEASURE → VERIFY → OPERATE → UPDATE
```

Sources are converted through mechanisms, invariants, assumptions, tradeoffs, failure modes, falsifiable claims, verification, transfer limits, and frontier questions. Reading alone does not constitute mastery.

## Domain scope (open-ended)

### Language semantics
Memory models, type systems, ownership/borrowing, runtime behavior, interpreters/VMs, FFI, undefined behavior, concurrency semantics.

### Algorithms & data structures
Invariants, complexity, cache behavior, probabilistic / concurrent / persistent structures.

### Compilers
Parsing, IR, optimization, dataflow, codegen, JIT/AOT, correctness, sanitizer instrumentation.

### Systems programming
Process/thread models, virtual memory, filesystems, I/O, networking, synchronization, kernel/userspace.

### Databases (code view)
Storage engines, indexes, WAL, recovery, transactions, concurrency control, query planning.

### Distributed systems (code view)
Clocks/order, replication, consensus, consistency, partitions, fault models, state machines, idempotency limits.

### Verification
Property testing, fuzzing, sanitizers, static analysis, model checking, differential testing, proof where leverage justifies it.

### Performance
Profiling, CPU/memory/cache, I/O, parallelism, vectorization, benchmarking methodology, uncertainty and baseline discipline.

### Reliability & production
Retries, timeouts, backpressure, observability, deployment, rollback, capacity, reproducible builds, supply-chain provenance, crash recovery.

### Security
Threat models, cryptographic assumptions, identity, authentication, authorization, isolation, secrets, dependency trust, protocol and implementation attack surfaces.

### Software architecture
Architectural drivers, quality attributes, interfaces, dependency direction, alternatives, tactics, tradeoffs, reversibility, migration, evolution.

### Empirical software engineering
Interviews, qualitative coding, surveys, experiments, repository mining, instrumentation, statistical reasoning, validity, replication, bounded generalization.

### Doctoral research practice
Prior-art recovery, problem definition, model construction, falsifiable hypotheses, experimental design, adversarial falsification, reproducibility, peer criticism, transfer limits, research writing.

## Conversion pipeline (per important source)

```text
SOURCE → concept → mechanism/invariant → assumptions/tradeoffs/failure modes
      → falsifiable claims → implementation/reproduction
      → adversarial challenge → measurement/verification → evidence receipt
      → transfer/synthesis → teaching/retention → frontier question
```

## Standing doctoral source nucleus

The provenance registry in [`../sources/REGISTRY.yaml`](../sources/REGISTRY.yaml) is seeded with current and canonical authority surfaces spanning:

- Carnegie Mellon Software Engineering Ph.D. curriculum;
- programming-language semantics and type systems;
- program analysis and abstract interpretation;
- operating and distributed systems;
- distributed algorithms and impossibility results;
- compilers and optimization;
- database internals and recovery;
- software architecture and quality attributes;
- modern cryptography;
- advanced algorithms;
- empirical software-engineering methods.

The nucleus is deliberately not a static reading list. Each source is a feeder into claims, challenges, implementations, evidence, synthesis, teaching artifacts, and revalidation.
