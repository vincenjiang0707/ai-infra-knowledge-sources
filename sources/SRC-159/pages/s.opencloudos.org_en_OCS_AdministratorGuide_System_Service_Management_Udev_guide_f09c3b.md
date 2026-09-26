source: https://docs.opencloudos.org/en/OCS/AdministratorGuide/System_Service_Management/Udev_guide/

# udev机制与使用

## 1. 介绍

systemd-udev 是 Linux 系统中的一个重要组件，它负责设备管理和热插拔支持。udev 是用户空间设备管理器，它与内核空间的设备驱动程序协同工作，以便在设备连接或断开时执行相应的操作。systemd-udev 是 systemd 项目中 udev 的实现。

以下是 systemd-udev 机制的一些关键特性和组件：

-
`规则文件`

：udev 使用一组规则文件来定义设备的命名、权限、所有权和其他属性。这些规则文件通常位于`/etc/udev/rules.d/`

和`/lib/udev/rules.d/`

目录中。规则文件的文件名以数字开头，数字越小，优先级越高。udev 会按照文件名的字母顺序处理这些文件。 -
`事件`

：当设备连接或断开时，内核会生成一个事件。udev 监听这些事件，并根据规则文件执行相应的操作。事件包括设备的添加、删除、更改等。 -
`设备节点`

：udev 根据规则文件为设备创建设备节点（device nodes），通常位于`/dev/`

目录下。设备节点是用户空间程序与设备驱动程序进行通信的接口。 -
`系统集成`

：systemd-udev 与 systemd 系统管理器紧密集成。systemd 会启动和监控 udevd 服务（udev daemon），并处理设备相关的事件。此外，systemd 也可以根据设备的添加或删除自动启动或停止相关的服务。 -
`规则匹配`

：udev 规则文件中的规则可以根据设备的属性（如设备类型、制造商、型号等）进行匹配。这使得 udev 能够为不同类型的设备执行特定的操作。 -
`规则动作`

：udev 规则文件中的规则可以执行各种动作，如设置设备节点的权限、所有权、创建符号链接、运行脚本等。这使得 udev 能够根据设备的特性自动配置设备。

## 2. 使用方法

### 2.1 规则文件：

udev 使用规则文件来定义设备的命名、权限、所有权和其他属性。规则文件通常位于 `/etc/udev/rules.d/`

和 `/lib/udev/rules.d/`

目录中。要创建自定义规则，请在 `/etc/udev/rules.d/`

目录下创建一个新文件，文件名以数字开头，数字越小，优先级越高。例如，一个名为 `10-my-custom.rules`

的文件，里面定义的规则优先级比`99-systemd.rules`

中定义的规则优先级更高。

接下来，以系统中默认配置的一些udev规则文件为例，来理解规则文件的语法：

#### 2.1.1 TTY设备:

```
SUBSYSTEM=="tty", KERNEL=="tty[a-zA-Z]*|hvc*|xvc*|hvsi*|ttysclp*|sclp_line*|3270/tty[0-9]*", TAG+="systemd"
```


**SUBSYSTEM=="tty"**：此条件表示规则仅适用于属于 "tty" 子系统的设备。这意味着，当一个与 tty 子系统有关的设备被添加、删除或更改时，才会匹配此规则。**KERNEL=="tty[a-zA-Z]|hvc|xvc|hvsi|ttysclp**：这条条件进一步限制匹配的设备必须符合给定的内核名称模式。在这个例子中，规则将匹配以下任何一种设备：*|sclp_line*|3270/tty[0-9]- tty[a-zA-Z]*：名称以 "tty" 开头并后跟任意数量的字母的设备。
- hvc*：名称以 "hvc" 开头的设备。
- xvc*：名称以 "xvc" 开头的设备。
- hvsi*：名称以 "hvsi" 开头的设备。
- ttysclp*：名称以 "ttysclp" 开头的设备。
- sclp_line*：名称以 "sclp_line" 开头的设备。
- 3270/tty[0-9]*：名称以 "3270/tty" 开头并后跟任意数量的数字的设备。

**TAG+="systemd"**：对于匹配上述条件的设备，这个操作给它添加 "systemd" 标签。这使得`systemd`

