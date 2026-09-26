source: https://docs.mthreads.com/playbook/playbook-doc-online/openclaw-skills

# 龙虾活了！让 OpenClaw 能说能听更能干的妙招

## 变更记录[](https://docs.mthreads.com#变更记录)

| 版本 | 日期 | 变更内容 |
|---|---|---|
| 1.0.0 | 2026-03-19 | 初始版本 |
| 1.0.1 | 2026-04-01 | 将 ASR 模型由 Whisper 更换为效果更好的 FunASR，将 TTS 模型由 Piper TTS 更换为效果更好的 Kokoro。新增 12 个推荐 Skill 的安装步骤及说明。 |

## 项目简介[](https://docs.mthreads.com#项目简介)

本文档以**小明**与**OpenClaw 智能助手**的真实交互故事为主线，带你走进一个沉浸式的技能部署之旅。你将亲身经历：

- 如何通过自然语言对话触发 Skills 的自动安装
- 各种 Skills 的实际应用场景
- 从零构建本地 AI 工具链的�完整体验

**主角介绍**：

**小明**：一位热爱探索 AI 技术的用户，喜欢用语音与智能助手进行自然交互**OpenClaw 智能助手**：部署在 MTT AIBOOK 上的 AI 助手，能够根据用户需求自动安装和配置 Skills

**难度**：中级，适合有编程基础的开发者体验

本文或视频为第三方开源 AI 智能体 OpenClaw 的部署与使用演示教程。根据国家工信部及互联网应急中心预警，该软件存在权限滥用、数据泄露、系统被控等已知风险。请您在充分了解技术原理、自行评估风险后自行决定是否使用。如因个人部署操作产生任何影响，摩尔线程不为此承担相关责任。

## 前置条件[](https://docs.mthreads.com#前置条件)

### 硬件要求[](https://docs.mthreads.com#硬件要求)

| 组件 | 要求 |
|---|---|
| 设备 | MTT AIBOOK 笔记本，型号 A141 |
| 存储空间 | >= 5GB |
| 网络 | ��网络环境通畅，可访问互联网 |

### 软件要求[](https://docs.mthreads.com#软件要求)

| 组件 | 要求 |
|---|---|
| 操作系统 | MTT AIBOOK 操作系统 AIOS（1.3.4） |
| Python | 3.10 |
| Node.js | 22.22+ |
| OpenClaw | 最新版本 |
| 飞书 | 已配置消息通道 |

### OpenClaw 初始配置[](https://docs.mthreads.com#openclaw-初始配置)

在开始本文档的 Skills 部署之前，需要先完成 OpenClaw 的基础配置：

-
**运行 Onboarding 配置**：openclaw onboard -
**安装飞书机器人**：# 安��装成功后，会自动弹出二维码，使用飞书扫描创建机器人npx -y @larksuite/openclaw-lark-tools install更多配置信息，请参阅

