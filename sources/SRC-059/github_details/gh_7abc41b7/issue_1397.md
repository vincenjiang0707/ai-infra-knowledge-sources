# [Issue #1397] Is LoRA mode fine tuning possible for paddleocr-vl-0.9b?

source: https://github.com/PaddlePaddle/ERNIE/issues/1397
state: closed | updated: 2025-12-20T02:43:18Z
labels: 

## 正文

I am trying to fine-tune paddleocr-vl-0.9b for devanagari text recognition, using full fine-tuning mode gave OOM error on my machine, now i am looking into whether fine-tuning this model in LoRA mode is possible or not. If it is, could you please point me to any resources to achieve this (tutorials, how to change the config files etc.)

I have tried by changing the fine_tuning parameter to LoRA and adding lora_rank: 8 in the yaml file, but i am getting: 
`TypeError: PretrainingTrainer.save_model() takes from 1 to 2 positional arguments but 3 were given`



## 评论 (7)

### forBlank · 2025-12-17

@DOOMBOT0 Thanks. We have addressed the problem and made the necessary fixes. Please pull the **latest** code from the **develop** branch and try again.

### DOOMBOT0 · 2025-12-17

@forBlank where can i pull the latest code from the develop branch? I haven't seen the option to do that yet.


### forBlank · 2025-12-17

@DOOMBOT0 Sorry, it's here https://github.com/PaddlePaddle/ERNIE/tree/develop. Let us know if you encounter any further issues.

### DOOMBOT0 · 2025-12-17

@forBlank   Thank you very much,if possible, can you also point to anything that teaches how to do lora finetuning for this model? eg: how to change the configuration file parameters to perform lora fine-tuning etc.

### forBlank · 2025-12-17

@DOOMBOT0 You are on the right track—setting the `fine_tuning` parameter to LoRA will start the LoRA SFT. However, the hyperparameters used for full-parameter fine-tuning are not perfectly suitable for LoRA. Currently, our suggestion is to increase the `learning_rate` and `packing_size`. We are still exploring the optical hyperparameters/best practices for LoRA with this model, so please stay tuned for future updates.

### DOOMBOT0 · 2025-12-17

@forBlank Thank you for your help, i will implement your suggestions for now and report if anything reportable occurs. I will close this issue for now.

### aaiccee · 2025-12-20

> [@DOOMBOT0](https://github.com/DOOMBOT0)您的思路是对的——将`fine_tuning`参数设置为 LoRA 将启动 LoRA SFT。但是，用于全参数微调的超参数并不完全适用于 LoRA。目前，我们建议增加`learning_rate`和`packing_size`。我们仍在利用此模型探索适用于 LoRA 的光学超参数/最佳实践，敬请关注后续更新。

我想问下 PaddleOCR-VL LoRA 微调后，怎么合并模型？erniekit export run_export.yaml lora=True 还是会报错
