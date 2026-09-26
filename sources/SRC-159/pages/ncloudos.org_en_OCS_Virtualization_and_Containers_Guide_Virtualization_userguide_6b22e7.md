source: https://docs.opencloudos.org/en/OCS/Virtualization_and_Containers_Guide/Virtualization_userguide/

# 虚拟化用户指南

# 1. 安装虚拟化组件

## 1.1 kvm模块

当前系统默认支持qemu-kvm虚拟化。KVM模块当前内核默认开启编译支持，无需再手动安装。当前系统支持INTEL的VT-X以及AMD的AMD-V虚拟化技术。

```
CONFIG_KVM_GUEST=y
CONFIG_HAVE_KVM=y
CONFIG_HAVE_KVM_PFNCACHE=y
CONFIG_HAVE_KVM_IRQCHIP=y
CONFIG_HAVE_KVM_IRQFD=y
CONFIG_HAVE_KVM_IRQ_ROUTING=y
CONFIG_HAVE_KVM_DIRTY_RING=y
CONFIG_HAVE_KVM_DIRTY_RING_TSO=y
CONFIG_HAVE_KVM_DIRTY_RING_ACQ_REL=y
CONFIG_HAVE_KVM_EVENTFD=y
CONFIG_KVM_MMIO=y
CONFIG_KVM_ASYNC_PF=y
CONFIG_HAVE_KVM_MSI=y
CONFIG_HAVE_KVM_CPU_RELAX_INTERCEPT=y
CONFIG_KVM_VFIO=y
CONFIG_KVM_GENERIC_DIRTYLOG_READ_PROTECT=y
CONFIG_KVM_COMPAT=y
CONFIG_HAVE_KVM_IRQ_BYPASS=y
CONFIG_HAVE_KVM_NO_POLL=y
CONFIG_KVM_XFER_TO_GUEST_WORK=y
CONFIG_HAVE_KVM_PM_NOTIFIER=y
CONFIG_KVM=m
CONFIG_KVM_INTEL=m
CONFIG_X86_SGX_KVM=y
CONFIG_KVM_AMD=m
CONFIG_KVM_AMD_SEV=y
```


`lscpu`

命令查看当前系统支持的虚拟化技术
```
Virtualization features:
Virtualization: VT-x
Hypervisor vendor: KVM
Virtualization type: full
```


## 1.2 qemu组件

系统不会默认安装`qemu`

组件，需要通过`dnf`

方式安装：

```
dnf install -y qemu
```


`qemu`

相关组件与架构相关，YUM源根据系统已自动屏蔽架构，只需要指定`qemu`

即可。
如果想通过`virsh`

管理，还需要安装`libvirt`

及其相关组件：

```
dnf install -y libvirt
```


`libvirt`

后，还需要手动启动libvirtd服务
```
systemctl start libvirtd
```


```
systemctl enable libvirtd
```


# 2. 虚拟机环境准备

## 2.1 虚拟机镜像

虚拟机启动可以使用正常装机使用的iso镜像，也可以使用虚拟化镜像直接启动，常用的虚拟化镜像格式为qcow2和raw。 他们有以下一些优势：

-
qcow2格式有着更高的压缩效率，它占用的磁盘空间更小。支持snapshot快照、动态调整镜像大小、加密以及压缩等高级功能。

-
raw格式则更加纯粹，即开即用，所以raw镜像的启动速度更快，但是也会占用更大的磁盘空间。


接下来以qcow2镜像为例，介绍一下虚拟机镜像的制作以及使用方法。

### 2.1.1 制作qcow2镜像

一般使用qemu-img命令来制作qcow2镜像

```
dnf install -y qemu-img
```


具体的创建命令为：

```
qemu-img create [--object OBJECTDEF] [-q] [-f FMT] [-b BACKING_FILE] [-F BACKING_FMT] [-u] [-o OPTIONS] FILENAME [SIZE]
```


-
`-f`

：指定了创建的镜像类型 -
`-o`

：指定了创建镜像使用的高级特性，例如压缩类型、加密类型等 -
`--object`

：指定qemu对象（一般无需指定） -
`-b`

：指定后端镜像，如果有指定BACKING_FILE，那当前镜像只会记录与BACKING_FILE的不同，BACKING_FILE不会被修改（除非用qemu-img commit命令） -
`-F`

：BACKING_FILE的镜像类型

### 2.1.2 查看镜像

通过qemu-img info可以查看镜像的信息

