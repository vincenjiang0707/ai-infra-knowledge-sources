# [Issue #1424] How to train ERNIE-4.5-300B-A47B-Base on multiple machines, is there a corresponding tutorial?

source: https://github.com/PaddlePaddle/ERNIE/issues/1424
state: open | updated: 2026-01-13T06:07:31Z
labels: 

## 正文

(empty)

## 评论 (1)

### nepeplwu · 2026-01-13

@YZBPXX 
There isn't a separate tutorial specifically for this part, but you can refer to the following resources:
1. https://github.com/PaddlePaddle/ERNIE/blob/release/v1.5/docs/erniekit.md#31-training-resources  The table here provides the training configurations and resource requirements that we have verified. Simply change the model in the configuration to the Base model.
2. Refer to our command-line tool usage instructions: https://github.com/PaddlePaddle/ERNIE/blob/release/v1.5/docs/erniekit.md#31-training-resources, which explains how to specify commands in a multi-machine environment.
3. https://github.com/PaddlePaddle/ERNIE/blob/release/v1.5/docs/erniekit.md#33-supervised-fine-tuning This section explains the data format and considerations required for SFT training.
