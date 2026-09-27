# [Issue #71] Add multi-gpu support for `from_quantized` call

source: https://github.com/dropbox/hqq/issues/71
state: closed | updated: 2024-08-28T10:09:10Z
labels: enhancement

## 正文

HQQ multi-gpu support is so far only supported for the `quantize_model` model call. 

## 评论 (1)

### mobicham · 2024-08-28

Closing this since this is gonna be supported directly in transformers: https://github.com/huggingface/transformers/pull/33141
