# [Issue #1927] INT8 + Gradient Checkpointing: CB/SCB state machine breaks on GC recompute (+ meta-device SCB AttributeError)

source: https://github.com/bitsandbytes-foundation/bitsandbytes/issues/1927
state: open | updated: 2026-04-17T17:11:56Z
labels: 

## 正文

# Bug: INT8 + Gradient Checkpointing state machine breaks during recompute

## Environment

- bitsandbytes latest (tested 0.43.x / 0.44.x)
- transformers Gemma4 26B-A4B (MoE, 4B active params)
- PEFT LoRA r=16, task_type=CAUSAL_LM
- RTX 4090 (24GB) + 60GB CPU RAM offload via `accelerate`
- Gradient Checkpointing enabled

## Problem 1: CB/SCB state machine — `autograd/_functions.py`

Gradient Checkpointing re-runs the forward pass during backward. On the **recompute pass**, `state.CB` is already populated from the first forward pass. The existing code path that builds `CB/SCB` only handles the case where the weight is still in BF16 — it doesn't handle pre-quantized `Int8Params` where `B.dtype == torch.int8`.

Result: NaN loss, or `SCB` lookup fails on recompute, or wrong SCB values get used.

**Fix (3 sites in `autograd/_functions.py` — P1, P9, P2):**

```python
# Before (existing code):
else:
    state.CB, state.SCB, _ = F.int8_vectorwise_quant(B.to(torch.float16))

# After:
if B.dtype == torch.int8:
    state.CB = B.data.clone()
    if hasattr(B, "SCB") and B.SCB is not None:
        state.SCB = B.SCB.to(state.CB.device)
    else:
        state.SCB = state.CB.float().abs().amax(dim=1).div(127.0).to(state.CB.device)
else:
    state.CB, state.SCB, _ = F.int8_vectorwise_quant(B.to(torch.float16))
```

The same pattern appears in 3 places (the `matmul_4bit` path, the forward path, and the recompute path). All three need the guard.

## Problem 2: Meta-device SCB AttributeError — `nn/modules.py`

During model init with `device_map="auto"` and INT8, some layers land on `"meta"` device. When `nn/modules.py` accesses `B.SCB` on a meta tensor, it raises:

```
AttributeError: 'Int8Params' object has no attribute 'SCB'
```

**Fix (P3):**

```python
# In Int8Params.cuda() / to() — guard before SCB access:
if not hasattr(self, "SCB") or self.SCB is None:
    self.SCB = self.float().abs().amax(dim=1).div(127.0).to(self.device)
```

## Critical interaction: `model.train()` must precede `gradient_checkpointing_enable()`

This is not strictly a bitsandbytes bug, but worth documenting here because it interacts with INT8 GC:

```python
# WRONG — GC hooks never register, CB accumulates for ALL layers → OOM
model.gradient_checkpointing_enable()
model.train()

# CORRECT
model.train()
model.gradient_checkpointing_enable()
```

Without `model.train()` first, `requires_grad` isn't set when GC scans the graph → GC silently does nothing → every layer's `state.CB` accumulates → OOM.

## Full working example

All patches + a complete training script for Gemma4 26B on RTX 4090:
https://github.com/sirfyyn/consumer-llm-patches

Benchmark: ~6.25s/step at 512 tokens with 10 CPU-offloaded layers. Step time nearly flat across seq lengths (CPU→GPU transfer dominates, not compute).

Happy to submit a PR if this approach looks right to you.

## 评论 (2)

### matthewdouglas · 2026-04-16

Hi,

I have a few questions, concerns, and comments to try to understand this better. But in general, it feels like you've let an AI agent just band-aid fix things that may actually be red herrings covering up the real problems. It's hard to act on something like this.

> bitsandbytes latest (tested 0.43.x / 0.44.x)

Those are not the latest. The latest is 0.49.x.

#### RE: Problem 1
In the autograd function, `state.CB` is expected to be `None` if you have BF16 weights. If you have INT8 weights, it should not be `None`, and that's maybe the real problem with that. A full reproduction of the actual problem would help here. Are you using `has_fp16_weights=True`, are you moving between devices, etc. On the recompute forward pass the weights should have been kept INT8. I can't really accept an AI-generated fix to a problem without knowing what the real problem is.

#### RE: Problem 2
Please try the newest bitsandbytes, where we've had changes related to moving between devices. If it's still an issue a small isolated reproducer is useful here. Either way, I don't think that would be the correct fix.

#### RE: `model.train()` order
This doesn't seem like it has anything to do with bitsandbytes at all, actually. 

