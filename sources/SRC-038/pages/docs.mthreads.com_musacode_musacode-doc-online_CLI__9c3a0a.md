source: https://docs.mthreads.com/musacode/musacode-doc-online/CLI命令行参考

# CLI 命令行参考

除了交互式 TUI，MUSACODE 还支持命令行直接调用：

`# 启动交互式 TUI`

musacode


# 直接发送提示词并获取结果（非交互模式）

musacode -p "解释一下这个项目的目录结构"


# 指定模型

musacode --model MT-KuaeCloud/GLM-4.7


# 从标准输入读取内容

cat error.log | musacode -p "分析这个错误日志"


# 输出为 JSON 格式（便于管道处理）

musacode -p "列出所有 TODO 项" --format json