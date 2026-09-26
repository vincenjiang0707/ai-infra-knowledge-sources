source: https://docs.mthreads.com/vgpu/version-2.9.2/vgpu-doc-online/install_guide

# 用户指南

本文面向系统管理员和运维人员，介绍 MT vGPU 的安装配置、虚拟 GPU 管理、状态监控、驱动维护，以及热迁移、休眠恢复和超分等高级功能的使用方法。

## 安装和配置 MT vGPU[](https://docs.mthreads.com#安装和配置-mt-vgpu)

### 步骤 1：确认驱动软件包[](https://docs.mthreads.com#步骤-1确认驱动软件包)

| 软件包名称 | 软件包描述 |
|---|---|
| MT_vGPU_HOST_DKMS_v2.9.2 | 适用 DKMS 的 deb 包和 rpm 包，Host 端使用，驱动 GPU，可将物理 GPU 切分成多个虚拟 GPU（vGPU），并发支持多个虚拟机使用。 |
| MT_vGPU_WINDOWS_GUEST_v2.9.2 | GPU Windows Guest 驱动安装包，Guest 端使用。 |
| MT_vGPU_LINUX_GUEST_v2.9.2 | GPU Linux Guest 驱动安装包，Guest 端使用。 |
| MT_vGPU_GMI_v2.9.2 | 摩尔线程 GPU 管理工具使用手册。 |
| MT_vGPU_MTML_v2.9.2 | GPU 管理函数库。 |
| MT_vGPU_DirectStream_v2.9.2 | 屏幕抓取及 GPU 硬件编码 SDK，在 Windows Guest 中工作，调用 GPU 的硬件能力对数据进行编码。 |
| MT_vGPU_MTAPI_v2.9.2 | virtual display、自定义分辨率等设置工具，Guest 端使用。 |
| MT_vGPU_DCGM_v2.9.2 | GPU 健康状态检查工具，Host 端使用。 |

驱动获取请联系：[developers@mthreads.com](mailto:developers@mthreads.com)。

### 步骤 2：准备安装环境[](https://docs.mthreads.com#步骤-2准备安装环境)

#### 1. 设置服务器 BIOS[](https://docs.mthreads.com#1-设置服务器-bios)

-
超 4G 地址空间译码：开启；详细设置方法参考对应服务器操作手册。

-
VMX（Intel）/ SVM（AMD）：开启；详细设置方法参考对应服务器操作手册。

-
Intel VT-d（IOMMU）：开启；详细设置方法参考对应服务器操作手册。

-
SR-IOV：开启；详细设置方法参考对应服务器操作手册。

注：如果 BIOS 有 ARIForwarding 配置项，需要将其开启。


#### 2. 设置操作系统[](https://docs.mthreads.com#2-设置操作系统)

##### 1. 更新 GRUB 配置[](https://docs.mthreads.com#1-更新-grub-配置)

更新操作系统 GRUB 文件，开启 IOMMU。以 Intel 服务器为例，在 `/etc/default/grub`

中添加 `intel_iommu=on`

：

`GRUB_CMDLINE_LINUX="...... intel_iommu=on"`



##### 2. 生成 GRUB 配置[](https://docs.mthreads.com#2-生成-grub-配置)

根据当前操作系统手动更新 GRUB 配置：

`grub2-mkconfig -o /boot/efi/EFI/$(vendor)/grub.cfg`



`-o`

目录需要根据当前系统实际启动方式（UEFI/Legacy）修改，Legacy 启动时为 `/boot/grub2/grub.cfg`

。

更新后重启服务器。

##### 3. 确认 IOMMU 已开启[](https://docs.mthreads.com#3-确认-iommu-已开启)

服务器重启后，确认 IOMMU 已开启。

可通过如下命令确认启动参数已生效：

`$ cat /proc/cmdline | grep -E "intel_iommu=on|amd_iommu=on"`



可通过如下命令确认系统已创建 IOMMU 分组：

`$ ls /sys/kernel/iommu_groups/`



若命令返回多个数字编号目录，表示系统已识别 IOMMU 分组。 也可通过如下命令查看内核 IOMMU 初始化日志：

`$ dmesg | grep -Ei "DMAR|IOMMU|vgpu mm"`

[ 8.011691] perf/amd_iommu: Detected AMD IOMMU #7 (2 banks, 4 counters/bank).

[ 8.496306] intel_iommu=on

[ 12.488279] vgpu mm iommu mode: ENABLE

[ 12.488281] vgpu mm iommu mapping mode: 2



#### 3. 查询 PCIe 设备基本信息[](https://docs.mthreads.com#3-查询-pcie-设备基本信息)

-
为确保服务器和操作系统已经识别 MTT S 系列 GPU，在 Host 操作系统中输入

`lspci -d 1ed5:`

命令查询设备 ID。# MTT S3000$ lspci -d 1ed5:03:00.0 3D controller: Moore Threads Technology Co.,Ltd MTT S300003:00.1 Multimedia audio controller: Moore Threads Technology Co.,Ltd MTT HDMI/DP Audio正常情况下，对应显卡的显示内容应该如上所示。


### 步骤 3：安装并验证 Host 驱动[](https://docs.mthreads.com#步骤-3安装并验证-host-驱动)

Host 驱动分为 GOLDEN 和 DKMS 两种驱动，DKMS 驱动所有用户都可以安装，GOLDEN 驱动为针对某个内核版本的定制驱动，二者功能无差异，选择其一即可。

#### 1. 安装 DKMS 通用驱动[](https://docs.mthreads.com#1-安装-dkms-通用驱动)

`$ rpm -ivh ~/xxx_xxx_dkms_mtvgpu_2.9.2_amd64.rpm`

Verifying... ################################# [100%]

Preparing... ################################# [100%]

Updating / installing...

1:mtvgpu-2.9.2-1 ################################# [100%]

Loading new mtgpu-2.9.2-000 DKMS files...

Building for 4.18.0-193.14.2.el8_2.x86_64

Building initial module for 4.18.0-193.14.2.el8_2.x86_64

Done.


mtgpu.ko.xz:

Running module version sanity check.


Running the pre_install script:


- Original module

- No original module exists within this kernel

- Installation

- Installing to /lib/modules/4.18.0-193.14.2.el8_2.x86_64/kernel/drivers/gpu/drm/mthreads/


Running the post_install script:


depmod....


DKMS: install completed.

Starting postinst...


postinst finished.



注：DKMS 驱动需要先安装 DKMS 工具。


#### 2. 确认内核模块已加载[](https://docs.mthreads.com#2-确认内核模块已加载)

列出当前加载的 vGPU 相关内核模块，确认 `mtgpu`

相关模块已加载。

`$ lsmod | grep "mtgpu"`

mtgpu 4530176 0

mtvgpu_basic 81920 1 mtgpu

