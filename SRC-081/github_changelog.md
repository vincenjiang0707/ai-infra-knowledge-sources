# Changelog (aggregated from releases.body)

> releases: 75

## v0.9.0 (2024-06-20)

## What's Changed (First Release since AutoGPTQ fork)

4 New Models plus `sym=False` asymmetry and `lm_head` quantized inference support. 

* ✨ [FEATURE/BUG] `sym=false` support by @qwopqwop200, @Qubitium, @fxmarty 
* ✨ [FEATURE] `lm_head` quantization inference by @Qubitium 
* 🚀 [MODEL] ChatGLM by @LRL-ModelCloud  @Qubitium 
* 🚀 [MODEL] MiniCPM model support by @LDLINGLINGLING, @Qubitium in https://github.com/ModelCloud/GPTQModel/pull/18
* 🚀 [MODEL] Phi-3 model support by @davidgxue, @ZX-ModelCloud in https://github.com/ModelCloud/GPTQModel/pull/27
* 🚀 [MODEL] QwenMoE model support by @bozheng-hit, @LRL-ModelCloud in https://github.com/ModelCloud/GPTQModel/pull/24
* 🚀 [CORE] Faster quantization and better quality (PPL) quant by @Qubitium 
* 👾[BUG] H100 crash by @Qubitium 
* 👾[BUG] Packing perf regression on high core-count systems by @Qubitium 
* 🚀 [REFRACTOR] Major refractor and code debloat by @Qubitium 
* 🤖 [CI] Code quality by @CSY-ModelCloud in https://github.com/ModelCloud/GPTQModel/pull/31
* 🤖 [CI] Add Perplexity regression test by @LRL-ModelCloud in https://github.com/ModelCloud/GPTQModel/pull/1
* 🤖 [CI] Add Runner by @CSY-ModelCloud in https://github.com/ModelCloud/GPTQModel/pull/3

**Full Changelog**: https://github.com/ModelCloud/GPTQModel/commits/v0.9.0

## v0.9.1 (2024-06-27)

## What's Changed

v0.9.1 is a huge release with 3 new models added in addition to new BITBLAS support from Microsoft. Batching in `.quantize()` has been fixed so the process is now more than 50% faster for batches enabled on large number of calibration data. Also added quantized model sharding support with optional hash security checking of weight files on model load. 

