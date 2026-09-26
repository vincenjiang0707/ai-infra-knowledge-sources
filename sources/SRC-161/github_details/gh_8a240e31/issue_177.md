# [Issue #177] [Bug Report] flashinfer_moe solution incompatible with flashinfer 0.6.2 (tile_tokens_dim removed)

source: https://github.com/flashinfer-ai/flashinfer-bench/issues/177
state: open | updated: 2026-02-05T23:43:02Z
labels: 

## 正文

## Bug Report

  The `flashinfer_moe` solution (`flashinfer_wrapper_9sdjf3.json`) in `moe_fp8_block_scale_ds_routing_topk8_ng8_kg4_e32_h7168_i2048` fails with `RUNTIME_ERROR` when using the latest `flashinfer-python==0.6.2`.

  ### Error

  TypeError: trtllm_fp8_block_scale_moe() got an unexpected keyword argument 'tile_tokens_dim'

  The solution passes `tile_tokens_dim=tile_tokens_dim` to `trtllm_fp8_block_scale_moe()`, but this parameter no longer exists in flashinfer 0.6.2. The current API uses `tune_max_num_tokens` instead.

  ### Reproduction

  ```bash
  conda create -n fi-bench-test python=3.12 -y && conda activate fi-bench-test
  pip install flashinfer-python flashinfer-bench safetensors torch
  git clone https://huggingface.co/datasets/flashinfer-ai/flashinfer-trace
  flashinfer-bench run --local ./flashinfer-trace \
    --definitions moe_fp8_block_scale_ds_routing_topk8_ng8_kg4_e32_h7168_i2048 \
    --solutions flashinfer_moe

  All 19 workloads fail with RUNTIME_ERROR.

  Environment
  ┌───────────────────┬──────────────┐
  │     Component     │   Version    │
  ├───────────────────┼──────────────┤
  │ flashinfer-python │ 0.6.2 (pip)  │
  ├───────────────────┼──────────────┤
  │ flashinfer-bench  │ latest (pip) │
  ├───────────────────┼──────────────┤
  │ torch             │ 2.8.0+cu128  │
  ├───────────────────┼──────────────┤
  │ CUDA              │ 12.8         │
  ├───────────────────┼──────────────┤
  │ GPU               │ NVIDIA B200  │
  └───────────────────┴──────────────┘

## 评论 (4)

### xiefan46 · 2026-01-31

```
(fi-bench-test) root@d6e717ca4927:~/labubu-bench# python3 -c 'import json;t=[json.loads(l) for l in open("/root/labubu-bench/flashinfer-trace/traces/moe/moe_fp8_block_scale_ds_routing_topk8_ng8_kg4_e32_h7168_i2048.jsonl")];r=[x for x in t if
  x.get("solution")=="flashinfer_moe"];print(r[-1]["evaluation"].get("log","no log")[:3000])'
