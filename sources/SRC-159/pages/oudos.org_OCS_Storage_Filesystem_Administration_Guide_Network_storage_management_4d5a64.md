source: https://docs.opencloudos.org/OCS/Storage_Filesystem_Administration_Guide/Network_storage_management/

# 网络存储管理

## 1 网络存储协议

### 1.1 iSCSI

iSCSI（Internet Small Computer System Interface）是一种基于 IP 网络的存储协议，它允许计算机通过网络连接到远程存储设备，并像本地存储一样访问数据，可以降低存储成本并提高存储的灵活性和可扩展性。

iSCSI 协议通过将 SCSI（Small Computer System Interface）命令封装在 TCP/IP 协议中来实现存储设备的远程访问。iSCSI 的关键组成如下：

- iSCSI Initiator：计算机上运行的 iSCSI 客户端，用于连接到远程存储设备并发送SCSI命令。
- iSCSI Target：远程存储设备上运行的 iSCSI 服务器，用于接受 iSCSI Initiator 发送的 SCSI 命令，并将数据传输回 iSCSI Initiator。
- SCSI Command：用于访问存储设备的命令，例如读取和写入数据等。
- TCP/IP Protocol：用于在网络上传输 iSCSI 命令和数据的协议。

#### 1.1.1 配置 iSCSI Target

iSCSI Target 有多种实现，LIO（Linux-IO）是 Linux 的一个开源的 iSCSI Target 软件，它是Linux内核的一部分，可以提供高性能、可靠的iSCSI存储服务。targetcli 软件包可用于配置 LIO，可以帮助用户创建、管理和监控 iSCSI Target，以便将存储设备提供给 iSCSI Initiator 进行访问。

##### 1.1.1.1 安装 targetcli

安装 targetcli 软件包：

```
dnf install targetcli
```


启动 target 服务：

```
systemctl start target
```


将 target 服务配置为在引导时启动：

```
systemctl enable target
```


如果服务器开启了防火墙，在防火墙中打开 iSCSI target 的端口 3260，并重新载入防火墙配置：

```
firewall-cmd --permanent --add-port=3260/tcp
firewall-cmd --reload
```


##### 1.1.1.2 创建 iSCSI target 对象

创建具有 iQN 格式唯一标识的 iSCSI target 对象以便让 iSCSI 客户端可以访问服务器中的存储设备。 iSCSI Qualified Name（iQN）是用于标识 iSCSI Target 和 iSCSI Initiator 的唯一名称。其格式如下：

```
iqn.<YYYY>-<MM>.<domain>:<identifier>
```


其中，`<YYYY>`

-`<MM>`

表示iQN的版本号，`<domain>`

表示公司或组织的域名，`<identifier>`

是一个唯一的标识符。iQN名称必须唯一，并且不能包含特殊字符或空格。

通过以下命令创建iSCSI target 对象： 运行 targetcli 工具，在交互式界面中进入 iscsi 目录

```
# targetcli
targetcli shell version 2.1.54
Copyright 2011-2013 by Datera, Inc and others.
For help on commands, type 'help'.
/> cd iscsi
/iscsi>
```


然后，创建默认名称的 iSCSI target 对象：

```
/iscsi> create
Created target iqn.2003-01.org.linux-iscsi.hostname.x8664:sn.f07a9caf5f4a.
Created TPG 1.
Global pref auto_add_default_portal=true
Created default portal listening on all IPs (0.0.0.0), port 3260.
```


或创建特定 iQN 格式的 iSCSI target 对象：

```
/iscsi> create iqn.2023-01.com.expamle:storage.target01
Created target iqn.2023-01.com.expamle:storage.target01.
Created TPG 1.
Global pref auto_add_default_portal=true
Created default portal listening on all IPs (0.0.0.0), port 3260.
```


创建完成后在 backstores/iscsi/ 目录执行 ls 命令查看验证创建的 iSCSI target 对象：

```
o- iscsi .................................................................. [Targets: 2]
o- iqn.2003-01.org.linux-iscsi.lxs-ocs23.x8664:sn.f07a9caf5f4a ............. [TPGs: 1]
| o- tpg1 ..................................................... [no-gen-acls, no-auth]
| o- acls ................................................................ [ACLs: 0]
| o- luns ................................................................ [LUNs: 0]
| o- portals .......................................................... [Portals: 1]
| o- 0.0.0.0:3260 ........................................................... [OK]
o- iqn.2023-01.com.expamle:storage.target01 ................................ [TPGs: 1]
o- tpg1 ..................................................... [no-gen-acls, no-auth]
o- acls ................................................................ [ACLs: 0]
o- luns ................................................................ [LUNs: 0]
o- portals .......................................................... [Portals: 1]
o- 0.0.0.0:3260 ........................................................... [OK]
```


可以看到创建 iSCSI target 时也会创建一个默认门户。这个门户设置为使用默认端口号侦听所有 IP 地址： `0.0.0.0:3260`

。

##### 1.1.1.3 iSCSI 后端存储

iSCSI 后端存储（iSCSI Backstore），是指服务器上的存储设备或存储系统，它可以是硬盘、SSD、RAID存储系统、网络存储设备等。iSCSI Backstore 负责存储数据，并通过 iSCSI Target 向 iSCSI Initiator 提供数据访问服务。 Linux-IO(LIO) 支持以下后端存储设备：

