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

---

## Update 2026-07-07 (2) — appended entries PM-43..PM-67 + second repo-HEAD binding

**Appended 2026-07-07T10:13:56Z (UTC).** Same issuer, same hash rule, same verification protocol
as the header above; nothing above this line was edited. **Second private
repo-HEAD binding:** `7c27f1db2ae3532749cdf71b4154b399640095ce`
(2026-07-07T06:04:50-04:00) — binds every private document and artifact as of
that commit, including all entries below. **Note on PM-23/PM-43:** PM-43 binds
the private position note v0.4 (which adds the qwen3-8b scale-leg section) and
supersedes PM-23 as the current note binding going forward; PM-23 remains the
valid binding for the v0.3 text. The int4-window PRELIMINARY artifact
(RESULTS.md §6) is still not on private main and remains pending a future
dated update.

| id | date | private commit | sha256 | description |
| --- | --- | --- | --- | --- |
| PM-43 | 2026-07-07 | `66d6eb2d` | `1c2bd60cef871ec0e19b36001e1a7be9e5e073df22e515593934f8b691be1972` | Position note v0.4 (private): adds the qwen3-8b scale-leg section and the E1 int4-sweep status to the v0.3 science text; the public v0.5 edition in this repository mirrors it. Supersedes PM-23 as the current note binding going forward. |
| PM-44 | 2026-07-07 | `66d6eb2d` | `9d4f43cc422a20d77aa1fd4379b47e15da3ef0910a393aa719ed9098556f0491` | Companion abstract of the position note, v0.4 revision (draft, not posted). |
| PM-45 | 2026-07-07 | `9ac04db4` | `9304fed2af0b23edc63c605ee7e34332e22b285e9d3bb94faf47a8eeb479dbb4` | Feature-resolution scaling note: two-point (1.7B to 8B) null-coupling analysis showing the implied scaling exponent is band-matching-dependent (its sign flips between defensible matchings) - the basis for quoting only the absolute null-floor drop, with the activation-norm-normalizer caveat. |
| PM-46 | 2026-07-07 | `9ac04db4` | `a801399f8f9b5c2b77b3a846ca5a5d45f4d5d7cb73f32b8f1609a1fc0dc56b82` | Scaling-analysis data pack behind PM-45 (per-band real/null report shifts at both scales; content private). |
| PM-47 | 2026-07-07 | `74751075` | `c74496dffad5617c7abccd9ac01a100921c65fcf84e4c314b08990fbbabce025` | qwen3-8b workspace-map sweep artifact: whole-context, alpha 0.25 - five contiguous dissociation bands (L4-7 through L20-23; real +1.43 to +6.71 nats vs null -0.07 to +1.16), continuation intact in each; late bands joint-flip, labeled. |
| PM-48 | 2026-07-07 | `74751075` | `8403a843b220dbca59eb89a39f081408d9444a37b41e0e4bd3e43f96774dac59` | qwen3-8b workspace-map sweep artifact: whole-context, alpha 0.5. |
| PM-49 | 2026-07-07 | `74751075` | `e7f0020266e8a747521d4ad57048533a8ae9d036f84156f16bd8e281126f9749` | qwen3-8b workspace-map sweep artifact: whole-context, alpha 1.0 (the matched-dose cell for the cross-scale null-floor comparison: median null shift 1.18 nats vs 4.58 at 1.7B). |
| PM-50 | 2026-07-07 | `74751075` | `8b516f879078944c0bf32532ab797a4a2f60940fe515982e9d9c812d339c6291` | qwen3-8b workspace-map sweep artifact: report-time-only (last position), alpha 0.5. |
| PM-51 | 2026-07-07 | `74751075` | `9171244468949944de28a972cf148278920e73ca7722b4aa42e7da646841a5c0` | qwen3-8b workspace-map sweep artifact: report-time-only, alpha 1.0 - three dissociating bands (L4-7 / L8-11 / L16-19: real +1.52 / +1.92 / +2.11 vs null +0.75 / +0.06 / +0.30); one band null-confounded, labeled. |
| PM-52 | 2026-07-07 | `74751075` | `8e2333c1792439b58327a8b0e777544e318defb5ba4393a5158c6586958ec0a1` | qwen3-8b workspace-map sweep artifact: report-time-only, alpha 2.0 - early bands dissociate (L0-3 / L4-7); late bands degenerate, labeled as such. |
| PM-53 | 2026-07-07 | `74751075` | `91abffc0cdf7bfac0b8a0d59cce387b4d5b9d930b246695923a85933aee57612` | qwen3-8b workspace-map mid-band focus artifact: whole-context, alpha 0.5 (includes the null-floor evidence cell L23-26: real +22.63 vs null +0.19, verdict joint_flip - cited only as null-floor evidence). |
| PM-54 | 2026-07-07 | `74751075` | `73629edd6d7d7ec5590864b44e2a5cb73242d8684e3289193b31c91655ec4f94` | qwen3-8b workspace-map mid-band focus artifact: report-time-only, alpha 1.0. |
| PM-55 | 2026-07-07 | `74751075` | `5f0b61998672fbd00445c5b89eef6ba6c634143ea1ac06ae9d80b27c22589f54` | qwen3-8b workspace-map mid-band focus artifact: report-time-only, alpha 2.0. |
| PM-56 | 2026-07-07 | `74751075` | `90fc0dc3c35f3118b3da85535f25126762a07f2e32d84caec875bf57f3e16985` | qwen3-8b concept-vector pack (Spanish/French contrast; extraction recipe identical to the 1.7B pack; content private). |
| PM-57 | 2026-07-07 | `74751075` | `c2b6e605b99577d3f02ceca62cb6d39fd471c23275debfff01acdb16b8815d8c` | Full-scale J-Lens direction-pack manifest (qwen3-1.7b, all layers): extraction provenance, per-model-file sha256, pack sha256. |
| PM-58 | 2026-07-07 | `74751075` | `7fd8c858dcebc16372e61ddcfa4e779edb0f321da24fcd62c64b67ad062537c1` | Weights-revision receipt for the qwen3-8b leg (upstream revision pin; hash-only entry). *(hash-only)* |
| PM-59 | 2026-07-07 | `74751075` | `3c8460bbc6b2f343923787a32ead8baefa38f6f99b8a8575adecaffdb9b10a95` | Oracle-environment receipt for the qwen3-8b leg (framework versions; hash-only entry). *(hash-only)* |
| PM-60 | 2026-07-07 | `27ceabcb` | `7f55150ffed1bf108ad3796fae0235ac781eb745b6d8b7e5dbe47164d323a23b` | K=4 null-ensemble summary for the flagship 1.7B cell (L8-11, alpha 0.25, whole-context): real +11.0251 nats bit-identical across all four re-runs; four independent norm-matched shuffle-nulls +1.0644 / +0.2319 / -1.0068 / -0.6091 (mean -0.0799); all four verdicts workspace_dissociation. |
| PM-61 | 2026-07-07 | `27ceabcb` | `779de4188bd87e1c82f6869c2a09c67f78c1bead71e5b5e1902a3584da1a867c` | Ensemble member artifact: null index 0 (the original single-null configuration). |
| PM-62 | 2026-07-07 | `27ceabcb` | `e882e102855f3ade575e24b9278a21904df21171160b8151cb3ca58b9ea6cdfb` | Ensemble member artifact: null index 1. |
| PM-63 | 2026-07-07 | `27ceabcb` | `63757e71570dd5fff49b66f59159a7ee380d87b6c1519846e590f7135c2fb333` | Ensemble member artifact: null index 2. |
| PM-64 | 2026-07-07 | `27ceabcb` | `52be7eb31df97c5e867f786ca86c3047261ee20275afcbf97255df2b965fe4e0` | Ensemble member artifact: null index 3. |
| PM-65 | 2026-07-07 | `7c27f1db` | `e455b861229e2ab582e5986b7df408f4e78e1c88b239509f36fd42623b5c28ef` | Position-sweep summary (20 cells: 10 single injection positions x 2 doses, band L8-11, qwen3-1.7b): a single consolidation site at position K=24 passes the dissociation gate at both doses; every other position reads at noise; continuation intact throughout. |
| PM-66 | 2026-07-07 | `7c27f1db` | `f8b7dba7cb45d1b686ad4c6f9bfe809f2c4b038cd4c6fb5b6875794c670965e7` | Position-sweep cell artifact: K=24, alpha 0.25 - real +0.5734 nats vs null -0.0055, verdict workspace_dissociation. |
| PM-67 | 2026-07-07 | `7c27f1db` | `002851ea677740d46687226a2e9f8dde8bfebf7f5184890d9505ddd40bf4b33a` | Position-sweep cell artifact: K=24, alpha 1.0 - real +1.5190 nats vs null +0.0250, verdict workspace_dissociation. |

