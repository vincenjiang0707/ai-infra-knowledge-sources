source: https://docs.mthreads.com/vgpu/version-2.9.2/vgpu-doc-online/releasenote

# 发布版本信息

## 摩尔线程 GPU 虚拟化驱动 MT vGPU v2.9.2 软件发布说明[](https://docs.mthreads.com#摩尔线程-gpu-虚拟化驱动-mt-vgpu-v292-软件发布说明)

2026年07月24日

## 1. 版本说明[](https://docs.mthreads.com#1-版本说明)

MT vGPU 是摩尔线程 GPU 虚拟化的驱动产品，包含将物理 GPU 切分为虚拟 GPU 的驱动程序、在虚拟机中使用 vGPU 的驱动程序、管理监控软件�、编程接口库，以及使用 GPU 进行硬件编码的软件开发套件等组件。下面对 MT vGPU v2.9.2 版本的新增功能、功能说明、环境兼容、驱动兼容、热升级版本支持、修复问题和已知问题进行说明。

## 2. v2.9.2 新增功能[](https://docs.mthreads.com#2-v292-新增功能)

- Windows 虚拟机新增支持休眠功能，
[详见操作手册](https://docs.mthreads.com/vgpu/version-2.9.2/vgpu-doc-online/install_guide#%E4%BC%91%E7%9C%A0%E5%92%8C%E6%81%A2%E5%A4%8D-mt-vgpu-%E8%99%9A%E6%8B%9F%E6%9C%BA) - Windows 虚拟机新增支持超分，
[详见操作手册](https://docs.mthreads.com/vgpu/version-2.9.2/vgpu-doc-online/install_guide#%E9%85%8D%E7%BD%AE-mt-vgpu-%E8%B6%85%E5%88%86) - Windows 虚拟机新增支持 Vulkan 1.3
- MT DirectStream 2.0 支持 HDR 抓屏及编码

## 3. 功能说明[](https://docs.mthreads.com#3-功能说明)

- 主机端提供 vGPU 驱动程序，提供 GPU 虚拟化功能
- GPU 卡支持 MTT S3000、MTT S3000E，支持单机 1 卡和单机多卡
- vGPU 切分：MTT S3000、MTT S3000E 最大支持 32 个 vGPU（1.0 GB），支持 1 GB × 32、1 GB × 28、2 GB × 16、4 GB × 8、8 GB × 4、16 GB × 2、32 GB × 1，配置详见《摩尔线程 vGPU 操作手册》附录
- 支持动态弹性切分，客户机可以混合切分任意 vGPU 类型，不需要重启主机
- GPU 调度方式支持 Best Effort 和 Equal Share 模式
- 主机端支持多种操作系统和内核版本组合，详情请见环境兼容介绍
- 客户机操作系统中提供 vGPU 显卡驱动，支持 Windows Server 2019、Windows 10 1909、Windows 10 21H2、Windows 11 24H2
- 主机端提供 GPU 管理工具和函数库，可对 GPU 的算力资源、显存资源进行实时监控
- 客户机中提供 GMI/MTML，可查询 GPU 显存利用率和 GPU 利用率
- Windows 中兼容 DirectX 框架，支持 DirectX 12
- Windows 中兼容 OpenGL 框架，支持 OpenGL 4.2
- Windows 中兼容 Vulkan 框架，支持 Vulkan 1.3
- Windows 中兼容 DXVA 2.0 硬件视频加速接口
- Linux 中兼容 OpenGL 框架，支持 OpenGL 4.6
- Linux 中兼容 Vulkan 框架，支持 Vulkan 1.3
- 支持混合模式和独显模式
- 提供 MT DirectStream 软件开发套件，支持 GPU 硬件编码
- 提供 MT Capture 软件开发套件，支持 GPU 硬件编码
- 编码格式支持 H.264、H.265，支持 8-bit、10-bit 视频编码
- 解码格式支持 H.264、H.265、VP9、AV1 等常用格式，支持 8-bit、10-bit 视频解码
- 支持常用主流分辨率，最大分辨率支持 7680 × 4320
- vGPU 支持 VGA-compatible 模式，并提供 Virtual Display
- 支持多种常见分辨率：800 × 600、1024 × 768、1152 × 864、1280 × 720、1280 × 768、1280 × 800、1280 × 960、1280 × 1024、1360 × 768、1366 × 768、1600 × 900、1600 × 1024、1600 × 1200、1680 × 1050、1920 × 1080、1920 × 1200、2560 × 1440、2560 × 1600、3840 × 2160、4096 × 2160、7680 × 4320
- 支持自定义分辨率
- 支持客户机驱动自动升级
- 支持主机驱动热升级
- 支持 MT vGPU 热迁移
- 支持 MT vGPU 休眠
- 支持 MT vGPU 超分
- 支持 7×24 小时连续稳定运行

## 4. 环境兼容[](https://docs.mthreads.com#4-环境兼容)

### GPU[](https://docs.mthreads.com#gpu)

- MTT S3000
- MTT S3000E
- MTT X300

### CPU[](https://docs.mthreads.com#cpu)

- Intel Xeon 系列 CPU
- Hygon 7390/7490/7493
- Kunpeng 920

### 主机端操作系统[](https://docs.mthreads.com#主机端操作系统)

- CentOS 7.5 + Kernel 5.10.0
- Ubuntu 20.04.1 + Kernel 5.4.0-42
- CentOS 7.9 + Kernel 5.10.38
- CentOS 7.6 + Kernel 4.18.0
- CentOS 7.6 + Kernel 4.19.12
- openEuler 20.03 + Kernel 4.19.0
- BCLinux-for-Euler-21.10 + Kernel 4.19.90-2107.6.0.0208.16.oe1.bclinux.x86_64
- Anolis OS + Kernel 5.10
- UnionTech OS Server 20（1000c）+ Kernel 4.19.0.x86_64
- Kylin Server V10 SP3（General Release 2303，ARM64）+ Kernel 4.19.0

### 客户机操作系统[](https://docs.mthreads.com#客户机操作系统)

- Windows 11 24H2
- Windows 10 1909、21H2、22H2
- Windows 10 2019 LTSC
- Windows Server 2019
- UOS 1050u3（Host CPU：Hygon）
- Kylin Desktop V10（2503，Host CPU：Hygon）
- Kylin Desktop V10 SP1（General Release 2203，ARM64，Host CPU：Kunpeng 920）
- NFSDesktop-5.0-G230-cloud-202407162121-amd64（Host CPU：Hygon）

### QEMU/KVM[](https://docs.mthreads.com#qemukvm)

- 2.11.2
- 4.2 及更高版本

## 5. 驱动兼容[](https://docs.mthreads.com#5-驱动兼容)

- 不兼容 2.5.x、2.6.x、2.7.x 版本
- 兼容 2.9.0、2.9.1 版本

## 6. 热升级版本支持[](https://docs.mthreads.com#6-热升级版本支持)

- 2.7.x → 2.9.0：不支持
- 2.9.0 → 2.9.1：支持 Windows 虚拟机热升级
- 2.9.1 → 2.9.2：支持 Windows 虚拟机热升级

## 7. 修复问题[](https://docs.mthreads.com#7-修复问题)

- 修复 Linux 双屏抓屏时可能出现花屏的问题
- 修复主机端出现 HWR 错误后无法恢复的问题

## 8. 其他使用说明[](https://docs.mthreads.com#8-其他使用说明)

- 在客户机中卸载驱动后，需要重启客户机，确保下一次安装客户机驱动工作正常

## 9. 已知问题[](https://docs.mthreads.com#9-已知问题)

- 使用 IDD 方式时，mtgpu-1132 类型与 QEMU Q35 机型的虚拟显卡不兼容，需要更换为
`pc-i440`

机型 - Kunpeng + Kylin 自带的影音播放器在商城更新后无法进行硬件解码
- 中望 CAD 软件商城版本在操作 2D 物体时比较卡顿
- Kylin Guest 中的影音播放器无法使用 GPU 硬件解码。使用
`QT_XCB_GL_INTEGRATION=xcb_egl`

环境变量启动播放器后，可以使用 GPU 硬件解码