```
# qemu-img info image.qcow2
image: image.qcow2
file format: qcow2
virtual size: 10 GiB (10737418240 bytes)
disk size: 196 KiB
cluster_size: 65536
Format specific information:
compat: 1.1
compression type: zlib
lazy refcounts: false
refcount bits: 16
corrupt: false
extended l2: false
```


### 2.1.3 镜像伸缩

通过`qemu-img resize`

命令，可以修改镜像大小：

```
qemu-img resize FILENAME [+|-]SIZE
```


## 2.2 虚拟机磁盘

除了镜像文件外，虚拟机还可以配置其他的普通磁盘文件。如host上的逻辑卷、SSD、NVMe等

## 2.3 虚拟机网络

虚拟机的网络需要通过host与外界联系，host可以通过linux网桥或者Open vSwitch网桥来创建虚拟网卡设备给虚拟机使用。 下面介绍两种网桥的配置方式：

### 2.3.1 普通网桥

普通网桥使用`brctl`

或者`nmcli`

工具进行管理，`brctl`

当前系统没有默认安装，后续支持后可通过YUM源下载。

#### 2.3.1.1 nmcli 方式

创建网桥

```
nmcli connection add type bridge con-name br0 ifname br0
```


```
nmcli connection modify br0 ipv6.method "auto"
```


```
# nmcli connection add type bridge-slave ifname eth4 master br0
# nmcli connection down 'Wired connection 2' && nmcli connection up br0
Connection 'Wired connection 2' successfully deactivated (D-Bus active path: /org/freedesktop/NetworkManager/ActiveConnection/5)
Connection successfully activated (master waiting for slaves) (D-Bus active path: /org/freedesktop/NetworkManager/ActiveConnection/12)
```


```
# nmcli connection show
NAME UUID TYPE DEVICE
br0 8a089744-b903-4864-b817-8eb81eab701a bridge br0
eth0-conn 3477734e-c1fa-3588-9a7a-f331be03a73a ethernet eth0
Wired connection 1 303bb4e1-7e70-3e86-bdcf-256e53a1fe8c ethernet eth3
eth1-conn 10cda315-f1d7-3717-b14a-30a3501907ec ethernet eth1
eth2-conn 75ef91ad-63f9-3a96-ad69-18a0d22638a7 ethernet eth2
bridge-slave-eth4 d588ede6-de80-406e-83b2-baee3c7f858e ethernet eth4
```


#### 2.3.1.2 brctl 方式

该方式创建的网桥在系统重启后会消失，建议优先使用nmcli方式创建。

```
dnf install bridge-utils -y
```


```
brctl addbr br0
```


```
brctl addif br0 eth0
```


```
ifconfig eth0 0.0.0.0 && dhclient br0
```


### 2.3.2 Open vSwitch网桥

系统默认没有安装openvswitch，所以需要手动安装：

```
dnf install openvswitch
```


```
systemctl start openvswitch.service
```


```
systemctl status openvswitch.service
● openvswitch.service - Open vSwitch
Loaded: loaded (/usr/lib/systemd/system/openvswitch.service; disabled; vendor preset: disabled)
Active: active (exited) since Thu 2023-05-25 19:25:54 CST; 13s ago
Process: 484587 ExecStart=/bin/true (code=exited, status=0/SUCCESS)
Main PID: 484587 (code=exited, status=0/SUCCESS)
CPU: 2ms
```


```
ovs-vsctl add-br br0
```


```
ovs-vsctl add-br br0
```


# 3. 虚拟机配置

常见的虚拟机配置方法有两种：

-
直接用qemu命令启动时，直接在启动命令中添加所需添加的配置

-
通过libvirt启动时，在xml里配置的虚拟机相关的启动参数


因为libvirt是我们推荐的管理虚拟机的方式，所以本文主要介绍如何通过XML方式配置虚拟机。

## 3.1 系统相关配置

这部分配置会对虚拟机进行一些基础配置，比如虚拟化类型、系统架构类型、时钟配置和电源配置等。

如下所示，`<domain type='kvm'>`

指定了虚拟机的类型为KVM虚拟机，`<name>OpenCloudOS</name>`

指定了虚拟机的名字为OpenCloudOS。

```
<domain type='kvm'>
<name>OpenCloudOS</name>
...
</domain>
```


### 3.1.1 特性配置

虚拟机的一些特性配置通过XML中的`<feature>`

字段来指定。如指定虚拟机支持ACPI功能：

```
<features>
<acpi/>
</features>
```


除此之外，还有其他的一些特性，如下：

```
<features>
<pae/>
<apic/>
<hap/>
<privnet/>
...
</features>
```


## 3.2 CPU/内存相关配置

XML中CPU/内存常用元素以及其子元素有下列：

-
`<vcpu>`

