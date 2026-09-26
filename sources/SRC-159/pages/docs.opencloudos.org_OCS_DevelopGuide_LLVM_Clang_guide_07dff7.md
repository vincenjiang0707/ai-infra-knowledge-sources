source: https://docs.opencloudos.org/OCS/DevelopGuide/LLVM_Clang_guide/

# LLVM/Clang使用指南

LLVM是一个模块化和可重用的编译器和工具链技术的集合，Clang是基于LLVM提供的库、工具开发的编译器前端，可编译C语言系列（C, C++, Objective C/C++, OpenCL, CUDA, and RenderScript），兼容GCC、编译快、诊断信息清晰。

## 1. 安装

可以运行以下命令来安装：

```
sudo dnf install llvm
sudo dnf install clang
```


安装完毕后可通过如下指令检查是否正确安装：

```
clang --version
```


链接器lld、调试器lldb、编译器运行时compile-rt按需安装：

```
sudo dnf install lld
sudo dnf install lldb
sudo dnf install compiler-rt
```


## 2. 使用

以简单的helloworld程序为例：

```
#include <stdio.h>
int main(int argc, char **argv) {
printf("hello world!!!\n");
return 0;
}
```


直接编译：

```
clang helloworld.c
```


```
clang helloworld.c
./a.out
hello world!!!
```


## 3. 附录

更多使用详情，请参考:

https://llvm.org/docs/UserGuides.html

https://clang.llvm.org/docs/UsersManual.html