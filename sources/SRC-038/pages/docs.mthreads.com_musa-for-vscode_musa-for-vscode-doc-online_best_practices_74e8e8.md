source: https://docs.mthreads.com/musa-for-vscode/musa-for-vscode-doc-online/best_practices

# 不同场景最佳实践

### 场景一：首次安装配置[](https://docs.mthreads.com#场景一首次安装配置)

#### 用户问题[](https://docs.mthreads.com#用户问题)

"我刚安装了 MUSA for VS Code 插件，但打开 .mu 文件后没有高亮和补全，该怎么办？"

#### 解决步骤[](https://docs.mthreads.com#解决步骤)

-
**确认 MUSA SDK 已安装**：# 检查 SDK 版本ls /usr/local/musa# 确认版本 >= 5.1.0 -
**确认插件已启用**：- 打开 Extensions 面板
- 确认 "MUSA Visual Studio Code Edition" 已显示 "Installed"

-
**生成 compile_commands.JSON**：

-
**如果使用 CMake**：cmake_minimum_required(VERSION 3.10)project(my_project LANGUAGES CXX)list(APPEND CMAKE_MODULE_PATH /usr/local/musa/cmake)include(EnableMUSALanguage)enable_language(MUSA)# 使用 Ninja 构建cmake -G Ninja -B build -S .cmake --build build -
**如果使用其他构建系统**：# 使用 bear 抓取编译命令bear -- make

- 重新打开工程目录

### 场景二：本地 Linux 开发[](https://docs.mthreads.com#场景二本地-linux-开发)

#### 用户问题[](https://docs.mthreads.com#用户问题-1)

"我在本地 Linux 机器上安装了 MUSA SDK，想用 VS Code 开发 MUSA 程序，怎么配置？"

#### 解决步骤[](https://docs.mthreads.com#解决步骤-1)

-
**确保前置条件满足**：- VS Code 1.108.0 或更高版本
- MUSA SDK 5.1.0 或更高版本
- 摩尔线程显示驱动

-
**安装插件**（见快速开始） -
**打开工程目录**：code /path/to/your/musa/project -
**验证功能**：`.mu`

文件应有语法高亮- 输入
`musa`

相关 API 应有补全 - 错误应有红色波浪线提示，警告应有黄色波浪线提示


### 场景三：Windows 远程开发[](https://docs.mthreads.com#场景三windows-远程开发)

#### 用户问题[](https://docs.mthreads.com#用户问题-2)

"我用的是 Windows 电脑，但开发环境在远程 Linux 服务器上，该怎么开发 MUSA 程序？"

#### 解决步骤[](https://docs.mthreads.com#解决步骤-2)

-
**在本地 Windows 安装**：- 安装 VS Code

-
**安装 Remote-SSH 扩展**：- 在 Extensions 面板搜索 "Remote - SSH"
- 安装 Microsoft 官方扩展

-
**连接到远程服务器**：- 按
`Ctrl+Shift+P`

- 输入 "Remote-SSH: Connect to Host"
- 输入
`username@remote-server-ip`

- 选择 Linux 作为目标平台

- 按
-
**在远程窗口中**：- 打开工程目录
- 安装 MUSA for VS Code 插件
- 确认 MUSA for VS Code 插件正常工作


GPU 调试目标必须运行于 Linux，Windows 只能作为 Host 通过 Remote-SSH 连接。

### 场景四：Windows Terminal 右键未出现 MUSACode 菜单[](https://docs.mthreads.com#场景四windows-terminal-右键未出现-musacode-菜单)

#### 用户问题[](https://docs.mthreads.com#用户问题-3)

"我在 Windows 的 VS Code Terminal 页面右键，没有出现 MUSACode 菜单，该怎么办？"

#### 原因分析[](https://docs.mthreads.com#原因分析)

VS Code 在不同操作系统中的终端右键默认行为不同。Windows 默认通常为 `copyPaste`

