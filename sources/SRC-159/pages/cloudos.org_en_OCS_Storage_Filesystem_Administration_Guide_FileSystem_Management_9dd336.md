source: https://docs.opencloudos.org/en/OCS/Storage_Filesystem_Administration_Guide/FileSystem_Management/

# 文件系统管理

## 1. 文件系统简介

### 1.1 文件系统概述

文件系统是操作系统组织和存储数据的一种方法。文件系统建立了文件、目录以及树形目录结构等抽象概念与存储设备数据块之间的映射，用户只需要记住文件路径，无需关心具体的存储设备及对应的数据块，文件系统负责存储空间的管理。当前，OpenCloudOS 支持的文件系统主要包括 ext4 和 xfs 。

### 1.2 ext4

ext4 是一种的日志文件系统，是 ext3 的升级版本，在 Linux 2.6.28 中作为一个功能完备且稳定的文件系统发布。ex4 文件系统具有向下兼容 ext3、支持最大 1EiB 的文件系统尺寸和最大 16TiB 的文件尺寸（4 KiB 块大小）、允许最多 64000 子目录、日志校验、在线磁盘整理、快速文件系统检查等特性。

### 1.3 xfs

xfs 是一种高性能日志文件系统，xfs 在处理并行 IO 方面极具优势，当跨多个存储设备时，IO 线程、文件系统带宽、文件和文件系统大小都具有极高的可扩展性。

### 1.5 ext4 和 xfs 比较

#### 1.5.1 限制

| 文件系统类型 | 最大文件名长度 | 路径字符限制 | 最大路径长度 | 最大文件尺寸 | 最大文件系统容量 |
|---|---|---|---|---|---|
| ext4 | 255B | 非 NUL 字符 | 无限制 | 16TiB | 1EiB |
| xfs | 255B | 非 NUL 字符 | 无限制 | 8EiB | 8EiB |

#### 1.5.2 元数据

| 文件系统类型 | 文件属主 | POSIX 文件权限 | 文件创建时间 | 文件最后访问时间 | 文件最后修改时间 | 元数据最后变化时间 | 访问控制列表 | 强制访问控制（MAC） | 扩展属性 |
|---|---|---|---|---|---|---|---|---|---|
| ext4 | 支持 | 支持 | 支持 | 支持 | 支持 | 支持 | 支持 | 支持 | 支持 |
| xfs | 支持 | 支持 | 支持 | 支持 | 支持 | 支持 | 支持 | 支持 | 支持 |

#### 1.5.3 其他

| 文件系统类型 | 硬链接 | 软链接 | 块日志 | 元数据日志 | 区分大小写 | 加密 | 扩缩容 | |
|---|---|---|---|---|---|---|---|---|
| ext4 | 支持 | 支持 | 支持 | 支持 | 支持 | 支持 | 支持离线扩缩容和在线扩容 | |
| xfs | 支持 | 支持 | 支持 | 支持 | 支持 | 不支持 | 仅支持在线扩容 |

## 2. 创建文件系统

要使用文件系统需要先创建文件系统，通常称为格式化。

### 2.1 创建 ext4 文件系统

#### 2.1.1 使用 mkfs.ext4 创建 ext4 文件系统

可以使用 mkfs、mkfs.ext4 和 mke2fs 命令创建 ext4 文件系统。mkfs 是前端入口，最终会根据 -t 选项指定的文件系统执行具体命令 mkfs.fstype。如：创建 ext4 文件系统最终使用的是命令 mkfs.ext4。mkfs.ext4 对应的二进制文件 实际是 /usr/sbin/mke2fs 的硬链接，执行 mkfs.ext4 命令，实际执行的是 mke2fs 命令。 mkfs 命令如下：

```
mkfs -t ext4 block-device
```


mkfs.ext4 命令如下：

```
mkfs.ext4 block-device
```


mke2fs 命令如下：

```
mke2fs -t ext4 block-device
```


下面的示例在块设备 /dev/sdb1 上创建 ext4 文件系统：

```
$ mkfs.ext4 /dev/sdb1
```


更多详细选项请参考 man mke2fs。

#### 2.1.2 文件系统创建时的默认参数

mkfs.ext4 通过读取 /etc/mke2fs.conf 对初始文件系统进行默认配置，OpenCloudOS 使用的默认配置如下：

```
[defaults]
base_features = sparse_super,large_file,filetype,resize_inode,dir_index,ext_attr
default_mntopts = acl,user_xattr
enable_periodic_fsck = 0
blocksize = 4096
inode_size = 256
inode_ratio = 16384
[fs_types]
ext3 = {
features = has_journal
}
ext4 = {
features = has_journal,extent,huge_file,flex_bg,metadata_csum,64bit,dir_nlink,extra_isize
}
small = {
blocksize = 1024
inode_ratio = 4096
}
floppy = {
blocksize = 1024
inode_ratio = 8192
}
big = {
inode_ratio = 32768
}
huge = {
inode_ratio = 65536
}
news = {
inode_ratio = 4096
}
largefile = {
inode_ratio = 1048576
blocksize = -1
}
largefile4 = {
inode_ratio = 4194304
blocksize = -1
}
hurd = {
blocksize = 4096
inode_size = 128
warn_y2038_dates = 0
}
```


配置文件使用了多个节，每个节下面列出了多个标签，每个标签还可以通过大括号定义子标签。下面对默认配置中的节和标签进行说明：

`[defaults]`

主要指定通用的默认参数，优先级低于 fs_type 节或者命令行参数执行的相同配置。

`[fs_type]`

主要指定特定文件系统或者特定使用场景下的默认参数，可以通过 mke2fs 的 -T 选项指定。

