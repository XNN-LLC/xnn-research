# Weight-space carriers of the global workspace: deletion microscopy meets J-space

> **PUBLIC EDITION — v0.5-public, 2026-07-07** (private v0.1 2026-07-06; v0.2–v0.4
> 2026-07-07). This is the public edition of a position note maintained in our private
> research repository.¹ Version lineage, stated exactly: the science text below is the
> public edition of **private v0.4** (PM-43), which added the qwen3-8b scale leg (§3.2)
> and the E1 int4-sweep status to the v0.3 science text; the earlier *v0.4-public*
> release of this file added explicit public authorship, company attribution, and
> LLM-assistance/accountability boundaries around the v0.3 science text (see
> `PUBLIC_UPDATE_V0_4.md`) — those additions are preserved below; *v0.5-public* is the
> two combined, and adds no private implementation details. Three mechanical
> transformations were applied for publication: (a) internal file paths are replaced by
> *italic descriptors* bound to entries of [`PRIORITY_MANIFEST.md`](PRIORITY_MANIFEST.md)
> (PM-xx) — sha256 commitments that make every citation verifiable under later
> disclosure; (b) pre-registered threshold *values* and other frozen constants are not
> printed — they are hash-committed (the verdict labels and all result numbers are
> printed in full); (c) implementation internals (module names, GPU-implementation
> detail, command flags, machine paths) are removed — they are bound collectively by the
> private repo-HEAD commitments in the manifest, and specific hardware is genericized
> ("a rented high-memory GPU instance"). Beyond those transformations, the earlier
> audit-fix rebindings (the §3.1/PM-41 readout binding, the verdict-vocabulary phrasing)
> are carried forward, and one dated cross-reference that postdates private v0.4 was
> added: the §3.2 parenthetical pointing to the completed K=4 null ensemble and position
> sweep (RESULTS.md §8–§9). Nothing else was changed.
>
> **Claim-tag legend (mandatory per our repo discipline):**
> - **[committed]** — proven at the stated scope by code, a run artifact, or a verdict in
>   the working (private¹) repository at the cited commit; externally committed-to via
>   the sha256 priority manifest in this repository (`PRIORITY_MANIFEST.md`).
> - **[preregistered]** — a frozen, hash-committed design; the evaluation has NOT run.
> - **[planned]** — a dated intention. Nothing tagged [planned] is a result.
>
> **Quote-verification status (done before publication):** every quotation below was
> verified against the full extracted text of the commentary PDF (Dehaene–Naccache,
> Eleos, Nanda sections) and against the published paper's main body (formal
> J-Lens/J-space definitions, author list and order, publication date, models, Figures
> 20/24/29 with captions, the variance and capacity numbers, the covert-content and
> routine-information quotes) on 2026-07-07. Known residue: the paper's appendix region
> truncates in programmatic fetches, so Figure 88 and A.17 are cited via the commentary's
> references to them; commentary quotes are anchored by author + quoted text, not page
> numbers.
>
> ¹ github.com/XNN-LLC/xnn-see-research is a **private repository**; artifact hashes are
> committed in [`PRIORITY_MANIFEST.md`](PRIORITY_MANIFEST.md); access under NDA on
> request. All commit hashes cited below refer to that repository and are bound by the
> manifest's repo-HEAD commitment.

---

## Authors / Background

This note is authored and maintained by Gleb Stepanov, an independent researcher
and developer and founder/lead developer of XNN LLC, an independent research
and development company based in Georgia, USA. XNN LLC is not an academic lab.

LLM systems may assist with writing, editing, and code workflows. They are not
the source of authority for the claims in this note. Claim authority is bounded
to committed artifacts, run results, timestamps, sha256 manifests, and
reproducible records referenced by the public priority manifest.

---

**Abstract.** Anthropic's "Verbalizable Representations Form a Global Workspace in
Language Models" (2026-07-06) identifies a small, privileged subspace of activation
space — J-space — that carries a model's reportable, flexibly-usable content, and shows
causally that swapping content in that space changes what the model *says about* its
processing without changing the processing itself. We think this is the most interesting
functional macro-object interpretability has produced in some time, and the accompanying
commentary states its two open weaknesses plainly: causal steering claims are hard to
distinguish from "just breaking the model," and ignition — the all-or-none workspace-entry
signature — "remains to be fully demonstrated." This note describes a complementary
research axis we have been building since June 2026 — state-dependent causal
necessity in *weight* space, measured with a quantization-residual deletion microscope
(`R = W − dequant(Q(W))`) under norm-matched shuffle-null controls, preregistration with
hash-committed numeric freezes, FDR over the entire search tree, and per-operation
silicon receipts on a self-contained runtime whose greedy CUDA decode is verified
bitwise-identical across runs — and reports a first result: on 2026-07-06, the day the
paper landed, our null-gated mapper reproduced the paper's central dissociation signature
on open weights (qwen3-1.7b) — a mid-band concept swap moves the model's verbal report
by +11.0 nats, 10.4x its norm-matched shuffle-null, while the automatic continuation
keeps writing the source language — and the same instrument's null *rejected* a
confounded variant of the experiment that an un-nulled pipeline would have published. The
preregistered ignition design (near-margin route-flips at MoE routing boundaries,
categorical and threshold-free) has passed its hard feasibility gate on OLMoE,
bit-identically reproduced; its confirmatory evaluation remains gated on sign-off. We
preview the remaining experiments (E1–E4), promise only the verdicts our gates return
(including negatives), and take no position on consciousness.

---

## 1. What the workspace paper established

### 1.1 The result, as we read it

*(Quotations below are verbatim from the published paper or, where marked, from its
commentary pack; both verification passes completed 2026-07-07 — see the header.)*

The paper (Gurnee, Sofroniew, …, Lindsey — co-lead asterisks on Gurnee, Sofroniew, and
Lindsey, with Lindsey last; July 6, 2026; results "on Claude Sonnet 4.5, but we
corroborate key results on Haiku 4.5 and Opus 4.5 as well";
transformer-circuits.pub/2026/workspace) introduces the **J-Lens**: per layer, the
average Jacobian from the residual stream at layer ℓ to the *final* residual stream —
"J_ℓ = E_{t, t'≥t, prompt} [∂h_{final,t'} / ∂h_{ℓ,t}]", "where the expectation is taken
over the source position t, all subsequent positions t' within the context, and a corpus
of one thousand prompts sampled from a pretraining-like distribution" — read out through
the final norm and unembedding: "lens(h_ℓ) = softmax(W_U norm(J_ℓ h_ℓ))". Directions
that survive the averaging are directions the model is *poised to report* — or, in the
Dehaene–Naccache commentary's gloss, "the averaging is the conceptual heart of the
method: it separates representations that are genuinely poised for report from those
that merely happen to leak into the output in one particular context." The **J-space**
is then "the set of points expressible as a sparse nonnegative combination of J-lens
vectors," with sparsity "no more than 25, which we empirically observed to be the number
of J-lens vectors that are meaningfully active at a given time"; it "typically accounts
for only a small fraction of total activation variance (varying by layer, but never more
than 10%)" (all paper-verbatim). It is selective in function, not just small: under an
automatic line-wrapping instruction "the model produces a fluent continuation that wraps
at approximately the right column, yet number tokens are entirely absent from the lens
across the prompt" — routine information stays out of the workspace unless a task
explicitly pulls it in.

