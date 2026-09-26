source: https://docs.mthreads.com/musacode/musacode-doc-online/MUSACODE简介

# MUSACODE 简介

## 什么是 MUSACODE[](https://docs.mthreads.com#什么是-musacode)

MUSACODE 是摩尔线程自主打造的 AI Coding Agent，旨在帮助开发者在终端或桌面端完成代码生成、调试、重构等任务。MUSACODE 不仅具备通用编程能力，helps you DIY your software，更致力于成为最好的 MUSA 编程工具，为算子开发、测试、编译和优化提供全流程支持。

## 核心功能[](https://docs.mthreads.com#核心功能)

MUSACODE 提供以下核心功能：

### 多模型与多提供商支持[](https://docs.mthreads.com#多模型与多提供商支持)

- 支持连接多家 LLM 提供商，包括 OpenAI（GPT）、Anthropic（Claude）、Google（Gemini）、AWS Bedrock、Groq、Azure、OpenRouter 等国际厂商，深度求索（DeepSeek）、阿里云（千问系列）、智谱 AI（GLM）、MiniMax、月之暗面（Kimi）等国内主流厂商，以及摩尔线程的 Coding Plan。
- 可自由选择最适合当前任务或最具成本效益的模型，也支持本地模型（如 Ollama、LM Studio）。

### 开发工具集成[](https://docs.mthreads.com#开发工具集成)

**LSP（语言服务器协议）支持**：为 LLM 自动加载合适的语言服务器，提供智能提示与语义分析。

### 灵活的交互方式[](https://docs.mthreads.com#灵活的交互方式)

**终端 TUI（文本用户界面）**：基于 OpenTUI 构建的交互式终端 UI，提供接近 IDE 的体验，支持 Vim 风格编辑。**桌面应用**：提供带有图形界面的原生桌面应用程序，支持 Windows 和 Linux，在更友好的环境中提供同样强大的 AI 编程能力。**多会话并行**：可在同一项目中并行启动多个代理会话。

### 隐私与数据安全[](https://docs.mthreads.com#隐私与数据安全)

**隐私优先设计**：MUSACODE 不存储用户的任何代码或上下文数据，所有处理均在本地或用户指定的模型服务上进行，适合对隐私敏感的环境。

### 子 Agent 与工具能力[](https://docs.mthreads.com#子-agent-与工具能力)

- 支持调用专门化的子 Agent，如
`@general`

（用于复杂搜索和多步骤任务）和`@search`

（快速探索代码库）。 - 具备文件操作、命令执行、代码智能分析、Web 获取等工具能力。