source: https://docs.opencloudos.org/OC9/ai-deployment/GPU-optimization-practice/amd-deployment/

# 基于 OpenCloudOS 的 AMD-ROCm 部署实践

目前， OpenCloudOS 已实现对 AMD 驱动与 ROCm 软件栈的深度适配和原生支持，为使用AMD GPU 用户提供了完整的 RPM 二进制软件包，包括内核级驱动、系统管理工具、计算库及AI框架适配组件。

本文档将指导如何在 OpenCloudOS 上快速完成 AMD GPU 驱动与 ROCm 的安装部署，并无缝运行上层AI模型与应用。

## 一、基础环境要求及说明

1、 **支持 OpenCloudOS 版本** ：系统要求参见下表1，仅支持该表中系统版本。如低于支持版本，请先升级内核。同时，在使用 AMD 驱动时，gcc版本建议和系统发行版保持一致，cmake版本不低于3.10。

2、 **支持的 GPU 设备** ：AMD Instinct MI300X系列

3、 **AMD GPU Driver (amdgpu) 版本** ：30.10.2

4、 **ROCm版本** ：7.0.2

5、 **环境检查** ：该部署流程中，驱动包主要以二进制形式安装，因此需严格按照第二节「前置检查」流程，匹配软硬件系统，确认CPU架构，操作系统版本是否在列表中。

| CPU架构 | 操作系统版本 | 内核版本 |
|---|---|---|
| x86_64 | 不小于 OpenCloudOS 9.4 | 不小于 6.6.104-41.oc9 |

表1：支持的 OpenCloudOS 系统版本

## 二、前置检查

```
# 检查CPU架构
uname -m
# 检查操作系统版本
lsb_release -a
# 检查内核版本
uname -r
# 检查是否已安装旧版驱动
yum list installed | grep amdgpu
# 检查GPU设备是否识别
lspci | grep DeviceID
```


如已安装旧驱动，请先执行：yum remove amdgpu-dkms

如 OpenCloudOS 内核版本不满足需求，请先升级至指定内核并设置默认启动内核（见表1）

## 三、安装ROCm runtime 以及 AMD GPU驱动

### 3.1 安装 EPOL 源

```
# 如使用 OpenCloudOS 9系统，请先安装EPOL软件源
dnf update
dnf install epol-extras-release
```


### 3.2 安装ROCm SDK包

关于 AMD ROCm 相关依赖包和 AMD GPU 驱动包的相关信息，请参看 **附录一：软件包清单** 。

```
# 一键安装 ROCm 相关依赖组件
dnf install rocm
```


### 3.3 安装 AMD GPU驱动

启用 yum 源执行, 驱动安装完成后重启系统：

```
# 安装驱动及依赖
dnf install dnf clean all
dnf install "kernel-headers-$(uname -r)" "kernel-devel-$(uname -r)"
dnf install amdgpu-dkms
lsmod |grep amdgpu
dkms status
```


```
# 验证驱动安装
dkms status
```


驱动卸载：

```
# 驱动热加载
modprobe amdgpu
# 驱动热卸载
modprobe -r amdgpu
#卸载amdgpu驱动包
dnf remove amdgpu-dkms
#如果卸载有dkms 脚本报错问题，可以尝试下面方式卸载
rpm -e --noscripts amdgpu-dkms
```


### 3.4 GPU固件升级（如需）

ROCm 和 amdgpu driver 版本对应 GPU 的 firmware 版本，请联系硬件厂商确定版本，通过机器BMC升级，然后需重启系统生效。

### 3.5 安装验证

输入`amd-smi`

查看AMDGPU设备状态

输入`rocm-smi`

查看ROCm System Management Interface状态

## 四、AI 框架安装与验证

### 4.1 安装PyTorch

```
# 在线安装（推荐）https://hub.docker.com/r/rocm/pytorch
docker pull rocm/pytorch:latest
```


### 4.2 运行 AI 框架（以 vLLM 示例）

