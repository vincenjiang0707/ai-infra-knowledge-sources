# [Issue #2679] Problems with Qwen3 Quantization

source: https://github.com/ModelCloud/GPTQModel/issues/2679
state: closed | updated: 2026-04-08T03:17:36Z
labels: 

## 正文

When I quantize sft-qwen3-4b, I found some issues. How can I solve it?:
`Traceback (most recent call last):
  File "/mnt/workspace/AudioLLM/quantize.py", line 639, in <module>
    main()
  File "/mnt/workspace/AudioLLM/quantize.py", line 616, in main
    quantize_gptq(
  File "/mnt/workspace/AudioLLM/quantize.py", line 334, in quantize_gptq
    _quantize_gptq_gptqmodel(
  File "/mnt/workspace/AudioLLM/quantize.py", line 490, in _quantize_gptq_gptqmodel
    model = GPTQModel.load(
  File "/root/miniconda3/envs/cosyvoice/lib/python3.10/site-packages/gptqmodel/models/auto.py", line 445, in load
    m = cls.from_pretrained(
  File "/root/miniconda3/envs/cosyvoice/lib/python3.10/site-packages/gptqmodel/models/auto.py", line 506, in from_pretrained
    return model_definition.from_pretrained(
  File "/root/miniconda3/envs/cosyvoice/lib/python3.10/site-packages/gptqmodel/models/loader.py", line 320, in from_pretrained
    dtype = auto_dtype(config=config, device=quantize_config.device, quant_inference=False)
  File "/root/miniconda3/envs/cosyvoice/lib/python3.10/site-packages/gptqmodel/utils/model.py", line 1237, in auto_dtype
    raise ValueError(f"dtype in config must be a torch.dtype, but got {dtype}")
ValueError: dtype in config must be a torch.dtype, but got bfloat16`

## 评论 (4)

### Judy-Liang · 2026-04-07

when I change config.json，"dypte" to "torch_dtype", then I got another issue:
`Traceback (most recent call last):
  File "/mnt/workspace/AudioLLM/quantize.py", line 663, in <module>
    main()
  File "/mnt/workspace/AudioLLM/quantize.py", line 640, in main
    quantize_gptq(
  File "/mnt/workspace/AudioLLM/quantize.py", line 334, in quantize_gptq
    _quantize_gptq_gptqmodel(
  File "/mnt/workspace/AudioLLM/quantize.py", line 514, in _quantize_gptq_gptqmodel
    model = GPTQModel.load(
  File "/root/miniconda3/envs/cosyvoice/lib/python3.10/site-packages/gptqmodel/models/auto.py", line 445, in load
    m = cls.from_pretrained(
  File "/root/miniconda3/envs/cosyvoice/lib/python3.10/site-packages/gptqmodel/models/auto.py", line 506, in from_pretrained
    return model_definition.from_pretrained(
  File "/root/miniconda3/envs/cosyvoice/lib/python3.10/site-packages/gptqmodel/models/loader.py", line 348, in from_pretrained
    model = build_shell_model(cls.loader, config=shell_config, **model_init_kwargs_without_internal)
  File "/root/miniconda3/envs/cosyvoice/lib/python3.10/site-packages/gptqmodel/utils/hf.py", line 1313, in build_shell_model
    shell = loader.from_config(
  File "/root/miniconda3/envs/cosyvoice/lib/python3.10/site-packages/transformers/models/auto/auto_factory.py", line 456, in from_config
    return model_class._from_config(config, **kwargs)
  File "/root/miniconda3/envs/cosyvoice/lib/python3.10/site-packages/transformers/modeling_utils.py", line 317, in _wrapper
    return func(*args, **kwargs)
  File "/root/miniconda3/envs/cosyvoice/lib/python3.10/site-packages/transformers/modeling_utils.py", line 2382, in _from_config
    model = cls(config, **kwargs)
TypeError: Qwen3ForCausalLM.__init__() got an unexpected keyword argument 'dtype'`

### ZX-ModelCloud · 2026-04-08

Could you please provide the versions of the libraries you are using—specifically `torch`, `gptqmodel`, and `transformers`?
I did not encounter this error when quantizing `SeaFill2025/Qwen3-4B-SFT` using version `v6.0.3`.

Alternatively, you could try installing the latest code directly from the source and then retrying. [install-from-source](https://github.com/ModelCloud/GPTQModel?tab=readme-ov-file#install-from-source)

### Judy-Liang · 2026-04-08

my libraries version:

- torch:2.7.1
- gptqmodel: 6.0.3
- transformers: 4.55.2

### ZX-ModelCloud · 2026-04-08

> my libraries version:
> 
> * torch:2.7.1
> * gptqmodel: 6.0.3
> * transformers: 4.55.2

The issue was reproduced in Transformers v4.55.2.

I will fix it.
