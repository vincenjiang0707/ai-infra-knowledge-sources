source: https://docs.opencloudos.org/en/OC9/install/PXE_install/

# OpenCloudOS 9 PXE 无人值守系统安装教程

**第一章 背景说明**

针对于运维工作中遇到的需要大批量安装OpenCloudOS 9系统的情况，可以通过网络装机的方式实现无人值守安装Linux操作系统，现需要配置一台pxe服务器用于pxe批量安装OpenCloudOS 9操作系统，本文介绍OpenCloudOS 9 PXE安装详细流程。在局域网场景下，PXE服务器需要提供DHCP服务和tftp服务以及HTTP服务，DHCP服务主要是为了给客户机提供IP地址，建立客户端与服务器的网络链接；tftp服务则是提供了安装系统所需要的引导文件；HTTP服务则是提供安装系统的软件包，三者缺一不可。

先分清两台机器：左边是已经装好系统、由你来配置的**服务机**；右边是还没有系统、只要设好网卡启动的**客户端**（可以有很多台）。三类服务都开在服务机上。

客户端开机后依次使用这三类服务：DHCP 分配地址并告知引导文件位置，TFTP 下发引导程序、内核和 initrd，HTTP 提供安装源和 Kickstart。

**第二章 局域网下部署PXE服务器**

在需要部署PXE服务器的机器中做以下操作

### 2.1 **服务端配置**

局域网下请确保下列软件列表中的软件已在PXE服务器中安装就绪

```
dnf install dhcp-server httpd tftp tftp-server
```


#### 2.1.1 配置dhcp

1.获取服务器局域网IP地址

```
ifconfig
```


以本机IP参数为例（192.168.10.230）

2.修改dhcpd.conf

文件位置：/etc/dhcp/dhcpd.conf

文件头部的注释可以保留。`option space pxelinux`

及以下四行按示例添加即可，无需改内容。

**Legacy启动**

```
# DHCP Server Configuration file.
# see /usr/share/doc/dhcp-server/dhcpd.conf.example
# see dhcpd.conf(5) man page
option space pxelinux;
option pxelinux.magic code 208 = string;
option pxelinux.configfile code 209 = text;
option pxelinux.pathprefix code 210 = text;
option pxelinux.reboottime code 211 = unsigned integer 32;
subnet 192.168.10.0 netmask 255.255.255.0 { # 【按本机修改】网段
range 192.168.10.60 192.168.10.69; # 【按本机修改】地址池
option routers 192.168.10.1; # 【按本机修改】网关
option broadcast-address 192.168.10.1; # 【按本机修改】广播地址
next-server 192.168.10.230; # 【按本机修改】PXE 服务器 IP
filename "pxelinux.0"; # Legacy 固定用这个
}
```


**UEFI启动**

```
# DHCP Server Configuration file.
# see /usr/share/doc/dhcp-server/dhcpd.conf.example
# see dhcpd.conf(5) man page
option space pxelinux;
option pxelinux.magic code 208 = string;
option pxelinux.configfile code 209 = text;
option pxelinux.pathprefix code 210 = text;
option pxelinux.reboottime code 211 = unsigned integer 32;
subnet 192.168.10.0 netmask 255.255.255.0 { # 【按本机修改】网段
range 192.168.10.60 192.168.10.69; # 【按本机修改】地址池
option routers 192.168.10.1; # 【按本机修改】网关
option broadcast-address 192.168.10.1; # 【按本机修改】广播地址
next-server 192.168.10.230; # 【按本机修改】PXE 服务器 IP
filename "uefi/grubaa64.efi"; # 【按架构选择】aarch64 用 grubaa64.efi；x86_64 用 BOOTX64.EFI 或 grubx64.efi
}
```


- 重启dhcp服务使配置生效

```
systemctl restart dhcpd.service --重启DHCP服务
systemctl enable dhcpd.service --设置为开机自启动
netstat -anlp | grep dhcpd --查看dhcp服务端口为67
```


