# [Issue #2933] [Bug]: Autoround DDP smoke tests failing

source: https://github.com/vllm-project/llm-compressor/issues/2933
state: closed | updated: 2026-07-16T16:50:26Z
labels: bug, autoround

## 正文

### ⚙️ Your current environment

llm-compressor main

### 🐛 Describe the bug

#2844 added some changes to AutoRound that breaks our nightly DDP smoke testing.

<details>
<summary>Error Logs</summary>

```
2026-07-16T03:19:43.5355434Z [torchrun1]:FAILED tests/llmcompressor/transformers/compression/test_compression_ddp.py::test_ddp_smoke_autoround - torch._dynamo.exc.TorchRuntimeError: Tensor device mismatch
2026-07-16T03:19:43.5356848Z [torchrun1]:  Explanation: Expected all tensors to be on the same device, but found at least two devices, cuda:1 and cuda:0!
2026-07-16T03:19:43.5357732Z [torchrun1]:  Hint: Move inputs, parameters, and buffers to the same device.
2026-07-16T03:19:43.5358231Z [torchrun1]:
2026-07-16T03:19:43.5358671Z [torchrun1]:  Developer debug context: call_function <built-in function mul>
2026-07-16T03:19:43.5359325Z [torchrun1]:
2026-07-16T03:19:43.5360027Z [torchrun1]: For more details about this graph break, please visit: https://meta-pytorch.github.io/compile-graph-break-site/gb/gb5173.html
2026-07-16T03:19:43.5360807Z [torchrun1]:
2026-07-16T03:19:43.5361089Z [torchrun1]:from user code:
2026-07-16T03:19:43.5362109Z [torchrun1]:   File "/home/runner/_work/llm-compressor-testing/llm-compressor-testing/TEST_VENV/lib/python3.12/site-packages/transformers/models/qwen3_moe/modeling_qwen3_moe.py", line 335, in forward
2026-07-16T03:19:43.5363360Z [torchrun1]:    hidden_states = self.input_layernorm(hidden_states)
2026-07-16T03:19:43.5363881Z [torchrun1]:                    ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
2026-07-16T03:19:43.5364982Z [torchrun1]:  File "/home/runner/_work/llm-compressor-testing/llm-compressor-testing/TEST_VENV/lib/python3.12/site-packages/torch/nn/modules/module.py", line 1778, in _wrapped_call_impl
2026-07-16T03:19:43.5366093Z [torchrun1]:    return self._call_impl(*args, **kwargs)
2026-07-16T03:19:43.5366550Z [torchrun1]:           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
2026-07-16T03:19:43.5367544Z [torchrun1]:  File "/home/runner/_work/llm-compressor-testing/llm-compressor-testing/TEST_VENV/lib/python3.12/site-packages/torch/nn/modules/module.py", line 1789, in _call_impl
2026-07-16T03:19:43.5368564Z [torchrun1]:    return forward_call(*args, **kwargs)
2026-07-16T03:19:43.5369154Z [torchrun1]:           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
2026-07-16T03:19:43.5370195Z [torchrun1]:  File "/home/runner/_work/llm-compressor-testing/llm-compressor-testing/TEST_VENV/lib/python3.12/site-packages/transformers/models/qwen3_moe/modeling_qwen3_moe.py", line 304, in forward
2026-07-16T03:19:43.5371436Z [torchrun1]:    return self.weight * hidden_states.to(input_dtype)
2026-07-16T03:19:43.5371975Z [torchrun1]:           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
2026-07-16T03:19:43.5372393Z [torchrun1]:

...

2026-07-16T03:19:39.8142940Z [torchrun1]:gb_type = 'Tensor device mismatch'
2026-07-16T03:19:39.8143234Z [torchrun1]:context = 'call_function <built-in function mul>'
2026-07-16T03:19:39.8143709Z [torchrun1]:explanation = 'Expected all tensors to be on the same device, but found at least two devices, cuda:1 and cuda:0!'
2026-07-16T03:19:39.8154230Z [torchrun1]:hints = ['Move inputs, parameters, and buffers to the same device.']
2026-07-16T03:19:39.8154869Z [torchrun1]:from_exc = FakeTensorDeviceMismatchError('Expected all tensors to be on the same device, but found at least two devices, cuda:1 and cuda:0!')
```

</details>


### 🛠️ Steps to reproduce

Run (with 2 GPUs)
```
pytest  tests/llmcompressor/transformers/compression/test_compression_ddp.py -k test_ddp_smoke_autoround
```

## 评论 (3)

### brian-dellabetta · 2026-07-16

@yiliu30 can you take a look?

### yiliu30 · 2026-07-16

Hi @brian-dellabetta, thanks for reporting this, I’ve prepared a fix here https://github.com/vllm-project/llm-compressor/pull/2934.



### brian-dellabetta · 2026-07-16

Thanks @yiliu30 !
