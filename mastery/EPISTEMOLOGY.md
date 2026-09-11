# Genius-Code Epistemology

## Purpose

Genius-Code treats software development as an evidence-producing engineering discipline, not as code generation. The target is not merely code that appears plausible or passes a happy-path test. The target is justified confidence about what a system means, what it does, why it does it, under which assumptions, how it fails, and which evidence would falsify the current belief.

This epistemology is distilled from doctoral software-engineering and computer-science foundations: programming-language semantics and type systems, program analysis, formal verification, algorithms, operating systems, distributed systems, databases, compilers, software architecture, security, testing, empirical software engineering, and research methodology.

## Prime law

> A software claim is only as strong as the evidence appropriate to that class of claim.

Different claims demand different proof burdens. A unit test cannot prove a distributed-systems liveness property. A benchmark cannot establish semantic correctness. A type checker cannot establish production availability. A successful deployment cannot prove the absence of exploitable attack paths. A peer-reviewed paper does not automatically establish that a result transfers to a different workload, architecture, organization, or threat model.

The engineering discipline is therefore:

```text
DEFINE → MODEL → IMPLEMENT → ANALYZE → CHALLENGE → MEASURE → VERIFY → OPERATE → UPDATE
```

Each transition must preserve assumptions, provenance, counterevidence, and the distinction between observation and inference.

## 1. Objects of knowledge

Every important software-development assertion should be classified before it is accepted.

### Semantic claims
Claims about what a program or language construct means.

Examples: evaluation order, aliasing behavior, ownership, lifetime, effects, memory ordering, undefined behavior, type soundness.

Preferred evidence: language specification, operational/denotational semantics, typing derivation, mechanized proof, compiler/runtime conformance tests.

### Functional-correctness claims
Claims that an implementation satisfies a specification or invariant.

Preferred evidence: executable specification, proofs, model checking, static analysis, property tests, differential tests, targeted unit/integration tests, counterexample search.

### Algorithmic claims
Claims about asymptotic complexity, approximation quality, termination, optimality, or probabilistic behavior.

Preferred evidence: mathematical proof plus adversarial examples and implementation measurement where machine effects matter.

### Systems claims
Claims involving scheduling, concurrency, storage, networking, resource management, failure, replication, or recovery.

Preferred evidence: explicit fault model, state-machine reasoning, concurrency stress, crash/restart testing, network fault injection, persistence/recovery tests, workload measurement, production traces.

### Performance claims
Claims about latency, throughput, memory, CPU, I/O, scaling, or efficiency.

Preferred evidence: reproducible benchmark design, distributions rather than averages alone, controlled baselines, workload definition, hardware/software versioning, statistical uncertainty, profiling, regression history.

### Reliability claims
Claims about behavior under faults and over time.

Preferred evidence: fault injection, chaos experiments where appropriate, recovery receipts, bounded retry/backoff behavior, durability tests, observability, SLO/error-budget history.

### Security claims
Claims about confidentiality, integrity, authentication, authorization, isolation, protocol safety, or resistance to an adversary.

Preferred evidence: explicit threat model, cryptographic assumptions, attack-surface enumeration, secure design review, static/dynamic analysis, dependency provenance, adversarial testing, independent review.

### Architecture and evolvability claims
Claims about modularity, change cost, deployability, portability, operability, or quality attributes.

Preferred evidence: explicit architectural drivers, interfaces and dependency constraints, alternatives considered, quality-attribute scenarios, change simulations, operational history, architecture decision records.

### Human and empirical claims
Claims about developer behavior, usability, productivity, organizational effects, or observed software-engineering practice.

Preferred evidence: appropriate qualitative/quantitative research design, sampling rationale, measurement validity, statistical analysis when applicable, replication, threats-to-validity analysis, and bounded generalization.

## 2. The software evidence stack

Confidence should rise through independent evidence modes rather than repeated versions of the same test.