-
FileIO是一种文件级别的 iSCSI 后端存储形式，它使用文件系统来管理数据存储。在FileIO中，iSCSI Target 将 iSCSI Initiator 发送的数据转换为文件系统中的文件，然后将数据存储在文件中。使用 FileIO 作为 iSCSI 后端存储可以提供更灵活的存储管理和更好的数据共享功能。 运行 targetcli 工具，在交互式界面中进入 backstores/fileio/ 目录创建 fileio 存储对象，然后执行 ls 命令验证： 以下示例中，file1 是 fileio 存储对象的名称，/tmp/test.img 是镜像文件路径。`fileio`

`/> cd backstores/fileio /backstores/fileio> create file1 /tmp/test.img Created fileio file1 with size 67108864 /backstores/fileio> ls o- fileio ......................................................... [Storage Objects: 1] o- file1 ............................ [/tmp/test.img (64.0MiB) write-back deactivated] o- alua ........................................................... [ALUA Groups: 1] o- default_tg_pt_gp ............................... [ALUA state: Active/optimized]`

-
Block是一种块级别的 iSCSI 后端存储形式，它使用块设备来管理数据存储。在 Block 中，iSCSI Target 将 iSCSI Initiator 发送的数据转换为块设备中的块，然后将数据存储在块中。使用 Block 作为 iSCSI 后端存储可以提供更高的数据传输速率和更好的数据保护。 运行 targetcli 工具，在交互式界面中进入 backstores/block/ 目录创建 block 存储对象，然后执行 ls 命令验证： 以下示例中，name参数指定块存储对象的名称， dev参数指定后端存储块设备。`Block`

`/> cd backstores/block /backstores/block> create name=block_backend dev=/dev/sda Created block storage object block_backend using /dev/sda. /backstores/block> ls o- block .......................................................... [Storage Objects: 1] o- block_backend ......................... [/dev/sda (16.0GiB) write-thru deactivated] o- alua ........................................................... [ALUA Groups: 1] o- default_tg_pt_gp ............................... [ALUA state: Active/optimized]`

-
PSCSI是一种传输数据的接口标准，使用平行传输技术，在SCSI总线上同时传输多个数据位。PSCSI 可以用于连接 iSCSI Target 和 iSCSI Initiator 之间的存储设备，例如硬盘、光驱、磁带机等。使用 PSCSI 接口连接 iSCSI Target 和 iSCSI Initiator 可以提供高速、高可靠性的数据存储和备份服务。 运行 targetcli 工具，在交互式界面中进入 backstores/pscsi/ 目录创建 pscsi 存储对象，然后执行 ls 命令验证： 以下示例中，name参数指定块存储对象的名称， dev参数指定后端存储块设备。`pscsi`

`/> cd backstores/pscsi /backstores/pscsi> create name=pscsi_backend dev=/dev/sr0 Note: block backstore recommended for SCSI block devices Created pscsi storage object pscsi_backend using /dev/sr0 /backstores/pscsi> ls o- pscsi .......................................................... [Storage Objects: 1] o- pscsi_backend .............................................. [/dev/sr0 deactivated] o- alua ........................................................... [ALUA Groups: 0]`

-
Ramdisk是一种虚拟存储设备，它将计算机内存中的一部分空间模拟成硬盘存储空间。Ramdisk可以作为一种 iSCSI 后端存储形式，用于提供临时存储或缓存服务。使用Ramdisk作为iSCSI后端存储可以提供更快的数据读写速度和更高的数据传输速率。 运行 targetcli 工具，在交互式界面中进入 backstores/ramdisk/ 目录创建 ramdisk 存储对象，然后执行 ls 命令验证： 以下示例中，name参数指定存储对象的名称， size指定用来模拟的内存大小`ramdisk`

`/> cd backstores/ramdisk /backstores/ramdisk> create name=rd_backend size=1GB Created ramdisk rd_backend with size 1GB. /backstores/ramdisk> ls o- ramdisk ........................................................ [Storage Objects: 1] o- rd_backend ................................................. [(1.0GiB) deactivated] o- alua ........................................................... [ALUA Groups: 1] o- default_tg_pt_gp ............................... [ALUA state: Active/optimized]`


##### 1.1.1.4 创建 iSCSI 门户

iSCSI 门户（Portal）是指 iSCSI Target和 iSCSI Initiator 之间的网络连接点。门户可以是物理网卡、虚拟网卡、IP 地址或 IP 地址范围等不同形式。门户用于连接 iSCSI Target和 iSCSI Initiator 之间的数据通道，以便进行数据传输和存储服务。

创建 iSCSI target 时也会创建一个默认门户。这个门户设置为使用默认端口号侦听所有 IP 地址：`0.0.0.0:3260`

。
若要删除默认门户后创建新的特定门户，方法如下：
运行 targetcli 工具，在交互式界面中进入 iSCSI target 对象的 TPG（target portal group）目录，并删除默认门户。

```
/> cd /iscsi/iqn.2023-01.com.expamle:storage.target01/tpg1/
/iscsi/iqn.20...target01/tpg1> portals/ delete ip_address=0.0.0.0 ip_port=3260
Deleted network portal 0.0.0.0:3260
```


然后，创建特定 IP 地址的门户，并执行 ls 命令验证：

```
/iscsi/iqn.20...target01/tpg1> portals/ create 192.168.1.
Using default IP port 3260
Created network portal 192.168.1.2:3260
/iscsi/iqn.20...target01/tpg1> ls
o- tpg1 ..................................................... [no-gen-acls, no-auth]
o- acls ................................................................ [ACLs: 0]
o- luns ................................................................ [LUNs: 0]
o- portals .......................................................... [Portals: 1]
o- 192.168.1.2:3260 ....................................................... [OK]
```


##### 1.1.1.5 创建 iSCSI LUN

