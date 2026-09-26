# [Issue #1524] [Feature Request] Perf 模块支持“长上下文前缀注入”以构造超长定长真实压测数据集

source: https://github.com/modelscope/evalscope/issues/1524
state: closed | updated: 2026-08-03T07:54:58Z
labels: enhancement

## 正文

## 功能描述 / Feature Description

希望 EvalScope 的 `Perf` 模块支持一种 **“长上下文前缀注入” (Long-context Prefix Injection)** 机制。允许用户通过指定长文本，与现有的短 prompt 数据集拼接，从而灵活构造出 128K/256K 级别的定长真实业务压测集。

## 需求背景 / Background

首先，非常感谢 @Yunnglin  在 #1483 中的快速响应与实现！`target_input_len` 配合 `cap`/`drop` 模式非常实用，我也完全认同官方关于“不做 Padding 以保持真实性”的设计思路。

但在实际的长文本压测场景中，我遇到了一个新的痛点：**缺乏超长上下文（如 128K/256K）的真实数据**。
当我们想测试模型在超长上下文下的性能时，现有方案存在局限：
1. **使用 `drop` 模式**：开源真实指令集大多在 4K-8K，设定 128K 会导致数据集被大量过滤，无数据可用。
2. **使用 `cap` 模式**：短文本原样保留，输入长短不一，无法严格测试特定长度下的性能瓶颈。
3. **使用 `random` 模式**：虽能定长，但生成的是高熵无意义 Token，失去了真实人类语言的低熵特征，无法真实反映 Prefix-Cache 的命中率或 MTP 的接受率。

## 预期行为 / Expected Behavior

希望框架能原生支持这种前缀拼接机制，具体设想如下：

## 预期行为 / Expected Behavior

希望框架能原生支持这种前缀拼接机制，具体设想如下：

1. **新增参数**：例如提供 `--long-prefix-file /path/to/long_text.txt`。
2. **处理逻辑**：在加载短 prompt 数据集时，框架在底层 Tokenizer 阶段，将指定的长文本作为前缀与短 Prompt 拼接，并结合 `target_input_len` 精确对齐到目标长度（如 128K）。
3. **注入角色控制 (Injection Role)**：
   为了更好适配主流推理框架的Prefix Caching机制，建议支持配置长前缀的注入角色：
   - **作为 `System Prompt` 注入（推荐）**：将长文本放入 System 角色，短 Prompt 放入 User 角色。这更符合真实 RAG 业务逻辑，且推理框架通常对 System Prompt 的 Cache 管理有专门优化。
   - **作为 `User Prompt` 前缀拼接**：直接将长文本拼在 User Prompt 的最前面。

## 其他信息 / Additional Information

- **业务价值**：这种机制让用户无需编写复杂的离线预处理脚本，即可通过框架原生能力，灵活构造任意目标长度。


## 评论 (2)

### ZhuXingcheng-666 · 2026-07-30

这个需求我这边也有，请帮忙评估下，谢谢~

### Yunnglin · 2026-08-03

已在 #1531 中实现并合入，感谢建议！

Perf 现在支持通过 `prefix_file` / `prefix_role` 注入真实长文本前缀，并结合 `target_input_len` 构造定长长上下文请求：

```bash
evalscope perf \
  --dataset openqa \
  --tokenizer-path Qwen/Qwen2.5-0.5B-Instruct \
  --dataset-args '{"target_input_len": 8192, "prefix_file": "long_text.txt", "prefix_role": "system"}' \
  ...
```

目前支持 `openqa`、`longalpaca`、纯文本格式的 `line_by_line`，以及 ShareGPT。前缀可作为 `system` 或 `user` 角色注入；推荐使用默认的 `system` 角色，以更贴近 RAG 和 Prefix Cache 场景。

使用时请注意：`prefix_file` 不能与 `input_len_mode="drop"` 组合，请使用默认的 `cap` 模式，由前缀补齐剩余长度。

