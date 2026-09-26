source: https://docs.opencloudos.org/en/OCS/Storage_Filesystem_Administration_Guide/Diskpart_management/

# 磁盘和分区管理

## 1.磁盘类型

在 Linux 系统中，磁盘都以块设备文件的形式出现在 /dev 目录下，根据磁盘接口类型的不同，磁盘块设备文件名称也不同，形式如下：

磁盘接口类型 |
磁盘块设备文件名 |
说明 |
例子 |
|---|---|---|---|
| SCSI/SATA/SAS | /dev/sdX | X 表示字母 a-z，依次对应存储设备。当该类型的磁盘数量超过 26 个时，使用两个字母，如 /dev/sdaa。 | /dev/sda |
| virtioblk | /dev/vdX | X 表示字母 a-z，依次对应存储设备。 | /dev/vda |
| NVMe | /dev/nvmeXnY | X 表示 NVMe 控制器编号（从 0 开始），Y 表示 NVMe 命名空间编号（从 1 开始）。命名空间通常与存储设备相对应。 | /dev/nvme0n1 |
| IDE | /dev/hdX | X 表示字母 a-z，依次对应存储设备。 | /dev/hda |

## 2.磁盘分区

通常在使用磁盘前，会将其分成一个或者多个逻辑区域，即磁盘分区。

划分好的磁盘分区会以块设备文件的形式出现在 /dev 目录下，形式如下：

磁盘块设备文件名 |
磁盘分区块设备文件名 |
说明 |
例子 |
|---|---|---|---|
| /dev/sdX | /dev/sdXN | N 表示分区编号（从 1 开始）。 | /dev/sda1 |
| /dev/vdX | /dev/vdXN | N 表示分区编号（从 1 开始）。 | /dev/vda1 |
| /dev/nvmeXnY | /dev/nvmeXnYpN | N 表示分区编号（从 1 开始）。 | /dev/nvme0n1p1 |
| /dev/hdX | /dev/hdXN | N 表示分区编号（从 1 开始）。 | /dev/hda1 |

### 2.1.磁盘分区表

在对磁盘分区前需要创建磁盘分区表，分区表保存了磁盘分区信息。OpenCloudOS 主要使用 MSDOS(MBR) 和 GPT（GUID Partition Table）两种类型的分区表。

分区表 |
最多分区数 |
最大分区大小 |
|---|---|---|
| MSDOS(MBR) | 4 个主分区或 3 个主分区和 1 个扩展分区（可以划分成多个逻辑分区） | 2TiB（扇区大小为 512B）16TiB（扇区大小为 4KB） |
| GPT | 128 | 8ZiB（扇区大小为 512B）64ZiB（扇区大小为 4KB） |

### 2.2.MSDOS 分区表

MSDOS分区表存在在磁盘的第一个扇区，通常是 512B 大小，主要包含如下数据：

- 主引导记录（Master Boot Record, MBR）:可以安装 bootloader 程序，大小为 446B
- 分区表（Partition Table）：记录磁盘分区信息，大小为 64B ，每个分区信息占用 16B，最多包含四个分区信息
- MBR 标记：内容是 55AA，大小为 2B

通常 legacy 引导下，使用 msdos 分区表，示例如下：

```
$ lsblk
NAME MAJ:MIN RM SIZE RO TYPE MOUNTPOINTS
sda 8:0 0 50G 0 disk
├─sda1 8:1 0 1G 0 part /boot
└─sda2 8:2 0 49G 0 part
├─os-root 253:0 0 30G 0 lvm /
└─os-home 253:1 0 19G 0 lvm /home
$ parted /dev/sda print
Model: ATA QEMU HARDDISK (scsi)
Disk /dev/sda: 53.7GB
Sector size (logical/physical): 512B/512B
Partition Table: msdos
Disk Flags:
Number Start End Size Type File system Flags
1 1049kB 1075MB 1074MB primary ext4 boot
2 1075MB 53.7GB 52.6GB primary lvm
```


示例中的系统盘使用了 msdos 分区表，总共有两个分区，一个 boot 分区，另一个分区作为逻辑卷的物理卷使用。

### 2.3.GPT 分区表

GPT 分区表使用 LBA 对磁盘进行编址，每个 LBA 512B。GPT 分区结构如下：

- LBA0：MBR 兼容区块，前 446B 存放 bootloader（UEFI 引导下，bootloader 不存放在此处），后 66B 为特殊标记，表明此磁盘为 GPT 分区
- LBA1：GPT 表头记录，记录分区表本身的位置和大小，备份分区放置的位置以及 CRC32 校验码
- LBA(2~33)：分区表，记录分区信息，每个 LBA 可以记录 4 个分区信息。
- LBA(-1)：GPT 表头记录的备份
- LBA(-33~-2)：分区表的备份

UEFI 引导下，使用 GPT 分区表，示例如下：

