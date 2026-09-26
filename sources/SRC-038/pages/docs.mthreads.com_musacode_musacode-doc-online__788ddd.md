source: https://docs.mthreads.com/musacode/musacode-doc-online/常见问题

# 常见问题

## MUSACODE 与其他 CodeAgent 有什么区别？[](https://docs.mthreads.com#musacode-与其他-codeagent-有什么区别)

MUSACODE 在强��大的通用编程能力的基础上，针对摩尔线程 MUSA 生态进行了专项增强，使其成为 MUSA 算子开发的最佳伴侣。

## 我的代码会被上传到云端吗？[](https://docs.mthreads.com#我的代码会被上传到云端吗)

隐私安全方面，MUSACODE 的代码分析和文件操作都在你的本地环境中完成。只有发送给 AI 模型的对话内容会通过网络传输，你可以通过配置本地模型（如 Ollama）实现完全离线使用。

## 如何在团队中统一配置？[](https://docs.mthreads.com#如何在团队中统一配置)

将项目级配置文件 `musacode.json`

和规则文件 `.musacode/rules/`

一起提交到版本库中，团队成员即可共享统一的 AI 编程规范。

## MUSACODE 支持哪些编程语言？[](https://docs.mthreads.com#musacode-支持哪些编程语言)

MUSACODE 支持所有主流编程语言，包括但不限于：

- C/C++
- Python
- Go
- Rust
- JavaScript/TypeScript

对于 MUSA 相关的 `.mu`

文件和 MUSA C/C++ 扩展，MUSACODE 提供了特别优化的支持。