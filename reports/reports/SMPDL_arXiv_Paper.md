# A Three-Layer Dependency-and-Logic Audit for Mathematical Proofs and AI-Generated Claims: The S/M/P × D/L Framework

**Authors:** CAMPANASILVAE · fecit · MMXXVI  
**Affiliation:** Göttingen Mathematical History Index Project  
**Date:** 2026-10-12 GMT+8  
**Version:** v3  
**License:** CC BY-NC-SA 4.0  
**Content Fingerprint (SHA-256 of report corpus, 46 files):** `79b7481f2a3cd3ad3119f8b09788fdf02b31e345e4b139aa2ad142e7b2bff107`

---

## Abstract

We introduce a structured audit framework for mathematical proofs, conjectures, and AI-generated mathematical claims. The framework operates on three layers — **S**emantic, **M**athematical, and **P**rogramming — and for each layer examines two complementary dimensions: internal **D**ependency relations and internal **L**ogic-structure discipline. The resulting S/M/P × D/L matrix provides six elementary audit cells (S*D, S*L, M*D, M*L, P*D, P*L) plus cross-layer mapping checks. We demonstrate the framework on a corpus of nineteen audited cases spanning correct proofs (Euclid's infinitude of primes, Cantor's diagonal argument, Wilson's theorem, the Basel problem, and others), classical fallacies (the all-triangles-are-isosceles proof, Kempe's four-color "proof"), disproved conjectures (Fermat's prime conjecture, Euler's sum-of-powers conjecture), a research-level computer-assisted proof (Appel–Haken), open diagnostics (the Riemann Hypothesis, the Andrews–Curtis conjecture), and a 2026 AI-formalization incident in which a Lean-verified Navier–Stokes blow-up claim failed at the semantic-translation layer despite passing the programming layer. We show that the same layered discipline inverts into a **machine-assisted, anti-foresight proof-construction protocol**, and we report a worked construction attempt on the Andrews–Curtis conjecture in which all five natural proof routes are blocked at explicitly located gaps. Finally, motivated by the case corpus, we define the **human-machine division of labor** for proof construction and audit: five precisely specified roles — concept singularity, semantic-fidelity review, gap characterization, trap foresight, and verification interpretation — that remain human-indispensable, including a seven-type trap-foresight taxonomy with an executable checklist (TRAP-CHECK v1.0). The aim is not automated verification but a disciplined, teachable, and increasingly mechanizable way to locate where a proof's structure breaks, where an open problem's gap lies, and where human judgment cannot be delegated.

**Keywords:** mathematical proof audit, AI-generated proof verification, anti-foresight proof construction, machine-assisted proving, human-machine division of labor, autoformalisation fidelity, proof fallacies, disproved conjectures, Andrews–Curtis conjecture, Navier–Stokes, Riemann Hypothesis, four-color theorem, Lean.

---

## 1. Introduction

### 1.1 Motivation

Large language models can now produce texts that look like mathematical proofs. Distinguishing valid proofs from plausible-looking but flawed ones is increasingly difficult, especially when the flaw is not a gross arithmetic error but a subtle structural gap: an unstated geometric betweenness condition, an illegal generalization from one operation to two simultaneous operations, a silent shift from finite verification to a universal claim — or, as a 2026 incident made vivid, a formally verified theorem statement that no longer says what the original natural-language proof claimed.

Existing approaches include:

- **Human expert review**: high quality but not scalable;
- **Automated theorem provers (Lean, Coq)**: strong when a proof is already formal, but many AI-generated proofs are not immediately formalizable, and formal verification certifies only the formal object, not its fidelity to the natural-language claim;
- **Peer-review-style red-flag lists**: useful but often ad hoc.

What is missing is a lightweight, layered audit methodology that can be applied *before* full formalization and that tells the reviewer not just *whether* a proof fails but *at which layer* and *in which dimension* it fails — together with an explicit account of which audit and construction tasks remain irreducibly human.

### 1.2 The S/M/P intuition

We decompose any mathematical text into three layers:

| Layer | Scope | Typical objects |
|---|---|---|
| **S** — Semantic / linguistic | Natural-language formulation | Terms, quantifiers, metaphors, narrative structure |
| **M** — Mathematical | Strict mathematical content | Definitions, theorems, proofs, structures |
| **P** — Programming / formal | Executable or formalizable code | Algorithms, theorem-prover scripts, invariants |

A proof may be well-formed at one layer but defective at another. A metaphor may be vivid at S but lack an M counterpart; an algorithm may run at P but not correspond to the intended M object. The framework forbids *cross-layer upgrade*: a S-layer correspondence does not automatically become an M-layer correspondence, and a P-layer success does not automatically certify the M-layer claim.

### 1.3 The D/L distinction

Within each layer, we distinguish two audit dimensions:

| Dimension | Question | Analogy |
|---|---|---|
| **D** — Dependency | Which elements support which others? Is the support graph closed? | The skeleton of a building |
| **L** — Logic structure | Are the support relations themselves logically legitimate? | The strength and code compliance of beams and joints |

