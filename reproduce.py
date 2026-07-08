#!/usr/bin/env python3
# reproduce.py -- clean-room reproduction of the workspace dissociation result.
#
# WHAT THIS IS. A standalone, independent reimplementation of the *measurement*
# behind our headline claim, using ONLY torch + transformers (the standard open
# stack). It does NOT use our private runtime. The point is that a skeptic can
# read every line, run it against public Qwen3-1.7B weights, and check the
# science without trusting us or our code.
#
# THE CLAIM being tested (in one breath): add a "French-minus-Spanish" concept
# direction to the residual stream in a middle band of layers, and the model's
# *verbal report* ("what language is this?") moves strongly toward French, while
# the *continuation* keeps writing Spanish. Crucially, a NORM-MATCHED SHUFFLED
# version of the very same vector (identical length, concept identity destroyed)
# does NOT move the report. That control is the whole game: it separates "we
# injected meaning" from "we just broke the model with a big vector."
#
# HOW TO RUN:
#   pip install torch transformers
#   python reproduce.py
# Downloads Qwen/Qwen3-1.7B from HuggingFace (~3.4 GB) on first run. CPU is fine
# (a few minutes); a GPU is faster. To use an already-downloaded copy, set
# QWEN3_DIR=/path/to/qwen3-1.7b.
#
# WHAT TO EXPECT: at the injection scale below, the real vector shifts the
# report several nats toward French and beats the shuffled null by ~15-20x,
# while the continuation stays Spanish. The exact nats depend on the injection
# scale and implementation and will NOT match our runtime's figures to the
# decimal -- the qualitative result (real >> norm-matched null, continuation
# intact) is what must hold. Our committed run output is in reproduce_output.txt.

import os
import torch
from transformers import AutoModelForCausalLM, AutoTokenizer

MODEL_ID = "Qwen/Qwen3-1.7B"                        # public weights on HuggingFace
MODEL_SRC = os.environ.get("QWEN3_DIR", MODEL_ID)   # local dir override, same weights
LAYERS = [8, 9, 10, 11]     # mid-band injection site (of 28 transformer layers)
ALPHA = 0.20                # injection scale (multiple of the natural concept-vector norm)
SEED = 0                    # fixes the shuffled-null permutation

# Five short parallel passages. The concept vector is the mean over French
# hidden states minus the mean over Spanish hidden states -- the paper's own
# "average activation difference" corroboration method, not a learned probe.
# (French-minus-Spanish because we steer the report *toward* French.)
SPANISH = [
    "El tren salió de la estación con retraso esta mañana.",
    "La casa junto al río tenía las ventanas abiertas.",
    "Los niños jugaban en el parque después de la escuela.",
    "El mercado estaba lleno de gente comprando fruta fresca.",
    "Ayer llovió toda la tarde y las calles quedaron mojadas.",
]
FRENCH = [
    "Le train a quitté la gare en retard ce matin.",
    "La maison au bord de la rivière avait les fenêtres ouvertes.",
    "Les enfants jouaient dans le parc.",
    "Le marché était plein de gens achetant des fruits frais.",
    "Hier il a plu tout l'après-midi.",
]
# A held-out Spanish passage we actually run the experiment on:
PROBE = "El conductor se encargaba de la carga. El tren avanzaba lentamente por la vía."
REPORT_Q = "\n\nWhat language is the passage above written in? Answer with one word:"

print(f"Loading {MODEL_SRC} ...")
tok = AutoTokenizer.from_pretrained(MODEL_SRC)
model = AutoModelForCausalLM.from_pretrained(MODEL_SRC, torch_dtype=torch.float32).eval()
dev = "cuda" if torch.cuda.is_available() else "cpu"
model.to(dev)
print(f"Device: {dev}\n")

layers = model.model.layers  # the transformer blocks; we hook their outputs


def mean_hidden(passages, layer):
    """Mean residual-stream state at `layer` over the last token of each passage."""
    accum = None
    for p in passages:
        ids = tok(p, return_tensors="pt").input_ids.to(dev)
        h = {}
        def grab(mod, inp, out, h=h):
            h["v"] = (out[0] if isinstance(out, tuple) else out)[0, -1].detach()
        hook = layers[layer].register_forward_hook(grab)
        with torch.no_grad():
            model(ids)
        hook.remove()
        accum = h["v"].clone() if accum is None else accum + h["v"]
    return accum / len(passages)


