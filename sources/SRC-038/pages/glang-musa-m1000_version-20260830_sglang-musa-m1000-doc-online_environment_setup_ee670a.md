source: https://docs.mthreads.com/sglang-musa-m1000/version-20260830/sglang-musa-m1000-doc-online/environment_setup

# 环境准备与部署

注意：本指南目前只适用于 M1000 AImodule 环境。安装前请确认设备系统、驱动和软件栈版本与待发布的软件包版本匹配。

## 步骤1 确认环境[](https://docs.mthreads.com#步骤1-确认环境)

### 确认操作系统版本[](https://docs.mthreads.com#确认操作系统版本)

仅支持 AIOS 1.4.1，请先和设备提供方确认设备是否为 AIOS 1.4.1。

### 确认 MUSA 环境[](https://docs.mthreads.com#确认-musa-环境)

执行 `musaInfo`

，输出正常则环境配置正确。

### 确认 MUSA 和 MUSA SDK 的版本号[](https://docs.mthreads.com#确认-musa-和-musa-sdk-的版本号)

请确认已安装的 MUSA 和 MUSA SDK 版本是否符合要求：

`musa`

版本号应为：`5.1.1-M1000`

`musa-sdk`

版本号应为：`5.1.1`


执行以下命令检查版本：

`sudo dpkg -l | grep musa`



正确输出如下：

`ii musa 5.1.1-M1000 arm64 Moore Threads MUSA driver [e29787e05]`

ii musa-sdk 5.1.1 arm64 Moore Threads MTGPU Software Development Kit



### 检查结果[](https://docs.mthreads.com#检查结果)

- 如果 MUSA 版本为
`5.1.1-M1000`

且 MUSA SDK 版本为`5.1.1`

，仍需执行 步骤2 下载并解压离线安装包以获取后续依赖文件，但无需重新安装 MUSA 和 MUSA SDK，可跳过 步骤3。 - 如果任一版本不符合要求，请先执行 步骤2 下载安装包，再按照 步骤3 更新 MUSA 和 MUSA SDK。

## 步骤2 相关依赖包[](https://docs.mthreads.com#步骤2-相关依赖包)

