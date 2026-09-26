source: https://docs.mthreads.com/musa-sdk/version-5.2.0/install_guide

# 安装 MUSA SDK 5.2.0

本文档介绍如何在 Linux 平台安装 MUSA SDK 5.2.0，包括驱动程序 (Linux Driver)、MUSA 开发工具包 (MUSA Toolkit)、加速库 (muDNN 和 MCCL)，以及按需安装 Torch-MUSA、Triton-MUSA、TileLang-MUSA、MATE 等 Python 组件。文档提供在线安装（APT）和离线安装两种方式，其中在线安装需要先配置 Mthreads APT 软件源，再安装对应软件包。按照本文档完成操作后，您可以快速搭建可用的 MUSA 开发环境。

执行以下所有操作需要具备系统管理员 root 权限或使用 `sudo`

命令。

## 安装流程概览[](https://docs.mthreads.com#安装流程概览)

建议按以下顺序完成安装。下表列出了各步骤的作用及是否必需：

| 步骤 | 操作 | 说明 | 是否必需 |
|---|---|---|---|
| 1 | 下载安装包 | 选择在线或离线安装方式，并准备对应安装资源 | 是 |
| 2 | 安装驱动 | 安装 Linux Driver，提供 GPU 驱动和设备管理能力 | 是 |
| 3 | 安装 MUSA Toolkit | 安装编译器、运行时和基础开发工具链 | 是 |
| 4 | 安装 muDNN | 安装深度学习训练和推理所需的加速库 | 按需 |
| 5 | 安装 MCCL | 安装单机多卡和多机多卡通信组件 | 按需 |
| 6 | 安装 Python 包 | 按需安装 Torch-MUSA、Triton-MUSA、TileLang-MUSA、MATE 等 Python 包 | 按需 |
| 7 | 验证安装 | 验证基础开发环境和按需安装的组件是否生效 | 建议 |

根据您的开发目标，可按以下方式继续：