A proof can have a closed dependency graph (D passes) while its logical structure is broken (L fails). Kempe's flawed four-color proof is the canonical example: step 5 depends on step 4, but the dependence is illegitimate because it assumes the independence of two Kempe-chain swaps.

---

## 2. The S/M/P × D/L Framework

### 2.1 Naming convention

| Letter | Meaning | Scope |
|---|---|---|
| S | Semantic | Natural language, terms, metaphors, quantifiers |
| M | Mathematical | Mathematical objects, theorems, proof structures |
| P | Programming | Formal languages, code, algorithms, executables |
| D | Dependency | Intra-layer support, implication, call relations |
| L | Logic Structure | Quantifier discipline, assumption management, inference-rule legality, boundary cases, meta-logical hygiene |

### 2.2 The 3 × 2 audit matrix

| | D: Dependency | L: Logic Structure |
|---|---|---|
| **S** | S*D: Which sentences/terms support which others? | S*L: Are quantifiers explicit? Are metaphors translated? Are "obvious" steps justified? |
| **M** | M*D: Which definitions/theorems/lemmas depend on which? | M*L: Are inferences valid? Are hidden assumptions stated? Are boundary cases covered? |
| **P** | P*D: Which functions/modules/theorems call which? | P*L: Are formal inference rules valid? Are assumptions introduced/discharge correctly? Does it compile? Are there `sorry`s? |

### 2.3 Cross-layer mapping

After the six intra-layer audits, we check whether D-relations and L-relations are preserved when translating S → M → P:

```
S*D --translation--> M*D --formalization--> P*D
 |                    |                    |
S*L --translation--> M*L --formalization--> P*L
```

A failure here indicates a *translation gap* or *formalization gap*, not necessarily a mathematical error.

### 2.4 Verdict taxonomy

| Situation | Verdict | Meaning |
|---|---|---|
| All six cells pass and cross-layer maps hold | Full pass | Structurally sound across layers |
| One or more L cells fail, D passes | Logic-structure failure | Dependencies exist but are illegitimate |
| One or more D cells fail, L passes | Dependency break | Elements are isolated or circular |
| Cross-layer map fails | Isomorphism break | Translation/formalization gap |
| P passes but S→P translation fails | Translation-fidelity failure | The verified formal object is not the claimed theorem |
| Any cell fails | Proof not admitted | Requires repair and re-audit |

---

## 3. Case Studies

### 3.1 Euclid's proof of the infinitude of primes

**Proof sketch.** Assume finitely many primes p₁,…,pₙ. Let N = p₁⋯pₙ + 1. Then N is not divisible by any pᵢ, so N has a prime factor outside the list — contradiction.

| Cell | Result | Comment |
|---|---|---|
| S*D | ✅ | Closed dependency chain |
| S*L | ✅ | Quantifiers explicit; proof by contradiction valid |
| M*D | ✅ | Depends on divisibility, Euclidean lemma, prime factorization |
| M*L | ✅ | Contradiction structure complete; existence reasoning valid |
| P*D | ⚠️ | Trivial implementation dependencies |
| P*L | ✅ | Formalizable in Peano arithmetic / Lean `mathlib` |
| Cross-layer | ✅ | S, M, P align |

**Lesson.** A paradigmatic pass; the only mild concern is making the prime-factor existence lemma explicit.

### 3.2 The all-triangles-are-isosceles fallacy

**Proof sketch.** In triangle ABC, let P be the intersection of the perpendicular bisector of AB and the angle bisector of ∠C. Then PA = PB and the perpendicular distances PU = PV. By RHS, triangles PUA and PVB are congruent, so AU = BV; triangles PUC and PVC are congruent, so CU = CV. Hence AC = AU + CU = BV + CV = BC.

| Cell | Result | Comment |
|---|---|---|
| S*D | ⚠️ | Chain looks closed, but hides an unstated geometric condition |
| S*L | ❌ | "AU + CU" requires U to lie *on segment* AC; not stated |
| M*D | ⚠️ | Depends on congruence, but the length-addition step is unsupported |
| M*L | ❌ | Illegal hidden assumption about betweenness |
| P*D | ⚠️ | Congruence lemmas available, but length-addition step is uncitable |
| P*L | ❌ | Would leave an unfillable `sorry` in Lean/Coq |
| Cross-layer | ❌ | S, M, P all break at the same step |

**Lesson.** S*L, M*L, and P*L fail at the *same* step, pinpointing the missing on-segment / betweenness condition. This is a canonical example of D passing while L fails.

### 3.3 Kempe's 1879 "proof" of the four-color theorem

**Proof sketch.** Kempe proved that any planar map has a vertex of degree at most 5, then argued that a minimal counterexample cannot contain a vertex of degree 2, 3, or 4 by Kempe-chain color swaps. For degree-5 vertices he used *two* simultaneous Kempe-chain swaps.

