source: https://docs.mthreads.com/codec/codec-doc-online/capture_user_guide

# MTCapture 2.0 编程指南

## 概述[](https://docs.mthreads.com#概述)

### 什么是 MTCapture？[](https://docs.mthreads.com#什么是mtcapture)

MTCapture 是摩尔线程（MooreThreads）推出的高性能桌面采集编码流化的软件开发套件（SDK），专为 MT 系列 GPU 设计。 支持从显存中直接获取桌面送显图像，并交由 GPU 完成桌面图像的编码压缩。

它解决了传统桌面图像采集与编码压缩方案中的三大核心痛点：

-
**高延迟**：CPU 中转导致帧传输延迟高，难以满足实时交互需求； -
**带宽瓶颈**：4K/8K 高帧率桌面，图像数据量大，在系统内存和显存之间传递数据时，PCIe 带宽易成为瓶颈； -
**生态割裂**：不同系统，桌面环境差异大，需对接不同抓屏编码接口 -
**高资源消耗**：CPU 直接复制桌面图像，且由 CPU 进行桌面图像编码压缩时，内存和 CPU 资源消耗高；

MTCapture 通过 GPU 内置的专用视频编码硬件单元（Video Processing Unit - VPU）与 **MUSA 统一系统架构**深度协同，实现“采集即编码压缩”，让桌面图像在显示同时，直接进入 VPU 进行编码压缩，生成压缩后的高压缩码流。

### 功能特性[](https://docs.mthreads.com#功能特性)

-
**兼容性好**：支持主流的 Linux 操作系统，以及 Xorg 或者 Wayland 桌面环境 -
**延迟低**：GPU 显存中的桌面图像，无需经过 CPU 拷贝，直接送入到 VPU -
**资源消耗低**：GPU 显存中的桌面图像，转换后直接送入 VPU，无需过多 GPU 资源 -
**帧率自适应**：桌面的采集及编码压缩与桌面更新率一致

### 典型应用场景[](https://docs.mthreads.com#典��型应用场景)

-
**数字孪生**：中心节点渲染的画面，视频推送在终端节点的显示 -
**直播推流**：桌面高清桌面采集与编码压缩一体成型 -
**云桌面**：虚拟机画面的低延迟采集与编码压缩

## 架构与工作原理[](https://docs.mthreads.com#架构与工作原理)

### 整体架构[](https://docs.mthreads.com#整体架构)

MTCapture 的数据流如下：

整个过程无需 CPU 参与，避免了 PCIe 回读和内存拷贝开销。

## 快速开始[](https://docs.mthreads.com#快速开始)

### 系统要求[](https://docs.mthreads.com#系统要求)

-
**GPU**：MooreThreads -
**驱动**：MUSA Driver ≥ v5.1.0 -
**操作系统**：Linux

### 安装 MUSA 驱动[](https://docs.mthreads.com#安装musa-驱动)

-
从

[developer.mthreads.com](https://developer.mthreads.com/)下载`MT Linux Driver`

-
安装驱动，并重启

-
下载

[DirectStream sdk](https://developer.mthreads.com/sdk/DirectStream)，获取 Header 及 Sample

### 使用方法[](https://docs.mthreads.com#使用方法)

-
加载

`libencode_musa.so`

，并获取`MTEncodeAPICreateInstance`

函数接口 -
通过

`MTEncodeAPICreateInstance`

，创建instance，获取默认配置参数，或者设定自定义参数 -
调用

`mtEncEncodeDesktop`

抓取桌面并编码出码流 -
读取编码出的码流，并循环调用

`mtEncEncodeDesktop`

进行持续抓屏编码 -
退出抓屏编码，释放资源


#### 伪代码如下[](https://docs.mthreads.com#伪代码如下)

`#include <mtEncodeAPI.h>`


hModule = Load library(mtencodeapi64.dll/libencode_musa.so);

pfCreateInstance = Get Address of "MTEncodeAPICreateInstance";

MT_ENCODE_API_FUNCTION_LIST m_mtEnc = {};

pfCreateInstance(&m_mtEnc);

m_mtEnc.mtEncCreateEncoder(&createEncoderParams, &m_hEncoder)


// get preset configuration

MT_ENC_PRESET_CONFIG presetConfig = {};

m_mtEnc.mtEncGetPresetConfig(m_hEncoder, ...);

// configuration parameters here...


// init encoder

m_mtEnc.mtEncInitEncoder(m_hEncoder, ...)


// create input and output buffers

m_mtEnc.mtEncCreateOutputBuffer(m_hEncoder, ...)


while (1) {

// fill data into an input buffer

// encode frame

m_mtEnc.mtEncEncodeDesktop(m_hEncoder, ...)

// get bitstream

m_mtEnc.mtEncLockOutputBuffer(m_hEncoder, ...)

m_mtEnc.mtEncUnlockOutputBuffer(m_hEncoder, ...)

}


// release resource & destroy encoder

m_mtEnc.mtEncReleaseOutputBuffer(m_hEncoder, ...)

m_mtEnc.mtEncReleaseEncoder(m_hEncoder)

Free Library(hModule)



### 实例重启[](https://docs.mthreads.com#实例重启)

由于�抓屏编码一体化，针对不同的桌面分辨率或者显示设置，使用的显存大小不同。故当桌面的显示设置发生变化时， 需要重启实例。在启动过程中，会自动检测桌面显示参数设置，并完成实例参数的配置。具体的做法如下：

-
监听

`MT_ENC_ERR_RESOLUTION_MISMATCHED`

； -
获取最新的桌面分辨率参数；

-
重建实例。


#### 需要重启实例的场景[](https://docs.mthreads.com#需要重启实例的场景)

| 场景 | 配置 |
|---|---|
| 分辨率 | 扩大、缩小 |
| 旋转 | 0/90/180/270 |

### 功能列表[](https://docs.mthreads.com#功能列表)

| 功能 | 特性 | 备注 |
|---|---|---|
| 桌面环境 | Xorg/Wayland | |
| 事件上报 | 显示配置变化 | |
| 编码加速 | VPU加速编码 | 支持H264/h265/av1 |
| 抓屏模式 | 自适应桌面刷新等 | |
| 分辨率 | 最大8K | |
| 多路并发 | 无最大路数限制 | 受限显存等因素 |