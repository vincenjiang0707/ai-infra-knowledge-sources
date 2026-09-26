# [Issue #1401] 使用evalscope+mmlu-pro精度集测试vllm-ascend镜像，得分总是比vllm-ascend官方的ais-bench工具低了5-6分

source: https://github.com/modelscope/evalscope/issues/1401
state: closed | updated: 2026-07-08T06:15:24Z
labels: 

## 正文

参考vllm-ascend社区的issue单号：https://github.com/vllm-project/vllm-ascend/issues/10068
这个问题更有可能是evalscope工具的问题，请帮忙分析。


## 评论 (2)

### Yunnglin · 2026-06-05

感谢反馈！为了定位具体的差异来源，能否提供以下信息：

1. **evalscope 输出目录的 zip 包**（`outputs/<timestamp>/` 下的完整目录），主要需要：
   - `predictions/` 目录下的 JSONL 文件（包含模型原始输出和提取的答案）
   - `reports/` 目录下的 JSON 报告文件
   - `configs/` 目录下的配置文件

2. **运行时使用的 evalscope 命令或配置**（TaskConfig 参数）

3. 如果方便的话，也提供 **ais-bench 测试同模型的详细分数**（按 subject 的分数对比）

有了 predictions 文件，我们可以分析答案提取的成功率和失败 case，定位是 prompt 导致模型输出格式不符，还是答案提取逻辑丢分。

### Yunnglin · 2026-07-08

这类“无法复现官方 / paper 分数”的问题，通常需要先对齐评测口径、采样参数和运行环境。当前信息还不足以判断为 EvalScope 框架侧 bug，先关闭该 issue；如果后续能提供最小可复现证据，欢迎 reopen 继续跟进。

建议按下面顺序排查：

1. **上传完整 `outputs/<timestamp>/`**
   - 至少包含 `configs/`、`predictions/`、`reports/`；
   - 如涉及 judge / agent / terminal-bench，请一并提供 `reviews/`、`trials/`、`agent/trajectory.json`、verifier 日志。

2. **先定位差异来源**
   - 模型原始输出错误：优先检查模型服务、采样参数、prompt 或官方口径；
   - 模型输出正确但 `extracted_prediction` 错：可能是答案提取问题；
   - 提取正确但 score 错：可能是 metric / judge / aggregation 配置问题；
   - 大量 error / timeout：先排查运行环境，再比较分数。

3. **对齐官方评测口径**
   请确认 prompt、system prompt、chat template、temperature、top_p、top_k、max_tokens、repeats、pass@k / vote@k / mean aggregation、judge model、benchmark 版本和 subset 都与官方一致。

4. **小样本集需要多次重复**
   AIME 等小样本 benchmark 单题就会带来几个百分点波动，建议使用 `repeats` 多次采样，并明确聚合方式。

5. **Agent / terminal-bench 类任务先查环境**
   请确认 Docker、容器网络、GitHub/PyPI/apt 访问、`timeout_multiplier` 等配置正常。环境不稳定时，总分通常不具备可比性。

6. **如需继续定位**
   请提供“模型输出正确但 EvalScope 提取或评分错误”的具体样本编号和完整 outputs，我们会继续排查。