可以识别并按需与这些设备进行互动。

#### 2.1.2 磁盘设备:

系统中磁盘相关的udev规则，主要是在`60-persistent-storage.rules`

该文件中配置的。

##### virtio虚拟磁盘：

```
# virtio-blk
KERNEL=="vd*[!0-9]", ATTRS{serial}=="?*", ENV{ID_SERIAL}="$attr{serial}", SYMLINK+="disk/by-id/virtio-$env{ID_SERIAL}"
```


`KERNEL=="vd*[!0-9]"`

：此条件表示规则适用于内核名称匹配`vd*`

的设备，但名称不能以数字结尾。即，它匹配的是虚拟磁盘设备，而非单独的磁盘分区。`ATTRS{serial}=="?*"`

：要求设备具有序列号属性（一种设备识别特征）。问号是通配符，表示指定属性至少有一个字符。`ENV{ID_SERIAL}="$attr{serial}"`

：将设备序列号属性值赋给环境变量`ID_SERIAL`

。`SYMLINK+="disk/by-id/virtio-$env{ID_SERIAL}"`

：为匹配的设备添加符号链接，使得`/dev/disk/by-id/`

目录下有一个名为`virtio-ID_SERIAL`

的文件指向此设备。

##### SCSI设备：

```
# SCSI devices
KERNEL=="sd*[!0-9]|sr*", ENV{ID_SERIAL}!="?*", IMPORT{program}="scsi_id --export --whitelisted -d $devnode", ENV{ID_BUS}="scsi"
KERNEL=="sd*|sr*|cciss*", ENV{DEVTYPE}=="disk", ENV{ID_SERIAL}=="?*", SYMLINK+="disk/by-id/$env{ID_BUS}-$env{ID_SERIAL}"
```


`KERNEL=="sd*[!0-9]|sr*"`

：此条件表示规则适用于内核名字匹配`sd*[!0-9]`

（SCSI/SATA磁盘设备而非分区）或`sr*`

（光驱设备）的设备。`ENV{ID_SERIAL}!="?*"`

：仅在设备未设置序列号环境变量（`ID_SERIAL`

环境变量未设置或为空）时才适用此规则。`IMPORT{program}="scsi_id --export --whitelisted -d $devnode"`

：如果匹配上述条件，运行`scsi_id`

程序，从实际的设备节点（`$devnode`

）获取设备信息，并将输出的信息导入`udev`

环境变量。这样可以让`udev`

获得设备的序列号（ID_SERIAL）。`ENV{ID_BUS}="scsi"`

：设置环境变量`ID_BUS`

为`scsi`

，表示设备类型等信息，用于接下来创建符号链接。`ENV{DEVTYPE}=="disk"`

：仅对设置了`DEVTYPE`

环境变量且值为`disk`

的设备适用此规则。这可以过滤掉分区设备，因为它们的`DEVTYPE`

值为`partition`

。`ENV{ID_SERIAL}=="?*"`

：仅在设备的序列号环境变量（`ID_SERIAL`

）已设置的情况下适用此规则。`SYMLINK+="disk/by-id/$env{ID_BUS}-$env{ID_SERIAL}"`

：为满足以上条件的整个磁盘设备添加符号链接，使得`/dev/disk/by-id/`

目录下有一个名为`ID_BUS-ID_SERIAL`

的文件指向此设备。

##### NVMe设备

```
# NVMe
KERNEL=="nvme*[0-9]n*[0-9]", ATTR{wwid}=="?*", SYMLINK+="disk/by-id/nvme-$attr{wwid}"
KERNEL=="nvme*[0-9]n*[0-9]p*[0-9]", ENV{DEVTYPE}=="partition", ATTRS{wwid}=="?*", SYMLINK+="disk/by-id/nvme-$attr{wwid}-part%n"
```


`KERNEL=="nvme*[0-9]n*[0-9]"`

：此条件表示规则匹配名字以`nvme`

开头，后接一数字，然后是`n`

，再接一数字的设备。这匹配的是 NVMe 设备，而非分区。`ATTR{wwid}=="?*"`

：要求设备具有 WWID 属性。`udev`