Three causal findings give the object its function (quotes paper-verbatim unless marked):

1. **Swaps flip reports, not processing** (Figure 20). "In the explicit report task, the
   model says 'Spanish' unmodified and 'French' under the swap"; downstream high-level
   inferences move with it ("'Hola' becomes 'Bonjour'; asked for the pre-Euro currency,
   'Peseta' becomes 'Franc'"), yet "in the continuation and anomaly detection tasks, the
   swap has no effect … it produces fluent Spanish regardless."
2. **Ablation dissociates flexible from routine** (Figure 24: "Effect of J-space ablation
   across a battery of tasks … under light, medium, and heavy ablation, normalized to
   unablated Sonnet 4.5"). Impaired: multi-hop reasoning, Caesar-cipher decoding, analogy
   completion, translation, sonnet writing, TriviaQA; preserved: MMLU, sentiment
   classification, SQuAD extraction, odd-one-out. Separately, as workspace-*content*
   evidence, the space holds unreported intermediates: instructed to "compute 3²−2 while
   writing sentence X," the J-space carries the unreported 9 and then 7
   (Dehaene–Naccache commentary's account of the hold-in-mind experiments).
3. **The space carries covert content.** Paper-verbatim: "the workspace sometimes
   encodes recognition of being in an evaluation (fake, fictional), and … ablating these
   representations can surface malicious propensities that were otherwise concealed";
   J-space shows "'secretly' and 'trick' in a model disposed to write malicious code,"
   and the model "internally flagging suspicious internet search results as a prompt
   injection" — none of it surfacing in the overt output.

Two aspects of the paper's own epistemics matter to us as much as the result. First, the
layer-band finding is corroborated by a forward-only method — in Nanda's commentary:
"Figure 88 provides significant additional corroboration, finding that the same bands of
layers where J-Lens works also work on estimates of the concept vectors derived by
simply taking average differences in activations. Deriving the same result with a
non-J-Lens method seems to rule out a fair amount of ways this could be spurious" (the
appendix figure number is cited per the commentary; the paper's appendix region
truncates in our programmatic fetches). Second, the paper ships with a commentary pack
containing the strongest available criticism: Dehaene and Naccache (the global-workspace
theorists themselves), Eleos AI, and Neel Nanda, whose group "replicated the core claims
on Qwen 3.6 27B" within days — n=25 prompts for the main replication, with the paper's
own ablations showing n=10 "almost as good," and a scaling probe on Qwen3.5-397B-A17B
(~1 hour, n=4, 8xH200) (Nanda replication notes, "Cost and Difficulty of Replicating
J-Lens"). Nanda's commentary states the standing weaknesses without varnish: needing
concepts to correspond to single vocabulary tokens "seems fairly restrictive"; the
average-Jacobian estimator is "a crude approach that will find noisy directions"; the
replication was agent-assisted — "a coding agent given the paper did it pretty well,
though we recommend sanity checking"; and, on his own negative-steering evidence, the
caveat that generalizes to every causal steering claim in this field: "it's always
difficult to rule out ways that steering is just breaking the model."

### 1.2 Why we think this matters (genuinely)

Interpretability has been prolific at producing *features* — atlases of directions that
correlate with concepts. It has been much poorer at producing *functional macro-objects*:
structures with a job description, a behavioral contract, and a falsifiable boundary
between what they do and do not carry. J-space is the latter kind of object. The
flexible-vs-routine ablation dissociation is a real behavioral contract; the
report-vs-continuation split in the swap experiments is a real boundary; and the covert
content result gives the object immediate safety relevance (a place to look for what a
model knows but does not say). The paper also imports, deliberately and carefully, the
one theory from cognitive science — global workspace theory — that comes with decades of
experimental signatures to check against, and then invites the theory's authors to grade
the attempt in public. That is how this kind of claim should be made.

We are writing this note because we believe the result — and because the two weaknesses
its own commentary names, steering-validity and missing ignition, are exactly the two
problems our program has been building instruments for since June.

---

## 2. The complementary axis: causal necessity in weight space

The paper asks: *where in activation space does reportable content live at runtime?* Our
program asks the adjacent question one level down: **which stored distinctions in the
weights are causally necessary for which behaviors, in which inference states, at what
precision?** Same object of interest — a privileged, functionally load-bearing subspace —
different substrate: bytes on disk rather than activations in flight. Everything below
is committed in the working (private¹) repository with commit hashes; this repository
carries the sha256 priority manifest (`PRIORITY_MANIFEST.md`), the genesis timeline
(`TIMELINE.md`), and this public edition.

### 2.1 State-dependent necessity, formalized (June 2026) **[committed `5223bc69`, refined `74c056ba`; PM-16]**

*The carrier-mapping theory document* (captured 2026-06-28; byte-identical from that
date through the current private HEAD — the manifest proves it) fixes the core
inversion: a physical weight bit has a fixed storage address, but its causal significance

```
I_b(s_t) = D( F_W(s_t), F_{W\b}(s_t) )
```

is a dynamic function of the inference state `s_t` (prompt, layer, token position, decode
step, routing state, KV history). The same perturbation can be numerically invisible in
one state and cross a discrete decision boundary in another — the document's motivating
example is an MoE router at `r_1 = 0.501` vs `r_2 = 0.499`, where a low-order
contribution flips the route, versus `0.8` vs `0.2`, where it cannot. Carriers are
predicted to organize into families (routing, magnitude, memory, **boundary**, redundant,
context-gated, coalition), and negatives are required to be coverage-scoped: "no
necessity observed under tested state coverage" is the only honest negative, never
"this bit is useless."

### 2.2 The preregistered apparatus (Phase 3) **[preregistered `4980cfb2` + numeric freeze `aca08a52`; PM-17, PM-18; apparatus code committed; feasibility gate PASSED (§5); confirmatory evaluation NOT run]**

*The Phase-3 preregistration* (2026-06-28, LOCKED; byte-identical through the current
private HEAD) turns the thesis into a fail-closed measurement design, and its
adversarial amendments are the part we would most like other groups to steal:

- **A1 — the first-proof substrate is a categorical event.** The crispest instantiation
  of state-dependent necessity is the discrete router top-k flip `1[e_l ≠ e'_l]` on a
  real MoE (OLMoE-1B-7B: 16 layers, 64 experts, top-8, `norm_topk_prob=false`, so the
  routing margin `m = r_rank8 − r_rank9` is exact algebra). No calibrated soft threshold
  anywhere in the headline signal.
- **A2 — no naive bit flips.** The intervention primitive is a representation-aware
  contribution fraction `δw = −α·w` over a frozen α-grid — dtype-agnostic, with no
  IEEE-catastrophe regime. Exponent/sign flips are demoted to a tripwire *control*.
- **A3 — an encoding-artifact firewall** (monotone-α response, re-quantization
  invariance, activation-regime logging) that must pass before any effect counts as
  semantics rather than a float-format accident.
- **A4–A8 — search honesty.** Frozen candidate budgets; family-wise/FDR correction over
  the *entire* search tree of (carrier, state) tests; mechanical state-set construction
  (no hand-picking the state where the effect lives); a global STOP if the null cannot be
  calibrated; a planted-necessity positive control so an insensitive apparatus cannot
  masquerade as an honest negative; and every carrier discovered on the development split
  must re-clear all gates at its frozen physical byte address on a held-out split.
- **Fail-closed verdict vocabulary:** `SUPPORTED` / `carrier_unsupported` /
  `STOP-UNDERPOWERED` / `MODE_DISAGREEMENT_INCONCLUSIVE` / `VOID` are all first-class,
  expected outcomes.

Status, stated exactly: the apparatus is implemented in-tree in the runtime (module set
private, bound by the repo-HEAD commitment), every numeric degree of freedom is frozen
and hash-committed (*the Phase-3 numeric freeze*, PM-18), the hard feasibility
precondition has now PASSED on the real substrate (§5), and the confirmatory evaluation
is gated on science-lead sign-off and has **not** run. There is no Phase-3 carrier
verdict to report, and this note claims none.

### 2.3 Quantization as a deletion microscope (July 2026) **[committed; five tools + one negative verdict; PM-20]**

*The deletion-microscopy program note* (2026-07-04) operationalizes a complementary,
static reading of the same question. One formula:

```
W_bf16 = dequant(Q(W_bf16)) + R        R = W_bf16 − dequant(Q(W_bf16))
```

Quantization is controlled deletion of distinctions inside the executable model. `R` is
not noise — it is an addressable map of everything the quantized pack can no longer tell
apart. The program's question: which part of `R` is numerical slack, and which part was
*holding a behavior*? The instrument chain, all on the private main branch:

1. **residual-ledger** — per-tensor inventory of `R` **[committed `f74586c7`]**;
2. **residual-reinject** — put pieces of `R` back (by layer, role, channel, tensor-name
   scope) and measure behavior recovery, with a **fail-closed norm-matched shuffle-null**
   built in **[committed `8821ffd6`]**;
3. **silicon-trace** — a per-operation output-checksum hook on the decode chain, one
   semantic hardware receipt per executed op **[committed `6d0c3744`]**;
4. **silicon-diff** — op-for-op diff of two traces; localizes *where* two packs diverge
   in execution, read at first divergence **[committed `59a95d6b`]**;
5. **proof-pack** — a mixed-precision pack binding base → reinstated carriers → the
   behavioral gates they restore → the source-weight fingerprint **[committed `9b941062`]**.

The carrier verdict rule is the discipline: a residual piece is a carrier candidate
**only if the real residual restores behavior better than a norm-matched shuffled
residual injected at the same site** (real < null on flips vs the bf16 reference), and
silicon-diff localizes the divergence onset at the claimed site. The whole loop runs as
one command on rented cloud GPUs (a committed one-command preset,
**[committed `9d4914ff`]**).

### 2.4 How the two axes compose

Their swap is our reinjection; their ablation is our deletion; their J-Lens is a
runtime-Jacobian lens where our microscope is a stored-precision lens; their "flexible vs
routine" split is the behavioral gate family our damage maps consume. The composition is
not a metaphor — it is an experiment (E1, §6): map the workspace band on an open model,
delete precision with int4, and ask whether workspace function is what breaks first, and
whether reinstating the *specific* residual at workspace-band sites (against its shuffle
null) is what restores it. If yes: the first weight-space localization of a global
workspace. If no: a null-gated negative — "workspace function survives int4 at this
scale" — which is publishable and constrains the object either way. The activation-space
half of that bridge is no longer hypothetical; it ran the day the paper landed (§3).

---

## 3. First result: the paper's dissociation, reproduced under a null it lacked (2026-07-06)

**[committed — instrument `8a1d0ed3`, verdict run `c80c6425`; artifacts: *the seven
dose-response JSONs*, PM-30..PM-36; headline PM-30]**

Within hours of reading the paper we built **workspace-map**: mean activation-difference
concept vectors (the paper's own Figure-88 corroboration method — deliberately, because it
is forward-only and cheap) extracted from a Spanish-vs-French contrast on qwen3-1.7b, then
injected device-side into a mid-layer band of the full-GPU decode chain, with three
readouts per arm: a **report** channel (the paper's question — "What language is the text
above written in?" — scored as log-odds between resolved answer-token sets), a
**continuation** channel (24 free-run tokens from the Spanish prompt, scored by lexical
language markers), and a **norm-matched shuffle-null arm** (a deterministic, seeded
permutation of the real injection vector per layer at the identical site; norm match
verified and recorded in the artifact — the identical discipline as residual-reinject).
The verdict rule was fixed before any run: a pre-registered report-shift support
threshold, a null-dominance ratio, and a continuation-degeneration detector (the exact
constants are recorded inside every artifact and hash-committed; PM-30..PM-36).

The dose–response, in full (band L8–11 of 28, swap Spanish→French; every row a committed
artifact):

| positions | α | report shift, real (nats) | report shift, null (nats) | continuation (real/null) | verdict |
| --- | --- | --- | --- | --- | --- |
| last | 0.0625 | +0.037 | +0.282 | Spanish / Spanish | no_report_flip |
| last | 0.125 | +0.109 | +0.565 | Spanish / Spanish | no_report_flip |
| last | 0.25 | +0.368 | +1.086 | Spanish / Spanish | no_report_flip |
| last | 0.5 | +1.400 | +1.748 | Spanish / Spanish | null_confounded |
| **all** | **0.25** | **+11.025** | **+1.064** | **Spanish / Spanish** | **workspace_dissociation** |
| all | 0.5 | +29.647 | +1.337 | French / Spanish | joint_flip |
| all | 1.0 | +28.09 | +1.71 | French / Spanish | joint_flip |

Three findings, in the order a skeptic should read them:

1. **The null caught a would-be false positive first.** Report-time-only injection
   (positions=last) *never* beats its shuffle-null: at every dose the random vector moves
   the report as much as or more than the real concept vector, and at α=0.5 the real
   shift (+1.400 nats, well above the pre-registered support threshold) is formally
   `null_confounded`. An un-nulled pipeline — including ours, had we built it without the
   gate — would have published those cells as successful report-steering. This is
   Nanda's "steering is just breaking the model" failure mode, caught *in vivo* by the
   exact control we argue for in §4.1.
2. **A genuine dissociation window exists.** Whole-context injection at α=0.25 moves the
   verbal report +11.0 nats toward "French" — **10.4x** the norm-matched null (+1.06),
   margin +9.96 nats — while the free-run continuation keeps writing Spanish in both arms
   (marker score 4:0 real, 3:0 null; no degeneration; baseline report log-odds −16.52
   reproduced end-to-end across binaries and model copies). Report channel moved,
   behavior channel intact, null quiet: the paper's central signature, on open weights,
   on a 1.7B model, under a control the original experiments did not carry.
3. **The window closes into honest joint steering.** At α=0.5 the report answer flips
   outright — and the continuation flips with it (coherent French). That is not a
   dissociation, and the instrument says so (`joint_flip`), exactly as a dose-response
   with a real boundary should behave.

Scope, stated plainly (the artifact carries these caveats verbatim): one model, one
concept pair, one report question with single-token answer sets, a lexical-marker proxy
for the continuation channel, mean-difference vectors from a small curated contrast — an
existence-level reproduction of the signature with a null, not a replication of the
paper's breadth. At the dissociation dose the report movement is a large log-odds shift,
not yet an argmax flip (that happens at α=0.5, where the continuation flips too). All raw
token streams are committed so every readout can be re-scored externally.

### 3.1 The J-Lens side of the bridge, oracle-grade **[committed `3503a160`; provenance artifact PM-41; readout recorded in this note, PM-23]**

To compare against the paper's estimator family (not just its activation-difference
corroboration method), we also built a torch-based J-Lens direction extractor, kept
strictly on the comparison-oracle side of our standing rule (external ML frameworks live
only in offline analysis scripts, never in the runtime; the native runtime consumes the
emitted pack as plain data). One construction note for exact comparability: our extractor
differentiates the output logits directly (d logit_v / d h_ℓ) — the composed form of the
paper's J_ℓ = ∂h_final/∂h_ℓ followed by its norm+unembed readout
lens(h) = softmax(W_U norm(J_ℓ h)); at the post-final-norm state the composed Jacobian
reduces to W_U exactly, which is precisely the bit-exact anchor we verify below. Its
proof run on qwen3-1.7b reproduces the paper's core observational phenomenon:
on a champagne-region prompt, the J-Lens readout makes " France" the top restricted token
at L19 and " Paris" top-1 from L21 through the output (peak at L25) **while the model's
actual next token is " the"** — content poised for report, not being reported. The chain
is anchored analytically: all 80 final-layer direction rows equal the tied unembedding
rows **bit-exactly (max |diff| = 0.0)**, proving the VJP → slice → average → serialize
path exact. Binding, stated precisely: the readout numbers and the anchor statement in
this subsection are recorded here, in the hash-committed note (PM-23); the PM-41
artifact is the extraction's provenance manifest — method parameters, per-model-file
sha256, emitted-pack sha256, official safetensors-parser verification — and does not
itself contain the readout table; the bit-exact final-layer anchor is independently
recomputable by any holder of the sha-pinned pack plus the sha-pinned model files. This
gives E1 both lenses: the cheap forward-only mapper (§3) and an exact-comparability
J-Lens pack.

### 3.2 Scale: the window migrates, the null floor drops (qwen3-8b, 2026-07-07) **[committed `74751075`; artifacts: the qwen3-8b 9-cell grid, PM-47..PM-56 — run on a rented high-memory GPU instance, cuda fp32]**

One day after the 1.7B result, the same instrument, pack-extraction recipe, and
pre-registered verdict rule ran unchanged on qwen3-8b (36 layers, d_model 4096 — 2x the
1.7B width). Three findings, each read directly from the committed per-band verdicts:

1. **The dissociation exists at both scales — and is *broader* at 8B.** At the 1.7B
   headline configuration (whole-context, α=0.25), 8B passes the gate in **five
   contiguous bands** (L4-7 through L20-23: real +1.43 to +6.71 nats vs null −0.07 to
   +1.16, continuation intact in every one), where 1.7B had exactly one passing band
   (L8-11). Late bands (L24+) joint-flip at this dose, honestly labeled.
2. **The window's geometry migrates.** The report-time-only protocol (positions=last) —
   which at 1.7B *never* beat its null at any dose (§3, the confound the gate caught) —
   **passes at 8B**: at α=1.0, L4-7 / L8-11 / L16-19 dissociate (real +1.52 / +1.92 /
   +2.11 vs null +0.75 / +0.06 / +0.30); at α=2.0, L0-3 / L4-7. The gate keeps biting at
   8B too: L12-15 at last/α=1.0 is `null_confounded`, and late bands at high dose end in
   `degenerate_continuation` — reported as such, not as steering. The best-dissociation
   cells also sit deeper in the network (depth-fraction ~0.5–0.6 at 8B vs 0.34 at 1.7B;
   *the feature-resolution scaling note* **[committed `9ac04db4`; PM-45]**).
3. **The one matching-free scale signal: the null floor drops faster than geometry.** At
   the matched dose with full multi-band coverage at both scales (α=1.0, whole-context),
   the median norm-matched-null report shift falls from **4.58 to 1.18 nats (÷3.9)**
   while the real shift stays the same order — against a pure random-superposition
   (sqrt-d) prediction of ÷1.41 for this width change. Even deep in the steering regime
   the 8B null stays quiet (mid-band L23-26 at α=0.5: real +22.63 vs null +0.19 — a
   `joint_flip`, cited only as null-floor evidence, not as a dissociation). We
   deliberately quote **no scaling exponent**: the companion analysis note shows the
   implied exponent is matching-choice-dependent — its *sign flips* between defensible
   band matchings — so the absolute null-floor drop is the only reading we consider
   robust, and even it carries a stated caveat (absolute nats are not strictly
   comparable across d_model without an activation-norm normalizer; two scale points fix
   a line, not a law).

Instrumentation for turning these single points into distributions is in place: a
K-null ensemble mode (error bars on every null floor) and a single-position probe mode
of the mapper **[committed `b3a6882e`]**; the first ensembles are in flight
**[planned]**. *(Completed since private v0.4 and recorded in this repository's results
ledger: the K=4 null ensemble on the flagship 1.7B cell and the 20-cell single-position
sweep — RESULTS.md §8–§9, PM-60..PM-67.)* Scope: same single concept pair and report
question as §3, two scale points, one architecture family — an existence-and-geometry
result, not a law.

---

## 4. Metrology, aimed at the stated weaknesses

Our contention in one sentence: **the field's bottleneck on causal claims is not
imagination, it is metrology** — controls, receipts, and preregistration strong enough
that a causal claim survives a hostile reader. Taking the commentary's weaknesses one at
a time:

### 4.1 "Steering is just breaking the model"

An intervention that changes behavior proves only that you perturbed *something* the
behavior depends on. The claim "this specific content moved" needs a matched control that
destroys the same amount of structure without the content. Our standing answer is the
**norm-matched shuffle-null**: every injection is paired with a shuffled vector of
identical norm and shape at the identical site (deterministic seeding), and a claim
requires beating it **[committed `8821ffd6`, `8a1d0ed3`]**. The Phase-3 design adds
stratum-matched random-carrier nulls, sham states, and a planted-necessity positive
control **[preregistered `4980cfb2`; PM-17]**.

As of this week the gate is demonstrated in *both* directions on the workspace question
itself **[committed `c80c6425`]**: it **passed** a true positive (the §3 dissociation:
real 10.4x null, continuation intact) and it **rejected** a confounded variant the same
day (every report-time-only cell: null ≥ real). A control that only ever rejects could be
insensitivity wearing a lab coat; a control that only ever passes is not a control. This
one has now done both, on the paper's own experimental object. E4 (§6) extends the offer:
the same nulls, run over the paper's remaining causal claims, published per-claim.

### 4.2 Single-token vocabulary bias

Nanda notes that "needing to have concepts correspond to single tokens seems fairly
restrictive" (Nanda commentary). Two of our design choices avoid vocabulary readout
entirely, and one inherits the limitation honestly. The Phase-3 headline signal is a
**router flip — a categorical routing event, not a token probability**
**[preregistered `4980cfb2`; feasibility committed, §5]**; OLMoE router instrumentation
is mature in our runtime (per-token expert traces; empirical-vs-analytic route agreement
3–19x above chance, our route-crossval instrument **[committed; recorded 2026-06-09 in
*the stack ground-truth document*, repo-HEAD-bound]**). Where output distributions are
the measure, our preregistered distance is a full-vocab Jensen–Shannon divergence with a
top-k-reordering companion gate — a tail-only JS bump with no top-k disturbance is
explicitly *not* admissible as an effect. And behavioral gates are read on full decoded
text under free-run and teacher-forcing (our teacher-forced decode and decode-parity
instruments **[committed `88ba49ea`, `6f2771c3`]**), a habit that has already caught one
of our own false positives (§4.5). The honest exception: the §3 *report* channel scores
single-token answer sets (the paper's own readout style) — its continuation channel and
the committed raw token streams are the mitigation, and multi-token report scoring is on
the E1 list.

### 4.3 Discovery is a multiple-comparisons machine

Any search over (sites × states × interventions) will eventually "find" something. The
Phase-3 answer is structural: frozen budgets, FDR over the whole search tree,
mechanically constructed state sets, DEV-split discovery with EVAL-split re-confirmation
at the frozen physical address, and a hash-committed numeric freeze so no threshold can
drift after seeing an effect **[preregistered `4980cfb2`, `aca08a52`; PM-17, PM-18]**.
The same habit, scaled down, is visible in §3: the verdict rule (support threshold, null
ratio, degeneration detector) was fixed before any run and is recorded inside every
artifact next to the raw numbers. We would like to see activation-space steering results
adopt the same three commitments: freeze the readout before the sweep, correct across the
sweep, re-confirm on held-out states.

### 4.4 "We recommend sanity checking" (the coding-agent problem)

Nanda's replication note observes that "a coding agent given the paper did it pretty
well, though we recommend sanity checking" ("Cost and Difficulty of Replicating
J-Lens"). The advice points at a real, growing failure mode: results mediated by large
stacks — and increasingly by agents driving them — need *receipts*, not trust. Our
stack's answer is architectural. The runtime is a self-contained runtime with a
hand-written GPU backend and zero third-party ML dependencies on the product path — no
torch, no vendor inference framework anywhere in the loop **[committed; *stack
ground-truth document*, repo-HEAD-bound]**. Greedy CUDA decode is now verified
**bitwise-deterministic across runs**: a standing regression test decodes three times on
the same device and asserts identical per-step top-8 logit streams (fnv1a64
`445f710a693a80c9`, 8 tokens, qwen3-1.7b), green in the Wave-0 integration gate
**[committed — test `76ff3b6e`, gate artifact PM-42 at `c74ccfea`; exclusive-device
condition recorded at `734d77df`]**. The §3 experiment carries its own determinism
block: baseline re-execution bitwise-identical, armed injection provably changes the
forward, disarmed state bitwise-identical again — scoped honestly to "this binary, this
machine, this backend." Correctness anchors are external where it counts: the ZAYA
forward is HF-reconciled at 2 tokens **[committed `e42a0d30`]** on a full-GPU per-layer
token-state path **[committed `faf7cf23`]**, the J-Lens oracle pack is anchored
bit-exactly to the tied unembedding (§3.1), and external ML frameworks are used *only*
as offline comparison oracles, never as the runtime. Every generated token can carry a
per-op checksum receipt (silicon-trace) diffable across packs (silicon-diff)
**[committed `6d0c3744`, `59a95d6b`]** — when two runs disagree, we can say at which
operation, on which tensor, they began to disagree. A carrier claim ships as a
proof-carrying pack binding bytes → gates → verdict **[committed `9b941062`]**. This is
what we mean by *receipts-grade* interpretability: the experiment's own execution is an
auditable object.

### 4.5 The negatives that show the gates bite

Discipline claims are cheap; here is ours spending real money to say "no." Our first
full weight-residual carrier hunt — gemma-4-E2B, OCR grounding, int4 deletion across the
text-decoder down-projections, the KV-producer attention layers, and the vision tower,
across three int4 tiers — returned **NO carrier**: the model reads the probe text
identically whether the reinjected residual is real or a norm-matched shuffle;
real-vs-null flip differences were ±1 with a sign that flipped between sites (2<3, 3<4,
4>3) — the definition of noise, and the null gate refused it **[committed; verdict at
`aeba806b`, *the microscopy program note*, PM-20]**. The same arc caught two would-be
false positives before they became claims: a grounding "signal" that was an artifact of
reading only the first output line, and a "fidelity hint" that reversed sign under site
change. An earlier end-to-end CUDA run on qwen3-0.6b was likewise refused (real 4/16 ≥
null 3/16 → not a carrier) while validating that silicon-diff localizes divergence onset
at the patch site. And the newest instrument continued the pattern in its first week:
the workspace-map null rejected the entire report-time-only arm of §3 as confounded
before admitting the whole-context dissociation. We report these because a methodology
whose controls have never rejected anything is advertising, not metrology. The honest
current score: weight-residual carriers found: zero; activation-space dissociations
found: one, null-gated, existence-level (§3).

---

## 5. Ignition: the missing experiment — precondition now passed, evaluation pending

In the commentary, Dehaene and Naccache are explicit: "**Ignition remains to be fully
demonstrated.** The J-space is shown to be limited in capacity, but the paper does not
establish the nonlinear, competitive, all-or-none entry into the workspace which,
according to GNW and several experiments, is a reliable signature of conscious access in
human and animal brains." They also specify the decisive experiment: "present a stimulus
at graded strengths … and ask whether J-space representations switch on with a
threshold-like nonlinearity … Better still, present stimuli exactly at threshold and
look for a bifurcation across runs, resulting in a bimodal distribution of J-space
activation" (Dehaene–Naccache commentary, "many differences are notable"). In fairness —
and the commentary itself notes this — the paper already points in this direction: its
section "Interpretation of ambiguous inputs solidifies at the workspace onset"
(Figure 29) runs "an experiment that provides the model with artificially ambiguous
input" and finds that later-layer J-space "quickly transitions to an all-or-none
representation of one of the possibilities" (commentary's wording), and hold-in-mind
dual-tasking degrades performance moderately (commentary, citing the paper's appendix
A.17). Dehaene's verdict stands: suggestive, not yet the demonstration.

We want to point out that this experiment has a natural, categorical, threshold-free
instantiation that has been sitting preregistered in our repository since June: the
**near-margin route flip at an MoE routing boundary**. A router's top-k selection *is* an
all-or-none commitment: a perturbation either crosses the margin `m = r_rank8 − r_rank9`
and discretely changes which experts execute — with downstream KV and trajectory
consequences — or it does not, and the bimodality is structural rather than fitted. The
Phase-3 design's state-dependence test is exactly the ignition contrast: the *same*
frozen physical carrier must flip the route in near-margin states and do nothing in
margin-safe states (F1), with margins computed before any perturbation, states drawn
mechanically, and the whole thing FDR-disciplined **[preregistered `4980cfb2`,
`aca08a52`; PM-17, PM-18]**.

**Status update (2026-07-06/07): the design's hard fail-closed precondition has now
PASSED on the real substrate.** The OLMoE M3-feasibility gate on OLMoE-1B-7B (weights
pinned to the HF revision and sha256-verified against the LFS manifest, PM-40) returned
`verdict: FEASIBLE` with zero demote reasons: the 3-shard index loads (3219 tensors); the
forward is token-correct on the anchor prompt; 384/384 routing records carry selected
expert ids plus raw-softmax router weights; and the categorical route-flip signal
`1[e ≠ e']` is *observable on all 16 MoE layers*, with within-top-k margins captured
(example: 3.386e-3) **[committed — evidence pack PM-37]**. A solo re-run under an
exclusive-GPU lock reproduced the entire evidence JSON **bit-identically** (zero
differing bytes — every margin, expert id, and probe value exact; PM-38 carries the same
sha256 as PM-37 in the public manifest) **[committed `47e37047`]**. What remains before
the confirmatory evaluation, stated exactly: science-lead sign-off on the numeric
freeze; the null-calibration run that sets the test's tau and margins (with its global
stability precondition); reconciliation of two freeze-vs-source constants (amendment
A10, PM-19); and one known DEV finding recorded in-tree (layer-0 route-flips sit at the
noise floor — the cross-layer hunt is the free-to-fail path). `SUPPORTED` is one of a
fail-closed verdict vocabulary, and we will report whichever verdict the gates return.

The claim boundary matters, so we state it twice. Structurally, a route commitment and
workspace entry are the same *class* of object: a discrete, state-conditioned,
all-or-none transition at a boundary, with persistent downstream consequences. We do
**not** claim a router flip *is* workspace ignition — a hard top-k is a step function by
construction, so its discreteness alone is trivial; the non-trivial, ignition-shaped
content of E3 is elsewhere: whether a frozen carrier's causal effect switches
categorically with pre-computed margin distance (necessity that is state-dependent, not
merely an argmax discontinuity), and whether near-margin flip events couple to the
workspace band (do they gate what becomes reportable?) — the junction E1 and E3 are
designed to probe **[planned]**. What we offer today: a preregistered, numerically
frozen, fail-closed design for measuring all-or-none commitment causally at a boundary,
on open weights, that anyone can audit — now with its feasibility precondition passed and
bit-identically reproduced.

---

## 6. What we are running next (preview, dated 2026-07-07)

Components are tagged individually; everything untagged is **[planned]**. These are
previews, not promises of results; the only thing we commit to is publishing whatever the
gates return, including negatives, with receipts. The coordinating plan is *the
workspace-carrier response plan* **[committed `042c4eee`; PM-22]**.

- **E1 — Workspace × quantization (the bridge).** The activation-space half now exists:
  the null-gated mapper with a validated dissociation configuration (band L8–11, swap
  mode, α=0.25, whole-context, ≥24 continuation tokens) **[committed `c80c6425`]**, a
  flexible-vs-routine behavioral gate suite (workspace-gates
  **[committed `69bfeb0b`]**), and an exact J-Lens oracle pack for comparability
  (§3.1 **[committed `3503a160`; PM-41]**). The int4 tier sweep has now also landed: on
  qwen3-1.7b, the finest production-representative int4 tier (grouping parameters
  hash-committed) **selectively breaks flexible tasks** — 9 bf16-correct flexible
  behaviors flip (suppression 4/6, trace-gap 4/5, two-hop 1/5) while routine stays 8/8;
  coarser tiers damage non-selectively, and per-item damage is non-monotone across tiers
  (different deletion maps, not nested) **[committed `859b4077`; PM-25..PM-29]** —
  exactly the fragile substrate the bridge needs. What remains IN FLIGHT:
  band-restricted residual reinjection, real vs shuffle-null, with silicon-diff
  localization and a proof-pack verdict (Stage C). A first reading exists but is
  **PRELIMINARY** and we flag it exactly as the results ledger does: the dissociation
  configuration still separates from its null on the int4 tier (real-minus-null +8.07
  nats vs +9.96 on bf16) — "single configuration, single model, artifact not yet merged
  to private main at manifest time … Do not cite as a confirmed result" (RESULTS.md §6).
  Either final outcome is a result: fragile-and-localized (first weight-space
  localization of a workspace) or robust (a null-gated "workspace function survives
  int4 at 1–2B scale").
- **E2 — Does a workspace exist without attention?** The same forward-only mapper across
  non-transformer recurrences on the same runtime. The substrate is unusual and already
  exists: our decoder runs 17+ architecture families through one loop
  **[committed; *repository index*, repo-HEAD-bound]**, including token-exact
  non-transformer forwards — Mamba2 **[committed `951b3cb1`]**, RWKV-7
  **[committed `2d157e7e`]**, xLSTM **[committed `9931fcad`]**, GLA
  **[committed `7ee4c1b1`]**, RetNet **[committed `32533431`]**. The recurrence question
  is raised in the commentary; on one universal runtime it is cheap to ask, and any
  answer is novel.
- **E3 — The ignition run.** Feasibility PASSED and bit-identically reproduced (§5
  **[committed `47e37047`]**); the frozen Phase-3 evaluation runs after sign-off and
  null-calibration, written up in workspace vocabulary: bimodal route commitment at
  boundary states, state-dependent carriers, fail-closed verdicts.
- **E4 — Receipts-grade replication of the paper's core causal claims.** The first item
  landed with the paper still on the front page: swap-moves-reports / continuation-spared,
  null-gated, §3 **[committed `c80c6425`]**. Remaining: the flexible-vs-routine ablation
  asymmetry under the same nulls, more concept pairs and models, and packaging as a
  one-command cloud preset (extending the committed preset **[committed `9d4914ff`]**),
  publishing per-claim verified / not-reproduced-with-receipts.

---

## 7. Scope, non-claims, and the claim ledger

### 7.1 What we are not claiming

We deliberately confine this note and the program it describes to **causal-carrier
metrology** — which stored distinctions are necessary for which behaviors, in which
states, under which controls — and we take no position here on the consciousness framing
that surrounds the workspace result; nothing in our instrumentation measures, or could
measure, anything about experience. Further honest boundaries, explicitly:

- **No weight-space carrier has been found to date.** The microscopy hunts returned
  null-gated negatives (§4.5). The §3 dissociation is an *activation-space* result — the
  bridge from the workspace band to specific weight-space carriers (E1's second half) has
  not run.
- **The §3 dissociation is existence-level, not breadth.** One model (qwen3-1.7b), one
  concept pair (Spanish/French), one report question with single-token answer sets, a
  lexical-marker continuation proxy; at the dissociation dose the report shift is a
  10.4x-null log-odds movement, not an argmax flip (the argmax flip arrives at α=0.5
  together with continuation steering — `joint_flip`, honestly labeled). Raw token
  streams are committed for external re-scoring.
- **Phase 3 has not run its confirmatory evaluation.** Feasibility PASSED (§5); sign-off,
  null-calibration, and two freeze-vs-source reconciliations remain; `SUPPORTED` is one
  of a fail-closed verdict vocabulary.
- **The scale result (§3.2) is two points, not a law.** Same single concept pair and
  report question at both scales; the window migration is a descriptive geometry
  observation; the feature-resolution exponent is matching-choice-dependent (its sign
  flips between defensible matchings), which is why we quote only the absolute
  null-floor drop, itself pending the activation-norm normalizer and K-null ensembles.
  The int4-window +8.07 reading is PRELIMINARY (Stage-C artifact not yet on main) and is
  not citable as a confirmed result.
- **Scale risk.** The paper's phenomenology is frontier-scale ("By default, we report
  results on Claude Sonnet 4.5, but we corroborate key results on Haiku 4.5 and Opus 4.5
  as well" — paper); the 27B replication already required care. Our substrates are
  0.6–7B. The §3 window exists at 1.7B, but band sharpness and capacity claims at
  frontier scale are not ours to make — and a small-scale negative on any E1–E4
  component would not falsify the paper's frontier-scale claim, and will not be
  presented as if it did.
- **Runtime claim boundaries.** HF token-exact reconciliation is committed at 2 tokens on
  ZAYA-8B; the other architectures are validated by native known-correct completions,
  determinism, and CPU↔CUDA parity, not per-layer HF parity (*stack ground-truth
  document*, repo-HEAD-bound). CUDA bitwise determinism is claimed per test scope: same
  binary, same device, exclusive access, greedy decode.

### 7.2 Claim ledger

| Claim | Tag | Evidence (private commits; manifest) |
| --- | --- | --- |
| State-dependent weight-carrier thesis formalized 2026-06-28 | committed | `5223bc69`, `74c056ba`; PM-16 |
| Phase-3 fail-closed design (route-flip, firewall, FDR, controls) | preregistered | `4980cfb2`; PM-17 |
| Phase-3 numeric freeze, hash-committed, DEV-only | preregistered | `aca08a52`; PM-18 (amendment A10: `23b9226d`; PM-19) |
| Phase-3 apparatus implemented (incl. OLMoE feasibility gate) | committed | repo-HEAD-bound (module set private) |
| Phase-3 M3-feasibility: FEASIBLE on OLMoE; route-flip observable on all 16 MoE layers; weights pinned + sha-verified | committed | `d43e85b2`; PM-37, PM-40 |
| M3-feasibility solo re-run reproduces evidence JSON bit-identically | committed | `47e37047`; PM-38, PM-39 (PM-38 sha256 = PM-37 sha256) |
| Phase-3 confirmatory evaluation verdict | none — not run | — |
| Five-tool deletion-microscopy chain | committed | `f74586c7`, `8821ffd6`, `6d0c3744`, `59a95d6b`, `9b941062`; PM-20 |
| One-command cloud preset for the full loop | committed | `9d4914ff` |
| gemma-4-E2B is int4-robust for OCR; no carrier; null gate refused false positives | committed | `aeba806b`; PM-20 |
| qwen3-0.6b e2e run refused (real 4/16 ≥ null 3/16); silicon-diff onset at patch site | committed | PM-20 |
| workspace-map: null-gated dissociation mapper, device-side injection on the full-GPU chain | committed | `8a1d0ed3` |
| Workspace dissociation on qwen3-1.7b: report +11.03 nats real vs +1.06 null (10.4x), continuation intact both arms | committed | `c80c6425`; PM-30 |
| Report-time-only injection is null-confounded at every dose (the un-nulled false positive) | committed | PM-32..PM-35 |
| Dose window closes into joint steering at α≥0.5 (report + continuation flip together) | committed | PM-31, PM-36 |
| qwen3-8b 9-cell grid: dissociation at both scales — 5 contiguous passing bands at all/α0.25; the last-position protocol (null-confounded at 1.7B) passes at α1.0–2.0; late bands degenerate, labeled | committed | `74751075`; PM-47..PM-56 |
| Null floor drops ÷3.9 (median \|Δreport_null\|, α1.0/all, 1.7B→8B) vs geometric ÷1.41; implied exponent is matching-dependent (sign flips) — only the absolute drop is quoted, with normalizer caveat | committed (analysis over committed artifacts) | `9ac04db4`; PM-45, PM-46 |
| K-null ensemble mode + single-position probe mode of the mapper | committed (instrument; flagship K=4 ensemble and position sweep since completed — RESULTS.md §8–§9) | `b3a6882e`; PM-60..PM-67 |
| Finest production-representative int4 tier selectively breaks flexible tasks on qwen3-1.7b (9 bf16-correct flips; routine 8/8); tiers are non-nested deletion maps | committed | `859b4077`; PM-25..PM-29 |
| This public prior repository: public note edition, RESULTS.md, TIMELINE.md, sha256 priority manifest (adversarial IP audit; PM-01..42 + Update 2026-07-07 (2), PM-43..67) | committed (this repository; verified live 2026-07-07) | this repository |
| E1 Stage-C band-restricted reinjection; int4-window real-minus-null +8.07 nats | IN FLIGHT — PRELIMINARY; artifact not on main; "do not cite as a confirmed result" | RESULTS.md §6 |
| Flexible-vs-routine behavioral gate suite (workspace-gates) | committed | `69bfeb0b` |
| J-Lens oracle extractor + qwen3-1.7b proof pack: France@L19 / Paris@L21+ while actual next token is " the"; final-layer rows bit-exact vs tied unembedding (max diff 0.0) | committed | `3503a160`; PM-41 (extraction provenance), PM-23 (readout record); anchor recomputable from the sha-pinned pack + model files |
| CUDA greedy decode bitwise-deterministic across 3 runs (top-8 logit stream fnv1a64 `445f710a693a80c9`) | committed | `76ff3b6e`, `c74ccfea`; PM-42 |
| Self-contained runtime; hand-written GPU backend; zero third-party ML deps on the product path | committed | repo-HEAD-bound |
| Full-GPU per-layer token-state decode; ZAYA 2-token HF-reconciled | committed | `faf7cf23`, `e42a0d30` |
| Decode-parity + teacher-forced damage map | committed | `6f2771c3`, `88ba49ea` |
| Token-exact non-transformer forwards (Mamba2/RWKV-7/xLSTM/GLA/RetNet) | committed | `951b3cb1`, `2d157e7e`, `9931fcad`, `7ee4c1b1`, `32533431` |
| OLMoE router instrumentation; route agreement 3–19x above chance | committed | repo-HEAD-bound (recorded 2026-06-09) |
| No finite-value clamps in the math chain (guarded by regression tests on both GPU runtimes) | committed | `98eca5c6`, `b35aa7ce`, `1370fcbd` |
| Int4 fragility damage map: finest tier selectively breaks flexible behaviors (9 flips), routine intact | committed | `859b4077`; PM-25..PM-29 (see RESULTS.md §2) |
| E1 Stage-C verdict, K-null ensembles at 8B, third scale point, E2, E3 evaluation, E4 remaining claims | planned | PM-22 |
| Workspace-band × residual-carrier bridge verdict | none — not run | — |

---

## References and pointers

- Gurnee, Sofroniew, et al. (Lindsey senior), "Verbalizable Representations Form a
  Global Workspace in Language Models," Anthropic, July 6, 2026.
  transformer-circuits.pub/2026/workspace — paper quotations verified against the
  published page 2026-07-07 (main body; the appendix region truncates in programmatic
  fetches, so appendix numbering — Figure 88, A.17 — is cited via the commentary).
- Commentary pack (Dehaene & Naccache; Eleos AI; N. Nanda) — commentary quotations are
  anchored by author and quoted text; verified against the full extracted PDF text
  2026-07-07:
  https://www-cdn.anthropic.com/files/4zrzovbb/website/cc4be2488d65e54a6ed06492f8968398ddc18ebe.pdf
- **This repository is the public prior record (cite this externally):**
  https://github.com/XNN-LLC/xnn-research — this public note edition, the results
  ledger ([`RESULTS.md`](RESULTS.md)), the genesis timeline
  ([`TIMELINE.md`](TIMELINE.md)), and the sha256 priority manifest
  ([`PRIORITY_MANIFEST.md`](PRIORITY_MANIFEST.md) / `priority_manifest.json`;
  PM-01..PM-42 + Update 2026-07-07 (2), PM-43..PM-67). Published 2026-07-07 after an
  adversarial IP audit.
- Working repository: github.com/XNN-LLC/xnn-see-research — **private**;¹ every
  document and artifact cited above is hash-committed in the manifest:
  - Theory: *carrier-mapping theory document* (PM-16)
  - Frozen design: *Phase-3 preregistration* (PM-17), *numeric freeze* (PM-18),
    *amendment A10* (PM-19)
  - Instrument line + negatives: *microscopy program note* (PM-20)
  - First results (this note §3, §3.2, §5): *dose-response artifacts* (PM-30..PM-36),
    *the qwen3-8b grid* (PM-47..PM-56), *J-Lens proof packs* (PM-41, PM-57),
    *feasibility evidence* (PM-37..PM-40), *integration gate* (PM-42),
    *null-ensemble and position-sweep artifacts* (PM-60..PM-67)
  - Scale analysis: *feature-resolution scaling note* (PM-45, PM-46)
  - Position note v0.4 (the private original of this edition): PM-43
  - Response plan (E1–E4): PM-22

*Contact: open an issue on this repository. This note is a public edition of a working
draft; corrections that make any claim here smaller and truer are the most useful kind.*
