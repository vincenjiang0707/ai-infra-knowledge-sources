source: https://docs.opencloudos.org/OC9/ai-deployment/ai-application-practice/tf-ds-model-deployment/

# Transformers + Deepspeed大模型部署指南

Transformers 库由 Hugging Face 开发，提供了大量预训练模型（如 BERT, GPT, T5 等），用于自然语言处理（NLP）任务，现在也支持图像和音频任务。

DeepSpeed 是一个深度学习优化库，由微软开发，主要用于分布式训练和大模型训练。它提供了 ZeRO（零冗余优化器）、模型并行、梯度检查点等功能.

本文档将展示如何在 OpenCloudOS 9 操作系统上，通过一键安装脚本和容器镜像拉取，快速启动 Transformers 以及 DeepSpeed 框架，并启动相关推理服务。

## 1.安装容器依赖

### 一键安装容器依赖

脚本下载地址：[点击下载执行脚本](https://ocweb-1319394267.cos.ap-guangzhou.myqcloud.com/docs/scripts/auto_install_vllm.sh)

```
sudo ./auto_install.sh
```


**备注**：关于一键安装脚本详细代码请

[查看该链接](https://gitee.com/OpenCloudOS/Document/blob/master/docs/OC9/ai-deployment/ai-application-practice/auto_install.sh)。

## 2.启动容器镜像

### 2.1 下载模型权重

如果已有权重，忽略下载跳转2.2小节，下载权重到位置/models/：

```
# 1. 安装 Git LFS
sudo dnf install -y git-lfs
# 2. 已安装的 Git LFS 注册进 Git
sudo git lfs install
# 3. 下载模型权重到/models/
sudo mkdir -p /models && sudo git clone https://huggingface.co/bert-base-uncased /models/bert-base-uncased
```


### 2.2 运行容器

```
sudo docker run -it --rm --gpus all --privileged -v /models:/models --name=opencloudos9_transformers_deepspeed opencloudos9-tf-dp
```


## 3.运行训练demo

### 3.1 基于bert-base-uncased 情感微调示例

在容器内执行：

```
cd /workspace/examples/
#使用部分数据集，时间稍快
python3 transformers_dataset_local_online_demo.py
#或者使用全部数据集进行微调后推理
python3 transformers_all_data.py
```


使用微调后的模型进行推理。使用部分数据集推理展示

```
推理结果:
======================================================================
测试 1: 'This movie is wonderful and inspiring!'
情感: 正面 😊
置信度: 88.74%
概率分布: [负面: 0.113, 正面: 0.887]
----------------------------------------------------------------------
测试 2: 'I really dislike this boring film.'
情感: 负面 😞
置信度: 86.57%
概率分布: [负面: 0.866, 正面: 0.134]
----------------------------------------------------------------------
测试 3: 'The acting is superb and the story is engaging.'
情感: 正面 😊
置信度: 81.33%
概率分布: [负面: 0.187, 正面: 0.813]
----------------------------------------------------------------------
测试 4: 'This is the worst movie ever made, complete waste of time.'
情感: 负面 😞
置信度: 85.25%
概率分布: [负面: 0.852, 正面: 0.148]
----------------------------------------------------------------------
测试 5: 'Nice and enjoyable film with great characters.'
情感: 正面 😊
置信度: 87.40%
概率分布: [负面: 0.126, 正面: 0.874]
----------------------------------------------------------------------
测试 6: 'The plot was predictable and the acting was mediocre at best.'
情感: 负面 😞
置信度: 84.40%
概率分布: [负面: 0.844, 正面: 0.156]
----------------------------------------------------------------------
测试 7: 'A cinematic masterpiece that deserves all the praise.'
情感: 正面 😊
置信度: 76.17%
概率分布: [负面: 0.238, 正面: 0.762]
----------------------------------------------------------------------
测试 8: 'I fell asleep halfway through, it was that boring.'
情感: 负面 😞
置信度: 80.20%
概率分布: [负面: 0.802, 正面: 0.198]
----------------------------------------------------------------------
测试 9: 'The visual effects are stunning and the action sequences are thrilling.'
情感: 正面 😊
置信度: 87.58%
概率分布: [负面: 0.124, 正面: 0.876]
----------------------------------------------------------------------
测试 10: 'Poor script, bad acting, and terrible direction.'
情感: 负面 😞
置信度: 84.85%
概率分布: [负面: 0.849, 正面: 0.151]
----------------------------------------------------------------------
=== 演示完成 ===
```


使用微调后的模型进行推理。使用全部数据集推理展示

```
9. 保存模型...
模型已保存到 ./my_sentiment_model
10. === 推理演示 ===
推理结果:
======================================================================
测试 1: 'This movie is wonderful and inspiring!'
情感: 正面 😊
置信度: 99.70%
概率分布: [负面: 0.003, 正面: 0.997]
----------------------------------------------------------------------
测试 2: 'I really dislike this boring film.'
情感: 负面 😞
置信度: 99.68%
概率分布: [负面: 0.997, 正面: 0.003]
----------------------------------------------------------------------
测试 3: 'The acting is superb and the story is engaging.'
情感: 正面 😊
置信度: 99.55%
概率分布: [负面: 0.004, 正面: 0.996]
----------------------------------------------------------------------
测试 4: 'This is the worst movie ever made, complete waste of time.'
情感: 负面 😞
置信度: 99.81%
概率分布: [负面: 0.998, 正面: 0.002]
----------------------------------------------------------------------
测试 5: 'Nice and enjoyable film with great characters.'
情感: 正面 😊
置信度: 99.60%
概率分布: [负面: 0.004, 正面: 0.996]
----------------------------------------------------------------------
```


### 3.2 基于bert-base-uncased情感微调示例，使用deepspeed优化训练

在容器内执行

```
cd /workspace/examples/
#xxx是单节点可用gpu数量，
torchrun --nproc_per_node=xxx transformers_deepspeed_demo.py
```


结果展示，使用Tesla V100-SXM2-32GB * 2 训练

```
DeepSpeed 训练模型推理结果:
======================================================================
测试 1: 'This movie is wonderful and inspiring!'
情感: 正面 😊
置信度: 99.86%
概率分布: [负面: 0.0014, 正面: 0.9986]
----------------------------------------------------------------------
测试 2: 'I really dislike this boring film.'
情感: 负面 😞
置信度: 99.72%
概率分布: [负面: 0.9972, 正面: 0.0028]
----------------------------------------------------------------------
测试 3: 'The acting is superb and the story is engaging.'
情感: 正面 😊
置信度: 99.82%
概率分布: [负面: 0.0018, 正面: 0.9982]
----------------------------------------------------------------------
测试 4: 'This is the worst movie ever made.'
情感: 负面 😞
置信度: 99.83%
概率分布: [负面: 0.9983, 正面: 0.0017]
----------------------------------------------------------------------
测试 5: 'Nice and enjoyable film with great characters.'
情感: 正面 😊
置信度: 99.83%
概率分布: [负面: 0.0017, 正面: 0.9983]
----------------------------------------------------------------------
=== DeepSpeed 训练演示完成 ===
```