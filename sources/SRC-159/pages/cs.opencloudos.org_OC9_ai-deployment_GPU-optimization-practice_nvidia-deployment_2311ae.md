source: https://docs.opencloudos.org/OC9/ai-deployment/GPU-optimization-practice/nvidia-deployment/

# 基于 OpenCloudOS 的 NVIDIA 部署实践

目前，OpenCloudOS 9 已实现对 NVIDIA Driver 和 CUDA 的深度适配和原生支持，为使用 NVIDIA GPU 用户提供了完整的 RPM 二进制软件包，包括内核级驱动、系统管理工具、计算库及AI框架适配组件。

本文档将指导如何在 OpenCloudOS 9 上快速完成NVIDIA Driver 和 CUDA 的安装部署，并无缝运行上层AI模型与应用。

## 一、基础环境要求及说明

1、 **支持 OpenCloudOS 内核版本** ：6.6内核（含其间各小版本）。如您使用的是 OpenCloudOS 7或8系列（5.4内核），建议您升级至 OpenCloudOS 9 版本（6.6 内核）。

2、 **支持的 GPU 驱动和对应CUDA 版本** ：

| 驱动版本 | 对应CUDA版本 |
|---|---|
| 525.147.05 | 12.0.1 |
| 530.41.03 | 12.1.1 |
| 535.274.02 | 12.2.2 |
| 545.29.06 | 12.3.2 |
| 550.163.01 | 12.4.1 |
| 555.58.02 | 12.5.1 |
| 560.35.03 | 12.6.3 |
| 570.195.03 | 12.8.1 |
| 575.64.05. | 12.9.1 |
| 580.95.05. | 13.0.1 |

3、 **支持的CUDA 版本** ：11.8.0、 12.0.1、 12.1.1、 12.2.2、 12.3.2、 12.4.1、 12.5.1、 12.6.3、 12.8.1、 12.9.1、 13.0.1。

## 二、安装 NVIDIA Driver

### 2.1 安装 OpenCloudOS EPOL源

```
dnf install epol-release
```


### 2.2 安装 NVIDIA Driver 驱动包

此处以 Nvidia-Driver-570 为例，若要安装其他版本，将对应软件包名中的版本号 570 替换为目标版本号即可。

备注：NVIDIA Driver 分为开源和闭源版本，因此部署流程中将分为开源模块安装和闭源模块安装两部分。关于闭源、开源模块的详细解释请见文末（附录二）。

```
# 安装开源模块
dnf install -y kmod-nvidia-570-dkms-open nvidia-570 nvidia-driver-570-open
# 安装闭源模块
dnf install -y kmod-nvidia-570-dkms nvidia-570 nvidia-driver-570
```


### 2.3 安装验证

```
# 重启机器
sudo reboot
# 查看已安装的驱动软件包
dnf list installed | grep nvidia
# 查看驱动信息
nvidia-smi
```


其中，Driver Version 为当前安装的驱动版本，CUDA Version 为当前安装的驱动所支持的最高CUDA Runtime API版本。

### 2.4 卸载驱动安装包

```
# 卸载开源模块
dnf remove -y kmod-nvidia-535-dkms-open nvidia-535 nvidia-driver-535-open
# 卸载闭源模块
dnf remove -y kmod-nvidia-535-dkms nvidia-535 nvidia-driver-535
```


## 三、安装 CUDA

针对用户需求以及使用场景的不同，OpenCloudOS 团队采用了全新的打包方案：

| 优化方向 | 传统方案 | 新方案 |
|---|---|---|
| 包结构 | 细分子包 | 拆分为 runtime/devel 两类子包 |
| 组件分层 | 静态库/工具与运行时捆绑 | 划分可执行文件、.so 动态库、头文件、.a 静态库 |

其中，runtime/ devel，对应组件范围如下：

| 类型 | 组件范围 | 适用场景 |
|---|---|---|
| Runtime | 可执行文件 + .SO 动态库 | 轻量级生产部署 |
| Devel | runtime + 头文件 + .a 静态库 | 代码编译/模型训练 |

