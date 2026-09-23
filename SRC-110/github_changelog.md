# Changelog (aggregated from releases.body)

> releases: 56

## v0.2.5 (2024-04-02)

Init release version: 0.2.5

## v0.2.6 (2024-04-03)

1. Support loading cmmlu from local disk

## v0.2.8 (2024-06-18)

1. Fix local dir eval
2. Add fuzzy match for templates
3. Add local models with templates

## v0.4.3 (2024-07-29)

1. Support async client infer for OpenAI API format evaluation
2. Support mulati-modal evaluation with VLMEvalKit as a eval-backend
3. Refactor setup, support pip install llmuses[opencompass], pip install llmuses[vlmeval], pip install llmuses[all]
4. Fix some bugs

## v0.5.2 (2024-08-09)


## Highlight features
- Support Multi-modal models evaluation (VLM Eval) 
- Transform the synchronous API to asynchronous for OpenAI's API format, speed up the evaluation process up to 10x .
- Support installation with format: `pip install evalscope[opencompass]` or `pip install evalscope[vlmeval]`


## Breaking Changes
None


## What's Changed
1. Support Multi-modal models evaluation (VLM Eval) 
2. Transform the synchronous API to asynchronous for OpenAI's API format, speed up the evaluation process up to 10x .
3. Support installation with format: `pip install evalscope[opencompass]` or `pip install evalscope[vlmeval]`
4. Update README
5. Add UT cases for VLM eval
6. Update examples for `OpenCompass` and `VLMEval` eval backends
7. Update version restrictions for ms-opencompass and ms-vlmeval dependencies.



## v0.5.5 (2024-10-15)

# Release Notes 

1. Added Dataset Support:
    - Enhanced multimodal evaluation capabilities, now supporting MMBench-Video, Video-MME, and MVBench video evaluations https://github.com/modelscope/evalscope/pull/146
    - Added cmb dataset https://github.com/modelscope/evalscope/pull/117

2. Support for `LongBench-write` quality evaluation of long text generation https://github.com/modelscope/evalscope/pull/136

3. Automatic downloading of `punkt_tab.zip` from `nltk` https://github.com/modelscope/evalscope/pull/140

4. Support for RAG evaluation https://github.com/modelscope/evalscope/pull/127:
    - Support for embeddings/reranker evaluation: Integration of `MTEB` (Massive Text Embedding Benchmark) and `CMTEB` (Chinese Massive Text Embedding Benchmark), supporting tasks such as retrieval and reranking
    - Support for end-to-end RAG evaluation: Integration of the `ragas` framework, supporting automatic generation of evaluation datasets and evaluation based on judge models

5. Documentation Updates:
    - Added "Blog" section https://github.com/modelscope/evalscope/pull/126, https://github.com/modelscope/evalscope/pull/135
    - Added support for dataset page https://github.com/modelscope/evalscope/pull/121
    - Updated function usage instructions https://github.com/modelscope/evalscope/pull/125, https://github.com/modelscope/evalscope/pull/134, https://github.com/modelscope/evalscope/pull/138, https://github.com/modelscope/evalscope/pull/137, https://github.com/modelscope/evalscope/pull/127

6. Updated dependencies: `nltk>=3.9` and `rouge-score>=0.1.0` https://github.com/modelscope/evalscope/pull/145, https://github.com/modelscope/evalscope/pull/143

# 中文说明

1. 新增数据集支持：
    - 完善多模态评测功能，支持MMBench-Video，Video-MME，MVBench视频评测 https://github.com/modelscope/evalscope/pull/146
    - 新增cmb数据集 https://github.com/modelscope/evalscope/pull/117

2. 支持`LongBench-write` 长文本生成的质量评测  https://github.com/modelscope/evalscope/pull/136

3. 支持从`nltk`自动下载 `punkt_tab.zip`  https://github.com/modelscope/evalscope/pull/140
3. 支持RAG评测：https://github.com/modelscope/evalscope/pull/127
    - 支持embeddings/reranker 评测：集成`MTEB`（Massive Text Embedding Benchmark）和 `CMTEB`（Chinese Massive Text Embedding Benchmark），支持检索、重排等任务评估
    - 支持RAG端到端评测：集成`ragas`框架，支持自动生成评测数据集和基于裁判员模型的评测

4. 文档更新
    - 增加 “博客” 板块  https://github.com/modelscope/evalscope/pull/126, https://github.com/modelscope/evalscope/pull/135
    - 增加支持的数据集页面 https://github.com/modelscope/evalscope/pull/121
    - 更新功能使用说明 https://github.com/modelscope/evalscope/pull/125, https://github.com/modelscope/evalscope/pull/134, https://github.com/modelscope/evalscope/pull/138, https://github.com/modelscope/evalscope/pull/137, https://github.com/modelscope/evalscope/pull/127

5. 更新依赖`nltk>=3.9`和`rouge-score>=0.1.0` https://github.com/modelscope/evalscope/pull/145, https://github.com/modelscope/evalscope/pull/143

## v0.6.0 (2024-11-08)

## Release Notes

1. Support multi-modal RAG evaluation #149
    - Add CLIP_Benchmark
    - Add end-to-end multi-modal RAG evaluation in Ragas
2. To be compatible with Ragas v0.2.3 #165 #171
3. Support truncating input for CLIP models #163 #164
4. Support saving knowledge graphs when generating datasets in Ragas #175



### Bug Fixes

1. Fix issue of abnormal metrics during CMTEB evaluation #157
2. Fix issue of GenerationConfig being None #173
3. Update datasets version constraints #184
4. Add publish workflow #186


### Documentation Updates

1. Update VLMEvalKit documentation #166
2. Update multi-modal RAG blog #172



## 中文说明

###  特性

1. 添加多模态RAG评测支持 #149
    - 支持CLIP_Benchmark
    - 支持Ragas端到端多模态RAG评测
2. 兼容Ragas v0.2.3 #165 #171
3. 支持CLIP模型截断输入 #163 #164
4. 支持Ragas生成数据集时保存知识图谱 #175


### 缺陷修复

1. 修复CMTEB评估时指标异常的问题 #157
2. 修复GenerationConfig为None的异常 #173
3. 更新datasets版本限制  #184
4. 增加publish workflow #186


### 文档更新

1. 更新VLMEvalKit文档 #166
2. 更新多模态RAG博客 #172

## v0.6.1 (2024-11-22)

## Release Notes

1. Add CMMLU benchmark #198
2. Add publish workflow   #186
3. Adapt RAGAS v0.2.5 and update readme #205
4. Adapt MTEB v1.19   #196


### Bug Fixes

1. Set datasets version: dataset>=3.0.0, <=3.0.1  #184
2. Set pyarrow version to <=17.0.0 to avoid installation issue on OSX.   #187
3. Add timeout for download punkt.zip   #206


### Documentation Updates

1. Update OpenCompass list all datasets docs   #199
2. Update RAGAS v0.2.5 docs   #205



## 中文说明

###  特性

1. 支持CMMLU benchmark    #198
2. 支持publish 流程        #186
3. 适配RAGAS v0.2.5并更新文档    #205
4. 适配 MTEB v1.19      #196


### 缺陷修复

1. 设置datasets 版本，修复兼容性问题: dataset>=3.0.0, <=3.0.1  #184
2. 设置 pyarrow版本：<=17.0.0 修复在OSX操作系统下的安装问题     #187
3. 增加下载punkt.zip时的超时时间   #206


### 文档更新

1. 更新OpenCompass作为backend时所支持的数据集列表文档   #199
2. 更新RAGAS v0.2.5 文档   #205


## v0.7.0 (2024-11-28)

## Release Notes

1. Refactor the `perf` module, more robust and easier to use.  #178
2. Add speed benchmarking in the `perf` module.  #178
3. Add multi-modal benchmark `flickr8k` in the `perf` module for speed benchmark.  #211


### Bug Fixes

1. Add timeout for download punkt.zip   #206
2. Fix parallel for speed benchmarking in the `perf` module.  #215


### Documentation Updates

1. Update VLM-Eval doc   #209
2. Update `perf` module doc   #178  #211



## 中文说明

###  特性

1. 重构`perf`模块，更鲁棒、更易用。  #178
2. 在`perf`模块中添加速度基准测试。   #178
3. 在`perf`模块中添加多模态基准 `flickr8k` 以进行速度基准测试。  #211


### 缺陷修复

1. 修复下载`punkt.zip`的超时问题。  #206
2. 修复`perf`模块中的速度基准测试并行问题。  #215


### 文档更新

1. 更新VLM-Eval文档。  #209
2. 更新`perf`模块文档。  #178  #211


## v0.7.1 (2024-11-28)

## Release Notes

1. Add PMMEval benchmark   #222


## 中文说明

###  特性

1. 增加PMMEval评测集  #222



## v0.7.2 (2024-12-04)

# Release Note
1. Remove `pyarrow` version requirement #225
2. Optimize warning info #223


# 中文说明
1. 移除 `pyarrow` 版本要求  #225
2. 优化 warning 信息 #223

## v0.8.0 (2024-12-14)

## Release Notes

1. Optimize `Native` eval and remove template_type #231
2. The evalscope perf command supports the --outputs-dir configuration. #232
3. Support  ragas 0.2.7 #234



### Bug Fixes

1.  Fix longwriter docs #239
2. Fix lint for longwriter #240
3. Fix lint #237 
4. Unify perf output #238


### Documentation Updates

1.  Fix longwriter docs #239
2. Optimize `Native` eval and remove template_type #231



## 中文说明

###  特性

1. 取消`Native`模式评测中template_type参数   #231
2. perf模块支持--output-dir   #232 
3. 支持适配最新的ragas 0.2.7版本 #234 


### 缺陷修复

1. 修复longwriter代码示例，优化流程  #239 
2. 修复lint，以及longwriter的lint   #240  #237 


### 文档更新

1. 更新longwriter文档  #239 
2. 更新`Native`评测模式的相关文档  #231 


## v0.8.1 (2024-12-17)

## What's Changed
* Unify `opencompass` and `vlmeval` output dirs by @Yunnglin in https://github.com/modelscope/evalscope/pull/242
* Perf add more metrics by @Yunnglin in https://github.com/modelscope/evalscope/pull/245
* Perf add `trust remote` parameter by @Yunnglin in https://github.com/modelscope/evalscope/pull/246
* Compat ms-swift<3.0 by @Yunnglin in https://github.com/modelscope/evalscope/pull/249
* Fix humaneval for native eval by @Yunnglin in https://github.com/modelscope/evalscope/pull/248

## 中文版本
* 统一 `opencompass` 和 `vlmeval` 输出目录，作者：@Yunnglin，相关链接：https://github.com/modelscope/evalscope/pull/242
* 模型压测：增加更多指标，作者：@Yunnglin，相关链接：https://github.com/modelscope/evalscope/pull/245
* 模型压测：添加`trust remote`参数，作者：@Yunnglin，相关链接：https://github.com/modelscope/evalscope/pull/246
* 兼容 ms-swift<3.0，作者：@Yunnglin，相关链接：https://github.com/modelscope/evalscope/pull/249
* 修复本地评估的 humaneval 问题，作者：@Yunnglin，相关链接：https://github.com/modelscope/evalscope/pull/248

**Full Changelog**: https://github.com/modelscope/evalscope/compare/v0.8.0...v0.8.1

## v0.8.2 (2024-12-26)

## What's Changed
* add user group by @Yunnglin in https://github.com/modelscope/evalscope/pull/251
* fix perf seed by @Yunnglin in https://github.com/modelscope/evalscope/pull/254
* add spawn env by @Yunnglin in https://github.com/modelscope/evalscope/pull/256
* Fix: sglang API response does not contain 'object' field. by @tghfly in https://github.com/modelscope/evalscope/pull/260
* fix parse response by @Yunnglin in https://github.com/modelscope/evalscope/pull/262
* fix predict  by @Yunnglin in https://github.com/modelscope/evalscope/pull/264
* compat ragas 0.2.9 and remove chinese prompt cache by @Yunnglin in https://github.com/modelscope/evalscope/pull/265

## New Contributors
* @tghfly made their first contribution in https://github.com/modelscope/evalscope/pull/260

**Full Changelog**: https://github.com/modelscope/evalscope/compare/v0.8.1...v0.8.2

## v0.9.0 (2025-01-03)

## What's Changed
#253
- Support for specifying model service API URL for evaluation: Evaluation can be performed on both local and remote model services.
- Support for custom schema for mixed data evaluation: Combine different datasets for a more comprehensive assessment of model -capabilities with less data.
- Add benchmark contribution guidelines: Users can add their own benchmarks to make the tool more powerful and beneficial for more people.

## 中文
#253
- 支持指定模型服务API URL评测：不论是本地模型还是远端模型服务都可以评测
- 支持自定义schema进行数据混合评测：混合不同的数据集，用更少的数据，更全面的评估模型能力
- 添加benchmark贡献指南：可以自行添加benchmark，让工具变的更强大，让更多人受益


**Full Changelog**: https://github.com/modelscope/evalscope/compare/v0.8.2...v0.9.0

## v0.10.0 (2025-01-20)

