source: https://docs.mthreads.com/digital-human/environment_setup

# 环境准备

注意

注意：本指南�目前只适用于 M1000 AImodule 环境，需要 AIOS 1.3.0 操作系统。

## Step0 确认环境[](https://docs.mthreads.com#step0-确认环境)

### 确认操作系统版本[](https://docs.mthreads.com#确认操作系统版本)

仅支持AIOS 1.3.0，查看当前操作系统版本的方法：

-
**方法一**： 查看设置 -> 关于 -> 操作系统系统名称 -
**方法二**： 命令行可执行`sudo dmidecode -t0`

- 有输出且 version = 1.3.0 则正常

- 若输出
`# No SMBIOS nor DMI entry point found, sorry.`

，请先和设备提供方确认设备是否是 AIOS 1.3.0.002。如果确认系统是 AIOS 1.3.0.002，建议重装musa (驱动) 和 musa-sdk (软件栈)，重装方法在文末 FAQ 章节


### 确认 musa 环境[](https://docs.mthreads.com#确认-musa-环境)

执行 `musaInfo`

，输出正常则环境配置正确。

如果报错未找到命令，执行：

`export PATH=/usr/local/musa-4.1.2/bin:${PATH}`

export LD_LIBRARY_PATH=/usr/local/musa-4.1.2/lib:${LD_LIBRARY_PATH}

# 再次执行 musaInfo，确认输出是否正常

musaInfo



## Step1 更新驱动[](https://docs.mthreads.com#step1-更新驱动)

### 1. 安装包下载和解压[](https://docs.mthreads.com#1-安装包下载和解压)

`wget -c https://mt-ai-data.tos-cn-shanghai.volces.com/vllm_musa/v1.3/release_M1000_1.3.0/20260116/musa%2Bm1000_release_1.3.0_20250623.tar.gz`

tar zxvf musa_m1000_release_1.3.0_20250623.tar.gz

cd musa_m1000_release_1.3.0_20250623



### 2. 安装脚本[](https://docs.mthreads.com#2-安装脚本)

`##################### 首先卸载当前驱动 ######################`

sudo dpkg -P musa-sdk

sudo dpkg -P musa # 输出 cryptsetup 的一些报错是正常的

sudo rm -rf /usr/local/musa*


##################### 安装新的驱动 ######################

sudo dpkg -i musa_3.1.3-AB100_arm64.deb

sudo dpkg -i musa-sdk_4.1.4-20251223_arm64.deb


##################### 重启电脑 ######################

sudo reboot



### 3. 输出说明[](https://docs.mthreads.com#3-输出说明)

提示

输出 firmware 相关的报错是正常的，可以忽略。

卸载和安装过程中可能会看到一些警告信息，如 `cryptsetup: ERROR: Couldn't resolve device /dev/root`

等，这些是正常的，可以忽略。

安装完成后，系统会提示需要重启：

`****************************************************************************`

* WARNING: The system needs to be restarted for MUSA driver! *

****************************************************************************



请按照提示重启系统。

## 【可选】打开性能模式（推荐）[](https://docs.mthreads.com#可选打开性能模式推荐)

### For T035 开发板[](https://docs.mthreads.com#for-t035-开发板)

#### From 界面 (推荐)[](https://docs.mthreads.com#from-界面-推荐)

界面右上角: 电源 -> 性能

#### From 命令行[](https://docs.mthreads.com#from-命令行)

首先执行 `sudo su`

进入 sudo 模式

| 模式 | 指令 |
|---|---|
High Performance（性能模式） | `echo 1 > /sys/devices/system/cpu/cpu8/online` `echo 1 > /sys/devices/system/cpu/cpu9/online` `echo 1 > /sys/devices/system/cpu/cpu10/online` `echo 1 > /sys/devices/system/cpu/cpu11/online` `echo performance > /sys/devices/system/cpu/cpufreq/policy0/scaling_governor` `echo performance > /sys/devices/system/cpu/cpufreq/policy4/scaling_governor` `echo performance > /sys/devices/system/cpu/cpufreq/policy8/scaling_governor` `echo perf > /sys/kernel/debug/musa/gpu00/dvfs_mode` `echo performance > /sys/class/thermal/thermal_zone6/perf_mode` |
Balance Mode（平衡模式） | `echo 1 > /sys/devices/system/cpu/cpu8/online` `echo 1 > /sys/devices/system/cpu/cpu9/online` `echo 1 > /sys/devices/system/cpu/cpu10/online` `echo 1 > /sys/devices/system/cpu/cpu11/online` `echo ondemand > /sys/devices/system/cpu/cpufreq/policy0/scaling_governor` `echo ondemand > /sys/devices/system/cpu/cpufreq/policy4/scaling_governor` `echo ondemand > /sys/devices/system/cpu/cpufreq/policy8/scaling_governor` `echo normal > /sys/kernel/debug/musa/gpu00/dvfs_mode` `echo balance > /sys/class/thermal/thermal_zone6/perf_mode` |
Power Saving（节电模式） | `echo powersave > /sys/devices/system/cpu/cpufreq/policy0/scaling_governor` `echo powersave > /sys/devices/system/cpu/cpufreq/policy4/scaling_governor` `echo powersave > /sys/devices/system/cpu/cpufreq/policy8/scaling_governor` `echo normal > /sys/kernel/debug/musa/gpu00/dvfs_mode` `echo powersave > /sys/class/thermal/thermal_zone6/perf_mode` `echo 0 > /sys/devices/system/cpu/cpu8/online` `echo 0 > /sys/devices/system/cpu/cpu9/online` `echo 0 > /sys/devices/system/cpu/cpu10/online` `echo 0 > /sys/devices/system/cpu/cpu11/online` |