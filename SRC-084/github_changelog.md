# Changelog (aggregated from releases.body)

> releases: 28

## 0.1.0-alpha (2023-12-01)

## HQQ 0.1.0-alpha

Alpha version with basic Hugging Face/Timm support.

### Supported models:

- Llama (Hugging Face)
- ViT (timm)

### Limitations:
- Uses a pure Pytorch implementation without optimizations. 
- Only supports single GPU runtime.
- Doesn't support Peft (LoRA, etc.) for custom training.


## 0.1.0 (2023-12-05)

## HQQ v0.1.0
### Improvements
- Added compile backend support
- Added Aten C++ backend (experimental)
- Faster bit unpacking via pre-allocated empty tensor
- Added VLLM support
- Refactoring to call `quantize_model()` on instances

### Supported models
- Llama (Hugging Face + VLLM)
- ViT-CLIP (timm)

### Limitations
- HF only supports single GPU runtime.
- VLLM only supports single GPU with a single worker.
- The compile backend sometimes creates issues with async runtime
- Doesn't support PEFT (LoRA, etc.).


## 0.1.1 (2023-12-18)

## HQQ v0.1.1
### Improvements:
- Added Mixtral support for Hugging Face.
- Added support for layer-wise custom quantization configs.

## 0.1.1.post1 (2024-01-03)

## HQQ v0.1.1.post1
No improvements over v0.1.1. Just removed Pytorch from the dependencies and updated the Readme.

## 0.1.2 (2024-01-08)

## HQQ v0.1.2
### Improvements
- Added LoRA support
- Added LoRA with fake quantization support (experimental)
- Optimizer V2 with scale update support
- Some code refactoring in quantize.py



## 0.1.2.post1 (2024-01-18)

## HQQ v0.1.2.post1
### Bug fixes
- Fixed LoRA adapter loading. 


## 0.1.3 (2024-02-12)

## HQQ v0.1.3
### New features
- Added CUDA kernels for dequantization (up to 2-3x inference speed-up vs. Pytorch)
- Added support for ```compute_dtype``` parameter (useful for float32/bfloat16 LoRA training)


## 0.1.3.post1 (2024-02-20)

## HQQ v0.1.3.post1
### New features
- meta_offloading support: allows offloading meta-data to the CPU hence achieving true n-bit storage on the GPU. 


## 0.1.4 (2024-02-28)

## HQQ v0.1.4
### New features
- Added 1-bit support with CUDA dequant kernels.


## 0.1.5 (2024-03-01)

