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

**Reading rule.** Private rows marked with manifest references are provable
today: request the document under NDA, hash it, compare. Private rows without a
manifest reference are ordinary git history in the private repository and are
provable by repository inspection under the same terms. Public-only update rows
are public repository history; they do not disclose or imply new private PM
entries.
