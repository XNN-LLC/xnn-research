# TIMELINE — dated priority narrative of the XNN SEE research program

Private-record rows below are bound to the private repository's git history:
the commit hash identifies the commit, and where a document is the priority
object its content sha256 is committed in `PRIORITY_MANIFEST.md` (PM-xx).
Public-only repository update rows are labeled as public repo updates and are
bound by this public repository's git history, not by new private PM entries.
The timeline proves *that* a formulation, design, instrument, verdict, or
public update existed at the stated date. It deliberately does **not** print
the founding formulations or any frozen constants — those are committed by hash
and disclosed selectively. Dates are commit author dates (US Eastern) unless
noted.

## 2026-05 — genesis: the founding formulation and the runtime

| Date | Event | Private commit | Manifest |
| --- | --- | --- | --- |
| 2026-05-06 | **Program birth.** Research workspace initialized with the founding v0.1 specification of the SEE program — the founding operational hypothesis on meaning-bearing distinctions under bounded-resource dynamics (first formula and first description; content private, hash-committed) — plus the founding research plan and the first source modules implementing the energy-accounting and distinction-dynamics substrate. | `80c125bc` | PM-01..PM-05 |
| 2026-05-06 → 05-07 | 160+ same-week experiment batches on the founding substrate (diagnostics, interventions, ablations, reproducibility tiers, verdict evaluator) — the fail-closed verdict culture is present from the first days. | `6e9a1ee6` … | — (git history) |
| 2026-05-13 | Project provenance record committed (creator/owner/lead developer recorded in-repo); production-core plan; first capture of runtime router traces from a real open-weight MoE — the pivot of the program's instruments onto real models begins. | `9d47be36`, `99583132` | PM-06 |
| 2026-05-19 | Hand-written GPU backend milestones for MoE execution land in the self-contained runtime (no third-party ML dependencies on the product path — a standing architectural rule from this period on). | `ccfd643b` | — (bound via PM-07) |
| 2026-05-30/31 | **Technical proof ledger + evidence dossier + in-repo authorship/IP timeline** generated from git history and executed validation commands (55/55 commands passed, 12/12 claims supported at that HEAD, `4e61c128…`), each artifact sha256-recorded in-repo. The program has treated its own history as evidence since May. | `4ec06f0f`, `a058bb36`, `ae4555f9`, `4e61c128`, `03be2186` | PM-07 |

## 2026-06 — from substrate to weight-space causal metrology

| Date | Event | Private commit | Manifest |
| --- | --- | --- | --- |
| 2026-06-05 | Full-GPU per-layer token-state decode chain; ZAYA forward HF-reconciled at 2 tokens (external oracle used for comparison only, never as runtime). | `faf7cf23`, `e42a0d30` | — |
| 2026-06-09 | OLMoE router instrumentation matures: per-token expert traces; empirical-vs-analytic route agreement 3–19x above chance (recorded in the stack ground-truth document, bound by the repo-HEAD commitment). | (ground-truth doc) | — |
| 2026-06-20 | Token-exact non-transformer forwards on the one runtime: Mamba2, RWKV-7, xLSTM, GLA, RetNet — the substrate that later makes the "workspace without attention" question cheap to ask. | `951b3cb1`, `2d157e7e`, `9931fcad`, `7ee4c1b1`, `32533431` | — |
| 2026-06-24 | **The honest-negative arc, written up and locked:** PSEK Phase 0 closed as a terminal negative; Phase 1 preregistered, then closed as STOP-UNDERPOWERED on the frozen design; Phase 2 preregistered with a locked numeric freeze. Negatives and STOPs are published verdicts, not abandoned drafts. | `5bfc7b2a`, `d6b971d7`, `105d28b2`, `5453aa12`, `03f8e240` | PM-11..PM-15 |
| 2026-06-28 | **First statement of state-dependent causal necessity of stored distinctions** — the carrier-mapping theory document (captured + refined same day; content byte-identical from this date through the current repo HEAD). Same day: the temporal-identity/provenance-horizon theory document and the provenance-horizon preregistration. | `5223bc69`, `74c056ba`, `15274a0d`, `59ac98a4` | PM-16, PM-08, PM-09 |
| 2026-06-28 | **Phase-3 preregistration LOCKED** — the fail-closed measurement design for state-dependent necessity: categorical route-flip substrate on a real MoE, representation-aware intervention primitive, encoding-artifact firewall, FDR over the whole search tree, planted-necessity positive control, five-verdict vocabulary. Content byte-identical from lock date through the current repo HEAD. | `4980cfb2` | PM-17 |
| 2026-06-29 | **Phase-3 numeric freeze** — every numeric degree of freedom frozen and hash-committed before any evaluation (DEV-only). Content byte-identical from freeze date through the current repo HEAD. | `aca08a52` | PM-18 |

