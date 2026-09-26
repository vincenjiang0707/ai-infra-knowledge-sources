source: https://docs.mthreads.com/playbook/playbook-doc-online/fastapi

# 【中级】FastAPI 本地大模型服务

## 更新日志[](https://docs.mthreads.com#更新日志)

| 版本 | 日期 | 变更描述 |
|---|---|---|
| 1.0.0 | 2026-03-10 | 初始版本，包含在 MTT AIBOOK 上完成基于 FastAPI 可视化界面的本地大模型 API 服务化 |

## 1. 项目简介[](https://docs.mthreads.com#1-项目简介)

本教程旨在指导开发者在 MTT AIBOOK 上通过 FastAPI 完成本地大模型 API 服务化以及快速构建前端界面。

**FastAPI 简介：** FastAPI 是一款功能强大的开源现代 Python Web 框架，专为构建高性能 API 服务和敏捷开发场景设计。它整合了基于 Pydantic 的自动数据验�证、原生异步（Asyncio）并发处理、自动生成交互式 API 文档以及严格的类型提示等核心功能。

**难度：中级，适合有编程基础的开发者体验**

## 2. 前置条件[](https://docs.mthreads.com#2-前置条件)

在开始本教程之前，请确保您已满足以下所有条件：

**硬件要求**：- AI 算力本 MTT AIBOOK，型号 A141
- 网络连接（用于下载模型及依赖包）
- 充足的存储空间（模型文件通常需要数 GB 到几十 GB 空间）

**软件要求**：- MTT AIBOOK 操作系统 AIOS（1.3.3-B17）及以上版本
- 已安装 Python 3.10 或更高版本（
`Python --version`

验证） - 已安装 pip 包管理工具（
`pip --version`

验证） - vLLM-MUSA 推理框架（vLLM 已预装），当前版本对齐 vLLM 社区 0.9.2 版本


## 3. 环境部署[](https://docs.mthreads.com#3-环境部署)

本章节描述如何获取模型文件并完成环境配置。

### 3.1 工具安装[](https://docs.mthreads.com#31-工具安装)

安装 git-lfs 来下载大型文件：

`sudo apt install git-lfs`

git lfs install



### 3.2 下载模型[](https://docs.mthreads.com#32-下载模型)

