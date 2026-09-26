# [Issue #951] [🎯 Roadmap] EvalScope Roadmap

source: https://github.com/modelscope/evalscope/issues/951
state: open | updated: 2026-09-07T09:26:25Z
labels: 

## 正文

## English Version

### Planned Benchmarks Support

#### 1. Agent
- [x] 𝜏²-Bench #959
- [x] Terminal-Bench
- [x] BrowseComp #1026
- [x] acebench #1025
- [x] τ³-bench #1272

#### 2. Code
- [x] Multi-E
- [x] SciCode
- [x] SWE-Bench #976
- [x] CodeForces #520 #914
- [x] Aider #520
- [x] SWE-Bench Multilingual #1024
- [x] SWE-Bench Pro #1210

#### 3. Instruction Following
- [x] IFBench

#### 4. Vision Language
- [x] Refcoco
- [x] MVBench
- [x] Video-MME-v2
- [x] CC-OCR
- [x] Caption datasets (MSVD / MSR-VTT / VQAv2) #495 #936
- [x] Olmocr-Bench #944

#### 5. Audio
- [x] fleurs
- [x] Common Voice 15 / WenetSpeech / MMAU, etc. #1181

#### 6. Chinese / Domain
- [x] LawBench #527
- [x] FewCLUE / cluewsc #618

#### 7. Safety
- [ ] Safety / compliance benchmarks #197 #742

### Features

- [x] **Performance Testing Enhancement**: Support dynamic concurrency adjustment and automatic testing of model service metrics including minimum latency, TTFT (Time To First Token), and maximum throughput
- [x] **Extended Evaluation Metrics**: Add support for more evaluation metrics, including cons@k, G-pass@k, etc.
- [x] **Function Call & Tool Use**: Add support for evaluating customized scenarios of function-call and tool-use
- [ ] **Prompt Management Optimization**: Improve prompt management to facilitate setting different prompts for benchmarks
- [ ] **Safety Benchmarks**: Support safety-related benchmarks (suggestions for datasets are welcome)
- [x] **UI Development**: Develop an interactive UI interface for visual model evaluation (long-term goal)
- [x] **Benchmark Collection**: More comprehensive support of benchmarking Collection for evaluating indexed benchmark suites
- [x] Stress testing support for embedding model services
- [x] **Image quality metrics**: SSIM / PSNR / LPIPS image evaluation metrics #770
- [ ] **Reranker via API**: Support invoking reranker through API #1029
- [x] **OpenAI Responses API**: Support stress testing and evaluation under the Responses protocol #1192

### Bug Fixes

1. **Embedding Model Evaluation**: Fix benchmark misalignment issue in embedding model evaluation
   Issue: https://github.com/modelscope/evalscope/issues/753
2. **RAG Evaluation**: Fix the issue where evaluation sets cannot be automatically constructed in rageval
   Issue: https://github.com/modelscope/evalscope/issues/859

---

## 中文版本

### 计划支持的基准测试

#### 1. Agent（智能体）
- [x] 𝜏²-Bench #959
- [x] Terminal-Bench
- [x] BrowseComp #1026
- [x] acebench #1025
- [x] τ³-bench #1272

#### 2. Code（代码）
- [x] Multi-E
- [x] SciCode
- [x] SWE-Bench #976
- [x] CodeForces #520 #914
- [x] Aider #520
- [x] SWE-Bench Multilingual #1024
- [x] SWE-Bench Pro #1210

#### 3. Instruction Following（指令遵循）
- [x] IFBench

#### 4. Vision Language（视觉语言）
- [x] Refcoco
- [x] MVBench
- [x] Video-MME-v2
- [x] CC-OCR
- [x] Caption 数据集 (MSVD / MSR-VTT / VQAv2) #495 #936
- [x] Olmocr-Bench #944

#### 5. Audio（音频）
- [x] fleurs
- [x] Common Voice 15 / WenetSpeech / MMAU 等 #1181

#### 6. Chinese / Domain（中文/领域）
- [x] LawBench #527
- [x] FewCLUE / cluewsc #618

#### 7. Safety（安全）
- [ ] Safety / compliance 数据集 #197 #742

### 功能特性