规则中的问号是通配符，表明指定属性至少有一个字符。`SYMLINK+="disk/by-id/nvme-$attr{wwid}"`

：为符合条件的设备添加符号链接，使得`/dev/disk/by-id/`

目录下有一个以`nvme-WWID`

命名的文件指向此设备。`KERNEL=="nvme*[0-9]n*[0-9]p*[0-9]"`

：此条件表示规则匹配名字以`nvme`

开头，后接一数字，然后是`n`

，再接一数字，以`p`

并接数字结束的设备。这种名称表示 NVMe 设备的分区。`ENV{DEVTYPE}=="partition"`

：仅针对设备类型为（以`DEVTYPE`

环境变量表示）`partition`

的设备应用此规则。`SYMLINK+="disk/by-id/nvme-$attr{wwid}-part%n"`

：为匹配的分区设备添加符号链接，链接位于`/dev/disk/by-id/`

目录，并以`nvme-WWID-partN`

命名，其中`N`

是分区序号。

#### 2.1.3 网络设备

网络设备稍微特殊一点，系统中的网络设备命名规则在`/usr/lib/udev/rules.d/80-net-setup-link.rules`

文件中指定。

```
SUBSYSTEM!="net", GOTO="net_setup_link_end"
IMPORT{builtin}="path_id"
ACTION=="remove", GOTO="net_setup_link_end"
IMPORT{builtin}="net_setup_link"
NAME=="", ENV{ID_NET_NAME}!="", NAME="$env{ID_NET_NAME}"
LABEL="net_setup_link_end"
```


`net_setup_link`

，然后如果名称还是为空且有环境变量`ID_NET_NAME`

，则将设备名称命名为`ID_NET_NAME`

。
这个内嵌函数`net_setup_link`

会执行`/usr/lib/systemd/network/99-default.link`

中定义动作。
```
# cat /usr/lib/systemd/network/99-default.link
[Match]
OriginalName=*
[Link]
NamePolicy=keep kernel database onboard slot path
AlternativeNamesPolicy=database onboard slot path
MACAddressPolicy=persistent
```


`[Match]`

：配置匹配条件，针对`OriginalName=*`

意味着这个配置将匹配所有网络接口。`[Link]`

：配置命名策略和参数：`NamePolicy=keep kernel database onboard slot path`

：设定网络接口的命名策略顺序。命名策略是按顺序尝试的，尝试一个策略之后，如果没有得到有效名称，将尝试下一个策略。这些策略分别解释如下：-`keep`

：保留内核分配的原始名称。`kernel`

：采用内核提供的名称。`database`

：基于硬件数据库中的设备数据库条目。`onboard`

：根据设备本身的索引（如主板插槽数）。`slot`

：根据设备在 PCI/USB 总线上的插槽信息。`path`

：根据设备的硬件路径（例如设备在总线上的拓扑）。

`AlternativeNamesPolicy=database onboard slot path`

：设定常规策略失败时采用的备选命名策略。此设置指定在保留或内核策略无法建立有效名称时使用的替代策略。`MACAddressPolicy=persistent`

：设定分配给网络接口的 MAC 地址策略。在本例中，`persistent`

表示设备的 MAC 地址是根据udev的数据持久化的，确保在系统重启时接口使用相同的 MAC 地址。


通过这个文件， `systemd-udevd`

生成了可预测网络接口名称。正常情况下，网络设备会以在主板上的接口位置或者PCI总线上的插槽位置命名，如`ens33`

、`enp0s3`

等。
但是为了保持兼容性，qcow2镜像会在启动参数中加入`biosdevname=0 net.ifnames=0`

，这样网络设备会以`ethX`

的方式命名。

除此之外，udev规则文件还有其他一些参数，如下：

-
匹配字段：

-
`ACTION`

：匹配设备事件，如 "add"（添加设备）或 "remove"（移除设备）。 `DEVPATH`

：匹配设备的 sysfs 路径。`KERNEL`

：匹配设备的内核名称，如 "sda" 或 "eth0"。`SUBSYSTEM`

：匹配设备所属的子系统，如 "usb"、"pci" 或 "block"。`DRIVER`