Machine-readable mirror of this update: the `updates` block and the tagged
entries (`"update": "2026-07-07-2"`) in
[`priority_manifest.json`](priority_manifest.json).

---

## Update 2026-07-07 (3) — appended entries PM-68..PM-86 + third repo-HEAD binding

**Appended 2026-07-07T21:54:09Z (UTC).** Same issuer, hash rule, and verification protocol as the
header; nothing above the previous update was edited. **Third private
repo-HEAD binding:** `e23f054dc3a8c790f365fb159888ae3beef9d6b0`
(2026-07-07T17:43:00-04:00). **This update resolves the RESULTS.md §6
PRELIMINARY exactly as promised:** the int4-window artifacts are now committed
(PM-68, PM-71). It also commits the E1 Stage-C **double-negative reinjection
verdict** (PM-75..PM-82), the marker-hygiene **rescore bundle** (PM-83 — a
deterministic multi-file digest; rule stated in the entry), and the A/B binary
timing record (PM-84..PM-86).

| id | date | private commit | sha256 | description |
| --- | --- | --- | --- | --- |
| PM-68 | 2026-07-07 | `99ccb6c8` | `6a4d3263b1d5039350f0d80936682518fcb185e7ecc6e34b25fac5cafc74475a` | E1 Stage-A cell: the dissociation window ON the production-representative int4 pack with its own concept pack - real +9.4191 vs null +1.3503 nats (margin +8.07), verdict workspace_dissociation, continuation intact. Resolves the former PRELIMINARY +8.07 reading as promised. |
| PM-69 | 2026-07-07 | `99ccb6c8` | `273cdcefd9fbc2decea7e7072c1dd11ec401170b3c97552e49ffe6a68f70e301` | E1 Stage-A cell: int4 pack at alpha 0.5 - joint_flip under original scoring (see the rescore bundle, PM-83). |
| PM-70 | 2026-07-07 | `99ccb6c8` | `833df5679f4abe943cf64e63c41c5d23d5a010a804d9a5db551d6a520f6b8aae` | E1 Stage-A cell: int4 pack at alpha 1.0 - joint_flip under original scoring. |
| PM-71 | 2026-07-07 | `99ccb6c8` | `7dc4d4c3ee95a93d0ed0c8e60a3ee23ea2840076fd9f267b6b086d5b8617f8c0` | E1 Stage-B transfer cell: bf16-extracted concept pack injected into the int4 model - real +9.5005 vs null +0.3599 nats (margin +9.14), workspace_dissociation: concept directions are precision-portable. |
| PM-72 | 2026-07-07 | `99ccb6c8` | `1e24bb246c225e585f820a75e384c0c8096986bd2925c6c33923c65493433b78` | E1 Stage-A cell: per-tensor int4 - the report channel is dead at baseline (log-odds -0.4493 vs -16.52 on bf16, i.e. near chance before any injection); verdict null_confounded; continuation indeterminate. |
| PM-73 | 2026-07-07 | `99ccb6c8` | `fd239cb3ef77b407b26e1e89e5e9e0433f0a6b9b81dd5076da250539da3fe308` | Concept-vector pack extracted from the production-representative int4 model (content private). |
| PM-74 | 2026-07-07 | `99ccb6c8` | `ca5663afec6cf53c1140ddb163f63e6fc5c091e9c1a19e04b68d717b28fb9246` | Concept-vector pack extracted from the per-tensor int4 model (content private). |
| PM-75 | 2026-07-07 | `e23f054d` | `64646a391d116b3c140ec16f93fdaa8de3cbf369bc8899dd9a7379afc9e2a450` | E1 Stage-C reinjection cell: REAL residual reinstated at the top residual-norm attention-value-projection band - window margin +7.80 (real +9.0652 / null +1.2630). |
| PM-76 | 2026-07-07 | `e23f054d` | `11fcbce90a18d9b5cc6d907d29d9cf26fbb389ea186934b0c3038411a8b9dd9a` | E1 Stage-C reinjection cell: norm-matched SHUFFLED residual at the same attention-value sites - window margin +7.52; real-minus-null = +0.28 nats (noise; no window restoration). |
| PM-77 | 2026-07-07 | `e23f054d` | `2aaf7e329b80eccfd1202bc33a2dcf2557f8b763fdcd77297e7c8d170b80d338` | E1 Stage-C reinjection cell: REAL residual reinstated at the top residual-norm MLP down-projection band - window margin +8.15. |
| PM-78 | 2026-07-07 | `e23f054d` | `c0207c0ebe7da97e0f5948b07c46010f000d94ddb99d362b3134173d16e88e73` | E1 Stage-C reinjection cell: norm-matched SHUFFLED residual at the same down-projection sites - window margin +8.35; real-minus-null = -0.20 nats (the null restored more than the real). |
| PM-79 | 2026-07-07 | `e23f054d` | `28d461f4fb75776c2b208f3ba7a766515581790216356eca3ee11a5496c1fb80` | E1 Stage-C gate battery, attention-value sites, REAL arm: 0/9 broken flexible gates restored; routine 8/8 intact. |
| PM-80 | 2026-07-07 | `e23f054d` | `4eb090a918313a82ab5bd726c93dd982c574d2465cf557ec818982b2412eb972` | E1 Stage-C gate battery, attention-value sites, NULL arm: 0/9 restored; routine 8/8. |
| PM-81 | 2026-07-07 | `e23f054d` | `62345a653c508a1d1da7c572cf07c8462fc8a9cc964317d048f4dfc33f22075e` | E1 Stage-C gate battery, down-projection sites, REAL arm: 0/9 restored; routine 8/8. |
| PM-82 | 2026-07-07 | `e23f054d` | `fe9d23f9ac3f41137c0e2f87d34da144b579bfcba6eaa70595da2bc4f1ea2476` | E1 Stage-C gate battery, down-projection sites, NULL arm: 1/9 (item S04) - the single restoration event of the whole leg occurred on a SHUFFLED-residual arm, i.e. at noise level; routine 8/8. |
| PM-83 | 2026-07-07 | `9357107c` | `d47308e0eabe0dfec5b0cc4a53da75ea953705ac3b09dc9fc272465cf8c0a4ea` | BUNDLE: the marker-hygiene rescore companions (60 files added at the two rescore commits; every affected artifact rescored offline, originals untouched). Bundle rule: sha256 over the newline-joined, name-sorted list of '<sha256(file bytes)>  <basename>' lines, one per *_RESCORED.json file added at the two commits (trailing newline). Under the rescore, exactly three per-band verdicts flip joint_flip -> workspace_dissociation (1.7B whole-context alpha 1.0 band L0-3; qwen3-8b whole-context alpha 0.25 band L24-27; qwen3-8b report-time-only alpha 1.0 band L20-23) - the dissociation window is WIDER at both scales; no verdict weakened. *(second commit for this bundle: e23f054d)* |
| PM-84 | 2026-07-07 | `7f808357` | `6dd45195b13125a5c563354951cd4a30ad9950b984c02b2a0aeb89de370d7bbf` | A/B binary timing record, arm 1: full workspace-map cell re-run on the mainline binary - readouts identical to arm 2. |
| PM-85 | 2026-07-07 | `7f808357` | `6dd45195b13125a5c563354951cd4a30ad9950b984c02b2a0aeb89de370d7bbf` | A/B binary timing record, arm 2: the same cell on the branch binary - readouts identical to arm 1. |
| PM-86 | 2026-07-07 | `7f808357` | `5356193d41929016130f23a068b8254b42aac260f11d7786dc8bf519b82bb21f` | A/B timing log: 133 s vs 1066 s wall (8x) for byte-equal readout payloads - recorded as an honest performance-anomaly note (content private; hash-only). *(hash-only)* |

