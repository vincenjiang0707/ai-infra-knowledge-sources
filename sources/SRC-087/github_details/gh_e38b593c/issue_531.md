# [Issue #531] [Bug][NPU]: Running simple example on NPU seems to be broken

source: https://github.com/vllm-project/speculators/issues/531
state: open | updated: 2026-09-16T19:58:13Z
labels: bug, stale

## 正文

### Your current environment

Please provide the following information about your environment if applicable:
I use vllm-ascend latest nightly docker image.
- vLLM:0.20.2 and vllm-ascend:0.19.1rc2.dev101+ga45cdf9b9
- Speculators:latest
- CUDA:None
- PyTorch:torch==2.10.0+cpu and torch_npu==2.10.0
- Transformers==5.5.3
- Hardware:Ascend A3 and aarch64 CPU
- Model:Qwen3-8B


### 🐛 Describe the bug

Run example script and found vllm server ready, but step 3: training is broken.
```
bash examples/train/eagle3_qwen3_8b_sharegpt_online_5k.sh
```

```
[rank0]: Traceback (most recent call last):
[rank0]:   File "/workspace/speculators/scripts/train.py", line 681, in <module>
[rank0]:     main(args)
[rank0]:   File "/workspace/speculators/scripts/train.py", line 380, in main
[rank0]:     trainer.run_training()
[rank0]:   File "/workspace/speculators/src/speculators/train/graceful_shutdown.py", line 118, in wrapper
[rank0]:     return fn(self, *args, **kwargs)
[rank0]:            ^^^^^^^^^^^^^^^^^^^^^^^^^
[rank0]:   File "/workspace/speculators/src/speculators/train/trainer.py", line 340, in run_training
[rank0]:     self.train_epoch(epoch)
[rank0]:   File "/workspace/speculators/src/speculators/train/trainer.py", line 209, in train_epoch
[rank0]:     _draft_tokens, loss, metrics = self.model(
[rank0]:                                    ^^^^^^^^^^^
[rank0]:   File "/usr/local/python3.11.15/lib/python3.11/site-packages/torch/nn/modules/module.py", line 1776, in _wrapped_call_impl
[rank0]:     return self._call_impl(*args, **kwargs)
[rank0]:            ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
[rank0]:   File "/usr/local/python3.11.15/lib/python3.11/site-packages/torch/nn/modules/module.py", line 1882, in _call_impl
[rank0]:     return inner()
[rank0]:            ^^^^^^^
[rank0]:   File "/usr/local/python3.11.15/lib/python3.11/site-packages/torch/nn/modules/module.py", line 1830, in inner
[rank0]:     result = forward_call(*args, **kwargs)
[rank0]:              ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
[rank0]:   File "/workspace/speculators/src/speculators/models/eagle3/core.py", line 204, in forward
[rank0]:     hidden_states = decoder_layer(
[rank0]:                     ^^^^^^^^^^^^^^
[rank0]:   File "/usr/local/python3.11.15/lib/python3.11/site-packages/transformers/modeling_layers.py", line 93, in __call__
[rank0]:     return super().__call__(*args, **kwargs)
[rank0]:            ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
[rank0]:   File "/usr/local/python3.11.15/lib/python3.11/site-packages/torch/nn/modules/module.py", line 1776, in _wrapped_call_impl
[rank0]:     return self._call_impl(*args, **kwargs)
[rank0]:            ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
[rank0]:   File "/usr/local/python3.11.15/lib/python3.11/site-packages/torch/nn/modules/module.py", line 1882, in _call_impl
[rank0]:     return inner()
[rank0]:            ^^^^^^^
[rank0]:   File "/usr/local/python3.11.15/lib/python3.11/site-packages/torch/nn/modules/module.py", line 1830, in inner
[rank0]:     result = forward_call(*args, **kwargs)
[rank0]:              ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
[rank0]:   File "/workspace/speculators/src/speculators/models/eagle3/model_definitions.py", line 93, in forward
[rank0]:     hidden_states, _ = self.self_attn(
[rank0]:                        ^^^^^^^^^^^^^^^
[rank0]:   File "/usr/local/python3.11.15/lib/python3.11/site-packages/torch/nn/modules/module.py", line 1776, in _wrapped_call_impl
[rank0]:     return self._call_impl(*args, **kwargs)
[rank0]:            ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
[rank0]:   File "/usr/local/python3.11.15/lib/python3.11/site-packages/torch/nn/modules/module.py", line 1787, in _call_impl
[rank0]:     return forward_call(*args, **kwargs)
[rank0]:            ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
[rank0]:   File "/usr/local/python3.11.15/lib/python3.11/site-packages/transformers/models/llama/modeling_llama.py", line 276, in forward
[rank0]:     attn_output, attn_weights = attention_interface(
[rank0]:                                 ^^^^^^^^^^^^^^^^^^^^
[rank0]:   File "/workspace/speculators/src/speculators/models/attention.py", line 49, in flex_attention_forward
[rank0]:     flex_attention_output = flex_attention(
[rank0]:                             ^^^^^^^^^^^^^^^
[rank0]:   File "/usr/local/python3.11.15/lib/python3.11/site-packages/torch/nn/attention/flex_attention.py", line 1475, in flex_attention
[rank0]:     _validate_device(query, key, value)
[rank0]:   File "/usr/local/python3.11.15/lib/python3.11/site-packages/torch/nn/attention/flex_attention.py", line 1331, in _validate_device
[rank0]:     raise ValueError(
[rank0]: ValueError: FlexAttention is only supported on CUDA, CPU or HPU devices. Found input tensors on npu device.
```

## 评论 (0)
