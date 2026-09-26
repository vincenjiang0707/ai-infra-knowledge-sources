source: https://docs.opencloudos.org/en/OC9/ai-deployment/ai-application-practice/vllm-model-deployment/

# vLLM大模型部署指南

vLLM 是专为大模型推理打造的高吞吐、低时延服务引擎，核心是 PagedAttention：像操作系统分页一样管理 KV Cache，解决长上下文/高并发下的显存碎片与抢占问题；配合 continuous batching（连续批处理）、推测解码与算子融合，让首 token 更快、稳态解码更高效。vLLM 原生兼容 HuggingFace 权重，支持单机多卡张量并行、流式输出、分页 KV 量化/压缩等优化，开箱提供 OpenAI 兼容 API（vllm.entrypoints.openai.api_server），易于接入现有应用与监控平台，适合从单机到小规模集群的在线推理与多会话场景。

本文档将展示如何在 OpenCloudOS 9 操作系统上，通过一键安装脚本和容器镜像拉取，快速启动 vLLM 框架和相关推理服务。

## 1.安装容器依赖

### 一键安装容器依赖

脚本下载地址：[点击下载执行脚本](https://ocweb-1319394267.cos.ap-guangzhou.myqcloud.com/docs/scripts/auto_install_vllm.sh)

```
sudo ./auto_install.sh
```


## 2.启动 vLLM 框架镜像

### 2.1 下载模型权重

备注：如果已有权重，请忽略2.1节下载步骤，直接跳转2.2小节，下载权重到位置/models/：

```
1. 安装 Git LFS
sudo dnf install -y git-lfs
2. 已安装的 Git LFS 注册进 Git
sudo git lfs install
3. 下载模型权重到/models/
sudo mkdir -p /models && sudo git clone https://www.modelscope.cn/Qwen/Qwen2.5-7B-Instruct.git /models/Qwen2.5-7B-Instruct
```


### 2.2.启动框架

```
sudo docker run -itd --name vllm_serving --rm --gpus all -p 8000:8000 -v /models/Qwen2.5-7B-Instruct:/models/Qwen2.5-7B-Instruct opencloudos/opencloudos9-vllm tail -f /dev/null
```


## 3.启动推理服务

进入到容器内：

```
sudo docker exec -it vllm_serving /bin/bash
```


启动推理服务：

```
python3 -m vllm.entrypoints.openai.api_server --model /models/Qwen2.5-7B-Instruct/ --served-model-name Qwen2.5-7B-Instruct --max-model-len=2048
```


容器外访问推理服务：

```
curl http://127.0.0.1:8000/v1/chat/completions \
-H 'Content-Type: application/json' \
-d '{
"model": "Qwen2.5-7B-Instruct",
"messages": [{"role":"user","content":"你好"}],
"max_tokens": 128,
"temperature": 0.7,
"stream": false
}'
```


## 4.结果展示

## 5.清理环境

```
# 1 停止容器
docker ps # 查找相关容器
docker stop vllm_serving
# 2 移除镜像
docker images # 查找相关镜镜像
docker rmi opencloudos/opencloudos9-vllm
```