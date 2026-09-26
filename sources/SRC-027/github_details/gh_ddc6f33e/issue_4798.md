# [Issue #4798] Muon: MoE expert weights may get the wrong dimension numbers on qwen3 / gpt-oss

source: https://github.com/AI-Hypercomputer/maxtext/issues/4798
state: closed | updated: 2026-08-26T01:34:41Z
labels: bug

## 正文

### Bug report

`muon_utils.transform_logic` only applies the per-expert mapping when the MoE module is
named `MoeBlock_0`:

```python
if "MoeBlock_0" in path:
    # exclude gate
    if _is_path_contain_any(("wi_0", "wi_1", "wo"), path):
      return mdn((-2,), (-1,))
```

`_is_path_contain_any` compares whole path segments, and the inner `if` has no `else`, so
a non-matching path falls through to the standard `mdn((0,), (-1,))` at the end of the
function. Where `RoutedMoE` / `RoutedAndSharedMoE` is actually attached:

| model | attribute | contains `MoeBlock_0` |
|---|---|---|
| `mixtral.py:108`, `envy.py:120` | `MoeBlock_0` | yes |
| `moe.py:3195` (`RoutedAndSharedMoE`: deepseek / deepseek4 / llama4 / gemma4) | `MoeBlock_0` | yes |
| `qwen3.py:1070` (qwen3-next) | `routed_experts` | no |
| `qwen3.py:1547` (qwen3 MoE) | `moe_block` | no |
| `qwen3_custom.py:136` | `moe_block` | no |
| `gpt_oss.py:121` | `GptOssMlp` | no |

The checkpoint mappings confirm the real paths: `param_mapping.py:1471-1479`
(qwen3-next) uses `mlp-routed_experts-wi_0` / `-wi_1` / `-wo`, and
`param_mapping.py:1832-1843` (gpt-oss) uses `GptOssMlp-wi_0` / `-wo`. No `MoeBlock_0`
segment in either.

If I'm reading this right, on those four the expert stack `[E, (L,) in, out]` gets
`reduction_axis=0`, i.e. the expert axis, so Newton-Schulz orthogonalizes *across*
experts rather than within each one, and `_shape_factor` is computed from the same axes.
Nothing raises, because the reshape is still valid.

It would also explain why this isn't caught: `test_model_integration` covers deepseek2/3/4,
kimi, llama2/3, gemma3 and qwen3-0.6b — every MoE model in that list routes through
`RoutedAndSharedMoE`'s nested `MoeBlock_0`, and qwen3-0.6b is dense.

Two more cases that look like the same fallthrough, and apply even when the module name
does match:

- `wi`, the fused gate+up kernel created when `prefuse_moe_weights=True` (`moe.py:537`),
  is not in the `("wi_0", "wi_1", "wo")` tuple.
- `wi_0_bias` / `wi_1_bias` / `wo_bias`, created when `mlp_bias=True` (`moe.py:603`, used
  by gpt-oss-20b / 120b), are not caught by the `segment == "bias"` exclusion because of
  the prefix, so they appear to be orthogonalized instead of going to the AdamW branch.

For what it's worth, #4779 appears to expect the same behaviour I do — it adds
`test_qwen3_next_moe_routed_experts` asserting
`("decoder", "mlp", "routed_experts", "wi_0") -> mdn((-2,), (-1,))` — but does not change
the matcher.

## Questions

1. Is this a real bug, or is Muon not expected to be used with these models yet?
2. If it's real, would matching on the leaf segment be acceptable —
   `path[-1] in ("wi", "wi_0", "wi_1", "wo")` — instead of a per-model list of module
   names? The reference trees in `optimizers_test.py` already encode that distinction —
   the expert `wi_0` is a leaf (`mdn((-2,), (-1,))`) while a dense `wi_0` has a `kernel`
   child (`mdn((0,), (-1,))`) — because `MlpBlock` reuses those names as `DenseGeneral`
   submodules (`linears.py:493`). The gpt-oss mapping shows both side by side:
   `GptOssMlp-gate-kernel` next to `GptOssMlp-wi_0`.

Happy to send a PR — I have the change and unit tests ready.


### Logs/Output

_No response_

### Environment Information

_No response_

### Additional Context

_No response_

## 评论 (2)

### shuningjin · 2026-08-17

Thanks for raising the issue! To answer the questions:

> Question 1: Is this a real bug, or is Muon not expected to be used with these models yet?

Muon is currently only supported for a few models. qwen3-dense, deepseek, are supported; qwen3-moe or gpt-oss are not supported.
https://github.com/AI-Hypercomputer/maxtext/blob/09bc4bc10007a143bc418128b0bbe9ab4686d951/src/maxtext/configs/types.py#L3815-L3825

To support more models, I would suggest following Section 3 in https://github.com/AI-Hypercomputer/maxtext/pull/2546


> Question2: If it's real, would matching on the leaf segment be acceptable — path[-1] in ("wi", "wi_0", "wi_1", "wo")

I think `path[-1] in ("wi", "wi_0", "wi_1", "wo")` these names are too generic. I would prefer them to be used with moe filter.

```
def _is_moe_path(path: Tuple[str, ...]) -> bool:
  moe_indicators = ("moe", "expert", "gptossmlp")
  return any(any(ind in segment.lower() for ind in moe_indicators) for segment in path[:-1])

# In transform_logic:
if _is_moe_path(path) and path[-1] in ("wi", "wi_0", "wi_1", "wo"):
  return mdn((-2,), (-1,))
```

### shuningjin · 2026-08-18

I see @parsley9877 have a [PR](https://github.com/AI-Hypercomputer/maxtext/pull/4843) to fix. Could you follow up?
