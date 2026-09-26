source: https://docs.mthreads.com/musa-for-vscode/musa-for-vscode-doc-online/user_guide

# 用户手册

## 核心功能[](https://docs.mthreads.com#核心功能)

`.mu`

文件识别[](https://docs.mthreads.com#mu-文件识别)

- 自动识别
`.mu`

为 MUSA C++ 文件 - 显示专属图标与语言模式标识

### 实时错误与告警[](https://docs.mthreads.com#实时错误与告警)

- 基于 MUSA 编译器前端进行增量分析
- 即时高亮语法/语义错误，同步至
**PROBLEMS**面板 - 错误使用红色波浪线，警告使用黄色波浪线，并支持实时反馈和动态清除

### 智能修复（Quick Fix）[](https://docs.mthreads.com#智能修复quick-fix)

- 对缺失头文件、简单拼写错误等问题提供一键修复
- 不支持复杂错误修正或批量修正
**操作方式：**将鼠标悬停在错误位置，点击灯泡图标，选择修复建议并应用

### 代码补全与跳转[](https://docs.mthreads.com#代码补全与跳转)

- 上下文感知补全（含 MUSA Runtime API、内核函数）
- 支持跳转至定义、声明、引用（包括 SDK 头文件）
- ��代码补全支持 C/C++ 和 MUSA 关键字、类型、方法、当前文件符号及成员列表

### 悬停信息[](https://docs.mthreads.com#悬停信息)

- 鼠标悬停显示变量类型、函数返回类型、参数列表、文档注释及 MUSA 特有属性

### 代码格式化[](https://docs.mthreads.com#代码格式化)

- 集成 clang-format，支持文档/选区格式化
**格式化整个文件：**在编辑器中右键点击，选择**Format Document**或**Format Document With****格式化选中代码：**选中代码后右键点击，选择**Format Selection**- 默认遵循 MUSA 官方编码规范

### 关键字高亮[](https://docs.mthreads.com#关键字高亮)

- 支持标准 C/C++ 与 MUSA 扩展关键字（如
`__musa__`

,`musaMalloc`

）

### musify：CUDA → MUSA 转换[](https://docs.mthreads.com#musifycuda--musa-转换)

- 在
`.cu`

文件中右键选择**Convert CUDA to MUSA** - 在当前文件中将 CUDA 关键字和 API 转换为 MUSA 代码，纯 C++ 代码不受影响
- 如果文件已修改但未保存，按提示先保存文件

### 反向 musify：MUSA → CUDA 转换[](https://docs.mthreads.com#反向-musifymusa--cuda-转换)

- 在
`.mu`

文件中右键选择**Convert MUSA to CUDA** - 在当前文件中将 MUSA 关键字和 API 转换为 CUDA 代码，纯 C++ 代码不受影响
- 如果文件已修改但未保存，按提示先保存文件

## MUSACode AI Coding Agent[](https://docs.mthreads.com#musacode-ai-coding-agent)

MUSA for VS Code v1.1.0 集成 MUSACode（`musacode`

）能力，可作为 MUSACode 的 VS Code 插件入口使�用。插件启动时会自动检测当前本地或远程开发环境中的 `musacode`

命令，并在状态栏显示连接状态。

MUSACode 是摩尔线程自主打造的 AI Coding Agent，可通过自然语言命令帮助开发者完成代码生成、调试、重构等任务，并面向 MUSA 算子开发、测试、编译和优化提供专项支持。通过 MUSA for VS Code，你可以在 VS Code 内使用 MUSACode 的 AI Coding Agent 能力，包括对话式开发、文件和代码上下文引用、变更审阅、命令执行确认以及多 Session 管理。

### 连接状态与重连[](https://docs.mthreads.com#连接状态与重连)

- 状态栏显示 MUSACode 当前连接状态
- 点击状态栏入口可查看详细状态
- 连接异常时，可手动刷新或重新连接
- 未检测到 MUSACode 时，可按提示选择稍后安装、查看安装文档或开始安装
- 当 MUSACode 不可用时，
`.mu`

文件识别、语言服务和 musify 功能仍可继续使用

### 侧边栏对话[](https://docs.mthreads.com#侧边栏对话)

- 点击 VS Code 侧边栏中的 MUSA for VS Code 入口
- 在对话面板中输入问题或开发任务
- 生成过程中可点击停止按钮中断输出

对话入口默认显示在 Primary Bar，也可移动到 Secondary Bar。

### Session 与历史记录[](https://docs.mthreads.com#session-与历史记录)

- 支持新建多个 Session，用于隔离不同任务上下文
- 支持切换、重命名和删除 Session
- 对话历史会按 Session 保存，可用于恢复之前的上下文

### 模型与 Agent 选择[](https://docs.mthreads.com#模型与-agent-选择)

- 模型列表来自当前 MUSACode 配置
- 可在对话面板中切换当前模型，切换后对后续对话生效
- 可选择可用 Agent，例如 Build 和 Plan

Build 是默认智能体，适用于编写新功能、修复 Bug、重构代码、运行测试和编译构建等需要完整工具权限的任务。Plan 是只读分析型智能体，适用于理解代码结构、制定方案、分析性能瓶颈和代码审查。

### 配置 MUSACode[](https://docs.mthreads.com#配置-musacode)

可在 VS Code 设置界面编辑 MUSACode 关键配置：

- Model URL
- API Key
- Model list

保存配置后，插件会自动刷新 MUSACode 连接状态。

MUSACode 也支持全局和项目两级配置文件。全局配置位于 `~/.config/musacode/musacode.json`

，项目级配置为工程根目录下的 `.musacode/musacode.json`

，且项目级配置优先级更高。

### 添加文件、目录和代码上下文[](https://docs.mthreads.com#添加文件目录和代码上下文)

**通过 @ 添加文件或目录：**

- 在对话输入框中输入
`@`

- 从文件或目录列表中选择目标路径
- 选中的路径会添加到当前对话上下文

**添加选中代码：**

- 在编辑器中选中代码片段
- 右键选择
**Add to Context** - 代码内容和来源文件会添加到对话上下文

**添加 Terminal 或 Output 内容：**

- 在 VS Code Terminal 或 Output 窗口中选中输出内容
- 右键选择
**Add to Context** - 选中内容会添加到当前对话上下文

Terminal 右键菜单依赖 VS Code 的终端上下文菜单设置。若右键只执行复制或粘贴，请将 `terminal.integrated.rightClickBehavior`

设置为 `default`

后重试。

### Review AI 代码修改[](https://docs.mthreads.com#review-ai-代码修改)

当 MUSACode 生成代码修改时，插件会打开 VS Code Diff 视图：

- 高亮展示修改前后的差异
- 显示变更统计
- MUSACode 修改后会直接写入磁盘
- 支持
**Keep All**保留全部变更 - 支持
**Undo All**恢复 AI 修改前的内容 - 支持逐行或逐片段检查和撤销

AI 代码修改 Diff 建议在 Git 管理的项目目录中使用。受保护路径、非 Git 工作区或缺少可用 Git 状态的场景下，Diff 视图可能无法正常展示。

### 命令执行确认[](https://docs.mthreads.com#命令执行确认)

当 MUSACode 返回需要执行的命令时，插件会先弹出确认对话框并展示命令详情。只有用户确认后，命令才会执行；也可以取消本次操作。

MUSACode 的只读操作（如读取文件、搜索代码、查看目录结构）通常可自动执行；写入或修改文件、执行 Shell 命令、安装依赖等可能产生副作用的操作需要用户确认。

## 高级配置[](https://docs.mthreads.com#高级配置)

整体参考 [Clangd 配置](https://clangd.llvm.org/config)，以下是 MUSA for VS Code 特有的配置：

### 指定 MUSA SDK 路径[](https://docs.mthreads.com#指定-musa-sdk-路径)

可以在 `settings.json`

自定义指向 MUSA SDK 安装目录的设置。插件会从该设置项指定的目录下查找 clangd 可执行文件，并启动其作为语言服务器。

`{`

// 默认值为 /usr/local/musa

"musa.sdkPath": "/custom/path/to/musa"

}



MUSA SDK 需要升级至 5.1.0 或更高版本。

### 与 vscode-clangd 的区别[](https://docs.mthreads.com#与-vscode-clangd-的区别)

- 增加 MUSA 语言支持（
`.mu`

文件） - 通过
`musify`

提供 MUSA/CUDA 代码转换功能 - 优先使用
`musa.sdkPath`

设置解析 clangd - 集成 MUSACode AI Coding Agent，提供对话、上下文引用、代码变更 Review 和命令执行确认能力

## 支持与资源[](https://docs.mthreads.com#支持与资源)

## 常见问题[](https://docs.mthreads.com#常见问题)

### Q：需要单独安装 clangd 语言服务器吗？[](https://docs.mthreads.com#q需要单独安装-clangd-语言服务器吗)

不需要。MUSA for VS Code 已包含 MUSA SDK 5.1.0 或更高版本 提供的 clangd language server。单独安装 clangd 语言服务器可能导致冲突。

### Q：可以在 Windows 上使用 MUSA for VS Code 吗？[](https://docs.mthreads.com#q可以在-windows-上使用-musa-for-vs-code-吗)

可以。Windows 10/11 作为 Host OS 受支持。v1.1.0 新增的 MUSACode AI Coding Agent 能力可在 Windows 本地使用；涉及 MUSA SDK 语言服务、编译、运行和 GPU 调试的工作流建议通过 Remote-SSH 连接到 Linux 机器。

### Q：为什么 Windows 下在 VS Code Terminal 中右键没有出现 `MUSACode`

菜单？[](https://docs.mthreads.com#q为什么-windows-下在-vs-code-terminal-中右键没有出现-musacode-菜单)

这通常不是插件功能异常，而是 VS Code Terminal 的默认右键行为导致的。Windows 下默认可能是复制粘贴模式，因此不会弹出上下文菜单。

请在 `settings.json`

中添加以下配置：

`{`

"terminal.integrated.rightClickBehavior": "default"

}



设置完成后，重新在 Terminal 中右键，确认 `MUSACode`

菜单是否已出现。

### Q：如何生成 compile_commands.json？[](https://docs.mthreads.com#q如何生成-compile_commandsjson)

对于 CMake 项目，使用 `EnableMUSALanguage`

模块。对于其他构建系统，使用 `bear`

工具：`bear -- make`

。

### Q：如果 IntelliSense 不工作怎么办？[](https://docs.mthreads.com#q如果-intellisense-不工作怎么办)

请确保：

- 已安装 MUSA SDK 5.1.0 或更高版本
`settings.json`

中正确配置了`musa.sdkPath`

- 项目根目录存在
`compile_commands.json`


### Q：MUSACode 对话入口没�有出现怎么办？[](https://docs.mthreads.com#qmusacode-对话入口没有出现怎么办)

请确认：

- 当前环境已安装并配置 MUSACode（
`musacode`

） - Model URL、API Key 和 Model list 等配置有效
- 状态栏中的 MUSACode 状态为已连接；如未连接，可手动刷新、重连、查看安装文档或触发安装