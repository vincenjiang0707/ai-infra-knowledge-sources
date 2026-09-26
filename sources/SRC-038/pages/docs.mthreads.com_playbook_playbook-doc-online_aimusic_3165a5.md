source: https://docs.mthreads.com/playbook/playbook-doc-online/aimusic

# 【中级】AI 音乐生成器，一键创作情感旋律

## 更新日志[](https://docs.mthreads.com#更新日志)

| 版本 | 日期 | 变更描述 |
|---|---|---|
| 1.0.0 | 2026-01-30 | 初始版本，包含在 AI 算力本 MTT AIBOOK （型号 A141）上的 AI 音乐生成器的完整代码和开发使用指南。 |

## 1. 项目简介[](https://docs.mthreads.com#1-项目简介)

本教程旨在指导开发者构建一个基于情感的 AI 音乐生成器，通过选择情感状态（快乐、悲伤、兴奋、平静），让 AI 自动生成符合该情感特征的专属音乐旋律。

**项目简介：** 心情低落时想听悲伤的曲调，兴奋时渴望激昂的节�奏？现在，只需轻点选择情感，AI 就能为您打造专属音乐！项目借助 Python 强大的音乐处理能力，融合数学音频合成技术，开发出"智能音乐创作助手"。无论您是否具备音乐基础，只要选定"快乐""悲伤""兴奋""平静"等情感状态，它就能精准理解您的心境，从音符选择、节奏编排到音调设计，一站式完成音乐创作。

**难度：中级，适合有编程基础的开发者体验**

## 2. 前置条件[](https://docs.mthreads.com#2-前置条件)

在开始本教程之前，请确保您已满足以下所有条件：

**硬件要求**：AI 算力本 MTT AIBOOK，型号 A141**音频设备**：音频输出设备（扬声器或耳机，用于播放生成的音乐）**操作系统**：MTT AIBOOK 操作系统 AIOS（1.3.1-B15）及以上版本**Python 版本**：已安装 Python 3.10 或更高版本（`python --version`

验证）**包管理工具**：已安装 pip 包管理工具（`pip --version`

验证）**代码编辑器**：已安装代码编辑器（推荐 VS Code/Cursor）**编程基础**：具备 Python 编程基础知识（熟悉基本语法和面向对象编程）**可选知识**：了解 Web 开发基本概念（可选，教程中会详细说明）

## 3. 环境部署[](https://docs.mthreads.com#3-环境部署)

本章节描述如何创建项目目录、获取代码并安装必要的依赖组件。

### 3.1 检查 Python 环境[](https://docs.mthreads.com#31-检查-python-环境)

-
打开终端（Linux Terminal）。

-
检查 Python 版本。

执行以下命令：

python --version提示确保 Python 版本在 3.10 或以上。如果版本不符合要求，请先升级 Python�。MTT AIBOOK 已预装了 Python 3.10 的开发环境。


### 3.2 创建项目目录[](https://docs.mthreads.com#32-创建项目目录)

-
创建项目目录。

mkdir music_agentcd music_agent项目目录将用于存放所有代码文件。

-
打开 VS Code。

code .或在 VS Code 中通过

**File -> Open Folder**打开`music_agent`

目录。

### 3.3 获取项目代码[](https://docs.mthreads.com#33-获取项目代码)

您可以通过以下两种方式获取项目代码：

#### 方式一：直接下载完整项目[](https://docs.mthreads.com#方式一直接下载完整项目)

-
克隆项目仓库。

git clone https://gitee.com/mthreadsacademy/project100.git**注意：**请将示例地址替换为实际的项目仓库地址。 -
进入项目目录。

cd project100/music_agent

#### 方式二：使用 AI 辅助生成代码[](https://docs.mthreads.com#方式二使用-ai-辅助生成代码)

-
使用 AI 提示词生成代码。 您可以在 ChatGPT、Claude 或其他 AI 编程助手中使用以下提示词：

