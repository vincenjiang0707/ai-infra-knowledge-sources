source: https://docs.mthreads.com/asr/asr-doc-online/sdk

# 客户端 SDK 与请求测试

本文档将介绍如何获取客户端示例代码，并向已部署好的本地 ASR 服务发起语音识别请求。

## 1. 获取客户端代码示例[](https://docs.mthreads.com#1-获取客户端代码示例)

首先，下载并解压包含客户端调用逻辑的示例代码压缩包：

`# 下载客户端代码压缩包`

wget -O client.tar.gz https://mtai-speech.tos-cn-shanghai.volces.com/zhenlinliang/local_asr/funasr_samples.tar.gz


# 解压代码包

tar -xvf client.tar.gz



## 2. 服务推理与验证[](https://docs.mthreads.com#2-服务推理与验证)

解压成功后，进入到对应的 Python 示例目录，使用 Python 脚本进行服务测试。


前置条件：请确保您的环境中已安装 Python 运行环境（建议 Python 3.7+），并根据实际情况安装代码可能需要的相关依赖库。

`# 切换到 Python 客户端示例目录`

cd samples/python/


# 发起服务请求

# 请将 ${YOUR_SERVER_IP} 和 ${YOUR_SERVER_PORT} 替换为您实际的服务端 IP 和端口（例如：10199）

python funasr_wss_client.py \

--host ${YOUR_SERVER_IP} \

--port ${YOUR_SERVER_PORT} \

--mode 2pass \

--audio_in test.wav



### 参数说明：[](https://docs.mthreads.com#参数说明)

`--host`

：服务端所在的服务器 IP 地址。`--port`

：提供本地 ASR 服务的端口号（如安装文档中配置部署的`10199`

）。`--mode`

：识别模式。如`2pass`

模式表示两路机制（即流式实时输出 + 离线最终结果修正）。`--audio_in`

：用于测试识别的输入音频文件路径（此处使用了示例包中自带的`test.wav`

进行验证）。