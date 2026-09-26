# [Issue #224] GPU specification used for EAGLE-3 training and inference?

source: https://github.com/SafeAILab/EAGLE/issues/224
state: open | updated: 2025-11-12T05:57:29Z
labels: 

## 正文

Hello, 
I'm currently studying your work and would like to reproduce your experiments more precisely.

Could you please share the GPU specifications (e.g., model type, number of GPUs, memory capacity) that were used for:
1. Training EAGLE-3
2. Running inference with EAGLE-3?

Thank you in advance!

## 评论 (1)

### LESSSE · 2025-11-12

According to the [EAGLE3 paper](https://arxiv.org/abs/2503.01840) there are 2 contradictory pieces of information related to inference results on LLaMA-Instruct 3.1 8B for the MT- Bench dataset (page 8, table 5) :
1) "Throughput improvement under different batch sizes on A100 and LLaMA-Instruct 3.1 8B for the MT- Bench datase"
2) "and the results on RTX3090 and LLaMA-Instruct 3.1 8B are shown in"
I would like to have a clarification for which one of these is correct. Thanks

@junghye01 you probably can find more info on the paper there, but it wouldn't hurt having this info in the README file
