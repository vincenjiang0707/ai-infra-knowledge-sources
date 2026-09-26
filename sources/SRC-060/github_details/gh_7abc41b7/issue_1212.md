# [Issue #1212] 部署ERNIE-4.5-VL-28B-A3B-PT模型，报错AttributeError: 'NoneType' object has no attribute 'shape'

source: https://github.com/PaddlePaddle/ERNIE/issues/1212
state: closed | updated: 2025-12-16T12:01:33Z
labels: 

## 正文

Traceback (most recent call last):
  File "/root/autodl-tmp/infer.py", line 41, in <module>
    generated_ids = model.generate(
                    ^^^^^^^^^^^^^^^
  File "/root/miniconda3/lib/python3.12/site-packages/torch/utils/_contextlib.py", line 116, in decorate_context
    return func(*args, **kwargs)
           ^^^^^^^^^^^^^^^^^^^^^
  File "/root/miniconda3/lib/python3.12/site-packages/transformers/generation/utils.py", line 2539, in generate
    result = self._sample(
             ^^^^^^^^^^^^^
  File "/root/miniconda3/lib/python3.12/site-packages/transformers/generation/utils.py", line 2867, in _sample
    outputs = self(**model_inputs, return_dict=True)
              ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/root/miniconda3/lib/python3.12/site-packages/torch/nn/modules/module.py", line 1736, in _wrapped_call_impl
    return self._call_impl(*args, **kwargs)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/root/miniconda3/lib/python3.12/site-packages/torch/nn/modules/module.py", line 1747, in _call_impl
    return forward_call(*args, **kwargs)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/root/.cache/huggingface/modules/transformers_modules/ERNIE-4.5-VL-28B-A3B-PT/modeling_ernie4_5_vl.py", line 4169, in forward
    outputs = self.model(
              ^^^^^^^^^^^
  File "/root/miniconda3/lib/python3.12/site-packages/torch/nn/modules/module.py", line 1736, in _wrapped_call_impl
    return self._call_impl(*args, **kwargs)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/root/miniconda3/lib/python3.12/site-packages/torch/nn/modules/module.py", line 1747, in _call_impl
    return forward_call(*args, **kwargs)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/root/.cache/huggingface/modules/transformers_modules/ERNIE-4.5-VL-28B-A3B-PT/modeling_ernie4_5_vl.py", line 2888, in forward
    cache_length = past_key_values[0][0].shape[1]
                   ^^^^^^^^^^^^^^^^^^^^^^^^^^^
AttributeError: 'NoneType' object has no attribute 'shape'

## 评论 (6)

### Jiang-Jia-Jun · 2025-09-03

@yvway Hi，你的FastDeploy版本是多少呢

### yvway · 2025-09-03

你好，我是用transformers部署，fastdeploy部署有版本要求吗？transformers不行的话，我想试试fastdeploy

### BossPi · 2025-09-03

您好，这个问题是由于transformers版本更新导致的，将transformers降级到4.53.0版本或者在预测时传入`use_cache=False`即可：
```
generated_ids = model.generate(
    inputs=inputs['input_ids'].to(device),
    **inputs,
    max_new_tokens=128,
    use_cache=False
    )
```

### yvway · 2025-09-03

好的，谢谢

### BossPi · 2025-09-03

不客气，如果还有其他问题，欢迎继续提问，我们会尽快为您解答

### nepeplwu · 2025-12-16

The issue has no response for a long time and will be closed. You can reopen or new another issue if are still confused.

---
_From Bot_
