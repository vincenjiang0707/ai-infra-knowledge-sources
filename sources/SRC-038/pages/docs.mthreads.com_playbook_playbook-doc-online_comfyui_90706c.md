source: https://docs.mthreads.com/playbook/playbook-doc-online/comfyui

# 【初级】在 MTT AIBOOK 本地运行 ComfyUI

## 更新日志[](https://docs.mthreads.com#更新日志)

| 版本 | 日期 | 变更描述 |
|---|---|---|
| 1.0.0 | 2026-01-29 | 初始版本，包含 ComfyUI 在 AI 算力本 MTT AIBOOK（版本 A141）上的部署、配置及使用指南。 |
| 1.0.1 | 2026-08-10 | 更新 ComfyUI 版本，替换原有安装流程、Python 版本要求、模型目录名及 SDXL-Lightning 工作流。 |

## 1. 目标与范围[](https://docs.mthreads.com#1-目标与范围)

本教程指导开发者在 AI 算力本 MTT AIBOOK 上部署和使用 ComfyUI，通过�可视化节点工作流实现 AI 图像生成，无需编程即可构建专属的图像生成流程。

**难度：初级，适合新手入门体验**

## 2. 前置条件[](https://docs.mthreads.com#2-前置条件)

在开始本教程之前，请确保您已满足以下所有条件：

**硬件:**- AI 算力本 MTT AIBOOK，版本 A141。
- 至少预留 16 GB 可用磁盘空间，用于保存压缩包、解压后的文件、模型和项目虚拟环境。

**软件:**- MTT AIBOOK 操作系统 AIOS (1.3.1-B15) 及以上版本。
- 设备已配置管理员权限（可使用 sudo 命令）。
- 网络环境通畅，可访问互联网（需下载 ComfyUI 及模型文件）。
- 需要安装 Python 3.10；包内离线 wheel 不支持 Python 3.11/3.12。
- 已安装 wget 或 curl 下载工具（用于获取工具包）。


## 3. 环境部署[](https://docs.mthreads.com#3-环境部署)

本章节描述如何获取 ComfyUI 并完成环境配置。

### 3.1 下载 ComfyUI[](https://docs.mthreads.com#31-下载-comfyui)

-
使用 wget 命令下载

**MTT AIBOOK 版 ComfyUI**工具包。wget https://apollo-appstore-pre.tos-cn-beijing.volces.com/appstore/release/comfyui-musa/releases/ComfyUI-0.3.26-torchmusa-2.9.0-m1000-ready-20260804.tar.zst工具包将下载到当前目录。

-
解压工具包到目标目录。

tar --zstd -xf ComfyUI-0.3.26-torchmusa-2.9.0-m1000-ready-20260804.tar.zstcd ComfyUI # 进入解压后的目录提示请记录 ComfyUI 的安装路径，后续操作将在此目录下进行。


### 3.2 安装依赖组件[](https://docs.mthreads.com#32-安装依赖组件)

-
定位到 ComfyUI 项目目录。

cd /path/to/ComfyUI # 替换为您的实际下载路径 -
首次安装并启动 ComfyUI。该脚本会自动创建项目内的 Python 3.10 虚拟环境。

./start-m1000.sh首次运行会从

`vendor-wheels`

离线安装 PyTorch 2.9.0、TorchMUSA 2.9.0 和其他依赖，验证 M1000 后启动服务；后续仍可执行`./start-m1000.sh`

启动。

## 4. 最佳实践[](https://docs.mthreads.com#4-最佳实践)

本章节指导您使用 ComfyUI 的核心场景及常用操作。

### 场景 1：启动 ComfyUI 服务[](https://docs.mthreads.com#场景-1启动-comfyui-服务)

通过命令行启动 ComfyUI Web 服务，提供可视化节点工作流界面：

-
定位到 ComfyUI 项目目录。

cd /path/to/ComfyUI # 替换为您的实际路径 -
使用一键脚本启动 ComfyUI 服务（MUSA GPU 模式）。

./start-m1000.sh**脚本默认配置说明：**`COMFYUI_LISTEN_ADDRESS`

默认为`0.0.0.0`

，监听所有网络接口。`COMFYUI_PORT`

默认为`8188`

。`COMFYUI_MUSA_DEVICE`

默认为`0`

，即第一块 MUSA 设备。- 脚本自动启用 GPU-only、FP16 和 FP16 UNet 参数。

-
验证服务启动。当看到类似以下输出时，说明 ComfyUI 服务已启动：

Starting serverTo see the GUI go to: http://0.0.0.0:8188日志中的