### 3.1 安装 CUDA 组件

此处以 cuda-12-8 为例，若要安装其他版本，将 12-8 替换为目标版本即可。

**Runtime 包安装：**

```
dnf install -y cuda-runtime-12-8
```


**Devel 包安装：**

```
dnf install -y cuda-devel-12-8
```


### 3.2 安装验证

```
# 查看已安装的 cuda 软件包
dnf list installed | grep cuda
# 查看 cuda 版本
nvcc --version
```


### 3.3 多版本共存支持（如需）

新版打包方案完美解决了 CUDA 多版本共存的问题，可下载多个版本的 CUDA，利用 update-alternatives 进行版本切换。如需兼容 CUDA 多版本共存，请参考 3.1 节中的 CUDA 安装方式，依次安装所需版本即可。例如，若同时安装 CUDA 12.2 与 12.9 版本，效果如下所示：

### 3.4 卸载CUDA组件

**Runtime 包安装：**

```
dnf remove -y cuda-runtime-12-8 cuda-toolkit-12-8-config-common
```


**Devel 包安装：**

```
dnf remove -y cuda-runtime-12-8 cuda-toolkit-12-8-config-common cuda-12-8 cuda-devel-12-8 cuda-toolkit-12-8
```


## 四、AI 应用安装与验证

### 4.1 运行大模型（以vLLM框架+Qwen示例）

#### 4.1.1 安装 uv

```
# 下载 uv
dnf install pip
pip install uv
# 推荐使用 uv 安装，智能处理依赖冲突
uv pip install vllm==0.10.0 --system
```


#### 4.1.2 服务启动

```
# 启动 vllm 服务，拉取大模型（此处以 Qwen 为例）
vllm serve "Qwen/Qwen3-0.6B"
# 若机器配置较低，可尝试如下命令启动服务
vllm serve "Qwen/Qwen3-0.6B" --gpu-memory-utilization 0.7 --max-model-len 1024 --max-num-seqs 4 --dtype float16 --block-size 16
```


运行界面如下

### 4.2 结果展示

**示例（1）：命令行测试**

```
# 另起终端
curl -X POST "http://localhost:8000/v1/chat/completions" -H "Content-Type: application/json" --data '{"model": "Qwen/Qwen3-0.6B","messages": [{"role": "user","content": "What is the capital of France?"}]}'
```


运行界面如下

**示例（2）：python代码部署和推理**

创建python程序，内容如下：

```
from vllm import LLM, SamplingParams
from transformers import AutoTokenizer
# 初始化模型参数
model_path = "Qwen/Qwen3-0.6B" # 替换为实际模型路径
llm = LLM(
model=model_path,
dtype="half", # 启用半精度推理（FP16）
trust_remote_code=True, # 对Hugging Face模型必须开启
tensor_parallel_size=1, # 单GPU运行
gpu_memory_utilization=0.8 # 显存利用率控制
)
# 配置生成参数
sampling_params = SamplingParams(
temperature=0.7,
top_p=0.95,
max_tokens=256,
repetition_penalty=1.1
)
# 构建对话模板
messages = [
{"role": "system", "content": "你是一个诗人"},
{"role": "user", "content": "写一首关于春天的七言绝句"}
]
tokenizer = AutoTokenizer.from_pretrained(model_path)
prompt = tokenizer.apply_chat_template(
conversation=messages,
tokenize=False,
add_generation_prompt=True
)
# 执行推理
outputs = llm.generate(
prompts=[prompt],
sampling_params=sampling_params
)
# 输出结果
for output in outputs:
generated_text = output.outputs[0].text
print(f"生成结果：\n{generated_text}")
```


### 4.3 运行大模型（以Ollama+Qwen示例）

#### 4.3.1 安装

```
# 安装依赖
dnf install -y gawk
# 下载安装脚本并安装
curl -fsSL https://ollama.com/install.sh | sh
```


