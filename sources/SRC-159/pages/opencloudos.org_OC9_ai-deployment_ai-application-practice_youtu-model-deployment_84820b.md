source: https://docs.opencloudos.org/OC9/ai-deployment/ai-application-practice/youtu-model-deployment/

# Youtu-agent大模型部署指南

Youtu-agent 是面向业务自动化的 LLM 智能体（Agent）工具集：开箱提供命令行对话与可配置的任务流，默认集成**搜索（Serper）与网页读取（Jina）**等工具，通过 OpenAI 兼容 API 对接DeepSeek、Qwen等模型，支持流式输出与可切换的场景配置（如 simple/base_search）。应用层用 .env 配置 UTU_LLM_*（模型/地址/密钥），可在本地或容器中快速部署，用于知识检索、长文摘要、问答与轻量自动化协作，亦可按需扩展更多工具与工作流。

本文档将展示如何在 OpenCloudOS 9 操作系统上，通过一键安装脚本和容器镜像拉取，快速启动 Youtu-agent 框架和相关推理服务。

## 1.安装容器依赖

### 一键安装容器依赖

脚本下载地址：[点击下载执行脚本](https://ocweb-1319394267.cos.ap-guangzhou.myqcloud.com/docs/scripts/auto_install_vllm.sh)

```
sudo ./auto_install.sh
```


## 2.启动Youtu-agent框架镜像

### 2.1 下载模型权重

如果已有权重，忽略下载跳转2.2小节，下载权重到位置/models/：

```
# 1. 安装 Git LFS
sudo dnf install -y git-lfs
# 2. 已安装的 Git LFS 注册进 Git
sudo git lfs install
# 3. 下载模型权重到/models/
sudo mkdir -p /models && sudo git clone https://www.modelscope.cn/Qwen/Qwen2.5-7B-Instruct.git /models/Qwen2.5-7B-Instruct
```


### 2.2 启动框架

```
sudo docker run -itd --name youtu_serving --rm opencloudos/opencloudos9-youtu tail -f /dev/null
```


## 3.启动推理服务

进入到容器内：

```
sudo docker exec -it youtu_serving /bin/bash
```


进入Youtu-agent：

```
cd ./youtu-agent/
```


修改.env:

```
# llm API 需兼容 OpenAI API 格式
# 配置你的 LLM , 可参考 https://api-docs.deepseek.com/
UTU_LLM_TYPE=chat.completions
UTU_LLM_MODEL=deepseek-chat
UTU_LLM_BASE_URL=https://api.deepseek.com/v1
UTU_LLM_API_KEY=<替换为你的 API Key>
# tools
# serper api key, ref https://serper.dev/playground
SERPER_API_KEY=<Access the URL in the comments to get the API Key>
# jina api key, ref https://jina.ai/reader
JINA_API_KEY=<Access the URL in the comments to get the API Key>
```


启动推理服务

```
source .venv/bin/activate
python scripts/cli_chat.py --config simple/base_search
```


## 4.结果展示

## 5.清理环境

```
# 1 停止容器
docker ps # 查找相关容器
docker stop youtu_serving
# 2 移除镜像
docker images # 查找相关镜镜像
docker rmi opencloudos/opencloudos9-youtu
```