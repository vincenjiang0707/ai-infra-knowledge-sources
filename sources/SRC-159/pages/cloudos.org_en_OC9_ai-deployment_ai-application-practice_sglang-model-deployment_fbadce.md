source: https://docs.opencloudos.org/en/OC9/ai-deployment/ai-application-practice/sglang-model-deployment/

# SGLang大模型部署指南

SGLang 是一个面向大语言模型（LLM）的高性能推理与服务框架，主打低时延与高并发：内置连续批处理、分块预填充（chunked prefill）与分页 KV Cache 等优化，结合推测解码/算子融合，让长上下文与多会话场景也能稳定吐字；支持多卡并行（如张量并行）、流式输出与监控指标，兼容 OpenAI 风格 API，开箱即可为 Qwen/DeepSeek 等模型提供高吞吐在线服务，适合从单机到多机的推理部署与二次开发。

本文档将展示如何在 OpenCloudOS 9 操作系统上，通过一键安装脚本和容器镜像拉取，快速启动 SGLang 框架和相关推理服务。

## 1.安装容器依赖

### 一键安装容器依赖

脚本下载地址：[点击下载执行脚本](https://ocweb-1319394267.cos.ap-guangzhou.myqcloud.com/docs/scripts/auto_install_vllm.sh)

```
sudo ./auto_install.sh
```


[查看该链接](https://gitee.com/OpenCloudOS/Document/blob/master/docs/OC9/ai-deployment/ai-application-practice/auto_install.sh)。

## 2.启动SGLang框架镜像

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
sudo docker run -itd --name sglang_serving --rm --gpus all -p 30000:30000 -v /models/Qwen2.5-7B-Instruct:/models/Qwen2.5-7B-Instruct opencloudos/opencloudos9-sglang tail -f /dev/null
```


## 3.启动推理服务

进入到容器内：

```
sudo docker exec -it sglang_serving /bin/bash
```


启动推理服务：

```
python3 -m sglang.launch_server --model-path /models/Qwen2.5-7B-Instruct/ --tp 1 --mem-fraction-static 0.7 --chunked-prefill-size 2048 --host 0.0.0.0
```


容器外访问推理服务：

```
curl -s http://127.0.0.1:30000/generate \
-H 'Content-Type: application/json' \
-d '{
"text": "介绍下自己",
"sampling_params": {
"max_new_tokens": 64,
"temperature": 0.8,
"top_p": 0.95
}
}'
```


## 4.结果展示

## 5.清理环境

```
# 1 停止容器
docker ps # 查找相关容器
docker stop sglang_serving
# 2 移除镜像
docker images # 查找相关镜镜像
docker rmi opencloudos/opencloudos9-sglang
```