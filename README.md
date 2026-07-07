# XNN Research — causal-carrier metrology (public priority record)

**Who we are.** XNN LLC is an independent research lab. Since May 2026 we have
been building a research program — SEE — around one discipline: **causal claims
about neural systems must survive matched null controls, preregistration, and
execution receipts, or they are not claims.** The program runs on a
self-contained runtime with a hand-written GPU backend and zero third-party ML
dependencies on the product path, so that every experiment's execution is an
auditable object rather than a stack of trusted frameworks.

**What this repository is.** The private research repository is not public.
This repository is the public, self-sufficient record of the program's claims,
dates, and results: the position note, the result tables, a dated timeline back
to the program's first formulation, and a **cryptographic priority manifest** —
sha256 commitments to the private documents and run artifacts, so that priority
is provable without disclosure. Full documents are disclosed selectively
(collaboration, NDA, publication).

## The thesis

- **State-dependent causal necessity.** A stored weight distinction has a fixed
  address but a *state-dependent* causal significance: the same perturbation
  can be invisible in one inference state and flip a discrete decision in
  another. Which distinctions are necessary, for which behaviors, in which
  states, at what precision — that is the program's question (theory
  formalized 2026-06-28, hash-committed; see `PRIORITY_MANIFEST.md`).
- **Deletion microscopy in weight space.** Quantization is controlled deletion:
  `R = W − dequant(Q(W))` is an addressable map of every distinction a
  quantized model can no longer make. Reinjecting pieces of `R` — always
  against a **norm-matched shuffled null at the same site** — asks which
  deleted distinctions were holding a behavior.
- **Null-gated causal claims.** Every steering/injection claim must beat a
  norm-matched shuffle-null; discovery sweeps are preregistered with
  hash-committed numeric freezes and FDR over the whole search tree; decodes
  are bit-deterministic with per-operation checksum receipts. Fail-closed
  verdicts (including STOP and VOID) are first-class outcomes.

## Relationship to Anthropic's global-workspace paper (2026-07-06)

Anthropic's "Verbalizable Representations Form a Global Workspace in Language
Models" identifies a privileged activation subspace (J-space) carrying
reportable, flexibly-usable content. Our program is the **complementary axis**:
the same class of object, one level down, in the *weights*. On the day the
paper landed we reproduced its central dissociation signature on open weights
(qwen3-1.7b) **under a control the original lacked** — a norm-matched
shuffle-null — and the same instrument's null *rejected* a confounded variant
that an un-nulled pipeline would have published. The same day, our
June-preregistered ignition-class design (near-margin route-flips at MoE
routing boundaries) passed its hard feasibility gate on OLMoE,
bit-identically reproduced. See `POSITION_NOTE.md` and `RESULTS.md`.

## The honest-score culture

We publish negatives with the same machinery as positives. The program's
current honest score, stated plainly: weight-space carriers found so far:
**zero** (a paid, full-instrument negative on gemma-4-E2B OCR is part of the
record); activation-space dissociations found: **one**, null-gated,
existence-level; two earlier program phases were closed as a **terminal
negative** and a **STOP-UNDERPOWERED** — both written up and hash-committed. A
methodology whose controls have never rejected anything is advertising, not
metrology.

## Files

| File | What it is |
| --- | --- |
| `POSITION_NOTE.md` | Public edition of the position note (v0.3, 2026-07-07): "Weight-space carriers of the global workspace: deletion microscopy meets J-space" |
| `RESULTS.md` | The numbers: dissociation dose-response, int4 fragility tier table, feasibility-gate criteria, determinism anchor, J-Lens oracle readout, preliminary int4-window result |
| `TIMELINE.md` | Dated priority narrative from the program's first formulation (2026-05-06) to the present, every row hash-committed |
| `PRIORITY_MANIFEST.md` / `priority_manifest.json` | The cryptographic prior: sha256 commitments to the private documents and artifacts behind every claim |
| `LICENSE` / `NOTICE.md` | All rights reserved; quotation permitted with attribution; no license to methods; patent rights reserved |

**Claim discipline used throughout:** [committed] — proven at the stated scope
by code, a run artifact, or a verdict in the private repository at the cited
commit, whose content hash is committed here; [preregistered] — a frozen,
hash-committed design whose evaluation has NOT run; [planned] — a dated
intention, never presented as a result. We take no position on consciousness;
this is causal-carrier metrology, nothing more.

Contact: open an issue on this repository.