，右键会执行复制或粘贴，而不是弹出上下文菜单，因此不会显示 `MUSACode`

菜单。这不是 MUSA for VS Code 插件本身的功能异常。

#### 解决步骤[](https://docs.mthreads.com#解决步骤-3)

-
**打开设置**：- 按
`Ctrl+,`

- 搜索
`terminal.integrated.rightClickBehavior`


- 按
-
**修改终端右键行为**：- 将
**Terminal > Integrated: Right Click Behavior**设置为`default`


- 将
-
**或者直接修改**：`settings.json`

{"terminal.integrated.rightClickBehavior": "default"} -
**重新在 Terminal 中右键验证**，确认已出现`MUSACode`

菜单

如果团队同时使用 Windows 和 Linux，建议统一将 `terminal.integrated.rightClickBehavior`

配置为 `default`

，减少平台默认行为差异带来的误判。

### 场景五：代码补全和跳转不工作[](https://docs.mthreads.com#场景五代码补全和跳转不工作)

#### 用户问题[](https://docs.mthreads.com#用户问题-4)

"我打开了 .mu 文件，但按 F12 无法跳转到定义，补全也不生效，怎么解决？"

#### 原因分析[](https://docs.mthreads.com#原因分析-1)

插件依赖 `compile_commands.json`

文件来理解编译命令和代码结构。

#### 解决步骤[](https://docs.mthreads.com#解决步骤-4)

-
**确认 compile_commands.json 存在**：# 在项目根目录执行ls -la compile_commands.json -
**如果没有，重新生成**：# 方法一：CMake + Ninjacmake -G Ninja -B build -S .cmake --build build# 方法二：使用 bearbear -- make cleanbear -- make -
**确认 compile_commands.json 位置正确**：- 文件应在项目根目录
- 或在 cmake 编译缓存目录下

-
**检查 VS Code 设置**：- 打开
`Ctrl+,`

→ 搜索 "clangd" - 确认 "Clangd: Arguments" 未包含干扰参数

- 打开

### 场景六：实时错误诊断[](https://docs.mthreads.com#场景六实时错误诊断)

#### 用户问题[](https://docs.mthreads.com#用户问题-5)

"我写的代码有语法错误，但 VS Code 没有显示红色下划线，该怎么启用？"

#### 解决步骤[](https://docs.mthreads.com#解决步骤-5)

-
**确保文件类型正确**：- 文件扩展名应为
`.mu`

- 右下角状态栏应显示 "MUSA"

- 文件扩展名应为
-
**手动触发诊断**：- 保存文件 (
`Ctrl+S`

) - 或按
`Ctrl+Shift+P`

→ "Clangd: Restart Language Server"