：指定虚拟机的虚拟CPU数量。 -
`<cpu>`

：指定虚拟机使用的CPU类型和特性。-
`mode`

: 指定CPU模式，可以是host-model、custom、host-passthrough等。 -
`match`

: 指定CPU匹配规则，可以是minimum、exact或strict。 -
`check`

: 指定CPU检查规则，可以是none、partial或full。 -
`model`

: 指定CPU型号，例如Intel Xeon或AMD Opteron。 -
`vendor`

: 指定CPU厂商，例如Intel或AMD。 -
`topology`

: 指定CPU拓扑结构，包括sockets、cores和threads。-
`sockets`

：指定虚拟CPU的socket数量。 -
`cores`

：指定每个socket中虚拟CPU的核心数量。 -
`threads`

：指定每个core中虚拟CPU的超线程数量。

-
-
`numa`

: 指定CPU NUMA节点信息。

-
-
`<memory>`

：指定虚拟机启动时的最大内存大小。`unit`

：指定内存大小的单位，支持KiB，MiB，GiB，TiB等。

-
`<maxMemory>`

：指定虚拟机运行时的最大内存大小，以使用内存热插拔功能。 -
`<currentMemory>`

：指定虚拟机当前使用的内存大小。

## 3.3 设备相关配置

XML中设备相关配置是由`<devices>`

这个元素指定的。其中包括网络设备、存储设备以及其他PCI设备（如鼠标、键盘、显卡等）。

### 3.3.1 网络相关配置

如果使用的是普通linux网桥（通过brctl创建），XML中需要如下配置

```
<devices>
<interface type='bridge'>
<source bridge='br0'/>
<target dev='vnet1'/>
<model type='virtio'/>
</interface>
...
</devices>
```


如果使用的是OVS网桥，则XML中需要在普通网桥的基础上，指定`openvswitch`

类型：

```
<devices>
<interface type='bridge'>
<source bridge='br0'/>
<virtualport type='openvswitch'/>
<model type='virtio'/>
</interface>
...
</devices>
```


### 3.3.2 存储相关配置

存储设备一般通过`<disk>`

指定。

`<disk>`

元素的常用属性有：

-
`type`

：指定磁盘类型，可以是file、block或network。 -
`device`

：指定以何种设备类型传递给虚拟机，可以是disk、cdrom、floppy（软盘）或lun。 -
`model`

：指定磁盘模型，例如virtio、scsi、ide等。 -
`snapshot`

：指定磁盘是否支持快照功能，可以是on或off。

`<disk>`

元素的常用子元素有：

-
`<driver>`

：指定磁盘驱动程序的类型和特性。-
`name`

：指定磁盘驱动程序的名称。 -
`type`

：指定磁盘驱动程序的类型，例如qemu、raw、qcow2等。 -
`cache`

：指定磁盘缓存策略，例如none、writeback、writethrough等。 -
`io`

：指定磁盘I/O模式，例如threads、native等。 -
`discard`

：指定磁盘是否支持TRIM/DISCARD命令，可以是unmap或ignore。

-
-
`<source>`

：指定磁盘镜像文件或设备的路径。-
`<file>`

：指定磁盘镜像文件的路径。 -
`<dev>`

：指定磁盘设备的路径。 -
`<protocol>`

：指定磁盘设备的协议类型。

-
-
`<target>`

：指定磁盘设备传递给虚拟机的名称和类型。-
`dev`

：指定磁盘设备的名称。 -
`bus`

：指定磁盘设备的总线类型，例如virtio、scsi、ide等。 -
`type`

：指定磁盘设备的类型，例如disk、cdrom、floppy等。

-
-
`<address>`

：指定磁盘设备的PCI地址或SCSI地址。 -
`<readonly>`

：指定磁盘是否为只读模式。 -
`<shareable>`

：指定磁盘是否为可共享模式。

例如：

```
<disk type='file' device='disk'>
<driver name='qemu' type='qcow2' queues='4' queue_size='256' />
<source file='/var/lib/libvirt/images/domain.qcow'/>
<backingStore type='file'>
<format type='qcow2'/>
<source file='/var/lib/libvirt/images/snapshot.qcow'/>
<backingStore type='block'>
<format type='raw'/>
<source dev='/dev/mapper/base'/>
<backingStore/>
</backingStore>
</backingStore>
<target dev='vdd' bus='virtio'/>
</disk>
<disk type='file' device='cdrom'>
<driver name='qemu' type='raw'/>
<source file='OpenCloudOS-Stream-2302-20230221.1111-x86_64-everything.iso'/>
<target dev='sdb' bus='scsi'/>
<readonly/>
<boot order='2'/>
</disk>
```