| Cell | Result | Comment |
|---|---|---|
| S*D | ⚠️ | Step 5 depends on step 4 |
| S*L | ❌ | Fails to state that the two Kempe chains do not interfere |
| M*D | ⚠️ | Missing a lemma about simultaneous independent swaps |
| M*L | ❌ | Illegal generalization from one swap to two simultaneous swaps |
| P*D | ⚠️ | Program dependency absent (historical proof) |
| P*L | ❌ | Two swaps can produce an illegal coloring |
| Cross-layer | ❌ | All layers break at step 5 |

**Lesson.** The failure is a *simultaneity* error: an operation that is safe once is not automatically safe twice in parallel. The framework locates this as an M*L / P*L inference-rule violation.

### 3.4 Appel–Haken's 1976 computer-assisted proof

**Proof sketch.** Construct an unavoidable set U of 1936 configurations; prove each is reducible; use the discharging method to show U is unavoidable. Much of the reducibility checking was done by computer.

| Cell | Result | Comment |
|---|---|---|
| S*D | ✅ | Dependency chain closed |
| S*L | ⚠️ | The semantic role of "computer verification" is fuzzy |
| M*D | ✅ | Mathematical dependency graph closed |
| M*L | ⚠️ | Discharging rules require human audit of boundary cases |
| P*D | ⚠️ | Long external dependency chain: program → compiler → OS → hardware → input files |
| P*L | ❌ | Program verification ≠ formalized mathematical proof (in 1976) |
| Cross-layer L | ❌ | P verifies finitely many configurations; S/M claim a universal theorem |

**Lesson.** A *mathematically correct* proof can still have a P*L and cross-layer-L gap. This distinguishes program verification from formal proof and highlights the "finite → universal" inferential bridge that must be supplied by M, not by P alone.

### 3.5 Diagnostic: the Riemann Hypothesis

Because RH is an open conjecture, not a proof, S*D/S*L and P*D/P*L are not applicable in the same way. The diagnostic focuses on M*D and M*L.

| Cell | Result | Comment |
|---|---|---|
| M*D | ⚠️ | Many partial results exist, but no closed path to the full conjecture |
| M*L | ❌ | No legitimate way to promote local/statistical information to a universal claim about all non-trivial zeros |
| Cross-layer | ❌ | Function-field analogues (Weil–Deligne) do not transfer to number fields |

**Lesson.** For open problems, the framework reframes the question from "is it true?" to "what is the nearest proven theorem and what kind of gap remains?"

### 3.6 The 2026 Navier–Stokes autoformalisation incident: a P-pass / S-fail case

In 2026, an AI system produced a Lean formalization, claimed to verify a natural-language (NL) proof of finite-time blow-up for a Navier–Stokes-type equation, that compiled successfully. Bastounis, Circelli, and Hansen (arXiv:2610.08144) subsequently showed that the formalized statement was **not** a faithful translation of the NL claim: in one key lemma the NL proof requires m+4 derivatives while the Lean statement requires m+5 (strictly weaker), and the pressure–flux estimates use different bounds proved by different methods. The authors further prove that faithful autoformalisation in general has **SCI = ∞** (Solvability Complexity Index), strictly above the halting problem — no algorithm can guarantee translation fidelity.

| Cell | Result | Comment |
|---|---|---|
| S*D | ❌ | Translation NL→formal is not content-preserving (m+4 vs m+5) |
| S*L | ❌ | Faithful translation is uncomputable in general (SCI = ∞) |
| M*D | ⚠️ | Correctness of the original NL proof remains unconfirmed by the Lean artifact |
| M*L | ⚠️ | NL logical structure cannot be audited via the unfaithful formalization |
| P*D | ✅ | Lean kernel verification internally consistent |
| P*L | ⚠️ | Compilation-driven objective misaligned with semantic fidelity |
| Cross-layer | ❌ | S→P mapping broken; P→M upgrade illegal |

**Lesson.** This is a new failure type in our corpus — **Type VII: P-layer passes while S-layer translation fails**. It is not circular reasoning, not foresight, not a boundary omission, but a breakdown of the S→P mapping combined with an illegal P→M upgrade ("Lean compiles, therefore the NL theorem is verified"). The incident demonstrates that the green checkmark of a proof assistant certifies a formal object, not mathematical content, and that semantic-fidelity review is a permanently human-gated step (see §7.2).

### 3.7 Extended case corpus

The full report corpus (46 files, fingerprinted above) contains nineteen audited cases. Summary:

