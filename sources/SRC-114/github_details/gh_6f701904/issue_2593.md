# [Issue #2593] Incorrect DeepSeek-R1 version in Inference Storage

source: https://github.com/mlcommons/inference/issues/2593
state: closed | updated: 2026-08-11T14:48:44Z
labels: 

## 正文

[MLCommons Inference Storage](https://inference.mlcommons-storage.org/index.html#deepseek-r1-benchmark) hosts [DeepSeek-r1-0528](https://huggingface.co/deepseek-ai/DeepSeek-R1-0528):
<img width="1035" height="282" alt="Image" src="https://github.com/user-attachments/assets/d64c98c2-fc98-421b-8fe2-e646f1a0bd8c" />

This is different from [DeepSeek-r1](https://huggingface.co/deepseek-ai/DeepSeek-R1) required by the reference:

<img width="829" height="206" alt="Image" src="https://github.com/user-attachments/assets/beda6284-a3b5-4b93-b3b2-d43d04554331" />

and used e.g. in [NVIDIA-based v6.0 submissions](https://github.com/mlcommons/inference_results_v6.0/tree/main/closed/NVIDIA/code/deepseek-r1/tensorrt#download-model):

<img width="1263" height="412" alt="Image" src="https://github.com/user-attachments/assets/c4354d98-040a-4824-b470-fb432dc342e2" />

## 评论 (1)

### hanyunfan · 2026-08-11

Solved