请访问 [摩尔线程开发者平台 SGLang-MUSA-M1000](https://developer.mthreads.com/sdk/download/soc?equipment=MTT+E300&os=Ubuntu+22.04&driverVersion=&version=1.4.1) 下载 `M1000_1.4.1_sglang_0831`

，并解压得到安装包目录：

`tar -zxvf SGLang-MUSA-M1000_M1000_1.4.1_sglang_0831.tar.gz`

cd 20260831_M1000_1.4.1_sglang/



解压后目录中包含以下文件：

| 组件 | 版本 | 安装包 |
|---|---|---|
| MUSA | 5.1.1 | `musa_5.1.1-M1000_arm64.deb` |
| MUSA SDK | 5.1.1 | `musa-sdk_5.1.1_arm64.deb` |
| Triton MUSA | 3.2.0 | `triton-3.2.0-cp310-cp310-linux_aarch64.whl` |
| Torch | 2.9.0 | `torch-2.9.0-cp310-cp310-linux_aarch64.whl` |
| Torch MUSA | 2.9.0 | `torch_musa-2.9.0-cp310-cp310-linux_aarch64.whl` |
| TorchAudio | 2.9.0+eaa9e4e | `torchaudio-2.9.0+eaa9e4e-cp310-cp310-linux_aarch64.whl` |
| TorchVision | 0.22.1+e98278b | `torchvision-0.22.1+e98278b-cp310-cp310-linux_aarch64.whl` |
| Torch C DLPack Ext | 0.1.5 | `torch_c_dlpack_ext-0.1.5-cp310-cp310-manylinux_2_24_aarch64.manylinux_2_28_aarch64.whl` |
| TileLang MUSA | 0.1.6.post2+musa.3 | `tilelang_musa-0.1.6.post2+musa.3-cp38-abi3-linux_aarch64.whl` |
| MATE | 0.2.5 | `mate-0.2.5-py3-none-any.whl` |
| Apache TVM FFI | 0.1.9.post3.dev0+musa.1.gf6b52d7f4.d20260703 | `apache_tvm_ffi-0.1.9.post3.dev0+musa.1.gf6b52d7f4.d20260703-cp310-cp310-manylinux_2_24_aarch64.manylinux_2_28_aarch64.whl` |
| SGLang Kernel | 0.4.1.dev20260907 | `sglang_kernel-0.4.1.dev20260907-cp39-abi3-linux_aarch64.whl` |
| SGLang | 0.5.10+20260907 | `sglang-0.5.10+20260907-py3-none-any.whl` |
| SGLang M1000 benchmark 脚本 | - | `scripts/` |
| conda 依赖 | - | `environment.yml` |

## 步骤3 系统环境配置[](https://docs.mthreads.com#步骤3-系统环境配置)

### 1. 卸载当前驱动[](https://docs.mthreads.com#1-卸载当前驱动)

`sudo dpkg -P musa-sdk`

sudo dpkg -P musa # 输出 cryptsetup 的一些报错是正常的

sudo rm -rf /usr/local/musa*



### 2. 安装新的驱动和软件栈[](https://docs.mthreads.com#2-安装新的驱动和软件栈)

`sudo dpkg -i musa_5.1.1-M1000_arm64.deb`

sudo dpkg -i musa-sdk_5.1.1_arm64.deb



安装完成后重启设备：

`sudo reboot`



### 3. 确认 MUSA 环境[](https://docs.mthreads.com#3-确认-musa-环境)

执行 `musaInfo`

，输出正常则环境配置正确。

如果提示找不到命令，可以先补充环境变量后再次验证：

`export PATH=/usr/local/musa/bin:${PATH}`

export LD_LIBRARY_PATH=/usr/local/musa/lib:${LD_LIBRARY_PATH}

musaInfo



## 步骤4 Python 环境配置[](https://docs.mthreads.com#步骤4-python-环境配置)

### 安装 Miniforge[](https://docs.mthreads.com#安装-miniforge)

如果设备尚未安装 Conda，推荐使用 Miniforge。Miniforge 提供适用于本设备
`Linux aarch64`

架构的 Conda 发行版。执行以下命令下载并安装：

`wget https://mirrors.tuna.tsinghua.edu.cn/github-release/conda-forge/miniforge/LatestRelease/Miniforge3-Linux-aarch64.sh`

bash Miniforge3-Linux-aarch64.sh



安装过程中：

- 按
**Enter**查看许可协议，输入`yes`

接受协议。 - 安装目录可使用默认值（通常为
`~/miniforge3`

）。 - 当提示是否运行
`conda init`

时输入`yes`

。

安装完成后重新打开终端，或执行以下命令使配置立即生效：

`source ~/.bashrc`

conda --version



如果安装时使用了其他目录，请将上述路径替换为实际安装目录。确认能够正常输出 Conda 版本号后，再继续创建 Python 环境。

推荐使用独立 conda 环境：

`conda create -n sglang-py310 python=3.10 -y`

conda activate sglang-py310


pip install --upgrade pip



安装 Torch、Torch MUSA 及相关 pip 依赖：

`pip install torch-2.9.0-cp310-cp310-linux_aarch64.whl`

pip install torch_musa-2.9.0-cp310-cp310-linux_aarch64.whl

pip install torchvision-0.22.1+e98278b-cp310-cp310-linux_aarch64.whl

pip install torchaudio-2.9.0+eaa9e4e-cp310-cp310-linux_aarch64.whl

pip install triton-3.2.0-cp310-cp310-linux_aarch64.whl

pip install torch_c_dlpack_ext-0.1.5-cp310-cp310-manylinux_2_24_aarch64.manylinux_2_28_aarch64.whl



### 环境验证[](https://docs.mthreads.com#环境验证)

输出 `true`

证明 Torch MUSA 环境安装正确：

`python3 -c "import torch; import torch_musa; print(torch.musa.is_available())" 2>/dev/null`



## 步骤5 从安装包安装 SGLang[](https://docs.mthreads.com#步骤5-从安装包安装-sglang)

在解压后的安装包目录中安装 TileLang MUSA、MATE、Apache TVM FFI、SGLang Kernel 和 SGLang：

`pip install tilelang_musa-0.1.6.post2+musa.3-cp38-abi3-linux_aarch64.whl`

pip install --no-deps mate-0.2.5-py3-none-any.whl

pip install apache_tvm_ffi-0.1.9.post3.dev0+musa.1.gf6b52d7f4.d20260703-cp310-cp310-manylinux_2_24_aarch64.manylinux_2_28_aarch64.whl

pip install sglang_kernel-0.4.1.dev20260907-cp39-abi3-linux_aarch64.whl

pip install --no-deps sglang-0.5.10+20260907-py3-none-any.whl



安装其他依赖：

`sudo apt update`

sudo apt install python3-pip git cmake wget build-essential g++ libstdc++-12-dev libnuma-dev curl

conda env update -f environment.yml



## 步骤6 安装验证[](https://docs.mthreads.com#步骤6-安装验证)

`pip list | grep sglang`



输出示例：

`sglang 0.5.10+20260907`

sglang-kernel 0.4.1.dev20260907



## 【可选】打开性能模式（推荐）[](https://docs.mthreads.com#可选打开性能模式推荐)

### For T035 开发板[](https://docs.mthreads.com#for-t035-开发板)

#### From 命令行[](https://docs.mthreads.com#from-命令行)

**性能模式**

`sudo powerprofilesctl set performance`



**平衡模式**

`sudo powerprofilesctl set balanced`



**节电模式**

`sudo powerprofilesctl set power-saver`



### For 天思盒子[](https://docs.mthreads.com#for-天思盒子)

#### From 界面 (推荐)[](https://docs.mthreads.com#from-界面-推荐)

界面右上角: 电源 -> 性能

#### From 命令行[](https://docs.mthreads.com#from-命令行-1)

**性能模式**

`#!/bin/sh`

sudo busybox devmem 0x280FD200 32 2650

sudo busybox devmem 0x280FD218 32 2650

sudo busybox devmem 0x280FD230 32 2650

sudo busybox devmem 0x280FD248 32 1500



**非性能模式**

`#!/bin/sh`

sudo busybox devmem 0x280FD200 32 1700

sudo busybox devmem 0x280FD218 32 1700

sudo busybox devmem 0x280FD230 32 1700

sudo busybox devmem 0x280FD248 32 730