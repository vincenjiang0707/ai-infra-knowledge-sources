source: https://docs.opencloudos.org/en/OCS/Storage_Filesystem_Administration_Guide/RAID_Management/

# RAID 管理

## 1. RAID 简介

### 1.1 RAID 概述

RAID 是独立磁盘冗余阵列（Redundant Array of Independent Disks）的缩写。RAID 设备是由多个存储设备按照特定的方式组合成的一个阵列，以单一设备出现在操作系统中，从而实现性能或冗余目标。 根据实现方式，RAID 可以分为软件 RAID 和硬件 RAID 两种形式：

**软件 RAID**

软件 RAID 设备通过内核 md (Multiple Devices) 设备驱动实现。

**硬件 RAID**

硬件 RAID 设备通过硬件设备（如 RAID 控制卡）实现。

### 1.2 RAID 级别

#### 1.2.1 RAID0

RAID0 称为条带卷，它将多个磁盘并联，组成一个大容量磁盘。写入数据时，数据会并行分散存放在不同的设备上。如果组成 RAID0 的多个设备大小不同，每个设备的大小都被视为与最小设备大小相同。设备的总容量为最小设备大小和组成 RAID 设备数量的乘积。RAID0 的优点是写入性能好，其缺点是没有冗余和容错能力，如果一个磁盘损坏，所有数据都会丢失。 RAID0 示意图如下，设备 dev1 和 dev2 组成 RAID0，写入数据 A 时，A 被分成多个数据块 A1 ~ A6，A1、A3、A5 写入设备 dev1，A2、A4、A6 写入设备 dev2。

```
RAID0
+---------+
｜ ｜
+----+ +----+
| A1 | | A2 |
|----| |----|
| A3 | | A4 |
|----| |----|
| A5 | | A6 |
|----| |----|
| | | |
+----+ +----+
dev1 dev2
```


#### 1.2.2 RAID1

RAID1 称为镜像，组成 RAID1 的存储设备互为镜像，每个设备都保存数据的副本。RAID1 的优点是可靠性高，其中一个存储设备损坏后，不会导致数据丢失。RAID1 有较好的读取性能。其缺点是写入速度有小幅下降。另外，RAID1 没有校验机制，如果设备间存在数据不一致的情况，RAID1 只会从第一个工作的存储设备上提供数据。 RAID1 示意图如下，设备 dev1 和 dev2 组成 RAID1，写入数据 A 时，A 被分成多个数据块 A1 ~ A3，每个数据块都会分别写入设备 dev1 和 dev2。

```
RAID1
+---------+
｜ ｜
+----+ +----+
| A1 | | A1 |
|----| |----|
| A2 | | A2 |
|----| |----|
| A3 | | A3 |
|----| |----|
| | | |
+----+ +----+
dev1 dev2
```


#### 1.2.3 RAID4

RAID4 使用单独的磁盘保存奇偶校验信息块。写入数据时，RAID4 将数据分成多个区块依次写入多个磁盘，最后根据多个磁盘的值计算出奇偶校验值保存在最后一块磁盘。RAID4 最少需要 3 块磁盘，其中一块磁盘损坏时，可以根据其他磁盘重建数据。 RAID4 示意图如下，设备 dev1、dev2 和 dev3 组成 RAID4。dev1 和 dev2 保存数据，dev3 保存校验值。

```
RAID4
+---------+---------+
｜ ｜ ｜
+----+ +----+ +----+
| A1 | | A2 | | Ap |
|----| |----| |----|
| B1 | | B2 | | Bp |
|----| |----| |----|
| C1 | | C2 | | Cp |
|----| |----| |----|
| | | | | |
+----+ +----+ +----+
dev1 dev2 dev3
```


#### 1.2.4 RAID5

RAID5 使用奇偶校验信息块，将数据和奇偶校验信息均匀分布在各个磁盘上。RAID5 最少需要 3 块磁盘，其中一块磁盘损坏时，可以根据其他磁盘重建数据。 RAID5 示意图如下，设备 dev1、dev2 和 dev3 组成 RAID4。数据和校验值分散保存到了三个存储设备上。

```
RAID5
+---------+---------+
｜ ｜ ｜
+----+ +----+ +----+
| A1 | | A2 | | Ap |
|----| |----| |----|
| B1 | | Bp | | B2 |
|----| |----| |----|
| Cp | | C1 | | C2 |
|----| |----| |----|
| | | | | |
+----+ +----+ +----+
dev1 dev2 dev3
```


#### 1.2.5 RAID6

