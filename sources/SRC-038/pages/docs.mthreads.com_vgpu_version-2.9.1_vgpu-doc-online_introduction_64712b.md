source: https://docs.mthreads.com/vgpu/version-2.9.1/vgpu-doc-online/introduction

# 产品介绍

MT vGPU 是摩尔线程 GPU 虚拟化的整体产品名称。摩尔线程 GPU 作为重要的算力，软件开发并提供了 GPU 虚拟化技术，满足数据中心中以 GPU 直通、vGPU 的方式使用 GPU 的需求。摩尔线程通过 PCIe Passthrough 技术支持 GPU 直通，通过软件截获直通的方式开发了 vGPU 驱动，并在后续产品中会支持基于 SR-IOV 方案。整体的软件产品通过 MT vGPU 的软件产品形态提供。虚拟化出来的 vGPU 的功能与物理 GPU 设备形态上完全一致，向上可以支持虚拟机中的业务运行。

虚拟化系统的架构图如下图所示：