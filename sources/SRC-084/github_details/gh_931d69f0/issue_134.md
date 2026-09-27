# [Issue #134] Saving quantized Aria weights

source: https://github.com/dropbox/hqq/issues/134
state: closed | updated: 2025-04-09T11:00:06Z
labels: 

## 正文

First of all, great work with the Aria HQQ quant!
Is it somehow possible to save the quantized weights? Neither `model.save_pretrained(save_dir)` nor `AutoHQQHFModel.save_quantized(model, save_dir)` seem to work with HQQ Aria for now, as the seem to only save a 2GB part of the model. Would be ideal to just pull the quant from the hub instead of the full model.
Thanks in advance,
Leon

## 评论 (3)

### mobicham · 2024-11-21

Hi @leon-seidel 
I don't think it's possible to do it with the current code. I can make a hacky version but I am waiting for the official PR to get merged, then I think we should be able to save/load directly via transformers: 
https://github.com/huggingface/transformers/pull/34157 

### leon-seidel · 2024-11-21

Alright, thank you!

### mobicham · 2025-04-09

Closing this issue since Aria is officially supported in transformers now.
