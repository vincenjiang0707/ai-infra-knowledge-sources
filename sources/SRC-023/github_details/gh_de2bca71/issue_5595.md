# [Issue #5595] [ROCm][AITER]: get_2stage_cfgs: topk -= int(is_ep) incorrectly strips Fused Shared Expert column, producing wrong kernel config and gibberish output

source: https://github.com/ROCm/aiter/issues/5595
state: closed | updated: 2026-09-23T07:16:28Z
labels: 

## 正文

### Problem Description

  **Description**

  When expert_mask is provided and the last column of topk_ids contains a real (non-masked) shared expert ID — as done by vLLM's Fused Shared Expert (FSE) feature (VLLM_ROCM_USE_AITER_FUSION_SHARED_EXPERTS=1) — the MoE layer produces entirely gibberish output with no errors or warnings.

**Root Cause**

  In get_2stage_cfgs, the EP convention strips one column from the topk count before the config lookup:

  EP convention: callers append one always-masked fake-expert slot to `topk_ids`, so runtime `topk` is routed_topk + 1. Tuned configs are keyed
  on routed_topk; strip the fake slot before building the lookup key.
```
  topk -= int(is_ep)

  is_ep is derived in fused_moe_() as:

  is_ep = expert_mask is not None

```
  The assumption is that when expert_mask is present, the last topk_ids column always holds a fake/masked expert (expert_mask[fake_id] = 0). This is correct for the standard EP path.

  However, vLLM's FSE feature pre-fills that same extra column with a real shared expert global ID (e.g., 256 for GLM with 256 routed experts), where expert_mask[256] = 1 (the shared expert is active on all ranks). The kernel config is therefore looked up for topk=8 effective experts, but the kernel is dispatched with 9 real experts, producing incorrect output.

 Reproducer

  Tested on the container directly — no vLLM required:

```
  import torch, inspect
  import aiter
  from aiter import ActivationType, QuantType
  from aiter.fused_moe import get_2stage_cfgs, fused_moe

  dtypes = aiter.dtypes

  # 1. Confirm fused_moe has no shared_expert_id parameter
  params = list(inspect.signature(fused_moe).parameters.keys())
  print('fused_moe params:', params)
  print('has shared_expert_id:', 'shared_expert_id' in params)

  # 2. Demonstrate topk decrement bug
  # GLM: 256 routed experts, top_k=8, 1 real shared expert -> topk_ids has 9 cols
  topk_actual = 9

  print('\n=== is_ep=True (triggered because expert_mask is not None) ===')
  cfg_ep = get_2stage_cfgs(
      token=128, model_dim=4096, inter_dim=2048,
      expert=256, topk=topk_actual,
      dtype=dtypes.fp8, q_dtype_a=dtypes.fp8, q_dtype_w=dtypes.fp8,
      q_type=QuantType.per_Token.value,
      use_g1u1=True, activation=ActivationType.Silu.value,
      doweight_stage1=False, hidden_pad=0, intermediate_pad=0,
      is_ep=True,
  )
  print('Config (internal topk=8, kernel processes 9 experts):', cfg_ep)

  print('\n=== is_ep=False (correct: shared expert is real, not fake) ===')
  cfg_fse = get_2stage_cfgs(
      token=128, model_dim=4096, inter_dim=2048,
      expert=256, topk=topk_actual,
      dtype=dtypes.fp8, q_dtype_a=dtypes.fp8, q_dtype_w=dtypes.fp8,
      q_type=QuantType.per_Token.value,
      use_g1u1=True, activation=ActivationType.Silu.value,
      doweight_stage1=False, hidden_pad=0, intermediate_pad=0,
      is_ep=False,
  )
  print('Config (topk=9, matches kernel):', cfg_fse)
  print('\nConfigs differ (proves wrong config selected under EP):', cfg_ep != cfg_fse)
```

  **Output:**
  fused_moe params: ['hidden_states', 'w1', 'w2', 'topk_weight', 'topk_ids', 'expert_mask',
    'activation', 'quant_type', 'doweight_stage1', 'w1_scale', 'w2_scale', 'a1_scale',
    'a2_scale', 'block_size_M', 'num_local_tokens', 'moe_sorting_dispatch_policy', 'dtype',
    'hidden_pad', 'intermediate_pad', 'bias1', 'bias2', 'splitk', 'swiglu_limit', 'beta',
    'linear_beta', 'gate_mode']
  has shared_expert_id: False

  === is_ep=True (triggered because expert_mask is not None) ===
  Config (internal topk=8, kernel processes 9 experts): MOEMetadata(... block_m=128 ...)

  === is_ep=False (correct: shared expert is real, not fake) ===
  Config (topk=9, matches kernel): MOEMetadata(... block_m=128 ...)

  Configs differ (proves wrong config selected under EP): True

**Expected Behaviour**

  When the extra topk_ids column contains a real expert (expert_mask[id] = 1), topk must not be decremented. The kernel config should be looked up for topk=9 to match the actual number of experts being processed.

**Suggested Fix**

  Add a has_fused_shared_expert: bool = False parameter to fused_moe() (and fused_moe_()) that bypasses the topk -= int(is_ep) decrement when the extra column is a real shared expert:

  `in get_2stage_cfgs / fused_moe_`:
```
  if is_ep and not has_fused_shared_expert:
      topk -= 1
```
 Alternatively, accept shared_expert_id: int = -1 directly in fused_moe() and handle the shared expert internally without embedding it in topk_ids at all — this is the approach taken in vLLM PR [vllm-project/vllm#53161](https://github.com/vllm-project/vllm/pull/53161).

 **Workaround**

  Disable FSE: VLLM_ROCM_USE_AITER_FUSION_SHARED_EXPERTS=0. The shared expert then runs as a separate MLP call, which is correct but loses the fusion benefit.

### Operating System

22.04.5 LTS 

### CPU

Intel(R) Xeon(R) Platinum 8480C

### GPU

AMD Instinct MI300X

### ROCm Version

7.2.3

### Installation Method

Python wheels

### Installed ROCm Packages / Versions

<details>
<summary>Installed ROCm packages / versions</summary>

```
Paste output here
```

</details>


### ROCm Component

_No response_

### Steps to Reproduce

_No response_

### (Optional for Linux users) Output of rocminfo --support

<details>
<summary>rocminfo --support output</summary>

```
Paste output here
```

</details>


### Additional Information

_No response_

## 评论 (2)

### yadaish · 2026-09-18

```
  topk -= int(is_ep)
```

You can create one PR to remove this line.

### psakhamo · 2026-09-21

@yadaish  submitted the [PR#5734](https://github.com/ROCm/aiter/pull/5734)