## What's Changed
### Feat: Add EvalScope dashboard by @Yunnglin in https://github.com/modelscope/evalscope/pull/277
  - Including single-model evaluation results and multi-model comparison, refer to the [📖 Visualizing Evaluation Results](https://evalscope.readthedocs.io/en/latest/get_started/visualization.html) for more details
### Others
* Add `model-id` in arguments by @Yunnglin in https://github.com/modelscope/evalscope/pull/274
* Add `ifeval` and unify report format by @Yunnglin in https://github.com/modelscope/evalscope/pull/275
* Add `iquiz` and use first metric by default for multi metrics by @Yunnglin in https://github.com/modelscope/evalscope/pull/288
* Support specifying system prompt by @Yunnglin in https://github.com/modelscope/evalscope/pull/283
* Bug-fix multi-metrics dataset by @Yunnglin in https://github.com/modelscope/evalscope/pull/282
* Bug-fix mmlu read local data by @Yunnglin in https://github.com/modelscope/evalscope/pull/273

## 功能更新
### 主要更新
* 添加评测报告可视化，由 @Yunnglin 在 https://github.com/modelscope/evalscope/pull/277 中实现
  - 包括单模型评估结果和多模型对比，更多详情请参考 [📖 可视化评估结果](https://evalscope.readthedocs.io/zh-cn/latest/get_started/visualization.html)
### 其他
* 在参数中添加 `model-id`，由 @Yunnglin 在 https://github.com/modelscope/evalscope/pull/274 中实现
* 添加 `ifeval` 评测基准；并统一报告格式，由 @Yunnglin 在 https://github.com/modelscope/evalscope/pull/275 中实现
* 添加 `iquiz`评测基准；支持多指标的评测集在展示结果时默认使用第一个指标的结果，由 @Yunnglin 在 https://github.com/modelscope/evalscope/pull/288 中实现
* 支持指定system prompt，由 @Yunnglin 在 https://github.com/modelscope/evalscope/pull/283 中实现
* 修复多指标数据集的错误，由 @Yunnglin 在 https://github.com/modelscope/evalscope/pull/282 中实现
* 修复 mmlu 读取本地数据的问题，由 @Yunnglin 在 https://github.com/modelscope/evalscope/pull/273 中实现

**Full Changelog**: https://github.com/modelscope/evalscope/compare/v0.9.0...v0.10.0

## v0.10.1 (2025-01-23)

## What's Changed
* Add visualization examples, support interface language switching between Chinese and English by @Yunnglin in https://github.com/modelscope/evalscope/pull/289, https://github.com/modelscope/evalscope/pull/294
* Add GPQA benchmark by @Yunnglin in https://github.com/modelscope/evalscope/pull/293
* Fix ifeval dependency by @Yunnglin in https://github.com/modelscope/evalscope/pull/292
* Fix viz subset by @Yunnglin in https://github.com/modelscope/evalscope/pull/295

## 更新内容
* 添加可视化示例，支持界面中英文切换  @Yunnglin 在 https://github.com/modelscope/evalscope/pull/289, https://github.com/modelscope/evalscope/pull/294
* 添加 GPQA 评测基准  @Yunnglin 在 https://github.com/modelscope/evalscope/pull/293
* 修复 ifeval 依赖  @Yunnglin 在 https://github.com/modelscope/evalscope/pull/292
* 修复可视化模型预测结果的bug  @Yunnglin 在 https://github.com/modelscope/evalscope/pull/295

**Full Changelog**: https://github.com/modelscope/evalscope/compare/v0.10.0...v0.10.1

## v0.11.0 (2025-02-13)

## 新功能
1. 支持评测DeepSeek-R1类模型数学推理能力，详见[最佳实践](https://evalscope.readthedocs.io/zh-cn/latest/best_practice/deepseek_r1_distill.html)
2. 支持`eval_batch_size`参数，加速模型评测
3. 支持设置测试集的`prompt_template`, `system_prompt`, `metrics_list`参数

---

## New Feature
1. Support for DeepSeek-R1 type models' mathematical reasoning capabilities. For details, see [Best Practices](https://evalscope.readthedocs.io/zh-cn/latest/best_practice/deepseek_r1_distill.html).
2. Support for the `eval_batch_size` parameter to accelerate model evaluation.
3. Support for setting `prompt_template`, `system_prompt`, and `metrics_list` parameters for the test set.

## What's Changed
* set default stop to list by @Yunnglin in https://github.com/modelscope/evalscope/pull/296
* update datasets version by @wangxingjun778 in https://github.com/modelscope/evalscope/pull/297
* Add ds distill collection by @Yunnglin in https://github.com/modelscope/evalscope/pull/298
* update custom general mcq by @Yunnglin in https://github.com/modelscope/evalscope/pull/299
* fix viz html label and num of sample by @Yunnglin in https://github.com/modelscope/evalscope/pull/300
* support load collection from remote by @Yunnglin in https://github.com/modelscope/evalscope/pull/303
* update perf doc by @Yunnglin in https://github.com/modelscope/evalscope/pull/305
* support multi metrics and system prompt by @Yunnglin in https://github.com/modelscope/evalscope/pull/306


**Full Changelog**: https://github.com/modelscope/evalscope/compare/v0.10.1...v0.11.0

## v0.12.0 (2025-02-27)

## 新功能
- 新增支持评测推理模型的思考效率，参考[📖思考效率评测最佳实践](https://evalscope.readthedocs.io/zh-cn/latest/best_practice/think_eval.html)，该实现参考了[Overthinking](https://doi.org/10.48550/arXiv.2412.21187) 和 [Underthinking](https://doi.org/10.48550/arXiv.2501.18585)两篇工作。
- 新增支持[AIME25](https://www.modelscope.cn/datasets/TIGER-Lab/AIME25), [MuSR](https://modelscope.cn/datasets/AI-ModelScope/MuSR), [ProcessBench](https://www.modelscope.cn/datasets/Qwen/ProcessBench/summary)三个模型推理相关评测基准。
- 支持评测时使用stream模式、指定请求超时时间、支持mps设备本地评测。

## New Features
- Added support for evaluating the reasoning efficiency of models. Refer to [📖 Best Practices for Evaluating Thinking Efficiency](https://evalscope.readthedocs.io/zh-cn/latest/best_practice/think_eval.html). This implementation is inspired by the works [Overthinking](https://doi.org/10.48550/arXiv.2412.21187) and [Underthinking](https://doi.org/10.48550/arXiv.2501.18585).
- Added support for three model inference benchmarks: [AIME25](https://www.modelscope.cn/datasets/TIGER-Lab/AIME25), [MuSR](https://modelscope.cn/datasets/AI-ModelScope/MuSR), and [ProcessBench](https://www.modelscope.cn/datasets/Qwen/ProcessBench/summary).
- Supports using stream mode during evaluation, specifying request timeout, and local evaluation on mps devices.

## What's Changed
* update doc by @Yunnglin in https://github.com/modelscope/evalscope/pull/308
* Update/docs by @Yunnglin in https://github.com/modelscope/evalscope/pull/309
* Update doc and limit plotly version by @Yunnglin in https://github.com/modelscope/evalscope/pull/312
* add AIME 2025 by @Yunnglin in https://github.com/modelscope/evalscope/pull/313
* add perf top_k by @Yunnglin in https://github.com/modelscope/evalscope/pull/317
* fix TPOP, report name comflict, query template by @Yunnglin in https://github.com/modelscope/evalscope/pull/321
* fix #323 by @Yunnglin in https://github.com/modelscope/evalscope/pull/325
* compat device by @Yunnglin in https://github.com/modelscope/evalscope/pull/329
* use openai package by @Yunnglin in https://github.com/modelscope/evalscope/pull/326
* Fix warning perf usage by @Yunnglin in https://github.com/modelscope/evalscope/pull/331
* Add benchmark: `musr` and `process bench`  by @Yunnglin in https://github.com/modelscope/evalscope/pull/324
* add max token for connection by @Yunnglin in https://github.com/modelscope/evalscope/pull/335
* fix stream by @Yunnglin in https://github.com/modelscope/evalscope/pull/337
* Add think eval by @Yunnglin in https://github.com/modelscope/evalscope/pull/316
* Fix device map by @Yunnglin in https://github.com/modelscope/evalscope/pull/342


**Full Changelog**: https://github.com/modelscope/evalscope/compare/v0.11.0...v0.12.0

## v0.12.1 (2025-03-10)

## 新功能
1. 新增最佳实践 [评测QwQ-32B和DeepSeek-R1模型](https://evalscope.readthedocs.io/zh-cn/latest/best_practice/eval_qwq.html) 包括模型推理能力测试和思考效率测试。
2. 新增支持SuperGPQA评测基准，指定`super_gpqa`来使用。
3. 多选题评测集支持指定`generation` 或 `logits`模式。
4. 支持模型输出结果后处理过滤器，目前支持：
    - `remove_until {string}` 过滤掉模型输出结果中指定字符串之前的部分。 
    - `extract {regex}` 提取模型输出结果中指定正则表达式匹配的部分。
5. 支持模型服务中的`reasoning_content`字段

## New Features
1. The multiple-choice question assessment set now supports specifying `generation` or `logits` mode.
2. Support for post-processing filters on model output results, currently including:
   - `remove_until {string}`: Filters out the part of the model output before the specified string.
   - `extract {regex}`: Extracts the portion of the model output that matches the specified regular expression.
3. Support for the `reasoning_content` field in the model service.
4. New support for the SuperGPQA evaluation benchmark.
5. Added best practices for [Evaluating QwQ Models](https://evalscope.readthedocs.io/en/latest/best_practice/eval_qwq.html), including tests for model reasoning capabilities and thinking efficiency.

## What's Changed
* update doc by @Yunnglin in https://github.com/modelscope/evalscope/pull/343
* fix stream finish reason by @Yunnglin in https://github.com/modelscope/evalscope/pull/347
* Update eval think by @Yunnglin in https://github.com/modelscope/evalscope/pull/348
* update IQ/EQ doc by @Yunnglin in https://github.com/modelscope/evalscope/pull/354
* support `generation` and `logits` output for benchmarks by @Yunnglin in https://github.com/modelscope/evalscope/pull/358
* fix/set_use_cache_remove_reviews_dir_bug by @x22x22 in https://github.com/modelscope/evalscope/pull/359
* add super gpqa by @Yunnglin in https://github.com/modelscope/evalscope/pull/361
* Update download datasts doc by @Yunnglin in https://github.com/modelscope/evalscope/pull/363
* Compat reasoning model and support filter by @Yunnglin in https://github.com/modelscope/evalscope/pull/370
* fix typo in README_zh by @yabea in https://github.com/modelscope/evalscope/pull/372
* Update arguments.py by @xuhanxiao0624 in https://github.com/modelscope/evalscope/pull/364
* add qwq eval doc by @Yunnglin in https://github.com/modelscope/evalscope/pull/376
* fix model path and encoding error by @Yunnglin in https://github.com/modelscope/evalscope/pull/380
* fix tool bench by @Yunnglin in https://github.com/modelscope/evalscope/pull/379

## New Contributors
* @x22x22 made their first contribution in https://github.com/modelscope/evalscope/pull/359
* @yabea made their first contribution in https://github.com/modelscope/evalscope/pull/372
* @xuhanxiao0624 made their first contribution in https://github.com/modelscope/evalscope/pull/364

**Full Changelog**: https://github.com/modelscope/evalscope/compare/v0.12.0...v0.12.1

## v0.13.0 (2025-03-14)

## 新功能
- 支持LLM-as-a-Judge进行评测，使用大模型来进行打分，参考[相关参数](https://evalscope.readthedocs.io/zh-cn/latest/get_started/parameters.html#judge)
- 新增支持 SimpleQA, Chinese SimpleQA, LiveCodeBench 三个评测基准，前两个需要指定judge 模型来评测，参考[使用示例](https://evalscope.readthedocs.io/zh-cn/latest/get_started/basic_usage.html#id9)

## New Features
- Support for LLM-as-a-Judge evaluation, using large language models for scoring. Refer to [relevant parameters](https://evalscope.readthedocs.io/en/latest/get_started/parameters.html#judge)
- Added support for three new evaluation benchmarks: SimpleQA, Chinese SimpleQA, and LiveCodeBench. The first two require specifying a judge model for evaluation. See [usage examples](https://evalscope.readthedocs.io/en/latest/get_started/basic_usage.html#id9)

## What's Changed
* Add judge model, support simple qa and chinese simple qa by @Yunnglin in https://github.com/modelscope/evalscope/pull/383
* suppor general judge by @Yunnglin in https://github.com/modelscope/evalscope/pull/385
* Add livecodebench by @Yunnglin in https://github.com/modelscope/evalscope/pull/386


**Full Changelog**: https://github.com/modelscope/evalscope/compare/v0.12.1...v0.13.0

## v0.13.1 (2025-03-24)

## 新功能
- 模型推理服务压测支持random生成指定范围长度的prompt，参考[使用指南](https://evalscope.readthedocs.io/zh-cn/latest/user_guides/stress_test/examples.html#random)
- 兼容ms-swift训练框架训练中评测，[参考](https://swift.readthedocs.io/zh-cn/latest/Instruction/%E8%AF%84%E6%B5%8B.html#id5)
- 修复框架稳定性相关bug

## New Features
- The model inference service stress testing now supports generating prompts of specified length using random values. Refer to the [user guide](https://evalscope.readthedocs.io/zh-cn/latest/user_guides/stress_test/examples.html#random) for more details.
- Compatible with evaluation during training using the ms-swift training framework. [Reference](https://swift.readthedocs.io/en/latest/Instruction/Evaluation.html#evaluation-during-training)
- Fixed bugs related to framework stability.

## What's Changed
* compat swift by @Yunnglin in https://github.com/modelscope/evalscope/pull/397
* Update perf random dataset by @Yunnglin in https://github.com/modelscope/evalscope/pull/399
* fix dump config by @Yunnglin in https://github.com/modelscope/evalscope/pull/401
* Filter illegal characters & Use asyncio.new_event_loop() instead of deprecated get_event_loop() by @Mengxi12345 in https://github.com/modelscope/evalscope/pull/411
* reduce save items and update doc by @Yunnglin in https://github.com/modelscope/evalscope/pull/406
* Fix loop eval by @Yunnglin in https://github.com/modelscope/evalscope/pull/415
* add perf no test connection by @Yunnglin in https://github.com/modelscope/evalscope/pull/417
* update doc by @Yunnglin in https://github.com/modelscope/evalscope/pull/422

## New Contributors
* @Mengxi12345 made their first contribution in https://github.com/modelscope/evalscope/pull/411

**Full Changelog**: https://github.com/modelscope/evalscope/compare/v0.13.0...v0.13.1

## v0.13.2 (2025-04-01)

## 更新
- 新增支持MMLU_Redux, AlpacaEval 和 ArenaHard 三个评测基准，使用注意事项请查看[文档](https://evalscope.readthedocs.io/zh-cn/latest/get_started/supported_dataset.html)
- `general_qa` 支持设置system字段
- `evalscope perf`对齐vLLM官方benchmarking，支持`extra_args`
- 移除多余的依赖项
- 修复RAGEval报错的问题

## Update
- Supported three evaluation benchmarks: MMLU_Redux, AlpacaEval, and ArenaHard. Please refer to the [documentation](https://evalscope.readthedocs.io/zh-cn/latest/get_started/supported_dataset.html) for usage instructions.
- `general_qa` now supports setting the system field.
- `evalscope perf` is aligned with the vLLM official benchmarking and supports `extra_args`.
- Removed unnecessary dependencies.
- Fixed the issue causing errors with RAGEval.

## What's Changed
* fix rageval local model by @Yunnglin in https://github.com/modelscope/evalscope/pull/429
* update vlmeval doc by @Yunnglin in https://github.com/modelscope/evalscope/pull/430
* Fix general qa by @Yunnglin in https://github.com/modelscope/evalscope/pull/433
* fix perf stream args by @Yunnglin in https://github.com/modelscope/evalscope/pull/434
* add perf extra args by @Yunnglin in https://github.com/modelscope/evalscope/pull/438
* support genera qa system by @Yunnglin in https://github.com/modelscope/evalscope/pull/439
* fix chat_adapter by @Yunnglin in https://github.com/modelscope/evalscope/pull/440
* support mmlu_redux benchmark by @Yunnglin in https://github.com/modelscope/evalscope/pull/428
* Fix perf request by @Yunnglin in https://github.com/modelscope/evalscope/pull/445
* Update requirements by @Yunnglin in https://github.com/modelscope/evalscope/pull/446
* Add AlpacaEval and ArenaHard by @Yunnglin in https://github.com/modelscope/evalscope/pull/437


**Full Changelog**: https://github.com/modelscope/evalscope/compare/v0.13.1...v0.13.2

## v0.14.0 (2025-04-10)

## 新功能
* 支持SwanLab 对模型压测结果的可视化
* 模型压测支持`/v1/completions`端点
* 支持embedding API服务性能评测
* 兼容langchain 0.3版本
* 增加对航运测评集Maritime Bench的支持
* 修复多选题解析的bad case

## New Features
* Support for SwanLab visualization of model stress test results
* Model stress testing now supports the `/v1/completions` endpoint
* Support for embedding API service performance evaluation
* Compatibility with langchain version 0.3
* Added support for the Maritime Bench evaluation set
* Fixed bad cases in multiple-choice question parsing

## What's Changed
* fix splitext by @Yunnglin in https://github.com/modelscope/evalscope/pull/447
* fix report by @Yunnglin in https://github.com/modelscope/evalscope/pull/454
* add SwanLab Support 添加SwanLab可视化支持 by @ShaohonChen in https://github.com/modelscope/evalscope/pull/453
* update autotokenizer by @Yunnglin in https://github.com/modelscope/evalscope/pull/456
* 增加对航运测评集Maritime Bench的支持 by @K-zhy in https://github.com/modelscope/evalscope/pull/455
* fix mmlu parser by @Yunnglin in https://github.com/modelscope/evalscope/pull/460
* update contribute doc by @Yunnglin in https://github.com/modelscope/evalscope/pull/458
* feat: swanlab config add `evalscope` and upgrade document by @Zeyi-Lin in https://github.com/modelscope/evalscope/pull/464
* Compat langchain v0.3 and embedding API by @Yunnglin in https://github.com/modelscope/evalscope/pull/463
* fix option parser by @Yunnglin in https://github.com/modelscope/evalscope/pull/466
* support perf completion by @Yunnglin in https://github.com/modelscope/evalscope/pull/467
* update livecodebench by @Yunnglin in https://github.com/modelscope/evalscope/pull/468

## New Contributors
* @ShaohonChen made their first contribution in https://github.com/modelscope/evalscope/pull/453
* @K-zhy made their first contribution in https://github.com/modelscope/evalscope/pull/455
* @Zeyi-Lin made their first contribution in https://github.com/modelscope/evalscope/pull/464

**Full Changelog**: https://github.com/modelscope/evalscope/compare/v0.13.2...v0.14.0

## v0.15.0 (2025-04-29)

## 新功能

* 支持文生图评测：支持MPS、HPSv2.1Score等8个指标，支持EvalMuse、GenAI-Bench等评测基准，参考[使用文档](https://evalscope.readthedocs.io/zh-cn/latest/user_guides/aigc/t2i.html)
* 新增Qwen3评测最佳实践，[欢迎阅读📖](https://evalscope.readthedocs.io/zh-cn/latest/best_practice/qwen3.html)
* 新增常见问题文档，[参考](https://evalscope.readthedocs.io/zh-cn/latest/get_started/faq.html)

## New Features

* Support for text-to-image evaluation: Includes 8 metrics such as MPS, HPSv2.1Score, and supports evaluation benchmarks like EvalMuse and GenAI-Bench. Refer to the [user documentation](https://evalscope.readthedocs.io/en/latest/user_guides/aigc/t2i.html).
* Added Qwen3 Evaluation Best Practices, [welcome to read 📖](https://evalscope.readthedocs.io/en/latest/best_practice/qwen3.html).
* Added FAQ document, [refer here](https://evalscope.readthedocs.io/en/latest/get_started/faq.html).

## What's Changed
* add livecodebench debug by @Yunnglin in https://github.com/modelscope/evalscope/pull/469
* fix app cli args by @Yunnglin in https://github.com/modelscope/evalscope/pull/480
* add preprocess for content by @Yunnglin in https://github.com/modelscope/evalscope/pull/485
* change mcq output type by @Yunnglin in https://github.com/modelscope/evalscope/pull/496
* add qa doc by @mushenL in https://github.com/modelscope/evalscope/pull/500
* Fix perf metrics by @Yunnglin in https://github.com/modelscope/evalscope/pull/506
* Add t2v metrics by @Yunnglin in https://github.com/modelscope/evalscope/pull/488
* add Qwen3 best practice by @Yunnglin in https://github.com/modelscope/evalscope/pull/516
* update docs by @wangxingjun778 in https://github.com/modelscope/evalscope/pull/517
* Update docs by @Yunnglin in https://github.com/modelscope/evalscope/pull/519

## New Contributors
* @mushenL made their first contribution in https://github.com/modelscope/evalscope/pull/500

**Full Changelog**: https://github.com/modelscope/evalscope/compare/v0.14.0...v0.15.0

## v0.15.1 (2025-04-30)


## What's Changed
* Fix Qwen3 best practice   #530 
* Fix doc and add enable_think args, fix requirement   #522
* Fix: improve multi-choice result handling in evaluator #523
* Add perf return resul  #528 


**Full Changelog**: https://github.com/modelscope/evalscope/compare/v0.15.0...v0.15.1

## v0.16.0 (2025-05-19)

## 新功能
-  支持模型服务性能压测支持设置多种并发，并输出美观的性能压测报告，[参考示例](https://evalscope.readthedocs.io/zh-cn/latest/user_guides/stress_test/quick_start.html#id3)。
-  支持[ToolBench-Static](https://modelscope.cn/datasets/AI-ModelScope/ToolBench-Static)数据集，评测模型的工具调用能力，参考[使用文档](https://evalscope.readthedocs.io/zh-cn/latest/third_party/toolbench.html)
-  支持[DROP](https://modelscope.cn/datasets/AI-ModelScope/DROP/dataPeview)和[Winogrande](https://modelscope.cn/datasets/AI-ModelScope/winogrande_val)评测基准，评测模型的推理能力。
- 支持`use_cache`重用评测结果

## New Features
- Supports performance stress testing of model services with various concurrency settings and outputs aesthetically pleasing performance reports. [See example](https://evalscope.readthedocs.io/zh-cn/latest/user_guides/stress_test/quick_start.html#id3).
- Supports the [ToolBench-Static](https://modelscope.cn/datasets/AI-ModelScope/ToolBench-Static) dataset to evaluate the tool invocation capabilities of models. Refer to the [user guide](https://evalscope.readthedocs.io/zh-cn/latest/third_party/toolbench.html).
- Supports [DROP](https://modelscope.cn/datasets/AI-ModelScope/DROP/dataPeview) and [Winogrande](https://modelscope.cn/datasets/AI-ModelScope/winogrande_val) evaluation benchmarks to assess the reasoning capabilities of models.
- Supports `use_cache` to reuse evaluation results.

## What's Changed
* fix preprocess args by @Yunnglin in https://github.com/modelscope/evalscope/pull/537
* fix report generation encoding to support chinese on windows by @antigone660 in https://github.com/modelscope/evalscope/pull/534
* fix config extension check by @Yunnglin in https://github.com/modelscope/evalscope/pull/544
* handle error during evaluation by @Yunnglin in https://github.com/modelscope/evalscope/pull/541
* Bug Fix: Allow Custom SwanLab Project Name by @ShaohonChen in https://github.com/modelscope/evalscope/pull/549
* support args json format by @Yunnglin in https://github.com/modelscope/evalscope/pull/551
* Add drop and winogrande by @Yunnglin in https://github.com/modelscope/evalscope/pull/546
* fix issue docs by @xiaoping378 in https://github.com/modelscope/evalscope/pull/562
* 新增judge模型的缓存利用 by @xh3204 in https://github.com/modelscope/evalscope/pull/566
* Support Perf multi parallel and rich output by @Yunnglin in https://github.com/modelscope/evalscope/pull/564
* Update review cache logic and doc by @Yunnglin in https://github.com/modelscope/evalscope/pull/574
* Refactor ToolBench eval by @Yunnglin in https://github.com/modelscope/evalscope/pull/556

## New Contributors
* @antigone660 made their first contribution in https://github.com/modelscope/evalscope/pull/534
* @xiaoping378 made their first contribution in https://github.com/modelscope/evalscope/pull/562
* @xh3204 made their first contribution in https://github.com/modelscope/evalscope/pull/566

**Full Changelog**: https://github.com/modelscope/evalscope/compare/v0.15.1...v0.16.0

## v0.16.1 (2025-06-03)

## 新功能
- 支持传递`--analysis-report`布尔参数，使用judge model生成分析报告，报告中包含模型评测结果的分析解读和建议。
- 新增支持大海捞针测试（Needle-in-a-Haystack），指定`needle_haystack`即可进行测试，并在`outputs/reports`文件夹下生成对应的heatmap，直观展现模型性能，使用[参考](https://evalscope.readthedocs.io/zh-cn/latest/third_party/needle_haystack.html)。
- 新增支持[DocMath](https://modelscope.cn/datasets/yale-nlp/DocMath-Eval/summary)和[FRAMES](https://modelscope.cn/datasets/iic/frames/summary)两个长文档评测基准，使用注意事项请查看[文档](https://evalscope.readthedocs.io/zh-cn/latest/get_started/supported_dataset.html)
- `--limit`支持设置0-1的浮点数，表示评测数据集的百分比数量。

## New Features
- Supports passing the `--analysis-report` boolean parameter, which uses the judge model to generate an analysis report. The report includes interpretative analysis and recommendations based on the model evaluation results.
- Added support for the Needle-in-a-Haystack test. Specify `needle_haystack` to conduct the test, and a corresponding heatmap will be generated in the `outputs/reports` folder, visually displaying the model's performance. For usage, refer to [this guide](https://evalscope.readthedocs.io/zh-cn/latest/third_party/needle_haystack.html).
- Added support for two long document evaluation benchmarks: [DocMath](https://modelscope.cn/datasets/yale-nlp/DocMath-Eval/summary) and [FRAMES](https://modelscope.cn/datasets/iic/frames/summary). Please check the [documentation](https://evalscope.readthedocs.io/zh-cn/latest/get_started/supported_dataset.html) for usage considerations.
- The `--limit` parameter now supports setting a float between 0 and 1, representing the percentage of the dataset to be evaluated.

## What's Changed
* [DOC] Update perf doc by @Yunnglin in https://github.com/modelscope/evalscope/pull/576
* Fix reranker model args by @Yunnglin in https://github.com/modelscope/evalscope/pull/580
* fix perf tpop by @Yunnglin in https://github.com/modelscope/evalscope/pull/587
* Refactor app & add report analysis by @Yunnglin in https://github.com/modelscope/evalscope/pull/591
* fix toolbench message by @Yunnglin in https://github.com/modelscope/evalscope/pull/592
* Support swanlab workspace env by @xcode03 in https://github.com/modelscope/evalscope/pull/600
* fix tool bench rouge error by @Yunnglin in https://github.com/modelscope/evalscope/pull/604
* Compat mteb v1.38 by @Yunnglin in https://github.com/modelscope/evalscope/pull/608
* add Frames and other long doc benchmarks by @Yunnglin in https://github.com/modelscope/evalscope/pull/609
* Add float limit (percentage) by @Yunnglin in https://github.com/modelscope/evalscope/pull/617

## New Contributors
* @xcode03 made their first contribution in https://github.com/modelscope/evalscope/pull/600

**Full Changelog**: https://github.com/modelscope/evalscope/compare/v0.16.0...v0.16.1

## v0.16.3 (2025-06-23)

# 新功能
- 新增支持BFCL-v3评测基准，用于评测模型在多种场景下的函数调用能力，使用[参考](https://evalscope.readthedocs.io/zh-cn/latest/third_party/bfcl_v3.html)。
- 更新文档：[支持的数据集](https://evalscope.readthedocs.io/zh-cn/latest/get_started/supported_dataset/index.html)、[自定义模型评测](https://evalscope.readthedocs.io/zh-cn/latest/advanced_guides/custom_model.html#)、[添加评测基准](https://evalscope.readthedocs.io/zh-cn/latest/advanced_guides/add_benchmark.html)。

# New Features
- Introduced support for the BFCL-v3 evaluation benchmark, designed to assess the model's function-calling capabilities across diverse scenarios. For more details, refer to the [documentation](https://evalscope.readthedocs.io/en/latest/third_party/bfcl_v3.html).
- Documentation updates include: [Supported Datasets](https://evalscope.readthedocs.io/en/latest/get_started/supported_dataset/index.html), [Custom Model Evaluation](https://evalscope.readthedocs.io/en/latest/advanced_guides/custom_model.html#), and [Adding Evaluation Benchmarks](https://evalscope.readthedocs.io/en/latest/advanced_guides/add_benchmark.html).

## What's Changed
* add needle show score params by @Yunnglin in https://github.com/modelscope/evalscope/pull/620
* fix clip request by @Yunnglin in https://github.com/modelscope/evalscope/pull/621
* fix logit register by @Yunnglin in https://github.com/modelscope/evalscope/pull/624
* Fix eval errors by @Yunnglin in https://github.com/modelscope/evalscope/pull/627
* [Fix] cross encoder args by @Yunnglin in https://github.com/modelscope/evalscope/pull/628
* [Doc]Add t2i best practice by @Yunnglin in https://github.com/modelscope/evalscope/pull/631
* Fix in benchmark, when the number of dataset index is less than parallel , the parallel will be insufficient. by @xcode03 in https://github.com/modelscope/evalscope/pull/634
* fix super gpqa error by @Yunnglin in https://github.com/modelscope/evalscope/pull/639
* add repetition penalty by @Yunnglin in https://github.com/modelscope/evalscope/pull/640
* [Feature] add overall metrics log by @Yunnglin in https://github.com/modelscope/evalscope/pull/653
* [Doc] Update benchmark documents by @Yunnglin in https://github.com/modelscope/evalscope/pull/650
* [Doc] Update the default value of max_tokens for model API errors by @Su-yj in https://github.com/modelscope/evalscope/pull/659
* make sure the stream parameter is included in the request_json by @Su-yj in https://github.com/modelscope/evalscope/pull/663
* [Benchmark] Add BFCL-v3 by @Yunnglin in https://github.com/modelscope/evalscope/pull/657
* [Refector] t2i metrics init by @Yunnglin in https://github.com/modelscope/evalscope/pull/660
* [Doc] Support general mcq jsonl, update new benchmark, model doc by @Yunnglin in https://github.com/modelscope/evalscope/pull/667

## New Contributors
* @Su-yj made their first contribution in https://github.com/modelscope/evalscope/pull/659

**Full Changelog**: https://github.com/modelscope/evalscope/compare/v0.16.1...v0.16.2

## v0.17.0 (2025-07-04)

## 新功能
- 重构了竞技场模式，支持自定义模型对战，输出模型排行榜，以及对战结果可视化，使用[参考](https://evalscope.readthedocs.io/zh-cn/latest/user_guides/arena.html)。
- 优化自定义数据集评测，支持无参考答案评测；优化LLM裁判使用，预置“无参考答案直接打分” 和 “判断答案是否与参考答案一致”两种模式，使用[参考](https://evalscope.readthedocs.io/zh-cn/latest/advanced_guides/custom_dataset/llm.html#qa)
- 重构结果可视化，支持两个模型评测结果对比、支持竞技场模式结果可视化，[参考](https://evalscope.readthedocs.io/zh-cn/latest/get_started/visualization.html)

## New Features
- Refactored Arena Mode: now supports custom model battles, outputs a model leaderboard, and provides battle result visualization. See [reference](https://evalscope.readthedocs.io/en/latest/user_guides/arena.html) for more details.
- Optimized custom dataset evaluation: now supports evaluation without reference answers. Enhanced LLM judge functionality with built-in modes for “direct scoring without reference answers” and “consistency check between answers and reference answers.” See [reference](https://evalscope.readthedocs.io/en/latest/advanced_guides/custom_dataset/llm.html#qa) for more details.
- Refactored result visualization: now supports comparison of evaluation results between two models, as well as visualization of Arena mode results. [See reference](https://evalscope.readthedocs.io/en/latest/get_started/visualization.html)

## What's Changed
* [Feature] Add CI test workflow by @Yunnglin in https://github.com/modelscope/evalscope/pull/671
* [Bug] fix load local data by @Yunnglin in https://github.com/modelscope/evalscope/pull/673
* [Refector] visualization by @Yunnglin in https://github.com/modelscope/evalscope/pull/661
* [BUG] fix perf zero error by @Yunnglin in https://github.com/modelscope/evalscope/pull/690
* [Refactor] Refact arena mode by @Yunnglin in https://github.com/modelscope/evalscope/pull/677


**Full Changelog**: https://github.com/modelscope/evalscope/compare/v0.16.3...v0.17.0

## v0.17.1 (2025-07-21)

## 新功能
- 模型压测支持随机生成图文数据，用于多模态模型压测，使用方法[参考](https://evalscope.readthedocs.io/zh-cn/latest/user_guides/stress_test/examples.html#id4)。
- 支持[τ-bench](https://github.com/sierra-research/tau-bench)，用于评估 AI Agent在动态用户和工具交互的实际环境中的性能和可靠性，使用方法[参考](https://evalscope.readthedocs.io/zh-cn/latest/get_started/supported_dataset/llm.html#bench)。
- 支持“人类最后的考试”([Humanity's-Last-Exam](https://modelscope.cn/datasets/cais/hle))，这一高难度评测基准，使用方法[参考](https://evalscope.readthedocs.io/zh-cn/latest/get_started/supported_dataset/llm.html#humanity-s-last-exam)。

## New Features

- The model stress testing now supports randomly generated image-text data for multimodal model stress testing. For usage instructions, see [here](https://evalscope.readthedocs.io/zh-cn/latest/user_guides/stress_test/examples.html#id4).
- Support for [τ-bench](https://github.com/sierra-research/tau-bench) has been added, enabling the evaluation of AI Agent performance and reliability in real-world scenarios involving dynamic user and tool interactions. For usage instructions, see [here](https://evalscope.readthedocs.io/zh-cn/latest/get_started/supported_dataset/llm.html#bench).
- Support for "[Humanity's Last Exam](https://modelscope.cn/datasets/cais/hle)", a high-difficulty evaluation benchmark, has been added. For usage instructions, see [here](https://evalscope.readthedocs.io/zh-cn/latest/get_started/supported_dataset/llm.html#humanity-s-last-exam).

## What's Changed
* [Feat] add perf sleep interval by @Yunnglin in https://github.com/modelscope/evalscope/pull/699
* [Benchmark] Add HLE by @Yunnglin in https://github.com/modelscope/evalscope/pull/705
* [Benchmark] Add tau-bench by @Yunnglin in https://github.com/modelscope/evalscope/pull/711
* [Feature] Update perf random generation by @Yunnglin in https://github.com/modelscope/evalscope/pull/713
* [Fix] Eval parser: humaneval, mmlu by @Yunnglin in https://github.com/modelscope/evalscope/pull/718


**Full Changelog**: https://github.com/modelscope/evalscope/compare/v0.17.0...v0.17.1

## v1.0.0 (2025-08-25)

## 新版本
版本 1.0 对评测框架进行了重大重构，在 `evalscope/api` 下建立了全新的、更模块化且易扩展的 API 层。主要改进包括：为基准、样本和结果引入了标准化数据模型；对基准和指标等组件采用注册表式设计；并重写了核心评测器以协同新架构。现有的基准已迁移到这一 API，实现更加简洁、一致且易于维护。

不兼容的更新请[参考](https://evalscope.readthedocs.io/zh-cn/latest/get_started/basic_usage.html#v1-0)。

## New version
Version 1.0 introduces a major overhaul of the evaluation framework, establishing a new, more modular and extensible API layer under `evalscope/api`. Key improvements include standardized data models for benchmarks, samples, and results; a registry-based design for components such as benchmarks and metrics; and a rewritten core evaluator that orchestrates the new architecture. Existing benchmark adapters have been migrated to this API, resulting in cleaner, more consistent, and easier-to-maintain implementations.

## What's Changed
* [Feature] Add image edit evaluation by @Yunnglin in https://github.com/modelscope/evalscope/pull/725
* [Doc] add tau-bench doc by @Yunnglin in https://github.com/modelscope/evalscope/pull/730
* [Fix] ragas local model by @Yunnglin in https://github.com/modelscope/evalscope/pull/732
* [Doc] Add qwen-code best practice doc by @Yunnglin in https://github.com/modelscope/evalscope/pull/734
* Fix: Incorrect keyword argument in call to csv_to_list() by @Zhuzhenghao in https://github.com/modelscope/evalscope/pull/745
* Add SECURITY.md by @wangxingjun778 in https://github.com/modelscope/evalscope/pull/750
* Update SECURITY.md by @wangxingjun778 in https://github.com/modelscope/evalscope/pull/752
* updata faq file by @mushenL in https://github.com/modelscope/evalscope/pull/744
* [Refactor] v1.0 by @Yunnglin in https://github.com/modelscope/evalscope/pull/739

## New Contributors
* @Zhuzhenghao made their first contribution in https://github.com/modelscope/evalscope/pull/745

**Full Changelog**: https://github.com/modelscope/evalscope/compare/v0.17.1...v1.0.0

## v1.0.1 (2025-09-05)


## 更新内容
- 支持视觉-语言多模态大模型的评测任务，例如：MathVista、MMMU，更多支持数据集请[参考](https://evalscope.readthedocs.io/zh-cn/latest/get_started/supported_dataset/vlm.html)。
- 支持图像编辑任务评测，支持[GEdit-Bench](https://modelscope.cn/datasets/stepfun-ai/GEdit-Bench) 评测基准，使用方法[参考](https://evalscope.readthedocs.io/zh-cn/latest/user_guides/aigc/image_edit.html)。
- 核心依赖移除`torch`，移动到`rag`和`aigc`可选依赖中。

## Update
- The evaluation tasks for vision-language multimodal large models are now supported, including MathVista and MMMU. For more information on the supported datasets, please refer to [this link](https://evalscope.readthedocs.io/zh-cn/latest/get_started/supported_dataset/vlm.html).
- Image editing task evaluation is now supported, with the GEdit-Bench evaluation benchmark available. For usage instructions, please refer to [this guide](https://evalscope.readthedocs.io/zh-cn/latest/user_guides/aigc/image_edit.html).
- The core dependency on `torch` has been removed and is now an optional dependency under `rag` and `aigc`.

## What's Changed
* [DOC] Update 1.0 custom doc by @Yunnglin in https://github.com/modelscope/evalscope/pull/793
* [Fix] Fix reasoning content by @Yunnglin in https://github.com/modelscope/evalscope/pull/797
* [Fix] Change old collection to new version by @Yunnglin in https://github.com/modelscope/evalscope/pull/798
* Reduce dataset loading time by @mmdbhs in https://github.com/modelscope/evalscope/pull/805
* [Fix] fix reranker pad token and embedding max tokens by @Yunnglin in https://github.com/modelscope/evalscope/pull/806
* [Feature] Add image edit task by @Yunnglin in https://github.com/modelscope/evalscope/pull/804
* [Benchmark] Add mmmu by @Yunnglin in https://github.com/modelscope/evalscope/pull/812
* add math_vista by @mushenL in https://github.com/modelscope/evalscope/pull/813
* [Fix] tau-bench zero scores by @Yunnglin in https://github.com/modelscope/evalscope/pull/814
* [Fix] collection eval by @Yunnglin in https://github.com/modelscope/evalscope/pull/816
* [Feature] add vlm adapter by @Yunnglin in https://github.com/modelscope/evalscope/pull/817
* [Feature] remove torch from framework by @Yunnglin in https://github.com/modelscope/evalscope/pull/818
* add MMMU_Pro by @mushenL in https://github.com/modelscope/evalscope/pull/819

## New Contributors
* @mmdbhs made their first contribution in https://github.com/modelscope/evalscope/pull/805

**Full Changelog**: https://github.com/modelscope/evalscope/compare/v1.0.0...v1.0.1

## v1.0.2 (2025-09-23)


## 新增功能
- 代码评测基准(HumanEval, LiveCodeBench)支持在沙箱环境中运行，要使用该功能需先安装[ms-enclave](https://github.com/modelscope/ms-enclave)。
- 新增支持RealWorldQA、AI2D、MMStar、MMBench、OmniBench等图文多模态评测基准，和Multi-IF、HealthBench、AMC等纯文本评测基准。

## New Features
- Code evaluation benchmarks (HumanEval, LiveCodeBench) now support execution in a sandbox environment. To utilize this feature, you must first install [ms-enclave](https://github.com/modelscope/ms-enclave).
- Added support for various image-text multimodal evaluation benchmarks such as RealWorldQA, AI2D, MMStar, MMBench, OmniBench, as well as pure text evaluation benchmarks like Multi-IF, HealthBench, and AMC.

## What's Changed
* [Benchmark] add Multi-IF by @Yunnglin in https://github.com/modelscope/evalscope/pull/822
* Add ai2d_adapter and real_world_qa_adapter by @mushenL in https://github.com/modelscope/evalscope/pull/824
* [Benchmark] Add health bench by @Yunnglin in https://github.com/modelscope/evalscope/pull/826
* fix: make _temp_run top-level to resolve M1 pickle error by @MemoryIt in https://github.com/modelscope/evalscope/pull/827
* [Fix] vlm tokenize by @Yunnglin in https://github.com/modelscope/evalscope/pull/829
* [Doc] update qwen next doc by @Yunnglin in https://github.com/modelscope/evalscope/pull/832
* [Fix] fix bfcl-v3 score by @Yunnglin in https://github.com/modelscope/evalscope/pull/833
* [Benchmark] Add MMBench and MMStar by @mushenL in https://github.com/modelscope/evalscope/pull/834
* [Benchmark] Add Omnibench by @Yunnglin in https://github.com/modelscope/evalscope/pull/837
* [Fix] Fix bfcl validation error by @Yunnglin in https://github.com/modelscope/evalscope/pull/838
* [Feature] add docker sandbox by @Yunnglin in https://github.com/modelscope/evalscope/pull/835
* [Fix] Fix thread pool error by @Yunnglin in https://github.com/modelscope/evalscope/pull/841
* [Benchmark] Add amc23 and OlympiadBench by @mushenL in https://github.com/modelscope/evalscope/pull/840
* [Benchmark] add minerva-math by @Yunnglin in https://github.com/modelscope/evalscope/pull/846

## New Contributors
* @MemoryIt made their first contribution in https://github.com/modelscope/evalscope/pull/827

**Full Changelog**: https://github.com/modelscope/evalscope/compare/v1.0.1...v1.0.2

## v1.1.0 (2025-10-14)

## 更新
- 支持OCRBench, OCRBench-v2, DocVQA, InfoVQA, ChartQA, BLINK 等图文多模态评测基准，所有支持的数据集请[参考](https://evalscope.readthedocs.io/zh-cn/latest/get_started/supported_dataset/vlm.html)
- 编写[Qwen3-Omni](https://evalscope.readthedocs.io/zh-cn/latest/best_practice/qwen3_omni.html)和[Qwen3-VL](https://evalscope.readthedocs.io/zh-cn/latest/best_practice/qwen3_vl.html)模型评测最佳实践
- 支持`pyproject.toml`安装

## Update
- The platform now supports OCRBench, OCRBench-v2, DocVQA, InfoVQA, ChartQA, BLINK, and other multimodal evaluation benchmarks. For a comprehensive list of supported datasets, please [refer](https://evalscope.readthedocs.io/en/latest/get_started/supported_dataset/vlm.html).
- Developed best practice guidelines for evaluating models with [Qwen3-Omni](https://evalscope.readthedocs.io/en/latest/best_practice/qwen3_omni.html) and [Qwen3-VL](https://evalscope.readthedocs.io/en/latest/best_practice/qwen3_vl.html).
- Installation via `pyproject.toml` is now supported.

## What's Changed
* [Doc] Add qwen omni doc by @Yunnglin in https://github.com/modelscope/evalscope/pull/854
* [Fix] Fix bfcl_v3 validation by @Yunnglin in https://github.com/modelscope/evalscope/pull/858
* [Feature] Add pyproject.toml by @Yunnglin in https://github.com/modelscope/evalscope/pull/857
* [Benchmark] Add ChartQA and BLINK by @Yunnglin in https://github.com/modelscope/evalscope/pull/861
* [Benchmark] Add DocVQA and InfoVQA by @Yunnglin in https://github.com/modelscope/evalscope/pull/862
* [Fix] transformers import by @Yunnglin in https://github.com/modelscope/evalscope/pull/865
* [Benchmark] Add OCRBench and OCRBench-v2 by @Yunnglin in https://github.com/modelscope/evalscope/pull/869
* [Fix] None string error by @Yunnglin in https://github.com/modelscope/evalscope/pull/871


**Full Changelog**: https://github.com/modelscope/evalscope/compare/v1.0.2...v1.1.0

## v1.1.1 (2025-10-27)

## 更新

1. 基准测试扩展
- 视觉/多模态评测：HallusionBench、POPE、PloyMath、MathVerse、MathVision、SimpleVQA、SeedBench2_plus 
- 文档理解： OmniDocBench 
- NLP任务： CoNLL2003、NER 任务集合（9个任务）、AA-LCR 
- 逻辑推理： VisuLogic、ZeroBench 

2. 功能增强 
- 性能基准测试优化：perf 功能优化，可获得与 vLLM benchmarking 相媲美的测试结果，参考[使用文档](https://evalscope.readthedocs.io/zh-cn/latest/user_guides/stress_test/vs_vllm_bench.html)
- 代码评测环境增强：沙箱环境支持本地/远程双模式运行，提升代码安全性与灵活性，参考[使用文档](https://evalscope.readthedocs.io/zh-cn/latest/user_guides/sandbox.html)

3. 性能与稳定性优化
- 修复数据集中 prompt tokens 计算问题
- 增加评测过程中心跳检测机制
- 修复 GSM8K 准确率计算并增强日志记录

4. 系统要求更新
- **Python版本要求**：提升至 ≥3.10 （无依赖更新）

## Updates

1. **Benchmark Extensions**
- Vision/Multimodal Evaluation: HallusionBench, POPE, PloyMath, MathVerse, MathVision, SimpleVQA, SeedBench2_plus
- Document Understanding: OmniDocBench
- NLP Tasks: CoNLL2003, NER Task Collection (9 tasks), AA-LCR
- Logic Reasoning: VisuLogic, ZeroBench

2. **Feature Enhancements**
- Optimized perf functionality to achieve results comparable to vllm benchmarking, see [documentation](https://evalscope.readthedocs.io/zh-cn/latest/user_guides/stress_test/vs_vllm_bench.html)
- Enhanced sandbox environment usage in code evaluation, supporting both local and remote execution modes, see [documentation](https://evalscope.readthedocs.io/zh-cn/latest/user_guides/sandbox.html)

3. **Performance and Stability Improvements**
- Fixed prompt tokens calculation issues in datasets
- Added heartbeat detection mechanism during evaluation process
- Fixed GSM8K accuracy calculation and enhanced logging

4. **System Requirements Update**
- **Python Version Requirement**: Upgraded to ≥3.10 (no dependency updates)


## What's Changed
* Datasets: prompt tokens count bug fixed by @Aktsvigun in https://github.com/modelscope/evalscope/pull/873
* [Benchmark] Add HallusionBench and POPE by @Yunnglin in https://github.com/modelscope/evalscope/pull/875
* [Feature] Add inflight process by @Yunnglin in https://github.com/modelscope/evalscope/pull/880
* [Benchmark] Add PloyMath by @Yunnglin in https://github.com/modelscope/evalscope/pull/882
* add math_verse math_vision simple_vqa by @mushenL in https://github.com/modelscope/evalscope/pull/881
* fix: update Python version requirement to >=3.10 by @nowang6 in https://github.com/modelscope/evalscope/pull/890
* [Feature] Update perf thoughput by @Yunnglin in https://github.com/modelscope/evalscope/pull/894
* [Feature] Add extra query by @Yunnglin in https://github.com/modelscope/evalscope/pull/895
* add AA-LCR benchmark to evalscope by @sophies-cerebras in https://github.com/modelscope/evalscope/pull/897
* [feature] add `--visualizer` parameter instead of --XXX_api_key in stress test by @ShaohonChen in https://github.com/modelscope/evalscope/pull/878
* [Feature] Add sandbox doc by @Yunnglin in https://github.com/modelscope/evalscope/pull/899
* fix gsm8k acc and add more log by @ms-cs in https://github.com/modelscope/evalscope/pull/903
* [Doc] Update writing by @Yunnglin in https://github.com/modelscope/evalscope/pull/904
* [Benchmark] Add OmniDocBench by @Yunnglin in https://github.com/modelscope/evalscope/pull/908
* [Benchmark] Add CoNLL2003 benchmark by @penguinwang96825 in https://github.com/modelscope/evalscope/pull/912
* add seed_bench_2_plus,visu_logic_adapter,zerobench by @mushenL in https://github.com/modelscope/evalscope/pull/916
* [Benchmark] Add NER suite by @penguinwang96825 in https://github.com/modelscope/evalscope/pull/921
* [Feature] Add pred heartbeat by @ms-cs in https://github.com/modelscope/evalscope/pull/922

## New Contributors
* @Aktsvigun made their first contribution in https://github.com/modelscope/evalscope/pull/873
* @nowang6 made their first contribution in https://github.com/modelscope/evalscope/pull/890
* @sophies-cerebras made their first contribution in https://github.com/modelscope/evalscope/pull/897
* @ms-cs made their first contribution in https://github.com/modelscope/evalscope/pull/903
* @penguinwang96825 made their first contribution in https://github.com/modelscope/evalscope/pull/912

**Full Changelog**: https://github.com/modelscope/evalscope/compare/v1.1.0...v1.1.1

## v1.2.0 (2025-11-11)


## 中文版

### 基准测试数据集
- 新增多个MCQA（多项选择问答）数据集
- 新增Drivelology基准测试
- 更新BFCL-v3，新增支持BFCL-v4基准测试
- 更新tau-bench，新增支持tau2-bench
- 支持WMT机器翻译评测和相关指标

### 功能增强
- 优化答案提取机制 - 使答案提取过程更加明确和可控
- 支持batch计算指标，例如Bertscore等
- 更新聚合评分功能 - 新增pass@k、vote@k、pass^k等指标聚合
- 更新OpenAI API参数 - 优化API调用参数配置

### 数据源更新
- 更新SimpleQA数据源 - 使用最新的SimpleQA数据
- 对齐AIME到AA标准 - 统一评测标准
- 更新MMLU-Pro - 使用最新的MMLU-Pro数据

### 问题修复
- 修复DROP数据集few_shot_num=3的问题
- 修复缓冲区解码错误 - 解决了decode buffer相关的错误

## English Version

### Benchmark Datasets
- Added multiple MCQA (Multiple Choice Question Answering) datasets
- Added Drivelology benchmark
- Updated BFCL-v3 and added support for BFCL-v4 benchmark
- Updated tau-bench and added support for tau2-bench
- Added support for WMT machine translation evaluation and related metrics

### Feature Enhancements
- Optimized answer extraction mechanism - making the answer extraction process more explicit and controllable
- Added support for batch metric computation, such as Bertscore
- Updated aggregate scoring functionality - added metric aggregations including pass@k, vote@k, pass^k, etc.
- Updated OpenAI API parameters - optimized API call parameter configuration

### Data Source Updates
- Updated SimpleQA data source - using the latest SimpleQA data
- Aligned AIME to AA standard - unified evaluation standards
- Updated MMLU-Pro - using the latest MMLU-Pro data

### Bug Fixes
- Fixed the issue with DROP dataset when few_shot_num=3
- Fixed buffer decoding error - resolved decode buffer related issues

## What's Changed
* [Benchmark] Add MCQA datasets by @penguinwang96825 in https://github.com/modelscope/evalscope/pull/923
* [Benchmark] Add Drivelology benchmark by @penguinwang96825 in https://github.com/modelscope/evalscope/pull/927
* [Benchmark] Add more MCQA datasets by @penguinwang96825 in https://github.com/modelscope/evalscope/pull/928
* [Benchmark] Add BFCL-v4 by @Yunnglin in https://github.com/modelscope/evalscope/pull/934
* fix (dorp allow few_shot_num=3 in dataset args) 当前存在few_shot_num=3时，会… by @yuhuan0311 in https://github.com/modelscope/evalscope/pull/940
* [Fix] update DROP metric by @Yunnglin in https://github.com/modelscope/evalscope/pull/941
* [Feature] Update Bertscore for DrivelologyNarrativeWriting by @Yunnglin in https://github.com/modelscope/evalscope/pull/935
* Update SimpleQA source by @Yunnglin in https://github.com/modelscope/evalscope/pull/948
* [Feature] Update OpenAI API parameter by @Yunnglin in https://github.com/modelscope/evalscope/pull/949
* [Fix] decode buffer error by @Yunnglin in https://github.com/modelscope/evalscope/pull/954
* feat: update WMT adapters and related metrics by @Epsilon617 in https://github.com/modelscope/evalscope/pull/938
* [Benchmark] Update tau-bench and tau2-bench by @Yunnglin in https://github.com/modelscope/evalscope/pull/959
* [Fix] Update mmlu-pro by @Yunnglin in https://github.com/modelscope/evalscope/pull/960
* [Doc] Fixed the configuration error in BFCL-v4 documentation example (#962) by @Tsumugii24 in https://github.com/modelscope/evalscope/pull/963
* align aime to AA by @sophies-cerebras in https://github.com/modelscope/evalscope/pull/965
* [ADD] Implement metric aggregation pass@k and vote@k #387 by @xin8coder in https://github.com/modelscope/evalscope/pull/964
* [Feature] make extract answer explict by @Yunnglin in https://github.com/modelscope/evalscope/pull/966
* [Feature] Update aggregate_scores by @Yunnglin in https://github.com/modelscope/evalscope/pull/967

## New Contributors
* @yuhuan0311 made their first contribution in https://github.com/modelscope/evalscope/pull/940
* @Epsilon617 made their first contribution in https://github.com/modelscope/evalscope/pull/938
* @Tsumugii24 made their first contribution in https://github.com/modelscope/evalscope/pull/963
* @xin8coder made their first contribution in https://github.com/modelscope/evalscope/pull/964

**Full Changelog**: https://github.com/modelscope/evalscope/compare/v1.1.1...v1.2.0

## v1.3.0 (2025-11-28)

## 中文版

### 基准测试数据集
- 多模态评测: 新增 A_OKVQA、CMMU、CMMMU、ScienceQA、V*Bench、MicroVQA 等多模态基准测试
- 代码评测: 新增 SWE-bench_Verified、SWE-bench_Lite、SWE-bench_Verified_mini、SciCode 等代码能力评测
- 通用评测: 新增 GSM8K-V、MGSM、IFBench、OpenAI MRCR 等基准测试

### 功能增强
- 自定义工具调用评测: 支持自定义函数调用(function-call)评测能力，参考[使用文档](https://evalscope.readthedocs.io/zh-cn/latest/advanced_guides/custom_dataset/llm.html#fc)
- 自定义多模态VQA评测: 新增自定义视觉问答(VQA)评测支持，参考[使用文档](https://evalscope.readthedocs.io/zh-cn/latest/advanced_guides/custom_dataset/vlm.html)
- 聚合评分: 更新聚合(agg)参数，优化评分聚合机制
- 性能测试: 优化性能测试(perf)相关参数配置

### 文档优化
- 更新 collection 相关文档说明，支持自定义构建评测指数（index），参考[使用文档](https://evalscope.readthedocs.io/zh-cn/latest/advanced_guides/collection/index.html)

### 问题修复
- 修复 perf completion endpoint streaming 相关问题
- 修复 judge model 错误日志显示问题
- 修复 --no-test-connection 参数 action 问题
- 修复函数调用类测试用例错误处理问题(Issue #1005)
- 修复 model args 相关问题

---

## English Version

### Benchmark Datasets
- Multimodal Evaluation: Added A_OKVQA, CMMU, CMMMU, ScienceQA, V*Bench, MicroVQA and other multimodal benchmarks
- Code Evaluation: Added SWE-bench_Verified, SWE-bench_Lite, SWE-bench_Verified_mini, SciCode for code capability assessment
- General Evaluation: Added GSM8K-V, MGSM, IFBench, OpenAI MRCR and other benchmarks

### Feature Enhancements
- Custom Evaluation: Added support for custom function-call evaluation
- Custom VQA: Added support for custom Visual Question Answering (VQA) evaluation
- Parameter Extension: Added extra_param_spec functionality for more flexible parameter configuration
- Aggregate Scoring: Updated aggregation (agg) parameters to optimize scoring aggregation mechanism
- Performance Testing: Optimized performance (perf) related parameter configuration

### Documentation
- Updated eval_type related documentation
- Updated collection documentation

### Bug Fixes
- Fixed perf completion endpoint streaming issues
- Fixed error log display for judge model
- Fixed --no-test-connection parameter action issue
- Fixed error handling for function-call test cases (Issue #1005)
- Fixed model args related issues

## What's Changed
* [Doc] Update doc eval_type by @Yunnglin in https://github.com/modelscope/evalscope/pull/970
* [Benchmark] Add A_OKVQA,  CMMU,  ScienceQ,  V*Bench by @mushenL in https://github.com/modelscope/evalscope/pull/973
* [Benchmark] Add SWE-bench_Verified, SWE-bench_Lite, SWE-bench_Verified_mini by @Yunnglin in https://github.com/modelscope/evalscope/pull/976
* [Feature] Add custom function-call eval by @Yunnglin in https://github.com/modelscope/evalscope/pull/982
* [Fix]  perf completion endpoint streaming by @Yunnglin in https://github.com/modelscope/evalscope/pull/983
* [Fix] fix error log of judge model by @Yunnglin in https://github.com/modelscope/evalscope/pull/986
* add openai mrcr by @sophies-cerebras in https://github.com/modelscope/evalscope/pull/987
* [Feature] Add extra param spec by @Yunnglin in https://github.com/modelscope/evalscope/pull/990
* Add gsm8k_v,mgsm and micro_vqa benchmarks by @mushenL in https://github.com/modelscope/evalscope/pull/995
* fix: fix --no-test-connection args action by @ljwh in https://github.com/modelscope/evalscope/pull/999
* Update collection doc by @Yunnglin in https://github.com/modelscope/evalscope/pull/997
* [Benchmark] Add IFBench by @Yunnglin in https://github.com/modelscope/evalscope/pull/1001
* 解决Issue1005 处理函数调用类测试用例错误 问题 by @hougedengwo in https://github.com/modelscope/evalscope/pull/1007
* [Benchmark] Add SciCode by @Yunnglin in https://github.com/modelscope/evalscope/pull/1011
* [Fix] update perf args by @Yunnglin in https://github.com/modelscope/evalscope/pull/1013
* [Fix] model args by @Yunnglin in https://github.com/modelscope/evalscope/pull/1014
* [Feature] update agg args by @Yunnglin in https://github.com/modelscope/evalscope/pull/1016
* [Feature] Add custom VQA by @Yunnglin in https://github.com/modelscope/evalscope/pull/1019
* [Benchmark] add CMMMU by @Yunnglin in https://github.com/modelscope/evalscope/pull/1020

## New Contributors
* @ljwh made their first contribution in https://github.com/modelscope/evalscope/pull/999
* @hougedengwo made their first contribution in https://github.com/modelscope/evalscope/pull/1007

**Full Changelog**: https://github.com/modelscope/evalscope/compare/v1.2.0...v1.3.0

## v1.4.0 (2025-12-16)

## 中文版

### 基准测试数据集
- 通用评测: 新增 EQ-Bench、ZebraLogicBench 等推理与逻辑评测基准
- 代码评测: 新增 MultiplE、MBPP 等代码能力评测
- 语音评测: 新增 FLEURS、LibriSpeech 等语音识别基准测试

### 功能增强
- 性能测试可视化: 新增 ClearML 可视化支持，优化性能测试(perf)监控能力
- 服务API: 新增 service api 功能，提供更灵活的服务调用方式，参考[文档](https://evalscope.readthedocs.io/zh-cn/latest/user_guides/service.html)
- 懒加载模型: 新增 lazy model 支持，优化模型加载机制
- 重试机制: 新增 retry function，提升评测稳定性
- 沙箱优化: 更新 sandbox 支持连接池(pool)和 MultiplE 多语言代码评测
- 随机算法优化: 更新性能测试随机算法，提升测试准确性
- UI增强: Dashboard 支持 HTTP params 参数配置
- 进度条优化: 更新 tqdm 进度显示机制

### 文档优化
- 更新自定义 VQA 相关文档
- 更新参数配置相关文档
- 更新基准测试(benchmarks)文档
- 更新服务(service)相关文档
- 更新 MTEB 相关链接

### 问题修复
- 修复 --analysis-report、--dataset-dir 等命令行参数问题
- 修复并发为1时的令牌吞吐量计算问题
- 修复 ChartQA、TAU2、OmniDocBench 等基准测试加载问题
- 修复 SWE-bench 镜像构建、MRCR 前导换行符支持等问题
- 修复 NLTK 资源检查相关问题

---

## English Version

### Benchmark Datasets
- General Evaluation: Added EQ-Bench, ZebraLogicBench for reasoning and logic evaluation
- Code Evaluation: Added MultiplE-MBPP, MBPP for code capability assessment
- Speech Evaluation: Added FLEURS, LibriSpeech for speech recognition benchmarks

### Feature Enhancements
- Performance Visualization: Added ClearML visualization support for performance (perf) monitoring
- Service API: Added service api functionality for more flexible service invocation
- Lazy Model Loading: Added lazy model support to optimize model loading mechanism
- Retry Mechanism: Added retry function to improve evaluation stability
- Sandbox Optimization: Updated sandbox with connection pool support and multiple-humaneval evaluation
- Random Algorithm: Updated performance testing random algorithm for improved accuracy
- UI Enhancement: Dashboard now supports HTTP params parameter configuration
- Progress Bar: Updated tqdm progress display mechanism

### Documentation
- Updated custom VQA documentation
- Updated parameter configuration documentation
- Updated benchmarks documentation
- Updated service documentation
- Updated MTEB related links

### Bug Fixes
- Fixed command-line parameter issues (--analysis-report, --dataset-dir, etc.)
- Fixed token throughput calculation at concurrency 1
- Fixed benchmark loading issues (ChartQA, TAU2, OmniDocBench, etc.)
- Fixed SWE-bench image build and MRCR leading newline support
- Fixed NLTK resource checking issues

## What's Changed
* [Feature] Add perf ClearML visualization by @Yunnglin in https://github.com/modelscope/evalscope/pull/1032
* [Doc] update custom vqa by @Yunnglin in https://github.com/modelscope/evalscope/pull/1036
* [Benchmark ]Add eq bench by @Yunnglin in https://github.com/modelscope/evalscope/pull/1037
* Feature/zebralogicbench by @nhes in https://github.com/modelscope/evalscope/pull/1035
* [Fix] Update tau2 by @Yunnglin in https://github.com/modelscope/evalscope/pull/1039
* [Feature] Add service api by @Yunnglin in https://github.com/modelscope/evalscope/pull/1042
* fix --analysis-report=true bug by @pumpkin12135 in https://github.com/modelscope/evalscope/pull/1046
* [feature] add lazy model by @Secbone in https://github.com/modelscope/evalscope/pull/1045
* [Doc] update parameter by @Yunnglin in https://github.com/modelscope/evalscope/pull/1048
* [Fix] update default work dir by @Yunnglin in https://github.com/modelscope/evalscope/pull/1049
* [Feature] Update perf random Algorithm by @Yunnglin in https://github.com/modelscope/evalscope/pull/1050
* [Feature] add retry function by @Yunnglin in https://github.com/modelscope/evalscope/pull/1051
* Fix --dataset-dir parameter to work correctly by @gbdjxgp in https://github.com/modelscope/evalscope/pull/1053
* [Fix] chartqa prompt by @Yunnglin in https://github.com/modelscope/evalscope/pull/1054
* [Benchmark] Add fleurs, librispeech by @Yunnglin in https://github.com/modelscope/evalscope/pull/1059
* [Fix] multi-if load by @Yunnglin in https://github.com/modelscope/evalscope/pull/1062
* [Benchmakr] Add MultiplE-mbpp, MBPP by @Yunnglin in https://github.com/modelscope/evalscope/pull/1066
* Update mteb link by @Samoed in https://github.com/modelscope/evalscope/pull/1065
* UI dashboard supports HTTP params parameters by @pumpkin12135 in https://github.com/modelscope/evalscope/pull/1060
* [Feature] update sandbox with pool and multiple-humaneval by @Yunnglin in https://github.com/modelscope/evalscope/pull/1073
* check_nltk_data does not accept a parameter by @Zhaoyi-Yan in https://github.com/modelscope/evalscope/pull/1071
* [Fix] update check nltk resource by @Yunnglin in https://github.com/modelscope/evalscope/pull/1078
* [Fix] omni doc bench load by @Yunnglin in https://github.com/modelscope/evalscope/pull/1079
* [Doc] update benchmarks doc by @Yunnglin in https://github.com/modelscope/evalscope/pull/1081
* [Doc] update service and doc by @Yunnglin in https://github.com/modelscope/evalscope/pull/1085
* fix: Output token throughput and Total token throughput on Concurrency 1 by @cdpath in https://github.com/modelscope/evalscope/pull/1083
* [Fix] SWE build image by @Yunnglin in https://github.com/modelscope/evalscope/pull/1087
* small fixes to mrcr to support leading \n characters by @sophies-cerebras in https://github.com/modelscope/evalscope/pull/1086
* [Feature] Update tqdm process by @Yunnglin in https://github.com/modelscope/evalscope/pull/1089

## New Contributors
* @nhes made their first contribution in https://github.com/modelscope/evalscope/pull/1035
* @pumpkin12135 made their first contribution in https://github.com/modelscope/evalscope/pull/1046
* @Secbone made their first contribution in https://github.com/modelscope/evalscope/pull/1045
* @gbdjxgp made their first contribution in https://github.com/modelscope/evalscope/pull/1053
* @Samoed made their first contribution in https://github.com/modelscope/evalscope/pull/1065
* @Zhaoyi-Yan made their first contribution in https://github.com/modelscope/evalscope/pull/1071
* @cdpath made their first contribution in https://github.com/modelscope/evalscope/pull/1083

**Full Changelog**: https://github.com/modelscope/evalscope/compare/v1.3.0...v1.4.0

## v1.4.1 (2026-01-05)

## 中文版

### 基准测试数据集
- 命名实体识别: 新增 12 个 NER（命名实体识别）数据集
- 语音识别: 新增 TORGO 数据集，用于构音障碍语音识别评测，支持 SemScore 评估
- 多模态评测: 新增 RefCOCO 基准测试
- 代码评测: 新增 Terminal-bench 终端命令能力评测

### 功能增强
- 性能测试: 新增 SLA 自动调优功能，优化性能测试体验
- 服务模式: 新增异步服务支持和 Gradio UI 界面
- 数据加载: 优化本地 JSONL 数据集加载功能

### 问题修复
- 修复 HallusionBench 数据加载问题
- 修复流式响应解析中的 SSE 分块处理问题

---

## English Version

### Benchmark Datasets
- Named Entity Recognition: Added 12 NER (Named Entity Recognition) datasets
- Speech Recognition: Added TORGO dataset for dysarthria speech recognition with SemScore evaluation
- Multimodal Evaluation: Added RefCOCO referring expression comprehension benchmark
- Code Evaluation: Added Terminal-bench for terminal command capability assessment

### Feature Enhancements
- Performance Testing: Added SLA auto-tuning functionality to optimize performance testing experience
- Service Mode: Added asynchronous service support and Gradio UI interface
- Data Loading: Optimized local JSONL dataset loading functionality

### Bug Fixes
- Fixed HallusionBench data loading issues
- Fixed SemScore computation errors
- Fixed eval_config loading related issues

## What's Changed
* [Fix] hallusion_bench load data by @Yunnglin in https://github.com/modelscope/evalscope/pull/1092
* [Feature] Add perf SLA auto tune by @Yunnglin in https://github.com/modelscope/evalscope/pull/1095
* [Feature] add service async and gradio ui by @Yunnglin in https://github.com/modelscope/evalscope/pull/1103
* fix(streaming): Robust parsing of SSE chunks with multiple events and \r\n normalization by @amumu96 in https://github.com/modelscope/evalscope/pull/1102
* Add 12 NER Datasets by @penguinwang96825 in https://github.com/modelscope/evalscope/pull/1106
* [Benchmark] Add TORGO Dataset for Dysarthria Speech Recognition with SemScore Evaluation by @penguinwang96825 in https://github.com/modelscope/evalscope/pull/1107
* [Benchmark] Add RefCOCO by @mushenL in https://github.com/modelscope/evalscope/pull/1109
* [Fix] computation error in SemScore by @penguinwang96825 in https://github.com/modelscope/evalscope/pull/1110
* [Feature] Update load local jsonl by @Yunnglin in https://github.com/modelscope/evalscope/pull/1111
* [Fix] eval_config load by @Yunnglin in https://github.com/modelscope/evalscope/pull/1116
* [Benchmark] Add terminal-bench by @Yunnglin in https://github.com/modelscope/evalscope/pull/1114

## New Contributors
* @amumu96 made their first contribution in https://github.com/modelscope/evalscope/pull/1102

**Full Changelog**: https://github.com/modelscope/evalscope/compare/v1.4.0...v1.4.1

## v1.4.2 (2026-01-19)

## 中文版

### 基准测试数据集
- 代码评测: 新增 HumanEvalPlus、MBPPPlus 等代码能力评测

### 功能增强
- 性能测试: 新增对 Embedding 和 Rerank 模型的性能测试支持

### 文档优化
- 新增 general_fc 最佳实践文档
- 更新 collection 相关文档说明，支持自定义构建评测指数（index），参考[使用文档](https://evalscope.readthedocs.io/zh-cn/latest/advanced_guides/collection/index.html)
- 更新性能测试文档，新增 Embedding 和 Rerank 模型评测说明

### 问题修复
- 修复性能测试日志输出问题
- 修复 SimpleVQA 图像加载问题

---

## English Version

### Benchmark Datasets
- Code Evaluation: Added HumanEvalPlus and MBPPPlus for code capability assessment

### Feature Enhancements
- Performance Testing: Added support for Embedding and Rerank models performance evaluation

### Documentation
- Added general_fc best practice documentation
- Updated collection documentation with support for custom index construction
- Updated performance testing documentation with Embedding and Rerank model evaluation instructions

### Bug Fixes
- Fixed performance testing log output issues
- Fixed SimpleVQA image loading issues

## What's Changed
* [Doc] Add general_fc best practice by @Yunnglin in https://github.com/modelscope/evalscope/pull/1130
* [Doc] update index collection doc by @Yunnglin in https://github.com/modelscope/evalscope/pull/1132
* [Fix] update perf log by @Yunnglin in https://github.com/modelscope/evalscope/pull/1135
* [Draft] feat(perf): add support for embedding and rerank models by @gbdjxgp in https://github.com/modelscope/evalscope/pull/1140
* add humanevalplus and mbppplus benchmarks by @mushenL in https://github.com/modelscope/evalscope/pull/1144
* [Doc]update perf embedding and rerank by @Yunnglin in https://github.com/modelscope/evalscope/pull/1147
* [fix] simplevqa image load by @Yunnglin in https://github.com/modelscope/evalscope/pull/1153


**Full Changelog**: https://github.com/modelscope/evalscope/compare/v1.4.1...v1.4.2

## v1.5.0 (2026-03-10)

## 中文版

### 基准测试数据集
- 数学评测: 新增 HMMT25 数学基准测试
- 代码评测: 新增 CL-bench (腾讯) 基准测试
- 修复 LiveCodeBench 代码提取逻辑，改为使用最后一个代码块

### 功能增强
- Judge LLM 类型指定: 支持在评测中指定 Judge LLM 的类型
- 火山引擎沙箱支持: 新增 Volcengine 沙箱环境支持
- Anthropic API 支持: 新增 Anthropic API 接入能力
- 性能测试进度条: 为 perf 数据集处理新增 tqdm 进度条显示
- 统一子集更新: 更新 unify subset 相关逻辑
- 服务端 Demo 更新: 优化 server demo 展示

### 文档优化
- 新增基准测试详情文档说明
- 更新 eval_type 相关文档
- 更新文档同步脚本

### 问题修复
- 修复空数据集跳过处理问题
- 修复 rate type 更新问题
- 修复 input_audio 错误前缀问题 (Issue #1152)

---

## English Version

### Benchmark Datasets
- Math Evaluation: Added HMMT25 math benchmark
- Code Evaluation: Added CL-bench (Tencent) benchmark
- Fixed LiveCodeBench code extraction to use the last fenced code block

### Feature Enhancements
- Judge LLM Type: Added support for specifying judge LLM type in evaluation
- Volcengine Sandbox: Added Volcengine sandbox environment support
- Anthropic API: Added Anthropic API integration support
- Performance Testing Progress Bar: Added tqdm progress display for perf dataset processing
- Unified Subset Update: Updated unify subset related logic
- Server Demo Update: Optimized server demo presentation

### Documentation
- Added benchmark detail documentation
- Updated eval_type related documentation
- Updated doc sync script

### Bug Fixes
- Fixed empty dataset skipping issue
- Fixed rate type update issue
- Fixed input_audio wrong prefix issue (Issue #1152)

## What's Changed
* feat: specify judge llm type by @jerryldh in https://github.com/modelscope/evalscope/pull/1157
* feat(benchmark): add HMMT25 math benchmark by @XChen-Zero in https://github.com/modelscope/evalscope/pull/1154
* [Fix] skip empty dataset by @Yunnglin in https://github.com/modelscope/evalscope/pull/1161
* feat: add Volcengine sandbox support by @XChen-Zero in https://github.com/modelscope/evalscope/pull/1160
* [Fix] update rate type by @Yunnglin in https://github.com/modelscope/evalscope/pull/1166
* [Feature] add perf dataset tqdm by @Yunnglin in https://github.com/modelscope/evalscope/pull/1168
* Fix LiveCodeBench extraction: use last fenced code block by @koshieguchi in https://github.com/modelscope/evalscope/pull/1170
* [Doc] benchmarks detail doc by @Yunnglin in https://github.com/modelscope/evalscope/pull/1180
* [Fix] fix input_audio wrong prefix (modelscope/evalscope#1152) by @labAxiaoming in https://github.com/modelscope/evalscope/pull/1174
* feat/Add CL-bench (tencent/CL-bench) benchmark by @XChen-Zero in https://github.com/modelscope/evalscope/pull/1191
* Add anthropic api by @Yunnglin in https://github.com/modelscope/evalscope/pull/1202
* update sync doc script by @Yunnglin in https://github.com/modelscope/evalscope/pull/1205
* [Feature] Update server demo by @Yunnglin in https://github.com/modelscope/evalscope/pull/1215
* [Doc] update eval_type by @Yunnglin in https://github.com/modelscope/evalscope/pull/1217
* [Feature] update unify subset by @Yunnglin in https://github.com/modelscope/evalscope/pull/1220

## New Contributors
* @jerryldh made their first contribution in https://github.com/modelscope/evalscope/pull/1157
* @XChen-Zero made their first contribution in https://github.com/modelscope/evalscope/pull/1154
* @koshieguchi made their first contribution in https://github.com/modelscope/evalscope/pull/1170
* @labAxiaoming made their first contribution in https://github.com/modelscope/evalscope/pull/1174

**Full Changelog**: https://github.com/modelscope/evalscope/compare/v1.4.2...v1.5.0

## v1.5.1 (2026-03-23)

## 中文版

### 基准测试数据集
- 新增 AIME 2026 数学竞赛基准测试
- 新增 MMMLU 多语言大规模多任务理解基准测试
- 新增 LongBench v2 长文本理解基准测试

### 功能增强
- 性能测试: 新增获取基准端点（get benchmark endpoint）功能，修复测试连接参数配置
- 性能测试: 优化 SLA 自动调优（SLA auto tune）功能
- 评测服务: 支持以表格形式返回评测结果，修复分析统计相关问题
- Judge 模型: 支持为 Judge LLM 配置 model_args 参数
- 请求追踪: 支持打印 request id，便于请求追踪与调试

### 问题修复
- 修复 `eval()` 安全性问题，替换为 `ast.literal_eval()` 处理字符串参数解析
- 修复性能测试（perf）tokenize 及空子集（empty subset）相关问题
- 修复数据集 shuffle 随机性问题，使用带种子的 `random.Random` 确保可复现性

---

## English Version

### Benchmark Datasets
- Added AIME 2026 math competition benchmark
- Added MMMLU (Multilingual Massive Multitask Language Understanding) benchmark
- Added LongBench v2 for long-context understanding evaluation

### Feature Enhancements
- Performance Testing: Added get benchmark endpoint and fixed test connection parameter configuration
- Performance Testing: Added SLA auto-tune functionality
- Evaluation Service: Support returning results in table format and fixed analysis bugs
- Judge Model: Added model_args support for judge LLM configuration
- Request Tracking: Added request ID printing for better request tracing and debugging

### Bug Fixes
- Fixed security issue by replacing `eval()` with `ast.literal_eval()` for string argument parsing
- Fixed perf tokenize and empty subset related issues
- Fixed dataset shuffling reproducibility by using seeded `random.Random`

## What's Changed
* Replace eval() with ast.literal_eval() in ParseStrArgsAction by @RinZ27 in https://github.com/modelscope/evalscope/pull/1221
* [Fix] update kontext_bench, refcoco by @Yunnglin in https://github.com/modelscope/evalscope/pull/1229
* [Benchmark]Add aime26 and  SLA auto tune by @Yunnglin in https://github.com/modelscope/evalscope/pull/1230
* [Fix] perf test connection args and add get benchmark endpoint by @Yunnglin in https://github.com/modelscope/evalscope/pull/1232
* [Benchmark] add mmmlu by @Yunnglin in https://github.com/modelscope/evalscope/pull/1235
* [Fix]perf tokenize and empty subset by @Yunnglin in https://github.com/modelscope/evalscope/pull/1236
* [Benchmark] Add longbench_v2 by @Yunnglin in https://github.com/modelscope/evalscope/pull/1237
* [Feature] Return table for service and fix analysis bug by @Yunnglin in https://github.com/modelscope/evalscope/pull/1240
* Add model_args for judge LLM by @haihongtran in https://github.com/modelscope/evalscope/pull/1241
* print request id by @strenuous-life in https://github.com/modelscope/evalscope/pull/1242
* [Fix] Use seeded random.Random for dataset shuffling by @pcabriada in https://github.com/modelscope/evalscope/pull/1243

## New Contributors
* @RinZ27 made their first contribution in https://github.com/modelscope/evalscope/pull/1221
* @haihongtran made their first contribution in https://github.com/modelscope/evalscope/pull/1241
* @strenuous-life made their first contribution in https://github.com/modelscope/evalscope/pull/1242
* @pcabriada made their first contribution in https://github.com/modelscope/evalscope/pull/1243

**Full Changelog**: https://github.com/modelscope/evalscope/compare/v1.5.0...v1.5.1

## v1.5.2 (2026-03-31)

## What's Changed
* [Feature] Add Skill by @Yunnglin in https://github.com/modelscope/evalscope/pull/1248
* [Fix] Modify error retry logic and judge_num_work parameter by @Yunnglin in https://github.com/modelscope/evalscope/pull/1251
* [Benchmarks]Add MIA-Bench by @Yunnglin in https://github.com/modelscope/evalscope/pull/1252
* 修复子进程中加载评测模型报错问题 by @liulei08 in https://github.com/modelscope/evalscope/pull/1254
* [update] server response by @Yunnglin in https://github.com/modelscope/evalscope/pull/1258

## New Contributors
* @liulei08 made their first contribution in https://github.com/modelscope/evalscope/pull/1254

**Full Changelog**: https://github.com/modelscope/evalscope/compare/v1.5.1...v1.5.2

## v1.5.2.post1 (2026-03-31)

## What's Changed
* [Update] dataset loader for datasets>4.0 by @Yunnglin in https://github.com/modelscope/evalscope/pull/1260


**Full Changelog**: https://github.com/modelscope/evalscope/compare/v1.5.2...v1.5.2.post1

## v1.6.0 (2026-04-13)

## 中文版

### 功能增强
- 服务日志优化: 更新 server 日志，提升日志信息展示与排查体验
- 依赖更新: 升级部分项目依赖，优化整体兼容性与稳定性
- 报告样式优化: 调整报告品牌色彩，新增固定品牌栏与品牌标志，提升展示效果

### 问题修复
- 修复多模态数据集加载错误问题，并补充 reasoning tokens 统计能力
- 修复性能测试自动追加 perf 后缀相关问题
- 修复 perf 路径处理异常，规范性能测试路径
- 修复 nltk 下载及 progress tracker 相关问题
- 修复性能测试中 fixed parallel 与 SLA rate 上限耦合问题，优化压测参数行为

---

## English Version

### Feature Enhancements
- Server Logging: Updated server logs to improve log visibility and troubleshooting experience
- Dependency Update: Updated project dependencies for better compatibility and stability
- Report Style Optimization: Refined report branding colors and added a fixed brand bar and brand logo for improved presentation

### Bug Fixes
- Fixed multimodal dataset loading errors and added reasoning token counting
- Fixed issues with automatically appending the perf suffix in performance testing
- Fixed abnormal perf path handling and normalized performance test paths
- Fixed nltk download and progress tracker related issues
- Fixed the coupling between fixed parallel and SLA rate upper bound in performance testing to improve parameter behavior

## What's Changed
* [Fix] Fix load multimodal dataset error and count reasoning tokens by @Yunnglin in https://github.com/modelscope/evalscope/pull/1267
* [Fix] Auto append perf suffix by @Yunnglin in https://github.com/modelscope/evalscope/pull/1268
* [Fix] normal perf path by @Yunnglin in https://github.com/modelscope/evalscope/pull/1269
* [Fix] download nltk and progress tracker by @Yunnglin in https://github.com/modelscope/evalscope/pull/1270
* style(report): 调整品牌色彩并添加固定品牌栏和品牌标志 by @ZhengYingqian in https://github.com/modelscope/evalscope/pull/1271
* [Feature]update server log by @Yunnglin in https://github.com/modelscope/evalscope/pull/1279
* fix(perf): decouple fixed parallel from SLA rate upper bound by @HouXianzhoua in https://github.com/modelscope/evalscope/pull/1286
* [Feature] Update dependancy by @Yunnglin in https://github.com/modelscope/evalscope/pull/1288

## New Contributors
* @ZhengYingqian made their first contribution in https://github.com/modelscope/evalscope/pull/1271
* @HouXianzhoua made their first contribution in https://github.com/modelscope/evalscope/pull/1286

**Full Changelog**: https://github.com/modelscope/evalscope/compare/v1.5.2.post1...v1.6.0

## v1.6.1 (2026-04-24)

## 中文版

### 基准测试数据集
- 新增 TIR-Bench 基准测试

### 功能增强
- Tokenize Prompt: 新增 tokenize prompt 开关，支持灵活控制 prompt 的 tokenize 行为
- 多轮性能测试: 新增多轮对话性能测试 (multi turn perf) 支持
- 自定义多轮性能测试: 新增自定义多轮性能测试 (custom multi_turn perf) 能力
- 评测集成性能测试: 在评测流程中集成性能测试 (perf in eval)
- 投机解码指标: 新增投机解码 (speculative decoding) 性能指标

### 问题修复
- 修复加载默认本地数据集的问题
- 修复 tokenize-prompt 长度语义问题
- 修复 tokenize 模板问题
- 更新 plot CDN 地址，避免网络加速后访问异常

---

## English Version

### Benchmark Datasets
- Added TIR-Bench benchmark

### Feature Enhancements
- Tokenize Prompt: Added tokenize prompt switch for flexible prompt tokenization control
- Percentile Metrics: Added support for P50, P90 percentile statistics
- Multi-turn Performance: Added multi-turn conversation performance testing (multi turn perf)
- Custom Multi-turn Performance: Added custom multi-turn performance testing (custom multi_turn perf)
- Perf in Evaluation: Integrated performance testing in evaluation workflow (perf in eval)
- Speculative Metrics: Added speculative decoding performance metrics

### Bug Fixes
- Fixed loading default local dataset issue
- Fixed tokenize-prompt length semantics issue
- Fixed tokenize template issue
- Updated plot CDN address to avoid access issues after network acceleration

## What's Changed
* [Feature] Add tokenize prompt switch by @Yunnglin in https://github.com/modelscope/evalscope/pull/1289
* Feat/support p50 p90 percentiles by @yonlunwu in https://github.com/modelscope/evalscope/pull/1283
* update log filehandler by @Yunnglin in https://github.com/modelscope/evalscope/pull/1292
* [Fix] load default local dataset by @Yunnglin in https://github.com/modelscope/evalscope/pull/1293
* [Benchmark] Add TIR-Bench by @Yunnglin in https://github.com/modelscope/evalscope/pull/1295
* [Feature]Add multi turn perf by @Yunnglin in https://github.com/modelscope/evalscope/pull/1298
* Ensure output directory is created automatically when dumping JSONL files by @ShaohonChen in https://github.com/modelscope/evalscope/pull/1296
* Fix tokenize-prompt length semantics by @zongjing1998 in https://github.com/modelscope/evalscope/pull/1301
* [Feature]update time zone by @Yunnglin in https://github.com/modelscope/evalscope/pull/1303
* [Feature] Add speculative perf metrics by @Yunnglin in https://github.com/modelscope/evalscope/pull/1306
* feat: 更新plot的cdn地址，避免网络加速后访问异常 by @ZhengYingqian in https://github.com/modelscope/evalscope/pull/1308
* [Feature] Add custom multi_turn perf by @Yunnglin in https://github.com/modelscope/evalscope/pull/1309
* [Feature] Add perf in eval by @Yunnglin in https://github.com/modelscope/evalscope/pull/1310
* [Fix] tokenize template issue by @Yunnglin in https://github.com/modelscope/evalscope/pull/1311

## New Contributors
* @yonlunwu made their first contribution in https://github.com/modelscope/evalscope/pull/1283
* @zongjing1998 made their first contribution in https://github.com/modelscope/evalscope/pull/1301

**Full Changelog**: https://github.com/modelscope/evalscope/compare/v1.6.0...v1.6.1

## v1.7.1 (2026-05-18)

## 中文版

### 基准测试数据集
- 多模态评测: 新增 AIR-Bench 基准测试支持
- 视频评测: 新增原生视频基准测试支持，包括 MVBench、Video-MME-v2

### 功能增强
- WebUI 与多轮评测: 重构 WebUI，并优化多轮评测能力
- 模型网关支持: 新增 LiteLLM 作为 AI gateway provider
- 性能测试: 新增 perf swe-smith 压测能力
- 性能测试: 新增 perf warmup 预热能力
- 自定义数据集: 支持 line_by_line_oai 自定义数据集模式
- 评测能力: 新增 multi-mcq 支持
- Agent 能力: 新增 agent loop 支持
- 评测资源管理: 为 T2V metric assets 新增 local-only 本地加载开关
- 沙箱能力: 更新 volcengine sandbox 支持

### 文档优化
- 更新 Web 相关文档说明

### 问题修复
- 修复 perf swe-smith 相关问题
- 修复 aigc device args 相关问题
- 修复 IFBench 评测逻辑问题

---

## English Version

### Benchmark Datasets
- Multimodal Evaluation: Added AIR-Bench benchmark support
- Video Evaluation: Added native video benchmark support, including MVBench and Video-MME-v2

### Feature Enhancements
- WebUI and Multi-turn Evaluation: Refactored WebUI and improved multi-turn evaluation capabilities
- Model Gateway Support: Added LiteLLM as an AI gateway provider
- Performance Testing: Added perf swe-smith benchmarking capability
- Performance Testing: Added perf warmup support
- Custom Dataset: Added support for line_by_line_oai custom dataset mode
- Evaluation Capability: Added multi-mcq support
- Agent Capability: Added agent loop support
- Evaluation Asset Management: Added local-only loading switch for T2V metric assets
- Sandbox Support: Updated volcengine sandbox support

### Documentation
- Updated Web-related documentation

### Bug Fixes
- Fixed perf swe-smith related issues
- Fixed aigc device args related issues
- Fixed IFBench evaluation logic issue

## What's Changed
* [Feature]Refact webui and multi-turn eval by @Yunnglin in https://github.com/modelscope/evalscope/pull/1315
* feat: add LiteLLM as AI gateway provider by @RheagalFire in https://github.com/modelscope/evalscope/pull/1317
* [Feature]Add perf swe-smith by @Yunnglin in https://github.com/modelscope/evalscope/pull/1321
* [Fix] perf swe-smith by @Yunnglin in https://github.com/modelscope/evalscope/pull/1322
* [Fix] perf swe-smith load by @Yunnglin in https://github.com/modelscope/evalscope/pull/1323
* [Fix] perf swe multi process by @Yunnglin in https://github.com/modelscope/evalscope/pull/1324
* [Feature]Update web and docs by @Yunnglin in https://github.com/modelscope/evalscope/pull/1326
* [Feature] Add perf warmup by @Yunnglin in https://github.com/modelscope/evalscope/pull/1329
* [Fix]update aigc device args by @Yunnglin in https://github.com/modelscope/evalscope/pull/1336
* Add local-only loading switch for T2V metric assets by @AuFlow in https://github.com/modelscope/evalscope/pull/1334
* [update] volcengine sandbox by @Yunnglin in https://github.com/modelscope/evalscope/pull/1337
* [Feature]Add multi-mcq by @Yunnglin in https://github.com/modelscope/evalscope/pull/1345
* [Feature] Add AIR-Bench benchmark support by @haoruilee in https://github.com/modelscope/evalscope/pull/1341
* support line_by_line_oai custom dataset mode by @llc-kc in https://github.com/modelscope/evalscope/pull/1342
* [Feature] Add native video benchmark support with MVBench and Video-MME-v2 by @haoruilee in https://github.com/modelscope/evalscope/pull/1343
* [Feature]Add agent loop by @Yunnglin in https://github.com/modelscope/evalscope/pull/1344
* [Fix] ifbench eval logic by @Yunnglin in https://github.com/modelscope/evalscope/pull/1346

## New Contributors
* @RheagalFire made their first contribution in https://github.com/modelscope/evalscope/pull/1317
* @AuFlow made their first contribution in https://github.com/modelscope/evalscope/pull/1334
* @haoruilee made their first contribution in https://github.com/modelscope/evalscope/pull/1341
* @llc-kc made their first contribution in https://github.com/modelscope/evalscope/pull/1342

**Full Changelog**: https://github.com/modelscope/evalscope/compare/v1.6.1...v1.7.1

## v1.8.0 (2026-05-28)

## 中文版

  ### 基准测试数据集
  - Agent 评测: 新增 SWE-Bench Pro、Tau3-Bench、GAIA、Terminal-Bench v2.1 等 Agent 能力评测基准
  - 通用评测: 新增 ArxivRollBench 学术论文理解基准测试
  - 厂商验证评测: 新增 k2、kimi、minimax 等厂商验证器基准测试

  ### 功能增强
  - OpenAI Responses API: 新增 OpenAI Responses API 支持 (Issue #1192)
  - API Reranker 评测: 支持 API reranker 评测能力 (Issue #1029)
  - Agent Bridge: 新增 Agent Bridge 功能及 WebUI 更新
  - MCP Server 支持: NativeAgentConfig 支持配置 MCP server
  - 图片压缩: 新增多模态评测可配置图片压缩功能
  - 性能测试 - Trie 回放: 支持 trie agentic trace replay、Turn 模型及 --duration 参数
  - 性能测试 - SwanLab: 支持自部署 SwanLab 的 swanlab_host 配置

  ### 文档优化
  - 统一 agent 相关指引至 AGENTS.md

  ### 问题修复
  - 修复 build_docker_images 未优先 subset 数据集的问题 (#1348)
  - 修复 tokenizer 加载时 max_position_embeddings AttributeError (#1354)
  - 修复 livecodebench 数据集迁移至 ModelScope parquet 格式 (#1357)
  - 修复 DatasetDict.from_dataset 中 repeats 参数无效的问题 (#1363)
  - 修复 perf open-loop / rate-paced 模式下实际 QPS 不稳定的问题 (#1367)
  - 修复 perf SLA 多轮平均后整数字段未取整的问题 (#1370)
  - 修复 agent sandbox 中 ms_enclave 缺失时未快速失败的问题 (#1372)

  ---

  ## English Version

  ### Benchmark Datasets
  - Agent Evaluation: Added SWE-Bench Pro, Tau3-Bench, GAIA, Terminal-Bench v2.1 for agent capability assessment
  - General Evaluation: Added ArxivRollBench for academic paper comprehension
  - Vendor Verifier: Added k2, kimi, minimax vendor verifier benchmarks

  ### Feature Enhancements
  - OpenAI Responses API: Added OpenAI Responses API support (Issue #1192)
  - API Reranker Evaluation: Added support for API reranker evaluation (Issue #1029)
  - Agent Bridge: Added Agent Bridge functionality with WebUI update
  - MCP Server Support: Added MCP server configuration for NativeAgentConfig
  - Image Compression: Added configurable image compression for VLM benchmarks
  - Perf - Trie Replay: Added trie agentic trace replay, Turn model, and --duration parameter
  - Perf - SwanLab: Added swanlab_host support for self-hosted SwanLab deployments

  ### Documentation
  - Unified agent instructions into AGENTS.md

  ### Bug Fixes
  - Fixed build_docker_images check to always subset dataset first (#1348)
  - Fixed max_position_embeddings AttributeError in tokenizer loading (#1354)
  - Fixed livecodebench migration to parquet dataset on ModelScope (#1357)
  - Fixed ineffective repeats in DatasetDict.from_dataset (#1363)
  - Fixed unstable realised QPS in open-loop / rate-paced benchmarks (#1367)
  - Fixed int fields rounding after SLA multi-run averaging (#1370)
  - Fixed fail-fast in EnclaveAgentEnvironment when ms_enclave is missing (#1372)

## What's Changed
* core: fix build_docker_images check to always subset dataset first by @liguodongiot in https://github.com/modelscope/evalscope/pull/1348
* [Update] old agent benchmarks by @Yunnglin in https://github.com/modelscope/evalscope/pull/1349
* perf: support swanlab_host for self-hosted SwanLab deployments by @Yunnglin in https://github.com/modelscope/evalscope/pull/1350
* [Benchmark] Add SWE-Bench pro and Tau3-Bench by @Yunnglin in https://github.com/modelscope/evalscope/pull/1351
* Add OpenAI Responses API support, solve #1192 by @haoruilee in https://github.com/modelscope/evalscope/pull/1352
* docs: unify agent instructions into AGENTS.md by @Yunnglin in https://github.com/modelscope/evalscope/pull/1353
* fix: handle max_position_embeddings AttributeError in tokenizer loading by @Yunnglin in https://github.com/modelscope/evalscope/pull/1354
* feat: add configurable image compression for VLM benchmarks by @Yunnglin in https://github.com/modelscope/evalscope/pull/1355
* fix: migrate livecodebench to parquet dataset on ModelScope by @Yunnglin in https://github.com/modelscope/evalscope/pull/1357
* [Fix] Fix ineffective repeats in DatasetDict.from_dataset by @we1sper in https://github.com/modelscope/evalscope/pull/1363
* fix(perf): stabilise realised QPS in open-loop / rate-paced benchmarks by @Syqinx in https://github.com/modelscope/evalscope/pull/1367
* [Feature] Add agent bridge and webui update by @Yunnglin in https://github.com/modelscope/evalscope/pull/1364
* fix(agent/sandbox): fail-fast in EnclaveAgentEnvironment when ms_enclave is missing by @Yunnglin in https://github.com/modelscope/evalscope/pull/1372
* feat: GAIA benchmark + MCP server support for NativeAgentConfig by @Yunnglin in https://github.com/modelscope/evalscope/pull/1371
* [Benchmark] Add ArxivRollBench by @liangzid in https://github.com/modelscope/evalscope/pull/1365
* fix(perf): round int fields after sla multi-run averaging by @qiumuyang in https://github.com/modelscope/evalscope/pull/1370
* feat(benchmarks): add k2/kimi/minimax vendor verifier benchmarks by @Yunnglin in https://github.com/modelscope/evalscope/pull/1375
* feat(perf): trie agentic trace replay + Turn model + --duration by @Yunnglin in https://github.com/modelscope/evalscope/pull/1374
* feat(benchmarks): add Terminal-Bench v2.1 + upgrade harbor integration by @Yunnglin in https://github.com/modelscope/evalscope/pull/1376
* feat: support API reranker evaluation, fix #1029 by @haoruilee in https://github.com/modelscope/evalscope/pull/1377

## New Contributors
* @liguodongiot made their first contribution in https://github.com/modelscope/evalscope/pull/1348
* @we1sper made their first contribution in https://github.com/modelscope/evalscope/pull/1363
* @Syqinx made their first contribution in https://github.com/modelscope/evalscope/pull/1367
* @liangzid made their first contribution in https://github.com/modelscope/evalscope/pull/1365
* @qiumuyang made their first contribution in https://github.com/modelscope/evalscope/pull/1370

**Full Changelog**: https://github.com/modelscope/evalscope/compare/v1.7.1...v1.8.0

## v1.8.1 (2026-06-16)

## 中文版

### 基准测试数据集
- 语音评测: 新增 Seed-TTS-Eval 基准测试
- Agent 与工具调用评测: 新增 ACEBench 基准测试
- OCR 评测: 新增 Maritime-OCR-Bench 基准测试
- 图像描述评测: 新增 Caption benchmarks 支持

### 功能增强
- RAG 评测: 重构 RAG Eval，支持 MTEB 2.x、RAGAS 0.4.x，并引入 Pydantic 配置
- SWE-Bench: 支持为 SWE-Bench 镜像配置自定义 DockerHub namespace
- 图像质量评测: 新增全参考图像质量指标

### 问题修复
- 修复 SciCode 中 assistant text blocks 读取问题
- 修复 Terminal-Bench 在 trials 前未检查 Docker CLI 的问题
- 修复多轮对话中 `reasoning_content` 未作为顶层字段透传的问题
- 修复 `service` optional-dependencies 中缺少 perf 依赖的问题
- 修复 RAG API encoder/reranker 中超过 `max_seq_length` 的文本截断问题
- 修复 agent bash 工具 stdout 空白字符保留问题，避免 patch 内容损坏
- 修复 Windows 环境下缓存写入可能触发 `PermissionError` 的问题

---

## English Version

### Benchmark Datasets
- Speech Evaluation: Added Seed-TTS-Eval benchmark
- Agent and Tool-Use Evaluation: Added ACEBench benchmark
- OCR Evaluation: Added Maritime-OCR-Bench benchmark
- Image Captioning Evaluation: Added Caption benchmarks support

### Feature Enhancements
- RAG Evaluation: Refactored RAG Eval with MTEB 2.x, RAGAS 0.4.x, and Pydantic configs
- SWE-Bench: Added support for custom DockerHub namespace for SWE-Bench images
- Image Quality Evaluation: Added full-reference image quality metrics

### Bug Fixes
- Fixed SciCode assistant text block parsing
- Fixed Terminal-Bench Docker CLI check before trials
- Fixed forwarding `reasoning_content` as a top-level field in multi-turn conversations
- Fixed missing perf dependencies in `service` optional-dependencies
- Fixed truncation for texts exceeding `max_seq_length` in RAG API encoder/reranker
- Fixed stdout whitespace preservation in agent bash tool to prevent patch corruption
- Fixed possible Windows `PermissionError` when writing cache files

## What's Changed
* fix(scicode): read assistant text blocks by @he-yufeng in https://github.com/modelscope/evalscope/pull/1381
* add seed_tts_eval benchmark, solve #1360  by @haoruilee in https://github.com/modelscope/evalscope/pull/1379
* feat(benchmarks): add ACEBench support, fix #1025 by @haoruilee in https://github.com/modelscope/evalscope/pull/1386
* fix(terminal_bench): check docker cli before trials by @Li-Bailiang in https://github.com/modelscope/evalscope/pull/1389
* refactor(rag_eval): MTEB 2.x + RAGAS 0.4.x + Pydantic configs by @Yunnglin in https://github.com/modelscope/evalscope/pull/1383
* add Maritime-OCR-Bench support by @K-zhy in https://github.com/modelscope/evalscope/pull/1388
* fix(models): forward reasoning_content as top-level field in multi-turn by @Yunnglin in https://github.com/modelscope/evalscope/pull/1396
* fix: include perf deps in `service` optional-dependencies by @Blackteaxx in https://github.com/modelscope/evalscope/pull/1398
* Add caption benchmarks by @haoruilee in https://github.com/modelscope/evalscope/pull/1402
* fix(rag): truncate texts exceeding max_seq_length in API encoder/reranker by @Yunnglin in https://github.com/modelscope/evalscope/pull/1407
* fix(agent): preserve stdout whitespace in bash tool to prevent patch corruption by @Yunnglin in https://github.com/modelscope/evalscope/pull/1409
* fix(cache): use persistent jsonl writer to avoid Windows PermissionError by @Yunnglin in https://github.com/modelscope/evalscope/pull/1410
* feat: allow custom DockerHub namespace for SWE-Bench images by @Yunnglin in https://github.com/modelscope/evalscope/pull/1417
* feat(metric): add full-reference image quality metrics by @haoruilee in https://github.com/modelscope/evalscope/pull/1412

## New Contributors
* @he-yufeng made their first contribution in https://github.com/modelscope/evalscope/pull/1381
* @Li-Bailiang made their first contribution in https://github.com/modelscope/evalscope/pull/1389
* @Blackteaxx made their first contribution in https://github.com/modelscope/evalscope/pull/1398

**Full Changelog**: https://github.com/modelscope/evalscope/compare/v1.8.0...v1.8.1

## v1.9.0 (2026-07-07)


## 中文版

### 基准测试数据集
- 长上下文与记忆评测: 新增 LongMemEval、LoCoMo QA 等长上下文记忆类基准测试
- Agent 与代码评测: 新增 BrowseComp、SWE-bench Multilingual agentic、BigCodeBench、BigCodeBench-Hard、GDPval、MCP-Atlas、SkillsBench、DeepSWE 等 Agent、代码和工具使用能力评测
- 多模态评测: 新增 ERQA、WorldVQA、CharXiv、BabyVision、EmbSpatial-Bench、MeasureBench 等多模态基准测试
- 数学与推理评测: 新增 arxivmath、cmath、hmmt26、imo_answerbench、AGIEval、ARC-AGI-2、KINA 等数学和通用推理基准测试
- 办公与文档评测: 新增 OfficeQA 办公场景问答评测

### 功能增强
- Agent Runner: 新增 OpenCode 和 OpenHands runner，并提供对应 Dockerfile 支持
- SkillsBench: 新增原生 SkillsBench runner 支持
- Agent API: 将 `run_agent_loop` 移动到 `evalscope.api.agent`，作为公开 API 使用
- 适配器架构: 重构 benchmark adapter 架构，新增 `AudioLanguageAdapter`、统一 `FunctionCallAdapter`，并合并 `AgentLoopAdapter`
- 性能测试: 支持 CPU 密集型请求生成并行化，提升 perf 请求构造效率
- 性能测试数据加载: 统一通过 `--data-source` 参数加载 perf 数据源，简化多数据集配置

### 文档优化
- 新增和更新多个 benchmark 文档、supported dataset 列表、Agent 使用文档和 SkillsBench 第三方文档
- 更新性能测试相关参数文档和多轮压测说明
- 更新 ThinkEval 相关最佳实践文档

### 问题修复
- 修复 SWE-bench 架构选择问题和 sandbox 登录 shell 执行问题
- 修复 ASR 评测中 filters 未在 WER 评分前生效的问题
- 修复 perf 在 OpenAI usage 缺少 `completion_tokens` 时的兼容性问题
- 修复 perf 多轮压测绝对时间速率调度和 event loop 关闭问题
- 修复 LiveCodeBench stdin buffer 支持问题
- 修复 ThinkBench 对新 `ReviewResult` 格式的适配问题
- 修复 GPQA answer choices 被括号清理正则错误截断的问题
- 修复 OpenAI-compatible streaming 聚合问题
- 修复 tau3_bench 在 completion usage 缺失时崩溃的问题

---

## English Version

### Benchmark Datasets
- Long-context and Memory Evaluation: Added LongMemEval, LoCoMo QA and other long-context memory benchmarks
- Agent and Code Evaluation: Added BrowseComp, SWE-bench Multilingual agentic, BigCodeBench, BigCodeBench-Hard, GDPval, MCP-Atlas, SkillsBench, DeepSWE and other agent, coding, and tool-use benchmarks
- Multimodal Evaluation: Added ERQA, WorldVQA, CharXiv, BabyVision, EmbSpatial-Bench, MeasureBench and other multimodal benchmarks
- Math and Reasoning Evaluation: Added arxivmath, cmath, hmmt26, imo_answerbench, AGIEval, ARC-AGI-2, KINA and other math and reasoning benchmarks
- Office and Document Evaluation: Added OfficeQA for office-scenario question answering

### Feature Enhancements
- Agent Runners: Added OpenCode and OpenHands runners with Dockerfile support
- SkillsBench: Added native SkillsBench runner support
- Agent API: Moved `run_agent_loop` to `evalscope.api.agent` as a public API
- Adapter Architecture: Refactored benchmark adapter architecture with `AudioLanguageAdapter`, unified `FunctionCallAdapter`, and merged `AgentLoopAdapter`
- Performance Testing: Parallelized CPU-bound request generation to improve perf workload preparation
- Performance Data Loading: Unified perf dataset loading through the `--data-source` parameter for simpler dataset configuration

### Documentation
- Added and updated benchmark documentation, supported dataset lists, Agent user guides, and SkillsBench third-party documentation
- Updated performance testing parameter documentation and multi-turn stress testing guides
- Updated ThinkEval best practice documentation

### Bug Fixes
- Fixed SWE-bench architecture selection and login shell execution in sandboxes
- Fixed ASR filters so they are applied before WER scoring
- Fixed compatibility when OpenAI usage blocks are missing `completion_tokens`
- Fixed absolute-time rate scheduling and event loop closing for multi-turn perf tests
- Fixed stdin buffer support in LiveCodeBench
- Fixed ThinkBench compatibility with the new `ReviewResult` format
- Fixed GPQA answer choice corruption caused by bracket-stripping regex
- Fixed OpenAI-compatible streaming aggregation
- Fixed tau3_bench crash when completion usage is missing

## What's Changed
* fix SWE-bench architecture selection by @Yunnglin in https://github.com/modelscope/evalscope/pull/1419
* Add LongMemEval benchmark by @Yunnglin in https://github.com/modelscope/evalscope/pull/1420
* Add LoCoMo QA benchmark by @Yunnglin in https://github.com/modelscope/evalscope/pull/1422
* Add BrowseComp benchmark support by @haoruilee in https://github.com/modelscope/evalscope/pull/1421
* Add SWE-bench Multilingual agentic benchmark by @Yunnglin in https://github.com/modelscope/evalscope/pull/1426
* feat: add BigCodeBench and BigCodeBench-Hard benchmark support by @Yunnglin in https://github.com/modelscope/evalscope/pull/1425
* refactor: move run_agent_loop to evalscope.api.agent as public API by @Yunnglin in https://github.com/modelscope/evalscope/pull/1427
* refactor: restructure adapter architecture - AudioLanguageAdapter, FunctionCallAdapter, merge AgentLoopAdapter by @Yunnglin in https://github.com/modelscope/evalscope/pull/1428
* Fix ASR filters before WER scoring by @haoruilee in https://github.com/modelscope/evalscope/pull/1431
* fix(perf): tolerate missing completion_tokens in OpenAI usage block by @angelynaye in https://github.com/modelscope/evalscope/pull/1432
* feat(agent): add OpenCode and OpenHands runners with Dockerfiles by @Yunnglin in https://github.com/modelscope/evalscope/pull/1429
* fix: support stdin buffer in LiveCodeBench by @Yunnglin in https://github.com/modelscope/evalscope/pull/1438
* fix: adapt thinkbench to new ReviewResult format by @Yunnglin in https://github.com/modelscope/evalscope/pull/1439
* fix(perf): absolute-time rate scheduling for multi-turn + close event loop by @Yunnglin in https://github.com/modelscope/evalscope/pull/1442
* Add GDPval benchmark integration by @Yunnglin in https://github.com/modelscope/evalscope/pull/1441
* (feat) Parallelize CPU-bound perf request generation by @haoruilee in https://github.com/modelscope/evalscope/pull/1440
* fix(gpqa): remove bracket-stripping regex that corrupts answer choices by @Yunnglin in https://github.com/modelscope/evalscope/pull/1448
* Add MCP-Atlas benchmark integration by @Yunnglin in https://github.com/modelscope/evalscope/pull/1445
* feat(perf): unify dataset loading with --data-source parameter by @Yunnglin in https://github.com/modelscope/evalscope/pull/1449
* feat: add ERQA and WorldVQA benchmarks by @Yunnglin in https://github.com/modelscope/evalscope/pull/1453
* Fix OpenAI-compatible streaming aggregation by @kaede316 in https://github.com/modelscope/evalscope/pull/1450
* feat(benchmarks): add CharXiv and BabyVision benchmarks by @Yunnglin in https://github.com/modelscope/evalscope/pull/1454
* feat(benchmarks): add arxivmath, cmath, hmmt26 and imo_answerbench benchmarks by @Yunnglin in https://github.com/modelscope/evalscope/pull/1455
* feat(benchmarks): add officeqa, agieval, arc_agi_2 benchmarks by @Yunnglin in https://github.com/modelscope/evalscope/pull/1458
* fix(agent): use login shell for SWE-bench sandboxes by @haoruilee in https://github.com/modelscope/evalscope/pull/1457
* feat(benchmark): add DeepSWE adapter by @Yunnglin in https://github.com/modelscope/evalscope/pull/1459
* feat(benchmarks): add EmbSpatial-Bench, KINA, and MeasureBench benchmarks by @Yunnglin in https://github.com/modelscope/evalscope/pull/1460
* Fix tau3_bench crash when completion usage is missing by @danielliu99 in https://github.com/modelscope/evalscope/pull/1462
* Add native SkillsBench runner support by @Yunnglin in https://github.com/modelscope/evalscope/pull/1451

## New Contributors
* @angelynaye made their first contribution in https://github.com/modelscope/evalscope/pull/1432
* @kaede316 made their first contribution in https://github.com/modelscope/evalscope/pull/1450
* @danielliu99 made their first contribution in https://github.com/modelscope/evalscope/pull/1462

**Full Changelog**: https://github.com/modelscope/evalscope/compare/v1.8.1...v1.9.0

## v1.9.1 (2026-07-21)

## 中文版

### 基准测试数据集
- 智能体评测: 新增 Claw-Eval (#1487)、ResearchRubrics (#1478)、Toolathlon 智能体基准测试
- 多模态评测: 新增 TVBench 视频理解基准测试 (#1471)
- 通用评测: 新增 WideSearch、PerspectiveGap (#1461) 基准测试

### 功能增强
- 性能测试: 新增 workload_trace 数据集插件，支持生产流量回放 (#1494)
- 性能测试: 统一 `--dataset-args` 参数，支持固定长度输入 (#1483, #1495)
- 性能测试: 新增 `/v1/rerank` endpoint 支持 (#1498)
- Web 服务: Dashboard 新增性能测试归档(archive)功能 (#1484)
- 模型支持: 支持 Anthropic prompt caching (#1444)
- 安全增强: 使用 SecretStr 对 eval / perf 密钥进行脱敏 (#1490)
- 性能优化: 重构 benchmark 数据集加载逻辑 (#1482)；优化 config 与 CLI 冷启动导入 (#1491)
- 前端优化: 加固前端工作流与报告生成 (#1492)

### 问题修复
- 修复 evaluator 样本总数日志，并对 per-subset `--limit` 给出警告 (#1497)
- 修复 Windows 下代码执行评分问题 (#1488)
- 修复 `line_by_line` 数据集 dict body 字段处理 (#1485)
- 修复多行 SSE 格式(id/event/data)解析问题 (#1474)
- 修复 trivia_qa prompt 及 repeats 格式化问题 (#1476)
- 修复 agent 沙箱命令超时未终止问题
- 修复 swe-bench 沙箱环境变量传递问题 (#1470)
- 修复 bfcl OpenAI base URL 归一化问题 (#1468)
- 修复 scicode 依赖，锁定 scipy < 1.14 (#1467)
- 修复 openai 流式响应中断重试问题 (#1464)
- 修复 openai 流式 TTFT 未包含 delta.reasoning 的问题 (#1463)
- 修复 sandbox manager stop 失败后的资源清理问题 (#1465)

---

## English Version

### Benchmark Datasets
- Agent Evaluation: Added Claw-Eval (#1487), ResearchRubrics (#1478), and Toolathlon agent benchmarks
- Multimodal Evaluation: Added TVBench video understanding benchmark (#1471)
- General Evaluation: Added WideSearch and PerspectiveGap (#1461) benchmarks

### Feature Enhancements
- Performance Testing: Added workload_trace dataset plugin for production traffic replay (#1494)
- Performance Testing: Unified `--dataset-args` with fixed-length input support (#1483, #1495)
- Performance Testing: Added `/v1/rerank` endpoint support (#1498)
- Web Service: Added performance benchmark archive to the dashboard (#1484)
- Model Support: Added Anthropic prompt caching support (#1444)
- Security: Masked eval / perf secrets with SecretStr (#1490)
- Performance: Refactored benchmark dataset loading (#1482); refined config and CLI cold-start imports (#1491)
- Frontend: Hardened frontend workflows and reporting (#1492)

### Bug Fixes
- Fixed resolved sample total logging and added warning for per-subset `--limit` (#1497)
- Fixed code execution scoring on Windows (#1488)
- Fixed dict body field handling in line_by_line dataset (#1485)
- Fixed multi-line SSE parsing with id, event, and data fields (#1474)
- Fixed trivia_qa prompt and repeats formatting (#1476)
- Fixed agent sandbox commands not terminating on timeout
- Fixed sandbox environment variable passing for swe-bench (#1470)
- Fixed OpenAI base URL normalization for bfcl (#1468)
- Fixed scicode dependency by pinning scipy below 1.14 (#1467)
- Fixed retry on interrupted OpenAI streaming responses (#1464)
- Fixed missing delta.reasoning in OpenAI streaming TTFT (#1463)
- Fixed resource cleanup after sandbox manager stop failure (#1465)


## v1.10.0 (2026-08-04)

## 中文版

### 基准测试数据集
- Agent 与自动化评测：新增 AutomationBench、DeepSearchQA、JobBench、BrowserGym MiniWoB 等评测能力
- 文档理解评测：新增 OmniDocBench v1.6 评测，并修复 OCR 相关兼容性

### 功能增强
- 性能测试：支持通过 `prefix_file` / `prefix_role` 注入长上下文前缀；补充百分位统计最小值和平均延迟指标
- Web 界面：性能列表新增 I/O token 列，支持删除历史记录

### 文档优化
- 修正中文文档中的拼写和语法问题

### 问题修复
- 修复 IFBench 下载错误的 NLTK English tagger 问题
- 修复数学解析器中未保存 `str.replace()` 返回值的问题
- 修复 CMMLU few-shot 加载、ARC 答案格式、Windows UTF-8 文件读写等兼容性问题
- 修复异步事件循环和任务生命周期、Anthropic tool-call ID、每 subset 浮点数 limit 等问题
- 修复性能测试的调度截止、无固定速率 HTML 报告、非流式 TTFT/TPOT/ITL 指标和缓存 token 同步问题

---

## English Version

### Benchmark Datasets
- Agent and automation evaluation: Added AutomationBench, DeepSearchQA, JobBench, BrowserGym MiniWoB, and related capabilities
- Document understanding evaluation: Added OmniDocBench v1.6 and fixed OCR compatibility

### Feature Enhancements
- Performance testing: Added long-context prefix injection with `prefix_file` / `prefix_role`, plus minimum percentile and average latency metrics
- Web UI: Added I/O token columns to performance lists and history-record deletion

### Documentation
- Corrected spelling and grammar in Chinese documentation

### Bug Fixes
- Fixed IFBench downloading the incorrect NLTK English tagger
- Fixed math parsing where the result of `str.replace()` was discarded
- Fixed CMMLU few-shot loading, ARC answer formatting, and Windows UTF-8 file I/O compatibility
- Fixed async event-loop and task lifecycle handling, Anthropic tool-call IDs, and per-subset float limits
- Fixed perf scheduling deadlines, HTML reports for no-fixed-rate runs, non-stream TTFT/TPOT/ITL metrics, and cached-token synchronization

## What's Changed
- fix(ifbench): download correct NLTK English tagger by @git-jxj in https://github.com/modelscope/evalscope/pull/1539
- fix: assign result of str.replace() in math parser by @LeoYueDev in https://github.com/modelscope/evalscope/pull/1536
- Fix OCR benchmark compatibility and add OmniDocBench v1.6 evaluation by @Yunnglin in https://github.com/modelscope/evalscope/pull/1535
- Fix CMMLU few-shot loading by @Yunnglin in https://github.com/modelscope/evalscope/pull/1534
- fix(docs): correct typos and grammar errors in Chinese documentation by @LeoYueDev in https://github.com/modelscope/evalscope/pull/1532
- feat(perf): long-context prefix injection via prefix_file/prefix_role by @Yunnglin in https://github.com/modelscope/evalscope/pull/1531
- feat: add direct BrowserGym MiniWoB evaluation by @Yunnglin in https://github.com/modelscope/evalscope/pull/1530
- fix: per-subset float limit and Anthropic tool call id sanitization by @Yunnglin in https://github.com/modelscope/evalscope/pull/1528
- feat(web): I/O token column for perf list and history record deletion by @Yunnglin in https://github.com/modelscope/evalscope/pull/1526
- fix: add encoding='utf-8' to remaining core file read/write for Windows compatibility by @Yunnglin in https://github.com/modelscope/evalscope/pull/1522
- fix: performance test progress and cancellation handling, plus tokenizer path support by @duxingx1a in https://github.com/modelscope/evalscope/pull/1520
- feat(perf): add min row to percentile table and label avg latency metrics by @Yunnglin in https://github.com/modelscope/evalscope/pull/1517
- fix: normalise ARC answerKey digits to letters in arc_adapter by @duxingx1a in https://github.com/modelscope/evalscope/pull/1516
- fix: add encoding='utf-8' to yaml_to_dict for Windows compatibility by @duxingx1a in https://github.com/modelscope/evalscope/pull/1515
- fix(web): accept completed invoke status by @afox666 in https://github.com/modelscope/evalscope/pull/1510
- Add JobBench benchmark by @Yunnglin in https://github.com/modelscope/evalscope/pull/1509
- fix(perf): sync server-reported cached_tokens for single-turn runs by @Yunnglin in https://github.com/modelscope/evalscope/pull/1508
- Fix async event loop and task lifecycle by @Yunnglin in https://github.com/modelscope/evalscope/pull/1507
- Add AutomationBench benchmark by @Yunnglin in https://github.com/modelscope/evalscope/pull/1505
- fix(perf): generate HTML report for open-loop runs with no fixed rate by @qiumuyang in https://github.com/modelscope/evalscope/pull/1503
- Add DeepSearchQA benchmark by @Yunnglin in https://github.com/modelscope/evalscope/pull/1502
- fix(perf): stop open-loop dispatch at duration deadline by @YingchaoX in https://github.com/modelscope/evalscope/pull/1501
- fix(perf): exclude non-stream requests from TTFT/TPOT/ITL metrics by @qiumuyang in https://github.com/modelscope/evalscope/pull/1499


## v1.11.0 (2026-08-24)

## 中文版

### 基准测试数据集

- 多模态评测：新增 PerceptionBench、ScreenSpot-Pro、PMC-VQA、LogicVista、CC-OCR-V2、SLAKE、olmOCR-Bench、CountQA 等视觉、多模态与文档理解基准。
- 推理与专业能力评测：新增 HiPhO 高中物理奥赛、PhyX 物理推理（选择题与开放题）、PLawBench 法律实践能力评测。
- 多语言评测：新增 Milu、ARC-Indic、GSM8K-Indic、IndicBoolQ、TriviaQA-Indic、IndicPara、Sanskriti、Hindi HellaSwag，以及 BhashaBench / BhashaBench-Multi 的金融、法律、农业和阿育吠陀子集。

### 功能增强

- 评测版本管理：新增原生评测版本与缓存身份校验，并支持确定性的选择题选项打乱，避免语义变更后复用不兼容缓存。
- Judge 评测：统一 LLM Judge 的 JSON 输出契约；格式不合法或 `[ERROR]` 回复将从指标统计中排除。
- 自定义数据集：`general_vmcq` 统一支持图片、视频、音频输入，并支持 Parquet 和二进制媒体字段；`general_vqa` 新增媒体占位符支持。
- 指标与报告：统一指标语义和评测报告展示，优化 Agent Trace 的步骤分组及工具调用与结果关联。
- 服务与 Web：评测界面支持 Sandbox 配置；优化报告列表元数据读取和条件请求。

### 文档优化

- 更新文本生成图像任务的指标选择说明。
- 修复 API 消息、工具调用和 Tau-bench `pass^k` 等文档说明问题。

### 问题修复

- 修复 IFBench NLTK 英文词性标注模型下载、ACEBench 官方评分协议对齐、IFEval 与 GPQA 结果可复现性等问题。
- 修复多选题括号答案和多答案场景下的标签提取问题。
- 修复 TaskConfig 未知字段被静默忽略的问题，提供相近字段建议；同时修复 `reasoning_effort` 参数透传。
- 修复 CMMMU 等视觉基准的媒体输入归一化、OmniDocBench 重复加载、VQA 信息读取等问题。
- 修复终端评测非法 reward 与未完成运行的结果报告问题，以及 BFCL 空工具调用丢失问题。
- 修复性能测试中的流式 usage 统计、空 content、请求构建失败、缺失 chat template 和插件返回空数据集等问题。
- 修复 Web 报告中的本地媒体渲染、空 `reasoning_tokens` 与后端空值处理问题。

---

## English Version

### Benchmark Datasets

- Multimodal Evaluation: Added PerceptionBench, ScreenSpot-Pro, PMC-VQA, LogicVista, CC-OCR-V2, SLAKE, olmOCR-Bench, CountQA, and other vision, multimodal, and document-understanding benchmarks.
- Reasoning and Domain Evaluation: Added HiPhO for high-school physics Olympiad problems, PhyX for multiple-choice and open-ended physical reasoning, and PLawBench for legal practice evaluation.
- Multilingual Evaluation: Added Milu, ARC-Indic, GSM8K-Indic, IndicBoolQ, TriviaQA-Indic, IndicPara, Sanskriti, Hindi HellaSwag, and BhashaBench / BhashaBench-Multi finance, legal, agriculture, and Ayurveda subsets.

### Feature Enhancements

- Evaluation Versioning: Added native evaluation versioning, cache identity checks, and deterministic choice shuffling to prevent incompatible cached predictions from being reused.
- Judge Evaluation: Unified LLM-judge JSON output contracts; malformed and `[ERROR]` responses are excluded from metric aggregation.
- Custom Datasets: Unified image, video, and audio inputs in `general_vmcq`, with Parquet and binary media-field support; added media placeholders to `general_vqa`.
- Metrics and Reports: Unified metric semantics and evaluation reports, with improved Agent Trace step grouping and tool-call/result linking.
- Service and Web: Added Sandbox configuration to the evaluation UI and improved report-list metadata retrieval with conditional requests.

### Documentation

- Clarified metric selection for text-to-image tasks.
- Fixed documentation issues for API messages, tool calls, and Tau-bench `pass^k`.

### Bug Fixes

- Fixed IFBench NLTK English tagger downloads, ACEBench official-protocol alignment, and reproducibility issues in IFEval and GPQA.
- Fixed answer-label extraction for bracketed and multiple-choice responses.
- Fixed silently ignored unknown TaskConfig keys with close-match suggestions, and fixed `reasoning_effort` parameter forwarding.
- Fixed media-input normalization across CMMMU and other vision benchmarks, repeated OmniDocBench loading, and VQA information handling.
- Fixed invalid-reward and incomplete-run reporting for terminal benchmarks, and BFCL empty tool-call handling.
- Fixed streaming usage accounting, empty content, request-building failures, missing chat templates, and empty plugin datasets in performance testing.
- Fixed local media rendering, null `reasoning_tokens`, and backend null handling in Web reports.

## What's Changed
* fix(ifbench): download correct NLTK English tagger by @git-jxj in https://github.com/modelscope/evalscope/pull/1539
* fix(acebench): align with the official protocol and fix milestone scoring by @Yunnglin in https://github.com/modelscope/evalscope/pull/1544
* fix: multi-choice answer extraction, ifeval determinism, LiveCodeBench system prompt, tau-bench pass^k docs by @Yunnglin in https://github.com/modelscope/evalscope/pull/1549
* feat(perception_bench): add PerceptionBench atomic visual perception benchmark by @Yunnglin in https://github.com/modelscope/evalscope/pull/1551
* feat(screenspot_pro): add ScreenSpot-Pro GUI grounding benchmark by @Yunnglin in https://github.com/modelscope/evalscope/pull/1550
* feat(plawbench): add PLawBench rubric-based legal practice benchmark by @Yunnglin in https://github.com/modelscope/evalscope/pull/1553
* feat(pmc_vqa): add PMC-VQA medical visual question answering benchmark by @Yunnglin in https://github.com/modelscope/evalscope/pull/1557
* feat(hipho): add HiPhO high school physics Olympiad benchmark by @Yunnglin in https://github.com/modelscope/evalscope/pull/1558
* fix(config): pass reasoning_effort through instead of whitelisting it by @Yunnglin in https://github.com/modelscope/evalscope/pull/1561
* fix(multi_choices): parse answer labels the model wrapped in brackets by @Yunnglin in https://github.com/modelscope/evalscope/pull/1560
* feat(logic_vista): add LogicVista visual logical reasoning benchmark by @Yunnglin in https://github.com/modelscope/evalscope/pull/1556
* fix(web): render local-path media in both dashboard chains by @Yunnglin in https://github.com/modelscope/evalscope/pull/1562
* feat(cc_ocr_v2): add CC-OCR-V2 real-world document OCR benchmark by @Yunnglin in https://github.com/modelscope/evalscope/pull/1559
* feat(web): add sandbox configuration to evaluation UI by @Dhru1001 in https://github.com/modelscope/evalscope/pull/1545
* fix: validate service output directory by @heliubj18 in https://github.com/modelscope/evalscope/pull/1554
* fix(perf): explain how to proceed when a tokenizer has no chat template by @Yunnglin in https://github.com/modelscope/evalscope/pull/1564
* Fix async loop shutdown timeout cascade by @Yunnglin in https://github.com/modelscope/evalscope/pull/1566
* fix(web): allow null reasoning_tokens in report content blocks by @Dhru1001 in https://github.com/modelscope/evalscope/pull/1563
* fix(web): normalize backend null to undefined at the API validation boundary by @Yunnglin in https://github.com/modelscope/evalscope/pull/1567
* feat(metrics): unify metric semantics and evaluation reporting by @Yunnglin in https://github.com/modelscope/evalscope/pull/1552
* refactor(web): isolate agent trace grouping from rendering by @Yunnglin in https://github.com/modelscope/evalscope/pull/1568
* fix(perf): surface fatal request-building errors instead of swallowing or retrying them by @Yunnglin in https://github.com/modelscope/evalscope/pull/1571
* fix(perf tests): repair stale local-endpoint perf tests (hang + outdated return contract) by @Yunnglin in https://github.com/modelscope/evalscope/pull/1573
* fix(perf): abort request generation when a plugin returns None for the whole dataset by @Yunnglin in https://github.com/modelscope/evalscope/pull/1574
* fix(perf): parse streaming usage independently of choices to fix 0 ca… by @OctoberGitHub in https://github.com/modelscope/evalscope/pull/1572
* fix(judge): fail closed on [ERROR] judge responses and surface silent extraction paths by @YuhaoLin2005 in https://github.com/modelscope/evalscope/pull/1576
* fix(gpqa): seed choice shuffle from the question so rerun-review is reproducible by @Yunnglin in https://github.com/modelscope/evalscope/pull/1583
* fix(agent): limit SWE-bench toolcall nudge to once by @Roovelrz in https://github.com/modelscope/evalscope/pull/1581
* feat(io): support `parquet` and binary image features in `general_vmcq` by @Moenupa in https://github.com/modelscope/evalscope/pull/1584
* fix(agent): make AgentLoop own the nudge count and give models an honest reminder by @Yunnglin in https://github.com/modelscope/evalscope/pull/1585
* fix: enforce strict judge output parsing by @atirna in https://github.com/modelscope/evalscope/pull/1588
* feat(benchmark): add CountQA object counting benchmark by @Yunnglin in https://github.com/modelscope/evalscope/pull/1590
* fix: correct self.dataset typo in VQA.info by @Ricardo-M-L in https://github.com/modelscope/evalscope/pull/1589
* feat(benchmark): add PhyX physical reasoning benchmark (phyx_mc, phyx_oe) by @Yunnglin in https://github.com/modelscope/evalscope/pull/1593
* feat(benchmark): add SLAKE bilingual medical VQA benchmark by @Yunnglin in https://github.com/modelscope/evalscope/pull/1592
* fix(perf): guard None content in openai_api token accounting by @tianba-sh in https://github.com/modelscope/evalscope/pull/1591
* fix(bfcl): patch bfcl_eval FC handler to stop dropping empty-tool_cal… by @Dhru1001 in https://github.com/modelscope/evalscope/pull/1596
* fix(multi-choice): parse the last valid answer label instead of the first by @juzihan0459 in https://github.com/modelscope/evalscope/pull/1597
* feat(benchmarks): add native Indic-language benchmark adapters (milu,… by @Dhru1001 in https://github.com/modelscope/evalscope/pull/1569
* docs(api): fix message and tool documentation typos by @BingH225 in https://github.com/modelscope/evalscope/pull/1600
* feat(io): unify loading image/video/audio for `general_vmcq` by @Moenupa in https://github.com/modelscope/evalscope/pull/1595
* feat(benchmark): add olmOCR-Bench document transcription benchmark by @ClaireXi99 in https://github.com/modelscope/evalscope/pull/1598
* perf(service): memoize report-list metadata and support conditional GET by @Yunnglin in https://github.com/modelscope/evalscope/pull/1607
* feat(benchmarks): Add Native Indic Benchmarks Phase 2  by @Dhru1001 in https://github.com/modelscope/evalscope/pull/1603
* refactor(judge): unify LLM judge scoring on a single JSON output contract by @Yunnglin in https://github.com/modelscope/evalscope/pull/1601
* docs: clarify text-to-image metric selection by @MrChenfafafa in https://github.com/modelscope/evalscope/pull/1612
* feat(eval): add native evaluation versioning and deterministic choices by @Yunnglin in https://github.com/modelscope/evalscope/pull/1615
* fix(terminal_bench): reject invalid trial rewards by @Excelius-Wang in https://github.com/modelscope/evalscope/pull/1610
* fix(eval): report incomplete terminal-bench runs by @Yunnglin in https://github.com/modelscope/evalscope/pull/1616
* feat(io): support media placeholders in `general_vqa` by @Moenupa in https://github.com/modelscope/evalscope/pull/1609
* fix(cmmmu): normalize image media inputs by @Excelius-Wang in https://github.com/modelscope/evalscope/pull/1618
* fix(benchmark): normalize remaining vision media by @Yunnglin in https://github.com/modelscope/evalscope/pull/1623
* fix(config): reject unknown task-config keys and consolidate deprecation/serialization by @Yunnglin in https://github.com/modelscope/evalscope/pull/1624
* fix(benchmark): load OmniDocBench v1.6 from snapshot by @Yunnglin in https://github.com/modelscope/evalscope/pull/1625

## New Contributors
* @Dhru1001 made their first contribution in https://github.com/modelscope/evalscope/pull/1545
* @heliubj18 made their first contribution in https://github.com/modelscope/evalscope/pull/1554
* @OctoberGitHub made their first contribution in https://github.com/modelscope/evalscope/pull/1572
* @YuhaoLin2005 made their first contribution in https://github.com/modelscope/evalscope/pull/1576
* @Roovelrz made their first contribution in https://github.com/modelscope/evalscope/pull/1581
* @Moenupa made their first contribution in https://github.com/modelscope/evalscope/pull/1584
* @atirna made their first contribution in https://github.com/modelscope/evalscope/pull/1588
* @Ricardo-M-L made their first contribution in https://github.com/modelscope/evalscope/pull/1589
* @tianba-sh made their first contribution in https://github.com/modelscope/evalscope/pull/1591
* @juzihan0459 made their first contribution in https://github.com/modelscope/evalscope/pull/1597
* @BingH225 made their first contribution in https://github.com/modelscope/evalscope/pull/1600
* @ClaireXi99 made their first contribution in https://github.com/modelscope/evalscope/pull/1598
* @MrChenfafafa made their first contribution in https://github.com/modelscope/evalscope/pull/1612
* @Excelius-Wang made their first contribution in https://github.com/modelscope/evalscope/pull/1610

**Full Changelog**: https://github.com/modelscope/evalscope/compare/v1.10.0...v1.11.0

## v1.11.1 (2026-08-31)


## 中文版

### 基准测试数据集

- 多模态评测：新增 SURDS、VLMs Are Biased、Ref-Adv-s、VisFactor、MedXpertQA、VTCBench 等视觉、多模态与长视频理解基准。
- 推理与专业能力评测：新增 $OneMillion-Bench、PRBench、HMMT-Nov-2025 等 Agent、深度推理与数学评测基准。

### 功能增强

- API 契约：Web API 响应契约改由 Pydantic 模型自动生成，提升前后端类型一致性。
- 缓存与数据集：隔离数据集缓存键，增强视频解码与 `limit` 参数校验。
- 模型服务：支持识别 HTTP 200 响应中的网关错误载荷，并优化音频预处理、流式响应、用量统计与重试行为。
- 性能测试：优化指标精度、关闭流程、闭环 warmup 交接，以及 SSE Unicode 内容处理。

### 文档优化

- 更新 README 与 Dashboard 使用说明。
- 修复 Model API 文档中的过期说明。

### 问题修复

- 修复 ProcessBench 等运行只产生部分指标时的报告异常：主指标不可用将被明确标记，不再错误地替换为辅助分数。
- 修复 General QA 在错误样本下的指标身份保留、指令级指标聚合、答案解析和 ROUGE 评分问题。
- 修复 IFBench 重复评测版本及唯一词约束校验问题。
- 修复 OmniDocBench 空页面指标、VTCBench HTML 标签解析、Toolathlon 任务生命周期与结果校验问题。
- 修复 Judge 延迟初始化并发、NLTK 镜像文件校验、缓存恢复不完整记录等问题。

---

## English Version

### Benchmark Datasets

- Multimodal Evaluation: Added SURDS, VLMs Are Biased, Ref-Adv-s, VisFactor, MedXpertQA, VTCBench, and other vision, multimodal, and long-video benchmarks.
- Reasoning and Domain Evaluation: Added $OneMillion-Bench, PRBench, and HMMT-Nov-2025 for agent, deep-reasoning, and mathematical evaluation.

### Feature Enhancements

- API Contracts: Web API response contracts are now generated from Pydantic models for stronger frontend/backend type consistency.
- Cache and Datasets: Isolated dataset cache keys and improved video decoding and `limit` validation.
- Model Services: Detects gateway-error payloads returned with HTTP 200, and improves audio preprocessing, streaming responses, usage accounting, and retry behavior.
- Performance Testing: Improved metric accuracy, shutdown handling, closed-loop warmup handoff, and Unicode handling in SSE streams.

### Documentation

- Updated README and Dashboard guidance.
- Fixed stale Model API documentation.

### Bug Fixes

- Fixed report failures when ProcessBench and similar runs emit only part of their metrics: unavailable primary metrics are now reported explicitly without substituting an auxiliary score.
- Fixed metric-identity preservation for failed General QA samples, instruction-level aggregation, answer parsing, and ROUGE scoring.
- Fixed duplicate evaluation versions and unique-word validation in IFBench.
- Fixed empty-page metrics in OmniDocBench, HTML tag parsing in VTCBench, and Toolathlon job lifecycle and result validation.
- Fixed concurrent lazy Judge initialization, NLTK mirror archive verification, and incomplete cache-resume records.

## What's Changed
* fix(rag): raise a clear error when a LogitScore reranker loads on an old sentence-transformers by @AmirF194 in https://github.com/modelscope/evalscope/pull/1620
* feat(io): unify undecoding behavior and support overlong images list by @Moenupa in https://github.com/modelscope/evalscope/pull/1626
* cicd(isort): migrate to ruff isort by @Moenupa in https://github.com/modelscope/evalscope/pull/1629
* fix(typing): add type hints to logger by @Moenupa in https://github.com/modelscope/evalscope/pull/1632
* docs: fix stale ModelAPI docstrings (nonexistent api_key_vars / ChatUserMessage) by @BingH225 in https://github.com/modelscope/evalscope/pull/1634
* fix(score): prune rouge scoring function and fix en version of rouge by @Moenupa in https://github.com/modelscope/evalscope/pull/1633
* feat(benchmarks): add hmmt_nov25 benchmark by @haoruilee in https://github.com/modelscope/evalscope/pull/1636
* feat(benchmark): support VTCBench by @Moenupa in https://github.com/modelscope/evalscope/pull/1635
* fix(perf): preserve Unicode line separators in SSE payloads by @Yunnglin in https://github.com/modelscope/evalscope/pull/1642
* fix(benchmark): VTCBench wrongly parsed html tags by @Moenupa in https://github.com/modelscope/evalscope/pull/1643
* test(perf): stop asserting log text in workload_trace tests by @Yunnglin in https://github.com/modelscope/evalscope/pull/1647
* fix(perf): hand closed-loop warmup over without draining the server by @Yunnglin in https://github.com/modelscope/evalscope/pull/1641
* fix(report): sync HTML reports with console theme by @Yunnglin in https://github.com/modelscope/evalscope/pull/1646
* chore: unify linting and formatting with Ruff by @Yunnglin in https://github.com/modelscope/evalscope/pull/1644
* feat: support MedXpertQA benchmark by @Yunnglin in https://github.com/modelscope/evalscope/pull/1655
* fix(web): derive API contracts from Pydantic by @Yunnglin in https://github.com/modelscope/evalscope/pull/1658
* feat(benchmarks): add PRBench by @Yunnglin in https://github.com/modelscope/evalscope/pull/1665
* feat: add OneMillion-Bench benchmark by @Yunnglin in https://github.com/modelscope/evalscope/pull/1667
* fix(benchmark): restore F821 and fix jobbench mis-ignored linting issue by @Moenupa in https://github.com/modelscope/evalscope/pull/1652
* feat: add VisFactor benchmark by @Yunnglin in https://github.com/modelscope/evalscope/pull/1661
* feat(benchmarks): add Ref-Adv-s by @Yunnglin in https://github.com/modelscope/evalscope/pull/1668
* feat(benchmarks): add VLMs Are Biased by @Yunnglin in https://github.com/modelscope/evalscope/pull/1669
* fix(metrics): correct answer parsing and text scoring by @git-jxj in https://github.com/modelscope/evalscope/pull/1649
* fix(models): correct retry semantics and Anthropic streaming by @git-jxj in https://github.com/modelscope/evalscope/pull/1651
* fix(models): correct cache, usage, streaming, and image outputs by @git-jxj in https://github.com/modelscope/evalscope/pull/1653
* fix(perf): improve metric accuracy, validation, and shutdown by @git-jxj in https://github.com/modelscope/evalscope/pull/1654
* feat(benchmarks): add SURDS by @Yunnglin in https://github.com/modelscope/evalscope/pull/1670
* fix(judge): serialize lazy judge initialization by @git-jxj in https://github.com/modelscope/evalscope/pull/1664
* fix(models): avoid blocking event loop during async audio preprocessing by @git-jxj in https://github.com/modelscope/evalscope/pull/1662
* fix(resources): verify NLTK mirror archives with pinned digests by @git-jxj in https://github.com/modelscope/evalscope/pull/1663
* fix(cache): deduplicate review state and tolerate torn resume rows by @git-jxj in https://github.com/modelscope/evalscope/pull/1657
* fix(benchmark): handle empty OmniDocBench page metrics by @git-jxj in https://github.com/modelscope/evalscope/pull/1666
* refactor(models): move litellm imports to module level by @seroze in https://github.com/modelscope/evalscope/pull/1678
* fix(metrics): make inst_level_* a micro-average over instructions by @arkrolin in https://github.com/modelscope/evalscope/pull/1672
* fix(ifbench): enforce unique words in sentence checker by @linhongyu510 in https://github.com/modelscope/evalscope/pull/1676
* fix(ifbench): remove duplicate evaluation version by @Excelius-Wang in https://github.com/modelscope/evalscope/pull/1681
* fix(perf): ignore metadata-only chunks in TTFT and ITL by @Excelius-Wang in https://github.com/modelscope/evalscope/pull/1645
* fix(benchmark): harden Toolathlon job lifecycle and result validation by @git-jxj in https://github.com/modelscope/evalscope/pull/1656
* fix(benchmark): preserve metric identities on General QA/VQA scoring errors by @git-jxj in https://github.com/modelscope/evalscope/pull/1660
* fix(dataset): isolate cache keys, undecode video, and validate limits consistently by @git-jxj in https://github.com/modelscope/evalscope/pull/1659
* fix(models): retry 200 responses that carry a gateway error payload by @seroze in https://github.com/modelscope/evalscope/pull/1673
* refactor(io): remove unused type cast and deduplicate code in media io by @Moenupa in https://github.com/modelscope/evalscope/pull/1683

## New Contributors
* @AmirF194 made their first contribution in https://github.com/modelscope/evalscope/pull/1620
* @seroze made their first contribution in https://github.com/modelscope/evalscope/pull/1678
* @arkrolin made their first contribution in https://github.com/modelscope/evalscope/pull/1672
* @linhongyu510 made their first contribution in https://github.com/modelscope/evalscope/pull/1676

**Full Changelog**: https://github.com/modelscope/evalscope/compare/v1.11.0...v1.11.1

## v1.12.0 (2026-09-16)

## 中文版

### 基准测试数据集

- 语音评测：新增 THCHS-30 国际音标（IPA）音素识别评测，支持 Phone Error Rate（PER）指标。
- 语音评测：LibriSpeech 新增 `test-other` 子集支持。

### 功能增强

- Agent 评测：新增 DeepSeek Harness Bridge Runner，支持通过 OpenAI Chat Completions Bridge 运行 `deepseek-harness`。
- Agent 评测：新增可选的工具调用参数 Schema 校验，帮助区分模型参数生成错误与工具执行错误。
- Agent 基准：Tau3-Bench 支持配置 Agent 最大执行步数 `max_steps`。
- 性能测试：新增基于 AIPerf 的 AgentX 回放场景，支持数据版本校验、运行有效性记录和敏感信息脱敏。
- 性能测试：新增可选 PD 分离式推理指标，包括 Steady ITL、PD Handoff Latency 和 PD Handoff Overhead。
- 性能测试：AgentX 支持 `tokenizer_trust_remote_code` 与 `benchmark_grace_period` 配置。
- Dashboard：报告列表支持按模型展示同一模型的多个报告，保持原始评测报告不变。
- Dashboard：聚合结果表首屏按批次展示，优化大规模模型与基准组合下的页面性能。

### 文档优化

- 更新 Agent Bridge、AgentX 性能测试、Tau3-Bench、评测架构和基准贡献说明。
- 修复基准 smoke evaluation 示例命令，并补充正确的 mock 评测配置。
- 更新产品网站入口及相关使用指引。

### 问题修复

- 修复多参考答案在 inclusion-based 评分中被拼接为单个错误目标的问题，影响 TriviaQA、MMLU-Redux 等评测。
- 修复 Judge 模板渲染、指标异常处理、包含匹配规则及 GeneralArena bootstrap 随机数处理，提升评测结果的正确性与可复现性。
- 修复 GeneralArena 导入历史评测结果时按行错配、将已生成回复带入 Judge 输入的问题；评测版本升级至 `v1.2`。
- 修复 Agent Bridge 丢失模型原始输出、性能指标和推理内容，以及上游生成失败未记录到 Agent Trace 的问题。
- 修复 Agent sandbox stdin 隔离和显式 stdin 传递问题。
- 修复 MCP 初始化错误被隐藏、service worker 无法运行 MCP stdio 客户端的问题。
- 修复空 ASR 转写被错误计为 WER=0 的问题；Seed-TTS-Eval 评测版本升级至 `v1.1`。
- 修复流式推理输出的 TTFT/ITL 统计、多轮 warmup 交接，以及带 token usage 的 Agent Trace 导致 Predictions API 返回 500 的问题。
- 修复 few-shot 配置未在数据加载前校验、CLI `benchmark-info` 导入错误、Dashboard 空分数行模型名异常换行等问题。
- 修复可用模块的导入期异常被误报为缺失依赖的问题，并移除会直接报错的 CLIP Benchmark 模板入口。

---

## English Version

### Benchmark Datasets

- Speech Evaluation: Added THCHS-30 IPA phoneme recognition with Phone Error Rate (PER) support.
- Speech Evaluation: Added the LibriSpeech `test-other` subset.

### Feature Enhancements

- Agent Evaluation: Added the DeepSeek Harness Bridge Runner for running `deepseek-harness` through the OpenAI Chat Completions Bridge.
- Agent Evaluation: Added optional tool-call argument Schema validation to distinguish invalid model arguments from tool execution failures.
- Agent Benchmarks: Added configurable Agent `max_steps` support for Tau3-Bench.
- Performance Testing: Added an AIPerf-based AgentX replay scenario with dataset-version validation, run-validity records, and secret redaction.
- Performance Testing: Added optional PD-disaggregated serving metrics, including Steady ITL, PD Handoff Latency, and PD Handoff Overhead.
- Performance Testing: Added `tokenizer_trust_remote_code` and `benchmark_grace_period` options for AgentX.
- Dashboard: Added display-only grouping of reports from the same model without mutating source evaluation reports.
- Dashboard: Added incremental rendering for aggregated results to improve large-scale dashboard performance.

### Documentation

- Updated documentation for Agent Bridge, AgentX performance testing, Tau3-Bench, evaluation architecture, and benchmark contributions.
- Fixed the benchmark smoke-evaluation example and documented the correct mock-evaluation configuration.
- Updated product website entry points and related guidance.

### Bug Fixes

- Fixed multi-reference answers being flattened into an invalid target in inclusion-based scoring, affecting benchmarks such as TriviaQA and MMLU-Redux.
- Fixed Judge template rendering, metric-failure handling, inclusion matching, and GeneralArena bootstrap RNG behavior for more correct and reproducible evaluation results.
- Fixed mispaired imported reviews and generated responses leaking into Judge inputs in GeneralArena; advanced its evaluation version to `v1.2`.
- Fixed Agent Bridge loss of original model outputs, performance metrics, reasoning content, and upstream generation failures in Agent Traces.
- Fixed Agent sandbox stdin isolation and explicit stdin forwarding.
- Fixed hidden MCP initialization errors and MCP stdio clients failing in service workers.
- Fixed empty ASR transcripts being scored as WER=0; advanced Seed-TTS-Eval to evaluation version `v1.1`.
- Fixed TTFT/ITL timing for streamed reasoning output, multi-turn warmup handoff, and Predictions API 500 errors caused by Agent Traces with token usage.
- Fixed late few-shot configuration validation, CLI `benchmark-info` imports, and model-name wrapping for empty Dashboard score rows.
- Fixed available modules' import-time failures being misreported as missing dependencies, and removed the CLIP Benchmark template entry point that always raised an error.

## What's Changed
* chore: tighten ruff rule baseline by @Yunnglin in https://github.com/modelscope/evalscope/pull/1686
* fix(perf): hand off multi-turn warmup without draining by @Yunnglin in https://github.com/modelscope/evalscope/pull/1684
* fix(clip_benchmark): remove __main__ block that always raises TypeError by @Anai-Guo in https://github.com/modelscope/evalscope/pull/1687
* chore: enforce F401 in evalscope/utils by @Moenupa in https://github.com/modelscope/evalscope/pull/1689
* fix(dep): remove dependency `overrides`; type check instead of runtime by @Moenupa in https://github.com/modelscope/evalscope/pull/1692
* feat(tau3_bench): support configurable max_steps parameter by @ZTJiu in https://github.com/modelscope/evalscope/pull/1690
* docs(agent): point prediction docstrings at the hook that resolves it by @ChenCJ-io in https://github.com/modelscope/evalscope/pull/1696
* fix(web): stop score-matrix model name wrapping character-by-character by @Dhru1001 in https://github.com/modelscope/evalscope/pull/1704
* fix(perf): measure TTFT from reasoning output by @git-jxj in https://github.com/modelscope/evalscope/pull/1700
* fix(bridge): record upstream generate failures on the agent trace by @ChenCJ-io in https://github.com/modelscope/evalscope/pull/1698
* fix(mcp): preserve initialization errors and support service stdio by @git-jxj in https://github.com/modelscope/evalscope/pull/1701
* refactor(metrics): give metric semantics one source per decision by @Yunnglin in https://github.com/modelscope/evalscope/pull/1705
* fix(eval): correct judge rendering, metric scoring, and bootstrap RNG by @git-jxj in https://github.com/modelscope/evalscope/pull/1702
* fix(judge): import canonicalize_producer_identity from its new module by @ChenCJ-io in https://github.com/modelscope/evalscope/pull/1711
* fix(bridge): keep the model output intact on reconstructed assistant messages by @ChenCJ-io in https://github.com/modelscope/evalscope/pull/1710
* fix(benchmark): validate few-shot capabilities by @Yunnglin in https://github.com/modelscope/evalscope/pull/1714
* feat(agent): validate tool-call arguments against the advertised schema by @ChenCJ-io in https://github.com/modelscope/evalscope/pull/1712
* fix(cli): enforce F401 in cli and fix benchmark info import errors by @Moenupa in https://github.com/modelscope/evalscope/pull/1691
* docs: fix the benchmark smoke evaluation command by @Excelius-Wang in https://github.com/modelscope/evalscope/pull/1721
* fix(audio): preserve empty ASR transcripts when scoring WER by @Excelius-Wang in https://github.com/modelscope/evalscope/pull/1722
* fix(agent): stop sandboxed commands from inheriting the evaluator's stdin by @ChenCJ-io in https://github.com/modelscope/evalscope/pull/1718
* feat(web): group same-model reports in the report list, display-only by @Dhru1001 in https://github.com/modelscope/evalscope/pull/1703
* fix(service): stop 500ing on predictions whose agent trace carries token usage by @Dhru1001 in https://github.com/modelscope/evalscope/pull/1725
* perf(web): cap dashboard's aggregated results table to 100 rows up front by @Dhru1001 in https://github.com/modelscope/evalscope/pull/1724
* feat(perf): add AgentX AIPerf scenario by @Yunnglin in https://github.com/modelscope/evalscope/pull/1716
* fix(utils): narrow check_import exception handling by @Bruce-Yii in https://github.com/modelscope/evalscope/pull/1720
* feat: add LibriSpeech test-other subset by @Yunnglin in https://github.com/modelscope/evalscope/pull/1733
* docs: align benchmark contribution examples with metadata requirements by @BingH225 in https://github.com/modelscope/evalscope/pull/1730
* fix(agent): forward exec stdin into the sandbox instead of dropping it by @ChenCJ-io in https://github.com/modelscope/evalscope/pull/1719
* fix(arena): validate review identities before pairing by @elandesberg in https://github.com/modelscope/evalscope/pull/1731
* fix(perf): forward tokenizer trust option for AgentX by @Xiangyi1996 in https://github.com/modelscope/evalscope/pull/1745
* feat(agent): add DeepSeek Harness bridge runner by @Yunnglin in https://github.com/modelscope/evalscope/pull/1746
* feat(benchmarks): add THCHS-30 phoneme recognition by @chenminupup in https://github.com/modelscope/evalscope/pull/1732
* feat(perf): add optional PD handoff metrics by @gbdjxgp in https://github.com/modelscope/evalscope/pull/1744
* fix(perf): forward AgentX benchmark grace period by @Xiangyi1996 in https://github.com/modelscope/evalscope/pull/1747
* fix(evaluator): preserve multi-alias targets for inclusion-based scoring by @Dhru1001 in https://github.com/modelscope/evalscope/pull/1727

## New Contributors
* @Anai-Guo made their first contribution in https://github.com/modelscope/evalscope/pull/1687
* @ZTJiu made their first contribution in https://github.com/modelscope/evalscope/pull/1690
* @ChenCJ-io made their first contribution in https://github.com/modelscope/evalscope/pull/1696
* @Bruce-Yii made their first contribution in https://github.com/modelscope/evalscope/pull/1720
* @elandesberg made their first contribution in https://github.com/modelscope/evalscope/pull/1731
* @Xiangyi1996 made their first contribution in https://github.com/modelscope/evalscope/pull/1745
* @chenminupup made their first contribution in https://github.com/modelscope/evalscope/pull/1732

**Full Changelog**: https://github.com/modelscope/evalscope/compare/v1.11.1...v1.12.0
