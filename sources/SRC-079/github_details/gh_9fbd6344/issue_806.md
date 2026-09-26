# [Issue #806] Quantized models in FP8/NVFP4 QAT do not show an improvement in accuracy when compared with PTQ models

source: https://github.com/NVIDIA/Model-Optimizer/issues/806
state: closed | updated: 2026-06-19T04:38:07Z
labels: bug, question, stale, investigating, waiting for feedback, torch.quantization

## 正文

**Before submitting an issue, please make sure it hasn't been already addressed by searching through the [existing and past issues](https://github.com/NVIDIA/Model-Optimizer/issues?q=is%3Aissue).**

## Describe the bug
<!-- Description of what the bug is, its impact (blocker, should have, nice to have) and any stack traces or error messages. -->

- I followed the notebook https://github.com/NVIDIA/Model-Optimizer/blob/main/examples/llm_qat/notebooks/QAT_QAD_Walkthrough.ipynb to perform NVFP4 QAT (as well as FP8 QAT). Both models when deployed using vLLM and evaluated using ifEval benchmarks show a great reduction in accuracy when compared with PTQ quantized models. Its my understanding that QAT models should show improvement in accuracy when compared with PTQ quantized models.

### Steps/Code to reproduce bug
<!-- Please list *minimal* steps or code snippet for us to be able to reproduce the bug. -->
<!-- A helpful guide on on how to craft a minimal bug report http://matthewrocklin.com/blog/work/2018/02/28/minimal-bug-reports. -->

- Calibration Size 512
- model used: meta-llama/Llama-3.1-8B-Instruct
- https://github.com/elizabetht/language-modeling-from-scratch/blob/main/quantization/model-optimizer/qat/output_executed_nvfp4_qat.ipynb

### Expected behavior
Accuracy evaluations should improve when compared with PTQ models using same format (ie NVFP4/FP8)

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


## 评论 (3)

### realAsma · 2026-05-21

Hi @elizabetht 

QAT could regress depending on the dataset and other QAT settings; If the dataset is not aligned with the downstream evaluation this is an expected behavior;

Could you try out QAD https://github.com/NVIDIA/Model-Optimizer/tree/main/examples/llm_qat#end-to-end-qad-example

See our paper on why QAD is better to recover reasoning abilities - https://research.nvidia.com/labs/nemotron/files/NVFP4-QAD-Report.pdf

### github-actions[bot] · 2026-06-05

Issue has not received an update in over 14 days. Adding stale label.

### github-actions[bot] · 2026-06-19

This issue was closed because it has been 14 days without activity since it has been marked as stale.
