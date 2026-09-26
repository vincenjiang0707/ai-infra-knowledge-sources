# [Issue #1074] ERNIE 4.5-0.3B 是否支持 OpenAI 的 json_schema 格式

source: https://github.com/PaddlePaddle/ERNIE/issues/1074
state: closed | updated: 2025-08-06T04:01:03Z
labels: 

## 正文

(empty)

## 评论 (4)

### kevincheng2 · 2025-07-31

@ZYJ-3721 你好，ERNIE 4.5-0.3B 已经支持 OpenAI 的 json_schema 格式，需要在服务启动时增加 `--guided-decoding-backend "auto"` 参数。
支持格式以及测试案例可以参考文档：https://github.com/PaddlePaddle/FastDeploy/blob/develop/docs/zh/features/structured_outputs.md

### miao200years · 2025-07-31

问一下问题是否被解决。

### ZYJ-3721 · 2025-07-31

> 问一下问题是否被解决。

已解决

### miao200years · 2025-08-01

好