另外，还支持 options 和 devices 节，具体可以查看 man 手册。

`base_features`

指定文件系统创建时默认启用的基本功能。OpenCloudOS 启用了 sparse_super、large_file、filetype、resize_inode、dir_index、ext_attr 特性。如果存在多个 base_features 配置项时，fs_type 节中最后一个生效。

`default_mntopts`

指定文件系统挂载时，默认使能的挂载配置。OpenCloudOS 启用了 acl 和 user_xattr 特性。

`enable_periodic_fsck`

指定系统启动时，是否强制执行文件系统周期性检查。OpenCloudOS 默认设置为 true，则每 180 天或者随机次数的挂载后系统启动时强制执行文件系统检查。

`blocksize`

指定文件系统默认块大小。OpenCloudOS 默认是 4096 字节。

`inode_size`

指定文件系统 inode 的大小。OpenCloudOS 默认是 256 字节。

`inode_ratio`

指定 inode 的比例，可以理解为创建文件系统使用的分区大小和 inode 数量的比例（实际上不是简单的比例关系，分区容量计算公式会有区别）。OpenCloudOS 默认是 16384。

`features`

指定禁用或者启用文件系统的一些额外功能。可以通过 `^featurename`

禁用功能，不加 `^`

则启动功能。

`ext3`

指定创建 ext3 文件系统时的一些参数，建议使用 ext4 文件系统。

`ext4`

指定创建 ext4 文件系统时的一些参数。OpenCloudOS 指定了 features 标签，启用了 has_journal、extent,huge_file、flex_bg、metadata_csum、64bit、dir_nlink 和 extra_isize。

`small`

针对小型文件系统使用场景的预设配置。

`floppy`

针对软盘使用场景的预设配置。

`big`

针对大型文件系统使用场景的预设配置。

`huge`

针对更大型文件系统使用场景的预设配置。

`news`

针对存储新闻数据使用场景的预设配置。

`largefile`

针对大文件使用场景的预设配置。

`largefile4`

针对更大文件使用场景的预设配置。

`hurd`

针对 GNU Hurd 操作系统的配置。
更多详细配置请参考 man mke2fs.conf。

#### 2.1.3 通过命令行选项指定文件系统创建时的参数

可以通过修改配置文件 /etc/mke2fs.conf 设置文件系统创建时的参数，另外也可以通过 mkfs.ext4 或 mke2fs 命令行选项设置默认参数。mke2fs 常用选项说明如下：
`-b`

指定块大小。
`-t`

指定文件系统类型，mkfs.ext4 命令无需指定，mke2fs 命令默认创建 ext2 文件系统。
`-i`

指定 inode_ratio。
`-I`

指定 inode 大小。
`-O`

指定文件系统的特性，特性前添加 ^ 禁用特性。
`-T`

指定文件系统使用场景，值为 /etc/mke2fs.conf 配置中 fs_types 列出的参数项。
更多选项请查询 man 手册。
下面的示例在块设备 /dev/sdb2 上创建了 ext4 文件系统，指定 block 大小为 2048 字节，inode 大小为 128 字节，并禁用了 metadata_csum 功能。

```
$ mkfs.ext4 -b 2048 -I 128 -O ^metadata_csum /dev/sdb2
```


### 2.2 创建 xfs 文件系统

可以使用 mkfs、mkfs.xfs 命令创建 ext4 文件系统。 mkfs 命令如下：

```
mkfs -t xfs block-device
```


mkfs.xfs 命令如下：

```
mkfs.xfs block-device
```


mkfs 是前端入口，最终会调用命令 mkfs.xfs。mkfs.xfs 常用选项说明如下：
`-b block_size_options`

指定文件系统块大小，如：`-b size=4096`

。

`-m global_metadata_options`

指定文件系统元数据区配置，如：`-m crc=1`

。

`-d data_section_options`

指定文件系统数据区配置，如：`-d agcount=4`

。

`-i inode_options`

指定 inode 区配置，如：`-i size=512`

。

下面的示例在块设备 /dev/sdb3 上创建 xfs 文件系统，指定 block 大小为 4096 字节，inode 大小为 512 字节，使能了 crc 功能。

```
$ mkfs.xfs -m crc=1 -i size=512 -f /dev/sdb3
```


更多详细选项请参考 man mkfs.xfs。

## 3. 挂载和卸载文件系统

### 3.1 挂载文件系统

#### 3.1.1 手动挂载文件系统

文件系统创建完成后，需要挂载到系统的某个目录下才可以使用。

**通过块设备文件路径挂载文件系统**

可以使用 mount 命令手动挂载文件系统。下面的示例，挂载设备 /dev/sdb1 到 /mnt 目录下：

```
$ mount /dev/sdb1 /mnt/
```


**通过块设备 UUID 挂载文件系统**

也可以通过 UUID 挂载设备。下面的示例挂载 UUID 为 f9ce3b49-da65-4eca-8692-7daf78db5dae 到 /data 目录下：

```
$ mount UUID=f9ce3b49-da65-4eca-8692-7daf78db5dae /data
```


**指定待挂载设备文件系统类型**

通常 mount 可以自动识别块设备上的文件系统类型，如果 mount 命令无法识别设备上的文件系统，可以通过 -t 选项指定文件系统类型，如下：

```
$ mount -t xfs /dev/sdb3 /home/test
```


**指定挂载属性**

可以通过 -o 选项指定挂载属性，下面的示例将文件系统挂载为只读：

```
$ mount -o ro /dev/sdb2 /data
```


更多详细选项请参考 man mount。

#### 3.1.2 自动挂载文件系统