-
**基础版提示词：**现在我希望你能在这个文件里面构建一个 agent，可以根据我提供的不同情感生成音乐。要求：1. 支持四种情感：快乐、悲伤、兴奋、平静2. 使用 Python 实现，包含 Flask 网页界面3. 生成 WAV 格式音频文件，可在浏览器中直接播放4. 使用数学方法合成音频，不依赖外部音源5. 界面要现代化，用户体验友好请创建完整的项目结构，包括：- 音乐生成核心逻辑- Flask 后端服务- HTML 前端界面- 依赖管理文件 -
**进阶版提示词：**请帮我创建一个基于情感的 AI 音乐生成器项目，具体要求如下：技术栈：- 后端：Python + Flask- 前端：HTML + CSS + JavaScript- 音频处理：NumPy + 数学合成功能需求：1. 情感音乐生成：- 快乐：C 大调，120 BPM，明亮音域- 悲伤：A 小调，75 BPM，低沉音域- 兴奋：G 大调，140 BPM，高音域快节奏- 平静：F 大调，85 BPM，舒缓节奏2. 音频合成技术：- 使用正弦波生成音调- 音符频率计算：440 * (2^(semitones/12))- 添加音频包络避免爆音- 输出 44.1kHz 采样率的 WAV 文件3. Web 界面设计：- 响应式布局，支持移动端- 四个情感按钮，渐变色设计- 实时加载状态提示- 内置音频播放器4. 项目结构：- app.py：Flask 主应用- music_emotion_agent.py：音乐生成核心- templates/index.html：前端页面- requirements.txt：依赖管理- static/music/：音频文件存储请提供完整的代码实现和详细注释。

-
-
手动创建项目结构。 如果使用 AI 生成代码，请按照以下结构创建文件：

music_agent/├── app.py # Flask 主应用├── music_emotion_agent.py # 音乐生成核心逻辑├── requirements.txt # 项目依赖├── templates/│ └── index.html # 前端界面└── static/└── music/ # 生成的音乐文件存储目录

### 3.4 安装项目依赖[](https://docs.mthreads.com#34-安装项目依赖)

-
在 VS Code 中打开终端。

点击右下角选择 Python 环境（推荐选择 base 环境）

在右上角打开终端（

**Terminal -> New Terminal**）。 -
安装 Python 依赖包。

pip install -r requirements.txt -
如果遇到安装问题，可使用国内镜像源。

pip install -i https://pypi.tuna.tsinghua.edu.cn/simple -r requirements.txt -
验证安装是否成功。

python -c "import flask, numpy; print('依赖安装成功！')"

若输出"依赖安装成功！"，说明依赖已正确安装。

## 4. 最佳实践[](https://docs.mthreads.com#4-最佳实践)

本章节指导您启动音乐生成服务并进行情感音乐创作。

### 场景1: 启动音乐生成服务[](https://docs.mthreads.com#场景1-启动音乐生成服务)

通过 Flask 启动 Web 服务，提供音乐生成界面：

-
启动 Flask 应用。

python app.py -
验证服务启动。

当看到类似以下输出时，说明服务已启动：

* Running on http://127.0.0.1:5000* Debug mode: on -
打开浏览器访问。

在本地设备：打开浏览器，访问

`http://localhost:5000`

-
停止服务。

在终端中按

`Ctrl+C`

终止运行。

### 场景2: 一键生成情感音乐[](https://docs.mthreads.com#场景2-一键生成情感音乐)

通过 Web 界面选择情感状态，生成专属音乐：

-
选择当前情感状态。 在 Web 界面中，您可以看到四个情感按钮：

**😊 快乐**：欢快明亮的旋律**😢 悲伤**：深沉忧郁的音调**🎉 兴奋**：激昂动感的节拍**😌 平静**：舒缓宁静的和声

-
点击对应按钮。 系统会自动分析情感特征，选择合适的音乐参数。

-
等待 AI 创作。 界面会显示"正在创作您的专属音乐，请稍候…"的加载提示。

-
享受专属音乐。 生成完成后会自动播放，您也可以手动控制播放、暂停和音量。


### 场景3: 技术原理解析[](https://docs.mthreads.com#场景3-技术原理解析)

了解音乐生成的核心技术原理。

#### 音乐参数设计[](https://docs.mthreads.com#音乐参数设计)

不同情感对应的音乐参数如下：

