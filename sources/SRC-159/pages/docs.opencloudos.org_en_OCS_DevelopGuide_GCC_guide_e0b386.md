source: https://docs.opencloudos.org/en/OCS/DevelopGuide/GCC_guide/

# GCC开发指南

## 1. GCC简介

GCC全称为GNU Compiler Collection，即GNU编译器套件。是GNU项目开发的编译器软件，最初支持C/C++，后拓展支持ObjectC、Go、Fortran等多种语言，发展为一个编译器套件，现在主要由FSF支持维护。

### 1.1 本系统上的GCC选型及维护政策

本系统上的GCC版本为12.x，在GCC上游社区的12版本完整维护周期内，本系统将会及时跟进小版本的更新，直至GCC12.x的最后一个版本后，本系统仍旧为GCC12的bugfix进行后续维护，直至本系统的当前版本不再维护。

### 1.2 本系统上的GCC组件

| 组件 | X86_64 | Aarch64 | Loongarch64 | Riscv64 | SW_64 | 说明 |
|---|---|---|---|---|---|---|
| gcc | 支持 | 支持 | 支持 | 暂无 | 暂无 | GCC的C编译器 |
| gcc-c++ | 支持 | 支持 | 支持 | 暂无 | 暂无 | GCC的C++编译器，有些发行版称为g++ |
| gccgo | 支持 | 支持 | 支持 | 暂无 | 暂无 | GCC的Golang编译器 |
| gfortran | 支持 | 支持 | 支持 | 暂无 | 暂无 | GCC的Fortran编译器 |
| gnat | 支持 | 支持 | 支持 | 暂无 | 暂无 | GCC的Ada编译器 |
| gcc-objc | 支持 | 支持 | 支持 | 暂无 | 暂无 | GCC的ObjectC编译器 |
| gcc-obgc++ | 支持 | 支持 | 支持 | 暂无 | 暂无 | GCC的ObjectC++编译器 |
| gcc-gdc | 支持 | 支持 | 支持 | 暂无 | 暂无 | GCC的D语言编译器 |
| gcc-gm2 | 不支持 | 不支持 | 不支持 | 不支持 | 不支持 | GCC的M2语言编译器，GCC13新增，本系统不支持 |

### 1.3 安装

```
# gcc
dnf install gcc
# gcc-c++
dnf install gcc-c++
# gccgo
dnf install gccgo
# gfortran
dnf install gfortran
# libtsan
dnf install libtsan
# 使用tsan进行开发
dnf install libtsan-devel
# 其他组件请参看1.2，按照组件名进行安装
# 请注意，libgomp不提供devel包
```


## 2. GCC使用介绍

### 2.1 GCC的使用流程简介 - 以C语言为例

以一个名为helloworld.c的C程序源码文件为例：

```
#include <stdio.h>
int main() {
printf("hello,world!\n");
return 0;
}
```


```
# 安装C编译器
dnf install gcc
# 编译为二进制
gcc -o helloworld helloworld.c
# 执行
./helloworld
```


### 2.2 GCC执行程序的更多功能介绍

编译器对源码处理过程可以分为预处理(也称预编译，Preprocessing)、编译 (Compilation)、汇编 (Assembly)和链接(Linking)四个过程。下面我们来尝试使用gcc进行分步骤处理。

以一个名为hellooc.cpp的文件为例，

```
#include <iostream>
using namespace std;
char* hellooc(char* oc) {
cout << "hello, " << oc << "!" << endl;
return oc;
}
```


需要安装相对应的GCC编译器开发环境

```
#安装GCC C++编译器和C++开发库、运行时
dnf install gcc-c++ libstdc++-devel
```


#### 2.2.1 预处理

首先进行预处理：

```
g++ -E -o hellooc.i hellooc.cpp
# 结果过长，本文档不做结果展示，请自行执行查看
less hellooc.i
```


#### 2.2.2 编译

然后执行编译(狭义的编译)，结果为汇编代码:

```
g++ -S -o hellooc.s -fPIC hellooc.i
# 结果过长，本文档不做结果展示，请自行执行查看
less hellooc.s
```


#### 2.2.3 汇编编译

继续执行汇编编译，结果为未链接的目标文件:

```
g++ -c -o hellooc.o hellooc.s
```


#### 2.2.4 链接

最后执行链接，结果为链接库:

```
# 动态链接
g++ -o hellooc.so -shared -lstdc++ hellooc.o
# 静态链接
ar rcs hellooc.a hellooc.o
```


```
hellooc.so: ELF 64-bit LSB shared object, x86-64, version 1 (SYSV), dynamically linked, BuildID[sha1]=92a45a52fc17fa866d765841e159d57271e767b1, not stripped
hellooc.a: current ar archive
```


### 3. 更多参考资料

本文档仅用于开发者了解本系统上的GCC组件支持情况、安装方式和简单的使用示例，更多GCC和开发资料，请查看GCC官方文档和第三方资料。

GCC 12.x 官方文档: https://gcc.gnu.org/gcc-12/

GCC 中文文档: https://runebook.dev/zh/docs/gcc/-index-