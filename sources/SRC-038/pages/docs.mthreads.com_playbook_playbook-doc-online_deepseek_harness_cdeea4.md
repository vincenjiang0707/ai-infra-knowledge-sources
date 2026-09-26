source: https://docs.mthreads.com/playbook/playbook-doc-online/deepseek_harness

# 【初级】在 MTT AIBOOK 上快速体验 DeepSeek Harness

## 更新日志[](https://docs.mthreads.com#更新日志)

| 版本 | 日期 | 变更说明 |
|---|---|---|
| 1.0.0 | 2026-08-27 | 首次发布 |

## 1. 教程简介[](https://docs.mthreads.com#1-教程简介)

本文介绍如何在 MTT AIBOOK 上启动 DeepSeek Harness 本地 Web 服务，完成首次 API Key 配置，并在工作区中提交第一个任务。

DeepSeek Harness 采用插件式架构，模型、工具、技能、会话、沙箱、存储、循环、调度和界面等能力由插件组合而成。本文聚焦首次启动和基础操作，不展开插件开发。

DeepSeek Harness 当前为开发者预览版，界面、模型列表和插件接口可能随版本变化。

## 2. 前置条件[](https://docs.mthreads.com#2-前置条件)

开始前，请确认以下条件：

### 硬件条件[](https://docs.mthreads.com#硬件条件)

| 项目 | 要求 |
|---|---|
| 设备 | MTT AIBOOK A141 |
| 处理器 | 12 个 ARM64 大核，最高主频约 2.65 GHz |
| 内存 | 32 GB |
| 存储 | 1 TB NVMe SSD |

### 软件要求[](https://docs.mthreads.com#软件要求)

| 软件或环境 | 要求 |
|---|---|
| 操作系统 | MTT AIOS 1.5.0 |
| 系统架构 | ARM64（`aarch64` ） |
| Node.js | 22.22.1（ARM64） |
| npm / npx | 10.9.4 |
| DeepSeek Harness | `@deepseek-ai/dsh 0.1.0-rc.6` |
| 浏览器 | Chromium 147.0.7727.55 |

可在终端执行以下命令确认 Node.js、npm、npx 和系统架构：

`uname -m`

node --version

npm --version

npx --version



### 其他准备[](https://docs.mthreads.com#其他准备)

- 准备可用的 DeepSeek 官方 API Key。
- 确保设备可以访问 DeepSeek 服务。
- 确保本地
`3080`

端口未被占用。

关于 DeepSeek API 的接口说明，请参阅 [DeepSeek API 文档](https://api-docs.deepseek.com/)。

API Key 属于敏感凭据，请勿将其发送给他人或上传到公开仓库。关于 API Key 的保存位置、有效期和费用规则，请以 DeepSeek 官方说明为准。

## 3. 启动本地服务[](https://docs.mthreads.com#3-启动本地服务)

-
在 MTT AIBOOK 上打开终端。

-
执行以下命令启动 DeepSeek Harness 本地服务：

npx --yes @deepseek-ai/dsh web -
等待终端输出本地访问地址：

dsh web: http://127.0.0.1:3080 -
保持运行服务的终端窗口打开，在 MTT AIBOOK 的 Chromium 浏览器中访问

`http://127.0.0.1:3080`

。

## 4. 完成首次配置[](https://docs.mthreads.com#4-完成首次配置)

### 4.1 配置 API Key[](https://docs.mthreads.com#41-配置-api-key)

首次打开页面时，会显示“**添加一个 API Key 开始使用**”对话框：

- 将 DeepSeek API Key 粘贴到“
**API 密钥**”输入框。 - 点击“
**保存并�继续**”。

### 4.2 阅读内测声明[](https://docs.mthreads.com#42-阅读内测声明)

保存 API Key 后，页面会显示 DeepSeek Harness 的内测声明。阅读声明后，点击“**继续**”进入主界面。

## 5. 创建第一个工作区会话[](https://docs.mthreads.com#5-创建第一个工作区会话)

进入主界面后，可以看到以下区域：

**工作区**：左侧显示**dsh 工作区**和“**新会话**”入口。**输入框**：中间用于描述要构建的内容。**模式切换**：底部可切换工作模式，本文示例为**Workspace Write**。**模型选择**：右下角用于选择模型，本文示例为**DeepSeek-V4-Flash High**。

创建会话并提交任务：

- 点击“
**新会话**”。 - 在输入框中输入任务需求，例如：
`做一个介绍 DeepSeek Harness 的网页`

。 - 点击
**发送**按钮提交任务。 - 如果任务需要向工作区写入文件，请保持
**Workspace Write**模式。

提交后，Harness 会根据当前工作区和所选模型开始处理任务。模型列表和处理结果可能因版本或配置不同而变化。

## 6. 后续访问[](https://docs.mthreads.com#6-后续访问)

以后使用时，请先确认 DeepSeek Harness 服务仍在运行，再访问以下地址：

`http://127.0.0.1:3080`



如果服务已经退出，需要重新在终端执行启动命令：

`npx --yes @deepseek-ai/dsh web`



## 7. 注意事项[](https://docs.mthreads.com#7-注意事项)

- DeepSeek Harness 当前为开发者预览版，核心插件和基础接口仍在持续演进。
`127.0.0.1:3080`

是本机地址，本文只介绍在 MTT AIBOOK 本机浏览器中访问。- 使用
**Workspace Write**前，请确认当前工作区和写入范围。 - 如果
`npx`

报告`Lock compromised`

，请优先按照 DeepSeek Harness 项目提供的源码安装说明操作，或清理 npm 缓存后重试。