在iSCSI中，LUN（Logical Unit Number）是指逻辑单元号码，它是一种逻辑上的存储单元，用于标识和管理iSCSI Target上的存储资源。LUN可以是硬盘、磁带、光驱等不同形式的存储设备，它们被分配给iSCSI Initiator作为可用的存储空间。 运行 targetcli 工具，在交互式界面中进入 iSCSI target 对象的 TPG（target portal group）目录，创建存储对象的 LUN，然后执行 ls 命令验证：

```
/> cd /iscsi/iqn.2023-01.com.expamle:storage.target01/tpg1/
/iscsi/iqn.20...target01/tpg1> luns/ create /backstores/fileio/file1
Created LUN 0.
/iscsi/iqn.20...target01/tpg1> luns/ create /backstores/block/block_backend
Created LUN 1.
/iscsi/iqn.20...target01/tpg1> luns/ create /backstores/ramdisk/rd_backend
Created LUN 2.
/iscsi/iqn.20...target01/tpg1> ls
o- tpg1 ..................................................... [no-gen-acls, no-auth]
o- acls ................................................................ [ACLs: 0]
o- luns ................................................................ [LUNs: 3]
| o- lun0 ...................... [fileio/file1 (/tmp/test.img) (default_tg_pt_gp)]
| o- lun1 .................... [block/block_backend (/dev/sda) (default_tg_pt_gp)]
| o- lun2 ................................ [ramdisk/rd_backend (default_tg_pt_gp)]
o- portals .......................................................... [Portals: 1]
o- 0.0.0.0:3260 ........................................................... [OK]
```


##### 1.1.1.6 iSCSI 访问控制

在 iSCSI 中，访问控制主要依赖于 CHAP 认证和 ACL。CHAP 认证和 ACL 即可以独立使用，也可以结合使用，以提供更高级别的安全控制。

** iSCSI CHAP 认证 **

CHAP 认证（Challenge Handshake Authentication Protocol）是一种用于在 iSCSI 连接过程中对设备进行验证的安全机制。CHAP 认证确保只有拥有正确用户名和密码的 iSCSI initiator 能够访问 iSCSI 目标。 通过默认参数创建的 iSCSI target 对象，CHAP 认证是默认关闭的。 运行 targetcli 工具，在交互式界面中进入 iSCSI target 对象的 TPG（target portal group）目录，将 CHAP 认证打开并设置userid和密码：

```
/iscsi/iqn.20...target01/tpg1> set attribute authentication=1
Parameter authentication is now '1'.
/iscsi/iqn.20...target01/tpg1> set auth userid=opencloudos
Parameter userid is now 'opencloudos'.
/iscsi/iqn.20...target01/tpg1> set auth password=opencloudos_passwd
Parameter password is now 'opencloudos_passwd'.
```


** iSCSI ACL **

ACL（访问控制列表）是一种基于访问权限对设备进行访问控制的安全机制。 iSCSI ACL 有如下三种情况：

- 如果存在 ACL，那么仅包含在 ACL 中的 initiator 可访问 iSCSI target。
- 如果不存在 ACL，且 tpg 的 generate_node_acls 属性值为 0，不会自动生成允许访问的 initiator 名单，因此 initiator 无法访问 iSCSI target。
- 如果不存在 ACL，且 tpg 的 generate_node_acls 属性值为 1，自动生成允许访问的 initiator 名单，所有 initiator 都可访问 iSCSI target。

通过默认参数创建的 iSCSI target 对象默认是第二种情况，可以通过以下任意一种方法使 iSCSI target 允许 initiator 访问：

-
将 initiator 名称手动添加到 ACL 中。 获取 initiator 中 /etc/iscsi/initiatorname.iscsi 文件中的 initiator 名称。 运行 targetcli 工具，在交互式界面中进入 iSCSI target 对象的 TPG（target portal group）目录，将initiator 添加 ACL 中并使用 ls 验证：

`/iscsi/iqn.20...target01/tpg1> acls/ create iqn.2023-01.org.opencloudos:cd5fc513ab43 Created Node ACL for iqn.2023-01.org.opencloudos:cd5fc513ab43 Created mapped LUN 0. Created mapped LUN 1. Created mapped LUN 2. /iscsi/iqn.20...target01/tpg1> ls o- tpg1 ........................................................ [gen-acls, no-auth] o- acls ................................................................ [ACLs: 1] | o- iqn.2023-01.org.opencloudos:cd5fc513ab43 ................... [Mapped LUNs: 3] | o- mapped_lun0 ...................................... [lun0 fileio/file1 (rw)] | o- mapped_lun1 ............................... [lun1 block/block_backend (rw)] | o- mapped_lun2 ................................ [lun2 ramdisk/rd_backend (rw)] o- luns ................................................................ [LUNs: 3] | o- lun0 ...................... [fileio/file1 (/tmp/test.img) (default_tg_pt_gp)] | o- lun1 .................... [block/block_backend (/dev/sda) (default_tg_pt_gp)] | o- lun2 ................................ [ramdisk/rd_backend (default_tg_pt_gp)] o- portals .......................................................... [Portals: 1] o- 0.0.0.0:3260 ........................................................... [OK]`

-
将 tpg 的

`generate_node_acls`

属性值修改为 1。注意，此方法建议结合 CHAP 认证使用，否则所有的 initiator 都可以访问 target，存着安全隐患。`/iscsi/iqn.20...target01/tpg1> set attribute generate_node_acls=1 Parameter generate_node_acls is now '1'.`


#### 1.1.2 配置 iSCSI 客户端

##### 1.1.2.1 安装 iscsi-initiator-utils

安装 iscsi-initiator-utils 软件包：

```
dnf install iscsi-initiator-utils
```


