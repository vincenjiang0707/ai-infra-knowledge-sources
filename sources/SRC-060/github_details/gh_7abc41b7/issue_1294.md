# [Issue #1294] chatml 格式的训练数据支持哪些模型？

source: https://github.com/PaddlePaddle/ERNIE/issues/1294
state: closed | updated: 2026-01-08T12:01:29Z
labels: 

## 正文

尊敬的Ernie 团队 ，您好~ 
    在官网看到了如下图所示的chatml 格式的数据，我想知道这个格式的数据目前适配哪些模型？
<img width="2184" height="966" alt="Image" src="https://github.com/user-attachments/assets/63a07440-ca02-45d8-843f-bdec2279d3c4" />

## 评论 (5)

### Jonathans575 · 2025-09-29

chatml格式适合纯文系列模型的function call（0.3b、21b、21b thinking、300b）和思考模型（21b thinking）

### Farewell-CK · 2025-09-29

大概明白了get, 十分感谢

### Farewell-CK · 2025-09-29

> chatml格式适合纯文系列模型的function call（0.3b、21b、21b thinking、300b）和思考模型（21b thinking）

在正式训练之前，我想确认一下，使用fastdeploy or erniekit or vllm  部署解锁工具调用的方法都一致吗？

### Jiang-Jia-Jun · 2025-10-09

FD与vllm调用接口是一致的

### nepeplwu · 2026-01-08

The issue has no response for a long time and will be closed. You can reopen or new another issue if are still confused.

---
_From Bot_