| 情感 | 音阶 | BPM | 音域 | 特点 |
|---|---|---|---|---|
快乐 | C 大调 | 120 | C4-E5 | 明亮欢快的旋律 |
悲伤 | A 小调 | 75 | A3-C5 | 深沉忧郁的音调 |
兴奋 | G 大调 | 140 | G4-B5 | 激昂动感的节拍 |
平静 | F 大调 | 85 | F4-F5 | 舒缓宁静的和声 |

#### 音频合成技术[](https://docs.mthreads.com#音频合成技术)

-
频率计算公式

# 频率计算公式frequency = 440.0 * (2 ** (semitones / 12.0))基于标准音 A4（440 Hz），通过半音数计算目标音符的频率。

-
正弦波生成

# 正弦波生成arr[i] = np.sin(2 * np.pi * frequency * i / sample_rate)使用 NumPy 生成正弦波信号，采样率通常为 44.1 kHz。


#### 节奏模式设计[](https://docs.mthreads.com#节奏模式设计)

不同情感对应的节奏模式：

| 情感 | 节奏模式 | 特点 |
|---|---|---|
快乐 | [1.0, 0.5, 0.5, 1.0] | 轻快跳跃 |
悲伤 | [2.0, 1.0, 1.0, 2.0] | 缓慢深沉 |
兴奋 | [0.25, 0.25, 0.5, 0.25, 0.25, 0.5] | 密集激烈 |
平静 | [2.0, 1.0, 1.0, 2.0] | 舒缓流畅 |

### 场景4: 探索更多可能性[](https://docs.mthreads.com#场景4-探索更多可能性)

基于现有技术原理，您可以尝试以下扩展功能：

-
**调整音乐长度**修改

`length`

参数生成更长的音乐：# 在 music_emotion_agent.py 中修改length = 10 # 默认值，可调整为 20、30 等 -
**添加新情感**在

`emotion_params`

