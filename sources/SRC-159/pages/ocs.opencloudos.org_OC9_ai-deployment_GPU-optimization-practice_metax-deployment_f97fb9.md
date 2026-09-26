source: https://docs.opencloudos.org/OC9/ai-deployment/GPU-optimization-practice/metax-deployment/

# 基于 OpenCloudOS 的沐曦部署实践

目前， OpenCloudOS 已实现对沐曦 MetaX 驱动与 MXMACA SDK 的深度适配和原生支持，为使用沐曦 GPU 用户提供了完整的 RPM 二进制软件包，包括内核级驱动、系统管理工具、计算库及AI框架适配组件。

本文档将指导如何在 OpenCloudOS 上快速完成沐曦 MetaX 驱动与 MXMACA SDK 的安装部署，并无缝运行上层AI模型与应用。

## 一、基础环境要求及说明

1、 **支持 OpenCloudOS 内核版本** ：系统及内核要求参见下表1， **仅支持该表中系统及内核版本，如低于支持版本，请先升级内核；若高于支持版本，OC社区与沐曦官方将尽快完善支持。** 同时，在使用maca-sdk驱动时，gcc版本建议和系统发行版保持一致，cmake版本不低于3.10。

2、 **支持的 GPU 设备** ：沐曦曦云 C500/C550/C588/C600/N260 系列

3、 **驱动软件版本** ：3.1.0.26

4、 **环境检查** ：该部署流程中，驱动包主要以二进制形式安装，因此需严格按照第二节「前置检查」流程，匹配软硬件系统，确认CPU架构，操作系统以及内核版本是否在列表中。若有任何一项不匹配，需按照表1升级软硬件系统。

5、 **其他要求** ：PCIe要求支持Gen5 X16，MMIO资源满足GPU板卡资源需求，服务器电源满足整机最大工作负载，单个PCIe槽位满足GPU单卡的供电需求。

| CPU架构 | 操作系统 | 内核版本 |
|---|---|---|
| x86_64 | OpenCloudOS 8 | 5.4.241-30.0017.19.oc8 |
| x86_64 | OpenCloudOS 9 | 6.6.104-41.oc9 |

表1：支持的 OpenCloudOS 系统版本

备注：以下部署流程以 OpenCloudOS 9 为例。

## 二、前置检查

请执行以下命令确认系统环境是否符合要求：

```
# 检查CPU架构
uname -m
# 检查操作系统版本
lsb_release -a
# 检查内核版本
uname -r
# 检查是否已安装旧版驱动
yum list installed | grep metax-driver
# 检查GPU设备是否识别
lspci | grep 9999
```


`yum remove metax-driver`

如 OpenCloudOS 内核版本不满足需求，请先升级至指定内核并设置默认启动内核（见表1）。

## 三、安装 MetaX 驱动及 MXMACA SDK

### 3.1 安装 OpenCloudOS EPOL源

```
# 如使用 OpenCloudOS 9 系统，请先安装 EPOL extras 软件源
dnf install epol-extras-release
```


### 3.2 安装MetaX驱动包

```
# 安装驱动及依赖
dnf install metax-driver-3.1.0.26
```


### 3.3 创建运行用户（可选）

目的是将非 root 用户加入 video 组，如已加入，该步骤无需处理。

```
sudo adduser <username>
sudo usermod -a -G video <username>
```


### 3.4 固件升级（如需）

MetaX系列GPU采用沐曦带内管理工具mx-smi对固件进行升级。mx-smi工具自动安装在驱动安装包的/opt/mxdriver/bin目录下。

```
# 查看当前固件版本
mx-smi --show-version
# 升级固件（需root）
sudo mx-smi -u /lib/firmware/metax/mxc500/mxvbios-xxx.bin -t 600
```


### 3.5 虚拟化安装（如需）

如需使用 GPU 的 SRIOV 硬件虚拟化功能，需安装mxgvm，如不需要该功能，则无需安装，否则可能会出现检测不到硬件设备的问题。

```
dnf install mxgvm-3.0.26
```


### 3.6 安装验证

可通过`mx-smi`

查看驱动安装结果

### 3.7 安装 MXMACA SDK包

