# [Issue #4024] [Bug] ModelInputs.split()中对max_kv_seqlen和sum_kv_seqlen的计算可能存在问题

source: https://github.com/InternLM/lmdeploy/issues/4024
state: closed | updated: 2026-06-18T06:26:38Z
labels: 

## 正文

### Checklist

- [x] 1. I have searched related issues but cannot get the expected help.
- [x] 2. The bug has not been fixed in the latest version.
- [x] 3. Please note that if the bug-related issue you submitted lacks corresponding environment info and a minimal reproducible demo, it will be challenging for us to reproduce and resolve the issue, reducing the likelihood of receiving feedback.

### Describe the bug

阅读LMdeploy最新源码时，我发现[`Engine.create_model_inputs()`](https://github.com/InternLM/lmdeploy/blob/83976c934ec6ec1fe0ead5822ae0f1edf9cb1579/lmdeploy/pytorch/engine/engine.py#L758)中对kv_seqlens字段的计算是将每个sequence的未计算部分（seq_length）和已计算部分（history_lengths）长度相加。

在 [`ModelInputs.split()`](https://github.com/InternLM/lmdeploy/blob/83976c934ec6ec1fe0ead5822ae0f1edf9cb1579/lmdeploy/pytorch/model_inputs.py#L262)中，对max_kv_seqlen的处理是 `max_kv_seqlen = self.max_kv_seqlen`，然后每步 `max_kv_seqlen += max_q_seqlen`。**这使得ModelInputs需要split时，split出来的第0个inp的max_kv_seqlen即为“本段seq_length+本序列split前的prompt总长度”，而非该字段期望的“本段seq_length+本段开头是第几个词元”。** 同时split出来的其他inp的max_kv_seqlen、sum_kv_seqlen也将是错误的。

也许，`ModelInputs.split()`中的`max_kv_seqlen = self.max_kv_seqlen`应该改成 `max_kv_seqlen = self.history_lengths[0].item()`？不知道这是否是一个bug还是我理解出现了偏差，希望跟各位大佬讨论，谢谢>_<



### Reproduction

纯读代码，不涉及复现

### Environment

```Shell
最新分支（https://github.com/InternLM/lmdeploy/commit/83976c934ec6ec1fe0ead5822ae0f1edf9cb1579）
```

### Error traceback

```Shell

```

## 评论 (1)

### grimoire · 2025-10-04

感谢汇报
这确实算是一个 bug。ModelInputs.split 是用来处理超长 prefill 的分块计算的，max_kv_seqlen 的初始值应该是历史长度+当前轮 q_seqlen。不过从 self.history_lengths 可能涉及到一次 host-device 同步，不算最好的解决方案，从原本的 max_kv_seqlen 和 max_q_seqlen 进行换算会比较好。我们会尽快修复，或者如果你有这个意向的话也欢迎提 PR。

另外这个值目前主要的用处是 attention 的 grid 以及 kv cache 的一些资源分配，超量分配会造成少量的浪费，但是不会对精度和性能造成太多影响。