当前版本对齐 vLLM 社区 v0.9.2，可以在 [Hugging Face](https://huggingface.co/) / [ModelScope](https://www.modelscope.cn/) 直接下载开源模型。对于量化模型，我们提供加速版模型。本教程提供 Qwen2.5-7B GPTQ 模型作为示例：

`git clone https://www.modelscope.cn/hiruyun/gptq-Qwen2.5-7B-Instruct-v2.git`



模型将下载到当前目录下的 `gptq-Qwen2.5-7B-Instruct-v2`

文件夹。

## 4. 最佳实践[](https://docs.mthreads.com#4-最佳实践)

### 场景 1：vLLM 启动模型[](https://docs.mthreads.com#场景-1vllm-启动模型)

#### 1. 脚本编写[](https://docs.mthreads.com#1-脚本编写)

通过脚本方式启动 vLLM 服务，提供模型推理 API：

注：vLLM server 后面跟的是下载模型的位置，请替换成自己的


**vLLM_start.sh:**

`#!/bin/bash`


# 注意：这里可能会提示输入 Linux 用户的密码

sudo sh -c "echo 3 > /proc/sys/vm/drop_caches"

echo "✅ 内存清理完成！"


# 设置 Triton 编译缓存目录

export TRITON_CACHE_DIR="/tmp/triton"


# 启动 vLLM 模型，请替换自己的模型路径

vLLM serve /home/devtech/下载/models/gptq-Qwen2.5-7B-Instruct-v2 \

--tensor-parallel-size 1 \

--gpu-memory-utilization 0.7 \

--quantization gptq \

--block-size 32 \

--num-gpu-blocks-override 1024 \

--max-model-len 16384 \

--swap-space 0 \

--enforce-eager \

--port 8000



#### 2. 设计思考[](https://docs.mthreads.com#2-设计思考)

**资源预留**：通过`--gpu-memory-utilization 0.7`

预留了 30% 显存，防止 FastAPI 进程或其他应用抢占显存导致 OOM（内存溢出）**兼容性设计**：vLLM 默认提供与 OpenAI 格式对齐的接口，这使得前端业务代码可以无缝切换不同的后端模型

#### 3. 预期现象[](https://docs.mthreads.com#3-预期现象)

### 场景 2：FastAPI 快速调用[](https://docs.mthreads.com#场景-2fastapi-快速调用)

#### 1. 启动场景 1 的大模型[](https://docs.mthreads.com#1-启动场景-1-的大模型)

`bash vLLM_start.sh`



**设计思考：**

**服务解耦**：将推理层（vLLM）与业务层（FastAPI）分离，可以确保业务逻辑的修改不会导致模型重新加载，极大提升开发效率

#### 2. 创建代码文件[](https://docs.mthreads.com#2-创建代码文件)

`touch fastapi_demo1.py`



#### 3. 进行依赖引入和变量设置[](https://docs.mthreads.com#3-进行依赖引入和变量设置)

`from fastapi import FastAPI`

from pydantic import BaseModel

import httpx

import uvicorn


# 定义变量

APP_HOST = "0.0.0.0" # 允许局域网访��问

APP_PORT = 7769 # 本地服务的端口

VLLM_URL = "http://127.0.0.1:8000/v1/chat/completions" # 底层 vLLM 地址

TIMEOUT = 90000.0 # 超时时间（秒）


# 请修改成你自己的模型路径

MODEL_PATH = "/home/mt/下载/models/gptq-Qwen2.5-7B-Instruct-v2"


# [推理超参数]

TEMPERATURE = 0.1 # 采样温度（0.1 较严谨，越高越随机）

REPETITION_PENALTY = 1.1 # 重复惩罚系数

MAX_TOKENS = 2048 # 最大生成长度



**设计思考：**

`APP_HOST = "0.0.0.0"`

：设置为主机监听模式，使得同一局域网内的其他设备也能通过 IP 访问该接口`TIMEOUT`

：由于大模型推理（尤其是生成长文本时）耗时较长，这里设置了一个较大的超时时间，防止连接意外中断**超参数��配置**：将`TEMPERATURE`

等参数提取为全局变量，方便后续根据业务场景（如：需要严谨回答还是创意回答）进行快速调整

#### 4. 数据结构定义[](https://docs.mthreads.com#4-数据结构定义)

利用 FastAPI 内置的 Pydantic 支持，定义接口接收的数据格式：

`app = FastAPI() # 初始化 Web 框架实例`


class AskRequest(BaseModel):

text: str



**代码解析：**

`FastAPI()`

：初始化 Web 框架实例`AskRequest`

：通过继承`BaseModel`

定义请求体。它会自动校验客户端发送的 JSON 数据是否包含`text`

字段且类型为字符串，如果不符将自动返回标准的错误响应

#### 5. 核心业务逻辑[](https://docs.mthreads.com#5-核心业务逻辑)

`@app.post("/ask")`

async def ask_model(req: AskRequest):

# 构造请求载荷，所有参数均来自前面的变量

payload = {

"model": MODEL_PATH, # 指定模型名称

"messages": [

{"role": "user", "content": req.text} # 用户输入的内容

],

"temperature": TEMPERATURE,

"repetition_penalty": REPETITION_PENALTY,

"max_tokens": MAX_TOKENS

}


# 异步请求底层的 vLLM 服务

async with httpx.AsyncClient() as client:

resp = await client.post(

VLLM_URL,

json=payload,

timeout=TIMEOUT

)


# 解析并提取文本

result_json = resp.json()

answer = result_json["choices"][0]["message"]["content"]

return {"reply": answer}



**设计思考：**

**异步非阻塞**：使用`async with httpx.AsyncClient()`

可以在等待模型推理结果的同时，不阻塞服务器处理其他并发请求，是构建高性能 API 的关键

**代码解析：**

`payload`

：严格遵循 OpenAI API 协议格式封装数据，确保与后端的 vLLM 服务完美对接`result_json["choices"][0]...`

：由于 LLM 的标准返回格式较为复杂，通过该路径可以直接剥离冗余信息，仅向前端返回最核心的文字内容

#### 6. 程序入口[](https://docs.mthreads.com#6-程序入口)

配置 Uvicorn 运行参数，启动 Web 服务：

`if __name__ == "__main__":`

uvicorn.run(app, host=APP_HOST, port=APP_PORT)



#### 7. 完整代码[](https://docs.mthreads.com#7-完整代码)

**fastapi_start.py:**

`from fastapi import FastAPI`

from pydantic import BaseModel

import httpx

import uvicorn


APP_HOST = "0.0.0.0" # 允许局域网访问

APP_PORT = 7769 # 本服务的端口

VLLM_URL = "http://127.0.0.1:8000/v1/chat/completions" # 底层 vLLM 地址

TIMEOUT = 90000.0 # 超时时间（秒）


# 请修改成你自己的模型路径

MODEL_PATH = "/home/mt/下载/models/gptq-Qwen2.5-7B-Instruct-v2"


# [推理超参数]

TEMPERATURE = 0.1 # 采样温度（0.1 较严谨，越高越随机）

REPETITION_PENALTY = 1.1 # 重复惩罚系数

MAX_TOKENS = 2048 # 最大生成长度


app = FastAPI()


class AskRequest(BaseModel):

text: str


@app.post("/ask")

async def ask_model(req: AskRequest):

# 构造请求载荷，所有参数均来自前面的变量

payload = {

"model": MODEL_PATH,

"messages": [

{"role": "user", "content": req.text}

],

"temperature": TEMPERATURE,

"repetition_penalty": REPETITION_PENALTY,

"max_tokens": MAX_TOKENS

}


# 异步请求底层的 vLLM 服务

async with httpx.AsyncClient() as client:

resp = await client.post(

VLLM_URL,

json=payload,

timeout=TIMEOUT

)


# 解析并提取文本

result_json = resp.json()

answer = result_json["choices"][0]["message"]["content"]

return {"reply": answer}


if __name__ == "__main__":

uvicorn.run(app, host=APP_HOST, port=APP_PORT)



#### 8. 测试和效果展示[](https://docs.mthreads.com#8-测试和效果展示)

**直接执行：**

`python fastapi_demo1.py`



**预期状况：**

**访问 http://localhost:7769/docs**

（7769 是在代码中定义的端口，若该端口已有服务可更换其他端口）

- 展开请求，点击
**"Try it out"** - 输入你想提问的问题并点击
**"Execute"** - 大模型回答内容会展示在 Responses 里

**参数解析：**

`curl`

：当你点击 Execute 的时候 Swagger 不仅帮你发了请求，还把你刚才的操作自动翻译成了等价的 curl 命令`Request URL`

：就是本次请求发送的目标**响应状态码**：200 代表成功

### 场景 3：Python 脚本调用[](https://docs.mthreads.com#场景-3python-脚本调用)

我们也可以不去前端，直接通过 Python 脚本调用。

#### 1. 编写代码 ask_client.py[](https://docs.mthreads.com#1-编写代码-ask_clientpy)

`import requests`


# ==================== 配置区 (修改这里) ====================


# [1] 服务器的地址 (对应你 FastAPI 的 APP_HOST 和 APP_PORT)

# 如果在本机运行，用 127.0.0.1；如果在局域网其他电脑，用实际 IP

API_URL = "http://127.0.0.1:7769/ask"


# [2] 你想询问的问题

USER_QUESTION = "请问什么是大模型 API 服务化？"


# ==================== 执行区 (直接运行) ====================


def start_ask():

# 构造请求数据，必须对应 FastAPI 里的 AskRequest 结构

payload = {

"text": USER_QUESTION

}


try:

# 发送 POST 请求

response = requests.post(API_URL, json=payload, timeout=120)


# 检查是否请求成功

response.raise_for_status()


# 解析返回的结果

result = response.json()


print(f"\n🚀 问：{USER_QUESTION}")

print(f"🤖 答：{result.get('reply')}\n")


except Exception as e:

print(f"❌ 调用失败，请确保 FastAPI 脚本已启动。错误信息：{e}")


if __name__ == "__main__":

start_ask()



#### 2. 测试运行[](https://docs.mthreads.com#2-测试运行)

**执行脚本：**

`python ask_client.py`



## 5. 附录[](https://docs.mthreads.com#5-附录)

### 5.1 常见问题[](https://docs.mthreads.com#51-常见问题)

| 问题描述 | 可能原因 | 解决方案 |
|---|---|---|
端口报错：运行时报错 `address ('0.0.0.0', 7769): address already in use` | 7769 端口已有服务 | 选择其他端口或者 `sudo lsof -i :7769` 查看占用进程 |
| vLLM 服务启动失败 | 模型路径错误、GPU 内存不足 | 检查模型路径是否正确，降低 `gpu-memory-utilization` 参数值 |
| 模型拉取失败 | 网络问题或路径错误 | 检查网络确认正常，换其他模型 |
打开页面显示 `"detail":"Not Found"` | 访问地址不正确，API 根目录无默认页面 | 请在网页末尾加 `/docs` ，如：`http://localhost:7769/docs` |
`"POST /ask HTTP/1.1" 500 Internal Server Error` | 询问的问题超时未回答 | 将 `TIMEOUT` 时间设置长一点，如 9000 |

### 5.2 相关资源[](https://docs.mthreads.com#52-相关资源)

**FastAPI 官网（了解 FastAPI 更多功能与方法）：**[https://fastapi.tiangolo.com/zh/](https://fastapi.tiangolo.com/zh/)**vLLM 官网（了解 LLM 高效推理引擎）：**[https://docs.vllm.ai/](https://docs.vllm.ai/)**ModelScope 官网（国内开源 AI 模型社区）：**[https://www.modelscope.cn/home](https://www.modelscope.cn/home)**Python 官方文档（学习 Python 基础语法）：**[https://docs.python.org/3/](https://docs.python.org/3/)