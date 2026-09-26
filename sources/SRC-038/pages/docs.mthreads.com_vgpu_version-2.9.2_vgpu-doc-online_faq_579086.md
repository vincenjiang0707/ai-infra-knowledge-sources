source: https://docs.mthreads.com/vgpu/version-2.9.2/vgpu-doc-online/faq

# 帮助（FAQ）

## 安装和配置[](https://docs.mthreads.com#安装和配置)

### 安装 Host 驱动失败，如何处理？[](https://docs.mthreads.com#安装-host-驱动失败如何处理)

**可能原因**

Host 驱动使用 DKMS 技术，会根据当前操作系统内核版本自动重新构建驱动。若系统未安装 DKMS、编译工具链不完整，或当前内核版本不满足要求，驱动构建可能失败。

**处理方法**

- 确认操作系统已安装 DKMS、GCC 和内核开发包。
- 确认 GCC 版本和操作系统内核版本满足当前版本要求。
- 重新安装 Host 驱动。
- 若仍安装失败，保留安装日志并联系技术支持。

### 如何确认 IOMMU 已开启？[](https://docs.mthreads.com#如何确认-iommu-已开启)

服务器重启后，可通过如下命令确认启动参数已生效：

`$ cat /proc/cmdline | grep -E "intel_iommu=on|amd_iommu=on"`



也可通过如下命令确认系统已创建 IOMMU 分组：

`$ ls /sys/kernel/iommu_groups/`



若命令返回多个数字编号目录，表示系统已识别 IOMMU 分组。

### 创建 vGPU 失败，如何处理？[](https://docs.mthreads.com#创建-vgpu-失败如何处理)

**可能原因**

- Host 驱动未正常加载。
- IOMMU 或 SR-IOV 未正确开启。
- GPU PCI 设备 BDF 地址填写错误。
- vGPU 类型不匹配或当前物理 GPU 资源不足。
- 超分开启后，尝试创建不同类型的 vGPU。

**处理方法**

- 运行
`lsmod | grep "mtgpu"`

，确认 Host 驱动已加载。 - 运行
`lspci -d 1ed5:`

，确认系统已识别 MTT S 系列 GPU。 - 重新确认
`mdevctl start`

命令中的 BDF 地址和`--type`

参数。 - 查看
[MTT S 系列显卡支持的 vGPU 性能和参数](https://docs.mthreads.com/vgpu/version-2.9.2/vgpu-doc-online/install_guide#mtt-s-%E7%B3%BB%E5%88%97%E6%98%BE%E5%8D%A1%E6%94%AF%E6%8C%81%E7%9A%84-vgpu-%E6%80%A7%E8%83%BD%E5%92%8C%E5%8F%82%E6%95%B0)，确认 vGPU 类型和可切分路数。

### 服务器重启或宕机，如何处理？[](https://docs.mthreads.com#服务器重启或宕机如何处理)

**可能原因**

显卡温度过高可能导致服务器重启或宕机。部分服务器未完成显卡硬件导入时，可能无法根据显卡温度自动调节风扇转速。

**处理方法**

在 BMC 中手动设置风扇转速，将风扇转速设置为 100%，并确认服务器散热状态正常。

## 虚拟机和远程访问[](https://docs.mthreads.com#虚拟机和远程访问)

### 虚拟机添加 vGPU 后，为什么无法通过 QEMU VNC 访问桌面？[](https://docs.mthreads.com#虚拟机添加-vgpu-后为什么无法通过-qemu-vnc-访问桌面)

**可能原因**

QEMU 自带的 VNC 不支持抓取 vGPU 桌面。

**处理方法**

安装 vGPU 驱动前，在虚拟机中安装 ToDesk、向日葵或 vncserver 等远程访问工具，并通过远程访问工具访问桌面。

### Windows Guest 收到驱动升级提醒后，如何处理？[](https://docs.mthreads.com#windows-guest-收到驱动升级提醒后如何处理)

Host 驱动升级后，Windows Guest 开机后会收到驱动升级提醒。请按照弹窗提示关闭可能正在使用 GPU 的应用程序，完成 Guest 驱动升级后重启操作系统，使升级生效。

若不希望 Guest 收到自动升级提醒，可在 Host 侧通过 `vgpu_upgrade_mode=0`

关闭升级提醒。具体方法请参见 [禁用 Guest 驱动自动升级](https://docs.mthreads.com/vgpu/version-2.9.2/vgpu-doc-online/install_guide#%E7%A6%81%E7%94%A8-guest-%E9%A9%B1%E5%8A%A8%E8%87%AA%E5%8A%A8%E5%8D%87%E7%BA%A7)。

## 高级功能[](https://docs.mthreads.com#高级功能)

### 热迁移 vGPU 虚拟机需要满足哪些条件？[](https://docs.mthreads.com#热迁移-vgpu-虚拟机需要满足哪些条件)

热迁移由内核、libvirt、QEMU 和 GPU 驱动共同协作完成。执行热迁移前，请确认：

- 源端和目标端的 MT GPU 及 MT vGPU 型号一致。
- 内核、QEMU 和 libvirt 版本满足要求。
- 目标主机可通过指定的连接 URL 访问。
- 虚拟机负载较高时，已设置足够的最大停机时间。

更多详情，参见 [热迁移 vGPU 虚拟机](https://docs.mthreads.com/vgpu/version-2.9.2/vgpu-doc-online/install_guide#%E7%83%AD%E8%BF%81%E7%A7%BB-vgpu-%E8%99%9A%E6%8B%9F%E6%9C%BA)。

### 休眠和恢复 MT vGPU 虚拟机失败，如何处理？[](https://docs.mthreads.com#休眠和恢复-mt-vgpu-虚拟机失败如何处理)

请优先检查以下项目：

- Guest 是否为 Windows Guest。
- 休眠端与恢复端的 vGPU 软件版本、vGPU 类型、GPU 硬件类型、IOMMU/SR-IOV、vCPU 和 RAM 配置是否一致。
- 当前是否正在执行热迁移、热插拔、热升级等与设备状态密切相关的操作。
- 超分功能是否已开启。若已开启超分，则无法使用休眠功能。
- 保存文件是否存在且完整，保存后到恢复前是否修改过 Guest 磁盘内容。

更多详情，参见 [休眠和恢复 MT vGPU 虚拟机](https://docs.mthreads.com/vgpu/version-2.9.2/vgpu-doc-online/install_guide#%E4%BC%91%E7%9C%A0%E5%92%8C%E6%81%A2%E5%A4%8D-mt-vgpu-%E8%99%9A%E6%8B%9F%E6%9C%BA)。

### 开启超分后，为什么无法创建其他类型的 vGPU？[](https://docs.mthreads.com#开启超分后为什么无法创建其他类型的-vgpu)

vGPU 超分功能开启后，只能创建同种类型的 vGPU。例如，创建 `mtgpu-1101`

后，就无法创建 `mtgpu-1102`

。如需创建其他类型的 vGPU，需要先销毁所有 `mtgpu-1101`

，再创建目标类型的 vGPU。

更多详情，参见 [配置 MT vGPU 超分](https://docs.mthreads.com/vgpu/version-2.9.2/vgpu-doc-online/install_guide#%E9%85%8D%E7%BD%AE-mt-vgpu-%E8%B6%85%E5%88%86)。