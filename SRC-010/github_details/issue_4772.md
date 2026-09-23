# [Issue #4772] [Feature] 启动服务时候支持直接关闭思考吗？

source: https://github.com/InternLM/lmdeploy/issues/4772
state: closed | updated: 2026-07-23T01:45:19Z
labels: 

## 正文

### Motivation

启动服务时候支持直接关闭思考吗？不需要思考

### Related resources

_No response_

### Additional context

_No response_

## 评论 (1)

### lvhan028 · 2026-07-22

服务侧没有这个选项。
客户端可以在请求中传入 enable_thinking: false 来关闭。
