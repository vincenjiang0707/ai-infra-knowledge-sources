# [Issue #1651] [Tracking Issue] Synthetic Acceptance for MTP Benchmarks / [Tracking Issue] MTP 基准测试的合成接受长度

source: https://github.com/SemiAnalysisAI/InferenceX/issues/1651
state: open | updated: 2026-07-08T17:10:11Z
labels: p0, in progress

## 正文

# Proposed Change: Synthetic Acceptance

Recently, all major serving frameworks (vLLM, SGLang, TensorRT-LLM) have added support for synthetic acceptance length (AL) for benchmarking purposes: the server can be configured to accept specific number of draft tokens in order to match (on average) a target acceptance length. Using this feature, we can match expected generation speeds with far higher consistency, and have much more control over the fidelity of the acceptance rate. 

Doing so will also ensure consistent benchmarking environments across FWs, avoid honest mistakes such as client side settings (e.g. chat-template), and provide uniform performance expectations when using random and pseudorandom text for benchmarking purposes.

For each model and number of speculated tokens, SemiAnalysis chooses a fixed AL based on the observed MTP AL calibrated on SpeedBench coding dataset using model-provider-recommended sampling parameters (M0). For example, running DSV4-Pro on SpeedBench coding with 3 MTP draft tokens gives a mean AL of ~2.75, so the settings would be roughly [MTP1: AL 1.85, MTP2: AL 2.45, MTP3: AL 2.75] (mock numbers).

We propose the following methodology:

## M0: New Github Action for Auditable Reference AL Generation
We introduce a new GitHub Action that integrates [SpeedBench](https://huggingface.co/datasets/nvidia/SPEED-Bench) to InferenceX. For each model that supports MTP, we use the workflow to generate reference AL values, with the coding dataset, for both thinking on and thinking off. All reference values will be generated using vLLM for consistency, for speculative tokens going from 1 to 7.

## M1: Evaluation runs for correct implementation of MTP

During evaluation the synthetic acceptance feature is disabled and the same model-provider-recommended sampling parameters are used. The eval script now includes two pieces:

1. Run SpeedBench, acceptance rate is automatically collected from the server at the end of the run. Then: we assert that the achieved acceptance length is above a threshold from the reference values.
2. Run the existing GSM8k evals to ensure accuracy still pass.

## M2: Apply Synthetic Acceptance During Benchmarks

During benchmarking synthetic acceptance is enabled with the target AL and uses the same prompt generation setup as non-MTP.  We will roll this out with single node first, followed by multi-node tests. To make sure the benchmarks are fair, we ensure implementation for synthetic MTP acceptance rates to be open, auditable, and mathematically equivalent for all participating FWs.


- [x] M0: New Github Action for Auditable Reference AL Generation
- [ ] M1: Evaluation runs for correct implementation of MTP
- [ ] M2: Apply Synthetic Acceptance During Benchmarks

## 中文说明
提议在 MTP 基准测试中引入合成接受长度（Synthetic Acceptance Length）机制。所有主流推理框架（vLLM、SGLang、TensorRT-LLM）现已支持配置合成接受长度，可按目标接受率匹配预期生成速度，确保跨框架基准测试环境的一致性。分三个里程碑推进：M0——新增 GitHub Action，使用 SpeedBench 编码数据集为每个支持 MTP 的模型生成可审计的参考接受长度值；M1——评估运行，禁用合成接受功能并断言实际接受长度达到阈值，同时运行 GSM8K 准确性评估；M2——在基准测试中启用合成接受，先单节点后多节点，确保各框架的实现公开、可审计且数学等价。


## 评论 (7)

### xinli-sw · 2026-06-02

https://github.com/SemiAnalysisAI/InferenceX/pull/1650 - draft GH actions
https://github.com/SemiAnalysisAI/InferenceX/pull/1592 - reference AL for DSV4 for early alignment

### xinli-sw · 2026-06-10

M0: https://github.com/SemiAnalysisAI/InferenceX/pull/1650, merged

### qiching · 2026-06-11

https://github.com/SemiAnalysisAI/InferenceX/pull/1706 - reference AL for Qwen3.5, DSR1, GLM-5

### qiching · 2026-06-15

https://github.com/SemiAnalysisAI/InferenceX/pull/1789 - Multi-node synthetic AL injection for MTP (dsv4 mtp2 bring-up)

### qiching · 2026-07-01

#1789 works good on function and performance. 
WIP: We plan to onboard multi-node injection to spilt 3 stage to optimize it to be general features benefit all framework

### qiching · 2026-07-01

#1706 [Done] Speedbench golden AL reference collection pipeline for all necessary models

### qiching · 2026-07-08

For multi-node injection, we spilt 3 stacked PR to achieve better scalability(MUST merge by the sequence from 0 to 3):
[PR0]: https://github.com/SemiAnalysisAI/InferenceX/pull/2087
[PR1]: https://github.com/SemiAnalysisAI/InferenceX/pull/2088
[PR2]: https://github.com/SemiAnalysisAI/InferenceX/pull/2090
[PR3]: https://github.com/SemiAnalysisAI/InferenceX/pull/2091


@xinli-sw @Ankur-singh @functionstackx 