Machine-readable mirror: the second `updates` element and the tagged entries
(`"update": "2026-07-07-3"`) in [`priority_manifest.json`](priority_manifest.json).

---

## Update 2026-07-07 (4) — appended entry PM-87 + fourth repo-HEAD binding

**Appended 2026-07-07T22:40:00Z (UTC).** Same issuer, hash rule, and verification protocol as the
header; nothing above the previous update was edited. **Fourth private
repo-HEAD binding:** `20992e97b98ecbcf6f1a2e54c2187d4c5f05e69a`. This update
binds the E2 attention-free workspace cells (Mamba2-780M, RWKV7-0.4B — RESULTS.md
§10) and the cross-lens equivalence (J-Lens vs activation-difference — RESULTS.md
§11) as a single deterministic bundle.

| id | date | private commit | sha256 | description |
| --- | --- | --- | --- | --- |
| PM-87 | 2026-07-07 | `20992e97` | `b5a38239b8361891f8d1d346c640b63544c2908643b9960aac2baa9ef2df8dd0` | BUNDLE: the E2 attention-free workspace cells + the cross-lens equivalence pack (17 files added at commit `20992e97`: the Mamba2-780M and RWKV7-0.4B intervene artifacts + concept packs + weight-provenance record; the J-Lens-vs-activation-difference comparison + geometry + per-α J-Lens cells + packs; and the scale-ladder note). Bundle rule: sha256 over the newline-joined, name-sorted list of `<sha256(file bytes)>  <basename>` lines, one per file added at the commit (trailing newline). Content: attention-free dissociation on Mamba2 (L12-15/L16-19: real +0.64/+1.86 vs null ~-0.13/-0.09) and RWKV7 (L4-7/L8-11: real +0.86/+1.13 vs null ~+0.08); cross-lens — J-Lens and activation-difference swap vectors both produce null-gated dissociation at L8-11 (J-Lens real +1.27 vs null +0.087 at α0.0625; activation-diff +11.03 vs +1.06 at α0.25). Seam commit for the non-transformer path: `a101cd44`. |

Machine-readable mirror: the third `updates` element and the tagged entry
(`"update": "2026-07-07-4"`) in [`priority_manifest.json`](priority_manifest.json).