RAID6 使用使用两个奇偶校验信息块。但将数据和奇偶校验信息分散存储在各个磁盘上。RAID6 最少需要 4 块磁盘，其中两块磁盘损坏时，可以根据其他磁盘重建数据。 RIAID6 示意图如下：

```
RAID6
+---------+---------+---------+
｜ ｜ ｜ ｜
+----+ +----+ +----+ +----+
| A1 | | A2 | | Ap | | Aq |
|----| |----| |----| |----|
| B1 | | Bp | | Bq | | B2 |
|----| |----| |----| |----|
| Cp | | Cq | | C1 | | C2 |
|----| |----| |----| |----|
| | | | | | | |
+----+ +----+ +----+ +----+
dev1 dev2 dev3 dev4
```


#### 1.2.6 RAID10

RAID10 是组合 RAID，先组两个 RAID1 镜像卷，然后再组成 RAID0。 RAID10 示意图如下：

```
RAID10
+-------------------+
｜ ｜
+---------+ +---------+
｜ ｜ ｜ ｜
+----+ +----+ +----+ +----+
| A1 | | A1 | | A2 | | A2 |
|----| |----| |----| |----|
| A3 | | A3 | | A4 | | A4 |
|----| |----| |----| |----|
| A5 | | A5 | | A6 | | A6 |
|----| |----| |----| |----|
| | | | | | | |
+----+ +----+ +----+ +----+
dev1 dev2 dev3 dev4
```


#### 1.2.7 不同 RAID 级别的比较

| RAID 级别 | 最小磁盘数 | 可用容量 | 随机读性能 | 随机写性能 | 容错性 | 应用场景 |
|---|---|---|---|---|---|---|
| RAID0 | 2 | n*单盘容量 | 高 | 高 | 无 | 适用于读写性能要求高，但容错性无要求的场景 |
| RAID1 | 2 | 1*单盘容量 | 中 | 较低 | 允许 (n-1) 块磁盘损坏 | 适用于对读写性能要求不高，但容错性要求高的场景 |
| RAID4 | 3 | (n-1)*单盘容量 | 较高 | 较低 | 允许 1 块磁盘损坏 | 适用于对读性能和容错性有一定要求的场景 |
| RAID5 | 3 | (n-1)*单盘容量 | 较高 | 较低 | 允许 1 块磁盘损坏 | 适用于对读性能和容错性有一定要求的场景 |
| RAID6 | 4 | (n-2)*单盘容量 | 较高 | 较高 | 允许 2 块磁盘损坏 | 适用于对读性能和容错性有一定要求的场景 |
| RAID10 | 4 | (n/2)*单盘容量 | 高 | 中 | 互为镜像的磁盘中有一块磁盘正常即可 | 适用于对读写性能和容错性要求高的场景 |

## 2. 软 RAID 管理

### 2.1 创建软 RAID

可以使用 mdadm 命令创建软 RAID。 下面的示例通过 /dev/sdb1 和 /dev/sdb2 组建 RAID1：

```
$ mdadm --create /dev/md0 --level=1 --raid-devices=2 /dev/sdb1 /dev/sdc1
```


*--level* 指定 RAID 级别。
*--raid-devices* 指定组建 RAID 的设备数量。
创建成功后，/dev 下面会出现 md0 设备。lsblk 可以查看到设备信息：

```
sdb 8:16 0 64G 0 disk
└─sdb1 8:17 0 8G 0 part
└─md0 9:0 0 8G 0 raid1
sdc 8:32 0 64G 0 disk
└─sdc1 8:33 0 8G 0 part
└─md0 9:0 0 8G 0 raid1
```


### 2.2 查看软 RAID

#### 2.2.1 查看软 RAID 信息

```
# mdadm --detail /dev/md0
/dev/md0:
Version : 1.2
Creation Time : Wed May 31 20:26:56 2023
Raid Level : raid1
Array Size : 8379392 (7.99 GiB 8.58 GB)
Used Dev Size : 8379392 (7.99 GiB 8.58 GB)
Raid Devices : 2
Total Devices : 2
Persistence : Superblock is persistent
Update Time : Wed May 31 20:29:05 2023
State : clean
Active Devices : 2
Working Devices : 2
Failed Devices : 0
Spare Devices : 0
Consistency Policy : resync
Name : OCS:0 (local to host OCS)
UUID : 9ef0643d:4ea3897d:4ddd4305:de505872
Events : 17
Number Major Minor RaidDevice State
0 8 17 0 active sync /dev/sdb1
1 8 33 1 active sync /dev/sdc1
```


