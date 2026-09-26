source: https://github.com/modelscope/evalscope/releases

# Releases: modelscope/evalscope

Releases · modelscope/evalscope

## Release list

## v1.12.0

## 中文版

### 基准测试数据集

- 语音评测：新增 THCHS-30 国际音标（IPA）音素识别评测，支持 Phone Error Rate（PER）指标。
- 语音评测：LibriSpeech 新增
`test-other`

子集支持。

### 功能增强

- Agent 评测：新增 DeepSeek Harness Bridge Runner，支持通过 OpenAI Chat Completions Bridge 运行
`deepseek-harness`

。 - Agent 评测：新增可选的工具调用参数 Schema 校验，帮助区分模型参数生成错误与工具执行错误。
- Agent 基准：Tau3-Bench 支持配置 Agent 最大执行步数
`max_steps`

。 - 性能测试：新增基于 AIPerf 的 AgentX 回放场景，支持数据版本校验、运行有效性记录和敏感信息脱敏。
- 性能测试：新增可选 PD 分离式推理指标，包括 Steady ITL、PD Handoff Latency 和 PD Handoff Overhead。
- 性能测试：AgentX 支持
`tokenizer_trust_remote_code`

与`benchmark_grace_period`

配置。 - Dashboard：报告列表支持按模型展示同一模型的多个报告，保持原始评测报告不变。
- Dashboard：聚合结果表首屏按批次展示，优化大规模模型与基准组合下的页面性能。

### 文档优化

- 更新 Agent Bridge、AgentX 性能测试、Tau3-Bench、评测架构和基准贡献说明。
- 修复基准 smoke evaluation 示例命令，并补充正确的 mock 评测配置。
- 更新产品网站入口及相关使用指引。

### 问题修复

- 修复多参考答案在 inclusion-based 评分中被拼接为单个错误目标的问题，影响 TriviaQA、MMLU-Redux 等评测。
- 修复 Judge 模板渲染、指标异常处理、包含匹配规则及 GeneralArena bootstrap 随机数处理，提升评测结果的正确性与可复现性。
- 修复 GeneralArena 导入历史评测结果时按行错配、将已生成回复带入 Judge 输入的问题；评测版本升级至
`v1.2`

。 - 修复 Agent Bridge 丢失模型原始输出、性能指标和推理内容，以及上游生成失败未记录到 Agent Trace 的问题。
- 修复 Agent sandbox stdin 隔离和显式 stdin 传递问题。
- 修复 MCP 初始化错误被隐藏、service worker 无法运行 MCP stdio 客户端的问题。
- 修复空 ASR 转写被错误计为 WER=0 的问题；Seed-TTS-Eval 评测版本升级至
`v1.1`

。 - 修复流式推理输出的 TTFT/ITL 统计、多轮 warmup 交接，以及带 token usage 的 Agent Trace 导致 Predictions API 返回 500 的问题。
- 修复 few-shot 配置未在数据加载前校验、CLI
`benchmark-info`

导入错误、Dashboard 空分数行模型名异常换行等问题。 - 修复可用模块的导入期异常被误报为缺失依赖的问题，并移除会直接报错的 CLIP Benchmark 模板入口。

## English Version

### Benchmark Datasets

- Speech Evaluation: Added THCHS-30 IPA phoneme recognition with Phone Error Rate (PER) support.
- Speech Evaluation: Added the LibriSpeech
`test-other`

subset.

### Feature Enhancements

- Agent Evaluation: Added the DeepSeek Harness Bridge Runner for running
`deepseek-harness`

through the OpenAI Chat Completions Bridge. - Agent Evaluation: Added optional tool-call argument Schema validation to distinguish invalid model arguments from tool execution failures.
- Agent Benchmarks: Added configurable Agent
`max_steps`

support for Tau3-Bench. - Performance Testing: Added an AIPerf-based AgentX replay scenario with dataset-version validation, run-validity records, and secret redaction.
- Performance Testing: Added optional PD-disaggregated serving metrics, including Steady ITL, PD Handoff Latency, and PD Handoff Overhead.
- Performance Testing: Added
`tokenizer_trust_remote_code`

and`benchmark_grace_period`

options for AgentX. - Dashboard: Added display-only grouping of reports from the same model without mutating source evaluation reports.
- Dashboard: Added incremental rendering for aggregated results to improve large-scale dashboard performance.

### Documentation

- Updated documentation for Agent Bridge, AgentX performance testing, Tau3-Bench, evaluation architecture, and benchmark contributions.
- Fixed the benchmark smoke-evaluation example and documented the correct mock-evaluation configuration.
- Updated product website entry points and related guidance.

### Bug Fixes

- Fixed multi-reference answers being flattened into an invalid target in inclusion-based scoring, affecting benchmarks such as TriviaQA and MMLU-Redux.
- Fixed Judge template rendering, metric-failure handling, inclusion matching, and GeneralArena bootstrap RNG behavior for more correct and reproducible evaluation results.
- Fixed mispaired imported reviews and generated responses leaking into Judge inputs in GeneralArena; advanced its evaluation version to
`v1.2`

. - Fixed Agent Bridge loss of original model outputs, performance metrics, reasoning content, and upstream generation failures in Agent Traces.
- Fixed Agent sandbox stdin isolation and explicit stdin forwarding.
- Fixed hidden MCP initialization errors and MCP stdio clients failing in service workers.
- Fixed empty ASR transcripts being scored as WER=0; advanced Seed-TTS-Eval to evaluation version
`v1.1`

. - Fixed TTFT/ITL timing for streamed reasoning output, multi-turn warmup handoff, and Predictions API 500 errors caused by Agent Traces with token usage.
- Fixed late few-shot configuration validation, CLI
`benchmark-info`

imports, and model-name wrapping for empty Dashboard score rows. - Fixed available modules' import-time failures being misreported as missing dependencies, and removed the CLIP Benchmark template entry point that always raised an error.

## What's Changed