### 3.3.3 总线相关配置

总线配置用于指定虚拟机中的设备总线类型和设备连接方式。常见的总线类型包括PCI、USB、Virtio等。总线配置可以通过 `<controller>`

元素进行配置， `<controller>`

元素有以下常用的属性：

-
`type`

：指定总线类型，例如ide、pci、usb、virtio等。 -
`index`

：指定总线的编号，从0开始。 -
`model`

：指定总线的模型，例如pci-root、usb-ehci、virtio-serial等。 -
`address`

：指定总线的地址，例如PCI地址或USB地址。-
`<type>`

：指定PCI地址的类型，可以是PCI或CCW。 -
`<domain>`

：指定总线的PCI域号。 -
`<bus>`

：指定总线的PCI总线号。 -
`<slot>`

：指定总线的PCI插槽号。 -
`<function>`

：指定总线的PCI功能号。

-

其中，`type`

和`model`

属性是一一对应的。对应关系如下：

| type值 | model值 | 说明 |
|---|---|---|
| pci | pcie-root | PCIe根节点 |
| pcie-root-port | PCIe总线根端口 | |
| pcie-to-pci-bridge | PCIe转PCI控制器 | |
| usb | ehci | USB 2.0控制器 |
| nec-xhci | USB 3.0控制器 | |
| scsi | virtio-scsi | virtio类型SCSI控制器，可以挂载磁盘，光盘等 |

具体用法如下：
下面例子中，定义了一个PCIe根节点，上面挂着一个`pcie-root-port`

也就是根端口，根端口只有一个plot，然后在根端口上挂载着一个`pcie-to-pci-bridge`

。

```
<devices>
<controller type='pci' index='0' model='pcie-root'/>
<controller type='pci' index='1' model='pcie-root-port'>
<address type='pci' domain='0x0000' bus='0x00' slot='0x01' function='0x0'/>
</controller>
<controller type='pci' index='2' model='pcie-to-pci-bridge'>
<address type='pci' domain='0x0000' bus='0x01' slot='0x00' function='0x0'/>
</controller>
</devices>
```


### 3.3.4 其他PCI设备相关配置

除了上述设备配置外，还有一些其他的常用的PCI设备。

#### 3.3.4.1 内存balloon设备

-
`<memballoon>`

：指定虚拟机的内存热插拔功能。-
`model`

：指定内存热插拔模型，可以是virtio或none，默认为virtio。 -
`stats`

：指定内存热插拔统计信息的开关，可以是on或off，默认为off。

-

下面的例子中，定义了一个memballoon，使用IOMMU进行内存管理，并且启用ATS，使用virto协议通信，他挂载bus0上的2号slot上，每10s更新一次控制器统计信息。

```
<devices>
<memballoon model='virtio'>
<address type='pci' domain='0x0000' bus='0x00' slot='0x02' function='0x0'/>
<stats period='10'/>
<driver iommu='on' ats='on'/>
</memballoon>
</devices>
```


#### 3.3.4.2 显示设备

虚拟机启动后，可以在host上通过`virsh console`

登录，开启ssh服务后还可以通过ssh服务登录。除此之外，也可以通过配置如vnc等显示设备登录，如下所示：

该例子中，配置了一个VNC显示设备，端口号为5901，如果被占用，会自动选择一个未被占用的端口号，监听所有的IP地址，并且键盘映射为英文。

```
<graphics type='vnc' port='5901' autoport='yes' listen='0.0.0.0' keymap='en-us'>
<listen type='address' address='0.0.0.0'/>
</graphics>
```


#### 3.3.4.3 媒体设备

如果在虚拟机中需要使用桌面，那就可能需要配置声卡和显卡，qemu也可以提供虚拟声卡和虚拟显卡。

如下所示，配置了一个ICH6模型的声卡设备和一个Cirrus模型的显卡设备。声卡设备的别名为 `sound0`

，PCI地址为 `domain='0x0000'`

、 `bus='0x00'`

、 `slot='0x06'`

、 `function='0x0'`

；显卡设备的别名为 `video0`

，PCI地址为 `domain='0x0000'`

、 `bus='0x00'`

、 `slot='0x02'`

、 `function='0x0'`

。显卡设备支持1个显示器，且为主显卡，显存大小为16384KB。

```
<sound model='ich6'>
<alias name='sound0'/>
<address type='pci' domain='0x0000' bus='0x00' slot='0x06' function='0x0'/>
</sound>
<video>
<model type='cirrus' vram='16384' heads='1' primary='yes'/>
<alias name='video0'/>
<address type='pci' domain='0x0000' bus='0x00' slot='0x02' function='0x0'/>
</video>
```


