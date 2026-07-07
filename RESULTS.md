# RESULTS — the numbers, with dates, commits, and manifest bindings

Every table below is read from committed run artifacts in the private
repository — with one labeled exception: the §5 J-Lens readout numbers are
recorded in the hash-committed position note (PM-23) rather than inside the
PM-41 artifact, which is the extraction's provenance manifest; §5 states the
binding exactly. Each artifact's content sha256 is committed in
`PRIORITY_MANIFEST.md` (PM-xx), so any later disclosure is verifiable
byte-for-byte. Verdict labels are produced by pre-registered rules; the rules'
exact thresholds are themselves hash-committed (inside the artifacts and the
frozen designs) and are not printed here. Alpha (α) values, layer bands, and
counts are experiment coordinates — results, not engineering internals.

---

## 1. Workspace dissociation dose-response (qwen3-1.7b, Spanish→French)

**Date 2026-07-06 · private commit `c80c6425` · manifest PM-30..PM-36.**
Mean activation-difference concept vectors injected device-side into a
mid-layer band (L8–11 of 28) on the full-GPU decode chain. Three readouts per
arm: report channel (log-odds between resolved answer-token sets), free-run
continuation channel (24 tokens, lexical language markers), and a norm-matched
shuffle-null arm (deterministically seeded permutation of the real vector,
same site, same norm). Baseline report log-odds −16.52, reproduced end-to-end
across binaries and model copies.

| positions | α | report shift, real (nats) | report shift, null (nats) | continuation (real/null) | verdict |
| --- | --- | --- | --- | --- | --- |
| last | 0.0625 | +0.037 | +0.282 | Spanish / Spanish | no_report_flip |
| last | 0.125 | +0.109 | +0.565 | Spanish / Spanish | no_report_flip |
| last | 0.25 | +0.368 | +1.086 | Spanish / Spanish | no_report_flip |
| last | 0.5 | +1.400 | +1.748 | Spanish / Spanish | null_confounded |
| **all** | **0.25** | **+11.025** | **+1.064** | **Spanish / Spanish** | **workspace_dissociation** |
| all | 0.5 | +29.647 | +1.337 | French / Spanish | joint_flip |
| all | 1.0 | +28.09 | +1.71 | French / Spanish | joint_flip |

Three readings, in the order a skeptic should take them: (1) every
report-time-only cell fails its null — the exact "steering is just breaking
the model" confound, caught by the gate an un-nulled pipeline lacks; (2) the
α=0.25 whole-context window is a genuine dissociation — report moves 10.4x its
null (margin +9.96 nats) while the continuation keeps writing the source
language in both arms; (3) at α≥0.5 the window closes into honest joint
steering, labeled as such. Scope: one model, one concept pair, one report
question with single-token answer sets, lexical-marker continuation proxy —
existence-level, with all raw token streams committed for external re-scoring.
*(2026-07-07 update: the flagship α=0.25 cell is now gated by a K=4 null
ensemble — §8 — and position-resolved to a single consolidation site — §9.)*

---

## 2. Int4 fragility tier table (qwen3-1.7b, W4 damage map)

**Date 2026-07-07 · private commit `859b4077` · manifest PM-25..PM-29.**
A 44-item behavioral battery in 4 families mapped to the workspace paper's
flexible-vs-routine paradigms (prompts private; battery hash-committed,
PM-26). Survivor discipline: an item counts only if bf16 passes it; pass rates
are over bf16-survivors. Greedy decode; paradigm-level graders. Tiers are
int4 grouped-quantization variants (exact grouping parameters hash-committed);
"asym fine-group" is the finest, production-representative tier. All runs
under an exclusive-GPU lock.

| family | bf16 | int4 asym fine-group | int4 sym fine-group | int4 sym per-tensor |
| --- | --- | --- | --- | --- |
| routine | 8/8 | **8/8** | 7/8 | 0/8 (gibberish) |
| suppression | 6/12 | **2/6** | 2/5 | 0/5 (gibberish) |
| trace-gap | 7/9 | **3/7** | 2/2 | 0/2 (gibberish) |
| two-hop | 5/15 | **4/5** | 5/5 | 0/3 (gibberish) |

(The sym-fine-group / per-tensor columns are a 17-item focus subset; a
coarser-grouped column exists in the private appendix, hash-committed.)

**Verdict:** the finest int4 tier selectively breaks bf16-correct FLEXIBLE
behaviors while leaving routine continuation 100% intact (8/8). **The nine
lock-held flips:**

