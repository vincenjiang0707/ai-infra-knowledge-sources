# [Issue #118] Hqq vs gguf

source: https://github.com/dropbox/hqq/issues/118
state: closed | updated: 2024-11-01T18:46:15Z
labels: 

## 正文

Is there an easy way to convert gguf to hqq and vice-versa? Any comparisons?
https://github.com/leafspark/AutoGGUF

## 评论 (3)

### mobicham · 2024-09-14

Hi! What of quantization is GGUF using? If it's asymmetric quantization (with both scales/zeros) it could be converted

### blap · 2024-09-14

> Hi! What of quantization is GGUF using? If it's asymmetric quantization (with both scales/zeros) it could be converted

Sorry. I don't know the specs, but here you can see details about it and how to convert hf to gguf from llama.cpp: https://github.com/ggerganov/llama.cpp/tree/master/gguf-py

### mobicham · 2024-09-14

Thanks for sharing,  looks like the logic is quite different, so I don't think both quantized outputs are compatible unfortunately.
