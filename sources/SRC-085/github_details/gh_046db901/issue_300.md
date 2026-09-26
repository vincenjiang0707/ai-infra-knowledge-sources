# [Issue #300] EAGLE3加速Llama3 8B中文效果不好的问题

source: https://github.com/SafeAILab/EAGLE/issues/300
state: closed | updated: 2025-09-18T01:07:58Z
labels: 

## 正文

我使用 Meta-Llama-3___1-8B-Instruct 对EAGLE3进行复现，草稿模型下载自作者在huggingface开源的参数yuhuili/EAGLE3-LLaMA3.1-Instruct-8B。
在我使用web启动EAGLE3推测编码推理服务后，我发现，相同的对话，使用英文回答有较高的预测成功概率，但是中文的预测效果会明显差一些。
这是由于大模型引起的还是草稿模型的训练不足呢？或者是其他问题导致的？可以解决吗？

示例截图如下：

<img width="1569" height="821" alt="Image" src="https://github.com/user-attachments/assets/da744782-f7a6-42ee-86ab-d5a5318e1f5e" />

<img width="1556" height="663" alt="Image" src="https://github.com/user-attachments/assets/5166cc84-e5e3-4000-abc0-1bdb5f91da54" />

## 评论 (1)

### hongyanz · 2025-09-17

因为我们压根没用中文数据集来训练草稿模型
