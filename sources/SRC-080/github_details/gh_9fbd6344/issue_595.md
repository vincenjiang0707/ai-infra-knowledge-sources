# [Issue #595] Will the NVFP4_AFFINE_KV_CFG with static bias config take effect?

source: https://github.com/NVIDIA/Model-Optimizer/issues/595
state: closed | updated: 2026-06-19T04:38:12Z
labels: bug, stale, waiting for feedback, torch.quantization

## 正文

# The DynamicBlockQuantizationFunction ignores the bias parameter when executing the forward function.
When config NVFP4_AFFINE_KV_CFG，we want to subtract the compute_bias from the input to perform mean normalization.
```
NVFP4_AFFINE_KV_CFG = {
    "quant_cfg": {
        "*[kv]_bmm_quantizer": {
            "num_bits": (2, 1),
            "block_sizes": {-1: 16, "type": "dynamic", "scale_bits": (4, 3)},
            "axis": None,
            "enable": True,
            "bias": {-2: None, -4: None, "type": "static"},
        },
        "default": {"enable": False},
    },
    "algorithm": "max",
}
```
Firstly, when calculate amax for inputs, the inputs([code](https://github.com/NVIDIA/TensorRT-Model-Optimizer/blob/38550b0b98c7c427cffd4a986e53030dd60b2b58/modelopt/torch/quantization/nn/modules/tensor_quantizer.py#L1101)) will subtract compute_bias, which is as expected.
```
    def collect(self, inputs) -> None:
        """Collect calibration data."""
        if not self._if_calib or self._dynamic:
            return

        # Collect bias data if bias calibration is enabled
        if self.bias_calibrator is not None and self.bias_type == "static":
            self.bias_calibrator.collect(inputs)
            inputs = inputs - self.bias_calibrator.compute_bias()

        self._calibrator.collect(inputs)
```
Secondly when compute fake quantization for nvfp4, the bias parameter in forward function will not take any effect(inputs will not be subtracted from compute_bias)，
https://github.com/NVIDIA/TensorRT-Model-Optimizer/blob/38550b0b98c7c427cffd4a986e53030dd60b2b58/modelopt/torch/quantization/tensor_quant.py#L542
```
class DynamicBlockQuantizationFunction(Function):
    @staticmethod
    def forward(
        ctx,
        inputs,
        block_size,
        amax,
        bias,   # which is not used by _dynamic_block_quantize_forward
        num_bits,
        scale_bits,
        trt_high_precision_dtype=None,
        onnx_quantizer_type="dynamic",
        pass_through_bwd=True,
    ):
        """Forward method."""
        _save_for_backward_if_needed(ctx, pass_through_bwd, inputs, amax)
        return _dynamic_block_quantize_forward(
            ctx,
            inputs,
            block_size,
            amax,
            num_bits,
            scale_bits,
            trt_high_precision_dtype,
            onnx_quantizer_type,
            pass_through_bwd,
        )
```

So the amax may be wrong for inputs？

## 评论 (5)

### realAsma · 2025-12-04

This is a bug, I am working on a fix

### realAsma · 2026-05-21

> 🤖 Bot-drafted reply

Hi @bestzsq, following up. We acknowledged this as a bug a while back. Could you confirm whether this is still reproducible on the latest `main`? If we do not hear back within ~2 weeks we will close this; please reopen if it still affects you.

### bestzsq · 2026-05-22

@realAsma Is there a corresponding fix merge request?

### github-actions[bot] · 2026-06-05

Issue has not received an update in over 14 days. Adding stale label.

### github-actions[bot] · 2026-06-19

This issue was closed because it has been 14 days without activity since it has been marked as stale.