- 保存文件 (
-
检查

**PROBLEMS**面板：- 按
`Ctrl+Shift+M`

打开 - 查看是否有错误信息

- 按

### 场景七：使用 Quick Fix 一键修复[](https://docs.mthreads.com#场景七使用-quick-fix-一键修复)

#### 用户问题[](https://docs.mthreads.com#用户问题-6)

"VS Code 提示我缺少头文件，但一个个手动添加太麻烦，有没有办法自动修复？"

#### 解决步骤[](https://docs.mthreads.com#解决步骤-6)

**将鼠标悬停在错误位置****点击灯泡图标，查看修复建议**：- 缺失头文件 → "Include xxx.h"
- 简单拼写错误 → "Rename to xxx"

**选择建议并应用**

Quick Fix 支持简单错误快速修正，不支持复杂错误修正或批量修正。

### 场景八：CUDA 代码迁移到 MUSA[](https://docs.mthreads.com#场景八cuda-代码迁移到-musa)

#### 用户问题[](https://docs.mthreads.com#用户问题-7)

"我有一个 CUDA 项目，想迁移到 MUSA，有工具可以帮助吗？"

#### 解决步骤[](https://docs.mthreads.com#解决步骤-7)

**使用 musify 进行转换**：

-
打开

`.cu`

文件 -
**右键点击**→ 选择**Convert CUDA to MUSA** -
在当前文件中将 CUDA 关键字和 API 转换为 MUSA 代码，纯 C++ 代码不受影响

-
如果文件已修改但未保存，按提示先保存文件

-
打开

`.mu`

文件 -
**右键点击**→ 选择**Convert MUSA to CUDA** -
在当前文件中将 MUSA 关键字和 API 转换为 CUDA 代码，纯 C++ 代码不受影响

-
如果文件已修改但未保存，按提示先保存文件


### 场景九：代码格式化[](https://docs.mthreads.com#场景九代码格式化)

#### 用户问题[](https://docs.mthreads.com#用户问题-8)

"我的代码格式很乱，有没有办法自动格式化？"

#### 解决步骤[](https://docs.mthreads.com#解决步骤-8)

**格式化整个文件**：

- 打开
`.mu`

文件 - 在编辑器中右键点击，选择
**Format Document**或**Format Document With**

**格式化选中部分**：

- 选中代码
- 右键点击选中代码，选择
**Format Selection**

**配置格式化规则**：
在项目根目录创建 `.clang-format`

文件：

`BasedOnStyle: Google`

IndentWidth: 4

ColumnLimit: 100



### 场景十：悬停查看 API 文档[](https://docs.mthreads.com#场景十悬停查看-api-文档)

#### 用户问题[](https://docs.mthreads.com#用户问题-9)

"我不记得某个 MUSA API 的参数，该怎么快速查看？"

#### 解决步骤[](https://docs.mthreads.com#解决步骤-9)

- 将鼠标悬停在 API 名称上
- 查看弹出信息：
- 函数签名
- 参数说明
- 返回值类型
- 简短描述


### 场景十一：自定义 SDK 路径[](https://docs.mthreads.com#场景十一自定义-sdk-路径)

#### 用户问题[](https://docs.mthreads.com#用户问题-10)

"我的 MUSA SDK 不在默认路径 `/usr/local/musa`

，该怎么配置？"

#### 解决步骤[](https://docs.mthreads.com#解决步骤-10)

-
**打开设置**：- 按
`Ctrl+,`

- 点击右上角打开 JSON 设置

- 按
-
**添加配置**：{"musa.sdkPath": "/custom/path/to/your/musa"} -
**重启 VS Code**，让设置生效

MUSA SDK 需要升级至 5.1.0 或更高版本。

### 场景十二：MUSACode 对话不可用[](https://docs.mthreads.com#场景十二musacode-对话不可用)

#### 用户问题[](https://docs.mthreads.com#用户问题-11)

"我安装了 v1.1.0 插件，但看不到 MUSACode 对话入口，或者状态栏显示未连接，怎么处理？"

#### 原因分析[](https://docs.mthreads.com#原因分析-2)

MUSACode AI Coding Agent 功能依赖当前本地或远程环境中的 MUSACode 以及有效的模型服务配置。若 MUSACode 不存在、模型配置无效或连接失败，插件会保留基础语言服务和 musify 功能，但不会进入完整 AI Coding Agent 工作流。

#### 解决步骤[](https://docs.mthreads.com#解决步骤-11)

-
**确认 MUSACode 已安装并可用**：- 在当前 VS Code 窗口对应的本地或远程终端中检查 MUSACode
- 可执行
`which musacode`

验证命令是否存在 - Remote-SSH 场景下，应检查远程 Linux 环境

-
**检查模型配置**：- 打开 VS Code 设置
- 检查 Model URL、API Key、Model list 等 MUSACode 配置
- 保存后等待插件刷新连接状态

-
**查看状态栏连接状态**：- 点击 MUSACode 状态栏入口查看详情
- 如状态异常，执行手动刷新或重连
- 如未安装，可按提示选择稍后安装、查看安装文档或开始安装

-
**回退验证基础功能**：- 打开
`.mu`

文件检查语法高亮 - 验证补全、跳转、musify 等基础功能是否正常

- 打开

### 场景十三：让 AI 修改代码并检查变更[](https://docs.mthreads.com#场景十三让-ai-修改代码并检查变更)

#### 用户问题[](https://docs.mthreads.com#用户问题-12)

"我希望 MUSACode 帮我修改代码，但需要先看清楚它改了什么，并在需要时撤销。"

#### 解决步骤[](https://docs.mthreads.com#解决步骤-12)

- 在侧边栏对话中描述要修改的目标
- 通过
`@`

添加相关文件或目录，或在编辑器中选中代码后右键选择**Add to Context** - 等待 MUSACode 生成修改
- 在 VS Code Diff 视图中检查变更内容
- 如需保留修改，可继续编辑或关闭 Diff 视图；如需恢复 AI 修改前的内容，可选择
**Undo All**，或逐行/逐片段撤销

AI 代码修改 Diff 建议在 Git 管理的项目目录中使用。受保护路径、非 Git 工作区或缺少可用 Git 状态的场景下，Diff 视图可能无法正常展示。

涉及构建、安装、删除、覆盖文件等命令时，插件会在执行前展示确认对话框。请确认命令内容和工作目录后再执行。

## 核心功能一览[](https://docs.mthreads.com#核心功能一览)

| 功能 | 说明 | 快捷键 |
|---|---|---|
`.mu` 文件识别 | 自动识别 MUSA 扩展名 | - |
| 语法高亮 | MUSA 关键字和语法 | - |
| 代码补全 | 上下文感知补全 | `Ctrl+Space` |
| 跳转定义 | 跳转到函数/变量定义 | `F12` |
| 查找引用 | 查找所有引用 | `Shift+F12` |
| 错误诊断 | 实时语法/语义错误 | - |
| Quick Fix | 一键修复建议 | 悬停错误并点击灯泡图标 |
| 代码格式化 | 自动格式化代码 | 右键菜单 |
| 悬停信息 | 显示类型和文档 | 鼠标悬停 |
| musify 转换 | CUDA ��↔ MUSA 互转 | 右键菜单 |
| MUSACode 对话 | 与 AI Coding Agent 进行工程上下文对话 | 侧边栏入口 |
| 添加上下文 | 添加文件、代码片段、Terminal 或 Output 内容到对话 | `@` 或右键菜单 |
| 代码变更 Review | 在 Diff 视图检查 AI 代码修改并按需撤销 | Keep / Undo |
| 命令执行确认 | 执行 MUSACode 返回命令前二次确认 | 确认对话框 |

## 常见问题速查表[](https://docs.mthreads.com#常见问题速查表)

| 问题 | 快速答案 |
|---|---|
| 插件安装失败 | MUSA for VS Code v1.1.0 需要 VS Code 1.108.0 或更高版本，低于该版本无法安装 |
| 没有代码补全 | 确认 compile_commands.json 存在 |
| 无法跳转定义 | 同上，或按 `Ctrl+Shift+P` → "Restart Language Server" |
| 远程连接失败 | 确认 SSH 密钥已配置，远程 MUSA SDK 已安装 |
Windows Terminal 右键没有 `MUSACode` 菜单 | 将 `terminal.integrated.rightClickBehavior` 设为 `default` |
| 格式化不生效 | 检查是否有 `.clang-format` 冲突 |
| musify 转换失败 | 检查原始 CUDA 代码语法是否正确 |
| SDK 版本过低 | 升级 MUSA SDK 到 5.1.0 或更高版本 |
| MUSACode 未连接 | 使用 `which musacode` 检查是否安装，确认 Model URL、API Key 和模型列表配置 |
| AI 修改需要撤销 | MUSACode 修改后会直接写入磁盘，可在 Diff 视图中选择 Undo All 恢复AI修改前的内容 |
| Diff 视图未正常展示 | 确认当前工程位于 Git 管理的项目目录中，避免在受保护路径或非 Git 工作区中执行 |
| 命令没有执行 | 确认命令执行弹窗中已选择允许 |