## HQQ v0.1.5
### New features
- Added support for multi-gpu FSDP QLoRA training  (https://github.com/mobiusml/hqq/pull/17)

### Issues
- ```torch.compile``` and the ```PYTORCH_COMPILE``` backend break with ```view_as_float=True```. No known solution for the moment.
- A bit slower inference with   ```view_as_float=True```. Solution: after training, the user can revert back to in bitpacking. 


## 0.1.6 (2024-03-19)

## HQQ v0.1.6
Use v0.1.6.post1 instead, unless you clone the repo first then install. 

### Features
- Quantize on target device.
- Meta-offloading uses pinned memory for faster/async transfers.
- Loading saved LoRA weights automatically adds LoRA modules if not already present.
- ```pip install``` automatically compiles the CUDA kernels now.
- CUDA backend automatically detected and used when available.
- You can quantize any HF model automatically via ```AutoHQQHFModel```.
- Faster meta-offloading with CUDA streams (experimental).
- Int8 matmul (experimental).
- Shared memory CUDA kernels (experimental).

### Bugs
- Fix Peft bias dtype.
- Removed auto backend setting in LoRA.
- All ```HQQLinear``` dtype/device-related overloads now return self which should solve a couple of issues.

### Other
- Refactor backends (using backprop backends by default now).
- Added typing.
- Ruff fix and reformat all Python files.
- Refactor ATEN for reference tensors.

### Issues
- Using CUDA streams for offloading is faster but uses more memory (~+700MB with Llama2-7B 2-bit/gs=16) . In fact, sometimes it's almost  as fast as keeping data on the GPU, so worth looking into this. 
- Shared memory CUDA kernels are a bit slower than without for some reason.
- The block size setting doesn't have much influence on the speed.
- Int8 matmul is slower than fp16 with the current "placeholder" implementation, it should be done on the Aten/CUDA side. 


## 0.1.6.post1 (2024-03-19)

## HQQ v0.1.6.post1
Same as <a href="https://github.com/mobiusml/hqq/releases/tag/0.1.6">v0.1.6</a> with a  ```find_packages``` fix https://github.com/mobiusml/hqq/pull/25 

## 0.1.6.post2 (2024-03-19)

## HQQ v0.1.6.post2
Same as <a href="https://github.com/mobiusml/hqq/releases/tag/0.1.6">v0.1.6</a> with ```setup.py``` fixes:

- ```find_packages``` fix: https://github.com/mobiusml/hqq/pull/25 
- Auto-build CUDA kernels via pypi package: https://github.com/mobiusml/hqq/pull/26


## 0.1.7 (2024-04-24)

## HQQ v0.1.7
-  Faster inference with torchao / marlin 4-bit kernels
- Multi-gpu support for `model.quantize()`
- Custom HF generator
- Various bug fixes/improvements


## 0.1.7.post2 (2024-05-06)

## HQQ v0.1.7.post2
- Various bug fixes, especially with `AutoHQQHFModel` and the patching logic, to make it work with any transformers model.
- Readme refactoring.
- Whisper example.


## v0.1.7.post3 (2024-05-28)

## HQQ v0.1.7.post3

-  Enable CPU quantization and runtime
- `_load_state_dict` fix
- fix `extra_repr` in `HQQLinear`
- fix `from_quantized` bugs
- fix `|` typing
- fix 3-bit `axis=1` slicing bug
- add 5/6 bit for testing

## v0.1.8 (2024-07-11)

## HQQ v0.1.8

-  Add BitBlas backend support 
- Simpler HQQLinear from weights `HQQLinear.from_weights(W, bias, etc.)`
- Fix memory leak while swaping layers for the TorchAO Backend
- Add `HQQLinear.unpack()` call 

## 0.2.0 (2024-08-28)

## HQQ v0.2.0

-  Bug fixes
- Safetensors support for transformers via https://github.com/huggingface/transformers/pull/33141
- `quant_scale`, `quant_zero` and `offload_meta` are now deprecated. You can still use them with the hqq lib, but you can't use them with the transformers lib


## 0.2.1 (2024-08-29)

## HQQ v0.2.1

-  `HQQLinear.state_dict()` for non-initialized layers. Mainly used in for https://github.com/huggingface/transformers/pull/33141


## 0.2.2 (2024-09-12)

## HQQ v0.2.2

- Support static cache compilation without using `HFGenerator`
- Fixing various issues related to `torch.compile`

## 0.2.3 (2025-02-17)

* VLLM support via patching - GemLite backend + on-the-fly quantization
* Add support for Aria 
* Add support to load quantized SequenceClassification
* Faster decoding via (custom cudagraphs, sdpa math backend, etc.)
* Fix bugs related torch compile and hf_generator related to the newer transformers versions
* Fix bugs related to saving quantized models with no grouping
* Fix bugs related to saving large quantized models 
* Update examples
* Add support for HQQLinear `.to(device)` 


## 0.2.3.post1 (2025-02-20)

Bug fixes: 
- Check `W_q` in state dict to fix peft issue https://github.com/mobiusml/hqq/issues/151
- Fix bugs related to `AutoHQQHFModel.save_to_safetensors`

## v0.2.5 (2025-03-17)

-Fix `.name` in backends
-Skip gemlite invalid in/out feature sizes in VLLM patching
-Faster VLLM packing via GemLite

## 0.2.6 (2025-05-13)

- Fix cuda build
- `torchcompile()` support for hqq_aten
- bfloat16 support for vllm/hqq
- Update vllm utils to support `hqq_gemlite` and `hqq_torch` aliases
- FIx vLLM v1 issues
- Extend `save_to_safetensors` to VLMs

**Full Changelog**: https://github.com/mobiusml/hqq/compare/v0.2.5...0.2.6

## 0.2.7 (2025-06-02)

- Fix `nan` bug when `max - min` is very small: https://github.com/mobiusml/hqq/commit/373cbea93892cb491a3c072e0036a37848926404
- Add `DISABLE_CUDA=1` env variable to disable building cuda kernels for then aten backend. This allows faster pip build. https://github.com/mobiusml/hqq/commit/861f6906a2ebf4c864603d7eebd2091b9beb2a77
- Improve memory usage https://github.com/mobiusml/hqq/commit/a566c78961ea408c747ad2a9bd4f3a9235ff3b70
- Fix vLLM torch fallback logic: https://github.com/mobiusml/hqq/commit/d3f14b494eb9939e05a7aba854796eab13da3d3b

## 0.2.7.post1 (2025-06-12)

Bug fixing:
-HIP graph fix in generation: https://github.com/mobiusml/hqq/commit/bc8f4c7d778a0cdbfe115299ea7253ed28948d31
-Fix `HQQLinear` with None linear inputs: https://github.com/mobiusml/hqq/commit/3b86ac950f699a4ca3584cb18bea023b2f5e1da9

## v0.2.8 (2025-08-18)

Bug fixing:
-Fix static cache init with new transformers version
-Add mxfp vllm patching utils
-Improve cuda graphs/compile settings for transformer models


## v0.2.8.post1 (2025-10-20)

Minor toml file patch