```
$ lsblk
NAME MAJ:MIN RM SIZE RO TYPE MOUNTPOINTS
sda 8:0 0 64G 0 disk
├─sda1 8:1 0 50M 0 part /boot/efi
├─sda2 8:2 0 512M 0 part /boot
└─sda3 8:3 0 63.4G 0 part
├─os-root 253:0 0 30G 0 lvm /
└─os-home 253:1 0 33.4G 0 lvm /home
$ parted /dev/sda print
Model: ATA Fedora Linux-0 S (scsi)
Disk /dev/sda: 68.7GB
Sector size (logical/physical): 512B/4096B
Partition Table: gpt
Disk Flags:
Number Start End Size File system Name Flags
1 1049kB 53.5MB 52.4MB fat16 EFI System Partition boot, esp
2 53.5MB 590MB 537MB ext4
3 590MB 68.7GB 68.1GB lvm
```


示例中的系统盘使用了 GPT 分区表，总共有三个分区，一个 EFI 分区，一个 boot 分区，另一个分区作为逻辑卷的物理卷使用。

## 3.磁盘及分区管理工具

### 3.1.使用 lsblk 查看块设备信息

lsblk 可以列出块设备信息，如下所示：

```
[root@localhost ~]# lsblk
NAME MAJ:MIN RM SIZE RO TYPE MOUNTPOINTS
sda 8:0 0 60G 0 disk
├─sda1 8:1 0 1M 0 part
├─sda2 8:2 0 1G 0 part /boot
└─sda3 8:3 0 59G 0 part
├─os-root 253:0 0 39.6G 0 lvm /
└─os-home 253:1 0 19.4G 0 lvm /home
sdb 8:16 0 30G 0 disk
├─sdb1 8:17 0 1G 0 part
├─sdb2 8:18 0 1G 0 part
├─sdb3 8:19 0 1K 0 part
├─sdb4 8:20 0 26G 0 part
└─sdb5 8:21 0 1G 0 part
sr0 11:0 1 13.8G 0 rom
```


- NAME：磁盘或分区设备名
- MAJ:MIN：磁盘或分区主次设备号
- RM：是否为可移除设备，0 表示不可移除，1 表示可移除
- SIZE：磁盘或分区容量
- RO：是否为只读设备，0 表示只读，1 表示非只读
- TYPE：设备类型，disk 表示磁盘，part 表示分区，lvm 表示逻辑卷
- MOUNTPOINTS：挂载点

另外，从 lsblk 的输出中还可以看出磁盘分区之间的从属关系。

更详细命令选项，可以参考 man 手册。

### 3.2.使用 blkid 查看块设备信息

blkid 可以打印出设备属性，如下所示：

```
[root@localhost ~]# blkid
/dev/mapper/os-home: UUID="f30c7d4a-c97d-427e-ba4e-24e28ffdebf5" BLOCK_SIZE="4096" TYPE="ext4"
/dev/sr0: BLOCK_SIZE="2048" UUID="2023-05-08-12-35-52-00" LABEL="OpenCloudOS" TYPE="iso9660" PTTYPE="PMBR"
/dev/mapper/os-root: UUID="2985bd9c-facc-49eb-8752-6c41915e65db" BLOCK_SIZE="4096" TYPE="ext4"
/dev/sda2: UUID="57139a63-0e14-410b-ae05-c395732c206b" BLOCK_SIZE="4096" TYPE="ext4" PARTUUID="846b8e84-0d7e-484f-9cb"
/dev/sda3: UUID="q6Vgxu-Wvpn-d3M9-c8Hk-dMT0-YXuM-Dccaml" TYPE="LVM2_member" PARTUUID="5d88c31f-ab83-46bd-b74e-bc507cc"
/dev/sdb4: PARTUUID="1144bcd9-04"
/dev/sdb2: PARTUUID="1144bcd9-02"
/dev/sdb5: PARTUUID="1144bcd9-05"
/dev/sdb1: PARTUUID="1144bcd9-01"
/dev/sda1: PARTUUID="603c9161-aa71-4196-bbb8-e138dd0421b5"
```


冒号前面的部分表示设备，后面的部分表示设备或文件系统属性。

更详细命令选项，可以参考 man 手册。

### 3.3.使用 parted 操作磁盘分区

#### 3.3.1.parted 概述

parted 命令支持 MSDOS 和 GPT 两种分区表，可以执行查看分区信息、创建分区表、创建分区、修改分区和删除分区等磁盘操作。

parted 命令支持交互式和命令行两种形式，直接执行 parted block-device 可以进入交互式界面，如下：

```
$ parted block-device
(parted)
```


在交换界面可以直接使用子命令。输入 help，可以查看支持的所有子命令，如下：

```
(parted) help
```


输入 help COMMAND，可以查看子命令 COMMAND 的用法，如下：

```
(parted) help COMMAND
```


输入 quit 可以退出交互界面。

```
(parted) quit
```


示例如下：

下面的示例进入交互界面，使用的磁盘是 /dev/sdb，执行了 help，然后退出交互界面。

