# [Issue #1850] Provide better way of recommending a dataset for global distillation for puzzletron algorithm

source: https://github.com/NVIDIA/Model-Optimizer/issues/1850
state: closed | updated: 2026-07-22T10:49:19Z
labels: feature request, torch.pruning

## 正文

Currently, it is unclear which dataset to use for global distillation for different models compressed with Puzzletron and Minitron.

Create a tutorial or a tool to recommend the best dataset for a particular model to compress, e.g. Llama 3.2 3B or Qwen3 8B. Answer those research questions based on the image below:
- Why wikitext/nemotronv2 datasets help to recover MMLU for Qwen3 8B but are harmful for Llama 3.2 3B
- Why wikitext helps more than nemotronv2 to improve MMLU for LLama 3.2 3B

Compressed and distilled models with Puzzletron:
<img width="1727" height="380" alt="Image" src="https://github.com/user-attachments/assets/d52a210a-23de-42af-8f3f-1aed7316e676" />

Notes:
- Look at @kevalmorabia97 a[blation on dataset selection for minitron distillation](https://github.com/NVIDIA/Model-Optimizer/blob/main/examples/megatron_bridge/tutorials/NVIDIA-Nemotron-3-Nano-30B-A3B-BF16/ABLATIONS.md#distillation)

## 评论 (1)

### danielkorzekwa · 2026-07-22

Moved to internal Nvidia task
