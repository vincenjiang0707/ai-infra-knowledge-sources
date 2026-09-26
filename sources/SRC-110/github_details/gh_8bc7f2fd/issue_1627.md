# [Issue #1627] close-loop压测第一批请求TTFT波动异常，导致p99没有参考价值

source: https://github.com/modelscope/evalscope/issues/1627
state: closed | updated: 2026-08-27T06:39:54Z
labels: 

## 正文

## 自查清单

在提交 issue 之前，请确保您已完成以下步骤:
- [x] 我已仔细阅读了[相关使用说明文档](https://evalscope.readthedocs.io/zh-cn/latest/get_started/parameters.html)
- [x] 我已查看了[常见问题解答](https://evalscope.readthedocs.io/zh-cn/latest/get_started/faq.html)
- [x] 我已搜索并查看了现有的 issues，确认这不是一个重复的问题

## 问题描述

目前针对部署于昇腾910B系列npu上的dsv4-0731-flash（带Dspark）模型服务进行压测，推理框架使用vllm，
服务侧设置允许最大活跃请求为32，总的prefill+decode的token budget为12.8k。

在上述条件下进行close-loop压测时发现第一批请求的TTFT出现异常波动，如下图

<img width="1442" height="626" alt="Image" src="https://github.com/user-attachments/assets/c9dbb8e4-c788-444f-bdb9-04af0d97ac28" />

<img width="1446" height="632" alt="Image" src="https://github.com/user-attachments/assets/898c7aac-1780-457f-8801-eeba674ffd90" />

<img width="1436" height="616" alt="Image" src="https://github.com/user-attachments/assets/98b31c55-7acc-4557-ab67-d27e99ec6502" />

自上而下分别为8、16、32并发下的情形，而具有波动的TTFT的首批请求数量恰好为并发数。

- 我已开启20%的warmup以确保warmup数能覆盖第一轮请求
- 我已将prompt token数设置为4k，尽可能避免触发chunked prefill（排除服务本身的等待）

## EvalScope 版本（必填）

Version: 1.10.0

## 使用的工具
- [x] Native / 原生框架
- [ ] Opencompass backend
- [ ] VLMEvalKit backend
- [ ] RAGEval backend
- [x] Perf / 模型推理压测工具
- [ ] Arena / 竞技场模式

## 执行的代码或指令
由于dsv4并未给出jinjia的template，因此使用了如下设置直接将token id发送至/v1/completion
```python
dataset="random",
tokenizer_path=cli.tokenizer,

apply_chat_template=False,
tokenize_prompt=True,
```

## 错误日志

请粘贴完整的错误日志或控制台输出。

## 运行环境

- 操作系统：
- Python版本：3.10.x

## 其他信息

如果有其他相关信息，请在此处提供。


## 评论 (2)

### Moenupa · 2026-08-25

猜测是 kernel JIT (e.g., flashinfer) 搜下 vllm log.

### Lotus0316 · 2026-08-26

> 猜测是 kernel JIT (e.g., flashinfer) 搜下 vllm log.

Thx感谢回复，我会往这个方向调查，不过感觉应该不是JIT：
- 一方面升腾的JIT策略似乎和N卡的很不一样
- 另一方面，因为在服务长稳运行的各个时间节点上进行压测都会稳定的出现第一批进入的请求出现TTFT剧烈波动，而且vllm log看起来也没有什么异常

但是我直接在服务端上vllm-bench也会出现类似的抖动，也许不是压测框架的问题