```
[root@localhost ~]# parted /dev/sdb
GNU Parted 3.5
Using /dev/sdb
Welcome to GNU Parted! Type 'help' to view a list of commands.
(parted) help
align-check TYPE N check partition N for TYPE(min|opt) alignment
help [COMMAND] print general help, or help on COMMAND
mklabel,mktable LABEL-TYPE create a new disklabel (partition table)
mkpart PART-TYPE [FS-TYPE] START END make a partition
name NUMBER NAME name partition NUMBER as NAME
print [devices|free|list,all] display the partition table, or available devices, or free space,
or all found partitions
quit exit program
rescue START END rescue a lost partition near START and END
resizepart NUMBER END resize partition NUMBER
rm NUMBER delete partition NUMBER
select DEVICE choose the device to edit
disk_set FLAG STATE change the FLAG on selected device
disk_toggle [FLAG] toggle the state of FLAG on selected device
set NUMBER FLAG STATE change the FLAG on partition NUMBER
toggle [NUMBER [FLAG]] toggle the state of FLAG on partition NUMBER
unit UNIT set the default unit to UNIT
version display the version number and copyright information of GNU Parted
(parted) quit
```


注意：如果不指定 block-device，会默认使用第一块磁盘，通常为 /dev/sda，可以通过命令的输出信息确认。

#### 3.3.2.使用 parted 查看分区

可以使用子命令 print 查看分区。

##### 3.3.2.1.使用 parted 交互界面查看分区

流程如下：

进入交互式界面。

```
$ parted block-device
```


使用子命令 print 显示当前磁盘分区信息或者所有磁盘分区信息。

```
(parted) print [devices|free|list,all]
```


参数为可选项，不加参数显示当前设备的分区信息。各参数含义如下：

`devices`

：显示所有激活的磁盘。

`free`

：查看当前磁盘的剩余容量。

`list,all`

：查看所有磁盘的分区信息。

示例如下：

下面的示例打印块设备 /dev/sda 的分区信息：

```
[root@localhost ~]# parted /dev/sda
GNU Parted 3.5
Using /dev/sda
Welcome to GNU Parted! Type 'help' to view a list of commands.
(parted) print
Model: ATA QEMU HARDDISK (scsi)
Disk /dev/sda: 64.4GB
Sector size (logical/physical): 512B/512B
Partition Table: gpt
Disk Flags: pmbr_boot
Number Start End Size File system Name Flags
1 1049kB 2097kB 1049kB bios_grub
2 2097kB 1076MB 1074MB ext4
3 1076MB 64.4GB 63.3GB lvm
```


- print 子命令列出的信息含义

`Model: ATA QEMU HARDDISK (scsi)`

：磁盘类型、制造商、型号和接口。

`Disk /dev/sda: 64.4GB`

：磁盘对应的块设备文件和容量。

`Sector size (logical/physical): 512B/512B`

：扇区大小。

`Partition Table: gpt`

：分区表类型。

`Disk Flags: pmbr_boot`

：磁盘标记，仅出现在 GPT 分区表的磁盘上，表示磁盘上存在特殊属性。示例中的 pmbr_boot 表示磁盘上存在保护性 MBR（PMBR），支持 BIOS 引导方式 。

`Number`

：分区编号。

`Start/End`

：分区起始和结束位置。

`Size`

：分区容量。

`File system`

：分区上文件系统类型。

`Name`

：分区名称，仅出现在 GPT 分区表的磁盘上，可重复。

`Flags`

：分区标记，示例中的 bios_grub 表示 BIOS boot 分区，BIOS 引导下，系统盘为 GPT 分区表时，必须存 BIOS boot 分区。

`Type`

：分区类型，仅出现 MSDOS 分区表的磁盘上，取值为 primary/extended/logical，分别对应主分区、扩展分区和逻辑分区。

##### 3.3.2.2.使用 parted 命令行查看分区

命令如下：

```
# parted block-device print
```


示例如下：

下面的示例打印块设备 /dev/sda 的分区信息：

```
[root@localhost ~]# parted /dev/sda print
Model: ATA QEMU HARDDISK (scsi)
Disk /dev/sda: 64.4GB
Sector size (logical/physical): 512B/512B
Partition Table: gpt
Disk Flags: pmbr_boot
Number Start End Size File system Name Flags
1 1049kB 2097kB 1049kB bios_grub
2 2097kB 1076MB 1074MB ext4
3 1076MB 64.4GB 63.3GB lvm
```


##### 3.3.2.3.更改显示单位

print 显示的位置和容量，默认单位为 compat，输入为 MB，输出为人类易读的形式，如 kB，MB，GB 等。这些数据不够精确，且以10进制为单位。当需要更精确的容量数据时，可以使用子命令 unit 修改显示单位。

```
(parted) unit UNIT
```


UNIT 为单位，支持的单位包括 s, B, kB, MB, GB, TB, compact, cyl, chs, %, kiB, MiB, GiB, TiB。

`s`

表示扇区。

`kB, MB, GB, TB`

基于十进制，后一个单位是前一个单位的 1000 倍。

`compat`

输入默认单位为 MB，输出单位则为人类易读的形式。

`cyl`

柱面。

`chs`

这是一个三元组 (cylinders, heads, sectors) 表示的位置，分别对应柱面，磁头，扇区。1 个柱面包含 255 个磁头，1 个磁头包含 2 个扇区。sectors 取值范围为 0 和 1，heads 的取值范围为 0～254。