#### 3.3.4.4 直通设备

直通设备是指将物理主机上的设备直接映射到虚拟机中，从而使虚拟机可以直接访问该设备，而无需通过虚拟化管理程序进行中间层的转发。在XML中，可以使用 `<hostdev>`

元素来配置直通设备。
`<hostdev>`

元素可以包含以下子元素：

-
`<source>`

：指定直通设备的源，可以是PCI设备、USB设备、SCSI设备等。 -
`<address>`

：在`<source>`

中指定直通设备在物理主机上的地址，在`<source>`

外指定虚拟机内地址。 -
`<driver>`

：指定设备的驱动名称。例如 "vfio"。

支持直通的设备包括PCI设备、USB设备、SCSI设备等。其中，PCI设备是最常见的直通设备类型，可以直接将物理主机上的PCI设备映射到虚拟机中，从而使虚拟机可以直接访问该设备。USB设备和SCSI设备也可以进行直通，但相对来说使用较少。

在配置直通设备时，需要注意以下几点：

- 直通设备需要在物理主机上进行解绑操作，才能被虚拟机使用。

```
virsh nodedev-detach pci_0000_02_00_0
```


-
直通设备只能被一个虚拟机使用，不能同时被多个虚拟机使用。

-
直通设备的性能通常比虚拟化设备更好，但也存在一些限制，例如无法进行热插拔操作等。


如下所示，虚拟机中包含了一个使用VFIO驱动程序进行直通的PCI设备。直通设备的模式为子系统模式，由虚拟化管理程序管理。直通设备的源地址（在host上的地址）为 `domain='0x0000'`

、 `bus='0xaf'`

、 `slot='0x00'`

、 `function='0x0'`

，使用VFIO驱动程序进行直通。直通设备的别名为 `hostdev0`

，在虚拟机中的PCI地址为 `domain='0x0000'`

、 `bus='0x00'`

、 `slot='0x09'`

、 `function='0x0'`

。

```
<hostdev mode='subsystem' type='pci' managed='yes'>
<driver name='vfio'/>
<source>
<address domain='0x0000' bus='0xaf' slot='0x00' function='0x0'/>
</source>
<alias name='hostdev0'/>
<address type='pci' domain='0x0000' bus='0x00' slot='0x09' function='0x0'/>
</hostdev>
```


# 4. 虚拟机管理

系统推荐使用 libvirt 来进行虚拟机生命周期的管理。

## 4.1 虚拟机的状态

### 4.1.1 创建虚拟机

当你准备好一个虚拟机的镜像、磁盘和XML，你就可以创建自己的虚拟机了。 这里给出一个最简单的虚拟机xml示例：

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


然后通过`virsh create`

命令创建

```
# virsh create test.xml
Domain 'OpenCloudOS' created from test.xml
```


```
# virsh list
Id Name State
-----------------------------
3 OpenCloudOS running
```


### 4.1.2 登陆虚拟机

创建成功后可以登录虚拟机了。登陆虚拟机的方式有以下几种：

#### 4.1.2.1 ssh登录

如果镜像配置了IP地址，并且支持ssh登录，可以通过该方式登录 检查虚拟机sshd服务是否正常

```
# systemctl status sshd
● sshd.service - OpenSSH server daemon
Loaded: loaded (/usr/lib/systemd/system/sshd.service; enabled; vendor preset: enabled)
Active: active (running) since Thu 2023-05-18 05:48:41 UTC; 1 week 0 days ago
Docs: man:sshd(8)
man:sshd_config(5)
Main PID: 737 (sshd)
Tasks: 1 (limit: 18845)
Memory: 5.1M
CPU: 1.430s
CGroup: /system.slice/sshd.service
└─737 "sshd: /usr/sbin/sshd -D [listener] 0 of 10-100 startups"
```


```
cat /etc/ssh/sshd_config
```


```
[root@localhost ~]# netstat -ntpl
Active Internet connections (only servers)
Proto Recv-Q Send-Q Local Address Foreign Address State PID/Program name
tcp 0 0 127.0.0.53:53 0.0.0.0:* LISTEN 684/systemd-resolve
tcp 0 0 0.0.0.0:36000 0.0.0.0:* LISTEN 737/sshd: /usr/sbin
```


```
ssh [user]@[hostip] -p [portid]
```


#### 4.1.2.2 vnc登录

如果XML中已配置好vnc，可以通过vnc登录主机对应端口号登陆虚拟机。