：匹配设备的驱动程序名称。`ATTR{key}`

：匹配设备属性。`key`

是设备属性的名称，如 "idVendor" 或 "idProduct"。`ENV{key}`

：匹配环境变量。`key`

是环境变量的名称，如 "ID_TYPE"。-
`TAG`

：匹配设备标签。 -
赋值字段：

-
`NAME`

：为设备指定名称。这个字段已经被废弃，现在建议使用`SYMLINK`

。 `SYMLINK`

：为设备创建符号链接。可以使用通配符和设备属性。`OWNER`

：设置设备文件的所有者。可以是用户名或用户 ID。`GROUP`

：设置设备文件的组。可以是组名或组 ID。`MODE`

：设置设备文件的权限。例如，"0660" 表示所有者和组成员有读写权限，其他用户无权限。`ATTR{key}`

：设置设备属性。`key`

是设备属性的名称，如 "power/control"。`ENV{key}`

：设置环境变量。`key`

是环境变量的名称，如 "ID_FS_TYPE"。-
`TAG+="tag"`

：为设备添加标签。 -
运行字段：

-
`RUN`

：在设备事件发生时执行指定的命令或脚本。例如，`RUN+="/usr/bin/my-script"`

。 `RUN{program}`

：在设备事件发生时执行指定的程序。例如，`RUN{program}="/usr/bin/my-program"`

。`IMPORT{program}`

：执行指定的程序，并将其输出导入到规则文件中。例如，`IMPORT{program}="/usr/bin/my-importer"`

。-
`IMPORT{file}`

：从指定的文件导入变量。例如，`IMPORT{file}="/etc/udev/my-vars.conf"`

。 -
控制字段：

-
`GOTO`

：跳转到指定的标签。例如，`GOTO="my_label"`

。 `LABEL`

：定义一个标签。例如，`LABEL="my_label"`

。

### 2.2 命令行工具：

udev 提供了一些命令行工具，如 `udevadm`

，用于查询和控制设备。以下是一些常用的 `udevadm`

子命令：

`udevadm info`

：查询设备信息。例如，`udevadm info -a -p /sys/class/block/sda`

会显示关于`/dev/sda`

设备的详细信息。`udevadm monitor`

：实时监控设备事件。这对于调试规则文件非常有用。`udevadm test`

：测试规则文件。例如，`udevadm test /sys/class/block/sda`

会应用规则文件并显示结果，但不会实际执行操作。`udevadm control`

：控制 udev 服务。例如，`udevadm control --reload-rules`

会重新加载规则文件。

### 3. 典型问题

#### 3.1 盘符漂移

##### 发生原因：

在系统启动过程中，内核会检测磁盘设备并给它们分配设备名。这些名称通常对应 `/dev`

文件系统下的设备节点，如 `/dev/sda`

或 `/dev/sdb`

等。然而内核中，设备名称分配依赖于设备被检测的顺序。因此，当设备接入顺序或硬件配置发生变化时，设备名可能与上一次启动时的不同。

##### 导致问题：

上一次启动时的`sda`

盘可能这次启动后变成`sdb`

。设备名称发生改变导致挂载点、数据存储目录、应用程序和服务找不到正确的设备。这可能导致文件系统挂载错误、服务启动失败和总体系统性能降低。

##### 解决方案：

可预测命名规则：引入 Predictable Network Interface Names（可预测设备接口名称）机制。设备按照可预测的命名规则分配名称，名称取决于设备的固定属性（如硬件地址、设备路径）。例如：

```
- 基于 UUID 的命名： `/dev/disk/by-uuid/` 目录下为设备提供基于其 UUID 的符号链接。
- 基于标签（Label） 的命名：根据设备的文件系统标签在 `/dev/disk/by-label/` 下生成符号链接。
- 基于硬件属性的命名：在 `/dev/disk/by-id/` 和 `/dev/disk/by-path/` 目录下为设备创建基于其硬件属性的符号链接。
```


如果需要使用磁盘名称，建议使用磁盘UUID代替。如

```
# cat /etc/fstab
UUID=f09f5404-7229-4e89-9620-867d9da74450 / ext4 noatime,acl,user_xattr 1 1
```