```
当单位设置为 chs 时，磁盘容量显示的最后一个扇区的三元组(cylinders, heads, sectors) 位置，sectors 通常为 1，磁盘总扇区数量为 (cylinders * 255 * 2 + heads * 2 + sectors + 1) 。
```


`%`

百分比。

`kiB, MiB, GiB, TiB`

基于二进制，后一个单位是前一个单位的 1024 倍。

#### 3.3.3.使用 parted 创建分区表

可以使用子命令 mklabel 或 mktable 创建分区表。

##### 3.3.3.1.使用 parted 交互界面创建分区表

流程如下：

进入交互式界面。

```
$ parted block-device
```


创建分区表。如果磁盘上已经存在分区表，会打印告警信息，并需要人工确认是否继续。

```
(parted) mklabel LABEL-TYPE
```


确认分区表是否创建成功。

```
(parted) print
```


示例如下：

下面的示例在块设备 /dev/sdb 上创建 gpt 分区表。

```
[root@localhost ~]# parted /dev/sdb
GNU Parted 3.5
Using /dev/sdb
Welcome to GNU Parted! Type 'help' to view a list of commands.
(parted) mklabel gpt
(parted) quit
Information: You may need to update /etc/fstab.
```


##### 3.3.3.2.使用 parted 命令行创建分区表

命令如下：

```
# parted block-device mklabel LABEL-TYPE
```


示例如下：

下面的示例在块设备 /dev/sdb 上创建 gpt 分区表。

```
[root@localhost ~]# parted /dev/sdb mklabel gpt 2Information: You may need to update /etc/fstab.
```


#### 3.3.4.使用 parted 创建分区

可以使用子命令 mkpart 创建分区。

##### 3.3.4.1.使用 parted 交互界面创建分区

流程如下：

进入交互式界面。

```
$ parted block-device
```


根据实际需求，修改显示单位。

```
(parted) unit UNIT
```


查看剩余空间信息是否满足需求，不满足则需要调整分区。

```
(parted) print free
```


创建分区。

```
(parted) mkpart PART-TYPE [FS-TYPE] START END
```


`PART-TYPE`

：当分区表为 MSDOS 时，可用值为 primary/extend/logical，分别对应主分区，扩展分区和逻辑分区，当扩展分区已存在时，才可以设置逻辑分区。当分区表为 GPT 时，该选项被设置为分区名称，可以为任意字符串。

`FS-TYPE`

：可选项，设置分区的文件系统，仅设置分区文件系统字段元数据的值，不会实际创建文件系统。

`START/END`

：分区起始和结束位置，支持的单位包括 s, B, kB, MB, GB, TB, compact, cyl, chs, %, kiB, MiB, GiB, TiB，不指定单位时使用当前 UNIT 下的默认单位。

分区创建完成后执行命令 partprobe，有些环境创建分区后，操作系统可能没有及时更新，内存中保留着旧的分区信息，使用 partprobe 命令通知操作系统重新扫描磁盘分区表，载入新的分区信息。

```
$ partprobe block-device
```


示例如下：

下面的示例在 /dev/sdb 上创建名为 test-part 的分区，分区起始位置为 1MiB，结束位置为 1GiB。

```
[root@localhost home]# parted /dev/sdb
GNU Parted 3.5
Using /dev/sdb
Welcome to GNU Parted! Type 'help' to view a list of commands.
(parted) unit kiB
(parted) print free
Model: ATA QEMU HARDDISK (scsi)
Disk /dev/sdb: 31457280kiB 9Sector size (logical/physical): 512B/512B
Partition Table: gpt
Disk Flags:
Number Start End Size File system Name Flags
17.0kiB 31457263kiB 31457247kiB Free Space
(parted) mkpart test-part 1MiB 1GiB
(parted) print free
Model: ATA QEMU HARDDISK (scsi)
Disk /dev/sdb: 31457280kiB
Sector size (logical/physical): 512B/512B
Partition Table: gpt
Disk Flags:
Number Start End Size File system Name Flags
17.0kiB 1024kiB 1007kiB Free Space
1 1024kiB 1048576kiB 1047552kiB test-part
1048576kiB 31457263kiB 30408688kiB Free Space
(parted) quit
[root@localhost ~]# partprobe /dev/sdb
```


##### 3.3.4.2.使用 parted 命令行创建分区

命令如下：

```
$ parted block-device mkpart PART-TYPE [FS-TYPE] START END
```


示例如下：

