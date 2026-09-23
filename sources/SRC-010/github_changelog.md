# Changelog (aggregated from releases.body)

> releases: 70

## v0.0.2 (2023-07-28)


## What's Changed

### 🚀 Features

* Add lmdeploy python package built scripts and CI workflow by @irexyc in <https://github.com/InternLM/lmdeploy/pull/163>, <https://github.com/InternLM/lmdeploy/pull/164>, <https://github.com/InternLM/lmdeploy/pull/170>
* Support LLama-2 with GQA by @lzhangzz in <https://github.com/InternLM/lmdeploy/pull/147> and @grimoire in <https://github.com/InternLM/lmdeploy/pull/160>
* Add Llama-2 chat template by @grimoire in <https://github.com/InternLM/lmdeploy/pull/140>
* Add decode-only forward pass by @lzhangzz in <https://github.com/InternLM/lmdeploy/pull/153>
* Support tensor parallelism in turbomind's python API by @grimoire <https://github.com/InternLM/lmdeploy/pull/82>
* Support w pack qkv by @tpoisonooo in <https://github.com/InternLM/lmdeploy/pull/83>

### 💥 Improvements

* Refactor the chat template of supported models using factory pattern  by @lvhan028 in <https://github.com/InternLM/lmdeploy/pull/144> and @streamsunshine in <https://github.com/InternLM/lmdeploy/pull/174>
* Add profile throughput benchmark by @grimoire in <https://github.com/InternLM/lmdeploy/pull/146>
* Remove slicing reponse and add resume api by @streamsunshine in <https://github.com/InternLM/lmdeploy/pull/154>
* Support DeepSpeed on autoTP and kernel injection by @KevinNuNu and @wangruohui in <https://github.com/InternLM/lmdeploy/pull/138>
* Add github action for publishing docker image by @RunningLeon in <https://github.com/InternLM/lmdeploy/pull/148>
* 

### 🐞 Bug fixes

* Fix getting package root path error in python3.9 by @lvhan028 in <https://github.com/InternLM/lmdeploy/pull/157>
* Return carriage caused overwriting at the same line by @wangruohui in <https://github.com/InternLM/lmdeploy/pull/143>
* Fix the offset during streaming chat by @lvhan028 in <https://github.com/InternLM/lmdeploy/pull/142>
* Fix concatenate bug in benchmark serving script by @rollroll90 in <https://github.com/InternLM/lmdeploy/pull/134>
* Fix attempted_relative_import by @KevinNuNu in <https://github.com/InternLM/lmdeploy/pull/125>

### 📚 Documentations

* Translate `en/quantization.md` into Chinese by @xin-li-67 in <https://github.com/InternLM/lmdeploy/pull/166>
* Check-in benchmark on real conversation data by @lvhan028 in <https://github.com/InternLM/lmdeploy/pull/156>
* Fix typo and missing dependant packages in REAME and requirements.txt by @vansin in <https://github.com/InternLM/lmdeploy/pull/123>, @APX103 in <https://github.com/InternLM/lmdeploy/pull/109>, @AllentDan in <https://github.com/InternLM/lmdeploy/pull/119> and @del-zhenwu in <https://github.com/InternLM/lmdeploy/pull/124>
* Add turbomind's architecture documentation by @lzhangzz in <https://github.com/InternLM/lmdeploy/pull/101>


## New Contributors
@streamsunshine @del-zhenwu @APX103 @xin-li-67 @KevinNuNu @rollroll90 


## v0.0.3 (2023-08-09)

## What's Changed

### 🚀 Features
* Support tensor parallelism without offline splitting model weights by @grimoire in https://github.com/InternLM/lmdeploy/pull/158
 * Add script to split HuggingFace model to the smallest sharded checkpoints by @LZHgrla in https://github.com/InternLM/lmdeploy/pull/199
 * Add non-stream inference api for chatbot by @lvhan028 in https://github.com/InternLM/lmdeploy/pull/200
 *
### 💥 Improvements
* Add issue/pr templates by @lvhan028 in https://github.com/InternLM/lmdeploy/pull/184
* Remove unused code to reduce binary size by @lzhangzz in https://github.com/InternLM/lmdeploy/pull/181
* Support serving with gradio without communicating to TIS by @AllentDan in https://github.com/InternLM/lmdeploy/pull/162
* Improve postprocessing in TIS serving by applying Incremental de-tokenizing by @lvhan028 in https://github.com/InternLM/lmdeploy/pull/197
* Support multi-session chat by @wangruohui in https://github.com/InternLM/lmdeploy/pull/178

### 🐞 Bug fixes
* Fix build test error and move turbmind csrc test cases to `tests/csrc` by @lvhan028 in https://github.com/InternLM/lmdeploy/pull/188
* Fix launching client error by moving lmdeploy/turbomind/utils.py to lmdeploy/utils.py by @lvhan028 in https://github.com/InternLM/lmdeploy/pull/191

### 📚 Documentations
* Update README.md by @tpoisonooo in https://github.com/InternLM/lmdeploy/pull/187
* Translate turbomind.md by @xin-li-67 in https://github.com/InternLM/lmdeploy/pull/173

## New Contributors
* @LZHgrla made their first contribution in https://github.com/InternLM/lmdeploy/pull/199

**Full Changelog**: https://github.com/InternLM/lmdeploy/compare/v0.0.2...v0.0.3

## v0.0.4 (2023-08-14)

<!-- Release notes generated using configuration in .github/release.yml at main -->