由于相关 RPM 包较多，推荐使用如下命令一键安装。本次适配提供的MXMACA SDK RPM包清单，请参考 **附录一：软件包列表** 。

```
# 一键安装所有SDK组件
dnf install maca_sdk
```


## 四、AI 框架安装与验证

### 4.1 拉取 AI 镜像

可至沐曦官方开发者社区[「AI 人工智能程序包」分类下](https://developer.metax-tech.com/softnova/ai-download?package_kind=AI)，复制wget命令，进行不同 AI 框架的镜像拉取。截图以 vLLM 为例所示：

备注：沐曦官方将在后续逐步提供适配 OpenCloudOS 9 的AI框架。

### 4.2 配置 cu-bridge 环境

```
dnf install -y git cmake
export MACA_PATH=/opt/maca
wget https://gitee.com/metax-maca/cu-bridge/repository/archive/3.1.0.zip
unzip 3.1.0.zip
mv cu-bridge-3.1.0 cu-bridge
sudo chmod 755 cu-bridge -Rf
cd cu-bridge
mkdir build && cd ./build
cmake -DCMAKE_INSTALL_PREFIX=/opt/maca/tools/cu-bridge ../
make && make install
export MACA_PATH=/opt/maca
export CUCC_PATH=/opt/maca/tools/cu-bridge
export PATH=$PATH:${CUCC_PATH}/tools:${CUCC_PATH}/bin
export CUCC_CMAKE_ENTRY=2 # 选择使用cu-bridge模拟CMake服务
export CUDA_PATH=${CUCC_PATH} # CUDA_PATH入口重定向到cu-bridge安装位置
```


### 4.3 启动容器

在容器中运行 AI 框架及大模型需要使用宿主机 GPU 能力，及直通宿主机GPU， **主要有如下两种方式（可选其一）：**

**4.3.1 Docker Run（推荐方式）：**

```
docker run -it --restart=always --device=/dev/dri --device=/dev/mxcd --device=/dev/infiniband --group-add video --name deepspeed_test --network=host --security-opt seccomp=unconfined --security-opt apparmor=unconfined --shm-size 100gb --ulimit memlock=-1 --privileged=true -v /home:/home [image_id] bash
```


#### 4.3.2 Metax-docker run ：

**（1）安装 metax-docker：**

从浏览器登录沐曦开发者社区，在云平台工具中可找到[ metax-docker 的下载页面](https://developer.metax-tech.com/softnova/category?package_kind=Cloud&dimension=metax&chip_name=%E6%9B%A6%E4%BA%91C500%E7%B3%BB%E5%88%97&deliver_type=%E5%88%86%E5%B1%82%E5%8C%85&series_name=metax-docker)。

选择合适版本的离线压缩包进行下载，用户可解压后根据安装环境选择合适的包进行安装。

```
# 安装metax-docker
mkdir metax-docker
tar -C metax-docker -xvf metax-docker_0.13.1.tar
cd metax-docker
sudo ./metax-docker_0.13.1.<ARCH>.run
```


**（2）使用metax-docker：**

用户需要安装版本≥19.03的 Docker 工具。同时应确保主机上已经正确安装了 MXMACA 软件栈。

```
# 在容器中使用曦云GPU
metax-docker run -it --rm --gpus=all user-application:1.0 /bin/bash
```


metax-docker 支持官方Docker的全部命令及参数，并在 .run 命令下支持额外参数，详细可[参考该链接的指南](https://developer.metax-tech.com/api/client/document/preview/818/3rd/10_metax_docker.html)。

### 4.4 运行大模型（以vLLM+Qwen示例）

```
# 安装依赖
dnf install pip curl
# 下载 modelscope
pip install modelscope
# 拉取大模型（以 Qwen 为例）
modelscope download --model 'Qwen/Qwen2-7b'
# 运行服务
vllm serve /root/.cache/modelscope/hub/models/Qwen/Qwen2-7b --port 8000 --served-model-name Qwen2-7b --served-model-name Qwen/Qwen2-7b
# 另起终端利用 curl 对话
curl http://localhost:8000/v1/chat/completions -H "Content-Type: application/json" -d '{"model": "Qwen/Qwen2-7b","messages": [{"role": "system", "content": "你是一个有帮助的助手"},{"role": "user", "content": "法国首都在哪？"}],"max_tokens": 100,"temperature": 0.7}'
```


### 4.5 运行结果展示

## 五、手动安装指南（备用方案）

若 MetaX 驱动或 MXMACA SDK 安装失败，可以从[沐曦官方开发者社区](https://developer.metax-tech.com/softnova/index)下载需要的驱动程序和SDK开发工具包进行安装。

### 附录一：软件包列表

| 分类 | 文件名 | 包名 |
|---|---|---|
驱动 |
metax-driver-3.1.0.26-1.x86_64.rpm | metax-driver |
| metax-linux-3.1.0.26-1.x86_64.rpm | metax-linux | |
| mxgvm-3.0.26-1.x86_64.rpm | mxgvm | |
| mxfw-3.1.0-1.noarch.rpm | mxfw | |
| mxsmt-3.1.0-1.x86_64.rpm | mxsmt | |
SDK |
commonlib_3.1.0-3.1.0.19-1.x86_64.rpm | commonlib |
| maca_sdk-3.1.0.19-1.x86_64.rpm | maca_sdk | |
| maca_sdk_3.1.0-3.1.0.19-1.x86_64.rpm | maca_sdk | |
| macainfo_3.1.0-3.1.0.19-1.x86_64.rpm | macainfo | |
| mcanalyzer_3.1.0-3.1.0.19-1.x86_64.rpm | mcanalyzer | |
| mcblas_3.1.0-3.1.0.19-1.x86_64.rpm | mcblas | |
| mcblaslt_3.1.0-3.1.0.19-1.x86_64.rpm | mcblaslt | |
| mcccl_3.1.0-3.1.0.19-1.x86_64.rpm | mcccl | |
| mcccltests-3.1.0-3.1.0.19-1.x86_64.rpm | mcccltests | |
| mccompiler_3.1.0-3.1.0.19-1.x86_64.rpm | mccompiler | |
| mcdnn_3.1.0-3.1.0.19-1.x86_64.rpm | mcdnn | |
| mcfft_3.1.0-3.1.0.19-1.x86_64.rpm | mcfft | |
| mcfile_3.1.0-3.1.0.19-1.x86_64.rpm | mcfile | |
| mcflashattn_3.1.0-3.1.0.19-1.x86_64.rpm | mcflashattn | |
| mcflashinfer_3.1.0-3.1.0.19-1.x86_64.rpm | mcflashinfer | |
| mcgpufort_3.1.0-3.1.0.19-1.x86_64.rpm | mcgpufort | |
| mchotspot_3.1.0-3.1.0.19-1.x86_64.rpm | mchotspot | |
| mcimage_3.1.0-3.1.0.19-1.x86_64.rpm | mcimage | |
| mcjpeg_3.1.0-3.1.0.19-1.x86_64.rpm | mcjpeg | |
| mckernellib_3.1.0-3.1.0.19-1.x86_64.rpm | mckernellib | |
| mcmathlib_3.1.0-3.1.0.19-1.x86_64.rpm | mcmathlib | |
| mcpti_3.1.0-3.1.0.19-1.x86_64.rpm | mcpti | |
| mcrand_3.1.0-3.1.0.19-1.x86_64.rpm | mcrand | |
| mcruntime_3.1.0-3.1.0.19-1.x86_64.rpm | mcruntime | |
| mcsolver_3.1.0-3.1.0.19-1.x86_64.rpm | mcsolver | |
| mcsolverit_3.1.0-3.1.0.19-1.x86_64.rpm | mcsolverit | |
| mcsparse_3.1.0-3.1.0.19-1.x86_64.rpm | mcsparse | |
| mcthrust_3.1.0-3.1.0.19-1.x86_64.rpm | mcthrust | |
| mctlass_3.1.0-3.1.0.19-1.x86_64.rpm | mctlass | |
| mctoolext_3.1.0-3.1.0.19-1.x86_64.rpm | mctoolext | |
| mctracer-3.1.0-3.1.0.19-1.x86_64.rpm | mctracer | |
| metax-fabricmanager_3.1.0-3.1.0.19-1.x86_64.rpm | metax-fabricmanager | |
| mxccl_plugin_3.1.0-3.1.0.19-1.x86_64.rpm | mxccl_plugin | |
| mxcompute_3.1.0-3.1.0.19-1.x86_64.rpm | mxcompute | |
| mxdiagease-3.1.0-3.1.0.19-1.x86_64.rpm | mxdiagease | |
| mxexporter-3.1.0-3.1.0.19-1.x86_64.rpm | mxexporter | |
| mxffmpeg-3.1.0-3.1.0.19-1.x86_64.rpm | mxffmpeg | |
| mxffmpeg-dev-3.1.0-3.1.0.19-1.x86_64.rpm | mxffmpeg-dev | |
| mxfortran_3.1.0-3.1.0.19-1.x86_64.rpm | mxfortran | |
| mxgdrcopy-3.1.0-3.1.0.19-1.x86_64.rpm | mxgdrcopy | |
| mxgpu_llvm_3.1.0-3.1.0.19-1.x86_64.rpm | mxgpu_llvm | |
| mxkw_3.1.0-3.1.0.19-1.x86_64.rpm | mxkw | |
| mxmaca-install-3.1.0-3.1.0.19-1.x86_64.rpm | mxmaca-install | |
| mxompi-3.1.0-3.1.0.19-1.x86_64.rpm | mxompi | |
| mxreport-3.1.0-3.1.0.19-1.x86_64.rpm | mxreport | |
| mxsm1-devel-3.1.0-3.1.0.19-1.x86_64.rpm | mxsm1-devel | |
| mxucx-3.1.0-3.1.0.19-1.x86_64.rpm | mxucx | |
| mxvpu_3.1.0-3.1.0.19-1.x86_64.rpm | mxvpu | |
| mxvs-3.1.0-3.1.0.19-1.x86_64.rpm | mxvs | |
| sample_3.1.0-3.1.0.19-1.x86_64.rpm | sample | |
| vscode-clangd_3.1.0-3.1.0.19-1.x86_64.rpm | vscode-clangd |

表2：软件包内容清单

**备注：**

metax-driver是驱动包元信息，安装依赖metax-linux/mxfw/mxsmt。

mxgvm是虚拟化驱动包，安装依赖metax-linux。

### 附录二：沐曦曦云系列GPU应用程序系统架构

### 附录三：沐曦曦云C500、C550系列硬件适配列表

| 产品 | 适配CPU | 主推拓扑 | 已适配OEM/厂商 | 优势 |
|---|---|---|---|---|
C500 |
Intel | common | 浪潮信息、新华三、联想、超聚变、中兴、宁畅等 | 1. 架构通用：基于经典4U PCIe AI服务器形态，易于适配、安装、维护，量产机型已覆盖主流OEM厂商，在各类整机产品中可适用范围最广。 2. 拓扑先进：通过C500 4卡互连拓扑并支持4种PCIe服务器经典拓扑（common，balance，cascade，直通），适应各类训练计算场景。 3. 多元平台：支持Intel及海光、飞腾、鲲鹏等国内外主流CPU平台。 4. 成熟稳定：已实现大规模交付并在多个超大规模集群部署并稳定运行。 |
| 海光4号 | balance | 浪潮计算机、新华三、联想、中兴、中科可控等 | ||
| 飞腾S5000C | balance | 长城等 | ||
| 鲲鹏920 | cascade | 超聚变、华鲲振宇等 | ||
C550 |
Intel | balance | 浪潮信息、新华三、联想、超聚变、中兴等 | 1. 架构通用：基于经典6U/8U OAM AI服务器形态，兼容OAM 1.5/2.0标准，可将UBB+OAM作为整体与机头进行适配，量产机型已覆盖主流OEM厂商。 2. 拓扑先进：通过C550 8卡全互连拓扑实现896GB/s国内领先带宽卡间互连，为各类训练计算场景提供标准服务器单机最强性能。 3. 多元平台：支持Intel及海光、飞腾、鲲鹏等国内外主流CPU平台。 4. 成熟稳定：已实现大规模交付并在多个超大规模集群部署并稳定运行。 5. 液冷兼容：提供液冷形态模组与液冷OAM服务器适配，已实现液冷OAM集群大规模部署。 |