```
[root@localhost home]# parted /dev/sdb unit MiB print free
Model: ATA QEMU HARDDISK (scsi)
Disk /dev/sdb: 30720MiB
Sector size (logical/physical): 512B/512B
Partition Table: gpt
Disk Flags:
Number Start End Size File system Name Flags
0.02MiB 1.00MiB 0.98MiB Free Space
1 1.00MiB 1024MiB 1023MiB test-part
1024MiB 30720MiB 29696MiB Free Space
[root@localhost home]# parted /dev/sdb mkpart test-part2 1024MiB 2048MiB
Information: You may need to update /etc/fstab.
[root@localhost home]# partprobe /dev/sdb
[root@localhost home]# parted /dev/sdb unit MiB print free
Model: ATA QEMU HARDDISK (scsi)
Disk /dev/sdb: 30720MiB
Sector size (logical/physical): 512B/512B
Partition Table: gpt
Disk Flags:
Number Start End Size File system Name Flags
0.02MiB 1.00MiB 0.98MiB Free Space
1 1.00MiB 1024MiB 1023MiB test-part
2 1024MiB 2048MiB 1024MiB test-part2
2048MiB 30720MiB 28672MiB Free Space
```


#### 3.3.5.使用 parted 调整分区

##### 3.3.5.1.使用 parted 交互界面调整分区

流程如下：

进入交互式界面。

```
$ parted block-device
```


根据实际需求，修改显示单位。

```
(parted) unit UNIT
```


查看分区信息。

```
(parted) print free
```


调整分区大小。

```
(parted) resizepart NUMBER END
```


`NUMBER`

：待调整分区的编号。

`END`

：调整后分区的结束位置，END 不能小于分区的起始大小。

重新扫描分区表。

```
$ partprobe block-device
```


示例如下：

```
[root@localhost home]# parted /dev/sdb
GNU Parted 3.5
Using /dev/sdb
Welcome to GNU Parted! Type 'help' to view a list of commands.
(parted) unit MiB
(parted) print free
Model: ATA QEMU HARDDISK (scsi)
Disk /dev/sdb: 30720MiB
Sector size (logical/physical): 512B/512B
Partition Table: gpt
Disk Flags:
Number Start End Size File system Name Flags
0.02MiB 1.00MiB 0.98MiB Free Space
1 1.00MiB 1024MiB 1023MiB test-part
2 1024MiB 2048MiB 1024MiB test-part2
2048MiB 30720MiB 28672MiB Free Space
(parted) resizepart 2 4096MiB
(parted) print free
Model: ATA QEMU HARDDISK (scsi)
Disk /dev/sdb: 30720MiB
Sector size (logical/physical): 512B/512B
Partition Table: gpt
Disk Flags:
Number Start End Size File system Name Flags
0.02MiB 1.00MiB 0.98MiB Free Space
1 1.00MiB 1024MiB 1023MiB test-part
2 1024MiB 4096MiB 3072MiB test-part2
4096MiB 30720MiB 26624MiB Free Space
(parted) quit
[root@localhost ~]# partprobe /dev/sdb
```


##### 3.3.5.2.使用 parted 命令行调整分区

命令如下：

```
$ parted block-device resizepart NUMBER END
```


示例如下：

```
[root@localhost home]# parted /dev/sdb unit MiB print free
Model: ATA QEMU HARDDISK (scsi)
Disk /dev/sdb: 30720MiB
Sector size (logical/physical): 512B/512B
Partition Table: gpt
Disk Flags:
Number Start End Size File system Name Flags
0.02MiB 1.00MiB 0.98MiB Free Space
1 1.00MiB 1024MiB 1023MiB test-part
2 1024MiB 2048MiB 1024MiB test-part2
2048MiB 30720MiB 28672MiB Free Space
[root@localhost home]# parted resizepart 2 4096MiB
[root@localhost home]# parted /dev/sdb resizepart 2 4096MiB
Information: You may need to update /etc/fstab.
[root@localhost home]# partprobe /dev/sdb
[root@localhost home]# parted /dev/sdb unit MiB print free
Model: ATA QEMU HARDDISK (scsi)
Disk /dev/sdb: 30720MiB
Sector size (logical/physical): 512B/512B
Partition Table: gpt
Disk Flags:
Number Start End Size File system Name Flags
0.02MiB 1.00MiB 0.98MiB Free Space
1 1.00MiB 1024MiB 1023MiB test-part
2 1024MiB 4096MiB 3072MiB test-part2
4096MiB 30720MiB 26624MiB Free Space
```


注意：缩小分区可能会导致数据丢失甚至文件系统损坏。

#### 3.3.6.使用 parted 删除分区

##### 3.3.6.1.使用 parted 交互界面删除分区

流程如下：

进入交互式界面。

```
$ parted block-device
```


查看分区信息。

```
(parted) print
```


删除分区。

```
(parted) rm NUMBER
```


重新扫描分区表。

```
$ partprobe block-device
```


注意：如果删除的分区存在文件系统，且已经写入到 /etc/fstab 文件内，需要从 /etc/fstab 中移除相关配置，否则，可能会导致操作系统启动失败。

示例如下：

```
[root@localhost home]# parted /dev/sdb
GNU Parted 3.5
Using /dev/sdb
Welcome to GNU Parted! Type 'help' to view a list of commands.
(parted) print
Model: ATA QEMU HARDDISK (scsi)
Disk /dev/sdb: 32.2GB
Sector size (logical/physical): 512B/512B
Partition Table: gpt
Disk Flags:
Number Start End Size File system Name Flags
1 1049kB 1074MB 1073MB ext4 test-part
2 1074MB 2147MB 1074MB ext4 test-part2
(parted) rm 2
(parted) print
Model: ATA QEMU HARDDISK (scsi)
Disk /dev/sdb: 32.2GB
Sector size (logical/physical): 512B/512B
Partition Table: gpt
Disk Flags:
Number Start End Size File system Name Flags
1 1049kB 1074MB 1073MB ext4 test-part
(parted) quit
Information: You may need to update /etc/fstab.
[root@localhost home]# partprobe /dev/sdb
```