```
<graphics type='vnc' port='5900' autoport='yes' listen='0.0.0.0' keymap='en-us' passwd='n8VfjbFK'/>
```


```
# virsh vncdisplay OpenCloudOS
:0
```


`主机IP`

:`端口号`

登录虚拟机。
#### 4.1.2.3 console登录

如果XML已配置console串口，可以在host上通过此方式登录。

```
# virsh console OpenCloudOS
Connected to domain 'OpenCloudOS'
Escape character is ^] (Ctrl + ])
localhost login: root
Password:
[root@localhost ~]#
```


### 4.1.3 重启虚拟机

物理机的重启可以冷重启和热重启，虚拟机也一样。

#### 4.1.3.1 热重启

虚拟机热重启就是正常走关机开机流程

```
# virsh reboot OpenCloudOS
Domain 'OpenCloudOS' is being rebooted
```


#### 4.1.3.2 冷重启

虚拟机冷重启，则类似于物理机的直接上电然后下电。

```
# virsh reset OpenCloudOS
Domain 'OpenCloudOS' was reset
```


### 4.1.4 关闭/销毁虚拟机

同重启虚拟机，关闭虚拟机也分正常流程关闭和直接销毁虚拟机。 正常关机：

```
# virsh shutdown OpenCloudOS
Domain 'OpenCloudOS' is being shutdown
```


销毁虚拟机：

```
# virsh destroy OpenCloudOS
Domain 'OpenCloudOS' destroyed
```


# 5. 虚拟机安全

## 5.1 虚拟机安全标签

`seclabel`

元素允许对安全驱动程序的操作进行控制，包含三种基本模式：

-
`dynamic`

： libvirt 自动生成唯一的安全标签； -
`static`

：应用程序/管理员选择标签； -
`none`

：禁用；

通过动态标签生成，libvirt 将始终自动重新标记与虚拟机关联的任何资源。对于静态标签分配，默认情况下，管理员或应用程序必须确保在任何资源上正确设置标签。但如果需要的话，也可以启用自动重新标记。

如果 libvirt 使用多个安全驱动程序，则可以使用多个 seclabel 标签，每个驱动程序一个，每个标签引用的安全驱动程序可以使用属性定义 `model`

。可在 XML 中配置 top-level 安全标签：

```
<seclabel type='dynamic' model='selinux'/>
<seclabel type='dynamic' model='selinux'>
<baselabel>system_u:system_r:svirt_t:s0</baselabel>
</seclabel>
<seclabel type='static' model='selinux' relabel='no'>
<label>system_u:system_r:svirt_t:s0:c392,c662</label>
</seclabel>
<seclabel type='static' model='selinux' relabel='yes'>
<label>system_u:system_r:svirt_t:s0:c392,c662</label>
</seclabel>
<seclabel type='none'/>
```


其中：

-
`type`

： 包含`dynamic`

、`static`

和`none`

三种，决定了 libvirt 是否生成 唯一的安全标签。如果忘记在 XML 中配置`type`

，则其值可能为`dynamic`

、或`none`

；如果忘记配置`type`

但是配置了`baselabel`

，则默认为`dynamic`

。 -
`model`

- 一个有效的安全模型名称，与当前激活的安全模型相匹配。 -
`relabel`

- 可设置为`yes`

或`no`

。如果使用动态标签分配，则必须设置`yes`

；如果使用静态标签分配，则默认为`no`

。 -
`<label>`

- 如果使用静态标签，则**必须指定要分配给虚拟域的完整安全标签**。内容的格式取决于使用的安全驱动程序：-
`SELinux`

: SELinux 上下文； -
`AppArmor`

：AppArmor 配置文件； -
`DAC`

: 所有者和组用冒号分隔，它们可以定义为用户/组名或 UID/GID。驱动程序将首先尝试将这些值解析为名称，但可以使用前导加号强制驱动程序将它们解析为 UID 或 GID；

-
-
`<baselabel>`

- 如果使用动态标签，则可以选择使用它来指定将用于生成实际标签的基本安全标签。内容的格式取决于所使用的安全驱动程序。 -
`<imagelabel>`

- 这是一个仅输出的元素，它显示了在与虚拟域关联的资源上使用的安全标签。内容的格式取决于所使用的安全驱动程序。当重新标记生效时，也可以通过禁用标记（如果文件存在于 NFS 或其他缺少安全标记的文件系统上）或请求备用标记来微调对特定源文件名所做的标记（当管理应用程序创建一个特殊标签以允许在域之间共享一些但不是全部资源时很有用）。当 seclabel 元素附加到特定路径而不是顶级域分配时，仅支持属性 relabel 或子元素标签。

