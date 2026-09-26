# [Issue #2745] [Bug] `sequential_epoch_end` qparam writeback crashes with `Inplace update to inference tensor outside InferenceMode` on speculative-decode heads (DeepSeek-V4 MTP)

source: https://github.com/vllm-project/llm-compressor/issues/2745
state: closed | updated: 2026-08-05T18:06:54Z
labels: 

## 正文

## Summary

Calibrating a DeepSeek-V4-class model with the multi-token-prediction (MTP) block in the recipe's quantization scope crashes deterministically at the END of the MTP block's calibration pass:

```
RuntimeError: Inplace update to inference tensor outside InferenceMode is not allowed.
You can make a clone to get a normal tensor before doing inplace update.
See https://github.com/pytorch/rfcs/pull/17 for more details.
```

The crash fires inside `compressed_tensors.distributed.utils.wait_for_comms` → `comm.wait()` during the `sequential_epoch_end` callback for the MTP block. Layers 0-42 (the main MoE blocks) calibrate cleanly with the same recipe shape; only the MTP block trips this. The MTP forward path in DeepSeek-V4-Flash includes a shared-embedding lookup (`mtp.0.embed.weight` aliases the main model's `embed.weight`) which is the most likely source of an inference-mode-marked tensor downstream — but the precise tensor genesis would need maintainer investigation.

**Two independent workstreams hit this same bug with the same root cause and the same workaround.** This issue plus the H200 W4A16 sibling repo's path (`pasta-paul/dsv4-flash-w4a16-fp8-mtp`) both converged on excluding MTP from the recipe (Option Y) as the fix. That convergence is part of why I'm filing — it's not a one-off.

## Reproducer

- Model: 671B-parameter DeepSeek-V4-Flash, BF16 source, 43 main MoE blocks + 1 MTP block, 256 routed experts per block.
- Hardware: 1× B300 SXM6 AC, on-demand (verified via IMDS).
- `llm-compressor` pin: `0.10.1.dev123+gf2aa32e2` (branch `kylesayrs/transformers-v5`).
- `compressed-tensors`: `0.15.1.a20260515`.
- Recipe (NVFP4 experts + FP8_BLOCK attn + MTP `e_proj`/`h_proj` quantized via `float-quantized`):

```python
QuantizationModifier(
    config_groups={
        "attention": QuantizationScheme(
            targets=[
                r"re:.*\.attn\.(wq_a|wq_b|wkv|wo_a|wo_b)$",
                r"re:.*mtp\.\d+\.(e_proj|h_proj)$",  # <— include MTP in scope
            ],
            format="float-quantized",
            **FP8_BLOCK,
        ),
        "experts": QuantizationScheme(
            targets=[r"re:.*\.ffn\.experts\.\d+\.(w1|w2|w3)$"],  # also matches mtp.0.ffn.experts.*
            format="nvfp4-pack-quantized",
            **NVFP4,
        ),
    },
    ignore=[
        "head", "embed",
        r"re:.*norm.*",
        r"re:.*\.ffn\.gate$",
        r"re:.*\.ffn\.gate\..*",
        r"re:.*\.ffn\.shared_experts\..*",
        r"re:.*\.hc_.*",
        r"re:hc_.*",
        r"re:.*\.attn\.attn_sink$",
        r"re:.*\.attn\.(compressor|indexer)\..*",
    ],
)
```

Launched as `python script.py --samples 64 --max-seq-len 512 --batch-size 1` (single-process; the multi-rank offload-cache deadlock from #2743 is orthogonal and not relevant here).

Sequence:
- Subgraphs 1-43 (main MoE blocks) calibrate and propagate cleanly. Per-subgraph wall ~60-120 s.
- Subgraph 44 (the MTP block) completes its calibration AND propagation passes — both tqdm bars hit 100%.
- `LifecycleCallbacks.sequential_epoch_end(subgraph)` then fires for subgraph 44 and crashes.

## Traceback (verbatim)

```
File ".../llmcompressor/pipelines/sequential/pipeline.py", line 163, in __call__
    LifecycleCallbacks.sequential_epoch_end(subgraph)
File ".../llmcompressor/core/session_functions.py", line 165, in sequential_epoch_end
    return cls.event(EventType.SEQUENTIAL_EPOCH_END, subgraph=subgraph, **kwargs)
File ".../llmcompressor/core/session_functions.py", line 91, in event
    return active_session().event(event_type, **kwargs)
File ".../llmcompressor/core/session.py", line 181, in event
    mod_data = self._lifecycle.event(...)
File ".../llmcompressor/core/lifecycle.py", line 204, in event
    data = mod.update_event(state=self.state, event=event, **kwargs)
File ".../llmcompressor/modifiers/modifier.py", line 122, in update_event
    self.on_event(state, event, **kwargs)
File ".../llmcompressor/modifiers/quantization/quantization/base.py", line 104, in on_event
    QuantizationMixin.sync_activation_observers(self, state.model)
File ".../llmcompressor/modifiers/quantization/quantization/mixin.py", line 288, in sync_activation_observers
    wait_for_comms(pending_comms)
File ".../compressed_tensors/distributed/utils.py", line 116, in wait_for_comms
    comm.wait()
RuntimeError: Inplace update to inference tensor outside InferenceMode is not allowed.
```

Note that `wait_for_comms` is being called with a **non-empty** `pending_comms` list even though our run had `Observer.synchronize` monkey-patched to return `[]` (see #2734 for that workaround's context). Something else queues a `dist.Work` that survives until `wait_for_comms`. Maintainer guidance on which observer/path that is would help isolate the root cause.

## Hypothesis on root cause

The MTP block's forward path in the vendored upstream model creates intermediate tensors under `torch.inference_mode()` — almost certainly because of the shared-embedding lookup (`mtp.0.embed.weight` aliases the main model's `embed.weight`, and the embedding `forward` is wrapped in `inference_mode` somewhere). When the quantization observer state propagates to a `weight_scale` / `weight_zero_point` writeback during `sequential_epoch_end`, the target parameter has been marked as an inference tensor, and the in-place update (the `comm.wait()` finalizing an `all_reduce`) trips the safety check.

This is consistent with how `inference_mode()` marks tensors and how the error message points at PyTorch RFC #17.

## Workaround (Option Y)

Both workstreams excluded MTP from the recipe entirely:

```python
ignore=[
    ...,
    r"re:.*mtp\..*",  # skip ALL MTP modules
]
```

The MTP weights ship BF16 (unquantized) in the artifact. They are still PRESENT (not dropped like stock HF transformers does via `_keys_to_ignore_on_load_unexpected`), and load cleanly in vLLM with `--speculative_config method=mtp`. For the artifacts I'm shipping, the differentiator is **presence**, not **precision**, so this is acceptable.

For users who actually need a quantized MTP block, this workaround doesn't apply.

## Asks

- **Documented:** "Speculative-decode heads (MTP-style) with shared-embedding lookups may need to be excluded from the quantization recipe via `ignore` until upstream resolves the inference-tensor interaction." A docs line + maybe a runtime warning when a recipe targets `*mtp*` / `*medusa*` / similar would catch users before they burn an hour of calibration.
- **Investigated:** trace which observer creates the lingering `dist.Work` that survives the no-op `synchronize` monkey-patch, and trace which write in the qparam-writeback path lands on an inference-mode tensor. The clone-before-update fix the error message suggests would live somewhere in `compressed_tensors.quantization.lifecycle.forward.update_offload_parameter` or its callee.
- **Tested:** a small integration test that runs `oneshot` against a 2-layer toy model with one speculative-decode-head-style block (shared embedding, e_proj/h_proj) would catch this on future branches.

## Diagnostic data available

Full log (`phase2b_1rank_mtp_inferencemode_crash_20260521T005306Z.log`), per-subgraph progress markers, and the in-script monkey-patches for `Observer.synchronize` + `modify_save_pretrained` + device-relocation + per-subgraph progress preserved on the B300 box at `/data/nvfp4-mtp/`. Happy to share or run additional probes if helpful.

cc @kylesayrs — this is adjacent to the `propagate_error` work (#2008) but a separate code path. Filing because the convergent independent reproducers from two workstreams suggested it's worth getting on the radar.

## 评论 (9)

### qubeena07 · 2026-07-28

Hi, I would like to work on this issue. My plan is to first build a small CPU only repro since the inference tensor rule is not NCCL specific, so I should be able to reproduce it with a toy model and torch distributed at world size one using the gloo backend. That should confirm whether a stat tensor is getting created inside inference_mode during a forward hook and then mutated in place later outside inference_mode during sequential_epoch_end. If that is the root cause, the fix would be to clone the tensor before the collective and rebind the attribute after the wait completes, rather than mutating the original tensor in place. Will share an update once I have a working repro and a proposed patch.

### brian-dellabetta · 2026-07-29

Hi @qubeena07 , your plan sounds good to me -- a working repro with a small model would be a great place to start. I will assign this to you, thanks!

### qubeena07 · 2026-07-29

Following up with the working small model repro you asked for.

I built a tiny toy model that mirrors the two things I think matter here: a main path whose forward is decorated with torch.inference_mode(), same as the vendored DeepSeek V3.2 Transformer.forward in this repo at src/llmcompressor/modeling/deepseekv32/model.py line 845, and an auxiliary MTP style block that reuses the same embedding module as the main path and consumes the main path hidden states as input, so it receives a tensor that was created inside inference_mode but is now being used outside it.

Ran this through the real GPTQModifier and SequentialPipeline, launched with torchrun so dist is actually initialized. At world size one it completes cleanly end to end, including through sequential_epoch_end for the MTP subgraph.

This lines up with something else I found earlier while trying to reproduce this without multi GPU access: a plain in place op on a tensor created inside inference_mode does crash as expected on its own, but the actual collective call in sync_activation_stats, meaning dist.all_reduce plus wait, does not trigger the crash at world size one with either gloo or NCCL. It looks like a single rank collective effectively does nothing, so nothing ever reaches the checked in place write that trips the guard.

Script is below in case anyone wants to run it against real multi GPU hardware, which I do not have. If either of you get a chance, running this same script with torchrun --nproc_per_node=2 across two actual GPUs would confirm whether this exact setup reproduces the crash, or whether there is an additional ingredient from the real model I am still missing.

```python
import types

import torch
import torch.nn as nn
import torch.distributed as dist
from torch.utils.data import DataLoader, Dataset
from compressed_tensors.offload import init_dist

from llmcompressor.core.session_functions import active_session
from llmcompressor.args.dataset_arguments import DatasetArguments
from llmcompressor.modifiers.quantization import GPTQModifier
from llmcompressor.pipelines import CalibrationPipeline

VOCAB, HIDDEN, SEQ_LEN, NUM_SAMPLES = 64, 128, 16, 8


class MainBlock(nn.Module):
    def __init__(self, hidden):
        super().__init__()
        self.proj = nn.Linear(hidden, hidden, bias=False)

    def forward(self, x):
        return self.proj(x)


class MainTransformer(nn.Module):
    """Mirrors llmcompressor's own vendored DeepSeek V3.2 Transformer.forward,
    which is decorated with torch.inference_mode()
    (src/llmcompressor/modeling/deepseekv32/model.py line 845). Any tensor
    this returns stays tagged as an inference tensor even after the call
    returns, regardless of whether the caller is still inside inference_mode."""

    def __init__(self, embed, hidden):
        super().__init__()
        self.embed = embed
        self.main_block = MainBlock(hidden)

    @torch.inference_mode()
    def forward(self, input_ids):
        x = self.embed(input_ids)
        return self.main_block(x)


class MTPBlock(nn.Module):
    """Auxiliary speculative decode style head. Reuses the same embedding
    module as the main path (mirrors mtp.0.embed.weight aliasing embed.weight
    in the issue), and consumes hidden_states produced by the decorated
    MainTransformer, i.e. an inference tensor escaping its creating scope."""

    def __init__(self, embed, hidden):
        super().__init__()
        self.embed = embed
        self.e_proj = nn.Linear(hidden, hidden, bias=False)
        self.h_proj = nn.Linear(hidden, hidden, bias=False)

    def forward(self, hidden_states, input_ids):
        embed_out = self.embed(input_ids)
        return self.e_proj(embed_out) + self.h_proj(hidden_states)


class ToyMTPModel(nn.Module):
    def __init__(self, vocab=VOCAB, hidden=HIDDEN):
        super().__init__()
        self.embed = nn.Embedding(vocab, hidden)
        self.transformer = MainTransformer(self.embed, hidden)
        self.mtp_block = MTPBlock(self.embed, hidden)
        self.config = types.SimpleNamespace(_attn_implementation="eager")

    @property
    def device(self):
        return next(self.parameters()).device

    def forward(self, input_ids):
        x = self.transformer(input_ids)
        mtp_out = self.mtp_block(x, input_ids)
        return x, mtp_out


class ToyDataset(Dataset):
    def __len__(self):
        return NUM_SAMPLES

    def __getitem__(self, idx):
        return {"input_ids": torch.randint(0, VOCAB, (SEQ_LEN,))}


def main():
    # init_dist()
    # rank = dist.get_rank()
    rank = 0

    model = ToyMTPModel()
    dataloader = DataLoader(ToyDataset(), batch_size=1)

    dataset_args = DatasetArguments(
        pipeline="sequential",
        sequential_targets=["MainTransformer", "MTPBlock"],
    )
    modifier = GPTQModifier(targets=[r"re:.*proj$"], scheme="W4A16")

    session = active_session()
    session.reset()
    session.initialize(
        model=model,
        recipe=[modifier],
        calib_data=dataloader,
        sequential_targets=dataset_args.sequential_targets,
    )

    try:
        pipeline = CalibrationPipeline.from_modifiers(
            session.lifecycle.recipe.modifiers, user="sequential"
        )
        pipeline(model, dataloader, dataset_args)
        session.finalize()
        print(f"rank {rank} succeeded, no crash")
    except RuntimeError as e:
        print(f"rank {rank} crashed: {e}")
        raise
    finally:
        pass
        # dist.destroy_process_group()


if __name__ == "__main__":
    main()

```

Launch with:

```
torchrun --nproc_per_node=2 repro_2745.py
```


### brian-dellabetta · 2026-07-30

Hi @qubeena07 , thanks for preparing this. I updated your python script above slightly, to use our internal init_dist, and I hit the same error -- `Inplace update to inference tensor outside InferenceMode is not allowed`

I updated the script again to run purely on CPU, single-process, and I hit the same error, so I don't think this is related to torchrun/distributed at all.

Is the solution simply to remove the inference_mode decorator because we are no longer just using the model def for inference? GPTQ and our on-loading logic will update weights in-place, so we can no longer make that assumption

<details><summary>Full logs & stack-trace</summary>

```
>>> CUDA_VISIBLE_DEVICES=none python /home/brian-dellabetta/projects/_scratch/deepseek_inference_mode.py

2026-07-30T14:52:42.8417 | reset | INFO - Compression lifecycle reset
2026-07-30T14:52:42.8419 | from_modifiers | INFO - Creating recipe from modifiers
Applying quantization config: 100%|██████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████| 3/3 [00:00<00:00, 4158.27it/s]
2026-07-30T14:52:42.8564 | initialize | INFO - Compression lifecycle initialized for 1 modifiers
2026-07-30T14:52:43.1083 | disable_lm_head | WARNING - Attempted to disable lm_head of instance ToyMTPModel, but was unable to to find lm_head. This may lead to unexpected OOM.
2026-07-30T14:52:43.1175 | targets_embeddings | WARNING - Cannot check embeddings. If this model has word embeddings, please implement `get_input_embeddings` and `get_output_embeddings`
2026-07-30T14:52:43.1184 | disable_lm_head | WARNING - Attempted to disable lm_head of instance ToyMTPModel, but was unable to to find lm_head. This may lead to unexpected OOM.
Preparing cache: 100%|██████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████| 8/8 [00:00<00:00, 12652.50it/s]
(1/3): Calibrating: 100%|███████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████| 8/8 [00:00<00:00, 12422.97it/s]
(1/3): Propagating: 100%|███████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████| 8/8 [00:00<00:00, 11151.36it/s]
(2/3): Calibrating: 100%|██████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████| 8/8 [00:00<00:00, 69.46it/s]
2026-07-30T14:52:43.2553 | compress_module_list | INFO - Quantizing transformer.main_block.proj using 8 samples
2026-07-30T14:52:43.4422 | GPTQ | METRIC - time 0.19s
2026-07-30T14:52:43.4423 | GPTQ | METRIC - error 0.66
2026-07-30T14:52:43.4427 | GPTQ | METRIC - Accelerator 0 | usage: 0.04% | total memory: 85.0 Gb
2026-07-30T14:52:43.5670 | GPTQ | METRIC - Accelerator 1 | usage: 0.00% | total memory: 85.0 Gb
2026-07-30T14:52:43.7080 | GPTQ | METRIC - Accelerator 2 | usage: 0.00% | total memory: 85.0 Gb
2026-07-30T14:52:43.8321 | GPTQ | METRIC - Accelerator 3 | usage: 0.00% | total memory: 85.0 Gb
2026-07-30T14:52:43.9547 | GPTQ | METRIC - Accelerator 4 | usage: 0.00% | total memory: 85.0 Gb
2026-07-30T14:52:44.0852 | GPTQ | METRIC - Accelerator 5 | usage: 0.00% | total memory: 85.0 Gb
2026-07-30T14:52:44.3422 | GPTQ | METRIC - Accelerator 6 | usage: 0.00% | total memory: 85.0 Gb
2026-07-30T14:52:44.5943 | GPTQ | METRIC - Accelerator 7 | usage: 0.00% | total memory: 85.0 Gb
rank 0 crashed: Inplace update to inference tensor outside InferenceMode is not allowed.You can make a clone to get a normal tensor before doing inplace update.See https://github.com/pytorch/rfcs/pull/17 for more details.
Traceback (most recent call last):
  File "/home/brian-dellabetta/projects/_scratch/deepseek_inference_mode.py", line 126, in <module>
    main()
  File "/home/brian-dellabetta/projects/_scratch/deepseek_inference_mode.py", line 114, in main
    pipeline(model, dataloader, dataset_args)
  File "/home/brian-dellabetta/projects/llm-compressor/src/llmcompressor/pipelines/sequential/helpers.py", line 488, in wrapper
    return func(*args, **kwargs)
           ^^^^^^^^^^^^^^^^^^^^^
  File "/home/brian-dellabetta/projects/llm-compressor/src/llmcompressor/pipelines/sequential/pipeline.py", line 160, in __call__
    LifecycleCallbacks.sequential_epoch_end(subgraph.submodules(model))
  File "/home/brian-dellabetta/projects/llm-compressor/src/llmcompressor/core/session_functions.py", line 165, in sequential_epoch_end
    return cls.event(EventType.SEQUENTIAL_EPOCH_END, modules=modules, **kwargs)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/brian-dellabetta/projects/llm-compressor/src/llmcompressor/core/session_functions.py", line 91, in event
    return active_session().event(event_type, **kwargs)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/brian-dellabetta/projects/llm-compressor/src/llmcompressor/core/session.py", line 181, in event
    mod_data = self._lifecycle.event(
               ^^^^^^^^^^^^^^^^^^^^^^
  File "/home/brian-dellabetta/projects/llm-compressor/src/llmcompressor/core/lifecycle.py", line 204, in event
    data = mod.update_event(state=self.state, event=event, **kwargs)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/brian-dellabetta/projects/llm-compressor/src/llmcompressor/modifiers/modifier.py", line 144, in update_event
    self.on_sequential_epoch_end(state, event, **kwargs)
  File "/home/brian-dellabetta/projects/llm-compressor/src/llmcompressor/modifiers/gptq/base.py", line 247, in on_sequential_epoch_end
    self.compress_modules()
  File "/home/brian-dellabetta/projects/llm-compressor/src/llmcompressor/modifiers/gptq/base.py", line 298, in compress_modules
    self.compress_module_list(list(self._num_samples.keys()))
  File "/home/brian-dellabetta/projects/llm-compressor/src/llmcompressor/modifiers/gptq/base.py", line 343, in compress_module_list
    update_offload_parameter(module, attr, val)
  File "/home/brian-dellabetta/projects/compressed-tensors/src/compressed_tensors/offload/__init__.py", line 145, in update_offload_parameter
    cache[name] = data
    ~~~~~^^^^^^
  File "/home/brian-dellabetta/projects/compressed-tensors/src/compressed_tensors/offload/cache/base.py", line 225, in __setitem__
    onloaded.copy_(value)
RuntimeError: Inplace update to inference tensor outside InferenceMode is not allowed.You can make a clone to get a normal tensor before doing inplace update.See https://github.com/pytorch/rfcs/pull/17 for more details.
```
</details>

### qubeena07 · 2026-07-30

That matches what I would expect, thanks for testing it on CPU, that rules out distributed being involved at all, which simplifies this a lot.

Agreed on the direction. torch.no_grad() gives the same gradient disabling benefit that forward pass needs, without the in place restriction, and this file was clearly written as pure inference reference code originally, not with calibration time weight mutation in mind. Checked the git history and this decorator came in as part of the initial DeepSeek V3.2 support PR, copied straight from what looks like the original reference implementation, so it was never really evaluated against how llm-compressor updates weights during GPTQ and offloading.

I will swap it to torch.no_grad() and confirm the repro passes, then put up a PR with that change plus a small regression test using the same toy model pattern from the script above, since it does not depend on downloading the real checkpoint. Will link back here once it is up.


### qubeena07 · 2026-07-30

PR is up: https://github.com/vllm-project/llm-compressor/pull/2987

### brian-dellabetta · 2026-07-30

Thanks @qubeena07 , it's just strange because I ran a script on DeepSeek 3.2 very similar to what @pasta-paul posted, but didn't hit this issue. And your script above works fine on QuantizationModifier, it's only GTPQModifier that is failing.

### qubeena07 · 2026-07-30

That is a good catch, thanks for confirming it is specific to GPTQModifier. That actually lines up with what I would expect looking at the code, QuantizationModifier only calibrates min and max ranges during sequential_epoch_end, while GPTQModifier actually computes a new reconstructed weight and writes it back through update_offload_parameter, which is the exact call that crashes in your traceback. So QuantizationModifier never exercises that in place write path the same way.

What I am not sure about is why your real DeepSeek 3.2 run did not hit it. Could you share a bit more about that script, specifically which modifier it used and whether the recipe actually targeted a module that shares weights with something computed inside the decorated Transformer.forward, the way mtp e_proj and h_proj do in the original issue. If your run used GPTQModifier but targeted only modules outside that shared or aliased path, that would explain why it stayed clean even with the decorator still in place, since the taint only becomes visible once a downstream module fed by the decorated output actually goes through a GPTQ writeback.

Happy to try to match your setup more closely on my end if that helps narrow it down.


### brian-dellabetta · 2026-08-03

Hi @qubeena07 , reading this with fresh eyes the caveat that GPTQModifier fails whereas QuantizaitonModifier succeeds is in-line with my previous results (details for the model I created are all in model card here -- https://huggingface.co/RedHatAI/DeepSeek-V3.2-NVFP4-FP8-BLOCK). My attempts with GPTQ failed for OOM issues, so i never reached that part of the model.

So I think we should be good with the changes in #2987 , will merge after resolving one thread there. @pasta-paul , if you would like to retry with those changes and let us know, feel free. Otherwise we will close this off once it merges, and can re-open if necessary