中定义新的情感类型：emotion_params = {"快乐": {...},"悲伤": {...},"兴奋": {...},"平静": {...},"神秘": { # 新增情感"scale": "D_minor","bpm": 90,"range": "D4-F5"}} -
**和声支持**添加多声部，创造更丰富的音乐层次：

# 在主旋律基础上添加和声harmony = generate_harmony(melody, emotion)audio = mix_audio(melody, harmony) -
**移动端适配**优化界面，支持手机端使用：

- 使用响应式 CSS 设计
- 优化触摸交互体验
- 适配不同屏幕尺寸

-
**音乐导出**添加 MP3 格式导出功能：

# 使用 pydub 库转换格式from pydub import AudioSegmentaudio = AudioSegment.from_wav("output.wav")audio.export("output.mp3", format="mp3") -
**AI 作词**结合大语言模型，为旋律配上歌词：

# 调用 LLM API 生成歌词lyrics = llm.generate_lyrics(emotion, melody_info)

### 常用操作命令[](https://docs.mthreads.com#常用操作命令)

| 操作 | 命令 |
|---|---|
| 检查 Python 版本 | `python --version` |
| 创建项目目录 | `mkdir music_agent && cd music_agent` |
| 安装依赖 | `pip install -r requirements.txt` |
| 使用国内镜像安装 | `pip install -i https://pypi.tuna.tsinghua.edu.cn/simple -r requirements.txt` |
| 启动 Flask 服务 | `python app.py` |
| 验证依赖安装 | `python -c "import flask, numpy; print('依赖安装成功！')"` |
| 停止服务 | 终端中按 `Ctrl+C` |

## 5. 附录[](https://docs.mthreads.com#5-附录)

### 5.1 项目亮点[](https://docs.mthreads.com#51-项目亮点)

-
**AI + 音乐理论**：基于音乐理论与情感心理学，为每种情感量身定制专属音阶、节奏和音域，一键生成情感旋律。 -
**纯数学音频合成**：采用正弦波合成技术，无需依赖外部音频库或音源文件，直接产出高质量音频。 -
**现代化 Web 交互**：界面采用美观的渐变设计，适配所有现代浏览器，点击按钮即可实时生成并播放音乐。 -
**全场景情感覆盖**：四大情感模式精准匹配心境：快乐模式使用 C 大调，奏响明亮欢快的旋律；悲伤模式使用 A 小调，演绎深沉忧郁的音调；兴奋模式使用 G 大调，迸发激昂动感的节拍；平静模式使用 F 大调，流淌舒缓宁静的和声。

### 5.2 小知识：什么是情感音乐？[](https://docs.mthreads.com#52-小知识什么是情感音乐)

情感音乐是基于音乐心理学原理，通过特定的音阶、节奏、音域和力度来表达和诱发特定情感的音乐形式。研究表明，大调音阶通常让人感到明亮和快乐，而小调音阶则容易引发忧郁和深沉的情感。节奏的快慢、音域的高低、音符的时值分布都会影响听者的情感体验。

在这个项目中，我们将这些音乐理论转化为算法，让 AI 能够根据指定的情感类型，自动选择合适的音乐参数，生成符合该情感特征的旋律。

### 5.3 最终效果展示[](https://docs.mthreads.com#53-最终效果展示)

#### 界面效果[](https://docs.mthreads.com#界面效果)

-
**现代化渐变背景设计**：美观的视觉体验。 -
**四个情感按钮**：清晰的视觉区分，直观的操作界面。 -
**实时加载状态提示**：友好的用户体验反馈。 -
**内置音频播放器**：支持播放、暂停、音量控制等功能。

#### 音乐效果[](https://docs.mthreads.com#音乐效果)

-
**快乐音乐**：明亮的 C 大调，轻快的节奏，让人心情愉悦。 -
**悲伤音乐**：深沉的 A 小调，缓慢的节拍，触动内心情感。 -
**兴奋音乐**：高亢的 G 大调，密集的节奏，激发活力。 -
**平静音乐**：温和的 F 大调，舒缓的旋律，带来宁静。

### 5.4 常见问题[](https://docs.mthreads.com#54-常见问题)

| 问题描述 | 可能原因 | 解决方案 |
|---|---|---|
依赖安装失败 | 网络问题或 pip 源不可用 | 1. 使用国内镜像源：`pip install -i https://pypi.tuna.tsinghua.edu.cn/simple -r requirements.txt` ；2. 检查网络连接。 |
Flask 服务启动失败 | 端口被占用或代码错误 | 1. 检查端口占用：`lsof -i :5000` （Linux）；2. 修改端口：在 app.py 中修改 `app.run(port=5001)` 。 |
浏览器无法访问 | 防火墙限制或 IP/端口错误 | 1. 检查服务是否启动：查看终端输出；2. 确认访问地址正确：`http://localhost:5000` ；3. 检查防火墙设置。 |
生成的音乐没有声音 | 音频文件生成失败或播放器问题 | 1. 检查 `static/music/` 目录是否存在；2. 查看浏览器控制台错误信息；3. 确认音频文件格式为 WAV。 |
音乐生成速度慢 | 计算资源不足或代码效率问题 | 1. 减少音乐长度参数；2. 优化音频生成算法；3. 使用更高效的 NumPy 操作。 |
AI 生成代码不符合需求 | 提示词不够详细或 AI 理解偏差 | 1. 使用进阶版提示词；2. 分步骤生成代码；3. 根据实际需��求手动调整代码。 |

### 5.5 相关资源[](https://docs.mthreads.com#55-相关资源)

**Python 官方文档**：[https://docs.python.org/3/](https://docs.python.org/3/)（学习 Python 基础语法）

**Flask 官方文档**：[https://flask.palletsprojects.com/](https://flask.palletsprojects.com/)（了解 Flask Web 框架）

**NumPy 官方文档**：[https://numpy.org/doc/](https://numpy.org/doc/)（学习数组处理和音频合成）

**音乐理论入门**：了解音阶、调式、节奏等基础概念

**情感计算研究**：了解情感与音乐的关系

### 5.6 学习路径建议[](https://docs.mthreads.com#56-学习路径建议)

通过完成本项目，您将深度体验以下实训内容：

-
**Python 音频处理与数学合成技术**：掌握使用 NumPy 进行音频信号处理 -
**Flask Web 应用开发实践**：学会构建简单的 Web 服务 -
**前端界面设计与交互优化**：理解现代 Web 界面设计原则 -
**音乐理论在编程中的创新应用**：将音乐知识转化为算法 -
**情感计算与人工智能的融合实践**：理解情感与技术的结合 -
**AI 辅助编程的实用技巧**：学会使用 AI 工具提高开发效率

立即开启您的 AI 音乐创作之旅，让情感在旋律中自由流淌！