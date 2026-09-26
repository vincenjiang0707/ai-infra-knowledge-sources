# [Issue #2081] [QUESTION] Qwen3 Omni VRAM memory leak

source: https://github.com/ModelCloud/GPTQModel/issues/2081
state: closed | updated: 2025-12-10T20:43:36Z
labels: 

## 正文

The model is around 70 GiB. I tried running GPTQModel on a RTX PRO 6000 with 96GiB vram but still ran out of memory. Config `QuantizeConfig(bits=4, group_size=128)`.

## 评论 (20)

### Qubitium · 2025-10-21

@tommyip  What version of gptqmodel are you using? Make sure you install `main` branch for latest gpu/cpu memory savings.  v5.0.0 (main branch) has hundreds of changes and optimizations not yet fully-released yet since we need to pass some critical ci tests.

```py
git clone --depth 1 ...
cd gptqmodel
pip install -v -e . --no-build-isolation
```

### tommyip · 2025-10-21

I did install the main branch with `uv pip install -v git+https://github.com/ModelCloud/GPTQModel --no-build-isolation`. This should be the same as cloning + build? The version shows as `5.0.0+dev`

### Qubitium · 2025-10-21

> I did install the main branch with `uv pip install -v git+https://github.com/ModelCloud/GPTQModel --no-build-isolation`. This should be the same as cloning + build? The version shows as `5.0.0+dev`

Yes. This is the same as clone + compile.  We are good here. 

You need to post the last 100 lines or so terminial output before you got the oom. I need to see what's going on and I need more debug info. 

### tommyip · 2025-10-21

Ahh I terminated the machine I was renting. This is the only screenshot I have:

<img width="2568" height="454" alt="Image" src="https://github.com/user-attachments/assets/9ffea6a4-e1ef-44c7-8df0-89852667807f" />

I can get more logs later today. I'll also try out an h200 to see if it works.

### Qubitium · 2025-10-21

@tommyip  Make sure to install flash-attention. It may reduce vram usage. Your vram usage and oom is very strange. We did test on A100 with 80GB of memory and it worked so how can it oom on 96GB but we had flash attention enabled and gptqmodel will auto enable it if flash attention is installd.  And collect detailed logs and screenshots next time it crashes so we can see at which step and overall situation awareness. 


### Jun-Howie · 2025-10-21

I remember seeing the 5.0.0 tag yesterday — did something happen to it?

### Qubitium · 2025-10-21

> I remember seeing the 5.0.0 tag yesterday — did something happen to it?

? 5.0 hasn't been released yet. we are doing final ci test validations. 

### tommyip · 2025-10-21

