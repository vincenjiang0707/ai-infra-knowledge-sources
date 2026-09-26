# [Issue #1752] glm-5.2 nvfp4 checkpoint

source: https://github.com/NVIDIA/Model-Optimizer/issues/1752
state: closed | updated: 2026-06-28T14:33:08Z
labels: feature request

## 正文

### Detailed description of the requested feature
We are currently running `nvidia/glm-5.1-nvfp4` on blackwell GPUs. It would be great to have an nvfp4 checkpoint of the original glm-5.2 weights


## 评论 (5)

### Trenton-Starkey · 2026-06-23

Hi this is WIP - please stay tuned to https://huggingface.co/collections/nvidia/inference-optimized-checkpoints-with-model-optimizer 

### gaby · 2026-06-25

@Trenton-Starkey Thank you, looking forward. Looking at GLM-5.1, the size difference with FP8 is really promising. 

### gaby · 2026-06-26

@bbartels https://huggingface.co/nvidia/GLM-5.2-NVFP4

### gaby · 2026-06-26

@Trenton-Starkey Is nvfp4 kv cache supported by these weights with vLLM ?

Nvidia blog: https://developer.nvidia.com/blog/optimizing-inference-for-long-context-and-large-batch-sizes-with-nvfp4-kv-cache/

HuggingFace Discussion: https://huggingface.co/nvidia/GLM-5.2-NVFP4/discussions/1

### gaby · 2026-06-28

GLM-5.2 improvements and NVFP4 cache is being tracked here: https://github.com/vllm-project/vllm/issues/46654
