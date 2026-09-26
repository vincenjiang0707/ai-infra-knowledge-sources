# [Issue #2790] [Bug]: AWQ w/ DDP and CPU offloading hits CUDA OOM

source: https://github.com/vllm-project/llm-compressor/issues/2790
state: closed | updated: 2026-07-23T14:20:20Z
labels: bug, awq

## 正文

### ⚙️ Your current environment

Current llm-compressor main, fresh env


### 🐛 Describe the bug


When AWQ is run with DDP and `offload_device=torch.device("cpu")`, a CUDA OOM error is raised during calibration, even with just 2 GPUs (in fact, even with just 1 🤔 ). Runs fine with `offload_device=None` or outside of torchrun/DDP.

```
(1/49): Calibrating: 100%|█████████████████████████████████████████████████████████████████████████████████████████████████████████████| 1024/1024 [00:00<00:00, 1461.24it/s]
Smoothing: 0it [00:00, ?it/s]
(1/49): Propagating: 100%|██████████████████████████████████████████████████████████████████████████████████████████████████████████████| 1024/1024 [00:04<00:00, 242.53it/s]
(2/49): Calibrating:   8%|█████████▍                                                                                                       | 85/1024 [00:25<04:39,  3.36it/s]
[rank0]: Traceback (most recent call last):
[rank0]:   File "/home/brian-dellabetta/projects/_scratch/huaxan_awq.py", line 67, in <module>
[rank0]:     oneshot(
[rank0]:   File "/home/brian-dellabetta/projects/llm-compressor/src/llmcompressor/entrypoints/oneshot.py", line 412, in oneshot
[rank0]:     one_shot()
[rank0]:   File "/home/brian-dellabetta/projects/llm-compressor/src/llmcompressor/entrypoints/oneshot.py", line 189, in __call__
[rank0]:     self.apply_recipe_modifiers(
[rank0]:   File "/home/brian-dellabetta/projects/llm-compressor/src/llmcompressor/entrypoints/oneshot.py", line 241, in apply_recipe_modifiers
[rank0]:     pipeline(
[rank0]:   File "/home/brian-dellabetta/projects/llm-compressor/src/llmcompressor/pipelines/independent/pipeline.py", line 45, in __call__
[rank0]:     pipeline(model, dataloader, dataset_args)
[rank0]:   File "/home/brian-dellabetta/projects/llm-compressor/src/llmcompressor/pipelines/sequential/helpers.py", line 475, in wrapper
[rank0]:     return func(*args, **kwargs)
[rank0]:            ^^^^^^^^^^^^^^^^^^^^^
[rank0]:   File "/home/brian-dellabetta/projects/llm-compressor/src/llmcompressor/pipelines/sequential/pipeline.py", line 153, in __call__
[rank0]:     outputs = subgraph.forward(model, **inputs)
[rank0]:               ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
[rank0]:   File "/home/brian-dellabetta/projects/llm-compressor/src/llmcompressor/pipelines/sequential/helpers.py", line 64, in forward
[rank0]:     return forward_fn(*args, **kwargs)
[rank0]:            ^^^^^^^^^^^^^^^^^^^^^^^^^^^
[rank0]:   File "<string>", line 5, in forward
[rank0]:   File "/home/brian-dellabetta/projects/.venv/lib64/python3.12/site-packages/transformers/modeling_layers.py", line 94, in __call__
[rank0]:     return super().__call__(*args, **kwargs)
[rank0]:            ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
[rank0]:   File "/home/brian-dellabetta/projects/.venv/lib64/python3.12/site-packages/torch/nn/modules/module.py", line 1779, in _wrapped_call_impl
[rank0]:     return self._call_impl(*args, **kwargs)
[rank0]:            ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
[rank0]:   File "/home/brian-dellabetta/projects/.venv/lib64/python3.12/site-packages/torch/nn/modules/module.py", line 1790, in _call_impl
[rank0]:     return forward_call(*args, **kwargs)
[rank0]:            ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
[rank0]:   File "/home/brian-dellabetta/projects/.venv/lib64/python3.12/site-packages/compressed_tensors/offload/module.py", line 58, in forward
[rank0]:     return self._original_forward_func(self, *args, **kwargs)
[rank0]:            ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
[rank0]:   File "/home/brian-dellabetta/projects/.venv/lib64/python3.12/site-packages/transformers/utils/deprecation.py", line 172, in wrapped_func
[rank0]:     return func(*args, **kwargs)
[rank0]:            ^^^^^^^^^^^^^^^^^^^^^
[rank0]:   File "/home/brian-dellabetta/projects/.venv/lib64/python3.12/site-packages/transformers/models/qwen3_moe/modeling_qwen3_moe.py", line 359, in forward
[rank0]:     hidden_states = self.mlp(hidden_states)
[rank0]:                     ^^^^^^^^^^^^^^^^^^^^^^^
[rank0]:   File "/home/brian-dellabetta/projects/.venv/lib64/python3.12/site-packages/torch/nn/modules/module.py", line 1779, in _wrapped_call_impl
[rank0]:     return self._call_impl(*args, **kwargs)
[rank0]:            ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
[rank0]:   File "/home/brian-dellabetta/projects/.venv/lib64/python3.12/site-packages/torch/nn/modules/module.py", line 1885, in _call_impl
[rank0]:     return inner()
[rank0]:            ^^^^^^^
[rank0]:   File "/home/brian-dellabetta/projects/.venv/lib64/python3.12/site-packages/torch/nn/modules/module.py", line 1833, in inner
[rank0]:     result = forward_call(*args, **kwargs)
[rank0]:              ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
[rank0]:   File "/home/brian-dellabetta/projects/.venv/lib64/python3.12/site-packages/compressed_tensors/offload/module.py", line 58, in forward
[rank0]:     return self._original_forward_func(self, *args, **kwargs)
[rank0]:            ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
[rank0]:   File "/home/brian-dellabetta/projects/llm-compressor/src/llmcompressor/modeling/qwen3_moe.py", line 82, in forward
[rank0]:     expert_out = expert_layer(hidden_states)[top_x]
[rank0]:                  ^^^^^^^^^^^^^^^^^^^^^^^^^^^
[rank0]:   File "/home/brian-dellabetta/projects/.venv/lib64/python3.12/site-packages/torch/nn/modules/module.py", line 1779, in _wrapped_call_impl
[rank0]:     return self._call_impl(*args, **kwargs)
[rank0]:            ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
[rank0]:   File "/home/brian-dellabetta/projects/.venv/lib64/python3.12/site-packages/torch/nn/modules/module.py", line 1790, in _call_impl
[rank0]:     return forward_call(*args, **kwargs)
[rank0]:            ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
[rank0]:   File "/home/brian-dellabetta/projects/.venv/lib64/python3.12/site-packages/compressed_tensors/offload/module.py", line 58, in forward
[rank0]:     return self._original_forward_func(self, *args, **kwargs)
[rank0]:            ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
[rank0]:   File "/home/brian-dellabetta/projects/.venv/lib64/python3.12/site-packages/transformers/models/qwen3_moe/modeling_qwen3_moe.py", line 209, in forward
[rank0]:     down_proj = self.down_proj(self.act_fn(self.gate_proj(x)) * self.up_proj(x))
[rank0]:                 ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
[rank0]:   File "/home/brian-dellabetta/projects/.venv/lib64/python3.12/site-packages/torch/nn/modules/module.py", line 1779, in _wrapped_call_impl
[rank0]:     return self._call_impl(*args, **kwargs)
[rank0]:            ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
[rank0]:   File "/home/brian-dellabetta/projects/.venv/lib64/python3.12/site-packages/torch/nn/modules/module.py", line 1885, in _call_impl
[rank0]:     return inner()
[rank0]:            ^^^^^^^
[rank0]:   File "/home/brian-dellabetta/projects/.venv/lib64/python3.12/site-packages/torch/nn/modules/module.py", line 1812, in inner
[rank0]:     args_kwargs_result = hook(self, args, kwargs)  # type: ignore[misc]
[rank0]:                          ^^^^^^^^^^^^^^^^^^^^^^^^
[rank0]:   File "/home/brian-dellabetta/projects/llm-compressor/src/llmcompressor/modifiers/utils/hooks.py", line 99, in wrapped_hook
[rank0]:     return hook(*args, **kwargs)
[rank0]:            ^^^^^^^^^^^^^^^^^^^^^
[rank0]:   File "/home/brian-dellabetta/projects/llm-compressor/src/llmcompressor/modifiers/transform/awq/base.py", line 417, in cache_parent_kwargs_hook
[rank0]:     self._parent_args_cache[module].append(values.arguments)
[rank0]:   File "/home/brian-dellabetta/projects/llm-compressor/src/llmcompressor/pipelines/cache.py", line 158, in append
[rank0]:     self.update(batch_index, values)
[rank0]:   File "/home/brian-dellabetta/projects/llm-compressor/src/llmcompressor/pipelines/cache.py", line 130, in update
[rank0]:     intermediates = {k: self._offload_value(v, device) for k, v in values.items()}
[rank0]:                         ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
[rank0]:   File "/home/brian-dellabetta/projects/llm-compressor/src/llmcompressor/pipelines/cache.py", line 331, in _offload_value
[rank0]:     offloaded = offloaded.pin_memory()
[rank0]:                 ^^^^^^^^^^^^^^^^^^^^^^
[rank0]:   File "/home/brian-dellabetta/projects/.venv/lib64/python3.12/site-packages/torch/_compile.py", line 54, in inner
[rank0]:     return disable_fn(*args, **kwargs)
[rank0]:            ^^^^^^^^^^^^^^^^^^^^^^^^^^^
[rank0]:   File "/home/brian-dellabetta/projects/.venv/lib64/python3.12/site-packages/torch/_dynamo/eval_frame.py", line 1263, in _fn
[rank0]:     return fn(*args, **kwargs)
[rank0]:            ^^^^^^^^^^^^^^^^^^^
[rank0]:   File "/home/brian-dellabetta/projects/llm-compressor/src/llmcompressor/pipelines/cache.py", line 399, in __torch_dispatch__
[rank0]:     return func(*args, **kwargs)
[rank0]:            ^^^^^^^^^^^^^^^^^^^^^
[rank0]:   File "/home/brian-dellabetta/projects/.venv/lib64/python3.12/site-packages/torch/_ops.py", line 865, in __call__
[rank0]:     return self._op(*args, **kwargs)
[rank0]:            ^^^^^^^^^^^^^^^^^^^^^^^^^
[rank0]: torch.AcceleratorError: CUDA error: out of memory
```

