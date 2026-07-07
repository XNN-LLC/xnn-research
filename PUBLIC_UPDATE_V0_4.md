# Public Update v0.4

Date: 2026-07-07

This public update adds explicit authorship, company attribution, and
accountability context to the public priority record.

## What changed

- Added `AUTHORS.md`, naming Gleb Stepanov as primary author, independent
  researcher and developer, and founder/lead developer of XNN LLC, an
  independent research and development company based in Georgia, USA.
- Updated the public position note header to `v0.4-public`.
- Added `LEVEL1_ATTESTATION_GPT2_V0_4.md`, a sanitized public Level 1
  model-BOM / weight-attestation companion for `openai-community/gpt2`.
- Added an LLM-assistance boundary: LLMs may assist with writing, editing, or
  code workflows, but claim authority remains tied to committed artifacts, run
  results, timestamps, sha256 manifests, and reproducible records.

## What did not change

- No private documents were copied into this repository.
- No private implementation internals, model payloads, command flags, machine
  paths, frozen constants, prompts, or trade-secret details were disclosed.
- The scientific body of `POSITION_NOTE.md` remains the public edition of the
  private v0.3 science text; v0.4-public is an accountability and attribution
  update to the public record plus a sanitized Level 1 attestation surface.
- Existing priority-manifest entries remain append-only commitments to the
  private record. This public v0.4 note does not rewrite prior manifest entries.
