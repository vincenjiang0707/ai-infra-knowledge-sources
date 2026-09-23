source: https://docs.mthreads.com/musa-for-vscode/musa-for-vscode-doc-online/introduction

# 产品介绍

## 什么是 MUSA for VS Code？[](https://docs.mthreads.com#什么是-musa-for-vs-code)

**MUSA for VS Code** 是由摩尔线程推出的面向 MUSA 异构计算平台的专业开发工具插件。它深度集成于 Microsoft Visual Studio Code，将 MUSA C/C++ 语言引入主流 IDE，提供从智能编辑、实时诊断、CUDA/MUSA 双向代码迁移到 MUSACode AI Coding Agent 的完整开发生命周期支持。

[MUSACode](https://docs.mthreads.com/playbook/playbook-doc-online/musacode) 是摩尔线程自主打造的 AI Coding Agent，基于终端交互，通过自然语言命令帮助开发者完成代码生成、调试、重构等任务，并面向 MUSA 算子开发、测试、编译和优化提供专项支持。从 v1.1.0 开始，MUSA for VS Code 同时作为 MUSACode 的 VS Code 插件入口使用，将 MUSACode 的终端 AI Coding Agent 能力带入 VS Code 图形界面。开发者可以在编辑器内完成对话、上下文引用、代码变更审阅和命令执行确认，而不必只依赖终端交互。

本插件基于 [MUSA SDK 5.1.0 或更高版本](https://docs.mthreads.com/musa-sdk/musa-sdk-doc-online/introduction/) 提供的 **clangd language server** 构建，并依托 [vscode-clangd](https://github.com/llvm-vs-code-extensions/vscode-clangd) 实现最佳兼容性。

无论您是在 Linux 本地工作站开发，还是通过 Remote-SSH 从 Windows/Linux 连接到远程 Linux 环境，MUSA for VS Code 均能提供一致、高效、可扩展的开发体验。

## 核心功能[](https://docs.mthreads.com#核心功能)

**智能代码编辑**：`.mu`

文件识别、关键字高亮、语义级补全、跳转、悬停信息**实时错误诊断**：编译错误与警告即时反馈，支持一键修复建议**代码现代化**：一键格式化（基于 clang-format）**跨生态迁移**：**musify**：CUDA → MUSA 自动转换**反向 musify**：MUSA → CUDA 验证

**clangd 智能引擎**：完整的 LSP 功能，包括跳转至定义、查找引用、重命名符号、悬停文档**MUSACode AI Coding Agent**：集成 MUSACode，支持侧边栏对话、多 Session、模型切换、文件/代码/终端上下文引用、Diff Review 和命令执行确认

## 使用场景[](https://docs.mthreads.com#使用场景)

- 本地工作站 MUSA SDK 开发
- 通过 SSH 远程开发 Linux 集群
- CUDA 到 MUSA 代码迁移项目
- MUSA 内核开发与调试
- 使用 MUSACode 分析工程、生成代码修改、检查变更与确认执行命令