启动 iscsid 服务：

```
systemctl start iscsid
```


将 iscsid 服务配置为在引导时启动：

```
systemctl enable iscsid
```


##### 1.1.2.2 检查或修改 initiator 名称

iscsid服务启动后，会生成 `/etc/iscsi/initiatorname.iscsi`

文件。

```
# cat /etc/iscsi/initiatorname.iscsi
InitiatorName=iqn.2023-01.org.opencloudos:cd5fc513ab43
```


如果在配置 iSCSI target 创建 iSCSI ACL 时被指定了 initiator 名称，请相应地修改 `/etc/iscsi/initiatorname.iscsi`

文件。

##### 1.1.2.3 配置 CHAP 验证信息

initiator 默认不启用 CHAP 认证，可以在修改 /etc/iscsi/iscsid.conf 文件启用 initiator 的 CHAP 验证：

```
# vi /etc/iscsi/iscsid.conf
node.session.auth.authmethod = CHAP
```


并添加 iSCSI target 的用户名和密码：

```
node.session.auth.username = opencloudos
node.session.auth.password = opencloudos_passwd
```


重启 iscsid 守护进程：

```
systemctl restart iscsid
```


重新发现 target，来更新 node 配置信息。这一步是必需的，否则会出现 CHAP 验证信息没有更新到 node 配置里面，从而导致认证失败。

##### 1.1.2.4 发现 target

通过以下 iscsiadm 命令发现指定 IP 和端口的 iSCSI target：

```
# iscsiadm --mode discovery --type sendtargets --portal 192.168.1.110:3260
192.168.1.110:3260,1 iqn.2023-01.com.expamle:storage.target01
```


会返回 target 的 IQN 标识。 后续可以通过此 IQN 标识登录到 target。

##### 1.1.2.5 登录登出 target

在登录前，按照认证需求配置好 ACL 和 CHAP，否则会出现登录验证失败问题。

可以通过以下命令登录 target。

```
# iscsiadm --mode node -T iqn.2023-01.com.expamle:storage.target01 --login
Logging in to [iface: default, target: iqn.2023-01.com.expamle:storage.target01, portal: 192.168.1.110,3260]
Login to [iface: default, target: iqn.2023-01.com.expamle:storage.target01, portal: 192.168.1.110,3260] successful.
```


登出 target。

```
# iscsiadm --mode node -T iqn.2023-01.com.expamle:storage.target01 --logout
Logging out of session [sid: 24, target: iqn.2023-01.com.expamle:storage.target01, portal: 192.168.1.110,3260]
Logout of [sid: 24, target: iqn.2023-01.com.expamle:storage.target01, portal: 192.168.1.110,3260] successful.
```


##### 1.1.2.6 监控 iSCSI 会话

查找正在运行的会话的信息：

```
# iscsiadm -m session -P 3
iSCSI Transport Class version 2.0-870
version 6.2.1.4
Target: iqn.2023-01.com.expamle:storage.target01 (non-flash)
Current Portal: 192.168.1.110:3260,1
Persistent Portal: 192.168.1.110:3260,1
**********
Interface:
**********
Iface Name: default
Iface Transport: tcp
Iface Initiatorname: iqn.2023-01.org.opencloudos:cd5fc513ab43
Iface IPaddress: 192.168.1.111
......
```


-P 3 会显示最全的信息，包括会话或设备状态、会话 ID、一些协商的参数以及可通过会话访问的 SCSI 设备。 如果只需要简短的输出，可以指定 -P 0 、-P 1 或 -P 2。

### 1.2 FCoE

FCoE（Fibre Channel over Ethernet）是一种用于封装光纤通道（FC）协议以通过以太网传输数据的网络技术。FCoE 使传统的以太网网络能够承载光纤通道协议，从而实现通过单一网络同步传输SCSI、IP和其他协议的数据。这样可以简化数据中心内部的网络架构，并降低成本。

#### 1.2.1 安装 FCoE 软件包

安装 fcoe-utils 软件包：

```
dnf install fcoe-utils
```


启用 ldpad 服务，需要确保以太网交换机开启了Data Center Bridging (DCB)功能，lldpad 服务用于 DCB 协议的实现。

```
systemctl start lldpad
```


将 ldpad 服务配置为在引导时启动：

```
systemctl enable lldpad
```


#### 1.2.2 配置和激活 FCoE 接口

确定要创建 FCoE 连接的物理以太网接口，运行以下命令，以太网网络设备上启用FCoE：

```
fcoeadm -i ens18
```


使用以下命令激活已创建的 FCoE 接口：

```
fcoeadm -e ens18
```


FCoE接口激活后可以与光纤通道网络进行通信。

### 1.3 NVMe over Fabrics

NVMe over Fabrics（简称 NVMe-oF）是一种用于在网络中远程访问和共享非易失性内存设备（如固态硬盘）的协议。NVMe-oF 旨在充分利用 NVMe（Non-Volatile Memory Express）协议的高延迟和高吞吐量特性，以实现接近本地连接的远程存储性能

#### 1.3.1 配置 NVMe-oF target

##### 1.3.1.1 安装 nvmetcli

安装 nvmetcli 软件包：

```
dnf install nvmetcli
```


启动 nvmet 服务：

```
systemctl start nvmet
```


将 nvmet 服务配置为在引导时启动：

```
systemctl enable nvmet
```


如果服务器开启了防火墙，在防火墙中打开 NVMe target 的端口 4420，并重新载入防火墙配置：

```
firewall-cmd --permanent --add-port=4420/tcp
firewall-cmd --reload
```


##### 1.3.1.2 创建 NVMe 子系统

