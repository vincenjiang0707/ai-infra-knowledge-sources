# [Issue #157] error when compiling with custom cuda graphs

source: https://github.com/dropbox/hqq/issues/157
state: closed | updated: 2025-04-14T14:54:08Z
labels: 

## 正文

Hello :)
I tried your latest hqq_lib_demo on a llama-1B, but get the following error:

ArgsMismatchError: too many positional arguments.
  func = 'forward' /home/ubuntu/miniconda3/envs/tree/lib/python3.10/site-packages/hqq/core/quantize.py:311, args = [<class 'torch.autograd.function.Function'>, <class 'torch.Tensor'>, <class 'method'>, <class 'NoneType'>], kwargs = {}

from user code:
   File "/home/ubuntu/miniconda3/envs/tree/lib/python3.10/site-packages/hqq/utils/generation_hf.py", line 286, in decode_one_token_sampled
    out = self.model(
  File "/home/ubuntu/miniconda3/envs/tree/lib/python3.10/site-packages/torch/nn/modules/module.py", line 1747, in _call_impl
    return forward_call(*args, **kwargs)
  File "/home/ubuntu/miniconda3/envs/tree/lib/python3.10/site-packages/transformers/utils/generic.py", line 965, in wrapper
    output = func(self, *args, **kwargs)
  File "/home/ubuntu/miniconda3/envs/tree/lib/python3.10/site-packages/transformers/utils/deprecation.py", line 172, in wrapped_func
    return func(*args, **kwargs)
  File "/home/ubuntu/miniconda3/envs/tree/lib/python3.10/site-packages/transformers/models/llama/modeling_llama.py", line 821, in forward
    outputs: BaseModelOutputWithPast = self.model(
  File "/home/ubuntu/miniconda3/envs/tree/lib/python3.10/site-packages/torch/nn/modules/module.py", line 1747, in _call_impl
    return forward_call(*args, **kwargs)
  File "/home/ubuntu/miniconda3/envs/tree/lib/python3.10/site-packages/transformers/utils/generic.py", line 965, in wrapper
    output = func(self, *args, **kwargs)
  File "/home/ubuntu/miniconda3/envs/tree/lib/python3.10/site-packages/transformers/models/llama/modeling_llama.py", line 571, in forward
    layer_outputs = decoder_layer(
  File "/home/ubuntu/miniconda3/envs/tree/lib/python3.10/site-packages/torch/nn/modules/module.py", line 1747, in _call_impl
    return forward_call(*args, **kwargs)
  File "/home/ubuntu/miniconda3/envs/tree/lib/python3.10/site-packages/transformers/models/llama/modeling_llama.py", line 318, in forward
    hidden_states, self_attn_weights = self.self_attn(
  File "/home/ubuntu/miniconda3/envs/tree/lib/python3.10/site-packages/torch/nn/modules/module.py", line 1747, in _call_impl
    return forward_call(*args, **kwargs)
  File "/home/ubuntu/miniconda3/envs/tree/lib/python3.10/site-packages/transformers/models/llama/modeling_llama.py", line 252, in forward
    query_states = self.q_proj(hidden_states).view(hidden_shape).transpose(1, 2)
  File "/home/ubuntu/miniconda3/envs/tree/lib/python3.10/site-packages/torch/nn/modules/module.py", line 1747, in _call_impl
    return forward_call(*args, **kwargs)
  File "/home/ubuntu/miniconda3/envs/tree/lib/python3.10/site-packages/hqq/core/quantize.py", line 872, in forward_pytorch_backprop
    return HQQMatmulNoCacheMul.apply(x, self.matmul, self.bias)

Set TORCH_LOGS="+dynamo" and TORCHDYNAMO_VERBOSE=1 for more information

I investigated a little, and found that torch.autograd.Function.apply() must only be passed Tensor-like arguments, while self.matmul is not.
I have hqq.__version__: 0.2.5
transformers.__version__: 4.51.1
torch.__version__: 2.5.1+cu124
But I guess I am missing something since it is working on your side.
Do you have any idea what I have done wrong?
Thx

## 评论 (3)

### mobicham · 2025-04-14

Hi, can you please share your code snippet? 

### llcnt · 2025-04-14

Thank you for your fast reply!
I found 2 differences in my code that explain the bug:
- I was using AutoModel from hf with a HQQConfig for quantizing the model, but it seems that `prepare_for_inference` does not change the HqqMatmul to 'torchaoint4Matmul';
- I was loading the mode in torch.float16 instead of bfloat16.

Changing these 2, make it work!

### mobicham · 2025-04-14

Yeah the torchao backend requires bfloat16! Glad to hear the problem was resolved!
