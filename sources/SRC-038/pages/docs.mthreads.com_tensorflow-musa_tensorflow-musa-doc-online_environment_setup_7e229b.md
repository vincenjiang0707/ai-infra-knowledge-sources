source: https://docs.mthreads.com/tensorflow-musa/tensorflow-musa-doc-online/environment_setup

# 环境准备

## 宿主机环境依赖[](https://docs.mthreads.com#宿主机环境依赖)

| 组件 | 版本要求 |
|---|---|
| MUSA Linux driver | 5.1.0 / 3.3.5 |
| mtml | 2.2.0 |
| mt-container-toolkit | 2.2.0 |

-
`MUSA Linux driver`

包含在 MUSA SDK 中，参考[下载及文档](https://www.mthreads.com/product/MUSASDK)。 -
`mt-container-toolkit`

包含在 KUAE 云原生套件中，参考[下载及文档](https://www.mthreads.com/product/CloudNativeSuite)。 -
`mtml`

参考[安装指南](https://docs.mthreads.com/gmc/gmc-doc-online/mtml/install_guide)。

## 宿主机环境检测[](https://docs.mthreads.com#宿主机环境检测)

`# 检查基础配置`

dpkg -l | grep -iE 'musa|mtml|mt-container-toolkit|mthreads'


# 检查 GMI

mthreads-gmi



**基础配置输出结果参考**

`mccxadmin@mccx-173:~$ dpkg -l | grep -iE 'musa|mtml|mt-peermem|mt-container-toolkit|mthreads'`

ii mt-container-toolkit 2.2.0-1 amd64 MT Container Toolkit

ii mtml 2.2.0 amd64 mt-management

ii musa 5.1.0-server amd64 Moore Threads MUSA driver




**mthreads-gmi信息参考**

`---------------------------------------------------------------------`

mthreads-gmi:2.3.2 Driver Version:5.1.0-server

---------------------------------------------------------------------

ID Name |PCIe |%GPU Mem

0 MTT S5000 |00000000:03:00.0 |0% 1428MiB(81920MiB)

...

---------------------------------------------------------------------



## 启动容器环境[](https://docs.mthreads.com#启动容器环境)

**拉取镜像**

`# MUSA SDK 5.1.0（推荐）`

docker pull registry.mthreads.com/presale/devtech/tensorflow_musa:5.1.0_20260623


# MUSA SDK 4.3.5

docker pull registry.mthreads.com/presale/devtech/tensorflow_musa:4.3.5_20260624



**启动容器**

`docker run -it --rm \`

--name tf_musa \

--privileged \

-v /path/to/dataset:/data \

-v /path/to/tensorflow_musa_playground:/workspace/playground \

registry.mthreads.com/presale/devtech/tensorflow_musa:5.1.0_20260623 \

/bin/bash




说明：`--privileged`

使容器能访问宿主机的 MUSA GPU 设备（`/dev/mtgpu.*`

）。

## 验证 MUSA 环境[](https://docs.mthreads.com#验证-musa-环境)

运行以下命令确认 MUSA 设备可见：

`import tensorflow as tf`

import tensorflow_musa


print("TensorFlow 版本:", tf.__version__)

devices = tf.config.list_physical_devices("MUSA")

print(f"MUSA 设备数: {len(devices)}")

for d in devices:

print(f" {d}")



预期输出（以 8 卡环境为例）：

`TensorFlow 版本: 2.15.1`

MUSA 设备数: 8

PhysicalDevice(name='/physical_device:MUSA:0', device_type='MUSA')

PhysicalDevice(name='/physical_device:MUSA:1', device_type='MUSA')

...

PhysicalDevice(name='/physical_device:MUSA:7', device_type='MUSA')