#### 2.2.2 查看软 RAID 中设备信息

```
$ mdadm --examine /dev/sdb1 /dev/sdc1
/dev/sdb1:
Magic : a92b4efc
Version : 1.2
Feature Map : 0x0
Array UUID : 9ef0643d:4ea3897d:4ddd4305:de505872
Name : OCS:0 (local to host OCS)
Creation Time : Wed May 31 20:26:56 2023
Raid Level : raid1
Raid Devices : 2
Avail Dev Size : 16758784 sectors (7.99 GiB 8.58 GB)
Array Size : 8379392 KiB (7.99 GiB 8.58 GB)
Data Offset : 18432 sectors
Super Offset : 8 sectors
Unused Space : before=18352 sectors, after=0 sectors
State : clean
Device UUID : 82cd6042:2195b1a3:af8878c1:27adb01f
Update Time : Wed May 31 20:29:05 2023
Bad Block Log : 512 entries available at offset 16 sectors
Checksum : a83c205d - correct
Events : 17
Device Role : Active device 0
Array State : AA ('A' == active, '.' == missing, 'R' == replacing)
/dev/sdc1:
Magic : a92b4efc
Version : 1.2
Feature Map : 0x0
Array UUID : 9ef0643d:4ea3897d:4ddd4305:de505872
Name : OCS:0 (local to host OCS)
Creation Time : Wed May 31 20:26:56 2023
Raid Level : raid1
Raid Devices : 2
Avail Dev Size : 16758784 sectors (7.99 GiB 8.58 GB)
Array Size : 8379392 KiB (7.99 GiB 8.58 GB)
Data Offset : 18432 sectors
Super Offset : 8 sectors
Unused Space : before=18352 sectors, after=0 sectors
State : clean
Device UUID : 9ef0643d:4ea3897d:4ddd4305:de505872
Name : OCS:0 (local to host OCS)
Creation Time : Wed May 31 20:26:56 2023
Raid Level : raid1
Raid Devices : 2
Avail D : 411e5461:7ae96988:623268d7:371605d1
Update Time : Wed May 31 20:29:05 2023
Bad Block Log : 512 entries available at offset 16 sectors
Checksum : 732bd83a - correct
Events : 17
Device Role : Active device 1
Array State : AA ('A' == active, '.' == missing, 'R' == replacing)
```


### 2.3 在 RAID 设备上创建分区及文件系统

可以在 RAID 设备上创建文件系统。 下面的例子在 /dev/md0 上创建 ext4 文件系统，如下所示：

```
$ mkfs.ext4 /dev/md0
```


也可以在 RAID 设备上创建分区，如下所示：

```
$ parted /dev/md0 mkpart testmd0 1MiB 1024MiB
```


创建完成后，通过 lsblk 查看，可以看到出现一个 /dev/md0p1 设备，为 md0 设备的第一个分区：

```
sdb 8:16 0 64G 0 disk
└─sdb1 8:17 0 8G 0 part
└─md0 9:0 0 8G 0 raid1
└─md0p1 259:1 0 1023M 0 part
sdc 8:32 0 64G 0 disk
└─sdc1 8:33 0 8G 0 part
└─md0 9:0 0 8G 0 raid1
└─md0p1 259:1 0 1023M 0 part
```


可以继续在分区上创建文件系统并挂载。

### 2.4 调整软 RAID 容量

可以使用如下命令调整 RAID 容量：

```
mdadm --grow --size=value md-device
```


*--grow* 表明调整容量。
*--size* 指定调整后的大小，单位为 KiB，小于当前容量实现缩容，大于当前容量实现扩容，容量需要小于组成 RAID 的设备容量。
下面的示例将 /dev/md0 缩容至 4GB（缩容前 8G）：

```
mdadm --grow --size=4194304 /dev/md0
```


### 2.5 转换软 RAID 的级别

软 RAID 支持从一个级别转换成另一个级别，支持的软 RAID 转换如下：

| 源级别 | 目标级别 |
|---|---|
| RAID0 | RAID4, RAID5, RAID10 |
| RAID1 | RAID0, RAID5 |
| RAID4 | RAID0, RAID5 |
| RAID5 | RAID0, RAID1, RAID4, RAID6, RAID10 |
| RAID6 | RAID5 |
| RAID10 | RAID0 |
| 下面的示例将 RAID1 转换成 RAID5： |

```
mdadm --grow /dev/md0 --level=5 --raid-devices=3 --force
```


