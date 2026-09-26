source: https://docs.opencloudos.org/en/OCS/Install_Guide/ocs-initramfs/

# 1. initrams介绍

initramfs（initial RAM filesystem）是一个临时的根文件系统，initramfs的主要目的是开机过程或者装机过程中**挂载用户根文件系统**。虽然内核也能够挂载根文件系统，但是用户根文件系统可能会在任意类型设备和任意文件系统上，内核如果包含所有类型设备和文件系统的驱动会变得很臃肿，难以维护，因此将相关的设备驱动放入initramfs中。

## 1.1 initramfs的工作流程

以下是 `initramfs`

如何找到并挂载根文件系统的过程

# 2 initramfs的查看

## 2.1 安装dracut

```
dnf install dracut -y
```


## 2.2 解压查看当前系统上的initramfs

```
mkdir initramfs_content&&cd initramfs_content
/usr/lib/dracut/skipcpio /boot/initramfs-$(uname -r).img | zcat | cpio -id
```


可以看到其目录结构为：

```
>ls
bin dev etc init lib lib64 proc root run sbin shutdown sys sysroot tmp usr var
```


## 2.3 使用lsinitrd查看initramfs

```
lsinitrd /boot/initramfs-$(uname -r).img
```


# 3 为当前系统重新制作initramfs

当操作系统出现如下情况时，我们需要重新为其制作initramfs

-
**内核更新**: 当您更新系统的 Linux 内核版本时，需要创建一个与新内核版本匹配的 initramfs 映像。

-
**添加/删除硬件设备驱动**: 如果您需要在 initramfs 中添加新的设备驱动，或者从中删除已有的设备驱动时，需要重新制作 initramfs。这确保在引导过程中，新添加的驱动可以被正确加载，从而支持系统中新增的硬件。

-
**更改文件系统**: 如果您更改了根文件系统的类型（例如，从 ext4 切换为 xfs），需要重新制作 initramfs，以确保引导过程中使用正确的文件系统驱动。


若是设备驱动和文件系统的更改，在重新制作initramfs前，需修改dracut.conf

## 3.1 配置dracut.conf

`dracut.conf`

是一个用于配置和定制 `dracut`

的设置的配置文件。它允许您修改 initramfs 映像的各种属性，包括要包含的驱动程序、文件系统支持、压缩格式等。 `dracut`

会在构建initramfs（初始化 RAM 文件系统）映像时读取该文件中的设置。

`dracut.conf`

涉及 `/etc/dracut.conf; /etc/dracut.conf.d/*.conf;/usr/lib/dracut/dracut.conf.d/*.conf`

其在 dracut 的初始化阶段加载。命令行参数将覆盖此处设置的任何值。
**注意**：

-
- 任何
`/etc/dracut.conf.d/*.conf`

文件都可以覆盖/`/etc/dracut.conf`

中的值 。配置文件按字母数字顺序读取。

- 任何
-
`/etc/dracut.conf`

和`/etc/dracut.conf.d/*.conf`

的设置优先级最高，将覆盖`/usr/lib/dracut/dracut.conf.d/*.conf`

中的相应设置


使用文本编辑器打开 `/etc/dracut.conf`


添加内容如下

```
# 添加 Intel Pro/1000 网络适配器 (e1000e) 和 AHCI 驱动
add_drivers+=" e1000e "
# 系统使用 ext4 文件系统
filesystems+=" ext4 "
```


## 3.2重新制作initramfs

```
dracut -f --kver $(uname -r)
```


查看重新制作的initramfs是否包含我们所需的驱动

```
> lsinitrd /boot/initramfs-$(uname -r).img | grep e1000e
drwxr-xr-x 2 root root 0 Apr 28 17:22 usr/lib/modules/6.1.26-2303.1.0.ocs23.x86_64/kernel/drivers/net/ethernet/intel/e1000e
-rw-r--r-- 1 root root 146356 Apr 28 17:22 usr/lib/modules/6.1.26-2303.1.0.ocs23.x86_64/kernel/drivers/net/ethernet/intel/e1000e/e1000e.ko.xz
```


## 3.3 重启判断是否生效

执行 `reboot`

，重启成功后，使用 `dmesg`

查看与驱动模块相关的日志条目

```
> dmesg | grep e1000
[ 2.339278] e1000: Intel(R) PRO/1000 Network Driver
[ 2.339279] e1000: Copyright (c) 1999-2006 Intel Corporation.
[ 2.714188] e1000 0000:02:01.0 eth0: (PCI:66MHz:32-bit) 00:0c:29:9e:d0:4f
[ 2.714196] e1000 0000:02:01.0 eth0: Intel(R) PRO/1000 Network Connection
[ 2.716442] e1000 0000:02:01.0 ens33: renamed from eth0
[ 5.055971] e1000: ens33 NIC Link is Up 1000 Mbps Full Duplex, Flow Control: None
```