#### 2.1.2 配置tftp

确认tftp配置如下（OpenCloudOS 9 使用 systemd 管理 tftp，根目录为 `/var/lib/tftpboot`

）：

```
# /usr/lib/systemd/system/tftp.service
[Unit]
Description=Tftp Server
Requires=tftp.socket
Documentation=man:in.tftpd
[Service]
ExecStart=/usr/sbin/in.tftpd -s /var/lib/tftpboot
StandardInput=socket
[Install]
Also=tftp.socket
# /usr/lib/systemd/system/tftp.socket
[Unit]
Description=Tftp Server Activation Socket
[Socket]
ListenDatagram=0.0.0.0:69
[Install]
WantedBy=sockets.target
```


```
mkdir -p /var/lib/tftpboot
systemctl enable --now tftp.socket
```


#### 2.1.3 配置http

1.配置http服务开机启动

```
systemctl restart httpd
systemctl enable httpd
```


2.关闭防火墙

```
systemctl stop firewalld
```


#### 2.1.4 ISO母盘部署

1.将客户端需要安装的ISO镜像挂载到指定目录（以OpenCloudOS-9.4-aarch64-everything为例）

```
mkdir -p /var/www/html/pxeboot
mount -o loop /path/to/OpenCloudOS-9.4-aarch64-everything.iso /var/www/html/pxeboot
# 【按本机修改】上一行改成你的 ISO 实际路径和文件名
```


2.制作启动文件

**Legacy启动**

```
cp -r /usr/share/syslinux/* /var/lib/tftpboot/
mkdir -p /var/lib/tftpboot/pxelinux.cfg
cp /var/www/html/pxeboot/isolinux/isolinux.cfg /var/lib/tftpboot/pxelinux.cfg/default
cp /var/www/html/pxeboot/isolinux/* /var/lib/tftpboot/
```


**UEFI启动**

```
mkdir -p /var/lib/tftpboot/uefi
cp /var/www/html/pxeboot/EFI/BOOT/*.efi /var/lib/tftpboot/uefi
cp /var/www/html/pxeboot/images/pxeboot/vmlinuz /var/lib/tftpboot/uefi
cp /var/www/html/pxeboot/images/install.img /var/lib/tftpboot/uefi
cp /var/www/html/pxeboot/images/pxeboot/initrd.img /var/lib/tftpboot/uefi
```


3.制作启动文件

**Legacy启动**

文件位置：/var/lib/tftpboot/pxelinux.cfg/default（若文件不存在，新建该文件）

删除default文件中多余的参数，保留如下内容。软件源用 `inst.repo`

在启动参数里指定，无需在 Anaconda 图形界面手填。只有标了 `【按本机修改】`

的行需要改 IP。

```
default vesamenu.c32
timeout 600
display boot.msg
label linux
menu label ^Install OpenCloudOS 9
menu default
kernel vmlinuz
append initrd=initrd.img inst.stage2=http://192.168.10.230/pxeboot inst.repo=http://192.168.10.230/pxeboot
# 【按本机修改】上一行两个 URL 里的 IP 改成 PXE 服务器地址
```


**UEFI启动**

文件位置：/var/lib/tftpboot/uefi/grub.cfg（若文件不存在，新建该文件）

前面的 `insmod`

等行不用改。aarch64 使用 `linux`

/ `initrd`

；x86_64 将这两行改为 `linuxefi`

/ `initrdefi`

。

```
set default="0"
function load_video {
insmod efi_gop
insmod efi_uga
insmod video_bochs
insmod video_cirrus
insmod all_video
}
load_video
set gfxpayload=keep
insmod tftp
insmod gzio
insmod part_gpt
insmod ext2
set timeout=60
menuentry 'Install OpenCloudOS 9' --class fedora --class gnu-linux --class gnu --class os {
linux (tftp)/uefi/vmlinuz ip=dhcp inst.stage2=http://192.168.10.230/pxeboot/ inst.repo=http://192.168.10.230/pxeboot
# 【按本机修改】上一行两个 URL 里的 IP；x86_64 把 linux 改成 linuxefi
initrd (tftp)/uefi/initrd.img
# 【按架构选择】x86_64 把 initrd 改成 initrdefi
}
```


