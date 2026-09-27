# [Issue #74] Can the quantization process be on CPU?

source: https://github.com/dropbox/hqq/issues/74
state: closed | updated: 2024-05-13T10:12:32Z
labels: 

## 正文

I noticed that in the HQQLinear and quantize func, the default device is cuda. And in the initialize function, the bias is put on GPU.
```
self.bias = (
                None
                if (self.linear_layer.bias is None)
                else self.linear_layer.bias.to(self.compute_dtype).cuda(self.device)
            )
```
I am wondering if the quantization process can be on CPU?

## 评论 (4)

### mobicham · 2024-05-13

The main goals are saving vram on GPUs + use fused CUDA/Triton kernels for faster inference, that's why we focus on GPUs. 
I can adapt the code to support CPU by changing `cuda()` to `to(device=...)` and enable fp32 during the quantization step, but that's gonna be very slow and goes against the main goals of the library. Any particular motivation to use the CPU? RAM is not a big issue since in the worst case can you can just increase the swap.



### mxjmtxrm · 2024-05-13

Thanks for your reply.
I tried to load model with HQQ and Deepspeed Zero3 using transformers. I met the following error:
```
File "/workspace/model.py", line 66, in create_model_and_tokenizer
    model = AutoModelForCausalLM.from_pretrained(
  File "/usr/local/lib/python3.10/dist-packages/transformers/models/auto/auto_factory.py", line 563, in from_pretrained
    return model_class.from_pretrained(
  File "/usr/local/lib/python3.10/dist-packages/transformers/modeling_utils.py", line 3692, in from_pretrained
    ) = cls._load_pretrained_model(
  File "/usr/local/lib/python3.10/dist-packages/transformers/modeling_utils.py", line 4126, in _load_pretrained_model
    new_error_msgs, offload_index, state_dict_index = _load_state_dict_into_meta_model(
  File "/usr/local/lib/python3.10/dist-packages/transformers/modeling_utils.py", line 889, in _load_state_dict_into_meta_model
    hf_quantizer.create_quantized_param(model, param, param_name, param_device, state_dict, unexpected_keys)
  File "/usr/local/lib/python3.10/dist-packages/transformers/quantizers/quantizer_hqq.py", line 141, in create_quantized_param
    hqq_layer = HQQLinear(
  File "/usr/local/lib/python3.10/dist-packages/hqq/core/quantize.py", line 391, in __init__
    self.initialize()
  File "/usr/local/lib/python3.10/dist-packages/hqq/core/quantize.py", line 399, in initialize
    else self.linear_layer.bias.to(self.compute_dtype).cuda(self.device)
RuntimeError: Invalid device, must be cuda device
```
The error is cased by self.device='cpu'. I found that the model will be loaded on CPU firstly. 
If there is any way to quantize models on GPU with Zero3?

### mobicham · 2024-05-13

Let me fix that part and test it on cpu

### mobicham · 2024-05-13

This should do it: https://github.com/mobiusml/hqq/commit/b21fe876dd71cad788471f3012efb70cf099072c 
I just tested it and I was able to quantize and do inference on CPU. 
Just make sure you use `compute_dtype=torch.float32` and use the `HQQLinear.set_backend(HQQBackend.PYTORCH)` because the default backend is for `CUDA`. 
In fact, I will switch by default to `PYTORCH` to avoid this kind of issues: https://github.com/mobiusml/hqq/commit/9f32c5a39d53f478f9ce4d0f56c57515997fc462
Also, moved cuda streams outside __init__ so it wouldn't complain when there's no gpu available: https://github.com/mobiusml/hqq/commit/d3108426f7d4285f73140a6a48f966e3ed881b32
This is also required when there's no gpu available: https://github.com/mobiusml/hqq/commit/cc2b9443e9f1797449616bdafdab07b1ed5f16ad
