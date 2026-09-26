# [Issue #4878] How can I add some dialects for optimization?

source: https://github.com/triton-lang/triton/issues/4878
state: closed | updated: 2026-09-04T12:18:34Z
labels: 

## 正文

I tried to incorporate some optimizations into Triton, but I don't know how to do it. If you have any ideas, please share them with me. I would greatly appreciate it. 

## 评论 (8)

### gavin838 · 2024-10-15

https://github.com/llvm/llvm-project/blob/main/mlir/docs/Tutorials/QuickstartRewrites.md, this doc maybe help you.

### zhananran · 2024-10-15

> https://github.com/llvm/llvm-project/blob/main/mlir/docs/Tutorials/QuickstartRewrites.md, this doc maybe help you.
I am truly grateful for your help.‌ 



### gavin838 · 2024-10-15

收到!谢谢

### zhananran · 2024-10-16

> 收到!谢谢

大佬，我想要加入affine，但是我发现affine有自己的Analysis，我能想到的lowering方法是triton->affine->triton->其他dialects  ，这样合理吗，或者有什么更好的方法吗？求解答orz

### Jokeren · 2024-11-05

https://github.com/microsoft/triton-shared

This might be what you're looking for?

### gavin838 · 2024-11-05

收到!谢谢

### zhananran · 2024-11-05

> https://github.com/microsoft/triton-shared
> 
> This might be what you're looking for?

Thank you very much!


### gavin838 · 2026-09-03

收到!谢谢
