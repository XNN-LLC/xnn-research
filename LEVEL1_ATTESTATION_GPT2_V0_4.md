# Level 1 Public Attestation Summary - GPT-2

Public update: v0.4-public, 2026-07-07

This document publishes a sanitized public summary of an internal Level 1
attestation run over `openai-community/gpt2`, using a deterministic,
weight-only Bill of Materials and root fingerprint. It is not a PM-43 manifest
entry, and it should not be read as a new private-manifest commitment. It does
not disclose model payloads, local machine paths, private repository internals,
command logs, or implementation details beyond the public claim boundary below.

## Attestation Summary

| Field | Value |
| --- | --- |
| Model | `openai-community/gpt2` |
| Run date | 2026-07-06 |
| Evidence class | Level 1 model BOM / weight attestation |
| Method scope | Deterministic, weight-only |
| Forward pass | None for this attestation |
| Root fingerprint algorithm | SHA-256 |
| Root fingerprint | `8374b3d401d6c584adbcd085291f020528fba4eee5cb272c57b308bf1d003e22` |
| Independent root agreement | matched: BOM export == weight fingerprint |
| BOM format | CycloneDX 1.5 |
| BOM serial number | `urn:uuid:64f8e763-0903-5bb4-9589-886cd594da1d` |
| Parameters | 137,022,720 |
| Tensors | 160 |
| Shards | 1 |
| Weight bytes hashed | 548,090,880 |
| Byte-addressable coverage | 100.0000% |

## Organ Rollup

| Organ | Tensors | Parameters | Parameter share | Payload bytes |
| --- | --- | --- | --- | --- |
| `h` | 156 | 97,637,376 | 71.26% | 390,549,504 |
| `wte` | 1 | 38,597,376 | 28.17% | 154,389,504 |
| `wpe` | 1 | 786,432 | 0.57% | 3,145,728 |
| `ln_f` | 2 | 1,536 | 0.00% | 6,144 |

All tensors in this run were F32.

## Public Claim Boundary

This v0.4 public summary reports the following narrow claims from the internal
run record:

- Every successfully read tensor payload byte in the safetensors weight file is
  mapped and hashed.
- The root fingerprint is reproducible from the name-sorted per-tensor SHA-256
  leaf digests.
- A byte-identical copy of the same weights reproduces the same root
  fingerprint.
- A changed tensor payload changes that tensor leaf digest and therefore changes
  the root fingerprint.
- The BOM export and independent weight-fingerprint path agreed on the same
  root fingerprint.
- The byte-addressability coverage for the weight payload is 100.0000% for this
  run.

## Not Claimed

This attestation does not claim:

- tokenizer, config, generation-template, chat-template, or executable-code
  coverage;
- behavioral equivalence, safety, alignment, restoration, or runtime behavior;
- a binary Merkle tree with public inclusion proofs;
- any causal-carrier, semantic-surgery, or global-workspace result;
- any public disclosure of the private repository, model-store layout, local
  paths, command logs, or implementation internals.

The root is reported as a flat hash over sorted tensor leaf digests. It is
useful for
tamper-evident identity and byte-level auditability, not as a behavioral model
certificate.

## Public Boundary

This is a public Level 1 evidence surface: a model can be treated as an
auditable byte object before any stronger interpretability or behavioral claim
is made. Higher-level claims require separate evidence classes and separate
claim boundaries.

The private working record contains the full local run evidence. This public
document intentionally publishes only the sanitized summary needed to describe
the v0.4-public attestation surface without disclosing private paths, raw
weights, scripts, logs, or trade-secret details. The public git commit that
adds this file is the public timestamp for this summary.