Installed flash attention but still getting OOM. Traceback:
```
Traceback (most recent call last): based config for targeting of modules                                                                            
  File "/workspace/qwen3/quant.py", line 18, in <module>░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░| 0:00:55 / 0:44:00 [1/48] 2.1%
    model.quantize(calibration_dataset, batch_size=1)                                                                                               
  File "/venv/main/lib/python3.12/site-packages/gptqmodel/models/base.py", line 1013, in quantize
    result = module_looper.loop(                                                                                                                    
             ^^^^^^^^^^^^^^^^^^^                                          
  File "/venv/main/lib/python3.12/site-packages/gptqmodel/looper/module_looper.py", line 963, in loop
    return self._loop_impl(fail_safe=fail_safe, **kwargs)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/venv/main/lib/python3.12/site-packages/torch/utils/_contextlib.py", line 120, in decorate_context
    return func(*args, **kwargs)                                          
           ^^^^^^^^^^^^^^^^^^^^^
  File "/venv/main/lib/python3.12/site-packages/gptqmodel/looper/module_looper.py", line 1204, in _loop_impl
    forward_outputs = self._run_forward_batches(
                      ^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/venv/main/lib/python3.12/site-packages/gptqmodel/looper/module_looper.py", line 406, in _run_forward_batches
    return self._run_forward_batches_single(
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/venv/main/lib/python3.12/site-packages/gptqmodel/looper/module_looper.py", line 521, in _run_forward_batches_single
    module_output = module(*layer_input, **additional_inputs)
                    ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/venv/main/lib/python3.12/site-packages/transformers/modeling_layers.py", line 94, in __call__
    return super().__call__(*args, **kwargs)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/venv/main/lib/python3.12/site-packages/torch/nn/modules/module.py", line 1775, in _wrapped_call_impl
    return self._call_impl(*args, **kwargs)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/venv/main/lib/python3.12/site-packages/torch/nn/modules/module.py", line 1786, in _call_impl
    return forward_call(*args, **kwargs)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/venv/main/lib/python3.12/site-packages/transformers/utils/deprecation.py", line 172, in wrapped_func
    return func(*args, **kwargs)
           ^^^^^^^^^^^^^^^^^^^^^
  File "/venv/main/lib/python3.12/site-packages/transformers/models/qwen3_omni_moe/modeling_qwen3_omni_moe.py", line 1535, in forward
    hidden_states, _ = self.self_attn(
                       ^^^^^^^^^^^^^^^
  File "/venv/main/lib/python3.12/site-packages/torch/nn/modules/module.py", line 1775, in _wrapped_call_impl
    return self._call_impl(*args, **kwargs)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/venv/main/lib/python3.12/site-packages/torch/nn/modules/module.py", line 1786, in _call_impl
    return forward_call(*args, **kwargs)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/venv/main/lib/python3.12/site-packages/transformers/utils/deprecation.py", line 172, in wrapped_func
    return func(*args, **kwargs)
           ^^^^^^^^^^^^^^^^^^^^^
  File "/venv/main/lib/python3.12/site-packages/transformers/models/qwen3_omni_moe/modeling_qwen3_omni_moe.py", line 1462, in forward
    attn_output, attn_weights = attention_interface(
                                ^^^^^^^^^^^^^^^^^^^^
  File "/venv/main/lib/python3.12/site-packages/transformers/integrations/sdpa_attention.py", line 96, in sdpa_attention_forward
    attn_output = torch.nn.functional.scaled_dot_product_attention(
                  ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
torch.OutOfMemoryError: CUDA out of memory. Tried to allocate 37.10 GiB. GPU 0 has a total capacity of 94.97 GiB of which 32.70 GiB is free. Including non-PyTorch memory, this process has 62.26 GiB memory in use. Of the allocated memory 58.69 GiB is allocated by PyTorch, and 2.78 GiB is reserved by PyTorch but unallocated. If reserved but unallocated memory is large try setting PYTORCH_CUDA_ALLOC_CONF=expandable_segments:True to avoid fragmentation.  See documentation for Memory Management  (https://pytorch.org/docs/stable/notes/cuda.html#environment-variables)
```
Package versions:
```
gptqmodel 1077c9545f019e29e3eac6313dbf6ed71b4530a9
torch                    2.9.0+cu128
torchvision              0.24.0
transformers             4.57.1   
triton                   3.5.0  
flash-attn               2.8.3 
nvidia-cuda-runtime-cu12 12.8.90 
```
GPU:
```
NVIDIA RTX PRO 6000 Blackwell Workstation
Driver Version: 575.57.08
CUDA Version: 12.9
```
Quant script:
```py
from datasets import load_dataset
from gptqmodel import GPTQModel, QuantizeConfig

model_id = "Qwen/Qwen3-Omni-30B-A3B-Instruct"
quant_path = "Qwen3-Omni-30B-A3B-Instruct-GPTQ-4bit"

calibration_dataset = load_dataset(
    "allenai/c4",
    data_files="en/c4-train.00001-of-01024.json.gz",
    split="train"
  ).select(range(1024))["text"]

quant_config = QuantizeConfig(bits=4, group_size=128)

model = GPTQModel.load(model_id, quant_config)

# increase `batch_size` to match gpu/vram specs to speed up quantization
model.quantize(calibration_dataset, batch_size=1)

model.save(quant_path)
```