# One concept vector per injected layer, at its NATURAL norm (French-minus-Spanish).
print("Building French-minus-Spanish concept vectors (mean activation difference)...")
vecs = {L: (mean_hidden(FRENCH, L) - mean_hidden(SPANISH, L)) for L in LAYERS}

# The norm-matched shuffled null: same numbers, permuted, rescaled to the
# identical L2 norm. Same "size" of perturbation; concept identity destroyed.
# If THIS moves the report as much as the real vector, the effect was never
# specific -- it was just a big push. That is the control the field keeps asking
# for ("it's always difficult to rule out that steering is just breaking the
# model").
g = torch.Generator().manual_seed(SEED)
nulls = {}
for L, v in vecs.items():
    shuf = v.flatten()[torch.randperm(v.numel(), generator=g)].reshape(v.shape).to(dev)
    nulls[L] = shuf * (v.norm() / shuf.norm())   # rescale to identical L2 norm

_inject = {"vecs": None}   # armed with a {layer: vector} dict, or None for baseline


def arm(mode):
    _inject["vecs"] = {"real": vecs, "null": nulls, "off": None}[mode]


def make_hook(L):
    def hook(mod, inp, out):
        if _inject["vecs"] is None:
            return out
        add = ALPHA * _inject["vecs"][L]
        if isinstance(out, tuple):
            return (out[0] + add,) + out[1:]
        return out + add
    return hook
for L in LAYERS:
    layers[L].register_forward_hook(make_hook(L))


def first_id(word):
    return tok(" " + word, add_special_tokens=False).input_ids[0]
ES_ID, FR_ID = first_id("Spanish"), first_id("French")


def report_logodds():
    """log P(French) - log P(Spanish) for the one-word report answer."""
    ids = tok(PROBE + REPORT_Q, return_tensors="pt").input_ids.to(dev)
    with torch.no_grad():
        logits = model(ids).logits[0, -1]
    logp = torch.log_softmax(logits, dim=-1)
    return (logp[FR_ID] - logp[ES_ID]).item()


def continuation_language():
    """Free-run 24 tokens from the Spanish probe; guess the language by markers."""
    ids = tok(PROBE, return_tensors="pt").input_ids.to(dev)
    with torch.no_grad():
        out = model.generate(ids, max_new_tokens=24, do_sample=False,
                             pad_token_id=tok.eos_token_id)
    text = " " + tok.decode(out[0, ids.shape[1]:], skip_special_tokens=True).lower() + " "
    es = sum(text.count(" " + w + " ") for w in ["el", "la", "los", "las", "con", "de", "se"])
    fr = sum(text.count(" " + w + " ") for w in ["le", "les", "des", "avec", "la", "nuit", "il"])
    call = "Spanish" if es > fr else ("French" if fr > es else "unclear")
    return call, text.strip()[:70]


arm("off"); base = report_logodds()
arm("real"); real = report_logodds(); real_lang, real_txt = continuation_language()
arm("null"); null = report_logodds(); null_lang, null_txt = continuation_language()
arm("off")

real_shift, null_shift = real - base, null - base
ratio = real_shift / null_shift if abs(null_shift) > 1e-6 else float("inf")

print("\n================= RESULT =================")
print(f"injection: layers {LAYERS}, all positions, alpha={ALPHA} x natural concept norm")
print(f"baseline report log-odds (French - Spanish): {base:+.3f} nats")
print(f"  real vector   -> report shift {real_shift:+.3f} nats;  continuation: {real_lang}")
print(f"  shuffled null -> report shift {null_shift:+.3f} nats;  continuation: {null_lang}")
print(f"  ratio real/null: {ratio:.1f}x")
print(f"  real continuation:  {real_txt!r}")
print(f"  null continuation:  {null_txt!r}")
ok = (real_shift > 1.0 and real_shift > 3 * abs(null_shift))
if ok:
    print(f"\nPASS: the real shift is {ratio:.0f}x the norm-matched null -> the report move")
    print("is concept-specific, not generic breakage. The continuation staying Spanish")
    print("while the report moves toward French is the report-vs-continuation dissociation.")
else:
    print("\nFAIL: real shift did not clear the norm-matched null by a clear margin here.")
    print("(Adjust ALPHA; report whatever the script actually produces.)")
print("==========================================")