## Highlight
* Support 4-bit LLM quantization and inference. Check [this](https://github.com/InternLM/lmdeploy/blob/main/docs/en/w4a16.md) guide for detailed information.
![image](https://github.com/InternLM/lmdeploy/assets/4560679/b38fc352-471e-4c06-9e31-5e251a6216f6)

## What's Changed
### 🚀 Features
* Blazing fast W4A16 inference by @lzhangzz in https://github.com/InternLM/lmdeploy/pull/202 
* Support AWQ  by @pppppM in https://github.com/InternLM/lmdeploy/pull/108 and @AllentDan in https://github.com/InternLM/lmdeploy/pull/228


### 💥 Improvements
* Add release note template by @lvhan028 in https://github.com/InternLM/lmdeploy/pull/211
* feat(quantization): kv cache use asymmetric by @tpoisonooo in https://github.com/InternLM/lmdeploy/pull/218

### 🐞 Bug fixes
* Fix TIS client got-no-space-result side effect brought by PR #197 by @lvhan028 in https://github.com/InternLM/lmdeploy/pull/222

### 📚 Documentations
* Update W4A16 News by @pppppM in https://github.com/InternLM/lmdeploy/pull/227
* Check-in user guide for w4a16 LLM deployment by @lvhan028 in https://github.com/InternLM/lmdeploy/pull/224

**Full Changelog**: https://github.com/InternLM/lmdeploy/compare/v0.0.3...v0.0.4

## v0.0.5 (2023-08-15)

<!-- Release notes generated using configuration in .github/release.yml at main -->

## What's Changed

### 🐞 Bug fixes
* Fix wrong RPATH using the absolute path instead of relative one by @irexyc in https://github.com/InternLM/lmdeploy/pull/239


**Full Changelog**: https://github.com/InternLM/lmdeploy/compare/v0.0.4...v0.0.5

## v0.0.6 (2023-08-25)

<!-- Release notes generated using configuration in .github/release.yml at main -->

## Highlights

* Support Qwen-7B with dynamic NTK scaling and logN scaling in turbomind
* Support tensor parallelism for W4A16
* Add OpenAI-like RESTful API
* Support Llama-2 70B 4-bit quantization

## What's Changed

### 🚀 Features
* Profiling tool for huggingface and deepspeed models by @wangruohui in https://github.com/InternLM/lmdeploy/pull/161
* Support windows platform by @irexyc in https://github.com/InternLM/lmdeploy/pull/209
* Qwen-7B, dynamic NTK scaling and logN scaling support in turbomind  by @lzhangzz in https://github.com/InternLM/lmdeploy/pull/230
* Add Restful API by @AllentDan in https://github.com/InternLM/lmdeploy/pull/223
* Support context decoding with DP in pytorch by @wangruohui in https://github.com/InternLM/lmdeploy/pull/193

### 💥 Improvements
* Support TP for W4A16 by @lzhangzz in https://github.com/InternLM/lmdeploy/pull/262
* Pass chat template args including meta_prompt to model(https://github.com/InternLM/lmdeploy/commit/7785142d7c13a21bc01c2e7c0bc10b82964371f1) by @AllentDan in https://github.com/InternLM/lmdeploy/pull/225
* Enable the Gradio server to call inference services through the RESTful API by @AllentDan in https://github.com/InternLM/lmdeploy/pull/287

### 🐞 Bug fixes
* Adjust dependency of gradio server by @AllentDan in https://github.com/InternLM/lmdeploy/pull/236
* Implement `movmatrix` using warp shuffling for CUDA < 11.8 by @lzhangzz in https://github.com/InternLM/lmdeploy/pull/267
* Add 'accelerate' to requirement list by @lvhan028 in https://github.com/InternLM/lmdeploy/pull/261
* Fix building with CUDA 11.3 by @lzhangzz in https://github.com/InternLM/lmdeploy/pull/280
* Pad tok_embedding and output weights to make their shape divisible by TP by @lvhan028 in https://github.com/InternLM/lmdeploy/pull/285
* Fix llama2 70b & qwen quantization error by @pppppM in https://github.com/InternLM/lmdeploy/pull/273
* Import turbomind in gradio server only when it is needed by @AllentDan in https://github.com/InternLM/lmdeploy/pull/303

### 📚 Documentations
* Remove specified version in user guide by @lvhan028 in https://github.com/InternLM/lmdeploy/pull/241
* docs(quantzation): update description by @tpoisonooo in https://github.com/InternLM/lmdeploy/pull/253 and https://github.com/InternLM/lmdeploy/pull/272
* Check-in FAQ by @lvhan028 in https://github.com/InternLM/lmdeploy/pull/256
* add readthedocs by @RunningLeon in https://github.com/InternLM/lmdeploy/pull/208

### 🌐 Other
* Update workflow for building docker image by @RunningLeon in https://github.com/InternLM/lmdeploy/pull/282
* Change to github-hosted runner for building docker image by @RunningLeon in https://github.com/InternLM/lmdeploy/pull/291

### Known issues
* 4-bit Qwen-7b model inference failed. #307 is addressing this issue.


**Full Changelog**: https://github.com/InternLM/lmdeploy/compare/v0.0.5...v0.0.6

## v0.0.7 (2023-09-04)

<!-- Release notes generated using configuration in .github/release.yml at main -->

## Highlights
* Flash attention 2 is supported, boosting context decoding speed by approximately 45% 
* Token_id decoding has been optimized for better efficiency
* The gemm-tunned script has been packed in the PyPI package

## What's Changed
### 🚀 Features
* Add flashattention2 by @grimoire in https://github.com/InternLM/lmdeploy/pull/196
### 💥 Improvements
* add llama_gemm to wheel  by @irexyc in https://github.com/InternLM/lmdeploy/pull/320
* Decode generated token_ids incrementally by @AllentDan in https://github.com/InternLM/lmdeploy/pull/309
### 🐞 Bug fixes
* Fix turbomind import error on windows by @irexyc in https://github.com/InternLM/lmdeploy/pull/316
* Fix profile_serving hung issue by @lvhan028 in https://github.com/InternLM/lmdeploy/pull/344
### 📚 Documentations
* Fix readthedocs building by @RunningLeon in https://github.com/InternLM/lmdeploy/pull/321
* fix(kvint8): update doc by @tpoisonooo in https://github.com/InternLM/lmdeploy/pull/315
* Update FAQ for restful api by @AllentDan in https://github.com/InternLM/lmdeploy/pull/319



**Full Changelog**: https://github.com/InternLM/lmdeploy/compare/v0.0.6...v0.0.7

## v0.0.8 (2023-09-11)

<!-- Release notes generated using configuration in .github/release.yml at main -->
## Highlight
* Support Baichuan2-7B-Base and Baichuan2-7B-Chat
* Support all features of Code Llama: code completion, infilling, chat / instruct, and python specialist

## What's Changed
### 🚀 Features
* Support baichuan2-chat chat template by @wangruohui in https://github.com/InternLM/lmdeploy/pull/378
* Support codellama by @lvhan028 in https://github.com/InternLM/lmdeploy/pull/359
### 🐞 Bug fixes
* [Fix] when using stream is False, continuous batching doesn't work by @sleepwalker2017 in https://github.com/InternLM/lmdeploy/pull/346
* [Fix] Set max dynamic smem size for decoder MHA to support context length > 8k by @lvhan028 in https://github.com/InternLM/lmdeploy/pull/377
* Fix exceed session len core dump for chat and generate by @AllentDan in https://github.com/InternLM/lmdeploy/pull/366
* [Fix] update puyu model by @Harold-lkk in https://github.com/InternLM/lmdeploy/pull/399

### 📚 Documentations
* [Docs] Fix quantization docs link by @LZHgrla in https://github.com/InternLM/lmdeploy/pull/367
* [Docs] Simplify `build.md` by @pppppM in https://github.com/InternLM/lmdeploy/pull/370
* [Docs] Update lmdeploy logo by @lvhan028 in https://github.com/InternLM/lmdeploy/pull/372

## New Contributors
* @sleepwalker2017 made their first contribution in https://github.com/InternLM/lmdeploy/pull/346

**Full Changelog**: https://github.com/InternLM/lmdeploy/compare/v0.0.7...v0.0.8

## v0.0.9 (2023-09-20)

<!-- Release notes generated using configuration in .github/release.yml at main -->

## Highlight

* Support InternLM 20B, including FP16, W4A16, and W4KV8

## What's Changed

### 🚀 Features
* Support InternLM 20B by @lvhan028 in https://github.com/InternLM/lmdeploy/pull/440

### 💥 Improvements
* Reduce gil switching by @irexyc in https://github.com/InternLM/lmdeploy/pull/407
* Profile token generation with more settings by @AllentDan in https://github.com/InternLM/lmdeploy/pull/364

### 🐞 Bug fixes
* Fix disk space limit for building docker image by @RunningLeon in https://github.com/InternLM/lmdeploy/pull/404
* more general pypi ci by @irexyc in https://github.com/InternLM/lmdeploy/pull/412
* Fix build.md by @pangsg in https://github.com/InternLM/lmdeploy/pull/411
* Fix memory leak by @irexyc in https://github.com/InternLM/lmdeploy/pull/415
* Fix token count bug by @AllentDan in https://github.com/InternLM/lmdeploy/pull/416
* [Fix] Support actual seqlen in flash-attention2 by @grimoire in https://github.com/InternLM/lmdeploy/pull/418
* [Fix] output[-1] when output is empty by @wangruohui in https://github.com/InternLM/lmdeploy/pull/405

### 🌐 Other
* rename readthedocs config file by @RunningLeon in https://github.com/InternLM/lmdeploy/pull/429
* bump version to v0.0.9 by @lvhan028 in https://github.com/InternLM/lmdeploy/pull/428

## New Contributors
* @pangsg made their first contribution in https://github.com/InternLM/lmdeploy/pull/411

**Full Changelog**: https://github.com/InternLM/lmdeploy/compare/v0.0.8...v0.0.9

## v0.0.10 (2023-09-26)

<!-- Release notes generated using configuration in .github/release.yml at main -->

## What's Changed
### 💥 Improvements
* [feature] Graceful termination of background threads in LlamaV2 by @akhoroshev in https://github.com/InternLM/lmdeploy/pull/458
* expose stop words and filter eoa by @AllentDan in https://github.com/InternLM/lmdeploy/pull/352
### 🐞 Bug fixes
* Fix side effect brought by supporting codellama: `sequence_start` is always true when calling `model.get_prompt` by @lvhan028 in https://github.com/InternLM/lmdeploy/pull/466
* Miss meta instruction of internlm-chat model by @lvhan028 in https://github.com/InternLM/lmdeploy/pull/470
* [bug] Fix race condition by @akhoroshev in https://github.com/InternLM/lmdeploy/pull/460
* Fix compatibility issues with Pydantic 2 by @aisensiy in https://github.com/InternLM/lmdeploy/pull/465
* fix benchmark serving cannot use Qwen tokenizer by @AllentDan in https://github.com/InternLM/lmdeploy/pull/443
* Fix memory leak by @lvhan028 in https://github.com/InternLM/lmdeploy/pull/488
### 📚 Documentations
* Fix typo in README.md by @eltociear in https://github.com/InternLM/lmdeploy/pull/462
### 🌐 Other
* bump version to v0.0.10 by @lvhan028 in https://github.com/InternLM/lmdeploy/pull/474

## New Contributors
* @eltociear made their first contribution in https://github.com/InternLM/lmdeploy/pull/462
* @akhoroshev made their first contribution in https://github.com/InternLM/lmdeploy/pull/458
* @aisensiy made their first contribution in https://github.com/InternLM/lmdeploy/pull/465

**Full Changelog**: https://github.com/InternLM/lmdeploy/compare/v0.0.9...v0.0.10

## v0.0.11 (2023-10-17)

<!-- Release notes generated using configuration in .github/release.yml at main -->

## What's Changed
### 🚀 Features
* Support CORS for openai api server by @aisensiy in https://github.com/InternLM/lmdeploy/pull/481
### 💥 Improvements
* make IPv6 compatible, safe run for coroutine interrupting by @AllentDan in https://github.com/InternLM/lmdeploy/pull/487
* support deploy qwen-14b-chat by @irexyc in https://github.com/InternLM/lmdeploy/pull/482
* add tp hint for deployment by @irexyc in https://github.com/InternLM/lmdeploy/pull/555
* Move `tokenizer.py` to the folder of lmdeploy by @grimoire in https://github.com/InternLM/lmdeploy/pull/543
### 🐞 Bug fixes
* Change `shared_instance` type from `weakptr` to `shared_ptr` by @lvhan028 in https://github.com/InternLM/lmdeploy/pull/507
* [Fix] Set the default value of `step` being 0 by @lvhan028 in https://github.com/InternLM/lmdeploy/pull/532
* [bug] fix mismatched shape for decoder output tensor by @akhoroshev in https://github.com/InternLM/lmdeploy/pull/517
* Fix typing of openai protocol. by @mokeyish in https://github.com/InternLM/lmdeploy/pull/554
### 📚 Documentations
* Fix typo in `docs/en/pytorch.md` by @shahrukhx01 in https://github.com/InternLM/lmdeploy/pull/539
* [Doc] update huggingface internlm-chat-7b model url by @AllentDan in https://github.com/InternLM/lmdeploy/pull/546
* [doc] Update benchmark command in w4a16.md by @del-zhenwu in https://github.com/InternLM/lmdeploy/pull/500
### 🌐 Other
* free runner disk by @irexyc in https://github.com/InternLM/lmdeploy/pull/552
* bump version to v0.0.11 by @lvhan028 in https://github.com/InternLM/lmdeploy/pull/567

## New Contributors
* @shahrukhx01 made their first contribution in https://github.com/InternLM/lmdeploy/pull/539
* @mokeyish made their first contribution in https://github.com/InternLM/lmdeploy/pull/554

**Full Changelog**: https://github.com/InternLM/lmdeploy/compare/v0.0.10...v0.0.11

## v0.0.12 (2023-10-24)

<!-- Release notes generated using configuration in .github/release.yml at main -->

## What's Changed
### 🚀 Features
* add solar chat template by @AllentDan in https://github.com/InternLM/lmdeploy/pull/576 and  https://github.com/InternLM/lmdeploy/pull/587
### 💥 Improvements
* change `model_format` to `qwen` when `model_name` starts with `qwen` by @lvhan028 in https://github.com/InternLM/lmdeploy/pull/575
* robust incremental decode for leading space by @AllentDan in https://github.com/InternLM/lmdeploy/pull/581

### 🐞 Bug fixes
* avoid splitting chinese characters during decoding by @AllentDan in https://github.com/InternLM/lmdeploy/pull/566
* Revert "[Docs] Simplify `build.md`" by @pppppM in https://github.com/InternLM/lmdeploy/pull/586
* Fix crash and remove `sys_instruct` from `chat.py` and `client.py` by @irexyc in https://github.com/InternLM/lmdeploy/pull/591
### 🌐 Other
* bump version to v0.0.12 by @lvhan028 in https://github.com/InternLM/lmdeploy/pull/604


**Full Changelog**: https://github.com/InternLM/lmdeploy/compare/v0.0.11...v0.0.12

## v0.0.13 (2023-10-30)

<!-- Release notes generated using configuration in .github/release.yml at main -->

## What's Changed
### 🚀 Features
* Add more user-friendly CLI  by @RunningLeon in https://github.com/InternLM/lmdeploy/pull/541
### 💥 Improvements
* support inference a batch of prompts by @AllentDan in https://github.com/InternLM/lmdeploy/pull/467
### 📚 Documentations
* Add "build from docker" section by @lvhan028 in https://github.com/InternLM/lmdeploy/pull/602
### 🌐 Other
* bump version to v0.0.13 by @lvhan028 in https://github.com/InternLM/lmdeploy/pull/620


**Full Changelog**: https://github.com/InternLM/lmdeploy/compare/v0.0.12...v0.0.13

## v0.0.14 (2023-11-09)

<!-- Release notes generated using configuration in .github/release.yml at main -->

## What's Changed

### 💥 Improvements
* Improve api_server and webui usage by @AllentDan in https://github.com/InternLM/lmdeploy/pull/544
* fix: gradio gr.Button.update deprecated after 4.0.0 by @hscspring in https://github.com/InternLM/lmdeploy/pull/637
* add cli to list the supported model names by @RunningLeon in https://github.com/InternLM/lmdeploy/pull/639
* Refactor model conversion by @irexyc in https://github.com/InternLM/lmdeploy/pull/296
* [Enchance] internlm message to prompt by @Harold-lkk in https://github.com/InternLM/lmdeploy/pull/499
* update turbomind session_len with model.session_len by @AllentDan in https://github.com/InternLM/lmdeploy/pull/634
* Manage session id using random int for gradio local mode by @aisensiy in https://github.com/InternLM/lmdeploy/pull/553
* Add UltraCM and WizardLM chat templates by @AllentDan in https://github.com/InternLM/lmdeploy/pull/599
* Add check env sub command by @RunningLeon in https://github.com/InternLM/lmdeploy/pull/654
### 🐞 Bug fixes
* [Fix] Qwen's quantization results are abnormal & Baichuan cannot be quantized by @pppppM in https://github.com/InternLM/lmdeploy/pull/605
* FIX: fix stop_session func bug by @yunzhongyan0 in https://github.com/InternLM/lmdeploy/pull/578
* fix benchmark serving computation mistake by @AllentDan in https://github.com/InternLM/lmdeploy/pull/630
* fix Tokenizer load error when the path of the being-converted model is not writable by @irexyc in https://github.com/InternLM/lmdeploy/pull/669
* fix tokenizer_info when convert the model by @irexyc in https://github.com/InternLM/lmdeploy/pull/661
### 🌐 Other
* bump version to v0.0.14 by @lvhan028 in https://github.com/InternLM/lmdeploy/pull/663

## New Contributors
* @hscspring made their first contribution in https://github.com/InternLM/lmdeploy/pull/637
* @yunzhongyan0 made their first contribution in https://github.com/InternLM/lmdeploy/pull/578

**Full Changelog**: https://github.com/InternLM/lmdeploy/compare/v0.0.13...v0.0.14

## v0.1.0a0 (2023-11-23)

<!-- Release notes generated using configuration in .github/release.yml at v0.1.0a0 -->

## What's Changed
### 🚀 Features
* Add extra_requires to reduce dependencies by @RunningLeon in https://github.com/InternLM/lmdeploy/pull/580
* TurboMind 2 by @lzhangzz in https://github.com/InternLM/lmdeploy/pull/590
* Support loading hf model directly by @irexyc in https://github.com/InternLM/lmdeploy/pull/685
### 💥 Improvements
* Fix Tokenizer encode by @AllentDan in https://github.com/InternLM/lmdeploy/pull/645
* Optimize for throughput by @lzhangzz in https://github.com/InternLM/lmdeploy/pull/701
* Replace mmengine with mmengine-lite by @zhouzaida in https://github.com/InternLM/lmdeploy/pull/715
### 🐞 Bug fixes
* Fix init of batch state by @lzhangzz in https://github.com/InternLM/lmdeploy/pull/682
* fix turbomind stream canceling by @grimoire in https://github.com/InternLM/lmdeploy/pull/686
* [Fix] Fix load_checkpoint_in_model bug by @HIT-cwh in https://github.com/InternLM/lmdeploy/pull/690
* Fix wrong eos_id and bos_id obtained through grpc api by @lvhan028 in https://github.com/InternLM/lmdeploy/pull/644
* Fix cache/output length calculation by @lzhangzz in https://github.com/InternLM/lmdeploy/pull/738
* [Fix] Skip empty batch by @lzhangzz in https://github.com/InternLM/lmdeploy/pull/747
### 📚 Documentations
* [Docs] Update Supported Matrix by @pppppM in https://github.com/InternLM/lmdeploy/pull/679
* [Docs] Update KV8 Docs by @pppppM in https://github.com/InternLM/lmdeploy/pull/681
* [Doc] Update restful api doc by @AllentDan in https://github.com/InternLM/lmdeploy/pull/662
* Check-in user guide about turbomind config by @lvhan028 in https://github.com/InternLM/lmdeploy/pull/680
### 🌐 Other
* bump version to v0.1.0a0 by @lvhan028 in https://github.com/InternLM/lmdeploy/pull/709

## New Contributors
* @zhouzaida made their first contribution in https://github.com/InternLM/lmdeploy/pull/715

**Full Changelog**: https://github.com/InternLM/lmdeploy/compare/v0.0.14...v0.1.0a0

## v0.1.0a1 (2023-11-29)

<!-- Release notes generated using configuration in .github/release.yml at main -->

## What's Changed
### 💥 Improvements
* Set the default value of `max_context_token_num` 1 by @lvhan028 in https://github.com/InternLM/lmdeploy/pull/761
* add triton server test and workflow yml by @RunningLeon in https://github.com/InternLM/lmdeploy/pull/760
* improvement(build): enable ninja and gold linker by @tpoisonooo in https://github.com/InternLM/lmdeploy/pull/767
* Report first-token-latency and token-latency percentiles by @lvhan028 in https://github.com/InternLM/lmdeploy/pull/736
* convert model with hf repo_id by @irexyc in https://github.com/InternLM/lmdeploy/pull/774
### 🐞 Bug fixes
* [Fix] build docker image failed since `packaging` is missing by @lvhan028 in https://github.com/InternLM/lmdeploy/pull/753
* [Fix] Rollback the data type of `input_ids` to `TYPE_UINT32` in preprocessor's proto by @lvhan028 in https://github.com/InternLM/lmdeploy/pull/758
* fix turbomind build on sm<80 by @grimoire in https://github.com/InternLM/lmdeploy/pull/754
* fix typo by @grimoire in https://github.com/InternLM/lmdeploy/pull/769
### 🌐 Other
* bump version to 0.1.0a1 by @lvhan028 in https://github.com/InternLM/lmdeploy/pull/776


**Full Changelog**: https://github.com/InternLM/lmdeploy/compare/v0.1.0a0...v0.1.0a1

## v0.1.0a2 (2023-12-06)

<!-- Release notes generated using configuration in .github/release.yml at main -->

## What's Changed
### 💥 Improvements
* Unify prefill & decode passes by @lzhangzz in https://github.com/InternLM/lmdeploy/pull/775
* add cuda12.1 build check ci by @irexyc in https://github.com/InternLM/lmdeploy/pull/782
* auto upload cuda12.1 python pkg to release when create new tag by @irexyc in https://github.com/InternLM/lmdeploy/pull/784
* Report the inference benchmark of models with different size by @lvhan028 in https://github.com/InternLM/lmdeploy/pull/794
* Add chat template for Yi by @AllentDan in https://github.com/InternLM/lmdeploy/pull/779
### 🐞 Bug fixes
* Fix early-exit condition in attention kernel by @lzhangzz in https://github.com/InternLM/lmdeploy/pull/788
* Fix missed arguments when benchmark static inference performance by @lvhan028 in https://github.com/InternLM/lmdeploy/pull/787
* fix extra colon in InternLMChat7B template by @C1rN09 in https://github.com/InternLM/lmdeploy/pull/796
* Fix local kv head num by @lvhan028 in https://github.com/InternLM/lmdeploy/pull/806
### 📚 Documentations
* Update benchmark user guide by @lvhan028 in https://github.com/InternLM/lmdeploy/pull/763
### 🌐 Other
* bump version to v0.1.0a2 by @lvhan028 in https://github.com/InternLM/lmdeploy/pull/807

## New Contributors
* @C1rN09 made their first contribution in https://github.com/InternLM/lmdeploy/pull/796

**Full Changelog**: https://github.com/InternLM/lmdeploy/compare/v0.1.0a1...v0.1.0a2

## v0.1.0 (2023-12-18)

<!-- Release notes generated using configuration in .github/release.yml at main -->

## What's Changed
### 🚀 Features
* Add extra_requires to reduce dependencies by @RunningLeon in https://github.com/InternLM/lmdeploy/pull/580
* TurboMind 2 by @lzhangzz in https://github.com/InternLM/lmdeploy/pull/590
* Support loading hf model directly by @irexyc in https://github.com/InternLM/lmdeploy/pull/685
* convert model with hf repo_id by @irexyc in https://github.com/InternLM/lmdeploy/pull/774
* Support turbomind bf16 by @grimoire in https://github.com/InternLM/lmdeploy/pull/803
* support image_embs input by @irexyc in https://github.com/InternLM/lmdeploy/pull/799
* Add api.py by @AllentDan in https://github.com/InternLM/lmdeploy/pull/805

### 💥 Improvements
* Fix Tokenizer encode by @AllentDan in https://github.com/InternLM/lmdeploy/pull/645
* Optimize for throughput by @lzhangzz in https://github.com/InternLM/lmdeploy/pull/701
* Replace mmengine with mmengine-lite by @zhouzaida in https://github.com/InternLM/lmdeploy/pull/715
* Set the default value of `max_context_token_num` 1 by @lvhan028 in https://github.com/InternLM/lmdeploy/pull/761
* add triton server test and workflow yml by @RunningLeon in https://github.com/InternLM/lmdeploy/pull/760
* improvement(build): enable ninja and gold linker by @tpoisonooo in https://github.com/InternLM/lmdeploy/pull/767
* Report first-token-latency and token-latency percentiles by @lvhan028 in https://github.com/InternLM/lmdeploy/pull/736
* Unify prefill & decode passes by @lzhangzz in https://github.com/InternLM/lmdeploy/pull/775
* add cuda12.1 build check ci by @irexyc in https://github.com/InternLM/lmdeploy/pull/782
* auto upload cuda12.1 python pkg to release when create new tag by @irexyc in https://github.com/InternLM/lmdeploy/pull/784
* Report the inference benchmark of models with different size by @lvhan028 in https://github.com/InternLM/lmdeploy/pull/794
* Simplify block manager by @lzhangzz in https://github.com/InternLM/lmdeploy/pull/812
* Disable attention mask when it is not needed by @lzhangzz in https://github.com/InternLM/lmdeploy/pull/813
* FIFO pipe strategy for api_server by @AllentDan in https://github.com/InternLM/lmdeploy/pull/795
* simplify the header of the benchmark table by @lvhan028 in https://github.com/InternLM/lmdeploy/pull/820
* add encode for opencompass by @AllentDan in https://github.com/InternLM/lmdeploy/pull/828
* fix: awq should save bin files by @hscspring in https://github.com/InternLM/lmdeploy/pull/793
* Support building docker image manually in CI by @RunningLeon in https://github.com/InternLM/lmdeploy/pull/825

### 🐞 Bug fixes
* Fix init of batch state by @lzhangzz in https://github.com/InternLM/lmdeploy/pull/682
* fix turbomind stream canceling by @grimoire in https://github.com/InternLM/lmdeploy/pull/686
* [Fix] Fix load_checkpoint_in_model bug by @HIT-cwh in https://github.com/InternLM/lmdeploy/pull/690
* Fix wrong eos_id and bos_id obtained through grpc api by @lvhan028 in https://github.com/InternLM/lmdeploy/pull/644
* Fix cache/output length calculation by @lzhangzz in https://github.com/InternLM/lmdeploy/pull/738
* [Fix] Skip empty batch by @lzhangzz in https://github.com/InternLM/lmdeploy/pull/747
* [Fix] build docker image failed since `packaging` is missing by @lvhan028 in https://github.com/InternLM/lmdeploy/pull/753
* [Fix] Rollback the data type of `input_ids` to `TYPE_UINT32` in preprocessor's proto by @lvhan028 in https://github.com/InternLM/lmdeploy/pull/758
* fix turbomind build on sm<80 by @grimoire in https://github.com/InternLM/lmdeploy/pull/754
* Fix early-exit condition in attention kernel by @lzhangzz in https://github.com/InternLM/lmdeploy/pull/788
* Fix missed arguments when benchmark static inference performance by @lvhan028 in https://github.com/InternLM/lmdeploy/pull/787
* fix extra colon in InternLMChat7B template by @C1rN09 in https://github.com/InternLM/lmdeploy/pull/796
* Fix local kv head num by @lvhan028 in https://github.com/InternLM/lmdeploy/pull/806
* Fix out-of-bound access by @lzhangzz in https://github.com/InternLM/lmdeploy/pull/809
* Set smem size for repetition penalty kernel by @lzhangzz in https://github.com/InternLM/lmdeploy/pull/818
* Fix cache verification by @lzhangzz in https://github.com/InternLM/lmdeploy/pull/821
* fix finish_reason by @AllentDan in https://github.com/InternLM/lmdeploy/pull/816
* fix turbomind awq by @grimoire in https://github.com/InternLM/lmdeploy/pull/847
* Fix stop requests by await before turbomind queue.get() by @AllentDan in https://github.com/InternLM/lmdeploy/pull/850
* [Fix] Fix meta tensor error by @pppppM in https://github.com/InternLM/lmdeploy/pull/848
* Fix cuda reinitialization in a multiprocessing setting by @grimoire in https://github.com/InternLM/lmdeploy/pull/862
* launch gradio server directly with hf model by @AllentDan in https://github.com/InternLM/lmdeploy/pull/856
* fix typo by @grimoire in https://github.com/InternLM/lmdeploy/pull/769
* Add chat template for Yi by @AllentDan in https://github.com/InternLM/lmdeploy/pull/779
* fix api_server stop_session and end_session by @AllentDan in https://github.com/InternLM/lmdeploy/pull/835
* Return the iterator after erasing it from a map by @irexyc in https://github.com/InternLM/lmdeploy/pull/864

### 📚 Documentations
* [Docs] Update Supported Matrix by @pppppM in https://github.com/InternLM/lmdeploy/pull/679
* [Docs] Update KV8 Docs by @pppppM in https://github.com/InternLM/lmdeploy/pull/681
* [Doc] Update restful api doc by @AllentDan in https://github.com/InternLM/lmdeploy/pull/662
* Check-in user guide about turbomind config by @lvhan028 in https://github.com/InternLM/lmdeploy/pull/680
* Update benchmark user guide by @lvhan028 in https://github.com/InternLM/lmdeploy/pull/763
* [Docs] Fix typo in `restful_api ` user guide by @maxchiron in https://github.com/InternLM/lmdeploy/pull/858
* [Docs] Fix typo in `restful_api ` user guide by @maxchiron in https://github.com/InternLM/lmdeploy/pull/859

### 🌐 Other
* bump version to v0.1.0a0 by @lvhan028 in https://github.com/InternLM/lmdeploy/pull/709
* bump version to 0.1.0a1 by @lvhan028 in https://github.com/InternLM/lmdeploy/pull/776
* bump version to v0.1.0a2 by @lvhan028 in https://github.com/InternLM/lmdeploy/pull/807
* bump version to v0.1.0 by @lvhan028 in https://github.com/InternLM/lmdeploy/pull/834

## New Contributors
* @zhouzaida made their first contribution in https://github.com/InternLM/lmdeploy/pull/715
* @C1rN09 made their first contribution in https://github.com/InternLM/lmdeploy/pull/796
* @maxchiron made their first contribution in https://github.com/InternLM/lmdeploy/pull/858

**Full Changelog**: https://github.com/InternLM/lmdeploy/compare/v0.0.14...v0.1.0

## v0.2.0 (2024-01-17)

<!-- Release notes generated using configuration in .github/release.yml at main -->

## What's Changed
### 🚀 Features
* Support internlm2 by @lvhan028 in https://github.com/InternLM/lmdeploy/pull/963
* [Feature] Add params config for api server web_ui by @amulil in https://github.com/InternLM/lmdeploy/pull/735
* [Feature]Merge `lmdeploy lite calibrate` and `lmdeploy lite auto_awq` by @pppppM in https://github.com/InternLM/lmdeploy/pull/849
* Compute cross entropy loss given a list of input tokens by @lvhan028 in https://github.com/InternLM/lmdeploy/pull/830
* Support QoS in api_server by @sallyjunjun in https://github.com/InternLM/lmdeploy/pull/877
* Refactor torch inference engine by @lvhan028 in https://github.com/InternLM/lmdeploy/pull/871
* add image chat demo by @irexyc in https://github.com/InternLM/lmdeploy/pull/874
* check-in generation config by @lvhan028 in https://github.com/InternLM/lmdeploy/pull/902
* check-in ModelConfig by @AllentDan in https://github.com/InternLM/lmdeploy/pull/907
* pytorch engine config by @grimoire in https://github.com/InternLM/lmdeploy/pull/908
* Check-in turbomind engine config by @irexyc in https://github.com/InternLM/lmdeploy/pull/909
* S-LoRA support by @grimoire in https://github.com/InternLM/lmdeploy/pull/894
* add init in adapters by @grimoire in https://github.com/InternLM/lmdeploy/pull/923
* Refactor LLM inference pipeline API by @AllentDan in https://github.com/InternLM/lmdeploy/pull/916
* Refactor gradio and api_server by @AllentDan in https://github.com/InternLM/lmdeploy/pull/918
* Add request distributor server by @AllentDan in https://github.com/InternLM/lmdeploy/pull/903
* Upgrade lmdeploy cli by @RunningLeon in https://github.com/InternLM/lmdeploy/pull/922

### 💥 Improvements
* add top_k value for /v1/completions and update the documents by @AllentDan in https://github.com/InternLM/lmdeploy/pull/870
* export "num_tokens_per_iter", "max_prefill_iters" and etc when converting a model by @lvhan028 in https://github.com/InternLM/lmdeploy/pull/845
* Move `api_server` dependencies from serve.txt to runtime.txt by @lvhan028 in https://github.com/InternLM/lmdeploy/pull/879
* Refactor benchmark bash script by @lvhan028 in https://github.com/InternLM/lmdeploy/pull/884
* Add test case for function regression by @zhulinJulia24 in https://github.com/InternLM/lmdeploy/pull/844
* Update test triton CI by @RunningLeon in https://github.com/InternLM/lmdeploy/pull/893
* Update dockerfile by @RunningLeon in https://github.com/InternLM/lmdeploy/pull/891
* Perform fuzzy matching on chat template according to model path by @AllentDan in https://github.com/InternLM/lmdeploy/pull/839
* support accessing lmdeploy version by lmdeploy.version_info by @lvhan028 in https://github.com/InternLM/lmdeploy/pull/910
* Remove `flash-attn` dependency of lmdeploy lite module by @lvhan028 in https://github.com/InternLM/lmdeploy/pull/917
* Improve setup by removing pycuda dependency and adding cuda runtime and cublas to RPATH by @irexyc in https://github.com/InternLM/lmdeploy/pull/912
* remove unused settings in turbomind engine config by @irexyc in https://github.com/InternLM/lmdeploy/pull/921
* Cleanup fixed attributes in turbomind engine config by @irexyc in https://github.com/InternLM/lmdeploy/pull/928
* fix get_gpu_mem by @grimoire in https://github.com/InternLM/lmdeploy/pull/934
* remove instance_num argument by @AllentDan in https://github.com/InternLM/lmdeploy/pull/931
* Fix matching results of several chat templates like llama2, solar, yi and so on by @AllentDan in https://github.com/InternLM/lmdeploy/pull/925
* add pytorch random sampling by @grimoire in https://github.com/InternLM/lmdeploy/pull/930
* suppress turbomind chat warning by @irexyc in https://github.com/InternLM/lmdeploy/pull/937
* modify type hint of api to avoid import _turbomind by @AllentDan in https://github.com/InternLM/lmdeploy/pull/936
* accelerate pytorch benchmark by @grimoire in https://github.com/InternLM/lmdeploy/pull/946
* Remove `tp` from pipline argument list by @lvhan028 in https://github.com/InternLM/lmdeploy/pull/947
* set gradio default value the same as chat.py by @AllentDan in https://github.com/InternLM/lmdeploy/pull/949
* print help for cli in case of failure by @RunningLeon in https://github.com/InternLM/lmdeploy/pull/955
* return dataclass for pipeline by @AllentDan in https://github.com/InternLM/lmdeploy/pull/952
* set random seed when it is None by @AllentDan in https://github.com/InternLM/lmdeploy/pull/958
* avoid run get_logger when import lmdeploy by @RunningLeon in https://github.com/InternLM/lmdeploy/pull/956
* support mlp s-lora by @grimoire in https://github.com/InternLM/lmdeploy/pull/957
* skip resume logic for pytorch backend by @AllentDan in https://github.com/InternLM/lmdeploy/pull/968
* Add ci for ut by @RunningLeon in https://github.com/InternLM/lmdeploy/pull/966

### 🐞 Bug fixes
* add tritonclient req by @RunningLeon in https://github.com/InternLM/lmdeploy/pull/872
* Fix uninitialized parameter by @lvhan028 in https://github.com/InternLM/lmdeploy/pull/875
* Fix overflow by @irexyc in https://github.com/InternLM/lmdeploy/pull/897
* Fix data offset by @AllentDan in https://github.com/InternLM/lmdeploy/pull/900
* Fix context decoding stuck issue when tp > 1 by @irexyc in https://github.com/InternLM/lmdeploy/pull/904
* [Fix] set scaling_factor 1 forcefully when sequence length is less than max_pos_emb by @lvhan028 in https://github.com/InternLM/lmdeploy/pull/911
* fix pytorch llama2 with new transformers by @grimoire in https://github.com/InternLM/lmdeploy/pull/914
* fix local variable 'output_ids' referenced before assignment by @irexyc in https://github.com/InternLM/lmdeploy/pull/919
* fix pipeline stop_words type error by @AllentDan in https://github.com/InternLM/lmdeploy/pull/929
* pass stop words to openai api by @AllentDan in https://github.com/InternLM/lmdeploy/pull/887
* fix profile generation multiprocessing error by @AllentDan in https://github.com/InternLM/lmdeploy/pull/933
* Miss __init__.py in modeling folder by @lvhan028 in https://github.com/InternLM/lmdeploy/pull/951
* fix cli with special arg names by @RunningLeon in https://github.com/InternLM/lmdeploy/pull/959
* fix logger in tokenizer by @RunningLeon in https://github.com/InternLM/lmdeploy/pull/960
### 📚 Documentations
* Improve user guide by @lvhan028 in https://github.com/InternLM/lmdeploy/pull/899
* Add user guide about pytorch engine by @grimoire in https://github.com/InternLM/lmdeploy/pull/915
* Update supported models and add quick start section in README by @lvhan028 in https://github.com/InternLM/lmdeploy/pull/926
* Fix scripts in benchmark doc by @panli889 in https://github.com/InternLM/lmdeploy/pull/941
* Update get_started and w4a16 tutorials by @lvhan028 in https://github.com/InternLM/lmdeploy/pull/945
* Add more docstring to api_server and proxy_server by @AllentDan in https://github.com/InternLM/lmdeploy/pull/965
* stable api_server benchmark result by a non-zero await by @AllentDan in https://github.com/InternLM/lmdeploy/pull/885
* fix pytorch backend can not properly stop by @AllentDan in https://github.com/InternLM/lmdeploy/pull/962
* [Fix] Fix `calibrate` bug when `transformers>4.36` by @pppppM in https://github.com/InternLM/lmdeploy/pull/967

### 🌐 Other
* bump version to v0.2.0 by @lvhan028 in https://github.com/InternLM/lmdeploy/pull/969

## New Contributors
* @amulil made their first contribution in https://github.com/InternLM/lmdeploy/pull/735
* @zhulinJulia24 made their first contribution in https://github.com/InternLM/lmdeploy/pull/844
* @sallyjunjun made their first contribution in https://github.com/InternLM/lmdeploy/pull/877
* @panli889 made their first contribution in https://github.com/InternLM/lmdeploy/pull/941

**Full Changelog**: https://github.com/InternLM/lmdeploy/compare/v0.1.0...v0.2.0

## v0.2.1 (2024-01-19)

<!-- Release notes generated using configuration in .github/release.yml at main -->

## What's Changed
### 💥 Improvements
* [Fix] interlm2 chat format by @Harold-lkk in https://github.com/InternLM/lmdeploy/pull/1002
### 🐞 Bug fixes
* fix baichuan2 conversion by @AllentDan in https://github.com/InternLM/lmdeploy/pull/972
* [Fix] interlm messages2prompt by @Harold-lkk in https://github.com/InternLM/lmdeploy/pull/1003
### 📚 Documentations
* add guide about installation on cuda 12+ platform by @lvhan028 in https://github.com/InternLM/lmdeploy/pull/988
### 🌐 Other
* bump version to v0.2.1 by @lvhan028 in https://github.com/InternLM/lmdeploy/pull/1005


**Full Changelog**: https://github.com/InternLM/lmdeploy/compare/v0.2.0...v0.2.1

## v0.2.2 (2024-01-31)

<!-- Release notes generated using configuration in .github/release.yml at main -->

## Highlight
### English version
  * The allocation strategy for k/v cache is changed.  The parameter `cache_max_entry_count` defaults to 0.8. It means the proportion of GPU **FREE** memory rather than **TOTAL** memory. The default value is updated to 0.8. It can help prevent OOM issues.
  * The pipeline API supports streaming inference. You may give it a try!
  ```python
  from lmdeploy import pipeline
  pipe = pipeline('internlm/internlm2-chat-7b')
  for item in pipe.stream_infer('hi, please intro yourself'):
      print(item)
  ```
  * Add api key and ssl to `api_server`
### Chinese version
  * TurboMind engine 修改了GPU memory分配策略。k/v cache 内存比例参数 cache_max_entry_count 缺省值变更为 0.8。它表示 GPU**空闲内存**的比例，不再是 GPU **总内存**的比例。
  * Pipeline 支持流式输出接口。可以尝试下如下代码：
  ```python
  from lmdeploy import pipeline
  pipe = pipeline('internlm/internlm2-chat-7b')
  for item in pipe.stream_infer('hi, please intro yourself'):
      print(item)
  ```
  * api_server 在接口中增加了 api_key


## What's Changed
### 🚀 Features
* add alignment tools by @grimoire in https://github.com/InternLM/lmdeploy/pull/1004
* support min_length for turbomind backend by @irexyc in https://github.com/InternLM/lmdeploy/pull/961
* Add stream mode function to pipeline by @AllentDan in https://github.com/InternLM/lmdeploy/pull/974
* [Feature] Add api key and ssl to http server by @AllentDan in https://github.com/InternLM/lmdeploy/pull/1048

### 💥 Improvements
* hide stop-words in output text by @grimoire in https://github.com/InternLM/lmdeploy/pull/991
* optimize sleep by @grimoire in https://github.com/InternLM/lmdeploy/pull/1034
* set example values to /v1/chat/completions in swagger UI by @AllentDan in https://github.com/InternLM/lmdeploy/pull/984
* Update adapters cli argument by @RunningLeon in https://github.com/InternLM/lmdeploy/pull/1039
* Fix turbomind end session bug. Add huggingface demo document by @AllentDan in https://github.com/InternLM/lmdeploy/pull/1017
* Support linking the custom built mpi by @lvhan028 in https://github.com/InternLM/lmdeploy/pull/1025
* sync mem size for tp by @lzhangzz in https://github.com/InternLM/lmdeploy/pull/1053
* Remove model name when loading hf model by @irexyc in https://github.com/InternLM/lmdeploy/pull/1022
* support internlm2-1_8b by @lvhan028 in https://github.com/InternLM/lmdeploy/pull/1073
* Update chat template for internlm2 base model by @lvhan028 in https://github.com/InternLM/lmdeploy/pull/1079
### 🐞 Bug fixes
* fix TorchEngine stuck when benchmarking with `tp>1` by @grimoire in https://github.com/InternLM/lmdeploy/pull/942
* fix module mapping error of baichuan model by @grimoire in https://github.com/InternLM/lmdeploy/pull/977
* fix import error for triton server by @RunningLeon in https://github.com/InternLM/lmdeploy/pull/985
* fix qwen-vl example by @irexyc in https://github.com/InternLM/lmdeploy/pull/996
* fix missing init file in modules by @RunningLeon in https://github.com/InternLM/lmdeploy/pull/1013
* fix tp mem usage by @grimoire in https://github.com/InternLM/lmdeploy/pull/987
* update indexes_containing_token function by @AllentDan in https://github.com/InternLM/lmdeploy/pull/1050
* fix flash kernel on sm 70 by @grimoire in https://github.com/InternLM/lmdeploy/pull/1027
* Fix baichuan2 lora by @grimoire in https://github.com/InternLM/lmdeploy/pull/1042
* Fix modelconfig in pytorch engine, support YI. by @grimoire in https://github.com/InternLM/lmdeploy/pull/1052
* Fix repetition penalty for long context by @irexyc in https://github.com/InternLM/lmdeploy/pull/1037
* [Fix] Support QLinear in rowwise_parallelize_linear_fn and colwise_parallelize_linear_fn by @HIT-cwh in https://github.com/InternLM/lmdeploy/pull/1072
### 📚 Documentations
* add docs for evaluation with opencompass by @RunningLeon in https://github.com/InternLM/lmdeploy/pull/995
* update docs for kvint8 by @RunningLeon in https://github.com/InternLM/lmdeploy/pull/1026
* [doc] Introduce project OpenAOE by @JiaYingLii in https://github.com/InternLM/lmdeploy/pull/1049
* update pipeline guide and FAQ about OOM by @lvhan028 in https://github.com/InternLM/lmdeploy/pull/1051
* docs update cache_max_entry_count for turbomind config by @zhyncs in https://github.com/InternLM/lmdeploy/pull/1067
### 🌐 Other
* update ut ci to new server node by @RunningLeon in https://github.com/InternLM/lmdeploy/pull/1024
* Ete testcase update by @zhulinJulia24 in https://github.com/InternLM/lmdeploy/pull/1023
* fix OOM in BlockManager by @zhyncs in https://github.com/InternLM/lmdeploy/pull/973
* fix use engine_config.tp when tp is None by @zhyncs in https://github.com/InternLM/lmdeploy/pull/1057
* Fix serve api by moving logger inside process for turbomind by @AllentDan in https://github.com/InternLM/lmdeploy/pull/1061
* bump version to v0.2.2 by @lvhan028 in https://github.com/InternLM/lmdeploy/pull/1076

## New Contributors
* @zhyncs made their first contribution in https://github.com/InternLM/lmdeploy/pull/973
* @JiaYingLii made their first contribution in https://github.com/InternLM/lmdeploy/pull/1049

**Full Changelog**: https://github.com/InternLM/lmdeploy/compare/v0.2.1...v0.2.2

## v0.2.3 (2024-02-06)

<!-- Release notes generated using configuration in .github/release.yml at main -->

## What's Changed
### 🚀 Features
* Support loading model from modelscope by @irexyc in https://github.com/InternLM/lmdeploy/pull/1069
### 💥 Improvements
* Remove caching tokenizer.json by @grimoire in https://github.com/InternLM/lmdeploy/pull/1074
* Refactor `get_logger` to remove the dependency of MMLogger from mmengine by @yinfan98 in https://github.com/InternLM/lmdeploy/pull/1064
* Use TM_LOG_LEVEL environment variable first by @zhyncs in https://github.com/InternLM/lmdeploy/pull/1071
* Speed up the initialization of w8a8 model for torch engine by @yinfan98 in https://github.com/InternLM/lmdeploy/pull/1088
* Make logging.logger's behavior consistent with MMLogger by @irexyc in https://github.com/InternLM/lmdeploy/pull/1092
* Remove owned_session for torch engine by @grimoire in https://github.com/InternLM/lmdeploy/pull/1097
* Unify engine initialization in pipeline by @irexyc in https://github.com/InternLM/lmdeploy/pull/1085
* Add skip_special_tokens in GenerationConfig  by @grimoire in https://github.com/InternLM/lmdeploy/pull/1091
* Use default stop words for turbomind backend in pipeline by @irexyc in https://github.com/InternLM/lmdeploy/pull/1119
* Add input_token_len to Response and update Response document by @AllentDan in https://github.com/InternLM/lmdeploy/pull/1115
### 🐞 Bug fixes
* Fix fast tokenizer swallows prefix space when there are too many white spaces by @AllentDan in https://github.com/InternLM/lmdeploy/pull/992
* Fix turbomind CUDA runtime error invalid argument by @zhyncs in https://github.com/InternLM/lmdeploy/pull/1100
* Add safety check for incremental decode by @AllentDan in https://github.com/InternLM/lmdeploy/pull/1094
* Fix device type of get_ppl for turbomind by @RunningLeon in https://github.com/InternLM/lmdeploy/pull/1093
* Fix pipeline init turbomind from workspace by @irexyc in https://github.com/InternLM/lmdeploy/pull/1126
* Add dependency version check and fix `ignore_eos` logic by @grimoire in https://github.com/InternLM/lmdeploy/pull/1099
* Change configuration_internlm.py to configuration_internlm2.py by @HIT-cwh in https://github.com/InternLM/lmdeploy/pull/1129

### 📚 Documentations
* Update contribution guide by @zhyncs in https://github.com/InternLM/lmdeploy/pull/1120
### 🌐 Other
* Bump version to v0.2.3 by @lvhan028 in https://github.com/InternLM/lmdeploy/pull/1123

## New Contributors
* @yinfan98 made their first contribution in https://github.com/InternLM/lmdeploy/pull/1064

**Full Changelog**: https://github.com/InternLM/lmdeploy/compare/v0.2.2...v0.2.3

## v0.2.4 (2024-02-22)

<!-- Release notes generated using configuration in .github/release.yml at main -->

## What's Changed
### 💥 Improvements
* use stricter rules to get weight file  by @irexyc in https://github.com/InternLM/lmdeploy/pull/1070
* check pytorch engine environment by @grimoire in https://github.com/InternLM/lmdeploy/pull/1107
* Update Dockerfile order to launch the http service by `docker run` directly by @AllentDan in https://github.com/InternLM/lmdeploy/pull/1162
* Support torch cache_max_entry_count by @grimoire in https://github.com/InternLM/lmdeploy/pull/1166
* Remove the manual model conversion during benchmark by @lvhan028 in https://github.com/InternLM/lmdeploy/pull/953
* update llama triton example by @zhyncs in https://github.com/InternLM/lmdeploy/pull/1153
### 🐞 Bug fixes
* fix embedding copy size by @irexyc in https://github.com/InternLM/lmdeploy/pull/1036
* fix pytorch engine with peft==0.8.2 by @grimoire in https://github.com/InternLM/lmdeploy/pull/1122
* support triton2.2 by @grimoire in https://github.com/InternLM/lmdeploy/pull/1137
* Add `top_k` in ChatCompletionRequest by @lvhan028 in https://github.com/InternLM/lmdeploy/pull/1174
* minor fix benchmark generation guide and script by @lvhan028 in https://github.com/InternLM/lmdeploy/pull/1175
### 📚 Documentations
* docs add debug turbomind guide by @zhyncs in https://github.com/InternLM/lmdeploy/pull/1121
### 🌐 Other
* Add eval ci by @RunningLeon in https://github.com/InternLM/lmdeploy/pull/1060
* Ete testcase add more models by @zhulinJulia24 in https://github.com/InternLM/lmdeploy/pull/1077
* Fix win ci by @irexyc in https://github.com/InternLM/lmdeploy/pull/1132
* bump version to v0.2.4 by @lvhan028 in https://github.com/InternLM/lmdeploy/pull/1171


**Full Changelog**: https://github.com/InternLM/lmdeploy/compare/v0.2.3...v0.2.4

## v0.2.5 (2024-03-05)

<!-- Release notes generated using configuration in .github/release.yml at main -->

## What's Changed
### 🚀 Features
* Support mistral and sliding window attention by @grimoire in https://github.com/InternLM/lmdeploy/pull/1075
* torch engine support chatglm3 by @grimoire in https://github.com/InternLM/lmdeploy/pull/1159
* Support qwen1.5 in pytorch engine by @grimoire in https://github.com/InternLM/lmdeploy/pull/1160
* Support mixtral for pytorch engine by @RunningLeon in https://github.com/InternLM/lmdeploy/pull/1133
* Support torch deepseek moe by @grimoire in https://github.com/InternLM/lmdeploy/pull/1163
* Support gemma model in pytorch engine by @grimoire in https://github.com/InternLM/lmdeploy/pull/1184
* Auto backend for pipeline and serve when backend is not set to pytorch explicitly by @RunningLeon in https://github.com/InternLM/lmdeploy/pull/1211
### 💥 Improvements
* Fix argument error by @ispobock in https://github.com/InternLM/lmdeploy/pull/1193
* Use LifoQueue for turbomind async_stream_infer by @AllentDan in https://github.com/InternLM/lmdeploy/pull/1179
* Update interactive output len strategy and response by @AllentDan in https://github.com/InternLM/lmdeploy/pull/1164
* Support `min_new_tokens` generation config in pytorch engine by @grimoire in https://github.com/InternLM/lmdeploy/pull/1096
* Batched sampling by @grimoire in https://github.com/InternLM/lmdeploy/pull/1197
* refactor the logic of getting `model_name` by @AllentDan in https://github.com/InternLM/lmdeploy/pull/1188
* Add parameter `max_prefill_token_num` by @lvhan028 in https://github.com/InternLM/lmdeploy/pull/1203
* optmize baichuan in pytorch engine by @grimoire in https://github.com/InternLM/lmdeploy/pull/1223
* check model required transformers version by @grimoire in https://github.com/InternLM/lmdeploy/pull/1220
* torch optmize chatglm3 by @grimoire in https://github.com/InternLM/lmdeploy/pull/1215
* Async torch engine by @grimoire in https://github.com/InternLM/lmdeploy/pull/1206
* remove unused kernel in pytorch engine by @grimoire in https://github.com/InternLM/lmdeploy/pull/1237
### 🐞 Bug fixes
* Fix session length for profile generation by @ispobock in https://github.com/InternLM/lmdeploy/pull/1181
* fix torch engine infer by @RunningLeon in https://github.com/InternLM/lmdeploy/pull/1185
* fix module map by @grimoire in https://github.com/InternLM/lmdeploy/pull/1205
* [Fix] Correct session length warning by @AllentDan in https://github.com/InternLM/lmdeploy/pull/1207
* Fix all devices occupation when applying tp to torch engine by updating device map by @grimoire in https://github.com/InternLM/lmdeploy/pull/1172
* Fix falcon chatglm2 template by @grimoire in https://github.com/InternLM/lmdeploy/pull/1168
* [Fix] Avoid AsyncEngine running the same session id by @AllentDan in https://github.com/InternLM/lmdeploy/pull/1219
* Fix `None` session_len by @lvhan028 in https://github.com/InternLM/lmdeploy/pull/1230
* fix multinomial sampling by @grimoire in https://github.com/InternLM/lmdeploy/pull/1228
* fix returning logits in prefill phase of pytorch engine by @grimoire in https://github.com/InternLM/lmdeploy/pull/1209
* optimize pytorch engine inference with falcon model by @grimoire in https://github.com/InternLM/lmdeploy/pull/1234
* fix bf16 multinomial sampling by @grimoire in https://github.com/InternLM/lmdeploy/pull/1239
* reduce torchengine prefill mem usage by @grimoire in https://github.com/InternLM/lmdeploy/pull/1240
### 📚 Documentations
* auto generate pipeline api for readthedocs by @RunningLeon in https://github.com/InternLM/lmdeploy/pull/1186
* Added tutorial document for deploying lmdeploy on Jetson series boards.  by @BestAnHongjun in https://github.com/InternLM/lmdeploy/pull/1192
* update doc index by @zhyncs in https://github.com/InternLM/lmdeploy/pull/1241
### 🌐 Other
* Add PR test workflow and check-in more testcases by @zhulinJulia24 in https://github.com/InternLM/lmdeploy/pull/1208
* fix pytest version by @zhulinJulia24 in https://github.com/InternLM/lmdeploy/pull/1236
* bump version to v0.2.5 by @lvhan028 in https://github.com/InternLM/lmdeploy/pull/1235

## New Contributors
* @ispobock made their first contribution in https://github.com/InternLM/lmdeploy/pull/1181
* @BestAnHongjun made their first contribution in https://github.com/InternLM/lmdeploy/pull/1192

**Full Changelog**: https://github.com/InternLM/lmdeploy/compare/v0.2.4...v0.2.5

## v0.2.6 (2024-03-19)

<!-- Release notes generated using configuration in .github/release.yml at main -->
## Highlight

Support vision-languange models (VLM) inference pipeline and serving.
Currently, it supports the following models, [Qwen-VL-Chat](https://huggingface.co/Qwen/Qwen-VL-Chat), LLaVA series [v1.5](https://huggingface.co/collections/liuhaotian/llava-15-653aac15d994e992e2677a7e), [v1.6](https://huggingface.co/collections/liuhaotian/llava-16-65b9e40155f60fd046a5ccf2) and [Yi-VL](https://huggingface.co/01-ai/Yi-VL-6B)

- VLM Inference Pipeline
```python
from lmdeploy import pipeline
from lmdeploy.vl import load_image

pipe = pipeline('liuhaotian/llava-v1.6-vicuna-7b')

image = load_image('https://raw.githubusercontent.com/open-mmlab/mmdeploy/main/tests/data/tiger.jpeg')
response = pipe(('describe this image', image))
print(response)
```
Please refer to the detailed guide from [here](https://lmdeploy.readthedocs.io/en/latest/inference/vl_pipeline.html)

- VLM serving by openai compatible server

```shell
lmdeploy server api_server liuhaotian/llava-v1.6-vicuna-7b --server-port 8000
```

- VLM Serving by gradio

```shell
lmdeploy serve gradio liuhaotian/llava-v1.6-vicuna-7b --server-port 6006
```

## What's Changed
### 🚀 Features
* Add inference pipeline for VL models by @irexyc in https://github.com/InternLM/lmdeploy/pull/1214
* Support serving VLMs by @AllentDan in https://github.com/InternLM/lmdeploy/pull/1285
* Serve VLM by gradio by @irexyc in https://github.com/InternLM/lmdeploy/pull/1293
* Add pipeline.chat api for easy use by @irexyc in https://github.com/InternLM/lmdeploy/pull/1292
### 💥 Improvements
* Hide qos functions from swagger UI if not applied by @AllentDan in https://github.com/InternLM/lmdeploy/pull/1238
* Color log formatter by @grimoire in https://github.com/InternLM/lmdeploy/pull/1247
* optimize filling kv cache kernel in pytorch engine by @grimoire in https://github.com/InternLM/lmdeploy/pull/1251
* Refactor chat template and support accurate name matching. by @AllentDan in https://github.com/InternLM/lmdeploy/pull/1216
* Support passing json file to chat template by @AllentDan in https://github.com/InternLM/lmdeploy/pull/1200
* upgrade peft and check adapters by @grimoire in https://github.com/InternLM/lmdeploy/pull/1284
* better cache allocation in pytorch engine by @grimoire in https://github.com/InternLM/lmdeploy/pull/1272
* Fall back to base template if there is no chat_template in tokenizer_config.json by @AllentDan in https://github.com/InternLM/lmdeploy/pull/1294
### 🐞 Bug fixes
* lazy load convert_pv jit function by @grimoire in https://github.com/InternLM/lmdeploy/pull/1253
* [BUG] fix the case when num_used_blocks < 0  by @jjjjohnson in https://github.com/InternLM/lmdeploy/pull/1277
* Check bf16 model in torch engine by @grimoire in https://github.com/InternLM/lmdeploy/pull/1270
* fix bf16 check by @grimoire in https://github.com/InternLM/lmdeploy/pull/1281
* [Fix] fix triton server chatbot init error by @AllentDan in https://github.com/InternLM/lmdeploy/pull/1278
* Fix concatenate issue in profile serving by @ispobock in https://github.com/InternLM/lmdeploy/pull/1282
* fix torch tp lora adapter by @grimoire in https://github.com/InternLM/lmdeploy/pull/1300
* Fix crash when api_server loads a turbomind model by @irexyc in https://github.com/InternLM/lmdeploy/pull/1304
### 📚 Documentations
* fix config for readthedocs by @RunningLeon in https://github.com/InternLM/lmdeploy/pull/1245
* update badges in README by @lvhan028 in https://github.com/InternLM/lmdeploy/pull/1243
* Update serving guide including api_server and gradio by @lvhan028 in https://github.com/InternLM/lmdeploy/pull/1248
* rename restful_api.md to api_server.md by @lvhan028 in https://github.com/InternLM/lmdeploy/pull/1287
* Update readthedocs index by @lvhan028 in https://github.com/InternLM/lmdeploy/pull/1288
### 🌐 Other
* Parallelize testcase and refactor test workflow by @zhulinJulia24 in https://github.com/InternLM/lmdeploy/pull/1254
* Accelerate sample request in benchmark script by @ispobock in https://github.com/InternLM/lmdeploy/pull/1264
* Update eval ci cfg by @RunningLeon in https://github.com/InternLM/lmdeploy/pull/1259
* Test case bugfix and add restful interface testcases. by @zhulinJulia24 in https://github.com/InternLM/lmdeploy/pull/1271
* bump version to v0.2.6 by @lvhan028 in https://github.com/InternLM/lmdeploy/pull/1299

## New Contributors
* @jjjjohnson made their first contribution in https://github.com/InternLM/lmdeploy/pull/1277

**Full Changelog**: https://github.com/InternLM/lmdeploy/compare/v0.2.5...v0.2.6

## v0.3.0 (2024-04-03)

<!-- Release notes generated using configuration in .github/release.yml at main -->

## Highlight
* Refactor attention and optimize GQA(#1258 #1307 #1116), achieving 22+ and 16+ RPS for internlm2-7b and internlm2-20b, about 1.8x faster than vLLM
* Support new models, including Qwen1.5-MOE(#1372), DBRX(#1367), DeepSeek-VL(#1335)


## What's Changed
### 🚀 Features
* Add tensor core GQA dispatch for `[4,5,6,8]` by @lzhangzz in https://github.com/InternLM/lmdeploy/pull/1258
* upgrade turbomind to v2.1 by by @lzhangzz in https://github.com/InternLM/lmdeploy/pull/1307, https://github.com/InternLM/lmdeploy/pull/1116
* Support slora to pipeline by @AllentDan in https://github.com/InternLM/lmdeploy/pull/1286
* Support qwen for pytorch engine by @RunningLeon in https://github.com/InternLM/lmdeploy/pull/1265
* Support Triton inference server python backend by @ispobock in https://github.com/InternLM/lmdeploy/pull/1329
* torch engine support dbrx by @grimoire in https://github.com/InternLM/lmdeploy/pull/1367
* Support qwen2 moe for pytorch engine by @RunningLeon in https://github.com/InternLM/lmdeploy/pull/1372
* Add deepseek vl by @AllentDan in https://github.com/InternLM/lmdeploy/pull/1335
### 💥 Improvements
* rm unused var by @zhyncs in https://github.com/InternLM/lmdeploy/pull/1256
* Expose cache_block_seq_len to API by @ispobock in https://github.com/InternLM/lmdeploy/pull/1218
* add chat template for deepseek coder model by @lvhan028 in https://github.com/InternLM/lmdeploy/pull/1310
* Add more log info for api_server by @AllentDan in https://github.com/InternLM/lmdeploy/pull/1323
* remove cuda cache after loading vison model by @irexyc in https://github.com/InternLM/lmdeploy/pull/1325
* Add new chat cli with auto backend feature by @RunningLeon in https://github.com/InternLM/lmdeploy/pull/1276
* Update rewritings for qwen by @RunningLeon in https://github.com/InternLM/lmdeploy/pull/1351
* lazy import accelerate.init_empty_weights for vl async engine by @irexyc in https://github.com/InternLM/lmdeploy/pull/1359
* update lmdeploy pypi packages deps to cuda12 by @irexyc in https://github.com/InternLM/lmdeploy/pull/1368
* update `max_prefill_token_num` for low gpu memory by @grimoire in https://github.com/InternLM/lmdeploy/pull/1373
* Optimize pipeline of pytorch engine by @grimoire in https://github.com/InternLM/lmdeploy/pull/1328
### 🐞 Bug fixes
* fix different stop/bad words length in batch by @irexyc in https://github.com/InternLM/lmdeploy/pull/1246
* Fix performance issue of chatbot by @ispobock in https://github.com/InternLM/lmdeploy/pull/1295
* add missed argument by @irexyc in https://github.com/InternLM/lmdeploy/pull/1317
* Fix dlpack memory leak by @ispobock in https://github.com/InternLM/lmdeploy/pull/1344
* Fix invalid context for Internstudio platform by @lzhangzz in https://github.com/InternLM/lmdeploy/pull/1354
* fix benchmark generation by @grimoire in https://github.com/InternLM/lmdeploy/pull/1349
* fix window attention by @grimoire in https://github.com/InternLM/lmdeploy/pull/1341
* fix batchApplyRepetitionPenalty by @irexyc in https://github.com/InternLM/lmdeploy/pull/1358
* Fix memory leak of DLManagedTensor by @ispobock in https://github.com/InternLM/lmdeploy/pull/1361
* fix vlm inference hung with tp by @irexyc in https://github.com/InternLM/lmdeploy/pull/1336
* [Fix] fix the unit test of model name deduce by @AllentDan in https://github.com/InternLM/lmdeploy/pull/1382
### 📚 Documentations
* add citation in readme by @RunningLeon in https://github.com/InternLM/lmdeploy/pull/1308
* Add slora example for pipeline by @AllentDan in https://github.com/InternLM/lmdeploy/pull/1343
### 🌐 Other
* Add restful interface regrssion daily test workflow. by @zhulinJulia24 in https://github.com/InternLM/lmdeploy/pull/1302
* Add offline mode for testcase workflow by @zhulinJulia24 in https://github.com/InternLM/lmdeploy/pull/1318
* workflow bugfix and add llava-v1.5-13b testcase by @zhulinJulia24 in https://github.com/InternLM/lmdeploy/pull/1339
* Add benchmark test workflow by @zhulinJulia24 in https://github.com/InternLM/lmdeploy/pull/1364
* bump version to v0.3.0 by @lvhan028 in https://github.com/InternLM/lmdeploy/pull/1387


**Full Changelog**: https://github.com/InternLM/lmdeploy/compare/v0.2.6...v0.3.0

## v0.4.0 (2024-04-23)

<!-- Release notes generated using configuration in .github/release.yml at main -->

## Highlights

**Support for Llama3 and additional Vision-Language Models (VLMs):**
- We now support Llama3 and an extended range of Vision-Language Models (VLMs), including InternVL versions 1.1 and 1.2, MiniGemini, and InternLMXComposer2.

**Introduce online int4/int8 KV quantization and inference**
- data-free online quantization
- Supports all nvidia GPU models with Volta architecture (sm70) and above
- KV int8 quantization has almost lossless accuracy, and KV int4 quantization accuracy is within an acceptable range
- Efficient inference, with int8/int4 KV quantization applied to llama2-7b, RPS is improved by approximately 30% and 40% respectively compared to fp16

The following table shows the evaluation results of three LLM models with different KV numerical precision:

| -           | -       | -             | llama2-7b-chat | -       | -       | internlm2-chat-7b | -       | -       | qwen1.5-7b-chat | -       | -       |
| ----------- | ------- | ------------- | -------------- | ------- | ------- | ----------------- | ------- | ------- | --------------- | ------- | ------- |
| dataset     | version | metric        | kv fp16        | kv int8 | kv int4 | kv fp16           | kv int8 | kv int4 | fp16            | kv int8 | kv int4 |
| ceval       | -       | naive_average | 28.42          | 27.96   | 27.58   | 60.45             | 60.88   | 60.28   | 70.56           | 70.49   | 68.62   |
| mmlu        | -       | naive_average | 35.64          | 35.58   | 34.79   | 63.91             | 64      | 62.36   | 61.48           | 61.56   | 60.65   |
| triviaqa    | 2121ce  | score         | 56.09          | 56.13   | 53.71   | 58.73             | 58.7    | 58.18   | 44.62           | 44.77   | 44.04   |
| gsm8k       | 1d7fe4  | accuracy      | 28.2           | 28.05   | 27.37   | 70.13             | 69.75   | 66.87   | 54.97           | 56.41   | 54.74   |
| race-middle | 9a54b6  | accuracy      | 41.57          | 41.78   | 41.23   | 88.93             | 88.93   | 88.93   | 87.33           | 87.26   | 86.28   |
| race-high   | 9a54b6  | accuracy      | 39.65          | 39.77   | 40.77   | 85.33             | 85.31   | 84.62   | 82.53           | 82.59   | 82.02   |

The below table presents LMDeploy's inference performance with quantized KV.

| model             | kv type | test settings                            | RPS   | v.s. kv fp16 |
| ----------------- | ------- | ---------------------------------------- | ----- | ------------ |
| llama2-chat-7b    | fp16    | tp1 / ratio 0.8 / bs 256 / prompts 10000 | 14.98 | 1.0          |
| -                 | int8    | tp1 / ratio 0.8 / bs 256 / prompts 10000 | 19.01 | 1.27         |
| -                 | int4    | tp1 / ratio 0.8 / bs 256 / prompts 10000 | 20.81 | 1.39         |
| llama2-chat-13b   | fp16    | tp1 / ratio 0.9 / bs 128 / prompts 10000 | 8.55  | 1.0          |
| -                 | int8    | tp1 / ratio 0.9 / bs 256 / prompts 10000 | 10.96 | 1.28         |
| -                 | int4    | tp1 / ratio 0.9 / bs 256 / prompts 10000 | 11.91 | 1.39         |
| internlm2-chat-7b | fp16    | tp1 / ratio 0.8 / bs 256 / prompts 10000 | 24.13 | 1.0          |
| -                 | int8    | tp1 / ratio 0.8 / bs 256 / prompts 10000 | 25.28 | 1.05         |
| -                 | int4    | tp1 / ratio 0.8 / bs 256 / prompts 10000 | 25.80 | 1.07         |


## What's Changed
### 🚀 Features
* Support qwen1.5 in turbomind engine by @lvhan028 in https://github.com/InternLM/lmdeploy/pull/1406
* Online 8/4-bit KV-cache quantization by @lzhangzz in https://github.com/InternLM/lmdeploy/pull/1377
* Support qwen1.5-*-AWQ model inference in turbomind by @lvhan028 in https://github.com/InternLM/lmdeploy/pull/1430
* support Internvl chat v1.1, v1.2 and v1.2-plus by @irexyc in https://github.com/InternLM/lmdeploy/pull/1425
* support Internvl chat llava by @irexyc in https://github.com/InternLM/lmdeploy/pull/1426
* Add llama3 chat template by @AllentDan in https://github.com/InternLM/lmdeploy/pull/1461
* Support mini gemini llama by @AllentDan in https://github.com/InternLM/lmdeploy/pull/1438
* add interactive api in service for VL models by @AllentDan in https://github.com/InternLM/lmdeploy/pull/1444
* support output logprobs with turbomind backend. by @irexyc in https://github.com/InternLM/lmdeploy/pull/1391
* support internlm-xcomposer2-7b & internlm-xcomposer2-4khd-7b by @irexyc in https://github.com/InternLM/lmdeploy/pull/1458
* Add qwen1.5 awq quantization by @AllentDan in https://github.com/InternLM/lmdeploy/pull/1470
### 💥 Improvements
* Reduce binary size, add `sm_89` and `sm_90` targets by @lzhangzz in https://github.com/InternLM/lmdeploy/pull/1383
* Use new event loop instead of the current loop for pipeline by @AllentDan in https://github.com/InternLM/lmdeploy/pull/1352
* Optimize inference of pytorch engine with tensor parallelism by @grimoire in https://github.com/InternLM/lmdeploy/pull/1397
* add llava-v1.6-34b template by @irexyc in https://github.com/InternLM/lmdeploy/pull/1408
* Initialize vl encoder first to avoid OOM by @AllentDan in https://github.com/InternLM/lmdeploy/pull/1434
* Support model_name  customization for api_server by @AllentDan in https://github.com/InternLM/lmdeploy/pull/1403
* Expose dynamic split&fuse parameters by @lvhan028 in https://github.com/InternLM/lmdeploy/pull/1433
* warning transformers version by @grimoire in https://github.com/InternLM/lmdeploy/pull/1453
* Optimize apply_rotary kernel and remove useless inference_mode by @grimoire in https://github.com/InternLM/lmdeploy/pull/1457
* set infinity timeout to nccl by @grimoire in https://github.com/InternLM/lmdeploy/pull/1465
* Feat: format internlm2 chat template by @liujiangning30 in https://github.com/InternLM/lmdeploy/pull/1456
### 🐞 Bug fixes
* handle SIGTERM by @grimoire in https://github.com/InternLM/lmdeploy/pull/1389
* fix chat cli `ArgumentError` error happened in python 3.11 by @RunningLeon in https://github.com/InternLM/lmdeploy/pull/1401
* Fix llama_triton_example by @AllentDan in https://github.com/InternLM/lmdeploy/pull/1414
* miss --trust-remote-code in converter, which is side effect brought by pr #1406 by @lvhan028 in https://github.com/InternLM/lmdeploy/pull/1420
* fix sampling kernel by @grimoire in https://github.com/InternLM/lmdeploy/pull/1417
* Fix loading single safetensor file error by @AllentDan in https://github.com/InternLM/lmdeploy/pull/1427
* remove space in deepseek template by @grimoire in https://github.com/InternLM/lmdeploy/pull/1441
* fix free repetition_penalty_workspace_ buffer by @irexyc in https://github.com/InternLM/lmdeploy/pull/1467
* fix adapter failure when tp>1 by @grimoire in https://github.com/InternLM/lmdeploy/pull/1476
* get model in advance to fix downloading from modelscope error by @irexyc in https://github.com/InternLM/lmdeploy/pull/1473
* Fix the side effect in engine_intance brought by #1391 by @lvhan028 in https://github.com/InternLM/lmdeploy/pull/1480
### 📚 Documentations
* Add model name corresponding to the test data in the doc by @wykvictor in https://github.com/InternLM/lmdeploy/pull/1400
* fix typo in get_started guide by @lvhan028 in https://github.com/InternLM/lmdeploy/pull/1411
* Add async openai demo for api_server by @AllentDan in https://github.com/InternLM/lmdeploy/pull/1409
* add the recommendation version for Python Backend by @zhyncs in https://github.com/InternLM/lmdeploy/pull/1436
* Update kv quantization and inference guide by @lvhan028 in https://github.com/InternLM/lmdeploy/pull/1412
* update doc for llama3 by @zhyncs in https://github.com/InternLM/lmdeploy/pull/1462
### 🌐 Other
* hack cmakelist.txt in pr_test workflow by @zhulinJulia24 in https://github.com/InternLM/lmdeploy/pull/1405
* Add benchmark report generated in summary by @zhulinJulia24 in https://github.com/InternLM/lmdeploy/pull/1419
* add restful completions v1 test case by @ZhoujhZoe in https://github.com/InternLM/lmdeploy/pull/1416
* Add kvint4/8 ete testcase by @zhulinJulia24 in https://github.com/InternLM/lmdeploy/pull/1448
* impove rotary embedding of qwen in torch engine by @grimoire in https://github.com/InternLM/lmdeploy/pull/1451
* change cutlass url in ut by @RunningLeon in https://github.com/InternLM/lmdeploy/pull/1464
* bump version to v0.4.0 by @lvhan028 in https://github.com/InternLM/lmdeploy/pull/1469

## New Contributors
* @wykvictor made their first contribution in https://github.com/InternLM/lmdeploy/pull/1400
* @ZhoujhZoe made their first contribution in https://github.com/InternLM/lmdeploy/pull/1416
* @liujiangning30 made their first contribution in https://github.com/InternLM/lmdeploy/pull/1456

**Full Changelog**: https://github.com/InternLM/lmdeploy/compare/v0.3.0...v0.4.0

## v0.4.1 (2024-05-07)

<!-- Release notes generated using configuration in .github/release.yml at main -->

## What's Changed
### 🚀 Features
* Add colab demo by @AllentDan in https://github.com/InternLM/lmdeploy/pull/1428
* support starcoder2 by @grimoire in https://github.com/InternLM/lmdeploy/pull/1468
* support OpenGVLab/InternVL-Chat-V1-5 by @irexyc in https://github.com/InternLM/lmdeploy/pull/1490
### 💥 Improvements
* variable `CTA_H` & fix qkv bias by @lzhangzz in https://github.com/InternLM/lmdeploy/pull/1491
* refactor vision model loading by @irexyc in https://github.com/InternLM/lmdeploy/pull/1482
* fix installation requirements for windows by @irexyc in https://github.com/InternLM/lmdeploy/pull/1531
* Remove split batch inside pipline inference function by @AllentDan in https://github.com/InternLM/lmdeploy/pull/1507
* Remove first empty chunck for api_server by @AllentDan in https://github.com/InternLM/lmdeploy/pull/1527
* add benchmark script to profile pipeline APIs by @lvhan028 in https://github.com/InternLM/lmdeploy/pull/1528
* Add input validation by @AllentDan in https://github.com/InternLM/lmdeploy/pull/1525
### 🐞 Bug fixes
* fix local variable 'response' referenced before assignment in async_engine.generate by @irexyc in https://github.com/InternLM/lmdeploy/pull/1513
* Fix turbomind import in windows by @irexyc in https://github.com/InternLM/lmdeploy/pull/1533
* Fix convert qwen2 to turbomind by @AllentDan in https://github.com/InternLM/lmdeploy/pull/1546
* Adding api_key and model_name parameters to the restful benchmark by @NiuBlibing in https://github.com/InternLM/lmdeploy/pull/1478
### 📚 Documentations
* update supported models for Baichuan by @zhyncs in https://github.com/InternLM/lmdeploy/pull/1485
* Fix typo in w8a8.md by @Infinity4B in https://github.com/InternLM/lmdeploy/pull/1523
* complete build.md by @YanxingLiu in https://github.com/InternLM/lmdeploy/pull/1508
* update readme wechat qrcode by @vansin in https://github.com/InternLM/lmdeploy/pull/1529
* Update docker docs for VL api by @vody-am in https://github.com/InternLM/lmdeploy/pull/1534
* Format supported model table using html syntax by @lvhan028 in https://github.com/InternLM/lmdeploy/pull/1493
* doc: add example of deploying api server to Kubernetes by @uzuku in https://github.com/InternLM/lmdeploy/pull/1488
### 🌐 Other
* add modelscope and lora testcase by @zhulinJulia24 in https://github.com/InternLM/lmdeploy/pull/1506
* bump version to v0.4.1 by @lvhan028 in https://github.com/InternLM/lmdeploy/pull/1544

## New Contributors
* @NiuBlibing made their first contribution in https://github.com/InternLM/lmdeploy/pull/1478
* @Infinity4B made their first contribution in https://github.com/InternLM/lmdeploy/pull/1523
* @YanxingLiu made their first contribution in https://github.com/InternLM/lmdeploy/pull/1508
* @vody-am made their first contribution in https://github.com/InternLM/lmdeploy/pull/1534
* @uzuku made their first contribution in https://github.com/InternLM/lmdeploy/pull/1488

**Full Changelog**: https://github.com/InternLM/lmdeploy/compare/v0.4.0...v0.4.1

## v0.4.2 (2024-05-27)

<!-- Release notes generated using configuration in .github/release.yml at main -->
## Highlight

- Support 4-bit weight-only quantization and inference on VMLs, such as InternVL v1.5, LLaVa, InternLMXComposer2

**Quantization**

```python
lmdeploy lite auto_awq OpenGVLab/InternVL-Chat-V1-5 --work-dir ./InternVL-Chat-V1-5-AWQ
```

**Inference with quantized model**

```python
from lmdeploy import pipeline, TurbomindEngineConfig
from lmdeploy.vl import load_image

pipe = pipeline('./InternVL-Chat-V1-5-AWQ', backend_config=TurbomindEngineConfig(tp=1, model_format='awq'))

img = load_image('https://raw.githubusercontent.com/open-mmlab/mmdeploy/main/tests/data/tiger.jpeg')
out = pipe(('describe this image', img))
print(out)
```

- Balance vision model when deploying VLMs with multiple GPUs

```python
from lmdeploy import pipeline, TurbomindEngineConfig
from lmdeploy.vl import load_image

pipe = pipeline('OpenGVLab/InternVL-Chat-V1-5', backend_config=TurbomindEngineConfig(tp=2))

img = load_image('https://raw.githubusercontent.com/open-mmlab/mmdeploy/main/tests/data/tiger.jpeg')
out = pipe(('describe this image', img))
print(out)
```

## What's Changed
### 🚀 Features
* PyTorch Engine hash table based prefix caching by @grimoire in https://github.com/InternLM/lmdeploy/pull/1429
* support phi3 by @grimoire in https://github.com/InternLM/lmdeploy/pull/1497
* Turbomind prefix caching by @ispobock in https://github.com/InternLM/lmdeploy/pull/1450
* Enable search scale for awq by @AllentDan in https://github.com/InternLM/lmdeploy/pull/1545
* [Feature] Support vl models quantization by @AllentDan in https://github.com/InternLM/lmdeploy/pull/1553
### 💥 Improvements
* make Qwen compatible with Slora when TP > 1 by @jjjjohnson in https://github.com/InternLM/lmdeploy/pull/1518
* Optimize slora by @grimoire in https://github.com/InternLM/lmdeploy/pull/1447
* Use a faster format for images in VLMs by @isidentical in https://github.com/InternLM/lmdeploy/pull/1575
* add chat-template args to chat cli by @RunningLeon in https://github.com/InternLM/lmdeploy/pull/1566
* Get the max session len from config.json by @AllentDan in https://github.com/InternLM/lmdeploy/pull/1550
* Optimize w8a8 kernel by @grimoire in https://github.com/InternLM/lmdeploy/pull/1353
* support python 3.12 by @irexyc in https://github.com/InternLM/lmdeploy/pull/1605
* Optimize moe by @grimoire in https://github.com/InternLM/lmdeploy/pull/1520
* Balance vision model weights on multi gpus by @irexyc in https://github.com/InternLM/lmdeploy/pull/1591
* Support user-specified IMAGE_TOKEN position for deepseek-vl model by @irexyc in https://github.com/InternLM/lmdeploy/pull/1627
* Optimize GQA/MQA by @grimoire in https://github.com/InternLM/lmdeploy/pull/1649
### 🐞 Bug fixes
* fix logger init by @AllentDan in https://github.com/InternLM/lmdeploy/pull/1598
* Bugfix: wrongly assign gen_config with True  by @thelongestusernameofall in https://github.com/InternLM/lmdeploy/pull/1594
* Enable split-kv for attention by @lzhangzz in https://github.com/InternLM/lmdeploy/pull/1606
* Fix xcomposer2 vision model process by @irexyc in https://github.com/InternLM/lmdeploy/pull/1640
* Fix NTK scaling by @lzhangzz in https://github.com/InternLM/lmdeploy/pull/1636
* Fix illegal memory access when seq_len < 64 by @lzhangzz in https://github.com/InternLM/lmdeploy/pull/1616
* Fix llava vl template by @irexyc in https://github.com/InternLM/lmdeploy/pull/1620
* [side-effect] fix deepseek-vl when tp is 1 by @irexyc in https://github.com/InternLM/lmdeploy/pull/1648
* fix logprobs output by @irexyc in https://github.com/InternLM/lmdeploy/pull/1561
* fix fused-moe in triton2.2.0 by @grimoire in https://github.com/InternLM/lmdeploy/pull/1654
* Align tokenizers in pipeline and api_server benchmark scripts by @AllentDan in https://github.com/InternLM/lmdeploy/pull/1650
* [side-effect] fix UnboundLocalError for internlm-xcomposer2-4khd-7b by @irexyc in https://github.com/InternLM/lmdeploy/pull/1661
* remove paged attention prefill autotune by @grimoire in https://github.com/InternLM/lmdeploy/pull/1658
* Fix transformers 4.41.0 prompt may differ after encode decode by @AllentDan in https://github.com/InternLM/lmdeploy/pull/1617
### 📚 Documentations
* Fix typo in w8a8.md  by @chg0901 in https://github.com/InternLM/lmdeploy/pull/1568
* Update doc for prefix caching by @ispobock in https://github.com/InternLM/lmdeploy/pull/1597
* Update VL document by @AllentDan in https://github.com/InternLM/lmdeploy/pull/1657
### 🌐 Other
* remove first empty token check and add input validation testcase  by @zhulinJulia24 in https://github.com/InternLM/lmdeploy/pull/1549
* add more model into benchmark and evaluate workflow by @zhulinJulia24 in https://github.com/InternLM/lmdeploy/pull/1565
* add vl awq testcase and refactor pipeline testcase by @zhulinJulia24 in https://github.com/InternLM/lmdeploy/pull/1630
* bump version to v0.4.2 by @lvhan028 in https://github.com/InternLM/lmdeploy/pull/1644

## New Contributors
* @isidentical made their first contribution in https://github.com/InternLM/lmdeploy/pull/1575
* @chg0901 made their first contribution in https://github.com/InternLM/lmdeploy/pull/1568
* @thelongestusernameofall made their first contribution in https://github.com/InternLM/lmdeploy/pull/1594

**Full Changelog**: https://github.com/InternLM/lmdeploy/compare/v0.4.1...v0.4.2

## v0.5.0 (2024-07-01)

<!-- Release notes generated using configuration in .github/release.yml at main -->

## What's Changed
### 🚀 Features
* support MiniCPM-Llama3-V 2.5  by @irexyc in https://github.com/InternLM/lmdeploy/pull/1708
* [Feature]: Support llava for pytorch engine by @RunningLeon in https://github.com/InternLM/lmdeploy/pull/1641
* Device dispatcher by @grimoire in https://github.com/InternLM/lmdeploy/pull/1775
* Add GLM-4-9B-Chat by @lzhangzz in https://github.com/InternLM/lmdeploy/pull/1724
* Torch deepseek v2 by @grimoire in https://github.com/InternLM/lmdeploy/pull/1621
* Support internvl-chat for pytorch engine by @RunningLeon in https://github.com/InternLM/lmdeploy/pull/1797
* Add interfaces to the pipeline to obtain logits and ppl by @irexyc in https://github.com/InternLM/lmdeploy/pull/1652
* [Feature]: Support cogvlm-chat by @RunningLeon in https://github.com/InternLM/lmdeploy/pull/1502
### 💥 Improvements
* support mistral and llava_mistral in turbomind by @lvhan028 in https://github.com/InternLM/lmdeploy/pull/1579
* Add health endpoint by @AllentDan in https://github.com/InternLM/lmdeploy/pull/1679
* upgrade the version of the dependency package peft by @grimoire in https://github.com/InternLM/lmdeploy/pull/1687
* Follow the conventional model_name by @AllentDan in https://github.com/InternLM/lmdeploy/pull/1677
* API Image URL fetch timeout  by @vody-am in https://github.com/InternLM/lmdeploy/pull/1684
* Support internlm-xcomposer2-4khd-7b awq by @AllentDan in https://github.com/InternLM/lmdeploy/pull/1666
* update dockerfile and docs by @RunningLeon in https://github.com/InternLM/lmdeploy/pull/1715
* lazy import VLAsyncEngine to avoid bringing in VLMs dependencies when deploying LLMs by @lvhan028 in https://github.com/InternLM/lmdeploy/pull/1714
* feat: align with OpenAI temperature range by @zhyncs in https://github.com/InternLM/lmdeploy/pull/1733
* feat: align with OpenAI temperature range in api server by @zhyncs in https://github.com/InternLM/lmdeploy/pull/1734
* Refactor converter about get_input_model_registered_name and get_output_model_registered_name_and_config by @lvhan028 in https://github.com/InternLM/lmdeploy/pull/1702
* Refine max_new_tokens logic to improve user experience by @AllentDan in https://github.com/InternLM/lmdeploy/pull/1705
* Refactor loading weights by @grimoire in https://github.com/InternLM/lmdeploy/pull/1603
* refactor config by @grimoire in https://github.com/InternLM/lmdeploy/pull/1751
* Add anomaly handler by @lzhangzz in https://github.com/InternLM/lmdeploy/pull/1780
* Encode raw image file to base64 by @irexyc in https://github.com/InternLM/lmdeploy/pull/1773
* skip inference for oversized inputs by @grimoire in https://github.com/InternLM/lmdeploy/pull/1769
* fix: prevent numpy breakage by @zhyncs in https://github.com/InternLM/lmdeploy/pull/1791
* More accurate time logging for ImageEncoder and fix concurrent image processing corruption by @irexyc in https://github.com/InternLM/lmdeploy/pull/1765
* Optimize kernel launch for triton2.2.0 and triton2.3.0 by @grimoire in https://github.com/InternLM/lmdeploy/pull/1499
* feat: auto set awq model_format from hf by @zhyncs in https://github.com/InternLM/lmdeploy/pull/1799
* check driver mismatch by @grimoire in https://github.com/InternLM/lmdeploy/pull/1811
* PyTorchEngine adapts to the latest internlm2 modeling. by @grimoire in https://github.com/InternLM/lmdeploy/pull/1798
* AsyncEngine create cancel task in exception. by @grimoire in https://github.com/InternLM/lmdeploy/pull/1807
* compat internlm2 for pytorch engine by @RunningLeon in https://github.com/InternLM/lmdeploy/pull/1825
* Add model revision & download_dir to cli by @irexyc in https://github.com/InternLM/lmdeploy/pull/1814
* fix image encoder request queue  by @irexyc in https://github.com/InternLM/lmdeploy/pull/1837
* Harden stream callback by @lzhangzz in https://github.com/InternLM/lmdeploy/pull/1838
* Support Qwen2-1.5b awq by @AllentDan in https://github.com/InternLM/lmdeploy/pull/1793
* remove chat template config in turbomind engine by @irexyc in https://github.com/InternLM/lmdeploy/pull/1161
* misc: align PyTorch Engine temprature with TurboMind by @zhyncs in https://github.com/InternLM/lmdeploy/pull/1850
* docs: update cache-max-entry-count help message by @zhyncs in https://github.com/InternLM/lmdeploy/pull/1892
### 🐞 Bug fixes
* fix typos by @irexyc in https://github.com/InternLM/lmdeploy/pull/1690
* [Bugfix] fix internvl-1.5-chat vision model preprocess and freeze weights by @DefTruth in https://github.com/InternLM/lmdeploy/pull/1741
* lock setuptools version in dockerfile by @RunningLeon in https://github.com/InternLM/lmdeploy/pull/1770
* Fix openai package can not use proxy stream mode by @AllentDan in https://github.com/InternLM/lmdeploy/pull/1692
* Fix finish_reason by @AllentDan in https://github.com/InternLM/lmdeploy/pull/1768
* fix uncached stop words by @grimoire in https://github.com/InternLM/lmdeploy/pull/1754
* [side-effect]Fix param `--cache-max-entry-count` is not taking effect (#1758) by @QwertyJack in https://github.com/InternLM/lmdeploy/pull/1778
* support qwen2 1.5b by @lvhan028 in https://github.com/InternLM/lmdeploy/pull/1782
* fix falcon attention by @grimoire in https://github.com/InternLM/lmdeploy/pull/1761
* Refine AsyncEngine exception handler by @AllentDan in https://github.com/InternLM/lmdeploy/pull/1789
* [side-effect] fix weight_type caused by PR #1702 by @lvhan028 in https://github.com/InternLM/lmdeploy/pull/1795
* fix best_match_model by @irexyc in https://github.com/InternLM/lmdeploy/pull/1812
* Fix Request completed log by @irexyc in https://github.com/InternLM/lmdeploy/pull/1821
* fix qwen-vl-chat hung by @irexyc in https://github.com/InternLM/lmdeploy/pull/1824
* Detokenize with prompt token ids by @AllentDan in https://github.com/InternLM/lmdeploy/pull/1753
* Update engine.py to fix small typos by @WANGSSSSSSS in https://github.com/InternLM/lmdeploy/pull/1829
* [side-effect] bring back "--cap" argument in chat cli by @lvhan028 in https://github.com/InternLM/lmdeploy/pull/1859
* Fix vl session-len by @AllentDan in https://github.com/InternLM/lmdeploy/pull/1860
* fix gradio vl "stop_words" by @irexyc in https://github.com/InternLM/lmdeploy/pull/1873
* fix qwen2 cache_position for PyTorch Engine when transformers>4.41.2 by @zhyncs in https://github.com/InternLM/lmdeploy/pull/1886
* fix model name matching for internvl by @RunningLeon in https://github.com/InternLM/lmdeploy/pull/1867
### 📚 Documentations
* docs: add BentoLMDeploy in README by @zhyncs in https://github.com/InternLM/lmdeploy/pull/1736
* [Doc]: Update docs for internlm2.5 by @RunningLeon in https://github.com/InternLM/lmdeploy/pull/1887
### 🌐 Other
* add longtext generation benchmark by @zhulinJulia24 in https://github.com/InternLM/lmdeploy/pull/1694
* add qwen2 model into testcase by @zhulinJulia24 in https://github.com/InternLM/lmdeploy/pull/1772
* fix pr test for newest internlm2 model by @zhulinJulia24 in https://github.com/InternLM/lmdeploy/pull/1806
* react test evaluation config by @zhulinJulia24 in https://github.com/InternLM/lmdeploy/pull/1861
* bump version to v0.5.0 by @lvhan028 in https://github.com/InternLM/lmdeploy/pull/1852

## New Contributors
* @DefTruth made their first contribution in https://github.com/InternLM/lmdeploy/pull/1741
* @QwertyJack made their first contribution in https://github.com/InternLM/lmdeploy/pull/1778
* @WANGSSSSSSS made their first contribution in https://github.com/InternLM/lmdeploy/pull/1829

**Full Changelog**: https://github.com/InternLM/lmdeploy/compare/v0.4.2...v0.5.0

## v0.5.1 (2024-07-16)

<!-- Release notes generated using configuration in .github/release.yml at main -->

## What's Changed
### 🚀 Features
* Support phi3-vision by @RunningLeon in https://github.com/InternLM/lmdeploy/pull/1845
* Support internvl2 chat template by @AllentDan in https://github.com/InternLM/lmdeploy/pull/1911
* support gemma2 in pytorch engine by @grimoire in https://github.com/InternLM/lmdeploy/pull/1924
* Add tools to api_server for InternLM2 model by @AllentDan in https://github.com/InternLM/lmdeploy/pull/1763
* support internvl2-1b by @RunningLeon in https://github.com/InternLM/lmdeploy/pull/1983
* feat: support llama2 and internlm2 on 910B by @yao-fengchen in https://github.com/InternLM/lmdeploy/pull/2011
* Support glm 4v by @RunningLeon in https://github.com/InternLM/lmdeploy/pull/1947
* support internlm-xcomposer2d5-7b by @irexyc in https://github.com/InternLM/lmdeploy/pull/1932
* add chat template for codegeex4 by @RunningLeon in https://github.com/InternLM/lmdeploy/pull/2013
### 💥 Improvements
* misc: rm unnecessary files by @zhyncs in https://github.com/InternLM/lmdeploy/pull/1875
* drop stop words by @grimoire in https://github.com/InternLM/lmdeploy/pull/1823
* Add usage in stream response by @fbzhong in https://github.com/InternLM/lmdeploy/pull/1876
* Optimize sampling on pytorch engine. by @grimoire in https://github.com/InternLM/lmdeploy/pull/1853
* Remove deprecated chat cli and vl examples by @lvhan028 in https://github.com/InternLM/lmdeploy/pull/1899
* vision model use tp number of gpu by @irexyc in https://github.com/InternLM/lmdeploy/pull/1854
* misc: add default api_server_url for api_client by @zhyncs in https://github.com/InternLM/lmdeploy/pull/1922
* misc: add transformers version check for TurboMind Tokenizer by @zhyncs in https://github.com/InternLM/lmdeploy/pull/1917
* fix: append _stats when size > 0 by @zhyncs in https://github.com/InternLM/lmdeploy/pull/1809
* refactor: update awq linear and rm legacy by @zhyncs in https://github.com/InternLM/lmdeploy/pull/1940
* feat: add gpu topo for check_env by @zhyncs in https://github.com/InternLM/lmdeploy/pull/1944
* fix transformers version check for InternVL2 by @zhyncs in https://github.com/InternLM/lmdeploy/pull/1952
* Upgrade gradio by @AllentDan in https://github.com/InternLM/lmdeploy/pull/1930
* refactor sampling layer setup by @irexyc in https://github.com/InternLM/lmdeploy/pull/1912
* Add exception handler to imge encoder by @irexyc in https://github.com/InternLM/lmdeploy/pull/2010
* Avoid the same session id for openai endpoint by @AllentDan in https://github.com/InternLM/lmdeploy/pull/1995
### 🐞 Bug fixes
* Fix error link reference by @zihaomu in https://github.com/InternLM/lmdeploy/pull/1881
* Fix internlm-xcomposer2-vl awq search scale by @AllentDan in https://github.com/InternLM/lmdeploy/pull/1890
* fix SamplingDecodeTest and SamplingDecodeTest2 unittest failure by @zhyncs in https://github.com/InternLM/lmdeploy/pull/1874
* Fix smem size for fused split-kv reduction by @lzhangzz in https://github.com/InternLM/lmdeploy/pull/1909
* fix llama3 chat template by @AllentDan in https://github.com/InternLM/lmdeploy/pull/1956
* fix: set PYTHONIOENCODING to UTF-8 before start tritonserver by @zhyncs in https://github.com/InternLM/lmdeploy/pull/1971
* Fix internvl2-40b model export by @irexyc in https://github.com/InternLM/lmdeploy/pull/1979
* fix logprobs by @irexyc in https://github.com/InternLM/lmdeploy/pull/1968
* fix unexpected argument error when deploying "cogvlm-chat-hf" by @AllentDan in https://github.com/InternLM/lmdeploy/pull/1982
* fix mixtral and mistral cache_position by @zhyncs in https://github.com/InternLM/lmdeploy/pull/1941
* Fix the session_len assignment logic by @lvhan028 in https://github.com/InternLM/lmdeploy/pull/2007
* Fix logprobs openai api by @irexyc in https://github.com/InternLM/lmdeploy/pull/1985
* Fix internvl2-40b awq inference by @AllentDan in https://github.com/InternLM/lmdeploy/pull/2023
* Fix side effect of #1995 by @AllentDan in https://github.com/InternLM/lmdeploy/pull/2033
### 📚 Documentations
* docs: update faq for turbomind so not found by @zhyncs in https://github.com/InternLM/lmdeploy/pull/1877
* [Doc]: Change to sphinx-book-theme in readthedocs by @RunningLeon in https://github.com/InternLM/lmdeploy/pull/1880
* docs: update compatibility section in README by @zhyncs in https://github.com/InternLM/lmdeploy/pull/1946
* docs: update kv quant doc by @zhyncs in https://github.com/InternLM/lmdeploy/pull/1977
* docs: sync the core features in README to index.rst by @zhyncs in https://github.com/InternLM/lmdeploy/pull/1988
* Fix table rendering for readthedocs by @RunningLeon in https://github.com/InternLM/lmdeploy/pull/1998
* docs: fix Ada compatibility by @zhyncs in https://github.com/InternLM/lmdeploy/pull/2016
* update xcomposer2d5 docs by @irexyc in https://github.com/InternLM/lmdeploy/pull/2037
### 🌐 Other
* [ci] add internlm2.5 models into testcase by @zhulinJulia24 in https://github.com/InternLM/lmdeploy/pull/1928
* bump version to v0.5.1 by @lvhan028 in https://github.com/InternLM/lmdeploy/pull/2022

## New Contributors
* @zihaomu made their first contribution in https://github.com/InternLM/lmdeploy/pull/1881
* @fbzhong made their first contribution in https://github.com/InternLM/lmdeploy/pull/1876

**Full Changelog**: https://github.com/InternLM/lmdeploy/compare/v0.5.0...v0.5.1

## v0.5.2 (2024-07-26)

<!-- Release notes generated using configuration in .github/release.yml at main -->

## Highlight

- LMDeploy support Llama3.1 and its **Tool Calling**. An example of calling "Wolfram Alpha" to  perform complex mathematical calculations can be found from [here](https://github.com/InternLM/lmdeploy/blob/main/docs/en/serving/api_server_tools.md)

## What's Changed
### 🚀 Features
* Support glm4 awq by @AllentDan in https://github.com/InternLM/lmdeploy/pull/1993
* Support llama3.1 by @lvhan028 in https://github.com/InternLM/lmdeploy/pull/2122
* Support Llama3.1 tool calling by @AllentDan in https://github.com/InternLM/lmdeploy/pull/2123
### 💥 Improvements
* Remove the triton inference server backend "turbomind_backend" by @lvhan028 in https://github.com/InternLM/lmdeploy/pull/1986
* Remove kv cache offline quantization by @AllentDan in https://github.com/InternLM/lmdeploy/pull/2097
* Remove `session_len` and deprecated short names of the chat templates by @lvhan028 in https://github.com/InternLM/lmdeploy/pull/2105
* clarify "n>1" in GenerationConfig hasn't been supported yet by @lvhan028 in https://github.com/InternLM/lmdeploy/pull/2108
### 🐞 Bug fixes
* fix stop words for glm4 by @RunningLeon in https://github.com/InternLM/lmdeploy/pull/2044
* Disable peer access code by @lzhangzz in https://github.com/InternLM/lmdeploy/pull/2082
* set log level ERROR in benchmark scripts by @lvhan028 in https://github.com/InternLM/lmdeploy/pull/2086
* raise thread exception by @irexyc in https://github.com/InternLM/lmdeploy/pull/2071
* Fix index error when profiling token generation with `-ct 1`  by @lvhan028 in https://github.com/InternLM/lmdeploy/pull/1898
### 🌐 Other
* misc: replace slow Jimver/cuda-toolkit by @zhyncs in https://github.com/InternLM/lmdeploy/pull/2065
* misc: update bug issue template by @zhyncs in https://github.com/InternLM/lmdeploy/pull/2083
* update daily testcase new by @zhulinJulia24 in https://github.com/InternLM/lmdeploy/pull/2035
* bump version to v0.5.2 by @lvhan028 in https://github.com/InternLM/lmdeploy/pull/2143


**Full Changelog**: https://github.com/InternLM/lmdeploy/compare/v0.5.1...v0.5.2

## v0.5.2.post1 (2024-07-26)

<!-- Release notes generated using configuration in .github/release.yml at main -->

## What's Changed
### 🐞 Bug fixes
* [Hotfix] miss parentheses when calcuating the coef of llama3 rope which causes needle-in-hays experiment failed by @lvhan028 in https://github.com/InternLM/lmdeploy/pull/2157
### 🌐 Other
* bump version to 0.5.2.post1 by @lvhan028 in https://github.com/InternLM/lmdeploy/pull/2159


**Full Changelog**: https://github.com/InternLM/lmdeploy/compare/v0.5.2...v0.5.2.post1

## v0.5.3 (2024-08-07)

<!-- Release notes generated using configuration in .github/release.yml at main -->

## What's Changed
### 🚀 Features
* PyTorch Engine AWQ support by @grimoire in https://github.com/InternLM/lmdeploy/pull/1913
* Phi3 awq by @grimoire in https://github.com/InternLM/lmdeploy/pull/1984
* Fix chunked prefill by @lzhangzz in https://github.com/InternLM/lmdeploy/pull/2201
* support VLMs with Qwen as the language model by @irexyc in https://github.com/InternLM/lmdeploy/pull/2207
### 💥 Improvements
* Support specifying a prefix of assistant response by @AllentDan in https://github.com/InternLM/lmdeploy/pull/2172
* Strict check for `name_map` in `InternLM2Chat7B` by @SamuraiBUPT in https://github.com/InternLM/lmdeploy/pull/2156
* Check errors for attention kernels by @lzhangzz in https://github.com/InternLM/lmdeploy/pull/2206
* update base image to support cuda12.4 in dockerfile by @RunningLeon in https://github.com/InternLM/lmdeploy/pull/2182
* Stop synchronizing for `length_criterion` by @lzhangzz in https://github.com/InternLM/lmdeploy/pull/2202
* adapt MiniCPM-Llama3-V-2_5 new code by @irexyc in https://github.com/InternLM/lmdeploy/pull/2139
* Remove duplicate code by @cmpute in https://github.com/InternLM/lmdeploy/pull/2133
### 🐞 Bug fixes
* [Hotfix] miss parentheses when calcuating the coef of llama3 rope by @lvhan028 in https://github.com/InternLM/lmdeploy/pull/2157
* support logit softcap by @grimoire in https://github.com/InternLM/lmdeploy/pull/2158
* Fix gmem to smem WAW conflict in awq gemm kernel by @foreverrookie in https://github.com/InternLM/lmdeploy/pull/2111
* Fix gradio serve using a wrong chat template by @AllentDan in https://github.com/InternLM/lmdeploy/pull/2131
* fix runtime error when using dynamic scale rotary embed for InternLM2… by @CyCle1024 in https://github.com/InternLM/lmdeploy/pull/2212
* Add peer-access-enabled allocator by @lzhangzz in https://github.com/InternLM/lmdeploy/pull/2218
* Fix typos in profile_generation.py by @jiajie-yang in https://github.com/InternLM/lmdeploy/pull/2233
### 📚 Documentations
* docs: fix Qwen typo by @ArtificialZeng in https://github.com/InternLM/lmdeploy/pull/2136
* wrong expression by @ArtificialZeng in https://github.com/InternLM/lmdeploy/pull/2165
* clearify the model type LLM or MLLM in supported model matrix by @lvhan028 in https://github.com/InternLM/lmdeploy/pull/2209
* docs: add Japanese README by @eltociear in https://github.com/InternLM/lmdeploy/pull/2237
### 🌐 Other
* bump version to 0.5.2.post1 by @lvhan028 in https://github.com/InternLM/lmdeploy/pull/2159
* update news about cooperation with modelscope/swift by @lvhan028 in https://github.com/InternLM/lmdeploy/pull/2200
* bump version to v0.5.3 by @lvhan028 in https://github.com/InternLM/lmdeploy/pull/2242

## New Contributors
* @ArtificialZeng made their first contribution in https://github.com/InternLM/lmdeploy/pull/2136
* @foreverrookie made their first contribution in https://github.com/InternLM/lmdeploy/pull/2111
* @SamuraiBUPT made their first contribution in https://github.com/InternLM/lmdeploy/pull/2156
* @CyCle1024 made their first contribution in https://github.com/InternLM/lmdeploy/pull/2212
* @jiajie-yang made their first contribution in https://github.com/InternLM/lmdeploy/pull/2233
* @cmpute made their first contribution in https://github.com/InternLM/lmdeploy/pull/2133

**Full Changelog**: https://github.com/InternLM/lmdeploy/compare/v0.5.2...v0.5.3

## v0.6.0a0 (2024-08-26)

<!-- Release notes generated using configuration in .github/release.yml at main -->
## Highlight
- Optimize W4A16 quantized model inference by implementing GEMM in TurboMind Engine
  - Add GPTQ-INT4 inference 
  - Support CUDA architecture from SM70 and above, equivalent to the V100 and above.
- Optimize the prefilling inference stage of PyTorchEngine
- Distinguish between the concepts of the name of the deployed model and the name of the model's chat tempate

Before:
```shell
lmdeploy serve api_server /the/path/of/your/awesome/model \
    --model-name customized_chat_template.json 
```
After
```shell
lmdeploy serve api_server  /the/path/of/your/awesome/model \
    --model-name "the served model name"
    --chat-template customized_chat_template.json
```

## What's Changed
### 🚀 Features
* support vlm custom image process parameters in openai input format by @irexyc in https://github.com/InternLM/lmdeploy/pull/2245
* New GEMM kernels for weight-only quantization by @lzhangzz in https://github.com/InternLM/lmdeploy/pull/2090
* Fix hidden size and support mistral nemo by @AllentDan in https://github.com/InternLM/lmdeploy/pull/2215
* Support custom logits processors by @AllentDan in https://github.com/InternLM/lmdeploy/pull/2329
* support openbmb/MiniCPM-V-2_6 by @irexyc in https://github.com/InternLM/lmdeploy/pull/2351
* Support phi3.5 for pytorch engine by @RunningLeon in https://github.com/InternLM/lmdeploy/pull/2361
### 💥 Improvements
* Remove deprecated arguments from API and clarify model_name and chat_template_name by @lvhan028 in https://github.com/InternLM/lmdeploy/pull/1931
* Fix duplicated session_id when pipeline is used by multithreads by @irexyc in https://github.com/InternLM/lmdeploy/pull/2134
* remove eviction param by @grimoire in https://github.com/InternLM/lmdeploy/pull/2285
* Remove QoS serving by @AllentDan in https://github.com/InternLM/lmdeploy/pull/2294
* Support send tool_calls back to internlm2 by @AllentDan in https://github.com/InternLM/lmdeploy/pull/2147
* Add stream options to control usage by @AllentDan in https://github.com/InternLM/lmdeploy/pull/2313
* add device type for pytorch engine in cli by @RunningLeon in https://github.com/InternLM/lmdeploy/pull/2321
* Update error status_code to raise error in openai client by @AllentDan in https://github.com/InternLM/lmdeploy/pull/2333
* Change to use device instead of device-type in cli by @RunningLeon in https://github.com/InternLM/lmdeploy/pull/2337
* Add GEMM test utils by @lzhangzz in https://github.com/InternLM/lmdeploy/pull/2342
* Add environment variable to control SILU fusion by @lzhangzz in https://github.com/InternLM/lmdeploy/pull/2343
* Use single thread per model instance by @lzhangzz in https://github.com/InternLM/lmdeploy/pull/2339
* add cache to speed up docker building by @RunningLeon in https://github.com/InternLM/lmdeploy/pull/2344
* add max_prefill_token_num argument in CLI by @lvhan028 in https://github.com/InternLM/lmdeploy/pull/2345
* torch engine optimize prefill for long context by @grimoire in https://github.com/InternLM/lmdeploy/pull/1962
* Refactor turbomind (1/N) by @lzhangzz in https://github.com/InternLM/lmdeploy/pull/2352
* feat(server): enable `seed` parameter for openai compatible server. by @DearPlanet in https://github.com/InternLM/lmdeploy/pull/2353
### 🐞 Bug fixes
* enable run vlm with pytorch engine in gradio by @RunningLeon in https://github.com/InternLM/lmdeploy/pull/2256
* fix side-effect: failed to update tm model config with tm engine config by @lvhan028 in https://github.com/InternLM/lmdeploy/pull/2275
* Fix internvl2 template and update docs by @irexyc in https://github.com/InternLM/lmdeploy/pull/2292
* fix the issue missing dependencies in the Dockerfile and pip by @ColorfulDick in https://github.com/InternLM/lmdeploy/pull/2240
* Fix the way to get "quantization_config" from model's coniguration by @lvhan028 in https://github.com/InternLM/lmdeploy/pull/2325
* fix(ascend): fix import error of pt engine in cli by @CyCle1024 in https://github.com/InternLM/lmdeploy/pull/2328
* Default rope_scaling_factor of TurbomindEngineConfig to None by @lvhan028 in https://github.com/InternLM/lmdeploy/pull/2358
* Fix the logic of update engine_config to TurbomindModelConfig for both tm model and hf model by @lvhan028 in https://github.com/InternLM/lmdeploy/pull/2362
### 📚 Documentations
* Reorganize the user guide and update the get_started section by @lvhan028 in https://github.com/InternLM/lmdeploy/pull/2038
* cancel support baichuan2 7b awq in pytorch engine by @grimoire in https://github.com/InternLM/lmdeploy/pull/2246
* Add user guide about slora serving  by @AllentDan in https://github.com/InternLM/lmdeploy/pull/2084
### 🌐 Other
* test prtest image update by @zhulinJulia24 in https://github.com/InternLM/lmdeploy/pull/2192
* Update python support version  by @wuhongsheng in https://github.com/InternLM/lmdeploy/pull/2290
* fix Windows compile error by @zhyncs in https://github.com/InternLM/lmdeploy/pull/2303
* fix: follow up #2303 by @zhyncs in https://github.com/InternLM/lmdeploy/pull/2307
* [ci] benchmark react by @zhulinJulia24 in https://github.com/InternLM/lmdeploy/pull/2183
* bump version to v0.6.0a0 by @lvhan028 in https://github.com/InternLM/lmdeploy/pull/2371

## New Contributors
* @wuhongsheng made their first contribution in https://github.com/InternLM/lmdeploy/pull/2290
* @ColorfulDick made their first contribution in https://github.com/InternLM/lmdeploy/pull/2240
* @DearPlanet made their first contribution in https://github.com/InternLM/lmdeploy/pull/2353

**Full Changelog**: https://github.com/InternLM/lmdeploy/compare/v0.5.3...v0.6.0a0

## v0.6.0 (2024-09-13)

<!-- Release notes generated using configuration in .github/release.yml at main -->
## Highlight
- Optimize W4A16 quantized model inference by implementing GEMM in TurboMind Engine
  - Add GPTQ-INT4 inference
  - Support CUDA architecture from SM70 and above, equivalent to the V100 and above.
- Refactor PytorchEngine
  - Employ CUDA graph to boost the inference performance (30%)
  - Support more models in Huawei Ascend platform
- Upgrade `GenerationConfig`
  - Support `min_p` sampling
  - Add `do_sample=False` as the default option
  - Remove `EngineGenerationConfig` and merge it to `GenertionConfig`
- Support guided decoding
- Distinguish between the concepts of the name of the deployed model and the name of the model's chat tempate
Before:
```
lmdeploy serve api_server /the/path/of/your/awesome/model \
    --model-name customized_chat_template.json
```
After
```
lmdeploy serve api_server  /the/path/of/your/awesome/model \
    --model-name "the served model name"
    --chat-template customized_chat_template.json
```

## Break Changes
- TurboMind model converter. Please re-convert the models if you uses this feature
- `EngineGenerationConfig` is removed. Please use `GenerationConfig` instead
- Chat template. Please use `--chat-template` to specify it

## What's Changed
### 🚀 Features
* support vlm custom image process parameters in openai input format by @irexyc in https://github.com/InternLM/lmdeploy/pull/2245
* New GEMM kernels for weight-only quantization by @lzhangzz in https://github.com/InternLM/lmdeploy/pull/2090
* Fix hidden size and support mistral nemo by @AllentDan in https://github.com/InternLM/lmdeploy/pull/2215
* Support custom logits processors by @AllentDan in https://github.com/InternLM/lmdeploy/pull/2329
* support openbmb/MiniCPM-V-2_6 by @irexyc in https://github.com/InternLM/lmdeploy/pull/2351
* Support phi3.5 for pytorch engine by @RunningLeon in https://github.com/InternLM/lmdeploy/pull/2361
* Add auto_gptq to lmdeploy lite by @AllentDan in https://github.com/InternLM/lmdeploy/pull/2372
* build(ascend): add Dockerfile for ascend aarch64 910B by @CyCle1024 in https://github.com/InternLM/lmdeploy/pull/2278
* Support guided decoding for pytorch backend by @AllentDan in https://github.com/InternLM/lmdeploy/pull/1856
* support min_p sampling parameter by @irexyc in https://github.com/InternLM/lmdeploy/pull/2420
* Refactor pytorch engine by @grimoire in https://github.com/InternLM/lmdeploy/pull/2104
* refactor pytorch engine(ascend) by @yao-fengchen in https://github.com/InternLM/lmdeploy/pull/2440
### 💥 Improvements
* Remove deprecated arguments from API and clarify model_name and chat_template_name by @lvhan028 in https://github.com/InternLM/lmdeploy/pull/1931
* Fix duplicated session_id when pipeline is used by multithreads by @irexyc in https://github.com/InternLM/lmdeploy/pull/2134
* remove eviction param by @grimoire in https://github.com/InternLM/lmdeploy/pull/2285
* Remove QoS serving by @AllentDan in https://github.com/InternLM/lmdeploy/pull/2294
* Support send tool_calls back to internlm2 by @AllentDan in https://github.com/InternLM/lmdeploy/pull/2147
* Add stream options to control usage by @AllentDan in https://github.com/InternLM/lmdeploy/pull/2313
* add device type for pytorch engine in cli by @RunningLeon in https://github.com/InternLM/lmdeploy/pull/2321
* Update error status_code to raise error in openai client by @AllentDan in https://github.com/InternLM/lmdeploy/pull/2333
* Change to use device instead of device-type in cli by @RunningLeon in https://github.com/InternLM/lmdeploy/pull/2337
* Add GEMM test utils by @lzhangzz in https://github.com/InternLM/lmdeploy/pull/2342
* Add environment variable to control SILU fusion by @lzhangzz in https://github.com/InternLM/lmdeploy/pull/2343
* Use single thread per model instance by @lzhangzz in https://github.com/InternLM/lmdeploy/pull/2339
* add cache to speed up docker building by @RunningLeon in https://github.com/InternLM/lmdeploy/pull/2344
* add max_prefill_token_num argument in CLI by @lvhan028 in https://github.com/InternLM/lmdeploy/pull/2345
* torch engine optimize prefill for long context by @grimoire in https://github.com/InternLM/lmdeploy/pull/1962
* Refactor turbomind (1/N) by @lzhangzz in https://github.com/InternLM/lmdeploy/pull/2352
* feat(server): enable `seed` parameter for openai compatible server. by @DearPlanet in https://github.com/InternLM/lmdeploy/pull/2353
* support do_sample parameter by @irexyc in https://github.com/InternLM/lmdeploy/pull/2375
* refactor TurbomindModelConfig by @lvhan028 in https://github.com/InternLM/lmdeploy/pull/2364
* import dlinfer before imageencoding by @jinminxi104 in https://github.com/InternLM/lmdeploy/pull/2413
* ignore *.pth when download model from model hub by @lvhan028 in https://github.com/InternLM/lmdeploy/pull/2426
* inplace logits process as default by @grimoire in https://github.com/InternLM/lmdeploy/pull/2427
* handle invalid images by @irexyc in https://github.com/InternLM/lmdeploy/pull/2312
* Split token_embs and lm_head weights by @irexyc in https://github.com/InternLM/lmdeploy/pull/2252
* build: update ascend dockerfile by @CyCle1024 in https://github.com/InternLM/lmdeploy/pull/2421
* build nccl in dockerfile for cuda11.8 by @RunningLeon in https://github.com/InternLM/lmdeploy/pull/2433
* automatically set max_batch_size according to the device when it is not specified by @lvhan028 in https://github.com/InternLM/lmdeploy/pull/2434
* rename the ascend dockerfile by @lvhan028 in https://github.com/InternLM/lmdeploy/pull/2403
* refactor ascend kernels by @yao-fengchen in https://github.com/InternLM/lmdeploy/pull/2355
### 🐞 Bug fixes
* enable run vlm with pytorch engine in gradio by @RunningLeon in https://github.com/InternLM/lmdeploy/pull/2256
* fix side-effect: failed to update tm model config with tm engine config by @lvhan028 in https://github.com/InternLM/lmdeploy/pull/2275
* Fix internvl2 template and update docs by @irexyc in https://github.com/InternLM/lmdeploy/pull/2292
* fix the issue missing dependencies in the Dockerfile and pip by @ColorfulDick in https://github.com/InternLM/lmdeploy/pull/2240
* Fix the way to get "quantization_config" from model's coniguration by @lvhan028 in https://github.com/InternLM/lmdeploy/pull/2325
* fix(ascend): fix import error of pt engine in cli by @CyCle1024 in https://github.com/InternLM/lmdeploy/pull/2328
* Default rope_scaling_factor of TurbomindEngineConfig to None by @lvhan028 in https://github.com/InternLM/lmdeploy/pull/2358
* Fix the logic of update engine_config to TurbomindModelConfig for both tm model and hf model by @lvhan028 in https://github.com/InternLM/lmdeploy/pull/2362
* fix cache position for pytorch engine by @RunningLeon in https://github.com/InternLM/lmdeploy/pull/2388
* Fix /v1/completions batch order wrong by @AllentDan in https://github.com/InternLM/lmdeploy/pull/2395
* Fix some issues encountered by modelscope and community by @irexyc in https://github.com/InternLM/lmdeploy/pull/2428
* fix llama3 rotary in pytorch engine by @grimoire in https://github.com/InternLM/lmdeploy/pull/2444
* fix tensors on different devices when deploying MiniCPM-V-2_6 with tensor parallelism by @irexyc in https://github.com/InternLM/lmdeploy/pull/2454
* fix MultinomialSampling operator builder by @grimoire in https://github.com/InternLM/lmdeploy/pull/2460
* Fix initialization of runtime_min_p by @irexyc in https://github.com/InternLM/lmdeploy/pull/2461
* fix Windows compile error by @zhyncs in https://github.com/InternLM/lmdeploy/pull/2303
* fix: follow up #2303 by @zhyncs in https://github.com/InternLM/lmdeploy/pull/2307
### 📚 Documentations
* Reorganize the user guide and update the get_started section by @lvhan028 in https://github.com/InternLM/lmdeploy/pull/2038
* cancel support baichuan2 7b awq in pytorch engine by @grimoire in https://github.com/InternLM/lmdeploy/pull/2246
* Add user guide about slora serving  by @AllentDan in https://github.com/InternLM/lmdeploy/pull/2084
* Reorganize the table of content of get_started by @lvhan028 in https://github.com/InternLM/lmdeploy/pull/2378
* fix get_started user guide unaccessible by @lvhan028 in https://github.com/InternLM/lmdeploy/pull/2410
* add Ascend get_started by @jinminxi104 in https://github.com/InternLM/lmdeploy/pull/2417
### 🌐 Other
* test prtest image update by @zhulinJulia24 in https://github.com/InternLM/lmdeploy/pull/2192
* Update python support version  by @wuhongsheng in https://github.com/InternLM/lmdeploy/pull/2290
* [ci] benchmark react by @zhulinJulia24 in https://github.com/InternLM/lmdeploy/pull/2183
* bump version to v0.6.0a0 by @lvhan028 in https://github.com/InternLM/lmdeploy/pull/2371
* [ci] add daily test's coverage report  by @zhulinJulia24 in https://github.com/InternLM/lmdeploy/pull/2401
* update actions/download-artifact to v4 to fix security issue by @lvhan028 in https://github.com/InternLM/lmdeploy/pull/2419
* bump version to v0.6.0 by @lvhan028 in https://github.com/InternLM/lmdeploy/pull/2445

## New Contributors
* @wuhongsheng made their first contribution in https://github.com/InternLM/lmdeploy/pull/2290
* @ColorfulDick made their first contribution in https://github.com/InternLM/lmdeploy/pull/2240
* @DearPlanet made their first contribution in https://github.com/InternLM/lmdeploy/pull/2353
* @jinminxi104 made their first contribution in https://github.com/InternLM/lmdeploy/pull/2413

**Full Changelog**: https://github.com/InternLM/lmdeploy/compare/v0.5.3...v0.6.0

## v0.6.1 (2024-09-28)

<!-- Release notes generated using configuration in .github/release.yml at main -->

## What's Changed
### 🚀 Features
* Support user-sepcified data type by @lvhan028 in https://github.com/InternLM/lmdeploy/pull/2473
* Support minicpm3-4b by @AllentDan in https://github.com/InternLM/lmdeploy/pull/2465
* support Qwen2-VL with pytorch backend by @irexyc in https://github.com/InternLM/lmdeploy/pull/2449
### 💥 Improvements
* Add silu mul kernel by @grimoire in https://github.com/InternLM/lmdeploy/pull/2469
* adjust schedule to improve TTFT in pytorch engine by @grimoire in https://github.com/InternLM/lmdeploy/pull/2477
* Add max_log_len option to control length of printed log by @lvhan028 in https://github.com/InternLM/lmdeploy/pull/2478
* set served model name being repo_id from hub before it is downloaded by @lvhan028 in https://github.com/InternLM/lmdeploy/pull/2494
* Improve proxy server usage by @AllentDan in https://github.com/InternLM/lmdeploy/pull/2488
* CudaGraph mixin by @grimoire in https://github.com/InternLM/lmdeploy/pull/2485
* pytorch engine add get_logits by @grimoire in https://github.com/InternLM/lmdeploy/pull/2487
* Refactor lora by @grimoire in https://github.com/InternLM/lmdeploy/pull/2466
* support noaligned silu_and_mul by @grimoire in https://github.com/InternLM/lmdeploy/pull/2506
* optimize performance of ascend backend's update_step_context() by calculating kv_start_indices in a new way by @jiajie-yang in https://github.com/InternLM/lmdeploy/pull/2521
* Fix chatglm tokenizer failed when transformers>=4.45.0 by @AllentDan in https://github.com/InternLM/lmdeploy/pull/2520
### 🐞 Bug fixes
* Fix "TypeError: Got unsupported ScalarType BFloat16" by @SeitaroShinagawa in https://github.com/InternLM/lmdeploy/pull/2472
* fix ascend atten_mask by @yao-fengchen in https://github.com/InternLM/lmdeploy/pull/2483
* Catch exceptions thrown by turbomind inference thread by @lvhan028 in https://github.com/InternLM/lmdeploy/pull/2502
* The `get_ppl` missed the last token of each iteration during multi-iter prefill by @lvhan028 in https://github.com/InternLM/lmdeploy/pull/2499
* fix vl gradio by @irexyc in https://github.com/InternLM/lmdeploy/pull/2527
### 🌐 Other
* [ci] regular update by @zhulinJulia24 in https://github.com/InternLM/lmdeploy/pull/2431
* [CI] add base model evaluation by @zhulinJulia24 in https://github.com/InternLM/lmdeploy/pull/2490
* bump version to v0.6.1 by @lvhan028 in https://github.com/InternLM/lmdeploy/pull/2513

## New Contributors
* @SeitaroShinagawa made their first contribution in https://github.com/InternLM/lmdeploy/pull/2472

**Full Changelog**: https://github.com/InternLM/lmdeploy/compare/v0.6.0...v0.6.1

## v0.6.2 (2024-10-29)

<!-- Release notes generated using configuration in .github/release.yml at main -->

## Highlights

- PyTorch engine supports graph mode on ascend platform, doubling the inference speed
- Support llama3.2-vision models in PyTorch engine
- Support Mixtral in TurboMind engine, achieving 20+ RPS using SharedGPT dataset with 2 A100-80G GPUs


## What's Changed
### 🚀 Features
* support downloading models from openmind_hub by @cookieyyds in https://github.com/InternLM/lmdeploy/pull/2563
* Support pytorch engine kv int4/int8 quantization by @AllentDan in https://github.com/InternLM/lmdeploy/pull/2438
* feat(ascend): support w4a16 by @yao-fengchen in https://github.com/InternLM/lmdeploy/pull/2587
* [maca] add maca backend support. by @Reinerzhou in https://github.com/InternLM/lmdeploy/pull/2636
* Support mllama for pytorch engine by @AllentDan in https://github.com/InternLM/lmdeploy/pull/2605
* add --eager-mode to cli by @RunningLeon in https://github.com/InternLM/lmdeploy/pull/2645
* [ascend] add ascend graph mode by @CyCle1024 in https://github.com/InternLM/lmdeploy/pull/2647
* MoE support for turbomind by @lzhangzz in https://github.com/InternLM/lmdeploy/pull/2621
### 💥 Improvements
* [Feature] Add argument to disable FastAPI docs by @mouweng in https://github.com/InternLM/lmdeploy/pull/2540
* add check for device with cap 7.x by @grimoire in https://github.com/InternLM/lmdeploy/pull/2535
* Add tool role for langchain usage by @AllentDan in https://github.com/InternLM/lmdeploy/pull/2558
* Fix llama3.2-1b inference error by handling tie_word_embedding by @grimoire in https://github.com/InternLM/lmdeploy/pull/2568
* Add a workaround for saving internvl2 with latest transformers by @AllentDan in https://github.com/InternLM/lmdeploy/pull/2583
* optimize paged attention on triton3 by @grimoire in https://github.com/InternLM/lmdeploy/pull/2553
* refactor for multi backends in dlinfer by @CyCle1024 in https://github.com/InternLM/lmdeploy/pull/2619
* Copy sglang/bench_serving.py to lmdeploy as serving benchmark script by @lvhan028 in https://github.com/InternLM/lmdeploy/pull/2620
* Add barrier to prevent TP nccl kernel waiting. by @grimoire in https://github.com/InternLM/lmdeploy/pull/2607
* [ascend] refactor fused_moe on ascend platform by @yao-fengchen in https://github.com/InternLM/lmdeploy/pull/2613
* [ascend] support paged_prefill_attn when batch > 1 by @yao-fengchen in https://github.com/InternLM/lmdeploy/pull/2612
* Raise an error for the wrong chat template by @AllentDan in https://github.com/InternLM/lmdeploy/pull/2618
* refine pre-post-process by @jinminxi104 in https://github.com/InternLM/lmdeploy/pull/2632
* small block_m for sm7.x by @grimoire in https://github.com/InternLM/lmdeploy/pull/2626
* update check for triton by @grimoire in https://github.com/InternLM/lmdeploy/pull/2641
* Support llama3.2 LLM models in turbomind engine by @lvhan028 in https://github.com/InternLM/lmdeploy/pull/2596
* Check whether device support bfloat16 by @lvhan028 in https://github.com/InternLM/lmdeploy/pull/2653
* Add warning message about `do_sample` to alert BC by @lvhan028 in https://github.com/InternLM/lmdeploy/pull/2654
* update ascend dockerfile by @CyCle1024 in https://github.com/InternLM/lmdeploy/pull/2661
* fix supported model list in ascend graph mode by @jinminxi104 in https://github.com/InternLM/lmdeploy/pull/2669
* remove dlinfer version by @CyCle1024 in https://github.com/InternLM/lmdeploy/pull/2672
### 🐞 Bug fixes
* set outlines<0.1.0 by @AllentDan in https://github.com/InternLM/lmdeploy/pull/2559
* fix: make exit_flag verification for ascend more general by @CyCle1024 in https://github.com/InternLM/lmdeploy/pull/2588
* set capture mode thread_local by @grimoire in https://github.com/InternLM/lmdeploy/pull/2560
* Add distributed context in pytorch engine to support torchrun by @grimoire in https://github.com/InternLM/lmdeploy/pull/2615
* Fix error in python3.8. by @Reinerzhou in https://github.com/InternLM/lmdeploy/pull/2646
* Align UT with triton fill_kv_cache_quant kernel by @AllentDan in https://github.com/InternLM/lmdeploy/pull/2644
* miss device_type when checking is_bf16_supported on ascend platform by @lvhan028 in https://github.com/InternLM/lmdeploy/pull/2663
* fix syntax in Dockerfile_aarch64_ascend by @CyCle1024 in https://github.com/InternLM/lmdeploy/pull/2664
* Set history_cross_kv_seqlens to 0 by default by @AllentDan in https://github.com/InternLM/lmdeploy/pull/2666
* fix build error in ascend dockerfile by @CyCle1024 in https://github.com/InternLM/lmdeploy/pull/2667
* bugfix: llava-hf/llava-interleave-qwen-7b-hf (#2497) by @deepindeed2022 in https://github.com/InternLM/lmdeploy/pull/2657
* fix inference mode error for qwen2-vl by @irexyc in https://github.com/InternLM/lmdeploy/pull/2668
### 📚 Documentations
* Add instruction for downloading models from openmind hub by @cookieyyds in https://github.com/InternLM/lmdeploy/pull/2577
* Fix spacing in ascend user guide by @Superskyyy in https://github.com/InternLM/lmdeploy/pull/2601
* Update get_started tutorial about deploying on ascend platform by @jinminxi104 in https://github.com/InternLM/lmdeploy/pull/2655
* Update ascend get_started tutorial about installing nnal by @jinminxi104 in https://github.com/InternLM/lmdeploy/pull/2662
### 🌐 Other
* [ci] add oc infer test in stable test by @zhulinJulia24 in https://github.com/InternLM/lmdeploy/pull/2523
* update copyright by @lvhan028 in https://github.com/InternLM/lmdeploy/pull/2579
* [Doc]: Lock sphinx version by @RunningLeon in https://github.com/InternLM/lmdeploy/pull/2594
* [ci] use local requirements for test workflow by @zhulinJulia24 in https://github.com/InternLM/lmdeploy/pull/2569
* [ci] add pytorch kvint testcase into function regresstion by @zhulinJulia24 in https://github.com/InternLM/lmdeploy/pull/2584
* [ci] React dailytest workflow by @zhulinJulia24 in https://github.com/InternLM/lmdeploy/pull/2617
* [ci] fix restful script by @zhulinJulia24 in https://github.com/InternLM/lmdeploy/pull/2635
* [ci] add internlm2_5_7b_batch_1 into evaluation testcase by @zhulinJulia24 in https://github.com/InternLM/lmdeploy/pull/2631
* match torch and torch_vision version by @grimoire in https://github.com/InternLM/lmdeploy/pull/2649
* Bump version to v0.6.2 by @lvhan028 in https://github.com/InternLM/lmdeploy/pull/2659

## New Contributors
* @mouweng made their first contribution in https://github.com/InternLM/lmdeploy/pull/2540
* @cookieyyds made their first contribution in https://github.com/InternLM/lmdeploy/pull/2563
* @Superskyyy made their first contribution in https://github.com/InternLM/lmdeploy/pull/2601
* @Reinerzhou made their first contribution in https://github.com/InternLM/lmdeploy/pull/2636
* @deepindeed2022 made their first contribution in https://github.com/InternLM/lmdeploy/pull/2657

**Full Changelog**: https://github.com/InternLM/lmdeploy/compare/v0.6.1...v0.6.2

## v0.6.2.post1 (2024-11-07)

<!-- Release notes generated using configuration in .github/release.yml at 0.6.2.post1 -->

## What's Changed
### Bugs
* Fix llama3.2 VL vision in "Supported Modals" documents @blankanswer in #2703
* miss to read moe_ffn weights from converted tm model @lvhan028 in #2698
* better tp exit log @grimoire in #2677
* fix index error when computing ppl on long-text prompt  @lvhan028  in #2697
* Support min_tokens, min_p parameters for api_server @AllentDan  in 2681
* fix ascend get_started.md link @CyCle1024 in #2696
* Call cuda empty_cache to prevent OOM when quantizing model @AllentDan in #2671 
* Fix turbomind TP for v0.6.2 by @lzhangzz in https://github.com/InternLM/lmdeploy/pull/2713
### 🌐 Other
* [[ci] support v100 dailytest (](https://github.com/InternLM/lmdeploy/commit/434195ea0c80b38dc2cf80c79d53a30f22b53aab)https://github.com/InternLM/lmdeploy/pull/2665[)](https://github.com/InternLM/lmdeploy/commit/434195ea0c80b38dc2cf80c79d53a30f22b53aab)
* bump version to 0.6.2.post1 by @lvhan028 in https://github.com/InternLM/lmdeploy/pull/2717


**Full Changelog**: https://github.com/InternLM/lmdeploy/compare/v0.6.2...v0.6.2.post1

## v0.6.3 (2024-11-16)

<!-- Release notes generated using configuration in .github/release.yml at main -->

## What's Changed
### 🚀 Features
* support yarn in turbomind backend by @irexyc in https://github.com/InternLM/lmdeploy/pull/2519
* add linear op on dlinfer platform by @yao-fengchen in https://github.com/InternLM/lmdeploy/pull/2627
* support turbomind head_dim 64 by @irexyc in https://github.com/InternLM/lmdeploy/pull/2715
* [Feature]: support LlavaForConditionalGeneration with turbomind inference by @deepindeed2022 in https://github.com/InternLM/lmdeploy/pull/2710
* Support Mono-InternVL with PyTorch backend by @wzk1015 in https://github.com/InternLM/lmdeploy/pull/2727
* Support Qwen2-MoE models by @lzhangzz in https://github.com/InternLM/lmdeploy/pull/2723
* Support mixtral moe AWQ quantization. by @AllentDan in https://github.com/InternLM/lmdeploy/pull/2725
* Support chemvlm by @RunningLeon in https://github.com/InternLM/lmdeploy/pull/2738
* Support molmo in turbomind by @lvhan028 in https://github.com/InternLM/lmdeploy/pull/2716
### 💥 Improvements
* Call cuda empty_cache to prevent OOM when quantizing model by @AllentDan in https://github.com/InternLM/lmdeploy/pull/2671
* feat: support dynamic/llama3 rotary embedding in ascend graph mode by @tangzhiyi11 in https://github.com/InternLM/lmdeploy/pull/2670
* Add ensure_ascii = False for json.dumps by @AllentDan in https://github.com/InternLM/lmdeploy/pull/2707
* Flatten cache and add flashattention by @grimoire in https://github.com/InternLM/lmdeploy/pull/2676
* Support ep, column major moe kernel. by @grimoire in https://github.com/InternLM/lmdeploy/pull/2690
* Remove one of the duplicate bos tokens by @AllentDan in https://github.com/InternLM/lmdeploy/pull/2708
* Check server input by @irexyc in https://github.com/InternLM/lmdeploy/pull/2719
* optimize dlinfer moe by @tangzhiyi11 in https://github.com/InternLM/lmdeploy/pull/2741
### 🐞 Bug fixes
* Support min_tokens, min_p parameters for api_server by @AllentDan in https://github.com/InternLM/lmdeploy/pull/2681
* fix index error when computing ppl on long-text prompt by @lvhan028 in https://github.com/InternLM/lmdeploy/pull/2697
* Better tp exit log. by @grimoire in https://github.com/InternLM/lmdeploy/pull/2677
* miss to read moe_ffn weights from converted tm model by @lvhan028 in https://github.com/InternLM/lmdeploy/pull/2698
* Fix turbomind TP by @lzhangzz in https://github.com/InternLM/lmdeploy/pull/2706
* fix decoding kernel for deepseekv2 by @grimoire in https://github.com/InternLM/lmdeploy/pull/2688
* fix tp exit code for pytorch engine by @RunningLeon in https://github.com/InternLM/lmdeploy/pull/2718
* fix assert pad >= 0 failed when inter_size is not a multiple of group… by @Vinkle-hzt in https://github.com/InternLM/lmdeploy/pull/2740
* fix issue that mono-internvl failed to fallback pytorch engine by @lvhan028 in https://github.com/InternLM/lmdeploy/pull/2744
* Remove use_fast=True when loading tokenizer for lite auto_awq by @AllentDan in https://github.com/InternLM/lmdeploy/pull/2758
* set wrong head_dim for mistral-nemo by @lvhan028 in https://github.com/InternLM/lmdeploy/pull/2761
### 📚 Documentations
* Update ascend readme by @jinminxi104 in https://github.com/InternLM/lmdeploy/pull/2756
* fix ascend get_started.md link by @CyCle1024 in https://github.com/InternLM/lmdeploy/pull/2696
* Fix llama3.2 VL vision in "Supported Modals" documents by @blankanswer in https://github.com/InternLM/lmdeploy/pull/2703
### 🌐 Other
* [ci] support v100 dailytest  by @zhulinJulia24 in https://github.com/InternLM/lmdeploy/pull/2665
* [ci] add more testcase into evaluation and daily test by @zhulinJulia24 in https://github.com/InternLM/lmdeploy/pull/2721
* feat: support multi cards in ascend graph mode by @tangzhiyi11 in https://github.com/InternLM/lmdeploy/pull/2755
* bump version to v0.6.3 by @lvhan028 in https://github.com/InternLM/lmdeploy/pull/2754

## New Contributors
* @blankanswer made their first contribution in https://github.com/InternLM/lmdeploy/pull/2703
* @tangzhiyi11 made their first contribution in https://github.com/InternLM/lmdeploy/pull/2670
* @wzk1015 made their first contribution in https://github.com/InternLM/lmdeploy/pull/2727
* @Vinkle-hzt made their first contribution in https://github.com/InternLM/lmdeploy/pull/2740

**Full Changelog**: https://github.com/InternLM/lmdeploy/compare/v0.6.2...v0.6.3

## v0.6.4 (2024-12-09)

<!-- Release notes generated using configuration in .github/release.yml at main -->

## What's Changed
### 🚀 Features
* feature: support qwen2.5 fuction_call by @akai-shuuichi in https://github.com/InternLM/lmdeploy/pull/2737
* [Feature] support minicpm-v_2_6 for pytorch engine. by @Reinerzhou in https://github.com/InternLM/lmdeploy/pull/2767
* Support qwen2-vl AWQ quantization by @AllentDan in https://github.com/InternLM/lmdeploy/pull/2787
* Add DeepSeek-V2 support by @lzhangzz in https://github.com/InternLM/lmdeploy/pull/2763
* [ascend]feat: support kv int8 by @yao-fengchen in https://github.com/InternLM/lmdeploy/pull/2736
### 💥 Improvements
* Optimize update_step_ctx on Ascend by @jinminxi104 in https://github.com/InternLM/lmdeploy/pull/2804
* Add Ascend installation adapter by @zhabuye in https://github.com/InternLM/lmdeploy/pull/2817
* Refactor turbomind (2/N) by @lzhangzz in https://github.com/InternLM/lmdeploy/pull/2818
* add openssh-server installation in dockerfile by @lvhan028 in https://github.com/InternLM/lmdeploy/pull/2830
* Add version restrictions in runtime_ascend.txt to ensure functionality by @zhabuye in https://github.com/InternLM/lmdeploy/pull/2836
* better kv allocate by @grimoire in https://github.com/InternLM/lmdeploy/pull/2814
* Update internvl chat template by @AllentDan in https://github.com/InternLM/lmdeploy/pull/2832
* profile throughput without new threads by @grimoire in https://github.com/InternLM/lmdeploy/pull/2826
* [dlinfer] change dlinfer kv_cache layout and ajust paged_prefill_attention api. by @Reinerzhou in https://github.com/InternLM/lmdeploy/pull/2847
* [maca] add env to support different mm layout on maca. by @Reinerzhou in https://github.com/InternLM/lmdeploy/pull/2835
* Supports W8A8 quantization for more models by @AllentDan in https://github.com/InternLM/lmdeploy/pull/2850
### 🐞 Bug fixes
* disable prefix-caching for vl model by @grimoire in https://github.com/InternLM/lmdeploy/pull/2825
* Fix gemma2 accuracy through the correct softcapping logic by @AllentDan in https://github.com/InternLM/lmdeploy/pull/2842
* fix accessing before initialization by @lvhan028 in https://github.com/InternLM/lmdeploy/pull/2845
* fix the logic to verify whether AutoAWQ has been successfully installed by @grimoire in https://github.com/InternLM/lmdeploy/pull/2844
* check whether backend_config is None or not before accessing its attr by @lvhan028 in https://github.com/InternLM/lmdeploy/pull/2848
* [ascend] convert kv cache to nd format in ascend graph mode by @tangzhiyi11 in https://github.com/InternLM/lmdeploy/pull/2853
### 📚 Documentations
* Update supported models & Ascend doc by @jinminxi104 in https://github.com/InternLM/lmdeploy/pull/2765
* update supported models by @lvhan028 in https://github.com/InternLM/lmdeploy/pull/2849
### 🌐 Other
* [CI] Split vl testcases into turbomind and pytorch backend by @zhulinJulia24 in https://github.com/InternLM/lmdeploy/pull/2751
* [dlinfer] Fix qwenvl rope error for dlinfer backend by @JackWeiw in https://github.com/InternLM/lmdeploy/pull/2795
* [CI] add more testcase for mllm models by @zhulinJulia24 in https://github.com/InternLM/lmdeploy/pull/2791
* Update dlinfer-ascend version in runtime_ascend.txt by @jinminxi104 in https://github.com/InternLM/lmdeploy/pull/2865
* bump version to v0.6.4 by @lvhan028 in https://github.com/InternLM/lmdeploy/pull/2864

## New Contributors
* @akai-shuuichi made their first contribution in https://github.com/InternLM/lmdeploy/pull/2737
* @JackWeiw made their first contribution in https://github.com/InternLM/lmdeploy/pull/2795
* @zhabuye made their first contribution in https://github.com/InternLM/lmdeploy/pull/2817

**Full Changelog**: https://github.com/InternLM/lmdeploy/compare/v0.6.3...v0.6.4

## 0.6.5 (2024-12-30)

<!-- Release notes generated using configuration in .github/release.yml at main -->

## What's Changed
### 🚀 Features
* [dlinfer] feat: add DlinferFlashAttention to support qwen vl. by @Reinerzhou in https://github.com/InternLM/lmdeploy/pull/2952
### 💥 Improvements
* refactor PyTorchEngine check env by @grimoire in https://github.com/InternLM/lmdeploy/pull/2870
* refine multi-backend setup.py by @jinminxi104 in https://github.com/InternLM/lmdeploy/pull/2880
* Refactor VLM modules by @lvhan028 in https://github.com/InternLM/lmdeploy/pull/2810
* [dlinfer] only compile the language model in vl models by @tangzhiyi11 in https://github.com/InternLM/lmdeploy/pull/2893
* Optimize tp broadcast by @grimoire in https://github.com/InternLM/lmdeploy/pull/2889
* unfeeze torch version in dockerfile by @RunningLeon in https://github.com/InternLM/lmdeploy/pull/2906
* support tp > n_kv_heads for pt engine by @RunningLeon in https://github.com/InternLM/lmdeploy/pull/2872
* replicate kv for some models when tp is divisble by kv_head_num by @irexyc in https://github.com/InternLM/lmdeploy/pull/2874
* Fallback to pytorch engine when the model is quantized by smooth quant by @lvhan028 in https://github.com/InternLM/lmdeploy/pull/2953
* Torchrun launching multiple api_server by @AllentDan in https://github.com/InternLM/lmdeploy/pull/2402
### 🐞 Bug fixes
* [Feature] Support for loading lora adapter weights in safetensors format by @Galaxy-Husky in https://github.com/InternLM/lmdeploy/pull/2860
* fix cpu cache by @grimoire in https://github.com/InternLM/lmdeploy/pull/2881
* Fix args type in docstring by @Galaxy-Husky in https://github.com/InternLM/lmdeploy/pull/2888
* Fix llama3.1 chat template by @fzyzcjy in https://github.com/InternLM/lmdeploy/pull/2862
* Fix typo by @ghntd in https://github.com/InternLM/lmdeploy/pull/2916
* fix: Incorrect stats size during inference of throughput benchmark when concurrency > num_prompts by @pancak3 in https://github.com/InternLM/lmdeploy/pull/2928
* fix lora name and rearange wqkv for internlm2 by @RunningLeon in https://github.com/InternLM/lmdeploy/pull/2912
* [dlinfer] fix moe op for dlinfer. by @Reinerzhou in https://github.com/InternLM/lmdeploy/pull/2917
* [side effect] fix vlm quant failed by @lvhan028 in https://github.com/InternLM/lmdeploy/pull/2914
* fix torch_dtype by @RunningLeon in https://github.com/InternLM/lmdeploy/pull/2933
* support unaligned qkv heads by @grimoire in https://github.com/InternLM/lmdeploy/pull/2930
* fix mllama inference without image by @RunningLeon in https://github.com/InternLM/lmdeploy/pull/2947
* Support torch_dtype modification and update FAQs for AWQ quantization by @AllentDan in https://github.com/InternLM/lmdeploy/pull/2898
* Fix exception handler for proxy server by @AllentDan in https://github.com/InternLM/lmdeploy/pull/2901
* Fix torch_dtype in lite by @AllentDan in https://github.com/InternLM/lmdeploy/pull/2956
* [side-effect] bring back quantization of qwen2-vl, glm4v and etc. by @lvhan028 in https://github.com/InternLM/lmdeploy/pull/2954
* add a thread pool executor to control the vl engine traffic by @lvhan028 in https://github.com/InternLM/lmdeploy/pull/2970
* [side-effect] fix gradio demo error by @lvhan028 in https://github.com/InternLM/lmdeploy/pull/2976
### 🌐 Other
* [dlinfer] fix engine checker by @tangzhiyi11 in https://github.com/InternLM/lmdeploy/pull/2891
* Bump version to v0.6.5 by @lvhan028 in https://github.com/InternLM/lmdeploy/pull/2955

## New Contributors
* @Galaxy-Husky made their first contribution in https://github.com/InternLM/lmdeploy/pull/2860
* @fzyzcjy made their first contribution in https://github.com/InternLM/lmdeploy/pull/2862
* @ghntd made their first contribution in https://github.com/InternLM/lmdeploy/pull/2916
* @pancak3 made their first contribution in https://github.com/InternLM/lmdeploy/pull/2928

**Full Changelog**: https://github.com/InternLM/lmdeploy/compare/v0.6.4...0.6.5

## v0.7.0 (2025-01-15)

<!-- Release notes generated using configuration in .github/release.yml at main -->

## What's Changed
### 🚀 Features
* Support moe w8a8 in pytorch engine by @grimoire in https://github.com/InternLM/lmdeploy/pull/2894
* Support DeepseekV3 fp8 by @grimoire in https://github.com/InternLM/lmdeploy/pull/2967
* support new backend cambricon by @JackWeiw in https://github.com/InternLM/lmdeploy/pull/3002
* support-moe-fp8 by @RunningLeon in https://github.com/InternLM/lmdeploy/pull/3007
* add internlm3-dense(turbomind) & chat template by @irexyc in https://github.com/InternLM/lmdeploy/pull/3024
* support internlm3 on pt by @RunningLeon in https://github.com/InternLM/lmdeploy/pull/3026
* Support internlm3 quantization by @AllentDan in https://github.com/InternLM/lmdeploy/pull/3027
### 💥 Improvements
* Optimize awq kernel in pytorch engine by @grimoire in https://github.com/InternLM/lmdeploy/pull/2965
* Support fp8 w8a8 for pt backend by @RunningLeon in https://github.com/InternLM/lmdeploy/pull/2959
* Optimize lora kernel by @grimoire in https://github.com/InternLM/lmdeploy/pull/2975
* Remove threadsafe by @grimoire in https://github.com/InternLM/lmdeploy/pull/2907
* Refactor async engine & turbomind IO by @lzhangzz in https://github.com/InternLM/lmdeploy/pull/2968
* [dlinfer]rope refine by @JackWeiw in https://github.com/InternLM/lmdeploy/pull/2984
* Expose spaces_between_special_tokens by @AllentDan in https://github.com/InternLM/lmdeploy/pull/2991
* [dlinfer]change llm op interface of paged_prefill_attention. by @JackWeiw in https://github.com/InternLM/lmdeploy/pull/2977
* Update request logger by @lvhan028 in https://github.com/InternLM/lmdeploy/pull/2981
* remove decoding by @grimoire in https://github.com/InternLM/lmdeploy/pull/3016
### 🐞 Bug fixes
* Fix build crash in nvcr.io/nvidia/pytorch:24.06-py3 image by @zgjja in https://github.com/InternLM/lmdeploy/pull/2964
* add tool role in BaseChatTemplate as tool response in messages by @AllentDan in https://github.com/InternLM/lmdeploy/pull/2979
* Fix ascend dockerfile by @jinminxi104 in https://github.com/InternLM/lmdeploy/pull/2989
* fix internvl2 qk norm by @grimoire in https://github.com/InternLM/lmdeploy/pull/2987
* fix xcomposer2 when transformers is upgraded greater than 4.46  by @irexyc in https://github.com/InternLM/lmdeploy/pull/3001
* Fix get_ppl & get_logits by @lvhan028 in https://github.com/InternLM/lmdeploy/pull/3008
* Fix typo in w4a16 guide by @Yan-Xiangjun in https://github.com/InternLM/lmdeploy/pull/3018
* fix blocked fp8 moe kernel by @grimoire in https://github.com/InternLM/lmdeploy/pull/3009
* Fix async engine by @lzhangzz in https://github.com/InternLM/lmdeploy/pull/3029
* [hotfix] Fix get_ppl by @lvhan028 in https://github.com/InternLM/lmdeploy/pull/3023
* Fix MoE gating for DeepSeek V2 by @lzhangzz in https://github.com/InternLM/lmdeploy/pull/3030
* Fix empty response for pipeline by @lzhangzz in https://github.com/InternLM/lmdeploy/pull/3034
* Fix potential hang during TP model initialization by @lzhangzz in https://github.com/InternLM/lmdeploy/pull/3033
### 🌐 Other
* [ci] add w8a8 and internvl2.5 models into testcase by @zhulinJulia24 in https://github.com/InternLM/lmdeploy/pull/2949
* bump version to v0.7.0 by @lvhan028 in https://github.com/InternLM/lmdeploy/pull/3010

## New Contributors
* @zgjja made their first contribution in https://github.com/InternLM/lmdeploy/pull/2964
* @Yan-Xiangjun made their first contribution in https://github.com/InternLM/lmdeploy/pull/3018

**Full Changelog**: https://github.com/InternLM/lmdeploy/compare/0.6.5...v0.7.0

## v0.7.0.post1 (2025-01-25)

<!-- Release notes generated using configuration in .github/release.yml at main -->

## What's Changed
### 💥 Improvements
* use weights iterator while loading by @RunningLeon in https://github.com/InternLM/lmdeploy/pull/2886
### 🐞 Bug fixes
* [dlinfer] fix ascend qwen2_vl graph_mode by @yao-fengchen in https://github.com/InternLM/lmdeploy/pull/3045
* fix error in interactive api by @lvhan028 in https://github.com/InternLM/lmdeploy/pull/3074
* fix sliding window mgr by @grimoire in https://github.com/InternLM/lmdeploy/pull/3068
* More arguments in api_client, update docstrings by @AllentDan in https://github.com/InternLM/lmdeploy/pull/3077
### 🌐 Other
* [ci] add internlm3 into testcase by @zhulinJulia24 in https://github.com/InternLM/lmdeploy/pull/3038
* add internlm3 to supported models by @lvhan028 in https://github.com/InternLM/lmdeploy/pull/3041
* update pre-commit config by @lvhan028 in https://github.com/InternLM/lmdeploy/pull/2683
* [maca] add cudagraph support on maca backend. by @Reinerzhou in https://github.com/InternLM/lmdeploy/pull/2834
* bump version to v0.7.0.post1 by @lvhan028 in https://github.com/InternLM/lmdeploy/pull/3076


**Full Changelog**: https://github.com/InternLM/lmdeploy/compare/v0.7.0...v0.7.0.post1

## v0.7.0.post2 (2025-01-27)

<!-- Release notes generated using configuration in .github/release.yml at main -->

## What's Changed
### 💥 Improvements
* Add deepseek-r1 chat template by @AllentDan in https://github.com/InternLM/lmdeploy/pull/3072
* Update tokenizer by @lvhan028 in https://github.com/InternLM/lmdeploy/pull/3061
### 🐞 Bug fixes
* Add system role to deepseek chat template by @AllentDan in https://github.com/InternLM/lmdeploy/pull/3031
* Fix xcomposer2d5 by @irexyc in https://github.com/InternLM/lmdeploy/pull/3087
### 🌐 Other
* bump version to v0.7.0.post2 by @lvhan028 in https://github.com/InternLM/lmdeploy/pull/3094


**Full Changelog**: https://github.com/InternLM/lmdeploy/compare/v0.7.0.post1...v0.7.0.post2

## v0.7.0.post3 (2025-02-10)

<!-- Release notes generated using configuration in .github/release.yml at main -->

## What's Changed
### 💥 Improvements
* Set max concurrent requests by @AllentDan in https://github.com/InternLM/lmdeploy/pull/2961
* remove logitswarper by @grimoire in https://github.com/InternLM/lmdeploy/pull/3109
### 🐞 Bug fixes
* fix user guide about cogvlm deployment by @lvhan028 in https://github.com/InternLM/lmdeploy/pull/3088
* fix postional argument by @lvhan028 in https://github.com/InternLM/lmdeploy/pull/3086
### 🌐 Other
* [Fix] fix the URL judgment problem in Windows by @Lychee-acaca in https://github.com/InternLM/lmdeploy/pull/3103
* bump version to v0.7.0.post3 by @lvhan028 in https://github.com/InternLM/lmdeploy/pull/3115

## New Contributors
* @Lychee-acaca made their first contribution in https://github.com/InternLM/lmdeploy/pull/3103

**Full Changelog**: https://github.com/InternLM/lmdeploy/compare/v0.7.0.post2...v0.7.0.post3

## v0.7.1 (2025-02-27)

<!-- Release notes generated using configuration in .github/release.yml at main -->

## What's Changed
### 🚀 Features
* support release pipeline by @irexyc in https://github.com/InternLM/lmdeploy/pull/3069
* [feature] add dlinfer w8a8 support. by @Reinerzhou in https://github.com/InternLM/lmdeploy/pull/2988
* [maca] support deepseekv2 for maca backend. by @Reinerzhou in https://github.com/InternLM/lmdeploy/pull/2918
* [Feature] support deepseek-vl2 for pytorch engine by @CUHKSZzxy in https://github.com/InternLM/lmdeploy/pull/3149
### 💥 Improvements
* use weights iterator while loading by @RunningLeon in https://github.com/InternLM/lmdeploy/pull/2886
* Add deepseek-r1 chat template by @AllentDan in https://github.com/InternLM/lmdeploy/pull/3072
* Update tokenizer by @lvhan028 in https://github.com/InternLM/lmdeploy/pull/3061
* Set max concurrent requests by @AllentDan in https://github.com/InternLM/lmdeploy/pull/2961
* remove logitswarper by @grimoire in https://github.com/InternLM/lmdeploy/pull/3109
* Update benchmark script and user guide by @lvhan028 in https://github.com/InternLM/lmdeploy/pull/3110
* support eos_token list in turbomind by @irexyc in https://github.com/InternLM/lmdeploy/pull/3044
* Use aiohttp inside proxy server && add --disable-cache-status argument by @AllentDan in https://github.com/InternLM/lmdeploy/pull/3020
* Update runtime package dependencies by @zgjja in https://github.com/InternLM/lmdeploy/pull/3142
* Make turbomind support embedding inputs on GPU by @chengyuma in https://github.com/InternLM/lmdeploy/pull/3177
### 🐞 Bug fixes
* [dlinfer] fix ascend qwen2_vl graph_mode by @yao-fengchen in https://github.com/InternLM/lmdeploy/pull/3045
* fix error in interactive api by @lvhan028 in https://github.com/InternLM/lmdeploy/pull/3074
* fix sliding window mgr by @grimoire in https://github.com/InternLM/lmdeploy/pull/3068
* More arguments in api_client, update docstrings by @AllentDan in https://github.com/InternLM/lmdeploy/pull/3077
* Add system role to deepseek chat template by @AllentDan in https://github.com/InternLM/lmdeploy/pull/3031
* Fix xcomposer2d5 by @irexyc in https://github.com/InternLM/lmdeploy/pull/3087
* fix user guide about cogvlm deployment by @lvhan028 in https://github.com/InternLM/lmdeploy/pull/3088
* fix postional argument by @lvhan028 in https://github.com/InternLM/lmdeploy/pull/3086
* Fix UT of deepseek chat template by @lvhan028 in https://github.com/InternLM/lmdeploy/pull/3125
* Fix internvl2.5 error after eviction by @grimoire in https://github.com/InternLM/lmdeploy/pull/3122
* Fix cogvlm and phi3vision by @RunningLeon in https://github.com/InternLM/lmdeploy/pull/3137
* [fix] fix vl gradio, use pipeline api and remove interactive chat by @irexyc in https://github.com/InternLM/lmdeploy/pull/3136
* fix the issue that stop_token may be less than defined in model.py by @irexyc in https://github.com/InternLM/lmdeploy/pull/3148
* fix typing by @lz1998 in https://github.com/InternLM/lmdeploy/pull/3153
* fix min length penalty by @irexyc in https://github.com/InternLM/lmdeploy/pull/3150
* fix default temperature value by @irexyc in https://github.com/InternLM/lmdeploy/pull/3166
* Use pad_token_id as image_token_id for vl models by @RunningLeon in https://github.com/InternLM/lmdeploy/pull/3158
* Fix tool call prompt for InternLM and Qwen by @AllentDan in https://github.com/InternLM/lmdeploy/pull/3156
* Update qwen2.py by @GxjGit in https://github.com/InternLM/lmdeploy/pull/3174
* fix temperature=0 by @grimoire in https://github.com/InternLM/lmdeploy/pull/3176
* fix blocked fp8 moe by @grimoire in https://github.com/InternLM/lmdeploy/pull/3181
* fix deepseekv2 has no attribute use_mla error by @CUHKSZzxy in https://github.com/InternLM/lmdeploy/pull/3188
* fix unstoppable chat by @lvhan028 in https://github.com/InternLM/lmdeploy/pull/3189
### 🌐 Other
* [ci] add internlm3 into testcase by @zhulinJulia24 in https://github.com/InternLM/lmdeploy/pull/3038
* add internlm3 to supported models by @lvhan028 in https://github.com/InternLM/lmdeploy/pull/3041
* update pre-commit config by @lvhan028 in https://github.com/InternLM/lmdeploy/pull/2683
* [maca] add cudagraph support on maca backend. by @Reinerzhou in https://github.com/InternLM/lmdeploy/pull/2834
* bump version to v0.7.0.post1 by @lvhan028 in https://github.com/InternLM/lmdeploy/pull/3076
* bump version to v0.7.0.post2 by @lvhan028 in https://github.com/InternLM/lmdeploy/pull/3094
* [Fix] fix the URL judgment problem in Windows by @Lychee-acaca in https://github.com/InternLM/lmdeploy/pull/3103
* bump version to v0.7.0.post3 by @lvhan028 in https://github.com/InternLM/lmdeploy/pull/3115
* [ci] fix some fail in daily testcase by @zhulinJulia24 in https://github.com/InternLM/lmdeploy/pull/3134
* Bump version to v0.7.1 by @lvhan028 in https://github.com/InternLM/lmdeploy/pull/3178

## New Contributors
* @Lychee-acaca made their first contribution in https://github.com/InternLM/lmdeploy/pull/3103
* @lz1998 made their first contribution in https://github.com/InternLM/lmdeploy/pull/3153
* @GxjGit made their first contribution in https://github.com/InternLM/lmdeploy/pull/3174
* @chengyuma made their first contribution in https://github.com/InternLM/lmdeploy/pull/3177
* @CUHKSZzxy made their first contribution in https://github.com/InternLM/lmdeploy/pull/3149

**Full Changelog**: https://github.com/InternLM/lmdeploy/compare/v0.7.0...v0.7.1

## v0.7.2 (2025-03-19)

<!-- Release notes generated using configuration in .github/release.yml at main -->

## What's Changed
### 🚀 Features
* [Feature] support qwen2.5-vl for pytorch engine by @CUHKSZzxy in https://github.com/InternLM/lmdeploy/pull/3194
* Support reward models by @lvhan028 in https://github.com/InternLM/lmdeploy/pull/3192
* Add collective communication kernels by @lzhangzz in https://github.com/InternLM/lmdeploy/pull/3163
* PytorchEngine multi-node support v2 by @grimoire in https://github.com/InternLM/lmdeploy/pull/3147
* Add flash mla by @AllentDan in https://github.com/InternLM/lmdeploy/pull/3218
* Add gemma3 implementation by @AllentDan in https://github.com/InternLM/lmdeploy/pull/3272
### 💥 Improvements
* remove update badwords by @grimoire in https://github.com/InternLM/lmdeploy/pull/3183
* defaullt executor ray by @grimoire in https://github.com/InternLM/lmdeploy/pull/3210
* change ascend&camb default_batch_size to 256 by @jinminxi104 in https://github.com/InternLM/lmdeploy/pull/3251
* Tool reasoning parsers and streaming function call by @AllentDan in https://github.com/InternLM/lmdeploy/pull/3198
* remove torchelastic flag by @grimoire in https://github.com/InternLM/lmdeploy/pull/3242
* disable flashmla warning on sm<90 by @grimoire in https://github.com/InternLM/lmdeploy/pull/3271
### 🐞 Bug fixes
* Fix missing cli chat option by @lzhangzz in https://github.com/InternLM/lmdeploy/pull/3209
* [ascend] fix multi-card distributed inference failures by @tangzhiyi11 in https://github.com/InternLM/lmdeploy/pull/3215
* fix for small cache-max-entry-count by @grimoire in https://github.com/InternLM/lmdeploy/pull/3221
* [dlinfer] fix glm-4v graph mode on ascend by @jinminxi104 in https://github.com/InternLM/lmdeploy/pull/3235
* fix qwen2.5 pytorch engine dtype error on NPU by @tcye in https://github.com/InternLM/lmdeploy/pull/3247
* [Fix] failed to update the tokenizer's eos_token_id into stop_word list by @lvhan028 in https://github.com/InternLM/lmdeploy/pull/3257
* fix dsv3 gate scaling by @grimoire in https://github.com/InternLM/lmdeploy/pull/3263
* Fix the bug for reading dict error by @GxjGit in https://github.com/InternLM/lmdeploy/pull/3196
* Fix get ppl by @lvhan028 in https://github.com/InternLM/lmdeploy/pull/3268
### 📚 Documentations
* Specifiy lmdeploy version in benchmark guide  by @lyj0309 in https://github.com/InternLM/lmdeploy/pull/3216
* [ascend] add Ascend docker image by @jinminxi104 in https://github.com/InternLM/lmdeploy/pull/3239
### 🌐 Other
* [ci] testcase refactoring by @zhulinJulia24 in https://github.com/InternLM/lmdeploy/pull/3151
* [ci] add testcase for native communicator by @zhulinJulia24 in https://github.com/InternLM/lmdeploy/pull/3217
* [ci] add volc evaluation testcase by @zhulinJulia24 in https://github.com/InternLM/lmdeploy/pull/3240
* [ci] remove v100 testconfig by @zhulinJulia24 in https://github.com/InternLM/lmdeploy/pull/3253
* add rdma dependencies into docker file by @CUHKSZzxy in https://github.com/InternLM/lmdeploy/pull/3262
* docs: update ascend docs for docker running by @CyCle1024 in https://github.com/InternLM/lmdeploy/pull/3266
* bump version to v0.7.2 by @lvhan028 in https://github.com/InternLM/lmdeploy/pull/3252

## New Contributors
* @lyj0309 made their first contribution in https://github.com/InternLM/lmdeploy/pull/3216
* @tcye made their first contribution in https://github.com/InternLM/lmdeploy/pull/3247

**Full Changelog**: https://github.com/InternLM/lmdeploy/compare/v0.7.1...v0.7.2

## v0.7.2.post1 (2025-03-21)

<!-- Release notes generated using configuration in .github/release.yml at main -->

## What's Changed
### 💥 Improvements
* Add spaces_between_special_tokens to /v1/interactive and make compatible with empty text by @AllentDan in https://github.com/InternLM/lmdeploy/pull/3283
* add env var to control timeout by @CUHKSZzxy in https://github.com/InternLM/lmdeploy/pull/3291
### 🐞 Bug fixes
* fix activation grid oversize by @grimoire in https://github.com/InternLM/lmdeploy/pull/3282
* Set ensure_ascii=False for tool calling by @AllentDan in https://github.com/InternLM/lmdeploy/pull/3295
### 🌐 Other
* bump version to v0.7.2.post1 by @lvhan028 in https://github.com/InternLM/lmdeploy/pull/3298


**Full Changelog**: https://github.com/InternLM/lmdeploy/compare/v0.7.2...v0.7.2.post1

## v0.7.3 (2025-04-14)

<!-- Release notes generated using configuration in .github/release.yml at dev -->

## What's Changed
### 🚀 Features
* Add Qwen3 and Qwen3MoE by @lzhangzz in https://github.com/InternLM/lmdeploy/pull/3305
* [Feature] support qwen3 and qwen3-moe for pytorch engine by @CUHKSZzxy in https://github.com/InternLM/lmdeploy/pull/3315
* [ascend]support deepseekv2 by @yao-fengchen in https://github.com/InternLM/lmdeploy/pull/3206
* support ascend w8a8 graph_mode by @yao-fengchen in https://github.com/InternLM/lmdeploy/pull/3267
* support Llama4 by @grimoire in https://github.com/InternLM/lmdeploy/pull/3408
### 💥 Improvements
* Add spaces_between_special_tokens to /v1/interactive and make compatible with empty text by @AllentDan in https://github.com/InternLM/lmdeploy/pull/3283
* add env var to control timeout by @CUHKSZzxy in https://github.com/InternLM/lmdeploy/pull/3291
* optimize mla, remove load `v` by @grimoire in https://github.com/InternLM/lmdeploy/pull/3334
* refactor dlinfer rope by @yao-fengchen in https://github.com/InternLM/lmdeploy/pull/3326
* enable qwenvl2.5 graph mode on ascend by @jinminxi104 in https://github.com/InternLM/lmdeploy/pull/3367
* Optimize ascend moe by @yao-fengchen in https://github.com/InternLM/lmdeploy/pull/3364
* find port by @grimoire in https://github.com/InternLM/lmdeploy/pull/3429
### 🐞 Bug fixes
* fix activation grid oversize by @grimoire in https://github.com/InternLM/lmdeploy/pull/3282
* Set ensure_ascii=False for tool calling by @AllentDan in https://github.com/InternLM/lmdeploy/pull/3295
* add `v` check by @grimoire in https://github.com/InternLM/lmdeploy/pull/3307
* Fix Qwen3MoE config parsing by @lzhangzz in https://github.com/InternLM/lmdeploy/pull/3336
* Fix finish reasons by @AllentDan in https://github.com/InternLM/lmdeploy/pull/3338
* remove think_end_token_id in streaming content by @AllentDan in https://github.com/InternLM/lmdeploy/pull/3327
* Fix the finish_reason by @AllentDan in https://github.com/InternLM/lmdeploy/pull/3350
* support List[dict] prompt input without do_preprocess by @irexyc in https://github.com/InternLM/lmdeploy/pull/3385
* fix tensor dispatch in dynamo by @wanfengcxz in https://github.com/InternLM/lmdeploy/pull/3417
### 📚 Documentations
* update ascend doc by @yao-fengchen in https://github.com/InternLM/lmdeploy/pull/3420
### 🌐 Other
* bump version to v0.7.2.post1 by @lvhan028 in https://github.com/InternLM/lmdeploy/pull/3298
* Optimize internvit by @caikun-pjlab in https://github.com/InternLM/lmdeploy/pull/3316
* bump version to v0.7.3 by @lvhan028 in https://github.com/InternLM/lmdeploy/pull/3416

## New Contributors
* @wanfengcxz made their first contribution in https://github.com/InternLM/lmdeploy/pull/3417
* @caikun-pjlab made their first contribution in https://github.com/InternLM/lmdeploy/pull/3316

**Full Changelog**: https://github.com/InternLM/lmdeploy/compare/v0.7.2...v0.7.3

## v0.8.0 (2025-05-04)

<!-- Release notes generated using configuration in .github/release.yml at main -->

## What's Changed
### 🚀 Features
* Torch dp support by @grimoire in https://github.com/InternLM/lmdeploy/pull/3207
* Add deep gemm with tma pre allocated by @AllentDan in https://github.com/InternLM/lmdeploy/pull/3287
* Add mixed DP + TP by @lzhangzz in https://github.com/InternLM/lmdeploy/pull/3229
* Add Qwen3 and Qwen3MoE by @lzhangzz in https://github.com/InternLM/lmdeploy/pull/3305
* [ascend] support multi nodes on ascend device by @tangzhiyi11 in https://github.com/InternLM/lmdeploy/pull/3260
* [Feature] support qwen3 and qwen3-moe for pytorch engine by @CUHKSZzxy in https://github.com/InternLM/lmdeploy/pull/3315
* [ascend]support deepseekv2 by @yao-fengchen in https://github.com/InternLM/lmdeploy/pull/3206
* add deepep by @zhaochaoxing in https://github.com/InternLM/lmdeploy/pull/3313
* support ascend w8a8 graph_mode by @yao-fengchen in https://github.com/InternLM/lmdeploy/pull/3267
* support all2all ep by @zhaochaoxing in https://github.com/InternLM/lmdeploy/pull/3370
* optimize ep in decoding stage by @zhaochaoxing in https://github.com/InternLM/lmdeploy/pull/3383
* Warmup deepgemm by @grimoire in https://github.com/InternLM/lmdeploy/pull/3387
* support Llama4 by @grimoire in https://github.com/InternLM/lmdeploy/pull/3408
* add twomicrobatch support by @SHshenhao in https://github.com/InternLM/lmdeploy/pull/3381
* Support phi4 mini by @RunningLeon in https://github.com/InternLM/lmdeploy/pull/3467
* [Dlinfer][Ascend] support 310P by @JackWeiw in https://github.com/InternLM/lmdeploy/pull/3484
* support qwen3 fp8 by @CUHKSZzxy in https://github.com/InternLM/lmdeploy/pull/3505
### 💥 Improvements
* Add spaces_between_special_tokens to /v1/interactive and make compatible with empty text by @AllentDan in https://github.com/InternLM/lmdeploy/pull/3283
* add env var to control timeout by @CUHKSZzxy in https://github.com/InternLM/lmdeploy/pull/3291
* refactor attn param by @irexyc in https://github.com/InternLM/lmdeploy/pull/3164
* Verbose log by @grimoire in https://github.com/InternLM/lmdeploy/pull/3329
* optimize mla, remove load `v` by @grimoire in https://github.com/InternLM/lmdeploy/pull/3334
* support dp decoding with cudagraph by @grimoire in https://github.com/InternLM/lmdeploy/pull/3311
* optimize quant-fp8 kernel by @grimoire in https://github.com/InternLM/lmdeploy/pull/3345
* refactor dlinfer rope by @yao-fengchen in https://github.com/InternLM/lmdeploy/pull/3326
* enable qwenvl2.5 graph mode on ascend by @jinminxi104 in https://github.com/InternLM/lmdeploy/pull/3367
* Add AIOHTTP_TIMEOUT env var for proxy server by @AllentDan in https://github.com/InternLM/lmdeploy/pull/3355
* disable sync batch on dp eager mode by @grimoire in https://github.com/InternLM/lmdeploy/pull/3382
* fix for deepgemm update by @grimoire in https://github.com/InternLM/lmdeploy/pull/3380
* Add string before hash tokens in blocktrie by @RunningLeon in https://github.com/InternLM/lmdeploy/pull/3386
* optimize moe get sorted idx by @grimoire in https://github.com/InternLM/lmdeploy/pull/3356
* use half/bf16 lm_head output by @irexyc in https://github.com/InternLM/lmdeploy/pull/3213
* remove ep eager check by @grimoire in https://github.com/InternLM/lmdeploy/pull/3392
* Optimize ascend moe by @yao-fengchen in https://github.com/InternLM/lmdeploy/pull/3364
* optimize fp8 moe kernel by @grimoire in https://github.com/InternLM/lmdeploy/pull/3419
* ray async forward execute by @grimoire in https://github.com/InternLM/lmdeploy/pull/3443
* map internvl3 chat template to builtin chat template internvl2_5 by @lvhan028 in https://github.com/InternLM/lmdeploy/pull/3450
* Refactor turbomind (low-level abstractions) by @lzhangzz in https://github.com/InternLM/lmdeploy/pull/3423
* remove barely used code to improve maintenance by @lvhan028 in https://github.com/InternLM/lmdeploy/pull/3462
* optimize sm80 long context by @grimoire in https://github.com/InternLM/lmdeploy/pull/3465
* move partial_json_parser from ’serve.txt‘ to ‘runtime.txt‘ by @lvhan028 in https://github.com/InternLM/lmdeploy/pull/3493
* support qwen3-dense models awq quantization by @lvhan028 in https://github.com/InternLM/lmdeploy/pull/3503
* Optimize MoE gate for Qwen3 by @lzhangzz in https://github.com/InternLM/lmdeploy/pull/3500
* Pass num_tokens_per_iter and max_prefill_iters params through in `lmdeploy serve api_server` by @josephrocca in https://github.com/InternLM/lmdeploy/pull/3504
* [Dlinfer][Ascend] Optimize performance of 310P device by @JackWeiw in https://github.com/InternLM/lmdeploy/pull/3486
* optimize longcontext decoding by @grimoire in https://github.com/InternLM/lmdeploy/pull/3510
* Support min_p in openai completions_v1 by @josephrocca in https://github.com/InternLM/lmdeploy/pull/3506
### 🐞 Bug fixes
* fix activation grid oversize by @grimoire in https://github.com/InternLM/lmdeploy/pull/3282
* Set ensure_ascii=False for tool calling by @AllentDan in https://github.com/InternLM/lmdeploy/pull/3295
* fix sliding window multi chat by @grimoire in https://github.com/InternLM/lmdeploy/pull/3302
* add `v` check by @grimoire in https://github.com/InternLM/lmdeploy/pull/3307
* Fix Qwen3MoE config parsing by @lzhangzz in https://github.com/InternLM/lmdeploy/pull/3336
* Fix finish reasons by @AllentDan in https://github.com/InternLM/lmdeploy/pull/3338
* remove think_end_token_id in streaming content by @AllentDan in https://github.com/InternLM/lmdeploy/pull/3327
* Fix the finish_reason by @AllentDan in https://github.com/InternLM/lmdeploy/pull/3350
* set cmake policy minimum version as 3.5 by @lvhan028 in https://github.com/InternLM/lmdeploy/pull/3376
* fix dp cudagraph by @grimoire in https://github.com/InternLM/lmdeploy/pull/3372
* fix flashmla eagermode by @grimoire in https://github.com/InternLM/lmdeploy/pull/3375
* close engine after each benchmark-generation iter  by @grimoire in https://github.com/InternLM/lmdeploy/pull/3269
* [Fix] fix `image_token_id` error of qwen2-vl and deepseek by @ao-zz in https://github.com/InternLM/lmdeploy/pull/3358
* fix stopping criteria by @grimoire in https://github.com/InternLM/lmdeploy/pull/3384
* support List[dict] prompt input without do_preprocess by @irexyc in https://github.com/InternLM/lmdeploy/pull/3385
* add rayexecutor release timeout by @grimoire in https://github.com/InternLM/lmdeploy/pull/3403
* fix tensor dispatch in dynamo by @wanfengcxz in https://github.com/InternLM/lmdeploy/pull/3417
* fix linting error by upgrade to ubuntu-latest by @lvhan028 in https://github.com/InternLM/lmdeploy/pull/3442
* fix awq tp for pytorch engine by @RunningLeon in https://github.com/InternLM/lmdeploy/pull/3435
* fix mllm testcase fail by @caikun-pjlab in https://github.com/InternLM/lmdeploy/pull/3458
* remove paged attention autotune by @grimoire in https://github.com/InternLM/lmdeploy/pull/3452
* Remove empty prompts in benchmark scripts by @lvhan028 in https://github.com/InternLM/lmdeploy/pull/3460
* failed to end session properly by @lvhan028 in https://github.com/InternLM/lmdeploy/pull/3471
* fix qwen2.5-vl chat template by @CUHKSZzxy in https://github.com/InternLM/lmdeploy/pull/3475
* Align forward arguments of deepgemm blockedf8 by @RunningLeon in https://github.com/InternLM/lmdeploy/pull/3474
* fix turbomind lib missing to link nccl by exporting nccl path by @lvhan028 in https://github.com/InternLM/lmdeploy/pull/3479
* fix dsvl2 no attr config error by @CUHKSZzxy in https://github.com/InternLM/lmdeploy/pull/3477
* fix flash attention crash on triton3.1.0 by @grimoire in https://github.com/InternLM/lmdeploy/pull/3478
* Fix disorder of ray execution by @RunningLeon in https://github.com/InternLM/lmdeploy/pull/3481
* update dockerfile by @CUHKSZzxy in https://github.com/InternLM/lmdeploy/pull/3482
* fix output logprobs by @irexyc in https://github.com/InternLM/lmdeploy/pull/3488
* Fix Qwen2MoE shared expert gate by @lzhangzz in https://github.com/InternLM/lmdeploy/pull/3491
* fix replicate kv for qwen3-moe by @grimoire in https://github.com/InternLM/lmdeploy/pull/3499
* fix sampling if data overflow after temperature penalty by @irexyc in https://github.com/InternLM/lmdeploy/pull/3508
### 📚 Documentations
* update qwen2.5-vl-32b docs by @CUHKSZzxy in https://github.com/InternLM/lmdeploy/pull/3446
### 🌐 Other
* bump version to v0.7.2.post1 by @lvhan028 in https://github.com/InternLM/lmdeploy/pull/3298
* [ci] add think function testcase by @zhulinJulia24 in https://github.com/InternLM/lmdeploy/pull/3299
* merge dev into main by @lvhan028 in https://github.com/InternLM/lmdeploy/pull/3348
* [ci] add vl models into pipeline interface testcase by @zhulinJulia24 in https://github.com/InternLM/lmdeploy/pull/3374
* merge dev to main branch by @lvhan028 in https://github.com/InternLM/lmdeploy/pull/3378
* opt experts memory and permute by @zhaochaoxing in https://github.com/InternLM/lmdeploy/pull/3390
* Revert "opt experts memory and permute" by @zhaochaoxing in https://github.com/InternLM/lmdeploy/pull/3406
* merge dev to main by @lvhan028 in https://github.com/InternLM/lmdeploy/pull/3400
* add Hopper GPU dockerfile by @CUHKSZzxy in https://github.com/InternLM/lmdeploy/pull/3415
* optimize internvit by @caikun-pjlab in https://github.com/InternLM/lmdeploy/pull/3433
* fix stop/bad words by @irexyc in https://github.com/InternLM/lmdeploy/pull/3492
* [ci] testcase bugfix and add more models into testcase by @zhulinJulia24 in https://github.com/InternLM/lmdeploy/pull/3463
* bump version to v0.8.0 by @lvhan028 in https://github.com/InternLM/lmdeploy/pull/3432

## New Contributors
* @zhaochaoxing made their first contribution in https://github.com/InternLM/lmdeploy/pull/3313
* @ao-zz made their first contribution in https://github.com/InternLM/lmdeploy/pull/3358
* @wanfengcxz made their first contribution in https://github.com/InternLM/lmdeploy/pull/3417
* @SHshenhao made their first contribution in https://github.com/InternLM/lmdeploy/pull/3381
* @josephrocca made their first contribution in https://github.com/InternLM/lmdeploy/pull/3504

**Full Changelog**: https://github.com/InternLM/lmdeploy/compare/v0.7.2...v0.8.0

## v0.9.0 (2025-06-19)

<!-- Release notes generated using configuration in .github/release.yml at main -->

## What's Changed
### 🚀 Features
* LMDeploy Distserve by @JimyMa in https://github.com/InternLM/lmdeploy/pull/3304
* allow api server terminated through requests from clients by @RunningLeon in https://github.com/InternLM/lmdeploy/pull/3533
* support update params for pytorch backend from api server by @irexyc in https://github.com/InternLM/lmdeploy/pull/3535
* support eplb for Qwen3-MoE by @zhaochaoxing in https://github.com/InternLM/lmdeploy/pull/3582
* support update params for turbomind backend by @irexyc in https://github.com/InternLM/lmdeploy/pull/3566
* Quantize Qwen3 MoE bf16 model to fp8 model at runtime by @grimoire in https://github.com/InternLM/lmdeploy/pull/3631
* [Feat]: Support internvl3-8b-hf by @RunningLeon in https://github.com/InternLM/lmdeploy/pull/3633
* Add FP8 MoE for turbomind by @lzhangzz in https://github.com/InternLM/lmdeploy/pull/3601
### 💥 Improvements
* reduce ray memory usage by @grimoire in https://github.com/InternLM/lmdeploy/pull/3487
* use dlblas by @zhaochaoxing in https://github.com/InternLM/lmdeploy/pull/3489
* internlm3 dense fp8 by @CUHKSZzxy in https://github.com/InternLM/lmdeploy/pull/3527
* random pad input ids by @grimoire in https://github.com/InternLM/lmdeploy/pull/3530
* ray nsys profile support by @grimoire in https://github.com/InternLM/lmdeploy/pull/3448
* update blockedfp8 scale name by @CUHKSZzxy in https://github.com/InternLM/lmdeploy/pull/3532
* start engine loop on server startup event by @grimoire in https://github.com/InternLM/lmdeploy/pull/3523
* update two microbatch by @SHshenhao in https://github.com/InternLM/lmdeploy/pull/3540
* [ascend]set transdata dynamic shape true by @JackWeiw in https://github.com/InternLM/lmdeploy/pull/3531
* ray safe exit by @grimoire in https://github.com/InternLM/lmdeploy/pull/3545
* support update params with dp=1 for pytorch engine by @irexyc in https://github.com/InternLM/lmdeploy/pull/3562
* Skip dp dummy input forward by @grimoire in https://github.com/InternLM/lmdeploy/pull/3552
* Unclock mutual exclusivity of argument:  `tool-call-parser` and `reasoning-parser` by @jingyibo123 in https://github.com/InternLM/lmdeploy/pull/3550
* perform torch.cuda.empty_cache() after conversion by @bltcn in https://github.com/InternLM/lmdeploy/pull/3570
* pipeline warmup by @irexyc in https://github.com/InternLM/lmdeploy/pull/3548
* Launch multiple api servers for dp > 1 by @RunningLeon in https://github.com/InternLM/lmdeploy/pull/3414
* support awq for Qwen2.5-VL  by @RunningLeon in https://github.com/InternLM/lmdeploy/pull/3559
* support qwen3 /think & /no_think & enable_thinking parameter by @BUJIDAOVS in https://github.com/InternLM/lmdeploy/pull/3564
* Eplb by @zhaochaoxing in https://github.com/InternLM/lmdeploy/pull/3572
* Update benchmark by @lvhan028 in https://github.com/InternLM/lmdeploy/pull/3578
* block output when prefetch next forward inputs. by @grimoire in https://github.com/InternLM/lmdeploy/pull/3573
* support both eplb and microbatch simultaneously by @zhaochaoxing in https://github.com/InternLM/lmdeploy/pull/3591
* Add log_file and set loglevel in launch_servers by @RunningLeon in https://github.com/InternLM/lmdeploy/pull/3596
* 1. add migration flow control by @JimyMa in https://github.com/InternLM/lmdeploy/pull/3599
* sampling on the tokenizer's vocab by @grimoire in https://github.com/InternLM/lmdeploy/pull/3604
* update deepgemm version by @grimoire in https://github.com/InternLM/lmdeploy/pull/3606
* [Ascend] set default distrbuted backend as ray for ascend device by @JackWeiw in https://github.com/InternLM/lmdeploy/pull/3603
* Blocked fp8 tma by @grimoire in https://github.com/InternLM/lmdeploy/pull/3470
* [PDDisaggreagtion] Async migration by @JimyMa in https://github.com/InternLM/lmdeploy/pull/3610
* move dp loop to model agent by @grimoire in https://github.com/InternLM/lmdeploy/pull/3598
* update some logs of proxy_server and pt engine by @lvhan028 in https://github.com/InternLM/lmdeploy/pull/3621
* improve loading model performance by shuffling the weight files by @irexyc in https://github.com/InternLM/lmdeploy/pull/3625
* add benchmark scripts about pipeline api and inference engines according to the config file by @lvhan028 in https://github.com/InternLM/lmdeploy/pull/3622
### 🐞 Bug fixes
* [ascend] fix recompile on different rank by @jinminxi104 in https://github.com/InternLM/lmdeploy/pull/3513
* fix attention sm86 by @grimoire in https://github.com/InternLM/lmdeploy/pull/3519
* fix stopwords kv cache by @grimoire in https://github.com/InternLM/lmdeploy/pull/3494
* [bug fix] fix PD Disaggregation in DSV3 by @JimyMa in https://github.com/InternLM/lmdeploy/pull/3547
* fix proxy server heart beat by @irexyc in https://github.com/InternLM/lmdeploy/pull/3543
* fix dp>1 tp=1 ep=1 by @grimoire in https://github.com/InternLM/lmdeploy/pull/3555
* fix mixtral on new transformers by @grimoire in https://github.com/InternLM/lmdeploy/pull/3580
* [Fix]: reset step after eviction by @RunningLeon in https://github.com/InternLM/lmdeploy/pull/3589
* fix parsing dynamic rope param failed by @lvhan028 in https://github.com/InternLM/lmdeploy/pull/3575
* Fix batch infer for gemma3vl by @RunningLeon in https://github.com/InternLM/lmdeploy/pull/3592
* Fix symbol error when dlBLAS is not imported by @zhaochaoxing in https://github.com/InternLM/lmdeploy/pull/3597
* read distributed envs by @grimoire in https://github.com/InternLM/lmdeploy/pull/3600
* fix side-effect caused by PR 3590 by @lvhan028 in https://github.com/InternLM/lmdeploy/pull/3608
* fix bug in qwen2 by @LKJacky in https://github.com/InternLM/lmdeploy/pull/3614
* fix awq kernel by @grimoire in https://github.com/InternLM/lmdeploy/pull/3618
* fix flash mla interface by @grimoire in https://github.com/InternLM/lmdeploy/pull/3617
* add sampling_vocab_size by @irexyc in https://github.com/InternLM/lmdeploy/pull/3607
* fix for default quant by @grimoire in https://github.com/InternLM/lmdeploy/pull/3640
* Fix log file env in ray worker by @RunningLeon in https://github.com/InternLM/lmdeploy/pull/3624
* fix qwen3 chat template by @lvhan028 in https://github.com/InternLM/lmdeploy/pull/3641
* fix vlm runtime quant by @grimoire in https://github.com/InternLM/lmdeploy/pull/3644
* Fix 'Namespace' object has no attribute 'num_tokens_per_iter' when serving by gradio by @lvhan028 in https://github.com/InternLM/lmdeploy/pull/3647
* Synchronize weight processing by @lzhangzz in https://github.com/InternLM/lmdeploy/pull/3649
* Fix zero scale in fp8 quantization by @lzhangzz in https://github.com/InternLM/lmdeploy/pull/3652
### 🌐 Other
* update doc for  ascend 300I Duo docker image by @jinminxi104 in https://github.com/InternLM/lmdeploy/pull/3526
* simulate EPLB for benchmark only by @lvhan028 in https://github.com/InternLM/lmdeploy/pull/3490
* [ci] add test workflow for 3090 machine by @zhulinJulia24 in https://github.com/InternLM/lmdeploy/pull/3561
* [ci] fix transformers version in prtest by @zhulinJulia24 in https://github.com/InternLM/lmdeploy/pull/3584
* [Misc] minor api_server and tm loader, and upgrade docformatter to resolve lint error by @lvhan028 in https://github.com/InternLM/lmdeploy/pull/3590
* [ci] add qwen3 models into testcase by @zhulinJulia24 in https://github.com/InternLM/lmdeploy/pull/3593
* update Dockerfile by @CUHKSZzxy in https://github.com/InternLM/lmdeploy/pull/3634
* check in lmdeploy-builder on cuda 12.4 and 12.8 platform by @lvhan028 in https://github.com/InternLM/lmdeploy/pull/3630
* fix blocked fp8 overflow by @grimoire in https://github.com/InternLM/lmdeploy/pull/3650
* Bump version to v0.9.0 by @lvhan028 in https://github.com/InternLM/lmdeploy/pull/3609

## New Contributors
* @JimyMa made their first contribution in https://github.com/InternLM/lmdeploy/pull/3304
* @jingyibo123 made their first contribution in https://github.com/InternLM/lmdeploy/pull/3550
* @bltcn made their first contribution in https://github.com/InternLM/lmdeploy/pull/3570
* @BUJIDAOVS made their first contribution in https://github.com/InternLM/lmdeploy/pull/3564
* @LKJacky made their first contribution in https://github.com/InternLM/lmdeploy/pull/3614

**Full Changelog**: https://github.com/InternLM/lmdeploy/compare/v0.8.0...v0.9.0

## v0.9.1 (2025-07-04)

<!-- Release notes generated using configuration in .github/release.yml at main -->

## What's Changed
### 🚀 Features
* feature: enable tool_call and reasoning_content parsing for qwen3 by @ywx217 in https://github.com/InternLM/lmdeploy/pull/3615
* Support Mooncake migration backend for PD disaggregation by @Risc-lt in https://github.com/InternLM/lmdeploy/pull/3620
* Support load fused moe weights by @RunningLeon in https://github.com/InternLM/lmdeploy/pull/3672
* Seperate api_server and pytorch engine into different processors by @grimoire in https://github.com/InternLM/lmdeploy/pull/3627
* add reward model api by @CUHKSZzxy in https://github.com/InternLM/lmdeploy/pull/3665
### 💥 Improvements
* [ascend]import patch at initiazing time by @JackWeiw in https://github.com/InternLM/lmdeploy/pull/3662
* [ascend]use custon transdata in python kernel by @JackWeiw in https://github.com/InternLM/lmdeploy/pull/3671
* move import transformers in patch by @grimoire in https://github.com/InternLM/lmdeploy/pull/3660
* set ray envs by @grimoire in https://github.com/InternLM/lmdeploy/pull/3643
* raise ImportError when enable ep and not install dlblas by @zhaochaoxing in https://github.com/InternLM/lmdeploy/pull/3636
* Reduce sampling memory usage by @lzhangzz in https://github.com/InternLM/lmdeploy/pull/3666
### 🐞 Bug fixes
* fix dockerfile by @lvhan028 in https://github.com/InternLM/lmdeploy/pull/3657
* Fix top-p only sampling with padded vocab size by @lzhangzz in https://github.com/InternLM/lmdeploy/pull/3661
* fix pt engine stop & cancel by @irexyc in https://github.com/InternLM/lmdeploy/pull/3681
* Fix convert bf16 to numpy by @RunningLeon in https://github.com/InternLM/lmdeploy/pull/3686
* disable torch.compile in cuda graph runner by @grimoire in https://github.com/InternLM/lmdeploy/pull/3691
* fix reward model api by @CUHKSZzxy in https://github.com/InternLM/lmdeploy/pull/3703
### 📚 Documentations
* add reward model documents by @CUHKSZzxy in https://github.com/InternLM/lmdeploy/pull/3706
### 🌐 Other
* upgrade torch and triton by @grimoire in https://github.com/InternLM/lmdeploy/pull/3677
* support do_preprocess=False for chat.completions by @irexyc in https://github.com/InternLM/lmdeploy/pull/3645
* [ci] change flash atten installation in pr test by @zhulinJulia24 in https://github.com/InternLM/lmdeploy/pull/3688
* fix profile_throughput.py by @irexyc in https://github.com/InternLM/lmdeploy/pull/3692
* fix profile_generation.py by @irexyc in https://github.com/InternLM/lmdeploy/pull/3707
* update dlblas version in dockerfile by @CUHKSZzxy in https://github.com/InternLM/lmdeploy/pull/3711
* bump version to v0.9.1 by @lvhan028 in https://github.com/InternLM/lmdeploy/pull/3685

## New Contributors
* @ywx217 made their first contribution in https://github.com/InternLM/lmdeploy/pull/3615
* @Risc-lt made their first contribution in https://github.com/InternLM/lmdeploy/pull/3620

**Full Changelog**: https://github.com/InternLM/lmdeploy/compare/v0.9.0...v0.9.1

## v0.9.2 (2025-07-26)

<!-- Release notes generated using configuration in .github/release.yml at main -->

## What's Changed
### 🚀 Features
* [Feature] metrics support by @CUHKSZzxy in https://github.com/InternLM/lmdeploy/pull/3534
* Relax FP8 TP requirement by @lzhangzz in https://github.com/InternLM/lmdeploy/pull/3697
* FA3 by @zhaochaoxing in https://github.com/InternLM/lmdeploy/pull/3623
* support qwen2/2.5-vl in turbomind by @irexyc in https://github.com/InternLM/lmdeploy/pull/3744
* feat: add pytorch_engine_qwen2_5vl_sm120 by @kolmogorov-quyet in https://github.com/InternLM/lmdeploy/pull/3750
* Internvl pt by @RunningLeon in https://github.com/InternLM/lmdeploy/pull/3765
* Improve internvl for turbomind engine by @lvhan028 in https://github.com/InternLM/lmdeploy/pull/3769
### 💥 Improvements
* Refactor linear by @grimoire in https://github.com/InternLM/lmdeploy/pull/3653
* remove python3.8 support and add python3.13 support by @lvhan028 in https://github.com/InternLM/lmdeploy/pull/3638
* refactor vl inputs split by @grimoire in https://github.com/InternLM/lmdeploy/pull/3699
* [Fix]: Replace mutable default with default_factory for scheduler_stats by @ConvolutedDog in https://github.com/InternLM/lmdeploy/pull/3730
* Fix the logic of calculating max_new_tokens and determining finish_reason by @lvhan028 in https://github.com/InternLM/lmdeploy/pull/3727
* Override HF config.json via CLI by @CUHKSZzxy in https://github.com/InternLM/lmdeploy/pull/3722
* feat(build): Integrate and build turbomind backend directly in setup.py by @windreamer in https://github.com/InternLM/lmdeploy/pull/3726
* Generate the benchmark output filename with given arguments by @lvhan028 in https://github.com/InternLM/lmdeploy/pull/3740
* Make loading llm without vlm as an option by @grimoire in https://github.com/InternLM/lmdeploy/pull/3745
### 🐞 Bug fixes
* add ray to ascend requirements by @sigma-plus in https://github.com/InternLM/lmdeploy/pull/3713
* fix accessing undefined attribute `seq_aux` of deepseek-r1-0528 by @lvhan028 in https://github.com/InternLM/lmdeploy/pull/3728
* [Fix]: Avoid quantize qk norm for qwen3 dense models by @taishan1994 in https://github.com/InternLM/lmdeploy/pull/3733
* fix py313 env creation failed when building lmdeploy-builder image by @lvhan028 in https://github.com/InternLM/lmdeploy/pull/3739
* [Fix]: kernel meta retrieval for SM7X does not work by @xiaoajie738 in https://github.com/InternLM/lmdeploy/pull/3746
* limit max_session_len by @grimoire in https://github.com/InternLM/lmdeploy/pull/3751
* fix internvl norm by @grimoire in https://github.com/InternLM/lmdeploy/pull/3756
* support qwen3 moe yarn and vlm hf_overrides by @grimoire in https://github.com/InternLM/lmdeploy/pull/3757
* [PD Disaggregation] fix double unshelf by @JimyMa in https://github.com/InternLM/lmdeploy/pull/3762
* fix(build): fix version parse regex to support post-release versions by @windreamer in https://github.com/InternLM/lmdeploy/pull/3764
* adapt transformers>=v4.52.0 to loading qwen2.5-vl with turbomind by @irexyc in https://github.com/InternLM/lmdeploy/pull/3771
* fix chat template with tool call by @RunningLeon in https://github.com/InternLM/lmdeploy/pull/3773
* fix vl nothink mode by @RunningLeon in https://github.com/InternLM/lmdeploy/pull/3776
### 📚 Documentations
* update reward model docs by @CUHKSZzxy in https://github.com/InternLM/lmdeploy/pull/3721
### 🌐 Other
* update twomicrobatch by @SHshenhao in https://github.com/InternLM/lmdeploy/pull/3651
* [CI]: Upgrade to py310 for ut by @RunningLeon in https://github.com/InternLM/lmdeploy/pull/3718
* [ci] update dailytest environment and scripts by @zhulinJulia24 in https://github.com/InternLM/lmdeploy/pull/3716
* Preliminary Blackwell (sm_120a, RTX 50 series) support by @lzhangzz in https://github.com/InternLM/lmdeploy/pull/3701
* [ci] add fp8 evaluation workflow by @zhulinJulia24 in https://github.com/InternLM/lmdeploy/pull/3729
* Add VRAM bandwidth utilization stat to attention test by @lzhangzz in https://github.com/InternLM/lmdeploy/pull/3731
* doc: fix dead links to MindX DL to recover CI. by @windreamer in https://github.com/InternLM/lmdeploy/pull/3741
* fix free cache in MPEngine branch by @JimyMa in https://github.com/InternLM/lmdeploy/pull/3670
* fix: make RelWithDebInfo default cmake build type by @windreamer in https://github.com/InternLM/lmdeploy/pull/3774
* bump version to v0.9.2 by @lvhan028 in https://github.com/InternLM/lmdeploy/pull/3770

## New Contributors
* @sigma-plus made their first contribution in https://github.com/InternLM/lmdeploy/pull/3713
* @ConvolutedDog made their first contribution in https://github.com/InternLM/lmdeploy/pull/3730
* @windreamer made their first contribution in https://github.com/InternLM/lmdeploy/pull/3726
* @taishan1994 made their first contribution in https://github.com/InternLM/lmdeploy/pull/3733
* @xiaoajie738 made their first contribution in https://github.com/InternLM/lmdeploy/pull/3746
* @kolmogorov-quyet made their first contribution in https://github.com/InternLM/lmdeploy/pull/3750

**Full Changelog**: https://github.com/InternLM/lmdeploy/compare/v0.9.1...v0.9.2

## v0.9.2.post1 (2025-08-19)

<!-- Release notes generated using configuration in .github/release.yml at dev-0.9.2post1 -->

## What's Changed

* Fix interns1 LLM mapping for turbomind engine by @lvhan028 in https://github.com/InternLM/lmdeploy/pull/3848
* bump version to v0.9.2.post1 by @lvhan028 in https://github.com/InternLM/lmdeploy/pull/3849


**Full Changelog**: https://github.com/InternLM/lmdeploy/compare/v0.9.2...v0.9.2.post1

## v0.10.0 (2025-09-09)

<!-- Release notes generated using configuration in .github/release.yml at main -->

## What's Changed
### 🚀 Features
* support offloading weights & kv_cache for turbomind by @irexyc in https://github.com/InternLM/lmdeploy/pull/3798
* Add PPU backend support  by @guozixu2001 in https://github.com/InternLM/lmdeploy/pull/3807
* Add turbomind metrics by @lvhan028 in https://github.com/InternLM/lmdeploy/pull/3811
* PytorchEngine support gpt-oss bf16 by @grimoire in https://github.com/InternLM/lmdeploy/pull/3820
* support sleep/wakeup for pt engine by @irexyc in https://github.com/InternLM/lmdeploy/pull/3687
* [ascend] run intern-s1 on A3 by @yao-fengchen in https://github.com/InternLM/lmdeploy/pull/3831
* Initial gpt-oss support for turbomind by @lzhangzz in https://github.com/InternLM/lmdeploy/pull/3839
* Support GLM-4-0414 and GLM-4.1V by @CUHKSZzxy in https://github.com/InternLM/lmdeploy/pull/3846
* support internvl3.5 by @lvhan028 in https://github.com/InternLM/lmdeploy/pull/3886
* Update turbomind communication library by @lzhangzz in https://github.com/InternLM/lmdeploy/pull/3736
* MXFP4 support for turbomind GEMM library by @lzhangzz in https://github.com/InternLM/lmdeploy/pull/3927
* Dispatch MXFP4 weight conversion for sm70 & sm75 by @lzhangzz in https://github.com/InternLM/lmdeploy/pull/3937
### 💥 Improvements
* fix: turbomind backend config in cli serve by @PeymanRM in https://github.com/InternLM/lmdeploy/pull/3784
* remove deprecated codes by @lvhan028 in https://github.com/InternLM/lmdeploy/pull/3759
* Refactor FP8 MoE GEMM by @lzhangzz in https://github.com/InternLM/lmdeploy/pull/3795
* Fix build rope params by @grimoire in https://github.com/InternLM/lmdeploy/pull/3760
* Optimize rmsnorm with head_dim=128 by @grimoire in https://github.com/InternLM/lmdeploy/pull/3814
* Simplify GEMM interface by @lzhangzz in https://github.com/InternLM/lmdeploy/pull/3818
* Optimize create_model_inputs and schedule_decoding by @grimoire in https://github.com/InternLM/lmdeploy/pull/3766
* add remote logs;optimize forward lock by @grimoire in https://github.com/InternLM/lmdeploy/pull/3737
* support deepgemm new api by @grimoire in https://github.com/InternLM/lmdeploy/pull/3827
* remove serving with gradio by @lvhan028 in https://github.com/InternLM/lmdeploy/pull/3829
* Deprecate interactive mode from api_server by @lvhan028 in https://github.com/InternLM/lmdeploy/pull/3830
* build(docker): Try to optimize docker by @windreamer in https://github.com/InternLM/lmdeploy/pull/3779
* Make a common chat.py to replace each engine's by @lvhan028 in https://github.com/InternLM/lmdeploy/pull/3836
* Ray mp engine backend by @grimoire in https://github.com/InternLM/lmdeploy/pull/3790
* [Feat] support using external ray pg with bundles by @CyCle1024 in https://github.com/InternLM/lmdeploy/pull/3850
* Remove unused code in PT Engine by @grimoire in https://github.com/InternLM/lmdeploy/pull/3858
* support logprobs by @grimoire in https://github.com/InternLM/lmdeploy/pull/3852
* optimize prefill preprocess by @grimoire in https://github.com/InternLM/lmdeploy/pull/3869
* fix flash-attn bc by @grimoire in https://github.com/InternLM/lmdeploy/pull/3873
* Graph warmup by @grimoire in https://github.com/InternLM/lmdeploy/pull/3851
* Improve turbomind's prefix cache by @lvhan028 in https://github.com/InternLM/lmdeploy/pull/3835
* Support OpenAI compatible parameter max_completion_tokens by @Huarong in https://github.com/InternLM/lmdeploy/pull/3876
* [ascend] add env to set rt visable by ray and disable warmup by @tangzhiyi11 in https://github.com/InternLM/lmdeploy/pull/3894
* support cache_max_entry_count >= 1 for Turbomind backend by @lh9171338 in https://github.com/InternLM/lmdeploy/pull/3913
* adjust default values by @lvhan028 in https://github.com/InternLM/lmdeploy/pull/3921
* [refactor][chat_template][1/N] adopt tokenizer's apply_chat_template by @lvhan028 in https://github.com/InternLM/lmdeploy/pull/3845
* use FA 2.8.3 which is compatible with torch 2.8.0 by @lvhan028 in https://github.com/InternLM/lmdeploy/pull/3936
* refactor ascend Dockerfile by @yao-fengchen in https://github.com/InternLM/lmdeploy/pull/3926
### 🐞 Bug fixes
* fix gemma3 by @grimoire in https://github.com/InternLM/lmdeploy/pull/3772
* fix head_dim=None by @grimoire in https://github.com/InternLM/lmdeploy/pull/3793
* fix user-specified max_session_len by @grimoire in https://github.com/InternLM/lmdeploy/pull/3785
* remove 'lmdeploy convert' from CLI by @lvhan028 in https://github.com/InternLM/lmdeploy/pull/3813
* Fix EP with large batch size by @grimoire in https://github.com/InternLM/lmdeploy/pull/3808
* fix internvl disable_vision_encoder by @grimoire in https://github.com/InternLM/lmdeploy/pull/3800
* Align response behavior across both engines by @lvhan028 in https://github.com/InternLM/lmdeploy/pull/3821
* fix: set text_config.tie_word_embedding = False in qwen2vl by @zenosai in https://github.com/InternLM/lmdeploy/pull/3824
* Fix v1 comp protocol by @CUHKSZzxy in https://github.com/InternLM/lmdeploy/pull/3828
* [dlinfer] fix get_backend err by @yao-fengchen in https://github.com/InternLM/lmdeploy/pull/3847
* Update internvl.py to fix InternLM/lmdeploy#3528 by @zodiacg in https://github.com/InternLM/lmdeploy/pull/3837
* fix partial rotary factor by @CUHKSZzxy in https://github.com/InternLM/lmdeploy/pull/3861
* fix: duplicated token usage in /chat/completions stream mode by @Huarong in https://github.com/InternLM/lmdeploy/pull/3859
* fix chatting with VLM model via CLI by @lvhan028 in https://github.com/InternLM/lmdeploy/pull/3862
* fix inference on windows platform by @irexyc in https://github.com/InternLM/lmdeploy/pull/3865
* fix prebuild on cuda12.8 by @lvhan028 in https://github.com/InternLM/lmdeploy/pull/3857
* Fix uninitialized members in cuBLAS wrapper by @lzhangzz in https://github.com/InternLM/lmdeploy/pull/3874
* fix flashmla build for cuda12.4 by @CUHKSZzxy in https://github.com/InternLM/lmdeploy/pull/3872
* [Fix] ray mp engine on ascend platform by @CyCle1024 in https://github.com/InternLM/lmdeploy/pull/3877
* fix bug: leaves empty by @Tsundoku958 in https://github.com/InternLM/lmdeploy/pull/3868
* Fix side effect brought by gpt-oss support by @lvhan028 in https://github.com/InternLM/lmdeploy/pull/3880
* fix pytorch metrics in mp engine by @CUHKSZzxy in https://github.com/InternLM/lmdeploy/pull/3882
* Fix stream assert error when wakeup 30+ times by @CyCle1024 in https://github.com/InternLM/lmdeploy/pull/3883
* fix batched prefill by @grimoire in https://github.com/InternLM/lmdeploy/pull/3887
* fix side effect brought by #3821 by @lvhan028 in https://github.com/InternLM/lmdeploy/pull/3888
* check_env in multiprocess by @grimoire in https://github.com/InternLM/lmdeploy/pull/3879
* fix cli serve --help by @RunningLeon in https://github.com/InternLM/lmdeploy/pull/3895
* 1. [PD Disaggregation] Some Bug Fix (adapte p2p_initialize, metrics, uniexecutor with pd disagg) by @JimyMa in https://github.com/InternLM/lmdeploy/pull/3893
* Resolve a crash in the `sleep` endpoint by casting the `level` parameter from string to int by @irexyc in https://github.com/InternLM/lmdeploy/pull/3897
* Fix nccl for docker cu11 by @RunningLeon in https://github.com/InternLM/lmdeploy/pull/3896
* disable check_env in multiprocess on dlinfer devices by @tangzhiyi11 in https://github.com/InternLM/lmdeploy/pull/3914
* [dlinfer] fix nn layout typo and scale t by @yuchiwang in https://github.com/InternLM/lmdeploy/pull/3915
* fix chat and warmup of lora adapter by @grimoire in https://github.com/InternLM/lmdeploy/pull/3911
* build(acsend): try to fix acsend CI docker build by @windreamer in https://github.com/InternLM/lmdeploy/pull/3906
* fix internvl3 hf by @CUHKSZzxy in https://github.com/InternLM/lmdeploy/pull/3932
* build(docker): fix ascend tag name by @windreamer in https://github.com/InternLM/lmdeploy/pull/3939
* put eot_token to stop_words by @lvhan028 in https://github.com/InternLM/lmdeploy/pull/3941
### 📚 Documentations
* update proxy docs by @CUHKSZzxy in https://github.com/InternLM/lmdeploy/pull/3796
* add missing docs by @CUHKSZzxy in https://github.com/InternLM/lmdeploy/pull/3871
* fix docs by @CUHKSZzxy in https://github.com/InternLM/lmdeploy/pull/3885
* update news and citation by @lvhan028 in https://github.com/InternLM/lmdeploy/pull/3889
### 🌐 Other
* add prometheus client by @CUHKSZzxy in https://github.com/InternLM/lmdeploy/pull/3792
* fix: add dummy_prefill guard for PD connection operations by @FirwoodLin in https://github.com/InternLM/lmdeploy/pull/3803
* minor fix about the log level and logs by @lvhan028 in https://github.com/InternLM/lmdeploy/pull/3758
* assert PytorchEngineConfig block size by @Tsundoku958 in https://github.com/InternLM/lmdeploy/pull/3826
* [ci] change restful api into openai and add more testcase by @zhulinJulia24 in https://github.com/InternLM/lmdeploy/pull/3866
* remove ppu backend by @yao-fengchen in https://github.com/InternLM/lmdeploy/pull/3904
* [ci] remove flash attn installation in ete test workflow by @zhulinJulia24 in https://github.com/InternLM/lmdeploy/pull/3908
* dlinfer backend support ray by @yao-fengchen in https://github.com/InternLM/lmdeploy/pull/3903
* style(types): fix return type annotation for get_all_requests by @xiaoajie738 in https://github.com/InternLM/lmdeploy/pull/3919
* upgrade torch to 2.8.0 and triton 3.4.0 by @lvhan028 in https://github.com/InternLM/lmdeploy/pull/3930
* Dlinfer readme by @jinminxi104 in https://github.com/InternLM/lmdeploy/pull/3938
* bump version to v0.10.0 by @lvhan028 in https://github.com/InternLM/lmdeploy/pull/3933

## New Contributors
* @PeymanRM made their first contribution in https://github.com/InternLM/lmdeploy/pull/3784
* @FirwoodLin made their first contribution in https://github.com/InternLM/lmdeploy/pull/3803
* @zenosai made their first contribution in https://github.com/InternLM/lmdeploy/pull/3824
* @Tsundoku958 made their first contribution in https://github.com/InternLM/lmdeploy/pull/3826
* @guozixu2001 made their first contribution in https://github.com/InternLM/lmdeploy/pull/3807
* @zodiacg made their first contribution in https://github.com/InternLM/lmdeploy/pull/3837
* @Huarong made their first contribution in https://github.com/InternLM/lmdeploy/pull/3859
* @yuchiwang made their first contribution in https://github.com/InternLM/lmdeploy/pull/3915
* @lh9171338 made their first contribution in https://github.com/InternLM/lmdeploy/pull/3913

**Full Changelog**: https://github.com/InternLM/lmdeploy/compare/v0.9.2...v0.10.0

## v0.10.1 (2025-09-26)

<!-- Release notes generated using configuration in .github/release.yml at main -->

## What's Changed
### 🚀 Features
* Add ROCm support: installation guide and FlashAttention compatibility for AMD GPUs by @Vivicai1005 in https://github.com/InternLM/lmdeploy/pull/3925
* support gpt-oss basic output by @irexyc in https://github.com/InternLM/lmdeploy/pull/3956
* Add FP8*(B)F16 GEMM by @lzhangzz in https://github.com/InternLM/lmdeploy/pull/3960
* Support GLM-4.5 by @CUHKSZzxy in https://github.com/InternLM/lmdeploy/pull/3863
* [Refactor]: Remove tokenizer when building engine by @RunningLeon in https://github.com/InternLM/lmdeploy/pull/3978
* Support InternVL3.5-Flash by @CUHKSZzxy in https://github.com/InternLM/lmdeploy/pull/3952
* support gpt-oss function/reasoning in /v1/chat/completions by @irexyc in https://github.com/InternLM/lmdeploy/pull/3962
* support returning stop_str in output by @lvhan028 in https://github.com/InternLM/lmdeploy/pull/3984
* Support SDAR by @grimoire in https://github.com/InternLM/lmdeploy/pull/3922
### 💥 Improvements
* specify installation on GeForce RTX 50 series by @lvhan028 in https://github.com/InternLM/lmdeploy/pull/3947
* cherry pick PR-3708 to return token_id by @lvhan028 in https://github.com/InternLM/lmdeploy/pull/3976
* Optimize AsyncEngine generation method by @shell-nlp in https://github.com/InternLM/lmdeploy/pull/3982
* Use blocking sync when TP engine is idling by @lzhangzz in https://github.com/InternLM/lmdeploy/pull/3974
* add openai_harmony to requirements by @irexyc in https://github.com/InternLM/lmdeploy/pull/4006
### 🐞 Bug fixes
* fix bugs with triton3.4.0 by @grimoire in https://github.com/InternLM/lmdeploy/pull/3946
* fix longrope by @grimoire in https://github.com/InternLM/lmdeploy/pull/3968
* Fix tm rl usage in xtuner by @irexyc in https://github.com/InternLM/lmdeploy/pull/3912
* Disable prefix caching when serving a VLM model by @lvhan028 in https://github.com/InternLM/lmdeploy/pull/3990
* remove NCCL_LAUNCH_MODE by @irexyc in https://github.com/InternLM/lmdeploy/pull/3994
* return the last token's logprobs, logits and last_hidden_states if include_stop_str_in_output is requested by @lvhan028 in https://github.com/InternLM/lmdeploy/pull/4000
* [Fix] device args in chat cli when using pytorch engine by @CyCle1024 in https://github.com/InternLM/lmdeploy/pull/3999
* fix internvl by @CUHKSZzxy in https://github.com/InternLM/lmdeploy/pull/3997
* fix not-returned iterator in SequenceManager::Erase by @irexyc in https://github.com/InternLM/lmdeploy/pull/4001
* fix cudagraph without warmup by @grimoire in https://github.com/InternLM/lmdeploy/pull/4005
* fix internvl flash long context acc by @CUHKSZzxy in https://github.com/InternLM/lmdeploy/pull/4003
### 🌐 Other
* [ci] update daily testcase by @zhulinJulia24 in https://github.com/InternLM/lmdeploy/pull/3944
* [maca] change kv layout from pagedattn to flashattn by @yuchiwang in https://github.com/InternLM/lmdeploy/pull/3958
* remove cudnn by @irexyc in https://github.com/InternLM/lmdeploy/pull/3969
* build(pypi): add cuda 12.8 support for wheels by @windreamer in https://github.com/InternLM/lmdeploy/pull/3948
* [CI] add ascend test by @littlegy in https://github.com/InternLM/lmdeploy/pull/3959
* update serve requirement by @RunningLeon in https://github.com/InternLM/lmdeploy/pull/3986
* [ci] add h800 function test workflow by @zhulinJulia24 in https://github.com/InternLM/lmdeploy/pull/3985
* bump version to v0.10.1 by @lvhan028 in https://github.com/InternLM/lmdeploy/pull/3989

## New Contributors
* @Vivicai1005 made their first contribution in https://github.com/InternLM/lmdeploy/pull/3925
* @shell-nlp made their first contribution in https://github.com/InternLM/lmdeploy/pull/3982
* @littlegy made their first contribution in https://github.com/InternLM/lmdeploy/pull/3959

**Full Changelog**: https://github.com/InternLM/lmdeploy/compare/v0.10.0...v0.10.1

## v0.10.2 (2025-10-28)

<!-- Release notes generated using configuration in .github/release.yml at main -->

## What's Changed
### 🚀 Features
* add /generate api by @irexyc in https://github.com/InternLM/lmdeploy/pull/4019
* Guided decoding with xgrammar for TurboMind by @windreamer in https://github.com/InternLM/lmdeploy/pull/3965
* Reimplement guided decoding with xgrammar for PyTorch Engine by @windreamer in https://github.com/InternLM/lmdeploy/pull/4028
### 💥 Improvements
* [ascend] support aclgraph by @yao-fengchen in https://github.com/InternLM/lmdeploy/pull/4063
* Leverage incremental output between the inference and async engines to improve performance by @lvhan028 in https://github.com/InternLM/lmdeploy/pull/4054
* Optimize multinomial sampling by @grimoire in https://github.com/InternLM/lmdeploy/pull/4056
### 🐞 Bug fixes
* zmqrpc localhost only by @grimoire in https://github.com/InternLM/lmdeploy/pull/4017
* fix bug: dp+tp warmup by @Tsundoku958 in https://github.com/InternLM/lmdeploy/pull/3991
* fix dllm long-context by @grimoire in https://github.com/InternLM/lmdeploy/pull/4012
* Fix GPT-OSS streaming tool call parsing by @QwertyJack in https://github.com/InternLM/lmdeploy/pull/4023
* move releasing resource from async_engine to inference engine by @lvhan028 in https://github.com/InternLM/lmdeploy/pull/4041
* fix: fix tokenizer parsing bug for guided decoding by @windreamer in https://github.com/InternLM/lmdeploy/pull/4044
* Fix message content field handling for tool calls and multimodal input by @QwertyJack in https://github.com/InternLM/lmdeploy/pull/4029
* fix builder for kimi-k2 by @CUHKSZzxy in https://github.com/InternLM/lmdeploy/pull/4069
* Skip unnecessary sampling and fix the random offset by @grimoire in https://github.com/InternLM/lmdeploy/pull/4068
* fix duplicated stop_token_string when ignore_special_tokens is False by @irexyc in https://github.com/InternLM/lmdeploy/pull/4077
### 🌐 Other
* Drop CUDA 11.8 build support, upgrade CI/CD to CUDA 12.6/12.8 by @windreamer in https://github.com/InternLM/lmdeploy/pull/4013
* remove profile_generation.py and its testcases by @lvhan028 in https://github.com/InternLM/lmdeploy/pull/4027
* [ci] refactor eval into api eval and add h800 eval workflow by @zhulinJulia24 in https://github.com/InternLM/lmdeploy/pull/4008
* Add Docker image for NVIDIA Jetson by @windreamer in https://github.com/InternLM/lmdeploy/pull/3834
* [ci] refactor api evaluate test into llm judger evaluation by @littlegy in https://github.com/InternLM/lmdeploy/pull/4046
* Check color logger by @grimoire in https://github.com/InternLM/lmdeploy/pull/4060
* Update API testing with HLE and LCB datasets by @littlegy in https://github.com/InternLM/lmdeploy/pull/4061
* update ascend requirements by @yao-fengchen in https://github.com/InternLM/lmdeploy/pull/4066
* bump version to v0.10.2 by @lvhan028 in https://github.com/InternLM/lmdeploy/pull/4062


**Full Changelog**: https://github.com/InternLM/lmdeploy/compare/v0.10.1...v0.10.2

## v0.11.0 (2025-12-04)

<!-- Release notes generated using configuration in .github/release.yml at main -->

## What's Changed
### 🚀 Features
* add endpoint /abort_request by @lvhan028 in https://github.com/InternLM/lmdeploy/pull/4092
* Qwen3 next by @grimoire in https://github.com/InternLM/lmdeploy/pull/4039
* Support Qwen3-VL by @CUHKSZzxy in https://github.com/InternLM/lmdeploy/pull/4093
* Support sync weights with flattened bucket tensor by @RunningLeon in https://github.com/InternLM/lmdeploy/pull/4109
* Support group router for moe models by @RunningLeon in https://github.com/InternLM/lmdeploy/pull/4120
* [Feature]: return routed experts to reuse by @RunningLeon in https://github.com/InternLM/lmdeploy/pull/4090
* support context parallel by @irexyc in https://github.com/InternLM/lmdeploy/pull/3951
* fope by @grimoire in https://github.com/InternLM/lmdeploy/pull/4043
* [Feature]: Support speculative decoding by @RunningLeon in https://github.com/InternLM/lmdeploy/pull/3945
* Moe bf16 ep by @grimoire in https://github.com/InternLM/lmdeploy/pull/4144
### 💥 Improvements
* Enlarge gc threshold by @grimoire in https://github.com/InternLM/lmdeploy/pull/4076
* remove num_tokens from EngineOutput by @lvhan028 in https://github.com/InternLM/lmdeploy/pull/4088
* revert masking vocab_size by @lvhan028 in https://github.com/InternLM/lmdeploy/pull/4089
* feat: add json_object support in response_format by @windreamer in https://github.com/InternLM/lmdeploy/pull/4080
* support image_data input to /generate endpoint by @irexyc in https://github.com/InternLM/lmdeploy/pull/4086
* [Fix] all RayEngineWorker actors created at node 0 in RL training by @CyCle1024 in https://github.com/InternLM/lmdeploy/pull/4107
* Optimize sleep level=1 for turbomind backend by @irexyc in https://github.com/InternLM/lmdeploy/pull/4074
* [Feat] enable ascend update_params by @CyCle1024 in https://github.com/InternLM/lmdeploy/pull/4111
* Enhance request checker by @lvhan028 in https://github.com/InternLM/lmdeploy/pull/4104
* Refactor dp tp by @grimoire in https://github.com/InternLM/lmdeploy/pull/4004
* fix kernel numerical error by @grimoire in https://github.com/InternLM/lmdeploy/pull/4133
* free ray put by @grimoire in https://github.com/InternLM/lmdeploy/pull/4137
* Reduce experts cache when resize by @RunningLeon in https://github.com/InternLM/lmdeploy/pull/4138
* support interleave text and image in messages by @lvhan028 in https://github.com/InternLM/lmdeploy/pull/4141
* optimize rms norm by @grimoire in https://github.com/InternLM/lmdeploy/pull/4153
* fix evict policy by @Tsundoku958 in https://github.com/InternLM/lmdeploy/pull/4127
### 🐞 Bug fixes
* fix type hint by @grimoire in https://github.com/InternLM/lmdeploy/pull/4078
* Fix inputs split by @RunningLeon in https://github.com/InternLM/lmdeploy/pull/4083
* add missing update_model_meta by @jinminxi104 in https://github.com/InternLM/lmdeploy/pull/4099
* Fix update_params for pytorch backend when loading vl model by @irexyc in https://github.com/InternLM/lmdeploy/pull/4101
* workaround for issue "TypeError argument 'tokens': 'NoneType' object cannot be converted to 'PyString" by @lvhan028 in https://github.com/InternLM/lmdeploy/pull/4103
* fix bug: schedule ratio support prefix-caching by @Tsundoku958 in https://github.com/InternLM/lmdeploy/pull/4100
* remove prefill free ratio threshold by @grimoire in https://github.com/InternLM/lmdeploy/pull/4110
* fix key error: api_server node might be removed by @lvhan028 in https://github.com/InternLM/lmdeploy/pull/4112
* Incorrectly judging the request as a bad request by @lvhan028 in https://github.com/InternLM/lmdeploy/pull/4121
* fix dist config keys by @grimoire in https://github.com/InternLM/lmdeploy/pull/4125
* proxy server miss media_type in streaming mode by @lvhan028 in https://github.com/InternLM/lmdeploy/pull/4130
* Fix logprobs to_tensor by @RunningLeon in https://github.com/InternLM/lmdeploy/pull/4132
* Fix cli help by @RunningLeon in https://github.com/InternLM/lmdeploy/pull/4139
* fix and optimize fill_kv_cache_quant by @grimoire in https://github.com/InternLM/lmdeploy/pull/4140
* fix: fix package deprecation introduced by CUDA 13 by @windreamer in https://github.com/InternLM/lmdeploy/pull/4117
* yield empty list for token_ids when it runs out of tokens by @lvhan028 in https://github.com/InternLM/lmdeploy/pull/4148
* Fix interns1 routed experts outputs by @RunningLeon in https://github.com/InternLM/lmdeploy/pull/4149
* fix qwen3-30-a3b lcb-code score by @yao-fengchen in https://github.com/InternLM/lmdeploy/pull/4142
* Fix ep deployment issues by @CUHKSZzxy in https://github.com/InternLM/lmdeploy/pull/4084
* Fix dllm to not use fa3 decoding by @RunningLeon in https://github.com/InternLM/lmdeploy/pull/4159
* fix: handle non-tuple decoder outputs during Qwen-2.5 quantization by @chengyuma in https://github.com/InternLM/lmdeploy/pull/4158
* fix cu11 docker build by @CUHKSZzxy in https://github.com/InternLM/lmdeploy/pull/4165
* Fix model config by @CUHKSZzxy in https://github.com/InternLM/lmdeploy/pull/4170
* fix lora by @grimoire in https://github.com/InternLM/lmdeploy/pull/4172
* fix cmake logic detect sm70, sm75 by @tuilakhanh in https://github.com/InternLM/lmdeploy/pull/4175
### 📚 Documentations
* Update model evalution guide by @lvhan028 in https://github.com/InternLM/lmdeploy/pull/4094
* [Docs]: Add guide for update weights by @RunningLeon in https://github.com/InternLM/lmdeploy/pull/4151
### 🌐 Other
* add dockerfile to build dev image by @lvhan028 in https://github.com/InternLM/lmdeploy/pull/4091
* add ascend_a3 Dockerfile by @yao-fengchen in https://github.com/InternLM/lmdeploy/pull/4097
* [ci] refactor longtext benchmark by @zhulinJulia24 in https://github.com/InternLM/lmdeploy/pull/4087
* enable metrics by default by @lvhan028 in https://github.com/InternLM/lmdeploy/pull/4108
* Replace pynvml with nvidia-ml-py in requirements by @myhloli in https://github.com/InternLM/lmdeploy/pull/4118
* [ci] add free disk before build test whl package and add session_len args in benchmark script by @zhulinJulia24 in https://github.com/InternLM/lmdeploy/pull/4136
* Add prefixcache functionality and performance testing by @littlegy in https://github.com/InternLM/lmdeploy/pull/4119
* [ci] modify pipeline.close and add more case into pr_test by @zhulinJulia24 in https://github.com/InternLM/lmdeploy/pull/4150
* bump version to v0.11.0 by @lvhan028 in https://github.com/InternLM/lmdeploy/pull/4155

## New Contributors
* @myhloli made their first contribution in https://github.com/InternLM/lmdeploy/pull/4118
* @tuilakhanh made their first contribution in https://github.com/InternLM/lmdeploy/pull/4175

**Full Changelog**: https://github.com/InternLM/lmdeploy/compare/v0.10.2...v0.11.0

## v0.11.1 (2025-12-24)

<!-- Release notes generated using configuration in .github/release.yml at main -->

## What's Changed
### 🚀 Features
* [ascend] support dptp by @tangzhiyi11 in https://github.com/InternLM/lmdeploy/pull/4218
* Support Deepseek v32 by @grimoire in https://github.com/InternLM/lmdeploy/pull/4026
### 💥 Improvements
* Improve metrics by @CUHKSZzxy in https://github.com/InternLM/lmdeploy/pull/4178
* reserve blocks for dummy inputs by @grimoire in https://github.com/InternLM/lmdeploy/pull/4157
* Add vision id for Qwen3-VL by @CUHKSZzxy in https://github.com/InternLM/lmdeploy/pull/4183
* [Enhance]: Return routed experts when request canceled by @RunningLeon in https://github.com/InternLM/lmdeploy/pull/4197
* Add mm processor args for Qwen3-VL by @CUHKSZzxy in https://github.com/InternLM/lmdeploy/pull/4196
* support chat_template_kwargs in v1/chat/completions by @lvhan028 in https://github.com/InternLM/lmdeploy/pull/4201
* Refactor scheduler and engine.py by @grimoire in https://github.com/InternLM/lmdeploy/pull/4163
* update dp timeout by @grimoire in https://github.com/InternLM/lmdeploy/pull/4204
* Improve Qwen3-VL by @CUHKSZzxy in https://github.com/InternLM/lmdeploy/pull/4207
### 🐞 Bug fixes
* [Fix]: Split routed experts with query lens by @RunningLeon in https://github.com/InternLM/lmdeploy/pull/4180
* [Maca] fix ray and memory sync by @wanfengcxz in https://github.com/InternLM/lmdeploy/pull/4164
* Build block trie in prefill and add hit rate by @RunningLeon in https://github.com/InternLM/lmdeploy/pull/4184
* fix fope by @CUHKSZzxy in https://github.com/InternLM/lmdeploy/pull/4191
* fix hf modules read/write conflicts by multi processors by @lvhan028 in https://github.com/InternLM/lmdeploy/pull/4188
* Some Minor fix by @windreamer in https://github.com/InternLM/lmdeploy/pull/4185
* fix insecure deserialization when calling torch.load() by @lvhan028 in https://github.com/InternLM/lmdeploy/pull/4202
* Fix processor args by @CUHKSZzxy in https://github.com/InternLM/lmdeploy/pull/4200
* remove get_model_config to avoid pickle hf_config error in rpc calling by @lvhan028 in https://github.com/InternLM/lmdeploy/pull/4217
* Fix quant scale-fmt by @grimoire in https://github.com/InternLM/lmdeploy/pull/4212
* Fix requests of mix return_logprobs by @RunningLeon in https://github.com/InternLM/lmdeploy/pull/4222
* fix fillkv quant8 by @grimoire in https://github.com/InternLM/lmdeploy/pull/4229
* fix scale-fmt by @grimoire in https://github.com/InternLM/lmdeploy/pull/4230
### 📚 Documentations
* [Docs]: Add guide for VLMEvalKit by @CUHKSZzxy in https://github.com/InternLM/lmdeploy/pull/4156
### 🌐 Other
* Add FA3 by @CUHKSZzxy in https://github.com/InternLM/lmdeploy/pull/4166
* Add distributed test cases by @littlegy in https://github.com/InternLM/lmdeploy/pull/4161
* Add generate test by @littlegy in https://github.com/InternLM/lmdeploy/pull/4181
* [ci] add mllm eval  by @zhulinJulia24 in https://github.com/InternLM/lmdeploy/pull/4194
* [ascend] refactor code by @yao-fengchen in https://github.com/InternLM/lmdeploy/pull/4176
* install serve.txt when building the docker image by @lvhan028 in https://github.com/InternLM/lmdeploy/pull/4219
* bump version to v0.11.1 by @lvhan028 in https://github.com/InternLM/lmdeploy/pull/4221


**Full Changelog**: https://github.com/InternLM/lmdeploy/compare/v0.11.0...v0.11.1

## v0.12.0 (2026-02-04)

<!-- Release notes generated using configuration in .github/release.yml at main -->

## What's Changed
### 🚀 Features
* Add Gloo communication to turbomind by @irexyc in https://github.com/InternLM/lmdeploy/pull/3362
* [Feat] Support llm-compressor AWQ models in TurboMind by @43758726 in https://github.com/InternLM/lmdeploy/pull/4290
* Router replay for gpt oss by @RunningLeon in https://github.com/InternLM/lmdeploy/pull/4298
* Support llm-compressor symmetric quantized model inference in TurboMind by @43758726 in https://github.com/InternLM/lmdeploy/pull/4305
* Support Intern-S1-Pro by @CUHKSZzxy in https://github.com/InternLM/lmdeploy/pull/4318
### 💥 Improvements
* Configurable max CTAs and NVLS usage for CUDA IPC communicator by @lzhangzz in https://github.com/InternLM/lmdeploy/pull/4227
* Improve aborting all sessions by @lvhan028 in https://github.com/InternLM/lmdeploy/pull/4215
* Moe Reduce kernel by @grimoire in https://github.com/InternLM/lmdeploy/pull/4228
* Refactor attn by @grimoire in https://github.com/InternLM/lmdeploy/pull/4238
* Optimize exception raising and error process by @grimoire in https://github.com/InternLM/lmdeploy/pull/4236
* [AsyncEngine Refactor 1/N] define MultimodalProcessor to handle multimodal data processing by @lvhan028 in https://github.com/InternLM/lmdeploy/pull/4250
* [AsyncEngine Refactor 2/N] Remove deprecates from chat template by @lvhan028 in https://github.com/InternLM/lmdeploy/pull/4252
* Configurable uvicorn timeout by @CUHKSZzxy in https://github.com/InternLM/lmdeploy/pull/4255
* Adapt to dlsime v0.0.2 by @JimyMa in https://github.com/InternLM/lmdeploy/pull/4242
* [Fix] fix quant calibration dataset by @43758726 in https://github.com/InternLM/lmdeploy/pull/4256
* lmdeploy suppport parrllel embedding by @Tsundoku958 in https://github.com/InternLM/lmdeploy/pull/4192
* Refactor turbomind engine by @lzhangzz in https://github.com/InternLM/lmdeploy/pull/4223
* Refactor Engine & ModelAgent interact by @grimoire in https://github.com/InternLM/lmdeploy/pull/4265
* Support sleep and destroy deepep buffer by @RunningLeon in https://github.com/InternLM/lmdeploy/pull/4246
* add yarn truncate by @grimoire in https://github.com/InternLM/lmdeploy/pull/4301
* [AsyncEngine Refactor 3/N] Introduce Session and SessionManager by @lvhan028 in https://github.com/InternLM/lmdeploy/pull/4253
* Add warning about NCCL 2.27 memory leaks by @lzhangzz in https://github.com/InternLM/lmdeploy/pull/4313
### 🐞 Bug fixes
* Fix fope cos/sin coef device type by @CUHKSZzxy in https://github.com/InternLM/lmdeploy/pull/4240
* Fix include_stop_str_in_output with output_logits Exception by @windreamer in https://github.com/InternLM/lmdeploy/pull/4244
* fix logit softcapping is None by @grimoire in https://github.com/InternLM/lmdeploy/pull/4247
* Fix performance regression for prefix caching by @lzhangzz in https://github.com/InternLM/lmdeploy/pull/4270
* convert float16 weight to bfloat16 for FP8 models by @lvhan028 in https://github.com/InternLM/lmdeploy/pull/4276
* [ascend] fix dp multinode rank_table mapping by @tangzhiyi11 in https://github.com/InternLM/lmdeploy/pull/4268
* [Fix] move calibrate load dataset location by @43758726 in https://github.com/InternLM/lmdeploy/pull/4289
* fix ignore-eos by @grimoire in https://github.com/InternLM/lmdeploy/pull/4282
* fix MPEngine poll by @grimoire in https://github.com/InternLM/lmdeploy/pull/4287
* Fix prefix caching by @lzhangzz in https://github.com/InternLM/lmdeploy/pull/4292
* Fix gemma chat template by @lvhan028 in https://github.com/InternLM/lmdeploy/pull/4280
* Fix scheduler metrics by @lzhangzz in https://github.com/InternLM/lmdeploy/pull/4294
* Fix NVLS init for mixed DP+TP by @lzhangzz in https://github.com/InternLM/lmdeploy/pull/4296
* [side-effect] The tool message dump is incomplete by @lvhan028 in https://github.com/InternLM/lmdeploy/pull/4299
* Fix mla with spec tokens by @RunningLeon in https://github.com/InternLM/lmdeploy/pull/4302
* fix stop long context by @grimoire in https://github.com/InternLM/lmdeploy/pull/4309
* fix crash on client disconnect (Ctrl+C) by @lvhan028 in https://github.com/InternLM/lmdeploy/pull/4308
* Ensure the pipe benchmark uses kwargs when calling `pipe.stream_infer` by @lvhan028 in https://github.com/InternLM/lmdeploy/pull/4312
* fix get_ppl for long context by @lvhan028 in https://github.com/InternLM/lmdeploy/pull/4314
* fix  sleep engine for dp=1 by @RunningLeon in https://github.com/InternLM/lmdeploy/pull/4315
### 🌐 Other
* [ci] fix fail testcase and add generate testcase in pr test by @zhulinJulia24 in https://github.com/InternLM/lmdeploy/pull/4231
* Pin nvshmem version by @CUHKSZzxy in https://github.com/InternLM/lmdeploy/pull/4257
* fix: Pin `timm` version to avoid failed tests by @windreamer in https://github.com/InternLM/lmdeploy/pull/4258
* docs: add generated openapi spec documentation by @windreamer in https://github.com/InternLM/lmdeploy/pull/4251
* fix: get rid of buggy timm-1.0.23 by @windreamer in https://github.com/InternLM/lmdeploy/pull/4260
* [ascend] fix paged prefill by @tangzhiyi11 in https://github.com/InternLM/lmdeploy/pull/4254
* Fix ascend/maca/camb runtime_requirements by @jinminxi104 in https://github.com/InternLM/lmdeploy/pull/4262
* docs: refine the documents by @windreamer in https://github.com/InternLM/lmdeploy/pull/4259
* docs: add cli docs by @windreamer in https://github.com/InternLM/lmdeploy/pull/4264
* Drop support for Python 3.9 as it has reached end-of-life by @lvhan028 in https://github.com/InternLM/lmdeploy/pull/4281
* bump version to v0.12.0 by @lvhan028 in https://github.com/InternLM/lmdeploy/pull/4300

## New Contributors
* @43758726 made their first contribution in https://github.com/InternLM/lmdeploy/pull/4256

**Full Changelog**: https://github.com/InternLM/lmdeploy/compare/v0.11.1...v0.12.0

## v0.12.1 (2026-02-13)

<!-- Release notes generated using configuration in .github/release.yml at main -->

## What's Changed
### 🚀 Features
* support glm-4.7-flash by @RunningLeon in https://github.com/InternLM/lmdeploy/pull/4320
* [ascend]suppot ep by @yao-fengchen in https://github.com/InternLM/lmdeploy/pull/3696
### 💥 Improvements
* fix rotary embedding for transformers v5 by @grimoire in https://github.com/InternLM/lmdeploy/pull/4303
* Improve metrics log by @CUHKSZzxy in https://github.com/InternLM/lmdeploy/pull/4297
* Support ignore layers in quant config for qwen3 models by @RunningLeon in https://github.com/InternLM/lmdeploy/pull/4293
* add custom noaux kernel by @grimoire in https://github.com/InternLM/lmdeploy/pull/4345
* fix qwen3vl with transformers5 by @grimoire in https://github.com/InternLM/lmdeploy/pull/4348
### 🐞 Bug fixes
* fix tool call parser's streaming cursor by @lvhan028 in https://github.com/InternLM/lmdeploy/pull/4333
* Fix data race for guided decoding in TP mode by @lzhangzz in https://github.com/InternLM/lmdeploy/pull/4341
* fa3 check by @grimoire in https://github.com/InternLM/lmdeploy/pull/4340
* Fix time series preprocess by @CUHKSZzxy in https://github.com/InternLM/lmdeploy/pull/4339
* Negative KV sequence length error in Attention op by @jinminxi104 in https://github.com/InternLM/lmdeploy/pull/4316
* fix qwen3-vl-moe long context by @grimoire in https://github.com/InternLM/lmdeploy/pull/4342
* fix: move quantized norm to CPU instead of stale q_linear reference in smooth_quant by @Mr-Neutr0n in https://github.com/InternLM/lmdeploy/pull/4352
* update noaux-kernel check by @grimoire in https://github.com/InternLM/lmdeploy/pull/4358
### 🌐 Other
* change INPUT_CUDA_VERSION to 12.6.2 by @lvhan028 in https://github.com/InternLM/lmdeploy/pull/4322
* add Qwen3-8B accuracy evaluation in llm_compressor.md by @43758726 in https://github.com/InternLM/lmdeploy/pull/4319
* [ci] refactor ete testcase by @zhulinJulia24 in https://github.com/InternLM/lmdeploy/pull/4274
* Set alias interns1_1 for interns1_pro by @lvhan028 in https://github.com/InternLM/lmdeploy/pull/4334
* build(docker): skip FA2 when use cu13 by @windreamer in https://github.com/InternLM/lmdeploy/pull/4356
* bump version to v0.12.1 by @lvhan028 in https://github.com/InternLM/lmdeploy/pull/4350

## New Contributors
* @Mr-Neutr0n made their first contribution in https://github.com/InternLM/lmdeploy/pull/4352

**Full Changelog**: https://github.com/InternLM/lmdeploy/compare/v0.12.0...v0.12.1

## v0.12.2 (2026-03-18)

<!-- Release notes generated using configuration in .github/release.yml at main -->

## What's Changed
### 🚀 Features
* support glm5 by @grimoire in https://github.com/InternLM/lmdeploy/pull/4355
* Qwen/Internlm/Llama Dense/Moe model fp8 quant online by @43758726 in https://github.com/InternLM/lmdeploy/pull/4324
* Qwen3.5 by @grimoire in https://github.com/InternLM/lmdeploy/pull/4351
* GLM-4.7-Flash Turbomind support by @lapy in https://github.com/InternLM/lmdeploy/pull/4362
* Support router replay and ignore quant layer for qwen3.5 by @RunningLeon in https://github.com/InternLM/lmdeploy/pull/4394
* [Feature] Add TurboMind support for Qwen3.5 models (dense + MoE) by @lapy in https://github.com/InternLM/lmdeploy/pull/4389
* support repetition ngram logits processor by @grimoire in https://github.com/InternLM/lmdeploy/pull/4288
### 💥 Improvements
* Compatible with transformers 5.0 at TurboMind side by @lvhan028 in https://github.com/InternLM/lmdeploy/pull/4304
* Support fp32 head for qwen and internlm models by @RunningLeon in https://github.com/InternLM/lmdeploy/pull/4160
* Reduce MLA kv-cache memory by @lzhangzz in https://github.com/InternLM/lmdeploy/pull/4373
* add recurrent_gated_delta_rule kernel by @grimoire in https://github.com/InternLM/lmdeploy/pull/4376
* [ascend]adapt for s1-pro dp*tp+ep by @yao-fengchen in https://github.com/InternLM/lmdeploy/pull/4380
* Support glm4.7 with mtp by @RunningLeon in https://github.com/InternLM/lmdeploy/pull/4346
* Faster MLA kernels by @lzhangzz in https://github.com/InternLM/lmdeploy/pull/4391
* Attention kernel self-registration and decoupled dispatching by @lzhangzz in https://github.com/InternLM/lmdeploy/pull/4396
### 🐞 Bug fixes
* fix: change debug log from ERROR to DEBUG in RepetitionPenaltyKernel by @murray-macdonald in https://github.com/InternLM/lmdeploy/pull/4363
* Fix quant config parsing for internvl awq model by @RunningLeon in https://github.com/InternLM/lmdeploy/pull/4369
* Fix XGrammar bitmask initialization and add null check for gen_config in generate method by @windreamer in https://github.com/InternLM/lmdeploy/pull/4349
* fix the logic of closing session by @lvhan028 in https://github.com/InternLM/lmdeploy/pull/4370
* Fix authorization by @lvhan028 in https://github.com/InternLM/lmdeploy/pull/4338
* Fix some minor issues and provide tests for Pipeline by @windreamer in https://github.com/InternLM/lmdeploy/pull/4365
* fix dllm mask on set_step by @grimoire in https://github.com/InternLM/lmdeploy/pull/4278
* fix models for transformers>=5 by @grimoire in https://github.com/InternLM/lmdeploy/pull/4381
* fix exception when aborting a request by @lvhan028 in https://github.com/InternLM/lmdeploy/pull/4403
* fix inference crashed on v100 with qwen3.5-0.8b by @lvhan028 in https://github.com/InternLM/lmdeploy/pull/4420
### 🌐 Other
* ci(lint): skip flaky deadlink test for python wiki page by @windreamer in https://github.com/InternLM/lmdeploy/pull/4357
* fix fa3 install by @irexyc in https://github.com/InternLM/lmdeploy/pull/4361
* fix lint by @windreamer in https://github.com/InternLM/lmdeploy/pull/4375
* upgrade triton and torch by @grimoire in https://github.com/InternLM/lmdeploy/pull/4379
* Add speculative decoding test by @littlegy in https://github.com/InternLM/lmdeploy/pull/4377
* ci: integrate clang-format lint into pre-commit hooks by @windreamer in https://github.com/InternLM/lmdeploy/pull/4390
* Update dockerfile by removing cu11 and changing cu12.4 to cu12.6 by @lvhan028 in https://github.com/InternLM/lmdeploy/pull/4398
* manually build dev image instead of publishing it every version by @lvhan028 in https://github.com/InternLM/lmdeploy/pull/4409
* bump version to v0.12.2 by @lvhan028 in https://github.com/InternLM/lmdeploy/pull/4378

## New Contributors
* @murray-macdonald made their first contribution in https://github.com/InternLM/lmdeploy/pull/4363
* @lapy made their first contribution in https://github.com/InternLM/lmdeploy/pull/4362

**Full Changelog**: https://github.com/InternLM/lmdeploy/compare/v0.12.1...v0.12.2

## v0.12.3 (2026-04-08)

<!-- Release notes generated using configuration in .github/release.yml at main -->

## What's Changed
### 🚀 Features
* Support video inputs by @CUHKSZzxy in https://github.com/InternLM/lmdeploy/pull/4360
* feat: fully implement compressed-tensors gs32 support in TurboMind by @lapy in https://github.com/InternLM/lmdeploy/pull/4429
* Draft model update params by @CUHKSZzxy in https://github.com/InternLM/lmdeploy/pull/4452
### 💥 Improvements
* support qwen3.5 on volta by @grimoire in https://github.com/InternLM/lmdeploy/pull/4405
* Optimize Qwen3.5 by @lzhangzz in https://github.com/InternLM/lmdeploy/pull/4434
* Builtin mrope by @grimoire in https://github.com/InternLM/lmdeploy/pull/4393
* delete ray remote function return value by @grimoire in https://github.com/InternLM/lmdeploy/pull/4422
* support cache_seqlen on recurrent-gdr and causal-conv1d-update by @grimoire in https://github.com/InternLM/lmdeploy/pull/4417
* safe ray api by @CUHKSZzxy in https://github.com/InternLM/lmdeploy/pull/4455
* add R3 for qwen3-vl-moe models by @lvhan028 in https://github.com/InternLM/lmdeploy/pull/4457
* Align rope init in lmdeploy by @RangiLyu in https://github.com/InternLM/lmdeploy/pull/4466
* Make tilelang a Linux-only dependency (like triton) by @Copilot in https://github.com/InternLM/lmdeploy/pull/4469
* prepare chunk indices before cache initialize by @grimoire in https://github.com/InternLM/lmdeploy/pull/4458
* unify rope device by @CUHKSZzxy in https://github.com/InternLM/lmdeploy/pull/4467
* custom processor args by @CUHKSZzxy in https://github.com/InternLM/lmdeploy/pull/4472
* Assign sequential api_server ports when proxy_url is unset by @lvhan028 in https://github.com/InternLM/lmdeploy/pull/4416
* disable fla intracard_backend by @grimoire in https://github.com/InternLM/lmdeploy/pull/4482
* [Fix][Feat] Fix worker sorting with external pg bundles & Support persistent buffer for update_params by @CyCle1024 in https://github.com/InternLM/lmdeploy/pull/4397
* simplify interns1 pro codes by @CUHKSZzxy in https://github.com/InternLM/lmdeploy/pull/4480
### 🐞 Bug fixes
* fix test_hf_overrides for transformers>5 by @grimoire in https://github.com/InternLM/lmdeploy/pull/4418
* fix qwen3.5 pytorch multimodal inference by @CUHKSZzxy in https://github.com/InternLM/lmdeploy/pull/4430
* fix `generate` endpoint by @CUHKSZzxy in https://github.com/InternLM/lmdeploy/pull/4432
* Make Intern-S1-Pro compatible with Transformers 5.0+ by @lvhan028 in https://github.com/InternLM/lmdeploy/pull/4435
* fix multiround chat by @CUHKSZzxy in https://github.com/InternLM/lmdeploy/pull/4438
* fix(async_engine): make safe_run cancellation cleanup reliable with shield and SafeRunException by @lvhan028 in https://github.com/InternLM/lmdeploy/pull/4439
* release state cache by @CUHKSZzxy in https://github.com/InternLM/lmdeploy/pull/4462
* Split/tool call args json for qwen3coder tool calls (Qwen3.5)  by @lapy in https://github.com/InternLM/lmdeploy/pull/4433
* fix(turbomind): fix dimension mismatch in ApplyTokenBitmaskInplace by @windreamer in https://github.com/InternLM/lmdeploy/pull/4456
* fix metrics by @CUHKSZzxy in https://github.com/InternLM/lmdeploy/pull/4410
* fix security issues by @CUHKSZzxy in https://github.com/InternLM/lmdeploy/pull/4447
* fix qwen3.5 fp8 support by @grimoire in https://github.com/InternLM/lmdeploy/pull/4470
* fix image / video resize function by @CUHKSZzxy in https://github.com/InternLM/lmdeploy/pull/4478
* fix dynamic ntk device by @CUHKSZzxy in https://github.com/InternLM/lmdeploy/pull/4483
* fix pagedattention pointer range by @grimoire in https://github.com/InternLM/lmdeploy/pull/4494
* fix glm4.7-flash by @grimoire in https://github.com/InternLM/lmdeploy/pull/4500
* Fix torch awq by @grimoire in https://github.com/InternLM/lmdeploy/pull/4503
### 🌐 Other
* [ci] add legacy test workflow and test config by @zhulinJulia24 in https://github.com/InternLM/lmdeploy/pull/4387
* chore: add CLAUDE.md and Claude Code skills by @CUHKSZzxy in https://github.com/InternLM/lmdeploy/pull/4413
* Fix CI errors including linting error and unit test error by @lvhan028 in https://github.com/InternLM/lmdeploy/pull/4431
* Use pyupgrade and ruff to modernize LMDeploy Python Code by @windreamer in https://github.com/InternLM/lmdeploy/pull/4392
* reduce ci memory by @irexyc in https://github.com/InternLM/lmdeploy/pull/4471
* fix: add safe.directory for git in docker workflows by @windreamer in https://github.com/InternLM/lmdeploy/pull/4474
* [ci] add nightly docker build workflow by @zhulinJulia24 in https://github.com/InternLM/lmdeploy/pull/4406
* split docker wheel preparation into staged build steps and use python 3.12 as the default version by @lvhan028 in https://github.com/InternLM/lmdeploy/pull/4476
* [Feat]: Support qwen35 with mtp by @RunningLeon in https://github.com/InternLM/lmdeploy/pull/4437
* bump version to v0.12.3 by @lvhan028 in https://github.com/InternLM/lmdeploy/pull/4493

## New Contributors
* @RangiLyu made their first contribution in https://github.com/InternLM/lmdeploy/pull/4466
* @Copilot made their first contribution in https://github.com/InternLM/lmdeploy/pull/4469

**Full Changelog**: https://github.com/InternLM/lmdeploy/compare/v0.12.2...v0.12.3

## v0.13.0 (2026-05-12)

<!-- Release notes generated using configuration in .github/release.yml at main -->

## What's Changed
### 🚀 Features
* [Ascend] support qwen3.5 35BA3B by @wanfengcxz in https://github.com/InternLM/lmdeploy/pull/4485
* feat: Add TurboQuant (quant_policy=42) support for KV Cache Quantization by @windreamer in https://github.com/InternLM/lmdeploy/pull/4510
* [refactor] [api_server] [2/N] improve tool parsers by abstracting xml parser by @lvhan028 in https://github.com/InternLM/lmdeploy/pull/4548
* feat(turbomind): integrate cublasGemmGroupedBatchedEx for Qwen3.5 MoE  inference on Blackwell GPUs with memory copy optimizations by @hd9568 in https://github.com/InternLM/lmdeploy/pull/4490
* feat: add Anthropic-compatible serving endpoints by @lvhan028 in https://github.com/InternLM/lmdeploy/pull/4538
* Support InternS2 Preview by @CUHKSZzxy in https://github.com/InternLM/lmdeploy/pull/4575
### 💥 Improvements
* lmdeploy support kernel block size by @Tsundoku958 in https://github.com/InternLM/lmdeploy/pull/4421
* Reject requests on stale session or sleeping engine by @lvhan028 in https://github.com/InternLM/lmdeploy/pull/4496
* Add modern logging utils by @lzhangzz in https://github.com/InternLM/lmdeploy/pull/4486
* refine dlinfer update_weights by @yao-fengchen in https://github.com/InternLM/lmdeploy/pull/4519
* feat(serve): expose repetition n-gram params on OpenAI routes by @lvhan028 in https://github.com/InternLM/lmdeploy/pull/4522
* Refactor step inputs by @grimoire in https://github.com/InternLM/lmdeploy/pull/4504
* fix lite module for transformers>=5.0 by @43758726 in https://github.com/InternLM/lmdeploy/pull/4488
* [refactor] [api_server] [1/N] Improve reasoning and tool-call parsers by @lvhan028 in https://github.com/InternLM/lmdeploy/pull/4468
* fix: prevent prefill starvation under high decode load by @grimoire in https://github.com/InternLM/lmdeploy/pull/4532
* Mixed modality by @CUHKSZzxy in https://github.com/InternLM/lmdeploy/pull/4531
* optimize get_sorted_idx in moe by @grimoire in https://github.com/InternLM/lmdeploy/pull/4529
* Map user-input session_id to internal session_id to maintain session identity by @lvhan028 in https://github.com/InternLM/lmdeploy/pull/4523
* support more message item types by @CUHKSZzxy in https://github.com/InternLM/lmdeploy/pull/4501
* add explicit trust_remote_code controls to resolve the security issue by @lvhan028 in https://github.com/InternLM/lmdeploy/pull/4511
### 🐞 Bug fixes
* [ascend] fix prefix caching by @yao-fengchen in https://github.com/InternLM/lmdeploy/pull/4448
* fix update params by @CUHKSZzxy in https://github.com/InternLM/lmdeploy/pull/4514
* fix ray mem leak by @grimoire in https://github.com/InternLM/lmdeploy/pull/4487
* Fix mtp  by @RunningLeon in https://github.com/InternLM/lmdeploy/pull/4517
* fix kernel-block-size by @grimoire in https://github.com/InternLM/lmdeploy/pull/4521
* fix: use `is not None` check for seed to prevent seed=0 being silently ignored by @kuishou68 in https://github.com/InternLM/lmdeploy/pull/4526
* Fix qwen35 dp by @grimoire in https://github.com/InternLM/lmdeploy/pull/4535
* Fix mtp for rl by @RunningLeon in https://github.com/InternLM/lmdeploy/pull/4520
* cancel request and block new inputs when sleeping by @grimoire in https://github.com/InternLM/lmdeploy/pull/4541
* Fix mp engine by @RunningLeon in https://github.com/InternLM/lmdeploy/pull/4540
* Fix cache sizing and cache block layout edge cases by @grimoire in https://github.com/InternLM/lmdeploy/pull/4552
* Fix qwen3.5-moe mtp with tp>1 by @RunningLeon in https://github.com/InternLM/lmdeploy/pull/4568
* block_offsets padding 0 by @grimoire in https://github.com/InternLM/lmdeploy/pull/4569
* hotfix: resolve test issues for v0.13.0 by @lvhan028 in https://github.com/InternLM/lmdeploy/pull/4571
* ResponseParser forget to strip <think> tag in non-stream mode by @lvhan028 in https://github.com/InternLM/lmdeploy/pull/4576
* yield error when prompt processing suffers exception by @lvhan028 in https://github.com/InternLM/lmdeploy/pull/4574
* Fix the reprefill of evicted seqs with invalid draft tokens by @RunningLeon in https://github.com/InternLM/lmdeploy/pull/4564
* Support mtp fp8 by @RunningLeon in https://github.com/InternLM/lmdeploy/pull/4572
### 🌐 Other
* Use env LMDEPLOY_FP32_MAMBA_SSM_DTYPE to control the dtype of recurrent state by @lvhan028 in https://github.com/InternLM/lmdeploy/pull/4518
* add tool and reasoning test by @littlegy in https://github.com/InternLM/lmdeploy/pull/4388
* update h config and add glm4.7 mtp test by @littlegy in https://github.com/InternLM/lmdeploy/pull/4424
* [ci] change test whl into python 312 and use test images by @zhulinJulia24 in https://github.com/InternLM/lmdeploy/pull/4513
* [Misc] fix typos in turbomind.py and model.py by @ZhijunLStudio in https://github.com/InternLM/lmdeploy/pull/4543
* [Misc] fix mutable default arguments by @ZhijunLStudio in https://github.com/InternLM/lmdeploy/pull/4544
* Add docker/Dockerfile_patch; minor tweaks in messages.py and setup.py. by @lvhan028 in https://github.com/InternLM/lmdeploy/pull/4546
* remove barely used skills and checkin docker-build skill by @lvhan028 in https://github.com/InternLM/lmdeploy/pull/4560
* bump version to v0.13.0 by @lvhan028 in https://github.com/InternLM/lmdeploy/pull/4549

## New Contributors
* @kuishou68 made their first contribution in https://github.com/InternLM/lmdeploy/pull/4526
* @ZhijunLStudio made their first contribution in https://github.com/InternLM/lmdeploy/pull/4543
* @hd9568 made their first contribution in https://github.com/InternLM/lmdeploy/pull/4490

**Full Changelog**: https://github.com/InternLM/lmdeploy/compare/v0.12.3...v0.13.0

## 0.14.0a1 (2026-06-01)

<!-- Release notes generated using configuration in .github/release.yml at v0.14.0a1 -->

## What's Changed
### 🚀 Features
* FP8 kv cache quantization by @CUHKSZzxy in https://github.com/InternLM/lmdeploy/pull/4563
### 💥 Improvements
* Update turbomind modeling infrastructure by @lzhangzz in https://github.com/InternLM/lmdeploy/pull/4557
* refactor(turbomind): consolidate CUDA error handling and add manual stacktracing by @lzhangzz in https://github.com/InternLM/lmdeploy/pull/4565
* Add Qwen3.5 Moe lite awq by @43758726 in https://github.com/InternLM/lmdeploy/pull/4561
* [Improve]: Drain queues when sleep engine by @RunningLeon in https://github.com/InternLM/lmdeploy/pull/4577
* Extend chat completions by introducing token-in/out and returning routed experts by @lvhan028 in https://github.com/InternLM/lmdeploy/pull/4593
* Follow openai's spec to add "AllowedToolChoice" and report 400 when parsing request failed by @lvhan028 in https://github.com/InternLM/lmdeploy/pull/4585
* Improve health endpoint by @lvhan028 in https://github.com/InternLM/lmdeploy/pull/4615
* Remove state init by @grimoire in https://github.com/InternLM/lmdeploy/pull/4604
* Include spec stats in metrics by @RunningLeon in https://github.com/InternLM/lmdeploy/pull/4625
### 🐞 Bug fixes
* fix the anthropic adapter by @lvhan028 in https://github.com/InternLM/lmdeploy/pull/4578
* Fix Structured Output for GPT-OSS Models by @windreamer in https://github.com/InternLM/lmdeploy/pull/4386
* Allow W8A8Linear to accept dtype during initialization instead of hard code by @43758726 in https://github.com/InternLM/lmdeploy/pull/4586
* fix: compact split multimodal tensors by @CUHKSZzxy in https://github.com/InternLM/lmdeploy/pull/4583
* Fix legacy VLM preprocessors for normalized image data by @CUHKSZzxy in https://github.com/InternLM/lmdeploy/pull/4584
* fix dockerfile which missing common.txt by @lvhan028 in https://github.com/InternLM/lmdeploy/pull/4608
* fix: enable FA3 for SM80+ GPUs and fix CUDA version comparison by @windreamer in https://github.com/InternLM/lmdeploy/pull/4591
* flatten_kv_cache zero padding by @grimoire in https://github.com/InternLM/lmdeploy/pull/4613
* align streaming usage chunks with OpenAI spec by @lvhan028 in https://github.com/InternLM/lmdeploy/pull/4616
* fix(vl): reduce multimodal feature memory use by @CUHKSZzxy in https://github.com/InternLM/lmdeploy/pull/4603
* fix memleak when input contain large image data by @grimoire in https://github.com/InternLM/lmdeploy/pull/4610
* fix(turbomind): map Intern-S1 HF checkpoint keys by @lvhan028 in https://github.com/InternLM/lmdeploy/pull/4617
* fix(serve): emit all stream_chunk deltas to fix concurrent tool-call streaming by @lvhan028 in https://github.com/InternLM/lmdeploy/pull/4622
* fix cp inference by @irexyc in https://github.com/InternLM/lmdeploy/pull/4619
* refactor(serve): avoid per-request tokenizer work in parsers by @lvhan028 in https://github.com/InternLM/lmdeploy/pull/4633
* Bring MixtralForCausalLM back to Turbomind by @43758726 in https://github.com/InternLM/lmdeploy/pull/4623
* fix model loading on windows by @irexyc in https://github.com/InternLM/lmdeploy/pull/4626
### 🌐 Other
* chore: gate request logs behind request level by @CUHKSZzxy in https://github.com/InternLM/lmdeploy/pull/4581
* miss rdkit for intern-s models by @lvhan028 in https://github.com/InternLM/lmdeploy/pull/4587
* extract common deps into requirements/common.txt by @lvhan028 in https://github.com/InternLM/lmdeploy/pull/4595
* Remove staled cli arg in vlmevalkit docs by @CUHKSZzxy in https://github.com/InternLM/lmdeploy/pull/4598
* log reponse for debugging by @lvhan028 in https://github.com/InternLM/lmdeploy/pull/4592
* cancel in-progress runs when PR is updated or merged by @lvhan028 in https://github.com/InternLM/lmdeploy/pull/4609
* TEST: update qwen3.5 397b test by @littlegy in https://github.com/InternLM/lmdeploy/pull/4607
* TEST: update video test by @littlegy in https://github.com/InternLM/lmdeploy/pull/4606


**Full Changelog**: https://github.com/InternLM/lmdeploy/compare/v0.13.0...0.14.0a1

## 0.14.0a2 (2026-06-16)

<!-- Release notes generated using configuration in .github/release.yml at main -->

## What's Changed
### 🚀 Features
* FP8 kv cache quantization by @CUHKSZzxy in https://github.com/InternLM/lmdeploy/pull/4563
* Support Qwen3 Omni by @CUHKSZzxy in https://github.com/InternLM/lmdeploy/pull/4411
* support qwen3.5(vit) inference in turbomind backend by @irexyc in https://github.com/InternLM/lmdeploy/pull/4602
* Add OpenAI Responses-compatible endpoint by @CUHKSZzxy in https://github.com/InternLM/lmdeploy/pull/4582
### 💥 Improvements
* Update turbomind modeling infrastructure by @lzhangzz in https://github.com/InternLM/lmdeploy/pull/4557
* refactor(turbomind): consolidate CUDA error handling and add manual stacktracing by @lzhangzz in https://github.com/InternLM/lmdeploy/pull/4565
* Add Qwen3.5 Moe lite awq by @43758726 in https://github.com/InternLM/lmdeploy/pull/4561
* [Improve]: Drain queues when sleep engine by @RunningLeon in https://github.com/InternLM/lmdeploy/pull/4577
* Extend chat completions by introducing token-in/out and returning routed experts by @lvhan028 in https://github.com/InternLM/lmdeploy/pull/4593
* Follow openai's spec to add "AllowedToolChoice" and report 400 when parsing request failed by @lvhan028 in https://github.com/InternLM/lmdeploy/pull/4585
* Improve health endpoint by @lvhan028 in https://github.com/InternLM/lmdeploy/pull/4615
* Remove state init by @grimoire in https://github.com/InternLM/lmdeploy/pull/4604
* Include spec stats in metrics by @RunningLeon in https://github.com/InternLM/lmdeploy/pull/4625
* Add raw chat completion logprob output by @lvhan028 in https://github.com/InternLM/lmdeploy/pull/4637
* fix(pytorch): offload guided decoding CPU ops to thread pool to prevent event loop blocking by @windreamer in https://github.com/InternLM/lmdeploy/pull/4590
* update gated delta rule state layout by @grimoire in https://github.com/InternLM/lmdeploy/pull/4636
* Improve kernel dispatch for dp>1 by @RunningLeon in https://github.com/InternLM/lmdeploy/pull/4653
* Extend v1/messages by introducing token-in/out and returning routed experts by @lvhan028 in https://github.com/InternLM/lmdeploy/pull/4642
* Fuse gdr preprocess by @grimoire in https://github.com/InternLM/lmdeploy/pull/4656
* refactor: simplify multimodal preprocessing expansion by @CUHKSZzxy in https://github.com/InternLM/lmdeploy/pull/4663
### 🐞 Bug fixes
* fix the anthropic adapter by @lvhan028 in https://github.com/InternLM/lmdeploy/pull/4578
* Fix Structured Output for GPT-OSS Models by @windreamer in https://github.com/InternLM/lmdeploy/pull/4386
* Allow W8A8Linear to accept dtype during initialization instead of hard code by @43758726 in https://github.com/InternLM/lmdeploy/pull/4586
* fix: compact split multimodal tensors by @CUHKSZzxy in https://github.com/InternLM/lmdeploy/pull/4583
* Fix legacy VLM preprocessors for normalized image data by @CUHKSZzxy in https://github.com/InternLM/lmdeploy/pull/4584
* fix dockerfile which missing common.txt by @lvhan028 in https://github.com/InternLM/lmdeploy/pull/4608
* fix: enable FA3 for SM80+ GPUs and fix CUDA version comparison by @windreamer in https://github.com/InternLM/lmdeploy/pull/4591
* flatten_kv_cache zero padding by @grimoire in https://github.com/InternLM/lmdeploy/pull/4613
* align streaming usage chunks with OpenAI spec by @lvhan028 in https://github.com/InternLM/lmdeploy/pull/4616
* fix(vl): reduce multimodal feature memory use by @CUHKSZzxy in https://github.com/InternLM/lmdeploy/pull/4603
* fix memleak when input contain large image data by @grimoire in https://github.com/InternLM/lmdeploy/pull/4610
* fix(turbomind): map Intern-S1 HF checkpoint keys by @lvhan028 in https://github.com/InternLM/lmdeploy/pull/4617
* fix(serve): emit all stream_chunk deltas to fix concurrent tool-call streaming by @lvhan028 in https://github.com/InternLM/lmdeploy/pull/4622
* fix cp inference by @irexyc in https://github.com/InternLM/lmdeploy/pull/4619
* refactor(serve): avoid per-request tokenizer work in parsers by @lvhan028 in https://github.com/InternLM/lmdeploy/pull/4633
* Bring MixtralForCausalLM back to Turbomind by @43758726 in https://github.com/InternLM/lmdeploy/pull/4623
* fix model loading on windows by @irexyc in https://github.com/InternLM/lmdeploy/pull/4626
* Fix mtp cudagraph when no warmup in RL by @RunningLeon in https://github.com/InternLM/lmdeploy/pull/4641
* fix: remove hard CUDA_PATH assert on Windows, search DLL paths from multiple sources by @windreamer in https://github.com/InternLM/lmdeploy/pull/4628
* Fix unit test by removing latest-transformers-unsupported models by @lvhan028 in https://github.com/InternLM/lmdeploy/pull/4649
* Fix qwen3.5 mtp  by @RunningLeon in https://github.com/InternLM/lmdeploy/pull/4652
* fix gdr kernel for tilelang>=0.1.9 by @grimoire in https://github.com/InternLM/lmdeploy/pull/4660
* [Fix]: Revert the reuse of cudagraph buffer for mtp by @RunningLeon in https://github.com/InternLM/lmdeploy/pull/4661
* Fix client-disconnect session leaks in PyTorch MP engine by @grimoire in https://github.com/InternLM/lmdeploy/pull/4655
* fix cancel stopped seq by @RunningLeon in https://github.com/InternLM/lmdeploy/pull/4654
* feat: support num_experts_per_tok=10 in turbomind backend by @irexyc in https://github.com/InternLM/lmdeploy/pull/4665
* fix batched seqs with different stop words by @RunningLeon in https://github.com/InternLM/lmdeploy/pull/4671
* Move warmup inside wakeup by @RunningLeon in https://github.com/InternLM/lmdeploy/pull/4667
* Fix dequant_mixed by @irexyc in https://github.com/InternLM/lmdeploy/pull/4657
* Improve engine health monitoring by @lvhan028 in https://github.com/InternLM/lmdeploy/pull/4645
* fix qwen3.5 27b gdr preprocess by @grimoire in https://github.com/InternLM/lmdeploy/pull/4676
### 📚 Documentations
* docs: update multimodal model support docs by @CUHKSZzxy in https://github.com/InternLM/lmdeploy/pull/4643
### 🌐 Other
* chore: gate request logs behind request level by @CUHKSZzxy in https://github.com/InternLM/lmdeploy/pull/4581
* miss rdkit for intern-s models by @lvhan028 in https://github.com/InternLM/lmdeploy/pull/4587
* extract common deps into requirements/common.txt by @lvhan028 in https://github.com/InternLM/lmdeploy/pull/4595
* Remove staled cli arg in vlmevalkit docs by @CUHKSZzxy in https://github.com/InternLM/lmdeploy/pull/4598
* log reponse for debugging by @lvhan028 in https://github.com/InternLM/lmdeploy/pull/4592
* cancel in-progress runs when PR is updated or merged by @lvhan028 in https://github.com/InternLM/lmdeploy/pull/4609
* TEST: update qwen3.5 397b test by @littlegy in https://github.com/InternLM/lmdeploy/pull/4607
* TEST: update video test by @littlegy in https://github.com/InternLM/lmdeploy/pull/4606
* Validate final chat response structure by @lvhan028 in https://github.com/InternLM/lmdeploy/pull/4621
* Support dp for qwen35 mtp by @RunningLeon in https://github.com/InternLM/lmdeploy/pull/4611
* [ci] refactor testcoverage config by @zhulinJulia24 in https://github.com/InternLM/lmdeploy/pull/4630
* TEST: update ascend and mtp test config by @littlegy in https://github.com/InternLM/lmdeploy/pull/4659
* TEST: update FP8 processing logic and remove duplicate MTP tests by @littlegy in https://github.com/InternLM/lmdeploy/pull/4668
* freeze tilelang version by @grimoire in https://github.com/InternLM/lmdeploy/pull/4669
* fix windows ci by @irexyc in https://github.com/InternLM/lmdeploy/pull/4672
* [ci] add mtp test config in pr_test by @zhulinJulia24 in https://github.com/InternLM/lmdeploy/pull/4651


**Full Changelog**: https://github.com/InternLM/lmdeploy/compare/v0.13.0...0.14.0a2

## v0.14.0 (2026-06-24)

<!-- Release notes generated using configuration in .github/release.yml at main -->

## What's Changed
### 🚀 Features
* FP8 kv cache quantization by @CUHKSZzxy in https://github.com/InternLM/lmdeploy/pull/4563
* Support Qwen3 Omni by @CUHKSZzxy in https://github.com/InternLM/lmdeploy/pull/4411
* support qwen3.5(vit) inference in turbomind backend by @irexyc in https://github.com/InternLM/lmdeploy/pull/4602
* Add OpenAI Responses-compatible endpoint by @CUHKSZzxy in https://github.com/InternLM/lmdeploy/pull/4582
* Add /get_ppl endpoint by @irexyc in https://github.com/InternLM/lmdeploy/pull/4679
### 💥 Improvements
* Update turbomind modeling infrastructure by @lzhangzz in https://github.com/InternLM/lmdeploy/pull/4557
* refactor(turbomind): consolidate CUDA error handling and add manual stacktracing by @lzhangzz in https://github.com/InternLM/lmdeploy/pull/4565
* Add Qwen3.5 Moe lite awq by @43758726 in https://github.com/InternLM/lmdeploy/pull/4561
* [Improve]: Drain queues when sleep engine by @RunningLeon in https://github.com/InternLM/lmdeploy/pull/4577
* Extend chat completions by introducing token-in/out and returning routed experts by @lvhan028 in https://github.com/InternLM/lmdeploy/pull/4593
* Follow openai's spec to add "AllowedToolChoice" and report 400 when parsing request failed by @lvhan028 in https://github.com/InternLM/lmdeploy/pull/4585
* Improve health endpoint by @lvhan028 in https://github.com/InternLM/lmdeploy/pull/4615
* Remove state init by @grimoire in https://github.com/InternLM/lmdeploy/pull/4604
* Include spec stats in metrics by @RunningLeon in https://github.com/InternLM/lmdeploy/pull/4625
* Add raw chat completion logprob output by @lvhan028 in https://github.com/InternLM/lmdeploy/pull/4637
* fix(pytorch): offload guided decoding CPU ops to thread pool to prevent event loop blocking by @windreamer in https://github.com/InternLM/lmdeploy/pull/4590
* update gated delta rule state layout by @grimoire in https://github.com/InternLM/lmdeploy/pull/4636
* Improve kernel dispatch for dp>1 by @RunningLeon in https://github.com/InternLM/lmdeploy/pull/4653
* Extend v1/messages by introducing token-in/out and returning routed experts by @lvhan028 in https://github.com/InternLM/lmdeploy/pull/4642
* Fuse gdr preprocess by @grimoire in https://github.com/InternLM/lmdeploy/pull/4656
* refactor: simplify multimodal preprocessing expansion by @CUHKSZzxy in https://github.com/InternLM/lmdeploy/pull/4663
* feat: configure cudagraph capture batch sizes by @CUHKSZzxy in https://github.com/InternLM/lmdeploy/pull/4573
* Refactor prefix caching for pytorch engine by @grimoire in https://github.com/InternLM/lmdeploy/pull/4618
* Pading one more block for fa3 prefill by @RunningLeon in https://github.com/InternLM/lmdeploy/pull/4674
* Add usage.prompt_tokens_details.cached_tokens for prefix caching by @lvhan028 in https://github.com/InternLM/lmdeploy/pull/4670
* Optimize XML tool parsers with incremental streaming and fast-path buffering by @lvhan028 in https://github.com/InternLM/lmdeploy/pull/4664
### 🐞 Bug fixes
* fix the anthropic adapter by @lvhan028 in https://github.com/InternLM/lmdeploy/pull/4578
* Fix Structured Output for GPT-OSS Models by @windreamer in https://github.com/InternLM/lmdeploy/pull/4386
* Allow W8A8Linear to accept dtype during initialization instead of hard code by @43758726 in https://github.com/InternLM/lmdeploy/pull/4586
* fix: compact split multimodal tensors by @CUHKSZzxy in https://github.com/InternLM/lmdeploy/pull/4583
* Fix legacy VLM preprocessors for normalized image data by @CUHKSZzxy in https://github.com/InternLM/lmdeploy/pull/4584
* fix dockerfile which missing common.txt by @lvhan028 in https://github.com/InternLM/lmdeploy/pull/4608
* fix: enable FA3 for SM80+ GPUs and fix CUDA version comparison by @windreamer in https://github.com/InternLM/lmdeploy/pull/4591
* flatten_kv_cache zero padding by @grimoire in https://github.com/InternLM/lmdeploy/pull/4613
* align streaming usage chunks with OpenAI spec by @lvhan028 in https://github.com/InternLM/lmdeploy/pull/4616
* fix(vl): reduce multimodal feature memory use by @CUHKSZzxy in https://github.com/InternLM/lmdeploy/pull/4603
* fix memleak when input contain large image data by @grimoire in https://github.com/InternLM/lmdeploy/pull/4610
* fix(turbomind): map Intern-S1 HF checkpoint keys by @lvhan028 in https://github.com/InternLM/lmdeploy/pull/4617
* fix(serve): emit all stream_chunk deltas to fix concurrent tool-call streaming by @lvhan028 in https://github.com/InternLM/lmdeploy/pull/4622
* fix cp inference by @irexyc in https://github.com/InternLM/lmdeploy/pull/4619
* refactor(serve): avoid per-request tokenizer work in parsers by @lvhan028 in https://github.com/InternLM/lmdeploy/pull/4633
* Bring MixtralForCausalLM back to Turbomind by @43758726 in https://github.com/InternLM/lmdeploy/pull/4623
* fix model loading on windows by @irexyc in https://github.com/InternLM/lmdeploy/pull/4626
* Fix mtp cudagraph when no warmup in RL by @RunningLeon in https://github.com/InternLM/lmdeploy/pull/4641
* fix: remove hard CUDA_PATH assert on Windows, search DLL paths from multiple sources by @windreamer in https://github.com/InternLM/lmdeploy/pull/4628
* Fix unit test by removing latest-transformers-unsupported models by @lvhan028 in https://github.com/InternLM/lmdeploy/pull/4649
* Fix qwen3.5 mtp  by @RunningLeon in https://github.com/InternLM/lmdeploy/pull/4652
* fix gdr kernel for tilelang>=0.1.9 by @grimoire in https://github.com/InternLM/lmdeploy/pull/4660
* [Fix]: Revert the reuse of cudagraph buffer for mtp by @RunningLeon in https://github.com/InternLM/lmdeploy/pull/4661
* Fix client-disconnect session leaks in PyTorch MP engine by @grimoire in https://github.com/InternLM/lmdeploy/pull/4655
* fix cancel stopped seq by @RunningLeon in https://github.com/InternLM/lmdeploy/pull/4654
* feat: support num_experts_per_tok=10 in turbomind backend by @irexyc in https://github.com/InternLM/lmdeploy/pull/4665
* fix batched seqs with different stop words by @RunningLeon in https://github.com/InternLM/lmdeploy/pull/4671
* Move warmup inside wakeup by @RunningLeon in https://github.com/InternLM/lmdeploy/pull/4667
* Fix dequant_mixed by @irexyc in https://github.com/InternLM/lmdeploy/pull/4657
* Improve engine health monitoring by @lvhan028 in https://github.com/InternLM/lmdeploy/pull/4645
* fix qwen3.5 27b gdr preprocess by @grimoire in https://github.com/InternLM/lmdeploy/pull/4676
* Fix dequant mixed for qwen3.5 quantized model made by vllm/llm-compressor by @irexyc in https://github.com/InternLM/lmdeploy/pull/4675
* [Bugfix] Fix double-counted max_q_seqlen in decode delta kv_seqlens by @waynehacking8 in https://github.com/InternLM/lmdeploy/pull/4685
* Fix scheduler for ssm by @RunningLeon in https://github.com/InternLM/lmdeploy/pull/4691
* fix(serve): avoid parallel tool-call argument leakage in XML parsers by @lvhan028 in https://github.com/InternLM/lmdeploy/pull/4692
* fix prefix caching by @grimoire in https://github.com/InternLM/lmdeploy/pull/4700
### 📚 Documentations
* docs: update multimodal model support docs by @CUHKSZzxy in https://github.com/InternLM/lmdeploy/pull/4643
### 🌐 Other
* chore: gate request logs behind request level by @CUHKSZzxy in https://github.com/InternLM/lmdeploy/pull/4581
* miss rdkit for intern-s models by @lvhan028 in https://github.com/InternLM/lmdeploy/pull/4587
* extract common deps into requirements/common.txt by @lvhan028 in https://github.com/InternLM/lmdeploy/pull/4595
* Remove staled cli arg in vlmevalkit docs by @CUHKSZzxy in https://github.com/InternLM/lmdeploy/pull/4598
* log reponse for debugging by @lvhan028 in https://github.com/InternLM/lmdeploy/pull/4592
* cancel in-progress runs when PR is updated or merged by @lvhan028 in https://github.com/InternLM/lmdeploy/pull/4609
* TEST: update qwen3.5 397b test by @littlegy in https://github.com/InternLM/lmdeploy/pull/4607
* TEST: update video test by @littlegy in https://github.com/InternLM/lmdeploy/pull/4606
* Validate final chat response structure by @lvhan028 in https://github.com/InternLM/lmdeploy/pull/4621
* Support dp for qwen35 mtp by @RunningLeon in https://github.com/InternLM/lmdeploy/pull/4611
* [ci] refactor testcoverage config by @zhulinJulia24 in https://github.com/InternLM/lmdeploy/pull/4630
* TEST: update ascend and mtp test config by @littlegy in https://github.com/InternLM/lmdeploy/pull/4659
* TEST: update FP8 processing logic and remove duplicate MTP tests by @littlegy in https://github.com/InternLM/lmdeploy/pull/4668
* freeze tilelang version by @grimoire in https://github.com/InternLM/lmdeploy/pull/4669
* fix windows ci by @irexyc in https://github.com/InternLM/lmdeploy/pull/4672
* [ci] add mtp test config in pr_test by @zhulinJulia24 in https://github.com/InternLM/lmdeploy/pull/4651
* support disaggregated weight update by @irexyc in https://github.com/InternLM/lmdeploy/pull/4638
* bump version to v0.14.0 by @lvhan028 in https://github.com/InternLM/lmdeploy/pull/4689

## New Contributors
* @waynehacking8 made their first contribution in https://github.com/InternLM/lmdeploy/pull/4685

**Full Changelog**: https://github.com/InternLM/lmdeploy/compare/v0.13.0...v0.14.0

## v0.15.0 (2026-07-31)

<!-- Release notes generated using configuration in .github/release.yml at main -->

## What's Changed
### 🚀 Features
* Support long-context and MTP prefix-cache hits by @grimoire in https://github.com/InternLM/lmdeploy/pull/4688
* [Feature] Add guided decoding support for speculative decoding by @windreamer in https://github.com/InternLM/lmdeploy/pull/4559
* feat(turbomind): memory allocator, object cache, and scheduler integration by @lzhangzz in https://github.com/InternLM/lmdeploy/pull/4717
* feat: add AgRs all2all backend by @irexyc in https://github.com/InternLM/lmdeploy/pull/4739
* DeepSeek V4 support by @grimoire in https://github.com/InternLM/lmdeploy/pull/4554
* Support memdecode  by @lvhan028 in https://github.com/InternLM/lmdeploy/pull/4767
### 💥 Improvements
* Force blksize=128 for linear attention on ascend by @jinminxi104 in https://github.com/InternLM/lmdeploy/pull/4705
* refactor: unify interleaved MRoPE rotary embedding by @CUHKSZzxy in https://github.com/InternLM/lmdeploy/pull/4644
* Refine multi-node support on ascend-A3 by @jinminxi104 in https://github.com/InternLM/lmdeploy/pull/4711
* [Improve]: Remove dlblas from lmdeploy by @RunningLeon in https://github.com/InternLM/lmdeploy/pull/4682
* replace sync with wait event in h2d by @grimoire in https://github.com/InternLM/lmdeploy/pull/4709
* Respect --server-port in DP mode when proxy-url is set by @lvhan028 in https://github.com/InternLM/lmdeploy/pull/4712
* add --language-model-only for text-only VLM inference and remove --disable-vision-encoder by @lvhan028 in https://github.com/InternLM/lmdeploy/pull/4716
* Optimize TTFT by @grimoire in https://github.com/InternLM/lmdeploy/pull/4695
* Optimize BaseResponseParser streaming and add parser benchmark by @lvhan028 in https://github.com/InternLM/lmdeploy/pull/4697
* Support fp8 moe only for qwen3.5 by @RunningLeon in https://github.com/InternLM/lmdeploy/pull/4740
* clear runtime state in sleep by @grimoire in https://github.com/InternLM/lmdeploy/pull/4729
* feat(serve): add --generation-config CLI for server sampling defaults by @lvhan028 in https://github.com/InternLM/lmdeploy/pull/4708
* fix: gzip torch profiler traces by default by @CUHKSZzxy in https://github.com/InternLM/lmdeploy/pull/4747
* Optimize tp fp8 moe for small average router per expert by @grimoire in https://github.com/InternLM/lmdeploy/pull/4751
* refactor(pytorch): clarify scheduler and input-maker control flow by @grimoire in https://github.com/InternLM/lmdeploy/pull/4727
* Guard DP dummy inputs around pending work by @grimoire in https://github.com/InternLM/lmdeploy/pull/4738
* Remove interactive chat and make inference stateless by @lvhan028 in https://github.com/InternLM/lmdeploy/pull/4730
* feat(turbomind): Derive composable TurboMind parallel configurations by @lzhangzz in https://github.com/InternLM/lmdeploy/pull/4769
* Add generic tensor copy and architecture-aware Gated Delta Rule support by @lzhangzz in https://github.com/InternLM/lmdeploy/pull/4757
* Add GDR CP controls and legacy kernel override by @lzhangzz in https://github.com/InternLM/lmdeploy/pull/4779
* fix(turbomind): fix zero-centered RMSNorm for Qwen3.5 by @lzhangzz in https://github.com/InternLM/lmdeploy/pull/4790
### 🐞 Bug fixes
* fix prefix caching by @grimoire in https://github.com/InternLM/lmdeploy/pull/4700
* fix `_reduce_split_kernel` for triton 3.5.1 by @irexyc in https://github.com/InternLM/lmdeploy/pull/4696
* fix triton fp8 all_reduce group by @grimoire in https://github.com/InternLM/lmdeploy/pull/4702
* fix(serve): use unique chatcmpl id for chat completions responses by @lvhan028 in https://github.com/InternLM/lmdeploy/pull/4707
* [Bugfix] Fix ImportError in get_chat_template for builtin chat-template names by @waynehacking8 in https://github.com/InternLM/lmdeploy/pull/4690
* [Bugfix] Fix InternVL/InternVL3 LoRA loading TypeError in adapter fallback by @waynehacking8 in https://github.com/InternLM/lmdeploy/pull/4684
* Force blksize=128 when head_dim=256 on ascend by @wanfengcxz in https://github.com/InternLM/lmdeploy/pull/4723
* fix HCCL port conflict on multi-dp rank startup(single node) by @wanfengcxz in https://github.com/InternLM/lmdeploy/pull/4722
* fix: fail fast on invalid serve parsers by @CUHKSZzxy in https://github.com/InternLM/lmdeploy/pull/4701
* fix: parse multimodal tool messages by @CUHKSZzxy in https://github.com/InternLM/lmdeploy/pull/4680
* Reprobe once for health request by @RunningLeon in https://github.com/InternLM/lmdeploy/pull/4703
* fix: enable graph capture during DP warmup decoding by @wanfengcxz in https://github.com/InternLM/lmdeploy/pull/4728
* fix: proper XGrammar integration for guided decoding by @windreamer in https://github.com/InternLM/lmdeploy/pull/4726
* fix: release multimodal payload after mp handoff by @CUHKSZzxy in https://github.com/InternLM/lmdeploy/pull/4725
* Fix MTP recurrent state round-trip for Qwen3.5 by @RunningLeon in https://github.com/InternLM/lmdeploy/pull/4744
* Fix mtp dpmeta and guard the warmup by @RunningLeon in https://github.com/InternLM/lmdeploy/pull/4741
* Fix GLM MTP  by @RunningLeon in https://github.com/InternLM/lmdeploy/pull/4749
* fix false negative healthy status check for turbomind  by @irexyc in https://github.com/InternLM/lmdeploy/pull/4745
* fix(vl): forward tools to multimodal chat templates by @lvhan028 in https://github.com/InternLM/lmdeploy/pull/4759
* fix: restrict remote media domains by @CUHKSZzxy in https://github.com/InternLM/lmdeploy/pull/4734
* fix(turbomind): restore INT8 KV quant-param offset in block layout by @lzhangzz in https://github.com/InternLM/lmdeploy/pull/4764
* fix(turbomind): avoid async TP shutdown deadlock by @lzhangzz in https://github.com/InternLM/lmdeploy/pull/4770
* fix: bound grouped GEMM scheduling by routed tokens by @lzhangzz in https://github.com/InternLM/lmdeploy/pull/4771
* feat(turbomind): enable SM90 GDR PDL and fix CP matrix layout by @lzhangzz in https://github.com/InternLM/lmdeploy/pull/4787
* fix(serve): auto-generate batch completion sessions to avoid id collision (#4773) by @Anai-Guo in https://github.com/InternLM/lmdeploy/pull/4774
* feat(turbomind): restore metrics reporting by @lvhan028 in https://github.com/InternLM/lmdeploy/pull/4768
* fix: skip interns2 preview time-series weights by @CUHKSZzxy in https://github.com/InternLM/lmdeploy/pull/4801
* fix(serve): handle missing logprobs attrs on TurbomindEngineConfig in Anthropic messages by @lvhan028 in https://github.com/InternLM/lmdeploy/pull/4800
### 🌐 Other
* bump version to v0.14.0 by @lvhan028 in https://github.com/InternLM/lmdeploy/pull/4689
* TEST: Improve tool test by @littlegy in https://github.com/InternLM/lmdeploy/pull/4632
* chore: update deepgemm revision by @CUHKSZzxy in https://github.com/InternLM/lmdeploy/pull/4713
* TEST：Add H Prefix Cache Test, HF Path Conversion, and Ascend Multi-node Startup Config by @littlegy in https://github.com/InternLM/lmdeploy/pull/4706
* chore: remove deprecated model support by @CUHKSZzxy in https://github.com/InternLM/lmdeploy/pull/4693
* [Ascend] support qwen35 mtp on Ascend-A3 by @wanfengcxz in https://github.com/InternLM/lmdeploy/pull/4721
* ci: pin jlumbroso/free-disk-space to a full commit SHA by @kobihikri in https://github.com/InternLM/lmdeploy/pull/4748
* fix: install xgrammar for jetson docker by @CUHKSZzxy in https://github.com/InternLM/lmdeploy/pull/4758
* update turbomind builder image by @irexyc in https://github.com/InternLM/lmdeploy/pull/4752
* fix(autotest): drop flaky text inequality in same session_id generate test by @littlegy in https://github.com/InternLM/lmdeploy/pull/4766
* fix(benchmark): seed NumPy RNG so --seed controls random-mode lengths (#4784) by @Anai-Guo in https://github.com/InternLM/lmdeploy/pull/4785
* update anthropic endpoint test by @littlegy in https://github.com/InternLM/lmdeploy/pull/4594
* Update multimodal toolcall tests by @littlegy in https://github.com/InternLM/lmdeploy/pull/4742
* Remove obsolete C++ tests by @lzhangzz in https://github.com/InternLM/lmdeploy/pull/4796
* [Docs] Fix typos in contribution guide by @cupkk in https://github.com/InternLM/lmdeploy/pull/4807
* bump version to v0.15.0 by @lvhan028 in https://github.com/InternLM/lmdeploy/pull/4791

## New Contributors
* @kobihikri made their first contribution in https://github.com/InternLM/lmdeploy/pull/4748
* @Anai-Guo made their first contribution in https://github.com/InternLM/lmdeploy/pull/4785
* @cupkk made their first contribution in https://github.com/InternLM/lmdeploy/pull/4807

**Full Changelog**: https://github.com/InternLM/lmdeploy/compare/v0.14.0...v0.15.0

## v0.16.0 (2026-08-19)

<!-- Release notes generated using configuration in .github/release.yml at main -->

## What's Changed
### 🚀 Features
* Support Interns2 mobius by @RunningLeon in https://github.com/InternLM/lmdeploy/pull/4816
* feat: support GLM-5.2 by @CUHKSZzxy in https://github.com/InternLM/lmdeploy/pull/4737
* Intern-S2-Mobius meta-MoE support, MoE gate v2, CP attention fixes by @lzhangzz in https://github.com/InternLM/lmdeploy/pull/4835
* Add TurboMind ViT support for InternVL and Qwen VL models by @irexyc in https://github.com/InternLM/lmdeploy/pull/4719
* feat: add Hy3 support, MTP, and FP8 optimizations by @yidingcheng0206 in https://github.com/InternLM/lmdeploy/pull/4815
### 💥 Improvements
* refactor: report cache usage directly by @lvhan028 in https://github.com/InternLM/lmdeploy/pull/4798
* SM90 native BF16/FP8 GEMM kernels, fused-SiLU quantization, and linear test harness by @lzhangzz in https://github.com/InternLM/lmdeploy/pull/4795
* refactor: split api server endpoints by @lvhan028 in https://github.com/InternLM/lmdeploy/pull/4797
* refactor(pytorch): derive CUDA step metadata from selected operators by @grimoire in https://github.com/InternLM/lmdeploy/pull/4805
* optimize and modularize SSM prefix caching by @grimoire in https://github.com/InternLM/lmdeploy/pull/4788
* perf(guided-decoding): optimize with async D2H copy and xgrammar v0.2.1 by @windreamer in https://github.com/InternLM/lmdeploy/pull/4605
* refactor(serve): split chat_completions endpoint into a package by @lvhan028 in https://github.com/InternLM/lmdeploy/pull/4840
* feat(chat-completions): add usage.completion_tokens_details by @lvhan028 in https://github.com/InternLM/lmdeploy/pull/4842
* feat(pytorch): add optimized Gluon blocked FP8 GEMM for Hopper by @grimoire in https://github.com/InternLM/lmdeploy/pull/4830
* perf(pytorch): add opt-in torch.compile for decode CUDA graphs by @grimoire in https://github.com/InternLM/lmdeploy/pull/4808
* Ssm prefix cache non aligned by @grimoire in https://github.com/InternLM/lmdeploy/pull/4799
* perf: optimize GLM-5.2 serving by @CUHKSZzxy in https://github.com/InternLM/lmdeploy/pull/4827
* refactor: separate request preprocessing from generation by @lvhan028 in https://github.com/InternLM/lmdeploy/pull/4856
### 🐞 Bug fixes
* [Bugfix] Fix PyTorch H2D input lifetime across CUDA streams by @grimoire in https://github.com/InternLM/lmdeploy/pull/4792
* fix(serve): reject empty/falsy prompt input in format_prompts and AsyncEngine.generate by @SuperMarioYL in https://github.com/InternLM/lmdeploy/pull/4803
* Fix ray mp duplicate output by @RunningLeon in https://github.com/InternLM/lmdeploy/pull/4833
* fix(turbomind): dispatch cuMemcpyBatchAsync by CUDA runtime version by @lvhan028 in https://github.com/InternLM/lmdeploy/pull/4838
* fix(disagg): use JSON instead of pickle for P2P ZMQ requests (#4804) by @Anai-Guo in https://github.com/InternLM/lmdeploy/pull/4812
* fix(serve): emit signatures for Anthropic thinking blocks by @matrix72c in https://github.com/InternLM/lmdeploy/pull/4851
* Fix int4 KV cache quantization range when the packed head width is not a power of two by @truong-v in https://github.com/InternLM/lmdeploy/pull/4850
* fix: harden serving request validation by @lvhan028 in https://github.com/InternLM/lmdeploy/pull/4872
* fix: fix allgather/allgather2d for cuda-ipc when byte_width is not multiple of uint by @irexyc in https://github.com/InternLM/lmdeploy/pull/4873
### 📚 Documentations
* docs: update recent model support by @CUHKSZzxy in https://github.com/InternLM/lmdeploy/pull/4855
* docs,tests: cover Qwen3.8 preserve_thinking support by @lvhan028 in https://github.com/InternLM/lmdeploy/pull/4869
### 🌐 Other
* docs: remove non-existent `--enable-metrics` flag from metrics/spec_decoding guides by @latent-9 in https://github.com/InternLM/lmdeploy/pull/4809
* Upgrade to cu130 by @RunningLeon in https://github.com/InternLM/lmdeploy/pull/4753
* TEST: update turbomind qwen3.5 config by @littlegy in https://github.com/InternLM/lmdeploy/pull/4778
* chore: use python3.12 for docformatter pre-commit hook by @lvhan028 in https://github.com/InternLM/lmdeploy/pull/4839
* ci: support CUDA 13.0 Docker builds and publishing by @lvhan028 in https://github.com/InternLM/lmdeploy/pull/4817
* TEST: update deepseekv4-flash config by @littlegy in https://github.com/InternLM/lmdeploy/pull/4836
* [ci] Adjust evaluation gate benchmark datasets to reduce runtime and extend coverage by @zhulinJulia24 in https://github.com/InternLM/lmdeploy/pull/4834
* [ci] remove old models and refactor interface testcase by @zhulinJulia24 in https://github.com/InternLM/lmdeploy/pull/4806
* bump version to v0.16.0 by @lvhan028 in https://github.com/InternLM/lmdeploy/pull/4847

## New Contributors
* @latent-9 made their first contribution in https://github.com/InternLM/lmdeploy/pull/4809
* @SuperMarioYL made their first contribution in https://github.com/InternLM/lmdeploy/pull/4803
* @yidingcheng0206 made their first contribution in https://github.com/InternLM/lmdeploy/pull/4815
* @matrix72c made their first contribution in https://github.com/InternLM/lmdeploy/pull/4851
* @truong-v made their first contribution in https://github.com/InternLM/lmdeploy/pull/4850

**Full Changelog**: https://github.com/InternLM/lmdeploy/compare/v0.15.0...v0.16.0

## v0.17.0 (2026-09-01)

<!-- Release notes generated using configuration in .github/release.yml at main -->

## What's Changed
### 🚀 Features
* Integrate DeepEPv2 by @irexyc in https://github.com/InternLM/lmdeploy/pull/4783
* feat(pytorch): support Kimi K2.6  by @qescccczmr in https://github.com/InternLM/lmdeploy/pull/4846
* feat(kv_connector): support mooncake store by @caikun-pjlab in https://github.com/InternLM/lmdeploy/pull/4903
### 💥 Improvements
* feat(chat-completions): server-side fan-out for n>1 choices by @lvhan028 in https://github.com/InternLM/lmdeploy/pull/4841
* perf: further optimize GLM-5.2 serving by @CUHKSZzxy in https://github.com/InternLM/lmdeploy/pull/4853
* perf(cuda): use PDL for paged attention and V4 prefill by @grimoire in https://github.com/InternLM/lmdeploy/pull/4861
* [ascend] update attn op_backend by @wanfengcxz in https://github.com/InternLM/lmdeploy/pull/4900
* perf(pytorch): optimize compact blocked FP8 MoE and route preparation by @grimoire in https://github.com/InternLM/lmdeploy/pull/4857
* perf(pytorch): reduce speculative decoding pre/post-processing overhead by @grimoire in https://github.com/InternLM/lmdeploy/pull/4877
* support page size that are not power of two by @irexyc in https://github.com/InternLM/lmdeploy/pull/4854
* feat: support structural_tag response_format for turbomind and pytorch engines by @windreamer in https://github.com/InternLM/lmdeploy/pull/4906
### 🐞 Bug fixes
* fix(turbomind): restore FP8 weight-only fallback on pre-sm90 GPUs by @lvhan028 in https://github.com/InternLM/lmdeploy/pull/4871
* fix(vl): raise a clear error on malformed data URLs by @SuperMarioYL in https://github.com/InternLM/lmdeploy/pull/4837
* fix(api): fix reponses interface by @caikun-pjlab in https://github.com/InternLM/lmdeploy/pull/4893
* Fix/dsv4 native transformers warmup by @grimoire in https://github.com/InternLM/lmdeploy/pull/4878
* fix: support inline system messages in Anthropic API by @lvhan028 in https://github.com/InternLM/lmdeploy/pull/4882
* fix: bound DSA prefill score memory by @CUHKSZzxy in https://github.com/InternLM/lmdeploy/pull/4896
* fix(build): correct GEMM kernel archive link order by @lvhan028 in https://github.com/InternLM/lmdeploy/pull/4910
* fix: reject unavailable GLM tool calls by @CUHKSZzxy in https://github.com/InternLM/lmdeploy/pull/4901
* fix(pytorch): avoid Triton miscompile in paged attention reduction by @lvhan028 in https://github.com/InternLM/lmdeploy/pull/4920
* fix Intern-S2-Preview-FP8 convert by @irexyc in https://github.com/InternLM/lmdeploy/pull/4923
### 🌐 Other
* [Fix] Validate cross-file Markdown link targets by @JimmyWang0417 in https://github.com/InternLM/lmdeploy/pull/4868
* Update README to Reflect EuroSys 2027 Paper Acceptance by @Youhe-Jiang in https://github.com/InternLM/lmdeploy/pull/4891
* docs: fix grammar in README by @MarkHe1222 in https://github.com/InternLM/lmdeploy/pull/4866
* improve(autotest): trim unused model configs and gate routed_experts on yaml by @littlegy in https://github.com/InternLM/lmdeploy/pull/4885
* build: remove flashinfer from CUDA runtime requirements by @CUHKSZzxy in https://github.com/InternLM/lmdeploy/pull/4902
* [ci] add base api eval test workflow by @zhulinJulia24 in https://github.com/InternLM/lmdeploy/pull/4874
* bump version to v0.17.0 by @lvhan028 in https://github.com/InternLM/lmdeploy/pull/4914

## New Contributors
* @JimmyWang0417 made their first contribution in https://github.com/InternLM/lmdeploy/pull/4868
* @Youhe-Jiang made their first contribution in https://github.com/InternLM/lmdeploy/pull/4891
* @MarkHe1222 made their first contribution in https://github.com/InternLM/lmdeploy/pull/4866
* @qescccczmr made their first contribution in https://github.com/InternLM/lmdeploy/pull/4846

**Full Changelog**: https://github.com/InternLM/lmdeploy/compare/v0.16.0...v0.17.0
