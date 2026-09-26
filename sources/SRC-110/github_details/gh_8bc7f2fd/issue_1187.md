# [Issue #1187] 使用evalscope评测deepseek-r1-1.5b模型，设置n=64，无法达到原文效果

source: https://github.com/modelscope/evalscope/issues/1187
state: closed | updated: 2026-07-08T06:15:31Z
labels: 

## 正文

## 自查清单

在提交 issue 之前，请确保您已完成以下步骤:
- [x] 我已仔细阅读了[相关使用说明文档](https://evalscope.readthedocs.io/zh-cn/latest/get_started/parameters.html)
- [x] 我已查看了[常见问题解答](https://evalscope.readthedocs.io/zh-cn/latest/get_started/faq.html)
- [x] 我已搜索并查看了现有的 issues，确认这不是一个重复的问题

## 问题描述

请简要描述您遇到的问题。

## EvalScope 版本（必填）
v0.xx.x

## 使用的工具
- [x] Native / 原生框架
- [ ] Opencompass backend
- [ ] VLMEvalKit backend
- [ ] RAGEval backend
- [ ] Perf / 模型推理压测工具
- [ ] Arena / 竞技场模式

## 执行的代码或指令

请提供您执行的主要代码或指令。

## 错误日志

请粘贴完整的错误日志或控制台输出。

## 运行环境

- 操作系统：
- Python版本：

## 其他信息

如果有其他相关信息，请在此处提供。


## 评论 (6)

### Yunnglin · 2026-02-05

请给出具体运行的命令和benchmark上的差距对比

### haodongze · 2026-02-05

from evalscope import TaskConfig, run_task
from evalscope.constants import EvalType

task_cfg = TaskConfig(
    model='DeepSeek-R1-Distill-Qwen-1.5B',   # 模型名称 (需要与部署时的模型名称一致)
    api_url='http://127.0.0.1:8001/v1/chat/completions',  # 推理服务地址
    api_key='EMPTY',
    eval_type=EvalType.SERVICE,   # 评测类型，SERVICE表示评测推理服务
    datasets=['aime24'],
    eval_batch_size=32,       # 发送请求的并发数
    generation_config={       # 模型推理配置
        'max_tokens': 20000,  # 最大生成token数，建议设置为较大值避免输出截断
        'temperature': 0.6,   # 采样温度 (deepseek 报告推荐值)
        'top_p': 0.95,        # top-p采样 (deepseek 报告推荐值)
        'n': 5                # 每个请求产生的回复数量 (注意 lmdeploy 目前只支持 n=1)
    },
)

run_task(task_cfg=task_cfg)

采用vllm最新版本部署，性能只有18%

### haodongze · 2026-02-05

论文结果是28%，重复64次测试还是不到20%

### VoiceBeer · 2026-02-16

想请问下这些注释是有官方例子吗？我看issue里的好多人给的示例代码里对应的注释都差不太多，但我看官方的文档里好像没有这些实操的例子

### wakaka-tt · 2026-06-14

我也遇到这样的问题, 请问你解决了吗？  `    parser.add_argument('--samples', '-s', type=int, default=256, help='批处理大小 (batch_size)')
    parser.add_argument('--repeats', '-r', type=int, default=1, 
                       help='每个问题的生成次数 (用于 pass@k 计算)')
    parser.add_argument('--work-dir', default='outputs', help='输出目录')
    parser.add_argument('--max-tokens', type=int, default=8192, help='最大生成 token 数')
    parser.add_argument('--temperature', type=float, default=0.6, help='采样温度')
    parser.add_argument('--top-p', type=float, default=0.95, help='Top-p 采样参数')
    parser.add_argument('--limit', type=int, default=None, help='限制评估样本数量 (用于测试)')

    args = parser.parse_args()

    task_cfg = TaskConfig(
        model=args.model,
        api_url=args.api_url,
        api_key=args.api_key,
        eval_type=EvalType.OPENAI_API,
        datasets=['aime24','amc', 'math_500'],#['minerva_math', 'olympiad_bench']#
        repeats=args.repeats,  # ✅ 关键：每个样本生成 repeats 次
        eval_batch_size=args.samples,
        dataset_args={
            'aime24': {
                'aggregation': 'mean_and_pass_at_k',  # ✅ 启用 pass@k 计算
                'few_shot_num': 0,  # 0-shot 评估
            },
             'amc': {
                'aggregation': 'mean_and_pass_at_k',  # ✅ 启用 pass@k 计算
                'few_shot_num': 0,  # 0-shot 评估
                 'subset_list' : ['amc23']
            },
            'math_500':{
                'aggregation': 'mean_and_pass_at_k',  # ✅ 启用 pass@k 计算
                'few_shot_num': 0,  # 0-shot 评估
            }
            
        },
        generation_config={
            'max_tokens': args.max_tokens,
            'temperature': args.temperature,
            'top_p': args.top_p,
            'timeout': 600,
        },
        work_dir=args.work_dir,
        limit=args.limit,  # 用于快速测试
    )`

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