### 🛠️ Steps to reproduce

Run script below with `torchrun --nproc_per_node=1 ./script.py`.

<details>
<summary>Script</summary>

```python

"""
Recipe: W4A16 GPTQ (4-bit weights, 16-bit activations)
Smallest model size. Hessian-based GPTQ. Marlin kernels in vLLM.
Run with: torchrun --nproc_per_node=8 this_script.py
"""

import torch
from datasets import load_dataset
from transformers import AutoModelForCausalLM, AutoTokenizer
from compressed_tensors.offload import init_dist, load_offloaded_model
from llmcompressor import oneshot
from llmcompressor.modifiers.awq import AWQModifier

MODEL_ID = "Qwen/Qwen3-30B-A3B"
CALIBRATION_DATASET = "neuralmagic/calibration"
NUM_SAMPLES = 1024
SCHEME = "W4A16"
MAX_SEQUENCE_LENGTH = 512

# Step 1: init distributed context
init_dist()

# Step 2: offloaded model load
with load_offloaded_model():
    model = AutoModelForCausalLM.from_pretrained(
        MODEL_ID, dtype="auto", device_map="auto_offload"
    )
tokenizer = AutoTokenizer.from_pretrained(MODEL_ID)

# Step 3: rank-shard the dataset (manual equivalent of get_rank_partition for load_from_disk)
# ds = load_from_disk(CALIBRATION_DATASET)
# ds = ds.select(range(min(NUM_SAMPLES, len(ds))))
# rank = torch.distributed.get_rank()
# world_size = torch.distributed.get_world_size()
# ds = ds.shard(num_shards=world_size, index=rank, contiguous=True)

# Select calibration dataset.
DATASET_ID = "HuggingFaceH4/ultrachat_200k"
DATASET_SPLIT = "train_sft"


# Load dataset and preprocess.
ds = load_dataset(DATASET_ID, split=f"{DATASET_SPLIT}[:{NUM_SAMPLES}]")
ds = ds.shuffle(seed=42)


def preprocess(example):
    return {
        "text": tokenizer.apply_chat_template(
            example["messages"],
            tokenize=False,
        )
    }


ds = ds.map(preprocess)


recipe = AWQModifier(
    targets=["Linear"],
    scheme=SCHEME,
    ignore=["lm_head", "re:.*mlp.gate$", "re:.*mlp.shared_expert_gate$"],
    # offload_device=None,
)

oneshot(
    model=model,
    recipe=recipe,
    dataset=ds,
    max_seq_length=MAX_SEQUENCE_LENGTH,
    num_calibration_samples=NUM_SAMPLES,
)

# Save (rank 0 only would also work, but save_pretrained handles this)
SAVE_DIR = MODEL_ID.split("/")[-1] + "-" + SCHEME + "_AWQ-DDP"
model.save_pretrained(SAVE_DIR, save_compressed=True)
tokenizer.save_pretrained(SAVE_DIR)

# Step 4 (cleanup): destroy process group
torch.distributed.destroy_process_group()

```