| item | behavior (one line) |
| --- | --- |
| S03 | avoid-naming: bf16 withholds the forbidden word; int4 names it ("the domestic cat") |
| S04 | avoid-naming: bf16 answers "white"; int4 violates via "a pale blue" |
| S06 | avoid-naming: bf16 withholds; int4 blurts the forbidden '"honey"' |
| S12 | avoid-naming: constraint violated downstream of the answer ("heart") |
| G02 | trace-gap: held cue word recalled by bf16 across distractor sentences; int4 loses it |
| G03 | trace-gap: as G02 (held word lost exactly when distractors intervene) |
| G05 | trace-gap: as G02, longer gap |
| G06 | trace-gap: as G02, longer gap |
| H15 | two-hop: bf16 answers " Pound sterling"; int4 degrades to echoing the question |

Signature detail: both gap-0 recall items HOLD while gap-8/16 items die — the
distractor-bridging signature, not generic recall loss. Tier-ladder shape:
asym fine-group = selective flexible-only damage; sym fine-group = flexible
damage plus the first routine crack (a repetition item degenerates); sym
per-tensor = total collapse (0/18 incl. routine) — the non-selective endpoint.
Per-item damage is NOT monotone across tiers: the tiers are different deletion
maps `R`, not nested ones — exactly the object residual-reinjection dissects
per site. Claim boundary: this is a *damage map*, not a carrier claim; WHERE
the causal residual lives is the reinjection question (real-vs-null per site)
— answered at first order in §6.2: an honest negative; the deletion is
diffuse at the tested sites.

---

## 3. Ignition-design feasibility gate (OLMoE-1B-7B) — FEASIBLE, bit-identical

**Date 2026-07-06 (solo re-run 2026-07-07Z) · private commits `d43e85b2`,
`47e37047` · manifest PM-37..PM-40.**
The hard fail-closed precondition of the June-preregistered near-margin
route-flip evaluation (PM-17, PM-18), on the real substrate, GPU decode chain:

| criterion | result |
| --- | --- |
| Model index + shards load (public OLMoE-1B-7B, weights pinned to the HF revision, sha256-verified against the LFS manifest) | 3/3 shards, 3219 weight-map entries |
| Forward token-correct on the anchor prompt | PASS (" Paris") |
| Routing records carry selected expert ids + raw-softmax router weights | 384/384 records |
| Categorical route-flip signal `1[e ≠ e']` observable | **all 16 MoE layers**, within-top-k margins captured (example 3.386e-3) |
| Verdict | **FEASIBLE**, zero demote reasons |
| Solo re-run under an exclusive-GPU lock | **bit-identical** — zero differing bytes; PM-37 and PM-38 carry the SAME sha256 in the public manifest |

What remains before the confirmatory evaluation (stated exactly): science-lead
sign-off on the numeric freeze; the null-calibration run (with its global
stability precondition); reconciliation of two freeze-vs-source constants
(amendment A10, PM-19); one recorded DEV finding (layer-0 route-flips sit at
the noise floor). `SUPPORTED` is one of a fail-closed verdict vocabulary.

---

## 4. Determinism anchor (CUDA greedy decode)

**Date 2026-07-06 · private commits `76ff3b6e`, `c74ccfea` · manifest PM-42.**
Standing regression: three decodes on the same device under one exclusive
hold, asserting identical per-step top-8 logit streams. Result: 3 runs bitwise
identical, 8 generated tokens (qwen3-1.7b), per-step top-8 logit stream
fnv1a64 **`445f710a693a80c9`**. Scope claimed honestly: same binary, same
device, exclusive access, greedy decode. The dissociation experiment (§1)
additionally carries its own determinism block: baseline re-execution
bitwise-identical; armed injection provably changes the forward; disarmed
state bitwise-identical again.

---

## 5. J-Lens comparison-oracle readout (qwen3-1.7b)

**Date 2026-07-06/07 · private commit `3503a160` · manifest PM-41
(extraction provenance) + PM-23 (readout record).**
A torch-based J-Lens direction extractor, kept strictly on the
comparison-oracle side of our standing rule (no torch anywhere in the
runtime; the native runtime consumes the emitted pack as plain data),
reproduces the paper's core observational phenomenon on open weights: on a
champagne-region prompt, the lens readout makes " France" the top restricted
token at L19 and " Paris" top-1 from L21 through the output (peak L25) **while
the model's actual next token is " the"** — content poised for report, not
being reported. Anchor: all 80 final-layer direction rows equal the tied
unembedding rows **bit-exactly (max |diff| = 0.0)**, proving the
extract→slice→average→serialize path exact.

Binding, stated precisely: the readout numbers and the anchor statement above
are recorded in the hash-committed position note (PM-23). The PM-41 artifact
is the extraction's provenance manifest — method parameters, per-model-file
sha256, emitted-pack sha256, official-parser verification — and does not
itself contain the readout table. The bit-exact final-layer anchor is
independently **recomputable** by any holder of the sha-pinned direction pack
plus the sha-pinned model files.

---

