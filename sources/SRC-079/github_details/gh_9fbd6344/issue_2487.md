# [Issue #2487] Repeated "intermediate output already stored" warnings during gradient accumulation

source: https://github.com/NVIDIA/Model-Optimizer/issues/2487
state: open | updated: 2026-09-22T14:16:13Z
labels: bug

## 正文



## Describe the bug

I noticed that when training with gradient accumulation (`gradient_accumulation_steps=8`), both the teacher and student's wrapped modules repeatedly emit the following warnings on nearly every step:

```text
UserWarning: Teacher's Module `Qwen2ForCausalLM` already has an intermediate output stored.
This is expected when `DistillationModel.compute_kd_loss` is not called in eval mode.

UserWarning: Student's Module `DistillQwen2ForCausalLM` already has an intermediate output stored.
This is undesired behavior unless Activation Checkpointing is in use.
```

I may be misunderstanding the intended behavior here, so I wanted to ask whether these warnings are expected during normal gradient accumulation.

**Impact:** Nice to have / clarity issue. Training continues, but the warnings appear very frequently and make it difficult to distinguish them from potentially important training warnings.

In particular, the second warning mentions that the behavior is "undesired" unless Activation Checkpointing is being used. I would appreciate clarification on whether this indicates an actual correctness or memory issue in this configuration.

### Steps/Code to reproduce bug

1. Wrap a student model with `mtd.convert(..., mode=[("kd_loss", {...})])` as in the configuration above.

2. Train using `Trainer` with:

```python
TrainingArguments(
    per_device_train_batch_size=1,
    gradient_accumulation_steps=8,
    ...
)
```

3. Activation checkpointing is **not** enabled in this configuration.

4. Observe the warnings being emitted repeatedly during the micro-batch forward passes.

### Expected behavior

Could you please clarify whether these warnings are expected when using gradient accumulation without activation checkpointing?

If this is expected behavior, it would be helpful if the documentation could explain why the intermediate output is stored and confirm whether it is safely overwritten for each micro-batch rather than being incorrectly reused.

Alternatively, if these warnings indicate an issue with the current configuration, I would appreciate any guidance on the recommended setup.

### Who can help?


## System information

* Container used (if applicable): none / bare venv
* OS: Ubuntu Linux
* CPU architecture: x86_64
* GPU name: NVIDIA DGX B200
* GPU memory size: 192GB
* Number of GPUs: 1
* Library versions:

  * Python: 3.12.3
  * ModelOpt version or commit hash: 0.46.1
  * CUDA: 13.2.86
  * PyTorch: 2.12.0.dev20260408+cu128
  * Transformers: 5.14.1
  * TensorRT-LLM: N/A
  * ONNXRuntime: N/A
  * TensorRT: N/A
* Any other details: `gradient_accumulation_steps=8`, `per_device_train_batch_size=1`, activation checkpointing disabled.


## 评论 (2)

### Edwardssss · 2026-09-21

Thanks for the detailed report and reproduction steps — that made this straightforward to pin down. I reproduced it on current `main`, and the trigger looks different from `gradient_accumulation_steps`.

Counting the `"already has an intermediate output stored"` warning over a fixed 16 micro-batch forwards with a plain `Trainer`:

| `gradient_accumulation_steps` | micro-batch forwards | optimizer steps | warnings |
|---|---|---|---|
| 1 | 16 | 16 | 30 |
| 4 | 16 | 4 | 30 |
| 16 | 16 | 1 | 30 |

The count follows forwards, not steps: the first forward is silent, and every forward after it warns once per hooked module (15 teacher + 15 student in the run above).

The cause is the capture lifecycle. Both hooks latch `_intermediate_output` on every forward, and the only code that clears it is `DistillationModel.compute_kd_loss()`. A loop that never calls it leaves the capture set, so the next forward reports it — and a plain `transformers.Trainer` is such a loop, because its default `compute_loss` reads the student's own CE from `outputs.loss`.

Your two questions, directly:

- **Is the stored output reused incorrectly?** No. The hook always overwrites it, and `compute_kd_loss()` reads then clears it, so no loss ever consumes a stale activation. It also retains at most one extra activation until the next forward: bounded, not a leak.
- **Is there a real issue here?** The warnings are worth acting on, for a different reason than they suggest: if `compute_kd_loss()` is never called, **no KD loss is applied at all** and training silently falls back to CE. In my setup `train_loss` was 2.2164 without it versus 1.4895 with it. Neither message says this today — the student one points at Activation Checkpointing, and the teacher one calls the situation "expected" while still raising a `UserWarning`.

One note on the frequency you saw: Python deduplicates a warning by (message, location), so under default filters this appears once per message rather than every step. Seeing it repeatedly suggests deduplication was disabled in that run (`-W always`, `PYTHONWARNINGS=always`, pytest, or one warning registry per DDP rank); in those setups the count does scale with epoch length.

I opened #2492, which limits each warning to once per captured activation — re-armed when the capture is cleared, so Activation Checkpointing still reports re-forwards — and rewrites both messages to name the missing `compute_kd_loss()` call and its consequence. If the current wording was deliberate, I am glad to adjust it.

For reference, these hook functions are identical in 0.46.x and `main` — the last change before this one was the layerwise addition in #802 — so this applies to your 0.46.1 as well.

### TheSabari07 · 2026-09-22

Hi @kevalmorabia97, I’d love to work on this issue. If it’s okay, could you please assign it to me?

