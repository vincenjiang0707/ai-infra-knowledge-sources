# [Issue #1334] How to add eval dataset into paddleOCR-VL SFT

source: https://github.com/PaddlePaddle/ERNIE/issues/1334
state: closed | updated: 2025-11-17T08:19:18Z
labels: 

## 正文

Hi all,
Recently I'm trying to finetune paddleOCR-VL(0.9B) with SFT following the guide : https://github.com/PaddlePaddle/ERNIE/blob/develop/docs/paddleocr_vl_sft.md .
However, the [example yaml script](https://github.com/PaddlePaddle/ERNIE/blob/develop/examples/configs/PaddleOCR-VL/sft/run_ocr_vl_sft_16k.yaml) seems doesn't support the dataset eval, even I split the example dataset to 2 parts manually.

Is that possible to have eval dataset in this SFT training ? Or is there a replacement to use transformer/peft/trl library to finetune the model? (Due to the flash mask , it looks there is no free lunch from huggingface familiy ....)

BR

## 评论 (5)

### jerrywind · 2025-11-07

Hi @lugimzzz,
what's the progress ? 

### forBlank · 2025-11-07

Hi, during the training process, checkpoints are saved periodically based on the `save_steps` parameter. We recommend using these checkpoints with PaddleOCR to run inference on your validation set, which allows you to evaluate the training performance.

For more details on PaddleOCR inference usage, please refer to the documentation: https://www.paddleocr.ai/latest/version3.x/pipeline_usage/PaddleOCR-VL.html

### jerrywind · 2025-11-09

Hi @forBlank ,
Thanks for your comments. 
In an another word, you means currently PaddleOCR-VL doesn't support training with evaluating ?
Some RL fine-tunes like DPO couldn't run with training step together ?
BR

### forBlank · 2025-11-13

Hi @jerrywind ,
For training with evaluating: It is on our roadmap and will be supported in a future release.
For RL in OCR: The OCR task is a typical perception and recognition problem with a deterministic output. We believe that Supervised Fine-Tuning (SFT) is sufficient for this, so we don’t have plans to support Reinforcement Learning (RL) at this time. Could you please describe the specific requirement or use case you have in mind for using RL?

### jerrywind · 2025-11-17

Hi @forBlank,
I'm tring to do some research on solving the traditional chinese characters with similar shapes, there is a proper way that to list the similiar shapes list of chars and use RL to tell model about what's right and what's wrong ....
Anyway, I could use other techs to overcome it .
That's for you response.
This ticket could be closed :)
BR