由于 RAID5 至少需要 3 块磁盘，而转换前的 RAID1 由 2 块磁盘组成，还需要添加一块磁盘，命令如下：

```
mdadm --manage /dev/md0 --add /dev/sdb2
```


执行完成后，可以通过如下命令查看软 RAID 的最新状态：

```
$ mdadm --detail /dev/md0
/dev/md0:
Version : 1.2
Creation Time : Wed May 31 20:26:56 2023
Raid Level : raid5
Array Size : 4194304 (4.00 GiB 4.29 GB)
Used Dev Size : 4194304 (4.00 GiB 4.29 GB)
Raid Devices : 3
Total Devices : 3
Persistence : Superblock is persistent
Update Time : Thu Jun 1 10:16:43 2023
State : clean, reshaping
Active Devices : 3
Working Devices : 3
Failed Devices : 0
Spare Devices : 0
Layout : left-symmetric
Chunk Size : 64K
Consistency Policy : resync
Reshape Status : 42% complete
Delta Devices : 1, (2->3)
Name : OCS:0 (local to host OCS)
UUID : 9ef0643d:4ea3897d:4ddd4305:de505872
Events : 39
Number Major Minor RaidDevice State
0 8 17 0 active sync /dev/sdb1
1 8 33 1 active sync /dev/sdc1
2 8 18 2 active sync /dev/sdb2
```


### 2.6 替换软 RAID 中损坏的磁盘

下面的示例中 /dev/sdb1 和 /dev/sdc1 组成 RAID1：

```
$ mdadm --detail /dev/md0
/dev/md0:
Version : 1.2
Creation Time : Thu Jun 1 11:55:27 2023
Raid Level : raid1
...
Number Major Minor RaidDevice State
0 8 17 0 active sync /dev/sdb1
1 8 33 1 active sync /dev/sdc1
```


假设 sdb1 分区出现问题，我们需要用 sdb2 替换 sdb1，操作流程如下： 首先需要将有问题的分区标记为故障：

```
$ mdadm --manage /dev/md0 --fail /dev/sdb1
```


然后从 RAID 中删除故障分区：

```
$ mdadm --manage /dev/md0 --remove /dev/sdb1
```


向 RAID 中添加新的设备：

```
$ mdadm --manage /dev/md0 --add /dev/sdb2
```


最后，查看 RAID 信息，验证是否添加成功：

```
$ mdadm --detail /dev/md0
/dev/md0:
Version : 1.2
Creation Time : Thu Jun 1 11:55:27 2023
Raid Level : raid1
...
Rebuild Status : 11% complete
Name : OCS:0 (local to host OCS)
UUID : 88e4b53b:05d6162b:b81126ea:bba23288
Events : 29
Number Major Minor RaidDevice State
2 8 18 0 spare rebuilding /dev/sdb2
1 8 33 1 active sync /dev/sdc1
```


可以看到 /dev/sdb2 添加成功，正在重建数据。

### 2.7 删除软 RAID

下面的示例演示如何删除由 /dev/vdb、/dev/vdc、/dev/vdd 和 /dev/vde 组成的 raid6 级别软 RAID 设备 /dev/md0： 查看软 RAID 信息：

```
# mdadm --detail /dev/md0
/dev/md0:
Version : 1.2
Creation Time : Wed Jun 7 12:55:57 2023
Raid Level : raid6
Array Size : 33519616 (31.97 GiB 34.32 GB)
Used Dev Size : 16759808 (15.98 GiB 17.16 GB)
Raid Devices : 4
Total Devices : 4
Persistence : Superblock is persistent
Update Time : Wed Jun 7 12:58:58 2023
State : clean
Active Devices : 4
Working Devices : 4
Failed Devices : 0
Spare Devices : 0
Layout : left-symmetric
Chunk Size : 512K
Consistency Policy : resync
Name : localhost.localdomain:0 (local to host localhost.localdomain)
UUID : fa8f7b1f:4545ff4b:d2d7bfad:9249434a
Events : 17
Number Major Minor RaidDevice State
0 252 16 0 active sync /dev/vdb
1 252 32 1 active sync /dev/vdc
2 252 48 2 active sync /dev/vdd
3 252 64 3 active sync /dev/vde
```


停止软 RAID 设备 /dev/md0：

```
$ mdadm --stop /dev/md0
mdadm: stopped /dev/md0
```


清理磁盘上软 RAID 元数据：

```
$ mdadm --zero-superblock /dev/vdb /dev/vdc /dev/vdd /dev/vde
```


命令执行成功后，软 RAID 设备 /dev/md0 则被删除。