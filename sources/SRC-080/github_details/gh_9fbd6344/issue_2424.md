# [Issue #2424] calling mtq.quantize causes AttributeError: 'tuple' object has no attribute 'dim'

source: https://github.com/NVIDIA/Model-Optimizer/issues/2424
state: open | updated: 2026-09-16T00:41:38Z
labels: question

## 正文

Make sure you already checked the [examples](https://github.com/NVIDIA/Model-Optimizer/tree/main/examples) and [documentation](https://nvidia.github.io/Model-Optimizer/) before submitting an issue.

## How would you like to use ModelOpt

running `python Model-Optimizer/examples/diffusers/quantization/quantize.py --model sdxl-turbo --format fp8 --n-steps 4 --calib-size 128` 

results in

>  File "c:\python\.venv\lib\site-packages\torch\nn\functional.py", line 3040, in group_norm
>     if input.dim() < 2:
> AttributeError: 'tuple' object has no attribute 'dim'

the full output:



> c:\python\.venv\lib\site-packages\torch\jit\_script.py:1491: FutureWarning: `torch.jit.script` is deprecated. Please switch to `torch.compile` or `torch.export`.
>   warnings.warn(
> c:\python\.venv\lib\site-packages\modelopt\torch\__init__.py:55: UserWarning: transformers 4.56.0 is not tested with current version of modelopt and may cause issues. Please install recommended version with `pip install -U nvidia-modelopt[hf]` if working with HF models.
>   _warnings.warn(
> 2026-09-13 18:24:43 | INFO     | __main__ | Starting Enhanced Diffusion Model Quantization
> 2026-09-13 18:24:43 | INFO     | __main__ | Validating configurations...
> 2026-09-13 18:24:43 | INFO     | __main__ | Creating pipeline for sdxl-turbo
> 2026-09-13 18:24:43 | INFO     | __main__ | Model path: stabilityai/sdxl-turbo
> 2026-09-13 18:24:43 | INFO     | __main__ | Data type: {'default': torch.float16}
> Loading pipeline components...:  57%|█████████████████████████████▋                      | 4/7 [00:02<00:01,  1.70it/s]`torch_dtype` is deprecated! Use `dtype` instead!
> Loading pipeline components...: 100%|████████████████████████████████████████████████████| 7/7 [00:05<00:00,  1.35it/s]
> 2026-09-13 18:24:56 | INFO     | __main__ | Pipeline created successfully
> 2026-09-13 18:24:56 | INFO     | __main__ | Moving pipeline to CUDA
> 2026-09-13 18:24:57 | INFO     | __main__ | Initializing calibration...
> 2026-09-13 18:24:57 | INFO     | __main__ | Loading calibration prompts from {'name': 'Gustavosta/Stable-Diffusion-Prompts', 'split': 'train', 'column': 'Prompt'}
> 2026-09-13 18:25:00 | INFO     | __main__ | Quantizing backbone: unet
> 2026-09-13 18:25:00 | INFO     | __main__ | Building quantization config for fp8
> 2026-09-13 18:25:00 | INFO     | __main__ | Quant config {'quant_cfg': [{'quantizer_name': '*', 'enable': False}, {'quantizer_name': '*weight_quantizer', 'cfg': {'num_bits': (4, 3), 'axis': None, 'trt_high_precision_dtype': 'Half'}}, {'quantizer_name': '*input_quantizer', 'cfg': {'num_bits': (4, 3), 'axis': None, 'trt_high_precision_dtype': 'Half'}}, {'quantizer_name': '*output_quantizer', 'enable': False}, {'quantizer_name': '*softmax_quantizer', 'cfg': {'num_bits': (4, 3), 'axis': None, 'trt_high_precision_dtype': 'Half'}}], 'algorithm': {'method': 'max'}}
> 2026-09-13 18:25:00 | INFO     | __main__ | Checking for LoRA layers...
> 2026-09-13 18:25:00 | INFO     | __main__ | Starting model quantization for unet...
> Inserted 3502 quantizers
> 2026-09-13 18:25:01 | INFO     | __main__ | Starting calibration with 64 batches
> Calibration:   0%|                                                                           | 0/64 [00:00<?, ?batch/s]Token indices sequence length is longer than the specified maximum sequence length for this model (101 > 77). Running this sequence through the model will result in indexing errors
> The following part of your input was truncated because CLIP can only handle sequences up to 77 tokens: ['incev, in style of lee souder, in plastic, dark atmosphere, tilt shift, depth of field,', 'trending on art station <|endoftext|><|endoftext|><|endoftext|><|endoftext|><|endoftext|><|endoftext|><|endoftext|><|endoftext|><|endoftext|><|endoftext|><|endoftext|><|endoftext|><|endoftext|><|endoftext|><|endoftext|><|endoftext|><|endoftext|><|endoftext|><|endoftext|><|endoftext|>']
> Token indices sequence length is longer than the specified maximum sequence length for this model (101 > 77). Running this sequence through the model will result in indexing errors
> The following part of your input was truncated because CLIP can only handle sequences up to 77 tokens: ['incev, in style of lee souder, in plastic, dark atmosphere, tilt shift, depth of field,', 'trending on art station <|endoftext|>!!!!!!!!!!!!!!!!!!!']
> Calibration:   0%|                                                                           | 0/64 [00:03<?, ?batch/s]
> 2026-09-13 18:25:05 | ERROR    | __main__ | Quantization failed: 'tuple' object has no attribute 'dim'
> Traceback (most recent call last):
>   File "C:\python\Model-Optimizer\examples\diffusers\quantization\quantize.py", line 706, in main
>     quantizer.quantize_model(
>   File "C:\python\Model-Optimizer\examples\diffusers\quantization\quantize.py", line 239, in quantize_model
>     mtq.quantize(backbone, quant_config, forward_loop)
>   File "c:\python\.venv\lib\site-packages\modelopt\torch\quantization\model_quant.py", line 247, in quantize
>     return calibrate(model, config.get("algorithm"), forward_loop=forward_loop)
>   File "c:\python\.venv\lib\site-packages\modelopt\torch\quantization\model_quant.py", line 110, in calibrate
>     apply_mode(
>   File "c:\python\.venv\lib\site-packages\modelopt\torch\opt\conversion.py", line 419, in apply_mode
>     model, metadata = get_mode(m).convert(model, config, **kwargs)  # type: ignore  [call-arg]
>   File "c:\python\.venv\lib\site-packages\modelopt\torch\quantization\mode.py", line 351, in wrapped_func
>     return wrapped_calib_func(
>   File "c:\python\.venv\lib\site-packages\modelopt\torch\quantization\mode.py", line 273, in wrapped_calib_func
>     func(model, forward_loop=forward_loop, **kwargs)
>   File "c:\python\.venv\lib\site-packages\torch\utils\_contextlib.py", line 124, in decorate_context
>     return func(*args, **kwargs)
>   File "c:\python\.venv\lib\site-packages\modelopt\torch\quantization\model_calib.py", line 354, in max_calibrate
>     forward_loop(model)
>   File "C:\python\Model-Optimizer\examples\diffusers\quantization\quantize.py", line 704, in forward_loop
>     calibrator.run_calibration(batched_prompts)
>   File "C:\python\Model-Optimizer\examples\diffusers\quantization\calibration.py", line 103, in run_calibration
>     self.pipe(**common_args, **extra_args).images
>   File "c:\python\.venv\lib\site-packages\torch\utils\_contextlib.py", line 124, in decorate_context
>     return func(*args, **kwargs)
>   File "c:\python\.venv\lib\site-packages\diffusers\pipelines\stable_diffusion_xl\pipeline_stable_diffusion_xl.py", line 1292, in __call__
>     image = self.vae.decode(latents, return_dict=False)[0]
>   File "c:\python\.venv\lib\site-packages\diffusers\utils\accelerate_utils.py", line 46, in wrapper
>     return method(self, *args, **kwargs)
>   File "c:\python\.venv\lib\site-packages\diffusers\models\autoencoders\autoencoder_kl.py", line 294, in decode
>     decoded = self._decode(z).sample
>   File "c:\python\.venv\lib\site-packages\diffusers\models\autoencoders\autoencoder_kl.py", line 265, in _decode
>     dec = self.decoder(z)
>   File "c:\python\.venv\lib\site-packages\torch\nn\modules\module.py", line 1783, in _wrapped_call_impl
>     return self._call_impl(*args, **kwargs)
>   File "c:\python\.venv\lib\site-packages\torch\nn\modules\module.py", line 1794, in _call_impl
>     return forward_call(*args, **kwargs)
>   File "c:\python\.venv\lib\site-packages\diffusers\models\autoencoders\vae.py", line 298, in forward
>     sample = self.mid_block(sample, latent_embeds)
>   File "c:\python\.venv\lib\site-packages\torch\nn\modules\module.py", line 1783, in _wrapped_call_impl
>     return self._call_impl(*args, **kwargs)
>   File "c:\python\.venv\lib\site-packages\torch\nn\modules\module.py", line 1794, in _call_impl
>     return forward_call(*args, **kwargs)
>   File "c:\python\.venv\lib\site-packages\diffusers\models\unets\unet_2d_blocks.py", line 746, in forward
>     hidden_states = resnet(hidden_states, temb)
>   File "c:\python\.venv\lib\site-packages\torch\nn\modules\module.py", line 1783, in _wrapped_call_impl
>     return self._call_impl(*args, **kwargs)
>   File "c:\python\.venv\lib\site-packages\torch\nn\modules\module.py", line 1794, in _call_impl
>     return forward_call(*args, **kwargs)
>   File "c:\python\.venv\lib\site-packages\diffusers\models\resnet.py", line 327, in forward
>     hidden_states = self.norm1(hidden_states)
>   File "c:\python\.venv\lib\site-packages\torch\nn\modules\module.py", line 1783, in _wrapped_call_impl
>     return self._call_impl(*args, **kwargs)
>   File "c:\python\.venv\lib\site-packages\torch\nn\modules\module.py", line 1794, in _call_impl
>     return forward_call(*args, **kwargs)
>   File "c:\python\.venv\lib\site-packages\torch\nn\modules\normalization.py", line 334, in forward
>     return F.group_norm(input, self.num_groups, self.weight, self.bias, self.eps)
>   File "c:\python\.venv\lib\site-packages\torch\nn\functional.py", line 3040, in group_norm
>     if input.dim() < 2:
> AttributeError: 'tuple' object has no attribute 'dim'

### Who can help?

<!-- To expedite the response to your issue, it would be helpful if you could identify the appropriate person(s) to tag using the @ symbol.
If you are unsure about whom to tag, you can leave it blank, and we will make sure to involve the appropriate person. -->

- ?

## System information

<!-- Run this script to automatically collect system information: https://github.com/NVIDIA/Model-Optimizer/blob/main/.github/ISSUE_TEMPLATE/get_system_info.py -->

- Container used (if applicable): ?
- OS (e.g., Ubuntu 22.04, CentOS 7, Windows 10): ? <!-- If Windows, please add the `windows` label to the issue. -->Windows 11
- CPU architecture (x86_64, aarch64): Core i7 13700K
- GPU name (e.g. H100, A100, L40S): RTX5080
- GPU memory size: 32gb
- Number of GPUs: 1
- Library versions (if applicable):
  - Python: 3.10.14
  - ModelOpt version or commit hash: 0.46.1
  - CUDA: 13.2
  - PyTorch: 2.14.0+cu132
  - Transformers:  4.56.0
  - TensorRT-LLM: ?
  - ONNXRuntime: 1.23.2
  - TensorRT: 10.16.1.11
- Any other details that may help: ?


## 评论 (1)

### mikemikimike · 2026-09-15

Implemented and submitted https://github.com/NVIDIA/Model-Optimizer/pull/2435. The image calibration path now requests latent pipeline output, so calibration does not decode through the VAE. An offline regression test covers the Calibrator.run_calibration call contract. Validation: pytest tests/examples/diffusers/test_calibration.py; pytest tests/unit tests/examples/diffusers/test_calibration.py (3,780 passed, 15 skipped); pre-commit run --all-files.
