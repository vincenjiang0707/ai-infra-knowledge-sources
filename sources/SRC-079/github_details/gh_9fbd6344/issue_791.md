# [Issue #791] How to switch calibration algorithm from 'max' to 'histogram' in INT8_WEIGHT_ONLY_CFG?

source: https://github.com/NVIDIA/Model-Optimizer/issues/791
state: closed | updated: 2026-06-19T04:38:10Z
labels: feature request, stale, waiting for feedback

## 正文

My question:

 Hi,I am currently using the following INT8 quantization configuration:

`INT8_WEIGHT_ONLY_CFG = {
    "quant_cfg": {
        "*weight_quantizer": {"num_bits": 8, "axis": 0},
        "*input_quantizer": {"enable": False},
        **_default_disabled_quantizer_cfg,
    },
    "algorithm": "max",
}`

I would like to use the histogram calibration algorithm instead of max. Could you please advise on how to correctly modify this configuration to enable histogram-based calibration?

Specifically, should I simply change the "algorithm" field, or are there additional parameters required within "quant_cfg"?

Thanks!

## 评论 (4)

### realAsma · 2026-01-29

Histogram calibration isn't exposed via the high-level "algorithm" field, and this code path is not well tested or actively maintained. If you still want to use it, here's how:

```
from modelopt.torch.quantization.model_calib import (
    enable_stats_collection,
    finish_stats_collection,
)

# Config with histogram calibrator
# NOTE: histogram only supports per-tensor scaling (axis=None), NOT per-channel (axis=0)
INT8_HISTOGRAM_CFG = {
    "quant_cfg": {
        "*weight_quantizer": {"num_bits": 8, "axis": None, "calibrator": "histogram"},
        "*input_quantizer": {"enable": False},
    },
    "algorithm": "max",
}

# Quantize without running calibration
model = mtq.quantize(model, INT8_HISTOGRAM_CFG, forward_loop=None)

# Collect histogram stats
enable_stats_collection(model)
for batch in calibration_data:
    model(batch)

# Compute amax from histogram (method: "entropy", "mse", or None for max)
finish_stats_collection(model, method="entropy")
```

### realAsma · 2026-05-21

> 🤖 Bot-drafted reply

Hi @Hyubo, following up - did the histogram-calibration snippet above work for your use case? Note that path is not actively maintained, so we recommend sticking with the supported "max" / "awq" algorithms when possible. If we do not hear back within ~2 weeks we will close this; please reopen if it still applies.

### github-actions[bot] · 2026-06-05

Issue has not received an update in over 14 days. Adding stale label.

### github-actions[bot] · 2026-06-19

This issue was closed because it has been 14 days without activity since it has been marked as stale.
