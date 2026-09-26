# [Issue #110] Errors occurred during the environment and training

source: https://github.com/FasterDecoding/Medusa/issues/110
state: closed | updated: 2024-06-26T02:47:16Z
labels: 

## 正文

An error was encountered during installation

error: subprocess-exited-with-error

An error was encountered during the training run

NameError: name 'is_flash_attn_available' is not defined. Did you mean: 'is_flash_attn_2_available'?

## 评论 (2)

### blacker521 · 2024-06-26

1.subprocess-exited-with-error
Run before installing the environment
`pip install setuptools-scm
`

### blacker521 · 2024-06-26

NameError: name 'is_flash_attn_available' is not defined. Did you mean: 'is_flash_attn_2_available'?
change ` /medusa/model/modeling_llama_kv.py`
`is_flash_attn_available `to `is_flash_attn_2_available`
