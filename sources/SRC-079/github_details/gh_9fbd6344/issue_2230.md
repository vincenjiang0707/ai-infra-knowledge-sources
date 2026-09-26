# [Issue #2230] hf_ptq.py: deprecated --auto_quantize_bits CLI flag silently no-ops instead of enabling AutoQuantize

source: https://github.com/NVIDIA/Model-Optimizer/issues/2230
state: open | updated: 2026-08-24T16:03:52Z
labels: 

## 正文

## Description

`examples/hf_ptq/hf_ptq.py`'s deprecated `--auto_quantize_bits` CLI flag (and its siblings `--auto_quantize_method`, `--auto_quantize_score_size`, `--auto_quantize_cost_model`, `--auto_quantize_active_moe_expert_ratio`) is documented as still enabling the AutoQuantize CLI path via a conversion shim:

```python
# Deprecated AutoQuantize CLI flags: kept as a backward-compat shim that converts them into an
# AutoQuantizeConfig on the fly (see _auto_quantize_config_from_cli). Prefer --recipe. The old
# CLI also lives on the 0.45 branch.
parser.add_argument(
    "--auto_quantize_bits",
    ...
)
```

`_auto_quantize_config_from_cli` does not exist anywhere in the file (or the repo). `quantize_main()` only enables AutoQuantize by checking whether `--recipe` resolves to a `ModelOptAutoQuantizeRecipe`; `args.auto_quantize_bits` is never read in the actual quantization path.

**Effect**: a legacy command still relying on `--auto_quantize_bits` (e.g. carried over from the 0.45 branch's CLI) silently runs plain PTQ instead of AutoQuantize, with no warning or error pointing back at the cause.

## Fix

Fixed in #2129 by rejecting `--auto_quantize_bits` at `parse_args()` instead of letting it silently no-op, pointing users at an AutoQuantize `--recipe`.

Found via a CodeRabbit review comment on that PR.


## 评论 (1)

### wyattearp · 2026-08-22

Fixed by https://github.com/NVIDIA/Model-Optimizer/pull/2129
