source: https://docs.opencloudos.org/OC9/ai-deployment/ai-application-practice/tensorrt-model-deployment/

# TensorRT-LLM大模型部署指南

TensorRT-LLM 是 NVIDIA 面向大模型推理的高性能编译与服务框架：基于 TensorRT/CUDA，把 Hugging Face 等权重一键编译为高效引擎，内置 FP8/INT8 量化、FlashAttention/融合算子、分页 KV Cache、CUDA Graphs、连续批处理和 推测解码 等优化，并支持 张量/流水线/张量并行 与 NCCL 多卡多机。通过 trtllm-serve 或 Triton 可直接暴露 OpenAI 兼容 API，覆盖 A/H/B 系列 GPU，在保持精度的前提下显著降低 TTFT/ITL、提升 Token 吞吐，适合从在线高并发到离线批量生成的各类部署场景。

本文档将展示如何在 OpenCloudOS 9 操作系统上，通过一键安装脚本和容器镜像拉取，快速启动 TensorRT-LLM 框架和相关推理服务。

## 1.安装容器依赖

### 一键安装容器依赖

脚本下载地址：[点击下载执行脚本](https://ocweb-1319394267.cos.ap-guangzhou.myqcloud.com/docs/scripts/auto_install_vllm.sh)

```
sudo ./auto_install.sh
```


## 2.启动TensorRT-LLM框架镜像

### 2.1下载模型权重

如果已有权重，忽略下载跳转2.2小节，下载权重到位置/models/：

```
# 1. 安装 Git LFS
sudo dnf install -y git-lfs
# 2. 已安装的 Git LFS 注册进 Git
sudo git lfs install
# 3. 下载模型权重到/models/
sudo mkdir -p /models && sudo git clone https://www.modelscope.cn/Qwen/Qwen2.5-7B-Instruct.git /models/Qwen2.5-7B-Instruct
```


### 2.2启动框架

```
sudo docker run -itd --name tensorrt_serving --rm --gpus all -p 8000:8000 -v /models/Qwen2.5-7B-Instruct:/models/Qwen2.5-7B-Instruct opencloudos/opencloudos9-tensorrt_llm tail -f /dev/null
```


## 3.启动推理服务

进入到容器内：

```
sudo docker exec -it tensorrt_serving /bin/bash
```


启动推理服务：

```
trtllm-serve "/models/Qwen2.5-7B-Instruct" --host 0.0.0.0 --port 8000
```


当出现“running on http://**”表示推理服务启动成功：

容器外访问推理服务：

```
curl http://localhost:8000/v1/chat/completions \
-H 'Content-Type: application/json' \
-d '{
"model": "Qwen2.5-7B-Instruct",
"messages": [{"role":"user","content":"你好"}],
"max_tokens": 128
}'
```


## 4.结果展示

## 5.清理环境

```
# 1 停止容器
docker ps # 查找相关容器
docker stop tensorrt_serving
# 2 移除镜像
docker images # 查找相关镜镜像
docker rmi opencloudos/opencloudos9-tensorrt_llm
```