## 6. E1 resolved: the int4 window is committed, and the reinjection verdict is an honest negative

*(This section previously carried a PRELIMINARY +8.07 readout with a promise
to hash-commit the artifact in a dated manifest update. That promise is now
kept: the artifacts are committed and bound in manifest Update 2026-07-07 (3).)*

### 6.1 The int4 window, committed (E1 Stages A+B)

**Date 2026-07-07 · private commit `99ccb6c8` (under the exclusive-GPU lock) ·
manifest PM-68..PM-74.** The §1 dissociation configuration (L8–11, α=0.25,
whole-context) re-run on quantized packs:

| pack / concept source | report shift real (nats) | null (nats) | window margin | verdict |
| --- | --- | --- | --- | --- |
| bf16, own pack (§1 reference) | +11.025 | +1.064 | **+9.96** | workspace_dissociation |
| int4 asym fine-group, own pack | +9.419 | +1.350 | **+8.07** | workspace_dissociation |
| int4 asym fine-group, **bf16-extracted pack (transfer)** | +9.501 | +0.360 | **+9.14** | workspace_dissociation |
| int4 sym per-tensor | (channel dead at baseline: report log-odds −0.45 vs −16.52 on bf16) | — | — | null_confounded |

Two findings: **(a) the workspace window survives production-representative
int4** at nearly full strength; **(b) concept directions are
precision-portable** — the bf16-extracted directions steer the int4 model at
essentially the bf16 margin (+9.14), so the *content geometry* survives
quantization even better than the model's own extracted copy. The per-tensor
tier destroys the report channel before any injection — consistent with §2's
total-collapse endpoint.

### 6.2 The reinjection verdict — HONEST NEGATIVE (double-negative)

**Date 2026-07-07 · private commit `e23f054d` · manifest PM-75..PM-82.**
E1 Stage C asked WHERE the int4 damage lives: reinstate the real deleted
residual `R` at the two top residual-norm-ranked site rollups (the
attention-value-projection band and the MLP down-projection band), each
against a norm-matched shuffled-residual null at the identical sites, and read
both channels:

| channel | attention-value sites | down-projection sites |
| --- | --- | --- |
| dissociation window (real-minus-null change) | **+0.28 nats** (noise) | **−0.20 nats** (null restored *more*) |
| broken flexible gates restored (real arm) | **0/9** | **0/9** |
| gates restored (null arm) | 0/9 | 1/9 (S04) — the leg's only restoration event, on a *shuffled* arm |
| routine control block | 8/8 intact everywhere | 8/8 intact everywhere |

**Formal verdict: no localized carrier at the tested sites under the tested
budget — the real residual beats its null on NEITHER channel.** The one
restoration event of the entire leg occurred on a null arm, which is exactly
what noise looks like. First-order picture: **the int4 deletion that breaks
flexible behavior is DIFFUSE** — it is not concentrated in the top
residual-norm sites the deletion ledger ranks first. Coverage-scoped honestly:
two site rollups, one reinjection budget, one model; "no necessity observed
under tested state coverage," never "no carrier exists."

### 6.3 Rescore note (marker hygiene) — the window got WIDER, not narrower

**Date 2026-07-07 · private commits `9357107c`, `e23f054d` · manifest PM-83
(deterministic 60-file bundle digest; rule in the entry).** A marker-hygiene
fix (ambiguous short stopword markers shared across the language pair excluded
from the continuation lexicon) was applied as an **offline rescore**:
companion artifacts committed for every affected cell, **originals untouched**.
Net effect: exactly **three per-band verdicts flip `joint_flip` →
`workspace_dissociation`** (1.7B whole-context α=1.0 band L0-3; qwen3-8b
whole-context α=0.25 band L24-27; qwen3-8b report-time-only α=1.0 band
L20-23) and none weaken — under corrected scoring the dissociation window is
**wider at both scales**. Headline rows in §1/§7 keep their original scoring;
the companions carry the corrected one.

---

## 7. Scale: qwen3-8b 9-cell grid — the window migrates, the null floor drops

**Date 2026-07-07 · private commit `74751075` · manifest PM-47..PM-56 (grid + pack),
PM-45/PM-46 (analysis) · run on a rented high-memory GPU instance, cuda fp32.**
The same instrument, pack-extraction recipe, and pre-registered verdict rule ran
unchanged on qwen3-8b (36 layers, d_model 4096 — 2x the 1.7B width). Read
directly from the committed per-band verdicts:

- **Dissociation at both scales — broader at 8B.** At the 1.7B headline
  configuration (whole-context, α=0.25), 8B passes the gate in **five
  contiguous bands** (L4-7 through L20-23: real +1.43 to +6.71 nats vs null
  −0.07 to +1.16; continuation intact in every one), where 1.7B had exactly one
  passing band (L8–11). Late bands (L24+) joint-flip at this dose, labeled.
