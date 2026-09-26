# [Issue #3059] [Bug]: Noisy gpt_oss test

source: https://github.com/vllm-project/llm-compressor/issues/3059
state: closed | updated: 2026-09-03T23:11:05Z
labels: bug, good first issue

## 正文

Please fix this noisy test for gpt_oss. This test `test_linearize.py` is generally noisy, so as stretch goal, it would be nice to determine why NaNs are being generated in the first place.

```
FAILED tests/llmcompressor/modeling/test_linearize.py::test_linearize_moe[gpt_oss] - AssertionError: assert tensor(nan, device='cuda:0') < 1e-10
--
  | +  where tensor(nan, device='cuda:0') = <function mse_loss at 0x7fd654cdda20>(tensor([[    nan,     nan,     nan,  ...,     nan,     nan,     nan],\n        [-0.6101,  1.4156,  0.4008,  ...,  0.699... nan,     nan,     nan],\n        [ 7.5286,  0.2846, -1.6951,  ..., -1.0187, -3.8526,  4.8506]],\n       device='cuda:0'), tensor([[    nan,     nan,     nan,  ...,     nan,     nan,     nan],\n        [-0.6101,  1.4156,  0.4008,  ...,  0.699... nan,     nan,     nan],\n        [ 7.5286,  0.2846, -1.6951,  ..., -1.0187, -3.8526,  4.8506]],\n       device='cuda:0'))
  | +    where <function mse_loss at 0x7fd654cdda20> = <module 'torch.nn.functional' from '/workspace/build/buildkite/testvenv/lib/python3.10/site-packages/torch/nn/functional.py'>.mse_loss
  | +      where <module 'torch.nn.functional' from '/workspace/build/buildkite/testvenv/lib/python3.10/site-packages/torch/nn/functional.py'> = <module 'torch.nn' from '/workspace/build/buildkite/testvenv/lib/python3.10/site-packages/torch/nn/__init__.py'>.functional
  | +        where <module 'torch.nn' from '/workspace/build/buildkite/testvenv/lib/python3.10/site-packages/torch/nn/__init__.py'> = torch.nn
```


## 评论 (9)

### original4422 · 2026-08-20

Hi! I would like to work on this. My proposed approach:

- Adjust the regression setup so every GPT-OSS expert parameter used by `forward` is initialized deterministically, including `gate_up_proj_bias` and `down_proj_bias`.
- Assert that both original and linearized outputs are finite (rather than masking invalid values with `equal_nan`), while retaining the existing MSE equivalence threshold and coverage for the other MoE cases.
- Run the focused tests and quality checks. The existing GPT-OSS parameterization is CUDA-only, so I will rely on project CI for that GPU case and clearly report local limits.

A tiny CPU probe reproduced the likely cause: the two `torch.empty` biases above are left uninitialized by the current test setup; initializing them makes the output finite and self-MSE zero.

Per `CONTRIBUTING.md`, could a maintainer assign this issue / green-light this approach before I start?

### original4422 · 2026-08-24

Thanks for the assignment/green light. I noticed the issue was unassigned again about a minute later, so I want to avoid misreading the signal or duplicating work. Was the unassignment intentional? I’ll hold off on implementation/PR until you confirm that I should proceed with the approach above.

### kylesayrs · 2026-08-24

@original4422 Are you an openclaw agent? This issue in particular is meant for humans only

### dougc333 · 2026-08-25

Can I take this? I am human.  

### Roy214 · 2026-08-25

Hi @kylesayrs 

I can also contribute to this.

### Roy214 · 2026-08-25

Tests:

```
pytest tests/llmcompressor/modeling/test_linearize.py::test_linearize_moe -k gpt_oss
========================================================= test session starts =========================================================
platform linux -- Python 3.12.5, pytest-9.1.1, pluggy-1.6.0
rootdir: /home/dev/llm-compressor
configfile: pyproject.toml
plugins: anyio-4.14.2, rerunfailures-16.6, mock-3.15.1
collected 30 items / 29 deselected / 1 selected                                                                                       

tests/llmcompressor/modeling/test_linearize.py .                                                                                [100%]

========================================================== warnings summary ===========================================================
../lc-env/lib64/python3.12/site-packages/torch/jit/_script.py:365: 14 warnings
  /home/dev/lc-env/lib64/python3.12/site-packages/torch/jit/_script.py:365: DeprecationWarning: `torch.jit.script_method` is deprecated. Please switch to `torch.compile` or `torch.export`.
    warnings.warn(

-- Docs: https://docs.pytest.org/en/stable/how-to/capture-warnings.html
============================================ 1 passed, 29 deselected, 14 warnings in 0.52s ============================================

```

```
git diff
diff --git a/tests/llmcompressor/modeling/test_linearize.py b/tests/llmcompressor/modeling/test_linearize.py
index 965afc18f..329581901 100644
--- a/tests/llmcompressor/modeling/test_linearize.py
+++ b/tests/llmcompressor/modeling/test_linearize.py
@@ -32,6 +32,11 @@ CONFIG_OVERRIDES = {
     "cohere2_moe": {"hidden_size": 256, "intermediate_size": 256},
     "gemma4": {"num_experts": 16, "top_k_experts": 4, "moe_intermediate_size": 2304},
     "glm_moe_dsa": {"hidden_size": 512},
+    "gpt_oss": {
+        "hidden_size": 256,
+        "intermediate_size": 256,
+        "num_local_experts": 16,
+    },
```


### original4422 · 2026-08-26

@kylesayrs
Hi guy, I'm a human


### princesavsaviya · 2026-08-26

I'd like to take this. 

Plan is to run test_linearize_moe[gpt_oss] in a loop locally to isolate whether the NaN originates in the linearized output tensor or the reference tensor (both show nan in the traceback, so need to check which one goes bad first). Then determine if it's input-dependent or a determinism gap in the linearization path.

### dsikka · 2026-09-03

Resolved by: https://github.com/vllm-project/llm-compressor/pull/3123
