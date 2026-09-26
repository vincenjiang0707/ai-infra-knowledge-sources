# [Issue #1215] 文心一言21B模型，张量并行启动不了

source: https://github.com/PaddlePaddle/ERNIE/issues/1215
state: open | updated: 2026-01-13T03:38:12Z
labels: 

## 正文

我使用FastDeploy部署文心一言21B模型，有两个T4显卡，设置了--tensor_parallel_size 2，启动失败。

<img width="1060" height="663" alt="Image" src="https://github.com/user-attachments/assets/60b587df-0d99-48fd-87cf-85db9dcc2d72" />

。

<img width="1063" height="694" alt="Image" src="https://github.com/user-attachments/assets/0a41dd00-143e-475f-af13-34754a2c771e" />


## 评论 (7)

### Kyo1234567 · 2025-09-02

我们也试了两张A16的显卡，报错也类似。<!-- Failed to upload "1.jpg" -->

### Kyo1234567 · 2025-09-02

![Image](https://github.com/user-attachments/assets/59ec95a3-5221-44cd-888e-e502232669ad)

### Kyo1234567 · 2025-09-02

这张图是A16卡报的错。

![Image](https://github.com/user-attachments/assets/f0f7475c-cc9f-4fdf-8adf-1e4e9268fd87)

### lizexu123 · 2025-09-02

export LD_LIBEARY_PATH=/usr/local/nvcc设置一下呢？

### Kyo1234567 · 2025-09-03

LD_LIBEARY_PATH=/usr/local/nvcc设置了，错误跟之前一样。我在windows机器上，使用nvcc --version是有输出的。我不知道Linux上nvcc到底是个什么文件，也搜索不到

### lizexu123 · 2025-09-03

不好意思，看错了，Ubuntu上是nccl库，windows平台上不清楚nccl在哪里，可以查一下，下面是ububtu下nccl的库文件，我理解名称应该是一样的，但是后缀应该不同，windows平台我们从来没跑过，不清楚能不能跑，如果是ubuntu，在设置下export LD_LIBEARY_PATH=/usr/local/nccl

<img width="699" height="94" alt="Image" src="https://github.com/user-attachments/assets/f31a8d97-021a-42ca-9e55-cc81d545d23d" />

### Jiang-Jia-Jun · 2026-01-13

FastDeploy目前支持的仅包含80/86/89/90架构GPU卡，可以试下vLLM在T4上