# 6. 虚拟机冷/热插拔

## 6.1 PCI设备热插拔

PCI设备主要挂载在`pcie-root-port`

上，`pcie-root-port`

上挂载的设备支持热插拔，但是`pcie-root-port`

本身并不支持，所以在创建虚拟机的时候需要提前预留可能要热插拔的`pcie-root-port`

数量。
PCI设备的热插主要通过`virsh attach-device`

、`virsh attach-disk`

、`virsh attach-interface`

命令实现。

### 6.1.2 网卡热插拔

#### 6.1.2.1 attach-device方式

`network-device.xml`

中配置需要热插的网络设备（名称可自己定义）

```
# cat network-device.xml
<interface type='bridge'>
<mac address='52:54:00:76:f2:bb'/>
<source bridge='br0'/>
<virtualport type='openvswitch'/>
<model type='virtio'/>
<driver name='vhost' queues='2'/>
</interface>
```


```
# virsh attach-device OpenCloudOS network-device.xml
Device attached successfully
```


```
# ifconfig
eth0: flags=4163<UP,BROADCAST,RUNNING,MULTICAST> mtu 1500
inet6 fe80::3547:1464:cd51:dd20 prefixlen 64 scopeid 0x20<link>
ether 52:54:00:76:f2:bb txqueuelen 1000 (Ethernet)
RX packets 17 bytes 2156 (2.1 KiB)
RX errors 0 dropped 0 overruns 0 frame 0
TX packets 41 bytes 6146 (6.0 KiB)
TX errors 0 dropped 0 overruns 0 carrier 0 collisions 0
lo: flags=73<UP,LOOPBACK,RUNNING> mtu 65536
inet 127.0.0.1 netmask 255.0.0.0
inet6 ::1 prefixlen 128 scopeid 0x10<host>
loop txqueuelen 1000 (Local Loopback)
RX packets 182 bytes 14804 (14.4 KiB)
RX errors 0 dropped 0 overruns 0 frame 0
TX packets 182 bytes 14804 (14.4 KiB)
TX errors 0 dropped 0 overruns 0 carrier 0 collisions 0
```


```
# virsh detach-device OpenCloudOS network-device.xml
Device detached successfully
```


#### 6.1.2.2 attach-interface

不需要XML，直接通过命令挂载

```
# virsh attach-interface OpenCloudOS bridge br0
```


```
# virsh detach-interface OpenCloudOS bridge br0
```


### 6.1.3 磁盘热插拔

#### 6.1.3.1 attach-device方式

创建一个虚拟设备XML

```
# cat new-disk.xml
<disk type='file' device='disk'>
<driver name='qemu' type='qcow2' cache='none' io='native'/>
<source file='/var/lib/libvirt/images/new-disk.qcow2'/>
<backingStore/>
<target dev='sda' bus='scsi'/>
<address type='drive' controller='0' bus='0' target='1' unit='0'/>
</disk>
```


```
# virsh attach-device OpenCloudOS new-disk.xml
Device attached successfully
```


```
# lsblk
NAME MAJ:MIN RM SIZE RO TYPE MOUNTPOINTS
sda 8:0 0 1G 0 disk
vda 252:0 0 10G 0 disk
└─vda1 252:1 0 10G 0 part /
```


```
# virsh detach-device OpenCloudOS new-disk.xml
Device detached successfully
```


#### 6.1.3.2 attach-disk方式

命令格式为

```
virsh attach-disk <domain> <source> <target>
```


```
virsh attach-disk OpenCloudOS /root/disk.img vdb
```


```
# virsh detach-disk OpenCloudOS vdb
```


# 7. 虚拟机迁移

## 7.1 虚拟机冷迁移

冷迁移需要虚拟机关机，所以如果您的业务对业务连续性有要求，建议优先使用热迁移。

### 7.1.1 环境准备

确认源和目的母机环境支持迁移。

-
架构相同

-
虚拟机所需资源足够（CPU、内存等）

-
网络配置一致（网桥）

-
目的端已安装qemu和libvirt组件，并且libvirtd服务已启用


### 7.1.2 迁移步骤

- 在源服务器上，确保要迁移的虚拟机已关机。
`# virsh shutdown OpenCloudOS`

- 在源服务器上，导出虚拟机的 XML 配置。这将作为目标服务器上虚拟机的配置模板：
`virsh dumpxml OpenCloudOS > myvm.xml`

