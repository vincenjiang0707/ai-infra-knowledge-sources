# [Issue #253] [BUG] TypeError: Descriptors cannot be created directly.

source: https://github.com/mit-han-lab/llm-awq/issues/253
state: closed | updated: 2025-01-08T14:34:27Z
labels: 

## 正文

I get below error if i run awq search on llama2-7b-hf model.

```
TypeError: Descriptors cannot be created directly.
If this call came from a _pb2.py file, your generated code is out of date and must be regenerated with protoc >= 3.19.0.
If you cannot immediately regenerate your protos, some other possible workarounds are:
 1. Downgrade the protobuf package to 3.20.x or lower.
 2. Set PROTOCOL_BUFFERS_PYTHON_IMPLEMENTATION=python (but this will use pure-Python parsing and will be much slower).
```
is there any fix or a way to debug this issue?

`python -m awq.entry --model_path llama2-7b-chat-hf/ --w_bit 4 --q_group_size 128 --run_awq --dump_awq anawq_cache/llama2-7b-w4-g128.pt`


## 评论 (0)
