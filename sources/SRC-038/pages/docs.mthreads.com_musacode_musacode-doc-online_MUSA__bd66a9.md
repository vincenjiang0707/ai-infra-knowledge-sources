source: https://docs.mthreads.com/musacode/musacode-doc-online/MUSA算子开发专属能力

# MUSA 算子开发专属能力

MUSACODE 不仅是一个通用的 AI 编程助手，更是专为 MUSA 生态量身打造的开发利器。主要优势包括：

## 算子代码生成[](https://docs.mthreads.com#算子代码生成)

用自然语言描述算子逻辑，MUSACODE 直接生成符合 MUSA 规范的 kernel 代码。

`> 帮我写一个 MUSA 的 softmax kernel，支持 fp16 和 fp32，输入维度为 (batch, seq_len, hidden_dim)`



MUSACODE 会生成完整的 kernel 实现，包含合理的线程块划分、共享内存使用和数值稳定性处理。

## CUDA 到 MUSA 迁移[](https://docs.mthreads.com#cuda-到-musa-迁移)

如果你有现成的 CUDA 代码，MUSACODE 可以帮助你高效迁移。

`> 把这个 CUDA kernel 转换为 MUSA 版本，注意 API 差异和硬件特性适配`



MUSACODE 会自动处理 API 映射、头文件替换和硬件特性适配。

## 编译与调试[](https://docs.mthreads.com#编译与调试)

MUSACODE 可以�直接调用 MUSA 工具链帮助你编译和调试。

`> 用 mcc 编译当前项目，如果有编译错误帮我修复`

> 运行 musa-gdb 调试这个 kernel，看看 block (0,0) 的 shared memory 内容



## 性能分析与优化[](https://docs.mthreads.com#性能分析与优化)

结合 MUSA 性能分析工具，MUSACODE 可以帮助你识别和解决性能瓶颈。

`> 对 matmul kernel 做一次 profiling，分析 occupancy 和 memory bandwidth 利用率`

> 当前 kernel 的 occupancy 只有 25%，帮我优化线程配置来提高占用率



## 测试生成[](https://docs.mthreads.com#测试生成)

自动生成算子的单元测试和正确性验证代码。

`> 为 softmax kernel 生成单元测试，包括边界条件和精度对比测试`