创建 NVMe 子系统：

```
# nvmetcli
/> cd subsystems
/subsystems> create nqn.2023-01.com.example:nvme:tcp
/subsystems> ls
o- subsystems ............................................................... [...]
o- nqn.2023-01.com.example:nvme:tcp [version=1.3, allow_any=0, serial=cd01892890f4dce748ed]
o- allowed_hosts ........................................................ [...]
o- namespaces ........................................................... [...]
```


创建命名空间：

```
/subsystems> cd nqn.2023-01.com.example:nvme:tcp/
/subsystems/n...e:nvme:tcp> cd namespaces
/subsystems/n...ic/namespaces> create nsid=1
```


命名空间关联块设备并使能：

```
/subsystems/n...ic/namespaces> cd 1
/subsystems/n.../namespaces/1> set device path=/dev/sda
Parameter path is now '/dev/sda'.
/subsystems/n.../namespaces/1> enable
The Namespace has been enabled.
```


设置允许访问的的主机

- 允许所有主机访问

```
/subsystems/n...e:nvme:tcp> set attr allow_any_host=1
Parameter allow_any_host is now '1'.
```


- 可以只允许特定的主机访问，需要先在 hosts 目录创建主机 nqn，再到子系统的 allowed_hosts 关联︰

```
/subsystems> cd /hosts/
/hosts> create nqn.2023-01.com.example:nvme:initiator
/hosts> cd /subsystems/nqn.2023-01.com.example:nvme:fabric/allowed_hosts/
/subsystems/n...allowed_hosts> create nqn.2023-01.com.example:nvme:initiator
```


验证创建的子系统

```
/subsystems> ls
o- subsystems ............................................................... [...]
o- nqn.2023-01.com.example:nvme:tcp [version=1.3, allow_any=0, serial=cd01892890f4dce748ed]
o- allowed_hosts ........................................................ [...]
| o- nqn.2023-01.com.example:nvme:initiator ............................. [...]
o- namespaces ........................................................... [...]
o- 1 [path=/dev/sda, uuid=c167f008-0623-49d6-99c5-3b1891d56e49, grpid=1, enabled]
```


##### 1.3.1.2 创建 NVMe 传输端口

创建传输端口：

```
/> cd ports
/ports> create portid=1
/ports> cd 1
/ports/1> set addr adrfam=ipv4 trtype=tcp traddr=0.0.0.0 trsvcid=4420
Parameter adrfam is now 'ipv4'.
Parameter trtype is now 'tcp'.
Parameter traddr is now '0.0.0.0'.
Parameter trsvcid is now '4420'.
```


示例中创建协议类型为tcp的传输端口，监听的 IP 地址和端口为 0.0.0.0: 4420。

将传输端口和子系统关联：

```
/ports/1> cd subsystems
/ports/1/subsystems> create nqn.2023-01.com.example:nvme:tcp
```


验证创建的传输端口

```
/ports> ls
o- ports .................................................................... [...]
o- 1 ......... [trtype=tcp, traddr=0.0.0.0, trsvcid=4420, inline_data_size=16384]
o- ana_groups ........................................................... [...]
| o- 1 ...................................................... [state=optimized]
o- referrals ............................................................ [...]
o- subsystems ........................................................... [...]
o- nqn.2023-01.com.example:nvme:fabric ................................ [...]
```


#### 1.3.2 配置 nvme-cli

安装 nvme-cli 命令行工具。

```
dnf install nvme-cli
```


加载传输端口使用的协议对应的内核模块，

```
modprobe nvme-tcp
```


发现 NVMe-oF target，命令格式为：

```
nvme discover -t TRANSPORT -a DISCOVERY_CONTROLLER_ADDRESS -s SERVICE_ID
```


如

```
# nvme discover -t tcp -a 192.168.1.110 -s 4420
Discovery Log Number of Records 1, Generation counter 6
=====Discovery Log Entry 0======
trtype: tcp
adrfam: ipv4
subtype: current discovery subsystem
treq: not specified, sq flow control disable supported
portid: 1
trsvcid: 4420
subnqn: nqn.2014-08.org.nvmexpress.discovery
traddr: 192.168.1.110
eflags: none
sectype: none
```


连接 NVMe-oF target

```
nvme connect -t tcp -a 192.168.1.110 -s 4420 -n nqn.2023-01.com.example:nvme:tcp
```


查看新添加到系统的nvme盘

```
# nvme list
Node Generic SN Model Namespace Usage Format FW Rev
--------------- -------------- -------------------- ------------ ---------- ----------------------- ---------------- --------
/dev/nvme0n1 /dev/ng0n1 cd01892890f4dce748ed Linux 0x1 17.18 GB / 17.18 GB 512 B + 0 B 6.1.26-2
# nvme list-subsys
nvme-subsys0 - NQN=nqn.2023-01.com.example:nvme:fabric
\
+- nvme0 tcp traddr=192.168.1.110,trsvcid=4420,src_addr=192.168.1.111 live
# lsblk
NAME MAJ:MIN RM SIZE RO TYPE MOUNTPOINTS
vda 253:0 0 50G 0 disk
├─vda1 253:1 0 1M 0 part
└─vda2 253:2 0 50G 0 part /
nvme0n1 259:1 0 16G 0 disk
```


可见系统中添加了一个 16G 的 nvme 盘。

## 2 多路径 I/O

多路径设备 (Multipath devices) 是一种提供冗余和负载平衡连接的技术。通常情况下，本地设备不需要配置为多路径设备，因为它们只有一个物理路径连接到服务器。多路径配置主要适用于连接到多个控制器或交换机的共享存储设备（如 SAN 存储中的设备），通过这种方式能提供冗余、负载均衡和故障转移能力。

