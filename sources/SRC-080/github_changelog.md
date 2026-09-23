# Changelog (aggregated from releases.body)

> releases: 33

## 0.1.0 (2024-08-12)

## What's Changed
* Address Test Failures by @Satrat in https://github.com/vllm-project/llm-compressor/pull/1
* Remove SparseZoo Usage by @Satrat in https://github.com/vllm-project/llm-compressor/pull/2
* SparseML Cleanup by @markurtz in https://github.com/vllm-project/llm-compressor/pull/6
* Remove all references to Neural Magic copyright within LLM Compressor by @markurtz in https://github.com/vllm-project/llm-compressor/pull/7
* Add FP8 Support by @Satrat in https://github.com/vllm-project/llm-compressor/pull/4
* Fix Weekly Test Failure by @Satrat in https://github.com/vllm-project/llm-compressor/pull/8
* Add Scheme UX for QuantizationModifier by @Satrat in https://github.com/vllm-project/llm-compressor/pull/9
* Add Group Quantization Test Case by @Satrat in https://github.com/vllm-project/llm-compressor/pull/10
* Loguru logging standardization for LLM Compressor by @markurtz in https://github.com/vllm-project/llm-compressor/pull/11
* Clarify Function Names for Logging by @Satrat in https://github.com/vllm-project/llm-compressor/pull/12
* [ Examples ] E2E Examples by @robertgshaw2-neuralmagic in https://github.com/vllm-project/llm-compressor/pull/5
* Update setup.py by @robertgshaw2-neuralmagic in https://github.com/vllm-project/llm-compressor/pull/15
* SmoothQuant Mapping Defaults by @Satrat in https://github.com/vllm-project/llm-compressor/pull/13
* Initial README by @bfineran in https://github.com/vllm-project/llm-compressor/pull/3
* [Bug] Fix validation errors for smoothquant modifier + update examples by @rahul-tuli in https://github.com/vllm-project/llm-compressor/pull/19
* [MOE Quantization] Warn against "undercalibrated" modules  by @dbogunowicz in https://github.com/vllm-project/llm-compressor/pull/20
* Port SparseML Remote Code Fix by @Satrat in https://github.com/vllm-project/llm-compressor/pull/21
* Update Quantization Save Defaults by @Satrat in https://github.com/vllm-project/llm-compressor/pull/22
* [Bugfix] Add fix to preserve modifier order when passed as a list by @rahul-tuli in https://github.com/vllm-project/llm-compressor/pull/26
* GPTQ - move calibration of quantiztion params to after hessian calibration by @bfineran in https://github.com/vllm-project/llm-compressor/pull/25
* Fix typos by @eldarkurtic in https://github.com/vllm-project/llm-compressor/pull/31
* Remove ceiling from `datasets` dep by @mgoin in https://github.com/vllm-project/llm-compressor/pull/27
* Revert naive compression format by @Satrat in https://github.com/vllm-project/llm-compressor/pull/32
* Fix layerwise targets by @Satrat in https://github.com/vllm-project/llm-compressor/pull/36
* Move Weight Update Out Of Loop by @Satrat in https://github.com/vllm-project/llm-compressor/pull/40
* Fix End Epoch Default by @Satrat in https://github.com/vllm-project/llm-compressor/pull/39
* Fix typos in example for w8a8 quant by @eldarkurtic in https://github.com/vllm-project/llm-compressor/pull/38
* Model Offloading Support Pt 2 by @Satrat in https://github.com/vllm-project/llm-compressor/pull/34
* set version to 1.0.0 for release by @bfineran in https://github.com/vllm-project/llm-compressor/pull/44
* Update version for first release by @markurtz in https://github.com/vllm-project/llm-compressor/pull/50
* BugFix: Update TRL example scripts to point to the right SFTTrainer by @rahul-tuli in https://github.com/vllm-project/llm-compressor/pull/51
* Update examples/quantization_24_sparse_w4a16 README by @dbarbuzzi in https://github.com/vllm-project/llm-compressor/pull/52
* Fix Failing Transformers Tests by @Satrat in https://github.com/vllm-project/llm-compressor/pull/53
* Offloading Bug Fix by @Satrat in https://github.com/vllm-project/llm-compressor/pull/58

## New Contributors
* @markurtz made their first contribution in https://github.com/vllm-project/llm-compressor/pull/6
* @bfineran made their first contribution in https://github.com/vllm-project/llm-compressor/pull/3
* @dbogunowicz made their first contribution in https://github.com/vllm-project/llm-compressor/pull/20
* @eldarkurtic made their first contribution in https://github.com/vllm-project/llm-compressor/pull/31
* @mgoin made their first contribution in https://github.com/vllm-project/llm-compressor/pull/27
* @dbarbuzzi made their first contribution in https://github.com/vllm-project/llm-compressor/pull/52

**Full Changelog**: https://github.com/vllm-project/llm-compressor/commits/0.1.0

## 0.2.0 (2024-09-23)

## What's Changed
* Correct Typo in SparseAutoModelForCausalLM docstring by @kylesayrs in https://github.com/vllm-project/llm-compressor/pull/56
* Disable Default Bitmask Compression by @Satrat in https://github.com/vllm-project/llm-compressor/pull/60
* TRL Example fix by @rahul-tuli in https://github.com/vllm-project/llm-compressor/pull/59
* Fix typo by @rahul-tuli in https://github.com/vllm-project/llm-compressor/pull/63
* Correct typo by @kylesayrs in https://github.com/vllm-project/llm-compressor/pull/61
* correct import in README.md by @zzc0430 in https://github.com/vllm-project/llm-compressor/pull/66
* Fix for issue #43 -- starcoder model by @horheynm in https://github.com/vllm-project/llm-compressor/pull/71
* Update README.md by @robertgshaw2-neuralmagic in https://github.com/vllm-project/llm-compressor/pull/74
* Layer by Layer Sequential GPTQ Updates by @Satrat in https://github.com/vllm-project/llm-compressor/pull/47
* [ Docs ] Update main readme by @robertgshaw2-neuralmagic in https://github.com/vllm-project/llm-compressor/pull/77
* [ Docs ] `gemma2` examples by @robertgshaw2-neuralmagic in https://github.com/vllm-project/llm-compressor/pull/78
* [ Docs ] Update `FP8` example to use dynamic per token by @robertgshaw2-neuralmagic in https://github.com/vllm-project/llm-compressor/pull/75
* [ Docs ] Overhaul `accelerate` user guide by @robertgshaw2-neuralmagic in https://github.com/vllm-project/llm-compressor/pull/76
* Support `kv_cache_scheme` for quantizing KV Cache by @mgoin in https://github.com/vllm-project/llm-compressor/pull/88
* Propagate `trust_remote_code` Argument by @kylesayrs in https://github.com/vllm-project/llm-compressor/pull/90
* Fix for issue #81 by @horheynm in https://github.com/vllm-project/llm-compressor/pull/84
* Fix for issue 83 by @horheynm in https://github.com/vllm-project/llm-compressor/pull/85
* [ DOC ] Big Model Example by @robertgshaw2-neuralmagic in https://github.com/vllm-project/llm-compressor/pull/99
* Enable obcq/finetune integration tests with `commit` cadence by @dsikka in https://github.com/vllm-project/llm-compressor/pull/101
* metric logging on GPTQ path by @horheynm in https://github.com/vllm-project/llm-compressor/pull/65
* Update test config files by @dsikka in https://github.com/vllm-project/llm-compressor/pull/97
* remove workflows + update runners by @dsikka in https://github.com/vllm-project/llm-compressor/pull/103
* metrics by @horheynm in https://github.com/vllm-project/llm-compressor/pull/104
* add debug by @horheynm in https://github.com/vllm-project/llm-compressor/pull/108
* Add FP8 KV Cache quant example by @mgoin in https://github.com/vllm-project/llm-compressor/pull/113
* Add vLLM e2e tests by @dsikka in https://github.com/vllm-project/llm-compressor/pull/117
* Fix style, fix noqa by @kylesayrs in https://github.com/vllm-project/llm-compressor/pull/123
* GPTQ Algorithm Cleanup by @kylesayrs in https://github.com/vllm-project/llm-compressor/pull/120
* GPTQ Activation Ordering by @kylesayrs in https://github.com/vllm-project/llm-compressor/pull/94
* demote recipe string initialization to debug and make more descriptive by @kylesayrs in https://github.com/vllm-project/llm-compressor/pull/116
* compressed-tensors main dependency for base-tests by @kylesayrs in https://github.com/vllm-project/llm-compressor/pull/125
* Set `ready` label for transformer tests; add message reminder on PR opened by @dsikka in https://github.com/vllm-project/llm-compressor/pull/126
* Fix markdown check test by @dsikka in https://github.com/vllm-project/llm-compressor/pull/127
* Naive Run Compressed Pt. 2 by @Satrat in https://github.com/vllm-project/llm-compressor/pull/62
* Fix transformer test conditions by @dsikka in https://github.com/vllm-project/llm-compressor/pull/131
* Run Compressed Tests by @Satrat in https://github.com/vllm-project/llm-compressor/pull/132
* Correct typo by @kylesayrs in https://github.com/vllm-project/llm-compressor/pull/124
* Activation Ordering Strategies by @kylesayrs in https://github.com/vllm-project/llm-compressor/pull/121
* Fix README Issue by @robertgshaw2-neuralmagic in https://github.com/vllm-project/llm-compressor/pull/139
* update by @dsikka in https://github.com/vllm-project/llm-compressor/pull/143
* Update finetune and oneshot tests by @dsikka in https://github.com/vllm-project/llm-compressor/pull/114
* Validate Recipe Parsing Output by @kylesayrs in https://github.com/vllm-project/llm-compressor/pull/100
* fix build error for nightly by @dhuangnm in https://github.com/vllm-project/llm-compressor/pull/145
* Fix recipe nested in configs by @kylesayrs in https://github.com/vllm-project/llm-compressor/pull/140
* MOE example with warning by @rahul-tuli in https://github.com/vllm-project/llm-compressor/pull/87
* Bug Fix: recipe stages were not being concatenated by @rahul-tuli in https://github.com/vllm-project/llm-compressor/pull/150
* fix package name bug for nightly by @dhuangnm in https://github.com/vllm-project/llm-compressor/pull/155
* Add descriptions for pytest marks by @kylesayrs in https://github.com/vllm-project/llm-compressor/pull/156
* Fix Sparsity Unit Test by @Satrat in https://github.com/vllm-project/llm-compressor/pull/153
* Fix: Error during model saving with shared tensors by @rahul-tuli in https://github.com/vllm-project/llm-compressor/pull/158
* Update 2:4 Examples by @dsikka in https://github.com/vllm-project/llm-compressor/pull/161
* DeepSeek: Fix Hessian Estimation by @Satrat in https://github.com/vllm-project/llm-compressor/pull/157
* bump up main to 0.2.0 by @dhuangnm in https://github.com/vllm-project/llm-compressor/pull/163
* Fix help dialogue by @kylesayrs in https://github.com/vllm-project/llm-compressor/pull/151
* Add MoE and Compressed Inference Examples by @Satrat in https://github.com/vllm-project/llm-compressor/pull/160
* Separate `trust_remote_code` args by @kylesayrs in https://github.com/vllm-project/llm-compressor/pull/152
* Enable a skipped finetune test by @dsikka in https://github.com/vllm-project/llm-compressor/pull/169
* Fix filename in example command by @dbarbuzzi in https://github.com/vllm-project/llm-compressor/pull/173
* Add DeepSeek V2.5 Example by @dsikka in https://github.com/vllm-project/llm-compressor/pull/171
* fix quality by @dsikka in https://github.com/vllm-project/llm-compressor/pull/176
* Patch log function name in gptq by @kylesayrs in https://github.com/vllm-project/llm-compressor/pull/168
* README for Modifiers by @Satrat in https://github.com/vllm-project/llm-compressor/pull/165
* Fix default for sequential updates by @dsikka in https://github.com/vllm-project/llm-compressor/pull/186
* fix default test case by @dsikka in https://github.com/vllm-project/llm-compressor/pull/193
* Fix Initalize typo by @Imss27 in https://github.com/vllm-project/llm-compressor/pull/190
* Update MoE examples by @mgoin in https://github.com/vllm-project/llm-compressor/pull/192

## New Contributors
* @zzc0430 made their first contribution in https://github.com/vllm-project/llm-compressor/pull/66
* @horheynm made their first contribution in https://github.com/vllm-project/llm-compressor/pull/71
* @dsikka made their first contribution in https://github.com/vllm-project/llm-compressor/pull/101
* @dhuangnm made their first contribution in https://github.com/vllm-project/llm-compressor/pull/145
* @Imss27 made their first contribution in https://github.com/vllm-project/llm-compressor/pull/190

**Full Changelog**: https://github.com/vllm-project/llm-compressor/compare/0.1.0...0.2.0

## 0.3.0 (2024-11-13)

## What's New in v0.3.0

