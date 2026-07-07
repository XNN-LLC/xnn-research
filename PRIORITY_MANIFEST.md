# PRIORITY MANIFEST — cryptographic commitments to the private record

**Issuer:** XNN LLC · **Generated:** 2026-07-07T07:21:41Z

**The claim.** These hashes commit us to the content of the referenced
documents and run artifacts as of the stated dates. Full documents are
disclosed selectively (collaboration, NDA, publication); any disclosed copy is
verifiable byte-for-byte against this manifest. A hash commitment is a
commitment to content, **not** a disclosure of it: no formula, constant,
prompt, schema, or engineering detail can be recovered from a sha256.

**Private repository.** github.com/XNN-LLC/xnn-see-research (private).
HEAD at manifest generation: **`b931ee8bf61a459ae0b2a7de0f9fa563289c518d`**
(2026-07-07T01:32:11-04:00). The repo-HEAD commitment additionally binds every
in-repo document and artifact not individually listed below.

**Hash rule.** `sha256` over the exact file bytes as stored in the private
repository at the stated commit (git blob content). Where the note says
*hashed at repo HEAD*, the stated commit is the HEAD above and the date column
records the document's origin date.

**Verification protocol (under NDA or at publication).** (1) We disclose the
document; (2) you compute `sha256(file bytes)` and compare with this manifest;
(3) for commit binding, we open the private repository at the stated commit —
the git object graph (commit -> tree -> blob) independently timestamps the
same bytes. GitHub's push records provide a third-party timestamp upper bound.

**Update policy.** Append-only; dated updates; existing entries are never
edited. The PRELIMINARY int4-window artifact (RESULTS.md, section 6) will be
appended once it lands on private main.

**Public v0.4 note.** `POSITION_NOTE.md` is now labeled `v0.4-public` in this
public repository because public authorship, company attribution, and
LLM-assistance/accountability boundaries were added around the previously
published science text. PM-23 wording below predates that wrapper; read PM-23
as binding the private v0.3 science text and readout record, not the public
v0.4 wrapper. The v0.4 public wrapper and companion files are public repository
artifacts, not new private PM entries.

**A verifiable detail inside this manifest:** PM-37 and PM-38 — the
feasibility-gate evidence file and its independent solo re-run under an
exclusive-GPU lock — carry the **same sha256**. The bit-identical-reproduction
claim is thus checkable in public, today, without any disclosure.

## Entries