存储区域网络（SAN）是一种专用的高速网络，将服务器与独立的共享存储设备（例如磁盘阵列或磁带库）连接起来。SAN提供了一种集中式存储架构，允许多个服务器访问这些共享存储设备，并将其视为本地存储。SAN 网络通常采用 Fibre Channel（光纤通道）或 iSCSI 协议传输数据。

在 Linux 中，由 Device Mapper 内核组件实现对多路径设备的抽象和管理，device-mapper-multipath 软件包提供用户态多路径设备管理功能，它主要提供如下功能：

- multipath 命令：用于创建、删除和管理多路径设备。
- multipathd 守护程序：后台运行服务，监控路径状态、路径故障及其恢复。
- 库文件和配置文件：提供了创建和管理多路径设备所需的基本功能和设置。

以下介绍 device-mapper-multipath 软件包的使用方法。

### 2.1 安装device-mapper-multipath

系统默认不安装 device-mapper-multipath，若系统没有安装该软件包，可以使用以下命令安装：

```
dnf install device-mapper-multipath
```


安装后，系统默认会在启动时自动启动 multipathd 服务和加载 dm-multipath 模块，以便系统能够自动管理多路径设备。因此在安装完成后，可以通过重启服务器来启动 multipathd 服务。

若要在不重启服务器的情况下启动 multipathd 服务，需要先使用以下命令确保系统加载 dm-multipath 内核模块：

```
modprobe dm-multipath
```


然后再启动 multipathd 服务：

```
systemctl start multipathd
```


启动后，multipathd 会自动创建和删除多路径设备并监控路径。 如通过多个网络接口连接到同一 iSCSI target：

```
# iscsiadm --mode session -P 1
Target: iqn.2023-01.com.expamle:storage.target01 (non-flash)
Current Portal: 192.168.1.110:3260,1
Persistent Portal: 192.168.1.110:3260,1
......
Iface Initiatorname: iqn.2023-01.org.opencloudos:4adcc7b7850
Iface IPaddress: 192.168.1.111
......
Internal iscsid Session State: NO CHANGE
Current Portal: 192.168.2.110:3260,1
Persistent Portal: 192.168.2.110:3260,1
......
Iface Initiatorname: iqn.2023-01.org.opencloudos:4adcc7b7850
Iface IPaddress: 192.168.2.111
......
Internal iscsid Session State: NO CHANGE
```


multipathd 就会自动识别多条链路上的 iSCSI 设备，并创建多路径设备：

```
# multipath -l
mpatha (36001405c142596a6bff46e89e75bc3b3) dm-1 LIO-ORG,file1
size=64M features='1 queue_if_no_path' hwhandler='1 alua' wp=ro
`-+- policy='service-time 0' prio=0 status=active
|- 3:0:0:0 sda 8:0 active undef running
`- 2:0:0:0 sdb 8:16 active undef running
mpathb (3600140514f70dd82701490da74f98e30) dm-0 LIO-ORG,rd_backend
size=1.0G features='1 queue_if_no_path' hwhandler='1 alua' wp=ro
`-+- policy='service-time 0' prio=0 status=active
|- 2:0:0:1 sdc 8:32 active undef running
`- 3:0:0:1 sdd 8:48 active undef running
```


### 2.2 配置 multipath.conf

multipathd 服务首次运行时会 multipath.conf 文件，若需要对默认配置进行修改，可以打开 `/etc/multipath.conf`

文件进行编辑：

```
vi /etc/multipath.conf
```


对以下内容进行修改：

```
defaults {
user_friendly_names yes
find_multipaths yes
path_grouping_policy multibus
path_checker readsector0
prio const
failback immediate
rr_min_io 100
no_path_retry 18
}
```


- user_friendly_names 配置 multipath 守护程序如何为多路径设备分配名称。此选项设置为yes，则多路径设备将使用可读的别名（如mpatha）。设置为no，系统将使用设备的UUID作为名称。建议使用yes以便于识别和管理设备。
- find_multipaths 设置为 yes 时，通知多路径工具检测硬件属性相同的设备，并将其视为同一多路径设备。默认为yes。
- path_grouping_policy 定义了多路径设备如何将各个路径归组。可用选项包括 failover、 multibus、 group_by_serial、 group_by_prio等。
- path_checker 设定用于检查路径有效性的方法。有效值为readsector0、tur（Test Unit Ready）等。默认值通常为 readsector0。
- path_prio 设置多路径设备的路径优先级策略。对于某些存储提供商，可能需要将其设置为alua，以更好地利用 Advanced Asymmetric Logical Unit Access 策略。
- rr_min_io 对于轮询策略，此值定义了在将 I/O 切换到下一个路径之前，要处理的最小读/写请求数。越高的值将导致在切换路径前处理更多的 I/O ，从而减少开销。
- no_path_retry 所有路径都失效后重试连接的次数。可以使用数字或queue（无限重试直到路径可用）。

若想排除那些不想被识别为多路径设备的设备，可以添加以下配置：

```
blacklists {
devnode: "^(ram|raw|loop|sr|fd|zram)[a-z0-9]*"
}
```


保存对配置文件的修改后，需要重启多路径守护进程使新的配置生效：

```
systemctl restart multipathd
```


### 2.3 multipath 命令

#### 2.3.1 查看多路径设备

显示所有多路径设备： 要查看系统上当前配置的所有多路径设备，可以使用 -ll 或 -l 选项。

