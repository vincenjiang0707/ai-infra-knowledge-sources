# [Issue #869] inference discrepancy between onnxruntime and trt8.6(trt10.11 too)

source: https://github.com/NVIDIA/Model-Optimizer/issues/869
state: closed | updated: 2026-06-15T13:47:32Z
labels: stale, onnx.quantization, internal bug filed

## 正文

**Before submitting an issue, please make sure it hasn't been already addressed by searching through the [existing and past issues](https://github.com/NVIDIA/Model-Optimizer/issues?q=is%3Aissue).**

## Describe the bug
<!-- Description of what the bug is, its impact (blocker, should have, nice to have) and any stack traces or error messages. -->

- I'd used tensort8.6.1 to convert an existing onnx model with qdq nodes, say a model exported using Model Optimizer Toolkit, to run on a orin-equiped platform. However, the inference result of the engine is not good as expected, it showed a large discrepancy compared with the original qdq onnx. For convenience, i again tried trt8.6.1 and trt10.11 on my local x86-64 workstation to convert the onnx into engine, to verify if i can see the same phenomenon. Unfortunately, yes. I calculated cosine similarity between qdq onnx and generated engine according to trt8.6 and trt10.11 respectively.
<div style="display: flex; gap: 1px;justify-content: center;">
  <img src="https://github.com/user-attachments/assets/fd15278e-bab4-4865-84ce-b34607cfa80c" alt="trt10.11 qdq onnx vs engine" style="width: 15%;">
  <img src="https://github.com/user-attachments/assets/9ba34c89-353c-4948-b21d-f8f36f7beb21" alt="trt8.6.1 qdq onnx vs engine" style="width: 15%;">
</div>
As depicted above, we can indeed see a large discrepancy.  

### Steps/Code to reproduce  #bug
<!-- Please list *minimal* steps or code snippet for us to be able to reproduce the bug. -->
<!-- A helpful guide on on how to craft a minimal bug report http://matthewrocklin.com/blog/work/2018/02/28/minimal-bug-reports. -->

- convert command:
`trtexec --onnx=quant0206.onnx --saveEngine=quant_0206.engine --dumpProfile=true --best --verbose=true`

### Expected behavior

### Who can help?

<!-- To expedite the response to your issue, it would be helpful if you could identify the appropriate person(s) to tag using the @ symbol.
If you are unsure about whom to tag, you can leave it blank, and we will make sure to involve the appropriate person. -->

- I really appreciate if anyone can help solve the problem, or some instructive advice on how to solve it. I guess the problem may be caused by the conversion process from onnx to trt in which precision lost occurred in some operators.  

## System information

<!-- Run this script to automatically collect system information: https://github.com/NVIDIA/Model-Optimizer/blob/main/.github/ISSUE_TEMPLATE/get_system_info.py -->

- Container used (if applicable): nvcr.io/nvidia/tensorrt-llm/release:1.0.0
- OS (e.g., Ubuntu 22.04, CentOS 7, Windows 10): ? <!-- If Windows, please add the `windows` label to the issue. --> Ubuntu 20.04
- CPU architecture (x86_64, aarch64): x86_64
- GPU name (e.g. H100, A100, L40S): GT3060
- GPU memory size: 12G
- Number of GPUs: 1
- Library versions (if applicable):
  - Python: 3.9
  - ModelOpt version or commit hash: 0.40.0
  - CUDA: nvcc: NVIDIA (R) Cuda compiler driver
Copyright (c) 2005-2021 NVIDIA Corporation
Built on Wed_Jun__2_19:15:15_PDT_2021
Cuda compilation tools, release 11.4, V11.4.48
Build cuda_11.4.r11.4/compiler.30033411_0
  - PyTorch: 2.0
  - Transformers: not used
  - TensorRT-LLM: not used
  - ONNXRuntime: 1.19.2-gpu
  - TensorRT: trt8.6 or trt10.11
- Any other details that may help: 


## 评论 (18)

### zzqiuzz · 2026-02-09