- 使用 scp、rsync 或其他方法，将虚拟机的磁盘镜像文件（例如，qcow2 或raw 格式）和导出的 XML 配置文件从源服务器复制到目标服务器。确保将文件放在目标服务器的适当位置。
`scp /var/lib/libvirt/images/new-disk.qcow2 root@[dest_ip]:/var/lib/libvirt/images/`

-
（可选）如果对虚拟机配置进行了修改（例如，更改网络适配器设置），请确保在此步骤应用所需的更改。

-
在目标服务器上，使用导入的 XML 配置文件定义新虚拟机：

`virsh create myvm.xml`


## 7.2 虚拟机热迁移

### 7.2.1 环境准备

-
同冷迁移，需要确认源和目的母机支持迁移。

-
修改libvirtd配置

`/etc/libvirt/libvitd.conf`

，修改以下配置，启用TCP

```
listen_tls = 1
listen_tcp = 0
auth_tcp = "none"
```


- 启用libvirtd-tcp.socket服务

```
systemctl stop libvirtd
systemctl start libvirtd-tcp.socket
systemctl start libvirtd
```


- 然后需要确认源和目的母机是否联通，如果以下命令可以正常执行，说明网络环境正常

```
virsh -c qemu+tcp://[dest_ip]/system list
```


- 将镜像/磁盘文件通过scp拷贝到目的母机目录下。

```
scp /var/lib/libvirt/images/new-disk.qcow2 root@[dest_ip]:/var/lib/libvirt/images/
```


### 7.2.2 迁移步骤

```
virsh migrate --live --unsafe --persistent OpenCloudOS qemu+ssh://<dest_ip>/system tcp://<dest_ip>
```


`--persistent`

参数会把虚拟机的配置文件持久化，存储在`/etc/libvirt/qemu/`

下。
# 8. 典型问题

## 8.1 镜像访问权限问题

当出现以下报错的时候，说明libvirt 用户和组没有访问该qcow2镜像的权限。

```
# virsh create test.xml
error: Failed to create domain from test.xml
error: Cannot access storage file '/root/OpenCloudOS-Stream-23-20230524.0259-x86_64.qcow2' (as uid:107, gid:107): Permission denied
```


### 解决方法：

将需要使用的镜像，移动或者拷贝到libvirt可以访问的目录，例如`/var/lib/libvirt/images/`

。

```
mv /root/OpenCloudOS-Stream-23-20230524.0259-x86_64.qcow2 /var/lib/libvirt/images/
```


## 8.2 镜像文件标签问题

配置静态安全标签 `seclabel`

后，使用 `virsh`

创建虚拟机时，可能会出现如下报错，同时查看 `message`

或 `audit.log`

会发现 “AVC” 相关拒绝消息，表明此时发生了 SELinux 的拒绝动作：

```
virsh create test.xml
error: Failed to create domain from test.xml
error: internal error: process exited while connecting to monitor: 2023-05-30T12:54:39.770343Z qemu-system-x86_64: -blockdev {"driver":"file","filename":"/var/lib/libvirt/images/OpenCloudOS-Stream-23-20230530.0142-x86_64-test3.qcow2","node-name":"libvirt-1-storage","auto-read-only":true,"discard":"unmap"}: Could not open '/var/lib/libvirt/images/OpenCloudOS-Stream-23-20230530.0142-x86_64-test3.qcow2': Permission denied
# 查看message或audit日志
grep "AVC" /var/log/messages
2023-05-30T20:54:39.770352+08:00 localhost audit[65317]: AVC avc: denied { read } for pid=65317 comm="qemu-system-x86" name="OpenCloudOS-Stream-23-20230530.0142-x86_64-test3.qcow2" dev="vda1" ino=206 scontext=system_u:system_r:svirt_t:s0:c392,c662 tcontext=unconfined_u:object_r:admin_home_t:s0 tclass=file permissive=0
```


此时为qcow2镜像文件标签异常，下载时存放位置的默认标签规则，不被当前进程识别导致AVC拒绝。

### 解决方法：

将qcow2文件标签恢复即可，建议优先采用 `restorecon`

恢复：

```
# 方式1
restorecon -v /var/lib/libvirt/images/OpenCloudOS-Stream-.qcow2
# 方式2
chcon -t svirt_image_t /var/lib/libvirt/images/OpenCloudOS-Stream-xx.qcow2
# 方式3
# 调整 xml 文件，修改配置为 `dynamic` 类型
```


## 8.3 多个安全标签配置

配置多个安全标签 `seclabel`

后，create 虚拟机报错如下：

```
virsh create test5.xml
error: Failed to create domain from test5.xml
error: seclabel for model selinux is already provided
```


### 解决方法：

修改 `test.xml`

文件，调整为一个 `<seclabel>`

配置。