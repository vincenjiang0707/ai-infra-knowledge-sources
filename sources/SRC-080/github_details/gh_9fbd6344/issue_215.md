# [Issue #215] INT8 to FP8 scale conversion

source: https://github.com/NVIDIA/Model-Optimizer/issues/215
state: closed | updated: 2026-09-25T11:44:05Z
labels: 

## 正文

https://github.com/NVIDIA/TensorRT-Model-Optimizer/blob/11b3eb6c78c81770d2d1b2aa384e1175a82c351c/modelopt/onnx/quantization/fp8.py#L124

I believe the conversion should be as follow: 
 np_fp8_scale = (np_scale * 127.0) / 448.0 

The current implementation is using a reverse multiplier which does not calculate FP8 scales correctly. 

## 评论 (6)

### i-riyad · 2025-06-16

Thanks for raising this! The current line:

`np_fp8_scale = (np_scale * 448.0) / 127.0
`

is intentional and correct for TensorRT FP8 deployment. The goal is not to preserve the original INT8 real-value range, but to expand it so that the FP8 quantized values make full use of FP8’s ±448 range — which improves numerical stability and performance in FP8 kernels.

If we used the reversed ratio (127 / 448), that would preserve INT8 behavior more closely, but often underutilizes FP8 precision and may lead to instability or rounding errors in deployment.

Let us know if you’re seeing unexpected behavior with this scaling in practice!

### roamiri · 2025-06-16

Thank you for your response. Please let me know if I’ve misunderstood anything. Here’s my current understanding:

1) The scaling factors are defined as:
'int8_scale = max / 127'
'fp8_scale = max / 448'
Therefore, 'fp8_scale = int8_scale * (127 / 448)'

2) Based on the current ratio used in the source code, the quantized weight tensors have a minimum and maximum value of approximately ±36. I ran MobileNetV2 using this configuration, and observed that the FP8 quantized tensors indeed fall within this ±36 range. However, they should ideally span ±448, which would be achieved by applying the suggested change.

### matri123 · 2025-06-17

Same confusion.
Also think should be 'fp8_scale = int8_scale * (127 / 448)'.

### i-riyad · 2025-06-30

Sorry for the confusion. I have updated my previous comment for clarity.
After careful observation, we see that the current equation can also be problematic.
With the current approach:

`fp8_scale = int8_scale * (448 / 127)
`

the original INT8 scale is expanded by ~3.5× (448 / 127 ≈ 3.52). This means activations or weights that previously worked well with smaller real values now get significantly scaled up, potentially causing:
- Activation blow-up
- Saturation or clipping in FP8 representation
- Layer imbalance

The real solution would be to implement direct amax calibration for FP8 instead of directly converting INT8 scales. This approach mitigates issues from either side:
- Inflating real values from INT8 mapping (current equation)
- Values being too small and rounding to zero (reversed equation)

We will work on this.

### tgavon · 2026-09-14

Hi @i-riyad , is this fixed already? cause from what i saw, 
https://github.com/NVIDIA/Model-Optimizer/blob/3c87751903124deeb3cb5aaf17b19816cfd9d3de/modelopt/onnx/quantization/fp8.py#L73

still has `scale*448/127`

### dajiaohuang · 2026-09-25

On current `main` at `ed7e8795`, `int8_to_fp8()` in `modelopt/onnx/quantization/fp8.py` still applies the `448/127` scale factor ([source](https://github.com/NVIDIA/Model-Optimizer/blob/ed7e87953c1a3ed6a21c8bf6eac90565fa6b7a36/modelopt/onnx/quantization/fp8.py#L75-L78)). I also saw the earlier note that direct amax calibration is the intended path and that either fixed ratio can be problematic. Is a tracked follow-up planned to use amax calibration here?