Also when `batch_size != 1` I get:
```
  File "/venv/main/lib/python3.12/site-packages/transformers/models/qwen3_omni_moe/modeling_qwen3_omni_moe.py", line 1462, in forward
    attn_output, attn_weights = attention_interface(
                                ^^^^^^^^^^^^^^^^^^^^
  File "/venv/main/lib/python3.12/site-packages/transformers/integrations/sdpa_attention.py", line 96, in sdpa_attention_forward
    attn_output = torch.nn.functional.scaled_dot_product_attention(
                  ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
RuntimeError: The expanded size of the tensor (17640) must match the existing size (8820) at non-singleton dimension 3.  Target sizes: [2, 32, 8820, 17640].  Tensor sizes: [2, 1, 8820, 8820]
```

### Qubitium · 2025-10-22

@tommyip  Your dataset contains single row size exceeding 40k in size. Loop over your dataset rows and only select 1024 that is at or below 2048 or 4096 or 8192 in length or something sane. 40K will blow up inferene vram. 

### ZX-ModelCloud · 2025-10-22

The maximum text length of the calibration_dataset you're using is **40123**. This would take up too much memory.
You can limit the maximum length.

```
from datasets import load_dataset
from gptqmodel import GPTQModel, QuantizeConfig

model_id = "Qwen/Qwen3-Omni-30B-A3B-Instruct"
quant_path = "Qwen3-Omni-30B-A3B-Instruct-GPTQ-4bit"

calibration_dataset = load_dataset(
    "allenai/c4",
    data_files="en/c4-train.00001-of-01024.json.gz",
    split="train"
  )

calibration_dataset = calibration_dataset.filter(lambda x: len(x["text"]) <= 8192)
calibration_dataset = calibration_dataset.select(range(1024))["text"]

quant_config = QuantizeConfig(bits=4, group_size=128)

model = GPTQModel.load(model_id, quant_config)

# increase `batch_size` to match gpu/vram specs to speed up quantization
model.quantize(calibration_dataset, batch_size=1)

model.save(quant_path)
```



### tommyip · 2025-10-22

Thanks. I got it to quantize around half the model but still hit OOM at [22/48] step even at 2048 row size. The vram usage grows slowly overtime - is this suppose to happen?
Did you managed to run the full quant process with the A100?

