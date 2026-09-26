# [Issue #1493] [需求]EvalScope 模型推理性能评测支持 Multi-LoRA 服务的性能评测

source: https://github.com/modelscope/evalscope/issues/1493
state: open | updated: 2026-07-23T05:05:03Z
labels: 

## 正文

## 自查清单

在提交 issue 之前，请确保您已完成以下步骤:
- [ 1 ] 我已仔细阅读了[相关使用说明文档](https://evalscope.readthedocs.io/zh-cn/latest/get_started/parameters.html)
- [ 1 ] 我已查看了[常见问题解答](https://evalscope.readthedocs.io/zh-cn/latest/get_started/faq.html)
- [ 1 ] 我已搜索并查看了现有的 issues，确认这不是一个重复的问题

## 需求描述

当前EvalSope已支持对模型服务进行模型推理性能评测可用于测试基于 OpenAI API 的推理服务

随着 LoRA成为大模型参数高效微调的主流方案，越来越多的推理框架（如 vLLM）采用 单 Base Model + 多 LoRA Adapter 的服务化部署方式。多个业务或租户共享同一个 Base Model，请求通过 OpenAI API 的 model 字段选择对应的 LoRA Adapter，实现不同领域能力的在线推理。

在这种部署模式下，LoRA 已经成为请求级配置，而不是模型部署配置。同一个服务实例中，不同请求可能对应不同的 LoRA Adapter，这也是目前 Multi-LoRA 在线服务的典型访问模式。

性能评测：无法模拟 Multi-LoRA 服务中的混合流量，不能评估不同 LoRA 并发访问下的吞吐、时延等性能指标。
## 建议方案

建议增加 Multi-LoRA 服务评测能力，支持请求级指定目标模型（LoRA Adapter），同时兼容现有单模型评测流程。

## EvalScope 版本（必填）
v1.9.0

## 使用的工具
- [] Perf / 模型推理压测工具



## 评论 (2)

### Yunnglin · 2026-07-17

@UMR19 感谢反馈！关于 **Multi-LoRA 混合流量压测**，其实当前版本（无需升级）就能通过 `line_by_line` 数据集在**请求级指定不同的 model（LoRA Adapter）**来实现，思路如下：

### 用法

`line_by_line` 数据集支持“每行一个完整请求体（JSON object）”格式。你只要在每行请求体里显式写上 `model` 字段指向对应的 LoRA Adapter，evalscope 就会**原样保留、按并发把混合流量打到服务端**（`--model` 只作为未显式指定 model 的行的默认值）。

**1. 准备数据文件 `multi_lora.jsonl`**，按你想要的流量分布把请求“编排”进去：

```jsonl
{"messages": [{"role": "user", "content": "介绍一下杭州"}], "model": "lora-A"}
{"messages": [{"role": "user", "content": "写一首诗"}], "model": "lora-B"}
{"messages": [{"role": "user", "content": "解释相对论"}], "model": "lora-A"}
{"messages": [{"role": "user", "content": "翻译这段话"}], "model": "lora-C"}
```

> 想模拟热点/倾斜流量（比如 80% 打 lora-A），按比例多写对应行即可。

**2. 发起压测：**

```bash
evalscope perf \
  --url http://127.0.0.1:8000/v1/chat/completions \
  --api openai \
  --model lora-A \
  --dataset line_by_line \
  --dataset-path multi_lora.jsonl \
  --parallel 16 \
  --number 1000
```

这样多个 LoRA 的请求会**并发混合**打到同一个 vLLM 实例上，能真实反映 batch 内多 LoRA 争用、adapter 换入换出等对整体吞吐/时延的影响。

### 当前的限制

这种方式得到的是**混合流量的整体性能指标**，暂时还有两点做不到，也是我们评估是否要进一步支持的点：
1. **内置分配策略**：目前分布需要你手动编排进数据文件，不能通过参数（随机/加权/zipf）自动生成；
2. **per-adapter 分维度指标**：指标是全局聚合的，暂时无法输出「每个 LoRA 各自的 TTFT / 吞吐 / SLA」。

想确认下你的场景：**你主要需要的是「混合流量整体性能」，还是必须看到「每个 LoRA 各自的性能指标」？** 这能帮我们判断上面两点的优先级。你可以先用上面的方式试跑，有问题随时反馈～


### UMR19 · 2026-07-23

您好， @Yunnglin 我是想看混合流量整体性能，主要想看到切换 LoRA 带来的 TTFT 损失，吞吐量等指标