* ✨ [FEATURE + New FORMAT] Add Bitblas Format/Kernel Support by @LeiWang1999 @ZX-ModelCloud @Qubitium  in https://github.com/ModelCloud/GPTQModel/pull/39
* ✨ [FEATURE] Save sharded by @LaaZa @CSY-ModelCloud @PZS-ModelCloud  in https://github.com/ModelCloud/GPTQModel/pull/40 https://github.com/ModelCloud/GPTQModel/pull/69
* ✨ [FEATURE/SECURITY] Add `verify_hash` to validate model weights via stored hashes by @PZS-ModelCloud in https://github.com/ModelCloud/GPTQModel/pull/50
*  🚀 [CORE/REFACTOR] Consolidate 6+ passive `use_xxx` and `disable_xxx`  args to single explicit `backend` arg by @ZX-ModelCloud in https://github.com/ModelCloud/GPTQModel/pull/68
* 🚀 [MODEL] DeepSeek-V2 support by @LRL-ModelCloud in https://github.com/ModelCloud/GPTQModel/pull/51
* 🚀 [MODEL] DeepSeek-V2-Lite support by @LRL-ModelCloud in https://github.com/ModelCloud/GPTQModel/pull/74
* 🚀 [MODEL] DBRX Converted support by @Qubitium @LRL-ModelCloud  in https://github.com/ModelCloud/GPTQModel/pull/38
* 👾 [FIX] Batching of calibration data in .quantize() by @LRL-ModelCloud in https://github.com/ModelCloud/GPTQModel/pull/70
* 👾 [FIX] Cannot pickle 'module' object for 8 bit (fix #47) by @CSY-ModelCloud in https://github.com/ModelCloud/GPTQModel/pull/49
* 👾 [FIX] Format load check by @Qubitium in https://github.com/ModelCloud/GPTQModel/pull/53
* 👾 [FIX] `save_quantized()` using wrong model to obtain state_dict() by @LRL-ModelCloud in https://github.com/ModelCloud/GPTQModel/pull/54
* 👾 [FIX] Rename exllama_kernels class name to fix import/ext conflicts with autogptq by @CSY-ModelCloud in https://github.com/ModelCloud/GPTQModel/pull/71
* 🤖 [CI] Speed up unit tests  @CSY-ModelCloud in https://github.com/ModelCloud/GPTQModel/pull/37 and https://github.com/ModelCloud/GPTQModel/pull/41 and https://github.com/ModelCloud/GPTQModel/pull/46 and  https://github.com/ModelCloud/GPTQModel/pull/55
* 🤖 [CI] Improve unit tests  @ZYC-ModelCloud  in https://github.com/ModelCloud/GPTQModel/pull/58  https://github.com/ModelCloud/GPTQModel/pull/72
* 🤖 👾 [CI] FIx Marlin format `desc_act` must be False. by @LRL-ModelCloud in https://github.com/ModelCloud/GPTQModel/pull/57


## New Contributors
* @LeiWang1999 in https://github.com/ModelCloud/GPTQModel/pull/39
* @LaaZa in https://github.com/ModelCloud/GPTQModel/pull/40
* @PZS-ModelCloud in https://github.com/ModelCloud/GPTQModel/pull/50
* @ZYC-ModelCloud  in https://github.com/ModelCloud/GPTQModel/pull/58

**Full Changelog**: https://github.com/ModelCloud/GPTQModel/compare/v0.9.0...v0.9.1

## v0.9.2 (2024-06-29)

## What's Changed

Added auto-padding of model in/out-features for exllama and exllama v2. Fixed quantization of OPT and DeepSeek V2-Lite models. Fixed inference for DeepSeek V2-Lite.

* ✨ [FEATURE/FIX] Padding infeatures/outfeatures for exllama, exllama v2, and marlin by @Qubitium @LRL-ModelCloud  in https://github.com/ModelCloud/GPTQModel/pull/98
* ✨ [REFRACTOR] remove use_cuda_fp16 argument by @ZX-ModelCloud in https://github.com/ModelCloud/GPTQModel/pull/97
* ✨ [REFRACTOR] `model.post_init`  by @PZS-ModelCloud in https://github.com/ModelCloud/GPTQModel/pull/103
* ✨ [BUILD] Add UV PIP usage instructions information by @CL-ModelCloud in https://github.com/ModelCloud/GPTQModel/pull/114
* 👾 [FIX] DeepSeek-V2-Lite load by @LRL-ModelCloud in https://github.com/ModelCloud/GPTQModel/pull/112
* 👾 [FIX] Opt fc1/fc2 layer modules should not be quantized by @Qubitium in https://github.com/ModelCloud/GPTQModel/pull/118

## New Contributors
* @CL-ModelCloud made their first contribution in https://github.com/ModelCloud/GPTQModel/pull/114

**Full Changelog**: https://github.com/ModelCloud/GPTQModel/compare/v0.9.1...v0.9.2



## v0.9.3 (2024-07-02)

## What's Changed
* 🚀 [MODEL] Add Gemma 2 support by @LRL-ModelCloud in https://github.com/ModelCloud/GPTQModel/pull/131
* 🚀 [OTHER] Calculate ppl on gpu by @ZYC-ModelCloud in https://github.com/ModelCloud/GPTQModel/pull/135
* ✨ [REFRACTOR] BaseQuantLinear and avoid using shared QuantLinear cls name by @PZS-ModelCloud in https://github.com/ModelCloud/GPTQModel/pull/116
* ✨ [KERNEL] Bitblas cache stablity  by @Qubitium in https://github.com/ModelCloud/GPTQModel/pull/129
* 👾 [FIX] Export TORCH_CUDA_ARCH_LIST in install.sh by @LeiWang1999 in https://github.com/ModelCloud/GPTQModel/pull/133
* 👾 [FIX] Limit Bitblas numexpr thread usage by @Qubitium in https://github.com/ModelCloud/GPTQModel/pull/125
* 👾 [FIX] Revert "Skip opt fc1/fc2 for quantization" due to inference regressions (#118)" by @Qubitium in https://github.com/ModelCloud/GPTQModel/pull/149
* ✨ [REFRACTOR] remove max_memory arg by @CL-ModelCloud in https://github.com/ModelCloud/GPTQModel/pull/144
* 🤖 [CI] Fix test was skipped by @CSY-ModelCloud in https://github.com/ModelCloud/GPTQModel/pull/145
* 🤖 [CI] Add GPU selector for runner by @CSY-ModelCloud in https://github.com/ModelCloud/GPTQModel/pull/148

## New Contributors
* @LeiWang1999 made their first contribution in https://github.com/ModelCloud/GPTQModel/pull/133

**Full Changelog**: https://github.com/ModelCloud/GPTQModel/compare/v0.9.2...v0.9.3

## v0.9.4 (2024-07-04)

## What's Changed
* 🚀  [FEATURE] Added Transformers Integration via monkeypatch by @ZX-ModelCloud in https://github.com/ModelCloud/GPTQModel/pull/147
* 👾 [FIX] Typo causing Gemma 2 errors by @LRL-ModelCloud in https://github.com/ModelCloud/GPTQModel/pull/158


**Full Changelog**: https://github.com/ModelCloud/GPTQModel/compare/v0.9.3...v0.9.4

## v0.9.5 (2024-07-05)

## What's Changed

Another large update with added support for Intel/Qbits quantization/inference on CPU. Cuda kernels have been fully deprecated in favor of better performing Exllama (v1/v2), Marlin, and Triton kernels.

* 🚀🚀 [KERNEL] Added Intel QBits support with [2, 3, 4, 8] bits quantization/inference on CPU by @CSY-ModelCloud in https://github.com/ModelCloud/GPTQModel/pull/137
* ✨ [CORE] BaseQuantLinear add SUPPORTED_DEVICES by @ZX-ModelCloud in https://github.com/ModelCloud/GPTQModel/pull/174
* ✨ [DEPRECATION] Remove Backend.CUDA and Backend.CUDA_OLD by @ZX-ModelCloud in https://github.com/ModelCloud/GPTQModel/pull/165
* 👾 [CI] FIX test perplexity by @ZYC-ModelCloud in https://github.com/ModelCloud/GPTQModel/pull/160


**Full Changelog**: https://github.com/ModelCloud/GPTQModel/compare/v0.9.4...v0.9.5

## v0.9.6 (2024-07-08)

## What's Changed

[Intel/AutoRound](https://github.com/intel/auto-round) QUANT_METHOD support added for a potentially higher quality quantization with `lm_head` module quantization support for even more vram reduction: format export to `FORMAT.GPTQ` for max inference compatibility.

* 🚀 [CORE] Add AutoRound as Quantizer option by @LRL-ModelCloud in https://github.com/ModelCloud/GPTQModel/pull/166
* 👾 [FIX] [CI] Update test by @CSY-ModelCloud in https://github.com/ModelCloud/GPTQModel/pull/177
* 👾 Cleanup Triton by @Qubitium in https://github.com/ModelCloud/GPTQModel/pull/178


**Full Changelog**: https://github.com/ModelCloud/GPTQModel/compare/v0.9.5...v0.9.6

## v0.9.7 (2024-07-08)

## What's Changed
* 🚀 [MODEL] InternLM 2.5 support by @LRL-ModelCloud in https://github.com/ModelCloud/GPTQModel/pull/182


**Full Changelog**: https://github.com/ModelCloud/GPTQModel/compare/v0.9.6...v0.9.7

## v0.9.8 (2024-07-13)

## What's Changed

1. Marlin end-to-end in/out feature padding for max model support
2. Run quantized models (`FORMAT.GPTQ`) directly using fast vLLM backend!
3.  Run quantized models (`FORMAT.GPTQ`) directly using fast SGLang backend!

* 🚀 🚀  [CORE] Marlin end-to-end in/out feature padding by @LRL-ModelCloud in https://github.com/ModelCloud/GPTQModel/pull/183 https://github.com/ModelCloud/GPTQModel/pull/192
* 🚀 🚀 [CORE] Add vLLM Backend for FORMAT.GPTQ by @PZS-ModelCloud in https://github.com/ModelCloud/GPTQModel/pull/190
* 🚀 🚀 [CORE] Add SGLang Backend by @PZS-ModelCloud in https://github.com/ModelCloud/GPTQModel/pull/191
* 🚀 [CORE] Use Triton v2 to  pack gptq/gptqv2 formats by @LRL-ModelCloud in https://github.com/ModelCloud/GPTQModel/pull/202
* ✨ [CLEANUP] remove triton warmup by @Qubitium in https://github.com/ModelCloud/GPTQModel/pull/200
* 👾 [FIX] 8bit choosing wrong packer by @Qubitium in https://github.com/ModelCloud/GPTQModel/pull/199
* ✨ [CI] [CLEANUP] Improve Unit Tests by CSY, PSY, and ZYC 
* ✨ [DOC] Consolidate Examples by ZYC in https://github.com/ModelCloud/GPTQModel/pull/225
 

**Full Changelog**: https://github.com/ModelCloud/GPTQModel/compare/v0.9.7...v0.9.8

## v0.9.9 (2024-07-24)

## What's Changed

Added Llama-3.1 support, Gemma2 27B quant inference support via vLLM, auto pad_token normalization, fixed auto-round quant compat for vLLM/SGLang.


* [CI] by @CSY-ModelCloud in https://github.com/ModelCloud/GPTQModel/pull/238, https://github.com/ModelCloud/GPTQModel/pull/236, https://github.com/ModelCloud/GPTQModel/pull/237, https://github.com/ModelCloud/GPTQModel/pull/241, https://github.com/ModelCloud/GPTQModel/pull/242, https://github.com/ModelCloud/GPTQModel/pull/243, https://github.com/ModelCloud/GPTQModel/pull/246, https://github.com/ModelCloud/GPTQModel/pull/247, https://github.com/ModelCloud/GPTQModel/pull/250
* [FIX] explicitly call torch.no_grad() by @LRL-ModelCloud in https://github.com/ModelCloud/GPTQModel/pull/239
* Bitblas update by @Qubitium in https://github.com/ModelCloud/GPTQModel/pull/249
* [FIX] calib avg for calib dataset arg passed as tensors by @Qubitium, @LRL-ModelCloud  in https://github.com/ModelCloud/GPTQModel/pull/254, https://github.com/ModelCloud/GPTQModel/pull/258
* [MODEL] gemma2 27b can load with vLLM now by @LRL-ModelCloud in https://github.com/ModelCloud/GPTQModel/pull/257
* [OPTIMIZE] to optimize vllm inference, set an environment variable 'VLLM_ATTENTI… by @LRL-ModelCloud in https://github.com/ModelCloud/GPTQModel/pull/260
* [FIX] hard set batch_size to 1 for 4.43.0 transformer due to compat/regression by @LRL-ModelCloud in https://github.com/ModelCloud/GPTQModel/pull/279
* FIX vllm llama 3.1 support by @Qubitium in https://github.com/ModelCloud/GPTQModel/pull/280
* Use better defaults values for quantization config by @Qubitium in https://github.com/ModelCloud/GPTQModel/pull/281
* [REFRACTOR] Cleanup backend and model_type usage by @LRL-ModelCloud in https://github.com/ModelCloud/GPTQModel/pull/276
* [FIX] allow auto_round lm_head quantization by @LRL-ModelCloud in https://github.com/ModelCloud/GPTQModel/pull/282
* [FIX] [MODEL] Llama-3.1-8B-Instruct's eos_token_id is a list by @CSY-ModelCloud in https://github.com/ModelCloud/GPTQModel/pull/284
* [FIX] add release_vllm_model, and import destroy_model_parallel in release_vllm_model by @LRL-ModelCloud in https://github.com/ModelCloud/GPTQModel/pull/288
* [FIX] autoround quants compat with vllm/sglang by @Qubitium in https://github.com/ModelCloud/GPTQModel/pull/287

**Full Changelog**: https://github.com/ModelCloud/GPTQModel/compare/v0.9.8...v0.9.9

## v0.9.10 (2024-07-30)

## What's Changed

Ported vllm/nm gptq_marlin inference kernel with expanded bits (8bits), group_size (64,32), and desc_act support for all GPTQ models with `format = FORMAT.GPTQ`. Auto calculate auto-round nsamples/seglen parameters based on calibration dataset. Fixed `save_quantized()` called on pre-quantized models with non-supported backends.  HF transformers depend updated to ensure Llama 3.1 fixes are correctly applied to both quant and inference stage. 

* [CORE] add marlin inference kernel by @ZX-ModelCloud in https://github.com/ModelCloud/GPTQModel/pull/310
* [CI] Increase timeout to 40m by @CSY-ModelCloud in https://github.com/ModelCloud/GPTQModel/pull/295, https://github.com/ModelCloud/GPTQModel/pull/299
* [FIX] save_quantized() by @ZX-ModelCloud in https://github.com/ModelCloud/GPTQModel/pull/296
* [FIX] autoround nsample/seqlen to be actual size of calibration_dataset. by @LRL-ModelCloud in https://github.com/ModelCloud/GPTQModel/pull/297,  @LRL-ModelCloud in https://github.com/ModelCloud/GPTQModel/pull/298
* Update HF transformers to 4.43.3 by @Qubitium in https://github.com/ModelCloud/GPTQModel/pull/305
* [CI] remove test_marlin_hf_cache_serialization() by @ZX-ModelCloud in https://github.com/ModelCloud/GPTQModel/pull/314

**Full Changelog**: https://github.com/ModelCloud/GPTQModel/compare/v0.9.9...v0.9.10

## v0.9.11 (2024-08-09)

## What's Changed

Added LG EXAONE 3.0 model support. New dynamic per layer/module flexible quantization where each layer/module may have different bits/params. Added proper sharding support to backend.BITBLAS. Auto-heal quantization errors due to small damp values.

* [CORE] add support for pack and shard to bitblas by @LRL-ModelCloud in https://github.com/ModelCloud/GPTQModel/pull/316
* Add `dynamic` bits by @PZS-ModelCloud in https://github.com/ModelCloud/GPTQModel/pull/311, https://github.com/ModelCloud/GPTQModel/pull/319, https://github.com/ModelCloud/GPTQModel/pull/321, https://github.com/ModelCloud/GPTQModel/pull/323, https://github.com/ModelCloud/GPTQModel/pull/327
* [MISC] Adjust the validate order of QuantLinear when BACKEND is AUTO by @ZX-ModelCloud in https://github.com/ModelCloud/GPTQModel/pull/318
* add save_quantized log model total size by @PZS-ModelCloud in https://github.com/ModelCloud/GPTQModel/pull/320
* Auto damp recovery by @CSY-ModelCloud in https://github.com/ModelCloud/GPTQModel/pull/326
* [FIX] add missing original_infeatures by @CSY-ModelCloud in https://github.com/ModelCloud/GPTQModel/pull/337
* Update Transformers to 4.44.0 by @Qubitium in https://github.com/ModelCloud/GPTQModel/pull/336
* [MODEL] add exaone model support by @LRL-ModelCloud in https://github.com/ModelCloud/GPTQModel/pull/340
* [CI] Upload wheel to local server by @CSY-ModelCloud in https://github.com/ModelCloud/GPTQModel/pull/339
* [MISC] Fix assert by @CSY-ModelCloud in https://github.com/ModelCloud/GPTQModel/pull/342


**Full Changelog**: https://github.com/ModelCloud/GPTQModel/compare/v0.9.10...v0.9.11

## v1.0.0 (2024-08-14)

## What's Changed

40% faster multi-threaded `packing`, new `lm_eval` api, fixed python 3.9 compat. 

* Add `lm_eval` api by @PZS-ModelCloud in https://github.com/ModelCloud/GPTQModel/pull/338
* Multi-threaded `packing` in quantization by PZS-ModelCloud in https://github.com/ModelCloud/GPTQModel/pull/354
* [CI] Add TGI unit test by @PZS-ModelCloud in https://github.com/ModelCloud/GPTQModel/pull/348
* [CI] Updates by @CSY-ModelCloud in https://github.com/ModelCloud/GPTQModel/pull/347,  https://github.com/ModelCloud/GPTQModel/pull/352, https://github.com/ModelCloud/GPTQModel/pull/353,  https://github.com/ModelCloud/GPTQModel/pull/355, @CSY-ModelCloud in https://github.com/ModelCloud/GPTQModel/pull/357
* Fix python 3.9 compat by @PZS-ModelCloud in https://github.com/ModelCloud/GPTQModel/pull/358


**Full Changelog**: https://github.com/ModelCloud/GPTQModel/compare/v0.9.11...v1.0.0

## v1.0.2 (2024-08-17)

## What's Changed

Upgrade the AutoRound package to v0.3.0. Pre-built WHL and PyPI source releases are now available. Installation can be done by downloading our pre-built WHL or using `pip install gptqmodel --no-build-isolation`.

* [CORE] Autoround v0.3 by @LRL-ModelCloud in https://github.com/ModelCloud/GPTQModel/pull/368
* [CI] Lots of CI fixups by @CSY-ModelCloud 

**Full Changelog**: https://github.com/ModelCloud/GPTQModel/compare/v1.0.0...v1.0.2

## v1.0.3 (2024-09-19)

## What's Changed

* [MODEL] Add minicpm3 by @LDLINGLINGLING in https://github.com/ModelCloud/GPTQModel/pull/385
* [FIX] fix minicpm3 support by @LRL-ModelCloud in https://github.com/ModelCloud/GPTQModel/pull/387
* [MODEL] Added GRIN-MoE support by @LRL-ModelCloud in https://github.com/ModelCloud/GPTQModel/pull/388

## New Contributors
* @LDLINGLINGLING made their first contribution in https://github.com/ModelCloud/GPTQModel/pull/385
* @mrT23 made their first contribution in https://github.com/ModelCloud/GPTQModel/pull/386

**Full Changelog**: https://github.com/ModelCloud/GPTQModel/compare/v1.0.2...v1.0.3

## v1.0.4 (2024-09-26)

## What's Changed

Liger Kernel support added for ~50% vram reduction in quantization stage for some models. Added toggle to disable parallel packing to avoid oom larger models. Transformers depend updated to 4.45.0 for Llama 3.2 support. 

* [FEATURE] add a parallel_packing toggle by @LRL-ModelCloud in https://github.com/ModelCloud/GPTQModel/pull/393
* [FEATURE] add liger_kernel support by @LRL-ModelCloud in https://github.com/ModelCloud/GPTQModel/pull/394


**Full Changelog**: https://github.com/ModelCloud/GPTQModel/compare/v1.0.3...v1.0.4

## v1.0.5 (2024-09-26)

## What's Changed
Added partial quantization support Llama 3.2 Vision model. v1.0.5 allows quantization of text-layers (layers responsible for text-generation) only. We will add vision layer support shortly. A Llama 3.2 11B Vision Instruct models will quantize to 50% of the size in 4bit mode. Once vision layer support is added, the size will reduce to expected ~1/4. 

* [MODEL] Add Llama 3.2 Vision (mllama)* support by @LRL-ModelCloud in https://github.com/ModelCloud/GPTQModel/pull/401


**Full Changelog**: https://github.com/ModelCloud/GPTQModel/compare/v1.0.4...v1.0.5

## v1.0.6 (2024-09-26)

## What's Changed

Patch release to fix loading of quantized Llama 3.2 Vision model. 

* [FIX] mllama loader by @LRL-ModelCloud in https://github.com/ModelCloud/GPTQModel/pull/404


**Full Changelog**: https://github.com/ModelCloud/GPTQModel/compare/v1.0.5...v1.0.6

## v1.0.7 (2024-10-08)

## What's Changed

Fixed marlin (faster) kernel was not auto-selected for some models and `autoround` quantization save throwing json errors. 

* [FIX] marlin_inference_linear not correctly auto selected for eligible models by @ZX-ModelCloud in https://github.com/ModelCloud/GPTQModel/pull/413
* [FIX] remove "scale" and "zp" Tensor from layer_config by @ZX-ModelCloud in https://github.com/ModelCloud/GPTQModel/pull/414
* [FIX] Failed unit test by @ZX-ModelCloud in https://github.com/ModelCloud/GPTQModel/pull/420


**Full Changelog**: https://github.com/ModelCloud/GPTQModel/compare/v1.0.6...v1.0.7

## v1.0.8 (2024-10-11)

## What's Changed

Moved QBits to optional. Add Python 3.12 wheels and fix wheel generation for cuda 11.8. 

* [PKG] update vllm/sglang optional depends by @PZS-ModelCloud in https://github.com/ModelCloud/GPTQModel/pull/423
* [FIX] autoround depend causing torch-cpu to be installed  by @Qubitium in https://github.com/ModelCloud/GPTQModel/pull/422


**Full Changelog**: https://github.com/ModelCloud/GPTQModel/compare/v1.0.7...v1.0.8

## v1.0.9 (2024-10-13)

## What's Changed

Fixed HF integration to work with latest transformers.  Moved AutoRound to optional. Update flaky CI tests. 

* [FIX] mark auto_round extras_require by @LRL-ModelCloud in https://github.com/ModelCloud/GPTQModel/pull/430
* [BUILD] update compile flags by @Qubitium in https://github.com/ModelCloud/GPTQModel/pull/428
* [FIX] failed test_transformers_integration.py by @ZX-ModelCloud in https://github.com/ModelCloud/GPTQModel/pull/435


**Full Changelog**: https://github.com/ModelCloud/GPTQModel/compare/v1.0.8...v1.0.9

## v1.1.0 (2024-10-29)



## What's Changed

IBM Granite model support. Full auto-buildless wheel install from pypi. Reduce max cpu memory usage by >20% during quantization. 100% CI model/feature coverage. Updated hf-integration support with latest transformers.

Full deprecations: liger-kernel support and exllama v1 quant kernel. 

* Fix deprecated by @CSY-ModelCloud in https://github.com/ModelCloud/GPTQModel/pull/447
* [COMPAT] [FIX] vllm params by @ZYC-ModelCloud in https://github.com/ModelCloud/GPTQModel/pull/448
* add estimate-vram by @PZS-ModelCloud in https://github.com/ModelCloud/GPTQModel/pull/452
* add field uri by @ZYC-ModelCloud in https://github.com/ModelCloud/GPTQModel/pull/449
* auto infer model base name from model files by @ZYC-ModelCloud in https://github.com/ModelCloud/GPTQModel/pull/451
* remove exllama v1 by @PZS-ModelCloud in https://github.com/ModelCloud/GPTQModel/pull/453
* [SECURITY]  drop support of loading unsafe .bin weights by @ZYC-ModelCloud in https://github.com/ModelCloud/GPTQModel/pull/460
* [MODEL] add granite support by @LRL-ModelCloud in https://github.com/ModelCloud/GPTQModel/pull/466
* Split base.py file by @ZYC-ModelCloud in https://github.com/ModelCloud/GPTQModel/pull/465
* Move save_quantized function into saver.py by @ZYC-ModelCloud in https://github.com/ModelCloud/GPTQModel/pull/467
* remove deprecated exllama v1 code by @Qubitium in https://github.com/ModelCloud/GPTQModel/pull/473
* [MISC] move model def file to model_def folder by @PZS-ModelCloud in https://github.com/ModelCloud/GPTQModel/pull/479
* [FIX] Fix unit test by @PZS-ModelCloud in https://github.com/ModelCloud/GPTQModel/pull/480
* Download whl in setup.py by @CSY-ModelCloud in https://github.com/ModelCloud/GPTQModel/pull/481
* [Fix] cpu memory leak by @ZX-ModelCloud in https://github.com/ModelCloud/GPTQModel/pull/485
* [CI] set ninja threads to 4 by @CSY-ModelCloud in https://github.com/ModelCloud/GPTQModel/pull/487
* [FIX] sharded model loading error by @ZX-ModelCloud in https://github.com/ModelCloud/GPTQModel/pull/490
* add internlm test by @PZS-ModelCloud in https://github.com/ModelCloud/GPTQModel/pull/491
* remove needless function by @ZYC-ModelCloud in https://github.com/ModelCloud/GPTQModel/pull/494
* Fix unit test by @ZYC-ModelCloud in https://github.com/ModelCloud/GPTQModel/pull/495
* [FIX] fix test_integration by @PZS-ModelCloud in https://github.com/ModelCloud/GPTQModel/pull/497
* [Test] add codegen and xverse test by @PZS-ModelCloud in https://github.com/ModelCloud/GPTQModel/pull/496


**Full Changelog**: https://github.com/ModelCloud/GPTQModel/compare/v1.0.9...v1.1.0

## v1.2.0 (2024-11-11)

Note: 

v1.2.0 was released with wrong version value of 1.2.1-dev. 

We are re-releasing 1.2.0 correctly as 1.2.1. 

https://github.com/ModelCloud/GPTQModel/releases/tag/v1.2.1

## v1.2.1 (2024-11-11)

## What's Changed

- Meta MobileLLM model support added.
- lm-eval[gptqmodel] integration merged upstream. 
- Intel/IPEX cpu inference merged replacing QBits (deprecated). 
- Auto-fix/patch ChatGLM-3/GLM-4 compat with latest transformers. 
- New .load() and .save() api. 100% model CI coverage and unit testing. 

Note that 1.2.1 and 1.2.0 are the same. 1.2.0 release had a bad version  name: 1.2.1-dev embedded in code/release. 
 
PR Logs

* [KERNEL] [CPU] Replace QBits with IPEX by @jiqing-feng in https://github.com/ModelCloud/GPTQModel/pull/527
* [MODEL] add mobilellm support by @LRL-ModelCloud in https://github.com/ModelCloud/GPTQModel/pull/509
* [MODEL] [FIX] chatglm-3 and glm-4 compat with latest transformer by @LRL-ModelCloud in https://github.com/ModelCloud/GPTQModel/pull/555
* [API]  Replace from_pretrained and from_quantized with unified load() by @ZYC-ModelCloud in https://github.com/ModelCloud/GPTQModel/pull/535
* [FIX] throw exception when avg_loss is NaN by @LRL-ModelCloud in https://github.com/ModelCloud/GPTQModel/pull/514
* Remove exllama in gptqmodel_ext folder by @ZYC-ModelCloud in https://github.com/ModelCloud/GPTQModel/pull/521
* Save quant log to csv by @CSY-ModelCloud in https://github.com/ModelCloud/GPTQModel/pull/524
* [CI] Use lm-eval for model regression tests by @PZS-ModelCloud in https://github.com/ModelCloud/GPTQModel/pull/518

## New Contributors
* @jiqing-feng made their first contribution in https://github.com/ModelCloud/GPTQModel/pull/527

**Full Changelog**: https://github.com/ModelCloud/GPTQModel/compare/v1.1.0...v1.2.1

## v1.2.3 (2024-11-25)

Stable release with all feature and model unit tests passing. Fixed lots of model unit tests that did not pass or passed incorrectly in previous releases.  

HF GLM support added. GLM/ChatGLM has two different code forks: one if non-hf integrated, and latest one is integrated into transformers. HF GLM and non-HF GLM are not weight compatible and we support both variants.

## What's Changed
* Add GLM (HF-ied) support by @Qubitium in https://github.com/ModelCloud/GPTQModel/pull/581
* unit tests add args USE_VLLM by @ZYC-ModelCloud in https://github.com/ModelCloud/GPTQModel/pull/582
* Quantize record info by @ZYC-ModelCloud in https://github.com/ModelCloud/GPTQModel/pull/583
* [MISC] add gptqmodel[eval] and remove sentencepiece by @PZS-ModelCloud in https://github.com/ModelCloud/GPTQModel/pull/602
* [MISC] requirements remove gekko, ninja, huggingface-hub, protobuf  by @PZS-ModelCloud in https://github.com/ModelCloud/GPTQModel/pull/603
* release gpu vram after layer.fwd by @LRL-ModelCloud in https://github.com/ModelCloud/GPTQModel/pull/616
* Delete unsupported model & skip gptnoex by @CSY-ModelCloud in https://github.com/ModelCloud/GPTQModel/pull/617
* [FIX] Some models put hidden_states in kwargs instead of args. by @ZX-ModelCloud in https://github.com/ModelCloud/GPTQModel/pull/621
* lm_eval vllm task add max_model_len=4096 args by @LRL-ModelCloud in https://github.com/ModelCloud/GPTQModel/pull/625
* try catch should only work with lmeval by @CSY-ModelCloud in https://github.com/ModelCloud/GPTQModel/pull/628
* set USE_VLLM = False by @LRL-ModelCloud in https://github.com/ModelCloud/GPTQModel/pull/629
* [FIX] if load quantized model. we will not monkey_path forward by @LRL-ModelCloud in https://github.com/ModelCloud/GPTQModel/pull/638
* simplified ModelLoader ModelWriter func by @ZYC-ModelCloud in https://github.com/ModelCloud/GPTQModel/pull/637
* disable chat for test_mpt by @CSY-ModelCloud in https://github.com/ModelCloud/GPTQModel/pull/641
* Update unit_tests.yml by @Qubitium in https://github.com/ModelCloud/GPTQModel/pull/642
* fix tokenized[0] wrong when getting value from BatchEncoding type by @CSY-ModelCloud in https://github.com/ModelCloud/GPTQModel/pull/643

## New Contributors
* @jiqing-feng made their first contribution in https://github.com/ModelCloud/GPTQModel/pull/527

**Full Changelog**: https://github.com/ModelCloud/GPTQModel/compare/v1.2.1...v1.2.3

## v1.3.0 (2024-11-26)

## What's Changed

Zero-Day Hymba model support added. Removed `tqdm` and `rogue` depends.

* Move lm-eval to utils to make it optional, fixed #664 by @CSY-ModelCloud in https://github.com/ModelCloud/GPTQModel/pull/666
* Add ipex bench code by @LRL-ModelCloud in https://github.com/ModelCloud/GPTQModel/pull/660
* [MODEL] add hymba support by @LRL-ModelCloud in https://github.com/ModelCloud/GPTQModel/pull/651
* [FIX] HymbaConfig.conv_dim keys is converted from str to int by @ZX-ModelCloud in https://github.com/ModelCloud/GPTQModel/pull/674
* [FIX] progress first index starts from 1 instead of 0 by @ZX-ModelCloud in https://github.com/ModelCloud/GPTQModel/pull/673


**Full Changelog**: https://github.com/ModelCloud/GPTQModel/compare/v1.2.3...v1.3.0

## v1.3.1 (2024-11-29)

## What's Changed

⚡ Olmo2 model support. 
⚡ Intel XPU acceleration via IPEX. 
Sharding compat fix due to api deprecation in HF Transformers. 
Removed triton dependency. Triton kernel now optionally dependent on triton pkg.
Fixed Hymba Test (Hymba requires desc_act=False)

* [FIX] use split_torch_state_dict_into_shards to replace shard_checkpoint by @LRL-ModelCloud in https://github.com/ModelCloud/GPTQModel/pull/682
* [Model] add olmo2 support by @LRL-ModelCloud in https://github.com/ModelCloud/GPTQModel/pull/678
* [FIX] Hymba currently only supports a batch size of 1 by @ZX-ModelCloud in https://github.com/ModelCloud/GPTQModel/pull/683
* [CI] fix extensions is not defined by @CSY-ModelCloud in https://github.com/ModelCloud/GPTQModel/pull/684
* Ipex XPU support by @jiqing-feng in https://github.com/ModelCloud/GPTQModel/pull/608
* [FIX] add require_pkgs_version and checks by @ZX-ModelCloud in https://github.com/ModelCloud/GPTQModel/pull/693
* fix ipex test by @Qubitium in https://github.com/ModelCloud/GPTQModel/pull/691
* [FIX] remove require_transformers_version and require_tokenizers_version by @ZX-ModelCloud in https://github.com/ModelCloud/GPTQModel/pull/695
* Remove use_safetensors argument by @ZX-ModelCloud in https://github.com/ModelCloud/GPTQModel/pull/696
* Revert exllamav1 by @CSY-ModelCloud in https://github.com/ModelCloud/GPTQModel/pull/692
* Make Triton optional by @CSY-ModelCloud in https://github.com/ModelCloud/GPTQModel/pull/697
* Unify backend use by @LRL-ModelCloud in https://github.com/ModelCloud/GPTQModel/pull/700
* [FIX] fix test_hymba by @ZX-ModelCloud in https://github.com/ModelCloud/GPTQModel/pull/704
* FIX IPEX XPU selection by @Qubitium in https://github.com/ModelCloud/GPTQModel/pull/705
* fix cpu/xpu backend selection by @jiqing-feng in https://github.com/ModelCloud/GPTQModel/pull/706
* Upgrade device-smi depend by @Qubitium in https://github.com/ModelCloud/GPTQModel/pull/708
* [FIX] hymba quant needs desc_act=False by @ZX-ModelCloud in https://github.com/ModelCloud/GPTQModel/pull/710


**Full Changelog**: https://github.com/ModelCloud/GPTQModel/compare/v1.3.0...v1.3.1

## v1.4.0 (2024-12-10)

## What's Changed

⚡ `EvalPlus` harness integration merged upstream. We now support both `lm-eval` and `EvalPlus`. 
⚡ Added pure torch `Torch` kernel. 
⚡ Refactored `Cuda` kernel to be `DynamicCuda` kernel. 
⚡ `Triton` kernel now auto-padded for max model support. 
⚡ `Dynamic` quantization now supports both positive +::default, and -: negative matching which allows matched modules to be skipped entirely for quantization.
⚡Added auto-kernel fallback for unsupported kernel/module pairs. 
🐛  Fixed auto-`Marlin` kernel selection. 
🗑 Deprecated the saving of `Marlin` weight format. `Marlin` allows auto conversion of `gptq` format to `Marlin` during runtime. `gptq` format allows max kernel flexibility including `Marlin` kernel support. 

Lots of internal refractor and cleanup in-preparation for transformers/optimum/peft upstream PR merge.

* Remove Marlin old kernel and Marlin format saving. Marlin[new] is still supported via inference.  by @CSY-ModelCloud in https://github.com/ModelCloud/GPTQModel/pull/714
* Remove marlin(old) kernel codes & do ruff by @CSY-ModelCloud in https://github.com/ModelCloud/GPTQModel/pull/719
* [FIX] gptq v2 load by @ZX-ModelCloud in https://github.com/ModelCloud/GPTQModel/pull/724
* Add hf_convert_gptq_v1_to_v2_format, hf_convert_gptq_v2_to_v1_format,… by @LRL-ModelCloud in https://github.com/ModelCloud/GPTQModel/pull/727
* if use the ipex quant linear, no need to convert by @LRL-ModelCloud in https://github.com/ModelCloud/GPTQModel/pull/730
* hf_select_quant_linear add device_map by @LRL-ModelCloud in https://github.com/ModelCloud/GPTQModel/pull/732
* Add TorchQuantLinear by @ZX-ModelCloud in https://github.com/ModelCloud/GPTQModel/pull/735
* Add QUANT_TYPE in qlinear by @jiqing-feng in https://github.com/ModelCloud/GPTQModel/pull/736
* Replace error with warning for Intel CPU check by @CSY-ModelCloud in https://github.com/ModelCloud/GPTQModel/pull/737
* Add BACKEND.AUTO_CPU by @LRL-ModelCloud in https://github.com/ModelCloud/GPTQModel/pull/739
* Fix ipex linear check by @jiqing-feng in https://github.com/ModelCloud/GPTQModel/pull/741
* fFx select quant linear by @jiqing-feng in https://github.com/ModelCloud/GPTQModel/pull/742
* Now meta.quantizer value can be an array by @ZX-ModelCloud in https://github.com/ModelCloud/GPTQModel/pull/744
* Receive checkpoint_format argument by @ZX-ModelCloud in https://github.com/ModelCloud/GPTQModel/pull/747
* Modify hf convert gptq v2 to v1 format by @ZX-ModelCloud in https://github.com/ModelCloud/GPTQModel/pull/749
* update score max negative delta by @CSY-ModelCloud in https://github.com/ModelCloud/GPTQModel/pull/748
* [CI] max parallel jobs 10 by @CSY-ModelCloud in https://github.com/ModelCloud/GPTQModel/pull/751
* hymba got high score by @CSY-ModelCloud in https://github.com/ModelCloud/GPTQModel/pull/752
* hf_select_quant_linear() always set pack=True by @ZX-ModelCloud in https://github.com/ModelCloud/GPTQModel/pull/754
* Refractor CudaQuantLinear to DynamicCudaQuantLinear by @ZX-ModelCloud in https://github.com/ModelCloud/GPTQModel/pull/759
* Remove filename prefix on qlinear dir by @ZX-ModelCloud in https://github.com/ModelCloud/GPTQModel/pull/760
* Replace Nvidia-smi with devicesmi by @CSY-ModelCloud in https://github.com/ModelCloud/GPTQModel/pull/761
* Fix XPU training by @jiqing-feng in https://github.com/ModelCloud/GPTQModel/pull/763
* Fix auto marlin kernel selection by @CSY-ModelCloud in https://github.com/ModelCloud/GPTQModel/pull/765
* Add BaseQuantLinear SUPPORTS_TRAINING declaration by @LRL-ModelCloud in https://github.com/ModelCloud/GPTQModel/pull/766
* Add Eval() api to support LM-Eval or EvalPlus benchmark harnesses by @CL-ModelCloud in https://github.com/ModelCloud/GPTQModel/pull/750
* Fix validate_device by @LRL-ModelCloud in https://github.com/ModelCloud/GPTQModel/pull/769
* Force BaseQuantLinear properties to be explicitly declared by all QuantLinears by @ZX-ModelCloud in https://github.com/ModelCloud/GPTQModel/pull/767
* Convert str backend to enum backend by @LRL-ModelCloud in https://github.com/ModelCloud/GPTQModel/pull/772
* Remove nested list in dict by @CSY-ModelCloud in https://github.com/ModelCloud/GPTQModel/pull/774
* Fix training qlinear by @LRL-ModelCloud in https://github.com/ModelCloud/GPTQModel/pull/777
* Check kernel by @CSY-ModelCloud in https://github.com/ModelCloud/GPTQModel/pull/764
* BACKEND.AUTO if backend is None by @LRL-ModelCloud in https://github.com/ModelCloud/GPTQModel/pull/781
* Fix lm_head quantize test by @CSY-ModelCloud in https://github.com/ModelCloud/GPTQModel/pull/784
* Fix exllama doesn't support 8 bit by @CSY-ModelCloud in https://github.com/ModelCloud/GPTQModel/pull/790
* Use set() to avoid calling torch twice by @CSY-ModelCloud in https://github.com/ModelCloud/GPTQModel/pull/791
* Fix ipex cpu backend import error and fix too much logs by @jiqing-feng in https://github.com/ModelCloud/GPTQModel/pull/793
* Eval API opt by @CL-ModelCloud in https://github.com/ModelCloud/GPTQModel/pull/794
* Fixed ipex linear param check and logging once by @jiqing-feng in https://github.com/ModelCloud/GPTQModel/pull/795
* Check device before sync by @LRL-ModelCloud in https://github.com/ModelCloud/GPTQModel/pull/796
* Only AUTO will try other quant linears by @CSY-ModelCloud in https://github.com/ModelCloud/GPTQModel/pull/797
* Add SUPPORTS_AUTO_PADDING property to QuantLinear by @LRL-ModelCloud in https://github.com/ModelCloud/GPTQModel/pull/799
* Dynamic now support skipping modules/layers by @CSY-ModelCloud in https://github.com/ModelCloud/GPTQModel/pull/804
* Fix module was skipped but still be looped by @CSY-ModelCloud in https://github.com/ModelCloud/GPTQModel/pull/806
* Make Triton kernel auto-pad on features/group_size by @LRL-ModelCloud in https://github.com/ModelCloud/GPTQModel/pull/808


**Full Changelog**: https://github.com/ModelCloud/GPTQModel/compare/v1.3.1...v1.4.0

## v1.4.1 (2024-12-13)

## What's Changed

⚡ Added Qwen2-VL model support. 
⚡ `mse` quantization control exposed in QuantizeConfig
⚡ New `GPTQModel.patch_hf()` and `GPTQModel.patch_vllm()` monkey patch api to allow Transformers/Optimum/Peft to use GPTQModel while upstream PRs are pending.
⚡ New `GPTQModel.patch_vllm()` monkey patch api to allow `vLLM` to correctly load `dynamic`/mixed gptq quantized models. 

* Add warning for vllm/sglang when using dynamic feature by @CSY-ModelCloud in https://github.com/ModelCloud/GPTQModel/pull/810
* Update Eval() usage sample by @CL-ModelCloud in https://github.com/ModelCloud/GPTQModel/pull/819
* auto select best device by @CSY-ModelCloud in https://github.com/ModelCloud/GPTQModel/pull/822
* Fix error msg by @CSY-ModelCloud in https://github.com/ModelCloud/GPTQModel/pull/823
* allow pass meta_quantizer from save() by @CSY-ModelCloud in https://github.com/ModelCloud/GPTQModel/pull/824
* Quantconfig add mse field by @CL-ModelCloud in https://github.com/ModelCloud/GPTQModel/pull/825
* [MODEL] add qwen2_vl support by @LRL-ModelCloud in https://github.com/ModelCloud/GPTQModel/pull/826
* check cuda when there's only cuda device by @CSY-ModelCloud in https://github.com/ModelCloud/GPTQModel/pull/830
* Update lm-eval test by @CL-ModelCloud in https://github.com/ModelCloud/GPTQModel/pull/831
* add patch_vllm() by @ZX-ModelCloud in https://github.com/ModelCloud/GPTQModel/pull/829
* Monkey patch HF transformer/optimum/peft support by @CSY-ModelCloud in https://github.com/ModelCloud/GPTQModel/pull/818
* auto patch vllm by @CSY-ModelCloud in https://github.com/ModelCloud/GPTQModel/pull/837
* Fix lm-eval API BUG by @CL-ModelCloud in https://github.com/ModelCloud/GPTQModel/pull/838
* [FIX] dynamic get "desc_act" error by @ZX-ModelCloud in https://github.com/ModelCloud/GPTQModel/pull/841
* BaseModel add supports_desc_act by @ZX-ModelCloud in https://github.com/ModelCloud/GPTQModel/pull/842
* [FIX] should local import patch_vllm() by @ZX-ModelCloud in https://github.com/ModelCloud/GPTQModel/pull/844
* Mod vllm generate by @LRL-ModelCloud in https://github.com/ModelCloud/GPTQModel/pull/833
* fix patch_vllm by @LRL-ModelCloud in https://github.com/ModelCloud/GPTQModel/pull/850


**Full Changelog**: https://github.com/ModelCloud/GPTQModel/compare/v1.4.0...v1.4.1

## v1.4.2 (2024-12-16)

## What's Changed

⚡ MacOS `gpu` (MPS) + `cpu` inference and quantization support 
⚡ Added Cohere 2 model support

* Build Changes by @Qubitium in https://github.com/ModelCloud/GPTQModel/pull/855
* Fix MacOS support by @Qubitium in https://github.com/ModelCloud/GPTQModel/pull/861
* check device_map on from_quantized() by @ZX-ModelCloud in https://github.com/ModelCloud/GPTQModel/pull/865
* call patch for TestTransformersIntegration by @CSY-ModelCloud in https://github.com/ModelCloud/GPTQModel/pull/867
* Add MacOS gpu acceleration via MPS by @Qubitium in https://github.com/ModelCloud/GPTQModel/pull/864
* [MODEL] add cohere2 support  by @CL-ModelCloud in https://github.com/ModelCloud/GPTQModel/pull/869
* check device_map by @ZX-ModelCloud in https://github.com/ModelCloud/GPTQModel/pull/872
* set PYTORCH_ENABLE_MPS_FALLBACK for macos by @CSY-ModelCloud in https://github.com/ModelCloud/GPTQModel/pull/873
* check device_map int value by @ZX-ModelCloud in https://github.com/ModelCloud/GPTQModel/pull/876
* Simplify by @Qubitium in https://github.com/ModelCloud/GPTQModel/pull/877
* [FIX] device_map={"":None} by @ZX-ModelCloud in https://github.com/ModelCloud/GPTQModel/pull/878
* set torch_dtype to float16 for XPU by @CSY-ModelCloud in https://github.com/ModelCloud/GPTQModel/pull/875
* remove  IPEX device check by @ZX-ModelCloud in https://github.com/ModelCloud/GPTQModel/pull/879
* [FIX] call normalize_device() by @ZX-ModelCloud in https://github.com/ModelCloud/GPTQModel/pull/881
* [FIX] get_best_device() wrong usage by @ZX-ModelCloud in https://github.com/ModelCloud/GPTQModel/pull/882


**Full Changelog**: https://github.com/ModelCloud/GPTQModel/compare/v1.4.1...v1.4.2

## v1.4.4 (2024-12-17)

## What's Changed

⚡ Reduced memory usage during quantization
⚡ Fix `device_map={"":"auto"}` compat

* Speed up unit tests by @Qubitium in https://github.com/ModelCloud/GPTQModel/pull/885
* [FIX] hf select quant linear parse device map by @ZX-ModelCloud in https://github.com/ModelCloud/GPTQModel/pull/887
* Avoid cloning on gpu by @Qubitium in https://github.com/ModelCloud/GPTQModel/pull/886
* Expose hf_quantize() by @ZX-ModelCloud in https://github.com/ModelCloud/GPTQModel/pull/888
* Update integration hf code by @ZX-ModelCloud in https://github.com/ModelCloud/GPTQModel/pull/891
* Add back fasterquant() for compat by @Qubitium in https://github.com/ModelCloud/GPTQModel/pull/892

**Full Changelog**: https://github.com/ModelCloud/GPTQModel/compare/v1.4.2...v1.4.4

## v1.4.5 (2024-12-19)

## What's Changed

⚡ Windows 11 support added/validated with `DynamicCuda` and `Torch` kernels.
⚡ Ovis 1.6 VL model support with image data calibration. 
⚡ Reduced quantization vram usage.
🐛 Fixed `dynamic` controlled layer loading logic

* Refractor  by @Qubitium in https://github.com/ModelCloud/GPTQModel/pull/895
* Add platform check by @LRL-ModelCloud in https://github.com/ModelCloud/GPTQModel/pull/899
* Exclude marlin & exllama on windows by @CSY-ModelCloud in https://github.com/ModelCloud/GPTQModel/pull/898
* Remove unnecessary backslash in the expression  & typehint by @CSY-ModelCloud in https://github.com/ModelCloud/GPTQModel/pull/903
* Add DEVICE.ALL by @LRL-ModelCloud in https://github.com/ModelCloud/GPTQModel/pull/901
* [FIX] the error of loading quantized model with dynamic by @ZX-ModelCloud in https://github.com/ModelCloud/GPTQModel/pull/907
* [FIX] gpt2 quantize error by @ZX-ModelCloud in https://github.com/ModelCloud/GPTQModel/pull/912
* Simplify checking generated str for vllm test & fix transformers version for cohere2 by @CSY-ModelCloud in https://github.com/ModelCloud/GPTQModel/pull/914
* [MODEL] add OVIS support by @ZX-ModelCloud in https://github.com/ModelCloud/GPTQModel/pull/685
* Fix IDE warning marlin not in __all__ by @CSY-ModelCloud in https://github.com/ModelCloud/GPTQModel/pull/920


**Full Changelog**: https://github.com/ModelCloud/GPTQModel/compare/v1.4.4...v1.4.5

## v1.5.0 (2024-12-24)

## What's Changed

⚡ Multi-modal (image-to-text) optimized quantization support has been added for Qwen 2-VL and Ovis 1.6-VL. Previous image-to-text model quantizations did not use image calibration data, resulting in less than optimal post-quantization results. Version 1.5.0 is the first release to provide a stable path for multi-modal quantization: only text layers are quantized.
🐛 Fixed Qwen 2-VL model quantization vram usage and post-quant file copy of relevant config files.
🐛 Fixed install/compilations in envs with wrong TORCH_CUDA_ARCH_LIST set (Nvidia docker images) 
🐛 Warn about bad torch[cuda] install on Windows

* Fix backend not ipex by @CSY-ModelCloud in https://github.com/ModelCloud/GPTQModel/pull/930
* Fix broken ipex check by @Qubitium in https://github.com/ModelCloud/GPTQModel/pull/933
* Fix dynamic_cuda validation by @CSY-ModelCloud in https://github.com/ModelCloud/GPTQModel/pull/936
* Fix bdist_wheel does not exist on old setuptools by @CSY-ModelCloud in https://github.com/ModelCloud/GPTQModel/pull/939
* Add cuda warning on windows by @CSY-ModelCloud in https://github.com/ModelCloud/GPTQModel/pull/942
* Add torch inference benchmark by @CL-ModelCloud in https://github.com/ModelCloud/GPTQModel/pull/940
* Add `modality` to `BaseModel` by @ZX-ModelCloud in https://github.com/ModelCloud/GPTQModel/pull/937
* [FIX] qwen_vl_utils should be locally import by @ZX-ModelCloud in https://github.com/ModelCloud/GPTQModel/pull/946
* Filter torch cuda arch < 6.0 by @CSY-ModelCloud in https://github.com/ModelCloud/GPTQModel/pull/955
* [FIX] wrong filepath was used when model_id_or_path was hugging model id by @ZX-ModelCloud in https://github.com/ModelCloud/GPTQModel/pull/956
* Fix import error was not caught by @CSY-ModelCloud in https://github.com/ModelCloud/GPTQModel/pull/961


**Full Changelog**: https://github.com/ModelCloud/GPTQModel/compare/v1.4.5...v1.5.0

## v1.5.1 (2025-01-01)

## What's Changed

 🎉 2025! 
 
⚡ Added `QuantizeConfig.device` to clearly define which device is used for quantization: default = `auto`. Non-quantized models are always loaded on cpu by-default and each layer is moved to `QuantizeConfig.device` during quantization to minimize vram usage. 
💫   Improve `QuantLinear` selection from `optimum`.
🐛  Fix `attn_implementation_autoset` compat in latest transformers.

* Add QuantizeConfig.device and use.  by @Qubitium in https://github.com/ModelCloud/GPTQModel/pull/950
* fix hf_select_quant_linear by @LRL-ModelCloud in https://github.com/ModelCloud/GPTQModel/pull/966
* update vllm gptq_marlin code by @ZX-ModelCloud in https://github.com/ModelCloud/GPTQModel/pull/967
* fix cuda:0 not a enum device by @CSY-ModelCloud in https://github.com/ModelCloud/GPTQModel/pull/968
* fix marlin info for non-cuda device by @Qubitium in https://github.com/ModelCloud/GPTQModel/pull/972
* fix backend str bug by @CL-ModelCloud in https://github.com/ModelCloud/GPTQModel/pull/973
* hf select quant_linear with pack by @LRL-ModelCloud in https://github.com/ModelCloud/GPTQModel/pull/969
* remove auto select BACKEND.IPEX by @CSY-ModelCloud in https://github.com/ModelCloud/GPTQModel/pull/975
* fix autoround received a device_map by @CSY-ModelCloud in https://github.com/ModelCloud/GPTQModel/pull/976
* use enum instead of magic number by @CSY-ModelCloud in https://github.com/ModelCloud/GPTQModel/pull/979
* use new ci docker images by @CSY-ModelCloud in https://github.com/ModelCloud/GPTQModel/pull/980
* fix flash attntion was auto loaded on cpu for pretrained model by @CSY-ModelCloud in https://github.com/ModelCloud/GPTQModel/pull/981
* fix old transformer doesn't have _attn_implementation_autoset by @CSY-ModelCloud in https://github.com/ModelCloud/GPTQModel/pull/982
* fix gptbigcode test temporally by @CSY-ModelCloud in https://github.com/ModelCloud/GPTQModel/pull/983
* fix version parsing by @CSY-ModelCloud in https://github.com/ModelCloud/GPTQModel/pull/985


**Full Changelog**: https://github.com/ModelCloud/GPTQModel/compare/v1.5.0...v1.5.1

## v1.6.0 (2025-01-06)

## What's Changed

⚡ 25% faster quantization. 35% reduction in vram usage vs v1.5.  👀 
🎉  AMD ROCm (6.2+) support added and validated for 7900XT+ GPU. 
💫 Auto-tokenizer loader via load() api. For most models you no longer need to manually init a tokenizer for both inference and quantization.

* note about `batch_size` to speed up quant by @Qubitium in https://github.com/ModelCloud/GPTQModel/pull/992
* Add ROCm support by @CSY-ModelCloud in https://github.com/ModelCloud/GPTQModel/pull/993
* Add bits test by @ZX-ModelCloud in https://github.com/ModelCloud/GPTQModel/pull/995
* note about rocm support by @Qubitium in https://github.com/ModelCloud/GPTQModel/pull/998
* [FIX] wrong variable name by @ZX-ModelCloud in https://github.com/ModelCloud/GPTQModel/pull/997
* update rocm version tag by @CSY-ModelCloud in https://github.com/ModelCloud/GPTQModel/pull/999
* Auto-tokenizer will be called within `load()` by @LRL-ModelCloud in https://github.com/ModelCloud/GPTQModel/pull/996
* update transformers by @Qubitium in https://github.com/ModelCloud/GPTQModel/pull/1001
* [FIX] torch qlinear forward by @ZX-ModelCloud in https://github.com/ModelCloud/GPTQModel/pull/1002
* cleanup marlin info by @Qubitium in https://github.com/ModelCloud/GPTQModel/pull/1004
* Use custom forward hook by @LRL-ModelCloud in https://github.com/ModelCloud/GPTQModel/pull/1003
* fix hooked linear init by @LRL-ModelCloud in https://github.com/ModelCloud/GPTQModel/pull/1011
* add HookedConv1D by @LRL-ModelCloud in https://github.com/ModelCloud/GPTQModel/pull/1012
* record fwd time by @LRL-ModelCloud in https://github.com/ModelCloud/GPTQModel/pull/1013
* add PYTORCH_CUDA_ALLOC_CONF for global & do ruff by @CSY-ModelCloud in https://github.com/ModelCloud/GPTQModel/pull/1015
* [FIX] quantize_config could not read from config.json by @ZX-ModelCloud in https://github.com/ModelCloud/GPTQModel/pull/1022
* Fix quant time by @LRL-ModelCloud in https://github.com/ModelCloud/GPTQModel/pull/1025
* fix forward hook by @LRL-ModelCloud in https://github.com/ModelCloud/GPTQModel/pull/1027
* Fix hooked conv2d by @LRL-ModelCloud in https://github.com/ModelCloud/GPTQModel/pull/1030
* clean cache by @CL-ModelCloud in https://github.com/ModelCloud/GPTQModel/pull/1032


**Full Changelog**: https://github.com/ModelCloud/GPTQModel/compare/v1.5.1...v1.6.0

## v1.6.1 (2025-01-09)

## What's Changed

🎉  New OpenAI api compatible end-point via `model.serve(host, port)`. 
⚡ Auto-enable flash-attention2 for inference. 
🐛 Fixed `sym=False` loading regression.

* code opt by @CL-ModelCloud in https://github.com/ModelCloud/GPTQModel/pull/1038
* fix marlin validate rocm & do validate() if backend not AUTO by @CSY-ModelCloud in https://github.com/ModelCloud/GPTQModel/pull/1040
* add global rocm check by @CSY-ModelCloud in https://github.com/ModelCloud/GPTQModel/pull/1043
* [FIX] pass sym to make_quant by @LRL-ModelCloud in https://github.com/ModelCloud/GPTQModel/pull/1046
* enable flash attn for loading quantized by @CSY-ModelCloud in https://github.com/ModelCloud/GPTQModel/pull/1045
* add flash_attn2 test by @CSY-ModelCloud in https://github.com/ModelCloud/GPTQModel/pull/1047
* enable flash_attention only when device is cuda by @CSY-ModelCloud in https://github.com/ModelCloud/GPTQModel/pull/1050
* move flash attn test to correct folder by @CSY-ModelCloud in https://github.com/ModelCloud/GPTQModel/pull/1052
* Expose openai server api by @CL-ModelCloud in https://github.com/ModelCloud/GPTQModel/pull/1048
* update openai server by @CL-ModelCloud in https://github.com/ModelCloud/GPTQModel/pull/1058
* don't download whl for xpu env by @CSY-ModelCloud in https://github.com/ModelCloud/GPTQModel/pull/1059
* remove build tag for normal release by @CSY-ModelCloud in https://github.com/ModelCloud/GPTQModel/pull/1063
* disable flash attn 2 for internlm by @CSY-ModelCloud in https://github.com/ModelCloud/GPTQModel/pull/1065


**Full Changelog**: https://github.com/ModelCloud/GPTQModel/compare/v1.6.0...v1.6.1

## v1.7.0 (2025-01-17)

## What's Changed

⚡`backend.MLX` added for runtime-conversion and execution of GPTQ models on Apple's `MLX` framework on Apple Silicon (M1+). ⚡ Exports of gptq models to mlx also now possible. We have added mlx exported models to [huggingface.co/ModelCloud](https://huggingface.co/collections/ModelCloud/vortex-673743382af0a52b2a8b9fe2). 
⚡ lm_head quantization now fully support by GPTQModel without external pkg dependency.
🐛 Fixed `setup.py` not correctly detecting incompatible `setuptools`/`wheel` pkgs.


* [CI] run tests with linux tag by @CSY-ModelCloud in https://github.com/ModelCloud/GPTQModel/pull/1067
* Add backend.MLX by @LRL-ModelCloud in https://github.com/ModelCloud/GPTQModel/pull/1061
* add mlx generate test by @CL-ModelCloud in https://github.com/ModelCloud/GPTQModel/pull/1069
* [CI] upload source in build step by @CSY-ModelCloud in https://github.com/ModelCloud/GPTQModel/pull/1070
* code review by @CL-ModelCloud in https://github.com/ModelCloud/GPTQModel/pull/1072
* [CI] install mlx by @CSY-ModelCloud in https://github.com/ModelCloud/GPTQModel/pull/1071
* Add option to quantize `lm_head` by @ZX-ModelCloud in https://github.com/ModelCloud/GPTQModel/pull/1037
* fix test_packing by @LRL-ModelCloud in https://github.com/ModelCloud/GPTQModel/pull/1073
* [CI] add mlx test by @CSY-ModelCloud in https://github.com/ModelCloud/GPTQModel/pull/1074
* [CI] fix ci relase env name by @CSY-ModelCloud in https://github.com/ModelCloud/GPTQModel/pull/1078
* update mlx test by @CSY-ModelCloud in https://github.com/ModelCloud/GPTQModel/pull/1079
* convert to mlx support desc_act true by @LRL-ModelCloud in https://github.com/ModelCloud/GPTQModel/pull/1082
* [CI] add extra-index-url for pip install by @CSY-ModelCloud in https://github.com/ModelCloud/GPTQModel/pull/1083
* catch module error for setup.py by @CSY-ModelCloud in https://github.com/ModelCloud/GPTQModel/pull/1084

**Full Changelog**: https://github.com/ModelCloud/GPTQModel/compare/v1.6.1...v1.7.0

## v1.7.2 (2025-01-19)

## What's Changed

⚡Effective BPW (bits per weight) will now be logged during load(). 
⚡Reduce loading time on Intel Arc A770/B580 XPU by 3.3x. 
⚡Reduce memory usage in MLX conversion. 
🐛 Fix Marlin kernel auto-select not checking CUDA compute version.

* remove catching module error by @CSY-ModelCloud in https://github.com/ModelCloud/GPTQModel/pull/1088
* [FIX] monkey patch GPTQShuffle.convert_idx to use fixed convert_idx by @LRL-ModelCloud in https://github.com/ModelCloud/GPTQModel/pull/1090
* [FIX] monkey patch only once by @LRL-ModelCloud in https://github.com/ModelCloud/GPTQModel/pull/1091
* check CC >= 8 for marlin, fixed #1092 by @CSY-ModelCloud in https://github.com/ModelCloud/GPTQModel/pull/1093
* check compute capability for marlin in validate_device() by @CSY-ModelCloud in https://github.com/ModelCloud/GPTQModel/pull/1095
* torch get device with index of CUDA_VISIBLE_DEVICES, not value of it by @CSY-ModelCloud in https://github.com/ModelCloud/GPTQModel/pull/1096
* fix local model path & marlin test by @CSY-ModelCloud in https://github.com/ModelCloud/GPTQModel/pull/1097
* mod bits info by @CL-ModelCloud in https://github.com/ModelCloud/GPTQModel/pull/1100
* Reduce memory usage in mlx conversion by @Qubitium in https://github.com/ModelCloud/GPTQModel/pull/1099
* cleanup mlx code by @Qubitium in https://github.com/ModelCloud/GPTQModel/pull/1101


**Full Changelog**: https://github.com/ModelCloud/GPTQModel/compare/v1.7.0...v1.7.2

## v1.7.3 (2025-01-21)

## What's Changed

⚡ Telechat2 (China Telecom) model support
⚡ PhiMoE model support
🐛 Fix lm_head weights duplicated in post-quantize save() for models with tied-embedding.

* Add util.tensor_parameters() by @ZX-ModelCloud in https://github.com/ModelCloud/GPTQModel/pull/1107
* add require_dtype by @LRL-ModelCloud in https://github.com/ModelCloud/GPTQModel/pull/1109
* [MODEL] Add Telechat2 (China Telecom) by @1096125073 in https://github.com/ModelCloud/GPTQModel/pull/1106
* [FIX] Filter weight-sharing tensors when save by @ZX-ModelCloud in https://github.com/ModelCloud/GPTQModel/pull/1112
* Add telechat test by @LRL-ModelCloud in https://github.com/ModelCloud/GPTQModel/pull/1111
* [FIX] fix convert_gptq_to_mlx_weights by @LRL-ModelCloud in https://github.com/ModelCloud/GPTQModel/pull/1113
* add test_parameter_count.py by @ZX-ModelCloud in https://github.com/ModelCloud/GPTQModel/pull/1115
* Add gpqa eval task by @CL-ModelCloud in https://github.com/ModelCloud/GPTQModel/pull/1117
* [FIX] Call tied_weights() after load_checkpoint_in_model()  by @ZX-ModelCloud in https://github.com/ModelCloud/GPTQModel/pull/1119
* add phimoe support by @CSY-ModelCloud in https://github.com/ModelCloud/GPTQModel/pull/1118

## New Contributors
* @1096125073 made their first contribution in https://github.com/ModelCloud/GPTQModel/pull/1106

**Full Changelog**: https://github.com/ModelCloud/GPTQModel/compare/v1.7.2...v1.7.3

## v1.7.4 (2025-01-26)

## What's Changed
⚡ Faster `packing` for post-quantization model weight save. 
⚡ `Triton` kernel now validated for `Intel/XPU` when Intel Triton package is installed. 
⚡ New `compile()` api that allows torch to improve tps by ~4-8%. May need to disable flash_attention for some kernels.
🐛  Fix HF Transformers bug of downcasting fast tokenizer class on save.
🐛  Fix inaccurate `bpw` calculations. 
🐛  Fix `ROCm` compile with `setup.py` 

* Fix exllama slow pack() by @CSY-ModelCloud in https://github.com/ModelCloud/GPTQModel/pull/1128
* use optimized torch.round() codes by @CSY-ModelCloud in https://github.com/ModelCloud/GPTQModel/pull/1131
* fix shape mismatch for packing by @CSY-ModelCloud in https://github.com/ModelCloud/GPTQModel/pull/1132
* Speed up triton dequant by @Qubitium in https://github.com/ModelCloud/GPTQModel/pull/1136
* add torch compile with backend aot_ts by @CSY-ModelCloud in https://github.com/ModelCloud/GPTQModel/pull/1139
* disable sampling by @Qubitium in https://github.com/ModelCloud/GPTQModel/pull/1141
* mod triton-xpu by @CL-ModelCloud in https://github.com/ModelCloud/GPTQModel/pull/1135
* supress dynamo error by @CSY-ModelCloud in https://github.com/ModelCloud/GPTQModel/pull/1143
* fix bpw by @CL-ModelCloud in https://github.com/ModelCloud/GPTQModel/pull/1150
* [FIX] fix incorrectly saved the slow tokenizer by @LRL-ModelCloud in https://github.com/ModelCloud/GPTQModel/pull/1151
* Add mod chat by @CL-ModelCloud in https://github.com/ModelCloud/GPTQModel/pull/1154
* optimize pack by @Qubitium in https://github.com/ModelCloud/GPTQModel/pull/1153
* add quant time test by @CL-ModelCloud in https://github.com/ModelCloud/GPTQModel/pull/1155
* Export to hf model by @LRL-ModelCloud in https://github.com/ModelCloud/GPTQModel/pull/1157
* Fix bpw calculation by @Qubitium in https://github.com/ModelCloud/GPTQModel/pull/1163
* Inference speed test by @CL-ModelCloud in https://github.com/ModelCloud/GPTQModel/pull/1159

## New Contributors
* @isaranto made their first contribution in https://github.com/ModelCloud/GPTQModel/pull/1162

**Full Changelog**: https://github.com/ModelCloud/GPTQModel/compare/v1.7.3...v1.7.4

## v1.8.0 (2025-02-07)

## What's Changed

⚡ `DeekSeek v3/R1` model support. 
⚡  New flexible weight `packing`: allow quantized weights to be packed to `[int32, int16, int8]` dtypes. Triton and Torch kernels supports full range of new QuantizeConfig.pack_dtype.
⚡ New `auto_gc: bool` control in `quantize()` which can reduce quantization time for small model with no chance of oom. 
⚡ New `GPTQModel.push_to_hub() `api for easy quant model to HF repo. 
⚡ New `buffered_fwd: bool` control in model.quantize(). 
🐛 Fixed `bits=3` packing regression in v1.7.4.
🐛 Fixed Google Colab install requiring two install passes
🐛 Fixed Python 3.10 compatibility

* start 1.8.0-dev cycle by @Qubitium in https://github.com/ModelCloud/GPTQModel/pull/1168
* Flexible Pack DType by @Qubitium in https://github.com/ModelCloud/GPTQModel/pull/1158
* cuda needs to declare pack dtypes by @Qubitium in https://github.com/ModelCloud/GPTQModel/pull/1169
* fix pass pack dtype by @Qubitium in https://github.com/ModelCloud/GPTQModel/pull/1172
* Pass dtype by @Qubitium in https://github.com/ModelCloud/GPTQModel/pull/1173
* move in/out features and grop_size init to base by @Qubitium in https://github.com/ModelCloud/GPTQModel/pull/1174
* move self.maxq to base class by @Qubitium in https://github.com/ModelCloud/GPTQModel/pull/1175
* consolidate pack() into packer cls by @Qubitium in https://github.com/ModelCloud/GPTQModel/pull/1176
* Add `pack_dtype` to dynamic config and fix validate by @Qubitium in https://github.com/ModelCloud/GPTQModel/pull/1178
* format by @Qubitium in https://github.com/ModelCloud/GPTQModel/pull/1179
* Refract 4 by @Qubitium in https://github.com/ModelCloud/GPTQModel/pull/1180
* Refractor and simplify multi-kernel selection/init by @Qubitium in https://github.com/ModelCloud/GPTQModel/pull/1183
* Update/Refractor Bitblas/Marlin/Cuda by @Qubitium in https://github.com/ModelCloud/GPTQModel/pull/1184
* push bitblas logic down by @Qubitium in https://github.com/ModelCloud/GPTQModel/pull/1185
* Revert Bitblas to 0.0.1-dev13 by @Qubitium in https://github.com/ModelCloud/GPTQModel/pull/1186
* Do not export config.key if value is None by @Qubitium in https://github.com/ModelCloud/GPTQModel/pull/1187
* Fix examples/perplexity by @Qubitium in https://github.com/ModelCloud/GPTQModel/pull/1191
* [MODEL] add deepseek v3 support by @LRL-ModelCloud in https://github.com/ModelCloud/GPTQModel/pull/1127
* Push register buffer down to base class and rename all in/out features by @Qubitium in https://github.com/ModelCloud/GPTQModel/pull/1193
* Fix #1196 hf_transfer not accepting `max_memory` arg by @Qubitium in https://github.com/ModelCloud/GPTQModel/pull/1197
* reduce peak memory and reduce quant time by @Qubitium in https://github.com/ModelCloud/GPTQModel/pull/1198
* skip zero math by @Qubitium in https://github.com/ModelCloud/GPTQModel/pull/1199
* fix test_packing_speed by @Qubitium in https://github.com/ModelCloud/GPTQModel/pull/1202
* Update test_quant_time.py by @Qubitium in https://github.com/ModelCloud/GPTQModel/pull/1203
* experimental `buffered_fwd` quantize control by @Qubitium in https://github.com/ModelCloud/GPTQModel/pull/1205
* Fix dynamic regression on quant save by @Qubitium in https://github.com/ModelCloud/GPTQModel/pull/1208
* Python 3.10 type-hint compt bug by @Qubitium in https://github.com/ModelCloud/GPTQModel/pull/1213
* Fix colab install by @Qubitium in https://github.com/ModelCloud/GPTQModel/pull/1215
* add `GPTQModel.push_to_hub()` support by @Qubitium in https://github.com/ModelCloud/GPTQModel/pull/1216
* default to 8GB shard-size for model save by @Qubitium in https://github.com/ModelCloud/GPTQModel/pull/1217
* Auto gc toggle by @Qubitium in https://github.com/ModelCloud/GPTQModel/pull/1219
* fix 3bit packing and inference by @Qubitium in https://github.com/ModelCloud/GPTQModel/pull/1218


**Full Changelog**: https://github.com/ModelCloud/GPTQModel/compare/v1.7.4...v1.8.0

## v1.8.1 (2025-02-08)

## What's Changed

⚡ `DeekSeek v3/R1` model support. 
⚡  New flexible weight `packing`: allow quantized weights to be packed to `[int32, int16, int8]` dtypes. Triton and Torch kernels supports full range of new QuantizeConfig.pack_dtype.
⚡ Over 50% speedup for `vl` model quantization (Qwen 2.5-VL + Ovis)
⚡ New `auto_gc: bool` control in `quantize()` which can reduce quantization time for small model with no chance of oom. 
⚡ New `GPTQModel.push_to_hub() `api for easy quant model upload to HF repo. 
⚡ New `buffered_fwd: bool` control in model.quantize(). 
🐛 Fixed `bits=3` packing and `group_size=-1` regression in v1.7.4.
🐛 Fixed Google Colab install requiring two install passes
🐛 Fixed Python 3.10 compatibility

* Flexible Pack DType by @Qubitium in https://github.com/ModelCloud/GPTQModel/pull/1158
* cuda needs to declare pack dtypes by @Qubitium in https://github.com/ModelCloud/GPTQModel/pull/1169
* fix pass pack dtype by @Qubitium in https://github.com/ModelCloud/GPTQModel/pull/1172
* Pass dtype by @Qubitium in https://github.com/ModelCloud/GPTQModel/pull/1173
* move in/out features and grop_size init to base by @Qubitium in https://github.com/ModelCloud/GPTQModel/pull/1174
* move self.maxq to base class by @Qubitium in https://github.com/ModelCloud/GPTQModel/pull/1175
* consolidate pack() into packer cls by @Qubitium in https://github.com/ModelCloud/GPTQModel/pull/1176
* Add `pack_dtype` to dynamic config and fix validate by @Qubitium in https://github.com/ModelCloud/GPTQModel/pull/1178
* Refract 4 by @Qubitium in https://github.com/ModelCloud/GPTQModel/pull/1180
* Refractor and simplify multi-kernel selection/init by @Qubitium in https://github.com/ModelCloud/GPTQModel/pull/1183
* Update/Refractor Bitblas/Marlin/Cuda by @Qubitium in https://github.com/ModelCloud/GPTQModel/pull/1184
* push bitblas logic down by @Qubitium in https://github.com/ModelCloud/GPTQModel/pull/1185
* Revert Bitblas to 0.0.1-dev13 by @Qubitium in https://github.com/ModelCloud/GPTQModel/pull/1186
* Do not export config.key if value is None by @Qubitium in https://github.com/ModelCloud/GPTQModel/pull/1187
* Fix examples/perplexity by @Qubitium in https://github.com/ModelCloud/GPTQModel/pull/1191
* [MODEL] add deepseek v3 support by @LRL-ModelCloud in https://github.com/ModelCloud/GPTQModel/pull/1127
* Push register buffer down to base class and rename all in/out features by @Qubitium in https://github.com/ModelCloud/GPTQModel/pull/1193
* Fix #1196 hf_transfer not accepting `max_memory` arg by @Qubitium in https://github.com/ModelCloud/GPTQModel/pull/1197
* reduce peak memory and reduce quant time by @Qubitium in https://github.com/ModelCloud/GPTQModel/pull/1198
* skip zero math by @Qubitium in https://github.com/ModelCloud/GPTQModel/pull/1199
* fix test_packing_speed by @Qubitium in https://github.com/ModelCloud/GPTQModel/pull/1202
* Update test_quant_time.py by @Qubitium in https://github.com/ModelCloud/GPTQModel/pull/1203
* experimental `buffered_fwd` quantize control by @Qubitium in https://github.com/ModelCloud/GPTQModel/pull/1205
* Fix dynamic regression on quant save by @Qubitium in https://github.com/ModelCloud/GPTQModel/pull/1208
* Python 3.10 type-hint compt bug by @Qubitium in https://github.com/ModelCloud/GPTQModel/pull/1213
* Fix colab install by @Qubitium in https://github.com/ModelCloud/GPTQModel/pull/1215
* add `GPTQModel.push_to_hub()` support by @Qubitium in https://github.com/ModelCloud/GPTQModel/pull/1216
* default to 8GB shard-size for model save by @Qubitium in https://github.com/ModelCloud/GPTQModel/pull/1217
* Auto gc toggle by @Qubitium in https://github.com/ModelCloud/GPTQModel/pull/1219
* fix 3bit packing and inference by @Qubitium in https://github.com/ModelCloud/GPTQModel/pull/1218
* fix merge error by @CSY-ModelCloud in https://github.com/ModelCloud/GPTQModel/pull/1234
* fix var name by @CSY-ModelCloud in https://github.com/ModelCloud/GPTQModel/pull/1235
* fix visual llm slow forward by @LRL-ModelCloud in https://github.com/ModelCloud/GPTQModel/pull/1232

**Full Changelog**: https://github.com/ModelCloud/GPTQModel/compare/v1.7.4...v1.8.1


## v1.9.0 (2025-02-12)

## What's Changed

⚡ Offload tokenizer fixes to [Toke(n)icer](https://github.com/modelcloud/tokenicer) pkg. 
⚡ Optimized `lm_head` quant time and vram usage. 
⚡ Optimized `DeekSeek v3/R1` model quant vram usage. 
⚡ 3x speed-up for Torch kernel when using Pytorch >= 2.5.0 with model.compile(). 
⚡ New `calibration_dataset_concat_size` option to enable calibration data concat mode to mimic original GPTQ data packing strategy which may improve quant speed and accuracy for datasets like wikitext2.
🐛 Fixed Optimum compat and `XPU`/`IPEX` auto kernel selection regresion in v1.8.1


* Fix init arg order and `optimum` compat by @CSY-ModelCloud in https://github.com/ModelCloud/GPTQModel/pull/1240
* [FIX][Optimize] lm_head quantize by @ZX-ModelCloud in https://github.com/ModelCloud/GPTQModel/pull/1239
* [Model] [DeepSpeek] un-merge `gate_proj` and `up_proj`  by @LRL-ModelCloud in https://github.com/ModelCloud/GPTQModel/pull/1241
* Use Toke(n)icer by @CL-ModelCloud in https://github.com/ModelCloud/GPTQModel/pull/1242
https://github.com/ModelCloud/GPTQModel/pull/1244
* Add Tokenicer Test by @CL-ModelCloud in https://github.com/ModelCloud/GPTQModel/pull/1245
* prepare for 1.8.2 release by @Qubitium in https://github.com/ModelCloud/GPTQModel/pull/1243
* simplify calls to tokenicer by @CL-ModelCloud in https://github.com/ModelCloud/GPTQModel/pull/1246
* Update requirements.txt by @Qubitium in https://github.com/ModelCloud/GPTQModel/pull/1248
* fix trust_remote was lost by @CSY-ModelCloud in https://github.com/ModelCloud/GPTQModel/pull/1249
* fix trust_remote was lost by @CSY-ModelCloud in https://github.com/ModelCloud/GPTQModel/pull/1250
* prepare for 1.8.5 release by @Qubitium in https://github.com/ModelCloud/GPTQModel/pull/1251
* fix unit tests & tweak logic for selecting backends by @CSY-ModelCloud in https://github.com/ModelCloud/GPTQModel/pull/1253
* install tokenicer form git & do ruff by @CSY-ModelCloud in https://github.com/ModelCloud/GPTQModel/pull/1254
* fix k,v is not a dict by @CSY-ModelCloud in https://github.com/ModelCloud/GPTQModel/pull/1255
* fix not enough values to unpack (expected 2, got 1) by @CSY-ModelCloud in https://github.com/ModelCloud/GPTQModel/pull/1256
* fix sglang test requires numpy<2.0 by @CSY-ModelCloud in https://github.com/ModelCloud/GPTQModel/pull/1258
* fix ipex backend by @jiqing-feng in https://github.com/ModelCloud/GPTQModel/pull/1259
* ipex should be packable, reverted pr #1259 importer.py changes by @CSY-ModelCloud in https://github.com/ModelCloud/GPTQModel/pull/1260
* remove sentencepiece by @CSY-ModelCloud in https://github.com/ModelCloud/GPTQModel/pull/1261
* speed up torch dequantize by @Qubitium in https://github.com/ModelCloud/GPTQModel/pull/1262
* Add `calibration_dataset_concat_size` option/mode  by @LRL-ModelCloud in https://github.com/ModelCloud/GPTQModel/pull/1257
* add transformers test by @CSY-ModelCloud in https://github.com/ModelCloud/GPTQModel/pull/1264
* Add kernel torch.compile hook by @Qubitium in https://github.com/ModelCloud/GPTQModel/pull/1265
* [FIX]fix vl model prepare_dataset by @LRL-ModelCloud in https://github.com/ModelCloud/GPTQModel/pull/1266


**Full Changelog**: https://github.com/ModelCloud/GPTQModel/compare/v1.8.1...v1.9.0

## v2.0.0 (2025-03-03)

## What's Changed

🎉 GPTQ quantization internals are now broken into multiple stages (processes) for feature expansion. 
🎉 Synced Marlin kernel inference quality fix from upstream. Added MARLIN_FP16, lower-quality but faster backend. 
🎉 ModelScope support added. 
🎉 Logging and cli progress bar output has been revamped with sticky bottom progress. 
🎉 Added CI tests to track regression in kernel inference quality and sweep all bits/group_sizes. 
🎉 Delegate loggin/progressbar to [LogBar](https://github.com/modelcloud/logbar) pkg. 
🐛 Fix ROCm version auto detection in setup install.
🐛 Fixed generation_config.json save and load. 
🐛 Fixed Transformers v4.49.0 compat. Fixed compat of models without bos. 
🐛 Fixed group_size=-1 and bits=3 packing regression. 
🐛 Fixed Qwen 2.5 MoE regressions. 

* fix 3 bit packing regression， fixed #1278 by @CSY-ModelCloud in https://github.com/ModelCloud/GPTQModel/pull/1280
* Fix supported models list (syntax error) by @Forenche in https://github.com/ModelCloud/GPTQModel/pull/1281
* feat: load model from modelscope by @suluyana in https://github.com/ModelCloud/GPTQModel/pull/1283
* merge eval & utils.lm_eval by @CSY-ModelCloud in https://github.com/ModelCloud/GPTQModel/pull/1282
* fix modelscope import & tests by @CSY-ModelCloud in https://github.com/ModelCloud/GPTQModel/pull/1285
* allow passing model instance to evalplus & update tokenizer loading logics by @CSY-ModelCloud in https://github.com/ModelCloud/GPTQModel/pull/1284
* fix lm-eval & vllm check tokenizer type by @CSY-ModelCloud in https://github.com/ModelCloud/GPTQModel/pull/1287
* Fix `generation_config.json` not auto-saved by @Qubitium in https://github.com/ModelCloud/GPTQModel/pull/1292
* [SAVE] Save config files with empty state dict by @ZX-ModelCloud in https://github.com/ModelCloud/GPTQModel/pull/1293
* [SAVE] Save processor related config files by @ZX-ModelCloud in https://github.com/ModelCloud/GPTQModel/pull/1295
* fix wrong order of config save causing sharded tensors to be removed by @Qubitium in https://github.com/ModelCloud/GPTQModel/pull/1297
* [FIX] not pack when group_size=-1 by @ZX-ModelCloud in https://github.com/ModelCloud/GPTQModel/pull/1298
* cleanup marlin paths: marlin does conversion on `post_init` by @Qubitium in https://github.com/ModelCloud/GPTQModel/pull/1310
* bump tokenicer to v0.0.3 by @CSY-ModelCloud in https://github.com/ModelCloud/GPTQModel/pull/1308
* clean is_marlin_format for tests by @CSY-ModelCloud in https://github.com/ModelCloud/GPTQModel/pull/1311
* [CI] fix sglang test name & add status logs & remove exllama packing test by @CSY-ModelCloud in https://github.com/ModelCloud/GPTQModel/pull/1312
* skip v1 to v2 conversion for sym=True only kernels by @Qubitium in https://github.com/ModelCloud/GPTQModel/pull/1314
* bump tokenicer to 0.0.4 & remove FORMAT_FIELD_COMPAT_MARLIN by @CSY-ModelCloud in https://github.com/ModelCloud/GPTQModel/pull/1315
* revert is_marlin_format check by @CSY-ModelCloud in https://github.com/ModelCloud/GPTQModel/pull/1316
* Improve Marlin accuracy (default) but add `MARLIN_FP16` backend for faster with less-accuracy by @Qubitium in https://github.com/ModelCloud/GPTQModel/pull/1317
* marlin fp32 mode should also be enabled if kernel was selected due to… by @Qubitium in https://github.com/ModelCloud/GPTQModel/pull/1318
* refractor logger by @Qubitium in https://github.com/ModelCloud/GPTQModel/pull/1319
* fix typo by @Qubitium in https://github.com/ModelCloud/GPTQModel/pull/1320
* refractor logger and have progress bar sticky to bottom of cli by @Qubitium in https://github.com/ModelCloud/GPTQModel/pull/1322
* [CI] fix tokenicer upgraded transformers & install bitblas for test_save_quanted_model by @CSY-ModelCloud in https://github.com/ModelCloud/GPTQModel/pull/1321
* [CI] allow to select compiler server & move model test to correct dir by @CSY-ModelCloud in https://github.com/ModelCloud/GPTQModel/pull/1323
* fix bitblas loading regression by @Qubitium in https://github.com/ModelCloud/GPTQModel/pull/1324
* marlin fp16 warning missed check by @Qubitium in https://github.com/ModelCloud/GPTQModel/pull/1325
* fix custom logger overriding system level logger by @Qubitium in https://github.com/ModelCloud/GPTQModel/pull/1327
* fix progress bar for packing by @CSY-ModelCloud in https://github.com/ModelCloud/GPTQModel/pull/1326
* More log fixes by @Qubitium in https://github.com/ModelCloud/GPTQModel/pull/1328
* fix no backend when creating a quant linear by @CSY-ModelCloud in https://github.com/ModelCloud/GPTQModel/pull/1329
* use relative path instead of importing gptqmodel by @CSY-ModelCloud in https://github.com/ModelCloud/GPTQModel/pull/1331
* no need patch vllm now by @CSY-ModelCloud in https://github.com/ModelCloud/GPTQModel/pull/1332
* [CI] fix CI url by @CSY-ModelCloud in https://github.com/ModelCloud/GPTQModel/pull/1333
* fix oom by @CSY-ModelCloud in https://github.com/ModelCloud/GPTQModel/pull/1335
* add default value for backend, fix optimum doesn't pass it by @CSY-ModelCloud in https://github.com/ModelCloud/GPTQModel/pull/1334
* refractor pb and pb usage by @Qubitium in https://github.com/ModelCloud/GPTQModel/pull/1341
* fix generator has no length info by @CSY-ModelCloud in https://github.com/ModelCloud/GPTQModel/pull/1342
* replace utils.Progressbar with logbar by @CSY-ModelCloud in https://github.com/ModelCloud/GPTQModel/pull/1343
* [CI] update UI by @CSY-ModelCloud in https://github.com/ModelCloud/GPTQModel/pull/1344
* fix logbar api usage by @CSY-ModelCloud in https://github.com/ModelCloud/GPTQModel/pull/1345
* fix v2 to v1 missed logic bypass by @Qubitium in https://github.com/ModelCloud/GPTQModel/pull/1347
* [CI] fix xpu env has no logbar by @CSY-ModelCloud in https://github.com/ModelCloud/GPTQModel/pull/1346
* [CI] update runner ip env & fix show-statistics didn't run by @CSY-ModelCloud in https://github.com/ModelCloud/GPTQModel/pull/1348
* fix time was not imported by @CSY-ModelCloud in https://github.com/ModelCloud/GPTQModel/pull/1349
* update device-smi depend to v0.4.0 by @Qubitium in https://github.com/ModelCloud/GPTQModel/pull/1351
* [CI] install requirements.txt for m4 by @CSY-ModelCloud in https://github.com/ModelCloud/GPTQModel/pull/1352
* Exllama V1 is Packable by @ZX-ModelCloud in https://github.com/ModelCloud/GPTQModel/pull/1356
* [FIX] test_packable.py by @ZX-ModelCloud in https://github.com/ModelCloud/GPTQModel/pull/1357
* [setup] use torch.version.hip for rocm version check by @CSY-ModelCloud in https://github.com/ModelCloud/GPTQModel/pull/1360
* save/load peft lora by @Qubitium in https://github.com/ModelCloud/GPTQModel/pull/1358
* update device-smi to 0.4.1 for rocm fix by @Qubitium in https://github.com/ModelCloud/GPTQModel/pull/1362
* strip model path by @Qubitium in https://github.com/ModelCloud/GPTQModel/pull/1363
* [CI] exllama v1 kernel now eligible for quant stage by @Qubitium in https://github.com/ModelCloud/GPTQModel/pull/1364
* Fix transformers modeling code passing `input.shape[0] == 0` to nn.module by @Qubitium in https://github.com/ModelCloud/GPTQModel/pull/1365
* simplify log var by @Qubitium in https://github.com/ModelCloud/GPTQModel/pull/1368
* fix import by @CSY-ModelCloud in https://github.com/ModelCloud/GPTQModel/pull/1369
* update by @Qubitium in https://github.com/ModelCloud/GPTQModel/pull/1370

## New Contributors
* @Forenche made their first contribution in https://github.com/ModelCloud/GPTQModel/pull/1281
* @suluyana made their first contribution in https://github.com/ModelCloud/GPTQModel/pull/1283

**Full Changelog**: https://github.com/ModelCloud/GPTQModel/compare/v1.9.0...v2.0.0

## v2.1.0 (2025-03-13)

## What's Changed

✨ New QQQ quantization method and inference support! 
✨ New Google `Gemma 3` day-zero model support. 
✨ New Alibaba `Ovis 2` VL model support. 
✨ New AMD `Instella` day-zero model support. 
✨ New `GSM8K Platinum` and `MMLU-Pro` benchmarking suppport. 
✨ Peft Lora training with GPTQModel is now 30%+ faster on all gpu and IPEX devices. 
✨ Auto detect MoE modules not activated during quantization due to insufficient calibration data. 
✨ `ROCm` setup.py compat fixes. 
✨ Optimum and Peft compat fixes. 
✨ Fixed Peft bfloat16 training. 

* auto enable flash_attn only when flash-attn was installed by @CSY-ModelCloud in https://github.com/ModelCloud/GPTQModel/pull/1372
* Fix rocm compat by @Qubitium in https://github.com/ModelCloud/GPTQModel/pull/1373
* fix unnecessary mkdir by @CSY-ModelCloud in https://github.com/ModelCloud/GPTQModel/pull/1374
* add test_kernel_output_xpu.py by @CSY-ModelCloud in https://github.com/ModelCloud/GPTQModel/pull/1382
* clean test_kernel_output_xpu.py by @CSY-ModelCloud in https://github.com/ModelCloud/GPTQModel/pull/1383
* tremove xpu support of triton kernel by @Qubitium in https://github.com/ModelCloud/GPTQModel/pull/1384
* [MODEL] Add instella support by @LRL-ModelCloud in https://github.com/ModelCloud/GPTQModel/pull/1385
* Fix optimum/peft trainer integration by @CSY-ModelCloud in https://github.com/ModelCloud/GPTQModel/pull/1381
* rename peft test file by @CSY-ModelCloud in https://github.com/ModelCloud/GPTQModel/pull/1387
* [CI] fix wandb was not installed & update test_olora_finetuning_xpu.py by @CSY-ModelCloud in https://github.com/ModelCloud/GPTQModel/pull/1388
* Add lm-eval `GSM8k Platinum` by @Qubitium in https://github.com/ModelCloud/GPTQModel/pull/1394
* Remove cuda kernel by @Qubitium in https://github.com/ModelCloud/GPTQModel/pull/1396
* fix exllama kernels not compiled by @Qubitium in https://github.com/ModelCloud/GPTQModel/pull/1397
* update tests by @Qubitium in https://github.com/ModelCloud/GPTQModel/pull/1398
* make the kernel output validation more robust by @Qubitium in https://github.com/ModelCloud/GPTQModel/pull/1399
* speed up ci by @Qubitium in https://github.com/ModelCloud/GPTQModel/pull/1400
* add fwd counter by @yuchiwang in https://github.com/ModelCloud/GPTQModel/pull/1389
* allow triton and ipex to inherit torch kernel and use torch for train… by @Qubitium in https://github.com/ModelCloud/GPTQModel/pull/1401
* fix skip moe modules when fwd count is 0 by @Qubitium in https://github.com/ModelCloud/GPTQModel/pull/1404
* fix ipex linear post init for finetune by @jiqing-feng in https://github.com/ModelCloud/GPTQModel/pull/1406
* fix optimum compat by @Qubitium in https://github.com/ModelCloud/GPTQModel/pull/1408
* [Feature] Add mmlupro API by @CL-ModelCloud in https://github.com/ModelCloud/GPTQModel/pull/1405
* add training callback by @CSY-ModelCloud in https://github.com/ModelCloud/GPTQModel/pull/1409
* Fix bf16 training by @Qubitium in https://github.com/ModelCloud/GPTQModel/pull/1410
* fix bf16 forward for triton by @Qubitium in https://github.com/ModelCloud/GPTQModel/pull/1411
* Add QQQ by @Qubitium in https://github.com/ModelCloud/GPTQModel/pull/1402
* make IPEX or any kernel that uses Torch for Training to auto switch v… by @Qubitium in https://github.com/ModelCloud/GPTQModel/pull/1412
* [CI] xpu inference test by @CL-ModelCloud in https://github.com/ModelCloud/GPTQModel/pull/1380
* [FIX] qqq with eora by @ZX-ModelCloud in https://github.com/ModelCloud/GPTQModel/pull/1415
* [FIX] device error by @ZX-ModelCloud in https://github.com/ModelCloud/GPTQModel/pull/1417
* make quant linear expose internal buffers by @Qubitium in https://github.com/ModelCloud/GPTQModel/pull/1418
* Fix bfloat16 kernels by @Qubitium in https://github.com/ModelCloud/GPTQModel/pull/1420
* fix qqq bfloat16 forward by @Qubitium in https://github.com/ModelCloud/GPTQModel/pull/1423
* Fix ci10 by @Qubitium in https://github.com/ModelCloud/GPTQModel/pull/1424
* fix marlin bf16 compat by @Qubitium in https://github.com/ModelCloud/GPTQModel/pull/1427
* [CI] no need reinstall requirements by @CSY-ModelCloud in https://github.com/ModelCloud/GPTQModel/pull/1426
* [FIX] dynamic save error by @ZX-ModelCloud in https://github.com/ModelCloud/GPTQModel/pull/1428
* [FIX] super().post_init() calling order by @ZX-ModelCloud in https://github.com/ModelCloud/GPTQModel/pull/1431
* fix bitblas choose IPEX in cuda env by @CSY-ModelCloud in https://github.com/ModelCloud/GPTQModel/pull/1432
* Fix exllama is not packable by @Qubitium in https://github.com/ModelCloud/GPTQModel/pull/1433
* disable exllama for training by @Qubitium in https://github.com/ModelCloud/GPTQModel/pull/1435
* remove TritonV2QuantLinear for xpu test by @CSY-ModelCloud in https://github.com/ModelCloud/GPTQModel/pull/1436
* [MODEL] add gemma3 support by @LRL-ModelCloud in https://github.com/ModelCloud/GPTQModel/pull/1434
* fix the error when downloading models using modelscope by @mushenL in https://github.com/ModelCloud/GPTQModel/pull/1437
* Add QQQ Rotation by @ZX-ModelCloud in https://github.com/ModelCloud/GPTQModel/pull/1425
* fix no __init__.py by @CSY-ModelCloud in https://github.com/ModelCloud/GPTQModel/pull/1438
* Fix hardmard import by @Qubitium in https://github.com/ModelCloud/GPTQModel/pull/1441
* Eora final by @nbasyl in https://github.com/ModelCloud/GPTQModel/pull/1440
* triton is not validated for ipex by @Qubitium in https://github.com/ModelCloud/GPTQModel/pull/1445
* Fix exllama adapter by @Qubitium in https://github.com/ModelCloud/GPTQModel/pull/1446
* fix rocm compile by @Qubitium in https://github.com/ModelCloud/GPTQModel/pull/1447
* [FIX]  Correctly obtain the submodule's device by @ZX-ModelCloud in https://github.com/ModelCloud/GPTQModel/pull/1448
* fix rocm not compatible with exllama v2 and eora kernel by @Qubitium in https://github.com/ModelCloud/GPTQModel/pull/1449
* revert overflow code by @Qubitium in https://github.com/ModelCloud/GPTQModel/pull/1450
* add kernel dtype support and add full float15 vs bfloat16 kernel testing by @Qubitium in https://github.com/ModelCloud/GPTQModel/pull/1452
* [MODEL] add Ovis2 support and bug fix by @Fusionplay in https://github.com/ModelCloud/GPTQModel/pull/1454
* add unit test for ovis2 by @CSY-ModelCloud in https://github.com/ModelCloud/GPTQModel/pull/1456

## New Contributors
* @yuchiwang made their first contribution in https://github.com/ModelCloud/GPTQModel/pull/1389
* @mushenL made their first contribution in https://github.com/ModelCloud/GPTQModel/pull/1437
* @nbasyl made their first contribution in https://github.com/ModelCloud/GPTQModel/pull/1440
* @Fusionplay made their first contribution in https://github.com/ModelCloud/GPTQModel/pull/1454

**Full Changelog**: https://github.com/ModelCloud/GPTQModel/compare/v2.0.0...v2.1.0

## v2.2.0 (2025-04-03)

## What's Changed

✨ New Qwen 2.5 VL model support. Prelim Qwen 3 model support. 
✨ New samples log column during quantization to track module activation in MoE models. 
✨ Loss log column now color-coded to highlight modules that are friendly/resistant to quantization. 
✨ Progress (per-step) stats during quantization now streamed to log file. 
✨ Auto bfloat16 dtype loading for models based on model config. 
✨ Fix kernel compile for Pytorch/ROCm. 
✨ Slightly faster quantization and auto-resolve some low-level oom issues for smaller vram gpus.

* Enable ipex tests for CPU/XPU by @jiqing-feng in https://github.com/ModelCloud/GPTQModel/pull/1460
* test kernel accuracies with more shapes on cuda by @Qubitium in https://github.com/ModelCloud/GPTQModel/pull/1461
* Fix rocm flags by @Qubitium in https://github.com/ModelCloud/GPTQModel/pull/1467
* use table like logging format by @Qubitium in https://github.com/ModelCloud/GPTQModel/pull/1471
* stream process log entries to persistent file by @Qubitium in https://github.com/ModelCloud/GPTQModel/pull/1472
* fix some models need trust-remote-code arg by @Qubitium in https://github.com/ModelCloud/GPTQModel/pull/1474
* Fix wq dtype by @Qubitium in https://github.com/ModelCloud/GPTQModel/pull/1475
* add colors to quant loss column by @Qubitium in https://github.com/ModelCloud/GPTQModel/pull/1477
* add prelim qwen3 support by @Qubitium in https://github.com/ModelCloud/GPTQModel/pull/1478
* Update eora.py for further optimization by @nbasyl in https://github.com/ModelCloud/GPTQModel/pull/1488
* faster cholesky inverse and avoid oom when possible by @Qubitium in https://github.com/ModelCloud/GPTQModel/pull/1494
* [MODEL] supports qwen2_5_vl by @ZX-ModelCloud in https://github.com/ModelCloud/GPTQModel/pull/1493


**Full Changelog**: https://github.com/ModelCloud/GPTQModel/compare/v2.1.0...v2.2.0

## v3.0.0 (2025-04-14)


🎉 New ground-breaking `GPTQ v2` quantization option for improved model quantization accuracy validated by `GSM8K_PLATINUM` [benchmarks](https://github.com/ModelCloud/GPTQModel#quantization-using-gptq-v2) vs original gptq. 
✨ New `Phi4-MultiModal` model support. 
✨ New Nvidia `Nemotron Ultra` model support. 
✨ New `Dream` model support. New experimental multi-gpu quantization support. Reduced vram usage. Faster quantization.

## What's Changed
* Multi GPU Quantization by @Qubitium in https://github.com/ModelCloud/GPTQModel/pull/1502
* experimental multi-gpu quantization by @Qubitium in https://github.com/ModelCloud/GPTQModel/pull/1503
* reduce allocation by @Qubitium in https://github.com/ModelCloud/GPTQModel/pull/1504
* revert add_ by @Qubitium in https://github.com/ModelCloud/GPTQModel/pull/1506
* Switch to non-deprecated mlx.core.clear_cache() by @smpanaro in https://github.com/ModelCloud/GPTQModel/pull/1510
* Dream Model Support by @Qubitium in https://github.com/ModelCloud/GPTQModel/pull/1512
* fix disabling batch/mask for dream by @Qubitium in https://github.com/ModelCloud/GPTQModel/pull/1514
* reduce tensor device movement by @Qubitium in https://github.com/ModelCloud/GPTQModel/pull/1516
* fix deepseek v3 module order by @Qubitium in https://github.com/ModelCloud/GPTQModel/pull/1517
* Nemotron Ultra Support by @Qubitium in https://github.com/ModelCloud/GPTQModel/pull/1518
* faster process_batch by @Qubitium in https://github.com/ModelCloud/GPTQModel/pull/1519
* Fix missing arg due to recent `Processor` api changes by @Qubitium in https://github.com/ModelCloud/GPTQModel/pull/1523
* Fix gpt2 columns calculation by @Qubitium in https://github.com/ModelCloud/GPTQModel/pull/1524
* temp damper should not overwrite damp cfg by @Qubitium in https://github.com/ModelCloud/GPTQModel/pull/1526
* Replace module hooking with tree-defined targeting by @Qubitium in https://github.com/ModelCloud/GPTQModel/pull/1527
* Fix compat with XPU by @Qubitium in https://github.com/ModelCloud/GPTQModel/pull/1535
* Phi4 MultiModal by @Qubitium in https://github.com/ModelCloud/GPTQModel/pull/1511
* disable selection of ExllamaV2 kernel for group_size=16 for now by @Qubitium in https://github.com/ModelCloud/GPTQModel/pull/1537
* Add Gptqv2 by @yhhhli and @Qubitium in https://github.com/ModelCloud/GPTQModel/pull/1533

## New Contributors
* @smpanaro made their first contribution in https://github.com/ModelCloud/GPTQModel/pull/1510
* @yhhhli made their first contribution in https://github.com/ModelCloud/GPTQModel/pull/1533

**Full Changelog**: https://github.com/ModelCloud/GPTQModel/compare/v2.2.0...v3.0.0

## v4.0.0 (2025-08-22)

## Notable Changes


* Supprt add glm4 by @glide-the in https://github.com/ModelCloud/GPTQModel/pull/1559
* Add Xiaomi MiMo model by @Qubitium in https://github.com/ModelCloud/GPTQModel/pull/1571
* Free threading (GIL free) Quantization for Linear NxGPU scaling of Quantization by @Qubitium in https://github.com/ModelCloud/GPTQModel/pull/1581
* feat: add Qwen-Omni support. by @tiger-of-shawn in https://github.com/ModelCloud/GPTQModel/pull/1613
* add Qwen 2.5 Omni support by @Qubitium in https://github.com/ModelCloud/GPTQModel/pull/1615
* [MODEL] ERNIE4.5 by @LRL-ModelCloud in https://github.com/ModelCloud/GPTQModel/pull/1645
* [MODEL]support pangu_alpha model by @ZX-ModelCloud in https://github.com/ModelCloud/GPTQModel/pull/1646
* new baidu ernie & huawei pangu model support by @Qubitium in https://github.com/ModelCloud/GPTQModel/pull/1647
* [MODEL] Add falcon h1 support by @LRL-ModelCloud in https://github.com/ModelCloud/GPTQModel/pull/1621
* feat(gemma3): also support larger gemma3 models and not only small te… by @joennlae in https://github.com/ModelCloud/GPTQModel/pull/1627
* Add Group Aware Reordering (GAR) for Efficient Activation Reordering by @tgafni in https://github.com/ModelCloud/GPTQModel/pull/1656
* Enable pytorch fused op on XPU by @jiqing-feng in https://github.com/ModelCloud/GPTQModel/pull/1660
* [MODEL] Add Seed-OSS support by @LRL2-ModelCloud in https://github.com/ModelCloud/GPTQModel/pull/1702


## Other Changed
* [CI] add release source with github's vm by @CSY-ModelCloud in https://github.com/ModelCloud/GPTQModel/pull/1543
* Set format/method to string, enum by @Qubitium in https://github.com/ModelCloud/GPTQModel/pull/1546
* Fix rotation for tied embedding models by @smpanaro in https://github.com/ModelCloud/GPTQModel/pull/1550
* Fix missing import by @smpanaro in https://github.com/ModelCloud/GPTQModel/pull/1551
* Fix input processing for convolution by @Cecilwang in https://github.com/ModelCloud/GPTQModel/pull/1554
* [FIX] moe model quant division by zero issue by @LRL-ModelCloud in https://github.com/ModelCloud/GPTQModel/pull/1565
* [FIX] remove too short calib data by @LRL-ModelCloud in https://github.com/ModelCloud/GPTQModel/pull/1566
* Update qwen3 support by @Qubitium in https://github.com/ModelCloud/GPTQModel/pull/1567
* [FIX] hook_module and qwen3_moe by @LRL-ModelCloud in https://github.com/ModelCloud/GPTQModel/pull/1569
* [FIX] hook linear and triton by @LRL-ModelCloud in https://github.com/ModelCloud/GPTQModel/pull/1570
* [MISC] simplify model definition by @LRL-ModelCloud in https://github.com/ModelCloud/GPTQModel/pull/1572
* [FIX]qwen2 moe loop module by @LRL-ModelCloud in https://github.com/ModelCloud/GPTQModel/pull/1574
* Process threads by @Qubitium in https://github.com/ModelCloud/GPTQModel/pull/1576
* cleanup names by @Qubitium in https://github.com/ModelCloud/GPTQModel/pull/1578
* Api refractor by @Qubitium in https://github.com/ModelCloud/GPTQModel/pull/1579
* [CI] fix unit test was unable to run by @CSY-ModelCloud in https://github.com/ModelCloud/GPTQModel/pull/1580
* fix has_gil was not imported & device-smi api wrong by @CSY-ModelCloud in https://github.com/ModelCloud/GPTQModel/pull/1586
* Fix compat by @Qubitium in https://github.com/ModelCloud/GPTQModel/pull/1587
* fix older python didn't have EnumType by @CSY-ModelCloud in https://github.com/ModelCloud/GPTQModel/pull/1590
* allow hinv none to continue by @Qubitium in https://github.com/ModelCloud/GPTQModel/pull/1588
* [FIX] get_module_by_name_prefix by @LRL-ModelCloud in https://github.com/ModelCloud/GPTQModel/pull/1591
* [CI] update release CI, add torch 2.7.0 by @CSY-ModelCloud in https://github.com/ModelCloud/GPTQModel/pull/1592
* Update test_opt.py by @Qubitium in https://github.com/ModelCloud/GPTQModel/pull/1593
* remove bad test attributes by @Qubitium in https://github.com/ModelCloud/GPTQModel/pull/1594
* default damp way too low by @Qubitium in https://github.com/ModelCloud/GPTQModel/pull/1599
* FIX mult-gpu quant by @Qubitium in https://github.com/ModelCloud/GPTQModel/pull/1600
* Fix reset device next by @Qubitium in https://github.com/ModelCloud/GPTQModel/pull/1601
* fix reset by @Qubitium in https://github.com/ModelCloud/GPTQModel/pull/1602
* ctx should be target by @Qubitium in https://github.com/ModelCloud/GPTQModel/pull/1603
* fix qwen2-moe mlp.gate not quantized by @Qubitium in https://github.com/ModelCloud/GPTQModel/pull/1604
* disable streaming for now by @Qubitium in https://github.com/ModelCloud/GPTQModel/pull/1605
* disable streaming for now by @Qubitium in https://github.com/ModelCloud/GPTQModel/pull/1606
* addm falcon h1 notes by @Qubitium in https://github.com/ModelCloud/GPTQModel/pull/1622
* [FIX] Qwen2.5 vl quant by @LRL-ModelCloud in https://github.com/ModelCloud/GPTQModel/pull/1623

* Bump torch from 2.6.0 to 2.7.1 in /gptqmodel_ext/exllama_eora by @dependabot[bot] in https://github.com/ModelCloud/GPTQModel/pull/1628
* fix bug for device error by @kaixuanliu in https://github.com/ModelCloud/GPTQModel/pull/1631
* [FIX]config seq len by @LRL-ModelCloud in https://github.com/ModelCloud/GPTQModel/pull/1640
* gemma3 4B specific compat fix by @Qubitium in https://github.com/ModelCloud/GPTQModel/pull/1641
* register buffer for `wf_unsqueeze_zero` and `wf_unsqueeze_neg_one` to… by @kaixuanliu in https://github.com/ModelCloud/GPTQModel/pull/1642
* set_postfix is a tqdm function, no need anymore by @CSY-ModelCloud in https://github.com/ModelCloud/GPTQModel/pull/1643
* Alkali modified by @alkalimc in https://github.com/ModelCloud/GPTQModel/pull/1644

* fix exception to avoid memory issue by @jiqing-feng in https://github.com/ModelCloud/GPTQModel/pull/1679
* lm_head hooked by @Chunfei-He in https://github.com/ModelCloud/GPTQModel/pull/1673
* Bump the github-actions group across 1 directory with 2 updates by @dependabot[bot] in https://github.com/ModelCloud/GPTQModel/pull/1677
* fixed bugs when quantize lm_head by @528-dev in https://github.com/ModelCloud/GPTQModel/pull/1675
* Add gpt-neo model definition by @smpanaro in https://github.com/ModelCloud/GPTQModel/pull/1683
* Skip compile if MPS and < torch 2.8.0 by @smpanaro in https://github.com/ModelCloud/GPTQModel/pull/1684
* Model config.use_cache not correctly used during inference for some models by @LRL2-ModelCloud in https://github.com/ModelCloud/GPTQModel/pull/1686
* [FIX] transformers compat by @LRL2-ModelCloud in https://github.com/ModelCloud/GPTQModel/pull/1687
* Update module_looper.py by @LRL2-ModelCloud in https://github.com/ModelCloud/GPTQModel/pull/1690
* Update requirements.txt by @LRL2-ModelCloud in https://github.com/ModelCloud/GPTQModel/pull/1689
* Update version.py by @Qubitium in https://github.com/ModelCloud/GPTQModel/pull/1691
* add ACCEPT_USE_FLASH_ATTEN2_ARG by @LRL2-ModelCloud in https://github.com/ModelCloud/GPTQModel/pull/1693
* Fix kwarg vs pos arg hidden states by @LRL2-ModelCloud in https://github.com/ModelCloud/GPTQModel/pull/1694
* fix import Perplexity failed by @CSY-ModelCloud in https://github.com/ModelCloud/GPTQModel/pull/1695
* [CI] fix CI installed wrong libs' version by @CSY-ModelCloud in https://github.com/ModelCloud/GPTQModel/pull/1696
* [FIX] GIL Check by @ZX-ModelCloud in https://github.com/ModelCloud/GPTQModel/pull/1697
* [FIX] minicpm test by @LRL2-ModelCloud in https://github.com/ModelCloud/GPTQModel/pull/1698
* [FIX] use AutoModelForImageTextToText instead of AutoModelForVision2Seq by @ZX-ModelCloud in https://github.com/ModelCloud/GPTQModel/pull/1699
* [CI] change qwen2.5-omni model path by @ZX-ModelCloud in https://github.com/ModelCloud/GPTQModel/pull/1701
* [CI] install jieba for test_pangu_alpha by @CSY-ModelCloud in https://github.com/ModelCloud/GPTQModel/pull/1706
* disable torch.compile by @LRL2-ModelCloud in https://github.com/ModelCloud/GPTQModel/pull/1707
* FIX minicpm CI test by @LRL2-ModelCloud in https://github.com/ModelCloud/GPTQModel/pull/1708
* [CI] update torch for build by @CSY-ModelCloud in https://github.com/ModelCloud/GPTQModel/pull/1709
* [CI] update release matrix by @CSY-ModelCloud in https://github.com/ModelCloud/GPTQModel/pull/1710
* [CI] install torch compiled with cuda 126 by @CSY-ModelCloud in https://github.com/ModelCloud/GPTQModel/pull/1711
* use "attn_implementation" by @LRL2-ModelCloud in https://github.com/ModelCloud/GPTQModel/pull/1712
* prepare for 4.0.0 release by @Qubitium in https://github.com/ModelCloud/GPTQModel/pull/1704
* [CI] add 5090 support & install latest intel_extension_for_pytorch  by @CSY-ModelCloud in https://github.com/ModelCloud/GPTQModel/pull/1713
* [CI] don't compile 5090 for cuda < 12.8 by @CSY-ModelCloud in https://github.com/ModelCloud/GPTQModel/pull/1714
* [CI] Update unit test docker by @CSY-ModelCloud in https://github.com/ModelCloud/GPTQModel/pull/1715
* [CI] fix release ci by @CSY-ModelCloud in https://github.com/ModelCloud/GPTQModel/pull/1716
* fix model path is not public by @CSY-ModelCloud in https://github.com/ModelCloud/GPTQModel/pull/1720
* [CI] don't exit when package doesn't exist by @CSY-ModelCloud in https://github.com/ModelCloud/GPTQModel/pull/1719
* [CI] no need install logbar manually by @CSY-ModelCloud in https://github.com/ModelCloud/GPTQModel/pull/1721
* [CI] remove legacy tests & skip intel tests & disable flash_attn for some models by @CSY-ModelCloud in https://github.com/ModelCloud/GPTQModel/pull/1722
* [CI] no need install uv by @CSY-ModelCloud in https://github.com/ModelCloud/GPTQModel/pull/1723
* [CI] use new docker with uv binary to fix shim/uv didn't exist by @CSY-ModelCloud in https://github.com/ModelCloud/GPTQModel/pull/1724

## New Contributors
* @Cecilwang made their first contribution in https://github.com/ModelCloud/GPTQModel/pull/1554
* @glide-the made their first contribution in https://github.com/ModelCloud/GPTQModel/pull/1559
* @tiger-of-shawn made their first contribution in https://github.com/ModelCloud/GPTQModel/pull/1613
* @joennlae made their first contribution in https://github.com/ModelCloud/GPTQModel/pull/1627
* @kaixuanliu made their first contribution in https://github.com/ModelCloud/GPTQModel/pull/1631
* @alkalimc made their first contribution in https://github.com/ModelCloud/GPTQModel/pull/1644
* @tgafni made their first contribution in https://github.com/ModelCloud/GPTQModel/pull/1656
* @davedgd made their first contribution in https://github.com/ModelCloud/GPTQModel/pull/1664
* @Chunfei-He made their first contribution in https://github.com/ModelCloud/GPTQModel/pull/1673
* @528-dev made their first contribution in https://github.com/ModelCloud/GPTQModel/pull/1675
* @LRL2-ModelCloud made their first contribution in https://github.com/ModelCloud/GPTQModel/pull/1686

**Full Changelog**: https://github.com/ModelCloud/GPTQModel/compare/v3.0.0...v4.0.0

## v4.1.0 (2025-09-04)

# Notable Changes:

* Add a config option: mock_quantization to simplify heavy computations… by @avtc in https://github.com/ModelCloud/GPTQModel/pull/1731
* Add GLM-4.5-Air support by @avtc in https://github.com/ModelCloud/GPTQModel/pull/1730
* Add GPT-OSS support by @LRL2-ModelCloud in https://github.com/ModelCloud/GPTQModel/pull/1737
* Add LongCatFlashGPTQ by @LRL-ModelCloud in https://github.com/ModelCloud/GPTQModel/pull/1751
* Add Llama 4 Support by @Qubitium in https://github.com/ModelCloud/GPTQModel/pull/1508

## What's Changed
* Minor Cleanup by @Qubitium in https://github.com/ModelCloud/GPTQModel/pull/1718
* disable some compilation on torch 2.8 due to compat issues by @Qubitium in https://github.com/ModelCloud/GPTQModel/pull/1727
* add glm4 moe test by @LRL2-ModelCloud in https://github.com/ModelCloud/GPTQModel/pull/1734
* deprecate autoround by @Qubitium in https://github.com/ModelCloud/GPTQModel/pull/1735
* [FIX] test_kernel_output with XPU by @ZX-ModelCloud in https://github.com/ModelCloud/GPTQModel/pull/1741
* cleanup checks for GIL control, GIL=0, and python >= 3.13.3t by @Qubitium in https://github.com/ModelCloud/GPTQModel/pull/1743
* update torch/transformer depends by @Qubitium in https://github.com/ModelCloud/GPTQModel/pull/1749
* reduce pkg depend by @Qubitium in https://github.com/ModelCloud/GPTQModel/pull/1750
* fix triton compat check for 3.13.3t by @Qubitium in https://github.com/ModelCloud/GPTQModel/pull/1752
* Bump torch from 2.7.1 to 2.8.0 in /gptqmodel_ext/exllama_eora by @dependabot[bot] in https://github.com/ModelCloud/GPTQModel/pull/1755
* pkg update: tokenicer 0.0.5 by @Qubitium in https://github.com/ModelCloud/GPTQModel/pull/1756

## New Contributors
* @avtc made their first contribution in https://github.com/ModelCloud/GPTQModel/pull/1730

**Full Changelog**: https://github.com/ModelCloud/GPTQModel/compare/v4.0.0...v4.1.0

## v4.2.0 (2025-09-12)

## Notable Changes

* Add Qwen3-Next by @Qubitium and @LRL-ModelCloud in https://github.com/ModelCloud/GPTQModel/pull/1787
* Add Apertus support by @LRL-ModelCloud in https://github.com/ModelCloud/GPTQModel/pull/1767
* Add Kimi k2 support by @LRL-ModelCloud in https://github.com/ModelCloud/GPTQModel/pull/1768
* Add Klear support by @LRL-ModelCloud in https://github.com/ModelCloud/GPTQModel/pull/1769
* Add FastLLM support by @LRL-ModelCloud in https://github.com/ModelCloud/GPTQModel/pull/1771
* Add Nemotron H support by @LRL-ModelCloud in https://github.com/ModelCloud/GPTQModel/pull/1773
* Add `fail_safe` option by @LRL-ModelCloud in https://github.com/ModelCloud/GPTQModel/pull/1775
*  Use threading lock to protect unsafe tensor moves in multi-gpu by @Qubitium in https://github.com/ModelCloud/GPTQModel/pull/1778
* Avoid building experimental extensions to reduce wheel size by @Qubitium in https://github.com/ModelCloud/GPTQModel/pull/1763

## What's Changed
* Fix LlavaQwen2GPTQ by @LRL-ModelCloud in https://github.com/ModelCloud/GPTQModel/pull/1772
* Fix Q.to on multi-gpu gptq when proceeding fast and has many experts and gpus by @avtc in https://github.com/ModelCloud/GPTQModel/pull/1774
* Bump actions/setup-python from 5 to 6 in the github-actions group by @dependabot[bot] in https://github.com/ModelCloud/GPTQModel/pull/1758
* [CI] fix release jobs were skipped by @CSY-ModelCloud in https://github.com/ModelCloud/GPTQModel/pull/1759
* ignore compile warns about var declared but not used by @Qubitium in https://github.com/ModelCloud/GPTQModel/pull/1760
* allow prebuilt wheel path to be customized via env by @Qubitium in https://github.com/ModelCloud/GPTQModel/pull/1761
* add build toggles for all cpp kernels by @Qubitium in https://github.com/ModelCloud/GPTQModel/pull/1764
* fix multi gpu inference by @LRL-ModelCloud in https://github.com/ModelCloud/GPTQModel/pull/1762
* [CI] reduce wheel download size by @CSY-ModelCloud in https://github.com/ModelCloud/GPTQModel/pull/1765
* start 4.2.0-dev cycle by @Qubitium in https://github.com/ModelCloud/GPTQModel/pull/1766
* fix klear by @LRL-ModelCloud in https://github.com/ModelCloud/GPTQModel/pull/1770
* FIX transformers >= 4.56.1 force changed `torch.default_dtype` by @Qubitium in https://github.com/ModelCloud/GPTQModel/pull/1779
* fix multi gpu fail_safe by @LRL-ModelCloud in https://github.com/ModelCloud/GPTQModel/pull/1780
* fix device instance by @LRL-ModelCloud in https://github.com/ModelCloud/GPTQModel/pull/1783
* prepare for 4.2 release by @Qubitium in https://github.com/ModelCloud/GPTQModel/pull/1785


**Full Changelog**: https://github.com/ModelCloud/GPTQModel/compare/v4.1.0...v4.2.0

## v4.2.5 (2025-09-16)

## What's Changed
* Cleanup hyb_act by @Qubitium in https://github.com/ModelCloud/GPTQModel/pull/1791
* Remove torch import in setup.py by @Qubitium in https://github.com/ModelCloud/GPTQModel/pull/1729
* Refractor: rename `hyb_act` to `act_group_aware` by @Qubitium in https://github.com/ModelCloud/GPTQModel/pull/1794
* Cleanup by @Qubitium in https://github.com/ModelCloud/GPTQModel/pull/1795, https://github.com/ModelCloud/GPTQModel/pull/1796
* [CI] Add torch 2.8.0 by @CSY-ModelCloud in https://github.com/ModelCloud/GPTQModel/pull/1797
* [CI] torch-2.6.0+cu128-python-3.9 does not exist by @CSY-ModelCloud in https://github.com/ModelCloud/GPTQModel/pull/1798
* Fix wf_unsqueeze_zero and wf_unsqueeze_neg_one by @LRL-ModelCloud in https://github.com/ModelCloud/GPTQModel/pull/1799
* GAR field save to meta on quant save by @Qubitium in https://github.com/ModelCloud/GPTQModel/pull/1800
* Add pyproject.toml by @CSY-ModelCloud in https://github.com/ModelCloud/GPTQModel/pull/1801
* [CI] Don't detect arch list when it has already been set & fix build-system requirments by @CSY-ModelCloud in https://github.com/ModelCloud/GPTQModel/pull/1802


**Full Changelog**: https://github.com/ModelCloud/GPTQModel/compare/v4.2.0...v4.2.5

## v5.0.0 (2025-10-24)

## Notable Changes:

* New Data-parallel quant support for MoE models on multi-gpu using `nogil` Python (Python >= 3.13t with `PYTHON_GIL=0` env). 
* New `offload_to_disk` support enabled by default to massively reduce cpu ram usage. 
* New Intel optimized and Amd compatible `cpu` hw accelerated `TorchFused` kernel. 
* Packing stage is now 4x faster and now inlined with quantization. 
* Vram pressure for large models reduced during quantization. 
* `act_group_aware` is now 16k+ times faster and the default when `desc_act=False` for higher quality recovery without inference penalty of `desc_act=True`. 
* New beta quality AWQ support with full GEMM, GEMM_Fast, Marlin kernel support. 
* New LFM, Ling, Qwen3 Omni model support. 
* Bitblas kernel updated to support Bitblas 0.1.0.post1 reelase. 
* Quantization is now faster with reduced vram usage. Enhanced logging support with LogBar.
* And much much more...

## What's Changed
* rename `torch_dtype` to `dtype` to sync with hf transformers by @Qubitium in https://github.com/ModelCloud/GPTQModel/pull/1804
* drop support for python < 3.11 by @CSY-ModelCloud in https://github.com/ModelCloud/GPTQModel/pull/1805
* hard deprecated ipex in favor of torch_fused by @Qubitium in https://github.com/ModelCloud/GPTQModel/pull/1807
* update pyproject.toml by @CSY-ModelCloud in https://github.com/ModelCloud/GPTQModel/pull/1808
* [CI] release with 3.13t by @CSY-ModelCloud in https://github.com/ModelCloud/GPTQModel/pull/1811
* [QUANTIZATION] Add AWQ support by @ZX-ModelCloud in https://github.com/ModelCloud/GPTQModel/pull/1703
* find mapping by @LRL-ModelCloud in https://github.com/ModelCloud/GPTQModel/pull/1812
* Update README.md by @Qubitium in https://github.com/ModelCloud/GPTQModel/pull/1813
* Update version.py by @Qubitium in https://github.com/ModelCloud/GPTQModel/pull/1814
* Turtle in a half shell by @Qubitium in https://github.com/ModelCloud/GPTQModel/pull/1809
* note about memory saving by @Qubitium in https://github.com/ModelCloud/GPTQModel/pull/1817
* move fail_safe by @LRL-ModelCloud in https://github.com/ModelCloud/GPTQModel/pull/1818
* rename turtle method by @Qubitium in https://github.com/ModelCloud/GPTQModel/pull/1820
* add threads by @Qubitium in https://github.com/ModelCloud/GPTQModel/pull/1821
* remove AWQ mod defs by @ZX-ModelCloud in https://github.com/ModelCloud/GPTQModel/pull/1822
* [CI] use new docker by @CSY-ModelCloud in https://github.com/ModelCloud/GPTQModel/pull/1823
* Fix awq quantize by @LRL-ModelCloud in https://github.com/ModelCloud/GPTQModel/pull/1824
* [CI] use new docker for release source by @CSY-ModelCloud in https://github.com/ModelCloud/GPTQModel/pull/1825
* fix awq pack by @LRL-ModelCloud in https://github.com/ModelCloud/GPTQModel/pull/1826
* fix loading autoawq models and hf/vllm/sglang loading of newly awq qu… by @Qubitium in https://github.com/ModelCloud/GPTQModel/pull/1827
* wrong arg check by @Qubitium in https://github.com/ModelCloud/GPTQModel/pull/1828
* fix thread task var scoping by @Qubitium in https://github.com/ModelCloud/GPTQModel/pull/1829
* fix call param by @Qubitium in https://github.com/ModelCloud/GPTQModel/pull/1830
* fix threads > 1 not considered (unsafe) by @Qubitium in https://github.com/ModelCloud/GPTQModel/pull/1832
* cleanup by @Qubitium in https://github.com/ModelCloud/GPTQModel/pull/1833
* fix gptqmodel offload paths conflict by @Qubitium in https://github.com/ModelCloud/GPTQModel/pull/1834
* Ci test by @Qubitium in https://github.com/ModelCloud/GPTQModel/pull/1835
* eora: always diff in fp32 + cleanup by @Qubitium in https://github.com/ModelCloud/GPTQModel/pull/1836
* add register_buffer/parameter to NamedModule class by @Qubitium in https://github.com/ModelCloud/GPTQModel/pull/1837
* typo by @Qubitium in https://github.com/ModelCloud/GPTQModel/pull/1839
* add thread safety to all classes by @Qubitium in https://github.com/ModelCloud/GPTQModel/pull/1840
* fix fail_safe by @LRL-ModelCloud in https://github.com/ModelCloud/GPTQModel/pull/1844
* update marlin kernel by @ZX-ModelCloud in https://github.com/ModelCloud/GPTQModel/pull/1838
* fix fp32 reduce on/off by @Qubitium in https://github.com/ModelCloud/GPTQModel/pull/1845
* bypass marlin kernel bias issue by @Qubitium in https://github.com/ModelCloud/GPTQModel/pull/1846
* disable marlin atomics by default as it failed ci accuracy test by @Qubitium in https://github.com/ModelCloud/GPTQModel/pull/1847
* [FIX] awq marlin by @ZX-ModelCloud in https://github.com/ModelCloud/GPTQModel/pull/1816
* cleanup var names by @Qubitium in https://github.com/ModelCloud/GPTQModel/pull/1849
* pack per module by @LRL-ModelCloud in https://github.com/ModelCloud/GPTQModel/pull/1842
* [CI] use new docker by @CSY-ModelCloud in https://github.com/ModelCloud/GPTQModel/pull/1850
* tweak eora test by @Qubitium in https://github.com/ModelCloud/GPTQModel/pull/1851
* wait for thread tasks only when every module has completed. by @Qubitium in https://github.com/ModelCloud/GPTQModel/pull/1852
* [FIX] Compatible with vllm v0.10.2 by @ZX-ModelCloud in https://github.com/ModelCloud/GPTQModel/pull/1855
* move req.txt into toml by @CSY-ModelCloud in https://github.com/ModelCloud/GPTQModel/pull/1858
* do not create buffers only to overite them by @Qubitium in https://github.com/ModelCloud/GPTQModel/pull/1857
* pop states after use by @Qubitium in https://github.com/ModelCloud/GPTQModel/pull/1859
* [FIX] multiple "register_buffers" parameters by @ZX-ModelCloud in https://github.com/ModelCloud/GPTQModel/pull/1860
* Low memory pack by @Qubitium in https://github.com/ModelCloud/GPTQModel/pull/1861
* fix packing ci test by @Qubitium in https://github.com/ModelCloud/GPTQModel/pull/1862
* simplify by @Qubitium in https://github.com/ModelCloud/GPTQModel/pull/1853
* Fix 3bit packing regression in previous commit by @Qubitium in https://github.com/ModelCloud/GPTQModel/pull/1863
* remove deprecated `parallel_packing` property by @Qubitium in https://github.com/ModelCloud/GPTQModel/pull/1864
* Fix qqq quant/offloading by @Qubitium in https://github.com/ModelCloud/GPTQModel/pull/1866
* temp disable awq gemm kernel due to failing ci by @Qubitium in https://github.com/ModelCloud/GPTQModel/pull/1867
* update vllm compat by @Qubitium in https://github.com/ModelCloud/GPTQModel/pull/1869
* fix regression by @Qubitium in https://github.com/ModelCloud/GPTQModel/pull/1870
* fix setup.py crashed because torch may not support float8_e8m0fnu by @CSY-ModelCloud in https://github.com/ModelCloud/GPTQModel/pull/1871
* [FIX] AwqGEMMQuantLinear skip gptq_v1 convert to v2 by @ZX-ModelCloud in https://github.com/ModelCloud/GPTQModel/pull/1872
* Fix awq gemm auto kernel selection order by @Qubitium in https://github.com/ModelCloud/GPTQModel/pull/1873
* Update README.md by @Qubitium in https://github.com/ModelCloud/GPTQModel/pull/1874
* reduce forwarding to minimal by @Qubitium in https://github.com/ModelCloud/GPTQModel/pull/1876
* Update README.md by @Qubitium in https://github.com/ModelCloud/GPTQModel/pull/1877
* fix exllama tests by @Qubitium in https://github.com/ModelCloud/GPTQModel/pull/1879
* debug print all params/buffers by @Qubitium in https://github.com/ModelCloud/GPTQModel/pull/1880
* skip internal loading of non-pkg compatible quantization models, i.e.… by @Qubitium in https://github.com/ModelCloud/GPTQModel/pull/1881
* Loader by @Qubitium in https://github.com/ModelCloud/GPTQModel/pull/1882
* Cleanup awq by @Qubitium in https://github.com/ModelCloud/GPTQModel/pull/1883
* remove broken test by @Qubitium in https://github.com/ModelCloud/GPTQModel/pull/1884
* [CI] remove old cuda/torch support for release by @CSY-ModelCloud in https://github.com/ModelCloud/GPTQModel/pull/1885
* fix loader by @LRL-ModelCloud in https://github.com/ModelCloud/GPTQModel/pull/1886
* fix nvcc warnings about pending cuda > 13.x compat by @Qubitium in https://github.com/ModelCloud/GPTQModel/pull/1887
* fix packing speed test by @Qubitium in https://github.com/ModelCloud/GPTQModel/pull/1889
* fix licenses warning by @CSY-ModelCloud in https://github.com/ModelCloud/GPTQModel/pull/1888
* set licenses to apache by @CSY-ModelCloud in https://github.com/ModelCloud/GPTQModel/pull/1890
* [FIX] AwqGEMMQuantLinear should is PackableQuantLinear by @ZX-ModelCloud in https://github.com/ModelCloud/GPTQModel/pull/1891
* skip modules that have no parameters and no buffers since they can't be offloaded by @LRL-ModelCloud in https://github.com/ModelCloud/GPTQModel/pull/1892
* skip modules that have no parameters and no buffers since they can't offload by @LRL-ModelCloud in https://github.com/ModelCloud/GPTQModel/pull/1894
* Fix device check by @Qubitium in https://github.com/ModelCloud/GPTQModel/pull/1896
* [CI] disable test install by @CSY-ModelCloud in https://github.com/ModelCloud/GPTQModel/pull/1895
* remove hash feature by @Qubitium in https://github.com/ModelCloud/GPTQModel/pull/1897
* fix cuda ext cannot be loaded by @Qubitium in https://github.com/ModelCloud/GPTQModel/pull/1898
* lock numpy to 2.2.6 by @CSY-ModelCloud in https://github.com/ModelCloud/GPTQModel/pull/1899
* [FIX] test_lm_eval.py by @ZX-ModelCloud in https://github.com/ModelCloud/GPTQModel/pull/1900
* Patch fix model save by @Qubitium in https://github.com/ModelCloud/GPTQModel/pull/1901
* Ugly patch save 2 by @Qubitium in https://github.com/ModelCloud/GPTQModel/pull/1902
* fix potential leak by @Qubitium in https://github.com/ModelCloud/GPTQModel/pull/1904
* [FIX] test_integration by @ZX-ModelCloud in https://github.com/ModelCloud/GPTQModel/pull/1903
* fix build will uploaded a empty wheel by @CSY-ModelCloud in https://github.com/ModelCloud/GPTQModel/pull/1905
* fix lm_head quant by @LRL-ModelCloud in https://github.com/ModelCloud/GPTQModel/pull/1906
* batch tweaks by @Qubitium in https://github.com/ModelCloud/GPTQModel/pull/1907
* [FIX] test_kernel_output_torch_fused by @ZX-ModelCloud in https://github.com/ModelCloud/GPTQModel/pull/1908
* sync shell model with turtle before save by @Qubitium in https://github.com/ModelCloud/GPTQModel/pull/1910
* enable fail-safe mode for ci by @Qubitium in https://github.com/ModelCloud/GPTQModel/pull/1911
* fix batch code to ignore masked output by @Qubitium in https://github.com/ModelCloud/GPTQModel/pull/1912
* reduce memory with boolean masks by @Qubitium in https://github.com/ModelCloud/GPTQModel/pull/1913
* Potential fix for code scanning alert no. 17: Workflow does not contain permissions by @Qubitium in https://github.com/ModelCloud/GPTQModel/pull/1914
* fix cuda thread ctx by @Qubitium in https://github.com/ModelCloud/GPTQModel/pull/1915
* remove prev thread fix, replaced by main changes by @Qubitium in https://github.com/ModelCloud/GPTQModel/pull/1916
* diff colors per dtype/device by @Qubitium in https://github.com/ModelCloud/GPTQModel/pull/1917
* sync qqq init with super changes by @Qubitium in https://github.com/ModelCloud/GPTQModel/pull/1918
* remove auto-gc by @Qubitium in https://github.com/ModelCloud/GPTQModel/pull/1919
* remove buffered-fwd toggle by @Qubitium in https://github.com/ModelCloud/GPTQModel/pull/1920
* remove calibration_enable_gpu_cache toggle by @Qubitium in https://github.com/ModelCloud/GPTQModel/pull/1921
* fix use m_device derived since weight might not exists if module only… by @Qubitium in https://github.com/ModelCloud/GPTQModel/pull/1923
* [FIX] test_qqq with groupsize=-1 by @ZX-ModelCloud in https://github.com/ModelCloud/GPTQModel/pull/1922
* fix test_ppl by @LRL2-ModelCloud in https://github.com/ModelCloud/GPTQModel/pull/1926
* fix offload threading bug by @Qubitium in https://github.com/ModelCloud/GPTQModel/pull/1927
* [FIX] test_qqq with group_size=128 by @ZX-ModelCloud in https://github.com/ModelCloud/GPTQModel/pull/1925
* fix loading of og qqq quantized models on hf by @Qubitium in https://github.com/ModelCloud/GPTQModel/pull/1928
* Update README.md by @Qubitium in https://github.com/ModelCloud/GPTQModel/pull/1929
* fix inference mode not applied to threads by @Qubitium in https://github.com/ModelCloud/GPTQModel/pull/1930
* fix more thread tasks without proper ctx by @Qubitium in https://github.com/ModelCloud/GPTQModel/pull/1931
* fix eora compat by @Qubitium in https://github.com/ModelCloud/GPTQModel/pull/1932
* [FIX] calibration_dataset is empty by @ZX-ModelCloud in https://github.com/ModelCloud/GPTQModel/pull/1935
* add eora toggle to ci test by @Qubitium in https://github.com/ModelCloud/GPTQModel/pull/1934
* [FIX] test_serialization by @ZX-ModelCloud in https://github.com/ModelCloud/GPTQModel/pull/1936
* missing offload dealloc tracking by @Qubitium in https://github.com/ModelCloud/GPTQModel/pull/1937
* Update pyproject.toml by @Qubitium in https://github.com/ModelCloud/GPTQModel/pull/1938
* [FIX] QQQ quantize by @ZX-ModelCloud in https://github.com/ModelCloud/GPTQModel/pull/1940
* [FIX] gptqv2 by @ZX-ModelCloud in https://github.com/ModelCloud/GPTQModel/pull/1942
* Qwen3 omni moe support by @LRL2-ModelCloud in https://github.com/ModelCloud/GPTQModel/pull/1939
* Update README.md by @Qubitium in https://github.com/ModelCloud/GPTQModel/pull/1944
* Threadx by @Qubitium in https://github.com/ModelCloud/GPTQModel/pull/1945
* Fix thread pool bugs by @Qubitium in https://github.com/ModelCloud/GPTQModel/pull/1948
* update logbar depend version by @Qubitium in https://github.com/ModelCloud/GPTQModel/pull/1949
* [FIX] qwen2_5_vl by @ZX-ModelCloud in https://github.com/ModelCloud/GPTQModel/pull/1946
* Data Parallel by @Qubitium in https://github.com/ModelCloud/GPTQModel/pull/1950
* Fix auto gc thread not blocking on idle by @Qubitium in https://github.com/ModelCloud/GPTQModel/pull/1952
* Fix qwen3 omni by @LRL2-ModelCloud in https://github.com/ModelCloud/GPTQModel/pull/1951
* [FIX] bitblas by @ZX-ModelCloud in https://github.com/ModelCloud/GPTQModel/pull/1953
* Directly save meta files to disk on model save by @Qubitium in https://github.com/ModelCloud/GPTQModel/pull/1954
* Bypass accelerate by @Qubitium in https://github.com/ModelCloud/GPTQModel/pull/1955
* use tf32 ctx by @Qubitium in https://github.com/ModelCloud/GPTQModel/pull/1956
* awq fixes by @Qubitium in https://github.com/ModelCloud/GPTQModel/pull/1957
* fix turtle model not ready when looper starts by @Qubitium in https://github.com/ModelCloud/GPTQModel/pull/1958
* remove unused named_module.target_device_stream and preprocess_stream… by @Qubitium in https://github.com/ModelCloud/GPTQModel/pull/1959
* revert: stream properties cannot be pickled by @Qubitium in https://github.com/ModelCloud/GPTQModel/pull/1960
* Replicate + Turtle state fix by @Qubitium in https://github.com/ModelCloud/GPTQModel/pull/1961
* fix ctx for convert v1-v2 v2-v1 using in_place tensor mutation by @Qubitium in https://github.com/ModelCloud/GPTQModel/pull/1962
* Fix q to by @Qubitium in https://github.com/ModelCloud/GPTQModel/pull/1963
* FIx device memory usage: use device-smi `metrics` api by @Qubitium in https://github.com/ModelCloud/GPTQModel/pull/1964
* marlin atomics should be disabled by default by @Qubitium in https://github.com/ModelCloud/GPTQModel/pull/1965
* Update pyproject.toml by @Qubitium in https://github.com/ModelCloud/GPTQModel/pull/1967
* Fix pad tokens passed to quantization capture by @Qubitium in https://github.com/ModelCloud/GPTQModel/pull/1968
* Fix Python 3.14t compat and Marlin with Cuda 13.0 by @Qubitium in https://github.com/ModelCloud/GPTQModel/pull/1969
* auto switch cuda toolkit script for multiple venv with multiple torch… by @Qubitium in https://github.com/ModelCloud/GPTQModel/pull/1970
* FIX v2 to v1 conversion regression in latest refractors by @Qubitium in https://github.com/ModelCloud/GPTQModel/pull/1972
* Fix act_group_aware accuracy by using stable argsort by @Qubitium in https://github.com/ModelCloud/GPTQModel/pull/1973
* AWQ register_buffers: bool incorrectly passed by @Qubitium in https://github.com/ModelCloud/GPTQModel/pull/1974
* update bitblas kernel by @Qubitium in https://github.com/ModelCloud/GPTQModel/pull/1975
* fix tf32 on/off regression by @Qubitium in https://github.com/ModelCloud/GPTQModel/pull/1978
* fix thread safety for all torch.linalg and reuse ThreadSafe  by @Qubitium in https://github.com/ModelCloud/GPTQModel/pull/1979
* fix opt/qwen2.5/3 omni compat by @Qubitium in https://github.com/ModelCloud/GPTQModel/pull/1980
* Add OVIS 2.5 Support by @Qubitium in https://github.com/ModelCloud/GPTQModel/pull/1981
* Fix missing file by @Qubitium in https://github.com/ModelCloud/GPTQModel/pull/1983
* Fix replicate is not thread safe by @Qubitium in https://github.com/ModelCloud/GPTQModel/pull/1984
* Better progress bar by @Qubitium in https://github.com/ModelCloud/GPTQModel/pull/1985
* Fix missing memory release on cuda:0 by @Qubitium in https://github.com/ModelCloud/GPTQModel/pull/1986
* Use merged safetensors instead of multiple .dat files by @Qubitium in https://github.com/ModelCloud/GPTQModel/pull/1987
* fix transformers 4.57.0 compat by @Qubitium in https://github.com/ModelCloud/GPTQModel/pull/1989
* Replicate safety by @Qubitium in https://github.com/ModelCloud/GPTQModel/pull/1988
* missing upload by @Qubitium in https://github.com/ModelCloud/GPTQModel/pull/1990
* Fix tranformer backward compat by @Qubitium in https://github.com/ModelCloud/GPTQModel/pull/1991
* Fix Ovis regression by @Qubitium in https://github.com/ModelCloud/GPTQModel/pull/1992
* Logbar 0.1.0 by @Qubitium in https://github.com/ModelCloud/GPTQModel/pull/1993
* use logbar 0.1.1 with external log/pb conflict resolution by @Qubitium in https://github.com/ModelCloud/GPTQModel/pull/1994
* Bug fixes by @Qubitium in https://github.com/ModelCloud/GPTQModel/pull/1995
* Experimental groupsize 256, 512, 1024 for torch/triton kernel by @Qubitium in https://github.com/ModelCloud/GPTQModel/pull/1996
* Cleanup by @Qubitium in https://github.com/ModelCloud/GPTQModel/pull/1997
* add ling/ring support by @LRL2-ModelCloud in https://github.com/ModelCloud/GPTQModel/pull/2001
* [FIX] bitblas inference by @ZX-ModelCloud in https://github.com/ModelCloud/GPTQModel/pull/2002
* enable cpu torch fused op by @jiqing-feng in https://github.com/ModelCloud/GPTQModel/pull/2000
* Fix LING by @LRL2-ModelCloud in https://github.com/ModelCloud/GPTQModel/pull/2003
* [FIX] qqq quantize by @ZX-ModelCloud in https://github.com/ModelCloud/GPTQModel/pull/2005
* [FIX] gptq v2 quantize by @ZX-ModelCloud in https://github.com/ModelCloud/GPTQModel/pull/2006
* Make Torch kernel optimistically use triton dequant for 3.3x improvement by @Qubitium in https://github.com/ModelCloud/GPTQModel/pull/2007
* Fix model test model loading by @Qubitium in https://github.com/ModelCloud/GPTQModel/pull/2008
* use pypcre by @Qubitium in https://github.com/ModelCloud/GPTQModel/pull/2010
* [FIX] Add triton code for awq gemm by @ZX-ModelCloud in https://github.com/ModelCloud/GPTQModel/pull/2011
* Add lfm2 support by @LRL2-ModelCloud in https://github.com/ModelCloud/GPTQModel/pull/2012
* Update requirements.txt by @Qubitium in https://github.com/ModelCloud/GPTQModel/pull/2013
* Turtle pool by @Qubitium in https://github.com/ModelCloud/GPTQModel/pull/2009
* Fix race in threadpoolctl, bug in troch_sync helper by @Qubitium in https://github.com/ModelCloud/GPTQModel/pull/2014
* Torch replicate segfaults so let's default to simple copy by @Qubitium in https://github.com/ModelCloud/GPTQModel/pull/2015
* correctly report the actual kernel names by @Qubitium in https://github.com/ModelCloud/GPTQModel/pull/2016
* fix missing git add by @Qubitium in https://github.com/ModelCloud/GPTQModel/pull/2017
* [FIX] test with transformers/optimum/peft by @ZX-ModelCloud in https://github.com/ModelCloud/GPTQModel/pull/2018
* Fix multi gpu regression by @Qubitium in https://github.com/ModelCloud/GPTQModel/pull/2019
* Fix marlin kernel compiler warnings by @Qubitium in https://github.com/ModelCloud/GPTQModel/pull/2020
* Replicate by @Qubitium in https://github.com/ModelCloud/GPTQModel/pull/2021
* replicate still unsafe to use by @Qubitium in https://github.com/ModelCloud/GPTQModel/pull/2022
* Fix pack block by @Qubitium in https://github.com/ModelCloud/GPTQModel/pull/2023
* update scores by @Qubitium in https://github.com/ModelCloud/GPTQModel/pull/2024
* make act_group_aware default true by @Qubitium in https://github.com/ModelCloud/GPTQModel/pull/2025
* Make sure packer is part of dist by @Qubitium in https://github.com/ModelCloud/GPTQModel/pull/2026
* fix test by @LRL2-ModelCloud in https://github.com/ModelCloud/GPTQModel/pull/2028
* fix test_qzero_offsets by @LRL2-ModelCloud in https://github.com/ModelCloud/GPTQModel/pull/2029
* fix test_ppl by @LRL2-ModelCloud in https://github.com/ModelCloud/GPTQModel/pull/2030
* [FIX] unit test  and Adapted to mlx-lm 0.28.2 by @ZX-ModelCloud in https://github.com/ModelCloud/GPTQModel/pull/2031
* Fix attn mask ci test by @Qubitium in https://github.com/ModelCloud/GPTQModel/pull/2034
* Eora fix by @Qubitium in https://github.com/ModelCloud/GPTQModel/pull/2033
* remove logger board by @Qubitium in https://github.com/ModelCloud/GPTQModel/pull/2035
* Add Tensor Parallel optimized weight processor by @Qubitium in https://github.com/ModelCloud/GPTQModel/pull/2036
* safety check before cpp call by @Qubitium in https://github.com/ModelCloud/GPTQModel/pull/2037
* Use replicate by @Qubitium in https://github.com/ModelCloud/GPTQModel/pull/2038
* Tests by @Qubitium in https://github.com/ModelCloud/GPTQModel/pull/2039
* Fix qwen3 moe by @Qubitium in https://github.com/ModelCloud/GPTQModel/pull/2040
* fix test_dynamic by @LRL2-ModelCloud in https://github.com/ModelCloud/GPTQModel/pull/2041
* [FIX] unittest  test_packable / test_multi_gpu_inference / test_parameter_count by @ZX-ModelCloud in https://github.com/ModelCloud/GPTQModel/pull/2043
* Use spinner  by @Qubitium in https://github.com/ModelCloud/GPTQModel/pull/2042
* Memory fix by @Qubitium in https://github.com/ModelCloud/GPTQModel/pull/2045
* don't log batch values if batch is not enabled by @LRL2-ModelCloud in https://github.com/ModelCloud/GPTQModel/pull/2044
* optimize eora for multi-gpu and memory usage by @Qubitium in https://github.com/ModelCloud/GPTQModel/pull/2046
* Remove broken streams by @Qubitium in https://github.com/ModelCloud/GPTQModel/pull/2048
* Scores by @Qubitium in https://github.com/ModelCloud/GPTQModel/pull/2049
* [FIX] awq_moe by @ZX-ModelCloud in https://github.com/ModelCloud/GPTQModel/pull/2047
* Fix packing module scaling due to incorrect shared locking by @Qubitium in https://github.com/ModelCloud/GPTQModel/pull/2050
* [FIX] test_gptqv2, use original process_batch by @ZX-ModelCloud in https://github.com/ModelCloud/GPTQModel/pull/2051
* XIELUActivation will use some weights when activation init, so can't … by @LRL2-ModelCloud in https://github.com/ModelCloud/GPTQModel/pull/2052
* Stream quantized tensors by @Qubitium in https://github.com/ModelCloud/GPTQModel/pull/2053
* Fix offload false by @LRL2-ModelCloud in https://github.com/ModelCloud/GPTQModel/pull/2054
* Fix multi-gpu accumulation drift vs single gpu by @Qubitium in https://github.com/ModelCloud/GPTQModel/pull/2055
* nogil patch safetensors/triton by @Qubitium in https://github.com/ModelCloud/GPTQModel/pull/2056
* Update Tests by @Qubitium in https://github.com/ModelCloud/GPTQModel/pull/2059
* Fix streaming mem corruption by @Qubitium in https://github.com/ModelCloud/GPTQModel/pull/2060
* Fix streaming vram regression by @Qubitium in https://github.com/ModelCloud/GPTQModel/pull/2061
* Fix glm def by @Qubitium in https://github.com/ModelCloud/GPTQModel/pull/2062
* build whls for last 2 versions of pytorch and from py 3.10 to 3.14 by @Qubitium in https://github.com/ModelCloud/GPTQModel/pull/2063
* Fix setup by @Qubitium in https://github.com/ModelCloud/GPTQModel/pull/2064
* fix setup warnings by @Qubitium in https://github.com/ModelCloud/GPTQModel/pull/2065
* cleanup by @Qubitium in https://github.com/ModelCloud/GPTQModel/pull/2066
* [CI] remove py 3.14t by @CSY-ModelCloud in https://github.com/ModelCloud/GPTQModel/pull/2067
* [CI] update CI runner's ip by @CSY-ModelCloud in https://github.com/ModelCloud/GPTQModel/pull/2068
* lock parent by @Qubitium in https://github.com/ModelCloud/GPTQModel/pull/2069
* merge locking code by @Qubitium in https://github.com/ModelCloud/GPTQModel/pull/2070
* [CI] fold long logs & install tabulate by @CSY-ModelCloud in https://github.com/ModelCloud/GPTQModel/pull/2071
* Cleanup4 by @Qubitium in https://github.com/ModelCloud/GPTQModel/pull/2073
* [CI] fold release job's long logs by @CSY-ModelCloud in https://github.com/ModelCloud/GPTQModel/pull/2072
* [FIX] qwen vl quantize by @ZX-ModelCloud in https://github.com/ModelCloud/GPTQModel/pull/2075
* Fix multi-gpu loading of quantized model by @Qubitium in https://github.com/ModelCloud/GPTQModel/pull/2076
* [CI] remove unsupported versions by @CSY-ModelCloud in https://github.com/ModelCloud/GPTQModel/pull/2077
* [CI] use new docker image for CI by @CSY-ModelCloud in https://github.com/ModelCloud/GPTQModel/pull/2078
* remove unused 'debug' by @LRL2-ModelCloud in https://github.com/ModelCloud/GPTQModel/pull/2080
* [FIX] test_benchmark_gar / test_bits / test_dynamic by @ZX-ModelCloud in https://github.com/ModelCloud/GPTQModel/pull/2083
* Machete by @Qubitium in https://github.com/ModelCloud/GPTQModel/pull/2082
* allow py3.10 by @Qubitium in https://github.com/ModelCloud/GPTQModel/pull/2084
* fix nm-calibration dataset path by @CSY-ModelCloud in https://github.com/ModelCloud/GPTQModel/pull/2079
* Fix setup/cutlass was not installed & checkout dir doesn't exist by @CSY-ModelCloud in https://github.com/ModelCloud/GPTQModel/pull/2085
* device_map need {device_type:device_index} by @LRL2-ModelCloud in https://github.com/ModelCloud/GPTQModel/pull/2086
* [FIX] test_eval by @ZX-ModelCloud in https://github.com/ModelCloud/GPTQModel/pull/2087
* fix cutlass path by @Qubitium in https://github.com/ModelCloud/GPTQModel/pull/2088
* fix nvcc spawning too many threads by @Qubitium in https://github.com/ModelCloud/GPTQModel/pull/2090
* fix nvcc compiler warning by @Qubitium in https://github.com/ModelCloud/GPTQModel/pull/2091
* [CI] add python 3.14t to release  by @CSY-ModelCloud in https://github.com/ModelCloud/GPTQModel/pull/2089
* Temporally fix so files were not included in wheel by @CSY-ModelCloud in https://github.com/ModelCloud/GPTQModel/pull/2093
* Update README with python3-dev and ninja requirements by @Qubitium in https://github.com/ModelCloud/GPTQModel/pull/2094
* disable machete by @Qubitium in https://github.com/ModelCloud/GPTQModel/pull/2095
* [FIX] torch_fused on CPU by @ZX-ModelCloud in https://github.com/ModelCloud/GPTQModel/pull/2096
* [FIX] test_inference_speed by @ZX-ModelCloud in https://github.com/ModelCloud/GPTQModel/pull/2097
* Notes by @Qubitium in https://github.com/ModelCloud/GPTQModel/pull/2098
* fix setup license prop by @Qubitium in https://github.com/ModelCloud/GPTQModel/pull/2099
* fix transformers 4.57.1 breaking torchao compat by @Qubitium in https://github.com/ModelCloud/GPTQModel/pull/2100
* bitblas has strange compat issues with pip nvidia libs by @Qubitium in https://github.com/ModelCloud/GPTQModel/pull/2101
* note bitblas update by @Qubitium in https://github.com/ModelCloud/GPTQModel/pull/2102
* it is normal for some awq layers do not have err_loss info by @Qubitium in https://github.com/ModelCloud/GPTQModel/pull/2103
* fix threadx failing ci by @Qubitium in https://github.com/ModelCloud/GPTQModel/pull/2104
* Omni test by @Qubitium in https://github.com/ModelCloud/GPTQModel/pull/2105
* [CI] check wheel size by @CSY-ModelCloud in https://github.com/ModelCloud/GPTQModel/pull/2106
* Bump version from 5.0.0-dev0 to 5.0.0 by @Qubitium in https://github.com/ModelCloud/GPTQModel/pull/2107


**Full Changelog**: https://github.com/ModelCloud/GPTQModel/compare/v4.2.5...v5.0.0

## v5.2.0 (2025-11-02)

# Notable Changes:

* Minimax M2, Granite Nano, Qwen3-VL, Brumpy model support
* `AWQ` quantization now out of beta and now fully integrated into life cycle
*  New `VramStrategy.Balanced` property to spread `MoE` modules  to different gpus
* New pure torch AWQ kernel
* New `calibration_concat_separator` property
* Fixed HF bug that did not save `mtp` layers for GLM 4.5/4.6 (air) models. 
* Fixed multi-gpu cuda asserts due to stream/sync 

## What's Changed
* try not adding mem guards for marlin kernel launch protection by @Qubitium in https://github.com/ModelCloud/GPTQModel/*pull/2108
* MoE vram by @Qubitium in https://github.com/ModelCloud/GPTQModel/pull/2110
* Fix GLM 4.5/4.6 and AIr not saving mtp layer after save (HF bug) by @LRL2-ModelCloud in https://github.com/ModelCloud/GPTQModel/pull/2109
* torchao 0.14.1 update by @Qubitium in https://github.com/ModelCloud/GPTQModel/pull/2111
* Test refractor by @Qubitium in https://github.com/ModelCloud/GPTQModel/pull/2113
* Bump the github-actions group with 2 updates by @dependabot[bot] in https://github.com/ModelCloud/GPTQModel/pull/2120
* [FIX] xpu unit test by @ZX-ModelCloud in https://github.com/ModelCloud/GPTQModel/pull/2122
* modular by @Qubitium in https://github.com/ModelCloud/GPTQModel/pull/2123
* update scores by @Qubitium in https://github.com/ModelCloud/GPTQModel/pull/2124
* Fp8 dequant by @Qubitium in https://github.com/ModelCloud/GPTQModel/pull/2125
* Model dequant by @Qubitium in https://github.com/ModelCloud/GPTQModel/pull/2126
* Fp4 e2m1 by @Qubitium in https://github.com/ModelCloud/GPTQModel/pull/2127
* [FIX] ovis2, compatible with transformers v4.57.1 by @ZX-ModelCloud in https://github.com/ModelCloud/GPTQModel/pull/2129
* fix cols padding by @LRL2-ModelCloud in https://github.com/ModelCloud/GPTQModel/pull/2130
* [FIX] ovis_1_6 quantization by @ZX-ModelCloud in https://github.com/ModelCloud/GPTQModel/pull/2131
* Minimax m2 by @Qubitium in https://github.com/ModelCloud/GPTQModel/pull/2128
* Fix awq marlin kernel for bf16 by @Qubitium in https://github.com/ModelCloud/GPTQModel/pull/2135
* [FIX] incorrect AWQ NODES by @ZX-ModelCloud in https://github.com/ModelCloud/GPTQModel/pull/2133
* add support_offload_to_disk check by @LRL2-ModelCloud in https://github.com/ModelCloud/GPTQModel/pull/2134
* Add Awq torch kernel by @Qubitium in https://github.com/ModelCloud/GPTQModel/pull/2137
* Marin by @Qubitium in https://github.com/ModelCloud/GPTQModel/pull/2139
* Marin scores by @Qubitium in https://github.com/ModelCloud/GPTQModel/pull/2141
* Fix triton version detection in nogil patcher by @amd-vlarakic in https://github.com/ModelCloud/GPTQModel/pull/2144
* Fix qwen2 omni by @LRL2-ModelCloud in https://github.com/ModelCloud/GPTQModel/pull/2140
* [MODEL] Add GraniteMoEHybrid by @ZX-ModelCloud in https://github.com/ModelCloud/GPTQModel/pull/2142
* Fold AWQ into proper Looper/Layer/Subset Lifecycle by @Qubitium in https://github.com/ModelCloud/GPTQModel/pull/2138
* Refine GPT-QModel description in README by @Qubitium in https://github.com/ModelCloud/GPTQModel/pull/2145
* fix device_map by @LRL2-ModelCloud in https://github.com/ModelCloud/GPTQModel/pull/2146
* [MODEL] Add Qwen3-VL by @techshoww in https://github.com/ModelCloud/GPTQModel/pull/2136
* Add calibration_concat_separator by @Qubitium in https://github.com/ModelCloud/GPTQModel/pull/2148
* add test_qwen3_vl.py by @LRL2-ModelCloud in https://github.com/ModelCloud/GPTQModel/pull/2147
* Fix triton monkeypatch by @Qubitium in https://github.com/ModelCloud/GPTQModel/pull/2149
* [MODEL] Add Brumby by @Qubitium in https://github.com/ModelCloud/GPTQModel/pull/2150
* Dedup/Cleanup by @Qubitium in https://github.com/ModelCloud/GPTQModel/pull/2151
* Prep for 5.2 release by @Qubitium in https://github.com/ModelCloud/GPTQModel/pull/2152
* Dedup3 by @Qubitium in https://github.com/ModelCloud/GPTQModel/pull/2153
* add missing file by @Qubitium in https://github.com/ModelCloud/GPTQModel/pull/2154
* GPTAQ rename by @Qubitium in https://github.com/ModelCloud/GPTQModel/pull/2155
* fix ci test by @Qubitium in https://github.com/ModelCloud/GPTQModel/pull/2158
* fix setup license by @Qubitium in https://github.com/ModelCloud/GPTQModel/pull/2160
* FIx snapshot_download receiving unsupported kwargs by @Qubitium in https://github.com/ModelCloud/GPTQModel/pull/2162
* Retry partial.to to fix accelerate invalid argument error for first moe layer for >4 GPU setups by @avtc in https://github.com/ModelCloud/GPTQModel/pull/2163
* Comments + Sync by @Qubitium in https://github.com/ModelCloud/GPTQModel/pull/2164
* Stats/Logs by @Qubitium in https://github.com/ModelCloud/GPTQModel/pull/2165

## New Contributors
* @amd-vlarakic made their first contribution in https://github.com/ModelCloud/GPTQModel/pull/2144
* @techshoww made their first contribution in https://github.com/ModelCloud/GPTQModel/pull/2136

**Full Changelog**: https://github.com/ModelCloud/GPTQModel/compare/v5.0.0...v5.2.0

## v5.4.0 (2025-11-09)

## Notable Changes:

* AWQ Torch Fused Kernel by @Qubitium in https://github.com/ModelCloud/GPTQModel/pull/2190
* Make torch fused op compilable by @jiqing-feng in https://github.com/ModelCloud/GPTQModel/pull/2182
* [FIX] AWQ MoE by @ZX-ModelCloud in https://github.com/ModelCloud/GPTQModel/pull/2171
* add :? capture only syntax by @Qubitium in https://github.com/ModelCloud/GPTQModel/pull/2173

## What's Changed
* Update latest news section in README.md by @Qubitium in https://github.com/ModelCloud/GPTQModel/pull/2166
* run forward pass even for empty subset to produce correct layer outputs by @avtc in https://github.com/ModelCloud/GPTQModel/pull/2161
* Reduce AWQ memory usage by @Qubitium in https://github.com/ModelCloud/GPTQModel/pull/2167
* Awq update by @Qubitium in https://github.com/ModelCloud/GPTQModel/pull/2168
* Retry partial to to fix accelerate invalid argument for first moe layer (reapply) by @avtc in https://github.com/ModelCloud/GPTQModel/pull/2169
* Awq update by @Qubitium in https://github.com/ModelCloud/GPTQModel/pull/2172
* adjust retry partial.to by @avtc in https://github.com/ModelCloud/GPTQModel/pull/2175
* cleanup awq_get_modules_for_scaling() by @ZX-ModelCloud in https://github.com/ModelCloud/GPTQModel/pull/2179
* [FIX] qwen3 moe sparse moe block by @ZX-ModelCloud in https://github.com/ModelCloud/GPTQModel/pull/2184
* Add module convert by @LRL2-ModelCloud in https://github.com/ModelCloud/GPTQModel/pull/2183
* Cleanup by @Qubitium in https://github.com/ModelCloud/GPTQModel/pull/2185
* Update pypcre version to 0.2.5 by @LRL2-ModelCloud in https://github.com/ModelCloud/GPTQModel/pull/2186
* Update pypcre version to 0.2.5 by @Qubitium in https://github.com/ModelCloud/GPTQModel/pull/2189
* [FIX] version("triton") crash on torch+xpu by @ZX-ModelCloud in https://github.com/ModelCloud/GPTQModel/pull/2188


**Full Changelog**: https://github.com/ModelCloud/GPTQModel/compare/v5.2.0...v5.4.0

## v5.4.2 (2025-11-15)

## Notable Changes:

* Fix double fwd regression by @Qubitium in https://github.com/ModelCloud/GPTQModel/pull/2198
* Add cli: gptqmodel env by @ZX-ModelCloud in https://github.com/ModelCloud/GPTQModel/pull/2192
* [CI] compile wheel with python -m build by @CSY-ModelCloud in https://github.com/ModelCloud/GPTQModel/pull/2193


## What's Changed
* Start v5.5.0 devel branch (odd version) by @Qubitium in https://github.com/ModelCloud/GPTQModel/pull/2191
* Update version from 5.5.0 to 5.4.2 patch release by @Qubitium in https://github.com/ModelCloud/GPTQModel/pull/2199
* [CI] copy wheel to local dir instead of using http server by @CSY-ModelCloud in https://github.com/ModelCloud/GPTQModel/pull/2200


**Full Changelog**: https://github.com/ModelCloud/GPTQModel/compare/v5.4.0...v5.4.2

## v5.6.0 (2025-12-09)

## Notable Changes:

* HF Kernel for CPU: AMX, AVX2, AVX512 optimized by @jiqing-feng in https://github.com/ModelCloud/GPTQModel/pull/2232
* Fix: Resolve performance regression during initial forward pass with offload_to_disk by @avtc in https://github.com/ModelCloud/GPTQModel/pull/2239
* Auto module tree by @LRL2-ModelCloud in https://github.com/ModelCloud/GPTQModel/pull/2204
* Afmoe support by @LRL2-ModelCloud in https://github.com/ModelCloud/GPTQModel/pull/2243
* Add dots1 by @Qubitium in https://github.com/ModelCloud/GPTQModel/pull/2231

## What's Changed
* Update description and code about GPTAQ in README.md by @wayneguow in https://github.com/ModelCloud/GPTQModel/pull/2202
* Update test cases for qwen2.5-vl and qwen3-vl by @wayneguow in https://github.com/ModelCloud/GPTQModel/pull/2203
* Optimize minimax m2 modelling forward pass by @avtc in https://github.com/ModelCloud/GPTQModel/pull/2176
* remove gemm ipex by @LRL2-ModelCloud in https://github.com/ModelCloud/GPTQModel/pull/2206
* Bump actions/checkout from 5 to 6 in the github-actions group by @dependabot[bot] in https://github.com/ModelCloud/GPTQModel/pull/2207
* Update device-smi dependency version to 0.5.2 by @Qubitium in https://github.com/ModelCloud/GPTQModel/pull/2208
* Fix loading an AWQ-quantized model with GPTQModel when it is not actu… by @LRL2-ModelCloud in https://github.com/ModelCloud/GPTQModel/pull/2209
* fix exllama v2 post init by @LRL2-ModelCloud in https://github.com/ModelCloud/GPTQModel/pull/2211
* [FIX] Add fallback for "module_dir" and "entry key" lookup by @ZX-ModelCloud in https://github.com/ModelCloud/GPTQModel/pull/2210
* Update unit_tests.yml by @Qubitium in https://github.com/ModelCloud/GPTQModel/pull/2213
* fix mps backend does not implement float64 by @Qubitium in https://github.com/ModelCloud/GPTQModel/pull/2216
* [FIX] _apply_quant() not being called with awq by @ZX-ModelCloud in https://github.com/ModelCloud/GPTQModel/pull/2218
* Fix AWQ Extension by @LRL2-ModelCloud in https://github.com/ModelCloud/GPTQModel/pull/2217
* Auto AWQ kernel selection for Transformers compat by @Qubitium in https://github.com/ModelCloud/GPTQModel/pull/2214
* Fix add bias for torch_fuse by @jiqing-feng in https://github.com/ModelCloud/GPTQModel/pull/2223
* [CI] Add torch_fused test with Bias by @ZX-ModelCloud in https://github.com/ModelCloud/GPTQModel/pull/2222
* [FIX] device_map with cpu only causing `CpuOffload` hooks to be injected  by @ZX-ModelCloud in https://github.com/ModelCloud/GPTQModel/pull/2225
* fix awq apply_scale and apply_clip multi thread issue by @LRL2-ModelCloud in https://github.com/ModelCloud/GPTQModel/pull/2224
* Fix CI test not pasing by @Qubitium in https://github.com/ModelCloud/GPTQModel/pull/2226
* Monkeypatch lm-eval latest broken imports by @Qubitium in https://github.com/ModelCloud/GPTQModel/pull/2227
* make file can be pytest called by @CSY-ModelCloud in https://github.com/ModelCloud/GPTQModel/pull/2228
* CI Fix awq weight mean by @LRL2-ModelCloud in https://github.com/ModelCloud/GPTQModel/pull/2229
* fix pycharm auto imported wrong path by @CSY-ModelCloud in https://github.com/ModelCloud/GPTQModel/pull/2230
* [FIX] TorchFusedAwqQuantLinear selection by @ZX-ModelCloud in https://github.com/ModelCloud/GPTQModel/pull/2233
* [CI] update CI path by @CSY-ModelCloud in https://github.com/ModelCloud/GPTQModel/pull/2236
* [Model] Mistral3 support by @LRL2-ModelCloud in https://github.com/ModelCloud/GPTQModel/pull/2238
* Update setup.py by @Qubitium in https://github.com/ModelCloud/GPTQModel/pull/2240
* Increase MAX_JOBS from 4 to 8 in release.yml by @Qubitium in https://github.com/ModelCloud/GPTQModel/pull/2241
* [FIX] non-peristent buffer was saved incorrectly by @ZX-ModelCloud in https://github.com/ModelCloud/GPTQModel/pull/2242

## New Contributors
* @wayneguow made their first contribution in https://github.com/ModelCloud/GPTQModel/pull/2202



## v5.6.2 (2025-12-12)

## Notable Changes
* FIX JIT Pytorch extension `pack_cpu_ext` stall by @ZX-ModelCloud in https://github.com/ModelCloud/GPTQModel/pull/2248
* Refractor Kernel External Dependency Validation by @LRL2-ModelCloud in https://github.com/ModelCloud/GPTQModel/pull/2249
* FIX some models not honoring model.config.use_cache by force pass use_cache=false by @LRL2-ModelCloud in https://github.com/ModelCloud/GPTQModel/pull/2246
* FIX Incorrect Triton dequant_kernel for 3-bit GPTQ (INT3) leads to Triton compile error / wrong dequantization #2251 by 
* Support llm-awq by @ZX-ModelCloud in https://github.com/ModelCloud/GPTQModel/pull/2252
 
## What's Changed
* Update version.py by @Qubitium in https://github.com/ModelCloud/GPTQModel/pull/2247
* Update README.md by @davedgd in https://github.com/ModelCloud/GPTQModel/pull/2250
* [CI] add torch 2.9.1 by @CSY-ModelCloud in https://github.com/ModelCloud/GPTQModel/pull/2254
@KingdalfGoodman in https://github.com/ModelCloud/GPTQModel/pull/2258
* Update license declaration in pyproject.toml by @CSY-ModelCloud in https://github.com/ModelCloud/GPTQModel/pull/2259
* Modify setup by @Qubitium in https://github.com/ModelCloud/GPTQModel/pull/2260
* Add release notes for version 5.6.2 by @Qubitium in https://github.com/ModelCloud/GPTQModel/pull/2261
* fix test_quant_formats.py by @LRL2-ModelCloud in https://github.com/ModelCloud/GPTQModel/pull/2262
* [CI] mount dateset dir to /monster/data/model/dataset by @CSY-ModelCloud in https://github.com/ModelCloud/GPTQModel/pull/2263
* fix parsing args by @CSY-ModelCloud in https://github.com/ModelCloud/GPTQModel/pull/2264

## New Contributors
* @KingdalfGoodman made their first contribution in https://github.com/ModelCloud/GPTQModel/pull/2258

**Full Changelog**: https://github.com/ModelCloud/GPTQModel/compare/v5.6.0...v5.6.2

## v5.6.4 (2025-12-15)

## What's Changed
* Bump the github-actions group with 2 updates by @dependabot[bot] in https://github.com/ModelCloud/GPTQModel/pull/2265
* remove random-word depend by @LRL2-ModelCloud in https://github.com/ModelCloud/GPTQModel/pull/2266
* Update pypcre version from 0.2.7 to 0.2.8 by @Qubitium in https://github.com/ModelCloud/GPTQModel/pull/2267
* Update version.py by @Qubitium in https://github.com/ModelCloud/GPTQModel/pull/2268


**Full Changelog**: https://github.com/ModelCloud/GPTQModel/compare/v5.6.2...v5.6.4

## v5.6.6 (2025-12-15)

## Notable Changes:

* Use static cuda ctx for triton kernel launch by @Qubitium in https://github.com/ModelCloud/GPTQModel/pull/2269
* Remove random-word depend by @LRL2-ModelCloud in https://github.com/ModelCloud/GPTQModel/pull/2266
* Update PyPcre depend from 0.2.7 to 0.2.8 by @Qubitium in https://github.com/ModelCloud/GPTQModel/pull/2267

## What's Changed
* Bump the github-actions group with 2 updates by @dependabot[bot] in https://github.com/ModelCloud/GPTQModel/pull/2265
* Update version.py by @Qubitium in https://github.com/ModelCloud/GPTQModel/pull/2268
* Ready 5.6.6 by @Qubitium in https://github.com/ModelCloud/GPTQModel/pull/2270


**Full Changelog**: https://github.com/ModelCloud/GPTQModel/compare/v5.6.2...v5.6.6

## v5.6.8 (2025-12-16)

## Notable Changes:

* Fix Triton check/import by @Qubitium in https://github.com/ModelCloud/GPTQModel/pull/2274

## What's Changed
* Add kernel selection log by @ZX-ModelCloud in https://github.com/ModelCloud/GPTQModel/pull/2275
* Update README.md by @Qubitium in https://github.com/ModelCloud/GPTQModel/pull/2276


**Full Changelog**: https://github.com/ModelCloud/GPTQModel/compare/v5.6.6...v5.6.8

## v5.6.10 (2025-12-16)

## Notable Changes:

* Triton check by @Qubitium in https://github.com/ModelCloud/GPTQModel/pull/2274
* Fix bitblas support for gptq_v2 format by @xxxxyu in https://github.com/ModelCloud/GPTQModel/pull/2281
* Fix awq triton kernel has invalid properties by @Qubitium in https://github.com/ModelCloud/GPTQModel/pull/2279

## What's Changed
* Add kernel selection log by @ZX-ModelCloud in https://github.com/ModelCloud/GPTQModel/pull/2275
* Update README.md by @Qubitium in https://github.com/ModelCloud/GPTQModel/pull/2276
* Update pypcre depend by @Qubitium in https://github.com/ModelCloud/GPTQModel/pull/2277
* Update version.py by @Qubitium in https://github.com/ModelCloud/GPTQModel/pull/2278
* Add macos unit tests by @CSY-ModelCloud in https://github.com/ModelCloud/GPTQModel/pull/2282
* Update README.md by @Qubitium in https://github.com/ModelCloud/GPTQModel/pull/2283

## New Contributors
* @xxxxyu made their first contribution in https://github.com/ModelCloud/GPTQModel/pull/2281

**Full Changelog**: https://github.com/ModelCloud/GPTQModel/compare/v5.6.6...v5.6.10

## v5.6.12 (2025-12-17)

## Notable Changes:

* `uv` compat
* Both `uv` and `pip` install will now display ui progress for external wheel/depend downloads.


## What's Changed
* [FIX] failed unittest by @ZX-ModelCloud in https://github.com/ModelCloud/GPTQModel/pull/2286
* fix wheel name mistaches with version name by @CSY-ModelCloud in https://github.com/ModelCloud/GPTQModel/pull/2288
* Setup download progress by @Qubitium in https://github.com/ModelCloud/GPTQModel/pull/2289
* Update latest news section in README.md by @Qubitium in https://github.com/ModelCloud/GPTQModel/pull/2290


**Full Changelog**: https://github.com/ModelCloud/GPTQModel/compare/v5.6.10...v5.6.12

## v5.7.0 (2026-02-10)

## Notable Changes:

* Feature: MoE.Routing control (Bypass or Override) by @avtc in https://github.com/ModelCloud/GPTQModel/pull/2235
* Feature: Use FailSafe Naive Quantization when GPTQ fails due to MoE uneven routing by @ZX-ModelCloud in https://github.com/ModelCloud/GPTQModel/pull/2293
* Feature: ability to pause/resume quantization via 'p' key by @avtc in https://github.com/ModelCloud/GPTQModel/pull/2294
* Glm4v support by @LRL2-ModelCloud in https://github.com/ModelCloud/GPTQModel/pull/2303
* Failsafe smoothers by @Qubitium in https://github.com/ModelCloud/GPTQModel/pull/2304
* New median strategy and SmoothPercentileAsymmetric smoother by @Qubitium in 
* Support for Qwen2.5-Omni calibration data includes audio. by @ChenShisen in https://github.com/ModelCloud/GPTQModel/pull/2309
* Add Smooth trigger based on group_size by @Qubitium in https://github.com/ModelCloud/GPTQModel/pull/2312
* Voxtral support by @LRL2-ModelCloud in https://github.com/ModelCloud/GPTQModel/pull/2315
* Better compat with triton-windows and other alternative triton packages by @Qubitium in https://github.com/ModelCloud/GPTQModel/pull/2395
* Dynamically map format/backend to kernel  by @Qubitium in https://github.com/ModelCloud/GPTQModel/pull/2353
* Add EXAONE4 support  by @namgyu-youn in https://github.com/ModelCloud/GPTQModel/pull/2405


## What's Changed
* [FIX] unittest by @ZX-ModelCloud in https://github.com/ModelCloud/GPTQModel/pull/2291
* [FIX] marlin forward by @ZX-ModelCloud in https://github.com/ModelCloud/GPTQModel/pull/2296
* FIX fast_hadamard_transform import by @LRL2-ModelCloud in https://github.com/ModelCloud/GPTQModel/pull/2298
* do not log moe errors if `failesafe` enabled by @Qubitium in https://github.com/ModelCloud/GPTQModel/pull/2299
* [CI] allow cancel action by @CSY-ModelCloud in https://github.com/ModelCloud/GPTQModel/pull/2300
* Fix non-rtn packing by @Qubitium in https://github.com/ModelCloud/GPTQModel/pull/2302
* log q vs weight abs.mean for loss column by @Qubitium in https://github.com/ModelCloud/GPTQModel/pull/2306
* fix inverted failsafe log condition by @Qubitium in https://github.com/ModelCloud/GPTQModel/pull/2310
https://github.com/ModelCloud/GPTQModel/pull/2311
* Allow failsafe to be none by @Qubitium in https://github.com/ModelCloud/GPTQModel/pull/2313
* move non-inference affecting fields to meta on save by @Qubitium in https://github.com/ModelCloud/GPTQModel/pull/2314
* [FIX] GPTQModel.load() can now correctly load non-quantized models. by @ZX-ModelCloud in https://github.com/ModelCloud/GPTQModel/pull/2317
* FIX hf kernel by @jiqing-feng in https://github.com/ModelCloud/GPTQModel/pull/2319
* [CI] test_qwen3_moe add eval task: GSM8K_PLATINUM_COT and MMLU_STEM by @ZX-ModelCloud in https://github.com/ModelCloud/GPTQModel/pull/2320
* Release 5.7 Prep by @Qubitium in https://github.com/ModelCloud/GPTQModel/pull/2318
* [FIX] Exclude unrouted MoE experts on load by @ZX-ModelCloud in https://github.com/ModelCloud/GPTQModel/pull/2321
* [FIX] Skip empty subset by @ZX-ModelCloud in https://github.com/ModelCloud/GPTQModel/pull/2322
* [FIX] GLM-4.5-Air quantize fail by @ZX-ModelCloud in https://github.com/ModelCloud/GPTQModel/pull/2323
* fix: offload_to_disk=True uses more vram than offload_to_disk=False by @avtc in https://github.com/ModelCloud/GPTQModel/pull/2325
* Fix import no_init_weights from transformers by @jiqing-feng in https://github.com/ModelCloud/GPTQModel/pull/2329
* [FIX] qqq quantize by @ZX-ModelCloud in https://github.com/ModelCloud/GPTQModel/pull/2330
* chery pick: attempt to fix terminal state after pause/resume handlers by @avtc in https://github.com/ModelCloud/GPTQModel/pull/2327
* [FIX] quantization to fail for non-MoE models by @ZX-ModelCloud in https://github.com/ModelCloud/GPTQModel/pull/2333
* Device check by @jiqing-feng in https://github.com/ModelCloud/GPTQModel/pull/2334
* FIX moe flag passing not passing nested ci test by @Qubitium in https://github.com/ModelCloud/GPTQModel/pull/2337
* Use safer checks for nullable properties where they may not exists at… by @Qubitium in https://github.com/ModelCloud/GPTQModel/pull/2338
* Fix unit test by @Qubitium in https://github.com/ModelCloud/GPTQModel/pull/2339
* Group module_tree/subsection parsing related tests to module_tree folder by @Qubitium in https://github.com/ModelCloud/GPTQModel/pull/2340
* Group kernel tests by @Qubitium in https://github.com/ModelCloud/GPTQModel/pull/2341
* Lifecycle: Move `awq.pack_module` to `submodule_finalize()` from `process()` by @ZX-ModelCloud in https://github.com/ModelCloud/GPTQModel/pull/2335
* Partial Revert 2235: temp remove moe bypass by @ZX-ModelCloud in https://github.com/ModelCloud/GPTQModel/pull/2343
* Re apply compute device filter by @Qubitium in https://github.com/ModelCloud/GPTQModel/pull/2345
* Re-apply moe routing bypass by @ZX-ModelCloud in https://github.com/ModelCloud/GPTQModel/pull/2347
* Fix: Zero point underflow in AWQ Exllama v2 kernel by @12345txy in https://github.com/ModelCloud/GPTQModel/pull/2351
* Remove unnecessary +1/-1 inference/packing zerpoint offset for AWQ Exllama v2 kernel by @Qubitium in https://github.com/ModelCloud/GPTQModel/pull/2352
* Normalize AWQ.qcfg `zero_point` to `sym` property by @Qubitium in https://github.com/ModelCloud/GPTQModel/pull/2355
* FIX sym True with AWQ by @ZX-ModelCloud in https://github.com/ModelCloud/GPTQModel/pull/2357
* Prepare for 5.7 by @Qubitium in https://github.com/ModelCloud/GPTQModel/pull/2358
* [FIX]  `self_attn.q_proj` was not quantized in the Moonlight Model by @ZX-ModelCloud in https://github.com/ModelCloud/GPTQModel/pull/2360
* [FIX] torch_fused inference error by @ZX-ModelCloud in https://github.com/ModelCloud/GPTQModel/pull/2362
* [FIX] FORMAT.LLM_AWQ was incorrectly quantized as FORMAT.GEMM by @ZX-ModelCloud in https://github.com/ModelCloud/GPTQModel/pull/2364
* [CI] load all tests include sub dirs & merge some small tests in to one file by @CSY-ModelCloud in https://github.com/ModelCloud/GPTQModel/pull/2363
* Fix evalplus output filename mismatch by @juraev in https://github.com/ModelCloud/GPTQModel/pull/2365
* [FIX] FORMAT.GEMV and FORMAT.GEMV_FAST could not be quantized by @ZX-ModelCloud in https://github.com/ModelCloud/GPTQModel/pull/2366
* [CI] add deps config for CI tests by @CSY-ModelCloud in https://github.com/ModelCloud/GPTQModel/pull/2368
* [FIX] unittest by @ZX-ModelCloud in https://github.com/ModelCloud/GPTQModel/pull/2370
* [FIX] In AWQProcessor, the failsafe threshold_value should be calculated based on the scale group, not the entire layer by @ZX-ModelCloud in https://github.com/ModelCloud/GPTQModel/pull/2369
* [CI] fix ci didn't read correct yaml by @CSY-ModelCloud in https://github.com/ModelCloud/GPTQModel/pull/2371
* [FIX] ci unittest by @ZX-ModelCloud in https://github.com/ModelCloud/GPTQModel/pull/2372
* [FIX] test_q4_bitblas and test_qqq  by @ZX-ModelCloud in https://github.com/ModelCloud/GPTQModel/pull/2373
* [CI] add test_integration deps by @CSY-ModelCloud in https://github.com/ModelCloud/GPTQModel/pull/2374
* [CI] fix torch version was upgraded by deps by @CSY-ModelCloud in https://github.com/ModelCloud/GPTQModel/pull/2377
* `select_quant_linear` should always receive a non-null `device` by @Qubitium in https://github.com/ModelCloud/GPTQModel/pull/2376
* [CI] uninstall pynvml by @CSY-ModelCloud in https://github.com/ModelCloud/GPTQModel/pull/2378
* [FIX] failed ci test by @ZX-ModelCloud in https://github.com/ModelCloud/GPTQModel/pull/2380
* [FIX] test_gptq by @ZX-ModelCloud in https://github.com/ModelCloud/GPTQModel/pull/2382
* [FIX] correct `has_captured_input_ids()` logic by using `> 0` check by @ZX-ModelCloud in https://github.com/ModelCloud/GPTQModel/pull/2383
* [FIX] test_model by @ZX-ModelCloud in https://github.com/ModelCloud/GPTQModel/pull/2384
* [FIX] unit test by @ZX-ModelCloud in https://github.com/ModelCloud/GPTQModel/pull/2385
* [CI] use new docker by @CSY-ModelCloud in https://github.com/ModelCloud/GPTQModel/pull/2387
* [FIX] ci test by @ZX-ModelCloud in https://github.com/ModelCloud/GPTQModel/pull/2388
* [FIX] unittest by @ZX-ModelCloud in https://github.com/ModelCloud/GPTQModel/pull/2389
* [FIX] missing ExllamaV2 kernels initialization in AutoRound by @ZX-ModelCloud in https://github.com/ModelCloud/GPTQModel/pull/2390
* [CI] keep uv up to date by @CSY-ModelCloud in https://github.com/ModelCloud/GPTQModel/pull/2391
* [FIX] test_awq by @ZX-ModelCloud in https://github.com/ModelCloud/GPTQModel/pull/2392
* [FIX] Incorrectly selected device by @ZX-ModelCloud in https://github.com/ModelCloud/GPTQModel/pull/2394
* [FIX] quantization failure for Qwen2/2.5/3 VL models with FlashAttention-2 by @ZX-ModelCloud in https://github.com/ModelCloud/GPTQModel/pull/2396
* [FIX] test_ovis2 and test_ovis_1_6_llama by @ZX-ModelCloud in https://github.com/ModelCloud/GPTQModel/pull/2397
* [FIX] test_stage_modules by @ZX-ModelCloud in https://github.com/ModelCloud/GPTQModel/pull/2398
* [CI] list test files with py file & fix duplicated test names by @CSY-ModelCloud in https://github.com/ModelCloud/GPTQModel/pull/2399
* [FIX] test_pause_resume by @ZX-ModelCloud in https://github.com/ModelCloud/GPTQModel/pull/2400
* [CI] update sort, root test files first by @CSY-ModelCloud in https://github.com/ModelCloud/GPTQModel/pull/2401
* [FIX] exllama_v1 kernel crash by @ZX-ModelCloud in https://github.com/ModelCloud/GPTQModel/pull/2402
* [FIX] test_chatglm by @ZX-ModelCloud in https://github.com/ModelCloud/GPTQModel/pull/2406
* set tokenicer>=0.0.6 by @CSY-ModelCloud in https://github.com/ModelCloud/GPTQModel/pull/2407
* Fix tokenizer_class incompatibility with transformers 5.0 by @juraev in https://github.com/ModelCloud/GPTQModel/pull/2403
* [FIX] model_test by @ZX-ModelCloud in https://github.com/ModelCloud/GPTQModel/pull/2410
* fixed ValueError: invalid pyproject.toml config: project.license. con… by @CSY-ModelCloud in https://github.com/ModelCloud/GPTQModel/pull/2412
* [FIX] module_tree tests by @ZX-ModelCloud in https://github.com/ModelCloud/GPTQModel/pull/2411
* fix license warning by @CSY-ModelCloud in https://github.com/ModelCloud/GPTQModel/pull/2413

## New Contributors
* @ChenShisen made their first contribution in https://github.com/ModelCloud/GPTQModel/pull/2309
* @12345txy made their first contribution in https://github.com/ModelCloud/GPTQModel/pull/2351
* @juraev made their first contribution in https://github.com/ModelCloud/GPTQModel/pull/2365
* @namgyu-youn made their first contribution in https://github.com/ModelCloud/GPTQModel/pull/2405

**Full Changelog**: https://github.com/ModelCloud/GPTQModel/compare/v5.6.12...v5.7.0

## v5.8.0 (2026-03-19)

## Notable Changes

* Transformers 5.3.0 compatibility. 
 
* **Video Quantization Support**
  * Added support for video input during quantization.

* **MoE & Model Support**
  * Added support for **Qwen 3.5** and **Qwen 3.5 MoE**.
  * Expanded compatibility for **Qwen 3** variants including **MoE / VL / Omni / Next**.
  * Added support for **LLada2** block diffusion LLM models.
  * Improved compatibility for **Mixtral**, **Phi-4**, **Nemotron Ultra**, **BaiChuan**, **ChatGLM**, **Yi**, and **GLM4V**.
  * Fixed multiple MoE-specific AWQ and multi-GPU issues, including routing, module tree, position embeddings, and device mismatches.

* **AWQ / GPTQ Kernels**
  * Added **CPU fused AWQ kernels** for `torch_fused` and `hf_kernel`.
  * Added **torch_int8 AWQ kernel**.
  * Added **BitBLAS AWQ kernel**.
  * Ported **Intel int8 GPTQ/AWQ kernels**.
  * Updated kernel selection to prefer **HF kernels** where they provide the best performance and compatibility.
  * Added BitBLAS fallback protection and fixed BitBLAS accuracy and qzero remap regressions.

* **Quantization Improvements**
  * Replaced greedy search with **ternary search** in SmoothBSE.
  * Fixed **SmoothMAD** overly aggressive clipping.
  * Added **layer-level dynamic skip** for fast quantization.
  * Added early stop when all remaining layers are skipped during quantization.
  * Fixed AWQ OOM and dequantization-related issues.

* **Runtime & Dequantization**
  * Added optional **CPU int64 `g_idx` cache** for TorchQuantLinear dequantization.
  * Improved TorchFused dequantization and fp32 dtype support.
  * Removed unnecessary symmetric handling in `dequantize_gemm`.
  * Fixed rotary embedding device mismatch by storing per-device rotary copies.
  * Added warmup protection for threaded timing.

* **Defuser Integration**
  * Integrated `defuser.convert_hf_model()`.
  * Integrated `defuser.materialize_model()`.
  * Integrated `defuser.replace_fused_blocks()`.
  * Improved defuser meta/offload compatibility and fused block handling.

* **Compatibility Fixes**
  * Improved compatibility with older and newer **Hugging Face Transformers** / **Optimum** versions.
  * Fixed import compatibility issues in `models/utils`.
  * Fixed rotary / embedding config compatibility with older HF and model variants.
  * Improved tokenizer and model compatibility updates related to `tokenicer`.
  * Fixed OSS compatibility issues.

* **Kernel / Backend Changes**
  * Hard deprecated **ExLLaMA v1** kernel.
  * Exposed the **Triton patcher** as an externally callable API.

## What's Changed
* support video input for quantization by @techshoww in https://github.com/ModelCloud/GPTQModel/pull/2386
* feat: moe-router-bypass-batch-size by @avtc in https://github.com/ModelCloud/GPTQModel/pull/2349
* [CI] use UV as python manager by @CSY-ModelCloud in https://github.com/ModelCloud/GPTQModel/pull/2415
* [CI] fix deps installation & gpu service api path by @CSY-ModelCloud in https://github.com/ModelCloud/GPTQModel/pull/2416
* [CI] auto release GPU if job has sth wrong or unrecoverable by @CSY-ModelCloud in https://github.com/ModelCloud/GPTQModel/pull/2417
* [CI] save log to disk & fix deps installation by @CSY-ModelCloud in https://github.com/ModelCloud/GPTQModel/pull/2418
* Replace Greedy with Tenary Search for SmoothBSE by @namgyu-youn in https://github.com/ModelCloud/GPTQModel/pull/2419
* Feature/LLada2 support: Block Diffusion LLM by @blazingbhavneek in https://github.com/ModelCloud/GPTQModel/pull/2422
* Bump the github-actions group with 2 updates by @dependabot[bot] in https://github.com/ModelCloud/GPTQModel/pull/2426
* [MODEL] supports qwen3_5 by @ZX-ModelCloud in https://github.com/ModelCloud/GPTQModel/pull/2427
* [FIX] eval bug for qwn3_5 quantized model by @ZX-ModelCloud in https://github.com/ModelCloud/GPTQModel/pull/2428
* [MODEL] supports qwen3_5_moe by @ZX-ModelCloud in https://github.com/ModelCloud/GPTQModel/pull/2433
* Update tokenicer dependency version to 0.0.7 by @Qubitium in https://github.com/ModelCloud/GPTQModel/pull/2434
* Optional `CPU` g_idx int64 cache for TorchQuantLinear dequant path by @Qubitium in https://github.com/ModelCloud/GPTQModel/pull/2431
* fix import compat issues for models/utils that is locked to higher ve… by @Qubitium in https://github.com/ModelCloud/GPTQModel/pull/2436
* call defuser.convert_hf_model() by @ZX-ModelCloud in https://github.com/ModelCloud/GPTQModel/pull/2437
* Update defuser dependency version to 0.0.3 by @Qubitium in https://github.com/ModelCloud/GPTQModel/pull/2439
* quantize mlp experts module for qwen3_5_moe by @ZX-ModelCloud in https://github.com/ModelCloud/GPTQModel/pull/2443
* Fix typo in setup.py causing wheel build failure (sys.abiflag -> sys.abiflags) by @beomchan0 in https://github.com/ModelCloud/GPTQModel/pull/2444
* call defuser's materialize_model()  by @ZX-ModelCloud in https://github.com/ModelCloud/GPTQModel/pull/2446
* Update defuser dependency version to 0.0.4 by @Qubitium in https://github.com/ModelCloud/GPTQModel/pull/2447
* port intel's int8 gptq/awq kernel over by @Qubitium in https://github.com/ModelCloud/GPTQModel/pull/2438
* expose triton patcher as externally callable by @Qubitium in https://github.com/ModelCloud/GPTQModel/pull/2448
* docs by @Qubitium in https://github.com/ModelCloud/GPTQModel/pull/2449
* Add AWQ support for CPU fused kernels (torch_fused & hf_kernel) by @jiqing-feng in https://github.com/ModelCloud/GPTQModel/pull/2445
* Cleanupx by @Qubitium in https://github.com/ModelCloud/GPTQModel/pull/2450
* Make HF kernels for gptq/awq highest priority as they are the highest… by @Qubitium in https://github.com/ModelCloud/GPTQModel/pull/2451
* rm sym in dequantize_gemm by @jiqing-feng in https://github.com/ModelCloud/GPTQModel/pull/2452
* fix awq rotary device mismatch. store per-device copy of rotary by @Qubitium in https://github.com/ModelCloud/GPTQModel/pull/2453
* add torch_int8 awq kernel by @Qubitium in https://github.com/ModelCloud/GPTQModel/pull/2454
* [CI] move check log to a new step by @CSY-ModelCloud in https://github.com/ModelCloud/GPTQModel/pull/2455
* cleanup hf kernel gptq/awq post_init loading by @Qubitium in https://github.com/ModelCloud/GPTQModel/pull/2457
* fix SmoothMAD overly-aggressive clipping by @Qubitium in https://github.com/ModelCloud/GPTQModel/pull/2459
* upgrade defuser version to 0.0.5 by @ZX-ModelCloud in https://github.com/ModelCloud/GPTQModel/pull/2460
* [FIX] test_qwen3_5_moe by @ZX-ModelCloud in https://github.com/ModelCloud/GPTQModel/pull/2461
* Update defuser dependency version to 0.0.6 by @Qubitium in https://github.com/ModelCloud/GPTQModel/pull/2462
* fix awq oom by @CSY-ModelCloud in https://github.com/ModelCloud/GPTQModel/pull/2458
* [CI] CUDA 131 + Torch 2.10.0 + Python 3.13 by @CSY-ModelCloud in https://github.com/ModelCloud/GPTQModel/pull/2463
* Fix the module_tree in Qwen3_5_Moe to correctly support AWQ by @ZX-ModelCloud in https://github.com/ModelCloud/GPTQModel/pull/2464
* [CI] fix git link cannot be installed by uv by @CSY-ModelCloud in https://github.com/ModelCloud/GPTQModel/pull/2465
* [FIX] GEMM can't pack by @ZX-ModelCloud in https://github.com/ModelCloud/GPTQModel/pull/2466
* [CI] add peft for test_asym_gptq_v1 & check log after test by @CSY-ModelCloud in https://github.com/ModelCloud/GPTQModel/pull/2467
* [CI] get path error from log & install pre-compiled bitblas by @CSY-ModelCloud in https://github.com/ModelCloud/GPTQModel/pull/2468
* [CI] fix log files were saved with wrong runid by @CSY-ModelCloud in https://github.com/ModelCloud/GPTQModel/pull/2469
* [FIX] where qwen3_5_moe got incorrect `position_embeddings` during `AWQ` quantization by @ZX-ModelCloud in https://github.com/ModelCloud/GPTQModel/pull/2470
* Update pypcre version to 0.2.13 by @CSY-ModelCloud in https://github.com/ModelCloud/GPTQModel/pull/2471
* read dependencies from requirements.txt by @CSY-ModelCloud in https://github.com/ModelCloud/GPTQModel/pull/2472
* add setuptools to requirements.txt by @CSY-ModelCloud in https://github.com/ModelCloud/GPTQModel/pull/2474
* set minimum setuptools version to 78.1.1 by @CSY-ModelCloud in https://github.com/ModelCloud/GPTQModel/pull/2475
* [FIX] device mismatch issue that occurred during multi-GPU AWQ quantization in moe Model by @ZX-ModelCloud in https://github.com/ModelCloud/GPTQModel/pull/2476
* [CI] auto uninstall unneeded pkgs by @CSY-ModelCloud in https://github.com/ModelCloud/GPTQModel/pull/2478
* fix ci failed tests by @ZX-ModelCloud in https://github.com/ModelCloud/GPTQModel/pull/2477
* update mixtral's module_tree by @ZX-ModelCloud in https://github.com/ModelCloud/GPTQModel/pull/2480
* Fix CI by @Qubitium in https://github.com/ModelCloud/GPTQModel/pull/2481
* [CI] add pypi as backup by @CSY-ModelCloud in https://github.com/ModelCloud/GPTQModel/pull/2482
* Ci fixes 2 by @Qubitium in https://github.com/ModelCloud/GPTQModel/pull/2483
* CI Tests Fix 3 by @Qubitium in https://github.com/ModelCloud/GPTQModel/pull/2484
* [CI] fix old models need old transformers by @CSY-ModelCloud in https://github.com/ModelCloud/GPTQModel/pull/2485
* fix failed test by @ZX-ModelCloud in https://github.com/ModelCloud/GPTQModel/pull/2486
* [CI] install latest bitblas & fix missing pkgs by @CSY-ModelCloud in https://github.com/ModelCloud/GPTQModel/pull/2487
* BaiChuan fix by @Qubitium in https://github.com/ModelCloud/GPTQModel/pull/2488
* Ci fix 5 by @Qubitium in https://github.com/ModelCloud/GPTQModel/pull/2489
* Shelll/Src module buffer registratio mismatch + Qwen 2.5 VL patch by @Qubitium in https://github.com/ModelCloud/GPTQModel/pull/2490
* [CI] install latest evalplus wheel by @CSY-ModelCloud in https://github.com/ModelCloud/GPTQModel/pull/2492
* [CI] throw error for fast check by @CSY-ModelCloud in https://github.com/ModelCloud/GPTQModel/pull/2493
* [FIX] test_post_quant_eora by @ZX-ModelCloud in https://github.com/ModelCloud/GPTQModel/pull/2494
* llama 3.2 gptq + marlin score update by @Qubitium in https://github.com/ModelCloud/GPTQModel/pull/2495
* [CI] fix pkg was installed twice if common list has one by @CSY-ModelCloud in https://github.com/ModelCloud/GPTQModel/pull/2497
* fix rotary/embedding config hf compat with older models and older hf by @Qubitium in https://github.com/ModelCloud/GPTQModel/pull/2496
* Update HFKernelLinear selection by @jiqing-feng in https://github.com/ModelCloud/GPTQModel/pull/2498
* fix awq llama test scores by @Qubitium in https://github.com/ModelCloud/GPTQModel/pull/2499
* fix ci test import/env by @Qubitium in https://github.com/ModelCloud/GPTQModel/pull/2500
* fix ci test by @ZX-ModelCloud in https://github.com/ModelCloud/GPTQModel/pull/2501
* Ci test bloom by @Qubitium in https://github.com/ModelCloud/GPTQModel/pull/2502
* CI: Use generate_stable_with_limit by @Qubitium in https://github.com/ModelCloud/GPTQModel/pull/2503
* [CI] test_multi_gpu_inference will get 5 GPUs by @CSY-ModelCloud in https://github.com/ModelCloud/GPTQModel/pull/2504
* hard deprecate exllama v1 kernel by @Qubitium in https://github.com/ModelCloud/GPTQModel/pull/2505
* [CI] fix multi-gpu by @CSY-ModelCloud in https://github.com/ModelCloud/GPTQModel/pull/2506
* fix qwen3-vl compat by @Qubitium in https://github.com/ModelCloud/GPTQModel/pull/2507
* Oss compat fix by @Qubitium in https://github.com/ModelCloud/GPTQModel/pull/2508
* missing arg by @Qubitium in https://github.com/ModelCloud/GPTQModel/pull/2509
* threaded timing needs warmup protection by @Qubitium in https://github.com/ModelCloud/GPTQModel/pull/2510
* bitblas arch fallback protection by @Qubitium in https://github.com/ModelCloud/GPTQModel/pull/2511
* baichun fix: 1) rotary compat 2) buffers not correctly registered by @Qubitium in https://github.com/ModelCloud/GPTQModel/pull/2512
* add missing by @Qubitium in https://github.com/ModelCloud/GPTQModel/pull/2513
* refractor awq weight mean cpu/cuda paths by @Qubitium in https://github.com/ModelCloud/GPTQModel/pull/2514
* Qwen 3 [MoE/VL/Omni/Next] Compat by @Qubitium in https://github.com/ModelCloud/GPTQModel/pull/2515
* Ci qwen2 compat by @Qubitium in https://github.com/ModelCloud/GPTQModel/pull/2516
* defuser and meta/offload fixes by @Qubitium in https://github.com/ModelCloud/GPTQModel/pull/2517
* hf transformer/optimum compat by @Qubitium in https://github.com/ModelCloud/GPTQModel/pull/2518
* Ci fix 11 by @Qubitium in https://github.com/ModelCloud/GPTQModel/pull/2519
* fix mmlupro compat by @Qubitium in https://github.com/ModelCloud/GPTQModel/pull/2520
* tokenicer update for model compat by @Qubitium in https://github.com/ModelCloud/GPTQModel/pull/2521
* add fast/slow mode for ci testing by @Qubitium in https://github.com/ModelCloud/GPTQModel/pull/2522
* fix bitblas kernel accuracy by enabling fp32 accumulation by @Qubitium in https://github.com/ModelCloud/GPTQModel/pull/2523
* [CI] Clean up transformers dependencies in deps.yaml by @CSY-ModelCloud in https://github.com/ModelCloud/GPTQModel/pull/2525
* [CI] max-parallel jobs -> 6 by @CSY-ModelCloud in https://github.com/ModelCloud/GPTQModel/pull/2527
* fix ci test by @ZX-ModelCloud in https://github.com/ModelCloud/GPTQModel/pull/2526
* add bitblas awq kernel by @Qubitium in https://github.com/ModelCloud/GPTQModel/pull/2524
* [CI] print env after all installations by @CSY-ModelCloud in https://github.com/ModelCloud/GPTQModel/pull/2528
* use layer-level dynamic skip for fast quant by @ZX-ModelCloud in https://github.com/ModelCloud/GPTQModel/pull/2529
* TorchFused: Add fp32 dtype support & fix AWQ dequantize by @jiqing-feng in https://github.com/ModelCloud/GPTQModel/pull/2531
* [CI] install bitblas for test_awq_bitblas by @CSY-ModelCloud in https://github.com/ModelCloud/GPTQModel/pull/2532
* [CI] fix pipline exit code was covered by @CSY-ModelCloud in https://github.com/ModelCloud/GPTQModel/pull/2533
* [CI] add missing deps & delete unneeded test by @CSY-ModelCloud in https://github.com/ModelCloud/GPTQModel/pull/2534
* use local model path & [CI] add HF_TOKEN for CI by @CSY-ModelCloud in https://github.com/ModelCloud/GPTQModel/pull/2535
* Bitblas gptq bf16 fix by @Qubitium in https://github.com/ModelCloud/GPTQModel/pull/2530
* Stop quantization early if all subsequent layers are skipped  by @ZX-ModelCloud in https://github.com/ModelCloud/GPTQModel/pull/2536
* [CI] set MAX_JOBS to nproc by @CSY-ModelCloud in https://github.com/ModelCloud/GPTQModel/pull/2539
* fix model's path by @CSY-ModelCloud in https://github.com/ModelCloud/GPTQModel/pull/2540
* Fix bitblas qzero remap regression by @Qubitium in https://github.com/ModelCloud/GPTQModel/pull/2541
* granite non-standard paramter turtle/shell sync issue by @Qubitium in https://github.com/ModelCloud/GPTQModel/pull/2542
* phi4 compat fix by @Qubitium in https://github.com/ModelCloud/GPTQModel/pull/2543
* nemotron ultra compat by @Qubitium in https://github.com/ModelCloud/GPTQModel/pull/2544
* call defuser.replace_fused_blocks() by @ZX-ModelCloud in https://github.com/ModelCloud/GPTQModel/pull/2545
* auto force fp16 for awq when working kernel does not support bf16 by @Qubitium in https://github.com/ModelCloud/GPTQModel/pull/2546
* bump defuser to 0.0.12 by @CSY-ModelCloud in https://github.com/ModelCloud/GPTQModel/pull/2547
* [FIX] replace random-based string generator with secrets by @ZX-ModelCloud in https://github.com/ModelCloud/GPTQModel/pull/2549
* [CI] fix bitblas cache invalid ELF header by @CSY-ModelCloud in https://github.com/ModelCloud/GPTQModel/pull/2548
* [FIX] `quant_log.csv` was not saved upon completion of AWQ quantization by @ZX-ModelCloud in https://github.com/ModelCloud/GPTQModel/pull/2550
* [CI] remove unused parameters by @CSY-ModelCloud in https://github.com/ModelCloud/GPTQModel/pull/2551
* Ci fix ovis 1 6 by @Qubitium in https://github.com/ModelCloud/GPTQModel/pull/2552
* [CI] compile with python build module & fix git files failed by @CSY-ModelCloud in https://github.com/ModelCloud/GPTQModel/pull/2554
* patch yi and glm4v by @Qubitium in https://github.com/ModelCloud/GPTQModel/pull/2553
* Update requirements.txt by @Qubitium in https://github.com/ModelCloud/GPTQModel/pull/2555
* upgrade defuser to 0.0.15 by @ZX-ModelCloud in https://github.com/ModelCloud/GPTQModel/pull/2557
* Compat regression fix by @Qubitium in https://github.com/ModelCloud/GPTQModel/pull/2556
* update marin score slow by @Qubitium in https://github.com/ModelCloud/GPTQModel/pull/2558
* [CI] revert build by @CSY-ModelCloud in https://github.com/ModelCloud/GPTQModel/pull/2561
* update require defuser version to 0.0.15 by @ZX-ModelCloud in https://github.com/ModelCloud/GPTQModel/pull/2562
* [CI] use python -m build -w --no-isolation by @CSY-ModelCloud in https://github.com/ModelCloud/GPTQModel/pull/2563
* update `module_tree` for `phimoe` by @ZX-ModelCloud in https://github.com/ModelCloud/GPTQModel/pull/2564
* [CI] remove torch 2.9.1 build by @CSY-ModelCloud in https://github.com/ModelCloud/GPTQModel/pull/2565
* [CI] fix vllm test  in test_eval by @CSY-ModelCloud in https://github.com/ModelCloud/GPTQModel/pull/2566
* update readme by @Qubitium in https://github.com/ModelCloud/GPTQModel/pull/2567
* fix ci test by @ZX-ModelCloud in https://github.com/ModelCloud/GPTQModel/pull/2568
* [FIX] test_chatglm by @ZX-ModelCloud in https://github.com/ModelCloud/GPTQModel/pull/2569
* fix test_chatglm_test by @ZX-ModelCloud in https://github.com/ModelCloud/GPTQModel/pull/2570
* Emit version by @Qubitium in https://github.com/ModelCloud/GPTQModel/pull/2571
* add torch 2.10 wheels by @Qubitium in https://github.com/ModelCloud/GPTQModel/pull/2572
* update logbar by @Qubitium in https://github.com/ModelCloud/GPTQModel/pull/2574

## New Contributors
* @blazingbhavneek made their first contribution in https://github.com/ModelCloud/GPTQModel/pull/2422
* @beomchan0 made their first contribution in https://github.com/ModelCloud/GPTQModel/pull/2444

**Full Changelog**: https://github.com/ModelCloud/GPTQModel/compare/v5.7.0...v5.8.0

## v6.0.3 (2026-04-02)

## Notable Changes: 

  ### Quantization and inference

  - Major ParoQuant improvements across speed, inference, and accuracy.
  - Added Paro inference support and a new layer optimizer.
  - Auto-enables AMP for the fast Paro implementation to better match reference behavior.
  - Added Paro rotation autotuning and fixed BF16 rotation support for the fused CUDA kernel.
  - Improved Paro stability with seeding fixes, cleanup, learned channel scale clamping, and contiguous tensor handling fixes.
  - Fixed a layer output replay/re-capture regression.
  - Added FOEM (First-Order Error Matters) for more accurate quantized LLM compensation, plus follow-up fixes to its data processing pipeline.
  - Replaced the old marlin_fp16 backend behavior with environment-flag control for FP32 reduction.

  ### Model and backend support

  - Added support for Gemma4, MiniCPMO, MiniCPMV, and GLM4-MoE-Lite.
  - Added PrismML/Bonsai model support for inference.
  - Fixed Qwen3_5QModel definition issues.
  - Fixed Qwen 3.5 rotary embedding behavior.
  - Fixed AWQ layer grouping for qwen3_5_moe, llama4, qwen2_moe, and qwen3_next.
  - Fixed awq_processor.dynamic so skipped layers are handled correctly.
  - Improved dtype compatibility.
  - Hugging Face kernels are now gated off on Python no-GIL builds until upstream wheel support is fixed.

  ### Evaluation, calibration, and usability

  - Integrated Evalution into the workflow.
  - Added evalution.VLLM and evalution.SGLang backends.
  - Fixed SGLang evaluation engine initialization.
  - Automatically determines MODEL_COMPAT_FAST_LAYER_COUNT.
  - Improved calibration data device handling.
  - Updated tokenizer handling, and collation now respects tokenizer padding_size.
  - Improved import performance by lazy-loading _DEVICE_THREAD_POOL.
  - Cleaned up warning behavior and added an option to suppress warnings.
  - Removed forced random seed overrides.

  ### Dependency and compatibility updates

  - Updated pypcre to 0.2.14.
  - Pinned logbar to >=0.4.1.
  - Updated transformers and defuser package versions.
  - Fixed SAVE_PATH handling and import path resolution issues.

### Breaking and removed

  - Removed GPTQModel.upload_to_hub().
  - Removed MLX export support.

## What's Changed
* [CI] fix pkgs' order & fix flashinfer version was overridden by @CSY-ModelCloud in https://github.com/ModelCloud/GPTQModel/pull/2575
* allow to disable warning by @CSY-ModelCloud in https://github.com/ModelCloud/GPTQModel/pull/2576
* lazy load _DEVICE_THREAD_POOL, to speed up import by @CSY-ModelCloud in https://github.com/ModelCloud/GPTQModel/pull/2577
* remove disable env check by @CSY-ModelCloud in https://github.com/ModelCloud/GPTQModel/pull/2578
* [CI] no need to set MAX_JOBS by @CSY-ModelCloud in https://github.com/ModelCloud/GPTQModel/pull/2579
* Update pypcre version to 0.2.14 by @Qubitium in https://github.com/ModelCloud/GPTQModel/pull/2581
* Nothing to see here... by @Qubitium in https://github.com/ModelCloud/GPTQModel/pull/2456
* dtype compat by @Qubitium in https://github.com/ModelCloud/GPTQModel/pull/2582
* fix test_moe_config by @ZX-ModelCloud in https://github.com/ModelCloud/GPTQModel/pull/2583
* fix new format test by @ZX-ModelCloud in https://github.com/ModelCloud/GPTQModel/pull/2586
* [CI] add test config by @CSY-ModelCloud in https://github.com/ModelCloud/GPTQModel/pull/2587
* fix Qwen3_5QModel definition by @ZX-ModelCloud in https://github.com/ModelCloud/GPTQModel/pull/2588
* speed up paroquant quant speed and resolve accuracy issues by @Qubitium in https://github.com/ModelCloud/GPTQModel/pull/2590
* append last commit to version by @CSY-ModelCloud in https://github.com/ModelCloud/GPTQModel/pull/2591
* speedup paroquant test by @ZX-ModelCloud in https://github.com/ModelCloud/GPTQModel/pull/2592
* [CI] generate release matrix from torch registry by @CSY-ModelCloud in https://github.com/ModelCloud/GPTQModel/pull/2593
* Evalution integration by @Qubitium in https://github.com/ModelCloud/GPTQModel/pull/2585
* move eval.sh to tests by @Qubitium in https://github.com/ModelCloud/GPTQModel/pull/2594
* remove warning by @Qubitium in https://github.com/ModelCloud/GPTQModel/pull/2595
* [CI] use new docker image by @CSY-ModelCloud in https://github.com/ModelCloud/GPTQModel/pull/2596
* [CI] install required pkg by @CSY-ModelCloud in https://github.com/ModelCloud/GPTQModel/pull/2597
* Automatically Determine MODEL_COMPAT_FAST_LAYER_COUNT by @ZX-ModelCloud in https://github.com/ModelCloud/GPTQModel/pull/2598
* [CI] no need to set MAX_JOBS by @CSY-ModelCloud in https://github.com/ModelCloud/GPTQModel/pull/2599
* Fix: Paroquant impl accuracy by @Qubitium in https://github.com/ModelCloud/GPTQModel/pull/2601
* remove forced random seed override in cls proper by @Qubitium in https://github.com/ModelCloud/GPTQModel/pull/2603
* Paro test by @Qubitium in https://github.com/ModelCloud/GPTQModel/pull/2604
* [FIX] incorrect SAVE_PATH by @ZX-ModelCloud in https://github.com/ModelCloud/GPTQModel/pull/2605
* pin logbar to >= 0.4.1 by @Qubitium in https://github.com/ModelCloud/GPTQModel/pull/2606
* Update the evalution scores by @ZX-ModelCloud in https://github.com/ModelCloud/GPTQModel/pull/2600
* Paro: auto enable amp for fast impl to sync with reference by @Qubitium in https://github.com/ModelCloud/GPTQModel/pull/2607
* paro: fix seeding and cleanup by @Qubitium in https://github.com/ModelCloud/GPTQModel/pull/2609
* gate hf kernel to non-nogil builds of python until upsteram fix wheels by @Qubitium in https://github.com/ModelCloud/GPTQModel/pull/2610
* [CI] use Ubuntu 24.04 docker image by @CSY-ModelCloud in https://github.com/ModelCloud/GPTQModel/pull/2612
* Fix layer output re-capture (replay) regression by @Qubitium in https://github.com/ModelCloud/GPTQModel/pull/2611
* remove legacy ppl codes by @Qubitium in https://github.com/ModelCloud/GPTQModel/pull/2613
* replace marlin_fp16 backend with env flag control for fp32 reduction … by @Qubitium in https://github.com/ModelCloud/GPTQModel/pull/2614
* [CI] default py 3.14t & install latest Evalution by @CSY-ModelCloud in https://github.com/ModelCloud/GPTQModel/pull/2616
* [CI] fix Evalution is private by @CSY-ModelCloud in https://github.com/ModelCloud/GPTQModel/pull/2617
* updat tokenicer by @Qubitium in https://github.com/ModelCloud/GPTQModel/pull/2618
* make collate respect tokenier padding_size by @Qubitium in https://github.com/ModelCloud/GPTQModel/pull/2620
* paro: clamp learned channel scales to avoid collapse by @Qubitium in https://github.com/ModelCloud/GPTQModel/pull/2622
* Calibration data device by @avtc in https://github.com/ModelCloud/GPTQModel/pull/2608
* [FIX] qwen3_5 rotary_embedding by @ZX-ModelCloud in https://github.com/ModelCloud/GPTQModel/pull/2624
* Temporarily disable gptqmodel spit_by feature by @ZX-ModelCloud in https://github.com/ModelCloud/GPTQModel/pull/2625
* use evalution.VLLM by @CSY-ModelCloud in https://github.com/ModelCloud/GPTQModel/pull/2615
* use evalution.SGLang by @ZX-ModelCloud in https://github.com/ModelCloud/GPTQModel/pull/2626
* paro: enter the dragon by @Qubitium in https://github.com/ModelCloud/GPTQModel/pull/2623
* [CI] use torch 2.11 by @CSY-ModelCloud in https://github.com/ModelCloud/GPTQModel/pull/2627
* [FIX] sglang evaluation engine initialization error. by @ZX-ModelCloud in https://github.com/ModelCloud/GPTQModel/pull/2629
* [MODEL] Add minicpmo support by @ZX-ModelCloud in https://github.com/ModelCloud/GPTQModel/pull/2630
* [CI] update CI path by @CSY-ModelCloud in https://github.com/ModelCloud/GPTQModel/pull/2633
* [FIX] qwen3_5_moe / llama4 / qwen2_moe / qwen3_next  awq layer grouping  by @ZX-ModelCloud in https://github.com/ModelCloud/GPTQModel/pull/2634
* Remove GPTQModel.upload_to_hub() api by @ZX-ModelCloud in https://github.com/ModelCloud/GPTQModel/pull/2635
* remove export to mlx option by @ZX-ModelCloud in https://github.com/ModelCloud/GPTQModel/pull/2636
* [MODEL] supports minicpmv by @ZX-ModelCloud in https://github.com/ModelCloud/GPTQModel/pull/2637
* Paro: layer optimizer by @Qubitium in https://github.com/ModelCloud/GPTQModel/pull/2628
* Paro inference by @Qubitium in https://github.com/ModelCloud/GPTQModel/pull/2638
* PrismAI/Bonsai Model Support (inference only) by @Qubitium in https://github.com/ModelCloud/GPTQModel/pull/2640
* Update README.md by @Qubitium in https://github.com/ModelCloud/GPTQModel/pull/2641
* Update transformers and defuser package versions by @Qubitium in https://github.com/ModelCloud/GPTQModel/pull/2642
* [CI] install gguf for test_local_model_paths by @CSY-ModelCloud in https://github.com/ModelCloud/GPTQModel/pull/2645
* fix imported path not found by @CSY-ModelCloud in https://github.com/ModelCloud/GPTQModel/pull/2646
* [MODEL] support glm4_moe_lite by @ZX-ModelCloud in https://github.com/ModelCloud/GPTQModel/pull/2644
* [FEATURE] Add `FOEM`: First-Order Error Matters; Accurate Compensation for Quantized LLM by @Xingyu-Zheng in https://github.com/ModelCloud/GPTQModel/pull/2639
* Revise README with latest news and article references by @Qubitium in https://github.com/ModelCloud/GPTQModel/pull/2647
* FIX paroquant bf16 rotation support for fused cuda kernel by @Qubitium in https://github.com/ModelCloud/GPTQModel/pull/2648
* paroquant rotation autotune  by @Qubitium in https://github.com/ModelCloud/GPTQModel/pull/2649
* [FIX] In `awq_processor`, `dynamic` did not correctly skip layers.  by @ZX-ModelCloud in https://github.com/ModelCloud/GPTQModel/pull/2650
* ruff fix by @Qubitium in https://github.com/ModelCloud/GPTQModel/pull/2651
* Ruff fix by @Qubitium in https://github.com/ModelCloud/GPTQModel/pull/2652
* update readme by @Qubitium in https://github.com/ModelCloud/GPTQModel/pull/2653
* fix: ensure contagious tensors by @Qubitium in https://github.com/ModelCloud/GPTQModel/pull/2655
* fix failed test by @ZX-ModelCloud in https://github.com/ModelCloud/GPTQModel/pull/2654
* [CI] move complex sh logics into py by @CSY-ModelCloud in https://github.com/ModelCloud/GPTQModel/pull/2656
* ci: direct post-quantized eval by @Qubitium in https://github.com/ModelCloud/GPTQModel/pull/2657
* fix failed test by @ZX-ModelCloud in https://github.com/ModelCloud/GPTQModel/pull/2658
* fix problems in the FOEM data processing pipeline by @Xingyu-Zheng in https://github.com/ModelCloud/GPTQModel/pull/2659
* Fix typo in latest news section of README by @Qubitium in https://github.com/ModelCloud/GPTQModel/pull/2660
* fix sdist version by @Qubitium in https://github.com/ModelCloud/GPTQModel/pull/2661
* Update README.md by @Qubitium in https://github.com/ModelCloud/GPTQModel/pull/2662
* add gemma4 by @Qubitium in https://github.com/ModelCloud/GPTQModel/pull/2663
* fix cpu fallback device restore by @Qubitium in https://github.com/ModelCloud/GPTQModel/pull/2664
* Update README.md by @Qubitium in https://github.com/ModelCloud/GPTQModel/pull/2665

## New Contributors
* @Xingyu-Zheng made their first contribution in https://github.com/ModelCloud/GPTQModel/pull/2639

**Full Changelog**: https://github.com/ModelCloud/GPTQModel/compare/v5.8.0...v6.0.3

## v7.0.0 (2026-04-28)

### 🔥 Major
- New Huawei Ascend NPU quantization support with torch based kernels for inference
- All CUDA/ROCm compiled kernels are now JIT (just-in-time) compiled on first use
-  Pip/UV install no longer requires the `--no-build-isolation` flag

### 🧠 New model support and compatibility wins

- Added support for GLM 5/5.1, GLM OCR, GLM ASR, Gemma 3n, Falcon Mamba, and InternVL Chat.
- Extended OpenVINO GPTQ patching to understand GPTQModel's newer kernels.
- Fixed Qwen3 dtype handling, Qwen3.5 MoE module-tree assertions, Qwen2-VL calibration input capture, and Qwen 3.6 MoE regressions.
- Fixed Llama4Router replacement behavior, Phi-3 defused MLP module mapping, Phi-4 runtime requirements, Instella rope-scaling compatibility, Ling compatibility, Mixtral MoE checkpoint module names, Brumby thread safety, Baichuan compatibility, and Gemma
3 saving.
- Fixed `exllamav3_torch` import under meta-device context.

### ⚡ Kernels, JIT, and hardware acceleration

- Moved all compilation required kernels to JIT compilation on first-use and cleaned up Marlin import probing, CUDA header handling, nvcc flag checks, and Torch/CUDA mismatch handling.
- Synced Marlin/Machete kernels with upstream and added hardware-specific Marlin boost paths.
- Guarded CUTLASS version mismatches and fixed generated-kernel staleness.
- Added global kernel rebuild support for CI and safer shared extension locks.
- Added Ascend NPU support.
- Fixed AWQ JIT cache invalidation, illegal memory access, SM120 execution, GEMM_Fast shared-memory launch, and BF16 bias validation.
- Fixed `BACKEND.MARLIN` loading for `gptq_v2` format and added Marlin import coverage.

### 🔥 Quantization, AWQ, FP8, and dequant

- Added FP8/FP4 CPU dequant and DeepSeek FP8 `.scale` dequant export.
- Added dtype auto-decoding and decode path updates.
- Reduced AWQ scale-search activation memory and split AWQ integration tests for cleaner coverage.
- Fail fast on unsupported act-group-aware GPTQ shapes instead of continuing into invalid layouts.
- Fixed INT3 qzero format conversion, GAR width compatibility, and GPTQ batched keep-mask handling.
- Improved AWQ W4A8 and BF16 validation paths, plus post-quant MoE routing behavior.
- Used loader device selection for EoRA adapter generation.

### 🐢 LazyTurtle, loading, and model plumbing

- Refactored input capture into `BaseQModel` and model-specific QModels for cleaner replay and calibration flows.
- Renamed and hardened the turtle path into LazyTurtle, with stricter materialization failures and better expected-skip handling.
- Fixed LazyTurtle materialization for non-square fused experts, PhiMoE, nested HF weight renames, reversed `WeightRenaming` semantics, and non-Safetensors checkpoints.
- Improved out-of-model tensor handling for MTP `prefix/files` paths.
- Removed `BaseModel.loader_requires_dtype` and normalized config dtype handling through `get_hf_config_dtype()`.
- Fixed multi-GPU replay output retention, GPTQ finalizer overlap, and quantization OOMs from retained callable cache keys.


### 🧰 CI, packaging, and developer workflow

- Cleaned up CI shell logic, environment setup, UV cache handling, reusable Torch tests, CPU-only grouping, runner selection, retry behavior, and offload temp paths.
- Kept CI and Torch CUDA versions aligned, moved to newer Docker images, and surfaced real exit codes and GPU names.
- Removed `lm-eval`, deprecated tests, deprecated artifact IDs, pause UI lifecycle code, and tabulate from CI/test paths.
- Migrated more regex usage to pcre/pcre2.
- Replaced temp path helpers with `tempfile.TemporaryDirectory()` for automatic cleanup.
- Updated requirements, dependencies, setuptools compatibility, and install-with-Torch validation.

## 💥 Breaking and removed

- Kernel loading behavior has shifted heavily toward JIT compilation, so custom deployment environments should verify compiler/CUDA compatibility.
- `lm-eval` references were removed from CI and test/docs paths.
- Deprecated tests, artifact handling, and pause UI lifecycle code were removed.

## Full Changelog:

* Refactor input capture flow into BaseQModel and model-specific QModels by @ZX-ModelCloud in https://github.com/ModelCloud/GPTQModel/pull/2666
* [CI] adjust venv logic by @CSY-ModelCloud in https://github.com/ModelCloud/GPTQModel/pull/2667
* [CI] remove verbose log flag for build by @CSY-ModelCloud in https://github.com/ModelCloud/GPTQModel/pull/2669
* Move more kernels to JIT compile path by @Qubitium in https://github.com/ModelCloud/GPTQModel/pull/2668
* Kernels migrate to jit compile by @Qubitium in https://github.com/ModelCloud/GPTQModel/pull/2670
* remove hf kernels dependency for cpu by @Qubitium in https://github.com/ModelCloud/GPTQModel/pull/2671
* fix marlin import paths probe by @Qubitium in https://github.com/ModelCloud/GPTQModel/pull/2673
* fix failed test by @Qubitium in https://github.com/ModelCloud/GPTQModel/pull/2674
* Extend OpenVINO's GPTQ patcher to understand GPTQModel new kernels. by @ZX-ModelCloud in https://github.com/ModelCloud/GPTQModel/pull/2675
* [CI] use same cuda version for CI & torch by @CSY-ModelCloud in https://github.com/ModelCloud/GPTQModel/pull/2676
* Handle mtp `prefix/files`in `out_of_model_tensors` by @ZX-ModelCloud in https://github.com/ModelCloud/GPTQModel/pull/2677
* bonsai refractor by @Qubitium in https://github.com/ModelCloud/GPTQModel/pull/2672
* glm 5/5.1 support by @Qubitium in https://github.com/ModelCloud/GPTQModel/pull/2680
* Normalize config `dtype` to `torch.dtype` in `get_hf_config_dtype()` by @ZX-ModelCloud in https://github.com/ModelCloud/GPTQModel/pull/2681
* [FIX] Qwen3ForCausalLM does not require the `dtype` argument. by @ZX-ModelCloud in https://github.com/ModelCloud/GPTQModel/pull/2682
* fix jit error because torch's cuda mismatchs local nvcc version by @CSY-ModelCloud in https://github.com/ModelCloud/GPTQModel/pull/2683
* fix: rotary_embed init by @Qubitium in https://github.com/ModelCloud/GPTQModel/pull/2684
* remove BaseModel.loader_requires_dtype by @ZX-ModelCloud in https://github.com/ModelCloud/GPTQModel/pull/2686
* [CI] no need build step by @CSY-ModelCloud in https://github.com/ModelCloud/GPTQModel/pull/2688
* refractor turtle to lazy by @Qubitium in https://github.com/ModelCloud/GPTQModel/pull/2687
* [CI] fix jobs are skipped by @CSY-ModelCloud in https://github.com/ModelCloud/GPTQModel/pull/2689
* [FIX] multi-GPU replay output retention OOM by @ZX-ModelCloud in https://github.com/ModelCloud/GPTQModel/pull/2692
* fp8/fp4 cpu dequant by @Qubitium in https://github.com/ModelCloud/GPTQModel/pull/2691
* refactor all monekypatches to use same lock by @ZX-ModelCloud in https://github.com/ModelCloud/GPTQModel/pull/2693
* [CI] decrease max parallel jobs to 4 by @CSY-ModelCloud in https://github.com/ModelCloud/GPTQModel/pull/2695
* [FIX] All cpp extensions should share the same lock instead of using a map of locks by @ZX-ModelCloud in https://github.com/ModelCloud/GPTQModel/pull/2696
* dtype auto decoder by @Qubitium in https://github.com/ModelCloud/GPTQModel/pull/2690
* Decode update by @Qubitium in https://github.com/ModelCloud/GPTQModel/pull/2698
* refractor processors by @Qubitium in https://github.com/ModelCloud/GPTQModel/pull/2697
* fix cuda header path conflict by @Qubitium in https://github.com/ModelCloud/GPTQModel/pull/2701
* [CI] add prefix for env name by @CSY-ModelCloud in https://github.com/ModelCloud/GPTQModel/pull/2704
* ignore .codex by @CSY-ModelCloud in https://github.com/ModelCloud/GPTQModel/pull/2703
* fix: stabilize baichuan compat test by @Qubitium in https://github.com/ModelCloud/GPTQModel/pull/2702
* Fix Qwen3.5 MoE module tree assertion by @Qubitium in https://github.com/ModelCloud/GPTQModel/pull/2705
* [CI] remove UV_INDEX_URL by @CSY-ModelCloud in https://github.com/ModelCloud/GPTQModel/pull/2706
* Fix: LazyTurtle materialization for non-square fused experts by @ZX-ModelCloud in https://github.com/ModelCloud/GPTQModel/pull/2707
* [CI] uv won't R/W /monster now by @CSY-ModelCloud in https://github.com/ModelCloud/GPTQModel/pull/2708
* Fix AWQ JIT cache invalidation by @Qubitium in https://github.com/ModelCloud/GPTQModel/pull/2709
* Split AWQ integration tests by @Qubitium in https://github.com/ModelCloud/GPTQModel/pull/2710
* Fix CI to install ModelCloud deps from git by @Qubitium in https://github.com/ModelCloud/GPTQModel/pull/2711
* migrate stdlib.re to pcre2 by @Qubitium in https://github.com/ModelCloud/GPTQModel/pull/2712
* [CI] show real exit code by @CSY-ModelCloud in https://github.com/ModelCloud/GPTQModel/pull/2713
* Remove lm-eval from CI and test/docs references by @Qubitium in https://github.com/ModelCloud/GPTQModel/pull/2714
* Remove pause UI controller lifecycle by @Qubitium in https://github.com/ModelCloud/GPTQModel/pull/2715
* [CI] re-mount /monster for uv by @CSY-ModelCloud in https://github.com/ModelCloud/GPTQModel/pull/2718
* Sync Marlin/Machete Kernel with upstream by @Qubitium in https://github.com/ModelCloud/GPTQModel/pull/2717
* Fix GPU CI allocation and streaming regressions by @Qubitium in https://github.com/ModelCloud/GPTQModel/pull/2719
* Guard CUTLASS version mismatches by @Qubitium in https://github.com/ModelCloud/GPTQModel/pull/2720
* Fix Marlin generated kernel staleness by @Qubitium in https://github.com/ModelCloud/GPTQModel/pull/2721
* Fix balanced MoE vram usage by @Qubitium in https://github.com/ModelCloud/GPTQModel/pull/2716
* Fix bias dtype and validate AWQ bf16 ops by @Qubitium in https://github.com/ModelCloud/GPTQModel/pull/2722
* Raise on LazyTurtle materialization failures and silence expected skips by @ZX-ModelCloud in https://github.com/ModelCloud/GPTQModel/pull/2723
* HW specific boost for Marlin by @Qubitium in https://github.com/ModelCloud/GPTQModel/pull/2724
* Update requirements.txt by @Qubitium in https://github.com/ModelCloud/GPTQModel/pull/2725
* [CI] share common venvs & add lock when installing pkgs by @CSY-ModelCloud in https://github.com/ModelCloud/GPTQModel/pull/2726
* [CI] set uv cache for differrent envs by @CSY-ModelCloud in https://github.com/ModelCloud/GPTQModel/pull/2728
* [FIX] Mixtral MoE checkpoint module name may not match modeling code by @ZX-ModelCloud in https://github.com/ModelCloud/GPTQModel/pull/2727
* Delete redundant AWQ logs. by @ZX-ModelCloud in https://github.com/ModelCloud/GPTQModel/pull/2731
* [CI] clean sh codes, simpilify logic by @CSY-ModelCloud in https://github.com/ModelCloud/GPTQModel/pull/2730
* Sync setuptools by @Qubitium in https://github.com/ModelCloud/GPTQModel/pull/2732
* [CI] test install with torch by @CSY-ModelCloud in https://github.com/ModelCloud/GPTQModel/pull/2733
* [CI] update release CI to latest docker by @CSY-ModelCloud in https://github.com/ModelCloud/GPTQModel/pull/2734
* [CI] check setuptools compatibility by @CSY-ModelCloud in https://github.com/ModelCloud/GPTQModel/pull/2735
* [CI] fix compat test by @CSY-ModelCloud in https://github.com/ModelCloud/GPTQModel/pull/2736
* [CI] remvoe unused params by @CSY-ModelCloud in https://github.com/ModelCloud/GPTQModel/pull/2737
* Disable MoE routing config in post-quant forawrd by @ZX-ModelCloud in https://github.com/ModelCloud/GPTQModel/pull/2738
* file cleanup by @Qubitium in https://github.com/ModelCloud/GPTQModel/pull/2740
* [CI] mount ci host path as uv cache dir by @CSY-ModelCloud in https://github.com/ModelCloud/GPTQModel/pull/2741
* marlin: cleanup by @Qubitium in https://github.com/ModelCloud/GPTQModel/pull/2742
* Fix nvcc flag check by @Qubitium in https://github.com/ModelCloud/GPTQModel/pull/2745
* [FIX] Avoid replacing modules like Llama4Router with HookedLinear by @ZX-ModelCloud in https://github.com/ModelCloud/GPTQModel/pull/2744
* Update depends by @Qubitium in https://github.com/ModelCloud/GPTQModel/pull/2746
* [CI] show gpu name on response by @CSY-ModelCloud in https://github.com/ModelCloud/GPTQModel/pull/2747
* [CI] no sn by @CSY-ModelCloud in https://github.com/ModelCloud/GPTQModel/pull/2748
* fix brumby compat, thread safety by @Qubitium in https://github.com/ModelCloud/GPTQModel/pull/2749
* [CI] always start with a new clean env by @CSY-ModelCloud in https://github.com/ModelCloud/GPTQModel/pull/2750
* Add Qwen 3.6 MoE quantization regressions by @Qubitium in https://github.com/ModelCloud/GPTQModel/pull/2752
* [FIX] phimoe quantization error with LazyTurtle by @ZX-ModelCloud in https://github.com/ModelCloud/GPTQModel/pull/2754
* [CI] refactor CI & mark no gpu tests by @CSY-ModelCloud in https://github.com/ModelCloud/GPTQModel/pull/2755
* [CI] no gpu tests first by @CSY-ModelCloud in https://github.com/ModelCloud/GPTQModel/pull/2756
* fix model def tree execution order ground truth by @Qubitium in https://github.com/ModelCloud/GPTQModel/pull/2753
* [CI] fix CI cannot get runner group, use cpu model instead by @CSY-ModelCloud in https://github.com/ModelCloud/GPTQModel/pull/2758
* [CI] fix no arg for ths func by @CSY-ModelCloud in https://github.com/ModelCloud/GPTQModel/pull/2759
* Looper fix by @Qubitium in https://github.com/ModelCloud/GPTQModel/pull/2757
* [CI] late import device_smi, so no need to install it in pre env by @CSY-ModelCloud in https://github.com/ModelCloud/GPTQModel/pull/2760
* Fail fast for unsupported act-group-aware GPTQ shapes by @ZX-ModelCloud in https://github.com/ModelCloud/GPTQModel/pull/2761
* fix gar width compat by @Qubitium in https://github.com/ModelCloud/GPTQModel/pull/2762
* fix int3 qzero format conversion by @Qubitium in https://github.com/ModelCloud/GPTQModel/pull/2763
* Fix Phi-3 defused MLP module mapping by @Qubitium in https://github.com/ModelCloud/GPTQModel/pull/2765
* Fix ci exposed compat issues by @Qubitium in https://github.com/ModelCloud/GPTQModel/pull/2766
* Fix ci regressions by @Qubitium in https://github.com/ModelCloud/GPTQModel/pull/2767
* [CI] install required pkgs for tests by @CSY-ModelCloud in https://github.com/ModelCloud/GPTQModel/pull/2768
* [FIX] test_instella by @ZX-ModelCloud in https://github.com/ModelCloud/GPTQModel/pull/2769
* [CI] add compute cap requirement for special tests by @CSY-ModelCloud in https://github.com/ModelCloud/GPTQModel/pull/2770
* [CI] allow CI skip test & clean ci logic by @CSY-ModelCloud in https://github.com/ModelCloud/GPTQModel/pull/2771
* [CI] install scipy for test_phi_4 by @CSY-ModelCloud in https://github.com/ModelCloud/GPTQModel/pull/2773
* fix mmlu ValueError by @CSY-ModelCloud in https://github.com/ModelCloud/GPTQModel/pull/2774
* Reduce AWQ scale-search activation memory by @Qubitium in https://github.com/ModelCloud/GPTQModel/pull/2775
* [REFACTOR] replace `checkpoint_path_aliases` with `HF_CONVERSION_MAP_REVERSED` by @ZX-ModelCloud in https://github.com/ModelCloud/GPTQModel/pull/2776
* [CI] add log to ensure old env is removed by @CSY-ModelCloud in https://github.com/ModelCloud/GPTQModel/pull/2777
* Fix thread-local CUDA linalg warmup in threadx by @Qubitium in https://github.com/ModelCloud/GPTQModel/pull/2778
* Fix CI offload temp path handling by @Qubitium in https://github.com/ModelCloud/GPTQModel/pull/2779
* [CI] retry if failed by @CSY-ModelCloud in https://github.com/ModelCloud/GPTQModel/pull/2780
* [CI] check time instead of checking retry count by @CSY-ModelCloud in https://github.com/ModelCloud/GPTQModel/pull/2781
* Add global kernel rebuild flag for CI by @Qubitium in https://github.com/ModelCloud/GPTQModel/pull/2782
* Use thread-and-device linalg warmups by @Qubitium in https://github.com/ModelCloud/GPTQModel/pull/2783
* Add Phi-4 runtime dependency requirements by @Qubitium in https://github.com/ModelCloud/GPTQModel/pull/2784
* Fix Qwen2-VL calibration input capture by @Qubitium in https://github.com/ModelCloud/GPTQModel/pull/2785
* Fix Ling compat by @Qubitium in https://github.com/ModelCloud/GPTQModel/pull/2786
* Remove tabulate from CI tests and migrate regex to pcre by @Qubitium in https://github.com/ModelCloud/GPTQModel/pull/2787
* Fix CI bootstrap imports and env activation by @Qubitium in https://github.com/ModelCloud/GPTQModel/pull/2788
* Refractor CI  by @Qubitium in https://github.com/ModelCloud/GPTQModel/pull/2789
* Fix CI bootstrap regex dependency by @Qubitium in https://github.com/ModelCloud/GPTQModel/pull/2790
* use tempfile to replace /tmp by @CSY-ModelCloud in https://github.com/ModelCloud/GPTQModel/pull/2791
* [CI] fix matrix over 255 &  make torch tests reusable & separate cpu only tests to a new group. by @CSY-ModelCloud in https://github.com/ModelCloud/GPTQModel/pull/2792
* Align LazyTurtle HF key resolution with reversed WeightRenaming semantics by @ZX-ModelCloud in https://github.com/ModelCloud/GPTQModel/pull/2793
* [CI} clean uv cache for CI by @CSY-ModelCloud in https://github.com/ModelCloud/GPTQModel/pull/2794
* replace makeTmp() with tempfile.TemporaryDirectory(), auto clean by @CSY-ModelCloud in https://github.com/ModelCloud/GPTQModel/pull/2795
* LazyTurtle now supports loading non-Safetensors models by @ZX-ModelCloud in https://github.com/ModelCloud/GPTQModel/pull/2796
* fix awq jit illegal memory access by @CSY-ModelCloud in https://github.com/ModelCloud/GPTQModel/pull/2798
* Fix LLMAWQ execution on SM120 GPUs by @CSY-ModelCloud in https://github.com/ModelCloud/GPTQModel/pull/2799
* Use loader device selection for EoRA adapter generation by @Qubitium in https://github.com/ModelCloud/GPTQModel/pull/2800
* Fix GEMM_Fast AWQ decode kernel shared memory launch by @Qubitium in https://github.com/ModelCloud/GPTQModel/pull/2801
* [CI] don't clean whl by @CSY-ModelCloud in https://github.com/ModelCloud/GPTQModel/pull/2802
* fix marlin jit error & update CI to latest image by @CSY-ModelCloud in https://github.com/ModelCloud/GPTQModel/pull/2803
* remove deprecated test by @CSY-ModelCloud in https://github.com/ModelCloud/GPTQModel/pull/2806
* [MODEL] support `glm_ocr` and `glm_asr` model by @ZX-ModelCloud in https://github.com/ModelCloud/GPTQModel/pull/2807
* [CI] add attn_gym for test_hymba by @CSY-ModelCloud in https://github.com/ModelCloud/GPTQModel/pull/2811
* split into 2 tests & fix fast mode didn't work by @CSY-ModelCloud in https://github.com/ModelCloud/GPTQModel/pull/2812
* Fix multi-GPU GPTQ finalizer overlap by @Qubitium in https://github.com/ModelCloud/GPTQModel/pull/2808
* [CI] remove deperacated artifact_id by @CSY-ModelCloud in https://github.com/ModelCloud/GPTQModel/pull/2816
* [FIX] multi-GPU quantization OOM by canonicalizing get_supported_kwargs cache keys by @ZX-ModelCloud in https://github.com/ModelCloud/GPTQModel/pull/2815
* remove deperacated tests. lazy_load_kernel no longer calls get_kernel by @CSY-ModelCloud in https://github.com/ModelCloud/GPTQModel/pull/2814
* [MODEL] support gemma3n by @ZX-ModelCloud in https://github.com/ModelCloud/GPTQModel/pull/2817
* [CI] install missing pkgs for tests & test_llama3_2_fp8 need 5090 & update .gitignore by @CSY-ModelCloud in https://github.com/ModelCloud/GPTQModel/pull/2819
* [MODEL] support `falcon_mamba` by @ZX-ModelCloud in https://github.com/ModelCloud/GPTQModel/pull/2820
* [FIX] an error occurring during Gemma 3 saving. by @ZX-ModelCloud in https://github.com/ModelCloud/GPTQModel/pull/2822
* fix batched calibration masking by @CSY-ModelCloud in https://github.com/ModelCloud/GPTQModel/pull/2823
* fix test_mmlupro by @CSY-ModelCloud in https://github.com/ModelCloud/GPTQModel/pull/2821
* [MODEL] support `internvl_chat` by @ZX-ModelCloud in https://github.com/ModelCloud/GPTQModel/pull/2826
* Support DeepSeek FP8 .scale dequant export by @CSY-ModelCloud in https://github.com/ModelCloud/GPTQModel/pull/2827
* [FIX] `BACKEND.MARLIN` Currently correct load `gptq_v2` format by @ZX-ModelCloud in https://github.com/ModelCloud/GPTQModel/pull/2828
* skip tests, until todo fixed by @CSY-ModelCloud in https://github.com/ModelCloud/GPTQModel/pull/2829
* Fix exllamav3_torch import under meta-device context by @dblundell in https://github.com/ModelCloud/GPTQModel/pull/2825
* Add Ascend NPU support by @Qubitium in https://github.com/ModelCloud/GPTQModel/pull/2831
* add marlin import test by @CSY-ModelCloud in https://github.com/ModelCloud/GPTQModel/pull/2832
* [FIX] LazyTurtle tensor-key alias resolution for nested HF weight renames by @ZX-ModelCloud in https://github.com/ModelCloud/GPTQModel/pull/2835

## New Contributors
* @dblundell made their first contribution in https://github.com/ModelCloud/GPTQModel/pull/2825

**Full Changelog**: https://github.com/ModelCloud/GPTQModel/compare/v6.0.3...v7.0.0

## v7.1.0 (2026-06-08)

## What's Changed
* [CI] fix release action cannot find uv & clean actions by @CSY-ModelCloud in https://github.com/ModelCloud/GPTQModel/pull/2837
* [CI] install timm for internvl chat by @CSY-ModelCloud in https://github.com/ModelCloud/GPTQModel/pull/2839
* Add Laguna model support by @Qubitium in https://github.com/ModelCloud/GPTQModel/pull/2836
* [MODEL] support `ernie4_5_vl_moe` by @ZX-ModelCloud in https://github.com/ModelCloud/GPTQModel/pull/2838
* fix AttributeError: 'NoneType' object has no attribute 'from_pretrained' by @CSY-ModelCloud in https://github.com/ModelCloud/GPTQModel/pull/2840
* Add GSM8K Platinum to Laguna regression by @Qubitium in https://github.com/ModelCloud/GPTQModel/pull/2841
* docs: update hardware support table by @Qubitium in https://github.com/ModelCloud/GPTQModel/pull/2842
* [FIX] ci test by @ZX-ModelCloud in https://github.com/ModelCloud/GPTQModel/pull/2843
* Add NPU quant method coverage by @Qubitium in https://github.com/ModelCloud/GPTQModel/pull/2845
* [FIX] AWQ device placement to follow planner target devices by @ZX-ModelCloud in https://github.com/ModelCloud/GPTQModel/pull/2847
* add nvidia/Nemotron-3-Nano-Omni-30B-A3B-Reasoning-BF16 support by @CSY-ModelCloud in https://github.com/ModelCloud/GPTQModel/pull/2846
* fix test_subset by @CSY-ModelCloud in https://github.com/ModelCloud/GPTQModel/pull/2849
* new template for Nemotron_3 test by @CSY-ModelCloud in https://github.com/ModelCloud/GPTQModel/pull/2851
* update internvl_chat pkgs by @CSY-ModelCloud in https://github.com/ModelCloud/GPTQModel/pull/2850
* add inclusionAI/Ling-2.6-flash support by @CSY-ModelCloud in https://github.com/ModelCloud/GPTQModel/pull/2844
* Refactor LazyTurtle checkpoint tensor resolution by @ZX-ModelCloud in https://github.com/ModelCloud/GPTQModel/pull/2852
* fix AttributeError: '_DummyConfig' object has no attribute 'model_type' by @CSY-ModelCloud in https://github.com/ModelCloud/GPTQModel/pull/2853
* fix apply_moe_config was not found by @CSY-ModelCloud in https://github.com/ModelCloud/GPTQModel/pull/2854
* added "qwen3_5_moe_text" definition and "qwen3_5_text" definition by @ZX-ModelCloud in https://github.com/ModelCloud/GPTQModel/pull/2857
* fix first layer was asserted, but only last 2 layers are quanted by @CSY-ModelCloud in https://github.com/ModelCloud/GPTQModel/pull/2861
* [MODEL] support "glm4v_moe" by @ZX-ModelCloud in https://github.com/ModelCloud/GPTQModel/pull/2862
* add LogBar progress to sync_all_meta() writes by @ZX-ModelCloud in https://github.com/ModelCloud/GPTQModel/pull/2860
* fix: handle float8 tensor serialization in streaming safetensors saves by @ZX-ModelCloud in https://github.com/ModelCloud/GPTQModel/pull/2863
* move causal_conv1d to gptqmodel/hf_kernels, not in root by @CSY-ModelCloud in https://github.com/ModelCloud/GPTQModel/pull/2864
* store logs file in ./logs, not in root dir by @CSY-ModelCloud in https://github.com/ModelCloud/GPTQModel/pull/2865
* [CI] fix dust or dir may mot exist by @CSY-ModelCloud in https://github.com/ModelCloud/GPTQModel/pull/2867
* fix tests/models/test_qwen3_5_text_only by @ZX-ModelCloud in https://github.com/ModelCloud/GPTQModel/pull/2866
* fix TestVoxtral::test_voxtral - IndexError: index out of range in self by @CSY-ModelCloud in https://github.com/ModelCloud/GPTQModel/pull/2870
* [CI] fix envs conflict on one host runner by @CSY-ModelCloud in https://github.com/ModelCloud/GPTQModel/pull/2871
* [FIX] test_hymba by @ZX-ModelCloud in https://github.com/ModelCloud/GPTQModel/pull/2872
* fix KeyError: 'type' & AutoTokenizer was not found by @CSY-ModelCloud in https://github.com/ModelCloud/GPTQModel/pull/2873
* [MODEL] support zamba and zamba2 by @ZX-ModelCloud in https://github.com/ModelCloud/GPTQModel/pull/2868
* no need to import AutoTokenizer which is unused by @CSY-ModelCloud in https://github.com/ModelCloud/GPTQModel/pull/2874
* [FIX] FP8 dequantization for cross-shard scales and partial edge blocks by @ZX-ModelCloud in https://github.com/ModelCloud/GPTQModel/pull/2875
* add retry to fix remote files missing in cache dir by @CSY-ModelCloud in https://github.com/ModelCloud/GPTQModel/pull/2876
* fix: preserve mtp.* tensors for dense Qwen3.5/Qwen3.6 models by @erm14254 in https://github.com/ModelCloud/GPTQModel/pull/2869
* fix 2 deps on CI by @CSY-ModelCloud in https://github.com/ModelCloud/GPTQModel/pull/2881
* fix assert was checking last layers by @CSY-ModelCloud in https://github.com/ModelCloud/GPTQModel/pull/2880
* fix rope_parameters is not inited by @CSY-ModelCloud in https://github.com/ModelCloud/GPTQModel/pull/2882
* fix AttributeError: 'FakeGPTQModel' object has no attribute '_sanitiz… by @CSY-ModelCloud in https://github.com/ModelCloud/GPTQModel/pull/2885
* [MODEL] support `minicpmv_4_6` by @ZX-ModelCloud in https://github.com/ModelCloud/GPTQModel/pull/2884
* improve JIT extension failure diagnostics for CI flakiness by @CSY-ModelCloud in https://github.com/ModelCloud/GPTQModel/pull/2886
* log stack trace for marlin jit error by @CSY-ModelCloud in https://github.com/ModelCloud/GPTQModel/pull/2887
* fix Qwen3OmniMoe throws get_input_embeddings NotImplementedError by @CSY-ModelCloud in https://github.com/ModelCloud/GPTQModel/pull/2888
* Fix dequantization for ignored layers, padded FP8 scales, and non-4D tensors by @ZX-ModelCloud in https://github.com/ModelCloud/GPTQModel/pull/2889
* fix command got wrong args by @CSY-ModelCloud in https://github.com/ModelCloud/GPTQModel/pull/2891
* print expected in error by @CSY-ModelCloud in https://github.com/ModelCloud/GPTQModel/pull/2890
* Fix InternVL tokenizer compat on transformers 5 by @CSY-ModelCloud in https://github.com/ModelCloud/GPTQModel/pull/2892
* [MODEL] support deepseek_v4 by @ZX-ModelCloud in https://github.com/ModelCloud/GPTQModel/pull/2877
* add kimi 2.5 support by @CSY-ModelCloud in https://github.com/ModelCloud/GPTQModel/pull/2858
* [CI] use torch 2.12.0 & python 3.14t as default on CI by @CSY-ModelCloud in https://github.com/ModelCloud/GPTQModel/pull/2894
* [MODEL ]support mimo_v2 by @ZX-ModelCloud in https://github.com/ModelCloud/GPTQModel/pull/2893
* [CI] auto clean cache & retry by @CSY-ModelCloud in https://github.com/ModelCloud/GPTQModel/pull/2895
* [FIX] ovis incompatibility with transformers v5 by @ZX-ModelCloud in https://github.com/ModelCloud/GPTQModel/pull/2896
* [MODEL] support `ovis2_5` by @ZX-ModelCloud in https://github.com/ModelCloud/GPTQModel/pull/2897
* fix paroquant was not included in release by @CSY-ModelCloud in https://github.com/ModelCloud/GPTQModel/pull/2900
* [CI] install release pkg instead of source by @CSY-ModelCloud in https://github.com/ModelCloud/GPTQModel/pull/2901
* [MODEL] support ovis2 6 moe by @ZX-ModelCloud in https://github.com/ModelCloud/GPTQModel/pull/2899
* [MODEL] support `interns1` by @ZX-ModelCloud in https://github.com/ModelCloud/GPTQModel/pull/2902
* [MODEL] support ovis2_6_next by @ZX-ModelCloud in https://github.com/ModelCloud/GPTQModel/pull/2904
* [MODEL] support `hrm_text` by @ZX-ModelCloud in https://github.com/ModelCloud/GPTQModel/pull/2905
* ascend kernel compat update: cann 9.1beta1 by @Qubitium in https://github.com/ModelCloud/GPTQModel/pull/2906
* fix test_subset.py by @ZX-ModelCloud in https://github.com/ModelCloud/GPTQModel/pull/2907
* Ascend tests by @Qubitium in https://github.com/ModelCloud/GPTQModel/pull/2908
* [MODEL] support `nemotron_labs_diffusion` by @ZX-ModelCloud in https://github.com/ModelCloud/GPTQModel/pull/2909
* [MODEL] support `hunyuan_v1_dense` and `hunyuan_v1_moe` by @ZX-ModelCloud in https://github.com/ModelCloud/GPTQModel/pull/2910
* [FIX] Avoid invoke `tensor.transpose(0, 1).contiguous()` when the shapes already match by @ZX-ModelCloud in https://github.com/ModelCloud/GPTQModel/pull/2913
* [FIX] `DeepSeek-V4-Pro` experts module can now be correctly dequantized to `BF16` by @ZX-ModelCloud in https://github.com/ModelCloud/GPTQModel/pull/2914
* [FIX] `weight_only_looper` did not support multi-GPU quantization. by @ZX-ModelCloud in https://github.com/ModelCloud/GPTQModel/pull/2915
* fix(hub): import create_repo from huggingface_hub (transformers dropped the passthrough) by @Anai-Guo in https://github.com/ModelCloud/GPTQModel/pull/2917
* [FIX] non-existent import in `transformers.utils.hub` with the latest `transformers` by @ZX-ModelCloud in https://github.com/ModelCloud/GPTQModel/pull/2918
* prep for v7.1.0 release by @Qubitium in https://github.com/ModelCloud/GPTQModel/pull/2919

## New Contributors
* @erm14254 made their first contribution in https://github.com/ModelCloud/GPTQModel/pull/2869
* @Anai-Guo made their first contribution in https://github.com/ModelCloud/GPTQModel/pull/2917

**Full Changelog**: https://github.com/ModelCloud/GPTQModel/compare/v7.0.0...v7.1.0

## v7.2.0 (2026-07-03)

## What's Changed
* [MODEL] support gemma4_unified by @HaozheZhang6 in https://github.com/ModelCloud/GPTQModel/pull/2921
* feat(models): register gemma4_unified_text text-only GPTQ definition by @Anai-Guo in https://github.com/ModelCloud/GPTQModel/pull/2925
* Fix Mllama (Llama3.2-11B-Vision) quantization by @JeevanBhoot in https://github.com/ModelCloud/GPTQModel/pull/2926
* Bump actions/checkout from 6 to 7 in the github-actions group by @dependabot[bot] in https://github.com/ModelCloud/GPTQModel/pull/2927
* [MODEL] support glm4v_moe_text, llama4_text and mllama_text_model by @ZX-ModelCloud in https://github.com/ModelCloud/GPTQModel/pull/2912
* [MODEL] support `hy_v3` and `ministral3` by @ZX-ModelCloud in https://github.com/ModelCloud/GPTQModel/pull/2911
* [MODEL] support `cohere2_moe` by @ZX-ModelCloud in https://github.com/ModelCloud/GPTQModel/pull/2929
* support minimax_m3_vl by @ZX-ModelCloud in https://github.com/ModelCloud/GPTQModel/pull/2930
* [MODEL] support `lfm2` by @ZX-ModelCloud in https://github.com/ModelCloud/GPTQModel/pull/2932
* [MODEL] support `lfm2_vl` by @ZX-ModelCloud in https://github.com/ModelCloud/GPTQModel/pull/2933
* Fix Mllama GPTQ loading for skipped cross-attention layers by @JeevanBhoot in https://github.com/ModelCloud/GPTQModel/pull/2934
* Bump version from 7.1.0 to 7.2.0 by @Qubitium in https://github.com/ModelCloud/GPTQModel/pull/2935

## New Contributors
* @HaozheZhang6 made their first contribution in https://github.com/ModelCloud/GPTQModel/pull/2921
* @JeevanBhoot made their first contribution in https://github.com/ModelCloud/GPTQModel/pull/2926

**Full Changelog**: https://github.com/ModelCloud/GPTQModel/compare/v7.1.0...v7.2.0

## v7.3.1 (2026-07-20)

## What's Changed
* [MODEL] support `deepsekk_vl_v2` by @ZX-ModelCloud in https://github.com/ModelCloud/GPTQModel/pull/2938
* [MODEL] support `deepseek_ocr2` by @ZX-ModelCloud in https://github.com/ModelCloud/GPTQModel/pull/2940
* Fix O(N^2) state-dict collection that stalled saves of large MoE models for offload_to_disk=True by @avtc in https://github.com/ModelCloud/GPTQModel/pull/2945
* Fix ExLlamaV2 kernels on Windows: link cublas.lib and enable PLATFORM.WIN32 by @xXpeira12 in https://github.com/ModelCloud/GPTQModel/pull/2944
* [MODEL] support `deepseek_vl` by @ZX-ModelCloud in https://github.com/ModelCloud/GPTQModel/pull/2942
* [FIX] `deepseek_ocr2` supports `OFFLOAD_TO_DISK=True` by @ZX-ModelCloud in https://github.com/ModelCloud/GPTQModel/pull/2941
* [FIX] `GLM-5.2` quantization error by @ZX-ModelCloud in https://github.com/ModelCloud/GPTQModel/pull/2947
* support `ModelOpt` `NVFP4` dequantization by @ZX-ModelCloud in https://github.com/ModelCloud/GPTQModel/pull/2948
* fix(triton): bound-check checkpoint g_idx to prevent OOB dequant read (#2949) by @Anai-Guo in https://github.com/ModelCloud/GPTQModel/pull/2950
* [MODEL] support `nemotron_h_puzzle` by @ZX-ModelCloud in https://github.com/ModelCloud/GPTQModel/pull/2951
* [FIX] `load_gguf_checkpoint()` compatible with the latest `transformers` by @ZX-ModelCloud in https://github.com/ModelCloud/GPTQModel/pull/2952
* [FIX]  The "Latest News" section of the README by @ZX-ModelCloud in https://github.com/ModelCloud/GPTQModel/pull/2953
* Update Evalution dependency version in pyproject.toml by @Qubitium in https://github.com/ModelCloud/GPTQModel/pull/2954
* Update version.py by @Qubitium in https://github.com/ModelCloud/GPTQModel/pull/2955
* Bump version from 7.3.0 to 7.3.1 by @Qubitium in https://github.com/ModelCloud/GPTQModel/pull/2956

## New Contributors
* @xXpeira12 made their first contribution in https://github.com/ModelCloud/GPTQModel/pull/2944

**Full Changelog**: https://github.com/ModelCloud/GPTQModel/compare/v7.2.0...v7.3.1

## v7.3.2 (2026-07-25)

## What's Changed
* Bump actions/setup-python from 6 to 7 in the github-actions group by @dependabot[bot] in https://github.com/ModelCloud/GPTQModel/pull/2957
* fix: support Transformers 5.14 cache and dtype APIs by @Qubitium in https://github.com/ModelCloud/GPTQModel/pull/2959
* Add Laguna S 2.1 model support by @Qubitium in https://github.com/ModelCloud/GPTQModel/pull/2960
* Fix Laguna Evalution runtime configuration by @Qubitium in https://github.com/ModelCloud/GPTQModel/pull/2961
* Update Evalution dependency version to 0.0.9 by @Qubitium in https://github.com/ModelCloud/GPTQModel/pull/2962
* Clamp reconstructed quantization codes before packing by @Qubitium in https://github.com/ModelCloud/GPTQModel/pull/2963
* Fix unsafe EoRA wq aliasing by @Qubitium in https://github.com/ModelCloud/GPTQModel/pull/2965
* [MODEL] support `inkling` by @ZX-ModelCloud in https://github.com/ModelCloud/GPTQModel/pull/2958
* fix(logger): stop _AdaptiveLoggerProxy.__getattr__ from recursing on deepcopy (fixes #2966) by @Anai-Guo in https://github.com/ModelCloud/GPTQModel/pull/2968
* fix: fence parallel calibration workers before completion by @Qubitium in https://github.com/ModelCloud/GPTQModel/pull/2969
* [MODEL]support `intern_s2_preview` by @ZX-ModelCloud in https://github.com/ModelCloud/GPTQModel/pull/2964
* Support quantized embedding inference without backend misselection by @Qubitium in https://github.com/ModelCloud/GPTQModel/pull/2971
* [MODEL] support `solar_open2` by @ZX-ModelCloud in https://github.com/ModelCloud/GPTQModel/pull/2970
* [MODEL] support `solar_open` by @ZX-ModelCloud in https://github.com/ModelCloud/GPTQModel/pull/2972
* fix: per-module dynamic kernel selection for mixed-bitwidth models by @Qubitium in https://github.com/ModelCloud/GPTQModel/pull/2973
* fix(cpp/tests): C++20 JIT flags for PyTorch 2.14 nightly by @Qubitium in https://github.com/ModelCloud/GPTQModel/pull/2974
* deps: bump logbar and pypcre to latest PyPI releases by @Qubitium in https://github.com/ModelCloud/GPTQModel/pull/2975
* test(llama3_2): update fast-mode MARLIN baseline scores by @Qubitium in https://github.com/ModelCloud/GPTQModel/pull/2976
* Update version.py by @Qubitium in https://github.com/ModelCloud/GPTQModel/pull/2977


**Full Changelog**: https://github.com/ModelCloud/GPTQModel/compare/v7.3.1...v7.3.2

## v7.3.4 (2026-08-19)

## What's Changed
* fix(loader,eval): disable continuous-batching CUDA graphs for paged attention and require Evalution>=0.0.10 by @Qubitium in https://github.com/ModelCloud/GPTQModel/pull/2978
* fix(qqq): per-device Hessian partials for balanced multi-GPU calibration by @Qubitium in https://github.com/ModelCloud/GPTQModel/pull/2979
* fix(rotation): persist rotation config and apply online Hadamard for inference and calibration by @Qubitium in https://github.com/ModelCloud/GPTQModel/pull/2980
* fix(qqq): accumulate Hessian in-place per device to reduce memory by @Qubitium in https://github.com/ModelCloud/GPTQModel/pull/2981
* fix(qlinear): size GPTQ buffers by pack_factor and skip Laguna g_proj quantization by @Qubitium in https://github.com/ModelCloud/GPTQModel/pull/2983
* fix(qlinear): size pack_original qweight/qzeros by bits/32 for 3-bit GPTQ by @Qubitium in https://github.com/ModelCloud/GPTQModel/pull/2984
* fix(qlinear): size GPTQ buffers by bits/pack_dtype_bits by @Qubitium in https://github.com/ModelCloud/GPTQModel/pull/2985
* Fix the issue where WeightOnlyLooper did not support dynamic skipping. by @ZX-ModelCloud in https://github.com/ModelCloud/GPTQModel/pull/2986
* perf(quant): bypass pcre.match for exact dynamic config patterns by @Qubitium in https://github.com/ModelCloud/GPTQModel/pull/2987
* perf(marlin): cache scale permutation tensors and use index_select by @Qubitium in https://github.com/ModelCloud/GPTQModel/pull/2988
* perf(lazy_turtle): targeted ancestor+subtree map in materialize_submodule by @Qubitium in https://github.com/ModelCloud/GPTQModel/pull/2989
* fix(runtime): support vLLM 0.26 and SGLang 0.5.16 by @ZX-ModelCloud in https://github.com/ModelCloud/GPTQModel/pull/2991
* Fix the issue where WeightOnlyLooper did not support dynamic skipping. by @ZX-ModelCloud in https://github.com/ModelCloud/GPTQModel/pull/2990
* docs: fix FP8Config/EXL3Config imports in README examples by @latent-9 in https://github.com/ModelCloud/GPTQModel/pull/2993
* gptq: add planar (gptq_p) checkpoint format with 3/5/6/7-bit support by @Qubitium in https://github.com/ModelCloud/GPTQModel/pull/2996
* feat: Swordfish kernel for Blackwell (GPTQ/AWQ) by AlpinDale by @Qubitium in https://github.com/ModelCloud/GPTQModel/pull/2997
* docs(readme): add Swordfish kernel attribution and citation by @Qubitium in https://github.com/ModelCloud/GPTQModel/pull/2998
* fix(swordfish): apply post-review fixes from GPT-QModel-Ultra PR #183 by @Qubitium in https://github.com/ModelCloud/GPTQModel/pull/2999
* feat: axk2 (A.X-K2) model support by @Qubitium in https://github.com/ModelCloud/GPTQModel/pull/3000
* chore(deps): bump logbar to >=0.4.12 and Evalution to >=0.0.11 by @Qubitium in https://github.com/ModelCloud/GPTQModel/pull/3002
* Add lazy-load smoke testing skill by @Qubitium in https://github.com/ModelCloud/GPTQModel/pull/3004
* fix(looper): pass dotted layer names to cache_inputs for correct lazy materialization by @Qubitium in https://github.com/ModelCloud/GPTQModel/pull/3003
* fix(quantization): cap thread growth and add region telemetry by @Qubitium in https://github.com/ModelCloud/GPTQModel/pull/3005
* fix(telemetry): make env-gating consistent and caps configurable by @Qubitium in https://github.com/ModelCloud/GPTQModel/pull/3006
* fix(quantization): remove torch.compile wrappers from hessian_inverse by @Qubitium in https://github.com/ModelCloud/GPTQModel/pull/3007
* fix looper concurrency safety by @Qubitium in https://github.com/ModelCloud/GPTQModel/pull/3008
* harden free-threaded lock ownership by @Qubitium in https://github.com/ModelCloud/GPTQModel/pull/3009
* enable native MPS GPTQ quantization by @Qubitium in https://github.com/ModelCloud/GPTQModel/pull/3011
* fix test fakes drift and MoE subset hook-order flake  by @Qubitium in https://github.com/ModelCloud/GPTQModel/pull/3012
* Optimize asymmetric 2-bit zero-point search by @Qubitium in https://github.com/ModelCloud/GPTQModel/pull/3013
* fix(eora): clamp covariance eigenvalues before inversion to avoid outlier adapters by @Qubitium in https://github.com/ModelCloud/GPTQModel/pull/3014
* fix(looper): pass the missing processor arg to the AWQ subset debug log by @Anai-Guo in https://github.com/ModelCloud/GPTQModel/pull/3016
* fix(cpp): add cross-process file lock for JIT kernel builds by @Ndgandhi23 in https://github.com/ModelCloud/GPTQModel/pull/3019
* fix(calibration): interpolate the item index in the unsupported-sequence error by @Anai-Guo in https://github.com/ModelCloud/GPTQModel/pull/3017
* feat(models): add Cohere Compass quantization support by @ZX-ModelCloud in https://github.com/ModelCloud/GPTQModel/pull/3018

## New Contributors
* @latent-9 made their first contribution in https://github.com/ModelCloud/GPTQModel/pull/2993
* @Ndgandhi23 made their first contribution in https://github.com/ModelCloud/GPTQModel/pull/3019

**Full Changelog**: https://github.com/ModelCloud/GPTQModel/compare/v7.3.2...v7.3.4

## v7.3.5 (2026-08-25)

## What's Changed
* [MODEL] add `Mage-VL`, `Muse Glimmer`, `OLMo 3`, `SmolLM3`, and `DeepSeek V3.2` quantization support by @ZX-ModelCloud in https://github.com/ModelCloud/GPTQModel/pull/3020
* Add LM-head and embedding quantization lifecycle by @Qubitium in https://github.com/ModelCloud/GPTQModel/pull/3021
* [MODEL] add `Unlimited-OCR` quantization support by @ZX-ModelCloud in https://github.com/ModelCloud/GPTQModel/pull/3023
* docs: refresh README with latest release notes and formatting by @Qubitium in https://github.com/ModelCloud/GPTQModel/pull/3024
* docs: consolidate model-support entries in Latest News by @Qubitium in https://github.com/ModelCloud/GPTQModel/pull/3025
* chore: bump logbar, pypcre, device-smi, and defuser to latest PyPI releases by @Qubitium in https://github.com/ModelCloud/GPTQModel/pull/3026
* Bump version from 7.3.4 to 7.3.5 by @Qubitium in https://github.com/ModelCloud/GPTQModel/pull/3027


**Full Changelog**: https://github.com/ModelCloud/GPTQModel/compare/v7.3.4...v7.3.5

## v7.3.6 (2026-08-31)

## What's Changed
* feat: support tile-misaligned GPTQ Marlin shapes by @ZX-ModelCloud in https://github.com/ModelCloud/GPTQModel/pull/3028
* Fix QQQ workspace lifetime and reduce packing memory by @yujiongzhang in https://github.com/ModelCloud/GPTQModel/pull/3029
* [MODEL] add `HunyuanOCR` quantization support by @ZX-ModelCloud in https://github.com/ModelCloud/GPTQModel/pull/3030
* [MODEL] Add `locateanything` quantization support by @ZX-ModelCloud in https://github.com/ModelCloud/GPTQModel/pull/3032
* feat: support tile-misaligned 4-bit AWQ Marlin shapes by @ZX-ModelCloud in https://github.com/ModelCloud/GPTQModel/pull/3033
* Fix CUDA JIT cache reuse and update CUTLASS by @Qubitium in https://github.com/ModelCloud/GPTQModel/pull/3039
* fix(tests): drop the extra self argument that makes TestKernelOutput.setUp raise TypeError by @Anai-Guo in https://github.com/ModelCloud/GPTQModel/pull/3037
* fix(tests): update run_layer_stage callers to the layer_names kwarg by @Anai-Guo in https://github.com/ModelCloud/GPTQModel/pull/3038
* fix(pack): forward quant_result to make_quant in pack_model by @Anai-Guo in https://github.com/ModelCloud/GPTQModel/pull/3034
* [MODEL] support `Qwen3.8 Flash Next` quantization by @ZX-ModelCloud in https://github.com/ModelCloud/GPTQModel/pull/3040
* fix(marlin): validate devices and register runtime buffers by @ZX-ModelCloud in https://github.com/ModelCloud/GPTQModel/pull/3041
* fix(awq): stop variable-length calibration collapsing to the last batch by @Leonccaa in https://github.com/ModelCloud/GPTQModel/pull/3036
* bump package dependencies to latest stable pypi versions by @Qubitium in https://github.com/ModelCloud/GPTQModel/pull/3042
* Reuse ABI-compatible JIT extension caches across Python/torch envs by @Qubitium in https://github.com/ModelCloud/GPTQModel/pull/3043
* Bump version from 7.3.5 to 7.3.6 by @Qubitium in https://github.com/ModelCloud/GPTQModel/pull/3044

## New Contributors
* @yujiongzhang made their first contribution in https://github.com/ModelCloud/GPTQModel/pull/3029
* @Leonccaa made their first contribution in https://github.com/ModelCloud/GPTQModel/pull/3036

**Full Changelog**: https://github.com/ModelCloud/GPTQModel/compare/v7.3.5...v7.3.6

## v7.4.0 (2026-09-08)

## What's Changed
* feat(models): add GLM-5 Next quantization support by @ZX-ModelCloud in https://github.com/ModelCloud/GPTQModel/pull/3045
* bench(marlin): add tile-padding performance by @ZX-ModelCloud in https://github.com/ModelCloud/GPTQModel/pull/3046
* [MODEL] support `apertus1p5` by @ZX-ModelCloud in https://github.com/ModelCloud/GPTQModel/pull/3047
* fix: normalize multimodal calibration inputs by @ZX-ModelCloud in https://github.com/ModelCloud/GPTQModel/pull/3049
* fix: improve quantization and runtime correctness by @ZX-ModelCloud in https://github.com/ModelCloud/GPTQModel/pull/3055
* Shared-input Hessian dedup: plan metadata, E2E validation, and telemetry by @Qubitium in https://github.com/ModelCloud/GPTQModel/pull/3052
* support lm-head/embed requant by @ZX-ModelCloud in https://github.com/ModelCloud/GPTQModel/pull/3050
* fix: isolate JIT extension cache fingerprint from unrelated kernel changes by @Qubitium in https://github.com/ModelCloud/GPTQModel/pull/3056
* Sync native GGUF support with current upstream types by @Qubitium in https://github.com/ModelCloud/GPTQModel/pull/3058
* feat: checkpointing and resuming quantization process from last checkpoint by @okdshin in https://github.com/ModelCloud/GPTQModel/pull/3057
* Update version.py by @Qubitium in https://github.com/ModelCloud/GPTQModel/pull/3060
* Fix Triton patch for pre-existing autotuner instances by @Qubitium in https://github.com/ModelCloud/GPTQModel/pull/3062
* [MODEL] support `ouro` and `spark2_5` by @ZX-ModelCloud in https://github.com/ModelCloud/GPTQModel/pull/3061
* Sync README release news and model support for 7.4.0 by @Qubitium in https://github.com/ModelCloud/GPTQModel/pull/3063
* Document quantization checkpoint and resume workflows by @Qubitium in https://github.com/ModelCloud/GPTQModel/pull/3064

## New Contributors
* @okdshin made their first contribution in https://github.com/ModelCloud/GPTQModel/pull/3057

**Full Changelog**: https://github.com/ModelCloud/GPTQModel/compare/v7.3.6...v7.4.0

## v7.5.0 (2026-09-15)

## What's Changed
* [MODEL] support K2 Horizon quantization by @ZX-ModelCloud in https://github.com/ModelCloud/GPTQModel/pull/3065
* fix(qlinear): harden empty-input and CUDA dispatch contracts by @ZX-ModelCloud in https://github.com/ModelCloud/GPTQModel/pull/3069
* Avoid full model scans during per-module finalization by @peter-positron in https://github.com/ModelCloud/GPTQModel/pull/3068
* Scope banner Git lookup to the package checkout by @peter-positron in https://github.com/ModelCloud/GPTQModel/pull/3066
* Align GPTQ keep masks with captured tensor devices by @peter-positron in https://github.com/ModelCloud/GPTQModel/pull/3067
* Align version with 7.5.0 development changelog by @Qubitium in https://github.com/ModelCloud/GPTQModel/pull/3070
* refactor(machete): harden runtime cache by @ZX-ModelCloud in https://github.com/ModelCloud/GPTQModel/pull/3071
* fix: make kernel selection device-aware by @ZX-ModelCloud in https://github.com/ModelCloud/GPTQModel/pull/3072
* test(kernels): expand edge-case coverage by @ZX-ModelCloud in https://github.com/ModelCloud/GPTQModel/pull/3073
* [MODEL] add `qwen_drive` quantization support by @ZX-ModelCloud in https://github.com/ModelCloud/GPTQModel/pull/3074
* Defer InternVL torchvision imports until image preprocessing by @peter-positron in https://github.com/ModelCloud/GPTQModel/pull/3078
* fix(looper): import Sequence used in paroquant_processor annotations by @Anai-Guo in https://github.com/ModelCloud/GPTQModel/pull/3080
* Fix partial packing words in the Torch fallback by @peter-positron in https://github.com/ModelCloud/GPTQModel/pull/3075
* Validate offload metadata before saving meta tensors by @peter-positron in https://github.com/ModelCloud/GPTQModel/pull/3076
* Validate required qweight tensors in GPTQ safetensors checkpoints by @peter-positron in https://github.com/ModelCloud/GPTQModel/pull/3077
* Apply model replay hooks during Paro layer preparation by @peter-positron in https://github.com/ModelCloud/GPTQModel/pull/3079
* [MODEL] add `nanbeige` quantization support by @ZX-ModelCloud in https://github.com/ModelCloud/GPTQModel/pull/3081
* [MODEL] add `diffusion_gemma` quantization support by @ZX-ModelCloud in https://github.com/ModelCloud/GPTQModel/pull/3082
* docs: finalize 7.5.0 release notes by @Qubitium in https://github.com/ModelCloud/GPTQModel/pull/3083

## New Contributors
* @peter-positron made their first contribution in https://github.com/ModelCloud/GPTQModel/pull/3068

**Full Changelog**: https://github.com/ModelCloud/GPTQModel/compare/v7.4.0...v7.5.0
