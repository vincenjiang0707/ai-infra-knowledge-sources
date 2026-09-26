# [Issue #270] Qwen2SdpaAttention中past_key_value = None，KV Cache 没有被正确更新和返回吗

source: https://github.com/SafeAILab/EAGLE/issues/270
state: open | updated: 2025-08-04T06:57:15Z
labels: 

## 正文

<img width="1131" height="825" alt="Image" src="https://github.com/user-attachments/assets/3b10a393-c0de-4c9d-8b7d-b25df426812c" />

## 评论 (1)

### exyexin · 2025-08-04

你可以去看下kvcache.py，kvcache的实现修改过了，在past_key.cat的时候直接在内存里增量复制
