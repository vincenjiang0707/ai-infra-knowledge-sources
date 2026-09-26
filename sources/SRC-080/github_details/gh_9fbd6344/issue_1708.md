# [Issue #1708] MiniMax M3 nvfp4 ckpt

source: https://github.com/NVIDIA/Model-Optimizer/issues/1708
state: open | updated: 2026-06-23T14:43:25Z
labels: feature request

## 正文

One of the main features of NVIDIA latest flagship Blackwell GPUs is NVFP4, the ability to have better perf at similar accuracy to BF16 due to having block size 16 and using E4M3 as the block scale instead of E8M0 unlike MXFP4.

what is the timelines for nvfp4 ckpts for MiniMax M3 will be out? https://huggingface.co/nvidia/models?search=nvfp4

OpenRouter (which hobbysts and small enterepises) use consistently show that MiniMax M3 for the past weeks consistently ranks high in popularity

+viz @xinli-sw @ncomly-nvidia @kedarpotdar-nv  @mxinO @Edwardf0t1


 
<img width="606" height="451" alt="Image" src="https://github.com/user-attachments/assets/5979f9e5-ce1a-4b90-9929-61e0f0e28305" />

## 评论 (1)

### Trenton-Starkey · 2026-06-23

Hi this is WIP please stay tuned to https://huggingface.co/collections/nvidia/inference-optimized-checkpoints-with-model-optimizer
