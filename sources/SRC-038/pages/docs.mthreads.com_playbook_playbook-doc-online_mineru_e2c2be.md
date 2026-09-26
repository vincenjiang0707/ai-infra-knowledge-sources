source: https://docs.mthreads.com/playbook/playbook-doc-online/mineru

# 【中级】部署 Mineru

## 更新日志[](https://docs.mthreads.com#更新日志)

| 版本 | 日期 | 变更描述 |
|---|---|---|
| 1.0.0 | 2026-02-09 | 初始版本，包含在 MTT AIBOOK 上安装和部署 Mineru 的完整指南。 |
| 1.0.1 | 2026-08-11 | 更新对 vLLM 环境部署的相关描述。 |

## 1. 项目简介[](https://docs.mthreads.com#1-项目简介)

本教程旨在指导开发者在 MTT AIBOOK 上部署并运行 Mineru，帮助您快速体验用 Mineru 批量转化复杂的 PDF 文件为 Markdown 格式。

**Mineru 简介：** MinerU 是一款功能强大的开源�智能文档结构化解析工具，专为 AI 场景文档处理和高效信息提取设计。它整合了智能版面分析、多模态内容提取、多语言 OCR 识别和多格式精准输出等核心功能，支持 PDF、图片等多类型文档向 Markdown、JSON 等机器可读格式的高质量转换。

## 2. 前置条件[](https://docs.mthreads.com#2-前置条件)

在开始本教程之前，请确保您已满足以下所有条件：

**硬件:**- AI 算力本 MTT AIBOOK，型号 A141
- 网络连接（用于下载模型及依赖包）
- 充足的存储空间（模型文件通常需要数 GB 到几十 GB 空间）

**软件:**- MTT AIBOOK 操作系统 AIOS（1.3.3-B17）及以上版本


## 3. 环境部署[](https://docs.mthreads.com#3-环境部署)

本章节描述如何部署 Mineru 的环境。

### 3.1 检查并安装 Conda[](https://docs.mthreads.com#31-检查并安装-conda)

-
**检查 Conda 是否已安装：**conda --version若已安装则终端会返回类似下方这样的版本信息，您可以直接跳到 3.2 节：

conda 25.11.1 -
**安装 Conda：**wget https://mirrors.tuna.tsinghua.edu.cn/github-release/conda-forge/miniforge/LatestRelease/Miniforge3-Linux-aarch64.shchmod +x Miniforge3-Linux-aarch64.sh./Miniforge3-Linux-aarch64.sh# 安装过程中需要输入 `yes` 并回车确认安装路径，默认安装路径在 `/home/$User`。source ~/.bashrc # 激活 conda

### 3.2 创建并激活 Conda 环境[](https://docs.mthreads.com#32-创建并激活-conda-环境)

**创建 Conda 虚拟环境：**

`conda create -n Mineru python=3.10`

conda activate Mineru



请确保接下来的操作都是在激活 Mineru 虚拟环境后的操作，命令行前面应该有您创建的 conda 环境名字 `(Mineru)`

。若没有可以执行以下命令激活：

`conda activate Mineru`



### 3.3 下载 Mineru 源码[](https://docs.mthreads.com#33-下载-mineru-源码)

`git clone https://github.com/opendatalab/MinerU.git`



若无法从 GitHub 站点下载源码工程，可从 Gitee 站点下载：

`git clone https://gitee.com/open-data-lab/MinerU.git`



### 3.4 安装 Mineru 依赖[](https://docs.mthreads.com#34-安装-mineru-依赖)

进入 Mineru 源码文件夹安装相关依赖：

`cd MinerU`

pip install -e .[core] -i https://mirrors.aliyun.com/pypi/simple



### 3.5 安装 PyTorch 和 vLLM 来支持 MUSA 加速[](https://docs.mthreads.com#35-安装-pytorch-和-vllm-来支持-musa-加速)

本文档将基于 vLLM 进行本地大模型的推理，因此需要安装部署 vLLM 及其相关依赖的环境，在确认 MTT AIBOOK 的系统版本后，根据以下链接的网页跳转到对应系统版本的安装部署指导文档，部署正确的 vLLM 及其环境依赖：

