source: https://docs.mthreads.com/s30/s30-doc-online/install_guide/

# 安装指导

## 1 硬件环境确认[](https://docs.mthreads.com#1-硬件环境确认)

将显卡 PCIe 接口插入至主板 PCIe 插槽并确保锁固。

## 2 BIOS 设置确认[](https://docs.mthreads.com#2-bios-设置确认)

1.飞腾 D2000 平台

确认主板 System BIOS 中的 PBF（Phytium Based Firmware）版本为 1.66 或比 1.66 更新的版本。请务必和 System BIOS 工程师或主板厂商确认，如果 PBF 版本低于 1.66， 容易出现 3D 性能不稳定的情况。

2.兆芯/海光/龙芯平台

确认主板 System BIOS 需要开启 Above 4G 和 Resizable BAR 功能（在不同主板上，上述功能命名可能会不同）。请务必和 System BIOS 工程师或主板厂商确认，若未打开就不能解锁 CPU 访问显存的限制，从而导致显卡性能不能完全释放。

## 3 操作系统准备[](https://docs.mthreads.com#3-操作系统准备)

1.定制版本下载

摩尔线程官网提供了统信桌面操作系统 V20 1050 update3 和银河麒麟桌面操作系统 V10 SP1 2303 的镜像下载链接，该操作系统镜像已经集成摩尔线程显卡驱动。

摩尔线程链接： [https://www.mthreads.com/product/S10](https://www.mthreads.com/product/S10)

2.操作系统官网下载

桌面操作系统镜像也可以从统信网站或者麒麟软件官方网站获得。

统信桌面操作系统链接：[https://www.chinauos.com/resource/download-professional](https://www.chinauos.com/resource/download-professional)

麒麟软件官网链接：[https://www.kylinos.cn/](https://www.kylinos.cn/)

## 4 显卡驱动安装[](https://docs.mthreads.com#4-显卡驱动安装)

摩尔线程显卡驱动提供了图形化安装和终端命令行安装两种安装方式，显卡驱动版本请咨询销售人员或者技术支持人员。本章以麒麟 V10 SP1 2303 系统为例进行两种安装方式展示，并提供查询显卡驱动版本的方法。

### 4.1 图形化安装显卡驱动[](https://docs.mthreads.com#41-图形化安装显卡驱动)

1.将显卡驱动 deb 文件拷贝至计算机本地（如系统桌面），双击 deb 文件，在弹出的安装器窗口中点击“一键安装”：

2.输入系统用户密码，点击“授权”：

3.点击“允许”安装：

4.显示驱动安装进度：

5.驱动安装完成：

6.重启系统后显卡驱动生效。

### 4.2 终端命令行安装显卡驱动[](https://docs.mthreads.com#42-终端命令行安装显卡驱动)

1.在显卡驱动文件所在目录打开终端 Terminal 窗口，输入命令：“sudo dpkg -i 驱动包名.deb”并回车（本例中驱动包为 musa_2.5.0-Kylin_amd64.deb），按照提示输入系统用户密码：

2.点击“允许”安装：

3.显示驱动安装进度：

4.驱动安装完成：

5.重启系统后显卡驱动生效。

### 4.3 驱动版本查询[](https://docs.mthreads.com#43-驱动版本查询)

1.打开终端 Terminal 窗口，输入命令：“dpkg -s musa”查询驱动版本，如下图所示驱动版本为 2.5.0-Kylin。

## 5 显卡驱动卸载[](https://docs.mthreads.com#5-显卡驱动卸载)

摩尔线程显卡驱动提供了终端命令行卸载和图形化卸载两种驱动卸载方式，麒麟系统只有终端命令行卸载，统信系统支持两种卸载方式。本章以麒麟 V10 SP1 2303 为例展示终端命令行卸载，以统信 V20 1060 为例展示图形化卸载。

### 5.1 终端命令行卸载显卡驱动[](https://docs.mthreads.com#51-终端命令行卸载显卡驱动)

1.打开终端 Terminal 窗口，输入命令：“dpkg -P musa”并回车：

2.输入系统用户密码之后，显示驱动卸载进度：

3.驱动卸载完成：

4.重启系统。

### 5.2 图像化卸载显卡驱动[](https://docs.mthreads.com#52-图像化卸载显卡驱动)

1.通过 deb 安装包卸载，双击安装包，点击“卸载：

2.点击“确定卸载”：

3.输入系统用户密码后点击“确定”：

4.驱动卸载进度：

5.提示“卸载成功”：

6.重启系统。