## 2026-07 (pre-paper) — the deletion microscope

| Date | Event | Private commit | Manifest |
| --- | --- | --- | --- |
| 2026-07-02 | Provenance-horizon numeric freeze committed. | `02ac4253` | PM-10 |
| 2026-07-03 | Decode-parity instrument (per-step decode trace + near-tie classifier). | `6f2771c3` | — |
| 2026-07-04 | **First deletion-microscopy formulation + the five-tool instrument chain, all committed in one day:** residual-ledger (per-tensor inventory of `R = W − dequant(Q(W))`), residual-reinject (causal reinjection with a fail-closed norm-matched shuffle-null), silicon-trace (per-operation output-checksum receipts), silicon-diff (op-for-op divergence localization), proof-pack (bytes → gates → verdict binding); teacher-forced decode harness; one-command cloud preset for the full loop. | `f74586c7`, `8821ffd6`, `6d0c3744`, `59a95d6b`, `9b941062`, `88ba49ea`, `9d4914ff` | PM-20 |
| 2026-07-04 | **The paid honest negative:** gemma-4-E2B OCR carrier hunt across three int4 tiers returns NO carrier — the null gate refuses the effect; two would-be false positives caught before becoming claims. Same day: the genesis-trace program statement (forward spectral provenance; ablation as the only verifier). | `aeba806b`, `e3476188` | PM-20, PM-21 |

## 2026-07-06 — the Anthropic workspace paper lands; same-day response

