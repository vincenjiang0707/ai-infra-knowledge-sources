# [Issue #3781] [Bug] fill_kv_cache 实现有bug

source: https://github.com/InternLM/lmdeploy/issues/3781
state: closed | updated: 2026-08-04T12:40:55Z
labels: 

## 正文

### Checklist

- [ ] 1. I have searched related issues but cannot get the expected help.
- [ ] 2. The bug has not been fixed in the latest version.
- [ ] 3. Please note that if the bug-related issue you submitted lacks corresponding environment info and a minimal reproducible demo, it will be challenging for us to reproduce and resolve the issue, reducing the likelihood of receiving feedback.

### Describe the bug

triton arange 参数要求是参数是2 的指数，fill_kv_cache 获取block 没有保证是2 的指数

<img width="1622" height="628" alt="Image" src="https://github.com/user-attachments/assets/8ec1dbab-5998-4a55-b6f1-c7ac04a30eb2" />

### Reproduction

qwen2_vl 3b 执行报错

### Environment

```Shell
qwen2_vl 3b
```

### Error traceback

```Shell

```

## 评论 (1)

### grimoire · 2025-07-28

这个 block_size 是 paged attention 中的 block 大小，是引擎的一个配置参数
https://github.com/InternLM/lmdeploy/blob/5f0647f1181312975f05d16eeb166d5a69afb6ef/lmdeploy/messages.py#L342

通常是要求必须是2的指数次的，如果不这么做，那么 fill_kv_cache / paged_attention 等很多模块/kernel都会受到影响，对性能没什么好处（要在 kernel 中加更多边界检查；attention 中的 tensorcore 使用也会更复杂）。因此这里对 block size 其实是有隐式的假设的，也许在启动引擎的检查中就应该加个断言？
