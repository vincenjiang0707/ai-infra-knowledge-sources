# [Issue #1998] How to quantize both vision encoder and llm together?

source: https://github.com/ModelCloud/GPTQModel/issues/1998
state: open | updated: 2026-04-25T10:46:30Z
labels: 

## 正文

I am trying to quantize dots_ocr model, whose submodules are ['model','vision_tower','lm_head'], as shown below:

<img width="398" height="82" alt="Image" src="https://github.com/user-attachments/assets/2e416a7b-bead-4a2b-bd02-4289d0d7c5d8" />

By tracing the code down, I found that this [code](https://github.com/ModelCloud/GPTQModel/blob/main/gptqmodel/looper/module_looper.py#L772) is for parsing modules for quantization, but it only return one module. By experiment, I can quantize either `vision_tower` or `model` separately and loading by vllm， but I can't quantize both due to above mechanism. Please help me figure out how to solve this, thanks^_^


## 评论 (8)

### LiMa-cas · 2025-10-15

I have quantized thinker or talker seperately，but I can not put them together，same questions

### XULU42 · 2025-10-15

I was able to quantize dots_ocr by changing [code](https://github.com/ModelCloud/GPTQModel/blob/main/gptqmodel/looper/module_looper.py#L901) here and below to a for loop. It works, but looks ugly, looking forward to official mechanism to support both model quantization.

### Qubitium · 2025-10-15

> I was able to quantize dots_ocr by changing [code](https://github.com/ModelCloud/GPTQModel/blob/main/gptqmodel/looper/module_looper.py#L901) here and below to a for loop. It works, but looks ugly, looking forward to official mechanism to support both model quantization.

@XULU42  Can you post your code diff? I would be awesome if you can create a PR to add this support. Don't worry about breaking things,once you create a PR and an associated unit test to `tests/models` (just copy another model's unit teset and modify) I can help with the PR testing and review. 

I am already overworked so don't have the time to implement everything that everyone wants without external help. 

### XULU42 · 2025-10-15

I would issue an PR later, but it seems to be a root change in module loop mechanism, may cause problem for other supported models. Thanks for your dedication to community. Your health is precious, please take care.

### Qubitium · 2025-10-15

> but it seems to be a root change in module loop mechanism, may cause problem for other supported models. 

Don't worry about breakage.  Module looper needs needs to eventually handle parallel models so I expect structual changes for world models where text, vision, audio module exists concurrently in the `modules` tree. Right now, the `module` tree auto extraction is expecting a linear single branch from top to bottom but current VL models are now structured where essentially there are two+ parallel branches in the module tree. 



### XULU42 · 2025-10-15

> > but it seems to be a root change in module loop mechanism, may cause problem for other supported models.
> 
> Don't worry about breakage. Module looper needs needs to eventually handle parallel models so I expect structual changes for world models where text, vision, audio module exists concurrently in the `modules` tree. Right now, the `module` tree auto extraction is expecting a linear single branch from top to bottom but current VL models are now structured where essentially there are two+ parallel branches in the module tree.

The situation is clear. Let's try to add mechanism to parse and quantize parallel branches.

### LWQuestc · 2026-03-06

> I was able to quantize dots_ocr by changing [code](https://github.com/ModelCloud/GPTQModel/blob/main/gptqmodel/looper/module_looper.py#L901) here and below to a for loop. It works, but looks ugly, looking forward to official mechanism to support both model quantization.
@XULU42 I've been working on something similar lately. If you don't mind, could I take a look at your code for reference? Thanks!


### namgyu-youn · 2026-03-15

Quantizing the vision encoder is uncommon because: (1) calibration requires multimodal (image-text) samples, whereas most pipelines are built around text-only inputs, (2) vision encoders represent a small fraction of total parameters (e.g., ~1.5% / 0.42B out of 27.44B in [Gemma3-27B](https://huggingface.co/google/gemma-3-27b-it/blob/main/config.json)).