1. **Definition** — terms, requirements, interfaces, invariants, threat/fault model, success criteria.
2. **Formal model** — semantics, state machines, types, logical properties, complexity model.
3. **Implementation structure** — code, data structures, dependencies, build graph, generated artifacts.
4. **Static evidence** — type checking, linting, abstract interpretation, dataflow/alias analysis, proof obligations, dependency analysis.
5. **Dynamic evidence** — examples, unit tests, integration tests, property testing, fuzzing, differential testing, sanitizers.
6. **Systems evidence** — concurrency, crash consistency, partial failure, distributed coordination, persistence, load, resource exhaustion.
7. **Operational evidence** — deployment receipts, telemetry, SLOs, incident behavior, rollback/recovery, supply-chain provenance.
8. **Research evidence** — comparison to prior art, experimental design, counterhypotheses, replication, peer criticism, transfer limits.

No higher layer retroactively erases a contradiction found below it. Contradictions are retained until resolved.

## 3. Source authority

Use the strongest available source for the proposition being evaluated.

```text
formal specification / standard / primary implementation contract
    ↓
original research paper / authoritative textbook / official graduate course
    ↓
maintainer documentation / verified source code / reproducible experiment
    ↓
high-quality secondary synthesis
    ↓
community explanation / anecdote
```

Authority is proposition-specific. Source code can be authoritative for current implementation behavior while a language standard is authoritative for required behavior. A benchmark result is authoritative only for its declared setup. A doctoral syllabus is authoritative for what the course teaches, not automatically for every claim made by every reading.

## 4. Mechanisms before slogans

Knowledge must be compressed into mechanisms, invariants, tradeoffs, and failure modes.

Bad compression:

> “Raft is reliable.”

Useful compression:

> “Raft achieves replicated state-machine consensus under its stated timing and failure assumptions by using leader election, term monotonicity, majority intersection, log matching, and commit rules; safety and availability must be reasoned about separately.”

Bad compression:

> “Rust is memory safe.”

Useful compression:

> “Rust’s ownership, borrowing, lifetimes, and type system prevent broad classes of memory errors in safe Rust; `unsafe`, FFI, implementation defects, logic errors, and concurrency/protocol mistakes remain separate proof obligations.”

For each source, extract:

```text
CONCEPT → MECHANISM → INVARIANT → ASSUMPTIONS → TRADEOFF → FAILURE MODE
        → FALSIFIABLE CLAIM → TEST/PROOF → TRANSFER LIMIT → FRONTIER QUESTION
```

## 5. Correctness is multidimensional

“Works” is not a single state.

A system may be:

- semantically valid but too slow;
- fast but incorrect under concurrency;
- functionally correct but unrecoverable after a crash;
- locally correct but unsafe under distributed partitions;
- available but insecure;
- secure in isolation but vulnerable through dependencies;
- well tested but inconsistent with its specification;
- proven under a model whose assumptions production violates.

Genius-Code therefore never collapses semantic correctness, functional correctness, reliability, security, performance, and operability into one undifferentiated PASS.

## 6. Testing and proof are complementary

Testing searches executions. Proof reasons over a model. Static analysis computes conservative information. Model checking explores a finite abstraction or state space. Fuzzing generates adversarial inputs. Production telemetry observes the deployed system.

Each has blind spots.

The strongest systems combine them according to risk:

```text
examples
  + properties
  + generated/adversarial inputs
  + static reasoning
  + formal reasoning where leverage justifies it
  + fault/load experiments
  + operational readback
```

The objective is not maximal ceremony. It is maximal reduction of consequential uncertainty per unit cost.

## 7. Distributed and concurrent systems require explicit models

Never reason about a distributed system as if calls happen sequentially and machines fail cleanly.

State explicitly:

- synchrony/asynchrony assumptions;
- crash, omission, Byzantine, corruption, and partition models;
- ordering and clock assumptions;
- consistency model;
- durability boundary;
- retry/idempotency semantics;
- quorum/intersection requirements;
- membership/change protocol;
- recovery and replay behavior.

For concurrency, identify shared state, happens-before relationships, atomicity boundaries, linearization points where applicable, lock ordering, memory model, starvation/deadlock risks, and cancellation behavior.

## 8. Databases are executable consistency machinery

Treat a database as more than persistence APIs. Reason about:

- logical model and invariants;
- physical layout and indexes;
- transaction boundaries;
- isolation level and anomalies;
- concurrency control;
- write-ahead logging and recovery;
- query planning and statistics;
- replication and failover;
- backup restore proof;
- schema evolution.

A successful write response is not proof of durable recoverability. A backup file is not proof of restoration. A transaction is not automatically serializable.