| Date | Event | Private commit | Manifest |
| --- | --- | --- | --- |
| 2026-07-06 | Anthropic publishes "Verbalizable Representations Form a Global Workspace in Language Models" + commentary pack (Dehaene–Naccache, Eleos AI, Nanda). External event — our territory mapping is same-day. | — | — |
| 2026-07-06 | **Response plan committed the same day:** the construct-by-construct mapping (their J-space/activation axis ↔ our carrier/weight axis) and the four-experiment program E1–E4. | `042c4eee` | PM-22 |
| 2026-07-06 | **Same-day instruments:** workspace-map (null-gated dissociation mapper, device-side injection on the full-GPU chain); workspace-gates (flexible-vs-routine behavioral gate suite); CUDA determinism regression (3 decodes, bit-identical logit streams) with the Wave-0 integration gate GREEN; J-Lens comparison-oracle direction packs with a bit-exact final-layer anchor. | `8a1d0ed3`, `69bfeb0b`, `76ff3b6e`, `c74ccfea`, `3503a160` | PM-41, PM-42 |
| 2026-07-06 | **The paper's central dissociation reproduced on open weights, null-gated, same day:** qwen3-1.7b, band L8–11, α=0.25, whole-context — report shift +11.03 nats real vs +1.06 null (10.4x), continuation intact in both arms; the same run-set's null REJECTED every report-time-only cell as confounded (the un-nulled false positive, caught in vivo). Seven dose-response artifacts committed. | `c80c6425` | PM-30..PM-36 |
| 2026-07-06 | **Ignition-class design becomes runnable:** the June-preregistered near-margin route-flip evaluation passes its hard M3-feasibility gate on OLMoE-1B-7B — verdict FEASIBLE, route-flip signal observable on all 16 MoE layers, weights pinned and sha-verified; solo re-run under an exclusive-GPU lock reproduces the evidence file **bit-identically** (the two artifacts' sha256 are equal in this manifest). Int4 fragility battery (44 items, 4 families) + bf16 baseline + residual ledger committed the same day. | `d43e85b2`, `47e37047`, `fd16b2a9` | PM-37..PM-40, PM-26, PM-29 |

## 2026-07-07 — verdicts and the position note

| Date | Event | Private commit | Manifest |
| --- | --- | --- | --- |
| 2026-07-07 | **W4 fragility VERDICT:** the finest production-representative int4 tier selectively breaks bf16-correct flexible behaviors on qwen3-1.7b (9 lock-held flips across suppression / trace-gap / two-hop) while routine continuation stays 100% intact — the E1 fragile substrate is found. All raws lock-held and committed. | `859b4077` | PM-25..PM-29 |
| 2026-07-07 | Phase-3 E3 preflight: numeric-freeze amendment A10 (a freeze-vs-source drift found and recorded), null-calibration runbook, seed-set fixture (contents private). | `23b9226d` | PM-19 |
| 2026-07-07 | **Position note v0.2 → v0.3:** every paper/commentary quotation verified against the published sources; the v0.3 public edition was published as this repository's `POSITION_NOTE.md` before the later v0.4-public attribution wrapper. | `b31121f6`, `b931ee8b` | PM-23, PM-24 |
| 2026-07-07 | **PRELIMINARY:** the dissociation window survives int4 deletion on the production-representative tier — real-minus-null report margin +8.07 nats (vs +9.96 on bf16) at the same L8–11 / α=0.25 configuration. Single configuration, artifact not yet on private main at manifest time; its sha256 will be appended in a dated manifest update. Treat as unconfirmed until then. | (pending) | (pending) |
| 2026-07-07 | **Public v0.4 accountability and Level 1 attestation update:** authorship, XNN LLC attribution, Georgia/USA company context, LLM-assistance boundary, and a sanitized GPT-2 model-BOM / weight-attestation companion added to the public repository. No private documents, raw weights, local paths, command logs, or implementation internals disclosed. | public repo | `AUTHORS.md`, `PUBLIC_UPDATE_V0_4.md`, `LEVEL1_ATTESTATION_GPT2_V0_4.md` |
| 2026-07-07 | This public priority record assembled; private repo HEAD at assembly: `b931ee8bf61a459ae0b2a7de0f9fa563289c518d`. | — | manifest header |

## 2026-07-07 — second wave: scale, ensembles, position resolution

| Date | Event | Private commit | Manifest |
| --- | --- | --- | --- |
| 2026-07-07 | **Scale leg (qwen3-8b), run on a rented high-memory GPU instance:** the same instrument and pre-registered verdict rule unchanged at 2x width — dissociation at both scales with five contiguous passing bands at whole-context α=0.25; the report-time-only protocol (null-confounded at 1.7B) passes at 8B; late bands degenerate, labeled; median null floor drops ÷3.9 vs a geometric prediction of ÷1.41. Full-scale J-Lens direction manifest (qwen3-1.7b, all layers) committed alongside. | `74751075` | PM-47..PM-59 |
| 2026-07-07 | **Feature-resolution scaling analysis with the honest matching caveat:** the implied scaling exponent is band-matching-dependent — its sign flips between defensible matchings — so no exponent is quoted; only the absolute null-floor drop is, with the activation-norm-normalizer caveat stated. | `9ac04db4` | PM-45, PM-46 |
| 2026-07-07 | Instrument upgrades: K-null ensemble mode (error bars on every null floor) and single-position probe mode of the workspace mapper. | `b3a6882e` | — (repo-HEAD-bound) |
| 2026-07-07 | **K=4 null ensemble on the flagship 1.7B cell:** real +11.0251 nats reproduced bit-identically across all four re-runs; four independent norm-matched nulls (+1.0644 / +0.2319 / −1.0068 / −0.6091, mean −0.0799); all four verdicts pass — the flagship dissociation is now ensemble-gated, and the original single null was the most adversarial of the four. | `27ceabcb` | PM-60..PM-64 |
| 2026-07-07 | Position-sweep driver + first partial single-position cells. | `4f4cf3ff` | (covered by PM-65) |
| 2026-07-07 | **Position sweep complete — a single consolidation site:** across 20 single-position cells (10 positions x 2 doses, band L8–11), exactly one position (K=24) passes the dissociation gate at both doses (α=0.25: real +0.573 vs null −0.006; α=1.0: real +1.519 vs null +0.025); every other position reads at noise; continuation intact throughout. | `7c27f1db` | PM-65..PM-67 |
| 2026-07-07 | **Position note v0.4** (private): adds the qwen3-8b scale-leg section and the E1 int4-sweep status; the v0.5-public edition in this repository mirrors it. PM-43 supersedes PM-23 as the current note binding going forward. | `66d6eb2d` | PM-43, PM-44 |
| 2026-07-07 | Stack ground-truth and repository-index documents refreshed to record the 2026-07-06/07 response wave (living documents, repo-HEAD-bound). | `b07548cf` | — |
| 2026-07-07 | Manifest **Update 2026-07-07 (2)** assembled (PM-43..PM-67, append-only); second private repo-HEAD binding: `7c27f1db2ae3532749cdf71b4154b399640095ce`. | — | manifest Update (2) |

## 2026-07-07 — third wave: E1 resolved, honest negative, rescore

| Date | Event | Private commit | Manifest |
| --- | --- | --- | --- |
| 2026-07-07 | **A/B binary timing record:** the same workspace-map cell run on two binaries — readout payloads byte-equal, wall clock 133 s vs 1066 s (8x) — committed as an honest performance-anomaly note; readout integrity unaffected. | `7f808357` | PM-84..PM-86 |
| 2026-07-07 | **The K=24 consolidation site identified:** the single passing position of the sweep (PM-65..PM-67) is the token " Los" — the first token of the prompt's second sentence. The consolidation site sits at a **sentence boundary**, consistent with content being consolidated where a clause closes (identity cross-checked against the committed sweep artifacts and the internal verification table). | (identity over PM-65..PM-67 artifacts) | PM-65..PM-67 |
| 2026-07-07 | **E1 Stages A+B (lock-held): the int4 window is committed** — own-pack margin +8.07; bf16-pack transfer margin +9.14 (concept directions are precision-portable); per-tensor int4 report channel dead at baseline (−0.45 vs −16.52). Resolves the §6 PRELIMINARY exactly as promised. | `99ccb6c8` | PM-68..PM-74 |
| 2026-07-07 | **Marker-hygiene fix + offline rescore:** companions committed for every affected artifact, originals untouched; exactly three per-band verdicts flip `joint_flip` → `workspace_dissociation` (1.7B α1.0 L0-3; 8B α0.25 L24-27; 8B last/α1.0 L20-23) — the window is WIDER under corrected scoring; nothing weakened. | `9357107c` | PM-83 |
| 2026-07-07 | **E1 reinjection legs complete — double-negative carrier verdict (honest negative):** the real residual reinstated at the two top residual-norm site rollups beats its norm-matched shuffled null on NEITHER channel (window +0.28/−0.20 = noise; gates 0/9 on real arms; the single restoration event on a null arm). First-order picture: **diffuse deletion**. Coverage-scoped. | `e23f054d` | PM-75..PM-82 |
| 2026-07-07 | Manifest **Update 2026-07-07 (3)** assembled (PM-68..PM-86, append-only); third private repo-HEAD binding: `e23f054dc3a8c790f365fb159888ae3beef9d6b0`. | — | manifest Update (3) |

**Reading rule.** Private rows marked with manifest references are provable
today: request the document under NDA, hash it, compare. Private rows without a
manifest reference are ordinary git history in the private repository and are
provable by repository inspection under the same terms. Public-only update rows
are public repository history; they do not disclose or imply new private PM
entries.
