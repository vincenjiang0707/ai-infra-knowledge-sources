# [Issue #84] Is HQQLinearLoRAWithFakeQuant differentiable?

source: https://github.com/dropbox/hqq/issues/84
state: closed | updated: 2024-06-15T17:52:47Z
labels: 

## 正文

Is HQQLinearLoRAWithFakeQuant differentiable? Since torch.round is not differentiable and is called by HQQLinearLoRAWithFakeQuant, do we need to use round_ste instead of torch.round?

## 评论 (1)

### mobicham · 2024-06-15

Yeah, that was just an experimental placeholder that I forgot to remove actually, should not be used. 
I practice, I noticed that ste is not working well with 4-bit/3-bit for some reason. Better to just freeze the quantized weights and train LoRA weights instead to not deal with those gradient issues and large vram requirements (HQQ+).
