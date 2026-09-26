# [Issue #75] How to use the finetuned mistal model for inference with Medusa

source: https://github.com/FasterDecoding/Medusa/issues/75
state: open | updated: 2024-05-11T17:37:57Z
labels: 

## 正文

How to use the finetuned mistal model for inference with Medusa

## 评论 (7)

### ctlllll · 2024-01-25

As an example, you can refer to the Zephyr model (`python -m medusa.inference.cli --model FasterDecoding/medusa-1.0-zephyr-7b-beta`) :)

### pradeepdev-1995 · 2024-01-25

@ctlllll 
It seems that , this command expectes a medusa model
```
python -m medusa.inference.cli --model [path of medusa model]
```
But in my case , i am using the mistral model-https://huggingface.co/mistralai/Mistral-7B-Instruct-v0.2 (not based on medusa). so shall i use medusa library to improve my mistral models inference time?

### eldhosemjoy · 2024-02-02

You will need to train the hugging face model on the medusa heads before you can use it for inference. 

### pradeepdev-1995 · 2024-02-02

@eldhosemjoy How to train the hugging face model on the Medusa heads?can you share the reference

### eldhosemjoy · 2024-02-02

You can use this script - https://github.com/FasterDecoding/Medusa/blob/main/medusa/train/train_legacy.py
This is a Llama example I suppose. you can try with Mistral.

### MoOo2mini · 2024-02-05

Is there no way to inference without training? I didn't have the computing resources to train, so I wanted to infer without training.


### nguptaHQ · 2024-05-11

Try this model which is ported to medusa.
https://huggingface.co/text-generation-inference/Mistral-7B-Instruct-v0.2-medusa/tree/main

