# [Issue #362] ONNX PTQ with NVFP4 fails on Vision CNN models

source: https://github.com/NVIDIA/Model-Optimizer/issues/362
state: closed | updated: 2026-08-14T14:05:28Z
labels: bug

## 正文

## Describe the bug
/examples)/onnx_ptq/torch_quant_to_onnx.py example is given and working for VIT based model. However when trying with Vision based model MobileNetv5_300m, Resnet50, Convnext, etc errors are produced consistently. A note in the documentation on the current limitations on what models can be converted using ONNX PTQ and nvfp4 would be helpful.

### Steps/Code to reproduce bug
cd /examples)/onnx_ptq/
python torch_quant_to_onnx.py \
    --timm_model_name=resnet50 \
    --quantize_mode=nvfp4 \
    --onnx_save_path=resnet50_nvfp4.onnx

### Expected behavior
Produces nvfp4 quantized onnx file without error.

## System information

- OS: Ubuntu 24.04.2 LTS
- CPU architecture: x86_64
- GPU name: NVIDIA RTX PRO 6000 Blackwell Workstation Edition
- GPU memory size: 95.6 GB
- Number of GPUs: 1
- Library versions (if applicable):
  - Python: 3.12.3
  - ModelOpt version or commit hash: 0.37.0.dev56+g26c203abd.d20250924
  - CUDA: 13.0
  - PyTorch: 2.10.0.dev20250924+cu130
  - Transformers: 4.56.2
  - ONNXRuntime: 1.22.0
  - TensorRT: 10.13.3.9


## 评论 (2)

### ajrasane · 2025-09-30

TensorRT does not support [Convolution](https://docs.nvidia.com/deeplearning/tensorrt/archives/tensorrt-861/operators/docs/Convolution.html#convolution) layers in NVFP4 precision. 
Hence this example targets and works well for ViT based models.
During torch quantization, we exclude the Convolution quantization with this [function](https://github.com/NVIDIA/TensorRT-Model-Optimizer/blob/17439e653df905aac91b7aa208543223f07dc7ec/examples/onnx_ptq/torch_quant_to_onnx.py#L46).

### geoffrey-delhomme · 2026-08-14

Adding a concrete data point in support of reopening this, or of documenting the limitation.

We hit the same wall on a convolutional detector (YOLOv8n) with ModelOpt 0.44.0:

- The ONNX CLI's `--quantize_mode` accepts only `fp8` / `int8` / `int4`.
- The Python dispatcher raises `RuntimeError: Invalid quantization mode choice` for anything else.
- The only `nvfp4` references in the ONNX path are dead opset-lookup plumbing.

We worked around it with ONNX-graph surgery, inserting genuine `FLOAT4E2M1` QDQ ourselves. That then runs into a separate TensorRT issue: a **W4A16 build succeeds while silently realizing FP32**, with no warning that the requested precision was discarded (filed separately as NVIDIA/TensorRT#4833).

A single documented line — *"ONNX PTQ NVFP4 is MatMul/Linear only"* — would have saved that entire detour. Either reopening this to track CNN support, or stating the limitation in the ONNX PTQ docs, would be a real improvement for anyone evaluating NVFP4 on vision models.