(Edit: maybe same memory leak as https://github.com/ModelCloud/GPTQModel/pull/1686?)

### Qubitium · 2025-10-23

Please send us the logs, not oom stacktrace, the actual logs preceding the oom. plus the oom stacktrace as well. If we can see the logs, we can't tell.  The terminal logs that shows step, error loss, module name, vram usage per gpu, etc. It has tons of info we need to debug. We can't just go by oom.  We know to now exactly where down to the module. 

### tommyip · 2025-10-23

Stdout/err logs on my RTX 5090. OOMed at layer 3.

[gptqmodel.log](https://github.com/user-attachments/files/23104332/gptqmodel.log)

### allerou4 · 2025-10-29

Hi, I encountered the same issue, I have four cards L20 with 48GB×4

and blow is the last couple of lines of the log, the distribution of memory usage is not balanced.

By the way, loss": "999999999.0000000000 means the quantization is bad?

{
    "process": "gptq",
    "layer": 43,
    "module": "mlp.experts.4.down_proj",
    "feat: in, out": "768, 2048",
    "dtype: size": "bf16: 3.1MB",
    "loss": "999999999.0000000000",
    "samples": "66189",
    "damp": "1.00000",
    "time": "2.013",
    "fwd_time": "94.184",
    "(v)ram": "cuda 44.1G, 21.5G, 12.1G, 3.7G"
}
{
    "process": "gptq",
    "layer": 43,
    "module": "mlp.experts.2.down_proj",
    "feat: in, out": "768, 2048",
    "dtype: size": "bf16: 3.1MB",
    "loss": "999999999.0000000000",
    "samples": "66189",
    "damp": "1.00000",
    "time": "2.018",
    "fwd_time": "94.184",
    "(v)ram": "cuda 44.1G, 21.5G, 12.1G, 3.7G"
}

### tommyip · 2025-11-27

Hey @Qubitium any plans to have a look at this issue? 🙏🏼 

### allerou4 · 2025-12-01

> Hey [@Qubitium](https://github.com/Qubitium) any plans to have a look at this issue? 🙏🏼

Hi， I successfully did it, look at my code:
```python
calibration_dataset = calibration_dataset.filter(lambda x: len(x["text"]) <= 1024)
calibration_dataset = calibration_dataset.select(range(256))["text"]
``` 
I just limited length under 1024 and used 256 samples.

I used a single A800 card with 80GB gpu memory, but memory consumption is around 220GB. I think the code may put a lot of stuff to cpu.

And I will do an experiment to see if 2048 samples works.

### tommyip · 2025-12-05

Indeed using much less samples and sequence length is a workaround. However, at the end of the run it wasn't able to save the weights from the offloaded tensors.

It is missing the tensor `code2wav.upsample.0.1.gamma`:
```
Traceback (most recent call last):
  File "/workspace/quant-omni/main.py", line 23, in <module>
    model.save(quant_path)
  File "/venv/main/lib/python3.12/site-packages/gptqmodel/models/base.py", line 807, in save
    self.save_quantized(
  File "/venv/main/lib/python3.12/site-packages/gptqmodel/models/writer.py", line 307, in save_quantized
    state_dict = get_state_dict_for_save(self.model, offload_root=offload_root)
                 ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/venv/main/lib/python3.12/site-packages/gptqmodel/utils/model.py", line 1419, in get_state_dict_for_save
    state_dict = _collect_state_dict_with_offload(model, offload_root)
                 ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/venv/main/lib/python3.12/site-packages/gptqmodel/utils/model.py", line 1380, in _collect_state_dict_with_offload
    raise FileNotFoundError(
FileNotFoundError: Offloaded tensor 'code2wav.upsample.0.1.gamma' not found in offload directory './gptqmodel_offload/bombe-delicatessen/'.
```

During module sync I can see it is missing that tensor:

```
...
INFO  Module: Sync code2wav.pre_transformer.norm <- from turtle (Qwen3OmniMoeRMSNorm)                                                                                                                                                                                              
INFO  Module: Sync code2wav.pre_transformer.rotary_emb <- from turtle (Qwen3OmniMoeRotaryEmbedding)                                                                                                                                                                                
INFO  Module: Sync code2wav.code_embedding <- from turtle (Embedding)                                                                                                                                                                                                              
INFO  Module: Sync code2wav.upsample.0.0.conv <- from turtle (ConvTranspose1d)                                                                                                                                                                                                     
INFO  Module: Sync code2wav.upsample.0.1.dwconv.conv <- from turtle (Conv1d)                                                                                                                                                                                                       
INFO  Module: Sync code2wav.upsample.0.1.norm <- from turtle (LayerNorm)                                                                                                                                                                                                           
INFO  Module: Sync code2wav.upsample.0.1.pwconv1 <- from turtle (Linear)                                                                                                                                                                                                           
INFO  Module: Sync code2wav.upsample.0.1.pwconv2 <- from turtle (Linear)                                                                                                                                                                                                           
INFO  Module: Sync code2wav.upsample.1.0.conv <- from turtle (ConvTranspose1d)                                                                                                                                                                                                     
INFO  Module: Sync code2wav.upsample.1.1.dwconv.conv <- from turtle (Conv1d)                                                                                                                                                                                                       
INFO  Module: Sync code2wav.upsample.1.1.norm <- from turtle (LayerNorm)                                                                                                                                                                                                           
INFO  Module: Sync code2wav.upsample.1.1.pwconv1 <- from turtle (Linear)                                                                                                                                                                                                           
INFO  Module: Sync code2wav.upsample.1.1.pwconv2 <- from turtle (Linear)                                                                                                                                                                                                           
INFO  Module: Sync code2wav.decoder.0.conv <- from turtle (Conv1d)                                                                                                                                                                                                                 
INFO  Module: Sync code2wav.decoder.1.block.0 <- from turtle (SnakeBeta)                                                                                                                                                                                                           
INFO  Module: Sync code2wav.decoder.1.block.1.conv <- from turtle (ConvTranspose1d)  
...
```

### allerou4 · 2025-12-10

> Indeed using much less samples and sequence length is a workaround. However, at the end of the run it wasn't able to save the weights from the offloaded tensors.
> 
> It is missing the tensor `code2wav.upsample.0.1.gamma`:
> 
> ```
> Traceback (most recent call last):
>   File "/workspace/quant-omni/main.py", line 23, in <module>
>     model.save(quant_path)
>   File "/venv/main/lib/python3.12/site-packages/gptqmodel/models/base.py", line 807, in save
>     self.save_quantized(
>   File "/venv/main/lib/python3.12/site-packages/gptqmodel/models/writer.py", line 307, in save_quantized
>     state_dict = get_state_dict_for_save(self.model, offload_root=offload_root)
>                  ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
>   File "/venv/main/lib/python3.12/site-packages/gptqmodel/utils/model.py", line 1419, in get_state_dict_for_save
>     state_dict = _collect_state_dict_with_offload(model, offload_root)
>                  ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
>   File "/venv/main/lib/python3.12/site-packages/gptqmodel/utils/model.py", line 1380, in _collect_state_dict_with_offload
>     raise FileNotFoundError(
> FileNotFoundError: Offloaded tensor 'code2wav.upsample.0.1.gamma' not found in offload directory './gptqmodel_offload/bombe-delicatessen/'.
> ```
> 
> During module sync I can see it is missing that tensor:
> 
> ```
> ...
> INFO  Module: Sync code2wav.pre_transformer.norm <- from turtle (Qwen3OmniMoeRMSNorm)                                                                                                                                                                                              
> INFO  Module: Sync code2wav.pre_transformer.rotary_emb <- from turtle (Qwen3OmniMoeRotaryEmbedding)                                                                                                                                                                                
> INFO  Module: Sync code2wav.code_embedding <- from turtle (Embedding)                                                                                                                                                                                                              
> INFO  Module: Sync code2wav.upsample.0.0.conv <- from turtle (ConvTranspose1d)                                                                                                                                                                                                     
> INFO  Module: Sync code2wav.upsample.0.1.dwconv.conv <- from turtle (Conv1d)                                                                                                                                                                                                       
> INFO  Module: Sync code2wav.upsample.0.1.norm <- from turtle (LayerNorm)                                                                                                                                                                                                           
> INFO  Module: Sync code2wav.upsample.0.1.pwconv1 <- from turtle (Linear)                                                                                                                                                                                                           
> INFO  Module: Sync code2wav.upsample.0.1.pwconv2 <- from turtle (Linear)                                                                                                                                                                                                           
> INFO  Module: Sync code2wav.upsample.1.0.conv <- from turtle (ConvTranspose1d)                                                                                                                                                                                                     
> INFO  Module: Sync code2wav.upsample.1.1.dwconv.conv <- from turtle (Conv1d)                                                                                                                                                                                                       
> INFO  Module: Sync code2wav.upsample.1.1.norm <- from turtle (LayerNorm)                                                                                                                                                                                                           
> INFO  Module: Sync code2wav.upsample.1.1.pwconv1 <- from turtle (Linear)                                                                                                                                                                                                           
> INFO  Module: Sync code2wav.upsample.1.1.pwconv2 <- from turtle (Linear)                                                                                                                                                                                                           
> INFO  Module: Sync code2wav.decoder.0.conv <- from turtle (Conv1d)                                                                                                                                                                                                                 
> INFO  Module: Sync code2wav.decoder.1.block.0 <- from turtle (SnakeBeta)                                                                                                                                                                                                           
> INFO  Module: Sync code2wav.decoder.1.block.1.conv <- from turtle (ConvTranspose1d)  
> ...
> ```

take a look at this one: https://github.com/ModelCloud/GPTQModel/issues/2197

### Qubitium · 2025-12-10

Should be partially or fully fixed in https://github.com/ModelCloud/GPTQModel/pull/2246

This is a bug within some modeling files which did not honor model.config.use_cache == False and instead passing use_cache = True causing k/v cache to be activated during quantization which we don't need and `leaks` the memory. It is not really leaking the memory as it is doing un-expected caching work when explicitedly told to not cache. 

### tommyip · 2025-12-10

Can confirm the issue is fixed in `main`, thanks @Qubitium. The model output when running with sglang is not as expected but that's a separate issue.