##### 3.3.6.2.使用 parted 命令行删除分区

命令如下：

```
$ parted block-device rm NUMBER
```


示例如下：

```
[root@localhost home]# parted /dev/sdb print
Model: ATA QEMU HARDDISK (scsi)
Disk /dev/sdb: 32.2GB
Sector size (logical/physical): 512B/512B
Partition Table: gpt
Disk Flags:
Number Start End Size File system Name Flags
1 1049kB 1074MB 1073MB ext4 test-part
2 1074MB 2147MB 1074MB ext4 test-part2
[root@localhost home]# parted /dev/sdb rm 2
Information: You may need to update /etc/fstab.
[root@localhost home]# parted /dev/sdb print
Model: ATA QEMU HARDDISK (scsi)
Disk /dev/sdb: 32.2GB
Sector size (logical/physical): 512B/512B
Partition Table: gpt
Disk Flags:
Number Start End Size File system Name Flags
1 1049kB 1074MB 1073MB ext4 test-part
```


更多命令选项，请参考 man 手册。

### 3.4.使用 fdisk/gdisk 操作磁盘分区

#### 3.4.1.fdisk 概述

fdisk 支持 MSDOS 和 GPT 两种分区表，可以执行查看分区信息、创建分区表、创建分区、修改分区和删除分区等磁盘操作。

fdisk 大部分操作需要在交互界面执行，直接执行 fdisk block-device 可以进入交互式界面，如下：

```
$ fdisk block-device 2Command (m for help):
```


使用 m 查看帮助信息：

```
Command (m for help): m
```


使用 q 退出交互界面：

```
Command (m for help): q
```


#### 3.4.2.使用 fdisk 查看分区

可以使用自命令 p 查看分区。

流程如下：

进入交互界面。

```
$ fdisk block-device
```


查看分区。

```
Command (m for help): p
```


示例如下：

下面的示例查看磁盘 /dev/sda 的分区。

```
[root@localhost home]# fdisk /dev/sda
Welcome to fdisk (util-linux 2.37.4).
Changes will remain in memory only, until you decide to write them.
Be careful before using the write command.
This disk is currently in use - repartitioning is probably a bad idea.
It's recommended to umount all file systems, and swapoff all swap
partitions on this disk.
Command (m for help): print
Disk /dev/sda: 60 GiB, 64424509440 bytes, 125829120 sectors
Disk model: QEMU HARDDISK
Units: sectors of 1 * 512 = 512 bytes
Sector size (logical/physical): 512 bytes / 512 bytes
I/O size (minimum/optimal): 512 bytes / 512 bytes
Disklabel type: gpt
Disk identifier: 3C81803B-8934-47FF-BE0B-37AE73EC68C0
Device Start End Sectors Size Type
/dev/sda1 2048 4095 2048 1M BIOS boot
/dev/sda2 4096 2101247 2097152 1G Linux filesystem
/dev/sda3 2101248 125827071 123725824 59G Linux LVM
```


`Disk /dev/sda`

：磁盘容量，分别以 GiB，bytes，sectors 三种单位显示。

`Disk model`

：磁盘型号。

`Units`

：显示单位。

`Sector size`

：扇区大小。

`Disklabel type`

：分区表类型，fdisk 下 MSDOS 分区表显示为 dos。

`Disk identifier`

：磁盘标识符。

`Device`

：分区块设备文件名。

`Start/End`

：起始和结束扇区。

`Sectors`

：分区总扇区数。

`Size`

：分区大小。

`Type`

：分区类型，对应 parted 的分区标记。

也可以使用 fdisk 命令行查看分区，命令如下：

```
fdisk -l [block-device]
```


不指定 block-device，则显示所有磁盘分区信息。

#### 3.4.3.使用 fdisk 创建分区表

可以使用子命令 g 创建 GPT 分区表或者使用子命令 o 创建 MSDOS 分区表。流程如下：

进入交互界面。

```
$ fdisk block-device
```


创建分区表。

```
Command (m for help): g
```


保存修改并退出交互界面。

```
Command (m for help): w
```


示例如下：

下面的示例在块设备 /dev/sdb 上创建 gpt 分区表。

```
[root@localhost home]# fdisk /dev/sdb
Welcome to fdisk (util-linux 2.37.4).
Changes will remain in memory only, until you decide to write them.
Be careful before using the write command.
Command (m for help): g
Created a new GPT disklabel (GUID: AC247B3E-7137-6B42-8F85-7D570A41D7FE).
The device contains 'dos' signature and it will be removed by a write command. See fdisk(8) man page and --wipe option for more details.
Command (m for help): w
The partition table has been altered.
Calling ioctl() to re-read partition table.
Syncing disks.
```