drm_display_helper 237568 1 mtgpu

vfio 73728 3 mtgpu,vfio_iommu_type1,mtvgpu_basic

kvm 1380352 2 mtgpu,kvm_intel

drm_kms_helper 270336 2 mtgpu,drm_display_helper

drm 811008 5 mtgpu,drm_kms_helper,drm_shmem_helper,drm_display_helper



看到上述内容表示内核驱动已经加载。

#### 3. 确认内核驱动工作正常[](https://docs.mthreads.com#3-确认内核驱动工作正常)

使用摩尔线程 GPU 管理工具 `mthreads-gmi`

确认内核驱动模块已经工作。

`$ mthreads-gmi -cf`

Wed Jul 31 03:13:00 2024

---------------------------------------------------------------

mthreads-gmi:2.3.4 Driver Version:2.9.2-000

---------------------------------------------------------------

ID Name |PCIe |%GPU Mem

Device Type |Pcie Lane Width |Temp MPC Capable

| ECC Mode

+-------------------------------------------------------------+

0 MTT S3000 |00000000:5e:00.0 |58% 30094MiB(32768MiB)

MPC Parent |16x(16x) |57C YES

| N/A

---------------------------------------------------------------



### 步骤 4：切分 vGPU[](https://docs.mthreads.com#步骤-4切分-vgpu)

vGPU 切分支持两种方式：

- mdevctl 方式。
- 设备文件方式。