[quant0206.zip](https://github.com/user-attachments/files/25175911/quant0206.zip)

### zzqiuzz · 2026-03-04

@ajrasane hello, same issue mentioned @ https://github.com/NVIDIA/TensorRT/issues/4708

### zzqiuzz · 2026-03-10

I again used tensort 8.6.1.6  to quantize the model implicitly  in the same quantization setting, say the same calibration data, calibration observer. The quantized engine outputs better results than that model opt does. Is this normal?  any updates here? @yeyu-nvidia  Thanks.

### yeyu-nvidia · 2026-03-10

@ajrasane Can you please take a look?

### gcunhase · 2026-04-06

@zzqiuzz thank you for bringing this to our attention.

I see that you provided the quantized model. Can you also please provide the following files?
1. Non-quantized ONNX model;
2. ORT inference script;
3. Cosine similarity script.

Thanks!

### zzqiuzz · 2026-04-08

@gcunhase Thank you for your help!  The zip file attatched below involved a non-quantized onnx model and an inference script including onnx inference, trt inference and result comparison using cosine similarity. You can refer it for more details.

[for_issue.zip](https://github.com/user-attachments/files/26557383/for_issue.zip)

### gcunhase · 2026-04-09

After some modifications in the script (ex: `GPUExecutionProvider` -> `CUDAExecutionProvider`) and creating a `requirements.txt`, I was able to replicate the ORT vs TRT output discrepancies with ORT 1.24.2 and TRT 10.14.

Debugging it (internal bug: 6064074).

Thanks!

### gcunhase · 2026-04-10

@zzqiuzz 
The **root cause** is that ORT and TRT interpret Q/DQ nodes fundamentally differently:
- **ORT simulates quantization in float** [1]. For a `DQ → Conv → Q` pattern, ORT executes it in 3 separate kernels:
    1. `DequantizeLinear`: INT8 × scale → FP16
    2. `Conv`: runs in FP16 with the dequantized inputs and dequantized weights
    3. `QuantizeLinear`: FP16 / scale → round → INT8
    The Conv itself executes at FP16 precision. Q/DQ just rounds the inputs/outputs.
 
- **TRT fuses Q/DQ into native INT8 kernels** [2]. For the same `DQ → Conv → Q` pattern, TRT fuses the entire chain into a single INT8 Conv kernel:
  1. `Conv`: INT8 inputs × INT8 weights → INT32 accumulator → rescale → INT8 output
  2. Intermediate values between fused ops (e.g., Clip inside a `Conv → Clip → Q` fusion) never materialize at FP16 — they stay in INT8/INT32

This causes three specific divergences:
- **Accumulation precision**: ORT accumulates Conv dot products in FP16 (10-bit mantissa). TRT accumulates in INT32 then truncates back to INT8. These produce different rounding at every multiply-add.
- **Fusion boundaries eliminate intermediate precision**: When TRT fuses `DQ → Conv_4 → Clip → Q → DQ → Conv_9 → Clip → Q`, the Clip output between `Conv_4` and `Conv_9` stays internal to the fused kernel at reduced precision. ORT materializes it as a full FP16 tensor. This is exactly why tensor `485` (after the first fused block) already shows cosine 0.888.
- **Cumulative rounding**: Each fused block introduces a small rounding difference. Through ~40 backbone Conv layers, these compound: 0.999 → 0.888 → 0.822 → 0.729 → 0.407 → 0.601. By the time data reaches the heads, ORT and TRT are computing on substantially different tensors.

**In short**: the Q/DQ ONNX model specifies what to quantize, but ORT computes in float with rounded values while TRT computes natively in INT8. They're not mathematically equivalent, and the gap grows with network depth.

**The practical path forward** is to validate the INT8 output against the FP32 or FP16 baseline within ORT or TRT, not cross-compare across SDKs. Assume that you're running in TRT. If TRT INT8 vs the TRT baseline is acceptable, the quantization is fine regardless of what ORT's simulation says. For that, you must use real calibration data in ModelOpt via `--calibration_data_path`, so that the scales are not generated from random data. The same way, real data should be used for accuracy evaluation during inference.

### Sources
**[1]** Inferred from the ORT documentation, source code, and issue reports:
- [ORT quantization docs](https://onnxruntime.ai/docs/performance/model-optimizations/quantization.html) state QDQ format "inserts DeQuantizeLinear(QuantizeLinear(tensor)) between the original operators to simulate the quantization and dequantization process"
- ORT CUDA provider source (quantize_linear.cc) registers only QuantizeLinear and DequantizeLinear as standalone CUDA kernels. There is no QLinearConv registered for CUDA — meaning Conv runs as a separate standard (float) kernel.
[GitHub Issue #12229](https://github.com/microsoft/onnxruntime/issues/12229) confirms this at runtime: "CUDA kernel not found in registries for Op type: QLinearConv" — when ORT tries to use the fused quantized Conv op, CUDA EP doesn't have it.
- [ORT quantization docs](https://onnxruntime.ai/docs/performance/model-optimizations/quantization.html) also state: "ONNX Runtime leverages the TensorRT Execution Provider for quantization on GPU" — implying CUDAExecutionProvider is not the intended path for INT8 execution.

**[2]** See more information in https://docs.nvidia.com/deeplearning/tensorrt/latest/inference-library/work-quantized-types.html#tensorrt-processing-of-q-dq-networks :
> Quantizable layers are deep-learning layers that can be converted to quantized layers by fusing with IQuantizeLayer and IDequantizeLayer instances. When TensorRT performs these fusions, it replaces the quantizable layers with quantized layers that operate on quantized data using compute operations suitable for quantized types.

### zzqiuzz · 2026-04-14

Thank you very much.
However, I have a question. The QDQ model generated by ModelOpt contains quantization scales, which are supposed to be parsed by TensorRT and converted into an engine with quantized operators. But now it turns out that the resulting engine performs much worse than the QDQ model. How can I fix this? Do I have to use implicit quantization instead? I had ttried the implicit quantization and indeed saw a good performance.


### gcunhase · 2026-04-14

@zzquizz are you using real calibration data with `--calibration_data_path`? If so, can you please share it?
Real calibration data is needed for accuracy retention.

### zzqiuzz · 2026-04-15

@gcunhase Yes, we indeed use the real calibration data. The download link to the calbration data with batchsize = 128:
https://drive.google.com/file/d/1Pwfk16_ulNVmIBmzhcFqyAYdk7dxYBB4/view?usp=sharing
Here's our quantization pipeline:
1. we firstly fed the orginal float32 onnx and real calibration data to the ModelOpt and got a qdq model(minmax observer);
2. Then we used TensorRt8.6 `trtexec` to parse the qdq model to get the quant engine;
3. we evaluated the engine and saw a  worse performance than the qdq onnx.

Thanks.

### gcunhase · 2026-04-15

Thanks for sharing the data! Will look into this further.

### gcunhase · 2026-04-17

## Calibration data investigation
I investigated INT8 quantization accuracy on ORT and TRT using the real calibration data provided. During inference, sample 0 from calibration set was used.

**Key Takeaways**:
1. **INT8 quantization accuracy is poor on both runtimes**: ORT FP32 vs ORT INT8 shows the same magnitude of error as TRT FP32 vs TRT INT8. The issue is not  necessarily ORT vs TRT, but INT8 PTQ quality.
2. **The ORT vs TRT INT8 gap is a secondary effect**: The cross-runtime cosine similarities are in the same ballpark as each runtime's own FP32 vs INT8 gap.
3. **Real calibration data did not fix the accuracy**: The model architecture is inherently sensitive to INT8 quantization.
4. **Outputs that match well** (`double_left/right_mask`, `max_double_cls/color_cls`, `keypoints_center_offset`) do so because they use Softmax/ArgMax (which normalize away errors) or have near-zero weights.
5. **The calibration method makes no meaningful difference for this model**: The INT8 accuracy loss is the same whether using entropy or minmax with real data. This reinforces that the model architecture itself is sensitive to INT8 quantization.

## Model architecture investigation
The model under investigation here is a **MobileNet-style depthwise separable backbone with a multi-task CenterNet-style detection head**. See the architecture:
- **Backbone**: Depthwise separable convolutions (3x3 depthwise + 1x1 pointwise), 24 residual Add connections, channel progression 32→64→128→256→512. This is MobileNetV2 or a close variant.
- **Neck**: ConvTranspose upsampling + Concat (FPN-like feature fusion), BatchNormalization
- **Heads**: 3 task-specific heads (bbox/keypoints, lane, double/curb) with CenterNet-style heatmap + regression outputs

MobileNet architectures are known to be sensitive to INT8 quantization. The reasons:
1. **Depthwise separable convolutions** — The 3x3 depthwise Conv has only 1 input channel per group (ex: Conv_8), so each output value is a sum of just 9 multiplications. With INT8, rounding errors in those 9 values have outsized impact. Standard 3x3 Convs sum over C_in × 9 values, which averages out errors.
2. **1x1 pointwise projections** — These are cross-channel linear projections where each output is a dot product over all input channels. INT8 rounding on the depthwise output propagates directly through the pointwise layer. This is exactly why Conv_262, Conv_26, Conv_171 (all 1x1 pointwise) are the most sensitive.
3. **Narrow bottlenecks** — MobileNet uses inverted residual blocks with narrow bottleneck channels (1x1->3x3->1x1 Convs instead of 3x3->1x1->3x3 Convs in ResNet), so information passes through low-dimensional representations where each value carries more information and quantization error has more impact.

This is well-documented in the literature, where MobileNets and other lightweight architectures consistently show larger accuracy drops from INT8 PTQ compared to ResNet or other wider architectures. See _Yun & Wong, ["Do All MobileNets Quantize Poorly? Gaining Insights into the Effect of Quantization on Depthwise Separable Convolutional Networks Through the Eyes of Multi-scale Distributional Dynamics"](https://openaccess.thecvf.com/content/CVPR2021W/MAI/papers/Yun_Do_All_MobileNets_Quantize_Poorly_Gaining_Insights_Into_the_Effect_CVPRW_2021_paper.pdf) (CVPRW 2021)_. This is the most directly relevant paper, and it specifically studies why MobileNets quantize poorly. The paper documents that _"Despite the success of MobileNets, there has been a well-documented phenomenon wherein simple post-training static quantization completely destroys their accuracy"_ and attributes it to the dynamic range mismatch between individual depthwise-conv channels and the overall tensor range.

QAT is the standard recommendation for quantizing MobileNets. Unfortunately, QAT is not supported in the ONNX workflow, so you'd have to go the torch quantization path, which is still being validated for Vision models (see https://github.com/NVIDIA/Model-Optimizer/pull/1263). You're welcome to try that path though and see if it helps. You may also refer to ModelOpt's [torch QAT example for ResNet-50](https://github.com/NVIDIA/Model-Optimizer/tree/main/examples/cnn_qat).

### zzqiuzz · 2026-04-21

@gcunhase Thank you for your assistance!
As expected, MobileNet-style models are highly sensitive to quantization. We deployed the aforementioned model on the Orin platform via implicit quantization with TensorRT 8.6, and added the following convolution layers to the quantization blacklist: "Conv_300", "Conv_302", "Conv_303", "Conv_304", "Conv_305", "Conv_307". This was because we observed that these convolutions significantly degrade the performance of the quantized model.
However, when we blacklisted these identical operators in ModelOpt to generate a QDQ model under the same quantization configuration, the resulting engine exhibited severely degraded performance. Our goal is for ModelOpt to produce behavior consistent with TensorRT’s implicit quantization. I guess there may exist some differences between the scaling factors generated by ModelOpt and TRT PTQ to conduct a deeper investigation.

### gcunhase · 2026-04-22

> We deployed the aforementioned model on the Orin platform via implicit quantization with TensorRT 8.6

Have you tried using the calibration cache from this workflow with ModelOpt instead of the calibration data? You can do so via `--calibration_cache_path`.

### zzqiuzz · 2026-04-23

Yes, I attempted to generate a QDQ model using the --calibration_cache_path parameter in ModelOpt（calibration_cache file generated by Trt）. It was observed that scales of 92 operators in total deviate slightly from those of the corresponding operators in the model which did not read the calib file.

<img width="1097" height="626" alt="Image" src="https://github.com/user-attachments/assets/7ac17d60-9402-4934-b029-b0408d769ec7" />

Subsequently, I parsed the newly generated QDQ model with TensorRT to construct a TRT engine. The inference results still present a substantial discrepancy relative to the results from the implicit precision mode.

### gcunhase · 2026-04-23

Do you mean that the quantized model generated with the calibration cache via ModelOpt is also not performing well?

### gcunhase · 2026-06-15

Closing as stale.