- [x] **性能测试增强**：支持动态调整并发，自动测试模型服务的最低时延、TTFT（首字时延）、最高吞吐量等指标
- [x] **扩展评测指标**：支持更多的评测指标，包括 cons@k、G-pass@k 等
- [x] **函数调用与工具使用**：支持评测自定义场景的函数调用（function-call）和工具使用（tool-use）
- [ ] **Prompt 管理优化**：优化 prompt 管理，方便为不同 benchmark 设置不同的 prompt
- [ ] **安全基准测试**：支持 safety 相关 benchmark（欢迎提供想要支持的数据集）
- [x] **UI 界面开发**：开发 UI 交互界面，用可视化的方式进行模型评测（长期目标）
- [x] **基准测试集合**：更全面地支持 Benchmarking Collection，用于评测基准测试套件
- [x] 支持 embedding 模型服务的压测
- [x] **图像质量指标**：支持 SSIM / PSNR / LPIPS 等图像评测指标 #770
- [ ] **Reranker API 调用**：支持通过 API 方式调用 reranker #1029
- [x] **OpenAI Responses API**：支持 Responses 协议的压测与评测 #1192

### Bug 修复

1. **嵌入模型评测**：修复 embedding 模型评测存在 benchmark 不对齐的问题
   Issue：https://github.com/modelscope/evalscope/issues/753
2. **RAG 评测**：修复 rageval 存在无法自动构建评测集的问题
   Issue：https://github.com/modelscope/evalscope/issues/859


## 评论 (3)

### LarytheLord · 2026-08-03

hi @Yunnglin, picking up on the "Safety Benchmarks: suggestions for datasets are welcome" item here.

i'd like to propose a framing-robustness benchmark, which is a bit different from the usual safety datasets. instead of asking whether a model refuses a harmful request, it measures whether a model's *judgment* of an already-stated harmful act survives having that act reworded. the act is held constant and only the framing changes, so any score movement is attributable to wording alone.

the rewrites come from a fixed, theory-grounded set of six discourse moves (euphemism, nominalization, agent deletion, functionalization, necessity/authorization, aggregation) rather than ad hoc paraphrases, so the perturbations are reproducible and each one is named.

from my own runs on this, judged cross-family so the generator and judge aren't the same lineage:
- euphemism is the dominant move by a clear margin, +1.90 mean acceptability gain vs +0.75 for the next one (n=81)
- it survives a strict binary "is this morally wrong, yes/no" instrument, so it isn't an artifact of asking for a number on a scale
- stacking moves does not compound, it saturates: euphemism alone scores higher than euphemism plus two other moves, and the pair that leaves the violent verb intact does essentially nothing

i checked what already exists before writing this. JADE mutates syntax until guardrails break, and the recent Chinese evasion work (arXiv 2605.29667) obfuscates lexically to dodge refusal. both target the refusal/compliance label. this targets a judge's moral verdict on an act that's already been stated plainly, which as far as i can tell isn't covered by anything in the benchmarks directory right now.

two questions before i put any code together:

1. is this in scope for what you had in mind under safety, or were you thinking specifically of refusal/compliance style datasets like the opencompass safety section referenced in #197?
2. since this is judge-scored rather than extractive, should the adapter follow the `alpaca_eval` / `arena_hard` / `general_arena` pattern rather than `DefaultDataAdapter`? happy to follow whichever you prefer.

i can start english-only and add a chinese set later, though i'd want a native speaker to check the chinese rewrites since the euphemism patterns don't translate directly.


### Yunnglin · 2026-08-04

@LarytheLord Thanks for the thoughtful proposal. This framing-robustness direction seems relevant to safety/alignment evaluation and is distinct from the usual refusal/compliance benchmarks.

Could you please open a dedicated issue so we can discuss it in more detail? It would be helpful to include:

- the benchmark goal and task definition;
- the proposed evaluation metrics;
- a few representative examples of an original item and its rewrites;
- a brief description of the dataset format and annotation/judging approach.

For implementation, [`drivel_binary`](https://github.com/modelscope/evalscope/blob/main/evalscope/benchmarks/drivelology/drivelology_binary_adapter.py) may be a useful reference for a strict binary-output task and custom metric aggregation. Once the design is clearer, we can discuss the appropriate adapter and scoring setup there.

### LarytheLord · 2026-08-04

opened #1540 with the details you asked for. thanks for the `drivel_binary` pointer, the strict binary output plus custom aggregation is the right shape for this since the scores are paired within an act rather than independent.

