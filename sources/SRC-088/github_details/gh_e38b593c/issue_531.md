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

## 评论 (12)

### menogrey · 2026-05-19

@momo609  plz take a look. Also cc @wjunLu

### sunny-infra · 2026-05-25

@menogrey Thank you for your interest in Ascend. Since Ascend does not yet support FlexAttention, the simplest approach is to skip the validation, as shown below.
<img width="884" height="266" alt="Image" src="https://github.com/user-attachments/assets/1c11a442-d3f1-4dcc-9571-1f532ce065d4" />
Additionally, the vllm-ascend image you are using only supports speculators 0.4.0; the new version has not been released yet. If you want to use speculators 0.5.0, you need to replace vllm-ascend in the image with the main repository version and upgrade the CANN version to CANN 0.9.0.

### sunny-infra · 2026-05-25

However, there is a drawback: after bypassing FlexAttention, the maximum training length per NPU can only be set to 4k. Hi @fynnsu ,@shanjiaz and @dsikka , could you assign this issue to me? I will try to solve it.

### shanjiaz · 2026-05-25

> However, there is a drawback: after bypassing FlexAttention, the maximum training length per NPU can only be set to 4k. Hi [@fynnsu](https://github.com/fynnsu) ,[@shanjiaz](https://github.com/shanjiaz) and [@dsikka](https://github.com/dsikka) , could you assign this issue to me? I will try to solve it.

@sunny-infra Yes! Thanks for taking this on. We currently don't have capacity to test on npu. Would really appreciate your help. Let us know if you have any questions!

### Sawyer117 · 2026-06-09

Sorry for the timeline noise here — I was iterating on the fix in #589 with several force-pushes. 

### shanjiaz · 2026-06-11

@sunny-infra Hey, just wanted to reach out and see if you've made any progress. Let us know if there's anything we could help with.

### shanjiaz · 2026-06-17

@menogrey @Sawyer117 @sunny-infra @momo609 Hey team! I've noticed lots of contributions for npu support, are you open to start a thread in vllm-slack/wechat to talk about potential collaboration? You can find us in #speculators channel in vllm. I can provide my wechat as well if it's easier. 

### sunny-infra · 2026-06-18

@shanjiaz That’s fantastic! This is exactly what we’re currently discussing — how to deepen our collaboration on speculators and deliver more user-friendly framework support for Ascend, just like vllm-ascend. I’m active in the #speculators and #sig-spec-decode channels on Slack. It would be great if I could add you on WeChat. My WeChat ID is Suny-Nov12.

### shanjiaz · 2026-06-18

@sunny-infra Could I have your slack id, just added you on wechat as well.

### menogrey · 2026-06-18

@shanjiaz  That will be great! Since Ascend Pytorch -- torch_npu doesn't support Flex attention now (Pytorch has a device validation, if skip the validation and use a fallback implementation, NPU will still work), maybe https://github.com/vllm-project/speculators/pull/589 can help us,  it would be even better if it could be extended to Eagle3, etc.
Additionally, As far as I know, https://github.com/vllm-project/speculators/pull/581 is also new feature for our vllm-ascend, related PR is https://github.com/vllm-project/vllm-ascend/pull/10042

### Sawyer117 · 2026-06-18

@shanjiaz Happy to connect for collaboration, my wechat is austin_c11

### github-actions[bot] · 2026-09-16

This issue has been automatically marked as stale because it has not had any activity within 90 days. It will be automatically closed if no further activity occurs within 30 days. Leave a comment if you feel this issue should remain open. Thank you!
