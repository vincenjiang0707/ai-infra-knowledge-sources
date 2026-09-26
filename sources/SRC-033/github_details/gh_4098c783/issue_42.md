# [Issue #42] Error occurs when I run stable diffusion 2.1

source: https://github.com/Ascend/pytorch/issues/42
state: open | updated: 2024-07-24T07:44:07Z
labels: 

## 正文

Loading pipeline components...: 100%|██████████| 6/6 [00:01<00:00,  3.86it/s]
  0%|                                                                                                                                                                                                                                                              | 0/50 [00:00<?, ?it/s].EZ9999: Inner Error!
EZ9999  [InferShape] The k-axis of a(64) and b(9216) tensors must be the same[FUNC:InferShape][FILE:matrix_calculation_ops.cc][LINE:1402]
        TraceBack (most recent call last):
        Failed to infer output shape[FUNC:BatchMatMulInferShape][FILE:matrix_calculation_ops.cc][LINE:2455]
        Call InferShapeAndType for node:BatchMatMul(BatchMatMul) failed[FUNC:Infer][FILE:infershape_pass.cc][LINE:119]
        process pass InferShapePass on node:BatchMatMul failed, ret:4294967295[FUNC:RunPassesOnNode][FILE:base_pass.cc][LINE:530]
        build graph failed, graph id:126, ret:1343242270[FUNC:BuildModel][FILE:ge_generator.cc][LINE:1443]
        [Build][SingleOpModel]call ge interface generator.BuildSingleOpModel failed. ge result = 1343242270[FUNC:ReportCallError][FILE:log_inner.cpp][LINE:161]
        [Build][Op]Fail to build op model[FUNC:ReportInnerError][FILE:log_inner.cpp][LINE:145]
        build op model failed, result = 500002[FUNC:ReportInnerError][FILE:log_inner.cpp][LINE:145]


My Code:
```
import torch
import torch_npu
from diffusers import StableDiffusionPipeline


pipe = StableDiffusionPipeline.from_pretrained(
    "path/to/stabilityai/stable-diffusion-2-1",
    torch_dtype=torch.float16
)
pipe = pipe.to("npu")
prompt = ......
image = pipe(prompt).images[0]
```
torch torch-npu version: 1.11.0
CANN 6.3


## 评论 (5)

### yunyiyun · 2024-06-21