```
# 拉取 vllm 容器镜像（准备好模型）
docker pull rocm/vllm-dev:nightly # to get the latest image
docker run -it --rm \
--network=host \
--group-add=video \
--ipc=host \
--cap-add=SYS_PTRACE \
--security-opt seccomp=unconfined \
--device /dev/kfd \
--device /dev/dri \
-v <path/to/your/models>:/app/models \
-e HF_HOME="/app/models" \
rocm/vllm-dev:nightly
# vllm 启动模型推理服务
vllm serve /app/models/DeepSeek-R1-Distill-Qwen-1.5B/ --port 8000 --served-model-name DeepSeek-R1-Distill-Qwen-1.5B &
# curl 开启chat对话
curl -X POST "http://localhost:8000/v1/chat/completions" \
-H "Content-Type: application/json" \
-d '{
"model": "DeepSeek-R1-Distill-Qwen-1.5B",
"messages": [
{"role": "user", "content": "你好,请介绍一下 linux"}
],
"max_tokens": 100
}'
```


### 4.3 运行模型（以Deepseek-R1为例）

### 4.4 结果展示

## 五、问题排查

若 AMD GPU 驱动或 ROCm 安装失败，可以从 [AMD ROCm官方开发者社区](https://rocm.docs.amd.com/projects/install-on-linux/en/latest/reference/install-faq.html) 获取帮助。

### 附录一：软件包清单

| 文件名（.rpm） | 包名 | |
|---|---|---|
AMD GPU-Driver |
amdgpu-core-7.0.70002-2226275 | amdgpu-core |
| libdrm-amdgpu-common-1.0.0.70002-2226275 | libdrm-amdgpu-common | |
| libdrm-amdgpu-2.4.124.70002-2226275 | libdrm-amdgpu | |
| libdrm-amdgpu-devel-2.4.124.70002-2226275 | libdrm-amdgpu-devel | |
| amd-smi-lib-26.0.2.70002-56 | amd-smi-lib | |
| hsa-amd-aqlprofile-1.0.0.70002-56 | hsa-amd-aqlprofile | |
| hip-runtime-amd-7.0.51831.70002-56 | hip-runtime-amd | |
| amdgpu-dkms-firmware-30.10.2.0.3010200-2226257 | amdgpu-dkms-firmware | |
| amdgpu-dkms-6.14.14-2226257 | amdgpu-dkms | |
ROCm |
rocm-core-7.0.2.70002-5664 | rocm-core |
| rocm-device-libs-1.0.0.70002-5664 | rocm-device-libs | |
| rocm-llvm-20.0.0.25385.70002-5664 | rocm-llvm | |
| rocminfo-1.0.0.70002-5664 | rocminfo | |
| rocm-smi-lib-7.8.0.70002-5664 | rocm-smi-lib | |
| rocm-dbgapi-0.77.4.70002-5664 | rocm-dbgapi | |
| rocm-cmake-0.14.0.70002-5664 | rocm-cmake | |
| rocm-language-runtime-7.0.2.70002-5664 | rocm-language-runtime | |
| rocm-hip-runtime-7.0.2.70002-5664 | rocm-hip-runtime | |
| rocm-hip-runtime-devel-7.0.2.70002-5664 | rocm-hip-runtime-devel | |
| rocm-opencl-2.0.0.70002-5664 | rocm-opencl | |
| rocm-debug-agent-2.1.0.70002-5664 | rocm-debug-agent | |
| rocm-gdb-16.3.70002-5664 | rocm-gdb | |
| rocm-openmp-7.0.2.70002-5664 | rocm-openmp | |
| rocm-hip-7.0.2.70002-5664 | rocm-hip | |
| rocm-developer-tools-7.0.2.70002-5664 | rocm-developer-tools | |
| rocm-opencl-devel-2.0.0.70002-5664 | rocm-opencl-devel | |
| rocm-opencl-sdk-7.0.2.70002-5664 | rocm-opencl-sdk | |
| rocm-7.0.2.70002-5664 | rocm |