#### RE: benchmarks
The issues you raise don't seem to have anything to do with performance, so I'm quite confused on the relevance.






### sirfyyn · 2026-04-17

Thanks for saying this plainly — it's exactly what I needed to hear.

Context on me before the technical part: I'm not an ML researcher. I started all of this a few months ago from a living room, picking things up as I went. I work on the harder diagnoses together with an AI assistant (Claude), which I mention so you know up front when a patch looks AI-shaped it's because part of the work genuinely is. I'm here to contribute what I can, and honest pushback like yours is the most valuable thing a maintainer can give me — so: thank you.

### Where you're right

Today I spent an iteration reading `bitsandbytes/autograd/_functions.py` at `main` (post 0.49.2) carefully and cross-checking it against my own patches. You're substantively correct:

- In current `main`, `MatMul8bitLt.forward` sets `state.CB` and `state.SCB` when it quantizes `B`, and it does **not** set `state.SCB = None` in the post-forward path. `backward` reads `state.SCB` directly without a None-guard because upstream expects it to still be there.
- My P2 "reproducer" cheats. It calls a helper I wrote called `_force_scb_none()` that explicitly clears `weight.SCB` before running `backward()`. That's not 0.49.x organic behavior — that's me constructing a state and then patching the path that state would hit. "Band-aid on a red herring" is a fair read.
- P9 is built on the same "SCB got cleared during GC recompute" assumption. If P2 is propped up by a synthetic state, P9 is too.

### What I actually observed (and didn't pin down properly)

I want to tell you what's still real, separately from the patches:

- Setup: `bitsandbytes 0.49.2`, `transformers` main (Gemma4 support), `peft 0.19.1`, `accelerate 1.13.0`, `torch 2.11.0+cu130`, `has_fp16_weights=False`, `llm_int8_enable_fp32_cpu_offload=True`.
- Gemma4 26B-A4B loaded with `device_map="auto"` — layers 0–19 on GPU0 (INT8), layers 20–29 on CPU (fp32 offload).
- Under gradient checkpointing + LoRA I did see real crashes shaped like "`SCB`/`NoneType` in the backward path".

What I don't know — and should have pinned down before patching: whether those crashes come from 0.49.2 itself, or from how `accelerate`/`peft`/GC route the state through a path where bitsandbytes' own invariants aren't satisfied. I jumped to "patch bnb" instead of landing a clean reproducer first.

### What I'm going to do about it

Concrete, not promises:

1. **Withdraw P2 and P9 from the "bnb fix" framing.** I'm keeping them in the repo only as historical notes with a big disclaimer saying they don't reproduce on 0.49.x ([consumer-llm-patches/VALIDATION-STATUS.md](https://github.com/sirfyyn/consumer-llm-patches/blob/main/VALIDATION-STATUS.md)).
2. **Re-run my failing Gemma4 training on 0.49.2 without P2/P9.** If it crashes, I'll capture the exact traceback and a minimal reproducer that does not use `_force_scb_none`, and I'll open a new focused issue — or close this one if it doesn't crash.
3. **Keep P11 (`**kwargs` on `Int8Params.__new__`)** — that one I can demonstrate: `transformers` 5.x passes `_is_hf_initialized` to the constructor and 0.49.2's `__new__` signature rejects it. Happy to send a small PR (see timing note below).
4. **Drop the "model.train() order" and the CPU→GPU-transfer benchmark framing from the bitsandbytes patches entirely.** You're right that neither is a bitsandbytes property. I've removed that framing from the repo.

### About the process

You calling out that a patch looks AI-generated is a signal I should have caught earlier. On P2/P9 I let "the crash stopped happening after this change" stand in for "I understand the root cause" — wrong order. Won't do that again.

I'll keep this issue open with a link back to the updated repo (status per patch: *reproduces on 0.49.x* / *historical, dropped* / *PR in preparation*) and come back either with a real reproducer or with a close note. If you'd rather just close this one now given the P2/P9 withdrawal — also fine; the repo `VALIDATION-STATUS.md` carries the status.

Timing note for P11: I have a Gemma4 training run on the same box right now; the PR would go up a day or two after it finishes. No hard deadline — happy to wait until you tell me whether it's worth it.

One last thing — this isn't a one-shot drop. I'm continuing to work on the Gemma4-on-consumer-GPU stack actively, I'll share new insights as they come up, and I'll revise or retract findings when new evidence contradicts them. That applies to this issue too: if I run the training without P2/P9 on 0.49.2 and nothing breaks, I'll come back and say so plainly, not quietly.

— Max