| id | date | private commit | sha256 | description |
| --- | --- | --- | --- | --- |
| PM-01 | 2026-05-06 | `80c125bc` | `d835b810d403110d525ea92a0377da3106d89a1027e7e6263974afbf223582f5` | Founding v0.1 specification of the SEE program: the first operational hypothesis and substrate design (first formula and first description; content private). *(founding priority object)* |
| PM-02 | 2026-05-06 | `80c125bc` | `337412e89f496d0863fe57e0c45bd52b98da8804e2f406836dace803738ff8e7` | Founding research plan of the SEE program (content private). |
| PM-03 | 2026-05-06 | `80c125bc` | `ea35ae7372ed67c2909c2e963acee1d293f38c18fb583cfb0e096654b49b1370` | Founding workspace README carrying the core-hypothesis statement (content private). |
| PM-04 | 2026-05-06 | `80c125bc` | `33ac693f7ae8e974dc4aca6db28448fa60164cf45d7b3b274f05f440c7004570` | Founding source module: bounded-resource (energy) accounting (source file; hash-only entry). *(hash-only)* |
| PM-05 | 2026-05-06 | `80c125bc` | `00e50e7d6a2b8693d4017cb0c9bf410de8ec354a6ca9048242e877d3f8ab1dbb` | Founding source module: distinction dynamics (source file; hash-only entry). *(hash-only)* |
| PM-06 | 2026-05-13 | `9d47be36` | `280c75137a53df9cb35801a3d2e358e26232e63db0e5d6ead0c0c588ccf91acd` | Project provenance record: creator, owner, and lead developer recorded in-repo. |
| PM-07 | 2026-05-31 | `03be2186` | `9f7941d20b1bc47c2fc4125811a74850ca77cc9f785286764151888b7ba48785` | In-repo authorship/IP timeline generated from git history and an executed technical proof ledger (55/55 validation commands passed, 12/12 claims supported at generation HEAD 4e61c128...). |
| PM-08 | 2026-06-28 | `15274a0d` | `617e2c8b5eca7bf9bcd7c0f2dc8e213f6cac11e689f65905f2c713af87d27b33` | Theory document: temporal identity and the provenance horizon — what a present computation state still proves about its past (content private). |
| PM-09 | 2026-06-28 | `59ac98a4` | `e812f2e39366cfc449fee875759b9095778597393ec5aa777b2506c8c5b9fd72` | Provenance-horizon preregistration (design-only, fail-closed; content private). |
| PM-10 | 2026-07-02 | `02ac4253` | `5e710f677ec4d012fa5e978499cf8361730e40592e176421317af8249e9c2948` | Provenance-horizon numeric freeze (frozen constants; content private). |
| PM-11 | 2026-06-24 | `5bfc7b2a` | `67876901607fd1e5c9d4644ca64c112fffdf4036f4aaba1e7bf4ac1d3cc4f934` | PSEK Phase 0: terminal-negative verdict, locked (an honest negative written up with the same rigor as a positive; content private). |
| PM-12 | 2026-06-24 | `d6b971d7` | `d5707fbbccbaa2b14f6a584cb346c2379ae86196f88a6d19e485021d901ef90c` | PSEK Phase 1: preregistration (design-only; content private). |
| PM-13 | 2026-06-24 | `105d28b2` | `36ab9f9be235abe3d57e828730e60a07ed776f5c412b9110e21ffeb6b3bd222b` | PSEK Phase 1: STOP-UNDERPOWERED verdict on the frozen design (verdict distinct from diagnosis; content private). |
| PM-14 | 2026-06-24 | `5453aa12` | `93127f721547b3a077bafeb25ea569ad8ad4cc49b28a9ebc7966381ac7d03dfd` | PSEK Phase 2: preregistration (design-only; content private). |
| PM-15 | 2026-06-24 | `03f8e240` | `c8263e8e68d59d32a427bfbc78cb96e8af2bcc5fd49df45d27319c18c615a4de` | PSEK Phase 2: locked numeric freeze (frozen constants; content private). |
| PM-16 | 2026-06-28 | `74c056ba` | `691dfd6a2ba29b36ad062da3794682d06f583a5639c1a5f2c9dc55ae50856682` | Theory document: state-dependent causal necessity of stored weight distinctions; carrier families; coverage-scoped negatives (captured 2026-06-28, refined same day). *(byte-identical at repo HEAD 2026-07-07)* |
| PM-17 | 2026-06-28 | `4980cfb2` | `6ba99fb543cf9e57d613d7ca364dfd383dae24cb8557603e18a98143ee0bd972` | Phase-3 preregistration, LOCKED: fail-closed design for measuring state-dependent necessity (categorical route-flip substrate, encoding-artifact firewall, FDR over the search tree, planted-necessity control, five-verdict vocabulary). *(byte-identical at repo HEAD 2026-07-07)* |
| PM-18 | 2026-06-29 | `aca08a52` | `0944d1c350454a747a06acd4fe74c5a5cc9239b18c86e418387ba72688273833` | Phase-3 numeric freeze: every numeric degree of freedom frozen and hash-committed before evaluation (DEV-only; constants private). *(byte-identical at repo HEAD 2026-07-07)* |
| PM-19 | 2026-07-07 | `23b9226d` | `6ed7ca1f352fd31d66fdbdab589ee47e3cbe2b69939732a210938feca759eb7d` | Phase-3 numeric-freeze amendment A10: a freeze-vs-source drift found and reconciled pre-evaluation (constants private). |
| PM-20 | 2026-07-04 | `b931ee8b` | `b91820681669f1b7fc24e8b0e625c15ae274200da77660da48dc3814bb0b745f` | Deletion-microscopy program note: quantization-residual R = W - dequant(Q(W)) as a deletion microscope; instrument chain; the gemma-4-E2B null-gated negative and refused false positives. *(first committed 2026-07-04; hashed at repo HEAD (includes verdicts through 2026-07-06))* |
| PM-21 | 2026-07-04 | `e3476188` | `bebab2ce4e254ef1fe09e656fb59e59b4a228b74fe3417f1b729708b43f7516b` | Program statement: forward spectral provenance of inference, with causal ablation as the only admissible verifier (content private). |
| PM-22 | 2026-07-06 | `b931ee8b` | `4e2dd11a91d5bdc831cab48bc2f0ae56f674ebc18e19ac4b1260de2381b8f912` | Same-day response plan to the Anthropic workspace paper: construct-by-construct mapping and the E1-E4 experiment program. *(created 2026-07-06 (042c4eee); hashed at repo HEAD)* |
| PM-23 | 2026-07-07 | `b931ee8b` | `e90f42696741d9adddb1711d6a1efb7728b9708427081ece5fd99dc8c12565cc` | Position note v0.3 (private original of this repository's POSITION_NOTE.md), quotations verified against the published paper and commentary. |
| PM-24 | 2026-07-07 | `b931ee8b` | `f41531d2c5cb2bb9903bd5505f4b9cc0826ac4a9a9a89f350ca94012dc372514` | Companion abstract of the position note (draft, not posted). |
| PM-25 | 2026-07-07 | `859b4077` | `e47e466c966ceb2f54112074b9176a11177906cd5d0e1bdfba0fae6f8e4203c1` | W4 fragility verdict: the finest production-representative int4 tier selectively breaks flexible behaviors on qwen3-1.7b; nine lock-held flips; tier-ladder shape. |
| PM-26 | 2026-07-07 | `859b4077` | `fded8bfa520e2704d0632f55385eaae5fe1dbc4a4b6987c907da23c38c1c2f1d` | W4 behavioral battery v2: 44 prompt items across 4 families mapped to the workspace paper's flexible-vs-routine paradigms (full prompts private). *(battery line first committed 2026-07-06 (fd16b2a9))* |
| PM-27 | 2026-07-07 | `859b4077` | `f20f1fb457a2cbc8cf06929b7637bea735e20b47cf636cbd0fc2f8daa181ac4d` | W4 graded summary table (survivor-based pass rates per family per tier). |
| PM-28 | 2026-07-07 | `859b4077` | `f72ea3742e87923ebf344b2371e1b83bb59b082dd6bb264f5c516fb41244754c` | W4 graded per-item results on the production-representative int4 tier (raw decodes; content private). |
| PM-29 | 2026-07-07 | `859b4077` | `7622e9d601882fa7043e2d376ed19a8cdbad6c4ec4fb5038ded66c8af3157ef8` | Per-tensor residual-deletion ledger for the production-representative int4 tier on qwen3-1.7b (site-level statistics; content private). *(first committed 2026-07-06 (fd16b2a9))* |
| PM-30 | 2026-07-06 | `c80c6425` | `3a076babc5e122e38d204fa5cfba0ff8e9aa40404015a7e361e67dc3d4ddaf92` | HEADLINE dissociation artifact: band L8-11, alpha 0.25, whole-context — report +11.025 nats real vs +1.064 null, continuation intact both arms; verdict workspace_dissociation; includes determinism block and raw token streams. |
| PM-31 | 2026-07-06 | `c80c6425` | `f598a12870522f512ab5901b902794df5cadfe148d7f50e295a9a67c5abfb8f2` | Dose-response artifact: alpha 0.5 whole-context — joint_flip (report and continuation flip together). |
| PM-32 | 2026-07-06 | `c80c6425` | `f0059d00d1b79b4d1fc826b5d73aea31461fc6f1f0ce0f58b6eca681f32aa86b` | Dose-response artifact: report-time-only injection, alpha 0.0625 — no_report_flip; null >= real. |
| PM-33 | 2026-07-06 | `c80c6425` | `f1c60f7c1613d5464411a063a547fe11d292d33c0681feecc2282e4e65a8f21c` | Dose-response artifact: report-time-only injection, alpha 0.125 — no_report_flip; null >= real. |
| PM-34 | 2026-07-06 | `c80c6425` | `fcf17f8da9f89b3bc2db688376b8b1de06d357f0076ef24246f00dd537a84dbc` | Dose-response artifact: report-time-only injection, alpha 0.25 — no_report_flip; null >= real. |
| PM-35 | 2026-07-06 | `c80c6425` | `fe5c47630b5e94f0e8fec848ecef047e44aba96e204d4a136fdcdb9246bc7383` | Dose-response artifact: report-time-only injection, alpha 0.5 — null_confounded (the would-be false positive the null caught). |
| PM-36 | 2026-07-06 | `c80c6425` | `e1c14eb65953706c1dba07a7172f448e5dab78979ffc5ee6ce25d1c1ac212b74` | Dose-response artifact: alpha 1.0 whole-context — joint_flip. |
| PM-37 | 2026-07-06 | `d43e85b2` | `e93f2a5aac28a3c42b8787e27744698d3b0ca81bf5de1bda321a89b8511f1585` | OLMoE M3-feasibility evidence pack: verdict FEASIBLE; 3/3 shards, 3219 weight-map entries; anchor forward token-correct; 384/384 routing records; route-flip observable on all 16 MoE layers. |
| PM-38 | 2026-07-06 | `47e37047` | `e93f2a5aac28a3c42b8787e27744698d3b0ca81bf5de1bda321a89b8511f1585` | Solo re-run of the M3-feasibility gate under an exclusive-GPU lock: BIT-IDENTICAL to PM-37 — note the sha256 equals PM-37's, the bit-identity claim is verifiable inside this public manifest. *(sha256 identical to PM-37 by construction)* |
| PM-39 | 2026-07-06 | `47e37047` | `c1eb519e35d8e8311ba7843a3c3abc5f718f0fbabec3d0dd5bc38d5ad5e6e98f` | Solo-confirm note: reproduction conditions and the zero-differing-bytes comparison (paths redacted in public quotation; file content private). |
| PM-40 | 2026-07-06 | `47e37047` | `9a70c0d347bb7296af0043f2d164a78d24e6bfffd9e67fe8b3f8ae7afb3d396c` | OLMoE weights provenance: HF revision pin + sha256 verification against the upstream LFS manifest. *(provenance captured with the gate run (d43e85b2); hashed at its relocated path (47e37047))* |
| PM-41 | 2026-07-06 | `3503a160` | `71610f102f4b774ed8cf88cc4ea2b2b30f000039da5edf6509694e1572fca30c` | J-Lens direction-pack proof manifest (qwen3-1.7b): extraction provenance, per-model-file sha256, pack sha256, official-parser verification. *(readout numbers are recorded in the position note, PM-23; the final-layer anchor is recomputable from the sha-pinned pack + model files)* |
| PM-42 | 2026-07-06 | `c74ccfea` | `db48627e945bd0fcd71245fb71f30c92c3930c43f5f752637b7ee3f27de48be4` | Wave-0 integration gate transcript: release build + anchor smoke + 3-run CUDA decode bitwise-determinism GREEN (per-step top-8 logit stream fnv1a64 445f710a693a80c9). |

Machine-readable mirror: [`priority_manifest.json`](priority_manifest.json).
