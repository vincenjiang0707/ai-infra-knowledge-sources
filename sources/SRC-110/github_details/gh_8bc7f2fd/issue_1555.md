# [Issue #1555] [需求]加入更多reasoning_effort选项

source: https://github.com/modelscope/evalscope/issues/1555
state: closed | updated: 2026-08-10T08:37:57Z
labels: enhancement

## 正文

## 功能描述 / Feature Description

加入全套OpenAI兼容API格式的reasoning_effort，即none, low, medium, high, xhigh, max

## 需求背景 / Background

现在evalscope通过硬编码的方式设计reasoning_effort，导致只能使用low, medium, high三个推理强度，限制模型能力。



## 评论 (1)

### Yunnglin · 2026-08-10

已修复，合并到 main 了（#1561，commit `d9be821a`）：`reasoning_effort` 之前是 `Literal['low','medium','high']`，o1 时代留下的白名单，`none` / `minimal` / `xhigh` / `max` 都会在 pydantic 校验阶段被拦掉。现在改成字符串原样透传、由服务端判断合法性——这个取值集合本来就不该由 EvalScope 定义（官方文档写的是 model-dependent，且 vLLM / SGLang 等兼容服务还能自定义），你列的 `max` 确实是官方取值，是我们文档之前漏了它。修复会在下个版本发布，在那之前从源码装 main 即可直接使用 `generation_config={'reasoning_effort': 'max'}`；不想升级的话，用 `generation_config={'extra_body': {'reasoning_effort': 'max'}}` 透传也等价。感谢反馈。