```
# multipath -l
mpatha (36001405c142596a6bff46e89e75bc3b3) dm-1 LIO-ORG,file1
size=64M features='1 queue_if_no_path' hwhandler='1 alua' wp=ro
`-+- policy='service-time 0' prio=0 status=active
|- 3:0:0:0 sda 8:0 active undef running
`- 2:0:0:0 sdb 8:16 active undef running
mpathb (3600140514f70dd82701490da74f98e30) dm-0 LIO-ORG,rd_backend
size=1.0G features='1 queue_if_no_path' hwhandler='1 alua' wp=ro
`-+- policy='service-time 0' prio=0 status=active
|- 2:0:0:1 sdc 8:32 active undef running
`- 3:0:0:1 sdd 8:48 active undef running
```


显示某个特定多路径设备： 要查看关于特定多路径设备的信息，请在命令后附加设备名称。

```
# multipath -ll mpatha
mpatha (36001405c142596a6bff46e89e75bc3b3) dm-1 LIO-ORG,file1
size=64M features='1 queue_if_no_path' hwhandler='1 alua' wp=ro
`-+- policy='service-time 0' prio=50 status=active
|- 3:0:0:0 sda 8:0 active ready running
`- 2:0:0:0 sdb 8:16 active ready running
```


#### 2.3.2 创建新的多路径设备

大部分情况下 multipathd 会自动识别和创建多路径设备。如果环境中有连接到相同的存储设备但属于不同的路径的 /dev/sdX 和 /dev/sdY 等类似的设备，multipathd 没有自动识别和创建，可以通过以下命令手动创建多路径设备：

```
multipath /dev/sdX /dev/sdY
```


#### 2.3.3 删除不再存在的多路径设备

要删除过期的多路径设备，可以使用 -f 选项删除：

```
multipath -f /dev/sdX
```


#### 2.3.4 禁用某条路径

要禁用某条特定的路径，可以使用 -B 选项禁用

```
multipath -B /dev/sdX
```


#### 2.3.5 重新加载多路径配置

对 `/etc/multipath.conf`

文件进行修改后，请使用以下命令重新加载配置：

```
multipath -v2
```


执行 multipath -v2 仅会重新扫描新的多路径，并不会应用存储在配置文件中的其他设置。 为了确保所有更改生效，建议在修改 /etc/multipath.conf 文件后重启 multipathd 服务。

## 3 网络文件共享

### 3.1 NFS

NFS（网络文件系统，Network File System）协议是一个用于访问远程文件系统的分布式网络协议。它允许客户端（在不同的操作系统上）访问和操作储存在网络上其他计算机的文件和文件夹。

#### 3.1.1 安装并启动NFS 服务

系统默认已安装 nfs-utils 软件包，若未安装，可以使用以下命令安装 nfs-utils 软件包：

```
dnf install nfs-utils
```


启动NFS服务

```
systemctl start nfs-server
```


将 NFS 服务配置为在引导时启动：

```
systemctl enable nfs-server
```


#### 3.1.2 配置exports文件

/etc/exports 文件用于定义要共享的文件系统、允许访问这些文件系统的客户端和其权限。 每行都表示一个共享的文件系统。每个定义的格式如下：

```
<directory> <host1>(<options>) <host2>(<options>) ...
```


`<directory>`

是要共享的服务器上的路径，例如 /srv/nfs/shared_directory。`<host>`

表示允许访问共享目录的客户端，可以是主机名、IP地址、子网或通配符（如*）。`<options>`

描述了共享的目录将如何被访问。主要选项有：- ro：以只读模式挂载。
- rw：以读写模式挂载。
- sync：同步提交更改，有助于实现数据一致性。
- async：异步提交更改，提高性能，但可能会损失数据一致性。
- no_root_squash：允许对共享目录具有根权限的客户端（即仅适用于非公共目录）。
- root_squash：对共享目录具有根权限的客户端使用nobody用户进行映射（默认行为，适用于公共目录）。
- all_squash：将所有用户和组映射为nobody用户。
- no_subtree_check：禁用子树检查，减少NFS的开销（建议选项）。

如允许多个客户端访问共享文件系统，并提供不同的权限：

```
/srv/nfs/shared 192.168.1.111(rw,sync,no_subtree_check) 192.168.1.112(ro,sync,no_subtree_check)
```


在创建或编辑/etc/exports文件后，需要重新加载NFS服务以应用更改：

```
exportfs -ra
```


或重启NFS服务以应用更改：

```
systemctl restart nfs-server
```


#### 3.1.3 客户端挂载共享目录

在客户端上挂载 NFS 共享目录时，可以指定一些配置选项来调整挂载设置。客户端也需要已安装 nfs-utils 软件包，才可以进行 NFS 挂载。 以下将详细介绍 NFS 客户端挂载配置。

##### 3.1.3.1 mount 命令挂载 NFS

使用 mount 命令手动挂载 NFS 共享目录：

```
mount -t nfs <server-ip>:/path/to/shared_directory /local/mount/directory -o <option>
```


`-t nfs`

指定文件系统类型为NFS。`<server-ip>`

NFS服务器的IP地址。`/path/to/shared_directory`

在NFS服务器上要共享的目录。`/local/mount/directory`

在客户端上要挂载NFS共享目录的本地目录。`-t <option>`

挂载选项，以逗号隔开`vers=<NFS version>`

：使用指定的NFS版本（例如，2, 3或 4）。`proto=<network protocol>`

：选择要用于传输数据的协议，如 udp 或 tcp。`hard`

：在NFS服务器不可用或失去连接时，应用程序会保持阻塞状态（默认选项）。`soft`

：当NFS服务器不可用或失去连接时，允许应用程序报告 I/O 错误。`intr`

