# [Issue #1387] 评测MInimax2.5在数据集terminal_bench_v2上的精度，结果得分只有1.16，官网得分51.7

source: https://github.com/modelscope/evalscope/issues/1387
state: closed | updated: 2026-07-08T06:15:27Z
labels: 

## 正文

评测命令：
evalscope eval \
  --model /models/MiniMax-M2.5 \
  --api-url http://0.0.0.0:8000/v1/chat/completions \
  --api-key EMPTY \
  --eval-type openai_api \
  --eval-batch-size 32 \
  --datasets terminal_bench_v2 \
  --work-dir ./outputs/MiniMax-M2.5  \
  --dataset-dir ./terminal-bench-2 \
  --ignore-errors \
  --generation-config '{
    "timeout": 36000,
    "stream": true
  }'  2>&1 | tee H20-terminal_bench_v2-MiniMax-M2.5.log

<img width="1156" height="164" alt="Image" src="https://github.com/user-attachments/assets/c007da53-bfe7-43a1-8098-3f08fd039384" />

Mnimax2.5官网得分：
https://www.modelscope.cn/models/MiniMax/MiniMax-M2.5/summary

<img width="1208" height="483" alt="Image" src="https://github.com/user-attachments/assets/3dfb9f92-7476-4c18-a93d-e6d3120335be" />

## 评论 (6)

### Yunnglin · 2026-06-01

您好，目前信息不足以定位，麻烦补充：

1. **打包 outputs**：`tar -czf tb2.tar.gz outputs/MiniMax-M2.5/<时间戳>/` 上传，重点保留 `logs/`、`reports/`、`predictions/` 和 `trials/<task>/agent/trajectory.json`。