</details>

## 评论 (9)

### JINO-ROHIT · 2026-06-03

i dont fully understand the entire library  but maybe it has something to do with the `_ofload_value` in cache.py, maybe ddp takes some pinned memory and the activations are also allocated to pin and eventually they run out. do you think this is right? i can debug a bit more towards the evening

### brian-dellabetta · 2026-06-03

Hi @JINO-ROHIT , yeah it must have something to do with pin memory. i don't undertsand why it's causing a CUDA OOM instead of CPU OOM though, it should be offloaded to cpu. Feel free to try it out, happy to assign this to you

### JINO-ROHIT · 2026-06-03

cool, i can take a deeper look , you can assign it to me :3

### brian-dellabetta · 2026-06-03

Thanks @JINO-ROHIT !

### huaxuan250 · 2026-06-09

Also by modifying the `sysctl -w vm.max_map_count=1048576` on my p4d instance, this issue seems to be mitigated

### brian-dellabetta · 2026-06-09

Thanks @huaxuan250 , given that I did some more research as to the root cause:

> vm.max_map_count is a Linux kernel limit on the number of VMAs (Virtual Memory Areas) per process, not a GPU resource. But it's directly connected to cudaMallocHost().
> 
> Here's the precise mechanism:
> 
> cudaMallocHost() calls mmap() to carve out a region of the process's virtual address space for the pinned allocation. Each call typically creates a new VMA entry in the kernel's mm_struct for that process.
> The kernel enforces vm.max_map_count as the per-process VMA ceiling (default 65536).
> When that ceiling is hit, mmap() returns ENOMEM.
> The CUDA driver has no other interpretation for ENOMEM from mmap() — it maps it to CUDA_ERROR_OUT_OF_MEMORY, which PyTorch surfaces as CUDA error: out of memory.
> So the error isn't reporting exhausted GPU RAM or CUDA BAR space — it's the kernel refusing to create more VMA entries, dressed up as a CUDA OOM because that's the only error code the driver has for a failed pinned allocation.

So the CUDA OOM was a slight red herring, and the memory pinning is the culprit. @JINO-ROHIT we'll want to find a solution that still allows for memory pinning, so that the prefetching works performantly. Will continue conversation in your PR

### JINO-ROHIT · 2026-06-10

indeed, pinging you there

### Tobi-Adesoye · 2026-06-15

@brian-dellabetta This OOM under CPU offloading and DDP usually points directly to activation accumulation. When weights are constantly swapped between host and device memory, PyTorch's autograd engine retains intermediate activation states in the VRAM buffer longer to wait for the backward pass or cross-rank communication syncs. Under AWQ, these hidden activation tensors can grow taller than the original model layer profiles, completely eating the VRAM headroom.

Tightening the mathematical headroom of the intermediate normalization steps is crucial here—compressing the peak activation footprint allows the offloading layer to cycle weights without hitting a hard physical VRAM wall.

### brian-dellabetta · 2026-07-23

I was able to run the example script with Qwen 3 30B to completion with the fixes in #2813 
