# [Issue #155] no run

source: https://github.com/dropbox/hqq/issues/155
state: closed | updated: 2025-04-09T11:04:32Z
labels: 

## 正文

https://huggingface.co/mobiuslabsgmbh/Llama-2-70b-hf-2bit_g16_s128-HQQ/discussions/1

## 评论 (1)

### mobicham · 2025-04-09

This is a very old model which is not compatible with >=v0.2. You can either install an old version of hqq, or you can quantize the model on-the-fly in transformers. 
https://github.com/mobiusml/hqq/?tab=readme-ov-file#transformers-

The documentation already says that you need `v0.1.8` to run the model

```
#This model is deprecated and requires older versions
pip install hqq==0.1.8
pip install transformers==4.46.0
```

Hope this helps!