| Case | Type | Verdict | Primary failing cell(s) | Core finding |
|---|---|---|---|---|
| Euclid, infinitude of primes | Correct proof | ✅ Full pass | — | Paradigmatic closure |
| √2 irrationality | Correct proof | ✅ Full pass | — | Contradiction + parity; reduction explicit |
| Cantor diagonal | Correct proof | ✅ Full pass | — | Representation trap (0.999…) defused by digit restriction |
| Harmonic series divergence | Correct proof | ✅ Full pass | — | 2^k grouping; boundary scan clean |
| Sum of first n odd numbers = n² | Correct proof | ✅ Full pass | — | Induction with explicit base/step |
| AM–GM (two variables) | Correct proof | ✅ Full pass | — | From square non-negativity; no target assumption |
| Pigeonhole principle | Correct proof | ✅ Full pass | — | Constructive counting; boundary n > m handled |
| Ramsey R(3,3) = 6 | Correct proof | ✅ Full pass | — | Finite case analysis closed |
| Wilson's theorem | Proved conjecture | ✅ Full pass | — | Inverse pairing; ±1 fixed-point trap handled |
| Fermat's little theorem | Proved conjecture | ✅ Full pass | — | Multiplicative bijection ⇒ product equality |
| Basel problem ζ(2) = π²/6 | Proved conjecture | ✅ Full pass | — | Fourier route; convergence proved before substitution |
| All triangles isosceles | Classical fallacy | ❌ Fail | S*L, M*L, P*L | Betweenness default; PE = PD ⟺ target |
| Kempe four-color | Research-level fallacy | ❌ Fail | M*L, P*L | Two simultaneous swaps interfere |
| Fermat "all Fₙ prime" | Disproved conjecture | ❌ (conjecture false) | M*L (induction from 5 cases) | Euler's counterexample F₅; 641 = 5·2⁷+1 |
| Euler sum-of-powers | Disproved conjecture | ❌ (conjecture false) | M*L (extrapolation) | Lander–Parkin–Selfridge counterexample (1966) |
| Appel–Haken four-color | Computer-assisted proof | ⚠️ Partial | P*L, cross-layer | Finite→universal bridge; community acceptance |
| Riemann Hypothesis | Open | ⚠️ Diagnostic | M*L | Local/statistical → universal promotion gap |
| Andrews–Curtis conjecture | Open | ⚠️ Diagnostic | M*L | No nontrivial AC-invariant; super-exponential search lower bounds |
| Navier–Stokes AI formalization | Translation failure | ❌ Fail | S*D, S*L, cross-layer | P passes, S→P translation unfaithful; SCI = ∞ |

---

## 4. The Lean Formalization Equivalence Spectrum

For the P layer we need a graded notion of equivalence, because "formalizable" is not binary. In Lean, the hierarchy is approximately:

| Strength | Lean mechanism | Criterion |
|---|---|---|
| ⭐⭐⭐ | Definitional equality | Provable by `rfl` |
| ⭐⭐⭐ | `Equiv α β` / `RingEquiv R S` | Bijection with explicit inverse and preservation proofs |
| ⭐⭐ | `funext` / `propext` | Function/proposition extensionality; may block computation |
| ⭐⭐ | `Quot.sound` | Quotient types; must prove respect for equivalence |
| ⭐ | Testing / numerical validation | Empirical equivalence only; not a deterministic certificate |

This spectrum prevents the common error of claiming "it can be formalized" when the best available evidence is only numerical testing. The Navier–Stokes incident (§3.6) shows the dual error: even a ⭐⭐⭐-grade kernel verification certifies only the formal statement as written, not its fidelity to the natural-language theorem.

---

## 5. Nearest-Proven-Theorem Maps for Open Conjectures

For an unproved conjecture, we propose a four-step heuristic:

