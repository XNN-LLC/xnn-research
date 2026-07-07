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
the causal residual lives is the reinjection question (real-vs-null per site).

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

## 6. PRELIMINARY — the dissociation window survives int4

**Date 2026-07-07 · artifact pending commit · manifest: to be appended.**
On the production-representative int4 tier (§2), the §1 dissociation
configuration (L8–11, α=0.25, whole-context) still separates from its null:
real-minus-null report margin **+8.07 nats**, vs **+9.96** on bf16.
**PRELIMINARY:** single configuration, single model, artifact not yet merged
to private main at manifest time; its sha256 will be appended to
`PRIORITY_MANIFEST.md` in a dated update. Do not cite as a confirmed result.

---

## Cross-references

- Method context and claim boundaries: `POSITION_NOTE.md`
- Dated narrative: `TIMELINE.md`
- Hash bindings for every artifact above: `PRIORITY_MANIFEST.md` /
  `priority_manifest.json`