`http://0.0.0.0:8188`

表示监听地址，不是浏览器访问地址。 -
访问 ComfyUI 界面。

- 在本地设备：打开浏览器，访问
[http://127.0.0.1:8188](http://127.0.0.1:8188) - 在远程设备：打开浏览器，访问
`http://设备实际IP:8188`

（需确保网络可达）

- 在本地设备：打开浏览器，访问
-
停止服务。在终端中按

**Ctrl+C**终止运行。

### 场景 2：使用工作流模板生成图像[](https://docs.mthreads.com#场景-2使用工作流模板生成图像)

通过 ComfyUI 提供的工作流模板，快速体验文本到图像的生成功能：

#### 步骤 1： 从工作流模板加载示例工作流[](https://docs.mthreads.com#步骤-1-从工作流模板加载示例工作流)

-
在 ComfyUI 界面中，点击顶部菜单栏的

**“工作流”**（Workflow）。 -
点击

**“浏览模板”**（Browse Templates）。 -
选择工作流模板。

在模板列表中，选择第一个工作流

**“图像生成”**（Image Generation）来加载它。 -
下载缺失的模型（如需要）。

如果弹出

**“缺少模型”**界面，点击**“下载”**按钮自动下载所需模型。注意所有模型都存储在

`<your ComfyUI installation>/ComfyUI/models/`

目录中，包含以下子文件夹：`checkpoints`

: 主模型文件`embeddings`

: 嵌入文件`vae`

: VAE 模型`loras`

: LoRA 模型`upscale_models`

: 放大模型


#### 步骤 2：从生成的图像中加载工作流[](https://docs.mthreads.com#步骤-2从生成的图像中加载工作流)

ComfyUI 生成的图像包含元数据，其中包括完整的工作流信息：

-
将 ComfyUI 生成的图像拖放到界面中。或者使用菜单

**Workflows -> Open**打开图像文件。 -
工作流将自动加载。系统会自动解析图像中的工作流信息并还原节点配置。该图片为 ComfyUI 提供的示例图片。


#### 步骤 3：生成第一张 AI 图片[](https://docs.mthreads.com#步骤-3生成第一张-ai-图片)

-
配置模型加载器。

在

**Checkpoint 加载器**（Checkpoint Loader）中，确保选中`v1-5-pruned-emaonly-fp16.safetensors`

模型。 -
点击

**“运行”**（Queue Prompt）按钮。 -
等待生成完成。

生成过程可能需要几秒到几分钟，取决于图像分辨率和模型复杂度。

-
查看生成的图像。

生成的图像将显示在

**“保存图像”**（Save Image）节点中，并自动保存到本地。 -
多次生成尝试。

如果对结果不满意，可以多次点击运行。每次运行时，KSampler 会根据 seed 参数使用不同的随机种子，因此每次生成都会产生不同的结果。


#### 步骤 4：生成自定义图片[](https://docs.mthreads.com#步骤-4生成自定义图片)

通过修改提示词来生成自定义内容：

-
理解正面提示词和负面提示词的条件输入。

**正面提示词**（Positive Prompt）：连接到 KSampler 的正面条件，引导模型生成目标内容。**负面提示词**（Negative Prompt）：连接到负面条件，引导模型避开不想要的内容。

-
修改 CLIP 文本编码器中的文本。

在

**CLIP 文本编码器**（CLIP Text Encode）节点中，修改正面提示词和负面提示词。-
正面提示词示�例：

anime style, 1girl with long pink hair, cherry blossom background, studio ghibli aesthetic, soft lighting, intricate detailsmasterpiece, best quality, 4k -
负面提示词示例：

low quality, blurry, deformed hands, extra fingers

-
-
点击运行生成图像。


**技术说明：正面/负面提示词与文本编码器**

正面提示词和负面提示词会分别编码为两组条件，用于引导采样器生成目标内容并抑制不希望出现的内容。

两组条件输入不等同于两套独立文本编码器；实际使用的编码器数量由具体模型架构决定。

例如，SDXL 内部包含多个文本编码器，但相关组合过程由模型加载器和文本编码节点统一封装。

### 场景 3：部署 Hugging Face 模型生成图片[](https://docs.mthreads.com#场景-3部署-hugging-face-模型生成图片)

ComfyUI 本身不内置模型，但允许您自由加载各类 Stable Diffusion 模型。Hugging Face 是目前主流的模型托管平台之一。

#### 步骤 1：选择并下载模型[](https://docs.mthreads.com#步骤-1选择并下载模型)

以 `sdxl_lightning_4step`

为例，展示自定义加载模型的方式：

-
下载模型文件。

wget https://huggingface.co/ByteDance/SDXL-Lightning/resolve/main/sdxl_lightning_4step.safetensors或者访问

[Hugging Face 模型页面](https://huggingface.co/ByteDance/SDXL-Lightning)选择合适的模型。 -
保存模型到指定目录。

mv sdxl_lightning_4step.safetensors ComfyUI/models/checkpoints/模型文件应放置在

`ComfyUI/models/checkpoints/`

目录下。 -
刷新或重启 ComfyUI。

重启服务后，新模型将出现在 Checkpoint 加载器的下拉列表中。


#### 步骤 2：导入工作流[](https://docs.mthreads.com#步骤-2导入工作流)

-
下载官方工作流文件。

wget https://huggingface.co/ByteDance/SDXL-Lightning/resolve/main/comfyui/sdxl_lightning_workflow_lora.json -
在 ComfyUI 界面中导入工作流。

- 点击菜单
**Workflows -> Load**。 - 选择下载的
`sdxl_lightning_workflow_lora.json`

文件。

- 点击菜单
-
配置模型加载器。在 Checkpoint 加载器中选择

`sdxl_lightning_4step.safetensors`

。

#### 步骤 3： 输入提示词并生成图片[](https://docs.mthreads.com#步骤-3-输入提示词并生成图片)

-
在文本编码器节点中输入提示词。

- 正面提示词：描述您想要生成的内容。
- 负面提示词：描述您不想要的内容。

-
点击

**“运行”**按钮。 -
等待生成完成并查看结果。生成的图像将自动保存到本地，可在界面中查看。


### 进阶操作：ComfyUI 工作流设计技巧[](https://docs.mthreads.com#进阶操作comfyui-工作流设计技巧)

-
**理解核心节点**。- 模型加载器（Checkpoint Loader）：加载主模型。
- 文本编码器（CLIP Text Encode）：将文本转换为模型可理解的向量。
- K 采样器（KSampler）：执行去噪迭代过程。
- VAE 解码器（VAE Decode）：将潜在空间转换为图像。
- 保存图像（Save Image）：保存生成的图像。

-
**理解数据流向**。从 Prompt → 编码 → 去噪 → 解码 → 输出的完整流程。

-
**使用多个 Prompt 输入**。可以创建多个文本编码器节点，实现更复杂的提示词组合。


### 常用操作命令[](https://docs.mthreads.com#常用操作命令)

| 操作 | 命令 |
|---|---|
| 下载 ComfyUI | `wget https://apollo-appstore-pre.tos-cn-beijing.volces.com/appstore/release/comfyui-musa/releases/ComfyUI-0.3.26-torchmusa-2.9.0-m1000-ready-20260804.tar.zst` |
| 解压工具包 | `tar --zstd -xf ComfyUI-0.3.26-torchmusa-2.9.0-m1000-ready-20260804.tar.zst` |
| 进入项目目录 | `cd ComfyUI` |
| 首次安装并启动 | `./start-m1000.sh` |
| 后续启动 ComfyUI 服务 | `./start-m1000.sh` |
| 下载模型到 checkpoints | `wget [模型 URL] -P models/checkpoints/` |
| 停止服务 | 终端中按 Ctrl+C |

## 5. 附录[](https://docs.mthreads.com#5-附录)

### 5.1 核心特点[](https://docs.mthreads.com#51-核心特点)

ComfyUI 在 MTT AIBOOK 上的部署具有以下核心优势：

**本地化部署**：所有模型与流程均在 MTT AIBOOK 本地运行，保障创作数据隐私与处理速度。**节点化创作**：通过可视化节点编排生成步骤，清晰可控，支持复杂流程设计与逻辑调试。**灵活可扩展**：支持社区插件与自定义节点，可持续拓展您的创�作工具箱。**零代码上手**：无需编程基础，通过连接节点即可实现专业级 AI 图像生成流程。

### 5.2 技术背景：为什么 ComfyUI 是 MTT AIBOOK 生态能力的展现？[](https://docs.mthreads.com#52-技术背景为什么-comfyui-是-mtt-aibook-生态能力的展现)

上游 ComfyUI 可通过不同 PyTorch 后端适配多类硬件，但普通 CUDA 安装方式不能直接用于 MTT AIBOOK 的 M1000 GPU。M1000 需要匹配的 MUSA 驱动、MUSA SDK、TorchMUSA 以及经过适配的 ComfyUI 发布包。

MTT AIBOOK 搭载摩尔线程 M1000 GPU。本发布包通过 PyTorch 2.9.0、TorchMUSA 2.9.0 和针对 MUSA 后端的 ComfyUI 适配，实现模型加载、采样、VAE 解码和图像保存等完整流程。

这不仅仅是“跑通一个 UI 工具”，更代表了 MTT AIBOOK 生态适配能力的体现：

**支持国产架构的 AI 部署能力****跨平台、异构 GPU 的兼容适配能力****对复杂项目（如 ComfyUI）底层逻辑的理解与重构能力**

MTT AIBOOK 的软硬协同能力，完美展现。

### 5.3 ComfyUI 进阶建议[](https://docs.mthreads.com#53-comfyui-进阶建议)

#### 1. 完整学习 ComfyUI 的核心节点[](https://docs.mthreads.com#1-完整学习-comfyui-的��核心节点)

学习文生图、图生图、区域控制等常用的核心节点，理解每个节点的功能与参数含义。

#### 2. 精通工作流设计：从模板“使用者”变成“构建者”[](https://docs.mthreads.com#2-精通工作流设计从模板使用者变成构建者)

**尝试从零开始创建工作流**：- 拖出模型加载器、文本编码器、UNet、采样器、保存节点，理解每个组件作用。
- 理解数据流向：从 Prompt → 编码 → 去噪 → 解码 → 输出。
- 学会使用多个 Prompt 输入、多分支图结构。


#### 3. 学会使用 ControlNet：精准控制图像结构[](https://docs.mthreads.com#3-学会使用-controlnet精准控制图像结构)

- 下载 ControlNet 模型（如 Canny、Pose、Depth 等 .pt 文件）。
- 在工作流中加入 ControlNetLoader 与 ControlNetApply 节点。
- 使用图像 + 文本联合生成，实现线稿上色、姿态复现、图转图创作。

#### 4. 玩转 LoRA 微调模型：创造您的专属风格[](https://docs.mthreads.com#4-玩转-lora-微调模型创造您的专属风格)

- 下载 .safetensors 格式 LoRA 模型。
- 拖出 Load LoRA 节点，设置路径与权重。
- LoRA 可用于：角色还原、人设风格统一、训练您自己的模型。

#### 5. 加入社区扩展生态[](https://docs.mthreads.com#5-加入社区扩展生态)

- 安装社区插件（如 ComfyUI Manager、NodeSuite 等）。
- 获取更多专业节点（如 Prompt 树状控制、遮罩处理、自动标签生成等）。
- 跟进 Discord / GitHub / Hugging Face 的最新社区流派与范例。

### 5.4 常见问题[](https://docs.mthreads.com#54-常见问题)

问题描述 | 可能原因 | 解决方案 |
|---|---|---|
服务启动失败或报错 | 依赖未正确安装或 Python 版本不兼容。 | 1. 检查 Python 3.10：`python3.10 --version` 。2. 重新执行一键脚本： `./start-m1000.sh` 。3. 检查错误日志定位具体问题。 |
浏览器无法访问 ComfyUI 界面 | 防火墙限制或 `IP` /端口错误。 | 1. 检查服务是否启动：`ps aux | grep main.py` 。2. 确认访问地址正确：http://[device_ip]:8188 。 3. 检查防火墙设置。 |
模型加载失败 | 模型文件路径错误或文件损坏。 | 1. 确认模型文件在 `models/checkpoints/` 目录下。2. 检查文件完整性。 3. 确认模型格式正确。 |
生成图像时出现 OOM（内存不足） | GPU 内存不足或图像分辨率过大。 | 1. 降低图像分辨率。 2. 使用量化模型。 3. 减小批处理大小。 |
工作流模板无法加载 | 模板文件格式错误或版本不兼容。 | 1. 确认模板文件为有效的 `JSON` 格式。2. 检查 ComfyUI 版本是否支持该模板。 3. 尝试从官方示例重新下载模板。 |
提示词效果不明显 | 提示词编写不当或模型选择不合适。 | 1. 参考优秀提示词示例。 2. 调整提示词权重。 3. 尝试不同的模型。 |

### 5.5 相关资源[](https://docs.mthreads.com#55-相关资源)

- ComfyUI 官方 GitHub：
[https://github.com/comfyanonymous/ComfyUI](https://github.com/comfyanonymous/ComfyUI) - Hugging Face 模型库：
[https://huggingface.co/](https://huggingface.co/) - Stable Diffusion 官方文档：
[https://stability.ai/](https://stability.ai/)