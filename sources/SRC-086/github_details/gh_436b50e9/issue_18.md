# [Issue #18] finetune vicuna-7b-1.5-16k

source: https://github.com/FasterDecoding/Medusa/issues/18
state: closed | updated: 2023-10-11T12:04:08Z
labels: 

## 正文

Tried to finetune vicuna-7b-1.5-16k, 16k lengths seems always throws OOM error. I have a 48GB RTXA6000, even batchsize=1 can't run.
went back to the regular 4k length vicuna-7b-1.5, I found when batchsize=2, it will already take up almost 40GB VRAM per GPU. 

Anyone have any ideas how to reduce the VRAM usage? How to finetune a 16k model? Open for any suggestions. 

## 评论 (6)

### leeyeehoo · 2023-09-15

Just wondering what dataset you use for fine-tuning? If you use the same dataset as we used it should be ok since they are all 7b models... 

### JianbangZ · 2023-09-15

> Just wondering what dataset you use for fine-tuning? If you use the same dataset as we used it should be ok since they are all 7b models...

ShareGPT. Have you tried to train https://huggingface.co/lmsys/vicuna-7b-v1.5-16k. I think the max_length=16384 is causing  huge VRAM requirement 

### ctlllll · 2023-09-15

Hi Jim,

You may want to try a quantized model (use `load_in_4bit` or `load_in_8bit`), this can save a little memory and works just like qLoRA. Also, gradient checkpointing can save some memory. But I feel it's generally very hard to train on such a long context with a single GPU, and you may want to decrease the `max_length` while training the heads. I guess this also works even if you switch the `max_length` back to 16384 for inference.

### JianbangZ · 2023-09-16

the orginal model is 16k length, can I set a smaller max_length with medusa training? 

### leeyeehoo · 2023-09-16

It can work. Medusa heads don't change the behavior of the original models. However, since we didn't try such a long-sequence model, we have no idea if medusa heads will have degradation when sequence length exceeds the max_length you set in training. Feel free to share the results and checkpoint if you want and we can conduct further investigation!

### JianbangZ · 2023-09-16

OK. I will share results once model is finetuned and tested. 
