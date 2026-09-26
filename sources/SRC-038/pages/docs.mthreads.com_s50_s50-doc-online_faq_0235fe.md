source: https://docs.mthreads.com/s50/s50-doc-online/faq

# 帮助（FAQ）

### 1.为什么有时会出现 3D 应用性能不高或者系统不稳？[](https://docs.mthreads.com#1为什么有时会出现-3d-应用性能不高或者系统不稳)

首先确认 System BIOS 设置，若是飞腾 D2000 平台，确保 PBF 大于等于 1.66；若是兆芯/海光/龙芯平台，确保开启 Above 4G 及 Resizable BAR。

### 2.兆芯/海光/龙芯平台如何确认 Resizable BAR 和 Above 4G 是否打开？[](https://docs.mthreads.com#2兆芯海光龙芯平台如何确认-resizable-bar-和-above-4g-是否打开)

在没有装显卡驱动的情况下，首先查询显卡的 Bus-Id，命令行为：lspci | grep VGA，如下图所示该显卡的 Bus-Id 为：04:00.0。

然后运行命令 lspci -vvvs 04:00.0， 查看显示的显存大小是否跟显卡硬件一致。如下图显示该显卡的显存为 4GB 与 MTT S30 4GB 硬件一致，说明已经打开 Resizable BAR 和 Above 4G。

### 3.为什么在安装操作系统过程中出现黑屏？[](https://docs.mthreads.com#3为什么在安装操作系统过程中出现黑屏)

统信 V20 1050 以及更新的版本/麒麟 V10 SP1 2303 以及更新的版本可以正常安装系统，若有旧版本操作系统安装需求，请联系销售人员或者技术支持人员。