#### 3.4.4.使用 fdisk 创建分区

可以使用子命令 n 创建分区。流程如下：

进入交互界面。

```
$ fdisk block-device
```


使用子命令 n，然后按照提示创建分区。

```
Command (m for help): n
```


保存修改并退出交互界面。

```
Command (m for help): w
```


重新扫描分区表。

```
$ partprobe block-device
```


示例如下：

- 示例一：在 MSDOS 分区表的磁盘上创建分区

下面的示例在 /dev/sdb 上创建了一个主分区，一个扩展分区和一个逻辑分区。

```
[root@localhost home]# fdisk /dev/sdb
Welcome to fdisk (util-linux 2.37.4).
Changes will remain in memory only, until you decide to write them.
Be careful before using the write command.
Command (m for help): n
Partition type
p primary (0 primary, 0 extended, 4 free)
e extended (container for logical partitions)
Select (default p): p
Partition number (1-4, default 1):
First sector (2048-62914559, default 2048):
Last sector, +/-sectors or +/-size{K,M,G,T,P} (2048-62914559, default 62914559): +1G
Created a new partition 1 of type 'Linux' and of size 1 GiB.
Command (m for help): n
Partition type
p primary (1 primary, 0 extended, 3 free)
e extended (container for logical partitions)
Select (default p): e
Partition number (2-4, default 2):
First sector (2099200-62914559, default 2099200):
Last sector, +/-sectors or +/-size{K,M,G,T,P} (2099200-62914559, default 62914559):
Created a new partition 2 of type 'Extended' and of size
GiB.
Command (m for help): n
All space for primary partitions is in use.
Adding logical partition 5
First sector (2101248-62914559, default 2101248):
Last sector, +/-sectors or +/-size{K,M,G,T,P} (2101248-62914559, default 62914559): +1G
Created a new partition 5 of type 'Linux' and of size 1 GiB.
Command (m for help): w
The partition table has been altered.
Calling ioctl() to re-read partition table.
Syncing disks.
[root@localhost home]# partprobe /dev/sdb
```


- 示例二：在 GPT 分区表的磁盘上创建分区

下面的示例在 /dev/sdb 上创建了一个 1G 大小的分区。

```
[root@localhost home]# fdisk /dev/sdb
Welcome to fdisk (util-linux 2.37.4).
Changes will remain in memory only, until you decide to write them.
Be careful before using the write command.
Command (m for help): n
Partition number (1-128, default 1):
First sector (2048-62914526, default 2048):
Last sector, +/-sectors or +/-size{K,M,G,T,P} (2048-62914526, default 62914526): +1G
Created a new partition 1 of type 'Linux filesystem' and of size 1 GiB.
Command (m for help): w
The partition table has been altered.
Calling ioctl() to re-read partition table.
Syncing disks.
[root@localhost home]# partprobe /dev/sdb
```


#### 3.4.5.使用 fdisk 删除分区

可以使用子命令 d 删除分区。流程如下：

进入交互界面。

```
$ fdisk block-device
```


使用子命令 p，查看分区信息。

```
Command (m for help): p
```


使用子命令 d，然后按照提示删除分区。

```
Command (m for help): d
```


保存修改并退出交互界面。

```
Command (m for help): w
```


重新扫描分区表。

```
$ partprobe block-device
```


注意：如果删除的分区存在文件系统，且已经写入到 /etc/fstab 文件内，需要从 /etc/fstab 中移除相关配置，否则，可能会导致操作系统启动失败。

示例如下：

```
[root@localhost home]# fdisk /dev/sdb
Welcome to fdisk (util-linux 2.37.4).
Changes will remain in memory only, until you decide to write them.
Be careful before using the write command.
Command (m for help): p
Disk /dev/sdb: 30 GiB, 32212254720 bytes, 62914560 sectors
Disk model: QEMU HARDDISK
Units: sectors of 1 * 512 = 512 bytes
Sector size (logical/physical): 512 bytes / 512 bytes
I/O size (minimum/optimal): 512 bytes / 512 bytes
Disklabel type: dos
Disk identifier: 0xe7cfb001
Device Boot Start End Sectors Size Id Type
/dev/sdb1 2048 2099199 2097152 1G 83 Linux
/dev/sdb2 2099200 4196351 2097152 1G 83 Linux
/dev/sdb3 4196352 8390655 4194304 2G 83 Linux
/dev/sdb4 8390656 62914559 54523904 26G 5 Extended
/dev/sdb5 8392704 10489855 2097152 1G 83 Linux
Command (m for help): d
Partition number (1-5, default 5): 2
Partition 2 has been deleted.
Command (m for help): w
The partition table has been altered.
Calling ioctl() to re-read partition table.
Syncing disks.
[root@localhost home]# partprobe /dev/sdb
```


更多命令选项，请参考 man 手册。

#### 3.4.6使用 gdisk 操作磁盘分区

gdisk 为 GPT 版本 fdisk，只支持 GPT分区表磁盘操作，在 MSDOS 分区表磁盘上操作会将分区表转换成 GPT 分区表。

