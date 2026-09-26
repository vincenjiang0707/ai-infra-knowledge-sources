source: https://docs.opencloudos.org/OCS/Install_Guide/ocs-cvm/

# 使用虚拟机镜像安装

## 1. 镜像概述

OpenCloudOS Stream 提供 qcow2 镜像，qcow2镜像启动后不需要手动选择安装，启动后就是一个正常可使用的OS环境，镜像内默认安装系统所需基本组件，镜像已配置好YUM源，如需安装或升级RPM包，可以直接通过`dnf`

命令安装、更新。

## 2. 镜像部署使用

### 2.1 下载地址

#### OpenCloudOS Stream（ocs）

- 下载地址：
[http://mirrors.opencloudos.tech/opencloudos-stream/releases/23/images/](http://mirrors.opencloudos.tech/opencloudos-stream/releases/23/images/) - 默认账户：
`root`

- 默认密码：
`Dis@init3`


#### OpenCloudOS 9（oc9）

- 下载地址：
[https://mirrors.opencloudos.org/opencloudos/9/images/qcow2/](https://mirrors.opencloudos.org/opencloudos/9/images/qcow2/) - 默认账户：
`opencloudos`

- 默认密码：
`opencloudos`


### 2.2 部署前环境准备

推荐使用qemu+libvirt方式部署镜像

#### 2.2.1 安装虚拟化组建

```
dnf install qemu libvirt -y
```


#### 2.2.2 启动libvirtd服务

```
systemctl start libvirtd
```


#### 2.2.3 准备镜像

将qcow2镜像下载到libvirt可以访问的目录，如`/var/lib/libvirt/images/`

。

#### 2.2.4 准备网络环境

创建的虚拟机如果需要使用母机的网络，需要在母机上创建网桥。

```
nmcli connection add type bridge con-name br0 ifname br0
nmcli connection up br0
```


将所需要使用的网络的网口添加到网桥中，如eth0

```
nmcli connection add type bridge-slave con-name eth0 ifname eth0 master br0
nmcli connection up eth0
```


通过dhclient获取br0的ip

```
dhclient br0
```


### 2.3 libvirt方式部署

#### 2.3.1 创建XML

这里给出一个最简单的libvirt XML文件`test.xml`

用以创建虚拟机，可以根据需要自行进行修改。

```
<domain type='kvm' xmlns:qemu='http://libvirt.org/schemas/domain/qemu/1.0'>
<name>OpenCloudOS</name>
<memory unit='GiB'>1</memory>
<vcpu>4</vcpu>
<os>
<type arch='x86_64'>hvm</type>
</os>
<features>
<acpi/>
</features>
<cpu mode='host-passthrough'>
<topology sockets='2' cores='2' threads='1'/>
</cpu>
<iothreads>1</iothreads>
<clock offset='utc'/>
<on_poweroff>destroy</on_poweroff>
<on_reboot>restart</on_reboot>
<on_crash>restart</on_crash>
<devices>
<emulator>/usr/bin/qemu-system-x86_64</emulator>
<disk type='file' device='disk'>
<driver name='qemu' type='qcow2' iothread="1"/>
<source file='/var/lib/libvirt/images/OpenCloudOS-Stream-23-20230524.0259-x86_64.qcow2'/>
<target dev='vda' bus='virtio'/>
<boot order='1'/>
</disk>
<interface type='bridge'>
<mac address='52:54:00:A1:B2:C3'/>
<source bridge='br0'/>
<model type='virtio'/>
<address type='pci' domain='0x0000' bus='0x00' slot='0x03' function='0x0'/>
</interface>
<controller type='scsi' index='0' model='virtio-scsi' />
<controller type='virtio-serial' index='0' />
<controller type='usb' index='0' model='ehci' />
<controller type='sata' index='0' />
<controller type='pci' index='0' model='pci-root'/>
<controller type='usb' model='ehci'/>
<input type='tablet' bus='usb'/>
<input type='keyboard' bus='usb'/>
<graphics type='vnc' listen='0.0.0.0' passwd='n8VfjbFK'/>
<serial type='pty'>
<target port='0'/>
</serial>
<console type='pty'>
<target type='serial' port='0'/>
</console>
</devices>
<seclabel type='dynamic' model='dac' relabel='yes'/>
</domain>
```


将XML中的`<source file='/var/lib/libvirt/images/OpenCloudOS-Stream-23-20230524.0259-x86_64.qcow2'/>`

替换为所需要安装的qcow2镜像路径。

虚拟机配置可以参考**《虚拟化用户指南》**章节.

#### 2.3.2 启动虚拟机

```
virsh create test.xml
```


### 2.4 qemu方式部署

可以通过直接执行 `qemu-system-*`

二进制程序，结合命令行参数启动 OpenCloudOS 虚拟机。以下为启动命令示例，参数可根据实际需求进行调整。

启动 x86_64 虚拟机命令示例:

```
qemu-system-x86_64 \
-m 8192 -smp 4 -cpu host \
-drive file=/var/lib/libvirt/images/OpenCloudOS-Stream-23-20230524.0259-x86_64.qcow2,bus=0,unit=0,media=disk \
-serial telnet:0.0.0.0:9999,server=on,wait=on,nodelay=on \
-vnc :0 \
-nographic
```


启动 loongarch64 虚拟机命令示例:

```
qemu-system-loongarch64 \
-accel tcg \
-m 4096 -smp 4 \
-machine virt -cpu la464 \
-bios /usr/share/edk2/loongarch64/QEMU_EFI.fd \
-drive file=/home/OpenCloudOS-GenericCloud-9.4-20250514.1.loongarch64-2.qcow2,if=virtio \
-device virtio-gpu-pci \
-vnc :1 \
-serial mon:stdio \
-netdev user,id=net0,hostfwd=tcp::6666-:22 \
-device e1000,netdev=net0
```


## 3. 注意事项

### 3.1 aarch64机器

在aarch64机器上创建qemu虚拟机，XML中的一些配置项需要做如下调整：

- aarch64虚拟机需要引导固件帮助启动。可以通过安装edk2-aarch64组件，然后在
标签新增如下配置完成。

```
<loader readonly='yes' type='pflash'>/usr/share/AAVMF/AAVMF_CODE.fd</loader>
<nvram>/usr/share/edk2/aarch64/QEMU_VARS.fd</nvram>
```


- 需要在type中指定
`machine='virt'`

。

```
<type arch='aarch64' machine='virt'>hvm</type>
```


除此之外，还需要安装seavgabios-bin组件

```
dnf install seavgabios-bin -y
```


### 3.2 CPU指令集

如果虚拟机CPU型号未显示指定，默认仅支持指令集 **x86_64-v1**，而当前编译的 glibc，编译时指定了编译选项 `-march=x86_64-v2`

，仅支持运行在 x86_64-v2 及以上环境，所以会导致虚拟机启动失败。启动时有如下报错：

```
[ 4.605199] x86/mm: Checked W+X mappings: passed, no W+X pages found.
[ 4.606044] Run /bin/bash as init process
[ 4.627350] traps: bash[1] trap invalid opcode ip:7f0a751f4da6 sp:7ffd97579870 error:0 in ld-linux-x86-64.so.2[7f0a751d8000+27000]
[ 4.631539] Kernel panic - not syncing: Attempted to kill init! exitcode=0x00000004
[ 4.632068] CPU: 0 PID: 1 Comm: bash Not tainted 5.18.15-2207.2.0.ocks #1
[ 4.632397] Hardware name: QEMU Standard PC (i440FX + PIIX, 1996), BIOS 1.16.0-1.fc37 04/01/2014
[ 4.632870] Call Trace:
[ 4.633501] <TASK>
[ 4.633749] dump_stack_lvl+0x33/0x46
[ 4.634132] panic+0x106/0x2ab
[ 4.634306] do_exit.cold+0x15/0x15
[ 4.634465] do_group_exit+0x2d/0x90
[ 4.634640] get_signal+0x975/0x980
[ 4.634800] arch_do_signal_or_restart+0x25/0x100
[ 4.635019] exit_to_user_mode_prepare+0xf0/0x130
[ 4.635218] irqentry_exit_to_user_mode+0x5/0x30
[ 4.635404] asm_exc_invalid_op+0x15/0x20
[ 4.635727] RIP: 0033:0x7f0a751f4da6
[ 4.636191] Code: 8d 03 00 00 48 8b 49 08 40 84 ff 4c 8b 05 aa 8e 01 00 4a 8d 34 21 48 0f 45 ce 48 8b 35 93 8d 01 00 48 8b 76 08 66 48 0f 6e c1 <66> 48 0f 3a 22 c6 01 0f 29 45 90 4d 85 c0 74 08 4d 8b 40 08 4c 89
[ 4.636929] RSP: 002b:00007ffd97579870 EFLAGS: 00000246
[ 4.637163] RAX: 00007f0a7520ceb0 RBX: 00007ffd97579930 RCX: 00007f0a751d6d78
[ 4.637439] RDX: 0000000000000000 RSI: 0000000000000d98 RDI: 0000000000000000
[ 4.637717] RBP: 00007ffd97579920 R08: 00007f0a7520cf50 R09: 00007f0a7520cec0
[ 4.637987] R10: 0000000000000032 R11: 000000006ffffdff R12: 00007f0a751d6000
[ 4.638253] R13: 0000000000000000 R14: 0000000000000000 R15: 0000000000000000
[ 4.638586] </TASK>
[ 4.639085] Kernel Offset: disabled
[ 4.639465] Rebooting in 180 seconds..
```


所以在配置XML时需要指定CPU使用母机相同类型，例如给出示例中的`<cpu mode='host-passthrough'>`

或者`<cpu mode='host-model'/>`

或者`-cpu host`

。