- chore: tighten ruff rule baseline by
[@Yunnglin](https://github.com/Yunnglin)in[#1686](https://github.com/modelscope/evalscope/pull/1686) - fix(perf): hand off multi-turn warmup without draining by
[@Yunnglin](https://github.com/Yunnglin)in[#1684](https://github.com/modelscope/evalscope/pull/1684) - fix(clip_benchmark): remove
**main**block that always raises TypeError by[@Anai-Guo](https://github.com/Anai-Guo)in[#1687](https://github.com/modelscope/evalscope/pull/1687) - chore: enforce F401 in evalscope/utils by
[@Moenupa](https://github.com/Moenupa)in[#1689](https://github.com/modelscope/evalscope/pull/1689) - fix(dep): remove dependency
`overrides`

; type check instead of runtime by[@Moenupa](https://github.com/Moenupa)in[#1692](https://github.com/modelscope/evalscope/pull/1692) - feat(tau3_bench): support configurable max_steps parameter by
[@ZTJiu](https://github.com/ZTJiu)in[#1690](https://github.com/modelscope/evalscope/pull/1690) - docs(agent): point prediction docstrings at the hook that resolves it by
[@ChenCJ-io](https://github.com/ChenCJ-io)in[#1696](https://github.com/modelscope/evalscope/pull/1696) - fix(web): stop score-matrix model name wrapping character-by-character by
[@Dhru1001](https://github.com/Dhru1001)in[#1704](https://github.com/modelscope/evalscope/pull/1704) - fix(perf): measure TTFT from reasoning output by
[@git-jxj](https://github.com/git-jxj)in[#1700](https://github.com/modelscope/evalscope/pull/1700) - fix(bridge): record upstream generate failures on the agent trace by
[@ChenCJ-io](https://github.com/ChenCJ-io)in[#1698](https://github.com/modelscope/evalscope/pull/1698) - fix(mcp): preserve initialization errors and support service stdio by
[@git-jxj](https://github.com/git-jxj)in[#1701](https://github.com/modelscope/evalscope/pull/1701) - refactor(metrics): give metric semantics one source per decision by
[@Yunnglin](https://github.com/Yunnglin)in[#1705](https://github.com/modelscope/evalscope/pull/1705) - fix(eval): correct judge rendering, metric scoring, and bootstrap RNG by
[@git-jxj](https://github.com/git-jxj)in[#1702](https://github.com/modelscope/evalscope/pull/1702) - fix(judge): import canonicalize_producer_identity from its new module by
[@ChenCJ-io](https://github.com/ChenCJ-io)in[#1711](https://github.com/modelscope/evalscope/pull/1711) - fix(bridge): keep the model output intact on reconstructed assistant messages by
[@ChenCJ-io](https://github.com/ChenCJ-io)in[#1710](https://github.com/modelscope/evalscope/pull/1710) - fix(benchmark): validate few-shot capabilities by
[@Yunnglin](https://github.com/Yunnglin)in[#1714](https://github.com/modelscope/evalscope/pull/1714) - feat(agent): validate tool-call arguments against the advertised schema by
[@ChenCJ-io](https://github.com/ChenCJ-io)in[#1712](https://github.com/modelscope/evalscope/pull/1712) - fix(cli): enforce F401 in cli and fix benchmark info import errors by
[@Moenupa](https://github.com/Moenupa)in[#1691](https://github.com/modelscope/evalscope/pull/1691) - docs: fix the benchmark smoke evaluation command by
[@Excelius-Wang](https://github.com/Excelius-Wang)in[#1721](https://github.com/modelscope/evalscope/pull/1721) - fix(audio): preserve empty ASR transcripts when scoring WER by
[@Excelius-Wang](https://github.com/Excelius-Wang)in[#1722](https://github.com/modelscope/evalscope/pull/1722) - fix(agent): stop sandboxed commands from inheriting the evaluator's stdin by
[@ChenCJ-io](https://github.com/ChenCJ-io)in[#1718](https://github.com/modelscope/evalscope/pull/1718) - feat(web): group same-model reports in the report list, display-only by
[@Dhru1001](https://github.com/Dhru1001)in[#1703](https://github.com/modelscope/evalscope/pull/1703) - fix(service): stop 500ing on predictions whose agent trace carries token usage by
[@Dhru1001](https://github.com/Dhru1001)in[#1725](https://github.com/modelscope/evalscope/pull/1725) - perf(web): cap dashboard's aggregated results table to 100 rows up front by
[@Dhru1001](https://github.com/Dhru1001)in[#1724](https://github.com/modelscope/evalscope/pull/1724) - feat(perf): add AgentX AIPerf scenario by
[@Yunnglin](https://github.com/Yunnglin)in[#1716](https://github.com/modelscope/evalscope/pull/1716) - fix(utils): narrow check_import exception handling by
[@Bruce-Yii](https://github.com/Bruce-Yii)in[#1720](https://github.com/modelscope/evalscope/pull/1720) - feat: add LibriSpeech test-other subset by
[@Yunnglin](https://github.com/Yunnglin)in[#1733](https://github.com/modelscope/evalscope/pull/1733) - docs: align benchmark contribution examples with metadata requirements by
[@BingH225](https://github.com/BingH225)in[#1730](https://github.com/modelscope/evalscope/pull/1730) - fix(agent): forward exec stdin into the sandbox instead of dropping it by
[@ChenCJ-io](https://github.com/ChenCJ-io)in[#1719](https://github.com/modelscope/evalscope/pull/1719) - fix(arena): validate review identities before pairing by
[@elandesberg](https://github.com/elandesberg)in[#1731](https://github.com/modelscope/evalscope/pull/1731) - fix(perf): forward tokenizer trust option for AgentX by
[@Xiangyi1996](https://github.com/Xiangyi1996)in[#1745](https://github.com/modelscope/evalscope/pull/1745) - feat(agent): add DeepSeek Harness bridge runner by
[@Yunnglin](https://github.com/Yunnglin)in[#1746](https://github.com/modelscope/evalscope/pull/1746) - feat(benchmarks): add THCHS-30 phoneme recognition by
[@chenminupup](https://github.com/chenminupup)in[#1732](https://github.com/modelscope/evalscope/pull/1732) - feat(perf): add optional PD handoff metrics by
[@gbdjxgp](https://github.com/gbdjxgp)in[#1744](https://github.com/modelscope/evalscope/pull/1744) - fix(perf): forward AgentX benchmark grace period by
[@Xiangyi1996](https://github.com/Xiangyi1996)in[#1747](https://github.com/modelscope/evalscope/pull/1747) - fix(evaluator): preserve multi-alias targets for inclusion-based scoring by
[@Dhru1001](https://github.com/Dhru1001)in[#1727](https://github.com/modelscope/evalscope/pull/1727)

## New Contributors

[@Anai-Guo](https://github.com/Anai-Guo)made their first contribution in[#1687](https://github.com/modelscope/evalscope/pull/1687)[@ZTJiu](https://github.com/ZTJiu)made their first contribution in[#1690](https://github.com/modelscope/evalscope/pull/1690)[@ChenCJ-io](https://github.com/ChenCJ-io)made their first contribution in[#1696](https://github.com/modelscope/evalscope/pull/1696)[@Bruce-Yii](https://github.com/Bruce-Yii)made their first contribution in[#1720](https://github.com/modelscope/evalscope/pull/1720)[@elandesberg](https://github.com/elandesberg)made their first contribution in[#1731](https://github.com/modelscope/evalscope/pull/1731)[@Xiangyi1996](https://github.com/Xiangyi1996)made their first contribution in[#1745](https://github.com/modelscope/evalscope/pull/1745)[@chenminupup](https://github.com/chenminupup)made their first contribution in[#1732](https://github.com/modelscope/evalscope/pull/1732)

**Full Changelog**: `v1.11.1...v1.12.0`

## v1.11.1

## 中文版

### 基准测试数据集

- 多模态评测：新增 SURDS、VLMs Are Biased、Ref-Adv-s、VisFactor、MedXpertQA、VTCBench 等视觉、多模态与长视频理解基准。
- 推理与专业能力评测：新增 $OneMillion-Bench、PRBench、HMMT-Nov-2025 等 Agent、深度推理与数学评测基准。

### 功能增强

- API 契约：Web API 响应契约改由 Pydantic 模型自动生成，提升前后端类型一致性。
- 缓存与数据集：隔离数据集缓存键，增强视频解码与
`limit`

参数校验。 - 模型服务：支持识别 HTTP 200 响应中的网关错误载荷，并优化音频预处理、流式响应、用量统计与重试行为。
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

## English Version

### Benchmark Datasets

- Multimodal Evaluation: Added SURDS, VLMs Are Biased, Ref-Adv-s, VisFactor, MedXpertQA, VTCBench, and other vision, multimodal, and long-video benchmarks.
- Reasoning and Domain Evaluation: Added $OneMillion-Bench, PRBench, and HMMT-Nov-2025 for agent, deep-reasoning, and mathematical evaluation.

### Feature Enhancements

- API Contracts: Web API response contracts are now generated from Pydantic models for stronger frontend/backend type consistency.
- Cache and Datasets: Isolated dataset cache keys and improved video decoding and
`limit`

validation. - Model Services: Detects gateway-error payloads returned with HTTP 200, and improves audio preprocessing, streaming responses, usage accounting, and retry behavior.
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

- fix(rag): raise a clear error when a LogitScore reranker loads on an old sentence-transformers by
[@AmirF194](https://github.com/AmirF194)in[#1620](https://github.com/modelscope/evalscope/pull/1620) - feat(io): unify undecoding behavior and support overlong images list by
[@Moenupa](https://github.com/Moenupa)in[#1626](https://github.com/modelscope/evalscope/pull/1626) - cicd(isort): migrate to ruff isort by
[@Moenupa](https://github.com/Moenupa)in[#1629](https://github.com/modelscope/evalscope/pull/1629) - fix(typing): add type hints to logger by
[@Moenupa](https://github.com/Moenupa)in[#1632](https://github.com/modelscope/evalscope/pull/1632) - docs: fix stale ModelAPI docstrings (nonexistent api_key_vars / ChatUserMessage) by
[@BingH225](https://github.com/BingH225)in[#1634](https://github.com/modelscope/evalscope/pull/1634) - fix(score): prune rouge scoring function and fix en version of rouge by
[@Moenupa](https://github.com/Moenupa)in[#1633](https://github.com/modelscope/evalscope/pull/1633) - feat(benchmarks): add hmmt_nov25 benchmark by
[@haoruilee](https://github.com/haoruilee)in[#1636](https://github.com/modelscope/evalscope/pull/1636) - feat(benchmark): support VTCBench by
[@Moenupa](https://github.com/Moenupa)in[#1635](https://github.com/modelscope/evalscope/pull/1635) - fix(perf): preserve Unicode line separators in SSE payloads by
[@Yunnglin](https://github.com/Yunnglin)in[#1642](https://github.com/modelscope/evalscope/pull/1642) - fix(benchmark): VTCBench wrongly parsed html tags by
[@Moenupa](https://github.com/Moenupa)in[#1643](https://github.com/modelscope/evalscope/pull/1643) - test(perf): stop asserting log text in workload_trace tests by
[@Yunnglin](https://github.com/Yunnglin)in[#1647](https://github.com/modelscope/evalscope/pull/1647) - fix(perf): hand closed-loop warmup over without draining the server by
[@Yunnglin](https://github.com/Yunnglin)in[#1641](https://github.com/modelscope/evalscope/pull/1641) - fix(report): sync HTML reports with console theme by
[@Yunnglin](https://github.com/Yunnglin)in[#1646](https://github.com/modelscope/evalscope/pull/1646) - chore: unify linting and formatting with Ruff by
[@Yunnglin](https://github.com/Yunnglin)in[#1644](https://github.com/modelscope/evalscope/pull/1644) - feat: support MedXpertQA benchmark by
[@Yunnglin](https://github.com/Yunnglin)in[#1655](https://github.com/modelscope/evalscope/pull/1655) - fix(web): derive API contracts from Pydantic by
[@Yunnglin](https://github.com/Yunnglin)in[#1658](https://github.com/modelscope/evalscope/pull/1658) - feat(benchmarks): add PRBench by
[@Yunnglin](https://github.com/Yunnglin)in[#1665](https://github.com/modelscope/evalscope/pull/1665) - feat: add OneMillion-Bench benchmark by
[@Yunnglin](https://github.com/Yunnglin)in[#1667](https://github.com/modelscope/evalscope/pull/1667) - fix(benchmark): restore F821 and fix jobbench mis-ignored linting issue by
[@Moenupa](https://github.com/Moenupa)in[#1652](https://github.com/modelscope/evalscope/pull/1652) - feat: add VisFactor benchmark by
[@Yunnglin](https://github.com/Yunnglin)in[#1661](https://github.com/modelscope/evalscope/pull/1661) - feat(benchmarks): add Ref-Adv-s by
[@Yunnglin](https://github.com/Yunnglin)in[#1668](https://github.com/modelscope/evalscope/pull/1668) - feat(benchmarks): add VLMs Are Biased by
[@Yunnglin](https://github.com/Yunnglin)in[#1669](https://github.com/modelscope/evalscope/pull/1669) - fix(metrics): correct answer parsing and text scoring by
[@git-jxj](https://github.com/git-jxj)in[#1649](https://github.com/modelscope/evalscope/pull/1649) - fix(models): correct retry semantics and Anthropic streaming by
[@git-jxj](https://github.com/git-jxj)in[#1651](https://github.com/modelscope/evalscope/pull/1651) - fix(models): correct cache, usage, streaming, and image outputs by
[@git-jxj](https://github.com/git-jxj)in[#1653](https://github.com/modelscope/evalscope/pull/1653) - fix(perf): improve metric accuracy, validation, and shutdown by
[@git-jxj](https://github.com/git-jxj)in[#1654](https://github.com/modelscope/evalscope/pull/1654) - feat(benchmarks): add SURDS by
[@Yunnglin](https://github.com/Yunnglin)in[#1670](https://github.com/modelscope/evalscope/pull/1670) - fix(judge): serialize lazy judge initialization by
[@git-jxj](https://github.com/git-jxj)in[#1664](https://github.com/modelscope/evalscope/pull/1664) - fix(models): avoid blocking event loop during async audio preprocessing by
[@git-jxj](https://github.com/git-jxj)in[#1662](https://github.com/modelscope/evalscope/pull/1662) - fix(resources): verify NLTK mirror archives with pinned digests by
[@git-jxj](https://github.com/git-jxj)in[#1663](https://github.com/modelscope/evalscope/pull/1663) - fix(cache): deduplicate review state and tolerate torn resume rows by
[@git-jxj](https://github.com/git-jxj)in[#1657](https://github.com/modelscope/evalscope/pull/1657) - fix(benchmark): handle empty OmniDocBench page metrics by
[@git-jxj](https://github.com/git-jxj)in[#1666](https://github.com/modelscope/evalscope/pull/1666) - refactor(models): move litellm imports to module level by
[@seroze](https://github.com/seroze)in[#1678](https://github.com/modelscope/evalscope/pull/1678) - fix(metrics): make inst_level_* a micro-average over instructions by
[@arkrolin](https://github.com/arkrolin)in[#1672](https://github.com/modelscope/evalscope/pull/1672) - fix(ifbench): enforce unique words in sentence checker by
[@linhongyu510](https://github.com/linhongyu510)in[#1676](https://github.com/modelscope/evalscope/pull/1676) - fix(ifbench): remove duplicate evaluation version by
[@Excelius-Wang](https://github.com/Excelius-Wang)in[#1681](https://github.com/modelscope/evalscope/pull/1681) - fix(perf): ignore metadata-only chunks in TTFT and ITL by
[@Excelius-Wang](https://github.com/Excelius-Wang)in[#1645](https://github.com/modelscope/evalscope/pull/1645) - fix(benchmark): harden Toolathlon job lifecycle and result validation by
[@git-jxj](https://github.com/git-jxj)in[#1656](https://github.com/modelscope/evalscope/pull/1656) - fix(benchmark): preserve metric identities on General QA/VQA scoring errors by
[@git-jxj](https://github.com/git-jxj)in[#1660](https://github.com/modelscope/evalscope/pull/1660) - fix(dataset): isolate cache keys, undecode video, and validate limits consistently by
[@git-jxj](https://github.com/git-jxj)in[#1659](https://github.com/modelscope/evalscope/pull/1659) - fix(models): retry 200 responses that carry a gateway error payload by
[@seroze](https://github.com/seroze)in[#1673](https://github.com/modelscope/evalscope/pull/1673) - refactor(io): remove unused type cast and deduplicate code in media io by
[@Moenupa](https://github.com/Moenupa)in[#1683](https://github.com/modelscope/evalscope/pull/1683)

## New Contributors

[@AmirF194](https://github.com/AmirF194)made their first contribution in[#1620](https://github.com/modelscope/evalscope/pull/1620)[@seroze](https://github.com/seroze)made their first contribution in[#1678](https://github.com/modelscope/evalscope/pull/1678)[@arkrolin](https://github.com/arkrolin)made their first contribution in[#1672](https://github.com/modelscope/evalscope/pull/1672)[@linhongyu510](https://github.com/linhongyu510)made their first contribution in[#1676](https://github.com/modelscope/evalscope/pull/1676)

**Full Changelog**: `v1.11.0...v1.11.1`

## v1.11.0

## 中文版

### 基准测试数据集

- 多模态评测：新增 PerceptionBench、ScreenSpot-Pro、PMC-VQA、LogicVista、CC-OCR-V2、SLAKE、olmOCR-Bench、CountQA 等视觉、多模态与文档理解基准。
- 推理与专业能力评测：新增 HiPhO 高中物理奥赛、PhyX 物理推理（选择题与开放题）、PLawBench 法律实践能力评测。
- 多语言评测：新增 Milu、ARC-Indic、GSM8K-Indic、IndicBoolQ、TriviaQA-Indic、IndicPara、Sanskriti、Hindi HellaSwag，以及 BhashaBench / BhashaBench-Multi 的金融、法律、农业和阿育吠陀子集。

### 功能增强

- 评测版本管理：新增原生评测版本与缓存身份校验，并支持确定性的选择题选项打乱，避免语义变更后复用不兼容缓存。
- Judge 评测：统一 LLM Judge 的 JSON 输出契约；格式不合法或
`[ERROR]`

回复将从指标统计中排除。 - 自定义数据集：
`general_vmcq`

统一支持图片、视频、音频输入，并支持 Parquet 和二进制媒体字段；`general_vqa`

新增媒体占位符支持。 - 指标与报告：统一指标语义和评测报告展示，优化 Agent Trace 的步骤分组及工具调用与结果关联。
- 服务与 Web：评测界面支持 Sandbox 配置；优化报告列表元数据读取和条件请求。

### 文档优化

- 更新文本生成图像任务的指标选择说明。
- 修复 API 消息、工具调用和 Tau-bench
`pass^k`

等文档说明问题。

### 问题修复

- 修复 IFBench NLTK 英文词性标注模型下载、ACEBench 官方评分协议对齐、IFEval 与 GPQA 结果可复现性等问题。
- 修复多选题括号答案和多答案场景下的标签提取问题。
- 修复 TaskConfig 未知字段被静默忽略的问题，提供相近字段建议；同时修复
`reasoning_effort`

参数透传。 - 修复 CMMMU 等视觉基准的媒体输入归一化、OmniDocBench 重复加载、VQA 信息读取等问题。
- 修复终端评测非法 reward 与未完成运行的结果报告问题，以及 BFCL 空工具调用丢失问题。
- 修复性能测试中的流式 usage 统计、空 content、请求构建失败、缺失 chat template 和插件返回空数据集等问题。
- 修复 Web 报告中的本地媒体渲染、空
`reasoning_tokens`

与后端空值处理问题。

## English Version

### Benchmark Datasets

- Multimodal Evaluation: Added PerceptionBench, ScreenSpot-Pro, PMC-VQA, LogicVista, CC-OCR-V2, SLAKE, olmOCR-Bench, CountQA, and other vision, multimodal, and document-understanding benchmarks.
- Reasoning and Domain Evaluation: Added HiPhO for high-school physics Olympiad problems, PhyX for multiple-choice and open-ended physical reasoning, and PLawBench for legal practice evaluation.
- Multilingual Evaluation: Added Milu, ARC-Indic, GSM8K-Indic, IndicBoolQ, TriviaQA-Indic, IndicPara, Sanskriti, Hindi HellaSwag, and BhashaBench / BhashaBench-Multi finance, legal, agriculture, and Ayurveda subsets.

### Feature Enhancements

- Evaluation Versioning: Added native evaluation versioning, cache identity checks, and deterministic choice shuffling to prevent incompatible cached predictions from being reused.
- Judge Evaluation: Unified LLM-judge JSON output contracts; malformed and
`[ERROR]`

responses are excluded from metric aggregation. - Custom Datasets: Unified image, video, and audio inputs in
`general_vmcq`

, with Parquet and binary media-field support; added media placeholders to`general_vqa`

. - Metrics and Reports: Unified metric semantics and evaluation reports, with improved Agent Trace step grouping and tool-call/result linking.
- Service and Web: Added Sandbox configuration to the evaluation UI and improved report-list metadata retrieval with conditional requests.

### Documentation

- Clarified metric selection for text-to-image tasks.
- Fixed documentation issues for API messages, tool calls, and Tau-bench
`pass^k`

.

### Bug Fixes

- Fixed IFBench NLTK English tagger downloads, ACEBench official-protocol alignment, and reproducibility issues in IFEval and GPQA.
- Fixed answer-label extraction for bracketed and multiple-choice responses.
- Fixed silently ignored unknown TaskConfig keys with close-match suggestions, and fixed
`reasoning_effort`

parameter forwarding. - Fixed media-input normalization across CMMMU and other vision benchmarks, repeated OmniDocBench loading, and VQA information handling.
- Fixed invalid-reward and incomplete-run reporting for terminal benchmarks, and BFCL empty tool-call handling.
- Fixed streaming usage accounting, empty content, request-building failures, missing chat templates, and empty plugin datasets in performance testing.
- Fixed local media rendering, null
`reasoning_tokens`

, and backend null handling in Web reports.

## What's Changed

- fix(ifbench): download correct NLTK English tagger by
[@git-jxj](https://github.com/git-jxj)in[#1539](https://github.com/modelscope/evalscope/pull/1539) - fix(acebench): align with the official protocol and fix milestone scoring by
[@Yunnglin](https://github.com/Yunnglin)in[#1544](https://github.com/modelscope/evalscope/pull/1544) - fix: multi-choice answer extraction, ifeval determinism, LiveCodeBench system prompt, tau-bench pass^k docs by
[@Yunnglin](https://github.com/Yunnglin)in[#1549](https://github.com/modelscope/evalscope/pull/1549) - feat(perception_bench): add PerceptionBench atomic visual perception benchmark by
[@Yunnglin](https://github.com/Yunnglin)in[#1551](https://github.com/modelscope/evalscope/pull/1551) - feat(screenspot_pro): add ScreenSpot-Pro GUI grounding benchmark by
[@Yunnglin](https://github.com/Yunnglin)in[#1550](https://github.com/modelscope/evalscope/pull/1550) - feat(plawbench): add PLawBench rubric-based legal practice benchmark by
[@Yunnglin](https://github.com/Yunnglin)in[#1553](https://github.com/modelscope/evalscope/pull/1553) - feat(pmc_vqa): add PMC-VQA medical visual question answering benchmark by
[@Yunnglin](https://github.com/Yunnglin)in[#1557](https://github.com/modelscope/evalscope/pull/1557) - feat(hipho): add HiPhO high school physics Olympiad benchmark by
[@Yunnglin](https://github.com/Yunnglin)in[#1558](https://github.com/modelscope/evalscope/pull/1558) - fix(config): pass reasoning_effort through instead of whitelisting it by
[@Yunnglin](https://github.com/Yunnglin)in[#1561](https://github.com/modelscope/evalscope/pull/1561) - fix(multi_choices): parse answer labels the model wrapped in brackets by
[@Yunnglin](https://github.com/Yunnglin)in[#1560](https://github.com/modelscope/evalscope/pull/1560) - feat(logic_vista): add LogicVista visual logical reasoning benchmark by
[@Yunnglin](https://github.com/Yunnglin)in[#1556](https://github.com/modelscope/evalscope/pull/1556) - fix(web): render local-path media in both dashboard chains by
[@Yunnglin](https://github.com/Yunnglin)in[#1562](https://github.com/modelscope/evalscope/pull/1562) - feat(cc_ocr_v2): add CC-OCR-V2 real-world document OCR benchmark by
[@Yunnglin](https://github.com/Yunnglin)in[#1559](https://github.com/modelscope/evalscope/pull/1559) - feat(web): add sandbox configuration to evaluation UI by
[@Dhru1001](https://github.com/Dhru1001)in[#1545](https://github.com/modelscope/evalscope/pull/1545) - fix: validate service output directory by
[@heliubj18](https://github.com/heliubj18)in[#1554](https://github.com/modelscope/evalscope/pull/1554) - fix(perf): explain how to proceed when a tokenizer has no chat template by
[@Yunnglin](https://github.com/Yunnglin)in[#1564](https://github.com/modelscope/evalscope/pull/1564) - Fix async loop shutdown timeout cascade by
[@Yunnglin](https://github.com/Yunnglin)in[#1566](https://github.com/modelscope/evalscope/pull/1566) - fix(web): allow null reasoning_tokens in report content blocks by
[@Dhru1001](https://github.com/Dhru1001)in[#1563](https://github.com/modelscope/evalscope/pull/1563) - fix(web): normalize backend null to undefined at the API validation boundary by
[@Yunnglin](https://github.com/Yunnglin)in[#1567](https://github.com/modelscope/evalscope/pull/1567) - feat(metrics): unify metric semantics and evaluation reporting by
[@Yunnglin](https://github.com/Yunnglin)in[#1552](https://github.com/modelscope/evalscope/pull/1552) - refactor(web): isolate agent trace grouping from rendering by
[@Yunnglin](https://github.com/Yunnglin)in[#1568](https://github.com/modelscope/evalscope/pull/1568) - fix(perf): surface fatal request-building errors instead of swallowing or retrying them by
[@Yunnglin](https://github.com/Yunnglin)in[#1571](https://github.com/modelscope/evalscope/pull/1571) - fix(perf tests): repair stale local-endpoint perf tests (hang + outdated return contract) by
[@Yunnglin](https://github.com/Yunnglin)in[#1573](https://github.com/modelscope/evalscope/pull/1573) - fix(perf): abort request generation when a plugin returns None for the whole dataset by
[@Yunnglin](https://github.com/Yunnglin)in[#1574](https://github.com/modelscope/evalscope/pull/1574) - fix(perf): parse streaming usage independently of choices to fix 0 ca… by
[@OctoberGitHub](https://github.com/OctoberGitHub)in[#1572](https://github.com/modelscope/evalscope/pull/1572) - fix(judge): fail closed on [ERROR] judge responses and surface silent extraction paths by
[@YuhaoLin2005](https://github.com/YuhaoLin2005)in[#1576](https://github.com/modelscope/evalscope/pull/1576) - fix(gpqa): seed choice shuffle from the question so rerun-review is reproducible by
[@Yunnglin](https://github.com/Yunnglin)in[#1583](https://github.com/modelscope/evalscope/pull/1583) - fix(agent): limit SWE-bench toolcall nudge to once by
[@Roovelrz](https://github.com/Roovelrz)in[#1581](https://github.com/modelscope/evalscope/pull/1581) - feat(io): support
`parquet`

and binary image features in`general_vmcq`

by[@Moenupa](https://github.com/Moenupa)in[#1584](https://github.com/modelscope/evalscope/pull/1584) - fix(agent): make AgentLoop own the nudge count and give models an honest reminder by
[@Yunnglin](https://github.com/Yunnglin)in[#1585](https://github.com/modelscope/evalscope/pull/1585) - fix: enforce strict judge output parsing by
[@atirna](https://github.com/atirna)in[#1588](https://github.com/modelscope/evalscope/pull/1588) - feat(benchmark): add CountQA object counting benchmark by
[@Yunnglin](https://github.com/Yunnglin)in[#1590](https://github.com/modelscope/evalscope/pull/1590) - fix: correct self.dataset typo in VQA.info by
[@Ricardo-M-L](https://github.com/Ricardo-M-L)in[#1589](https://github.com/modelscope/evalscope/pull/1589) - feat(benchmark): add PhyX physical reasoning benchmark (phyx_mc, phyx_oe) by
[@Yunnglin](https://github.com/Yunnglin)in[#1593](https://github.com/modelscope/evalscope/pull/1593) - feat(benchmark): add SLAKE bilingual medical VQA benchmark by
[@Yunnglin](https://github.com/Yunnglin)in[#1592](https://github.com/modelscope/evalscope/pull/1592) - fix(perf): guard None content in openai_api token accounting by
[@tianba-sh](https://github.com/tianba-sh)in[#1591](https://github.com/modelscope/evalscope/pull/1591) - fix(bfcl): patch bfcl_eval FC handler to stop dropping empty-tool_cal… by
[@Dhru1001](https://github.com/Dhru1001)in[#1596](https://github.com/modelscope/evalscope/pull/1596) - fix(multi-choice): parse the last valid answer label instead of the first by
[@juzihan0459](https://github.com/juzihan0459)in[#1597](https://github.com/modelscope/evalscope/pull/1597) - feat(benchmarks): add native Indic-language benchmark adapters (milu,… by
[@Dhru1001](https://github.com/Dhru1001)in[#1569](https://github.com/modelscope/evalscope/pull/1569) - docs(api): fix message and tool documentation typos by
[@BingH225](https://github.com/BingH225)in[#1600](https://github.com/modelscope/evalscope/pull/1600) - feat(io): unify loading image/video/audio for
`general_vmcq`

by[@Moenupa](https://github.com/Moenupa)in[#1595](https://github.com/modelscope/evalscope/pull/1595) - feat(benchmark): add olmOCR-Bench document transcription benchmark by
[@ClaireXi99](https://github.com/ClaireXi99)in[#1598](https://github.com/modelscope/evalscope/pull/1598) - perf(service): memoize report-list metadata and support conditional GET by
[@Yunnglin](https://github.com/Yunnglin)in[#1607](https://github.com/modelscope/evalscope/pull/1607) - feat(benchmarks): Add Native Indic Benchmarks Phase 2 by
[@Dhru1001](https://github.com/Dhru1001)in[#1603](https://github.com/modelscope/evalscope/pull/1603) - refactor(judge): unify LLM judge scoring on a single JSON output contract by
[@Yunnglin](https://github.com/Yunnglin)in[#1601](https://github.com/modelscope/evalscope/pull/1601) - docs: clarify text-to-image metric selection by
[@MrChenfafafa](https://github.com/MrChenfafafa)in[#1612](https://github.com/modelscope/evalscope/pull/1612) - feat(eval): add native evaluation versioning ...

[Read more](https://github.com/modelscope/evalscope/releases/tag/v1.11.0)

## v1.10.0

## 中文版

### 基准测试数据集

- Agent 与自动化评测：新增 AutomationBench、DeepSearchQA、JobBench、BrowserGym MiniWoB 等评测能力
- 文档理解评测：新增 OmniDocBench v1.6 评测，并修复 OCR 相关兼容性

### 功能增强

- 性能测试：支持通过
`prefix_file`

/`prefix_role`

注入长上下文前缀；补充百分位统计最小值和平均延迟指标 - Web 界面：性能列表新增 I/O token 列，支持删除历史记录

### 文档优化

- 修正中文文档中的拼写和语法问题

### 问题修复

- 修复 IFBench 下载错误的 NLTK English tagger 问题
- 修复数学解析器中未保存
`str.replace()`

返回值的问题 - 修复 CMMLU few-shot 加载、ARC 答案格式、Windows UTF-8 文件读写等兼容性问题
- 修复异步事件循环和任务生命周期、Anthropic tool-call ID、每 subset 浮点数 limit 等问题
- 修复性能测试的调度截止、无固定速率 HTML 报告、非流式 TTFT/TPOT/ITL 指标和缓存 token 同步问题

## English Version

### Benchmark Datasets

- Agent and automation evaluation: Added AutomationBench, DeepSearchQA, JobBench, BrowserGym MiniWoB, and related capabilities
- Document understanding evaluation: Added OmniDocBench v1.6 and fixed OCR compatibility

### Feature Enhancements

- Performance testing: Added long-context prefix injection with
`prefix_file`

/`prefix_role`

, plus minimum percentile and average latency metrics - Web UI: Added I/O token columns to performance lists and history-record deletion

### Documentation

- Corrected spelling and grammar in Chinese documentation

### Bug Fixes

- Fixed IFBench downloading the incorrect NLTK English tagger
- Fixed math parsing where the result of
`str.replace()`

was discarded - Fixed CMMLU few-shot loading, ARC answer formatting, and Windows UTF-8 file I/O compatibility
- Fixed async event-loop and task lifecycle handling, Anthropic tool-call IDs, and per-subset float limits
- Fixed perf scheduling deadlines, HTML reports for no-fixed-rate runs, non-stream TTFT/TPOT/ITL metrics, and cached-token synchronization

## What's Changed

- fix(ifbench): download correct NLTK English tagger by
[@git-jxj](https://github.com/git-jxj)in[#1539](https://github.com/modelscope/evalscope/pull/1539) - fix: assign result of str.replace() in math parser by
[@LeoYueDev](https://github.com/LeoYueDev)in[#1536](https://github.com/modelscope/evalscope/pull/1536) - Fix OCR benchmark compatibility and add OmniDocBench v1.6 evaluation by
[@Yunnglin](https://github.com/Yunnglin)in[#1535](https://github.com/modelscope/evalscope/pull/1535) - Fix CMMLU few-shot loading by
[@Yunnglin](https://github.com/Yunnglin)in[#1534](https://github.com/modelscope/evalscope/pull/1534) - fix(docs): correct typos and grammar errors in Chinese documentation by
[@LeoYueDev](https://github.com/LeoYueDev)in[#1532](https://github.com/modelscope/evalscope/pull/1532) - feat(perf): long-context prefix injection via prefix_file/prefix_role by
[@Yunnglin](https://github.com/Yunnglin)in[#1531](https://github.com/modelscope/evalscope/pull/1531) - feat: add direct BrowserGym MiniWoB evaluation by
[@Yunnglin](https://github.com/Yunnglin)in[#1530](https://github.com/modelscope/evalscope/pull/1530) - fix: per-subset float limit and Anthropic tool call id sanitization by
[@Yunnglin](https://github.com/Yunnglin)in[#1528](https://github.com/modelscope/evalscope/pull/1528) - feat(web): I/O token column for perf list and history record deletion by
[@Yunnglin](https://github.com/Yunnglin)in[#1526](https://github.com/modelscope/evalscope/pull/1526) - fix: add encoding='utf-8' to remaining core file read/write for Windows compatibility by
[@Yunnglin](https://github.com/Yunnglin)in[#1522](https://github.com/modelscope/evalscope/pull/1522) - fix: performance test progress and cancellation handling, plus tokenizer path support by
[@duxingx1a](https://github.com/duxingx1a)in[#1520](https://github.com/modelscope/evalscope/pull/1520) - feat(perf): add min row to percentile table and label avg latency metrics by
[@Yunnglin](https://github.com/Yunnglin)in[#1517](https://github.com/modelscope/evalscope/pull/1517) - fix: normalise ARC answerKey digits to letters in arc_adapter by
[@duxingx1a](https://github.com/duxingx1a)in[#1516](https://github.com/modelscope/evalscope/pull/1516) - fix: add encoding='utf-8' to yaml_to_dict for Windows compatibility by
[@duxingx1a](https://github.com/duxingx1a)in[#1515](https://github.com/modelscope/evalscope/pull/1515) - fix(web): accept completed invoke status by
[@afox666](https://github.com/afox666)in[#1510](https://github.com/modelscope/evalscope/pull/1510) - Add JobBench benchmark by
[@Yunnglin](https://github.com/Yunnglin)in[#1509](https://github.com/modelscope/evalscope/pull/1509) - fix(perf): sync server-reported cached_tokens for single-turn runs by
[@Yunnglin](https://github.com/Yunnglin)in[#1508](https://github.com/modelscope/evalscope/pull/1508) - Fix async event loop and task lifecycle by
[@Yunnglin](https://github.com/Yunnglin)in[#1507](https://github.com/modelscope/evalscope/pull/1507) - Add AutomationBench benchmark by
[@Yunnglin](https://github.com/Yunnglin)in[#1505](https://github.com/modelscope/evalscope/pull/1505) - fix(perf): generate HTML report for open-loop runs with no fixed rate by
[@qiumuyang](https://github.com/qiumuyang)in[#1503](https://github.com/modelscope/evalscope/pull/1503) - Add DeepSearchQA benchmark by
[@Yunnglin](https://github.com/Yunnglin)in[#1502](https://github.com/modelscope/evalscope/pull/1502) - fix(perf): stop open-loop dispatch at duration deadline by
[@YingchaoX](https://github.com/YingchaoX)in[#1501](https://github.com/modelscope/evalscope/pull/1501) - fix(perf): exclude non-stream requests from TTFT/TPOT/ITL metrics by
[@qiumuyang](https://github.com/qiumuyang)in[#1499](https://github.com/modelscope/evalscope/pull/1499)

## v1.9.1

## 中文版

### 基准测试数据集

- 智能体评测: 新增 Claw-Eval (
[#1487](https://github.com/modelscope/evalscope/pull/1487))、ResearchRubrics ([#1478](https://github.com/modelscope/evalscope/pull/1478))、Toolathlon 智能体基准测试 - 多模态评测: 新增 TVBench 视频理解基准测试 (
[#1471](https://github.com/modelscope/evalscope/pull/1471)) - 通用评测: 新增 WideSearch、PerspectiveGap (
[#1461](https://github.com/modelscope/evalscope/pull/1461)) 基准测试

### 功能增强

- 性能测试: 新增 workload_trace 数据集插件，支持生产流量回放 (
[#1494](https://github.com/modelscope/evalscope/pull/1494)) - 性能测试: 统一
`--dataset-args`

参数，支持固定长度输入 ([#1483](https://github.com/modelscope/evalscope/issues/1483),[#1495](https://github.com/modelscope/evalscope/pull/1495)) - 性能测试: 新增
`/v1/rerank`

endpoint 支持 ([#1498](https://github.com/modelscope/evalscope/pull/1498)) - Web 服务: Dashboard 新增性能测试归档(archive)功能 (
[#1484](https://github.com/modelscope/evalscope/pull/1484)) - 模型支持: 支持 Anthropic prompt caching (
[#1444](https://github.com/modelscope/evalscope/pull/1444)) - 安全增强: 使用 SecretStr 对 eval / perf 密钥进行脱敏 (
[#1490](https://github.com/modelscope/evalscope/pull/1490)) - 性能优化: 重构 benchmark 数据集加载逻辑 (
[#1482](https://github.com/modelscope/evalscope/pull/1482))；优化 config 与 CLI 冷启动导入 ([#1491](https://github.com/modelscope/evalscope/pull/1491)) - 前端优化: 加固前端工作流与报告生成 (
[#1492](https://github.com/modelscope/evalscope/pull/1492))

### 问题修复

- 修复 evaluator 样本总数日志，并对 per-subset
`--limit`

给出警告 ([#1497](https://github.com/modelscope/evalscope/pull/1497)) - 修复 Windows 下代码执行评分问题 (
[#1488](https://github.com/modelscope/evalscope/pull/1488)) - 修复
`line_by_line`

数据集 dict body 字段处理 ([#1485](https://github.com/modelscope/evalscope/pull/1485)) - 修复多行 SSE 格式(id/event/data)解析问题 (
[#1474](https://github.com/modelscope/evalscope/pull/1474)) - 修复 trivia_qa prompt 及 repeats 格式化问题 (
[#1476](https://github.com/modelscope/evalscope/pull/1476)) - 修复 agent 沙箱命令超时未终止问题
- 修复 swe-bench 沙箱环境变量传递问题 (
[#1470](https://github.com/modelscope/evalscope/pull/1470)) - 修复 bfcl OpenAI base URL 归一化问题 (
[#1468](https://github.com/modelscope/evalscope/pull/1468)) - 修复 scicode 依赖，锁定 scipy < 1.14 (
[#1467](https://github.com/modelscope/evalscope/pull/1467)) - 修复 openai 流式响应中断重试问题 (
[#1464](https://github.com/modelscope/evalscope/pull/1464)) - 修复 openai 流式 TTFT 未包含 delta.reasoning 的问题 (
[#1463](https://github.com/modelscope/evalscope/pull/1463)) - 修复 sandbox manager stop 失败后的资源清理问题 (
[#1465](https://github.com/modelscope/evalscope/pull/1465))

## English Version

### Benchmark Datasets

- Agent Evaluation: Added Claw-Eval (
[#1487](https://github.com/modelscope/evalscope/pull/1487)), ResearchRubrics ([#1478](https://github.com/modelscope/evalscope/pull/1478)), and Toolathlon agent benchmarks - Multimodal Evaluation: Added TVBench video understanding benchmark (
[#1471](https://github.com/modelscope/evalscope/pull/1471)) - General Evaluation: Added WideSearch and PerspectiveGap (
[#1461](https://github.com/modelscope/evalscope/pull/1461)) benchmarks

### Feature Enhancements

- Performance Testing: Added workload_trace dataset plugin for production traffic replay (
[#1494](https://github.com/modelscope/evalscope/pull/1494)) - Performance Testing: Unified
`--dataset-args`

with fixed-length input support ([#1483](https://github.com/modelscope/evalscope/issues/1483),[#1495](https://github.com/modelscope/evalscope/pull/1495)) - Performance Testing: Added
`/v1/rerank`

endpoint support ([#1498](https://github.com/modelscope/evalscope/pull/1498)) - Web Service: Added performance benchmark archive to the dashboard (
[#1484](https://github.com/modelscope/evalscope/pull/1484)) - Model Support: Added Anthropic prompt caching support (
[#1444](https://github.com/modelscope/evalscope/pull/1444)) - Security: Masked eval / perf secrets with SecretStr (
[#1490](https://github.com/modelscope/evalscope/pull/1490)) - Performance: Refactored benchmark dataset loading (
[#1482](https://github.com/modelscope/evalscope/pull/1482)); refined config and CLI cold-start imports ([#1491](https://github.com/modelscope/evalscope/pull/1491)) - Frontend: Hardened frontend workflows and reporting (
[#1492](https://github.com/modelscope/evalscope/pull/1492))

### Bug Fixes

- Fixed resolved sample total logging and added warning for per-subset
`--limit`

([#1497](https://github.com/modelscope/evalscope/pull/1497)) - Fixed code execution scoring on Windows (
[#1488](https://github.com/modelscope/evalscope/pull/1488)) - Fixed dict body field handling in line_by_line dataset (
[#1485](https://github.com/modelscope/evalscope/pull/1485)) - Fixed multi-line SSE parsing with id, event, and data fields (
[#1474](https://github.com/modelscope/evalscope/pull/1474)) - Fixed trivia_qa prompt and repeats formatting (
[#1476](https://github.com/modelscope/evalscope/pull/1476)) - Fixed agent sandbox commands not terminating on timeout
- Fixed sandbox environment variable passing for swe-bench (
[#1470](https://github.com/modelscope/evalscope/pull/1470)) - Fixed OpenAI base URL normalization for bfcl (
[#1468](https://github.com/modelscope/evalscope/pull/1468)) - Fixed scicode dependency by pinning scipy below 1.14 (
[#1467](https://github.com/modelscope/evalscope/pull/1467)) - Fixed retry on interrupted OpenAI streaming responses (
[#1464](https://github.com/modelscope/evalscope/pull/1464)) - Fixed missing delta.reasoning in OpenAI streaming TTFT (
[#1463](https://github.com/modelscope/evalscope/pull/1463)) - Fixed resource cleanup after sandbox manager stop failure (
[#1465](https://github.com/modelscope/evalscope/pull/1465))

## v1.9.0

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
- Agent API: 将
`run_agent_loop`

移动到`evalscope.api.agent`

，作为公开 API 使用 - 适配器架构: 重构 benchmark adapter 架构，新增
`AudioLanguageAdapter`

、统一`FunctionCallAdapter`

，并合并`AgentLoopAdapter`

- 性能测试: 支持 CPU 密集型请求生成并行化，提升 perf 请求构造效率
- 性能测试数据加载: 统一通过
`--data-source`

参数加载 perf 数据源，简化多数据集配置

### 文档优化

- 新增和更新多个 benchmark 文档、supported dataset 列表、Agent 使用文档和 SkillsBench 第三方文档
- 更新性能测试相关参数文档和多轮压测说明
- 更新 ThinkEval 相关最佳实践文档

### 问题修复

- 修复 SWE-bench 架构选择问题和 sandbox 登录 shell 执行问题
- 修复 ASR 评测中 filters 未在 WER 评分前生效的问题
- 修复 perf 在 OpenAI usage 缺少
`completion_tokens`

时的兼容性问题 - 修复 perf 多轮压测绝对时间速率调度和 event loop 关闭问题
- 修复 LiveCodeBench stdin buffer 支持问题
- 修复 ThinkBench 对新
`ReviewResult`

格式的适配问题 - 修复 GPQA answer choices 被括号清理正则错误截断的问题
- 修复 OpenAI-compatible streaming 聚合问题
- 修复 tau3_bench 在 completion usage 缺失时崩溃的问题

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
- Agent API: Moved
`run_agent_loop`

to`evalscope.api.agent`

as a public API - Adapter Architecture: Refactored benchmark adapter architecture with
`AudioLanguageAdapter`

, unified`FunctionCallAdapter`

, and merged`AgentLoopAdapter`

- Performance Testing: Parallelized CPU-bound request generation to improve perf workload preparation
- Performance Data Loading: Unified perf dataset loading through the
`--data-source`

parameter for simpler dataset configuration

### Documentation

- Added and updated benchmark documentation, supported dataset lists, Agent user guides, and SkillsBench third-party documentation
- Updated performance testing parameter documentation and multi-turn stress testing guides
- Updated ThinkEval best practice documentation

### Bug Fixes

- Fixed SWE-bench architecture selection and login shell execution in sandboxes
- Fixed ASR filters so they are applied before WER scoring
- Fixed compatibility when OpenAI usage blocks are missing
`completion_tokens`

- Fixed absolute-time rate scheduling and event loop closing for multi-turn perf tests
- Fixed stdin buffer support in LiveCodeBench
- Fixed ThinkBench compatibility with the new
`ReviewResult`

format - Fixed GPQA answer choice corruption caused by bracket-stripping regex
- Fixed OpenAI-compatible streaming aggregation
- Fixed tau3_bench crash when completion usage is missing

## What's Changed

- fix SWE-bench architecture selection by
[@Yunnglin](https://github.com/Yunnglin)in[#1419](https://github.com/modelscope/evalscope/pull/1419) - Add LongMemEval benchmark by
[@Yunnglin](https://github.com/Yunnglin)in[#1420](https://github.com/modelscope/evalscope/pull/1420) - Add LoCoMo QA benchmark by
[@Yunnglin](https://github.com/Yunnglin)in[#1422](https://github.com/modelscope/evalscope/pull/1422) - Add BrowseComp benchmark support by
[@haoruilee](https://github.com/haoruilee)in[#1421](https://github.com/modelscope/evalscope/pull/1421) - Add SWE-bench Multilingual agentic benchmark by
[@Yunnglin](https://github.com/Yunnglin)in[#1426](https://github.com/modelscope/evalscope/pull/1426) - feat: add BigCodeBench and BigCodeBench-Hard benchmark support by
[@Yunnglin](https://github.com/Yunnglin)in[#1425](https://github.com/modelscope/evalscope/pull/1425) - refactor: move run_agent_loop to evalscope.api.agent as public API by
[@Yunnglin](https://github.com/Yunnglin)in[#1427](https://github.com/modelscope/evalscope/pull/1427) - refactor: restructure adapter architecture - AudioLanguageAdapter, FunctionCallAdapter, merge AgentLoopAdapter by
[@Yunnglin](https://github.com/Yunnglin)in[#1428](https://github.com/modelscope/evalscope/pull/1428) - Fix ASR filters before WER scoring by
[@haoruilee](https://github.com/haoruilee)in[#1431](https://github.com/modelscope/evalscope/pull/1431) - fix(perf): tolerate missing completion_tokens in OpenAI usage block by
[@angelynaye](https://github.com/angelynaye)in[#1432](https://github.com/modelscope/evalscope/pull/1432) - feat(agent): add OpenCode and OpenHands runners with Dockerfiles by
[@Yunnglin](https://github.com/Yunnglin)in[#1429](https://github.com/modelscope/evalscope/pull/1429) - fix: support stdin buffer in LiveCodeBench by
[@Yunnglin](https://github.com/Yunnglin)in[#1438](https://github.com/modelscope/evalscope/pull/1438) - fix: adapt thinkbench to new ReviewResult format by
[@Yunnglin](https://github.com/Yunnglin)in[#1439](https://github.com/modelscope/evalscope/pull/1439) - fix(perf): absolute-time rate scheduling for multi-turn + close event loop by
[@Yunnglin](https://github.com/Yunnglin)in[#1442](https://github.com/modelscope/evalscope/pull/1442) - Add GDPval benchmark integration by
[@Yunnglin](https://github.com/Yunnglin)in[#1441](https://github.com/modelscope/evalscope/pull/1441) - (feat) Parallelize CPU-bound perf request generation by
[@haoruilee](https://github.com/haoruilee)in[#1440](https://github.com/modelscope/evalscope/pull/1440) - fix(gpqa): remove bracket-stripping regex that corrupts answer choices by
[@Yunnglin](https://github.com/Yunnglin)in[#1448](https://github.com/modelscope/evalscope/pull/1448) - Add MCP-Atlas benchmark integration by
[@Yunnglin](https://github.com/Yunnglin)in[#1445](https://github.com/modelscope/evalscope/pull/1445) - feat(perf): unify dataset loading with --data-source parameter by
[@Yunnglin](https://github.com/Yunnglin)in[#1449](https://github.com/modelscope/evalscope/pull/1449) - feat: add ERQA and WorldVQA benchmarks by
[@Yunnglin](https://github.com/Yunnglin)in[#1453](https://github.com/modelscope/evalscope/pull/1453) - Fix OpenAI-compatible streaming aggregation by
[@kaede316](https://github.com/kaede316)in[#1450](https://github.com/modelscope/evalscope/pull/1450) - feat(benchmarks): add CharXiv and BabyVision benchmarks by
[@Yunnglin](https://github.com/Yunnglin)in[#1454](https://github.com/modelscope/evalscope/pull/1454) - feat(benchmarks): add arxivmath, cmath, hmmt26 and imo_answerbench benchmarks by
[@Yunnglin](https://github.com/Yunnglin)in[#1455](https://github.com/modelscope/evalscope/pull/1455) - feat(benchmarks): add officeqa, agieval, arc_agi_2 benchmarks by
[@Yunnglin](https://github.com/Yunnglin)in[#1458](https://github.com/modelscope/evalscope/pull/1458) - fix(agent): use login shell for SWE-bench sandboxes by
[@haoruilee](https://github.com/haoruilee)in[#1457](https://github.com/modelscope/evalscope/pull/1457) - feat(benchmark): add DeepSWE adapter by
[@Yunnglin](https://github.com/Yunnglin)in[#1459](https://github.com/modelscope/evalscope/pull/1459) - feat(benchmarks): add EmbSpatial-Bench, KINA, and MeasureBench benchmarks by
[@Yunnglin](https://github.com/Yunnglin)in[#1460](https://github.com/modelscope/evalscope/pull/1460) - Fix tau3_bench crash when completion usage is missing by
[@danielliu99](https://github.com/danielliu99)in[#1462](https://github.com/modelscope/evalscope/pull/1462) - Add native SkillsBench runner support by
[@Yunnglin](https://github.com/Yunnglin)in[#1451](https://github.com/modelscope/evalscope/pull/1451)

## New Contributors

[@angelynaye](https://github.com/angelynaye)made their first contribution in[#1432](https://github.com/modelscope/evalscope/pull/1432)[@kaede316](https://github.com/kaede316)made their first contribution in[#1450](https://github.com/modelscope/evalscope/pull/1450)[@danielliu99](https://github.com/danielliu99)made their first contribution in[#1462](https://github.com/modelscope/evalscope/pull/1462)

**Full Changelog**: `v1.8.1...v1.9.0`

## v1.8.1

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
- 修复多轮对话中
`reasoning_content`

未作为顶层字段透传的问题 - 修复
`service`

optional-dependencies 中缺少 perf 依赖的问题 - 修复 RAG API encoder/reranker 中超过
`max_seq_length`

的文本截断问题 - 修复 agent bash 工具 stdout 空白字符保留问题，避免 patch 内容损坏
- 修复 Windows 环境下缓存写入可能触发
`PermissionError`

的问题

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
- Fixed forwarding
`reasoning_content`

as a top-level field in multi-turn conversations - Fixed missing perf dependencies in
`service`

optional-dependencies - Fixed truncation for texts exceeding
`max_seq_length`

in RAG API encoder/reranker - Fixed stdout whitespace preservation in agent bash tool to prevent patch corruption
- Fixed possible Windows
`PermissionError`

when writing cache files

## What's Changed

- fix(scicode): read assistant text blocks by
[@he-yufeng](https://github.com/he-yufeng)in[#1381](https://github.com/modelscope/evalscope/pull/1381) - add seed_tts_eval benchmark, solve
[#1360](https://github.com/modelscope/evalscope/issues/1360)by[@haoruilee](https://github.com/haoruilee)in[#1379](https://github.com/modelscope/evalscope/pull/1379) - feat(benchmarks): add ACEBench support, fix
[#1025](https://github.com/modelscope/evalscope/issues/1025)by[@haoruilee](https://github.com/haoruilee)in[#1386](https://github.com/modelscope/evalscope/pull/1386) - fix(terminal_bench): check docker cli before trials by @Li-Bailiang in
[#1389](https://github.com/modelscope/evalscope/pull/1389) - refactor(rag_eval): MTEB 2.x + RAGAS 0.4.x + Pydantic configs by
[@Yunnglin](https://github.com/Yunnglin)in[#1383](https://github.com/modelscope/evalscope/pull/1383) - add Maritime-OCR-Bench support by
[@K-zhy](https://github.com/K-zhy)in[#1388](https://github.com/modelscope/evalscope/pull/1388) - fix(models): forward reasoning_content as top-level field in multi-turn by
[@Yunnglin](https://github.com/Yunnglin)in[#1396](https://github.com/modelscope/evalscope/pull/1396) - fix: include perf deps in
`service`

optional-dependencies by[@Blackteaxx](https://github.com/Blackteaxx)in[#1398](https://github.com/modelscope/evalscope/pull/1398) - Add caption benchmarks by
[@haoruilee](https://github.com/haoruilee)in[#1402](https://github.com/modelscope/evalscope/pull/1402) - fix(rag): truncate texts exceeding max_seq_length in API encoder/reranker by
[@Yunnglin](https://github.com/Yunnglin)in[#1407](https://github.com/modelscope/evalscope/pull/1407) - fix(agent): preserve stdout whitespace in bash tool to prevent patch corruption by
[@Yunnglin](https://github.com/Yunnglin)in[#1409](https://github.com/modelscope/evalscope/pull/1409) - fix(cache): use persistent jsonl writer to avoid Windows PermissionError by
[@Yunnglin](https://github.com/Yunnglin)in[#1410](https://github.com/modelscope/evalscope/pull/1410) - feat: allow custom DockerHub namespace for SWE-Bench images by
[@Yunnglin](https://github.com/Yunnglin)in[#1417](https://github.com/modelscope/evalscope/pull/1417) - feat(metric): add full-reference image quality metrics by
[@haoruilee](https://github.com/haoruilee)in[#1412](https://github.com/modelscope/evalscope/pull/1412)

## New Contributors

[@he-yufeng](https://github.com/he-yufeng)made their first contribution in[#1381](https://github.com/modelscope/evalscope/pull/1381)- @Li-Bailiang made their first contribution in
[#1389](https://github.com/modelscope/evalscope/pull/1389) [@Blackteaxx](https://github.com/Blackteaxx)made their first contribution in[#1398](https://github.com/modelscope/evalscope/pull/1398)

**Full Changelog**: `v1.8.0...v1.8.1`

## v1.8.0

## 中文版

### 基准测试数据集

- Agent 评测: 新增 SWE-Bench Pro、Tau3-Bench、GAIA、Terminal-Bench v2.1 等 Agent 能力评测基准
- 通用评测: 新增 ArxivRollBench 学术论文理解基准测试
- 厂商验证评测: 新增 k2、kimi、minimax 等厂商验证器基准测试

### 功能增强

- OpenAI Responses API: 新增 OpenAI Responses API 支持 (Issue
[#1192](https://github.com/modelscope/evalscope/issues/1192)) - API Reranker 评测: 支持 API reranker 评测能力 (Issue
[#1029](https://github.com/modelscope/evalscope/issues/1029)) - Agent Bridge: 新增 Agent Bridge 功能及 WebUI 更新
- MCP Server 支持: NativeAgentConfig 支持配置 MCP server
- 图片压缩: 新增多模态评测可配置图片压缩功能
- 性能测试 - Trie 回放: 支持 trie agentic trace replay、Turn 模型及 --duration 参数
- 性能测试 - SwanLab: 支持自部署 SwanLab 的 swanlab_host 配置

### 文档优化

- 统一 agent 相关指引至 AGENTS.md

### 问题修复

- 修复 build_docker_images 未优先 subset 数据集的问题 (
[#1348](https://github.com/modelscope/evalscope/pull/1348)) - 修复 tokenizer 加载时 max_position_embeddings AttributeError (
[#1354](https://github.com/modelscope/evalscope/pull/1354)) - 修复 livecodebench 数据集迁移至 ModelScope parquet 格式 (
[#1357](https://github.com/modelscope/evalscope/pull/1357)) - 修复 DatasetDict.from_dataset 中 repeats 参数无效的问题 (
[#1363](https://github.com/modelscope/evalscope/pull/1363)) - 修复 perf open-loop / rate-paced 模式下实际 QPS 不稳定的问题 (
[#1367](https://github.com/modelscope/evalscope/pull/1367)) - 修复 perf SLA 多轮平均后整数字段未取整的问题 (
[#1370](https://github.com/modelscope/evalscope/pull/1370)) - 修复 agent sandbox 中 ms_enclave 缺失时未快速失败的问题 (
[#1372](https://github.com/modelscope/evalscope/pull/1372))

## English Version

### Benchmark Datasets

- Agent Evaluation: Added SWE-Bench Pro, Tau3-Bench, GAIA, Terminal-Bench v2.1 for agent capability assessment
- General Evaluation: Added ArxivRollBench for academic paper comprehension
- Vendor Verifier: Added k2, kimi, minimax vendor verifier benchmarks

### Feature Enhancements

- OpenAI Responses API: Added OpenAI Responses API support (Issue
[#1192](https://github.com/modelscope/evalscope/issues/1192)) - API Reranker Evaluation: Added support for API reranker evaluation (Issue
[#1029](https://github.com/modelscope/evalscope/issues/1029)) - Agent Bridge: Added Agent Bridge functionality with WebUI update
- MCP Server Support: Added MCP server configuration for NativeAgentConfig
- Image Compression: Added configurable image compression for VLM benchmarks
- Perf - Trie Replay: Added trie agentic trace replay, Turn model, and --duration parameter
- Perf - SwanLab: Added swanlab_host support for self-hosted SwanLab deployments

### Documentation

- Unified agent instructions into AGENTS.md

### Bug Fixes

- Fixed build_docker_images check to always subset dataset first (
[#1348](https://github.com/modelscope/evalscope/pull/1348)) - Fixed max_position_embeddings AttributeError in tokenizer loading (
[#1354](https://github.com/modelscope/evalscope/pull/1354)) - Fixed livecodebench migration to parquet dataset on ModelScope (
[#1357](https://github.com/modelscope/evalscope/pull/1357)) - Fixed ineffective repeats in DatasetDict.from_dataset (
[#1363](https://github.com/modelscope/evalscope/pull/1363)) - Fixed unstable realised QPS in open-loop / rate-paced benchmarks (
[#1367](https://github.com/modelscope/evalscope/pull/1367)) - Fixed int fields rounding after SLA multi-run averaging (
[#1370](https://github.com/modelscope/evalscope/pull/1370)) - Fixed fail-fast in EnclaveAgentEnvironment when ms_enclave is missing (
[#1372](https://github.com/modelscope/evalscope/pull/1372))

## What's Changed

- core: fix build_docker_images check to always subset dataset first by
[@liguodongiot](https://github.com/liguodongiot)in[#1348](https://github.com/modelscope/evalscope/pull/1348) - [Update] old agent benchmarks by
[@Yunnglin](https://github.com/Yunnglin)in[#1349](https://github.com/modelscope/evalscope/pull/1349) - perf: support swanlab_host for self-hosted SwanLab deployments by
[@Yunnglin](https://github.com/Yunnglin)in[#1350](https://github.com/modelscope/evalscope/pull/1350) - [Benchmark] Add SWE-Bench pro and Tau3-Bench by
[@Yunnglin](https://github.com/Yunnglin)in[#1351](https://github.com/modelscope/evalscope/pull/1351) - Add OpenAI Responses API support, solve
[#1192](https://github.com/modelscope/evalscope/issues/1192)by[@haoruilee](https://github.com/haoruilee)in[#1352](https://github.com/modelscope/evalscope/pull/1352) - docs: unify agent instructions into AGENTS.md by
[@Yunnglin](https://github.com/Yunnglin)in[#1353](https://github.com/modelscope/evalscope/pull/1353) - fix: handle max_position_embeddings AttributeError in tokenizer loading by
[@Yunnglin](https://github.com/Yunnglin)in[#1354](https://github.com/modelscope/evalscope/pull/1354) - feat: add configurable image compression for VLM benchmarks by
[@Yunnglin](https://github.com/Yunnglin)in[#1355](https://github.com/modelscope/evalscope/pull/1355) - fix: migrate livecodebench to parquet dataset on ModelScope by
[@Yunnglin](https://github.com/Yunnglin)in[#1357](https://github.com/modelscope/evalscope/pull/1357) - [Fix] Fix ineffective repeats in DatasetDict.from_dataset by
[@we1sper](https://github.com/we1sper)in[#1363](https://github.com/modelscope/evalscope/pull/1363) - fix(perf): stabilise realised QPS in open-loop / rate-paced benchmarks by
[@Syqinx](https://github.com/Syqinx)in[#1367](https://github.com/modelscope/evalscope/pull/1367) - [Feature] Add agent bridge and webui update by
[@Yunnglin](https://github.com/Yunnglin)in[#1364](https://github.com/modelscope/evalscope/pull/1364) - fix(agent/sandbox): fail-fast in EnclaveAgentEnvironment when ms_enclave is missing by
[@Yunnglin](https://github.com/Yunnglin)in[#1372](https://github.com/modelscope/evalscope/pull/1372) - feat: GAIA benchmark + MCP server support for NativeAgentConfig by
[@Yunnglin](https://github.com/Yunnglin)in[#1371](https://github.com/modelscope/evalscope/pull/1371) - [Benchmark] Add ArxivRollBench by
[@liangzid](https://github.com/liangzid)in[#1365](https://github.com/modelscope/evalscope/pull/1365) - fix(perf): round int fields after sla multi-run averaging by
[@qiumuyang](https://github.com/qiumuyang)in[#1370](https://github.com/modelscope/evalscope/pull/1370) - feat(benchmarks): add k2/kimi/minimax vendor verifier benchmarks by
[@Yunnglin](https://github.com/Yunnglin)in[#1375](https://github.com/modelscope/evalscope/pull/1375) - feat(perf): trie agentic trace replay + Turn model + --duration by
[@Yunnglin](https://github.com/Yunnglin)in[#1374](https://github.com/modelscope/evalscope/pull/1374) - feat(benchmarks): add Terminal-Bench v2.1 + upgrade harbor integration by
[@Yunnglin](https://github.com/Yunnglin)in[#1376](https://github.com/modelscope/evalscope/pull/1376) - feat: support API reranker evaluation, fix
[#1029](https://github.com/modelscope/evalscope/issues/1029)by[@haoruilee](https://github.com/haoruilee)in[#1377](https://github.com/modelscope/evalscope/pull/1377)

## New Contributors

[@liguodongiot](https://github.com/liguodongiot)made their first contribution in[#1348](https://github.com/modelscope/evalscope/pull/1348)[@we1sper](https://github.com/we1sper)made their first contribution in[#1363](https://github.com/modelscope/evalscope/pull/1363)[@Syqinx](https://github.com/Syqinx)made their first contribution in[#1367](https://github.com/modelscope/evalscope/pull/1367)[@liangzid](https://github.com/liangzid)made their first contribution in[#1365](https://github.com/modelscope/evalscope/pull/1365)[@qiumuyang](https://github.com/qiumuyang)made their first contribution in[#1370](https://github.com/modelscope/evalscope/pull/1370)

**Full Changelog**: `v1.7.1...v1.8.0`

## v1.7.1

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

- [Feature]Refact webui and multi-turn eval by
[@Yunnglin](https://github.com/Yunnglin)in[#1315](https://github.com/modelscope/evalscope/pull/1315) - feat: add LiteLLM as AI gateway provider by
[@RheagalFire](https://github.com/RheagalFire)in[#1317](https://github.com/modelscope/evalscope/pull/1317) - [Feature]Add perf swe-smith by
[@Yunnglin](https://github.com/Yunnglin)in[#1321](https://github.com/modelscope/evalscope/pull/1321) - [Fix] perf swe-smith by
[@Yunnglin](https://github.com/Yunnglin)in[#1322](https://github.com/modelscope/evalscope/pull/1322) - [Fix] perf swe-smith load by
[@Yunnglin](https://github.com/Yunnglin)in[#1323](https://github.com/modelscope/evalscope/pull/1323) - [Fix] perf swe multi process by
[@Yunnglin](https://github.com/Yunnglin)in[#1324](https://github.com/modelscope/evalscope/pull/1324) - [Feature]Update web and docs by
[@Yunnglin](https://github.com/Yunnglin)in[#1326](https://github.com/modelscope/evalscope/pull/1326) - [Feature] Add perf warmup by
[@Yunnglin](https://github.com/Yunnglin)in[#1329](https://github.com/modelscope/evalscope/pull/1329) - [Fix]update aigc device args by
[@Yunnglin](https://github.com/Yunnglin)in[#1336](https://github.com/modelscope/evalscope/pull/1336) - Add local-only loading switch for T2V metric assets by
[@AuFlow](https://github.com/AuFlow)in[#1334](https://github.com/modelscope/evalscope/pull/1334) - [update] volcengine sandbox by
[@Yunnglin](https://github.com/Yunnglin)in[#1337](https://github.com/modelscope/evalscope/pull/1337) - [Feature]Add multi-mcq by
[@Yunnglin](https://github.com/Yunnglin)in[#1345](https://github.com/modelscope/evalscope/pull/1345) - [Feature] Add AIR-Bench benchmark support by
[@haoruilee](https://github.com/haoruilee)in[#1341](https://github.com/modelscope/evalscope/pull/1341) - support line_by_line_oai custom dataset mode by
[@llc-kc](https://github.com/llc-kc)in[#1342](https://github.com/modelscope/evalscope/pull/1342) - [Feature] Add native video benchmark support with MVBench and Video-MME-v2 by
[@haoruilee](https://github.com/haoruilee)in[#1343](https://github.com/modelscope/evalscope/pull/1343) - [Feature]Add agent loop by
[@Yunnglin](https://github.com/Yunnglin)in[#1344](https://github.com/modelscope/evalscope/pull/1344) - [Fix] ifbench eval logic by
[@Yunnglin](https://github.com/Yunnglin)in[#1346](https://github.com/modelscope/evalscope/pull/1346)

## New Contributors

[@RheagalFire](https://github.com/RheagalFire)made their first contribution in[#1317](https://github.com/modelscope/evalscope/pull/1317)[@AuFlow](https://github.com/AuFlow)made their first contribution in[#1334](https://github.com/modelscope/evalscope/pull/1334)[@haoruilee](https://github.com/haoruilee)made their first contribution in[#1341](https://github.com/modelscope/evalscope/pull/1341)[@llc-kc](https://github.com/llc-kc)made their first contribution in[#1342](https://github.com/modelscope/evalscope/pull/1342)

**Full Changelog**: `v1.6.1...v1.7.1`

## v1.6.1

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

- [Feature] Add tokenize prompt switch by
[@Yunnglin](https://github.com/Yunnglin)in[#1289](https://github.com/modelscope/evalscope/pull/1289) - Feat/support p50 p90 percentiles by
[@yonlunwu](https://github.com/yonlunwu)in[#1283](https://github.com/modelscope/evalscope/pull/1283) - update log filehandler by
[@Yunnglin](https://github.com/Yunnglin)in[#1292](https://github.com/modelscope/evalscope/pull/1292) - [Fix] load default local dataset by
[@Yunnglin](https://github.com/Yunnglin)in[#1293](https://github.com/modelscope/evalscope/pull/1293) - [Benchmark] Add TIR-Bench by
[@Yunnglin](https://github.com/Yunnglin)in[#1295](https://github.com/modelscope/evalscope/pull/1295) - [Feature]Add multi turn perf by
[@Yunnglin](https://github.com/Yunnglin)in[#1298](https://github.com/modelscope/evalscope/pull/1298) - Ensure output directory is created automatically when dumping JSONL files by
[@ShaohonChen](https://github.com/ShaohonChen)in[#1296](https://github.com/modelscope/evalscope/pull/1296) - Fix tokenize-prompt length semantics by
[@zongjing1998](https://github.com/zongjing1998)in[#1301](https://github.com/modelscope/evalscope/pull/1301) - [Feature]update time zone by
[@Yunnglin](https://github.com/Yunnglin)in[#1303](https://github.com/modelscope/evalscope/pull/1303) - [Feature] Add speculative perf metrics by
[@Yunnglin](https://github.com/Yunnglin)in[#1306](https://github.com/modelscope/evalscope/pull/1306) - feat: 更新plot的cdn地址，避免网络加速后访问异常 by
[@ZhengYingqian](https://github.com/ZhengYingqian)in[#1308](https://github.com/modelscope/evalscope/pull/1308) - [Feature] Add custom multi_turn perf by
[@Yunnglin](https://github.com/Yunnglin)in[#1309](https://github.com/modelscope/evalscope/pull/1309) - [Feature] Add perf in eval by
[@Yunnglin](https://github.com/Yunnglin)in[#1310](https://github.com/modelscope/evalscope/pull/1310) - [Fix] tokenize template issue by
[@Yunnglin](https://github.com/Yunnglin)in[#1311](https://github.com/modelscope/evalscope/pull/1311)

## New Contributors

[@yonlunwu](https://github.com/yonlunwu)made their first contribution in[#1283](https://github.com/modelscope/evalscope/pull/1283)[@zongjing1998](https://github.com/zongjing1998)made their first contribution in[#1301](https://github.com/modelscope/evalscope/pull/1301)

**Full Changelog**: `v1.6.0...v1.6.1`