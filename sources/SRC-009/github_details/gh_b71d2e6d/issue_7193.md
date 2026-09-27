# [Issue #7193] [Bug]: High TTFT for the first request. Can vllm-serve warmup itself after startup?

source: https://github.com/vllm-project/vllm-ascend/issues/7193
state: open | updated: 2026-09-27T04:11:21Z
labels: bug

## 正文

### Your current environment

docker image today: main-openeuler

### 🐛 Describe the bug

After bootstrapping the `vllm serve` for Qwen3-Next, Qwen3-Coder-Next and Qwen3.5 models, 
it will do some compiling (using bisheng and clang-17) when receive the first request.

**That will obviously increase the TTFT.** So, can vllm warmup itself immediately after startup? That is important.


```
(APIServer pid=87) INFO:     Started server process [87]
(APIServer pid=87) INFO:     Waiting for application startup.
(APIServer pid=87) INFO:     Application startup complete.

(APIServer pid=87) WARNING 03-12 07:04:01 [warnings.py:110] /vllm-workspace/vllm/vllm/entrypoints/openai/chat_completion/protocol.py:377: Depreca
tionWarning: max_tokens is deprecated in favor of the max_completion_tokens field
(APIServer pid=87) WARNING 03-12 07:04:01 [warnings.py:110] /vllm-workspace/vllm/vllm/entrypoints/openai/chat_completion/serving.py:393: Deprecat
ionWarning: max_tokens is deprecated in favor of the max_completion_tokens field


(APIServer pid=87) INFO:     xx.xx.xx.xx:14167 - "POST /v1/chat/completions HTTP/1.1" 200 OK
(Worker_TP0_EP0 pid=370) [WARNING] Please DO NOT tune args ['num_warps', 'num_stages']!
(Worker_TP1_EP1 pid=371) [WARNING] Please DO NOT tune args ['num_warps', 'num_stages']!
(Worker_TP6_EP6 pid=376) [WARNING] Please DO NOT tune args ['num_warps', 'num_stages']!
(Worker_TP5_EP5 pid=375) [WARNING] Please DO NOT tune args ['num_warps', 'num_stages']!
(Worker_TP7_EP7 pid=377) [WARNING] Please DO NOT tune args ['num_warps', 'num_stages']!
(Worker_TP2_EP2 pid=372) [WARNING] Please DO NOT tune args ['num_warps', 'num_stages']!
(Worker_TP3_EP3 pid=373) [WARNING] Please DO NOT tune args ['num_warps', 'num_stages']!
(Worker_TP4_EP4 pid=374) [WARNING] Please DO NOT tune args ['num_warps', 'num_stages']!
......
(Worker_TP0_EP0 pid=370) [WARNING] Please DO NOT tune args ['num_warps', 'num_stages']!
(Worker_TP1_EP1 pid=371) [WARNING] Please DO NOT tune args ['num_warps', 'num_stages']!


(Worker_TP5_EP5 pid=375) INFO 03-12 07:04:44 [acl_graph.py:185] Replaying aclgraph
(Worker_TP0_EP0 pid=370) INFO 03-12 07:04:44 [acl_graph.py:185] Replaying aclgraph
(Worker_TP2_EP2 pid=372) INFO 03-12 07:04:44 [acl_graph.py:185] Replaying aclgraph
(Worker_TP4_EP4 pid=374) INFO 03-12 07:04:44 [acl_graph.py:185] Replaying aclgraph
(Worker_TP7_EP7 pid=377) INFO 03-12 07:04:44 [acl_graph.py:185] Replaying aclgraph
(Worker_TP1_EP1 pid=371) INFO 03-12 07:04:44 [acl_graph.py:185] Replaying aclgraph
(Worker_TP6_EP6 pid=376) INFO 03-12 07:04:44 [acl_graph.py:185] Replaying aclgraph
(Worker_TP3_EP3 pid=373) INFO 03-12 07:04:44 [acl_graph.py:185] Replaying aclgraph


(APIServer pid=87) INFO 03-12 07:04:47 [loggers.py:259] Engine 000: Avg prompt throughput: 1.0 tokens/s, Avg generation throughput: 22.0 tokens/s, Running: 1 reqs, Waiting: 0 reqs, GPU KV cache usage: 0.0%, Prefix cache hit rate: 0.0%
(APIServer pid=87) INFO 03-12 07:04:57 [loggers.py:259] Engine 000: Avg prompt throughput: 0.0 tokens/s, Avg generation throughput: 40.9 tokens/s, Running: 0 reqs, Waiting: 0 reqs, GPU KV cache usage: 0.0%, Prefix cache hit rate: 0.0%
(APIServer pid=87) INFO 03-12 07:05:07 [loggers.py:259] Engine 000: Avg prompt throughput: 0.0 tokens/s, Avg generation throughput: 0.0 tokens/s, Running: 0 reqs, Waiting: 0 reqs, GPU KV cache usage: 0.0%, Prefix cache hit rate: 0.0%


```

## 评论 (5)

### weijinqian0 · 2026-03-13

@zzzzwwjj Could you please take a look at this issue?

### 325146 · 2026-03-14

Hi! I'd like to work on this issue.<br><br>The high TTFT (Time To First Token) on the first request is indeed caused by the JIT compilation happening at runtime. This is a common issue with NPU/GPU backends that use just-in-time kernel compilation.<br><br>My plan:<br>1. Investigate the current warmup mechanism in vllm-ascend<br>2. Implement an automatic warmup that runs after model loading<br>3. Add a configuration option for users to customize warmup behavior<br>4. Test and measure the improvement in TTFT<br><br>Could you please assign this to me? I'll aim to have a PR ready within 5-7 days.

### MaoJianwei · 2026-03-14

> Hi! I'd like to work on this issue.The high TTFT (Time To First Token) on the first request is indeed caused by the JIT compilation happening at runtime. This is a common issue with NPU/GPU backends that use just-in-time kernel compilation.My plan:1. Investigate the current warmup mechanism in vllm-ascend2. Implement an automatic warmup that runs after model loading3. Add a configuration option for users to customize warmup behavior4. Test and measure the improvement in TTFTCould you please assign this to me? I'll aim to have a PR ready within 5-7 days.

Great 👍 Nice to see your progress @325146 

I have no permission to operate the `Assignees`.

### Bowen-Leee · 2026-08-14

where is your PR？ @325146 

### mashuiping · 2026-09-27

<img width="1980" height="827" alt="Image" src="https://github.com/user-attachments/assets/70825b19-9d52-497f-8030-1239e53a6874" />

目前 MRV2 dsv4 flash 补上 [warmup_kernels](https://github.com/vllm-project/vllm-ascend/pull/17556) + 绕过 [vLLM bug](https://github.com/vllm-project/vllm/issues/54455) +  处理 [Dflash dead BLOCK_SIZE ](https://github.com/vllm-project/vllm-ascend/pull/17554)，首个请求是可以完全正常无卡顿 prefill 和 decode 的