- 如果您只是进行 MUSA 程序开发，完成
**步骤 2**和**步骤 3**后即可开始编译和运行示例程序。 - 如果您希望使用容器环境，请先完成
**步骤 2**的宿主机驱动安装，再参见[Docker 镜像使用指南](https://docs.mthreads.com/musa-sdk/version-5.2.0/docker_guide)。 - 如果您涉及深度学习或多卡通信，请继续安装 muDNN 或 MCCL。
- 如果您还需要在 Python 环境中使用 Torch-MUSA、Triton-MUSA、TileLang-MUSA、MATE 等组件，请在完成基础环境安装后继续执行
**步骤 6**。

## 步骤 1：下载安装包[](https://docs.mthreads.com#步骤-1下载安装包)

MUSA SDK 提供在线安装和离线安装两种方式。您可以按照自己的习惯和环境条件进行选择，推荐优先使用在线安装（APT）。 下�表概述了两种安装方式的适用场景和说明：

| 安装方式 | 适用场景 | 说明 |
|---|---|---|
| 在线安装（APT） | 全新 Ubuntu 22.04 x86_64 Server 环境 | 通过 DEB 配置包自动配置 APT 软件源后直接安装 |
| 离线安装 | 受控环境、需要明确安装包版本 | 手动下载软件包并执行安装 |

使用在线安装（APT）前，建议先确认以下事项：

- APT 方式仅适用于上述全新 Ubuntu 22.04 x86_64 Server 环境。
- 如果系统中已经通过旧版 DEB、tar 包或其他方式安装过 Linux Driver 或 MUSA Toolkit，请先按原安装方式卸载干净，再执行在线安装流程。更多详情，参见
[历史版本](https://docs.mthreads.com/musa-sdk/version-5.1.0/install_guide)中的对应安装指导。

- 在线安装（APT）
- 离线安装

请按以下步骤，使用 DEB 配置包自动配置 APT 软件源：

-
下载配置包：

wget https://dl.mthreads.com/repo/repository/ubuntu2204/pool/jammy/amd64/musa-repo-jammy_1.0.0.11-1_all.deb -
安装配置包：

sudo dpkg -i musa-repo-jammy_1.0.0.11-1_all.deb -
更新本地缓存：

sudo apt update

更新缓存后，可通过 APT 直接安装以下组件：

| 组件 | 安装命令 |
|---|---|
| Linux Driver | `sudo apt install mthreads-driver` |
| MUSA Toolkit | `sudo apt install musa-toolkit` |
| muDNN | `sudo apt install mudnn` |
| MCCL（S5000 系列） | `sudo apt install mccl-s5000` |
| MCCL（S4000 系列） | `sudo apt install mccl-s4000` |

离线安装包通常应包含以下文件：

`├── MUSA SDK 5.2.0 发布说明.pdf`

├── MUSA_Programming_Guide_<version>.pdf

├── MT_Linux_Driver_5.2.0

│ └── musa_5.2.0-server_amd64.deb

├── MUSA_Toolkits_5.2.0

│ └── musa_toolkits_5.2.0.tar.gz

├── muDNN

│ └── mudnn.<version>.tar.gz

├── MCCL

│ └── mccl.<version>.tar.gz



## 步骤 2：安装驱动[](https://docs.mthreads.com#步骤-2安装驱动)

### 1. 确认资源需求[](https://docs.mthreads.com#1-确认资源需求)

- MT GPU 卡
- 操作系统：Ubuntu 22.04
- 内核版本：5.15.0-105-generic

集群内部机器无法直接在宿主机上安装 deb 包，请卸载 operator 相关组件后安装。

### 2. 配置 BIOS[](https://docs.mthreads.com#2-配置-bios)

-
**S4000 显卡**：如果使用的是内存 >=256G 的服务器，且显卡是 S4000，则必须**开启 IOMMU（VT-d）**选项 -
**S5000 显卡**：如果使用的显卡是 S5000，则必须**关闭 IOMMU (VT-d)**选项

#### 开启 IOMMU（Intel CPU）[](https://docs.mthreads.com#开启-iommuintel-cpu)

`# 如果 IOMMU 是关闭的，可通过如下步骤开启`

sudo sed -i 's/GRUB_CMDLINE_LINUX_DEFAULT="\(.*\)"/GRUB_CMDLINE_LINUX_DEFAULT="intel_iommu=on iommu.passthrough=0"/' /etc/default/grub

# 如果你的 CPU 是 AMD/HG，请改为 amd_iommu=on，而不是 intel_iommu=on

sudo update-grub

sudo reboot



#### 关闭 IOMMU（Intel CPU）[](https://docs.mthreads.com#关闭-iommuintel-cpu)

`# 如果 IOMMU 是开启的，可通过如下步骤关闭`

sudo sed -i 's/^GRUB_CMDLINE_LINUX_DEFAULT=.*/GRUB_CMDLINE_LINUX_DEFAULT="intel_iommu=off iommu=off iommu.passthrough=1 crashkernel=512M-:768M"/' /etc/default/grub

sudo update-grub

sudo reboot



#### 判断 IOMMU 当前状态[](https://docs.mthreads.com#判断-iommu-当前状态)

`sudo dmesg | grep -Ei "DMAR|IOMMU|VT-d|remapping"`



上述 `sed`

命令会清除系统上原有的 `quiet`

，以保证重启后 BMC 能看到图形界面。另外，请务必选择软重启，硬重启不能保证所有写入行为同步到文件。

**PC 配置**：如果是 PC，需要将 BIOS 中的`resize bar`

选项设置为 ON- 将显示器连接到主板上，并断开电源重新启动计算机。在启动过程中，按下
**Delete 键**以进入 BIOS 设置界面 - 在 BIOS 设置界面中，找到并开启
**Above 4G**选项 - 查找并将
**Resize Bar**开关置为 ON。请注意，大部分主板在首次开机时此选项默认为 OFF，并且通常显示在 BIOS 菜单的右上角 - 重启计算机，系统正常加载后，执行
`lspci -nn | grep 1ed5`

确认显卡已识别

- 将显示器连接到主板上，并断开电源重新启动计算机。在启动过程中，按下

### 3. 安装 MT 驱动[](https://docs.mthreads.com#3-安装-mt-驱动)

用于安装摩尔线程显卡的底层驱动程序。

-
**选择安装方式**- 在线安装（APT）
- 离线安装

完成 APT 配源后，可直接在线安装 Linux Driver。

-
**安装驱动**sudo apt install mthreads-driver -
**重启系统**强烈建议重启电脑来使驱动生效sudo reboot -
**如需在不重启的情况下重新加载驱动**sudo modprobe -rv mtgpusudo modprobe -v mtgpu

-
**确认环境依赖**# 查看 PCI 是否识别到显卡lspci -nn | grep 1ed5# 安装依赖包（若已安装请忽略）sudo apt install linux-headers-$(uname -r)sudo apt install linux-modules-$(uname -r)sudo apt install linux-modules-extra-$(uname -r)sudo apt install dkms -
**卸载驱动**# 卸载 old musa debsudo dpkg -P musasudo modprobe -rv mtgpu# 查询是否仍有 mtgpu ko 残留lsmod | grep mtgpu -
**安装驱动**安装 MT Linux Driver，以

`musa_5.2.0-server_amd64.deb`

包为例：注意：Linux Driver 版本与 MUSA Toolkit 版本独立，请根据硬件兼容性选择合适的 Linux Driver 版本。

sudo apt install ./musa_5.2.0-server_amd64.deb重启电脑来使驱动生效（强烈建议）：

sudo reboot如需在不重启的情况下重新加载驱动：

sudo modprobe -rv mtgpusudo modprobe -v mtgpu

提示执行

`sudo modprobe -rv mtgpu`

时，如提示`mtgpu is in use`

，请先执行`lsmod | grep mtgpu`

查看依赖关系，先卸载依赖`mtgpu`

的其他模块，再重新执行该命令；如仍无法卸载，请重启系统后重试。 -
**设置用户组**非 Root 用户如需获取设备使用权限，可参考以下方式设置：

# 把普通用户账号，加进 render & video groupsudo usermod -aG render,video ${USER}# 重新登入账户

### 4. 验证安装并查询版本[](https://docs.mthreads.com#4-验证安装并查询版本)

-
**使用 mthreads-gmi 验证**# 通过 mthreads-gmi 校验 Linux Driver 安装# 命令行执行 mthreads-gmi，能够展示 gmi 版本号、Driver 版本号、显卡相关主要信息等mthreads-gmi -
**查看版本信息**- 在线安装（APT）
- 离线安装

# 可通过包管理器或者 mthreads-gmi 工具查看驱动的版本信息dpkg -s mthreads-driver# 或者mthreads-gmi# 可通过包管理器或者 mthreads-gmi 工具查看驱动的版本信息dpkg -s musa# 或者mthreads-gmi

### 5. 配置其他选项[](https://docs.mthreads.com#5-配置其他选项)

**多卡环境，配置用户可见设备**

通过设置 `MUSA_VISIBLE_DEVICES`

环境变量来指定使用的显卡，如：

`export MUSA_VISIBLE_DEVICES=0,1,2,3`



指定前 4 张显卡可见。

**关闭开机自动加载 mtgpu.ko**

`# 在 /etc/modprobe.d/blacklist.conf 中设置`

echo "blacklist mtgpu" >> /etc/modprobe.d/blacklist.conf



## 步骤 3：安装 MUSA Toolkit[](https://docs.mthreads.com#步骤-3安装-musa-toolkit)

### 1. 确认前提条件[](https://docs.mthreads.com#1-确认前提条件)

已安装兼容版本 MT GPU 驱动。

-
检查 MT GPU 驱动版本：

mthreads-gmi -
若未安装或未安装适配版本 MT GPU 驱动，请先完成上一节的驱动安装与验证。


### 2. 安装 MUSA Toolkit[](https://docs.mthreads.com#2-安装-musa-toolkit)

MUSA Toolkit 包含了针对摩尔线程 GPU 进行通用计算开发的必要编译器和工具链，支持安装到主机（host）或 docker 环境中。

运行环境在 docker 上，建议通过 container-toolkit 创建容器，否则需要手动映射 host 上的 `/usr/lib/x86_64-linux-gnu/libmusa.so*`

到容器中。完整的镜像构建与容器开发步骤见 [Docker 镜像使用指南](https://docs.mthreads.com/musa-sdk/version-5.2.0/docker_guide)。

- 在线安装（APT）
- 离线安装

完成 APT 配源后，可直接在线安装 MUSA Toolkit。

`sudo apt install musa-toolkit`



-
**执行安装**先进入到安装包的下载目录下，然后依次执行：

# 以 musa_toolkits_5.2.0.tar.gz 为例tar -zxvf musa_toolkits_5.2.0.tar.gzcd musa_toolkits_installbash ./install.sh -u # 先卸载环境已安装的 musabash ./install.sh # 以上两条命令非 root 用户需要 sudo 提权执行正常安装完毕后，终端会输出如下提示：

Successfully installed MUSA in /usr/local/musaPlease export /usr/local/musa/bin to PATH in ~/.bashrcexport PATH=/usr/local/musa/bin:${PATH}Please export /usr/local/musa/lib to LD_LIBRARY_PATH in ~/.bashrcexport LD_LIBRARY_PATH=/usr/local/musa/lib:${LD_LIBRARY_PATH} -
**配置环境变量**-
文本编辑器打开用户终端配置文件：

vim ~/.bashrc -
在打开的配置文件末尾追加如下命令：

export MUSA_INSTALL_PATH=/usr/local/musaexport PATH=$MUSA_INSTALL_PATH/bin:$PATHexport LD_LIBRARY_PATH=$MUSA_INSTALL_PATH/lib:$LD_LIBRARY_PATH -
配置文件会在下次启动终端时生效。如果想立即在当前终端生效，请执行：

source ~/.bashrc

-

### 3. 验证安装[](https://docs.mthreads.com#3-验证安装)

验证 MUSA Toolkit 是否安装成功，运行以下命令：

`musa_version_query`



示例输出中的核心版本字段应与当前安装版本一致，例如：

`musa_toolkits:`

{

"version": "5.2.0",

...

}

mcc:

{

"version": "5.2.0",

...

}

musa_runtime:

{

"version": "5.2.0",

...

}



检查子模块是否正确包含以及数学库的架构是否正确。

**验证 musaInfo**：

`$ musaInfo`


compiler: mcc

--------------------------------------------------------------------------------

device# 0

Name: MTT S5000

Driver Version: 5.2

Runtime Version: 5.2

compute capability: 3.1

pciBusID: 0x2a

pciDeviceID: 0x0

pciDomainID: 0x0

multiProcessorCount: 56

maxThreadsPerMultiProcessor: 3072

isMultiGpuBoard: 1

clockRate: 1500 Mhz

memoryClockRate: 20000 Mhz

memoryBusWidth: 640

totalGlobalMem: 79.91 GB

sharedMemPerMultiprocessor: 192.00 KB

totalConstMem: 8192

sharedMemPerBlock: 192.00 KB

canMapHostMemory: 1

regsPerBlock: 131072

warpSize: 32

l2CacheSize: 62914560

computeMode: 0

maxThreadsPerBlock: 1024

maxThreadsDim.x: 1024

maxThreadsDim.y: 1024

maxThreadsDim.z: 1024

maxGridSize.x: 2147483647

maxGridSize.y: 2147483647

maxGridSize.z: 2147483647

concurrentKernels: 1

cooperativeLaunch: 1

cooperativeMultiDeviceLaunch: 0

isIntegrated: 0

maxTexture1D: 32768

maxTexture2D.width: 32768

maxTexture2D.height: 32768

maxTexture3D.width: 16384

maxTexture3D.height: 16384

maxTexture3D.depth: 2048

peers: device#1 device#2 device#3 device#4 device#5 device#6 device#7

non-peers: device#0

memInfo.total: 79.91 GB

memInfo.free: 79.32 GB (99%)



## 步骤 4：安装 muDNN[](https://docs.mthreads.com#步骤-4安装-mudnn)

### 1. 确认前提条件[](https://docs.mthreads.com#1-确认前提条件-1)

已安装兼容版本 MT GPU 驱动及 MUSA Toolkit。

### 2. 安装 muDNN[](https://docs.mthreads.com#2-安装-mudnn)

- 在线安装（APT）
- 离线安装

完成 APT 配源后，可按需选择以下方式之一安装 muDNN：

`# 默认方式，推荐`

sudo apt install mudnn


# 如需锁定到 MUSA 5 大版本

sudo apt install libmudnn3-musa-5



`mudnn`

是默认推荐入口，适合需要后续持续升级的场景。

`libmudnn3-musa-5`

会固定到 MUSA 5 大版本，适合需要锁定版本范围的场景；后续执行 `apt upgrade`

时，可能无法直接升级到更新版本。

-
**执行安装**# 以 mudnn.3.3.0.PH1.tar.gz 为例tar -zxvf mudnn.3.3.0.PH1.tar.gzcd mudnn && ./install_mudnn.sh -i -
**配置环境变量**DNN_PATH=$(realpath mudnn)export LD_LIBRARY_PATH=${DNN_PATH}/lib:$LD_LIBRARY_PATH

安装完成后，您可以查看 muDNN 的所有 API。

更多接口说明和使用示例，可参考 [muDNN](https://docs.mthreads.com/musa-sdk/version-5.2.0/07_libraries/03_muDNN/)。

## 步骤 5：安装 MCCL[](https://docs.mthreads.com#步骤-5安装-mccl)

### 1. 确认前置条件[](https://docs.mthreads.com#1-确认前置条件)

- 多张 MT GPU 卡（单节点/多节点）
- 一块或多块 InfiniBand 网卡
- 已安装 MUSA 驱动
- 已安装 MUSA Toolkit
- 已安装 mtml（容器内部直接安装 mtml 或者通过 host 端映射，若是通过 container-toolkit 方式起的容器，会直接映射进去）

### 2. 配置网络[](https://docs.mthreads.com#2-配置网络)

如果没有 IB 网卡，只有以太网，则无需配置 IB。PH1 架构走的 RoCE 网络，需要使用环境变量指定 RoCE v2 协议（`MCCL_IB_GID_INDEX=3`

）

#### 2.1 安装 IB 驱动[](https://docs.mthreads.com#21-安装-ib-驱动)

如果有 IB 网卡，但是 IB 驱动未安装，请先安装 IB 驱动。

#### 2.2 验证 IB 驱动[](https://docs.mthreads.com#22-验证-ib-驱动)

`$ ibstat`


CA 'mlx5_0'

CA type: MT4123

Number of ports: 1

Firmware version: 20.31.1014

Hardware version: 0

Node GUID: 0xb83fd203005682a2

System image GUID: 0xb83fd203005682a2

Port 1:

State: Active

Physical state: LinkUp

Rate: 200

Base lid: 12

LMC: 0

SM lid: 5

Capability mask: 0x2651e848

Port GUID: 0xb83fd203005682a2

Link layer: InfiniBand



如果其中一个 network port 的 physical state 是 **LinkUp**，而且 Link layer 标明为 **InfiniBand**，就说明已经使能了 IB 网络。

### 3. 安装 MPI 工具[](https://docs.mthreads.com#3-安装-mpi-工具)

MPI 工具为 MCCL 提供跨节点的进程管理和通信基础，协调不同机器间的初始连接。多机场景下需要安装 MPI 工具。

**选项 1：mpich 工具安装**（mpich-4.2.0rc3 版本）

`wget https://www.mpich.org/static/downloads/4.2.0rc3/mpich-4.2.0rc3.tar.gz`

tar -xzf mpich-4.2.0rc3.tar.gz

cd mpich-4.2.0rc3


# 若已经执行过 ./configure，需要执行 make clean 清除

make clean

./configure --with-device=ch3:sock

make -j64

sudo make install


# 验证，mpich 工具默认装在/usr/local/bin 路径

export PATH=/usr/local/bin:$PATH

mpirun --version



**选项 2：openMPI 工具安装**

`# 查看可用 openmpi 版本`

apt list -a openmpi-bin


# 安装 openMPI（建议使用 4.1.x 版本，此处以 4.1.2 版本为例）

wget https://www.open-mpi.org/software/ompi/v4.1/downloads/openmpi-4.1.2.tar.bz2

tar -jxf openmpi-4.1.2.tar.bz2

cd openmpi-4.1.2

./configure --prefix=/usr/local/openmpi --without-hcoll --without-ucx

make -j4 all

make install


# 验证，openmpi 工具手动安装统一装在/usr/local/openmpi 路径

export PATH=/usr/local/openmpi/bin/:$PATH

mpirun --version



### 4. 安装 MCCL[](https://docs.mthreads.com#4-安装-mccl)

- 在线安装（APT）
- 离线安装

完成 APT 配源后，根据显卡型号选择对应软件包：

`# S5000 系列显卡`

sudo apt install mccl-s5000


# S4000 系列显卡

sudo apt install mccl-s4000



安装 MCCL 包，以 `mccl.2.3.0.PH1.tar.gz`

为例：

`sudo tar -zxvf mccl.2.3.0.PH1.tar.gz`

cd ./mccl

sudo bash ./install.sh



更多接口说明和使用示例，可参考 [MCCL](https://docs.mthreads.com/musa-sdk/version-5.2.0/07_libraries/04_mccl/)。

## 步骤 6：安装 Python 包（按需）[](https://docs.mthreads.com#步骤-6安装-python-包按需)

### 1. 确认前置条件[](https://docs.mthreads.com#1-确认前置条件-1)

- 已完成 Linux Driver 和 MUSA Toolkit 安装。
- 已切换到目标 Python 环境，例如
`virtualenv`

、`conda`

或系统 Python。 - 当前外部 PyPI 源主要覆盖
`x86_64`

平台，以及 Python`3.10`

/`3.12`

环境。

### 2. 配置 PyPI 源[](https://docs.mthreads.com#2-配置-pypi-源)

如果您需要在 MUSA SDK 5.2.0 环境中使用 Torch-MUSA、Triton-MUSA、TileLang-MUSA、MATE 等 Python 组件，可通过以下��外部 PyPI 源安装：

`https://dl.mthreads.com/repo/api/pypi/pypi/simple`



您可以按需选择以下方式进行配置：

- 方式一：临时生效
- 方式二：写入配置
- 方式三：安装时指定

`export PIP_INDEX_URL=https://dl.mthreads.com/repo/api/pypi/pypi/simple`



`python -m pip config set global.index-url \`

https://dl.mthreads.com/repo/api/pypi/pypi/simple



如需查看当前配置：

`python -m pip config list`



`python -m pip install <package> \`

--index-url https://dl.mthreads.com/repo/api/pypi/pypi/simple



不要把 MUSA PyPI 源和公开 PyPI 镜像源混在同一次 `pip install`

中。需要安装普通第三方依赖时，请单独切换到对应的公开源安装。

### 3. 查询可用版本[](https://docs.mthreads.com#3-查询可用版本)

安装前，建议先查询目标包在外部 PyPI 源中的可用版本：

`python -m pip index versions <package> \`

--index-url https://dl.mthreads.com/repo/api/pypi/pypi/simple



例如：

`python -m pip index versions torch_musa \`

--index-url https://dl.mthreads.com/repo/api/pypi/pypi/simple

python -m pip index versions triton \

--index-url https://dl.mthreads.com/repo/api/pypi/pypi/simple

python -m pip index versions tilelang_musa \

--index-url https://dl.mthreads.com/repo/api/pypi/pypi/simple

python -m pip index versions mate \

--index-url https://dl.mthreads.com/repo/api/pypi/pypi/simple



如果当前 `pip`

版本不支持 `pip index versions`

，请先升级 `pip`

。

### 4. 安装常用 Python 包[](https://docs.mthreads.com#4-安装常用-python-包)

请按实际需要选择安装对应 Python 包，通常无需一次性安装全部组件。

#### Torch-MUSA（`torch`

/ `torch_musa`

）[](https://docs.mthreads.com#torch-musatorch--torch_musa)

`python -m pip install torch==2.9.1 torch_musa==2.9.1`



请确保 `torch`

与 `torch_musa`

的版本、Python tag 和平台 tag 相互匹配。

更多安装和使用说明，可参考 [Torch-MUSA](https://docs.mthreads.com/torchmusa/torchmusa-doc-online/install_guide)。

#### LiteCCL Ops（`liteccl_ops`

）[](https://docs.mthreads.com#liteccl-opsliteccl_ops)

`python -m pip install liteccl_ops==1.0.0`



`liteccl_ops`

是 LiteCCL 的 Python 扩展包。

#### Triton-MUSA（`triton`

）[](https://docs.mthreads.com#triton-musatriton)

`python -m pip uninstall -y triton`

python -m pip install triton



`triton_musa`

仓库发布到 PyPI 后的包名是 `triton`

。

如需指定 `triton`

版本，可选择：

`python -m pip install triton==3.2.0`

python -m pip install triton==3.6.0



安装完成后通过 `import triton`

使用。更多接口说明和使用示例，可参考 [Triton-MUSA](https://docs.mthreads.com/musa-sdk/version-5.2.0/libraries/openlibs/kernel_dsl_compiler_stack/triton)。

#### TileLang-MUSA（`tilelang_musa`

）[](https://docs.mthreads.com#tilelang-musatilelang_musa)

`python -m pip install 'tilelang_musa==0.1.8+musa.3'`



以下示例统一使用 `tilelang_musa`

作为包名。

更多接口说明和使用示例，可参考 [TileLang-MUSA](https://docs.mthreads.com/musa-sdk/version-5.2.0/libraries/openlibs/kernel_dsl_compiler_stack/tilelang)。

#### MATE（`mate`

）[](https://docs.mthreads.com#matemate)

`python -m pip install mate==0.2.3`



如需同仓库 wrapper 包，或查看更多接口说明和使用示例，可参考 [MATE](https://mate-docs.mthreads.com/latest/)。

#### Apache TVM FFI（`apache-tvm-ffi`

）[](https://docs.mthreads.com#apache-tvm-ffiapache-tvm-ffi)

`python -m pip install 'apache-tvm-ffi==0.1.9.post3+musa.1'`



如需安装 Torch DLPack 扩展包，可继续执行：

`python -m pip install 'torch-c-dlpack-ext==0.1.5+musa5.2.0torch2.9.1'`



某些 Python 包还会依赖额外的运行时组件或产品级配置；如需继续验证功能，请以对应产品文档为准。

## 步�骤 7：验证安装[](https://docs.mthreads.com#步骤-7验证安装)

建议先完成基础开发环境验证，再根据实际安装的可选组件继续验证。

如果您只安装了 Linux Driver 和 MUSA Toolkit，确认 `mthreads-gmi`

、`musa_version_query`

和 `musaInfo`

输出正常即可。

### 1. 验证 MCCL（按需）[](https://docs.mthreads.com#1-验证-mccl按需)

以下多机配置和通信验证仅在安装 MCCL 时需要。

-
**确认版本**export LD_LIBRARY_PATH=/usr/local/musa/lib:$LD_LIBRARY_PATH/usr/local/musa/bin/mccl_version -
**多机 config 文件配置**（2 节点为例）-
mpich 配置文件：

`hostfile_with_mpich`

<node1_ip>:<process_num><node2_ip>:<process_num> -
openmpi 配置文件：

`hostfile_with_openmpi`

<node1_ip> slots=process_num<node2_ip> slots=process_num

-
-
**功能验证**# 单机验证./all_reduce_perf -b 1M -e 1024M -f 2 -g 1# 多机验证（openmpi）mpirun --allow-run-as-root --mca btl_tcp_if_include bond0 -hostfile ./hostfile_with_openmpi \-x LD_LIBRARY_PATH=/usr/local/musa/lib:/usr/local/lib \-x MCCL_PROTOS=2 -x MCCL_NET_SHARED_BUFFERS=0 \-x MCCL_ALGOS=1 -x MCCL_IB_GID_INDEX=3 \./all_reduce_perf -b 1M -e 1024M -f 2 -g 1# 多机验证（mpich）mpirun -hostfile ./hostfile_with_mpich \-env LD_LIBRARY_PATH=/usr/local/musa/lib:/usr/local/lib \-env MCCL_PROTOS=2 -env MCCL_NET_SHARED_BUFFERS=0 \-env MCCL_ALGOS=1 -env MCCL_IB_GID_INDEX=3 \./all_reduce_perf -b 1M -e 1024M -f 2 -g 1

### 2. 验证 Python 包（按需）[](https://docs.mthreads.com#2-验证-python-包按需)

如�果您已经安装 Torch-MUSA、Triton-MUSA、TileLang-MUSA 或 MATE，可先执行以下基础验证：

`python - <<'PY'`

import torch

import torch_musa

print("torch:", torch.__version__)

print("torch_musa:", torch_musa.__version__)

print("musa available:", torch.musa.is_available())

PY



`python -m pip show triton`



`python - <<'PY'`

import triton

print("triton:", triton.__version__)

PY



`python - <<'PY'`

import tilelang

print("tilelang import ok")

PY



`python - <<'PY'`

import mate

print("mate import ok")

PY



## 卸载 MUSA[](https://docs.mthreads.com#卸载-musa)

如需卸载 MUSA SDK 及相关组件，请根据实际安装方式执行对应操作。

- 在线安装（APT）
- 离线安装

`# 按需移除已安装的可选组件`

# 根据显卡型号选择其一

# S5000 系列显卡

sudo apt remove mccl-s5000


# S4000 系列显卡

sudo apt remove mccl-s4000


# muDNN

sudo apt remove mudnn


# 如安装的是锁定 MUSA 5 大版本的包，按需移除

sudo apt remove libmudnn3-musa-5


# 基础组件

sudo apt remove musa-toolkit

sudo apt remove mthreads-driver


# 清�理 APT 自动安装的依赖

sudo apt autoremove


# 如需立即完成驱动卸载，建议重启系统

sudo reboot



`# 卸载 MUSA deb 包`

sudo dpkg -P musa


# 移除 mtgpu 内核模块

sudo modprobe -rv mtgpu


# 查询是否仍有 mtgpu ko 残留

lsmod | grep mtgpu



- 若
`sudo modprobe -rv mtgpu`

提示`mtgpu is in use`

，请先执行`lsmod | grep mtgpu`

查看依赖关系，先卸载依赖`mtgpu`

的其他模块，再重新执行该命令；如仍无法卸载，请重启系统后重试 - 对于在线安装（APT），
`apt remove`

不会自动清理所有依赖，建议继续执行`sudo apt autoremove`

- 如需清理 MUSA Toolkit，删除
`/usr/local/musa`

目录即可：`sudo rm -rf /usr/local/musa`

- 请手动编辑
`~/.bashrc`

文件，移除 MUSA 相关的环境变量设置

## 常见问题[](https://docs.mthreads.com#常见问题)

## Q1: 配置 APT 软件源后，执行 `sudo apt update`

失败怎么办？

- 确认当前环境为全新 Ubuntu 22.04 x86_64 Server。
- 确认系统可以正常访问软件源地址
`https://dl.mthreads.com/`

。 - 确认 DEB 配置包已安装成功后，再重新执行
`sudo apt update`

：

`dpkg -l | grep musa-repo-jammy`

sudo apt update



## Q2: 已完成配源，但 `apt install`

提示找不到软件包怎么办？

- 先执行
`sudo apt update`

更新本地缓存。 - 确认当前环境在 APT 方式支持范围内。
- 可使用以下命令检查软件包是否已出现在 APT 缓存中：

`apt search mthreads-driver`

apt search musa-toolkit

apt search mudnn

apt search libmudnn3-musa-5



## Q3: 系统中已安装旧版 Linux Driver 或 MUSA Toolkit，在线安装报冲突怎么办？

如果系统中已经通过�旧版 DEB、tar 包或其他方式安装过 Linux Driver 或 MUSA Toolkit，请先按原安装方式卸载干净，再重新执行在线安装流程。更多详情，参见[历史版本](https://docs.mthreads.com/musa-sdk/version-5.1.0/install_guide)中的对应安装指导。

## Q4: 为什么执行 `apt remove`

后仍有依赖包残留？

`apt remove`

默认只移除指定软件包，不会自动清理所有依赖。对于在线安装（APT），建议继续执行以下命令清理自动安装的依赖：

`sudo apt autoremove`



## Q5: 驱动安装后无法识别设备

`# 检查 PCI 识别`

lspci -nn | grep 1ed5


# 检查驱动加载

lsmod | grep mtgpu


# 重新加载驱动

sudo modprobe -rv mtgpu

sudo modprobe -v mtgpu



若重载时提示 `mtgpu is in use`

，请先执行 `lsmod | grep mtgpu`

检查依赖关系，先卸载依赖 `mtgpu`

的其他模块，再重新执行相关命令。

## Q6: IOMMU 配置问题

- S4000 显卡：必须开启 IOMMU。Intel CPU 使用
`intel_iommu=on iommu.passthrough=0`

，AMD/HG CPU 使用`amd_iommu=on`

- S5000 显卡：必须关闭 IOMMU。Intel CPU 可参考前文的
[关闭 IOMMU 步骤](https://docs.mthreads.com#disable-iommu-intel)

## Q7: 权限不足

`# 将用户添加到 render 和 video 组`

sudo usermod -aG render,video ${USER}

# 重新登录



## Q8: Docker 环境中使用 MUSA

- 推荐使用官方分层镜像进行开发和运行，完整步骤见
[Docker 镜像使用指南](https://docs.mthreads.com/musa-sdk/version-5.2.0/docker_guide) - 使用 container-toolkit 创建容器（推荐）
- 或手动映射
`/usr/lib/x86_64-linux-gnu/libmusa.so*`

到容器中