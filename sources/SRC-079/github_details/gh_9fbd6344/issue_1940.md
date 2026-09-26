# [Issue #1940] TE 2.17 `_GroupedLinear.forward` signature change breaks ModelOpt MoE quantization

source: https://github.com/NVIDIA/Model-Optimizer/issues/1940
state: closed | updated: 2026-07-08T20:13:27Z
labels: 

## 正文

## Summary

Bumping Transformer Engine from 2.16 to 2.17 in Megatron-Bridge breaks ModelOpt quantization for a Qwen3 MoE model using TE `GroupedLinear`.

Observed versions:

- Transformer Engine: `2.17.0+2e559f06` (`2e559f062497bef768dfbe9d7e45548fadeca80a`)
- NVIDIA ModelOpt: `0.44.0rc5`
- Megatron-Bridge PR: https://github.com/NVIDIA-NeMo/Megatron-Bridge/pull/4696
- Failing GitHub Actions job: https://github.com/NVIDIA-NeMo/Megatron-Bridge/actions/runs/28888905556/job/85735341477?pr=4696

The same test passes with TE `2.16.0+d64bc14d`.

## Failure

The first causal exception occurs on the initial quantization calibration forward:

```text
File ".../transformer_engine/pytorch/module/grouped_linear.py", line 1788, in forward
    out, new_workspaces = linear_fn(
File ".../modelopt/torch/quantization/plugins/transformer_engine.py", line 178, in te_grouped_quantized_linear_fn
    num_gemms = len(args[sig_params.index("non_tensor_args") - ctx_offset][0])
TypeError: object of type 'bool' has no len()
```

## Cause

TE 2.17 changed the private `_GroupedLinear.forward` argument layout.

TE 2.16:

```python
forward(ctx, inp, non_tensor_args, *weights_and_biases)
# non_tensor_args[0] is m_splits
```

TE 2.17:

```python
forward(ctx, inp, m_splits, non_tensor_args, *weights_and_biases)
# non_tensor_args[0] is now use_bias
```

ModelOpt detects `non_tensor_args` in the signature and assumes its first element is always `m_splits`. With TE 2.17, it therefore calls `len()` on `use_bias`.

The compatibility logic likely needs to prefer the explicit `m_splits` parameter when present, while retaining the `non_tensor_args[0]` fallback for TE 2.16.

## Reproduction

In a two-GPU Megatron-Bridge environment using the versions above:

```bash
uv run python -m pytest -s -x \
  tests/functional_tests/test_groups/quantization/models/qwen/test_qwen3_moe_quantization_workflow.py::TestQwen3MoeQuantizationWorkflow::test_qwen3_moe_quantization_and_generation_with_expert_parallelism
```

The quantization subprocess fails during the first ModelOpt calibration forward with the traceback above.


## 评论 (1)

### cuichenx · 2026-07-07

Megatron-Bridge entry point: `examples/quantization/quantize.py:main` imports `modelopt.torch.quantization as mtq` and, for this FP8 calibration path, calls `mtq.quantize(unwrapped_model, mtq_config, ptq_forward_loop_func)` (line 180 at PR head `247bdde63f073f5c811106a6d3abaa5ce5ad7743`). The failing functional test launches that script under `torch.distributed.run` with `--export-quant-cfg fp8 --tp 2 --etp 2`.