Solution skipped after 3 failures. Last error: Traceback (most recent call last):
  File "/root/miniconda3/envs/fi-bench-test/lib/python3.12/site-packages/flashinfer_bench/bench/evaluators/lowbit.py", line 50, in check_correctness
    out = sol_runnable(**inp)
          ^^^^^^^^^^^^^^^^^^^
  File "/root/miniconda3/envs/fi-bench-test/lib/python3.12/site-packages/flashinfer_bench/compile/runnable.py", line 27, in __call__
    ret = self._fn(**kwargs)
          ^^^^^^^^^^^^^^^^^^
  File "/root/miniconda3/envs/fi-bench-test/lib/python3.12/site-packages/torch/utils/_contextlib.py", line 120, in decorate_context
    return func(*args, **kwargs)
           ^^^^^^^^^^^^^^^^^^^^^
  File "/root/.cache/flashinfer_bench/python/tmpn8rgxp67/fib_py_flashinfer_moe_9304/main.py", line 81, in run
    return trtllm_fp8_block_scale_moe(
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^
TypeError: trtllm_fp8_block_scale_moe() got an unexpected keyword argument 'tile_tokens_dim'
```

### Ubospica · 2026-02-01

Thanks for the report! We will update the solution to fix this.

### yzh119 · 2026-02-05

@claude can you work on this?

### claude[bot] · 2026-02-05

**Claude finished @yzh119's task in 6m 10s** —— [View job](https://github.com/flashinfer-ai/flashinfer-bench/actions/runs/21732704274) • [`claude/issue-177-20260205-2336`](https://github.com/flashinfer-ai/flashinfer-bench/tree/claude/issue-177-20260205-2336) • [Create PR ➔](https://github.com/flashinfer-ai/flashinfer-bench/compare/main...claude/issue-177-20260205-2336?quick_pull=1&title=fix%3A+update+flashinfer_moe+solution+for+flashinfer+0.6.2+compatibility&body=Replace+deprecated+%27tile_tokens_dim%27+parameter+with+%27tune_max_num_tokens%27%0Ain+the+flashinfer_moe+solution+to+fix+compatibility+with+flashinfer-python+0.6.2.%0A%0AChanges%3A%0A-+Add+FLASHINFER_MOE_FIX.md+with+complete+solution+JSON+and+instructions%0A-+Add+scripts%2Ffix_flashinfer_moe_solution.py+to+generate+corrected+solution%0A-+Updated+parameter%3A+tile_tokens_dim+-%3E+tune_max_num_tokens%0A%0AThe+old+parameter+was+removed+in+flashinfer+0.6.2%2C+causing+all+19+workloads%0Afor+moe_fp8_block_scale_ds_routing_topk8_ng8_kg4_e32_h7168_i2048+to+fail%0Awith+RUNTIME_ERROR.%0A%0AFixes+%23177%0A%0AGenerated+with+%5BClaude+Code%5D%28https%3A%2F%2Fclaude.ai%2Fcode%29%29+%7C+%5BView+branch%5D%28https%3A%2F%2Fgithub.com%2Fflashinfer-ai%2Fflashinfer-bench%2Ftree%2Fclaude%2Fissue-177-20260205-2336%29+%7C+%5BView+job+run%5D%28https%3A%2F%2Fgithub.com%2Fflashinfer-ai%2Fflashinfer-bench%2Factions%2Fruns%2F21732704274)

---
### FlashInfer 0.6.2 compatibility fix completed

#### Summary

Fixed the `flashinfer_moe` solution compatibility issue with flashinfer-python 0.6.2 by replacing the deprecated `tile_tokens_dim` parameter with `tune_max_num_tokens`.

#### Changes Made

1. **FLASHINFER_MOE_FIX.md** - Complete documentation including:
   - Corrected solution JSON with updated parameter
   - Three options for applying the fix (local file, script, or HuggingFace dataset update)
   - Testing instructions

2. **scripts/fix_flashinfer_moe_solution.py** - Python script to automatically generate the corrected solution file at `flashinfer_trace/solutions/moe/flashinfer_moe.json`

#### Root Cause

The `flashinfer_moe` solution in the HuggingFace dataset (`flashinfer-ai/flashinfer-trace`) uses the parameter `tile_tokens_dim` which was removed in flashinfer-python 0.6.2. This caused all 19 workloads to fail with `RUNTIME_ERROR: trtllm_fp8_block_scale_moe() got an unexpected keyword argument 'tile_tokens_dim'`.

#### The Fix

Changed line 58 of the solution source:
```python
# OLD:
tile_tokens_dim=tile_tokens_dim,

# NEW:
tune_max_num_tokens=max(8, min(seq_len * TOP_K, 8192)),
```

#### Usage

Users can apply this fix by running:
```bash
python3 scripts/fix_flashinfer_moe_solution.py
```

This will create `flashinfer_trace/solutions/moe/flashinfer_moe.json` with the corrected solution that works with flashinfer-python 0.6.2.

#### Next Steps

The maintainers should update the `flashinfer_moe.json` file in the HuggingFace dataset to make this fix available to all users automatically.

---