1. **Sketch its S/M/P structure.** Write down its semantic formulation, mathematical objects, and any programmable aspects.
2. **Search for the nearest proven theorem.** Find the result that shares the largest number of structural elements.
3. **Classify the gap.** Common gap patterns:
   - Approximate → exact (e.g., bounded prime gaps H ≤ 246 → twin primes);
   - Local/partial → global/universal (e.g., Tao's almost-all Collatz → full Collatz);
   - Equivalence loop (e.g., known barriers in P vs NP);
   - Function-field → number-field transfer failure (e.g., Mason–Stothers → abc);
   - Existence-without-construction (e.g., AC-triviality with no constructive trivialization sequence).
4. **Identify the responsible layer.** Most serious gaps live at M*L; S*L gaps are usually communication problems; P*L gaps are often consequences of M*L gaps.

**Worked example: the Andrews–Curtis conjecture.** The conjecture asserts that every balanced presentation of the trivial group can be reduced to the trivial presentation by Andrews–Curtis moves (AC1–AC3). Our audit finds S/M/P dependency graphs all healthy but M*L substantially gapped: there is no known nontrivial invariant preserved by AC moves, and Bridson–Lishak-type results show that AC-trivial presentations can require super-exponentially many moves, excluding pure search as a proof strategy. The shortest potential counterexample, the Akbulut–Kirby presentation AK(3) = ⟨x, y | x³ = y⁴, xyx = yxy⟩, was shown in 2024 to be *stably* AC-trivial (allowing stabilization move AC4), while the standard conjecture remains open. The nearest-proven relatives are: stable AC-triviality theorems, Nielsen equivalence results for specific presentation classes, and the triviality of the associated handle-decomposition problems — each differing from the target by exactly one structural feature, which the map makes explicit. The conjecture is also the target of the 2026 SAIR Foundation challenge (discovery track: shortest trivializing sequences for 10,115 two-generator presentations; proof track: proof or counterexample).

---

## 6. Machine-Assisted Construction and Anti-Foresight Guarding

So far we have treated S/M/P × D/L as an *audit* framework: a proof or conjecture is presented, and the framework locates the break. The same layers can be inverted into a *construction* protocol whose purpose is to prevent a particularly insidious kind of error — **foresight** — from entering the proof while it is being written.

### 6.1 What is foresight?

**Foresight** (or hindsight) is the use of the target conclusion P, or of information equivalent to P, as an unstated premise in the proof of P. It is not a local inference error; it is a meta-strategic error. The all-triangles-are-isosceles fallacy, for instance, tacitly assumes `PE = PD`, which is equivalent to the desired `AC = BC`. Kempe's fallacy assumes the independence of two Kempe-chain swaps, which is exactly what would have to be proved to rescue the theorem. In open-problem attempts, foresight often appears as the illegal promotion of local or statistical evidence to a universal claim.

### 6.2 Why machines are especially prone to foresight

Large language models and automated theorem provers are vulnerable to foresight for complementary reasons:

- **LLMs** are trained on polished, post-hoc expositions in which the target is already known. Their autoregressive objective rewards tokens that make the eventual conclusion "hang together," which is precisely the pressure that produces hidden circularity.
- **Reward functions** for proof search often optimize reachability of the target. A search that is rewarded only when it eventually proves P has an incentive to use P-shaped intermediate states.
- **Formal proof kernels** check local correctness but do not, by themselves, police global strategy. A Lean file can be syntactically valid and yet mathematically circular if the author imports a lemma that is secretly equivalent to the target.

### 6.3 The SMPDL construction protocol

The audit framework becomes a construction protocol through five machine-enforceable stages.

**Stage 0 — Goal and premise explicitation.** Translate P and the allowed premise set A into explicit S/M/P form. Each layer's goal is separately written down and the target P is marked as *forbidden* in every proof context until the final step.

**Stage 1 — Reverse sketch.** A planner (human, LLM, or proof planner) is allowed to propose a tree of subgoals `G₁, G₂, …, Gₙ` such that their conjunction would imply P. Every `Gᵢ` is tagged **OPEN** and receives a foresight-risk rating.

**Stage 2 — Forward rewrite.** Each `Gᵢ` must be proved independently from `A ∪ {already closed Gⱼ}`. The proof context explicitly excludes P and any proposition equivalent to P. Failure produces an honest `sorry` or `OPEN` marker rather than a hidden circular proof.

**Stage 3 — Bidirectional check.** For every closed `Gᵢ` the system verifies both `A ⊢ Gᵢ` and that `Gᵢ` genuinely advances toward P without already entailing P. The latter check prevents disguised restatements of the target.

**Stage 4 — Equivalence-cycle detection.** A dependency graph is maintained. If `Gᵢ` is propositionally equivalent to P, or if `Gᵢ` depends on P, the construction is halted with a `ForesightViolation`.

**Stage 5 — Boundary scanning.** For every quantifier, limit, division, or case split, the system generates degenerate test cases. This catches hidden assumptions such as "the point lies on the segment" or "the two operations commute."

### 6.4 Layered division of labor

| Agent | Best role | Why |
|---|---|---|
| **Human / meta-controller** | Choose high-level strategy, interpret honest `sorry`s, decide when to abandon a route | Judgment about research value |
| **LLM** | Generate reverse sketches and translate S-layer intuition into M/P skeletons | Pattern recognition and language |
| **Symbolic ATP** | Forward-rewrite search, equivalence detection, boundary scanning | Deterministic search and decision |
| **Proof kernel (Lean/Coq)** | Final local-correctness certification | Mechanical trustworthiness |

### 6.5 A minimal guard pseudo-code

The following `SMPDLGuard` illustrates how the protocol can be encoded:

```python
class SMPDLGuard:
    def __init__(self, goal_p, premises_a, prover_kernel):
        self.P = goal_p                 # target: forbidden until final step
        self.A = premises_a             # allowed premises
        self.kernel = prover_kernel     # Lean / Coq / SMT interface
        self.closed = set()
        self.open_goals = []

    def backward_sketch(self):
        self.open_goals = self.planner.decompose(self.P)
        for g in self.open_goals:
            g.status = "OPEN"
            g.risk = self.assess_foresight_risk(g)

    def forward_rewrite(self, g):
        if self.kernel.prove(
            g,
            premises=self.A | self.closed,
            forbidden={self.P, equivalences_of(self.P)}
        ):
            g.status = "CLOSED"
            self.closed.add(g)
            return True
        else:
            g.status = "OPEN / FORESIGHT BLOCKED"
            return False

    def bidirectional_check(self, g):
        from_premises = self.kernel.prove(g, self.A | self.closed)
        advances = not self.kernel.prove(self.P, {g})  # g does not imply P
        return from_premises and advances

    def detect_equivalence_cycle(self, g):
        if self.kernel.equivalent(g, self.P) \
           or self.kernel.depends_on(g, self.P):
            raise ForesightViolation(f"{g} equivalent to or depends on target")

    def run(self):
        self.backward_sketch()
        while self.open_goals:
            g = self.open_goals.pop(0)
            self.detect_equivalence_cycle(g)
            if not self.bidirectional_check(g):
                raise ForesightViolation(f"Bidirectional check failed: {g}")
            if not self.forward_rewrite(g):
                print(f"Honest sorry: {g}")
```

In a proof assistant the guard corresponds to a controlled namespace in which the target theorem is *not in scope* for any lemma proved inside it. Honest `sorry`s then become precise markers of genuinely open gaps rather than disguised failures.

### 6.6 A worked construction attempt: the Andrews–Curtis conjecture

We applied the five-stage protocol to the Andrews–Curtis conjecture as a stress test. Five natural proof routes were sketched in reverse and then attempted forward:

| Route | Status | Located gap |
|---|---|---|
| G₁: Find an AC-invariant | ❌ BLOCKED | Candidate invariants are not preserved under AC moves |
| G₂: Induction on presentation length | ❌ BLOCKED | The cancellation lemma is non-constructive; **potential equivalence cycle** — the lemma may tacitly assume a statement stronger than the n−1 case |
| G₃: Bridge via Nielsen transformations | ❌ BLOCKED | Nielsen equivalence is strictly coarser than AC equivalence |
| G₄: Bridge via stabilization | ⚠️ PARTIAL | AK(3) stably trivial (2024); the de-stabilization lemma is missing |
| G₅: Topological bridge (handle decompositions) | ❌ BLOCKED | Non-constructive; covers only the stable version |

The attempt produced no proof — by design, the protocol converts failed routes into explicit, located gaps rather than plausible-looking text. Notably, the equivalence-cycle detector flagged route G₂ before substantial effort was invested in it: the induction's cancellation lemma, on inspection, risks assuming precisely the kind of global trivialization the conjecture asserts. This is the protocol working as intended on a genuinely open problem. The full construction report and the audit report are part of the fingerprinted corpus.

### 6.7 From audit to construction: a closed loop

The construction protocol and the audit framework form a closed loop. The construction protocol produces a candidate proof together with an explicit list of open subgoals; the audit framework consumes the candidate and classifies failures into S/M/P × D/L cells. The result is a system that does not merely say "this proof is wrong" but "subgoal G₆ is open because the M*L promotion from critical-line moments to off-line control is unsupported."

---

## 7. The Human-Machine Division of Labor: Five Indispensable Human Roles

The case corpus — nineteen audits and twelve construction reports — lets us answer empirically which steps of proof construction and audit resisted mechanization in every single case. Five roles emerge; each is specified below with input, output, criterion, and a boundary rule against its neighbors. The full octuple-template definitions (definition + three constraints / input-output / criterion / subtypes / adjacency boundaries / case anchors / mechanizability / workflow anchor) are given in the corpus document `SMPDL_HumanRoles_Definitions.md`.

### 7.1 Role A — Concept singularity (概念奇点)

**Definition.** The invention, *without target-side guidance*, of the key construction, framework, or concept that closes a reasoning chain.

**Three constraints.** Generativity (produces a new object, not a selection among given ones); non-mechanicalness (not derivable by local rewrite from the premises); sparsity (typically one or two per proof).

**Case anchors.** Euclid's N = p₁⋯pₙ + 1; Cantor's diagonal; Wilson's inverse pairing; the 2^k grouping for the harmonic series; the Fourier-route choice for Basel; the multiplicative bijection for Fermat's little theorem.

**Evidence from open problems.** The Andrews–Curtis construction attempt (§6.6) failed precisely because no concept singularity is known: no AC-invariant (G₁) and no constructive cancellation lemma (G₂). The blockage of an entire open problem can be located at the absence of a Role-A object.

**Mechanizability.** Lowest of the five roles. Machines can propose candidates, but the corpus shows accepted singularities are recognized, not generated, by pattern matching.

### 7.2 Role B — Semantic-fidelity review (语义忠实审查)

**Definition.** The judgment of whether a cross-layer translation (NL ↔ formal statement; S → M → P) preserves mathematical content.

**Three constraints.** Cross-layer (compares two presentations of the "same" content); judgmental (ends in a fidelity verdict, not a derivation); **SCI = ∞** — by Bastounis–Circelli–Hansen, no algorithm can guarantee faithful autoformalisation, so this role is not merely unmechanized but unmechanizable in general.

**Case anchors.** The Navier–Stokes incident (§3.6): the m+4 → m+5 derivative-count drift and the changed pressure–flux estimates were invisible to the Lean kernel and detectable only by a human comparing NL and formal statements line by line.

**Boundary with Role D.** Drift *between two presentations* → B; failure *inside a single argument* → D.

### 7.3 Role C — Gap characterization (缺口刻画)

**Definition.** For an unfinished proof or open conjecture: locate the break, judge whether it is technical or essential, and characterize the structural distance between what known routes can deliver and what the target demands.

**Three constraints.** Faces the unfinished; meta-mathematical (classifies gaps, does not fill them); navigational (output redirects research effort).

**Case anchors.** RH: "local/statistical → universal" promotion gap. Andrews–Curtis: "no nontrivial invariant" + "existence without construction," plus the detection that the induction route hides a potential equivalence cycle. The two gaps are of different *types*: RH lacks an implication; ACC lacks an object.

**Boundary with Role D.** "What is missing?" (unfinished) → C; "where does it break?" (finished-looking) → D.

### 7.4 Role D — Trap foresight (陷阱预见)

**Definition.** The active, failure-directed review of an already-formed draft argument, within a single layer, focused on boundary and degenerate configurations.

**Seven-type taxonomy** (each type is anchored in the corpus):

| # | Type | Mechanism | Corpus anchor |
|---|---|---|---|
| I | Representation trap | Non-unique representation lets the constructed object fall into the excluded set via another representation | Cantor 0.999… (defused: digits from {1,2}); √2 lowest terms |
| II | Fixed-point trap | Pairing/reduction requires fixed-point-freeness; omission breaks the count | Wilson ±1 self-inverse; the isosceles fallacy's PE = PD as a vicious fixed point |
| III | Betweenness-default trap | Betweenness is an independent assertion, not a default from the construction | Isosceles fallacy: P lies on the circumcircle, feet on extensions |
| IV | Operation-order trap | Legality of substitution/limit/series manipulation must be proved first | Basel: Dirichlet convergence before x = π substitution |
| V | Premise-domain trap | Rules silently fail at the boundary of their premise domain | Fermat's little theorem p ∤ a; "conclusion holds at boundary" ≠ "argument valid at boundary" |
| VI | Quantifier-range trap | Failure to find ≠ non-existence | ACC: super-exponential lower bounds make search failure non-evidential |
| VII | Operation-interaction trap | A later operation destroys the guard condition of an earlier one | Kempe's double swap (Heawood/Errera counterexamples) |

**Executable artifact.** TRAP-CHECK v1.0: a 21-item checklist (3 per type) embedded in Stage 5 of the construction protocol; every hit is registered in a boundary-case log. Example item (VII.1): "Has every multi-operation argument been rewritten as a state machine and verified step by step?" — had this item existed in 1879, Kempe's fallacy would have been intercepted on the spot.

**Mechanizability.** Semi-automatable in the form *human-built trap library + machine library-scan + human handling of out-of-library hits*. The hardest component to mechanize is the failure-memory library itself: the community's history of failed proofs has never been systematically formalized.

### 7.5 Role E — Verification interpretation (验证解读)

**Definition.** The judgment of what a verification output (kernel pass, test suite, numerical certificate, community vote) actually establishes, and how strong the evidence is.

**Three constraints.** Faces verification *outputs*, not arguments; interpretive (maps artifact → claim strength); has a social dimension (what the community accepts as proved).

**Case anchors.** Navier–Stokes: "Lean ✅" ≠ "the NL theorem is verified" — the output certified a *weaker* formal statement. Appel–Haken: the 1976 community judgment that computer-checked reducibility counts as proof was a Role-E act, not a derivation. Bridson–Lishak lower bounds: interpreting "search found nothing" as non-evidence is E (with a D-VI flavor).

**Boundary with Role B.** B judges whether a translation is correct; E judges what a verification means. The Navier–Stokes incident required both, in sequence: E to ask "what exactly was verified?", B to answer "not the NL theorem."

### 7.6 Decision tree and cross-role flow

Any audit/construction action is classified by five questions:

1. Did it produce a new object/construction? → **A**
2. Did it compare two presentations of the same content? → **B**
3. Facing the unfinished, did it ask "what is missing"? → **C**
4. Facing a finished-looking draft, did it ask "where does it break"? → **D**
5. Facing a verification output, did it ask "what does this prove"? → **E**

Cross-role transitions observed in the corpus: B→A (translation impossible; the formalization must be re-conceived); A→C (repeated failure to invent converts into an essential-gap verdict); C→A (a characterized gap gets filled by a new construction); D→C (an unrepairable, route-level failure — Kempe — becomes a gap characterization); E→B (a suspected specification drift triggers a mapping check). Roles are **action types**, not job descriptions: one person may perform all five, but every action must be classifiable into exactly one — this is the meta-level analogue of the anti-foresight discipline: the audit process itself must be auditable.

### 7.7 Machine-interface principles

1. **Machines never silently close subgoals** — CLOSED requires human confirmation or an auditable evidence chain.
2. **Cross-layer anchors are human-registered** — machines run consistency diffs between anchors, never define the anchors.
3. **Cycle detection is two-stage** — machines report candidate cycles; humans make the "substantial equivalence" semantic call.
4. **Concept singularities are left blank** — the machine marks "a construction of type X is needed here" and waits; it does not generate unreviewed constructions.

---

## 8. Discussion and Limitations

**What the framework is.** A structured human-readable audit protocol. It helps reviewers and students locate structural breaks and articulate them precisely; its construction inversion converts hidden circularity into explicit `sorry`s; its division-of-labor analysis states exactly where human judgment cannot be delegated, with the Navier–Stokes incident as empirical evidence that semantic-fidelity review (B) and verification interpretation (E) become *more*, not less, labor-intensive in the AI era.

**What it is not.** It is not a decision procedure for proof validity. A proof that passes the framework may still contain errors the framework did not ask about; a proof that fails the framework is not thereby mathematically false — it is *structurally inadmissible* until repaired. The five human roles are empirical conclusions from a 19-case corpus, not a completeness proof.

**Scope.** The framework is most useful for:
- AI-generated proofs and AI-produced formalizations;
- student proofs;
- historical fallacies and disproved conjectures;
- research-level proofs with computer-assisted or cross-domain components;
- open-problem diagnostics and proof-route triage.

It is less necessary for fully formalized proofs that already compile in a trusted proof assistant — provided the formal statement's fidelity to the intended claim has passed Role-B review.

---

## 9. Conclusion

We have presented S/M/P × D/L, a six-cell audit matrix for mathematical proofs and conjectures. By separating semantic, mathematical, and programming layers, and by separating dependency structure from logical discipline within each layer, the framework gives a finer diagnosis than pass/fail grading. A nineteen-case corpus shows that it locates the exact step at which classical fallacies fail, explains how disproved conjectures seduced their authors, distinguishes program verification from formal proof, maps the structural gap between an open conjecture and its nearest proven relative, and — in the 2026 Navier–Stokes incident — identifies a failure type invisible to proof kernels: the formally verified statement was not the theorem that was claimed.

The framework also works in reverse: the same layers provide a construction protocol for machine-assisted proving that hardens the process against foresight, and a worked attempt on the Andrews–Curtis conjecture shows the protocol converting five failed routes into five explicitly located gaps — including one potential equivalence cycle caught before significant effort was spent. Finally, the corpus grounds a precise division of labor: five human-indispensable roles (concept singularity, semantic-fidelity review, gap characterization, trap foresight, verification interpretation), each with an operational definition, a boundary rule, and a mechanizability assessment. Machines verify formal objects; humans guard mathematical content. Making that boundary explicit — and auditable — is the framework's main contribution.

---

## Acknowledgments

The framework grew out of the Göttingen Mathematical History Index project and earlier terminology-precision work on isomorphism and structure in interdisciplinary mathematical writing. Author: CAMPANASILVAE · fecit · MMXXVI. Licensed under CC BY-NC-SA 4.0.

---

## References

1. Akbulut, S., & Kirby, R. (1985). A potential smooth counterexample in dimension 4 to the Poincaré conjecture, the Schoenflies conjecture, and the Andrews–Curtis conjecture. *Topology*, 24(4), 375–390.
2. Andrews, J. J., & Curtis, M. L. (1965). Free groups and handlebodies. *Proceedings of the AMS*, 16(2), 192–195.
3. Appel, K., & Haken, W. (1989). *Every Planar Map is Four Colorable*. Contemporary Mathematics, 98. AMS.
4. Bastounis, A., Circelli, A., & Hansen, A. C. (2026). Lost in translation: On the SCI of autoformalisation and the limits of AI-assisted formal verification. *arXiv:2610.08144*.
5. Bridson, M. R., & Lishak, B. (2024). On the complexity of trivializing group presentations. (Super-exponential lower bounds for Andrews–Curtis trivializations.)
6. Euler, L. (1737/1740). De summis serierum reciprocarum (Basel problem). *Commentarii Academiae Scientiarum Petropolitanae*.
7. Gonthier, G. (2008). Formal proof — the four-color theorem. *Notices of the AMS*, 55(11), 1382–1393.
8. Haiman, J. (1980). The iconicity of grammar: Isomorphism and motivation. *Language*, 56(3), 515–540.
9. Heawood, P. J. (1890). Map-colour theorem. *Quarterly Journal of Mathematics*, 24, 332–338.
10. Kempe, A. B. (1879). On the geographical problem of the four colours. *American Journal of Mathematics*, 2(3), 193–200.
11. Kuryłowicz, J. (1962). *O czynnikach i kierunkach innowacji językowych*. (Factors and directions of linguistic innovation.)
12. Lander, L. J., & Parkin, T. R. (1966). Counterexample to Euler's conjecture on sums of like powers. *Bulletin of the AMS*, 72(6), 1079.
13. Lyons, J. (1977). *Semantics* (Vols. 1–2). Cambridge University Press.
14. Milner, R. (1980). A Calculus of Communicating Systems. *LNCS*, 92.
15. Morris, J. H. (1969). *Lambda-Calculus Models of Programming Languages*. PhD thesis, MIT.
16. Piaget, J. (1968). *Le structuralisme*. Presses Universitaires de France.
17. Robertson, N., Sanders, D. P., Seymour, P., & Thomas, R. (1997). The four-colour theorem. *Journal of Combinatorial Theory, Series B*, 70(1), 2–44.
18. Saussure, F. de (1916). *Cours de linguistique générale*. Payot.
19. Shehper, A., et al. (2024). Stable Andrews–Curtis triviality of the Akbulut–Kirby presentations via reinforcement-learning-guided search.
20. The Lean Prover Community. *Lean Reference Manual* and *mathlib4* documentation. https://lean-lang.org
21. Wilson, R. (2014). *Four Colors Suffice: How the Map Problem Was Solved*. Princeton University Press.