配置完成后查看69端口是否被监听，并在可以连接server的机器上测试tftp：

```
netstat -apndl | grep 69 | grep udp
tftp -v 192.168.10.230 -c get uefi/initrd.img
# 【按本机修改】上一行 IP 改成 PXE 服务器地址
```


**2.2 客户端配置**

硬件要求：支持PXE协议的网卡，同时保证内存>=2G

- 客户端加电启动后，网卡将自动发送DHCP请求，部署系统服务端响应DHCP请求、发送IP并传输系统初始化文件，客户机接收后开始执行操作系统安装步骤。
- 正确配置后，客户端会出现 GRUB 菜单，条目为
`Install OpenCloudOS 9`

，倒计时结束后自动进入 Anaconda 安装。`grub.cfg`

中已写`inst.repo`

时，安装源无需再配。未配置 Kickstart 时，磁盘、账号等仍要在图形界面中完成。

**第三章 无人值守（Kickstart）**

无人值守安装需要配置一个kickstart文件，这个文件相当于收集了手工执行配置的内容，进行自动配置。当前 OpenCloudOS 9 系统不自动生成kickstart文件，因此需要手动改写一个模版。可参考已安装系统上的 `/root/anaconda-ks.cfg`

。

将文件保存为 `/var/www/html/ks/anaconda-ks.cfg`

，然后在 `/var/lib/tftpboot/uefi/grub.cfg`

中加入 `inst.ks`

。下面同样：没标注的行可直接用，标了 `【按本机修改】`

的按环境改。

```
# Generated by Anaconda 38.23.2
# Generated by pykickstart v3.43
#version=DEVEL
# Use graphical install
graphical
url --url="http://192.168.10.230/pxeboot" # 【按本机修改】PXE 服务器上的 HTTP 安装源
# Keyboard layouts
keyboard --vckeymap=cn --xlayouts='cn'
# System language
lang zh_CN.UTF-8
# Run the Setup Agent on first boot
firstboot --enable
# Generated using Blivet version 3.8.0
ignoredisk --only-use=sda # 【按本机修改】客户端真实磁盘，如 vda、nvme0n1
# System bootloader configuration
bootloader --append="crashkernel=1G-4G:192M,4G-64G:256M,64G-:512M" --location=mbr --boot-drive=sda
# 【按本机修改】上一行 --boot-drive 与 ignoredisk 保持一致
# Partition clearing information
clearpart --none --initlabel
autopart --type=lvm
# System timezone
timezone Asia/Beijing --utc
rootpw --plaintext ChangeMe # 【按本机修改】改成自己的密码，或改用 --iscrypted
%packages
@^server-product-environment
%end
```


在 grub.cfg 的内核参数中加入 `inst.ks`

：

```
set default="0"
function load_video {
insmod efi_gop
insmod efi_uga
insmod video_bochs
insmod video_cirrus
insmod all_video
}
load_video
set gfxpayload=keep
insmod tftp
insmod gzio
insmod part_gpt
insmod ext2
set timeout=60
menuentry 'Install OpenCloudOS 9' {
linux (tftp)/uefi/vmlinuz ip=dhcp inst.stage2=http://192.168.10.230/pxeboot/ inst.repo=http://192.168.10.230/pxeboot inst.ks=http://192.168.10.230/ks/anaconda-ks.cfg
# 【按本机修改】上一行三个 URL 里的 IP；x86_64 把 linux 改成 linuxefi
initrd (tftp)/uefi/initrd.img
# 【按架构选择】x86_64 把 initrd 改成 initrdefi
}
```


内核行同时带上 `inst.stage2`

、`inst.repo`

和 `inst.ks`

。客户端再次PXE启动后，Anaconda会读取Kickstart并自动安装。