[https://docs.mthreads.com/vllm-musa-m1000/vllm-musa-m1000-doc-online/AIBook/](https://docs.mthreads.com/vllm-musa-m1000/vllm-musa-m1000-doc-online/AIBook/)

根据文档指引部署成功后，即可进行下一步。

注意：AIOS 1.5.0 及以上版本，相关的 vLLM 及 vLLM 依赖环境将由系统自动更新，而无需用户手动更新。

### 3.6 下载模型[](https://docs.mthreads.com#36-下载模型)

运行以下脚本：

`mineru-models-download`



建议选择 ModelScope（国内下载源更快）：

`Please select the model download source: (huggingface, modelscope) [huggingface]: modelscope`

Please select the model type to download: (pipeline, vlm, all) [all]: all

#自己选择源,直接回车默认是 huggingface



## 4. 最佳实践[](https://docs.mthreads.com#4-最佳实践)

本章节指导您完成 Mineru 的开发、配置和使用流程。

### 场景 1: 命令行启动 Mineru 的 Pipeline 模式解析对应文件夹的所有 PDF[](https://docs.mthreads.com#场景-1-命令行启动-mineru-的-pipeline-模式解析对应文件夹的所有-pdf)

-
**激活 Conda 虚拟环境：**conda activate Mineru -
**准备好你想解析的 PDF 文件并执行以下命令：**mineru -p ./pdfs/ -o ./output -b pipeline --source local -d musa:0**参数说明：**参数 说明 示例 `-p`

指定待解析的 PDF 文件/文件夹位置 `./pdfs/demo1.pdf`

或`./pdfs/`

`-o`

指定结果输出位置 `./output`

`-b`

指定启动模式 `pipeline`

`--source`

模型来源 `local`

（本地已有模型）`-d musa:0`

MUSA 加速参数 不建议更改或删除 执行后会看到下面类似输出：

-
**结果展示：（后续场景使用中的结果与其类似）**解析产物会存放在当前目录的

`/output`

文件夹内：(是上面`-o`

对应的位置)。**解析产物说明：**产物 说明 示例 `*.md`

Mineru 解析后的 Markdown 文件 `demo2.md`

`*_origin.pdf`

原始输入 PDF 的副本��，方便对照检查 `demo2_origin.pdf`

`*_span.pdf`

可视化调试文件，用细框标出最小粒度的文本/元素边界框 `demo2_span.pdf`

`*_layout.pdf`

可视化调试文件，用色块标出识别到的版面结构 `demo2_layout.pdf`

`images/`

存放从文档中提取的图片、公式截图、图表 - - 解析产物一: Markdown 文件
- 解析产物二：
`*_origin.pdf`

(`*`

代表你通过 Mineru 选定的 PDF 文件名，后面出现类似格式)。 原始输入 PDF 的副本，方便对照检查解析结果 - 解析产物三：·
`*_span.pdf`

： 可视化调试文件，用细框标出最小粒度的文本 / 元素边界框，用排查识别问题： - 解析产物四：
`*_layout.pdf`

可视化调试文件，用色块标出识别到的版面结构（标题、文本、图片、表格等）： - 解析产物五：
`images/`

存放的是从文档中提取的图片、公式截图、图表，与`*.md`

中的图片引用关联提取的表格：


### 场景 2: Hybrid-Auto-Engine 模式[](https://docs.mthreads.com#场景-2-hybrid-auto-engine-模式)

与场景 1 类似，使用 `-b`

选择 `hybrid-auto-engine`

模式：

`mineru -p ./pdfs/ -o ./output -b hybrid-auto-engine --source local -d musa:0`



结果展示请参考[场景1](https://docs.mthreads.com#%E5%9C%BA%E6%99%AF-1-%E5%91%BD%E4%BB%A4%E8%A1%8C%E5%90%AF%E5%8A%A8-mineru-%E7%9A%84-pipeline-%E6%A8%A1%E5%BC%8F%E8%A7%A3%E6%9E%90%E5%AF%B9%E5%BA%94%E6%96%87%E4%BB%B6%E5%A4%B9%E7%9A%84%E6%89%80%E6%9C%89-pdf)。

### 场景 3: 命令行参数详解[](https://docs.mthreads.com#场景-3-命令行参数详解)

参数 | 参数说明 | 推荐/建议值 |
|---|---|---|
`-p` | 指定要分析的 PDF 文件路径，可以是包含多个 PDF 文件的文件夹路径 | 按需填写实际的文件/文件夹路径 |
`-o` | 指定解析后产物的存放路径 | 按需填写实际的存放路径 |
`-b` | 指定要启动的 Mineru 模式 | `pipeline` / `hybrid-auto-engine` |
`--source` | 指定 Mineru 启动模型的位置 | `local` （本地已有模型，无需检验下载，节省时间）；模型更新后可选用 `modelscope` / `huggingface` |
`-d musa:0` | MUSA 加速参数 | 不建议更改或删除 |

### 场景 4: FastAPI 方式调用[](https://docs.mthreads.com#场景-4-fastapi-方式调用)

-
设置环境变量

export MINERU_MODEL_SOURCE=localexport MINERU_DEVICE_MODE=musa:0export VLLM_USE_V1=1 -
执行命令启动服务

mineru-api --host 0.0.0.0 --port 8000提示**注意事项：**`--port`

是端口参数，可通过`sudo lsof -i:8000`

来查询 8000 端口是否被占用。- 若占用则选择其他端口。

-
访问对应网址

`http://0.0.0.0:8000/docs`

-
点击

**try it out**： -
参数选择：

- 选择对应的要解析的文件。
- 设置
`output_dir`

为对应的输出目录。 - 模式
`backend`

只推荐使用`pipeline`

模式。

运行时后台有相关日志，显示对应产出结果位置。 具体最终产出结果文件的意义参考场景一的结果展示。


### 场景 5: 启动Gradio WebUI 可视化前端[](https://docs.mthreads.com#场景-5-启动gradio-webui-可视化前端)

-
配置环境变量：

export MINERU_MODEL_SOURCE=localexport MINERU_DEVICE_MODE=musa:0export VLLM_USE_V1=1 -
启动服务：

mineru-gradio --server-name 0.0.0.0 --server-port 7860若 7860 端口被占用请选择其他端口。更多关于端口是否被占用，可参考

[场景四](https://docs.mthreads.com#%E5%9C%BA%E6%99%AF-4-fastapi-%E6%96%B9%E5%BC%8F%E8%B0%83%E7%94%A8)的注意事项。 -
访问 WebUI：

打开浏览器访问

`http://0.0.0.0:7860`

。 -
上传你要解析的 PDF：

- 上传你要解析的 PDF。
- 选择
`hybrid-auto-engine`

或者`pipeline`

模式。 - 点击启用（vLLM 模式暂不支持）。

**解析结果：**

### 常用操作命令[](https://docs.mthreads.com#常用操作命令)

| 操作 | 命令 |
|---|---|
| 检查 Conda | `conda --version` |
| 激活 Conda 环境 | `conda activate Mineru` |
| 下载 Mineru 源码 | `git clone https://gitee.com/open-data-lab/MinerU.git` |
| 安装 Mineru 依赖 | `pip install -e .[core] -i https://mirrors.aliyun.com/pypi/simple` |
| Pipeline 模式解析 | `mineru -p ./pdfs/ -o ./output -b pipeline --source local -d musa:0` |
| Hybrid 模式解析 | `mineru -p ./pdfs/ -o ./output -b hybrid-auto-engine --source local -d musa:0` |
| 启动 FastAPI 服务 | `mineru-api --host 0.0.0.0 --port 8000` |
| 启动 Gradio WebUI | `mineru-gradio --server-name 0.0.0.0 --server-port 7860` |
| 下载模型 | `mineru-models-download` |
| 查询端口占用 | `sudo lsof -i:8000` |

## 5. 附录[](https://docs.mthreads.com#5-附录)

### 5.1 Mineru 亮点[](https://docs.mthreads.com#51-mineru-亮点)

-
**文档解析精准且全面：**- 可高精度还原含合并单元格、跨页单元格的表格。
- 输出标准 HTML 或 Markdown 格式以便后续分析。
- 对文档中的数学公式，能精准转换为可编辑的 LaTeX 格式。

-
**轻量化部署适配性广：**- 基于仅 1.2B 参数量的模型构建。
- 资源消耗低。

-
**适配多元实用场景：**- 能自动清理页眉、页脚、水印等干扰内容，提升提取内容的纯净度。
- 输出格式丰富，包含 JSON、Markdown 等。


### 5.2 常见问题[](https://docs.mthreads.com#52-常见问题)

| 问题描述 | 可能原因 | 解决方案 |
|---|---|---|
| 依赖安装失败 | 网络问题或 pip 源不可用 | 1. 使用国内镜像源：`pip config set global.index-url https://mirrors.tuna.tsinghua.edu.cn/pypi/web/simple` 。2. 检查网络连接。 |
| NumPy 版本冲突 | NumPy 版本过高（2.x）与 PyTorch 不兼容 | 安装指定版本：`pip install numpy==1.26` |
| Mineru 命令行模式启动过慢或报错 | 网络问题或未添加指定的启动参数 | 1. 检查网络连接。 2. 确认添加参数 `-d musa:0` 和参数 `--source local` |
| Mineru 的 Gradio 和 FastAPI 模式访问对应网址报错 | 端口被占用，环境变量未添加 | 1. 确保在当前命令行配置环境变量。 2. 切换其他端口，或者停掉对应端口服务 |

### 5.3 相关资源[](https://docs.mthreads.com#53-相关资源)

- Mineru 官方文档：
[https://opendatalab.github.io/MinerU/zh/quick_start/](https://opendatalab.github.io/MinerU/zh/quick_start/) - Mineru 官网：
[https://mineru.net/?source=github](https://mineru.net/?source=github) - PDF-Extract-Kit（Mineru 的底层提取算法）：
[https://github.com/opendatalab/PDF-Extract-Kit](https://github.com/opendatalab/PDF-Extract-Kit) - Conda 用户指南：
[https://docs.conda.org.cn/projects/conda/en/stable/user-guide/index.html](https://docs.conda.org.cn/projects/conda/en/stable/user-guide/index.html)