：允许用户中断挂起的硬盘挂载。`rsize=<bytes>`

：指定客户端每次从NFS服务器读取的字节大小。`wsize=<bytes>`

：指定客户端每次向NFS服务器写入的字节大小。`timeo=<timeout>`

：设置读写超时（以十分之一秒为单位）。`retrans=<retries>`

：在超时后允许的重新传输次数。`nolock`

：禁用NFS客户端和服务器上的文件锁定。`noatime`

：禁止在访问文件时改变文件的访问时间。

如使用NFS版本3，软挂载和自定义读写大小挂载共享目录：

```
mount -t nfs -o vers=3,soft,rsize=32768,wsize=32768 192.168.1.110:/srv/nfs/shared /mnt/nfs/shared
```


##### 3.1.3.2 fstab 文件配置自动挂载 NFS

为了在每次启动系统时自动挂载NFS共享目录，需要在 `/etc/fstab`

文件中添加以下条目：

```
<server-ip>:/path/to/shared_directory /local/mount/directory nfs <options> 0 0
```


各个选项参考 mount 命令挂载 NFS 章节

如每次启动系统时自动挂载NFS共享目录：

```
192.168.1.110:/srv/nfs/shared /mnt/nfs/sharednfs vers=3,soft,rsize=32768,wsize=32768 0 0
```


##### 3.1.3.3 验证挂载的 nfs 文件系统

使用以下命令验证 nfs 文件系统是否挂载成功

```
# df -T | grep nfs
192.168.1.110:/srv/nfs/shared nfs 51287520 6336960 42312896 14% /mnt/nfs/shared
```


### 3.2 Samba

Samba是一款用于在Linux/Unix和Windows计算机之间共享文件和打印机的软件，以下是介绍使用Samba文件共享的简要步骤。

#### 3.2.1 安装并启动Samba 服务

可以使用以下命令安装 samba 软件包：

```
dnf install samba
```


启动 samba 服务

```
systemctl start smb
```


将 NFS 服务配置为在引导时启动：

```
systemctl enable smb
```


#### 3.2.2 配置 Samba

编辑配置文件 `/etc/samba/smb.conf`

以定义共享设置，在文件末尾添加以下内容来配置新的共享：

```
[SharedDirectory]
path = /srv/samba/shared
browseable = yes
read only = no
create mask = 0644
directory mask = 0755
guest ok = yes
```


`[SharedDirectory]`

中括号中的 SharedDirectory 为定义的共享目录名称`path`

服务器上的共享目录路径。`browseable`

指示共享是否可以在网络邻居中列出。`read only`

定义共享的只读访问权限（设置为no可同时进行读写）。`create mask`

指定文件创建时的文件权限。`directory mask`

指定目录创建时的目录权限。`guest ok`

指示客户端是否能够访问共享，而无需提供密码。

当设置了guest ok = no 时，需要创建Samba用户。先在Linux系统上创建一个新用户：

```
sudo useradd samba_user
```


然后为 Samba 服务创建相同的用户，并设置密码：

```
smbpasswd -a samba_user
```


更改或编辑 smb.conf 文件后，需要重新启动Samba服务以应用更改：

```
systemctl restart smb
```


对于配置好上述内容仍然无法访问samba的共享文件夹的部分情况下，重新可以解决该问题。

#### 3.2.3 客户端访问 Samba 共享

客户端要访问 Samba 共享，需要安装 cifs-utils 软件包：

```
dnf install cifs-utils
```


以下将详细介绍 Samba 客户端挂载配置。

#### 3.2.3.1 使用 mount 命令挂载 Samba 共享

使用下面的 mount 命令挂载 Samba 共享。

```
mount -t cifs -o username=<samba_user>,password=<samba_password> //<server-ip>/SharedDirectory /mnt/samba/shared
```


`<samba_user>`

Samba 用户名`<samba_password>`

Samba 密码`<server-ip>`

Samba 服务的IP 地址`SharedDirectory`

Samba 服务在`/etc/samba/smb.conf`

文件中定义的共享名称`/mnt/samba/shared`

本地挂载目录

若 Samba 共享允许访客访问，可以使用以下命令：

```
mount -t cifs -o guest //<server-ip>/SharedDirectory /mnt/samba/shared
```


#### 3.2.3.2 fstab 文件配置自动挂载 Samba

要在系统重启后自动挂载共享，请在 `/etc/fstab`

文件中添加以下条目:

```
//<server-ip>/SharedDirectory /mnt/samba/shared cifs credentials=/etc/samba-credentials.txt,uid=1000,gid=1000 0 0
```


`<server-ip>`

Samba 服务的IP地址`SharedDirectory`

Samba 服务在`/etc/samba/smb.conf`

文件中定义的共享名称。`/mnt/samba/shared`

本地挂载 Samba 共享的目录。`credentials`

凭据文件的路径，该文件包含Samba用户名和密码。`uid`

本地用户的用户 ID，默认为 nobody 用户的用户 ID。`gid`

本地用户的组 ID，默认为 nobody 用户的组 ID。

然后在 `/etc`

目录下创建一个名为 `/etc/samba-credentials.txt`

的文件，包含Samba用户名和密码：

```
username=<samba_user>
password=<samba_password>
```


更改凭据文件的权限以保护它：

```
chmod 600 /etc/samba-credentials.txt
```


##### 3.1.3.3 验证挂载的 Samba 共享

使用以下命令验证 Samba 共享是否挂载成功

```
# df -T | grep cifs
//192.168.1.110/SharedDirectory cifs 51287520 8980936 42306584 18% /mnt/samba/shared
```