2. **基线问题**：MiniMax 官方 51.7 只在模型卡公布，[官方 leaderboard](https://www.tbench.ai/leaderboard/terminal-bench/2.0) 无对应提交条目，harness 未公开。terminal-bench 对 harness 极敏感（同模型可差 10+ 个点），evalscope 默认 `terminus-2` 与官方大概率不一致，直接对比不严谨。

3. **采样参数缺失**：MiniMax 官方推荐 `temperature=1.0, top_p=0.95, top_k=40, min_p=0.01`，您只设了 `timeout/stream`，会严重影响 tool call 稳定性。建议加上后重跑。

4. 顺带提一下：`--dataset-dir` 对该 benchmark 不生效，adapter 从 Harbor Hub 下载到 `~/.cache/evalscope/`。


### wenruihua · 2026-06-01

[terminal_bench_v2.zip](https://github.com/user-attachments/files/28460216/terminal_bench_v2.zip)
这是结果得分只有1.16的日志，
采样参数的设置以及数据集的重新设置并测试，结果随后附上

### Yunnglin · 2026-06-01

已分析您的 outputs，得分 1.16 = 86 个 task 中只有 1 个成功（`log-summary-date-ranges`），**与模型/harness/采样参数都无关**，全部卡在 Docker 环境。

主要失败日志：`Error response from daemon: all predefined address pools have been fully subnetted`，少量为 `AgentSetupTimeoutError: 360s` / `AgentTimeoutError: 3600s`。根因是 `--eval-batch-size 32` 让 32 个 trial 并发各起一个 docker network，超过 Docker 默认地址池上限。

建议先 `docker network prune -f && docker container prune -f` 清理残留，再把 `--eval-batch-size` 降到 4，并通过 `--dataset-args '{"terminal_bench_v2":{"extra_params":{"timeout_multiplier":2.0}}}'` 加大超时倍率重跑。如果跑全量仍超池，再修改 `/etc/docker/daemon.json` 扩大 `default-address-pools` 并重启 dockerd。


### wenruihua · 2026-06-03

按照上述-eval-batch-size 4和大超时倍率10倍重新跑的结果，得分似乎并不高，得分3.37
evalscope eval \
  --model /models/MiniMax-M2.5 \
  --api-url http://0.0.0.0:8000/v1/chat/completions \
  --api-key EMPTY \
  --eval-type openai_api \
  --eval-batch-size 4 \
  --datasets terminal_bench_v2 \
  --work-dir ./outputs/MiniMax-M2.5  \
  --datasets terminal_bench_v2 \
  --ignore-errors \
  --generation-config '{
    "timeout": 360000,
    "stream": true
  }'

[20260601_192938.zip](https://github.com/user-attachments/files/28531867/20260601_192938.zip)

加上采样参数测试，得分1.12
evalscope eval \
  --model /models/MiniMax-M2.5 \
  --api-url http://0.0.0.0:8000/v1/chat/completions \
  --api-key EMPTY \
  --eval-type openai_api \
  --eval-batch-size 4 \
  --datasets terminal_bench_v2 \
  --work-dir ./outputs/MiniMax-M2.5  \
  --ignore-errors \
  --generation-config '{
    "timeout": 360000,
    "stream": true,
    "temperature": 1.0, 
    "top_p": 0.95, 
    "top_k": 40, 
    "min_p": 0.01
  }'

[20260602_093234.zip](https://github.com/user-attachments/files/28531914/20260602_093234.zip)

### Yunnglin · 2026-06-03

简单总结：两次跑分波动跟模型/采样参数无关。
- **`timeout_multiplier` 实际没生效**：您写在了 `--generation-config` 的 `timeout` 里（那是 HTTP 请求超时），每个 trial 的 `config.json` 里仍是 `1.0`。正确写法 → `--dataset-args '{"terminal_bench_v2":{"extra_params":{"timeout_multiplier":10.0}}}'`
- **真正瓶颈：容器内访问外网失败**。89 个 task 中 42 个走到 verifier，其中 23 个 verifier 日志报 `curl: (56)/(28)`、`failed to download https://github.com/astral-sh/uv/...`、`uvx: command not found`，直接 reward=0；另外 40 个 `AgentSetupTimeoutError` 卡在 `terminus_2/tmux_session._attempt_tmux_installation`（apt 装 tmux 超时），本质同源。

网络层不通之前，分数都不可信。

## 您可以自行排查 outputs

把下面脚本存为 `analyze.py`，直接跑 `python analyze.py outputs/MiniMax-M2.5/<时间戳>` —— 会把失败分布、网络错误关键词、卡住的 phase 全列出来，下次不用再来回贴日志：

```python
import json, os, re, sys
from collections import Counter

root = sys.argv[1].rstrip('/')
review = next((os.path.join(dp, f) for dp, _, fs in os.walk(f'{root}/reviews')
               for f in fs if f.endswith('.jsonl')), None)
if not review:
    sys.exit(f'no review jsonl under {root}/reviews')

by_exc, passed, multi = Counter(), [], None
for line in open(review):
    s = json.loads(line)['sample_score']
    name = s['sample_metadata']['name']
    acc = s['score']['value'].get('acc', 0)
    result = (s['sample_metadata'].get('result') or {})
    if multi is None:
        multi = result.get('config', {}).get('timeout_multiplier')
    if acc == 1:
        passed.append(name); continue
    ex = (result.get('exception_info') or {}).get('exception_type') or 'NoException(reward=0)'
    by_exc[ex] += 1

print(f'\n[{root}]  timeout_multiplier = {multi}  (1.0 = 未生效)')
print(f'passed: {len(passed)}/{len(passed)+sum(by_exc.values())}  -> {passed}')
print('\n=== failure breakdown ===')
for k, v in by_exc.most_common(): print(f'  {v:3d}  {k}')

# Verifier 日志关键词扫描
pats = {
    'curl_recv_fail (56)':   r'curl: \(56\)',
    'curl_timeout (28)':     r'curl: \(28\)',
    'curl_refused (7)':      r'curl: \(7\)',
    'dns_fail':              r'Could not resolve host',
    'connect_fail':          r'Failed to connect to',
    'apt_fetch_fail':        r'E: Failed to fetch',
    'github_dl_fail':        r'(failed to download|failed to fetch).*github\.com',
    'pip_no_dist':           r'No matching distribution',
    'pip_read_timeout':      r'(ReadTimeoutError|HTTPSConnectionPool)',
    'docker_pull_fail':      r'(error pulling|manifest unknown|toomanyrequests)',
}
hits = Counter()
trials = f'{root}/trials'
for t in os.listdir(trials):
    p = f'{trials}/{t}/verifier/test-stdout.txt'
    if not os.path.exists(p): continue
    text = open(p, errors='replace').read()
    for name, pat in pats.items():
        if re.search(pat, text, re.I): hits[name] += 1

print('\n=== verifier 网络错误关键词 (有命中=容器出网有问题) ===')
for k, v in hits.most_common(): print(f'  {v:3d}  {k}')
if not hits: print('  (无命中，看 trial.log 与 exception_info 找别的原因)')
```

## 解读规则

| 输出 | 含义 | 行动 |
|---|---|---|
| `timeout_multiplier = 1.0` | `--dataset-args` 没传对 | 按上面写法补 |
| 大量 `AgentSetupTimeoutError` | 容器装 tmux 卡住 | 容器出网有问题，配代理 |
| 大量 `EnvironmentStartTimeoutError` | 容器/镜像起不来 | 检查 dockerd 拉镜像与磁盘 |
| 大量 `VerifierTimeoutError` / `NoException(reward=0)` + verifier 网络关键词命中 | 容器拉 github/pypi 失败 | 给容器配代理 |
| 上面 hits 全 0 | 真的是模型/任务问题 | 看具体 trial 的 `agent/trajectory.json` |

配代理位置：dockerd 在 `/etc/systemd/system/docker.service.d/http-proxy.conf`（影响 `docker pull`），容器内进程在 `~/.docker/config.json` 的 `proxies.default` 段（影响容器里跑的 apt/curl/pip）。

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