[飞书机器人参考文档](https://www.feishu.cn/content/article/7613711414611463386)。 -
**（可选）切换默认模型**：本文 Onboarding 过程中选择 Kimi-k2.5 作为默认模型。如需切换模型，使用以下命令：

openclaw config

## 第一章：语音转录能力 --- FunASR[](https://docs.mthreads.com#第一章语音转录能力-----funasr)

### 1.1 功能介绍[](https://docs.mthreads.com#11-功能介绍)

[ FunASR](https://github.com/modelscope/FunASR) 由阿��里达摩院开源的语音识别模型，支持高精度的语音转录。

| 特性 | 说明 |
|---|---|
| 功能 | 将语音转换为文字 |
| 语言支持 | 多语言，中文支持效果极佳 |
| 模型类型 | Paraformer / SenseVoice |
| 运行方式 | 本地运行，无需联网 |

### 1.2 安装部署[](https://docs.mthreads.com#12-安装部署)

**💬 小明**：「安装 FunASR 作为语音转录功能应用程序。」

智能助手检测到需求，自动开始安装：

**🤖 智能助手**：「FunASR 已经安装好了！现在你可以发语音给我，我能识别了。」

**安装过程**：

- 检测系统环境和 Python 版本
- 安装 FunASR 及相关依赖包
- 下载中文语音识别模型

### 1.3 功能验证[](https://docs.mthreads.com#13-功能验证)

小明发送了一条语音消息测试：

**🤖 智能助手**：「语音转录成功！识别到的内容是："你好，请帮我记录今天的待办事项"」

FunASR 语音转录能力已就绪。

## 第二章：语音合成能力 --- Kokoro[](https://docs.mthreads.com#第二章语音合成能力-----kokoro)

### 2.1 功能介绍[](https://docs.mthreads.com#21-功能介绍)

[ Kokoro](https://github.com/hexgrad/Kokoro) 是一个轻量级、高质量的本地语音合成引擎。

| 特性 | 说明 |
|---|---|
| 功能 | 将文字转换为语音 |
| 语言支持 | 多语言，中文效果优秀 |
| 模型 | zf_xiaobei（年轻中文女声） |
| 运行方式 | 本地运行，无需联网 |

### 2.2 安装部署[](https://docs.mthreads.com#22-安装部署)

**💬 小明**：「部署 Kokoro 作为语音合成应用程序。」

智能助手开始安装：

**🤖 智能助手**：「Kokoro 部署完成！」

**部署状态**：

- Kokoro 已安装
- 中文语音模型已下载（zf_xiaobei）
- 语音合成功能正常

**模型信息**：

- 语言：中文（zh_CN）
- 声音：zf_xiaobei（年轻中文女声）
- 质量：标准（平衡速度和质量）

要试试合成一段语音吗？

### 2.3 功能验证[](https://docs.mthreads.com#23-功能验证)

**💬 小明**：「发送生成的音频文件给我，说"养龙虾真好"。」

**🤖 智能助手**：「语音已生成！但由于飞书 API 限制，无法直接发送音频文件。」

### 2.4 飞书语音消息闭环[](https://docs.mthreads.com#24-飞书语音消息闭环)

**💬 小明**：「你想办法帮我搞定。」

**🤖 智能助手**：「搞定！二维码已发送，扫描即可下载音频文件！」

**音频信息**：

- 文本："养龙虾真好"
- 格式：MP3

**💬 小明**：「让飞书 API 支持语音发送。」

**🤖 智能助手**：「搞定！飞书语音消息发送工具已配置完成！」

**功能**：

- 自动将音频转换为 opus 格式（飞书要求）
- 上传音频文件到飞书
- 发送语音消息

语音消息应该已经发送到你的飞书了！检查一下收到了吗？

小明收到了第一条语音消息，**语音交互闭环完成**。

## 第三章：图片文字识别能力 --- PaddleOCR[](https://docs.mthreads.com#第三章图片文字识别能力-----paddleocr)

### 3.1 功能介绍[](https://docs.mthreads.com#31-功能介绍)

[ PaddleOCR](https://github.com/PaddlePaddle/PaddleOCR) 是百度开源的 OCR 工具，支持中英文文字识别。

| 特性 | 说明 |
|---|---|
| 功能 | 识别图片中的文字 |
| 语言支持 | 80+ 语言，中英文效果优秀 |
| 能力 | 文字检测、文字识别、表格识别 |
| 运行方式 | 本地运行，无需联网 |

### 3.2 安装部署[](https://docs.mthreads.com#32-安装部署)

**💬 小明**：「安装 PaddleOCR 作为图片识别功能应用程序。」

智能助手开始安装：

**🤖 智能助手**：「PaddleOCR 需要装一下。我来装...搞定！PaddleOCR 已安装，版本 3.4.0，可以识别图片中的文字。现在你可以发图片给我，我能识别了。」

**安装过程**：

- 安装 PaddleOCR 及依赖包
- 下载中文识别模型
- 配置 protobuf 版本兼容性

### 3.3 功能验证[](https://docs.mthreads.com#33-功能验证)

小明发送了一张关于 **Agentic AI 组织变革**的信息图：

**🤖 智能助手**：「图片识别成功！这是一张关于 Agentic AI（智能体 AI）组织变革的信息图。」

**主要内容**：

- 标题：AGENTIC AI: Leaders Guide to Org Chart Evolution
- 副标题：From Silos to Networks: The Next Paradigm for the AI Era
- 对比传统组织与新型智能体组织
- 5 大变革支柱：商业模式、运营模式、治理、人才、技术与数据

需要我详细解释某个部分吗？

PaddleOCR 完美识别了复杂的英文图表信息。

## 第四章：视觉检测能力 --- YOLO NPU[](https://docs.mthreads.com#第四章视觉检测能力-----yolo-npu)

### 4.1 功能介绍[](https://docs.mthreads.com#41-功能介绍)

[ YOLO NPU](https://gitee.com/MooreThreads-AI-SOC/M1000_Developer_Document/tree/master/user_cases/UC_Samples_OpenClaw/skills/yolo-npu) 使用 NPU 加速的 YOLOv8 模型进行目标检测。

| 特性 | 说明 |
|---|---|
| 功能 | 实时物体检测 |
| 加速方式 | NPU 硬件加速 |
| 检测类别 | COCO 80 类（人、车、动物、家具等） |
| 输入方式 | 图片文件 / 摄像头实时拍摄 |

### 4.2 安装部署[](https://docs.mthreads.com#42-安装部署)

**💬 小明**：「帮我安装 YOLO NPU Skill，从 [https://gitee.com/MooreThreads-AI-SOC/M1000_Developer_Document/tree/master/user_cases/UC_Samples_OpenClaw/skills/yolo-npu](https://gitee.com/MooreThreads-AI-SOC/M1000_Developer_Document/tree/master/user_cases/UC_Samples_OpenClaw/skills/yolo-npu) 安装。」

**🤖 智能助手**：「正在从 Gitee 安装 YOLO NPU Skill...安装完成！YOLO NPU Skill 已就绪，支持摄像头拍照和图片检测。要试试吗？」

**安装过程**：

- 从 Gitee 下载 yolo-npu Skill
- 检测 mtnn 驱动版本（需要 1.4+）
- 创建 conda 环境 npu（python3.10）
- 安装 opencv-python、numpy 和 mtnn_api
- 下载 YOLOv8m 模型（.mtnn 格式）

### 4.3 实战：识别画面中有几个人[](https://docs.mthreads.com#43-实战识别画面中有几个人)

**💬 小明**：「帮我打开电脑的摄像头，拍张照片，看一下这照片有几个人。请用语音回答我。」

智能助手执行了完整的流程：

- 调用摄像头拍照
- 使用 YOLO NPU 进行人物检测
- 使用视觉模型分析画面细节
- 使用 Kokoro 合成语音回复
- 发送语音消息

**🤖 智能助手**（语音）：「搞定！照片里有 2 个人，两位都是男性。左边的人面向右侧，右边的人面向左侧。」

### 4.4 实时检测：看看桌上有什么[��](https://docs.mthreads.com#44-实时检测看看桌上有什么)

**💬 小明**：「使用笔记本自带 USB 摄像头，抓拍一张图片，识别后的文字和图像结果都发送给我。」

**🤖 智能助手**：「搞定！」

**识别结果**：

- 检测到 2 个物体
- 1 个人（置信度 72%）
- 1 把椅子（置信度 70%）

图片和语音都已发送！

## 第五章：记忆更新[](https://docs.mthreads.com#第五章记忆更新)

### 5.1 记住用户偏好[](https://docs.mthreads.com#51-记住用户偏好)

**💬 小明**：「请记住，FunASR 作为语音转录功能应用程序；用 Kokoro 来做语音合成的功能。我后面飞书交互，都是用语音。」

**🤖 智能助手**：「明白了！已更新 USER.md！」

**语音功能已部署完成**：

**FunASR**--- 语音转录（识别你说的话）**Kokoro**--- 语音合成（把文字转成语音）

**飞书交互模式**：

- 你发语音 → 我用 FunASR 识别 → 我处理 → 用 Kokoro 合成语音回复

### 5.2 添加图片识别能力[](https://docs.mthreads.com#52-添加图片识别能力)

**💬 小明**：「默认用本地的 PaddleOCR 作为�图片识别功能应用程序。」

**🤖 智能助手**：「已更新！PaddleOCR 已加入工具列表。」

**当前本地 AI 工具栈**：

**FunASR**--- 语音转文字**Kokoro**--- 文字转语音**PaddleOCR**--- 图片文字识别**YOLO NPU**--- 物体检测

全部本地运行，无需联网，隐私安全。

## 第六章：完整的 Skills 工具链[](https://docs.mthreads.com#第六章完整的-skills-工具链)

### 6.1 工具链总览[](https://docs.mthreads.com#61-工具链总览)

经过一系列探索，小明的智能助手拥有了完整的本地 AI 能力：

| 能力 | 工具 | 用途 | 章节 |
|---|---|---|---|
| 🎤 语音转录 | FunASR | 识别语音消息 | 第一章 |
| 🔊 语音合成 | Kokoro | 生成语音回复 | 第二章 |
| 👁️ 文字识别 | PaddleOCR | 识别图片中的文字 | 第三章 |
| 🎯 物体检测 | YOLO NPU | 实时目标检测 | 第四章 |

**全部本地运行，无需联网，隐私安全。**

### 6.2 Skills 目录结构[](https://docs.mthreads.com#62-skills-目录结构)

`~/.openclaw/workspace/skills/`

└── yolo-npu/

├── SKILL.md

├── _meta.json

├── install.sh

├── yolo_npu.py

├── yolo_live.py

└── yolov8m.mtnn



### 6.3 语音交互工作流[](https://docs.mthreads.com#63-语音交互工作流)

`┌───────────────────�──────────────────────────────────────────┐`

│ 小明发送语音消息（飞书） │

└─────────────────────────────────────────────────────────────┘

│

▼

┌─────────────────────────────────────────────────────────────┐

│ OpenClaw 接收音频文件（audio 消息类型） │

└─────────────────────────────────────────────────────────────┘

│

▼

┌─────────────────────────────────────────────────────────────┐

│ FunASR 语音转录 │

└─────────────────────────────────────────────────────────────┘

│

▼

┌─────────────────────────────────────────────────────────────┐

│ LLM 处理文本，生成回复 │

└─────────────────────────────────────────────────────────────┘

│

▼

┌─────────────────────────────────────────────────────────────┐

│ Kokoro 合成语音 │

└─────────────────────────────────────────────────────────────┘

│

▼

┌─────────────────────────────────────────────────────────────┐

│ 转换为 opus 格式，发送语音消息（飞书） │

└─────────────────────────────────────────────────────────────┘



### 6.4 摄像头检测工作流[](https://docs.mthreads.com#64-摄像头检测工作流)

`小明请求 "看看桌上有什么"`

│

▼

自动安装/调用 YOLO NPU Skill

│

▼

拍照 + 检测物体

│

├─→ 返回 JSON 结果

│

└─→ 保存标注图片

│

▼

发送图片 + 语音说明



## 第七章：ClawHub Skills 扩展包应用[](https://docs.mthreads.com#第七章clawhub-skills-扩展包应用)

### 7.1 扩展包简介[](https://docs.mthreads.com#71-扩展包简介)

在掌握了基础的本地音视频与视觉能力后，为了让 OpenClaw 智能助手应对更复杂的日常办公与开发任务，你可以通过 [ClawHub](https://clawhub.ai/)（OpenClaw 官方技能社区）安装更多进阶 Skills。

根据小明的进阶需求，本次引入 12 个涵盖智能体控制、网络搜索、办公软件处理和实用工具的核心 Skills。

自 AIOS 1.3.4 版本起，MTT AIBOOK 预装的 OpenClaw 已同步预装本章提及的 12 个 Skills。

### 7.2 扩展 Skills 功能一览表[](https://docs.mthreads.com#72-扩展-skills-功能一览表)

以下是 MTT AIBOOK 预装的 12 个热门 Skills 列表及其功能说明：

### 7.3 组合应用实战[](https://docs.mthreads.com#73-组合应用实战)

安装完成后，小明决定将这些扩展技能进行联动，测试助手的工作流处理能力。

**💬 小明**：「先用 weather 查一下今天上海的天气；然后用 Tavily Search 搜索一下"2026 年 AI 智能体行业发展趋势"；最后用 Summarize 把搜索结果总结成 3 个要点，并用 PPTX 帮我做成一份简单的 3 页幻灯片文件发给我。」

智能助手执行了完整的多步工作流：

- 调用 weather 获取上海天气
- 调用 Tavily Search 联网检索最新的智能体行业报告
- 调用 Summarize 对检索到的数百页网页内容进行高度浓缩
- 调用 PPTX 将浓缩的文字按照幻灯片格式（标题页、摘要页、趋势页）生成 .pptx 文件

**🤖 智能助手**：「搞定！上海今天晴转多云，气温 18-24°C。

关于 AI 智能体趋势的 PPT 已经为你生成完毕，文件已发送，请查收！你还需要我用 XLSX 帮你整理一份相关的市场数据表格吗？」

通过这 12 个 ClawHub 技能的加入，OpenClaw 智能助手正式从一个"能看能听"的工具，进化为了能够主动搜索、处理文档、自我进化的全能型 AI 办公助理。

### 7.4 Skills 安装方法[](https://docs.mthreads.com#74-skills-安装方法)

ClawHub 生态的 Skills 安装非常简便，只需将对应技能的 URL 喂给智能助手即可。

以安装 Tavily Search 和 PPTX 为例（这两个 Skills 已预装，此处仅作安装指引演示）：

**💬 小明**：「帮我安装网页搜索和办公处理相关的 Skills，比如 Tavily Search 和 PPTX，链接分别是 [https://clawhub.ai/matthew77/liang-tavily-search](https://clawhub.ai/matthew77/liang-tavily-search) 和 [https://clawhub.ai/ivangdavila/powerpoint-pptx。」](https://clawhub.ai/ivangdavila/powerpoint-pptx%E3%80%82%E3%80%8D)

智能助手开始依次拉取配置：

**🤖 智能助手**：「收到！正在从 ClawHub 下载安装...

✅ Tavily Search Skill 安装就绪！

✅ PPTX Skill 安装就绪！

以后你可以让我帮你搜集网上资料，并直接生成幻灯片了！」

## 附录[](https://docs.mthreads.com#附录)

### A. 相关资源[](https://docs.mthreads.com#a-相关资源)

| 资源 | 链接 |
|---|---|
| 摩尔线程开发者中心 |
|

[https://openclaw.ai](https://openclaw.ai)[https://github.com/openclaw](https://github.com/openclaw)[https://github.com/PaddlePaddle/PaddleOCR](https://github.com/PaddlePaddle/PaddleOCR)[https://github.com/hexgrad/Kokoro](https://github.com/hexgrad/Kokoro)[https://github.com/modelscope/FunASR](https://github.com/modelscope/FunASR)### B. 常见问题排查[](https://docs.mthreads.com#b-常见问题排查)

| 问题 | 可能原因 | 解决方案 |
|---|---|---|
| FunASR 加载失败 | MUSA 冲突 | 助手会自动设置环境变量 |
| PaddleOCR protobuf 错误 | 版本不兼容 | 助手会自动升级 protobuf |
| YOLO NPU 无法启动 | mtnn 驱动问题 | 运行 Skill 安装脚本检查驱动版本 |
| 飞书语音发送失败 | 格式不支持 | 助手会自动转换为 opus 格式 |
| ClawHub Skill 下载失败 | 网络连接超时或受限 | 检查本地网络，助手会自动尝试使用备用节点重新拉取 |
| Tavily Search 拒绝访问 | 未配置 API Key | 助手会提示前往官网获取免费 Key，并自动写入环境变量 |
| Agent Browser 无法控制网页 | 缺少浏览器内核 | 助手会自动触发 playwright install 等指令补齐环境 |
| PPTX / XLSX 文件生成报错 | 缺少文档处理依赖 | 助手会自动安装 python-pptx 或 openpyxl 依赖包 |

### C. Skills 一览表[](https://docs.mthreads.com#c-skills-一览表)

| Skill | 版本 | 功能 | 触发场景 |
|---|---|---|---|
| FunASR | - | 语音转文字 | 用户发送语音消息 |
| Kokoro | - | 文字转语音 | 用户需要语音回复 |
| PaddleOCR | 3.4.0 | 图片文字识别 | 用户发送图片 |
| YOLO NPU | 1.0.0 | 物体检测 | 用户请求拍照识别 |
| Self-Improving Agent | - | 自我优化 | 用户要求优化智能体自身代码或流程 |
| Proactive Agent | - | 主动执行与发问 | 开启主动模式或处理模糊任务 |
| Skill-Creator | - | 自动编写新 Skill | 用户提出全新的技能需求 |
| Find Skills | - | 检索生态技能 | 用户在 ClawHub 中寻找扩展功能 |
| Agent Browser | - | 浏览器自动化控制 | 用户需要智能体代替操作网页交互 |
| Tavily Search | - | AI 网络搜索 | 用户查询最新网络资讯或行业数据 |
| Summarize | - | 长文本摘要 | 用户发送长文档或网页链接求总结 |
| Web Scraper | - | 网页数据抓取 | 用户需要提取特定网页的结构化内容 |
| PPTX | - | 幻灯片处理 | 用户要求生成或修改 PPT 演示文稿 |
| XLSX | - | 表格数据处理 | 用户要求整理或分析 Excel 表格 |
| Skill Vetter | - | 技能安全审查 | 安装不明来源 Skill 前的自动代码评估 |
| weather | - | 实时天气查询 | 用户询问某城市或地区的实时天气 |

## 结语[](https://docs.mthreads.com#结语)

通过小明与 OpenClaw 智能助手的沉浸式互动故事，我们共同见证了 MTT AIBOOK 用户如何一步步构建起属于自己的全能 AI 工作站。OpenClaw Skills 展现出的核心价值不仅在于技术本身，更在于其赋能用户的方式：

-
**交互零门槛（自然语言触发）**：用户无需学习复杂的命令行或配置文件，只需像小明一样通过日常对话表达需求，Skills 即可完成从环境检测、依赖下载到模型配置的闭环。 -
**隐私与效能的平衡（本地优先 + 混合生态）**：音视频转录（FunASR）、语音合成（Kokoro）及视觉检测（YOLO NPU/PaddleOCR）等核心能力完全驻留在本地运行，确保了隐私安全与极低延迟；而通过 ClawHub 接入的 Tavily Search、Agent Browser 等云端技能，则为助手插上了实时资讯与联网办公的翅膀。 -
**能力的无限叠加（模块化组合）**：Skills 之间并非孤立存在。从小明最初的"语音转文字"，到后来的"视觉识别"，再到最后的"联网搜索生成 PPT"，多个 Skills 的协同工作让智能体能够胜任从简单指令到复杂业务流的跨越。 -
**智能体的自我生长（持续进化）**：通过 USER.md 对用户偏好的记忆，以及 Self-Improving Agent 和 Skill-Creator 的加入，助手不再是一个死板的程序，而是一个能够理解用户意图并不断学习新技能的"数字伙伴"。

### 故事回顾[](https://docs.mthreads.com#故事回顾)

| 小明的需求阶段 | 触发的核心 Skill / 机制 | 最终达成的效果 |
|---|---|---|
| 基础感知：让助手能听会说 | FunASR, Kokoro | 助手具备了高精度的听觉与自然的中文表达能力 |
| 多模态增强：让助手能看会认 | PaddleOCR, YOLO NPU | 助手能够识别复杂图表、拍照片数人数、实时监测环境 |
| 闭环交互：让反馈更及时 | 飞书语音工具，USER.md | 实现飞书语音消息闭环，并记住小明的交互偏好 |
| 办公提效：让助手协助工作 | Tavily Search, Summarize, PPTX | 助手能够全网搜集行业资讯、总结要点并自动输出演示文稿 |
| 技能扩展：探索无限可能 | ClawHub 12 核心技能包 | 赋予助手控制浏览器、处理 Excel、查询天气及安全审查的能力 |
| 自我进化：让助手更懂开发 | Skill-Creator, Self-Improving | 小明只需通过对话即可指导助手编写并安装全新的 Skill |

随着 OpenClaw 社区的不断壮大，更多强大的 Skills 将持续涌现。

现在，快拿起你的 MTT AIBOOK，开启 AI 智能体的探索之旅吧！

祝你的 OpenClaw 探索之旅愉快！