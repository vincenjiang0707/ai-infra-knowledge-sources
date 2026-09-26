# [Issue #1615] INT4 Quantization Export

source: https://github.com/NVIDIA/Model-Optimizer/issues/1615
state: open | updated: 2026-06-08T03:22:40Z
labels: bug, torch.quantization, triaged

## 正文

**Before submitting an issue, please make sure it hasn't been already addressed by searching through the [existing and past issues](https://github.com/NVIDIA/Model-Optimizer/issues?q=is%3Aissue).**

## Describe the bug
Hi, I encountered an issue. I have tried quantizing the vit_base_patch16_224 model in INT4 . The problem is that when exporting to ONNX, the pre_process function in INT4QuantExporter can only match subgraphs like DequantizeLinear -> Reshape -> Transpose -> MatMul/Gemm. In fact, there are other subgraphs, such as DequantizeLinear -> Transpose -> MatMul/Gemm, which cannot be handled successfully. How can I fix this? Thanks.

- ?

### Steps/Code to reproduce bug
<!-- Please list *minimal* steps or code snippet for us to be able to reproduce the bug. -->
<!-- A helpful guide on on how to craft a minimal bug report http://matthewrocklin.com/blog/work/2018/02/28/minimal-bug-reports. -->

- ?

### Expected behavior

### Who can help?

<!-- To expedite the response to your issue, it would be helpful if you could identify the appropriate person(s) to tag using the @ symbol.
If you are unsure about whom to tag, you can leave it blank, and we will make sure to involve the appropriate person. -->

- ?

## System information

<!-- Run this script to automatically collect system information: https://github.com/NVIDIA/Model-Optimizer/blob/main/.github/ISSUE_TEMPLATE/get_system_info.py -->

- Container used (if applicable): ?
- OS (e.g., Ubuntu 22.04, CentOS 7, Windows 10): ? <!-- If Windows, please add the `windows` label to the issue. -->
- CPU architecture (x86_64, aarch64): ?
- GPU name (e.g. H100, A100, L40S): ?
- GPU memory size: ?
- Number of GPUs: ?
- Library versions (if applicable):
  - Python: ?
  - ModelOpt version or commit hash: ?
  - CUDA: ?
  - PyTorch: ?
  - Transformers: ?
  - TensorRT-LLM: ?
  - ONNXRuntime: ?
  - TensorRT: ?
- Any other details that may help: ?


## 评论 (2)

### ChenhanYu · 2026-06-05

## Triage Analysis

| Field | Value |
|-------|-------|
| Classification | Bug |
| Severity | Medium |
| Complexity | Moderate |
| Auto-fixable | No |

### Summary
The INT4QuantExporter's pre_process method assumes a fixed subgraph pattern of DequantizeLinear -> Reshape -> Transpose -> MatMul/Gemm, but fails when the graph has alternative patterns like DequantizeLinear -> Transpose -> MatMul/Gemm (without Reshape). This occurs when quantizing models like vit_base_patch16_224 where the weight tensor doesn't require reshaping before transposition.

### Root Cause / Approach
In `INT4QuantExporter.pre_process()`, the code unconditionally assumes the first child node of a DequantizeLinear node is a Reshape node (line: `assert reshape_node.op_type == "Reshape"`). When the exported ONNX graph has DequantizeLinear -> Transpose -> MatMul/Gemm (skipping Reshape), this assertion fails. The code needs to handle multiple possible subgraph patterns between DequantizeLinear and MatMul/Gemm nodes.

### Suggested Fix
Modify the `pre_process` method to detect the actual subgraph pattern after each DequantizeLinear node. Instead of unconditionally assuming a Reshape node, check the op_type of the first child node and handle multiple patterns: (1) DequantizeLinear -> Reshape -> Transpose -> MatMul/Gemm, (2) DequantizeLinear -> Transpose -> MatMul/Gemm, (3) DequantizeLinear -> MatMul/Gemm directly. For pattern (2), skip the Reshape-related logic, get the target shape from the weight tensor itself or from value_info, and proceed with the Transpose handling. For pattern (3), simply skip both Reshape and Transpose handling.

### Relevant Files
- `modelopt/onnx/export/int4_exporter.py`
- `modelopt/onnx/export/base_exporter.py`
- `modelopt/torch/quantization/export_onnx.py`

---
_Auto-triaged by pensieve `/magic-triage`_

### zajzhuaijun · 2026-06-08

thanks.I have fixed this problem by distinguishing DQ came from int4 or int8. By the way ,I found another problem. I quantized vit model with mode FP8. Then compile use command “trtexec --onnx=vit_base_patch16_224_fp8_fp8_default_cfg.onnx --stronglyTyped --verbose --profilingVerbosity=detailed”. And I received the Error msg:"Internal Error: MyelinCheckException: nvrtc_compile.cpp:1110: CHECK(success) failed. NVRTC Compilation failure
[06/08/2026-11:17:53] [E] Error[9]: Error Code: 9: Skipping tactic 0x0000000000000000 due to exception [myelin_graph.h:attachExceptionMsgToGraph:960] MyelinCheckException: nvrtc_compile.cpp:1110: CHECK(success) failed. NVRTC Compilation failure
[06/08/2026-11:17:53] [V] [TRT] {ForeignNode[/head/weight_quantizer/fp8_weights...(Unnamed Layer* 1722) [ElementWise]]} (Myelin[0x80000023]) profiling completed in 59.8356 seconds. Fastest Tactic: 0xd15ea5edd15ea5ed Time: inf
[06/08/2026-11:17:53] [E] Error[10]: IBuilder::buildSerializedNetwork: Error Code 10: Internal Error (Could not find any implementation for node {ForeignNode[/head/weight_quantizer/fp8_weights...(Unnamed Layer* 1722) [ElementWise]]}.)". After debug the code ,I found adding " n_sm = FP8QuantExporter._insert_qdq_after_softmax(graph)" will cause the compile error.Why?
