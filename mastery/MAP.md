# Mastery Map — Genius-Code

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
Property testing, fuzzing, sanitizers, static analysis, model checking, differential testing.

### Performance
Profiling, CPU/memory/cache, I/O, parallelism, vectorization, benchmarking methodology.

### Reliability & production
Retries, timeouts, backpressure, observability, deployment, rollback, capacity, reproducible builds, supply-chain provenance.

## Conversion pipeline (per important source)

```text
SOURCE → mechanisms/invariants → falsifiable claims → implementation/reproduction
      → adversarial challenge → measurement/verification → evidence receipt
      → transfer/synthesis → frontier question
```
