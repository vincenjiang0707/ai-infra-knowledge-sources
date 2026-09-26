# [Issue #41] 链接时报错torch_npu::init_npu(std::string const&)

source: https://github.com/Ascend/pytorch/issues/41
state: open | updated: 2024-09-21T06:48:06Z
labels: 

## 正文

编译时候报错torch_npu::init_npu(std::string const&)
nm 命令查找libtorch_npu.so，也未找到这个函数

## 评论 (5)

### ChengruiZhang · 2024-06-19

![image](https://github.com/Ascend/pytorch/assets/35398790/32458e8c-a192-466d-add1-3bba10e0b35b)
不论是pip还是源码编译出的库中均会出现类似的问题

### yunyiyun · 2024-06-21

如果是使用libtorch_npu，请使用build_libtorch_npu.py编译获得

### HowardZorn · 2024-09-20

I also have the same issue. Your libtorch_npu does not contain any version of the symbol `torch_npu::init_npu`.

### HowardZorn · 2024-09-20

A Huawei employee said, "This symbol is only provided by libtorch_npu, but not the python package torch_npu". So it should be compiled by ourselves. 

But there is a possible non-compiling solution:

```c
// torch_npu::init_npu(device_index);
aclInit(nullptr);
c10_npu::SetDevice(device_index);
```

### yunyiyun · 2024-09-21

> A Huawei employee said, "This symbol is only provided by libtorch_npu, but not the python package torch_npu". So it should be compiled by ourselves.
> 
> But there is a possible non-compiling solution:
> 
> ```c
> // torch_npu::init_npu(device_index);
> aclInit(nullptr);
> c10_npu::SetDevice(device_index);
> ```

https://www.hiascend.com/document/detail/zh/Pytorch/60RC2/configandinstg/instg/insg_0007.html