gdisk 功能与操作方式与 fdisk 类似，可参考 fdisk 操作指

### 3.5.parted 和 fdisk 工具比较

- parted 和 fdisk 均支持 msdos 和 GPT 两种分区表。
- parted 提供了了交互模式和单行命令模式两种交互方式，而 fdisk 仅支持交互模式。
- parted 支持的单位较多，可以通过扇区，柱面，磁柱，百分比，尺寸等进行分区，而 fdisk 仅支持扇区和尺寸。
- parted 功能丰富、子命令多、参数多，而 fdisk 相对简洁。

## 4.swap 空间

### 4.1.swap 空间概述

当系统物理内存占满时，操作系统将启用 swap 空间（如果存在的情况下）,内核将内存中不活跃的页面交换到 swap 空间。

swap 空间可以是专门的 swap 分区，也可以是 swap 文件。推荐的系统 swap 空间如下：

| 物理内存（RAM） | 推荐的 swap 空间大小（不需要休眠） | 推荐的 swap 空间大小（需要休眠） |
|---|---|---|
| 小于 2G | RAM 的 2 倍 | RAM 的 3 倍 |
| 2G ~ 8G | 与 RAM 相等 | RAM 的 2 倍 |
| 8G ~ 16G | 至少 4G | RAM 的 1.5 倍 |
| 大于 64G | 至少 4G | 不推荐休眠 |

### 4.2.添加 swap 空间

#### 4.2.1.添加 swap 分区

首先需要使用 parted 或者 fdisk 命令创建一个分区，如 /dev/sdb1：

```
sdb 8:16 0 64G 0 disk
└─sdb1 8:17 0 8G 0 part
```


格式化 swap 空间：

```
$ mkswap /dev/sdb1
```


在 /etc/fstab 中添加挂载条目：

```
/dev/sdb1 swap swap defaults 0 0
```


执行下面的命令生成挂载单元：

```
$ systemd daemon-reload
```


激活 swap：

```
$ swapon -v /dev/sdb1
```


查看 swap 是否生效:

```
$ cat /proc/swaps
Filename Type Size Used Priority
/dev/sdb1 partition 8388604 0 -2
$ free -h
total used free shared buff/cache available
Mem: 7.3Gi 404Mi 6.5Gi 33Mi 444Mi 6.7Gi
Swap: 8.0Gi 0B 8.0Gi
```


从显示结果可以看到 swap 信息，说明已经生效。

也可以使用逻辑卷创建 swap 空间，操作方法相似。

#### 4.2.2.添加 swap 文件

首先创建一个空文件：

```
$ dd if=/dev/zero of=/data/swapfile bs=1M count=8192
```


格式化 swap 空间：

```
mkswap /data/swapfile
```


在 /etc/fstab 中添加挂载条目：

```
/data/swapfile swap swap defaults 0 0
```


执行下面的命令生成挂载单元：

```
systemd daemon-reload
```


激活 swap：

```
swapon -v /data/swapfile
```


查看 swap 是否生效:

```
$ cat /proc/swaps
Filename Type Size Used Priority
/data/swapfile file 8388604 0 -2
$ free -h
total used free shared buff/cache available
Mem: 7.3Gi 432Mi 75Mi 33Mi 6.8Gi 6.7Gi
Swap: 8.0Gi 0B 8.0Gi
```


从显示结果可以看到 swap 信息，说明已经生效。

### 4.3.删除 swap 空间

#### 4.3.1删除 swap 空间说明

可以使用 swapoff 命令关闭 swap 空间。关闭 swap 空间前需要关注系统内存使用情况，swapoff 命令会通过申请内存将 swap 空间中的内存移会物理内存，如果系统内存不足，会导致 oom。当 oom 系统处理策略为杀进程时，swapoff 命令将会被 kill；当 oom 系统处理策略为 panic 时，系统将重启。

#### 4.3.2.删除 swap 分区

关闭 swap:

```
swapoff -v /dev/sdb1
```


删除 sdb1 分区。

```
parted /dev/sdb rm 1
```


删除 /etc/fstab 中对应条目。

重新生成挂载单元：

```
systemctl daemon-reload
```


查看是否生效：

```
$ cat /proc/swaps
Filename Type Size Used Priority
$ free -h
total used free shared buff/cache available
Mem: 7.3Gi 421Mi 92Mi 33Mi 6.8Gi 6.7Gi
Swap: 0B 0B 0B
```


从显示结果可以看到 swap 已经关闭。

#### 4.3.3.删除 swap 文件

关闭 swap:

```
swapoff -v /data/swapfile
```


删除 swap 文件。

```
rm /data/swapfile
```


删除 /etc/fstab 中对应条目。

重新生成挂载单元：

```
systemctl daemon-reload
```


查看是否生效：

```
$ cat /proc/swaps
Filename Type Size Used Priority
$ free -h
total used free shared buff/cache available
Mem: 7.3Gi 421Mi 92Mi 33Mi 6.8Gi 6.7Gi
Swap: 0B 0B 0B
```


从显示结果可以看到 swap 已经关闭。