两种方式的本质都是对设备文件进行操作以达到对 vGPU 设备管理的目的。更多关于 MT vGPU 支持的显卡切分类型，请参见 [MTT S 系列显卡支持的 vGPU 性能和参数](https://docs.mthreads.com#mtt-s-%E7%B3%BB%E5%88%97%E6%98%BE%E5%8D%A1%E6%94%AF%E6%8C%81%E7%9A%84-vgpu-%E6%80%A7%E8%83%BD%E5%92%8C%E5%8F%82%E6%95%B0)。

#### mdevctl 方式[](https://docs.mthreads.com#mdevctl-方式)

##### 1. 查看 GPU PCI 设备 BDF 地址[](https://docs.mthreads.com#1-查看-gpu-pci-设备-bdf-地址)

`$ lspci -d 1ed5:`

03:00.0 3D controller: Moore Threads Technology Co.,Ltd MTT S3000



`03:00.0`

为 GPU 的 BDF 地址。

`$ virsh nodedev-list --cap pci| grep 03_00_0`

pci_0000_03_00_0



完整的标识地址为 `0000:03:00.0`

。

##### 2. 创建 vGPU[](https://docs.mthreads.com#2-创建-vgpu)

`$ mdevctl start -u c4f702ca-c69d-4d7d-a526-5fdcf78d3428 -p 0000:03:00.0 --type mtgpu-1101`



`c4f702ca-c69d-4d7d-a526-5fdcf78d3428`

是 UUID，是 vGPU 设备的唯一标识；此 ID 可以是固定的 ID，也可以通过 uuidgen 工具生成：`uuidgen`

=> xxxxxxx。`-p`

GPU PCI 设备的 BDF 地址。`--type`

：vGPU 切分类型。

##### 3. 查看创建的 vGPU 设备[](https://docs.mthreads.com#3-查看创建的-vgpu-设备)

`$ mdevctl list`

c4f702ca-c69d-4d7d-a526-5fdcf78d3428 0000:03:00.0 mtgpu-1101



#### 设备文件方式[](https://docs.mthreads.com#设备文件方式)

##### 1. 定位 mdev 设备文件[](https://docs.mthreads.com#1-定位-mdev-设备文件)

`$ find /sys/ -name mdev_supported_types`

/sys/devices/pci0000:00/0000:00:01.0/0000:01:00.0/0000:02:00.0/0000:03:00.0/mdev_supported_types


$ echo c4f702ca-c69d-4d7d-a526-5fdcf78d3428 > /sys/devices/pci0000:00/0000:00:01.0/0000:01:00.0/0000:02:00.0/0000:03:00.0/mdev_supported_types/mtgpu-1101/create



设备文件实际地址可�按照这种方式定位：

`/sys/class/mdev_bus/domain\:bus\:slot.function/mdev_supported_types/`

。以上面的地址`0000:03:00.0`

为例，domain 为`0000`

、bus 为`03`

、slot 为`00`

、function 为`0`

。

##### 2. 查看切分出的 vGPU 设备[](https://docs.mthreads.com#2-查看切分出的-vgpu-设备)

`$ ls /sys/bus/mdev/devices/`

c4f702ca-c69d-4d7d-a526-5fdcf78d3428



### 步骤 5：创建带有 MT vGPU 的虚拟机[](https://docs.mthreads.com#步骤-5创建带有-mt-vgpu-的虚拟机)

#### QEMU 命令行[](https://docs.mthreads.com#qemu-命令行)

##### 1. 使用 QEMU 命令创建虚拟机[](https://docs.mthreads.com#1-使用-qemu-命令创建虚拟机)

使用 QEMU 命令行的参考命令如下：

`$ qemu-kvm -name 'Moore Threads GPU' \`

-machine q35,accel=kvm,usb=on \

-cpu host -smp 4,sockets=1 -m 4G \

-hda win10-vdi-snapshot.qcow2 \

-usb -device usb-tablet \

-device vfio-pci,sysfsdev=/sys/bus/mdev/devices/c4f702ca-c69d-4d7d-a526-5fdcf78d3428 \

-vnc :01 \

-net user -net nic \

-device intel-hda \

-device hda-duplex



其中，`-device vfio-pci,sysfsdev=/sys/bus/mdev/devices/c4f702ca-c69d-4d7d-a526-5fdcf78d3428`

为增加的 vGPU 的参数。

#### virsh XML[](https://docs.mthreads.com#virsh-xml)

##### 1. 在虚拟机 XML 配置中添加 vGPU 设备[](https://docs.mthreads.com#1-在虚拟机-xml-配置中添加-vgpu-设备)

在虚拟机的 XML 配置文件中添加如下配置：

`<hostdev mode='subsystem' type='mdev' managed='no' model='vfio-pci'>`

<source>

<address uuid='c4f702ca-c69d-4d7d-a526-5fdcf78d3428'/>

</source>

</hostdev>



##### 2. 启动虚拟机[](https://docs.mthreads.com#2-启动虚拟机)

`$ virsh create vm.xml`



### 步骤 6：安装 Guest 端显卡驱动[](https://docs.mthreads.com#步骤-6安装-guest-端显卡驱动)

vGPU 需要安装 Guest 驱动才能作为 3D 加速设备进行工作。

#### Windows[](https://docs.mthreads.com#windows)

未安装摩尔线程 Windows 驱动的 vGPU 设备如下图所示：

**使用 MT_vGPU_WINDOWS_GUEST 安装包安装方法如下：**

在虚拟机中，运行 PES 安装包 musa-desktop-win10-64bit_vdi.exe，安装 Windows 10 vGPU 驱动：

安装成功，如下图所示：

安装完成后重启虚拟机，并在 **设备管理器** > **显示适配器** 中确认摩尔线程 vGPU 设备显示正常、�无黄色感叹号，即可正常使用 vGPU 加速。

#### Linux[](https://docs.mthreads.com#linux)

未安装摩尔线程 Linux 驱动的 vGPU 设备如下图所示：

**使用 MT_vGPU_LINUX_GUEST 安装包安装方法如下：**

在虚拟机中，运行 musa_2.9.x-release-amd64.deb 安装包，安装 Linux Guest vGPU 驱动。

说明：以下 Linux Guest 安装界面截图中的版本号仅作示意，可能与当前发布的安装包版本不一致，请以实际安装包版本为准。


安装成功，如下图所示：

安装完成后重启虚拟机。

重启后，可通过如下命令确认 Guest 驱动工作正常：

`$ mthreads-gmi`

Mon Jun 9 06:31:58 2025

----------------------------------------------------------------------

mthreads-gmi:2.3.4 Driver Version:2.9.2

----------------------------------------------------------------------

ID Name |PCIe |%GPU Mem

Device Type |Pcie Lane Width |

+--------------------------------------------------------------------+

0 MTT S3000 MtvGPU-1101 |00000000:00:0d.0 |0% 0MiB(1024MiB)

Virtual |16x(16x) |

----------------------------------------------------------------------



若系统包含图形桌面，也可进一步确认虚拟显示已经正常创建。

## 管理 MT vGPU[](https://docs.mthreads.com#管理-mt-vgpu)

### 查询 vGPU[](https://docs.mthreads.com#查询-vgpu)

#### mdevctl 方式[](https://docs.mthreads.com#mdevctl-方式-1)

`$ mdevctl list`

c4f702ca-c69d-4d7d-a526-5fdcf78d3428 0000:03:00.0 mtgpu-1101



#### 设备文件方式[](https://docs.mthreads.com#设备文件方式-1)

`$ ls /sys/bus/mdev/devices/`

c4f702ca-c69d-4d7d-a526-5fdcf78d3428



### 删除 vGPU[](https://docs.mthreads.com#删除-vgpu)

#### mdevctl 方式[](https://docs.mthreads.com#mdevctl-方式-2)

`$ mdevctl stop -u c4f702ca-c69d-4d7d-a526-5fdcf78d3428`



#### 设备文件方式[](https://docs.mthreads.com#设备文件方式-2)

`$ echo 1 > /sys/bus/mdev/devices/c4f702ca-c69d-4d7d-a526-5fdcf78d3428/remove`



### 配置调度方式[](https://docs.mthreads.com#配置调度方式)

摩尔线程的 vGPU 支持两种调度方式：性能最优调度方式和时间切片调度方式。

注意：默认配置为性能最优调度方式。


| 调度方式 | 参数值 | 说明 |
|---|---|---|
| 性能最优调度方式（Best-effort scheduling） | `0` | 跨多个 vGPU 来平衡性能。每个 vGPU 独占整个 GPU 处理周期，当前周期完成后其他 vGPU 才会继续使用。在某些极端场景下，某个 vGPU 渲染任务多且重，可能导致其他 vGPU 无法获得时间片。 |
| 时间切片调度方式（Time-sliced scheduling） | `1` | 激活的 vGPU 会等分当前 GPU 的算力，即 equal share mode。 |

#### 步骤 1：创建调度配置文件[](https://docs.mthreads.com#步骤-1创建调度配置文件)

调度方式通过安装驱动时进行修改。

在 `/etc/modprobe.d`

目录下创建 `mtgpu.conf`

文件。

#### 步骤 2：设置调度策略[](https://docs.mthreads.com#步骤-2设置调度策略)

在配置文件中，通过参数 `mtgpu_vgpu_scheduling_policy`

选择调度方式。

参考如下配置：

`options mtgpu mtgpu_vgpu_scheduling_policy=0`



说明：如果选择了 Time Sliced Scheduling，

`mtgpu_vgpu_time_sliced_value`

的值会决定时分复用的时间，以毫秒为单位。

#### 步骤 3：重新加载驱动[](https://docs.mthreads.com#步骤-3重新加载驱动)

重新加载 mtgpu 驱动或重启服务器，使配置生效。

### 限制最大分辨�率[](https://docs.mthreads.com#限制最大分辨率)

mtgpu-1101 类型默认可以支持 4K 显示，由于 4K 对 GPU 资源消耗较多，并发时可能会影响其他用户的体验，因此 mtgpu-1101 类型 4k 显示功能可以在加载驱动阶段禁用。

#### 步骤 1：创建显示配置文件[](https://docs.mthreads.com#步骤-1创建显示配置文件)

在 `/etc/modprobe.d`

目录下创建 `mtgpu.conf`

文件，并在配置文件中添加如下内容：

`options mtgpu vgpu_1g_support_4k=0`



#### 步骤 2：重新加载驱动[](https://docs.mthreads.com#步骤-2重新加载驱动)

重新加载 mtgpu 驱动或重启服务器，使配置生效。

### 禁用 Guest 驱动自动升级[](https://docs.mthreads.com#禁用-guest-驱动自动升级)

Host 驱动升级后 Guest 默认会收到升级提醒，可以通过配置文件关闭升级提醒。

#### 步骤 1：创建升级配置文件[](https://docs.mthreads.com#步骤-1创建升级配置文件)

在 `/etc/modprobe.d`

目录下创建 `mtgpu.conf`

文件，并在配置文件中添加如下内容：

`options mtgpu vgpu_upgrade_mode=0`



#### 步骤 2：重新加载驱动[](https://docs.mthreads.com#步骤-2重新加载驱动-1)

重新加载 mtgpu 驱动或重启服务器，使配置生效。

说明：2.5.0 升级到 2.5.6 仍然需要删除

`/var/local/mthreads/wddm_driver.zip`

关闭 Guest 升级服务，2.5.6 升级到更高版本时可以通过`vgpu_upgrade_mode=0`

配置关闭。

### 使用 MT Virtual Display[](https://docs.mthreads.com#使用-mt-virtual-display)

查看 **MT-virt** 显示器标号。例如，**MT-virt** 显示器为 2 号显示器时，在 **屏幕设置** 中将显示方式设置为 **仅在 2 上显示**。

### 手动选择程序 GPU 加速[](https://docs.mthreads.com#手动选择程序-gpu-加速)

在单 GPU 模式且没有其他显示设备的场景下，所有应用都会默认使用摩尔线程 vGPU 作为加速，在有其他显示设备时需要设置为仅在 **MT Virtual Display** 上显示。

查看 **MT-virt** 显示器标号。例如，**MT-virt** 显示器为 2 号显示器时，在 **屏幕设置** 中将显示方式设置为 **仅在 2 上显示**。

## 监控 MT vGPU[](https://docs.mthreads.com#监控-mt-vgpu)

### 使用 MT GPU 管理工具[](https://docs.mthreads.com#使用-mt-gpu-管理工具)

通过摩尔线程 GPU 管理接口工具 mthreads-gmi 可以实现 GPU 和 vGPU 管�理和监控。

**显示帮助信息**

`$ mthreads-gmi --help`



**监控 GPU 整卡概括信息**

`$ mthreads-gmi -cf`



**监控 vGPU 解码详细信息**

`$ mthreads-gmi vgpu -ds`



**监控 vGPU 编码详细信息**

`$ mthreads-gmi vgpu -es`



**监控 vGPU 使用率**

`$ mthreads-gmi vgpu -u`



**监控 vGPU 详细信息**

`$ mthreads-gmi vgpu -q`



更多命令，参见 [mthreads-gmi 命令参考](https://docs.mthreads.com/gmc/gmc-doc-online/user_manual)。

## 维护驱动[](https://docs.mthreads.com#维护驱动)

### 卸载驱动[](https://docs.mthreads.com#卸载驱动)

#### Host[](https://docs.mthreads.com#host)

##### 步骤 1：关闭虚拟机[](https://docs.mthreads.com#步骤-1关闭虚拟机)

关闭所有使用 vGPU 设备的虚拟机。

##### 步骤 2：卸载 Host 驱动[](https://docs.mthreads.com#步骤-2卸载-host-驱动)

`$ rmmod mtgpu`

$ rmmod mtvgpu_basic

$ rpm -e mtvgpu



说明：若系统未加载

`mtvgpu_basic`

模块，可先通过`lsmod`

确认；未加载时可跳过该命令。

#### Windows Guest[](https://docs.mthreads.com#windows-guest)

##### 步骤 1：卸载 Windows Guest 驱动[](https://docs.mthreads.com#步骤-1卸载-windows-guest-驱动)

打开 **控制面板** > **程序** > **卸载程序**，卸载 **PES Control Center**。

#### Linux Guest[](https://docs.mthreads.com#linux-guest)

##### 步骤 1：卸载 Linux Guest 驱动[](https://docs.mthreads.com#步骤-1卸载-linux-guest-驱动)

以 root 权限运行：

`$ dpkg -P musa`



##### ��步骤 2：重启虚拟机[](https://docs.mthreads.com#步骤-2重启虚拟机)

重启虚拟机，使卸载操作生效。

### 升级驱动[](https://docs.mthreads.com#升级驱动)

升级前需要关闭使用 vGPU 的虚拟机；Host 驱动升级完成后，再分别处理 Windows Guest 和 Linux Guest 驱动升级。

驱动升级流程如下：

#### 步骤 1：升级 Host 驱动[](https://docs.mthreads.com#步骤-1升级-host-驱动)

关闭所有虚拟机，卸载 Host 驱动。

`$ rmmod mtgpu`

$ rmmod mtvgpu_basic

$ rpm -e mtvgpu



说明：若系统未加载

`mtvgpu_basic`

模块，可先通过`lsmod`

确认；未加载时可跳过该命令。

安装新版本 Host 驱动，加载内核驱动。

`$ rpm -ivh xxx_xxx_v1_3_mtvgpu_2.9.2-000_amd64.rpm`



#### 步骤 2：升级 Guest 驱动[](https://docs.mthreads.com#步骤-2升级-guest-驱动)

Windows Guest 驱动可按以下两种方式处理：

##### 方式 1：Windows Guest 提醒升级[](https://docs.mthreads.com#方式-1windows-guest-提醒升级)

Host 驱动升级完成后，Windows Guest 在下一次开机时会收到升级提醒，根据升级提醒完成 Guest 驱动升级。

提示用户关闭应用程序。

升级完成后提醒用户重启操作系统。

重启后驱动升级完成。

##### 方式 2：Windows Guest 手动卸载并重新安装 PES[](https://docs.mthreads.com#方式-2windows-guest-手动卸载并重新安装-pes)

若未通过升级提醒完成升级，可在 Windows Guest 中打开 **控制面板** > **程序** > **卸载程序**，卸载 **PES Control Center**，然后重新运行 PES 安装包 `musa-desktop-win10-64bit_vdi.exe`

完成安装，最后重启操作系统使升级生效。

#### Linux Guest 升级方式[](https://docs.mthreads.com#linux-guest-升级方式)

##### 方式 1：Linux Guest收到升级提醒[](https://docs.mthreads.com#方式-1linux-guest收到升级提醒)

Guest收到升级提醒，点击升级

提示用户关闭应用程序

升级完成后重启虚拟机

重启后驱动升级完成

##### 方式 2：手动升级[](https://docs.mthreads.com#方式-2手动升级)

Linux Guest 采用手动升级方式：先卸载旧版本 Linux Guest 驱动，再安装新版本 Linux Guest 安装包，最后重启虚拟机并确认 `/dev/dri/`

节点与 `lspci -k`

输出正常。

说明：不同 Linux 发行版或安装包格式的卸载、安装命令可能不同，请以当前 Linux Guest 安装包配套说明为准。


### 热升级驱动[](https://docs.mthreads.com#热升级驱动)

针对线上服务器需长时间稳定运行的需求，常规 Host 驱动版本升级需关闭虚拟机，会造成业务中断，而热升级方案可在几乎不中断业务的前提下完成驱动升级。MT vGPU 2.9.2 支持驱动热升级功能，具体可通过热升级升级至哪些版本，可参考对应版本的 Release Note。

`rpm -Uvh xxx_xxx_v1_3_mtvgpu_2.9.2-000_amd64.rpm`



## 使用高级功能[](https://docs.mthreads.com#使用高级功能)

### 热迁移 vGPU 虚拟机[](https://docs.mthreads.com#热迁移-vgpu-虚拟机)

vGPU 热迁移可以将一个带有 MT vGPU 设备的虚拟机，从一台服务器迁移到另外一台服务器，迁移过程中几乎不会造成服务中断或停机，对于已配置 MT vGPU 的虚拟机，其 vGPU 会随虚拟机一同迁移到另一台主机的 MT GPU 上，两台主机上的 MT GPU 及 MT vGPU 必须为同一型号。

热迁移由内核、libvirt、QEMU、GPU 驱动共同协作完成，因此对内核、libvirt、QEMU 版本有特定要求。

- 内核版本：openEuler 24.03（Kernel 6.6.0）、Ubuntu 24.04（Kernel 6.8.0）。
- QEMU 版本：8.2.0。
- Libvirt：9.10.0。

基于 KVM hypervisor 的 Linux 系统，可按如下步骤热迁移 vGPU 虚拟机：

#### 步骤 1：设置最大停机时间[](https://docs.mthreads.com#步骤-1设置最大停机时间)

若虚拟机负载较高，迁移可能无法在默认的最大停机时间内完成。为确保虚拟机迁移顺利完成，需保证最大停机时间超过实际迁移所需时间。

命令：

`virsh migrate-setmaxdowntime --domain $name --downtime $time`



其中：

`$name`

：本地主机上待迁移的虚拟机名称。`$time`

：虚拟机的最大停机时间（单位：毫秒）。

示例：将本地主机上名为 guestvm 的虚拟机的最大停机时间设置为 20 秒（20,000 毫秒）。

`virsh migrate-setmaxdowntime --domain guestvm --downtime 20000`



#### 步骤 2：执行热迁移[](https://docs.mthreads.com#步骤-2执行热迁移)

运行以下 virsh 迁移命令：

`virsh migrate --live $name $destination-url --verbose`



`$name`

指本地主机上待迁移的虚拟机名称。

`$destination-url`

指与待迁移虚拟机所指向的远程主机之间的连接 URL。例如，若要通过 SSH 隧道将虚拟机迁移到 IPv4 地址为 192.168.1.2 的远程主机的系统连接，可将 destination-url 指定为 `qemu+ssh://root@192.168.1.2/system`

。

以下示例为：通过 SSH 隧道将本地主机上名为 guestvm 的虚拟机，迁移到 IPv4 地址为 192.0.2.12 的远程主机的系统连接。

`virsh migrate --live guestvm qemu+ssh://root@192.168.1.2/system --verbose`



更多详情，参见 [Red Hat Enterprise Linux 9](https://docs.redhat.com/en/documentation/red_hat_enterprise_linux/9/html/configuring_and_managing_virtualization/migrating-virtual-machines_configuring-and-managing-virtualization)。

### 休眠和恢复 MT vGPU 虚拟机[](https://docs.mthreads.com#休眠和恢复-mt-vgpu-虚拟机)

MT vGPU 2.9.2 提供虚拟机休眠与恢复能力，支持通过 `virsh save`

/`virsh restore`

或 `virsh managedsave`

/`virsh start`

保存和恢复虚拟机运行状态。该功能可在不中断业务上下文的前提下，将 Guest 当前运行状态保存为由 Host 统一管理的文件，并在后续需要时快速恢复虚拟机运行。

与传统关机再开机相比，虚拟机休眠无需重新启动 Guest 操作系统、重新初始化驱动或重新启动业务应用，可缩短恢复时间并降低业务中断影响。当前版本采用“休眠前显式通知驱动”的方式：Host 侧脚本在执行 virsh 休眠命令前，先通知 Guest 内驱动暂停 GPU 命令并完成休眠前处理；驱动处理完成后，再执行虚拟机休眠保存动作，确保后续恢复流程可用。

#### MT vGPU 休眠机制��与执行流程[](https://docs.mthreads.com#mt-vgpu-休眠机制与执行流程)

MT vGPU 休眠功能涉及如下软件栈：

- 管理层（virsh/libvirt）
- 管理脚本发起
`virsh save`

、`virsh restore`

、`virsh managedsave`

、`virsh start`

。 - libvirt 接收休眠或恢复请求，并调用 QEMU 对虚拟机状态进行保存或恢复。

- 管理脚本发起
- 虚拟化执行层（QEMU）
- QEMU 负责虚拟机 CPU、内存及设备状态的序列化与反序列化。休眠流程复用了热迁移中的
`qemu_savevm_state_*`

状态保存框架。

- QEMU 负责虚拟机 CPU、内存及设备状态的序列化与反序列化。休眠流程复用了热迁移中的
- vGPU 软件层（Host/Guest）
- Host 侧保存脚本在真正执行休眠前，先通过通知机制与 Guest 内驱动协同。Guest 内驱动进入休眠准备状态，暂停 GPU 命令处理并整理恢复所需状态。

- 硬件资源层（vGPU instance / VRAM / PA 映射）
- 恢复后，虚拟机可能运行在新的 instance 或新的 VRAM 映射环境中。因此，恢复流程必须避免继续使用源端遗留的旧物理地址映射。


休眠本质上是“基于热迁移保存框架的一次性状态保存”。由于 Guest 侧在 vCPU 停止前几乎没有自然的收敛窗口，因此需要额外的预通知机制配合，在真正调用 `virsh save`

或 `virsh managedsave`

之前，让驱动先进入受控状态，完成 GPU 命令暂停和休眠前准备。

当前版本休眠流程如下：

- Host 侧执行休眠保存脚本。
- 脚本通知 Guest 内驱动进入休眠准备流程。
- 驱动暂停 GPU 命令并处理内部状态。
- 驱动返回处理完成状态。
- Host 侧继续执行
`virsh save`

或`virsh managedsave`

。 - libvirt/QEMU 保存虚拟机完整状态。
- 通过
`virsh restore`

或`virsh start`

恢复虚拟机。

命令说明：

| 命令 | 说明 |
|---|---|
`virsh save <vm-name> <save-file>` | 保存虚拟机运行状态到指定文件 |
`virsh restore <save-file>` | 从保存文件恢复虚拟机 |
`virsh managedsave <vm-name>` | 由 libvirt 管理保存文件 |
`virsh start <vm-name>` | 启动已执行 managedsave 的虚拟机并恢复其状态 |

`save`

与 `managedsave`

的选择建议如下：

`save`

：适合平台自行管理保存文件路径、跨兼容节点恢复，或需要对保存文件进行归档、搬迁和统一生命周期管理的场景。`managedsave`

：适合单机由 libvirt 管理保存文件的场景，操作更简单，但保存文件位置由 libvirt 管理，不适合需要平台显式管理保存文件路径的场景。

#### 准备使用环境[](https://docs.mthreads.com#准备使用环境)

使用虚拟机休眠功能前，请确认满足以下条件：

- Guest 为 Windows Guest。
- Host OS 版本满足要求：
- openEuler 24.03（Kernel 6.6.0）。
- Ubuntu 24.04（Kernel 6.8.0）。

- 软件版本满足要求：
- QEMU 8.2.0。
- Libvirt 9.10.0。
- MT vGPU 2.9.2 及对应配套组件。

- 使用 root 用户或具备 libvirt 管理权限、sysfs 节点写入权限的管理用户执行休眠和恢复操作。
- 休眠端与恢复端保持一致：
- vGPU 软件版本为 release_vgpu_2.9.2 及以上版本。
- vGPU 类型一致。
- IOMMU、SR-IOV 配置一致。
- vCPU、RAM 配置一致。
- GPU 硬件类型一致，例如 S3000 与 S3000E 不可混用。

- 当前未执行热迁移、热插拔、热升级等与设备状态密切相关的操作。
- 休眠功能默认开启，开启超分时休眠功能默认关闭。

部署时建议完成以下检查：

##### 步骤 1：确认组件版本[](https://docs.mthreads.com#步骤-1确认组件版本)

确认 libvirt 与 QEMU 版本符合要求。

##### 步骤 2：部署 vGPU 环境[](https://docs.mthreads.com#步骤-2部署-vgpu-环境)

安装匹配版本的 Host vGPU 驱动，创建 vGPU 设备，启动虚拟机并安装匹配版本的 Guest 驱动。

##### 步骤 3：可选确认休眠链路[](https://docs.mthreads.com#步骤-3可选确认休眠链路)

休眠功能默认开启，开启超分时休眠功能默认关闭。如需在上线前�确认可用性，建议在测试环境执行一次保存脚本演练，确认 `/sys/bus/mdev/devices/<uuid>/common`

节点存在，且脚本能够收到 `GUEST_SAVE_FINISHED`

状态。

#### 执行休眠保存[](https://docs.mthreads.com#执行休眠保存)

用户需要将通知 vGPU 和休眠命令封装到同一 Host 侧脚本中。休眠保存脚本应先通知 Guest 驱动暂停 GPU 命令并准备休眠，待驱动状态返回 `GUEST_SAVE_FINISHED`

后，再执行 `virsh save`

或 `virsh managedsave`

。

脚本中的关键变量说明如下：

`uuid`

：vGPU 设备 UUID，可通过`mdevctl list`

或`ls /sys/bus/mdev/devices/`

查询。`vm_name`

：虚拟机名称，可通过`virsh list --all`

查询。`vm_saved_imgfile`

：`save`

方式下保存虚拟机运行状态的文件路径，建议使用 Host 侧可用空间充足且由平台统一管理的目录。

建议的 Host 侧保存流程如下：

##### 步骤 1：检查虚拟机状态[](https://docs.mthreads.com#步骤-1检查虚拟机状态)

检查虚拟机是否存在且运行。若不存在或未运行，则退出。

##### 步骤 2：检查 vGPU common 节点[](https://docs.mthreads.com#步骤-2检查-vgpu-common-节点)

检查 vGPU common 节点是否存在。若节点不存在，则退出。

##### 步骤 3：通知 Guest 驱动准备休眠[](https://docs.mthreads.com#步骤-3通知-guest-驱动准备休眠)

通知 Guest 驱动暂停 GPU 命令并准备休眠。

##### 步骤 4：确认 Guest 驱动已就绪[](https://docs.mthreads.com#步骤-4确认-guest-驱动已就绪)

轮询查看 vGPU common 节点获取驱动状态。若超时（建议设置超时时间为 5s）仍未返回 `GUEST_SAVE_FINISHED`

，则退出。

##### 步骤 5：保存虚拟机状态[](https://docs.mthreads.com#步骤-5保存虚拟机状态)

调用 `virsh save`

或 `virsh managedsave`

保存虚拟机状态。

以下为示意代码，需根据平台脚本框架适配：

`#!/bin/bash`


uuid="<vgpu-uuid>"

vm_name="<vm-name>"

vm_saved_imgfile="<vm-saved-imgfile>"

common_node="/sys/bus/mdev/devices/${uuid}/common"


# step 1. 检查虚拟机是否存在且运行

if ! virsh list | grep -qw "${vm_name}"; then

echo "错误：虚拟机 ${vm_name} 未运行或不存在"

exit 1

fi


# step 2. 检查 vGPU common 节点是否存在

if [ ! -e "${common_node}" ]; then

echo "vGPU common 节点不存在：${common_node}"

exit 1

fi


# step 3. 通知 Guest 驱动暂停 GPU 命令并准备休眠

echo "vgpu_save_running" > "${common_node}"


# step 4. 检查 vGPU 保存准备状态，节点输出包含 GUEST_SAVE_FINISHED 后才继续休眠操作

status_output=$(cat "${common_node}")

if ! echo "${status_output}" | grep -q "GUEST_SAVE_FINISHED"; then

echo "状态未就绪，退出脚本"

exit 1

fi


# step 5. 休眠虚拟机。以下 save/managedsave 命令二选一

# save 方式

virsh save "${vm_name}" "${vm_saved_imgfile}"


# managedsave 方式

# virsh managedsave "${vm_name}"



#### 恢复虚拟机[](https://docs.mthreads.com#恢复虚拟机)

用户需要将环境检查和虚拟机恢复命令封装到同一 Host 侧脚本中。虚拟机恢复脚本应先检查环境是否支持恢复虚拟机，当满足恢复条件后，再执行 `virsh restore`

或 `virsh start`

。

建议的 Host 侧恢复流程如下：

##### 步骤 1：检查超分配置[](https://docs.mthreads.com#步骤-1检查超分配置)

检查当前环境的超分配置情况。若已开启超分，则退出。

##### 步骤 2：检查保存文件[](https://docs.mthreads.com#步骤-2检查保存文件)

检查指定保存文件是否存在。若不存在指定保存文件，则退出。

##### 步骤 3：恢复虚拟机状态[](https://docs.mthreads.com#步骤-3恢复虚拟机状态)

调用 `virsh restore`

或 `virsh start`

恢复虚拟机状态。

##### 步骤 4：处理恢复失败[](https://docs.mthreads.com#步骤-4处理恢复失败)

若恢复失败，则启用冷启动方案，保证虚拟机可以正常开机。

以下为示意代码，需根据平台脚本框架适配：

`#!/bin/bash`


vm_name="<vm-name>"

vm_saved_imgfile="<vm-saved-imgfile>"

xml_file="/tmp/${vm_name}_restore.xml"


# step 1. 检查当前环境的超分配置情况

VGPU_STATUS=$(cat /sys/module/mtgpu/parameters/vgpu_overcommit_enable 2>/dev/null || echo "UNKNOWN")

if [ "${VGPU_STATUS}" = "Y" ]; then

echo "当前环境已启用超分，不支持休眠，退出脚本，不执行虚拟机恢复"

exit 1

elif [ "${VGPU_STATUS}" != "N" ]; then

echo "vgpu_overcommit_enable 节点状态异常：${VGPU_STATUS}，仅支持 N 时执行恢复"

exit 1

fi


echo "vGPU 超分配置检查通过"


# step 2. 检查指定保存文件是否存在。以下分别为 save/managedsave 检查方式：

# save 方式

if [ ! -f "${vm_saved_imgfile}" ]; then

echo "恢复失败：保存文件 ${vm_saved_imgfile} 不存在"

exit 1

fi


# managedsave 方式

# if ! virsh list --managed-save --all | grep -qw "${vm_name}"; then

# echo "恢复失败：未找到 ${vm_name} 的 managedsave 状态"

# exit 1

# fi


# step 3. 调用 virsh restore 或 virsh start 恢复虚拟机状态。以下 save/managedsave 命令二选一：

# save 方式

if ! virsh restore "${vm_saved_imgfile}"; then

echo "virsh restore 执行失败，进入冷启动兜底流程"

virsh save-image-dumpxml "${vm_saved_imgfile}" > "${xml_file}" || { echo "导出 XML 失败"; exit 1; }

virsh destroy "${vm_name}" 2>/dev/null || true

virsh create "${xml_file}"

fi


# managedsave 方式

# if ! virsh start "${vm_name}"; then

# echo "virsh start 执行失败，进入冷启动兜底流程"

# virsh destroy "${vm_name}" 2>/dev/null || true

# virsh managedsave-remove "${vm_name}" 2>/dev/null || true

# virsh undefine "${vm_name}" 2>/dev/null || true

# virsh define "${xml_file}" || exit_script "define 虚拟机失败"

# virsh start "${vm_name}"

# fi



#### 处理失败场景[](https://docs.mthreads.com#处理失败场景)

常见失败场景及处理建议如下：

- vGPU common 节点不存在：检查 vGPU 是否已创建、虚拟机是否已绑定该 vGPU、Host 驱动是否正常加载。
- 未返回
`GUEST_SAVE_FINISHED`

：检查 Guest 驱动版本是否匹配、Guest 是否正常运行，以及当前是否正在执行热迁移、热插拔或热升级等操作。 `virsh save`

或`virsh managedsave`

执行失败：检查虚拟机状态、Host 剩余磁盘空间、libvirt/QEMU 服务状态和当前用户权限。`virsh restore`

执行失败：检查保存文件是否存在且完整，恢复端与休眠端的 vGPU 版本、vGPU 类型、GPU 硬件类型、IOMMU/SR-IOV、vCPU、RAM 配置是否一致。`virsh start`

恢复 managedsave 状态失败：检查是否存在 managedsave 状态，以及虚拟机定义是否仍然存在。- 恢复后 Guest 异常：检查保存文件与 Guest 磁盘镜像是否匹配，确认保存后到恢复前未修改 Guest 磁盘内容。

#### 查看限制与注意事项[](https://docs.mthreads.com#查看限制与注意事项)

- 休眠端与恢复端必须满足严格的版本、配置和硬件兼容要求。
- 热迁移、热插拔、热升级过程中不应同时执行休眠操作。
- 超分功能默认关闭。若启用超分，则无法使用休眠功能。
- 当前仅支持 Windows Guest。
- CPU 可用资源不足的情况下，虚拟机休眠或恢复可能会失败。
- 虚拟机重启过程中执行休眠指令，恢复虚拟机后虚拟机可能会关机（此为 Windows 自身逻辑所致）。
- save 文件与磁盘镜像之间有强一致性要求，保�存后到恢复前不应修改 Guest 磁盘内容，否则可能导致 Guest 文件系统损坏或状态不一致。
- 休眠后若要跨服务器恢复，需保证磁盘镜像在 save 和 restore 之间未改变，可使用网络共享磁盘，或拷贝虚拟机所有磁盘文件，否则可能破坏 Guest 文件系统。

### 配置 MT vGPU 超分[](https://docs.mthreads.com#配置-mt-vgpu-超分)

为了进一步提升服务器环境上的 GPU 利用率，参考 CPU 超分的做法引入 vGPU 超分功能，将原本的静态显存切分改为显存和系统内存动态交换的方式，提升 vGPU 的路数。需要注意的是，MT vGPU 2.9.2 及以上版本才开始支持 vGPU 超分功能。

#### 查看限制条件[](https://docs.mthreads.com#查看限制条件)

- vGPU 超分功能仅对
`mtgpu-1101`

类型生效。 - vGPU 超分功能开启后，只能创建同种类型的 vGPU。例如，创建
`mtgpu-1101`

后，就无法创建`mtgpu-1102`

；需要销毁所有`mtgpu-1101`

后才能创建`mtgpu-1102`

。 - vGPU 超分功能仅对 Windows 虚拟机生效。
- 设置超分比例前，需要在 Host 上预留足够的系统内存，否则超分功能无法开启。

#### 设置超分比例[](https://docs.mthreads.com#设置超分比例)

超分比例通过安装驱动时进行修改。

##### 步骤 1：修改超分配置文件[](https://docs.mthreads.com#步骤-1修改超分配置文件)

修改 `/etc/modprobe.d/0-mtgpu.conf`

文件。

##### 步骤 2：设置超分参数[](https://docs.mthreads.com#步骤-2设置超分参数)

在配置文件中，通过参数 `vgpu_overcommit_enable`

开启或关闭超分功能。其中，`0`

表示关闭超分（默认值）；`1`

表示开启超分。

在配置文件中，通过参数 `vgpu_overcommit_num`

设置超分的路数，范围为 1～6。

参考如下配置：

**开启超分**

开启超分功能，并新增 6 路 vGPU。

`options mtgpu vgpu_overcommit_enable=1`

options mtgpu vgpu_overcommit_num=6



说明：

`vgpu_overcommit_num=6`

表示增加 6 路 vGPU。原本`mtgpu-1101`

最大路数是 28 路，增加 6 路后为 34 路；同时，Host 会申请 6 GB 系统内存。

**关闭超分**

关闭超分功能。

`options mtgpu vgpu_overcommit_enable=0`



##### 步骤 3：重新加载驱动[](https://docs.mthreads.com#步骤-3重新加载驱动-1)

修改完成后，重新加载 mtgpu 驱动或重启服务器使配置生效。

#### 查询超分状态[](https://docs.mthreads.com#查询超分状态)

通过 `mthreads-gmi vgpu -q`

命令可以查询 vGPU 是否开启超分，以及当前 vGPU 使用了多少系统内存替代显存。

- 例如：

`# mthreads-gmi vgpu -q`


GPU0 00000000:31:00.0

Active vGPUs : 34

vGPU ID : 1

VM UUID : a05de014-726d-4152-adc8-50e354f5036f

VM Name : VM-1

vGPU Name : MT vGPU S3000-1101

vGPU Type : mtgpu-1101

vGPU UUID : c4f702ca-c69d-4d7d-a526-5fdcf78d3429

MPC : 0

FB Memory Usage

Total : 1024MiB

Used : 0MiB

Free : 1024MiB

Utilization

Gpu : 0%

Memory : 0%

Encoder Stats

Active Sessions : 0

Average FPS : 0

vGPU Over Commit

Enable : YES # YES 表示开启了 vGPU 超分

System Memory : 176MiB # 使用了 176 MB 系统内存作为显存



## 使用工具和 SDK[](https://docs.mthreads.com#使用工具和-sdk)

### 使用 MT DirectStream 示例[](https://docs.mthreads.com#使用-mt-directstream-示例)

**用例说明**：

| 文件名称 | 功能说明 |
|---|---|
| AppEncD3D11.exe | 从本地文件读取 YUV 数据进行编码，码流写入指定的文件。 |
| AppEncD3D11Perf.exe | 衡量 FPS 中的编码性能（一次性读入文件，所以 YUV 文件不宜过大），码流不写入文件。 |
| AppEncDDA.exe | 捕获桌面，并对捕获的图像进行编码（用于 virtual display 场景），码流写入文件 DDABitStream_x_x.h264（微软抓屏接口）。 |
| AppEncMTCapture.exe | 摩尔线程私有桌面抓屏编码方案，功能同 AppEncDDA.exe，效率更高，功能集成参考 mtencode API 手册或示例代码。 |

### 运行 MT DirectStream 示例[](https://docs.mthreads.com#运行-mt-directstream-示例)

#### 步骤 1：准备测试文件[](https://docs.mthreads.com#步骤-1准备测试文件)

准备一个 NV12 文件，用于 AppEncD3D11.exe 或 AppEncD3D11Perf.exe。

#### 步骤 2：执行测试命令[](https://docs.mthreads.com#步骤-2执行测试命令)

##### 编码文件[](https://docs.mthreads.com#编码文件)

使用 YUV 文件编码 h.264 码流：

`AppEncD3D11.exe -i 1920x1080_nv12.yuv -s 1920x1080 -src_fmt nv12 -bf 0 -rc cqp -constqp 20 -fps 25 -gop 30 -frames 100 -o out.h264`



##### 性能测试[](https://docs.mthreads.com#性能测试)

执行性能测试：

`AppEncD3D11Perf.exe -i 1920x1080_nv12.yuv -s 1920x1080 -src_fmt nv12 -bf 0 -rc cqp -constqp 20 -fps 25 -gop 30 -frames 50000 -o out-cqp.h264`



##### 抓屏编码[](https://docs.mthreads.com#抓屏编码)

使用微软 DDA 抓取屏幕并编码成 h.264 码流：

`AppEncDDA.exe -frames 500`



可参考如下最小示例调用 `AppEncMTCapture.exe`

：

`AppEncMTCapture.exe -fps 30 -output 0 -frames 500`



**参数说明：**

AppEncD3D11.exe/AppEncD3D11Perf.exe Options:

`-i Input file path`

-o Output file path

-s Input resolution in this form: WxH

-src_fmt input file pixel format(nv12, bgra)

-frames encode frame number

-profile H264: auto baseline main high

-fps Frame rate

-gop Length of GOP (Group of Pictures)

-bf Number of consecutive B-frames

-rc Rate control mode: cqp cbr

-bitrate Average bit rate, can be in unit of 1, K, M

-constqp QP value for cqp rate control mode


AppEncDDA.exe Options:

-frames encode frame number



`AppEncMTCapture.exe`

的其他参数请以安装包内帮助输出为准。

### 使用 MT API 自定义分辨率[](https://docs.mthreads.com#使用-mt-api-自定义分辨率)

`mtapi_resolution_sample.exe`

用于设置屏幕自定义分辨率，分辨率支持范围为 640 x 360 至当前规格支持的最大分辨率，使用方法如下：

说明：请以 MTAPI 安装包内 sample 名称为准。


#### 步骤 1：设置自定义分辨率[](https://docs.mthreads.com#步骤-1设置自定义分辨率)

`mtapi_resolution_sample.exe -t 0 1920 1080 60 -s 0 1920 1080 60`



#### 步骤 2：确认参数含义[](https://docs.mthreads.com#步骤-2确认参数含义)

-
`-t 0 1920 1080 60`

：在 0 号显示器上尝试创建 1920 x 1080 60 Hz 属性的显示器。 -
`-s 0 1920 1080 60`

：在 0 号显示器上保存 1920 x 1080 60 Hz 属性显示器的设置。

## 兼容性和规格[](https://docs.mthreads.com#兼容性和规格)

### MTT S 系列显卡支持的 vGPU 性能和参数[](https://docs.mthreads.com#mtt-s-系列显卡支持的-vgpu-性能和参数)

Windows Guest 性能和参数如下表：

| vGPU 类型 | 支持的 vGPU 路数 | 最大桌面分辨率 | 支持的虚拟显示器数量 | 最大编码分辨率 | 最大解码分辨率 | 10bit 桌面 | 144Hz 刷新率 |
|---|---|---|---|---|---|---|---|
| 1100 | 32 | 4096x2160 | 2 | 4096x2160 | 1920x1080 | 不支持 | 支持 |
| 1101 | 28 | 4096x2160 | 2 | 4096x2160 | 1920x1080 | 不支持 | 支持 |
| 1102 | 16 | 4096x2160 | 2 | 4096x2160 | 4096x2160 | 不支持 | 支持 |
| 1104 | 8 | 4096x2160 | 2 | 4096x2160 | 4096x2160 | 不支持 | 支持 |
| 1108 | 4 | 7680x4320 | 2 | 7680x4320 | 7680x4320 | 支持 | 支持 |
| 1116 | 2 | 7680x4320 | 2 | 7680x4320 | 7680x4320 | 支持 | 支持 |
| 1132 | 1 | 7680x4320 | 2 | 7680x4320 | 7680x4320 | 支持 | 支持 |

Linux Guest 性能和参数如下表：

| vGPU 类型 | 支持的 vGPU 路数 | 最大桌面分辨率 | 支持的虚拟显示器数量 | 最大编码分辨率 | 最大解码分辨率 | 10bit 桌面 | 144Hz 刷新率 |
|---|---|---|---|---|---|---|---|
| 1100 | 32 | 1920x1200 | 1 | 1920x1200 | 1920x1200 | 不支持 | 不支持 |
| 1101 | 28 | 1920x1200 | 2 | 1920x1200 | 1920x1200 | 不支持 | 不支持 |
| 1102 | 16 | 2560x1600 | 2 | 2560x1600 | 2560x1600 | 不支持 | 不支持 |
| 1104 | 8 | 4096x2160 | 2 | 4096x2160 | 4096x2160 | 不支持 | 不支持 |
| 1108 | 4 | 4096x2160 | 2 | 4096x2160 | 4096x2160 | 不支持 | 不支持 |
| 1116 | 2 | 4096x2160 | 2 | 4096x2160 | 4096x2160 | 不支持 | 不支持 |
| 1132 | 1 | 4096x2160 | 2 | 4096x2160 | 4096x2160 | 不支持 | 不支持 |