系统启动时 systemd 会根据 /etc/fstab 中配置，自动挂载文件系统。 示例如下：

```
/dev/mapper/os-root / ext4 defaults 1 1
UUID=88d0f4bd-bed0-4307-867e-50d02353fea2 /boot ext4 defaults 1 2
UUID=08C2-8D97 /boot/efi vfat umask=0077,shortname=winnt 0 2
/dev/mapper/os-home /home ext4 defaults 1 2
```


上面的配置文件共列出来四条挂载配置，每行代表一个挂载配置，共五个字段，下面对各个字段进行说明：

第一个字段：描述待挂载的设备，可以使用设备路径，也可以使用 UUID，也可以是特殊文件系统如 proc，远程文件系统 nfs 等 。

第二个字段：描述挂载点路径。对于 swap，该字段指定为 none。

第三个字段：描述文件系统类型。

第四个字段：描述挂载属性。

第五个字段：dump 根据该字段决定哪些文件系统需要 dump。

第六个字段：fsck 根据该字段决定文件系统检查的顺序。

手动执行 mount -a 命令，会自动挂载 /etc/fstab 配置的设备（如果挂载属性中配置了 noauto，则不会自动挂载）。

### 3.2 查看挂载信息

#### 3.2.1 使用 mount 查看挂载信息

可以使用 mount 可以查看系统当前挂载信息，如下：

```
$ mount
proc on /proc type proc (rw,nosuid,nodev,noexec,relatime)
sysfs on /sys type sysfs (rw,nosuid,nodev,noexec,relatime,seclabel)
...
/dev/mapper/os-root on / type ext4 (rw,relatime,seclabel)
...
```


从显示结果中可以看到挂载设备，挂载点，文件系统类型，挂载属性等挂载信息。

#### 3.2.2 使用 lsblk 查看挂载信息

可以使用 lsblk 查看当前系统的挂载信息，如下：

```
$ lsblk
NAME MAJ:MIN RM SIZE RO TYPE MOUNTPOINTS
sda 8:0 0 64G 0 disk
├─sda1 8:1 0 50M 0 part /boot/efi
├─sda2 8:2 0 512M 0 part /boot
└─sda3 8:3 0 63.4G 0 part
├─os-root 253:0 0 30G 0 lvm /
└─os-home 253:1 0 33.4G 0 lvm /home
sdb 8:16 0 64G 0 disk
├─sdb1 8:17 0 8G 0 part
├─sdb2 8:18 0 8G 0 part /data
└─sdb3 8:19 0 64M 0 part /home/test
```


从显示结果可以看到挂载设备，挂载点，文件系统容量等挂载信息。

#### 3.2.3 使用 df 命令查看挂载信息

可以使用 df -h 查看系统挂载信息，如下：

```
$ df -h
Filesystem Size Used Avail Use% Mounted on
devtmpfs 4.0M 0 4.0M 0% /dev
tmpfs 3.7G 0 3.7G 0% /dev/shm
tmpfs 1.5G 9.2M 1.5G 1% /run
/dev/mapper/os-root 30G 5.4G 23G 20% /
tmpfs 3.7G 16K 3.7G 1% /tmp
/dev/sda2 488M 238M 215M 53% /boot
/dev/sda1 50M 5.5M 45M 11% /boot/efi
/dev/mapper/os-home 33G 12M 31G 1% /home
tmpfs 748M 80K 748M 1% /run/user/1000
tmpfs 748M 28K 748M 1% /run/user/0
/dev/sdb2 7.8G 24K 7.4G 1% /data
/dev/sdb3 60M 4.0M 56M 7% /home/test
```


从显示结果中可以看到挂载设备，文件系统总容量，已使用空间大小，剩余可用空间大小，使用率，挂载点等信息。

使用 df -i 可以查看已挂载文件系统 inode 使用情况，如下：

```
$ df -i
Filesystem Inodes IUsed IFree IUse% Mounted on
devtmpfs 1048576 481 1048095 1% /dev
tmpfs 957374 1 957373 1% /dev/shm
tmpfs 819200 898 818302 1% /run
/dev/mapper/os-root 1966080 131563 1834517 7% /
tmpfs 1048576 27 1048549 1% /tmp
/dev/sda2 32768 226 32542 1% /boot
/dev/sda1 0 0 0 - /boot/efi
/dev/mapper/os-home 2195456 495 2194961 1% /home
tmpfs 191474 102 191372 1% /run/user/1000
tmpfs 191474 31 191443 1% /run/user/0
/dev/sdb2 524288 11 524277 1% /data
/dev/sdb3 32768 3 32765 1% /home/test
```


从显示结果中可以看到挂载设备，文件系统总 inode 数量，已使用 inode 数量，空闲 inode 数量，inode 使用率，挂载点等信息。

更多详细选项请参考 man df。

#### 3.2.4 使用 findmnt 查看挂载信息

使用 findmnt 命令显示系统挂载信息，如下：

