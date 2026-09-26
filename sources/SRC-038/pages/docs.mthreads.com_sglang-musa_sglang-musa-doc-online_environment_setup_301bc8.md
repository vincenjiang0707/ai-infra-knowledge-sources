source: https://docs.mthreads.com/sglang-musa/sglang-musa-doc-online/environment_setup

# 环境准备

## 环境依赖[](https://docs.mthreads.com#环境依赖)

| 组件 | 版本要求 |
|---|---|
| MUSA Linux driver | 3.3.5 |
| mt-peermem | 1.4 |
| mtml | 2.2.0 |
| mt-container-toolkit | 2.1.0/2.2.0 |

-
`MUSA Linux driver`

和`mt-peermem`

包含在 MUSA SDK 中，参考[下载及文档](https://www.mthreads.com/product/MUSASDK)。 -
`mt-container-toolkit`

包含在 KUAE 云原生套件中，参考[下载及文档](https://www.mthreads.com/product/CloudNativeSuite)。 -
`mtml`

参考[安装指南](https://docs.mthreads.com/gmc/gmc-doc-online/mtml/install_guide)。

## 环境检测[](https://docs.mthreads.com#环境检测)

`# 检查基础配置`

dpkg -l | grep -iE 'musa|mtml|mt-peermem|mt-container-toolkit|mthreads'


# 检查 GMI

mthreads-gmi



**基础配置输出结果参考**

`mccxadmin@mccx-173:~$ dpkg -l | grep -iE 'musa|mtml|mt-peermem|mt-container-toolkit|mthreads'`

ii mt-container-toolkit 2.1.0-1 amd64 MT Container Toolkit

ii mt-peermem 1.4 amd64 mt-peermem driver in DKMS format.

ii mtml 2.2.0 amd64 mt-management

ii musa 3.3.5-server amd64 Moore Threads MUSA driver




**mthreads-gmi信息参考**

`---------------------------------------------------------------------`

mthreads-gmi:2.3.2 Driver Version:3.3.5-server

---------------------------------------------------------------------

ID Name |PCIe |%GPU Mem

0 MTT S5000 |00000000:03:00.0 |0% 1428MiB(81920MiB)

...

---------------------------------------------------------------------



## GPU 内核模块参数配置[](https://docs.mthreads.com#gpu-内核模块参数配置)

首先通过 `mthreads-gmi mtlink -s`

命令查看 MTLink 状态。如果个别 GPU 的 LINK 不处于 UP 状态，联系售后诊断处理。如果输出 `Error: the requested operation is not available on target device`

, 则需要在内核模块参数配置 MTLink。

Decode 节点默认使用 ** DEEPEP_MODE=low_latency** 以降低时延。 在

**Decode 节点宿主机**（非容器内），配置摩尔线程 GPU 内核模块参数，使 PCIe 与 Mellanox InfiniBand 设备（vendor

**0x15B3**）路径一致，避免传输栈不匹配导致的异常。

-
编辑（或新建）

`/etc/modprobe.d/mtgpu.conf`

，在文件中增加配置（若已有其他`options mtgpu`

，可与厂商文档核对后合并）：options mtgpu enable_mtlink=1 mtlink_timer_expires=120000options mtgpu tp_pci_ob_enable=1 tp_pci_vender_id=0x15B3 -
保存后使配置生效任选其一：

- 推荐方式：
**重新打包内核 initramfs 镜像并重启**；`sudo update-initramfs -u -k "$(uname -r)" && sudo reboot`

- 维护窗口内卸载并重载模块：
`sudo modprobe -r mtgpu && sudo modprobe mtgpu`

（会中断当前 GPU 作业，若模块 busy 只能重启）。

- 推荐方式：
-
通过如下命令查看输出结果是否为

，`1`

及`1`

，用于确认模块已按预期加载：`5555`


`cat /sys/module/mtgpu/parameters/enable_mtlink`

cat /sys/module/mtgpu/parameters/tp_pci_ob_enable

cat /sys/module/mtgpu/parameters/tp_pci_vender_id



## RDMA 网卡检测[](https://docs.mthreads.com#rdma-网卡检测)

在 PD 分离部署模式中, 通过服务启动脚本中的 `--disaggregation-ib-device`

参数，指定 Prefill 与 Decode 节点之间 KV Cache 传输所使用的 RDMA 设备。该参数需与链路状态为 `Up`

的高速 RDMA HCA 设备名保持一致。请在宿主机或容器中运行如下脚本获取高速 RDMA 设备名列表，填入启动 Prefill 和 Decode 服务的参数中。例如 `--disaggregation-ib-device mlx5_2,mlx5_3,mlx5_4,mlx5_5,mlx5_8,mlx5_9,mlx5_10,mlx5_11`


确保运行一个模型服务的多台机器在同一个 RDMA 网段中，避免中转延迟造成通信或 KV Cache 传输超时。

每台机器的高速 RDMA 设备名列表可能不同，为减少手工操作，文档中部分启动脚本示例已包含以下检测代码，或者以脚本调用方式获取设备列表。

`#!/bin/bash`


IB_DEVS=()


for dev in /sys/class/infiniband/*; do

ibdev=$(basename "$dev")

for port in "$dev"/ports/*; do

# 速率（如 200 Gb/sec）

rate=$(cat "$port/rate" 2>/dev/null)

# link_layer: InfiniBand / Ethernet (RoCE)

link=$(cat "$port/link_layer" 2>/dev/null)

# 状态为 Up

state=$(cat "$port/state" 2>/dev/null)

# 只要是 200G/400G 且状态为 Up（IB 或 RoCE 都收）

if [[ "$rate" == *"200 Gb"* || "$rate" == *"400 Gb"* ]] && [[ "$state" == "4"* ]]; then

IB_DEVS+=("$ibdev")

break

fi

done

done

# 排序 + 去重

IB_DEVS_SORTED=$(printf "%s\n" "${IB_DEVS[@]}" | sort -V | uniq)

# 生成 MCCL / SGLang 变量

SGLANG_DISAGGREGATION_IB_DEVICES=$(echo "$IB_DEVS_SORTED" | paste -sd, -)

export SGLANG_DISAGGREGATION_IB_DEVICES

echo "IB_DEVICES=$SGLANG_DISAGGREGATION_IB_DEVICES"



## 业务网络网卡检测[](https://docs.mthreads.com#业务网络网卡检测)

启动推理服务时，系统环境变量 `GLOO_SOCKET_IFNAME`

`TP_SOCKET_IFNAME`

用于指定分布式进程初始化时 TCP socket 绑定的网络接口。主要用于节点发现和控制消息，数据量较小，不涉及 GPU 数据传输，需要配置普通以太网网卡（业务网络），而不是RDMA网卡。

MCCL 在多网卡机器上需选用业务网络接口建立 Bootstrap TCP 连接做节点间/Rank 间通信。如果 `hostname -i`

输出的不是业务网络，MCCL可能识别错误。为防止自动探测选到 lo / docker0 / 管理网卡导致超时，请设置环境变量 `MCCL_SOCKET_IFNAME`

绑定业务网络接口。

请使用以下脚本确定绑定接口（通常为 `bond0`

），然后启动容器时或启动推理服务前，对上述环境变量进行设置。

为减少手工操作，文档中启动容器及部署脚本示例已包含 `GLOO_SOCKET_IFNAME`

及 `TP_SOCKET_IFNAME`

环境变量设置，但不包含 `MCCL_SOCKET_IFNAME`

设置。请根据实际情况修改。
如果脚本输出为空，请先联系服务器管理员进行网络配置诊断。

` #!/bin/bash`


choose_control_nic() {


for iface in $(ls /sys/class/net); do


# 排除虚拟网卡

[[ "$iface" =~ ^(lo|docker|veth|virbr|br-|flannel|cni) ]] && continue


# 必须UP

state=$(cat /sys/class/net/$iface/operstate 2>/dev/null)

[[ "$state" != "up" ]] && continue


# 必须有IPv4

ip=$(ip -o -4 addr show $iface | awk '{print $4}')

[[ -z "$ip" ]] && continue


# 排除RDMA网卡

if [ -d /sys/class/net/$iface/device/infiniband ]; then

continue

fi


# 获取速率

speed=$(cat /sys/class/net/$iface/speed 2>/dev/null)


# 选择 >=25G

if [[ "$speed" -ge 25000 ]]; then

echo $iface

return

fi

done

}


IFACE=$(choose_control_nic)


if [[ -z "$IFACE" ]]; then

echo "No suitable control NIC found"

exit 1

fi


echo "Selected control NIC: $IFACE"



## 启动容器[](https://docs.mthreads.com#启动容器)

在 **每台参与推理的机器**（Prefill 节点、Decode 节点等）上执行容器启动命令，示例如下：

-
将 [DOCKER_IMAGE_ADDRESS] 替换为 “版本发布信息” 章节中的镜像地址，请根据 CPU 平台及所需模型选择。

-
根据实际情况修改 /mnt/shared/** 路径，作为宿主机上的共享存储目录，存放模型、启动脚本、日志文件等。


`docker run -d \`

--env MTHREADS_VISIBLE_DEVICES=0,1,2,3,4,5,6,7 \

--env MTHREADS_DRIVER_CAPABILITIES=all \

--env GLOO_SOCKET_IFNAME="bond0" \

--env TP_SOCKET_IFNAME="bond0" \

--net host \

--privileged \

--pid=host \

--pids-limit=65536 \

--shm-size 500g \

-v /mnt/shared/models:/data/models \

-v /mnt/shared/workspace:/data/workspace \

--name sglang-service \

[DOCKER_IMAGE_ADDRESS] \

bash -c 'apt-get update && apt-get install -y openssh-server && mkdir -p /var/run/sshd && sed -i "s/#PermitRootLogin prohibit-password/PermitRootLogin yes/" /etc/ssh/sshd_config && sed -i "s/^#\?Port .*/Port 62216/" /etc/ssh/sshd_config && service ssh start && sleep infinity'



| 参数 | 说明 |
|---|---|
`MTHREADS_VISIBLE_DEVICES` | 根据实际需要使用的 GPU 卡数配置 |
`GLOO_SOCKET_IFNAME` `TP_SOCKET_IFNAME` | 指定分布式通信使用的业务网网卡绑定接口，按实际接口名更改。 |
`--privileged` | 多机 MCCL 通信依赖容器以特权模式启动，单机可拉起模型建议删除该参数提高安全性，并保证 torch profiler 正常运行。 |
`-v /mnt/shared/models:/data/models` | 宿主机模型目录挂载，按需更改。 |
`-v /mnt/shared/workspace:/data/workspace` | 宿主机工作目录挂载，存放启动脚本、配置、日志等文件，按需更改。 |
`--name sglang-service` | 容器名称，按需更改。 |
| bash命令 | 容器内安装 `openssh-server` ，端口默认 62216，并允许 root 用户通过密码直接登录服务器。 |

上述容器启动脚本以及下面服务部署方法中涉及多节点部署方案的，均默认所有节点运行的容器都��共享同一个存储，绑定到容器相同的模型和工作目录路径下。

## 进入容器环境[](https://docs.mthreads.com#进入容器环境)

在 **每台参与推理的机器**（Prefill 节点、Decode 节点等）上执行命令进入容器环境，示例如下：

` docker exec -ti sglang-service bash`