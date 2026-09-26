# [Issue #147] 【bug】torch_npu不支持flex_attention，使用flex_attention进行训练会报错

source: https://github.com/Ascend/pytorch/issues/147
state: open | updated: 2026-08-12T08:07:42Z
labels: 

## 正文

torch_npu不支持flex_attention

**torch/nn/attention/flex_attention.py**

def _validate_device(query: Tensor, key: Tensor, value: Tensor) :

    if query.device.type == "cpu" and (
        query.requires_grad or key.requires_grad or value.requires_grad
    ):
        raise NotImplementedError(
            "FlexAttention does not support backward on CPU. Please set the input requires_grad to False or use another device."
        )
    if query.device.type == "mps" and (
        query.requires_grad or key.requires_grad or value.requires_grad
    ):
        raise NotImplementedError(
            "FlexAttention does not support backward on MPS. Please set the input requires_grad to False or use another device."
        )
    supported_devices = {"cuda", "cpu", "xpu", "hpu", "mps"}
    if query.device.type not in supported_devices:
        raise ValueError(
            "FlexAttention is only supported on CUDA, CPU, HPU, or MPS devices. "
            f"Found input tensors on {query.device.type} device."
        ) 


使用vllm-speculators训练等使用flex_attention场景会报如下错误，如果绕过会对性能产生较大影响建议适配：
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

## 评论 (2)

### hazelduan · 2026-06-28

遇到一样的问题，需要支持flex attention

### petrichorz · 2026-08-12

一样的问题，多模态模型常使用Flex Attn，目前cann9的sparse block attention无法完全满足功能替换，希望能支持
