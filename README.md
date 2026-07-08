# A language model reports one language while writing another — and we can move the report without moving the writing

Give a language model a Spanish passage and ask "what language is this?" — it says
Spanish. Now, inside the model, add a small "French-minus-Spanish" direction to the
middle layers. Ask again: it now says **French** — while it keeps *writing* fluent
Spanish. The thing it *says about* the text and the thing it *does with* the text have
come apart. This mirrors Anthropic's 2026 "global workspace" finding, and we add the one
control that makes it a real result: a **norm-matched shuffled** version of the same
injected vector (same size, meaning scrambled) barely moves the report at all. So the
report moved because of *what* we injected, not just because we perturbed the model.

## Reproduce it yourself

No account, no private code. Just the open stack:

```
pip install torch transformers
python reproduce.py
```

[`reproduce.py`](reproduce.py) is ~120 commented lines using only `torch` +
`transformers` against public `Qwen/Qwen3-1.7B`. It builds the concept vector from five
short Spanish/French sentence pairs, injects it at layers 8–11, and prints both arms.
Expected shape (our actual CPU run is in [`reproduce_output.txt`](reproduce_output.txt)):

```
baseline report log-odds (French - Spanish): -8.5 nats
  real vector   -> report shift +2.4 nats;  continuation: Spanish
  shuffled null -> report shift +0.04 nats; continuation: Spanish
  ratio real/null: ~55x   ->  PASS
```

The absolute numbers depend on the injection scale and will not match to the decimal —
what must hold is **real ≫ norm-matched null, with the continuation unchanged**. Turn the
scale up and the continuation flips too (joint steering): a dose–response with a real
boundary. Read every line and decide for yourself.

## The honest score

Stated plainly, so nobody has to dig for it:

- **Weight-space carriers found: zero.** We hunt for specific stored weights that carry a
  behavior, always against a shuffled-null control. So far none has beaten its null —
  including a paid, full-instrument negative on gemma OCR, and a reinjection test where
  the real deleted weights restored *nothing the shuffle didn't*. We publish these
  negatives.
- **Activation-space dissociations found: one**, null-gated, existence-level (the result
  above). It reproduces at a second model size (qwen3-8b) and, more surprisingly, in
  **attention-free** architectures (Mamba2, RWKV7) — see [`RESULTS.md`](RESULTS.md).
- Two earlier research phases were closed as a **terminal negative** and a
  **STOP-UNDERPOWERED**, both written up rather than buried.

A method whose controls have never rejected anything is advertising, not measurement.

## What's in this repo

| File | What it is |
| --- | --- |
| [`reproduce.py`](reproduce.py) / [`reproduce_output.txt`](reproduce_output.txt) | Clean-room reproduction + our actual run output |
| [`RESULTS.md`](RESULTS.md) | All result tables: the dissociation dose-response, scale (8b), attention-free models, cross-lens, int4 |
| [`POSITION_NOTE.md`](POSITION_NOTE.md) | The full write-up: how this relates to the workspace paper, the metrology, what we do and don't claim |
| [`AUTHORS.md`](AUTHORS.md) / [`LICENSE`](LICENSE) / [`NOTICE.md`](NOTICE.md) | Authorship, license, permitted-use |

We take no position on consciousness; this is measurement of which internal directions
are causally necessary for which behaviors, under controls.

Contact: open an issue on this repository.

---

## Provenance & priority record (for dating, not for reading)

The material below exists to timestamp what we had committed and when. It is archival —
skip it unless you specifically need to check a date or verify an artifact hash under
disclosure.

The full experiments run on a private research repository. This public repository carries
a **cryptographic priority record** — sha256 commitments to the private documents and run
artifacts — so that priority is provable without disclosing the private material. A hash
commits us to content; it discloses nothing.

- [`PRIORITY_MANIFEST.md`](PRIORITY_MANIFEST.md) / `priority_manifest.json` — the sha256
  commitments behind every claim, in dated append-only updates.
- [`TIMELINE.md`](TIMELINE.md) — dated narrative from the program's first formulation
  (2026-05-06) to the present; private rows are hash-committed, public-only rows labeled
  separately.
- `PUBLIC_UPDATE_V0_4.md` / `LEVEL1_ATTESTATION_GPT2_V0_4.md` — earlier public
  authorship/attestation companions.

**Claim tags used throughout:** [committed] = proven at the stated scope by a run
artifact or verdict at a cited commit, whose content hash is committed here;
[preregistered] = a frozen, hash-committed design whose evaluation has not run; [planned]
= a dated intention, never presented as a result.

Authored by Gleb Stepanov, founder of XNN LLC (Georgia, USA), an independent R&D company —
not an academic lab. LLM systems assist with writing and code; the authority for any claim
is the evidence record, not credentials.