#### 4.3.2 服务启动

```
# 服务启动
ollama serve
```


#### 4.3.3 运行Qwen模型

```
# 拉取大模型（此处以qwen为例）
ollama run qwen3:0.6b
```


## 附录：

### 附一：部署过程中可能出现的常见问题及处理方案：

**1） nvidia-smi 显示的 CUDA Version 与实际 CUDA 版本不一致**

需要注意的是，nvidia-smi 命令展示的结果中：Driver Version 和 CUDA Version 的对应关系。Driver Version 是当前安装的驱动版本，CUDA Version 代表驱动所支持的最高CUDA Runtime API版本，并不是不是 cuda-toolkit 版本。要查看 cuda-toolkit 版本，需要执行命令 nvcc --version。

**2）cuda-compat 问题（driver与cuda版本兼容）**

对于 CUDA 而言，每个 cuda 版本都有最合适的 Driver 版本。“每个 CUDA 工具包还附带 NVIDIA 显示驱动程序包，该驱动程序支持该版本的 CUDA 工具包中引入的所有功能”， 相当于是这个 cuda 版本开发时就根据这个版本的 Driver 开发的，功能上最兼容的一个版本对应关系。

这个最完美的版本对应关系在release说明中的 Table3 CUDA Toolkit and Corresponding Driver Versions可以看到。但是，如果想在一个比较老的 Driver 上跑比较新的 CUDA 版本，或则在一个比较新的 Driver 上跑一个比较老的 CUDA 版本，就涉及兼容性问题了。

为了让高版本的 CUDA 在较旧的硬件设备上运行，官方发布了cuda-compat包，用于兼容这种场景，效果表现为：高版本 CUDA 只能使用当前驱动所支持的最高版本 CUDA 的功能，而CUDA 升级所带来的功能无法使用，可以理解为当前 CUDA 的版本降级。

具体结论如下：

- 驱动版本 >= cuda版本，cuda不装compat，正常；装了compat，可能会有异常；
- 驱动版本 < cuda版本，cuda必须装compat。

**3）低版本 cuda 上运行 AI 框架时库文件缺失问题--vLLM**

vLLM 核心架构是自研高性能 C++/CUDA 内核，深度集成 PyTorch，编译时链接特定版本的 CUDA 运行时，与 PyTorch 的 CUDA 版本强相关。而高版本的 vLLM 都是根据较新的 PyTorch 来进行构建，因此在较低版本的系统 CUDA 环境中编译 vLLM 时会出现关键 symbol 缺失问题，如下：

在 cuda 12.2 中编译 vLLM 时会出现 cupti 相关 symbol 缺失问题，分析发现，PyTorch / Triton 自带的CUPTI库包含所需符号，但cuda12.2包含的CUPTI库没有所需符号：

切换到高版本的 cuda 12.9 环境时，测试结果包含目标symbol且可以成功运行：


这种情况下，执行命令：

```
export
LD_LIBRARY_PATH=/usr/local/lib/python3.11/site-packages/nvidia/cuda_cupti/lib:$LD_LIBRARY_PATH
```


### 附二：关于NVIDIA Driver 闭源及开源部分解释

NVIDIA Driver 分为开源和闭源版本。

闭源驱动由 NVIDIA 公司官方提供，内核模块来自 NVIDIA 官方 .run安装包中的闭源代码，通常拥有最新的功能和最优化的性能，包括对 NVIDIA 最新显卡架构的支持，以及对 DirectX、OpenGL 等图形接口的完整支持。缺点是它们不开放源代码，这可能会限制它们与 Linux 内核的兼容性，并且在社区支持方面不如开源驱动。

开源驱动（如 nouveau）是由社区维护的，内核模块来自 open-gpu-kernel-modules 仓库的开源代码，可以更好地与 Linux 内核集成。尽管它们可能在功能/性能上不如闭源驱动全面，但在某些方面，如内核兼容性，它们表现得更为出色。