## 9. Compilers and languages define the executable meaning boundary

Compiler reasoning connects source-level intent to machine behavior. Preserve distinctions among:

- syntax;
- static semantics;
- dynamic semantics;
- intermediate representations;
- optimization legality;
- code generation;
- runtime/ABI contracts;
- memory model;
- undefined or implementation-defined behavior.

Optimization is correct only when observable semantics permitted by the language are preserved under the relevant assumptions.

## 10. Architecture is constrained tradeoff reasoning

Architecture is not diagram production. It is the disciplined allocation of responsibilities and constraints to achieve quality attributes under cost and organizational limits.

Every architectural decision should expose:

```text
DRIVER → OPTIONS → DECISION → MECHANISM → QUALITY ATTRIBUTE
       → COST → RISK → EVIDENCE → REVERSIBILITY → REVISIT TRIGGER
```

Prefer explicit interfaces, dependency direction, failure containment, observability, replaceability, and migration paths over fashionable topology.

## 11. Security begins with an adversary

Before saying “secure,” define what is protected, from whom, with which trust anchors and assumptions.

Keep separate:

- cryptographic primitive security;
- protocol security;
- implementation security;
- identity/authentication;
- authorization;
- secret handling;
- dependency/supply-chain trust;
- runtime isolation;
- operational access and recovery.

Security claims without a threat model are incomplete.

## 12. Empirical software engineering is science about software practice

When the proposition concerns people, teams, repositories, productivity, defects, adoption, or organizational behavior, engineering intuition alone is insufficient.

Require:

- operationalized variables;
- representative sampling or explicit sampling limits;
- valid instrumentation;
- qualitative coding discipline where applicable;
- statistical assumptions where applicable;
- confound analysis;
- replication where feasible;
- explicit threats to construct, internal, external, and conclusion validity.

Correlation discovered in repository data is not automatically causation.

## 13. Doctoral research posture

A doctoral-level software engineer should be able to:

1. recover the strongest prior art;
2. define the problem precisely;
3. identify assumptions and existing limits;
4. construct a model or mechanism;
5. derive falsifiable claims;
6. build the artifact or experiment;
7. attack the favored hypothesis;
8. measure against credible baselines;
9. preserve counterevidence;
10. state exactly what the evidence does and does not establish;
11. produce a reproducible result;
12. update the model after failure.

Novelty without verification is speculation. Verification without relevance is sterile. Engineering quality requires both explanatory depth and operational consequence.

## 14. Foundational corpus

The standing corpus is seeded from authoritative doctoral/graduate sources including:

- Carnegie Mellon Software Engineering Ph.D. curriculum and Software Engineering Research framing;
- Robert Harper, *Practical Foundations for Programming Languages*;
- CMU 15-814 Types and Programming Languages;
- CMU 17-819 Program Analysis;
- MIT 6.852J Distributed Algorithms / Nancy Lynch, *Distributed Algorithms*;
- MIT 6.5840 Distributed Systems;
- CMU 15-712 Advanced and Distributed Operating Systems;
- *Operating Systems: Three Easy Pieces*;
- CMU 15-745 Optimizing Compilers;
- CMU 15-445/645 Database Systems;
- CMU/SEI *Software Architecture in Practice*;
- Stanford CS255 cryptography with Katz–Lindell and Boneh–Shoup;
- MIT 6.854J Advanced Algorithms reference corpus;
- CMU 17-803 Empirical Methods.

The source registry records the retrievable authority surfaces. Textbooks and papers should be converted into claims and mechanisms only when the actual source has been retrieved or an authoritative course/publisher description supports the narrower statement.

## 15. Genius-Code conversion contract

Every substantial source should eventually produce durable state in more than one plane:

```text
source registry
  → mastery concept
  → falsifiable claim
  → challenge
  → implementation or reproduction
  → verification evidence
  → synthesis
  → teaching artifact
  → retention/revalidation schedule
  → frontier question
```

Reading is acquisition. Mastery begins when the knowledge can survive implementation, adversarial testing, explanation, transfer to a new context, and later revalidation.

## Final rule

> Do not ask whether code looks intelligent. Ask what proposition it makes about reality, what mechanism makes that proposition true, what evidence supports it, what observation would disprove it, and whether the result survives contact with the runtime in which it must operate.