```
TARGET SOURCE FSTYPE OPTIONS
/ /dev/mapper/os-root
| ext4 rw,relatime,seclabel
|-/proc proc proc rw,nosuid,nodev,noexec,relatime
| `-/proc/sys/fs/binfmt_misc systemd-1 autofs rw,relatime,fd=31,pgrp=1,timeout=0,minproto=5,maxproto=5,direct,
| `-/proc/sys/fs/binfmt_misc binfmt_misc binfmt_mis rw,nosuid,nodev,noexec,relatime
|-/sys sysfs sysfs rw,nosuid,nodev,noexec,relatime,seclabel
| |-/sys/kernel/security securityfs securityfs rw,nosuid,nodev,noexec,relatime
| |-/sys/fs/cgroup cgroup2 cgroup2 rw,nosuid,nodev,noexec,relatime,seclabel,nsdelegate,memory_recur
| |-/sys/fs/pstore pstore pstore rw,nosuid,nodev,noexec,relatime,seclabel
...
|-/boot /dev/sda2 ext4 rw,relatime,seclabel
| `-/boot/efi /dev/sda1 vfat rw,relatime,fmask=0077,dmask=0077,codepage=437,iocharset=ascii,s
|-/home /dev/mapper/os-home
| ext4 rw,relatime,seclabel
| `-/home/test /dev/sdb3 xfs rw,relatime,seclabel,attr2,inode64,logbufs=8,logbsize=32k,noquot
`-/data /dev/sdb2 ext4 rw,relatime,seclabel
```


从显示结果中可以看到挂载点，挂载设备，文件系统类型，挂载属性等挂载信息。每条结果按照目录结构显示，比较直观。

可以通过指定文件系统类型，只显示特定文件系统的挂载信息，如下：

```
$ findmnt -t ext4
TARGET SOURCE FSTYPE OPTIONS
/ /dev/mapper/os-root ext4 rw,relatime,seclabel
├─/boot /dev/sda2 ext4 rw,relatime,seclabel
├─/home /dev/mapper/os-home ext4 rw,relatime,seclabel
└─/data /dev/sdb2 ext4 rw,relatime,seclabel
```


可以通过指定挂载点，显示当前挂载点下的挂载信息，如下：

```
$ findmnt /
TARGET SOURCE FSTYPE OPTIONS
/ /dev/mapper/os-root ext4 rw,relatime,seclabel
```


更多详细选项请参考 man findmnt。

### 3.3 卸载文件系统

#### 3.3.1 使用 umount 卸载文件系统

当文件系统不再使用时，可以通过 umount 命令卸载文件系统，如下：

```
umount /home/test
```


更多详细选项请参考 man umount。

#### 3.3.2 文件系统占用导致无法卸载

如果正在运行的进程占用着挂载点或者其子目录，会导致文件系统无法卸载，如下：

```
$ umount /home/test
umount: /home/test: target is busy.
```


可以使用 fuser 查看该目录占用情况，如下：

```
$ fuser -vm /home/test
USER PID ACCESS COMMAND
/home/test: root kernel mount /home/test
root 5360 ...e. main
```


如果确定进程不再需要，可以添加 -k 选项 kill 占用进程，如下：

```
$ fuser -kvm /home/test
USER PID ACCESS COMMAND
/home/test: root kernel mount /home/test
root 5360 ...e. main
[1]+ Killed /home/test/main
```


占用进程 kill 后，再使用 umount 命令卸载文件系统。

## 4 查看文件系统

### 4.1 使用 tune2fs 查看 ext4 文件系统信息

可以使用 tune2fs 查看 ext4 文件系统信息，示例如下：

```
$ tune2fs -l /dev/sdb2
tune2fs 1.46.5 (30-Dec-2021)
Filesystem volume name: <none>
Last mounted on: <not available>
Filesystem UUID: f9ce3b49-da65-4eca-8692-7daf78db5dae
Filesystem magic number: 0xEF53
Filesystem revision #: 1 (dynamic)
Filesystem features: has_journal ext_attr resize_inode dir_index filetype needs_recovery extent 64bit flex_bg sparse_super large_file huge_file dir_nlink extra_isize metadata_csum
Filesystem flags: unsigned_directory_hash
Default mount options: user_xattr acl
Filesystem state: clean
Errors behavior: Continue
Filesystem OS type: Linux
Inode count: 524288
Block count: 2097152
Reserved block count: 104857
Overhead clusters: 58505
Free blocks: 2038641
Free inodes: 524277
First block: 0
Block size: 4096
Fragment size: 4096
Group descriptor size: 64
Reserved GDT blocks: 1023
Blocks per group: 32768
Fragments per group: 32768
Inodes per group: 8192
Inode blocks per group: 512
Flex block group size: 16
Filesystem created: Mon May 29 14:12:24 2023
Last mount time: Mon May 29 19:23:26 2023
Last write time: Mon May 29 19:23:26 2023
Mount count: 1
Maximum mount count: -1
Last checked: Mon May 29 14:12:24 2023
Check interval: 0 (<none>)
Lifetime writes: 4129 kB
Reserved blocks uid: 0 (user root)
Reserved blocks gid: 0 (group root)
First inode: 11
Inode size: 256
Required extra isize: 32
Desired extra isize: 32
Journal inode: 8
Default directory hash: half_md4
Directory Hash Seed: 1f267a9b-0e32-493e-b2bc-36dfff3493e6
Journal backup: inode blocks
Checksum type: crc32c
Checksum: 0xbaacede8
```


从显示结果，可以看到文件系统启用的特性，Inode 信息，block 信息，组信息等。 更多详细选项请参考 man tune2fs。

### 4.2 使用 dumpe2fs 查看 ext4 文件系统信息

使用 dumpe2fs 可以查看 ext4 文件系统组信息，示例如下：

```
# dumpe2fs /dev/sdb2
dumpe2fs 1.46.5 (30-Dec-2021)
Filesystem volume name: <none>
Last mounted on: <not available>
Filesystem UUID: f9ce3b49-da65-4eca-8692-7daf78db5dae
Filesystem magic number: 0xEF53
Filesystem revision #: 1 (dynamic)
Filesystem features: has_journal ext_attr resize_inode dir_index filetype needs_recovery extent 64bit flex_bg sparse_super large_file huge_file dir_nlink extra_isize metadata_csum
Filesystem flags: unsigned_directory_hash
Default mount options: user_xattr acl
...
Journal start: 1
Journal checksum type: crc32c
Journal checksum: 0xcc4acf7c
Group 0: (Blocks 0-32767) csum 0xc849 [ITABLE_ZEROED]
Primary superblock at 0, Group descriptors at 1-1
Reserved GDT blocks at 2-1024
Block bitmap at 1025 (+1025), csum 0xa213e783
Inode bitmap at 1041 (+1041), csum 0xad0eeccc
Inode table at 1057-1568 (+1057)
23513 free blocks, 8181 free inodes, 2 directories, 8181 unused inodes
Free blocks: 9255-32767
Free inodes: 12-8192
Group 1: (Blocks 32768-65535) csum 0x880b [INODE_UNINIT, BLOCK_UNINIT, ITABLE_ZEROED]
Backup superblock at 32768, Group descriptors at 32769-32769
Reserved GDT blocks at 32770-33792
Block bitmap at 1026 (bg #0 + 1026), csum 0x00000000
Inode bitmap at 1042 (bg #0 + 1042), csum 0x00000000
Inode table at 1569-2080 (bg #0 + 1569)
31743 free blocks, 8192 free inodes, 0 directories, 8192 unused inodes
Free blocks: 33793-65535
Free inodes: 8193-16384
Group 2: (Blocks 65536-98303) csum 0x894a [INODE_UNINIT, BLOCK_UNINIT, ITABLE_ZEROED]
Block bitmap at 1027 (bg #0 + 1027), csum 0x00000000
Inode bitmap at 1043 (bg #0 + 1043), csum 0x00000000
Inode table at 2081-2592 (bg #0 + 2081)
32768 free blocks, 8192 free inodes, 0 directories, 8192 unused inodes
Free blocks: 65536-98303
Free inodes: 16385-24576
Group 3: (Blocks 98304-131071) csum 0xc70e [INODE_UNINIT, BLOCK_UNINIT, ITABLE_ZEROED]
Backup superblock at 98304, Group descriptors at 98305-98305
Reserved GDT blocks at 98306-99328
Block bitmap at 1028 (bg #0 + 1028), csum 0x00000000
Inode bitmap at 1044 (bg #0 + 1044), csum 0x00000000
Inode table at 2593-3104 (bg #0 + 2593)
31743 free blocks, 8192 free inodes, 0 directories, 8192 unused inodes
Free blocks: 99329-131071
Free inodes: 24577-32768
...
```


从显示结果可以看到，前半部分为文件系统概要信息，与 tune2fs 查看的信息相似，后半部分为各个组的元数据信息。 更多详细选项请参考 man dumpe2fs。

### 4.3 使用 xfs_info 查看 xfs 文件系统信息

可以使用 xfs_info 查看 xfs 文件系统信息，示例如下：

```
$ xfs_info /dev/sdb3
meta-data=/dev/sdb3 isize=512 agcount=4, agsize=4096 blks
= sectsz=4096 attr=2, projid32bit=1
= crc=1 finobt=1, sparse=1, rmapbt=0
= reflink=1 bigtime=0 inobtcount=0
data = bsize=4096 blocks=16384, imaxpct=25
= sunit=0 swidth=0 blks
naming =version 2 bsize=4096 ascii-ci=0, ftype=1
log =internal log bsize=4096 blocks=1221, version=2
= sectsz=4096 sunit=1 blks, lazy-count=1
realtime =none extsz=4096 blocks=0, rtextents=0
```


从显示结果可以看到文件系统元数据区信息，数据区信息，log区信息等。 更多详细选项请参考 man xfs_info。

## 5. 备份和恢复文件系统

### 5.1 使用 e2image 备份 ext4 文件系统

备份前，请卸载文件系统，卸载完成后执行如下命令：

```
e2image block-device ext4-metadata.img
```


*block-device* ：待备份文件系统的块设备。

*ext4-metadata.img* ：备份文件名称。

上面的命令未添加任何参数，只会备份元数据，其备份文件格式为 normal，e2image 的恢复功能只支持这种格式。 可以使用 -r 选项保存成 raw 格式，使用 -Q 选项保存成 qcow2 格式，如果需要保存数据，可以添加 -a 选项，如下所示：

```
e2image -r -a block-device ext4-backup.img
```


e2image 保存的 raw 格式文件是稀疏文件，可以压缩以节省空间，命令参考如下：

```
e2image -r block-device - | bzip2 > ext4-backup.img.bz2
```


e2image 备份的 raw 格式文件可以直接使用 mount 命令挂载，如下：

```
mount ext4-backup.img mountpoint
```


挂载后，可以通过挂载点查看文件系统中的文件。还可以通过 tune2fs 和 dumpe2fs 等命令查看备份文件。 更多详细选项请参考 man e2image。

### 5.2 使用 e2image 恢复 ext4 文件系统元数据

可以使用如下命令恢复 ext4 文件系统元数据：

```
e2image -I block-device ext4-metadata.img
```


ext4-metadata.img 为 e2image 命令保存的 normal 格式的元数据备份文件。 注意：e2image 仅对元数据进行恢复，无法恢复数据。

### 5.3 使用 dump 备份 ext4 文件系统

备份前需要先卸载文件系统，卸载完成后执行如下命令：

```
dump -0uf backup-file block-device
```


系统分区信息如下：

```
$ lsblk
NAME MAJ:MIN RM SIZE RO TYPE MOUNTPOINTS
sda 8:0 0 64G 0 disk
├─sda1 8:1 0 50M 0 part /boot/efi
├─sda2 8:2 0 512M 0 part /boot
└─sda3 8:3 0 63.4G 0 part
├─os-root 253:0 0 30G 0 lvm /
└─os-home 253:1 0 33.4G 0 lvm /home
```


下面的示例备份 /dev/sda2，即 boot 分区：

```
dump -0uf /home/sda2.backup /dev/sda2
```


恢复请参考 《使用 restore 恢复 ext4 文件系统》。 更多命令行选项请参考 man dump。

### 5.4 使用 restore 恢复 ext4 文件系统

如果 /dev/sda2 上的文件系统已损坏，下面的示例演示如何通过 dump 的备份文件恢复系统 boot 分区。 首先在 /dev/sda3 上创建 ext4 文件系统：

```
mkfs.ext4 /dev/sda2
```


然后挂载 /dev/sda2 到 /boot 目录：

```
mount /dev/sda2 /boot
```


进入到 boot 目录下执行如下命令：

```
restore -rf /home/sda2.backup
```


执行完成后，boot 分区下的文件恢复完成。 注意：efi 目录在另一个分区 /dev/sda1，这里不会被恢复。 更多命令行选项请参考 man restore。

### 5.5 使用 xfs_copy 备份 xfs 文件系统

备份前需要卸载文件系统，卸载完成后执行如下命令：

```
xfs_copy block-device xfs-backup.img
```


xfs_copy 会备份元数据和实际数据，备份文件可以直接使用 mount 命令挂载，也可以通过 xfs_info 命令查看。 更多详细选项请参考 man xfs_copy。

### 5.6 使用 xfs_metadump 备份 xfs 文件系统元数据

备份前，需要卸载文件系统，卸载完成后执行如下命令：

```
xfs_metadump -a block-device xfs-metadata.img
```


xfs_metadump 只保存文件系统元数据，可用于恢复 xfs 文件系统。 更多详细选项请参考 man xfs_metadump。

### 5.7 使用 xfs_mdrestore 恢复 xfs 文件系统共元数据

可以使用如下命令恢复 xfs 文件系统元数据：

```
xfs_mdrestore -gi xfs-metadata.img block-device
```


注意：xfs_mdrestore 仅恢复元数据，不能恢复数据。 更多详细选项请参考 man xfs_mdrestore。

### 5.8 使用 xfsdump 备份 xfs 文件系统

执行如下命令：

```
xfsdump -l level -L session_label -M media_label -f backup-file path
```


*level* 备份级别，0 标识全部备份。
*session_label* 会话标签，用以表明备份信息，可以为任意小于 255 字符的字符串。
*media_label* 介质标签，用以标识备份介质，可以为任意小于 255 字符的字符串。
*backup-file* 为生成的备份文件，*path* 表示待备份目录。

下面的示例备份 /data 目录（/dev/sdb6 挂载点）的内容：

```
xfsdump -l 0 -L "backup_data" -M "backup_sdb6" -f /home/sdb6.backup /dev/sdb6
```


恢复请参考 《使用 xfsrestore 恢复 xfs 文件系统》。 更多命令行选项请参考 man dump。

### 5.9 使用 xfsrestore 恢复 xfs 文件系统

如果 /dev/sdb6 上的文件系统已损坏，下面的示例演示如何通过 dump 的备份文件恢复。 首先在 /dev/sdb6 上创建 xfs 文件系统：

```
mkfs.xfs /dev/sdb6
```


然后挂载 /dev/sdb6 到 /data 目录：

```
mount /dev/sdb6 /data
```


执行如下命令：

```
xfsrestore -f /home/sdb6.backup /data
```


执行完成后，/data 下的文件恢复完成。 更多命令行选项请参考 man xfsrestore。

## 6 调整文件系统

### 6.1 使用 tune2fs 调整 ext4 文件系统属性

可以使用 -e 选项调整文件系统在内核中报错时的行为，使用如下命令查看当前行为：

```
$ tune2fs -l /dev/sdb2 | grep "Errors behavior"
Errors behavior: Continue
```


OpenCloudOS 默认行为为不做处理。如下示例将发生错误时的行为调整为重新挂载文件系统为只读以保护文件系统：

```
$ tune2fs -e remount-ro /dev/sdb2
```


可以使用 -o 选项调整文件系统当前挂载属性，属性前添加 ^ 禁用对应属性，使用如下命令查看当前默认挂载属性：

```
$ tune2fs -l /dev/sdb2 | grep "Default mount options"
Default mount options: user_xattr acl
```


如下示例禁用 acl 属性，启用 debug 属性：

```
$ tune2fs -o ^acl,debug /dev/sdb2
```


可以使用 -O 选项调整文件系统当前的一些特性，特性前添加 ^禁用对应特性，使用如下命令查看当前默认特性：

```
$ tune2fs -l /dev/sdb2 | grep "Filesystem features"
```


如下示例禁用 metadata_csum 特性，启用 mmp 特性：

```
$ tune2fs -O ^metadata,mmp /dev/sdb2
```


更多详细选项请参考 man tune2fs。

### 6.2 使用 resize2fs 调整 ext4 文件系统容量

resize2fs 支持在线扩容（文件系统处于挂载状态）和离线（文件系统处于卸载状态）扩缩容，命令如下：

```
resize2fs block-device size
```


size 小于当前容量时，实现缩容（可能会导致数据丢失），size 大于当前容量时，实现扩容。resize2fs 命令自身不能调整分区大小，所以，size 的大小要小于等于文件系统当前容量加上所在分区剩余容量。文件系统挂载时，只支持扩容。 通常，可以结合 growpart 命令先对分区进行扩容，如下所示： 使用 growpart 命令增大分区大小，如果待扩容分区到下一个分区之间或者最后一个分区之后没有可用容量，则无法扩容。扩容会占满待扩容分区到下一个分区之间或者最后一个分区之后所有可用容量。下面的示例扩容分区 /dev/sdb 磁盘上的第 8 个分区，扩容前分区 1G，文件系统大小为 1G：

```
$ growpart /dev/sdb 8
```


扩容后，分区大小为 46G，下面的命令使用 resize2fs 调整文件系统大小为 8G：

```
$ resize2fs /dev/sdb8 8G
```


另外，也可以结合 lvmextend/lvreduce 实现对逻辑卷上文件系统的扩容和缩容。 更多详细选项请参考 man resize2fs。

### 6.3 使用 xfs_admin 调整 xfs 文件系统参数

可以使用 xfs_admin 命令调整 xfs 文件系统参数。下面的命令使能 xfs 文件系统的 bigtime 特性：

```
xfs_admin -O bigtime=1 block-device
```


注意：该特性支持升级，不支持降级，即使能后将无法禁用。 更多详细选项请参考 man xfs_admin。

### 6.4 使用 xfs_growfs 调整 xfs 文件系统容量

xfs 仅支持在线（文件系统处于挂载状态）扩容，不支持缩容，命令如下：

```
xfs_growfs -d block-device
```


该命令会占满所有剩余可用空间。如果需要指定大小，可以使用 -D 选项指定：

```
xfs_growfs -D size block-device
```


size 为扩容后 block 数量。xfs_growfs 命令自身不能调整分区大小，扩容后的容量需要小于等于当前容量加上所在分区剩余容量。 更多详细选项请参考 man xfs_growfs。

## 7 修复文件系统

### 7.1 使用 fsck.ext4 修复 ext4 文件系统

可以使用 fsck、fsck.ext4 或 e2fsck 对文件系统执行检查修复。fsck 命令是前端入口，最终会调用 fsck.ext4，可以使用 -t 选项指定文件系统类型，不指定时，fsck 自动识别文件系统类型。fsck.ext4 命令对应的二进制文件是 /usr/sbin/e2fsck 的硬链接，两个命令相同。使用 e2fsck 时，可以通过 -t 指定文件系统类型，不指定时，e2fsck 自动识别文件系统类型。 执行检查或修复前，需要卸载文件系统。 下面的示例尝试自动修复文件系统错误，需要人工介入时，会停止修复并退出：

```
$ fsck.ext4 -p /dev/sdb5
/dev/sdb5: One or more block group descriptor checksums are invalid. FIXED.
/dev/sdb5: Group descriptor 0 checksum is 0x0000, should be 0x471e. FIXED.
/dev/sdb5: Group descriptor 1 checksum is 0x0000, should be 0x6325. FIXED.
/dev/sdb5: Group descriptor 2 checksum is 0x0000, should be 0x0f68. FIXED.
/dev/sdb5: Group descriptor 3 checksum is 0x0000, should be 0x2b53. FIXED.
fsck.ext4: A block group is missing an inode table while reading bad blocks inode
/dev/sdb5: UNEXPECTED INCONSISTENCY; RUN fsck MANUALLY.
(i.e., without -a or -p options)
```


使用 -a 选项，则不进行任何提示，自动完成修复动作，建议使用 -p 选项。 有时自动修复无法完全修复文件系统错误，可以使用手动修复命令，手动修复需要人工确认。 下面的示例执行手动修复，需要人工进行确认：

```
$ fsck.ext4 /dev/sdb5
e2fsck 1.46.5 (30-Dec-2021)
ext2fs_check_desc: Corrupt group descriptor: bad block for block bitmap
fsck.ext4: Group descriptors look bad... trying backup blocks...
/dev/sdb5 contains a file system with errors, check forced.
Resize inode not valid. Recreate<y>?
```


可以添加 -n 选项对所有需要人工确定的情况回复 no 实现对文件系统的检查：

```
$ fsck.ext4 -n /dev/sdb5
e2fsck 1.46.5 (30-Dec-2021)
ext2fs_check_desc: Corrupt group descriptor: bad block for block bitmap
fsck.ext4: Group descriptors look bad... trying backup blocks...
/dev/sdb5 contains a file system with errors, check forced.
Resize inode not valid. Recreate? no
Pass 1: Checking inodes, blocks, and sizes
Inode 7, i_blocks is 1520, should be 1504. Fix? no
Pass 2: Checking directory structure
Pass 3: Checking directory connectivity
Pass 4: Checking reference counts
Pass 5: Checking group summary information
Free blocks count wrong for group #0 (4294967295, counted=30644).
Fix? no
Free blocks count wrong for group #1 (0, counted=32703).
Fix? no
...
Free inodes count wrong for group #0 (0, counted=8181).
Fix? no
Directories count wrong for group #0 (0, counted=2).
Fix? no
...
Padding at end of inode bitmap is not set. Fix? no
Inode bitmap differences: Group 0 inode bitmap does not match checksum.
IGNORED.
Group 1 inode bitmap does not match checksum.
IGNORED.
Group 2 inode bitmap does not match checksum.
IGNORED.
...
/dev/sdb5: ********** WARNING: Filesystem still has errors **********
/dev/sdb5: 226/32768 files (0.0% non-contiguous), 67111/131072 blocks
```


可以添加 -y 选项对需要人工确认的情况回复 yes，实现自动修复：

```
$ fsck.ext4 -y /dev/sdb5
e2fsck 1.46.5 (30-Dec-2021)
ext2fs_check_desc: Corrupt group descriptor: bad block for block bitmap
fsck.ext4: Group descriptors look bad... trying backup blocks...
/dev/sdb5 contains a file system with errors, check forced.
Resize inode not valid. Recreate? yes
Pass 1: Checking inodes, blocks, and sizes
Pass 2: Checking directory structure
Pass 3: Checking directory connectivity
Pass 4: Checking reference counts
Pass 5: Checking group summary information
Free blocks count wrong for group #0 (4294967294, counted=30644).
Fix? yes
Free blocks count wrong for group #1 (0, counted=32703).
Fix? yes
Free blocks count wrong for group #2 (0, counted=32768).
Fix? yes
Free blocks count wrong for group #3 (0, counted=32703).
Fix? yes
Free blocks count wrong (63960, counted=128818).
Fix? yes
Free inodes count wrong for group #0 (0, counted=8181).
Fix? yes
Directories count wrong for group #0 (0, counted=2).
Fix? yes
Free inodes count wrong for group #1 (0, counted=8192).
Fix? yes
Free inodes count wrong for group #2 (0, counted=8192).
Fix? yes
Free inodes count wrong for group #3 (0, counted=8192).
Fix? yes
Free inodes count wrong (32542, counted=32757).
Fix? yes
Padding at end of inode bitmap is not set. Fix? yes
/dev/sdb5: ***** FILE SYSTEM WAS MODIFIED *****
/dev/sdb5: 11/32768 files (0.0% non-contiguous), 2254/131072 blocks
```


注意：文件系统修复成功，也有可能丢失数据。 不是所有的文件系统错误都能通过 fsck.ext4 命令修复，可以根据 fsck.ext4 的返回值，判读具体情况： 0：无错误 1：文件系统错误已修复 2：文件系统错误已修复，系统需要重启 4：文件系统错误未修复 8：操作错误 16：用法或语法错误 32：用户取消了 e2fsck 操作 128：共享库错误 更多详细选项请参考 man e2fsck。

### 7.2 使用 xfs_repair 修复 xfs 文件系统

可以使用 -n 选项，xfs_repair 不进行实际的修复，仅对文件系统进行检查：

```
# xfs_repair -n /dev/sdb5
Phase 1 - find and verify superblock...
Phase 2 - using internal log
- zero log...
- scan filesystem freespace and inode maps...
Metadata CRC error detected at 0xaaaab6b205a0, xfs_agi block 0x10/0x1000
agi has bad CRC for ag 0
bad magic # 0x0 for agi 0
bad version # 0 for agi 0
bad length # 0 for agi 0, should be 32768
bad uuid 00000000-0000-0000-0000-000000000000 for agi 0
would reset bad agi for ag 0
bad uncorrected agheader 0, skipping ag...
sb_icount 384, counted 320
sb_ifree 155, counted 123
sb_fdblocks 52465, counted 52139
root inode chunk not found
Phase 3 - for each AG...
- scan (but don't clear) agi unlinked lists...
- process known inodes and perform inode discovery...
- agno = 0
imap claims in-use inode 131 is free, would correct imap
imap claims in-use inode 132 is free, would correct imap
...
imap claims in-use inode 159 is free, would correct imap
- agno = 1
- agno = 2
- agno = 3
- process newly discovered inodes...
Phase 4 - check for duplicate blocks...
- setting up duplicate extent list...
- check for inodes claiming duplicate blocks...
- agno = 0
- agno = 1
- agno = 2
- agno = 3
No modify flag set, skipping phase 5
Phase 6 - check inode connectivity...
- traversing filesystem ...
- traversal finished ...
- moving disconnected inodes to lost+found ...
Phase 7 - verify link counts...
No modify flag set, skipping filesystem flush and exiting.
```


如下示例执行实际的修复：

```
# xfs_repair /dev/sdb5
Phase 1 - find and verify superblock...
Phase 2 - using internal log
- zero log...
- scan filesystem freespace and inode maps...
Metadata CRC error detected at 0xaaaac43c05a0, xfs_agi block 0x10/0x1000
agi has bad CRC for ag 0
bad magic # 0x0 for agi 0
bad version # 0 for agi 0
bad length # 0 for agi 0, should be 32768
bad uuid 00000000-0000-0000-0000-000000000000 for agi 0
reset bad agi for ag 0
bad levels 0 for inobt root, agno 0
bad agbno 0 for inobt root, agno 0
bad levels 0 for finobt root, agno 0
bad agbno 0 for finobt root, agno 0
agi unlinked bucket 0 is 0 in ag 0 (inode=0)
agi unlinked bucket 1 is 0 in ag 0 (inode=0)
...
agi unlinked bucket 63 is 0 in ag 0 (inode=0)
sb_icount 384, counted 320
sb_ifree 155, counted 123
root inode chunk not found
Phase 3 - for each AG...
- scan and clear agi unlinked lists...
- process known inodes and perform inode discovery...
- agno = 0
correcting imap
correcting imap
...
correcting imap
- agno = 1
- agno = 2
- agno = 3
- process newly discovered inodes...
Phase 4 - check for duplicate blocks...
- setting up duplicate extent list...
- check for inodes claiming duplicate blocks...
- agno = 0
- agno = 2
- agno = 3
- agno = 1
Phase 5 - rebuild AG headers and trees...
- reset superblock...
Phase 6 - check inode connectivity...
- resetting contents of realtime bitmap and summary inodes
- traversing filesystem ...
- traversal finished ...
- moving disconnected inodes to lost+found ...
Phase 7 - verify and correct link counts...
done
```


更多详细选项请参考 man xfs_repair。

## 8. 参考资料

- https://ext4.wiki.kernel.org/index.php/Main_Page
- https://man7.org/linux/man-pages/man5/ext4.5.html
- https://xfs.wiki.kernel.org/