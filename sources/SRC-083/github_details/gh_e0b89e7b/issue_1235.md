# [Issue #1235] out kwarg in matmul_4bit() is not working 

source: https://github.com/bitsandbytes-foundation/bitsandbytes/issues/1235
state: closed | updated: 2026-03-13T10:04:38Z
labels: Bug, Contributions Welcome

## 正文

### System Info

Linux 20.04

### Reproduction

output is defined as a tensor. The following works as expected:
`output = matmul_4bit(a, b)`

but the following does not, the elements in output are not changed. 
`matmul_4bit(a, b, out=output)`

### Expected behavior

`matmul_4bit(a, b, out=output)` is expected to have the output values set. It is a preferred way as it saves extra memory copy. 

## 评论 (4)

### matthewdouglas · 2024-06-03

Hi @chenqianfzh,

Thanks for reporting this issue. I believe that I see the same behavior with the 8bit version `matmul` as well.

For the 4bit version, this may work as expected when taking the `gemv` path, i.e. inputs where `a` is a 1D tensor with size divisible by selected blocksize.

### chenqianfzh · 2024-06-04

Thanks for checking it out. 

I am using this function in model reference, so a needs to high-dimensional tensors. :-(

> Hi @chenqianfzh,
> 
> Thanks for reporting this issue. I believe that I see the same behavior with the 8bit version `matmul` as well.
> 
> For the 4bit version, this may work as expected when taking the `gemv` path, i.e. inputs where `a` is a 1D tensor with size divisible by selected blocksize.



### vrdn-23 · 2024-06-13

Is there a fix planned for this anytime soon @matthewdouglas?

### HAKSOAT · 2025-03-29

Hi @matthewdouglas , I'm new to bitsandbytes and I would like to give this a shot.