- **The geometry migrates.** The report-time-only protocol (positions=last) —
  null-confounded at every dose at 1.7B (§1) — **passes at 8B**: α=1.0 gives
  three dissociating bands (L4-7 / L8-11 / L16-19: real +1.52 / +1.92 / +2.11
  vs null +0.75 / +0.06 / +0.30); α=2.0 gives L0-3 / L4-7. The gate still
  bites at 8B: L12-15 at last/α=1.0 is `null_confounded`; late bands at high
  dose end in `degenerate_continuation` — reported as such, not as steering.
  Best-dissociation cells sit deeper (depth-fraction ~0.5–0.6 vs 0.34 at 1.7B).
- **The one matching-free scale signal: the null floor.** At the matched dose
  with full multi-band coverage at both scales (α=1.0, whole-context), the
  median norm-matched-null report shift falls from **4.58 to 1.18 nats (÷3.9)**
  against a pure random-superposition (sqrt-d) prediction of ÷1.41 for this
  width change; even deep in the steering regime the 8B null stays quiet
  (L23-26 mid-band at α=0.5: real +22.63 vs null +0.19 — `joint_flip`, cited
  only as null-floor evidence). **No scaling exponent is quoted**: the
  hash-committed analysis note (PM-45) shows the implied exponent is
  band-matching-dependent — its sign flips between defensible matchings — so
  only the absolute drop is quoted, and even it carries stated caveats
  (absolute nats are not strictly comparable across d_model without an
  activation-norm normalizer; two scale points fix a line, not a law; same
  single concept pair and report question at both scales).
  *(Rescore note: under the marker-hygiene rescore — §6.3 — the whole-context
  α=0.25 window additionally gains band L24-27 and last/α=1.0 gains L20-23;
  the original artifacts are untouched, companions committed.)*

---

## 8. K=4 null ensemble on the flagship cell — now ensemble-gated

**Date 2026-07-07 · private commit `27ceabcb` · manifest PM-60..PM-64.**
The §1 flagship cell (qwen3-1.7b, L8–11, α=0.25, whole-context) re-run against
**four independent norm-matched shuffle-nulls**, with the real arm re-executed
in every run:

| arm | report shift (nats) | verdict |
| --- | --- | --- |
| real (x4 re-runs) | **+11.0251 — bit-identical across all four** | — |
| null, index 0 (the original) | +1.0644 | workspace_dissociation |
| null, index 1 | +0.2319 | workspace_dissociation |
| null, index 2 | −1.0068 | workspace_dissociation |
| null, index 3 | −0.6091 | workspace_dissociation |

Null ensemble mean −0.0799; max |null| = 1.0644 — the original single null
(§1) turns out to have been the *most adversarial* of the four, so the
published +9.96 margin was the conservative one. All four verdicts pass
independently; the real arm's bit-identity across re-runs doubles as an
in-experiment determinism cross-check. The flagship dissociation is no longer
a single-null result.

---

## 9. Position-resolved probe: a single consolidation site at K=24

**Date 2026-07-07 · private commits `4f4cf3ff` (driver + first cells),
`7c27f1db` (complete) · manifest PM-65..PM-67.**
Injection restricted to a **single context position K** (band L8–11,
qwen3-1.7b; 10 positions x 2 doses = 20 cells, one null index). Result: every
position reads at noise **except K=24**, which passes the dissociation gate at
both doses:

| cell | report shift, real (nats) | report shift, null (nats) | verdict |
| --- | --- | --- | --- |
| K=24, α=0.25 | **+0.573** | −0.006 | workspace_dissociation |
| K=24, α=1.0 | **+1.519** | +0.025 | workspace_dissociation |
| all other K ∈ {0,4,8,12,16,20,28,31,34}, both doses | ≤ +0.320 (largest: K=12, α=1.0) | ~0 | no_report_flip |

Early-context cells (K=0/4/8) move the report by ≤0.05 nats at α=0.25 — about
0.4% of the whole-context effect. The K=24 site accounts for ~5% of the
whole-context +11.03 at the same dose: the whole-context dissociation is not
the sum of one position, but exactly one compact consolidation site clears the
gate on its own. Continuation stays in the source language in every cell.
Scope: one band, one concept pair, one null index per cell (the K=4 ensemble
of §8 gates the whole-context flagship, not each position cell); single model.

---

## Cross-references

- Method context and claim boundaries: `POSITION_NOTE.md`
- Dated narrative: `TIMELINE.md`
- Hash bindings for every artifact above: `PRIORITY_MANIFEST.md` /
  `priority_manifest.json` (PM-01..42 + Update (2): PM-43..67 + Update (3):
  PM-68..86)
