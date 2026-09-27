# [Issue #4629] [Feature] qwen 3.6模型在V100上已经支持mtp了吗？ 如何开启mtp支持

source: https://github.com/InternLM/lmdeploy/issues/4629
state: closed | updated: 2026-06-16T04:13:27Z
labels: 

## 正文

### Motivation

[Feature] qwen 3.6模型在V100上如何开启mtp支持？

谢谢

### Related resources

_No response_

### Additional context

_No response_

## 评论 (3)

### simonjhy · 2026-06-14

我在qwen3.6-35b上通过如下参数启用mtp功能

      --speculative-algorithm qwen3_5_mtp
      --speculative-num-draft-tokens 3

但是日志里提示下面的错误。这个是有什么限制吗？

WARNING async_engine.py:129 - speculative decoding is not supported by turbomind

### simonjhy · 2026-06-14

  if speculative_config is not None and backend == 'turbomind':
      logger.warning('speculative decoding is not supported by turbomind')

现在这个是代码里看到这个，是turbowind根本不支持吗？

### lvhan028 · 2026-06-16

turbomind 还没有增加 speculative decoding 的功能。
请使用 --backend pytorch