### Key Features and Improvements
- **GPTQ Quantized-weight Sequential Updating** ([#177](https://github.com/vllm-project/llm-compressor/pull/177)): Introduced an efficient sequential updating mechanism for GPTQ quantization, improving model compression performance and compatibility.
- **Auto-Infer Mappings for SmoothQuantModifier** ([#119](https://github.com/vllm-project/llm-compressor/pull/119)): Automatically infers `mappings` based on model architecture, making SmoothQuant easier to apply across various models.
- **Improved Sparse Compression Usability** ([#191](https://github.com/vllm-project/llm-compressor/pull/191)): Added support for targeted sparse compression with specific ignore rules during inference, allowing for more flexible model configurations.
- **Generic Wrapper for Any Hugging Face Model** ([#185](https://github.com/vllm-project/llm-compressor/pull/185)): Added `wrap_hf_model_class` utility, enabling better support and integration for Hugging Face models i.e. not based on `AutoModelForCausalLM`.
- **Observer Restructure** ([#837](https://github.com/vllm-project/llm-compressor/pull/837)): Introduced calibration and frozen steps within `QuantizationModifier`, moving Observers from compressed-tensors to llm-compressor.

### Bug Fixes
- **Fix Tied Tensors Bug** ([#659](https://github.com/vllm-project/llm-compressor/pull/659))
- **Observer Initialization in GPTQ Wrapper** ([#883](https://github.com/vllm-project/llm-compressor/pull/883))
- **Sparsity Reload Testing** ([#882](https://github.com/vllm-project/llm-compressor/pull/882))

### Documentation
- **Updated SmoothQuant Tutorial** ([#115](https://github.com/vllm-project/llm-compressor/pull/115)): Expanded SmoothQuant documentation to include detailed mappings for easier implementation.


## What's Changed
* Fix compresed typo by @kylesayrs in https://github.com/vllm-project/llm-compressor/pull/188
* GPTQ Quantized-weight Sequential Updating by @kylesayrs in https://github.com/vllm-project/llm-compressor/pull/177
* Add: targets and ignore inference for sparse compression by @rahul-tuli in https://github.com/vllm-project/llm-compressor/pull/191
* switch tests from weekly to nightly by @dhuangnm in https://github.com/vllm-project/llm-compressor/pull/658
* Compression wrapper abstract methods by @kylesayrs in https://github.com/vllm-project/llm-compressor/pull/170
* Explicitly set sequential_update in examples by @kylesayrs in https://github.com/vllm-project/llm-compressor/pull/187
* Increase Sparsity Threshold for compressors by @rahul-tuli in https://github.com/vllm-project/llm-compressor/pull/679
* Add a generic `wrap_hf_model_class` utility to support VLMs by @mgoin in https://github.com/vllm-project/llm-compressor/pull/185
* Add tests for examples by @dbarbuzzi in https://github.com/vllm-project/llm-compressor/pull/149
* Rename to quantization config by @kylesayrs in https://github.com/vllm-project/llm-compressor/pull/730
* Implement Missing Modifier Methods by @kylesayrs in https://github.com/vllm-project/llm-compressor/pull/166
* Fix 2/4 GPTQ Model Tests by @dsikka in https://github.com/vllm-project/llm-compressor/pull/769
* SmoothQuant mappings tutorial by @rahul-tuli in https://github.com/vllm-project/llm-compressor/pull/115
* Fix import of `ModelCompressor` by @rahul-tuli in https://github.com/vllm-project/llm-compressor/pull/776
* update test by @dsikka in https://github.com/vllm-project/llm-compressor/pull/773
* [Bugfix] Fix saving offloaded state dict by @kylesayrs in https://github.com/vllm-project/llm-compressor/pull/172
* Auto-Infer `mappings` Argument for `SmoothQuantModifier` Based on Model Architecture by @rahul-tuli in https://github.com/vllm-project/llm-compressor/pull/119
* Update workflows/actions by @dbarbuzzi in https://github.com/vllm-project/llm-compressor/pull/774
* [Bugfix] Prepare KD Models when Saving by @kylesayrs in https://github.com/vllm-project/llm-compressor/pull/174
* Set Sparse compression to save_compressed by @rahul-tuli in https://github.com/vllm-project/llm-compressor/pull/821
* Install compressed-tensors after llm-compressor by @dbarbuzzi in https://github.com/vllm-project/llm-compressor/pull/825
* Fix test typo by @kylesayrs in https://github.com/vllm-project/llm-compressor/pull/828
* Add `AutoModelForCausalLM` example by @dsikka in https://github.com/vllm-project/llm-compressor/pull/698
* [Bugfix] Workaround tied tensors bug by @kylesayrs in https://github.com/vllm-project/llm-compressor/pull/659
* Only untie word embeddings by @kylesayrs in https://github.com/vllm-project/llm-compressor/pull/839
* Check for config hidden size by @kylesayrs in https://github.com/vllm-project/llm-compressor/pull/840
* Use float32 for Hessian dtype by @kylesayrs in https://github.com/vllm-project/llm-compressor/pull/847
* GPTQ: Depreciate non-sequential update option by @kylesayrs in https://github.com/vllm-project/llm-compressor/pull/762
* Typehint nits by @kylesayrs in https://github.com/vllm-project/llm-compressor/pull/826
* [ DOC ] Remove version restrictions in W8A8 exmaple by @miaojinc in https://github.com/vllm-project/llm-compressor/pull/849
* Fix inconsistence in example config of 2:4 sparse quantization by @yzlnew in https://github.com/vllm-project/llm-compressor/pull/80
* Fix forward function pass call by @dsikka in https://github.com/vllm-project/llm-compressor/pull/845
* [Bugfix] Use weight parameter of linear layer by @kylesayrs in https://github.com/vllm-project/llm-compressor/pull/836
* [Bugfix] Rename files to remove colons by @kylesayrs in https://github.com/vllm-project/llm-compressor/pull/846
* cover all 3.9-3.12 in commit testing by @dhuangnm in https://github.com/vllm-project/llm-compressor/pull/864
* Add marlin-24 recipe/configs for e2e testing by @dsikka in https://github.com/vllm-project/llm-compressor/pull/866
* [Bugfix] onload during sparsity calculation by @kylesayrs in https://github.com/vllm-project/llm-compressor/pull/862
* Fix HFTrainer overloads by @kylesayrs in https://github.com/vllm-project/llm-compressor/pull/869
* Support Model Offloading Tied Tensors Patch by @kylesayrs in https://github.com/vllm-project/llm-compressor/pull/872
* Add advice about dealing with non-invertable hessians by @kylesayrs in https://github.com/vllm-project/llm-compressor/pull/875
* seed commit workflow by @andy-neuma in https://github.com/vllm-project/llm-compressor/pull/877
* [Observer Restructure]: Add Observers; Add `calibration` and `frozen` steps to `QuantizationModifier` by @dsikka in https://github.com/vllm-project/llm-compressor/pull/837
* Bugfix observer initialization in `gptq_wrapper` by @rahul-tuli in https://github.com/vllm-project/llm-compressor/pull/883
* BugFix: Fix Sparsity Reload Testing by @dsikka in https://github.com/vllm-project/llm-compressor/pull/882
* Use custom unique test names for e2e tests by @dbarbuzzi in https://github.com/vllm-project/llm-compressor/pull/892
* Revert "Use custom unique test names for e2e tests (#892)" by @dsikka in https://github.com/vllm-project/llm-compressor/pull/893
* Move config["testconfig_path"] assignment by @dbarbuzzi in https://github.com/vllm-project/llm-compressor/pull/895
* Cap accelerate version to avoid bug by @kylesayrs in https://github.com/vllm-project/llm-compressor/pull/897
* Fix observing offloaded weight by @kylesayrs in https://github.com/vllm-project/llm-compressor/pull/896
* Update image in README.md by @mgoin in https://github.com/vllm-project/llm-compressor/pull/861
* update accelerate version by @kylesayrs in https://github.com/vllm-project/llm-compressor/pull/899
* [GPTQ] Iterative Parameter Updating by @kylesayrs in https://github.com/vllm-project/llm-compressor/pull/863
* Small fixes for release by @dsikka in https://github.com/vllm-project/llm-compressor/pull/901
* use smaller portion of dataset by @dsikka in https://github.com/vllm-project/llm-compressor/pull/902
* Update example to not fail hessian inversion by @dsikka in https://github.com/vllm-project/llm-compressor/pull/904
* Bump version to 0.3.0 by @dsikka in https://github.com/vllm-project/llm-compressor/pull/907

## New Contributors
* @miaojinc made their first contribution in https://github.com/vllm-project/llm-compressor/pull/849
* @yzlnew made their first contribution in https://github.com/vllm-project/llm-compressor/pull/80
* @andy-neuma made their first contribution in https://github.com/vllm-project/llm-compressor/pull/877

**Full Changelog**: https://github.com/vllm-project/llm-compressor/compare/0.2.0...0.3.0

## 0.3.1 (2024-12-12)

## What's Changed
* BLOOM Default Smoothquant Mappings by @kylesayrs in https://github.com/vllm-project/llm-compressor/pull/906
* [SparseAutoModelForCausalLM Deprecation] Feature change by @horheynm in https://github.com/vllm-project/llm-compressor/pull/881
* Correct "dyanmic" typo by @kylesayrs in https://github.com/vllm-project/llm-compressor/pull/888
* Explicit defaults for QuantizationModifier targets by @kylesayrs in https://github.com/vllm-project/llm-compressor/pull/889
* [SparseAutoModelForCausalLM Deprecation] Update examples  by @horheynm in https://github.com/vllm-project/llm-compressor/pull/880
* Support pack_quantized format for nonuniform mixed-precision by @mgoin in https://github.com/vllm-project/llm-compressor/pull/913
* Actually make the `run_compressed` test useful by @dsikka in https://github.com/vllm-project/llm-compressor/pull/920
* Fix for e2e tests by @horheynm in https://github.com/vllm-project/llm-compressor/pull/927
* [Bugfix] Correct metrics calculations by @kylesayrs in https://github.com/vllm-project/llm-compressor/pull/878
* Update kv_cache example by @dsikka in https://github.com/vllm-project/llm-compressor/pull/921
* [1/2] Expand e2e testing to prepare for lm-eval by @dsikka in https://github.com/vllm-project/llm-compressor/pull/922
* Update pytest command to capture results to file by @dbarbuzzi in https://github.com/vllm-project/llm-compressor/pull/932
* [Bugfix] DisableKVCache Context by @kylesayrs in https://github.com/vllm-project/llm-compressor/pull/834
* Add helpful info to the marlin-24 example  by @dsikka in https://github.com/vllm-project/llm-compressor/pull/946
* Remove requires_torch by @kylesayrs in https://github.com/vllm-project/llm-compressor/pull/949
* Remove unused sparseml.export utilities by @kylesayrs in https://github.com/vllm-project/llm-compressor/pull/950
* Implement HooksMixin by @kylesayrs in https://github.com/vllm-project/llm-compressor/pull/917
* Add LM Eval Testing by @dsikka in https://github.com/vllm-project/llm-compressor/pull/945
* update version by @dsikka in https://github.com/vllm-project/llm-compressor/pull/969


**Full Changelog**: https://github.com/vllm-project/llm-compressor/compare/0.3.0...0.3.1

## 0.4.0 (2025-01-16)

## What's Changed
* Record config file name as test suite property by @dbarbuzzi in https://github.com/vllm-project/llm-compressor/pull/947
* Update setup.py by @dsikka in https://github.com/vllm-project/llm-compressor/pull/975
* Depreciate OBCQ Helpers by @kylesayrs in https://github.com/vllm-project/llm-compressor/pull/977
* KV Cache, E2E Tests by @horheynm in https://github.com/vllm-project/llm-compressor/pull/742
* Use 1 GPU for offloading examples by @dsikka in https://github.com/vllm-project/llm-compressor/pull/979
* Replace tokenizer with processor by @kylesayrs in https://github.com/vllm-project/llm-compressor/pull/955
* Revert "KV Cache, E2E Tests (#742)" by @dsikka in https://github.com/vllm-project/llm-compressor/pull/989
* Fix SmoothQuant offload bug by @dsikka in https://github.com/vllm-project/llm-compressor/pull/978
* Add LM Eval Configs by @dsikka in https://github.com/vllm-project/llm-compressor/pull/980
* Fix `test_model_reload` test by @kylesayrs in https://github.com/vllm-project/llm-compressor/pull/1005
* Calibration and Compression Contexts by @kylesayrs in https://github.com/vllm-project/llm-compressor/pull/998
* Add info for clarity by @dsikka in https://github.com/vllm-project/llm-compressor/pull/1009
* [Bugfix] Pass `trust_remote_code_model=True` for deepseek examples by @dsikka in https://github.com/vllm-project/llm-compressor/pull/1012
* Vision Datasets by @kylesayrs in https://github.com/vllm-project/llm-compressor/pull/943
* Add example for fp8 kv cache of phi3.5 and gemma2 by @mgoin in https://github.com/vllm-project/llm-compressor/pull/991
* Update ReadMe and test for cpu_offloading by @dsikka in https://github.com/vllm-project/llm-compressor/pull/1013
* Adding amdsmi for AMD gpus by @citrix123 in https://github.com/vllm-project/llm-compressor/pull/1018
* CompressionLogger add time units by @kylesayrs in https://github.com/vllm-project/llm-compressor/pull/1026
* patch_tied_tensors_bug: support malformed model definitions by @kylesayrs in https://github.com/vllm-project/llm-compressor/pull/1014
* Add: 2of4 example with/without fp8 quantization by @rahul-tuli in https://github.com/vllm-project/llm-compressor/pull/1033
* Remove unccessary step in 2of4 Example by @dsikka in https://github.com/vllm-project/llm-compressor/pull/1034
* Remove Neural Magic copyright from files by @kylesayrs in https://github.com/vllm-project/llm-compressor/pull/992
* VLM Support via GPTQ Hooks and Data Pipelines by @kylesayrs in https://github.com/vllm-project/llm-compressor/pull/914
* [E2E Testing] KV-Cache by @horheynm in https://github.com/vllm-project/llm-compressor/pull/1004
* [E2E Testing] Add recipe check vllm e2e by @horheynm in https://github.com/vllm-project/llm-compressor/pull/929
* [MoE] GPTQ compress using callback not hook by @kylesayrs in https://github.com/vllm-project/llm-compressor/pull/1049
* Explicit dataset tokenizer `text` kwarg by @kylesayrs in https://github.com/vllm-project/llm-compressor/pull/1031
* Fix smoothquant ignore, Fix typing, Add glm mappings by @kylesayrs in https://github.com/vllm-project/llm-compressor/pull/1015
* [Test Fix] Quant model reload by @horheynm in https://github.com/vllm-project/llm-compressor/pull/974
* Remove old examples by @dsikka in https://github.com/vllm-project/llm-compressor/pull/1062
* VLM: Fix typo bug in TraceableLlavaForConditionalGeneration by @kylesayrs in https://github.com/vllm-project/llm-compressor/pull/1065
* Add tests for "examples/sparse_2of4_[...]" by @dbarbuzzi in https://github.com/vllm-project/llm-compressor/pull/1067
* VLM Image Examples by @kylesayrs in https://github.com/vllm-project/llm-compressor/pull/1064
* Add quick warning for DeepSeek with transformers 4.48.0 by @dsikka in https://github.com/vllm-project/llm-compressor/pull/1066
* [KV Cache] kv-cache end to end unit tests by @horheynm in https://github.com/vllm-project/llm-compressor/pull/141
* [E2E Testing] Fix HF upload by @horheynm in https://github.com/vllm-project/llm-compressor/pull/1061
* [Test Fix] Fix/update test_run_compressed by @horheynm in https://github.com/vllm-project/llm-compressor/pull/970
* Revert "[Test Fix] Fix/update test_run_compressed" by @mgoin in https://github.com/vllm-project/llm-compressor/pull/1071
* Sparse 2:4 + FP8 Quantization e2e vLLM tests by @dsikka in https://github.com/vllm-project/llm-compressor/pull/1073
* [Test Patch] Remove redundant code for "Fix/update test_run_compressed" by @horheynm in https://github.com/vllm-project/llm-compressor/pull/1072
* bump; set ct version by @dsikka in https://github.com/vllm-project/llm-compressor/pull/1076

## New Contributors
* @citrix123 made their first contribution in https://github.com/vllm-project/llm-compressor/pull/1018

**Full Changelog**: https://github.com/vllm-project/llm-compressor/compare/0.3.1...0.4.0

## 0.4.1 (2025-02-20)

## What's Changed
* Remove version by @dsikka in https://github.com/vllm-project/llm-compressor/pull/1077
* Require 'ready' label for transformers tests by @dbarbuzzi in https://github.com/vllm-project/llm-compressor/pull/1079
* GPTQModifier Nits and Code Clarity by @kylesayrs in https://github.com/vllm-project/llm-compressor/pull/1068
* Also run on pushes to `main` by @dbarbuzzi in https://github.com/vllm-project/llm-compressor/pull/1083
* VLM: Phi3 Vision Example by @kylesayrs in https://github.com/vllm-project/llm-compressor/pull/1032
* VLM: Qwen2_VL Example by @kylesayrs in https://github.com/vllm-project/llm-compressor/pull/1027
* Composability with sparse and quantization compressors by @rahul-tuli in https://github.com/vllm-project/llm-compressor/pull/948
* Remove `TraceableMistralForCausalLM` by @kylesayrs in https://github.com/vllm-project/llm-compressor/pull/1052
* [Fix Test Failure]: Propagate name change to test by @rahul-tuli in https://github.com/vllm-project/llm-compressor/pull/1088
* [Audio] Support Audio Datasets by @kylesayrs in https://github.com/vllm-project/llm-compressor/pull/1085
* [Test Fix] Add Quantization then finetune tests  by @horheynm in https://github.com/vllm-project/llm-compressor/pull/964
* [Smoothquant] Phi3 Vision Mappings by @kylesayrs in https://github.com/vllm-project/llm-compressor/pull/1089
* [VLM] Multimodal Data Collator by @kylesayrs in https://github.com/vllm-project/llm-compressor/pull/1087
* VLM: Model Tracing Guide by @kylesayrs in https://github.com/vllm-project/llm-compressor/pull/1030
* Turn off 2:4 sparse compression until supported in vllm by @rahul-tuli in https://github.com/vllm-project/llm-compressor/pull/1092
* [Test Fix] Fix Consecutive oneshot by @horheynm in https://github.com/vllm-project/llm-compressor/pull/971
* [Bug Fix] Fix test that requre GPU by @horheynm in https://github.com/vllm-project/llm-compressor/pull/1096
* Add Idefics3/SmolVLM quant support via traceable class by @leon-seidel in https://github.com/vllm-project/llm-compressor/pull/1095
* Traceability Guide: Clarity and typo by @kylesayrs in https://github.com/vllm-project/llm-compressor/pull/1099
* [VLM] Examples README by @kylesayrs in https://github.com/vllm-project/llm-compressor/pull/1057
* Raise warning for 24 compressed sparse-only models by @rahul-tuli in https://github.com/vllm-project/llm-compressor/pull/1107
* Remove log_model_load by @kylesayrs in https://github.com/vllm-project/llm-compressor/pull/1016
* Return empty sparsity config if targets and ignores are empty by @rahul-tuli in https://github.com/vllm-project/llm-compressor/pull/1115
* Remove uses of get_observer by @kylesayrs in https://github.com/vllm-project/llm-compressor/pull/939
* FSDP utils cleanup by @kylesayrs in https://github.com/vllm-project/llm-compressor/pull/854
* Update maintainers, add notice by @kylesayrs in https://github.com/vllm-project/llm-compressor/pull/1091
* Replace readme paths with urls by @kylesayrs in https://github.com/vllm-project/llm-compressor/pull/1097
* GPTQ add Arkiv link, move file location by @kylesayrs in https://github.com/vllm-project/llm-compressor/pull/1100
* Extend `remove_hooks` to remove subsets by @kylesayrs in https://github.com/vllm-project/llm-compressor/pull/1021
* [Audio] Whisper Example and Readme by @kylesayrs in https://github.com/vllm-project/llm-compressor/pull/1106
* [Audio] Add whisper fp8 dynamic example by @kylesayrs in https://github.com/vllm-project/llm-compressor/pull/1111
* [VLM] Update pixtral data collator to reflect latest transformers changes by @kylesayrs in https://github.com/vllm-project/llm-compressor/pull/1116
* Use unique test names in `TestvLLM` by @dbarbuzzi in https://github.com/vllm-project/llm-compressor/pull/1124
* Remove smoothquant from examples by @kylesayrs in https://github.com/vllm-project/llm-compressor/pull/1121
* Extend `disable_hooks` to keep subsets by @kylesayrs in https://github.com/vllm-project/llm-compressor/pull/1023
* Unpin `pynvml` to fix e2e test failures with vLLM by @dsikka in https://github.com/vllm-project/llm-compressor/pull/1125
* Replace LayerCompressor with HooksMixin by @kylesayrs in https://github.com/vllm-project/llm-compressor/pull/1038
* [Oneshot Refactor] Rename get_shared_processor_src to get_processor_name_from_model by @horheynm in https://github.com/vllm-project/llm-compressor/pull/1108
* Allow Shortcutting Min-max Observer by @kylesayrs in https://github.com/vllm-project/llm-compressor/pull/887
* [Polish] Remove unused code by @horheynm in https://github.com/vllm-project/llm-compressor/pull/1128
* Properly restore training mode with `eval_context` by @kylesayrs in https://github.com/vllm-project/llm-compressor/pull/1126
* SQ and QM: Remove `torch.cuda.empty_cache`, use `calibration_forward_context` by @kylesayrs in https://github.com/vllm-project/llm-compressor/pull/1114
* [Oneshot Refactor] dataclass Arguments by @horheynm in https://github.com/vllm-project/llm-compressor/pull/1103
* [Bugfix] SparseGPT, Pipelines by @kylesayrs in https://github.com/vllm-project/llm-compressor/pull/1130
* [Oneshot refactor] Refactor initialize_model_from_path by @horheynm in https://github.com/vllm-project/llm-compressor/pull/1109
* [e2e] Update vllm tests with additional datasets by @brian-dellabetta in https://github.com/vllm-project/llm-compressor/pull/1131
* Update: SparseGPT recipes by @rahul-tuli in https://github.com/vllm-project/llm-compressor/pull/1142
* Add timer support for testing by @dsikka in https://github.com/vllm-project/llm-compressor/pull/1137
* [Audio] Support Whisper V3 by @kylesayrs in https://github.com/vllm-project/llm-compressor/pull/1147
* Fix: Re-enable Sparse Compression for 2of4 Examples by @rahul-tuli in https://github.com/vllm-project/llm-compressor/pull/1153
* [VLM] Add caption to flickr dataset by @kylesayrs in https://github.com/vllm-project/llm-compressor/pull/1138
* [VLM] Update mllama traceable definition by @kylesayrs in https://github.com/vllm-project/llm-compressor/pull/1140
* Fix CPU Offloading  by @dsikka in https://github.com/vllm-project/llm-compressor/pull/1159
* [TRL_SFT_Trainer] Fix and Update Examples code by @horheynm in https://github.com/vllm-project/llm-compressor/pull/1161
* [TRL_SFT_Trainer] Fix TRL-SFT Distillation Training by @horheynm in https://github.com/vllm-project/llm-compressor/pull/1163
* Bump version for patch release by @dsikka in https://github.com/vllm-project/llm-compressor/pull/1166
* Update DeepSeek Examples  by @dsikka in https://github.com/vllm-project/llm-compressor/pull/1175
* Update gemma2 examples with a note about sample generation by @dsikka in https://github.com/vllm-project/llm-compressor/pull/1176

## New Contributors
* @leon-seidel made their first contribution in https://github.com/vllm-project/llm-compressor/pull/1095

**Full Changelog**: https://github.com/vllm-project/llm-compressor/compare/0.4.0...0.4.1

## 0.5.0 (2025-04-03)

## What's Changed
* re-add vllm e2e test now that bug is fixed by @brian-dellabetta in https://github.com/vllm-project/llm-compressor/pull/1162
* Fix Readme Imports by @kylesayrs in https://github.com/vllm-project/llm-compressor/pull/1165
* Remove event_called by @kylesayrs in https://github.com/vllm-project/llm-compressor/pull/1155
* Update: Test name by @rahul-tuli in https://github.com/vllm-project/llm-compressor/pull/1172
* Remove lifecycle initialized_structure attribute by @kylesayrs in https://github.com/vllm-project/llm-compressor/pull/1156
* [VLM] Qwen 2.5 VL by @kylesayrs in https://github.com/vllm-project/llm-compressor/pull/1113
* Revert bump by @dsikka in https://github.com/vllm-project/llm-compressor/pull/1178
* Remove CLI by @dsikka in https://github.com/vllm-project/llm-compressor/pull/1144
* Add group act order case to lm_eval test by @dsikka in https://github.com/vllm-project/llm-compressor/pull/1080
* Update e2e test timings ouputs by @dsikka in https://github.com/vllm-project/llm-compressor/pull/1179
* [Oneshot Refactor] Main refactor by @horheynm in https://github.com/vllm-project/llm-compressor/pull/1110
* [StageRunner Removal] Remove Evalulate / validate pathway by @horheynm in https://github.com/vllm-project/llm-compressor/pull/1145
* [StageRemoval] Remove Predict pathway by @horheynm in https://github.com/vllm-project/llm-compressor/pull/1146
* Fix 2of4 Apply Example by @dsikka in https://github.com/vllm-project/llm-compressor/pull/1181
* Fix Sparse2of4 Example by @dsikka in https://github.com/vllm-project/llm-compressor/pull/1182
* Add qwen moe w4a16 example by @mgoin in https://github.com/vllm-project/llm-compressor/pull/1186
* [Callbacks] Consolidate Saving Methods by @kylesayrs in https://github.com/vllm-project/llm-compressor/pull/1168
* lmeval tests multimodal by @brian-dellabetta in https://github.com/vllm-project/llm-compressor/pull/1150
* [Dataset Performance] Add num workers on dataset processing - labels, tokenization by @horheynm in https://github.com/vllm-project/llm-compressor/pull/1189
* Fix a minor typo by @eldarkurtic in https://github.com/vllm-project/llm-compressor/pull/1191
* [Callbacks] Remove pre_initialize_structure by @kylesayrs in https://github.com/vllm-project/llm-compressor/pull/1160
* Make `transformers-tests` job conditional on files changed by @dbarbuzzi in https://github.com/vllm-project/llm-compressor/pull/1197
* Update finetune tests to decrease execution time by @dsikka in https://github.com/vllm-project/llm-compressor/pull/1208
* Update transformers tests to speed-up execution by @dsikka in https://github.com/vllm-project/llm-compressor/pull/1211
* Fix logging bug in oneshot.py by @aman2304 in https://github.com/vllm-project/llm-compressor/pull/1213
* [Training] Decouple Argument parser by @horheynm in https://github.com/vllm-project/llm-compressor/pull/1207
* Remove MonkeyPatch for GPUs by @dsikka in https://github.com/vllm-project/llm-compressor/pull/1227
* [Cosmetic] Rename data_args to dataset_args by @horheynm in https://github.com/vllm-project/llm-compressor/pull/1206
* [Training] Datasets - update Module by @horheynm in https://github.com/vllm-project/llm-compressor/pull/1209
* [BugFix] Fix logging disabling bug and add tests by @aman2304 in https://github.com/vllm-project/llm-compressor/pull/1218
* [Training] Unifying Preprocess + Postprocessing logic for Train/Oneshot by @horheynm in https://github.com/vllm-project/llm-compressor/pull/1212
* [Docs] Add info on when to use which PTQ/Sparsification by @horheynm in https://github.com/vllm-project/llm-compressor/pull/1157
* [Callbacks] Remove `MagnitudePruningModifier.leave_enabled` by @kylesayrs in https://github.com/vllm-project/llm-compressor/pull/1198
* Replace Xenova model stub with nm-testing model stub by @kylesayrs in https://github.com/vllm-project/llm-compressor/pull/1239
* Offload Cache Support torch.dtype by @kylesayrs in https://github.com/vllm-project/llm-compressor/pull/1141
* Remove unused/duplicated/non-applicable utils from pytorch/utils/helpers by @kylesayrs in https://github.com/vllm-project/llm-compressor/pull/1174
* [Bugfix] Staged 2of4 example by @kylesayrs in https://github.com/vllm-project/llm-compressor/pull/1238
* wandb/tensorboard loggers set default init to False by @brian-dellabetta in https://github.com/vllm-project/llm-compressor/pull/1235
* fixing reproducibility of lmeval tests by @brian-dellabetta in https://github.com/vllm-project/llm-compressor/pull/1220
* [Audio] People's Speech dataset and tracer tool by @kylesayrs in https://github.com/vllm-project/llm-compressor/pull/1086
* Use KV cache constant names provided by compressed tensors  by @kylesayrs in https://github.com/vllm-project/llm-compressor/pull/1200
* [Bugfix] Raise error for processor remote code by @kylesayrs in https://github.com/vllm-project/llm-compressor/pull/1184
* Remove missing weights silencers in favor of HFQuantizer solution by @kylesayrs in https://github.com/vllm-project/llm-compressor/pull/1017
* Fix run_compressed tests by @dsikka in https://github.com/vllm-project/llm-compressor/pull/1246
* [Train] Training Pipeline by @horheynm in https://github.com/vllm-project/llm-compressor/pull/1214
* [Tests] Increase maximum quantization error by @kylesayrs in https://github.com/vllm-project/llm-compressor/pull/1245
* [Callbacks] Remove EventLifecycle and on_start event by @kylesayrs in https://github.com/vllm-project/llm-compressor/pull/1170
* [Bugfix] Disable generation of deepseek models with transformers>=4.48 by @kylesayrs in https://github.com/vllm-project/llm-compressor/pull/1259
* Remove clear_ml by @dsikka in https://github.com/vllm-project/llm-compressor/pull/1261
* [Tests] Remove clear_ml test from GHA by @kylesayrs in https://github.com/vllm-project/llm-compressor/pull/1265
* Remove click by @dsikka in https://github.com/vllm-project/llm-compressor/pull/1262
* [Bugfix] Remove constant pruning from 2of4 examples by @kylesayrs in https://github.com/vllm-project/llm-compressor/pull/1267
* Addback: ConstantPruningModifier for finetuning cases by @rahul-tuli in https://github.com/vllm-project/llm-compressor/pull/1272
* Remove docker by @kylesayrs in https://github.com/vllm-project/llm-compressor/pull/1255
* move failing mulitmodal lmeval tests to skipped folder by @brian-dellabetta in https://github.com/vllm-project/llm-compressor/pull/1273
* Replace tj-action/changed-files by @dbarbuzzi in https://github.com/vllm-project/llm-compressor/pull/1270
* [BugFix]: Sparse2of4 example sparsity-only case by @rahul-tuli in https://github.com/vllm-project/llm-compressor/pull/1282
* Revert "update" by @dsikka in https://github.com/vllm-project/llm-compressor/pull/1296
* Fix Multi-Context Manager Syntax for Python 3.9 Compatibility by @rahul-tuli in https://github.com/vllm-project/llm-compressor/pull/1287
* Revert "Fix Multi-Context Manager Syntax for Python 3.9 Compatibility… by @dsikka in https://github.com/vllm-project/llm-compressor/pull/1300
* [StageRunner] Stage Runner entrypoint and pipeline by @horheynm in https://github.com/vllm-project/llm-compressor/pull/1202
* Bump: Min python version to 3.9 by @rahul-tuli in https://github.com/vllm-project/llm-compressor/pull/1288
* Keep quantization enabled during calibration by @kylesayrs in https://github.com/vllm-project/llm-compressor/pull/1299
* [BugFix] TRL distillation bug fix by @horheynm in https://github.com/vllm-project/llm-compressor/pull/1278
* Update: Readme for fp8 support by @rahul-tuli in https://github.com/vllm-project/llm-compressor/pull/1304
* [GPTQ] Add inversion fallback by @kylesayrs in https://github.com/vllm-project/llm-compressor/pull/1283
* fix typo by @eldarkurtic in https://github.com/vllm-project/llm-compressor/pull/1290
* [Tests] Fix oneshot + finetune test by passing splits to oneshot by @kylesayrs in https://github.com/vllm-project/llm-compressor/pull/1316
* [Tests] Remove the `compress` entrypoint by @dsikka in https://github.com/vllm-project/llm-compressor/pull/1317
* Fix Multi-Context Manager Syntax for Python 3.9 Compatibility by @rahul-tuli in https://github.com/vllm-project/llm-compressor/pull/1313
* [BugFix] Directly Convert Modifiers to Recipe Instance by @rahul-tuli in https://github.com/vllm-project/llm-compressor/pull/1271
* bump version, tag ct by @dsikka in https://github.com/vllm-project/llm-compressor/pull/1318

## New Contributors
* @aman2304 made their first contribution in https://github.com/vllm-project/llm-compressor/pull/1213

**Full Changelog**: https://github.com/vllm-project/llm-compressor/compare/0.4.1...0.5.0

## 0.5.1 (2025-04-29)

## What's Changed
* Update nm-actions/changed-files to v1.16.0 by @dbarbuzzi in https://github.com/vllm-project/llm-compressor/pull/1311
* docs: fix missing git clone command and repo name typos in DEVELOPING.md by @gattshjott in https://github.com/vllm-project/llm-compressor/pull/1325
* Update e2e/lm-eval test infrastructure by @dbarbuzzi in https://github.com/vllm-project/llm-compressor/pull/1323
* fix(logger): normalize log_file_level input for consistency by @gattshjott in https://github.com/vllm-project/llm-compressor/pull/1324
* [Utils] Replace `preserve_attr` with `patch_attr` by @kylesayrs in https://github.com/vllm-project/llm-compressor/pull/1187
* Fix cut off log in entrypoints/utils.py `post_process()` by @mgoin in https://github.com/vllm-project/llm-compressor/pull/1336
* [Tests] Update condition for sparsity check to be more robust by @dsikka in https://github.com/vllm-project/llm-compressor/pull/1337
* [Utils] Add `skip_weights_download` for developers and testing by @kylesayrs in https://github.com/vllm-project/llm-compressor/pull/1334
* replace custom version handling with setuptools-scm by @dhellmann in https://github.com/vllm-project/llm-compressor/pull/1322
* [Compression] Update sparsity calculation lifecycle when fetching the compressor by @dsikka in https://github.com/vllm-project/llm-compressor/pull/1332
* [Sequential] Support models with nested `_no_split_modules`  by @kylesayrs in https://github.com/vllm-project/llm-compressor/pull/1329
* [Tracing] Remove `TraceableWhisperForConditionalGeneration` by @kylesayrs in https://github.com/vllm-project/llm-compressor/pull/1310
* Add torch device to list of offloadable types by @kylesayrs in https://github.com/vllm-project/llm-compressor/pull/1348
* Reduce SmoothQuant Repr by @kylesayrs in https://github.com/vllm-project/llm-compressor/pull/1289
* Use `align_module_device` util by @kylesayrs in https://github.com/vllm-project/llm-compressor/pull/1298
* Fix project URL in setup.py by @tiran in https://github.com/vllm-project/llm-compressor/pull/1353
* Update trigger on PR comment workflow by @dbarbuzzi in https://github.com/vllm-project/llm-compressor/pull/1357
* Add timing functionality to lm-eval tests by @ved1beta in https://github.com/vllm-project/llm-compressor/pull/1346
* [Callbacks][Docs] Add docstrings to saving functions by @kylesayrs in https://github.com/vllm-project/llm-compressor/pull/1201
* Move: recipe parsing test from `e2e/` to main test suite by @rahul-tuli in https://github.com/vllm-project/llm-compressor/pull/1360
* Smoothquant typehinting by @kylesayrs in https://github.com/vllm-project/llm-compressor/pull/1285
* AWQ Modifier by @brian-dellabetta in https://github.com/vllm-project/llm-compressor/pull/1177
* [Tests] Update transformers tests to run kv_cache tests by @dsikka in https://github.com/vllm-project/llm-compressor/pull/1364
* [Transformers] Support latest transformers by @dsikka in https://github.com/vllm-project/llm-compressor/pull/1352
* Update test_consecutive_runs.py by @dsikka in https://github.com/vllm-project/llm-compressor/pull/1366
* [Docs] Mention AWQ, some clean-up by @dsikka in https://github.com/vllm-project/llm-compressor/pull/1367
* Fix versioning for source installs by @dbarbuzzi in https://github.com/vllm-project/llm-compressor/pull/1370
* [Testing] Reduce error verbosity of cleanup by @kylesayrs in https://github.com/vllm-project/llm-compressor/pull/1365
* Update test_oneshot_and_finetune.py to use pytest.approx by @markurtz in https://github.com/vllm-project/llm-compressor/pull/1339
* [Tracing] Better runtime error messages by @kylesayrs in https://github.com/vllm-project/llm-compressor/pull/1307
* [Tests] Fix test case; update structure by @dsikka in https://github.com/vllm-project/llm-compressor/pull/1375
* fix: Make Recipe.model_dump() output compatible with model_validate() by @ved1beta in https://github.com/vllm-project/llm-compressor/pull/1328
* Add: documentation for enhanced `save_pretrained` parameters by @rahul-tuli in https://github.com/vllm-project/llm-compressor/pull/1377
* Revert "fix: Make Recipe.model_dump() output compatible .... by @rahul-tuli in https://github.com/vllm-project/llm-compressor/pull/1378
* AWQ resolved mappings -- ensure shapes align by @brian-dellabetta in https://github.com/vllm-project/llm-compressor/pull/1372
* Update w4a16_actorder_weight.yaml lmeval config by @dbarbuzzi in https://github.com/vllm-project/llm-compressor/pull/1380
* [WIP] Add AWQ Asym e2e test case by @dsikka in https://github.com/vllm-project/llm-compressor/pull/1374
* Bump version; set ct version by @dsikka in https://github.com/vllm-project/llm-compressor/pull/1381
* bugfix AWQ with Llama models and python 3.9 by @brian-dellabetta in https://github.com/vllm-project/llm-compressor/pull/1384
* awq -- hotfix to missing kwargs by @brian-dellabetta in https://github.com/vllm-project/llm-compressor/pull/1395

## New Contributors
* @gattshjott made their first contribution in https://github.com/vllm-project/llm-compressor/pull/1325
* @dhellmann made their first contribution in https://github.com/vllm-project/llm-compressor/pull/1322
* @tiran made their first contribution in https://github.com/vllm-project/llm-compressor/pull/1353
* @ved1beta made their first contribution in https://github.com/vllm-project/llm-compressor/pull/1346

**Full Changelog**: https://github.com/vllm-project/llm-compressor/compare/0.5.0...0.5.1

## 0.5.2 (2025-06-24)

## What's Changed
* Exclude images from package by @kylesayrs in https://github.com/vllm-project/llm-compressor/pull/1397
* [Tracing] Skip non-ancestors of sequential targets by @kylesayrs in https://github.com/vllm-project/llm-compressor/pull/1389
* Consolidate build config by @dbarbuzzi in https://github.com/vllm-project/llm-compressor/pull/1398
* [Tests] Disable silently failing kv cache test by @kylesayrs in https://github.com/vllm-project/llm-compressor/pull/1371
* Drop `flash_attn` skip for quantizing_moe example tests by @dbarbuzzi in https://github.com/vllm-project/llm-compressor/pull/1396
* [VLM] Fix mllama targets by @kylesayrs in https://github.com/vllm-project/llm-compressor/pull/1402
* [Tests] Use requires_gpu, fix missing gpu test skip, add explicit test for gpu from gha by @kylesayrs in https://github.com/vllm-project/llm-compressor/pull/1264
* Implement `QuantizationMixin` by @kylesayrs in https://github.com/vllm-project/llm-compressor/pull/1351
* Add new-features section by @rahul-tuli in https://github.com/vllm-project/llm-compressor/pull/1408
* [Tracing] Support tracing of Gemma3 [#1248] by @kelkelcheng in https://github.com/vllm-project/llm-compressor/pull/1373
* bugfix kv cache quantization with ignored layers by @brian-dellabetta in https://github.com/vllm-project/llm-compressor/pull/1312
* AWQ sanitize_kwargs minor cleanup by @brian-dellabetta in https://github.com/vllm-project/llm-compressor/pull/1405
* [Tracing][Testing] Add tracing tests by @kylesayrs in https://github.com/vllm-project/llm-compressor/pull/1335
* fix lm eval test reproducibility issues by @brian-dellabetta in https://github.com/vllm-project/llm-compressor/pull/1260
* Pipeline Extraction by @kylesayrs in https://github.com/vllm-project/llm-compressor/pull/1279
* Add `pull_request` trigger to base tests workflow by @dbarbuzzi in https://github.com/vllm-project/llm-compressor/pull/1417
* removing RecipeMetadata and references by @shanjiaz in https://github.com/vllm-project/llm-compressor/pull/1414
* Update examples to only load required number of samples from dataset by @kylesayrs in https://github.com/vllm-project/llm-compressor/pull/1118
* [Tracing] Reinstate ignore functionality by @kylesayrs in https://github.com/vllm-project/llm-compressor/pull/1423
* [Typo] overriden by @kylesayrs in https://github.com/vllm-project/llm-compressor/pull/1420
* Rename SparsityModifierMixin to SparsityModifierBase by @kylesayrs in https://github.com/vllm-project/llm-compressor/pull/1416
* Remove RecipeArgs class & its references by @shanjiaz in https://github.com/vllm-project/llm-compressor/pull/1429
* [Examples] Standardize AWQ example by @kylesayrs in https://github.com/vllm-project/llm-compressor/pull/1412
* [Logging] Support logging once by @kylesayrs in https://github.com/vllm-project/llm-compressor/pull/1431
* Add: deepseekv2 smoothquant mappings by @rahul-tuli in https://github.com/vllm-project/llm-compressor/pull/1433
* AWQ QuantizationMixin + SequentialPipeline by @brian-dellabetta in https://github.com/vllm-project/llm-compressor/pull/1426
* patch awq tests/readme after QuantizationMixin refactor by @brian-dellabetta in https://github.com/vllm-project/llm-compressor/pull/1439
* Added more tests for Quantization24SparseW4A16 by @shanjiaz in https://github.com/vllm-project/llm-compressor/pull/1434
* [GPTQ] Add `actorder` option to modifier by @kylesayrs in https://github.com/vllm-project/llm-compressor/pull/1424
* [Bugfix][Tracing] Fix qwen2_5_vl by @kylesayrs in https://github.com/vllm-project/llm-compressor/pull/1448
* [Tests] Use proper offloading utils in `test_compress_tensor_utils` by @kylesayrs in https://github.com/vllm-project/llm-compressor/pull/1449
* [Tracing] Fix Traceable Imports by @kylesayrs in https://github.com/vllm-project/llm-compressor/pull/1452
* [NVFP4] Enable FP4 Weight-Only Quantization by @dsikka in https://github.com/vllm-project/llm-compressor/pull/1309
* Pin transformers to <4.52.0 by @brian-dellabetta in https://github.com/vllm-project/llm-compressor/pull/1459
* AWQ Apply Scales Bugfix when smooth layer output length doesn't match balance layer input length by @brian-dellabetta in https://github.com/vllm-project/llm-compressor/pull/1451
* Fix #1344 Extend e2e tests to add asym support for W8A8-Int8  by @ved1beta in https://github.com/vllm-project/llm-compressor/pull/1345
* [Tests] Fix activation recipe for w8a8 asym by @dsikka in https://github.com/vllm-project/llm-compressor/pull/1461
* AWQ Qwen and Phi mappings by @brian-dellabetta in https://github.com/vllm-project/llm-compressor/pull/1440
* [Observer] Optimize mse observer  by @shanjiaz in https://github.com/vllm-project/llm-compressor/pull/1450
* Fix: Improve `SmoothQuant` Support for Mixture of Experts (MoE) Models by @rahul-tuli in https://github.com/vllm-project/llm-compressor/pull/1455
* [Tests] Add nvfp4a16 e2e test case  by @dsikka in https://github.com/vllm-project/llm-compressor/pull/1463
* [Docs] Update README to list fp4 by @dsikka in https://github.com/vllm-project/llm-compressor/pull/1462
* Remove duplicate model id var from awq example recipe by @AndrewMead10 in https://github.com/vllm-project/llm-compressor/pull/1467
* Added observer type for test_min_max by @shanjiaz in https://github.com/vllm-project/llm-compressor/pull/1466
* Disable kernels during calibration (and tracing) by @kylesayrs in https://github.com/vllm-project/llm-compressor/pull/1454
* [GPTQ] Fix actorder resolution, add sentinel by @kylesayrs in https://github.com/vllm-project/llm-compressor/pull/1453
* Set `show_progress` to True by @dsikka in https://github.com/vllm-project/llm-compressor/pull/1471
* Remove `compress` by @dsikka in https://github.com/vllm-project/llm-compressor/pull/1470
* raise error if block quantization is used, as it is not yet supported by @brian-dellabetta in https://github.com/vllm-project/llm-compressor/pull/1476
* [Tests] Increase max seq length for tracing tests by @kylesayrs in https://github.com/vllm-project/llm-compressor/pull/1478
* [Tests] Fix dynamic field to be a bool, not string by @dsikka in https://github.com/vllm-project/llm-compressor/pull/1480
* [Examples] Fix qwen vision examples by @kylesayrs in https://github.com/vllm-project/llm-compressor/pull/1481
* [NVFP4] Update to use `tensor_group` strategy; update observers by @dsikka in https://github.com/vllm-project/llm-compressor/pull/1484
* loosen lmeval assertions to upper or lower bound by @brian-dellabetta in https://github.com/vllm-project/llm-compressor/pull/1477
* Revert "expand observers to calculate gparams, add example for activa… by @dsikka in https://github.com/vllm-project/llm-compressor/pull/1486
* fix rest of the minmax tests by @shanjiaz in https://github.com/vllm-project/llm-compressor/pull/1469
* Add warning for non-divisible group quantization by @kylesayrs in https://github.com/vllm-project/llm-compressor/pull/1401
* [AWQ] Support accumulation for reduced memory usage by @kylesayrs in https://github.com/vllm-project/llm-compressor/pull/1435
* [Tracing] Code AutoWrapper by @kylesayrs in https://github.com/vllm-project/llm-compressor/pull/1411
* Removed RecipeTuple & RecipeContainer class by @shanjiaz in https://github.com/vllm-project/llm-compressor/pull/1460
* Unpin to support `transformers==4.52.3` by @kylesayrs in https://github.com/vllm-project/llm-compressor/pull/1479
* [Tests] GPTQ Actorder Resolution Tests by @kylesayrs in https://github.com/vllm-project/llm-compressor/pull/1468
* [Testing] Skip FP4 Test by @dsikka in https://github.com/vllm-project/llm-compressor/pull/1499
* [Bugfix] Remove tracing imports from tests by @kylesayrs in https://github.com/vllm-project/llm-compressor/pull/1498
* [Testing] Use a slightly larger model that works with group_size 128 by @dsikka in https://github.com/vllm-project/llm-compressor/pull/1502
* skip tracing tests if token unavailable by @brian-dellabetta in https://github.com/vllm-project/llm-compressor/pull/1493
* Fix missing logs when calling oneshot by @kelkelcheng in https://github.com/vllm-project/llm-compressor/pull/1446
* [NVFP4] Expand observers to calculate gparam, support NVFP4 Activations by @dsikka in https://github.com/vllm-project/llm-compressor/pull/1487
* [Tests] Remove duplicate test by @kylesayrs in https://github.com/vllm-project/llm-compressor/pull/1500
* [Model] Mistral3 example and test by @kylesayrs in https://github.com/vllm-project/llm-compressor/pull/1490
* [NVFP4] Use observers to generate global weight scales  by @dsikka in https://github.com/vllm-project/llm-compressor/pull/1504
* Revert "[NVFP4] Use observers to generate global weight scales " by @dsikka in https://github.com/vllm-project/llm-compressor/pull/1507
* [NVFP4] Update global scale generation by @dsikka in https://github.com/vllm-project/llm-compressor/pull/1508
* [NVFP4] Fix onloading of fused layers by @dsikka in https://github.com/vllm-project/llm-compressor/pull/1512
* Pin pandas to <2.3 by @dbarbuzzi in https://github.com/vllm-project/llm-compressor/pull/1515
* AWQModifier fast resolve mappings, better logging, MoE support by @brian-dellabetta in https://github.com/vllm-project/llm-compressor/pull/1444
* Update setup.py by @dsikka in https://github.com/vllm-project/llm-compressor/pull/1516
* Use model compression pathways by @kylesayrs in https://github.com/vllm-project/llm-compressor/pull/1419
* [Example] [Bugfix] Fix Gemma3 Generation by @kylesayrs in https://github.com/vllm-project/llm-compressor/pull/1517
* [Docs] Update ReadME details for FP4 by @dsikka in https://github.com/vllm-project/llm-compressor/pull/1519
* [Examples] [Bugfix] Perform sample generation before saving as compressed by @kylesayrs in https://github.com/vllm-project/llm-compressor/pull/1530
* Add citation information both in README as well as native GitHub file support by @markurtz in https://github.com/vllm-project/llm-compressor/pull/1527
* update compressed-tensors version requirement by @dhuangnm in https://github.com/vllm-project/llm-compressor/pull/1534

## New Contributors
* @kelkelcheng made their first contribution in https://github.com/vllm-project/llm-compressor/pull/1373
* @AndrewMead10 made their first contribution in https://github.com/vllm-project/llm-compressor/pull/1467

**Full Changelog**: https://github.com/vllm-project/llm-compressor/compare/0.5.1...0.5.2

## 0.6.0 (2025-06-24)

## What's Changed
* [Experimental] Mistral-format FP8 quantization by @mgoin in https://github.com/vllm-project/llm-compressor/pull/1359
* [Examples] [Bugfix] skip sparsity stats when saving checkpoints by @kylesayrs in https://github.com/vllm-project/llm-compressor/pull/1528
* [Examples] [Bugfix] Fix debug message by @kylesayrs in https://github.com/vllm-project/llm-compressor/pull/1529
* [Tests][NVFP4] No longer skip NVFP4A16 e2e test by @dsikka in https://github.com/vllm-project/llm-compressor/pull/1538
* [AWQ] Support for Calibration Datasets of varying feature dimension by @brian-dellabetta in https://github.com/vllm-project/llm-compressor/pull/1536
* fix qwen 2.5 VL multimodal example by @brian-dellabetta in https://github.com/vllm-project/llm-compressor/pull/1541
* [Example] [Bugfix] Fix Gemma ignore list by @kylesayrs in https://github.com/vllm-project/llm-compressor/pull/1531
* [Tests][NVFP4] Add e2e nvfp4 test by @dsikka in https://github.com/vllm-project/llm-compressor/pull/1543
* [Examples] Use more robust splits by @kylesayrs in https://github.com/vllm-project/llm-compressor/pull/1544
* [Bugfix] [Autowrapper] Fix visit_Delete by @kylesayrs in https://github.com/vllm-project/llm-compressor/pull/1532
* [Example] Fix Qwen VL ignore list by @arunmadhusud in https://github.com/vllm-project/llm-compressor/pull/1545
* [Tests] Fix `Qwen2.5-VL-7B-Instruct` Recipe by @dsikka in https://github.com/vllm-project/llm-compressor/pull/1548
* [Bugfix] Fix gemma2 generation by @kylesayrs in https://github.com/vllm-project/llm-compressor/pull/1552
* fix skipif check on tests involving gated HF models by @brian-dellabetta in https://github.com/vllm-project/llm-compressor/pull/1553
* [NVFP4] Fix global scale update when dealing with offloaded layers by @dsikka in https://github.com/vllm-project/llm-compressor/pull/1554
* oneshot entrypoint update by @ved1beta in https://github.com/vllm-project/llm-compressor/pull/1445
* LM Eval tests -- ignore vision tower for VL fp8 test by @brian-dellabetta in https://github.com/vllm-project/llm-compressor/pull/1562
* [Performance] Sequential onloading by @kylesayrs in https://github.com/vllm-project/llm-compressor/pull/1263
* [BugFix] Explicitly set gpu_memory_utilization by @rahul-tuli in https://github.com/vllm-project/llm-compressor/pull/1560
* Add Axolotl blog link by @rahul-tuli in https://github.com/vllm-project/llm-compressor/pull/1563
* [Bugfix] Fix multigpu `dispatch_for_generation` by @kylesayrs in https://github.com/vllm-project/llm-compressor/pull/1567
* [Testing] Set `VLLM_WORKER_MULTIPROC_METHOD` for e2e testing by @dsikka in https://github.com/vllm-project/llm-compressor/pull/1569
* [BugFix] Fix quantizaiton_2of4_sparse_w4a16 example  by @shanjiaz in https://github.com/vllm-project/llm-compressor/pull/1565
* [Pipelines] infer model device with optional override by @kylesayrs in https://github.com/vllm-project/llm-compressor/pull/1572
* bump up requirement for compressed-tensors to 0.10.2 by @dhuangnm in https://github.com/vllm-project/llm-compressor/pull/1581

## New Contributors
* @arunmadhusud made their first contribution in https://github.com/vllm-project/llm-compressor/pull/1545

**Full Changelog**: https://github.com/vllm-project/llm-compressor/compare/0.5.2...0.6.0

## 0.6.0.1 (2025-07-28)

## What's Changed
* Cap transformers version for hotfix 0.6.0.1 by @dhuangnm in https://github.com/vllm-project/llm-compressor/pull/1671


**Full Changelog**: https://github.com/vllm-project/llm-compressor/compare/0.6.0...0.6.0.1

## 0.7.0 (2025-08-20)

<img width="1536" height="1024" alt="lc" src="https://github.com/user-attachments/assets/5a444678-2171-4712-867f-319f3d807316" />


# LLM Compressor v0.7.0 release notes

This LLM Compressor v0.7.0 release introduces the following new features and enhancements:
* Transforms support, including QuIP and SpinQuant algorithms
* Apply multiple compressors to a single model for mixed-precision quantization
* Support for DeepSeekV3-style block FP8 quantization
* Expanded Mixture of Experts (MoE) calibration support, including support with NVFP4 quantization
* Llama4 quantization support with vLLM compatibility
* Configurable observer arguments 
* Simplified and unified Recipe classes for easier usage and debugging

## Introducing Transforms :sparkles: 

LLM Compressor now supports transforms. With transforms, you can inject additional matrix operations within a model for the purposes of increasing the accuracy recovery as a result of quantization. Transforms allow rotating weights or activations into spaces with smaller dynamic ranges, reducing quantization error.

Two algorithms are supported in this release:
* **QuIP transforms** inject transforms before and after weights to assist with weight-only quantization
* **SpinQuant transforms** inject transforms whose inverses span across multiple weights, assisting in both weight and activation quantization. In this release, fused R1 and R2 (i.e. offline)  transforms are available. The full lifecycle has been validated to confirm that the models produced by LLM Compressor match the performance outlined in the original [SpinQuant paper](https://arxiv.org/abs/2405.16406). Learned rotations and online R3 and R4 rotations will be added in a future release.

The functionality for both algorithms available through the new `QuIPModifier` and `SpinQuantModifier` classes.

## Applying multiple compressors to a single model

LLM Compressor now supports applying multiple compressors to a single model. This extends support for non-uniform quantization recipes, such as combining NVFP4 and FP8 quantization. This provides finer control over per-layer quantization, allowing more precise handling of layers that are especially sensitive to certain quantization types.

Models with more than one compressor applied have their format set to `mixed-precision` in the `config.json` file. Additionally, each `config_group` now includes a format key that specifies the format used for the layers targeted by that group.

## Support for DeepSeekV3-style block FP8 quantization

You can now apply DeepSeekV3-style block FP8 quantization during model compression, a technique designed to further compress large language models for more efficient inference. The changes encompass the fundamental implementation of block-wise quantization, robust handling of quantization parameters, updated documentation, and a practical example to guide users in applying this new compression scheme.

## Mixture of Experts support

LLM Compressor now includes enhanced general Mixture of Experts (MoE) calibration support, including support for MoEs with NVFP4 quantization. Forward passes of the MoE models can be controlled during calibration by adding custom modules to the `replace_modules_for_calibration` function which permanently changes the MoE module or `moe_calibration_context` function to temporarily update modules during calibration.

## Llama4 quantization

LLama4 quantization is now supported in LLM Compressor. To be quantized and runnable in vLLM, `Llama4TextMoe` modules are permanently replaced using the `replace_modules_for_calibration` method which linearizes the modules. This allows the model to be quantized to schemes including WN16 with GPTQ and NVFP4.

## Simplified and updated Recipe classes

Recipe classes have been updated with the following features:

* Merged multiple recipe-related classes into a single, unified `Recipe` class
* Simplified modifier creation, lifecycle management, and parsing logic
* Improved serialization and deserialization for clarity and maintainability
* Reduced redundant stages and arguments handling for easier debugging and usage

## Configurable Observer arguments

Observer arguments can now be configured as a dict through the `observer_kwargs` quantization argument, which can be set through oneshot recipes.

## 0.7.1 (2025-08-21)

## What's Changed
* [Examples] Create qwen_2_5_vl_example.py by @Zhao-Dongyu in https://github.com/vllm-project/llm-compressor/pull/1752
* [fix] Fix visual layer ignore pattern for Qwen2.5-VL models by @Zhao-Dongyu in https://github.com/vllm-project/llm-compressor/pull/1766
* [Transform] Fix QuIP targets by @kylesayrs in https://github.com/vllm-project/llm-compressor/pull/1770

## New Contributors
* @Zhao-Dongyu made their first contribution in https://github.com/vllm-project/llm-compressor/pull/1752

**Full Changelog**: https://github.com/vllm-project/llm-compressor/compare/0.7.0...0.7.1

## 0.8.0 (2025-10-03)

<img width="1536" height="1024" alt="0 8 0" src="https://github.com/user-attachments/assets/e7f1840f-fd6c-4dd7-a876-3b44b3c8bd29" />

# LLM Compressor v0.8.0 release notes

This LLM Compressor v0.8.0 release introduces the following new features and enhancements:

* Support for multiple modifiers in oneshot compression runs
* Quantization and calibration support for Qwen3 models including FP8 quantization support for Qwen3 VL MoE models
* Transforms support for non-full-size rotation sizes
* Improved accuracy recovery by updating W4A16 schemes to use `actorder` "weight" by default

## Support for multiple modifiers in oneshot compression runs ✨
<!-- https://issues.redhat.com/browse/INFERENG-1439 -->

LLM Compressor now supports using multiple modifiers in oneshot compression runs.

You can apply multiple modifiers across model layers. This includes applying different modifiers, such as AWQ and GPTQ, to specific submodules for W4A16 quantization all within a single oneshot call and with only pass-through calibration data.

Using multiple modifiers improves non-uniform model quantization, addressing issues such as varying layer sensitivity.

For more information, see [Non-uniform quantization](https://github.com/vllm-project/llm-compressor/tree/main/examples/quantization_non_uniform).

## Quantization and calibration support for Qwen3 models
<!-- https://issues.redhat.com/browse/INFERENG-2363 -->

Quantization and calibration support for Qwen3 models has been added to LLM Compressor.

An updated `Qwen3NextSparseMoeBlock` modeling definition has been added to temporarily update the MoE block during calibration in order to ensure that all the experts see data and are calibrated appropriately. This allows all experts to have calibrated scales while ensuring only the gated activation values are used.

FP8 and NVFP4 quantization examples have been added for the Qwen3-Next-80B-A3B-Instruct model. For more information see:

- [examples/quantization_w8a8_fp8/qwen3_next_example.py](https://github.com/vllm-project/llm-compressor/blob/main/examples/quantization_w8a8_fp8/qwen3_next_example.py)
- [examples/quantization_w4a4_fp4/qwen3_next_example.py](https://github.com/vllm-project/llm-compressor/blob/main/examples/quantization_w4a4_fp4/qwen3_next_example.py)

### FP8 quantization support for Qwen3 VL MoE models
<!-- https://issues.redhat.com/browse/INFERENG-2364 -->

LLM Compressor now supports quantization for Qwen3 VL MoE models. You can now use data-free pathways such as FP8 channel-wise and block-wise quantization. Pathways requiring data such W4A16 and NVFP4 are planned for a future release.

Examples have been added for FP8 quantization for the Qwen/Qwen3-VL-235B-A22B-Instruct model. 
For more information see:

- [examples/quantization_w8a8_fp8/qwen3_vl_moe_fp8_example.py](https://github.com/vllm-project/llm-compressor/blob/main/examples/quantization_w8a8_fp8/qwen3_vl_moe_fp8_example.py)

An updated definition has been added for `Qwen3VLMoeTextSparseMoeBlock` which replaces all the MoE blocks with a linearized model definition such that a list of layers is used as opposed to a 3D parameter. This model definition enables quantization and is runnable in vLLM.

## Transforms support for non-full-size rotation sizes
<!-- https://issues.redhat.com/browse/INFERENG-1882 -->

You can now set a `transform_block_size` field in the Transform-based modifier classes `SpinQuantModifier` and `QuIPModifier`. You can configure transforms of variable size with this field, and you no longer need to restrict hadamards to match the size of the weight.

It is typically beneficial to set the hadamard block size to match the quantization group size. Examples have been updated to show how to use this field when applying the QuIP Modifier. 

For more information, see:

- [quip_example.py](https://github.com/vllm-project/llm-compressor/blob/main/examples/transform/quip_example.py)
- [spinquant_example.py](https://github.com/vllm-project/llm-compressor/blob/main/examples/transform/spinquant_example.py)

To efficiently run QuIP-style rotations using the hadacore kernels in vLLM, see [examples/transform/README.md](https://github.com/vllm-project/llm-compressor/blob/main/examples/transform/README.md).

## Improved accuracy recovery by updating W4A16 schemes to use actorder "weight" by default

<!-- https://issues.redhat.com/browse/INFERENG-102 -->

The `GPTQModifier` class now uses "weight" activation ordering by default. Weight or "static" activation ordering has been shown to significantly improve accuracy recovery with no additional cost at runtime.

For more information and benchmarks, see [vllm/pull/8135](https://github.com/vllm-project/vllm/pull/8135)

## Updates and deprecations

### Support for R4 spinquant-style transforms

<!-- https://issues.redhat.com/browse/INFERENG-1142 -->

Support for R4 spinquant-style transforms has been added, which allows quantization of the `down_proj` layer with increased accuracy recovery. You can use this transform by specifying `SpinQuantModifier(rotations=["R4"])` in the oneshot recipe.

### Re-enabled support for W8A8 INT8 decompression
<!-- https://issues.redhat.com/browse/INFERENG-601 -->

W8A8 INT8 decompression and model generation has been re-enabled in LLM Compressor.

The following changes have been made:

- The `ModelCompressor` class has been updated to support compressing models initialized on the meta device.
- The `SparseCompressor` and `QuantizationCompressor` classes have been modified to be compatible with meta devices.
- The `compress_weight()` function has been modified across sparse compressors to accept module input, enabling correct behavior for meta-initialized shells.
- Decompression and offload device detection has been updated to handle meta modules and empty modules gracefully.

### Updated ignore lists in example recipes to capture all vision components

Ignore lists in example recipes were updated to correctly capture all vision components. Previously, some vision components like `model.vision_tower` were not being caught, causing downstream issues when serving models with vLLM.

### Deprecated and removed unittest.TestCase
<!-- https://issues.redhat.com/browse/INFERENG-1877 -->

The `unittest.TestCase` test case has been deprecated and removed and has been replaced with standardized `pytest` test definitions.

## 0.8.1 (2025-10-08)

## What's Changed
* Pick up compressed-tensors 0.12.2 for patch release by @dhuangnm in https://github.com/vllm-project/llm-compressor/pull/1904


**Full Changelog**: https://github.com/vllm-project/llm-compressor/compare/0.8.0...0.8.1

## 0.9.0 (2025-12-17)

<img width="1247" height="745" alt="lc0 9 0" src="https://github.com/user-attachments/assets/b84bc562-c603-4390-9a71-8fc8b6823a7e" />

# LLM Compressor v0.9.0 Release Notes

While working on this release, LLM Compressor reached over 100 contributors. Thank you to everyone for your contributions!

This LLM Compressor v0.9.0 release adds:

- Extended KV cache and attention quantization support
- Batched calibration support
- A new `model_free_ptq` pathway
- A new _AutoRound_ modifier
- Experimental support for MXFP4 quantization

Additionally, this release finalizes the initial support work for SpinQuant R3 style transforms.
This release also updates AWQ support to be further simplified and generic to quantization schemes beyond W4A16.

<!-- https://issues.redhat.com/browse/INFERENG-2911 -->
## Updated support for KV Cache and attention quantization ✨

KV cache quantization has been refactored to address limitations in supported schemes and lifecycle-related bugs.
The implementation has moved to compressed tensors, with new support for attention quantization.

This refactoring enables the following updates:
- Quantization of KV cache and attention using any scheme, including the new per-head strategy.
- Running KV/attention quantization experiments within Hugging Face for research and accuracy validation.
- Full compatibility with attention rotation via transforms.

These changes lay the groundwork for future work in creating and researching advanced attention and KV-cache quantized models.

<!-- https://issues.redhat.com/browse/INFERENG-3135 -->
<!-- https://issues.redhat.com/browse/INFERENG-3136 -->
## Added model-free post-training quantization ✨

Model-free post-training quantization (PTQ) enables quantization by directly operating on safetensors files.
This is particularly useful for models without a `transformers` model definition, such as some Mistral models.

> [!NOTE]
> Model-free PTQ currently supports data-free methods only, specifically FP8 quantization. 
> Model-free PTQ was used to quantize the [Mistral Large 3](https://huggingface.co/mistralai/Mistral-Large-3-675B-Instruct-2512) model.

See the [model_free_ptq](https://github.com/vllm-project/llm-compressor/tree/main/examples/model_free_ptq) usage examples for more information.

## Added AutoRound modifier

Added [AutoRoundModifier](https://github.com/vllm-project/llm-compressor/blob/main/examples/autoround/llama3_example.py) for quantization that uses [AutoRound](https://aclanthology.org/2024.findings-emnlp.662.pdf), an advanced post-training algorithm that optimizes rounding and clipping ranges through sign-gradient descent.
This approach combines the efficiency of post-training quantization with the adaptability of parameter tuning, delivering robust compression for large language models while maintaining strong performance.

<!-- https://issues.redhat.com/browse/INFERENG-2542 -->
## Calibration performance improvements

LLM Compressor now supports batched calibration for quantization and sparsification.

You can pass in `batch_size` and `data_collator` arguments to the `oneshot` compression entrypoint for improved calibration throughput. For built-in collation strategies, pass `"padding"` or `"truncation"` as string values for `data_collator`. The default collator from the `DefaultDataCollator` class is now `"truncation"`. The default value for `shuffle_calibration_samples` is now `False`.

<!-- https://issues.redhat.com/browse/INFERENG-2543 -->
<!-- https://issues.redhat.com/browse/INFERENG-3572 -->
## AWQ modifier updates

AWQ has been generalized to support more quantization types.
The previous implementation used one-off quantization logic that limited supported configurations.
By adopting existing LLM Compressor abstractions, the code is now simpler and supports new quantization schemes including INT8, FP8, and mixed schemes within a single model.

AWQ and SmoothQuant PTQ implementations previously used a suboptimal mapping-matching logic.
SmoothQuant couldn't handle MoE models, AWQ had buggy skip-layer logic, and neither could support certain parent contexts.

The `match_module_set` helper has been updated to handle all necessary situations, and both techniques now use this shared helper.
This enables SmoothQuant and AWQ support for MoE models, improves code maintainability, and eliminates several potential sources of bugs.

<!-- https://issues.redhat.com/browse/INFERENG-2661 -->
<!-- https://issues.redhat.com/browse/INFERENG-2662 -->
## Refactored observer functionality

Observer functionality has been refactored for simplicity, with several new observers introduced:

- `memoryless_minmax`: Computes min/max values in real time using dynamic quantization style. Recommended for PTQ weight quantization.
- `static_minmax`: Computes absolute min/max values across all observations.
Recommended for PTQ activation quantization.
- `memoryless_mse`: Computes optimal quantization parameters by minimizing MSE loss for each observation.
Recommended for PTQ weight quantization.

> [!IMPORTANT]
> `static_minmax` is now the default for NVFP4 activation quantization.
> Future releases will standardize on `memoryless_minmax` for weight quantization and `static_minmax` for activation quantization.

<!-- https://issues.redhat.com/browse/INFERENG-2365 -->
## Updated MoE calibration support with a new MoECalibrationModule class

An updated MoE calibration context that enables correct calibration of expert layers in MoE models has been added.
See the [moe_context.py#L29](https://github.com/vllm-project/llm-compressor/blob/main/src/llmcompressor/modeling/moe_context.py#L29) implementation for details.

The calibration context can be used to temporarily or permanently update MoE module definitions during calibration, ensuring all expert models receive data during forward passes.
This enables quantization support for Qwen3 VL and Qwen3 MoE models by using data-dependent schemes such as NVFP4, W4A16, and static activation quantization.

<!-- https://issues.redhat.com/browse/INFERENG-2164 -->
## Extended LLM Compressor activation quantization support

LLM Compressor now supports dynamic, group, and channel activation quantization for models.

<!-- https://issues.redhat.com/browse/INFERENG-1889 -->
<!-- https://issues.redhat.com/browse/INFERENG-1890 -->
## Added experimental support for MXFP4 quantization

LLM Compressor and compressed-tensors now support MXFP4 quantization and calibration of MXFP4 scales.
To use MXFP4 quantization, quantize models with the new MXFP4 preset scheme.
The `MXFP4PackedCompressor` class compresses and saves the model, packing both weights and scales as uint8 integers.

> [!NOTE]
> MXFP4 quantization is an experimental feature that is pending validation with vLLM.

### QuantizationArgs updates

Two new fields, `scale_dtype` and `zp_dtype`, have been added to the `QuantizationArgs` class:

- `scale_dtype`: When set to `None`, scales are saved using the default dense data type.
When specified, scales are compressed using the provided data type.
For example, NVFP4 saves scales as FP8, while MXFP4 saves them as uint8.
This data type is reflected in the model config.
- `zp_dtype`: Set to `None` for symmetric models.
For asymmetric models, this specifies the data type used to save zero-point values.

See the [quant_args.py#L157](https://github.com/vllm-project/compressed-tensors/blob/797d3019ef6867362796f412980547c74551f369/src/compressed_tensors/quantization/quant_args.py#L157) implementation for details.

<!-- https://issues.redhat.com/browse/INFERENG-2163 -->
## Added experimental R3 transforms support

LLM Compressor now has experimental support for applying transforms to attention in the style of the R3 rotation used in SpinQuant models.
R3 transforms can potentially increase accuracy recovery for extreme attention quantization.
R3 rotations are not yet supported in vLLM.

See the [llama3_attention_r3_nvfp4.py](https://github.com/vllm-project/llm-compressor/blob/main/examples/experimental/attention/llama3_attention_r3_nvfp4.py) example for details.

## Breaking changes

<!-- https://issues.redhat.com/browse/INFERENG-2422 -->
### Removed all training support APIs and functionality

Training support has been removed from LLM Compressor.
The `finetune` entrypoint and distillation modifier are no longer available.

For training workflows, use the LLM Compressor Axolotl integration.
See the [quantization_2of4_sparse_w4a16](https://github.com/vllm-project/llm-compressor/tree/main/examples/quantization_2of4_sparse_w4a16) examples for details.

<!-- https://issues.redhat.com/browse/INFERENG-2426 -->
### Removed support for Python 3.9

LLM Compressor v0.9.0 requires Python 3.10 or later.
LLM Compressor v0.8.0 is the last version to support Python 3.9.

## New Contributors
* @lkm2835 made their first contribution in https://github.com/vllm-project/llm-compressor/pull/1911
* @jessiewiswjc made their first contribution in https://github.com/vllm-project/llm-compressor/pull/1923
* @toncao made their first contribution in https://github.com/vllm-project/llm-compressor/pull/1925
* @siddhaka made their first contribution in https://github.com/vllm-project/llm-compressor/pull/1934
* @cajeonrh made their first contribution in https://github.com/vllm-project/llm-compressor/pull/1896
* @ojeda-e made their first contribution in https://github.com/vllm-project/llm-compressor/pull/1951
* @JartX made their first contribution in https://github.com/vllm-project/llm-compressor/pull/1947
* @zhanglei1172 made their first contribution in https://github.com/vllm-project/llm-compressor/pull/1942
* @ralphbean made their first contribution in https://github.com/vllm-project/llm-compressor/pull/1954
* @sairampillai made their first contribution in https://github.com/vllm-project/llm-compressor/pull/1851
* @stzoozz made their first contribution in https://github.com/vllm-project/llm-compressor/pull/1982
* @HDCharles made their first contribution in https://github.com/vllm-project/llm-compressor/pull/1963
* @sugatmahanti made their first contribution in https://github.com/vllm-project/llm-compressor/pull/1965
* @mratsim made their first contribution in https://github.com/vllm-project/llm-compressor/pull/2011
* @yiliu30 made their first contribution in https://github.com/vllm-project/llm-compressor/pull/1994
* @BigFaceBoy made their first contribution in https://github.com/vllm-project/llm-compressor/pull/2028
* @mutichung made their first contribution in https://github.com/vllm-project/llm-compressor/pull/2047
* @GOavi101 made their first contribution in https://github.com/vllm-project/llm-compressor/pull/2093
* @jaeminSon made their first contribution in https://github.com/vllm-project/llm-compressor/pull/2115

**Full Changelog**: https://github.com/vllm-project/llm-compressor/compare/0.8.1...0.9.0

## 0.9.0.1 (2026-01-21)

## What's Changed
* [v0.9.0.1 Fix] Make AutoRound Optional by @dsikka in https://github.com/vllm-project/llm-compressor/pull/2266

## Release Notes

### AutoRound installation change
AutoRound is no longer installed by default. It is now available as an optional dependency via llmcompressor[autoround]. Due to a known [upstream issue](https://github.com/intel/auto-round/issues/1296), AutoRound is currently supported only on x86_64 systems.

**Full Changelog**: https://github.com/vllm-project/llm-compressor/compare/0.9.0...0.9.0.1

## 0.9.0.2 (2026-02-13)

## What's Changed
* [Release 0.9.0.2] bump up pillow upper bound to 12.1.1 by @dhuangnm in https://github.com/vllm-project/llm-compressor/pull/2364


**Full Changelog**: https://github.com/vllm-project/llm-compressor/compare/0.9.0.1...0.9.0.2

## 0.10.0 (2026-03-02)

<img width="1536" height="1024" alt="header_v10_rel" src="https://github.com/user-attachments/assets/7af195ab-704d-45ab-9d7e-1653059cc9b3" />

# LLM Compressor v0.10.0

We're excited to announce LLM Compressor v0.10.0! This release brings significant performance improvements, updated quantization capabilities, and enhanced model offloading support.

**Highlights:**
- Distributed GPTQ with major performance improvements
- Enhanced compressed-tensors offloading (disk and distributed)
- Migration from accelerate to compressed-tensors offloading
- GPTQ support for FP4 microscale schemes (NVFP4, MXFP4)
- MXFP4 accuracy improvements


## Distributed Data Parallel (DDP) GPTQ Support ✨

GPTQ now supports fully distributed functionality, resulting in **significant speedups across the board**.

### Performance Benchmarks

| model_id | world_size | max_time | max_memory | save_time | flex_extract | eval_time |
|----------|------------|----------|------------|-----------|--------------|-----------|
| Meta-Llama-3-8B-Instruct | 1 | 745.03 | 5.82 | 19.57 | 0.7066 | 95.28 |
| Meta-Llama-3-8B-Instruct | 2 | 372.20 | 5.57 | 49.10 | 0.7089 | 95.24 |
| Meta-Llama-3-8B-Instruct | 4 | 264.07 | 5.82 | 52.50 | 0.7180 | 96.74 |
| Qwen3-30B-A3B | 1 | 14207.53 | 6.56 | 748.23 | 0.8704 | 209.93 |
| Qwen3-30B-A3B | 2 | 7018.25 | 6.36 | 696.65 | 0.8810 | 205.89 |
| Qwen3-30B-A3B | 4 | 3694.46 | 6.36 | 723.05 | 0.8832 | 217.62 |

GPTQ takes advantage of the underlying DDP improvements for calibration and adds on weight parallel compression. We also improved non-DDP GPTQ to be more accurate, resulting in a **free 5% GSM8K accuracy improvement** for Meta-Llama-3-8B-Instruct.

An example leveraging DDP with GPTQ can be found [here](https://github.com/vllm-project/llm-compressor/blob/main/examples/quantization_w4a16/llama3_ddp_example.py) and can be run using the following command, if running with 2 GPUs. 

```bash 
torchrun --nproc_per_node=2 llama3_ddp_example.py 
``` 

## Enhanced Compressed-Tensors Offloading ✨

<img width="1536" height="1024" alt="offload" src="https://github.com/user-attachments/assets/5cf921f2-ae64-4f0a-9b53-bc3c04cfb9f0" />

Compressed-tensors now supports loading transformers models that are **offloaded to disk** and/or **offloaded across distributed process ranks**.

### Disk Offloading

Disk offloading allows users to load and compress very large models which normally would not fit in CPU memory.

**Usage:**
```python
from compressed_tensors.offload import offloaded_model

with offloaded_model():
    AutoModelForCausalLM.from_pretrained(
        model_id,
        device_map="auto_offload",
        offload_folder="./offload_folder",
    )
```

**Examples**: 
- [Kimi-K2 with NVFP4](https://github.com/vllm-project/llm-compressor/blob/main/examples/disk_offloading/kimi_k2_example.py)

### Distributed Offloading

When loading offloaded models across distributed process ranks, `offloaded_model` ensures that the offloaded model memory is shared between ranks.

**Usage:**
```python
from compressed_tensors.offload import dist_init, offloaded_model

dist_init()  # initialize distributed process group
with offloaded_model():  # enables CT offloading
    AutoModelForCausalLM.from_pretrained(
        model_id,
        device_map="auto_offload",  # set device map
        offload_folder="./offload_folder",
    )

# (optional) partition dataset so don't have to load full dataset into cpu for each rank
ds = load_dataset(
    DATASET_ID,
    split=get_rank_partition(DATASET_SPLIT, NUM_CALIBRATION_SAMPLES)
)
# note: oneshot will also do partitioning if it detects DDP + all ranks have same data

# rest of flow is unchanged, set up modifiers and call oneshot, etc
```

Invoke the script with:
```bash
torchrun --nproc_per_node=<num_threads> script.py
```

### Offload Options Reference

**Non-Distributed Mode:**

| device_map | "auto" | "cuda" | "cpu" | "auto_offload" |
|------------|--------|--------|-------|----------------|
| offloaded_model required? | No | No | No | Yes |
| Behavior | Try to load model onto all visible cuda devices. Fallback to cpu and disk if model too large | Try to load model onto first cuda device only. Error if model is too large | Try to load model onto cpu. Error if the model is too large | Try to load model onto cpu. Fallback to disk if model is too large |
| LLM Compressor Use Case | Recommended for "basic" pipeline | | | Recommended for "sequential" pipeline |

**Distributed Mode:**

| device_map | "auto" | "cuda" | "cpu" | "auto_offload" |
|------------|--------|--------|-------|----------------|
| offloaded_model required? | Yes | Yes | Yes | Yes |
| Behavior | Try to load model onto device 0, then broadcast replicas to other devices. Fallback to cpu and disk if model too large | Try to load model onto device 0 only, then broadcast replicas to other devices. Error if model is too large | Try to load model onto cpu. Error if the model is too large | Try to load model onto cpu. Fallback to disk if model is too large |
| LLM Compressor Use Case | Recommended for "basic" pipeline | | | Recommended for "sequential" pipeline |

For more information regarding the behavior and options for loading offloaded models, see the [compressed-tensors PR #572](https://github.com/vllm-project/compressed-tensors/pull/572).


## Migration from Accelerate to Compressed-Tensors Offloading

**Important:** LLM Compressor v0.10 will no longer utilize offloading logic provided by huggingface's `accelerate` library, instead opting to integrate with model offloading provided by `compressed-tensors`.

### Benefits of Compressed-Tensors Offloading

The `compressed-tensors` offloading implementation provides many practical benefits over the `accelerate` library:

1. **Built for dynamic workloads** - CT offloading was designed for use cases like LLM Compressor's, where parameters are added and removed to modules, and module offloads can dynamically change.

2. **Universal model compatibility** - The architecture of accelerate offloading meant that many transformer models did not fully support it. Adding support often required changes and patches to the model definition. By contrast, CT offloading does not require any modifications to model definitions and works with full transparency across all transformer model definitions we've tested.

3. **Better performance** - CT offloading is often faster and requires lower peak memory than accelerate offloading due to its lazily loading implementation whereby individual parameters are only onloaded when required.

4. **Distributed support** - CT offloading supports distributed offloads coordinated between process ranks, allowing for models to be offloaded across ranks for parallelized workloads.

Models such as **qwen2_audio**, **whisper**, and others are now supported without requiring patches to the model definition.

### For further details on DDP and offloading support, see the [Big Models and Distributed Support guide](https://docs.vllm.ai/projects/llm-compressor/en/latest/guides/big_models_and_distributed/model_loading/)

## GPTQ FP4 Microscale Schemes Support

GPTQ now supports FP4 microscale schemes including **NVFP4** and **MXFP4**. Applying GPTQ to these schemes can result in improved recovery and overall quantization accuracy.

**Examples:**
- [MXFP4 Llama3 Example](https://github.com/vllm-project/llm-compressor/blob/main/examples/quantization_w4a16_fp4/mxfp4/llama3_example.py)
- [W4A4 FP4 GPTQ Example](https://github.com/vllm-project/llm-compressor/blob/main/examples/quantization_w4a4_fp4/llama3_gptq_example.py)


## MXFP4 Accuracy Improvements

MXFP4 support has been updated with accuracy improvements for its weight scale generation. The updated models can now be validated in vLLM using the marlin kernel when doing weight-only quantization (MXFP4A16).

This is supported as of vLLM v0.14.0: [compressed_tensors_w4a16_mxfp4.py](https://github.com/vllm-project/vllm/blob/main/vllm/model_executor/layers/quantization/compressed_tensors/schemes/compressed_tensors_w4a16_mxfp4.py)

**Note: MXFP4 with activation qauntization is not yet enabled in vLLM for compressed-tensors models.**

## AWQ Performance Improvements

Large scale refactor and optimization of AWQ resulted in:
- **5-10% speedup** on dense models
- **1-5% speedup** on MoE models

## Package Updates
- AutoRound is now a required package 
- An optional extra `qwen` has been added for pre-processing utilities (e.g qwen_vl_utils) that can be used for Qwen VL examples, such as https://github.com/vllm-project/llm-compressor/blob/main/examples/multimodal_vision/qwen3_vl_example.py

## New Contributors
* @aaarrvind made their first contribution in https://github.com/vllm-project/llm-compressor/pull/2121
* @isharif168 made their first contribution in https://github.com/vllm-project/llm-compressor/pull/2113
* @jangel97 made their first contribution in https://github.com/vllm-project/llm-compressor/pull/2109
* @JasonZhao47 made their first contribution in https://github.com/vllm-project/llm-compressor/pull/2182
* @antbob made their first contribution in https://github.com/vllm-project/llm-compressor/pull/2175
* @majiayu000 made their first contribution in https://github.com/vllm-project/llm-compressor/pull/2184
* @pdaxt made their first contribution in https://github.com/vllm-project/llm-compressor/pull/2185
* @mengniwang95 made their first contribution in https://github.com/vllm-project/llm-compressor/pull/2100
* @ishrith-gowda made their first contribution in https://github.com/vllm-project/llm-compressor/pull/2174
* @ZewenShen-Cohere made their first contribution in https://github.com/vllm-project/llm-compressor/pull/2189
* @Monishver11 made their first contribution in https://github.com/vllm-project/llm-compressor/pull/2214
* @jwpark33 made their first contribution in https://github.com/vllm-project/llm-compressor/pull/2204
* @xin3he made their first contribution in https://github.com/vllm-project/llm-compressor/pull/2169
* @menogrey made their first contribution in https://github.com/vllm-project/llm-compressor/pull/2200
* @maliktafheem made their first contribution in https://github.com/vllm-project/llm-compressor/pull/2229
* @mergify[bot] made their first contribution in https://github.com/vllm-project/llm-compressor/pull/2241
* @Felixqaq made their first contribution in https://github.com/vllm-project/llm-compressor/pull/2244
* @Etelis made their first contribution in https://github.com/vllm-project/llm-compressor/pull/2246
* @phaelon74 made their first contribution in https://github.com/vllm-project/llm-compressor/pull/2170
* @gDINESH13 made their first contribution in https://github.com/vllm-project/llm-compressor/pull/2223
* @saurabhaloneai made their first contribution in https://github.com/vllm-project/llm-compressor/pull/2321
* @colldata79 made their first contribution in https://github.com/vllm-project/llm-compressor/pull/2325
* @LudovicoYIN made their first contribution in https://github.com/vllm-project/llm-compressor/pull/2322
* @bartowski1182 made their first contribution in https://github.com/vllm-project/llm-compressor/pull/2316

**Full Changelog**: https://github.com/vllm-project/llm-compressor/compare/0.9.0.2...0.10.0

## 0.7.1.1 (2026-03-04)

## What's Changed
* Update pillow upper bound to 12.1.1 for 0.7.1.n release by @dhuangnm in https://github.com/vllm-project/llm-compressor/pull/2429


**Full Changelog**: https://github.com/vllm-project/llm-compressor/compare/0.7.1...0.7.1.1

## 0.10.0.1 (2026-03-13)

## What's Changed
* [Patch Release] Update compressed-tensors version in setup.py by @dsikka in https://github.com/vllm-project/llm-compressor/pull/2466


**Full Changelog**: https://github.com/vllm-project/llm-compressor/compare/0.10.0...0.10.0.1

## 0.10.0.2 (2026-05-01)

## What's Changed
* [For 0.10.0.2] Update pillow to fix security issue for release by @dhuangnm in https://github.com/vllm-project/llm-compressor/pull/2661


**Full Changelog**: https://github.com/vllm-project/llm-compressor/compare/0.10.0.1...0.10.0.2

## 0.9.0.3 (2026-05-05)

## What's Changed
* [For 0.9.0.3] Update pillow to fix security issue for release 0.9.0.3 by @dhuangnm in https://github.com/vllm-project/llm-compressor/pull/2660


**Full Changelog**: https://github.com/vllm-project/llm-compressor/compare/0.9.0.2...0.9.0.3

## 0.7.1.2 (2026-05-06)

## What's Changed
* [For 0.7.1.2] Update pillow version to fix security issue by @dhuangnm in https://github.com/vllm-project/llm-compressor/pull/2683


**Full Changelog**: https://github.com/vllm-project/llm-compressor/compare/0.7.1.1...0.7.1.2

## 0.11.0 (2026-06-02)

<img width="1536" height="1024" alt="ChatGPT Image Jun 2, 2026, 12_11_13 PM" src="https://github.com/user-attachments/assets/db6a6bf6-0ae3-4170-bf4b-e55ea8a3bd21" />

# LLM Compressor v0.11.0  

This release focuses on distributed computing enhancements, quantization lifecycle improvements, and expanded model support. Major highlights include DDP support for AWQ and SmoothQuant with significant speedups (up to 3.2x), a comprehensive refactor of the Compressed Tensors API, and observer/lifecycle refactors that simplify quantization workflows. New model support includes Qwen 3.5/3.6, Gemma 4, Kimi K2.6, and experimental DeepSeek-V4 support along with quantized checkpoints.

> Note: LLM Compressor v0.11.0 removes support for Sparse24 quantization formats and sparse model compression. This decision was made based upon lack of community interest and maintainability concerns. Support for sparse compression may be re-introduced as part of a future release. For Sparse24 compression support, please use LLM Compressor v0.10.0.2.

## Key Highlights  ✨

- **DDP Performance**: AWQ and SmoothQuant now support DDP with 2.9-3.2x speedups and up to 51% memory reduction per GPU (with 4 GPUs).
- **Compressed Tensors Refactor**: Simplified API with clear entrypoints, removed sparsity support, streamlined compressor architecture
- **Quantization Lifecycle**: Unified calibration timing (now at epoch end), decoupled observation from qparam calculation
- **Extended Quantization Support**: GPTQ actorder now works across all weight strategies, AWQ refactored for NVFP4 compatibility
- **Converter Entrypoint**: New tool and framework for converting from AutoAWQ and ModelOpt NVFP4 to Compressed-Tensors, as well as decompressing Compressed-Tensors checkpoints
- **Large Model Support**: DDP+GPTQ+disk offloading fixes for models like Qwen3-VL-235B-A22B

## DDP and Lifecycle Updates

- **AWQ DDP Support**: Added DDP (Distributed Data Parallel) functionality for AWQ resulting in significant speedups and reduced GPU memory usage:

  | Model | Single-GPU Time | DDP Time (4 GPUs) | Speedup | Single-GPU Memory | DDP Memory | Memory Reduction |
  |-------|-----------------|-------------------|---------|-------------------|------------|------------------|
  | Llama-3-8B | 7.02 min | 2.40 min | 2.9x | 10.20 GB | 4.99 GB | 51% |
  | Llama-3-8B (masked) | 8.13 min | 2.67 min | 3.0x | 10.14 GB | 4.98 GB | 51% |
  | Qwen3-30B-A3B | 459.65 min | 143.90 min | 3.2x | 4.13 GB | 3.36 GB | 19% |
  
  Accuracy metrics remain comparable between DDP and single-GPU approaches.

- **SmoothQuant DDP Support**: Added DDP support for SmoothQuant resulting in significant speedups:

  | GPUs | Total Time | Peak GPU Mem | Speedup |
  |------|------------|--------------|---------|
  | 1 GPU | 94.1 min | 8.93 GB | 1.00x |
  | 2 GPU | 58.7 min | 7.06 GB | 1.60x |
  | 4 GPU | 28.7 min | 7.06 GB | 3.28x |

Special thanks to @dzhengAP for their excellent contributions to the SmoothQuantModifier!

- **Observer Refactor**: Decoupled observation from quantization parameter calculation, allowing natural separation of responsibilities where `observer.forward()` records statistics about observed tensors while `get_qparams()` performs qparam calculation. This simplifies design and expands the types of observers supported. Key changes:
  - Observers now have `update_statistics_from_observed()` for forward pass and `get_qparams()` for parameter calculation
  - Global scale logic now entirely contained in observers (observers have references to fused weight observers for global_scale calculation)
  - Removed module references from observers, simplified observer utilities
  - Fixed imatrix observer synchronization in DDP and imatrix+global_scale bug
  - Consolidated synchronization logic with new `activation_statistics` concept for activation observers and one weight observer

- **DDP Support for Activation Quantization**: Added DDP support for quantization schemes with activation quantization. Extended QuantizationModifier to support distributed activation calibration via PR #2391 (merged Mar 27, 2026).
  
  **Implementation**: At `SEQUENTIAL_EPOCH_END` and `CALIBRATION_EPOCH_END`, activation observer min/max values are all-reduced across ranks. Scale/zero-point are then recomputed from the global statistics so all ranks have identical quantization parameters.
  
  **Key Changes**:
  - Added `synchronize()`, `recompute_qparams()`, `recompute_global_scale()` to Observer base class
  - Added `sync_activation_observers()` to QuantizationMixin (shared by QuantizationModifier and GPTQModifier)
  - Batch all async `dist.all_reduce` operations and wait once, matching GPTQ DDP pattern

- **DDP+GPTQ+Disk Offloading for Large Models**: Added fixes and features to enable DDP+GPTQ+disk offloading to work for very large models (e.g., Qwen3-VL-235B-A22B). Key improvements include:
  - Reduced shared memory overload and mmap issues for big models with DDP + CPU/disk offloading
  - Fixed MoE calibration context to use same offloading as original module (previously reverted to CPU offloading causing issues)
  - Only store original modules when needed to avoid mmap issues
  - Added synchronization steps during model saving to prevent thread timeout issues
  - Added sync points for MoE calibration context to handle NCCL timeout when different threads take varying time on large models
  - Fixed NVFP4 DDP support on A100 (NCCL broadcast workaround for FP8)
  - Reduced memory requirements of `moe_calibration_context` by removing retained module references after replacement

- **Distributed Model Compression**: Accelerate the model compression step (bit packing) by assigning modules across ranks and compressing them in parallel, greatly reducing runtime for large models, scaling linearly with the number of GPUs available.

- **Quantization Lifecycle Refactor**: Altered quantization lifecycle so weight and activation calibration both now happen on epoch end (previously weight calibration happened at start for QuantizationModifier but end for other modifiers). Benefits include simpler code, faster runtime due to reduced on/offloading during quantization, and quantization now disabled across the board during calibration (previously modifier-dependent).

- **Microscale Calibration Refactor**: Refactored microscale formats which require fused `global_scale` calculation. Rather than treating global scale as a generic qparam in the observer with additional post-modifications, the observer is now entirely responsible for `global_scale`. Observers are now fused (made aware of other observers with which they share a global_scale) so they can calculate a joint global_scale. Note: this requires that all fused observers have generated statistics through their forward method. This massively simplifies global_scale handling while maintaining accuracy.

## New Model Support

- **Qwen 3.5 and Qwen 3.6**: Calibration support has been added as part of this release with instructions summarized in the documentation for [Qwen3.5](https://docs.vllm.ai/projects/llm-compressor/en/latest/key-models/qwen3.5/) and [Qwen3.6](https://docs.vllm.ai/projects/llm-compressor/en/latest/key-models/qwen3.6/). Several quantized checkpoints have also been released, including:
  - [RedHatAI/Qwen3.6-35B-A3B-NVFP4](https://huggingface.co/RedHatAI/Qwen3.6-35B-A3B-NVFP4)
  - [RedHatAI/Qwen3.6-35B-A3B-FP8-dynamic](https://huggingface.co/RedHatAI/Qwen3.6-35B-A3B-FP8-dynamic)

- **Gemma 4**: Calibration support has been added with details listed in the documentation for [Gemma 4](https://docs.vllm.ai/projects/llm-compressor/en/latest/key-models/gemma4/). Several quantized checkpoints have also been released, including:
  - [RedHatAI/gemma-4-31B-it-NVFP4](https://huggingface.co/RedHatAI/gemma-4-31B-it-NVFP4)
  - [RedHatAI/gemma-4-31B-it-FP8-block](https://huggingface.co/RedHatAI/gemma-4-31B-it-FP8-block)
  - [RedHatAI/gemma-4-31B-it-FP8-Dynamic](https://huggingface.co/RedHatAI/gemma-4-31B-it-FP8-Dynamic)
  - [RedHatAI/gemma-4-26B-A4B-it-NVFP4](https://huggingface.co/RedHatAI/gemma-4-26B-A4B-it-NVFP4)
  - [RedHatAI/gemma-4-26B-A4B-it-FP8-Dynamic](https://huggingface.co/RedHatAI/gemma-4-26B-A4B-it-FP8-Dynamic)

- **Kimi K2.6**: This model was originally released in W4A16 packed quantized format. Decompression support has been enabled through the converters entrypoint and calibration support has also been added with details listed in the documentation for [Kimi K2.6](https://docs.vllm.ai/projects/llm-compressor/en/latest/key-models/kimi-k26/). Quantized checkpoints have also been released:
  - [RedHatAI/Kimi-K2.6-NVFP4](https://huggingface.co/RedHatAI/Kimi-K2.6-NVFP4)
  - [RedHatAI/Kimi-K2.6-FP8-BLOCK](https://huggingface.co/RedHatAI/Kimi-K2.6-FP8-BLOCK)

- **DeepSeek-V4**: Support for quantization of DeepSeekV4 Flash and Pro models. These features are currently available via experimental branches, but are planned for integration as part of the next release of LLM Compressor. More details can be found [here](https://docs.vllm.ai/projects/llm-compressor/en/latest/key-models/deepseek-v4/). Sample checkpoint:
  - [RedHatAI/DeepSeek-V4-Flash-NVFP4-FP8](https://huggingface.co/RedHatAI/DeepSeek-V4-Flash-NVFP4-FP8)

## Converter Entrypoint (Compressed-Tensors)

- **Model Format Conversion**: Added [`Converter`](https://github.com/vllm-project/compressed-tensors/blob/main/src/compressed_tensors/entrypoints/convert/converters/base.py#L19) entrypoint to enable decompression and conversion of models from various packed quantized formats to Compressed-Tensors format. Currently supports:
  - AutoAWQ to CT conversion
  - Compressed-Tensors Decompression
  - ModelOpt NVFP4 to CT Conversion
  - FP8 Block Decompression (popularized by DeepSeek)

  
  More details: https://docs.vllm.ai/projects/llm-compressor/en/latest/guides/entrypoints/convert/

## Compressed Tensors

- **Compressed Tensors Refactor**: Major simplification of compression API and architecture to reduce complexity, define easy-to-use APIs for module and state dict compression/decompression, and prepare for distributed parallel compression.



  **Architectural Changes**:
  - Simplified compressors: Removed separate "quantization" and "sparsity" compressors and hierarchy. Each format now has exactly one compressor. Compressors define which quantization schemes they support, modules compressed using whichever compressor supports them in priority order
  - Module compression API: Each `Compressor` class implements `Compressor.can_compress()`, `Compressor.compress()`, and `Compressor.decompress()` methods. You can use top-level `compress_module()` and `decompress_module()` to automatically infer which compressor to use to compress a module. 
  - Removed `CompressedLinear` wrapper class: ModelCompressor now adds `pre_forward` hook that triggers decompression on first forward pass.
  - Added `QuantizationStatus.DECOMPRESSED` state: weight already been qdqed permanently (distinct from `FROZEN` which still performs weight qdq during forward pass for emulation)

  **Breaking Changes**:
  - Removed all sparsity compressors and deprecated sparsity-related config arguments
  - Removed `CompressedLinear` class
  - `marlin24` sparsity no longer supported


## AWQ Refactor

- **Transform-Based Modifier**: Refactored AWQ to be a transform-based modifier (a modifier that modifies weights in place without applying quantization) as part of an ongoing effort to make AWQ compatible with more quantization formats, including NVFP4. This keeps AWQ separate from static activation calibration and makes for a cleaner implementation.

## GPTQ ActOrder Support

- **Extended Activation Ordering**: Extended GPTQ activation ordering (actorder) support beyond the original GROUP-only strategy to work across all weight quantization strategies: GROUP, TENSOR_GROUP, CHANNEL, TENSOR, and BLOCK.

  | Strategy | Modifier-level actorder (before) | After |
  |----------|----------------------------------|-------|
  | GROUP | propagated | propagated |
  | TENSOR_GROUP | silently ignored | propagated |
  | CHANNEL | silently ignored | propagated; GROUP → fallback |
  | TENSOR | silently ignored | propagated; GROUP → fallback |
  | BLOCK | silently ignored | propagated; GROUP → fallback |

## MXFP4 Linear Quantization

- **FlashInfer Backend Support**: Enabled MXFP4 Linear Quantization support in vLLM using the FlashInfer backend, allowing end-to-end support for MXFP4 checkpoints beyond Marlin. Benchmark results on Meta-Llama-3-8B-Instruct (gsm8k_cot_llama):

  | Backend | Flexible-Extract | Strict-Match |
  |---------|------------------|--------------|
  | FlashInfer | 0.6892 ± 0.0127 | 0.6846 ± 0.0128 |
  | Marlin (VLLM_MXFP4_USE_MARLIN=1) | 0.7604 ± 0.0118 | 0.7551 ± 0.0118 |
  | Dense (meta-llama/Meta-Llama-3-8B-Instruct) | 0.7998 ± 0.0110 | 0.7991 ± 0.0110 |

## Model Saving

- **MTP Layer Saving**: Fixed issue where models with MTP (multi-token prediction) layers were not including MTP layers in final checkpoints due to MTP layers not being loaded through the AutoModel pathway. Updated model saving to detect presence of MTP layers and update the safetensors in the final checkpoint accordingly.

## New Contributors
* @dik654 made their first contribution in https://github.com/vllm-project/llm-compressor/pull/2368
* @Yatimai made their first contribution in https://github.com/vllm-project/llm-compressor/pull/2418
* @omkar-334 made their first contribution in https://github.com/vllm-project/llm-compressor/pull/2414
* @JinRiYao2001 made their first contribution in https://github.com/vllm-project/llm-compressor/pull/2443
* @rtj1 made their first contribution in https://github.com/vllm-project/llm-compressor/pull/2330
* @2imi9 made their first contribution in https://github.com/vllm-project/llm-compressor/pull/2467
* @dzhengAP made their first contribution in https://github.com/vllm-project/llm-compressor/pull/2471
* @markypizz made their first contribution in https://github.com/vllm-project/llm-compressor/pull/2503
* @changjonathanc made their first contribution in https://github.com/vllm-project/llm-compressor/pull/2477
* @zeel2104 made their first contribution in https://github.com/vllm-project/llm-compressor/pull/2533
* @wiliyam made their first contribution in https://github.com/vllm-project/llm-compressor/pull/2556
* @vkduy made their first contribution in https://github.com/vllm-project/llm-compressor/pull/2567
* @xingzihai made their first contribution in https://github.com/vllm-project/llm-compressor/pull/2555
* @liwei109 made their first contribution in https://github.com/vllm-project/llm-compressor/pull/2464
* @aayush7511 made their first contribution in https://github.com/vllm-project/llm-compressor/pull/2493
* @sakunkun made their first contribution in https://github.com/vllm-project/llm-compressor/pull/2597
* @Nottlespike made their first contribution in https://github.com/vllm-project/llm-compressor/pull/2547
* @Alone-wl made their first contribution in https://github.com/vllm-project/llm-compressor/pull/2634
* @elwhyjay made their first contribution in https://github.com/vllm-project/llm-compressor/pull/2609
* @jayakumarpujar made their first contribution in https://github.com/vllm-project/llm-compressor/pull/2639
* @prdeepakbabu made their first contribution in https://github.com/vllm-project/llm-compressor/pull/2644
* @rk119 made their first contribution in https://github.com/vllm-project/llm-compressor/pull/2616
* @changwangss made their first contribution in https://github.com/vllm-project/llm-compressor/pull/2688
* @juju812 made their first contribution in https://github.com/vllm-project/llm-compressor/pull/2635
* @dshane1903 made their first contribution in https://github.com/vllm-project/llm-compressor/pull/2704
* @AsadShahid04 made their first contribution in https://github.com/vllm-project/llm-compressor/pull/2719
* @orestis-z made their first contribution in https://github.com/vllm-project/llm-compressor/pull/2725

**Full Changelog**: https://github.com/vllm-project/llm-compressor/compare/0.10.0...0.11.0

## 0.12.0 (2026-06-15)

<img width="1536" height="1024" alt="c6eabd02-d5f3-47ce-ac77-a7fb0ad7cac9" src="https://github.com/user-attachments/assets/bc5ba00d-a719-4cea-9845-42b236fbe115" />


# LLM Compressor v0.12.0 Release Notes

This release upgrades to Transformers v5 with improved MoE support, streamlines the dataset interface, and adds multi-GPU acceleration for model-free PTQ. Major highlights include comprehensive Transformers v5 integration with refactored MoE linearization, a simplified dataset split API that removes legacy multi-stage logic, multi-GPU distribution for model-free PTQ workflows, and expanded model coverage with Nemotron Ultra FP8 examples.

This release contains changes to example scripts with backwards compatibility with previous examples and scripts. Please read [Transformers v5](#transformers-v5) for more information.

## Key Highlights ✨
- Transformers v5 Upgrade (#2647): Full integration with Transformers v5, including refactored MoE linearization with `load_context` for efficient loading, updated model structure handling, and improved tied embeddings support. Maintains LM eval performance across the transition. Note: **LLM Compressor no longer supports installation with `transformers<5.0.0`**.
- Simplified Dataset Interface (#2551): Removed legacy multi-split logic, replacing `splits={"calibration": "train[:100]"}` with cleaner `split="train[:100]"` API. Legacy argument usage is deprecated and will be removed in a future release.
- Multi-GPU Model-Free PTQ (#2773): Added support to distribute model-free PTQ jobs across multiple GPUs for significant parallelization and speedup for quantization workflows.
- Nemotron Ultra Support (#2803): Added FP8 quantization example for Nemotron Ultra models in the model-free PTQ examples.


# Transformers v5 #

## Examples and Model Loading ##

* Example regexes and recipes have been updated to reflect new model structures introduced by Transformers v5


* Examples which utilize disk offloading or mixture-of-experts (MoE) calibration now load models with `load_context` provided by `llmcompressor.utils`. This context is a catch-all context and should be used in all scripts for efficient model loading.

```python
- from compressed_tensors.offload import load_offloaded_model
- from llmcompressor.modeling.moe.linearize import load_quantizable_moe
- 
- with load_offloaded_model(), load_quantizable_moe():
-     model = AutoModelForCausalLM.from_pretrained(model_id)

+ from llmcompressor.utils import load_context
+ 
+ with load_context():
+     model = AutoModelForCausalLM.from_pretrained(model_id)
```

* `dtype` now defaults to `"auto"`, so this explicit argument has been removed to reduce verbosity

```diff
- model = AutoModelForCausalLM.from_pretrained(model_id, dtype=”auto”)
+ model = AutoModelForCausalLM.from_pretrained(model_id)
```

* `from_pretrained` no longer supports `use_auth_token`. This argument has been removed from `oneshot`

## Expanded and Refactored MoE Support ##
Applying quantization to Mixture-of-Experts (MoE) models requires explicit linearization and class overriding in order to efficiently calibrate experts. This logic has been implemented by LLM Compressor through two pathways:
`llmcompressor.modeling.moe.linearize::linearize_moe` which replaces experts modules with linearized and calibration-friendly classes AFTER weights have already been loaded
`llmcompressor.modeling.moe.linearize::load_quantizable_moe` which replaces experts modules with linearized and calibration-friendly classes BEFORE weights have been loaded. This context is more efficient and reduces runtime during model loading.

Both of these pathways are called as needed by `llmcompressor.utils::load_context`. These implementations are capable of automatically handling >90% of all model definitions provided by `transformers`. For unconventional or custom model definitions, see [Adding MoE Calibration Support for a New Model]( https://docs.vllm.ai/projects/llm-compressor/en/latest/developer-tutorials/add-moe-support)

## Multi-GPU Model-Free PTQ

Model-free PTQ now supports distributing quantization jobs across multiple GPUs when available. This feature automatically detects available GPUs and parallelizes the quantization workflow, significantly reducing processing time for large models.

## Simplified Dataset Interface
  
The dataset split interface has been refactored to remove legacy multi-stage logic that previously supported separate datasets for training, oneshot, and eval in a single command. Since training and eval tasks are no longer supported in the same command, the API has been simplified.
 
Old interface:
```python
oneshot(
  model,
  dataset="ultrachat",
  splits={"calibration": "train_sft[:100]"}
)
```
New interface:
```python
oneshot(
  model,
  dataset="ultrachat",
  split="train_sft[:100]"
) 
```
  
The new API is backwards compatible and will issue warnings when using the old dictionary-based splits argument.

## Nemotron 3 Ultra Examples

This release adds model-free PTQ examples for NVIDIA's Nemotron-3-Ultra-550B model.
Pre-quantized FP8 checkpoints are available on HuggingFace:

- [NVIDIA-Nemotron-3-Ultra-550B-A55B-FP8-dynamic](https://huggingface.co/RedHatAI/NVIDIA-Nemotron-3-Ultra-550B-A55B-FP8-dynamic)
- [NVIDIA-Nemotron-3-Ultra-550B-A55B-FP8-block](https://huggingface.co/RedHatAI/NVIDIA-Nemotron-3-Ultra-550B-A55B-FP8-block)
- See the model-free [PTQ examples](https://github.com/vllm-project/llm-compressor/tree/main/examples/model_free_ptq) for usage details.

## Breaking Changes
- The minimum transformers version has been bumped up to v5.9

## New Contributors
* @JINO-ROHIT made their first contribution in https://github.com/vllm-project/llm-compressor/pull/2773
* @u7k4rs6 made their first contribution in https://github.com/vllm-project/llm-compressor/pull/2779
* @soyr-redhat made their first contribution in https://github.com/vllm-project/llm-compressor/pull/2794
* @arpitkh101 made their first contribution in https://github.com/vllm-project/llm-compressor/pull/2589
* @Priya95715 made their first contribution in https://github.com/vllm-project/llm-compressor/pull/2768

**Full Changelog**: https://github.com/vllm-project/llm-compressor/compare/0.11.0...0.12.0

## 0.7.1.3 (2026-06-26)

## What's Changed
* Allow requests 2.32.5+ versions by @dhuangnm in https://github.com/vllm-project/llm-compressor/pull/2859


**Full Changelog**: https://github.com/vllm-project/llm-compressor/compare/0.7.1.2...0.7.1.3

## 0.7.1.4 (2026-07-27)

## What's Changed
* [release-0.7.1] bump up pillow upper bound by @dhuangnm in https://github.com/vllm-project/llm-compressor/pull/2954


**Full Changelog**: https://github.com/vllm-project/llm-compressor/compare/0.7.1.3...0.7.1.4

## 0.9.0.4 (2026-07-27)

## What's Changed
* [release-0.9.0] bump up pillow and requests upper bounds by @dhuangnm in https://github.com/vllm-project/llm-compressor/pull/2955


**Full Changelog**: https://github.com/vllm-project/llm-compressor/compare/0.9.0.3...0.9.0.4

## 0.10.0.3 (2026-07-28)

## What's Changed
* [Deprecation] Remove Sparse24 e2e tests from release-0.10.0 by @deepak-kumar-neu in https://github.com/vllm-project/llm-compressor/pull/2720
* [release-0.10.0] bump up pillow and requests upper bound by @dhuangnm in https://github.com/vllm-project/llm-compressor/pull/2959


**Full Changelog**: https://github.com/vllm-project/llm-compressor/compare/0.10.0.2...0.10.0.3

## 0.12.0.1 (2026-07-31)

## What's Changed
* [release-0.12.0] update pillow upper bound by @dhuangnm in https://github.com/vllm-project/llm-compressor/pull/2961


**Full Changelog**: https://github.com/vllm-project/llm-compressor/compare/0.12.0...0.12.0.1

## 0.13.0 (2026-08-11)

<img width="1536" height="1024" alt="ab6cbf09-a397-40d4-82da-b790a4b0fb39" src="https://github.com/user-attachments/assets/83fa02ea-f410-4cff-9e5d-f0cf77599152" />

# Key Highlights

- **REAP Expert Pruning** — [#2864](https://github.com/vllm-project/llm-compressor/pull/2864): New modifier for structurally pruning Mixture-of-Experts (MoE) models by removing individual experts based on calibration-based saliency scores. Based on the [REAP the Experts paper](https://arxiv.org/pdf/2510.13999).
- **Arbitrary Bit-Width Quantization (Humming)** — [ct#732](https://github.com/vllm-project/compressed-tensors/pull/732), [ct#785](https://github.com/vllm-project/compressed-tensors/pull/785): Dense packing for non-power-of-2 bit widths (3, 5, 6, 7) with no wasted bits, plus 16 new WxAy presets covering W2–W8 weights with A4, A8, or A16 activations.
- **Observer Fusion and Deletion** — [#2865](https://github.com/vllm-project/llm-compressor/pull/2865): Refactored observer lifecycle and significantly reduced memory usage for large models due to observer statistics persisting after calibration.
- **Expanded MoE Architecture Support** — [#2847](https://github.com/vllm-project/llm-compressor/pull/2847): Extended MoE linearization to support a broader range of architectures, including Transformers v5.13.0 models.
- **Improved XPU Compatibility** — [#2776](https://github.com/vllm-project/llm-compressor/pull/2776), [#2884](https://github.com/vllm-project/llm-compressor/pull/2884): Migrated `torch.cuda` calls to `torch.accelerator` for Intel XPU support.
- **AutoRound Sub-Bit Quantization** — [#2895](https://github.com/vllm-project/llm-compressor/pull/2895): Added sub-bit quantization, including W2A16 attention / W4A16 MLP mixed precision.
- **Pre-Quantized Model Support** — [#2909](https://github.com/vllm-project/llm-compressor/pull/2909): `oneshot` now provides experimental support for pre-quantized models, provided the targeted layers have not been previously quantized.

## REAP Expert Pruning

**REAP (Router-weighted Expert Activation Pruning)** structurally compresses MoE models by permanently removing individual experts based on saliency scores computed during calibration. The algorithm is introduced in the [REAP the Experts: Why Pruning Prevails for One-Shot MoE Compression](https://arxiv.org/pdf/2510.13999) paper.

REAP can be combined with quantization modifiers. For example, users can prune low-saliency experts first and then quantize the remaining model to **FP8** or **NVFP4**.

## Arbitrary Bit-Width Quantization (Humming)

### Dense Packing for Non-Standard Bit Widths

The `pack_quantized` compressor in `compressed-tensors` now uses dense cross-element packing ([ct#732](https://github.com/vllm-project/compressed-tensors/pull/732)). Previously, 3-, 5-, 6-, and 7-bit formats used padded packing that wasted bits.

The new implementation:

- Packs 32 consecutive `intB` elements into exactly `num_bits` `int32` words.
- Uses no wasted bits and splits elements across `int32` boundaries when needed.
- Supports activation quantization in addition to weight-only schemes.

### Expanded WxAy Quantization Presets

A new `_int_wnam()` helper generates valid integer WxAy combinations ([ct#785](https://github.com/vllm-project/compressed-tensors/pull/785)), adding **16 presets** covering W2–W8 weights with A4, A8, or A16 activations, including W3A8, W5A16, and W6A8.

All presets use **group-128 symmetric weights** and **token-wise dynamic symmetric activations** and are supported in vLLM as of [vllm#46390](https://github.com/vllm-project/vllm/pull/46390).

W2–W7 weight-only (A16) schemes were also added as standalone presets ([ct#760](https://github.com/vllm-project/compressed-tensors/pull/760)), extending the previous W4A16 and W8A16 presets.

## Observer Fusion and Deletion

Observer lifecycle management was refactored to fix a memory leak where statistics persisted after calibration ([#2865](https://github.com/vllm-project/llm-compressor/pull/2865)):

- A dedicated `fusion_handler` manages fused observer groups.
- Statistics are deleted only after the full fusion group completes.
- Weight observers skip redundant observation when statistics already exist, reducing recomputation for AWQ/GPTQ workflows.

## Expanded MoE Support

MoE linearization now supports a broader range of architectures, including models introduced in Transformers v5.13.0 ([#2847](https://github.com/vllm-project/llm-compressor/pull/2847)). Import patterns were also refactored for backwards compatibility.

**Cohere2MoE SpinQuant** support was added ([#2867](https://github.com/vllm-project/llm-compressor/pull/2867)), including special handling for its parallel transformer block where one `input_layernorm` feeds attention, MLP, and the router.

## Lifecycle Improvements

### Calibration Events

Calibration events are now first-class lifecycle hooks ([#2783](https://github.com/vllm-project/llm-compressor/pull/2783), [#2784](https://github.com/vllm-project/llm-compressor/pull/2784)):

- Added `on_calibration_start`, `on_sequential_epoch_end`, and `on_calibration_end`.
- Calibration start/end logic is handled by the `Modifier` base class.
- Renamed `calibration_epoch_start/end` to `calibration_start/end`.

### Calibration Requirement Check

Each modifier now declares `requires_calibration_data()` ([#2947](https://github.com/vllm-project/llm-compressor/pull/2947)), replacing the hardcoded pipeline registry list. GPTQ, AutoRound, SparseGPT, Wanda, SmoothQuant, AWQ, and REAP explicitly require calibration.

### Pipeline Device Movement

Device movement logic has been removed from pipelines ([#2846](https://github.com/vllm-project/llm-compressor/pull/2846)). `load_offloaded_model` now handles distributed dispatch and disk offloading, simplifying pipeline logic.

## Distributed Improvements

- **Module Parallel Calibration** — [#2785](https://github.com/vllm-project/llm-compressor/pull/2785): Weight calibration can run in parallel across distributed workers.
- **Suspend Distributed Timeout** — [#2868](https://github.com/vllm-project/llm-compressor/pull/2868): Supports saving very large or disk-offloaded models taking more than 10 minutes.
- **AutoRound DDP** — [#2844](https://github.com/vllm-project/llm-compressor/pull/2844), [#2934](https://github.com/vllm-project/llm-compressor/pull/2934): Added Qwen MoE DDP example and fixed rank-local device placement.
- **DDP Smoke Tests** — [#2769](https://github.com/vllm-project/llm-compressor/pull/2769): Added comprehensive DDP tests with subsequent stability fixes in [#2840](https://github.com/vllm-project/llm-compressor/pull/2840), [#2857](https://github.com/vllm-project/llm-compressor/pull/2857), [#2863](https://github.com/vllm-project/llm-compressor/pull/2863), and [#2943](https://github.com/vllm-project/llm-compressor/pull/2943).

## Performance

- **`torch.compile` for MSE Observer** — [#2384](https://github.com/vllm-project/llm-compressor/pull/2384): Added chunked execution support for `torch.compile`, with significant speedups for activation quantization. Pass `enable_compile=True` to `oneshot` to enable.
- **`IntermediatesCache` `pin_memory` Fix** — [#2813](https://github.com/vllm-project/llm-compressor/pull/2813): Fixed a CUDA OOM issue with nested dispatchers.
- **Reduced Default Save Shard Size** — [#2927](https://github.com/vllm-project/llm-compressor/pull/2927): Reduced the default shard size to **20 GB** for improved network transfer performance.

## XPU Compatibility

All main-path `torch.cuda` calls have been migrated to `torch.accelerator` ([#2884](https://github.com/vllm-project/llm-compressor/pull/2884)). A `torch.cuda` linter was added to CI ([#2776](https://github.com/vllm-project/llm-compressor/pull/2776)), along with XPU Docker and testing infrastructure ([#2945](https://github.com/vllm-project/llm-compressor/pull/2945)).

## New Model Support

- **DeepSeek V4 Pro** — [#2858](https://github.com/vllm-project/llm-compressor/pull/2858), with automatic MTP weight copying ([#2951](https://github.com/vllm-project/llm-compressor/pull/2951)).
- **GLM 5.2** — [#2869](https://github.com/vllm-project/llm-compressor/pull/2869)
- **GLM 4.6** — [#2343](https://github.com/vllm-project/llm-compressor/pull/2343)
- **HunyuanMoE V3** — [#2928](https://github.com/vllm-project/llm-compressor/pull/2928)
- **Gemma 4** — [#2816](https://github.com/vllm-project/llm-compressor/pull/2816)
- **Mellum2** — [#2832](https://github.com/vllm-project/llm-compressor/pull/2832)
- **Cohere2MoE SpinQuant + NVFP4** — [#2867](https://github.com/vllm-project/llm-compressor/pull/2867)
- **Input Embedding Quantization example** — [#2830](https://github.com/vllm-project/llm-compressor/pull/2830)
- **New AWQ/SmoothQuant mappings** for Step3p5 ([#2770](https://github.com/vllm-project/llm-compressor/pull/2770)), Granite ([#2797](https://github.com/vllm-project/llm-compressor/pull/2797)), Nanbeige ([#2966](https://github.com/vllm-project/llm-compressor/pull/2966)), and Qwen3.5 MoE ([#2718](https://github.com/vllm-project/llm-compressor/pull/2718), [#2727](https://github.com/vllm-project/llm-compressor/pull/2727)).

## Breaking Changes

- Removed sparsity-preserving logic from GPTQ — [#2860](https://github.com/vllm-project/llm-compressor/pull/2860)
- Removed `IMatrixGatherer`; functionality consolidated into observers — [#2920](https://github.com/vllm-project/llm-compressor/pull/2920)
- Deprecated `GPTQ actorder=group` — [#2893](https://github.com/vllm-project/llm-compressor/pull/2893)
- Deprecated `reindex_fused_weights` — [#2737](https://github.com/vllm-project/llm-compressor/pull/2737)
- QuIP now defaults to input (`v`) rotations only — [#2815](https://github.com/vllm-project/llm-compressor/pull/2815)

## New Contributors
* @KKothuri made their first contribution in https://github.com/vllm-project/llm-compressor/pull/2830
* @EdalatiAli made their first contribution in https://github.com/vllm-project/llm-compressor/pull/2798
* @zhangxin81 made their first contribution in https://github.com/vllm-project/llm-compressor/pull/2718
* @Bias92 made their first contribution in https://github.com/vllm-project/llm-compressor/pull/2384
* @LeonEricsson made their first contribution in https://github.com/vllm-project/llm-compressor/pull/2833
* @wanadzhar913 made their first contribution in https://github.com/vllm-project/llm-compressor/pull/2770
* @jethac made their first contribution in https://github.com/vllm-project/llm-compressor/pull/2845
* @krishnateja95 made their first contribution in https://github.com/vllm-project/llm-compressor/pull/2832
* @Ryfernandes made their first contribution in https://github.com/vllm-project/llm-compressor/pull/2864
* @suluner made their first contribution in https://github.com/vllm-project/llm-compressor/pull/2884
* @Pruthvi226 made their first contribution in https://github.com/vllm-project/llm-compressor/pull/2870
* @HumphreySun98 made their first contribution in https://github.com/vllm-project/llm-compressor/pull/2797
* @chiptoe-svg made their first contribution in https://github.com/vllm-project/llm-compressor/pull/2917
* @w3lld1 made their first contribution in https://github.com/vllm-project/llm-compressor/pull/2909
* @f-baig made their first contribution in https://github.com/vllm-project/llm-compressor/pull/2966
* @arijitroy003 made their first contribution in https://github.com/vllm-project/llm-compressor/pull/2958
* @Roderick-Wu made their first contribution in https://github.com/vllm-project/llm-compressor/pull/2920
* @chensuyue made their first contribution in https://github.com/vllm-project/llm-compressor/pull/2945
* @latent-9 made their first contribution in https://github.com/vllm-project/llm-compressor/pull/2989
* @qubeena07 made their first contribution in https://github.com/vllm-project/llm-compressor/pull/2987

**Full Changelog**: https://github.com/vllm-project/llm-compressor/compare/0.12.0...0.13.0

## 0.14.0 (2026-09-22)

<img width="1536" height="1024" alt="llmc_v14" src="https://github.com/user-attachments/assets/cddb93c4-8746-4aff-9e57-83fc9fbd45b2" />

# LLM-Compressor v0.14.0

## Key Highlights ✨

- **GPTQ Performance Improvements #3128**
  - GPTQ now ships a Triton-based quantization kernel, approximately **15× faster end-to-end** than the previous implementation.
  - Layers that share the same shape can now be batched, achieving approximately **30× faster end-to-end performance** on some MoE workloads.
  - Hessian offloading has been removed.
  - The remaining eager path was independently sped up by **1.5–2×**.

- **Expanded MSE/iMatrix Observers #2950, #3076**
  - Added functionality to expand the grid search for iMatrix and MSE observers.
  - Enables identification of better local scales for NVFP4.
  - The expanded search space is a superset of the Fourosix-style quantization strategy.

- **MSE Observer Performance Improvements #2991**
  - Added a new Triton kernel for grid search, improving observation time by approximately **10×**.
  - Reaches bitwise parity with the eager path under full evaluation.

- **REAP DDP + e-Score Correction #3045, #3101**
  - REAP expert pruning now supports distributed DDP runs.
  - Added optional e-score correction bias.
  - Added a new HY3 example.

- **Model-Free PTQ Improvements #2976, #3053, #2935, #3158**
  - Replaced static round-robin GPU assignment with a dynamic, memory-aware scheduler.
  - Added mixed-precision and KV-cache quantization support.
  - Unified the entry point into a single `ModelFreePtqConverter` class.
  - Added profiler-based memory estimates.

- **Expanded MoE Machinery #3080, #3017, #3173, #3100**
  - Added `patch_moe_mappings()` for overriding 2D load mappings per checkpoint.
  - Added `repack_moe()` for restoring native fused 3D expert modules after linearization.
  - Added fast loading for `nemotron_h` (Nemotron 3 Ultra).
  - Added GPT-OSS expert linearization.

## GPTQ

The GPTQ modifier received its largest performance upgrade since launch in **#3128**:

- **New Triton GPTQ kernel:** Approximately **15× faster** than the previous eager implementation.
- **Layer batching:** Layers sharing the same shape can be quantized together, achieving approximately **1.67× higher throughput per batch** and up to **30× end-to-end speedups** on MoE workloads with many shared shapes.
- **Simplified Hessian handling:** Removed Hessian offloading.
- **Faster eager path:** Independently improved by approximately **1.5–2×**.
- **Hessian loop optimization:** Hoisted loop invariants out of the per-column quantization loop (#3097).
- **RTN fallback reporting:** Added an end-of-run summary for modules that fall back to RTN (#3098).
- **A100 FP8 support:** Fixed GPTQ FP8 handling with a supported Triton FP8 cast (#3181).

## Observers

### NVFP4 and MSE/iMatrix

- **Expanded grid search:** MSE and iMatrix observers now support an expansion factor, making their search space a superset of the Fourosix strategy (#2950).
- **NVFP4 quality:** The new expanded MSE observer outperforms GPTQ for NVFP4 on average across internal perplexity benchmarks.
- **Triton MSE grid search:** Added a Triton kernel for scale grid search with buffered per-qparam patience and adaptive 512-value tiling (#2991).
- **Bitwise parity:** The Triton MSE implementation reaches bitwise parity with the eager path under full evaluation.
- **Format coverage:** Supports INT, FP4, FP8, and FP16/BF16 with E8M0 scales.
- **Triton error buffer:** Added `triton_error_buffer` to enable approximate congruence between eager and Triton patience behavior.
- **Observer resolution:** Quantization-argument resolution and observer defaulting moved from `compressed-tensors` into LLM-Compressor (#3091).
- **Validation:** `MovingAverageMSEObserver` now validates `expand >= 1.0` (#3095).

## Model-Free PTQ

- **Dynamic GPU scheduling:** Replaced static round-robin assignment with a capacity-first, memory-aware scheduler that queries available GPU memory before each job and tracks reservations (#2976).
- **Reliable fallback:** Insufficient capacity now triggers an explicit fallback instead of silently dropping work.
- **Mixed precision:** Added mixed-precision quantization support (#3053).
- **KV-cache quantization:** Added KV-cache quantization support.
- **Unified API:** Consolidated model-free PTQ into `ModelFreePtqConverter` (#2935).
- **Memory estimation:** Added profiler-based memory estimates (#3158).

## REAP

- **Distributed support:** REAP expert pruning now supports DDP.
  - Saliency statistics are reduced across ranks.
  - Statistics are computed on rank 0.
  - Results are broadcast back to workers (#3045).
- **e-Score correction:** Added an optional e-score correction bias (#3101).
- **New example:** Added an HY3 REAP example.

## MoE

Expanded MoE support includes:

- `patch_moe_mappings()` — Override 2D load mappings on a per-checkpoint basis through a load context (#3080).
- `repack_moe()` — Restore native fused 3D expert modules so `save_pretrained()` writes Hugging Face-native keys (#3017).
- **Nemotron 3 Ultra:** Added fast-loading support and 2D conversion mappings for `nemotron_h` (#3173).
- **GPT-OSS:** Added expert linearization support (#3100).
- **Performance:** Experts are no longer onloaded when checking `FusedExpertsProtocol` (#3039).
- **Cleanup:** Removed `GraniteMoeLinearExperts` (#2885).

## New Model Support

- **GLM 5.3 / GLM 5.3 Flash** (#3164)
- **Kimi-K3**
  - Added native `KimiK3ForConditionalGeneration`.
  - Added quantization examples.
  - Added upfront model decompression.
  - #2994, #3184
- **Qwen3.8**
  - Added examples.
  - Updated AWQ/SmoothQuant mappings.
  - #3043, #3041
- **Muse Glimmer** — Added AWQ mappings (#3124)
- **Cohere2MoE** — Added AWQ and SmoothQuant support (#2938)
- **DeepSeekV2** — Added AWQ support (#2938)
- **Nanbeige** — Added AWQ/SmoothQuant mappings (#3073)
- **Glm4MoeLite** — Added AWQ/SmoothQuant mappings (#3072)
- **OlmoForCausalLM v1/v2**
  - Added AWQ/SmoothQuant mappings using the Exaone4-style mapping.
  - #2802

## New Examples

- **MR-GPTQ:** QuIP + GPTQ + NVFP4A16 (#2751)
- **FP8 Attention + AutoRound:** Qwen3 dense and MoE (#3092)
- **Mixed W2A16 / W4A16 MoE** (#2940)
- **GLM-5.2 MXFP4 × MXFP8** (#3048)
- **DeepSeek V4 MXFP4–MXFP8** (#2897)
- **GLM-5.3 MXFP4** (#3163)
- **Llama 3.3 70B MXFP8 + FP8 Attention** (#3160)
- **Qwen3 MoE** (#2946)
- **Agent skills**
  - Added a shared quantization skill for AWQ, SmoothQuant, GPTQ, and `QuantizationModifier`.
  - Added FP8/NVFP4 skill updates.
  - Added prebaked-dataset selection.
  - #2971

## Performance

- **GPTQ:** New Triton kernel and layer batching (#3128).
- **Subgraph tracing:** O(1) node-membership lookups (#2992, #2999).
- **AutoRound VRAM:** Calibration inputs can be offloaded to CPU for large `N` (#3055).
- **AutoRound memory:** Prevented `input_capture_hook` from accumulating GPU memory during optimization (#3024).

## Bug Fixes

- Upfront model decompression for Kimi-K3 (#3184)
- Distributed hang caused by incorrectly shaped `weight_global_scale` writeback (#3185)
- GPTQ FP8 handling on A100 (#3181)
- Prevent recursion into container modules in `observe/update_qparams` (#2990)
- Dtype serialization (#3152)
- `polynomial_decay` pruning scheduler for even exponents (#3096)
- Global scale shape (#3191)
- Qwen2.5-VL AWQ mapping for vision towers (#3169)
- Python 3.14 compatibility issues in `Recipe.dict()` and dataset split help text (#2778, #2871, #3140)
- `collect_env` crash on Apple Silicon/MPS (#3068)
- Decorated forwards without `functools.wraps` in `autowrap_forward` (#3058)
- `llmcompressor.trace` boolean flags now toggle correctly (#3070)
- Runtime issues in recipe validation, AutoRound, and AWQ (#2973)
- Weightless modules in distributed greedy bin packing (#3113)

## Refactoring & Breaking Changes

- Removed deprecated GPTQ Group/Dynamic Activation Ordering (#3038).
- Removed `GraniteMoeLinearExperts` (#2885).
- Moved observer resolution/defaulting into LLM-Compressor (#3091).
- Unified model-free PTQ under `ModelFreePtqConverter` (#2935).
- `TensorProfiler` is now imported from `compressed-tensors` (#3203).
- `exec_jobs_dynamic` was ported to `compressed-tensors` (#3075).

## Datasets & Miscellaneous

- Added the `perfectblend` prebaked dataset and `ultrachat` alias (#3060).
- Replaced example datasets with prebaked `perfectblend`/`flickr30k` datasets (#3062).
- Changed the default for `pad_to_max_length` (#3180).
- Added `resave_config` to preserve the original model configuration on save (#3147).
- Sequential onloading now supports frozen dataclasses (#2016).
- Modernized type hints across logger, datasets, and observers (#2960).

## Dependencies & Infrastructure

- **`compressed-tensors`:** Bumped to **0.19.0** (#3213).
- **`accelerate`:** Minimum version raised to **>=1.15.0** for full-disk offloading (#3176).
- **Transformers:** Updated the supported version range (#3122).
- **Pre-commit:** Added hooks mirroring `make quality` (#3120).


## Full Changelog
* Revise README for new Muse-Glimmer-30B checkpoints by @dsikka in https://github.com/vllm-project/llm-compressor/pull/3019
* Update review rules by @dsikka in https://github.com/vllm-project/llm-compressor/pull/3026
* load_quantizable_moe with new transformers version by @Roderick-Wu in https://github.com/vllm-project/llm-compressor/pull/3016
* [transformers] Update tests to use new compressed-tensors api, pin transformers by @kylesayrs in https://github.com/vllm-project/llm-compressor/pull/3021
* [MTP] Update to work with Qwen 3.8 by @dsikka in https://github.com/vllm-project/llm-compressor/pull/3033
* [Performance] [MoE] Don't onload weights when checking FusedExpertsProtocol by @kylesayrs in https://github.com/vllm-project/llm-compressor/pull/3039
* Update docs for LLM Compressor v0.13.0 by @dsikka in https://github.com/vllm-project/llm-compressor/pull/3036
* Add OlmoForCausalLM (v1/v2) AWQ mapping using exaone4-style by @HumphreySun98 in https://github.com/vllm-project/llm-compressor/pull/2802
* [Examples] Add qwen3_moe example by @kylesayrs in https://github.com/vllm-project/llm-compressor/pull/2946
* [Docs] Minor fixes for sequential onloading docs by @kylesayrs in https://github.com/vllm-project/llm-compressor/pull/2771
* Add e2e sanity prompts to tiny model finetune dataset by @kylesayrs in https://github.com/vllm-project/llm-compressor/pull/3047
* Update What's New with Nemotron 3.5 Lightning and Kimi-K3 checkpoints by @dsikka in https://github.com/vllm-project/llm-compressor/pull/3034
* feat: dynamic memory-aware GPU scheduling for model-free PTQ by @rohan9446 in https://github.com/vllm-project/llm-compressor/pull/2976
* fix: runtime bugs in recipe validation, autoround, and awq by @soyr-redhat in https://github.com/vllm-project/llm-compressor/pull/2973
* [Sequential Onloading] Support onloading and offloading frozen dataclasses by @kylesayrs in https://github.com/vllm-project/llm-compressor/pull/2016
* [Autowrapper] Skip dead branches when tracking local names by @kylesayrs in https://github.com/vllm-project/llm-compressor/pull/3046
* INFERENG-9489: Simplify Transformers tests detection using Buildkite `if_changed` by @rashmigottipati in https://github.com/vllm-project/llm-compressor/pull/2983
* [Examples] remove gpt oss example by @brian-dellabetta in https://github.com/vllm-project/llm-compressor/pull/2742
* [example]Add Mixed MXFP4-MXFP8 DS V4 by @yiliu30 in https://github.com/vllm-project/llm-compressor/pull/2897
* fix(autoround): prevent input_capture_hook from accumulating GPU memory during optimization by @xesdiny in https://github.com/vllm-project/llm-compressor/pull/3024
* [AWQ] [gemma3] remove input layernorm mapping by @brian-dellabetta in https://github.com/vllm-project/llm-compressor/pull/2571
* Add config filter flag to test runner script by @HDCharles in https://github.com/vllm-project/llm-compressor/pull/3027
* [Performance] Speed up subgraph tracing by @YingqiDuan in https://github.com/vllm-project/llm-compressor/pull/2992
* [debugging] update awq to work with qwen3.8 by @dsikka in https://github.com/vllm-project/llm-compressor/pull/3041
* [ModelFreePTQ] Support quantization configs by @kylesayrs in https://github.com/vllm-project/llm-compressor/pull/3053
* [Qwen3.8] Add qwen3_8 examples by @dsikka in https://github.com/vllm-project/llm-compressor/pull/3043
* [Bugfix] Increase version requirement for skipped kv tests by @kylesayrs in https://github.com/vllm-project/llm-compressor/pull/3056
* [REAP] DDP Support by @kylesayrs in https://github.com/vllm-project/llm-compressor/pull/3045
* MSE Observer Enhancement by @Roderick-Wu in https://github.com/vllm-project/llm-compressor/pull/2950
* [Examples] Glm5.2 MXFP4xMXFP8 by @kylesayrs in https://github.com/vllm-project/llm-compressor/pull/3048
* Remove GraniteMoeLinearExperts by @kylesayrs in https://github.com/vllm-project/llm-compressor/pull/2885
* [REAP] Replace Kimi-K3-0.40B with Qwen3.8-1.0B-A0.6B in DDP test by @kylesayrs in https://github.com/vllm-project/llm-compressor/pull/3067
* Add "perfectblend" prebaked dataset and "ultrachat" alias by @kylesayrs in https://github.com/vllm-project/llm-compressor/pull/3060
* disable moe_calibrate_all_experts for Autoround example. by @changwangss in https://github.com/vllm-project/llm-compressor/pull/2877
* Add Glm4MoeLiteForCausalLM to SmoothQuant MAPPINGS_REGISTRY by @robertlangdonn in https://github.com/vllm-project/llm-compressor/pull/3072
* docs: link FAQ from README by @Karunasagar12 in https://github.com/vllm-project/llm-compressor/pull/2913
* [Bugfix] Resolve decorated forwards without functools.wraps in autowrap_forward by @malaiwah in https://github.com/vllm-project/llm-compressor/pull/3058
* [Performance] Speed up subgraph tracing - add direct dict lookup for O(1) node membership checks by @wanadzhar913 in https://github.com/vllm-project/llm-compressor/pull/2999
* fix: use forward globals when autowrapping by @mikemikimike in https://github.com/vllm-project/llm-compressor/pull/3079
* [Tests] Nightly lmeval tests by @kylesayrs in https://github.com/vllm-project/llm-compressor/pull/3004
* Update What's New with Qwen.3.8 by @dsikka in https://github.com/vllm-project/llm-compressor/pull/3087
* docs: update Granite 4 fp8 guide for automatic MoE expert linearization by @devangpratap in https://github.com/vllm-project/llm-compressor/pull/3093
* Fix collect_env crash on Apple Silicon by @Isitthakkar11 in https://github.com/vllm-project/llm-compressor/pull/3068
* Skip compute-capability tests on backends without get_device_capability by @Isitthakkar11 in https://github.com/vllm-project/llm-compressor/pull/3084
* Remove GPTQ Group/Dynamic Activation Ordering by @Roderick-Wu in https://github.com/vllm-project/llm-compressor/pull/3038
* fix(trace): make llmcompressor.trace boolean flags actually toggleable by @Anai-Guo in https://github.com/vllm-project/llm-compressor/pull/3070
* Replace example datasets with prebaked "perfectblend" and "flickr30k" by @kylesayrs in https://github.com/vllm-project/llm-compressor/pull/3062
* imatrix expansion, add fouroversix observer by @Roderick-Wu in https://github.com/vllm-project/llm-compressor/pull/3076
* [GPTQ] Emit an end-of-run summary when modules fall back to RTN by @rishabhsinha17 in https://github.com/vllm-project/llm-compressor/pull/3098
* Enable applying AWQ and SmoothQuant with GPTQ and the QuantizationModifier by @dsikka in https://github.com/vllm-project/llm-compressor/pull/2971
* [Example] Update recipe by @dsikka in https://github.com/vllm-project/llm-compressor/pull/3035
* refactor: port exec_jobs_dynamic to compressed-tensors by @soyr-redhat in https://github.com/vllm-project/llm-compressor/pull/3075
* [REAP] Support e-score correction bias, add HY3 example by @kylesayrs in https://github.com/vllm-project/llm-compressor/pull/3101
* [Bugfix] Fix polynomial_decay pruning scheduler for even exponents by @winklemad in https://github.com/vllm-project/llm-compressor/pull/3096
* feat(moe): add patch_moe_mappings to override 2D load mappings per checkpoint by @Anai-Guo in https://github.com/vllm-project/llm-compressor/pull/3080
* [Fix] Recipe.dict() shadows builtin dict — unimportable on Python 3.14 (#2778) by @yushuosun in https://github.com/vllm-project/llm-compressor/pull/2871
* Add Cohere2MoE mappings (AWQ + SmoothQuant) and DeepseekV2 AWQ registration by @robertlangdonn in https://github.com/vllm-project/llm-compressor/pull/2938
* [Examples] Add MR-GPTQ (QuIP + GPTQ + NVFP4A16) example by @Yatimai in https://github.com/vllm-project/llm-compressor/pull/2751
* Explain calibration levers in the sequential OOM message by @rishabhsinha17 in https://github.com/vllm-project/llm-compressor/pull/3012
* [AutoRound] Offload calibration inputs to CPU to prevent VRAM OOM with large N by @xesdiny in https://github.com/vllm-project/llm-compressor/pull/3055
* [Example] Add Mixed W2A16 and W4A16 MoE Example by @yiliu30 in https://github.com/vllm-project/llm-compressor/pull/2940
* Move Observer Resolution and Defaulting to LLM-Compressor by @Roderick-Wu in https://github.com/vllm-project/llm-compressor/pull/3091
* [AWQ] Muse Glimmer Mappings by @brian-dellabetta in https://github.com/vllm-project/llm-compressor/pull/3124
* Update README with new model features and links by @dsikka in https://github.com/vllm-project/llm-compressor/pull/3110
* [LM Eval] Enable multiple cadence for lm-eval by @dsikka in https://github.com/vllm-project/llm-compressor/pull/3115
* [Tests] Use prebaked "perfectblend" as default calibration dataset for tests by @kylesayrs in https://github.com/vllm-project/llm-compressor/pull/3063
* refactor: unify model-free ptq into ModelFreePtqConverter class by @soyr-redhat in https://github.com/vllm-project/llm-compressor/pull/2935
* remove bad four over six by @HDCharles in https://github.com/vllm-project/llm-compressor/pull/3125
* Fix noisy GPT-OSS linearize test by @PranjalAdhikari in https://github.com/vllm-project/llm-compressor/pull/3123
* Register GptOssLinearExperts for gpt-oss expert linearization by @ganeshr10 in https://github.com/vllm-project/llm-compressor/pull/3100
* fix(args): escape '%' in DatasetArguments.splits help so argparse builds on Python 3.14 by @Anai-Guo in https://github.com/vllm-project/llm-compressor/pull/3140
* Update transformers to supported range by @dhuangnm in https://github.com/vllm-project/llm-compressor/pull/3122
* [Examples] [Tests] Add download limit for perfect blend by @kylesayrs in https://github.com/vllm-project/llm-compressor/pull/3141
* [Tests] Fix reap ddp vs single comparison test by @kylesayrs in https://github.com/vllm-project/llm-compressor/pull/3142
* feat: add FP8 attention and Autoround examples by @wimCCC in https://github.com/vllm-project/llm-compressor/pull/3092
* [Bugfix] Validate expand >= 1.0 in MovingAverageMSEObserver by @winklemad in https://github.com/vllm-project/llm-compressor/pull/3095
* [Tests] Fix ddp smoke tests by @kylesayrs in https://github.com/vllm-project/llm-compressor/pull/3146
* ci: add pre-commit hooks mirroring make quality by @orestis-z in https://github.com/vllm-project/llm-compressor/pull/3120
* Add resave_config to preserve original model config on save by @kylesayrs in https://github.com/vllm-project/llm-compressor/pull/3147
* Add NanbeigeForCausalLM to SmoothQuant MAPPINGS_REGISTRY by @robertlangdonn in https://github.com/vllm-project/llm-compressor/pull/3073
* Update CODEOWNERS by @dsikka in https://github.com/vllm-project/llm-compressor/pull/3155
* [Bugfix] Fix serialization of dtype by @kylesayrs in https://github.com/vllm-project/llm-compressor/pull/3152
* [Bugfix] Fix reap test by @kylesayrs in https://github.com/vllm-project/llm-compressor/pull/3153
* feat: add Kimi-K3 model definition and quantization example by @kylesayrs in https://github.com/vllm-project/llm-compressor/pull/2994
* Add GLM 5.3 MXFp4 example by @dsikka in https://github.com/vllm-project/llm-compressor/pull/3163
* examples: add Llama 3.3 70B MXFP8 and FP8 attention example by @changwangss in https://github.com/vllm-project/llm-compressor/pull/3160
* fix: Skip weightless modules in distributed greedy bin packing by @Asthenia0412 in https://github.com/vllm-project/llm-compressor/pull/3113
* [GPTQ] Hoist loop invariants out of the per-column quantization loop by @rishabhsinha17 in https://github.com/vllm-project/llm-compressor/pull/3097
* [Typing] Modernize type hints in logger, datasets, and observers by @arijitroy003 in https://github.com/vllm-project/llm-compressor/pull/2960
* [Tests] [Bugfix] Fix kwargs for prebaked datasets by @kylesayrs in https://github.com/vllm-project/llm-compressor/pull/3167
* [Tests] Reduce linearize test noise by @kylesayrs in https://github.com/vllm-project/llm-compressor/pull/3166
* [Tests] Weekly lm eval tests by @kylesayrs in https://github.com/vllm-project/llm-compressor/pull/3022
* [MFPTQ] Implement profiler-based memory estimates by @kylesayrs in https://github.com/vllm-project/llm-compressor/pull/3158
* [Tests] Fix perplexity test by @kylesayrs in https://github.com/vllm-project/llm-compressor/pull/3168
* [Tests] [Bugfix] Default to unset max_model_len by @kylesayrs in https://github.com/vllm-project/llm-compressor/pull/3170
* [Agents] Migrate .claude to .agents by @kylesayrs in https://github.com/vllm-project/llm-compressor/pull/3172
* Add batched GPTQ quantization with actorder support by @HDCharles in https://github.com/vllm-project/llm-compressor/pull/3128
* [Offloading] Bump required accelerate version by @kylesayrs in https://github.com/vllm-project/llm-compressor/pull/3176
* [Agents] Save multimodal processor for create-tiny-model skill by @kylesayrs in https://github.com/vllm-project/llm-compressor/pull/3175
* [MoE] Add nemotron_h fast loading support by @kylesayrs in https://github.com/vllm-project/llm-compressor/pull/3173
* Add explicit LinearExperts2D -> 3D MoE repack for HF-native saves by @GOavi101 in https://github.com/vllm-project/llm-compressor/pull/3017
* [Tracing] [Tests] Parameterize model tracing tests with tiny models collection by @kylesayrs in https://github.com/vllm-project/llm-compressor/pull/3174
* Add GLM-5.3-MXFP4 checkpoint to What's New section by @dsikka in https://github.com/vllm-project/llm-compressor/pull/3179
* [AWQ] Fix Qwen2.5-VL mapping registry entry (vision tower collapses MLP mapping) by @AbigaleD in https://github.com/vllm-project/llm-compressor/pull/3169
* Update dependency versions by @dhuangnm in https://github.com/vllm-project/llm-compressor/pull/3182
* [Datasets] Change `pad_to_max_length` default by @kylesayrs in https://github.com/vllm-project/llm-compressor/pull/3180
* [Model] GLM 5.3 Flash by @kylesayrs in https://github.com/vllm-project/llm-compressor/pull/3164
* [Bugfix] Do not recurse into container modules in observe/update_qparams by @Ar4ikov in https://github.com/vllm-project/llm-compressor/pull/2990
* [GPTQ] Fix FP8 handling on A100 and disable failing tests on A100 by @HDCharles in https://github.com/vllm-project/llm-compressor/pull/3181
* Skip CUDA compute-capability tests on XPU by @HDCharles in https://github.com/vllm-project/llm-compressor/pull/3187
* [Bugfix] Fix glm53 dequant example by @kylesayrs in https://github.com/vllm-project/llm-compressor/pull/3189
* [Bugfix] Fix distributed hang from mis-shaped weight_global_scale writeback by @kylesayrs in https://github.com/vllm-project/llm-compressor/pull/3185
* [AutoRound] Pad captured inputs to a common sequence length by @kylesayrs in https://github.com/vllm-project/llm-compressor/pull/3190
* [Observer] Triton grid search for the MSE observer by @Bias92 in https://github.com/vllm-project/llm-compressor/pull/2991
* [bugfix] fix global scale shape by @HDCharles in https://github.com/vllm-project/llm-compressor/pull/3191
* [Tests] Lower w4a4_nvfp4 recovery threshold to 0.94 by @kylesayrs in https://github.com/vllm-project/llm-compressor/pull/3186
* use load_context in llm-compressor by @HDCharles in https://github.com/vllm-project/llm-compressor/pull/3201
* [Tests] Catch upload failures for e2e tests by @kylesayrs in https://github.com/vllm-project/llm-compressor/pull/3197
* [Tests] Increase test consistency, reduce noise thresholds for unit tests by @kylesayrs in https://github.com/vllm-project/llm-compressor/pull/3198
* [Bugfix] [Tests] Add version gate to `test_model_trace` by @kylesayrs in https://github.com/vllm-project/llm-compressor/pull/3195
* refactor: import TensorProfiler from compressed-tensors as opposed to inline by @soyr-redhat in https://github.com/vllm-project/llm-compressor/pull/3203
* [Bugfix] Support upfront model decompression, Kimi-K3 by @kylesayrs in https://github.com/vllm-project/llm-compressor/pull/3184
* Update What's New with recent RedHatAI model checkpoints by @dsikka in https://github.com/vllm-project/llm-compressor/pull/3205
* [Tests] Add kimi-k3 dependencies by @kylesayrs in https://github.com/vllm-project/llm-compressor/pull/3207
* bump up compressed-tensors version by @dhuangnm in https://github.com/vllm-project/llm-compressor/pull/3213
* Update merge protections to remove maintainer review by @dsikka in https://github.com/vllm-project/llm-compressor/pull/3212
* Update CODEOWNERS to include Roderick-Wu by @Roderick-Wu in https://github.com/vllm-project/llm-compressor/pull/3215
* Update README with improved FP4 observer details by @Roderick-Wu in https://github.com/vllm-project/llm-compressor/pull/3219
* docs updates by @HDCharles in https://github.com/vllm-project/llm-compressor/pull/3214

## New Contributors
* @rohan9446 made their first contribution in https://github.com/vllm-project/llm-compressor/pull/2976
* @rashmigottipati made their first contribution in https://github.com/vllm-project/llm-compressor/pull/2983
* @xesdiny made their first contribution in https://github.com/vllm-project/llm-compressor/pull/3024
* @YingqiDuan made their first contribution in https://github.com/vllm-project/llm-compressor/pull/2992
* @robertlangdonn made their first contribution in https://github.com/vllm-project/llm-compressor/pull/3072
* @Karunasagar12 made their first contribution in https://github.com/vllm-project/llm-compressor/pull/2913
* @malaiwah made their first contribution in https://github.com/vllm-project/llm-compressor/pull/3058
* @mikemikimike made their first contribution in https://github.com/vllm-project/llm-compressor/pull/3079
* @devangpratap made their first contribution in https://github.com/vllm-project/llm-compressor/pull/3093
* @Isitthakkar11 made their first contribution in https://github.com/vllm-project/llm-compressor/pull/3068
* @Anai-Guo made their first contribution in https://github.com/vllm-project/llm-compressor/pull/3070
* @rishabhsinha17 made their first contribution in https://github.com/vllm-project/llm-compressor/pull/3098
* @winklemad made their first contribution in https://github.com/vllm-project/llm-compressor/pull/3096
* @yushuosun made their first contribution in https://github.com/vllm-project/llm-compressor/pull/2871
* @PranjalAdhikari made their first contribution in https://github.com/vllm-project/llm-compressor/pull/3123
* @ganeshr10 made their first contribution in https://github.com/vllm-project/llm-compressor/pull/3100
* @wimCCC made their first contribution in https://github.com/vllm-project/llm-compressor/pull/3092
* @Asthenia0412 made their first contribution in https://github.com/vllm-project/llm-compressor/pull/3113
* @AbigaleD made their first contribution in https://github.com/vllm-project/llm-compressor/pull/3169
* @Ar4ikov made their first contribution in https://github.com/vllm-project/llm-compressor/pull/2990

**Full Changelog**: https://github.com/vllm-project/llm-compressor/compare/0.13.0...0.14.0