model_zoo( https://gitee.com/ascend/ModelZoo-PyTorch/tree/master/PyTorch/built-in/diffusion/stablediffusion-2.1 ) 已有适配完成的，可以参考使用

### HoiM · 2024-06-21

升级到CANN 7.1 torch==2.1.0 torch-npu==2.1.0.post3后，又出现以下问题：
```
Traceback (most recent call last):
  File "test_script_npu.py", line 15, in <module>
    image = pipe(prompt).images[0]
  File "/path/to/miniconda3/envs/ascend/lib/python3.8/site-packages/torch/utils/_contextlib.py", line 115, in decorate_context
    return func(*args, **kwargs)
  File "/path/to/miniconda3/envs/ascend/lib/python3.8/site-packages/diffusers/pipelines/stable_diffusion/pipeline_stable_diffusion.py", line 1006, in __call__
    noise_pred = self.unet(
  File "/path/to/miniconda3/envs/ascend/lib/python3.8/site-packages/torch/nn/modules/module.py", line 1518, in _wrapped_call_impl
    return self._call_impl(*args, **kwargs)
  File "/path/to/miniconda3/envs/ascend/lib/python3.8/site-packages/torch/nn/modules/module.py", line 1527, in _call_impl
    return forward_call(*args, **kwargs)
  File "/path/to/miniconda3/envs/ascend/lib/python3.8/site-packages/diffusers/models/unets/unet_2d_condition.py", line 1209, in forward
    sample, res_samples = downsample_block(
  File "/path/to/miniconda3/envs/ascend/lib/python3.8/site-packages/torch/nn/modules/module.py", line 1518, in _wrapped_call_impl
    return self._call_impl(*args, **kwargs)
  File "/path/to/miniconda3/envs/ascend/lib/python3.8/site-packages/torch/nn/modules/module.py", line 1527, in _call_impl
    return forward_call(*args, **kwargs)
  File "/path/to/miniconda3/envs/ascend/lib/python3.8/site-packages/diffusers/models/unets/unet_2d_blocks.py", line 1288, in forward
    hidden_states = attn(
  File "/path/to/miniconda3/envs/ascend/lib/python3.8/site-packages/torch/nn/modules/module.py", line 1518, in _wrapped_call_impl
    return self._call_impl(*args, **kwargs)
  File "/path/to/miniconda3/envs/ascend/lib/python3.8/site-packages/torch/nn/modules/module.py", line 1527, in _call_impl
    return forward_call(*args, **kwargs)
  File "/path/to/miniconda3/envs/ascend/lib/python3.8/site-packages/diffusers/models/transformers/transformer_2d.py", line 440, in forward
    hidden_states = block(
  File "/path/to/miniconda3/envs/ascend/lib/python3.8/site-packages/torch/nn/modules/module.py", line 1518, in _wrapped_call_impl
    return self._call_impl(*args, **kwargs)
  File "/path/to/miniconda3/envs/ascend/lib/python3.8/site-packages/torch/nn/modules/module.py", line 1527, in _call_impl
    return forward_call(*args, **kwargs)
  File "/path/to/miniconda3/envs/ascend/lib/python3.8/site-packages/diffusers/models/attention.py", line 516, in forward
    ff_output = self.ff(norm_hidden_states)
  File "/path/to/miniconda3/envs/ascend/lib/python3.8/site-packages/torch/nn/modules/module.py", line 1518, in _wrapped_call_impl
    return self._call_impl(*args, **kwargs)
  File "/path/to/miniconda3/envs/ascend/lib/python3.8/site-packages/torch/nn/modules/module.py", line 1527, in _call_impl
    return forward_call(*args, **kwargs)
  File "/path/to/miniconda3/envs/ascend/lib/python3.8/site-packages/diffusers/models/attention.py", line 787, in forward
    hidden_states = module(hidden_states)
  File "/path/to/miniconda3/envs/ascend/lib/python3.8/site-packages/torch/nn/modules/module.py", line 1518, in _wrapped_call_impl
    return self._call_impl(*args, **kwargs)
  File "/path/to/miniconda3/envs/ascend/lib/python3.8/site-packages/torch/nn/modules/module.py", line 1527, in _call_impl
    return forward_call(*args, **kwargs)
  File "/path/to/miniconda3/envs/ascend/lib/python3.8/site-packages/diffusers/models/activations.py", line 120, in forward
    return torch_npu.npu_geglu(hidden_states, dim=-1, approximate=1)[0]
  File "/path/to/miniconda3/envs/ascend/lib/python3.8/site-packages/torch/_ops.py", line 692, in __call__
    return self._op(*args, **kwargs or {})
RuntimeError: aclnnGeGluV3 or aclnnGeGluV3GetWorkspaceSize not in libopapi.so, or libopapi.sonot found.
[ERROR] 2024-06-21-17:45:42 (PID:17481, Device:0, RankID:-1) ERR01004 OPS invalid pointer

```

### HoiM · 2024-06-21

> model_zoo( https://gitee.com/ascend/ModelZoo-PyTorch/tree/master/PyTorch/built-in/diffusion/stablediffusion-2.1 ) 已有适配完成的，可以参考使用

这个不是基于diffusers的

### Jerrling02 · 2024-07-20

same issue！do you have any updates？

### yunyiyun · 2024-07-24

> 升级到CANN 7.1 torch==2.1.0 torch-npu==2.1.0.post3后，又出现以下问题：
> 
> ```
> Traceback (most recent call last):
>   File "test_script_npu.py", line 15, in <module>
>     image = pipe(prompt).images[0]
>   File "/path/to/miniconda3/envs/ascend/lib/python3.8/site-packages/torch/utils/_contextlib.py", line 115, in decorate_context
>     return func(*args, **kwargs)
>   File "/path/to/miniconda3/envs/ascend/lib/python3.8/site-packages/diffusers/pipelines/stable_diffusion/pipeline_stable_diffusion.py", line 1006, in __call__
>     noise_pred = self.unet(
>   File "/path/to/miniconda3/envs/ascend/lib/python3.8/site-packages/torch/nn/modules/module.py", line 1518, in _wrapped_call_impl
>     return self._call_impl(*args, **kwargs)
>   File "/path/to/miniconda3/envs/ascend/lib/python3.8/site-packages/torch/nn/modules/module.py", line 1527, in _call_impl
>     return forward_call(*args, **kwargs)
>   File "/path/to/miniconda3/envs/ascend/lib/python3.8/site-packages/diffusers/models/unets/unet_2d_condition.py", line 1209, in forward
>     sample, res_samples = downsample_block(
>   File "/path/to/miniconda3/envs/ascend/lib/python3.8/site-packages/torch/nn/modules/module.py", line 1518, in _wrapped_call_impl
>     return self._call_impl(*args, **kwargs)
>   File "/path/to/miniconda3/envs/ascend/lib/python3.8/site-packages/torch/nn/modules/module.py", line 1527, in _call_impl
>     return forward_call(*args, **kwargs)
>   File "/path/to/miniconda3/envs/ascend/lib/python3.8/site-packages/diffusers/models/unets/unet_2d_blocks.py", line 1288, in forward
>     hidden_states = attn(
>   File "/path/to/miniconda3/envs/ascend/lib/python3.8/site-packages/torch/nn/modules/module.py", line 1518, in _wrapped_call_impl
>     return self._call_impl(*args, **kwargs)
>   File "/path/to/miniconda3/envs/ascend/lib/python3.8/site-packages/torch/nn/modules/module.py", line 1527, in _call_impl
>     return forward_call(*args, **kwargs)
>   File "/path/to/miniconda3/envs/ascend/lib/python3.8/site-packages/diffusers/models/transformers/transformer_2d.py", line 440, in forward
>     hidden_states = block(
>   File "/path/to/miniconda3/envs/ascend/lib/python3.8/site-packages/torch/nn/modules/module.py", line 1518, in _wrapped_call_impl
>     return self._call_impl(*args, **kwargs)
>   File "/path/to/miniconda3/envs/ascend/lib/python3.8/site-packages/torch/nn/modules/module.py", line 1527, in _call_impl
>     return forward_call(*args, **kwargs)
>   File "/path/to/miniconda3/envs/ascend/lib/python3.8/site-packages/diffusers/models/attention.py", line 516, in forward
>     ff_output = self.ff(norm_hidden_states)
>   File "/path/to/miniconda3/envs/ascend/lib/python3.8/site-packages/torch/nn/modules/module.py", line 1518, in _wrapped_call_impl
>     return self._call_impl(*args, **kwargs)
>   File "/path/to/miniconda3/envs/ascend/lib/python3.8/site-packages/torch/nn/modules/module.py", line 1527, in _call_impl
>     return forward_call(*args, **kwargs)
>   File "/path/to/miniconda3/envs/ascend/lib/python3.8/site-packages/diffusers/models/attention.py", line 787, in forward
>     hidden_states = module(hidden_states)
>   File "/path/to/miniconda3/envs/ascend/lib/python3.8/site-packages/torch/nn/modules/module.py", line 1518, in _wrapped_call_impl
>     return self._call_impl(*args, **kwargs)
>   File "/path/to/miniconda3/envs/ascend/lib/python3.8/site-packages/torch/nn/modules/module.py", line 1527, in _call_impl
>     return forward_call(*args, **kwargs)
>   File "/path/to/miniconda3/envs/ascend/lib/python3.8/site-packages/diffusers/models/activations.py", line 120, in forward
>     return torch_npu.npu_geglu(hidden_states, dim=-1, approximate=1)[0]
>   File "/path/to/miniconda3/envs/ascend/lib/python3.8/site-packages/torch/_ops.py", line 692, in __call__
>     return self._op(*args, **kwargs or {})
> RuntimeError: aclnnGeGluV3 or aclnnGeGluV3GetWorkspaceSize not in libopapi.so, or libopapi.sonot found.
> [ERROR] 2024-06-21-17:45:42 (PID:17481, Device:0, RankID:-1) ERR01004 OPS invalid pointer
> ```

cann 和 torch_npu 同步更新，可以的话使用最新的版本
