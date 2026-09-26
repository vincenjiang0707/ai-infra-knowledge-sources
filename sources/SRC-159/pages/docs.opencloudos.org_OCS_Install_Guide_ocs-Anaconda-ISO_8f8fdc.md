source: https://docs.opencloudos.org/OCS/Install_Guide/ocs-Anaconda-ISO/

# 使用 Anaconda ISO 镜像安装

## 1. 安装方式

### 1.1. 基于图形界面的安装

安装程序启动图形界面，用户可以通过图形界面对安装过程进行配置。

### 1.2. 基于文本界面的安装

安装程序启动文本界面，用户可以通过文本界面对安装过程进行配置。

### 1.3. 使用 Kickstart 执行自动安装

用户可以通过 Kickstart 文件对安装过程进行配置，实现安装过程的半自动化或全自动化。

## 2. 安装准备

### 2.1. 支持的架构

OpenClousOS 支持如下架构：

- x86_64（适用于 AMD 和 Intel 处理器）、aarch64（ARM 架构）以及 loongarch64（龙芯架构）。

### 2.2. 系统要求

安装 OpenCloudOS 操作系统前，您的环境需要满足以下要求：

- 最小内存：4GB
- 最小磁盘空间：50GB
- x86_64 版本系统需要在支持 x86_64-v2 及以上微架构的物理机、虚拟机部署

### 2.3. 已验证平台

已验证的物理机平台如下所示：

| 物理机平台 | 架构 | 规格 |
|---|---|---|
| Intel 服务器 | x86_64 | x86 96核 Intel(R) Xeon(R) Platinum 8255C CPU @ 2.50GHz 内存 256G，HDD 500G，SSD 3.6T，双网卡 |
| 泰山服务器 | aarch64 | aarch64 Kunpeng-920 128核2.6GHz内存512G，HDD 500G，SSD 3.6T，双25G网卡 |
| 长城服务器 | aarch64 | aarch64 长城擎天EF860128核，内存512G，HDD 1000G，SSD 4.4T |
| 龙芯 3C/3D/3E 5000 系列服务器 | loongarch64 | Loongson 3C5000 / 3D5000 / 3E5000，32 核 @ 2.0GHz～2.3GHz 内存 128 GB，SSD 1 TB，双千兆网卡 |
| 龙芯 3C/3D/3E 6000 系列服务器 | loongarch64 | Loongson 3C6000 / 3D6000 / 3E6000，64 核 @ 2.3GHz～2.5GHz 内存 256 GB，SSD 1 TB，双万兆网卡 |

已验证的虚拟机平台如下所示：

| 虚拟化平台 | HostOS | Host架构 | Host 芯片 | 固件 |
|---|---|---|---|---|
| qemu | MacOS | aarch64 | Apple M1 | UEFI |
| Parallels | MacOS | aarch64 | Apple M1 | UEFI |
| qemu | OpenCloudOS Stream | aarch64 | Kunpeng-920 | UEFI |
| vmware | Windows | x86_64 | Intel | UEFI/BIOS |
| virtualbox | Windows | x86_64 | Intel | UEFI/BIOS |
| Hyper V | Windows | x86_64 | Intel | UEFI/BIOS |
| qemu | OpenCloudOS Stream | x86_64 | Intel | UEFI/BIOS |
| qemu | OpenCloudOS Stream | loongarch64 | Loongson-3A5000 | UEFI |

注意：x86_64 架构下，OpenClousOS 仅支持 x86_64-v2 及以上微架构级别。通过 qemu 直接启动虚拟机时，默认为 x86_64-v1，需要通过 -cpu host 或者 -cpu max 参数指定。

### 2.4. 安装镜像说明

| 镜像类型 | 镜像文件名称 | 架构 | 说明 |
|---|---|---|---|
| everything iso | OpenCloudOS-Stream-23-YYYYMMDD-x86_64-everything.iso | x86_64 | everything ISO 镜像文件包含了所有软件包，分为 BaseOS 和 AppStream 两个软件仓库，无需配置额外的软件源，可以直接进行安装。 |
| everything iso | OpenCloudOS-Stream-23-YYYYMMDD-aarch64-everything.iso | aarch64 | everything ISO 镜像文>件包含了所有软件包，分为 BaseOS 和 AppStream 两个软件仓库，无需配置额外的软件源，可以直接进行安装。 |
| netinst iso | OpenCloudOS-Stream-23-YYYYMMDD-x86_64-netinst.iso | x86_64 | netinst ISO 镜像文件不包含任何软件包，需要在安装源设置界面配置网络安装源，然后进行安装，配置方式可以参考 安装指导>Anaconda 镜像安装>基于图形界面的安装>软件源 一节。 |
| netinst iso | OpenCloudOS-Stream-23-YYYYMMDD-aarch64-netinst.iso | aarch64 | netinst ISO 镜像文件不包含任何软件包，需要在安装源设置界面配置网络安装源，然后进行安装，配置方式可以参考 安装指导>Anaconda 镜像安装>基于图形界面的安装>软件源 一节。 |

安装镜像可以从 OpenCloudOS 社区官方网站获取 [https://www.opencloudos.org/iso](https://www.opencloudos.org/iso)。

## 3. 安装指导

### 3.1. 安装引导方式

| 安装引导方式 | 说明 |
|---|---|
| 光驱 | 用 everything iso 镜像刻录 DVD 光盘，将光盘放入支持光驱的物理设备后，并设置从光驱启动。也可以用 netinst iso 镜像刻录 DVD 光盘，该镜像不包含软件包，安装过程中需要设置额外的安装源。 |
| 虚拟光驱 | 将 everything iso 镜像添加或者挂载到支持虚拟光驱的服务器或者虚拟机平台（如 qemu、virtualbox 和 vmware 等），并设置从虚拟光驱启动。也可以将 netinst iso 镜像添加或者挂载到支持虚拟光驱的服务器或者虚拟机平台，该镜像不包含软件包，安装过程中需要设置额外的安装源。 |
| USB 启动盘 | 用 everything iso 镜像制作 USB 启动盘，将 USB 启动盘插入支持 USB 启动的物理设备后，并设置从 USB 启动。也可以用 netinst iso 镜像制作 USB 启动盘，该镜像不包含软件包，安装过程中需要设置额外的安装源。 |
| 网络引导 | 如果待安装 OS 的机器同网络环境下存在可用于安装系统的 PXE 服务器，将机器设置为网卡启动即可。如果 PXE 服务器下用于安装引导的引导菜单未设置 Kickstart 文件或者安装源，安装过程中还需要设置额外的安装源。 |

### 3.2. 创建安装源

通过 everything iso 刻录的光盘、挂载的虚拟光驱以及制作的 USB 启动盘启动安装，安装程序可以自动检测到安装源。通过 netinst iso 刻录的光盘、挂载的虚拟光驱以及制作的 USB 启动盘启动安装，安装过程中还需要设置额外的安装源。通过 PXE 服务器启动安装，需要在部署 PXE 服务器时，创建和配置安装源。

| 安装源类型 | 说明 |
|---|---|
| NFS | 将 everything iso 镜像中的内容复制到 NFS 服务器 NFS 共享目录中。另外，需要通过启动参数、Kickstart 文件或者安装交互界面为安装程序指定该安装源。 |
| HTTP/HTTPS | 将 everything iso 镜像中的内容复制到 HTTP/HTTPS 服务器上提供该服务的程序设置的根目录或者其子目录中。另外，需要通过启动参数、Kickstart 文件或者安装交互界面为安装程序指定该安装源。 |
| FTP | 将 everything iso 镜像中的内容复制到 FTP 服务器 FTP 服务器上提供该服务的程序设置的根目录或者其子目录中，需要通过启动参数、Kickstart 文件或者安装交互界面为安装程序指定安装源。 |

如何指定安装源可以参考为安装程序指定安装源章节。

### 3.3. 安装引导菜单

系统通过引导介质完成引导后，会使用 GRUB2 显示 OpenCloudOS 引导菜单，如下图所示：

使用键盘上下方向键选择不同的引导项，选中后按 "Enter" 键进入对应的引导项。如果 60s 内没有操作，则默认进入高亮引导项。

按 "e" 键可以修改选中的引导项，修改完成后，按 Ctrl+X 使修改生效，并继续启动。

按 "c" 键进入 grub 命令行。

引导菜单选项说明如下：

| 引导菜单选项 | 描述 |
|---|---|
| Install OpenCloudOS Stream 23 | 启动图形界面安装 OpenCloudOS Stream。 |
| Test this media & install OpenCloudOS Stream 23 | 默认选项，检查安装介质的完整性并启动图形界面安装 OpenCloudOS Stream。 |
| Troubleshooting | 问题定位选项。 |
| Troubleshooting --> Rescue a OpenCloudOS Stream system | 救援模式，在该模式下可进行问题定位和修复。 |

### 3.4. 基于图形界面的安装

#### 3.4.1. 安装语言设置界面

引导菜单保持默认启动选项进入 Install OpenCloudOS Stream 23 或者 Test this media & install OpenCloudOS Stream 23，启动一段时间后系统会进入图形安装界面。

首先显示的是安装语言设置界面，该界面设置安装过程中使用的语言。目前，OpenCloudOS Stream 仅支持中文和英文，默认为简体中文。OpenCloudOS 支持多种语言。

设置完成后，单击 "继续" 按钮，进入安装主界面。如果想要退出安装，单击 "退出" 按钮，系统会重启并重新引导进入引导菜单。

#### 3.4.2. 图形模式安装主界面

安装主界面如下图所示：

在安装主界面，用户可以进行键盘、语言、时间和日期、安装源、软件选择、安装磁盘、KDUMP、网络及用户等设置。

图标右下角存在告警符号，表示该选项未设置完成或者设置错误。安装主界面所有告警符号消除后，右下角的开始安装按钮才可以点击。

如果想要退出安装，单击"退出"按钮，系统会重启并重新引导进入引导菜单。

后面的章节对各个安装设置项进行说明。

#### 3.4.3. 键盘

在安装主界面单击"键盘"，进入键盘布局界面，如下图所示：

查看键盘布局：单击左侧选框下方的键盘图标查看当前键盘布局。

添加键盘布局：单击左侧选框下方的加号图标。

删除键盘布局：选中待删除的键盘布局，单击左侧选框下方的减号图标，如果当前只有一个键盘布局，则还需要重新选择一个键盘布局以替换当前键盘布局。

测试键盘布局：如果当前存在多个键盘布局，单击右上角键盘图标可以切换，在右侧文本库进入输入测试。

设置完成后，单击"完成"按钮回到安装主界面。

#### 3.4.4. 语言支持

在安装主界面单击"语言支持"，进入语言支持界面，如下图所示：

右侧复选框选中需要支持的语言。

设置完成后，单击"完成"按钮回到安装主界面。

#### 3.4.5. 时间和日期

在安装主界面单击"时间和日期"，进入时间和日期设置界面，如下图所示：

设置时区：可通过左上角地区和城市下拉框设置，也可以点击地图设置。

注意：如果需要手动设置日期和时间，需要关闭右上角网络时间。

设置完成后，单击"完成"按钮回到安装主界面。

#### 3.4.6. 安装源

在安装主界面单击"安装源"，进入安装源设置界面，如下图所示：

- 自动检测到的安装介质

当使用 everything.iso 进行安装时，安装程序会自动检测安装源，保持默认即可。

- ISO 文件

可以单击右侧"选择 ISO 按钮" 选择存在安装源的 ISO 文件。

- 在网络上
- http/https 方式：右侧文本框中输入网络安装源的 URL
- ftp 方式：右侧文本框中输入网络安装源的 ftp 地址
- nfs 方式：右侧文本框中输入网络安装源的 nfs 地址

额外软件仓库：设置额外的软件仓库，存在 http/https、ftp、nfs 三种方式，设置方法与上述相同。

设置完成后，单击"完成"按钮回到安装主界面。

#### 3.4.7. 软件选择

如果软件源设置正确，在安装主界面单击"软件选择"，进入软件选择设置界面，下图为 everything.iso 默认配置：

当前 OCS 默认有服务器和最小安装两个基本安装环境，每个安装环境下会默认安装不同数量的软件包。

选中基本环境后，右侧显示当前软件环境下可选的软件组。用户可以根据需要选择安装。

设置完成后，单击"完成"按钮回到安装主界面。

#### 3.4.8. 安装目的地

在安装主界面单击"安装目的地"，进入安装目标设置界面，如下图所示：

本地标准磁盘：选择待安装操作系统的磁盘

专用磁盘 & 网络磁盘：添加专用磁盘和网络磁盘

存储配置：

默认为自动，安装程序自动进行分区。如果未勾选通过删除或压缩已有分区来释放空间，则默认安装到选中磁盘的剩余空间，空间不足时会通过对话框提示用户回收空间。

也可以通过勾选删除或压缩已有分区来释放空间，主动进行空间回收。

如果选中自定义，单击完成按钮，则进入手动分区界面，如下图所示：

自动创建：如果空间充足，系统会根据可用存储空间自动创建分区，UEFI 启动方式下自动创建的分区为 /boot、/boot/efi 和 /，BIOS 启动方式下自动创建的分区为 /boot、BIOS boot 和 /。

手动创建：点开 "+" 按钮创建新挂载点，根据提示设置即可。创建完成后，选中该分区，右侧可以设置该分区挂点、期望容量、设备类型、文件系统等，如下图所示：

设置完成后，单击"完成"按钮并接受更改回到安装主界面。

#### 3.4.9. KDUMP

在安装主界面单击"KDUMP"，进入 KDUMP 设置界面，如下图所示：

启用 kdump：默认勾选，勾选后启用 kdump，不勾选则禁用 kdump

为 Kdump 保留的内存：启用 kdump 需要预留内存。选中自动，则根据内存大小配置，选中手动，则需要手动设置保留的内存数值。

设置完成后，单击"完成"按钮回到安装主界面。

#### 3.4.10. 网络和主机名

在安装主界面单击"网络与主机名"，进入网络与主机名设置界面，如下图所示：

设置主机名：在主机名文本框输入需要设置的主机名，单击"应用"按钮生效。

配置网络：左侧选框选中网口，单击"配置"按钮进行网络配置，配置界面如下：

设置完成后，单击"完成"按钮回到安装主界面。

#### 3.4.11. Root 账户

在安装主界面单击"Root 账户"，进入Root 账户设置界面，如下图所示：

安装程序默认禁用 root 账户，选择启用 root 账户后，需要设置 root 账户密码。同时可以设置是否允许 root 用户使用密码进行 SSH 登陆。

设置完成后，单击"完成"按钮回到安装主界面。

#### 3.4.12. 创建用户

在安装主界面单击"创建用户"，进入创建用户界面，如下图所示：

用户可以设置用户名和用户密码。如果 root 账户被禁用，则必须创建普通用户。

设置完成后，单击"完成"按钮回到安装主界面。

#### 3.4.13. 安装完成

所有必要的项目设置完成后，右下角的"开始安装"按钮则可以点击，单击开始安装，进入安装进度界面，等待安装完成。

安装完成后，右下角的"重启系统"按钮则可以点击，单击后，系统重启进入安装好的系统。

### 3.5. 基于文本界面的安装

当启动图形安装界面失败或通过修改引导菜单，在启动参数中添加 inst.text（如果启动参数中存在 inst.graphical，需要删除），安装程序进入命令行模式：

在命令行模式输入 2 (表示使用文本模式)，然后按回车键，进入文本模式安装主界面：

对应项目后面中括号内为 x，表示该选项设置完成，中括号内为 !，表示该选项未设置完成或者设置错误。

所有必须项设置完成后，则可以输入 b，按回车键开始安装。

### 3.6. 使用 VNC 执行远程安装

当启动图形安装界面失败或通过修改引导菜单，在启动参数中添加 inst.text（如果启动参数中存在 inst.graphical，需要删除），安装程序进入命令行模式。

在命令行模式输入 1（表示启动 VNC），按回车键，然后按照命令行提示设置 VNC 服务端密码（直接按回车键，则为空密码），最终命令行显示 VNC 服务器 ip 和端口号：

在与该机器网络互通的环境使用 vnc 客户端工具，通过命令行提示的 ip 地址和端口号以及设置的 VNC 密码连接即可进入安装语言设置界面，后续流程与图形界面安装方式相同。

注意：该安装方式需要网络。

### 3.7. 使用 Kickstart 执行自动安装

#### 3.7.1. Kickstart 安装简介

通常，OpenCloudOS 的安装需要人工介入，用户通过图形界面或者文本界面进行必要的配置，如：磁盘分区，账户设置等，然后才能进行安装。Kickstart 安装就是将必要的配置写入 Kickstart 文件，然后在启动引导项中指定 Kickstart 文件位置，安装程序则通过解析启动参数中指定的 Kickstart 文件，对安装过程自动配置，从而实现安装过程的半自动化或全自动化。

#### 3.7.2. 创建 Kickstart 文件

可以从已安装的 OpenCloudOS Stream 环境中获取 kickstart 文件，路径为 /root/anaconda-ks.cfg，然后根据需要进行修改，参考示例如下：

```
# Generated by Anaconda 38.4
# Generated by pykickstart v3.43
#version=DEVEL
# Use graphical install
graphical
%addon com_redhat_kdump --enable --reserve-mb='auto'
%end
# Keyboard layouts
keyboard --vckeymap=cn --xlayouts='cn'
# System language
lang zh_CN.UTF-8
# Use network installation
url --url="http://10.211.55.4/repo/BaseOS"
%packages
@^server-product-environment
@container-management
%end
# Generated using Blivet version 3.5.0
ignoredisk --only-use=sda
# Partition clearing information
clearpart --all --initlabel --drives=sda
# Disk partitioning information
part /boot/efi --fstype="efi" --ondisk=sda --size=64 --fsoptions="umask=0077,shortname=winnt"
part pv.1074 --fstype="lvmpv" --ondisk=sda --size=64958
part /boot --fstype="ext4" --ondisk=sda --size=512
volgroup os --pesize=4096 pv.1074
logvol /home --fstype="ext4" --size=34235 --name=home --vgname=os
logvol / --fstype="ext4" --size=30720 --name=root --vgname=os
# System timezone
timezone Asia/Beijing --utc
# Root password
rootpw --iscrypted --allow-ssh $y$j9T$vMmKHQemYJsi90Eymv.zIg4G$yBHKrrxsqtvbHhsM.fjHnl4Kqt4weD6kRpKlriNLVKD
user --groups=wheel --name=testuser --password=$y$j9T$Jq6FOkz7oYjkO8L7N7qwspE1$xz3XoGTo2SSmFkxAjKXtjZ2eympwjR/5CCRxTCBT7P4 --iscrypted --gecos="testuser"
```


Kickstart 文件一般包含命令和部分两种类型。命令为安装指令的关键字，其使用类似在 shell 中使用 Linux 命令。部分以一些%开头的关键字开始，每个部分都必须使用 %end 结束。

下面对示例 Kickstart 文件中涉及的命令和部分进行简要介绍：

- graphical

可选命令，表示以图形模式进行安装。可以替换成 text（文本模式安装）或 cmdline（完全非交互式安装，需要交互时安装会终止），默认为 graphical。

- %addon

可选部分，表示插件部分，可以存在多个插件部分，插件部分自身不包含任何选项，依赖具体的插件。

示例中配置了 com_redhat_kdump 插件，其选项如下：

--enable： 在安装的系统中使能 kdump

--disable：在安装的系统中禁用 kdump

--reserve-mb=：为 kdump 预留内存，单位为 MiB，示例中为 auto，表示由安装程序自动分配内存。

- keyboard

必需命令，配置键盘布局。是李忠该命令使用的选项用法如下：

--vckeymap=：指定 vconsole 键映射，其有效名称对应 /usr/lib/kbd/keymaps/xkb/ 目录下的文件名（去除 .map.gz 扩展名）。

--xlayouts=：指定 X 键盘布局。可以在 xkeyboard-config man page 中查看所有可用键盘布局。

- lang

必需命令，设置安装过程中使用的语言及安装后的系统默认语言。

- url

可选命令，实际运行安装，必须指定以下参数之一：

cdrom：使用光驱

harddrive：使用本地磁盘上的完整安装镜像执行安装。

nfs：从指定 nfs 服务器获取安装源。

liveimg：使用指定的磁盘镜像执行安装。

url：通过 ftp、http 或者 https 协议从指定地址获取安装源。

- %packages

必需部分，选定要安装的软件包，以 %end 结束。

@^environment_name：指定要安装的基本环境。

@group_name：指定要安装的软件组。

package_name：指定单个软件包。

- ignoredisk

可选命令，指定安装程序使用或者忽略的磁盘。

--drives=drive1,drive2,...：指定希望忽略的磁盘。

--only-use=drive1,dirve2,...：指定要使用的磁盘。

注意：必须使用 --drives 和 --only-use 其中之一。

- clearpart

可选命令，指定安装程序从系统中删除分区。示例中该命令使用的选项用法如下：

--all：清除所有分区。

--initlabel：为选中的磁盘创建默认的磁盘标签。

--drives：指定待清除分区的磁盘。

- part

必须命令（必须使用 part 或者 autopart 之一，autopart 指定安装程序自动分区），在磁盘上创建分区。示例中该命令使用的选项用法如下：

pv.id：用于创建 LVM 物理卷。

/path：指定分区挂载点。

--fstype=：指定分区上创建的文件系统类型。

--ondisk=：指定创建分区的磁盘。

--size：指定分区大小，单位为 MiB。

- volgroup

volgroup os --pesize=4096 pv.1074

可选命令，创建 LVM 卷组。示例中该命令使用的选项用法如下：

volgroup_name：指定卷组名称。

--pesize=：指定卷组物理扩展的大小。

pv.id：指定创建卷组包含的物理卷。

- logvol

可选命令，创建 LVM 逻辑卷。示例中该命令使用的选项用法如下：

--fstype=：指定逻辑卷上创建的文件系统类型。

--size：指定分区大小，单位为 MiB。

--name=：指定逻辑卷的名称。

--vgname=：指定创建逻辑卷的卷组。

注意：创建逻辑卷，首先需要创建物理卷，然后创建卷组包含物理卷，最后在卷组上创建逻辑卷。

- timezone

必需命令，设置系统时区。示例中该命令使用的选项用法如下：

timezone_name：指定时区。

--utc：如果存在，系统假定硬件始终被设置为 UTC 时间。

- rootpw

必需命令，设置 root 账户密码。

--iscrypted：表示命令参数提供的是加密后的密码，。

--allow-ssh：允许 root 用好通过 ssh 登陆。

password：纯文本或者加密后的密码字符串。

关于 Kickstart 更详细信息可以查阅社区文档：[https://pykickstart.readthedocs.io/en/latest](https://pykickstart.readthedocs.io/en/latest/)。

#### 3.7.3. 为安装程序指定 Kickstart 文件

- HTTP/HTTPS

将 Kickstart 文件放置到 HTTP/HTTPS 服务程序设置的根目录或者其子目录下。如：$HTTPROOT/ocs23-install/ks.cfg，则可以在引导选项中添加 inst.ks=http://http_server/ocs23-install/ks.cfg。

- NFS

将 Kickstart 文件放置到 NFS 共享目录下。如：$NFSROOT/ocs23-install/ks.cfg，则可以在引导选项中添加 inst.ks=nfs:nfs_server:/ocs23-install/ks.cfg。

- FTP

将 Kickstart 文件放置到 FTP 服务程序设置的根目录或者其子目录下。如：$FTPROOT/ocs23-install/ks.cfg，则可以在引导选项中添加 inst.ks=ftp://ftp_server/ocs23-install/ks.cfg。

- CD-ROM

将 ks 文件添加到了 Anaconda ISO 镜像 。如：ocs23-install/ks.cfg，则可以在引导选项中添加 inst.ks=cdrom:/ocs23-install/ks.cfg。

#### 3.7.4. 为安装程序指定安装源

- 通过 Kickstart 文件指定安装源

在 Kickstart 文件内可以通过 url 命令指定安装源，命令用法如下：

```
# 指定 http/https 安装源
url --url=http://http_server/repo_path
# 指定 nfs 安装源
url --url=nfs:nfs_server:/repo_path
# 指定 ftp 安装源
url --url=ftp://ftp_server/repo_path
```


- 通过安装引导菜单指定安装源

在安装引导菜单，可以添加 inst.repo 方式指定安装源，用法如下：

```
# 指定 http/https 安装源
inst.repo=http://http_server/repo_path
# 指定 nfs 安装源
inst.repo=nfs:nfs_server:/repo_path
# 指定 ftp 安装源
inst.repo=ftp://ftp_server/repo_path
```


- 通过安装交互界面指定安装源

可以通过图形安装模式主安装界面下安装源选项或者文本安装模式安装界面的 Installation source 设置安装源。

#### 3.7.5. Kickstart 半自动化安装

Kickstart 半自动化安装是指安装过程部分步骤需要人工介入，这里介绍的方法主要是指需要在安装启动参数中人工指定 kickstart 文件及安装源。

流程如下：

使用 netinst.iso 启动机器，在 grub 界面按 'e' 键。

在 grub 中添加 inst.ks=http://x.x.x.x/ks.cfg，x.x.x.x 为存放 ks.cfg 文件的 http 服务器 ip（部署方法可参考 Kickstart 全自动化安装章节）。

然后按 “Ctrl + x” 启动系统 ，等待安装完成，安装完成后，会显示如下界面，重启后进入系统（如果需要自动重启，可以在 kickstart 文件最后添加 reboot）：

#### 3.7.6. Kickstart 全自动化安装

Kickstart 全自动化安装流程如下：

待安装机器从网卡启动并发送 DHCP 请求 ==> 从 DHCP 服务器获取 IP 及 TFTP 服务器信息 ==> 从 TFTP 服务器获取 grub 引导程序，grub.cfg，vmlinuz 和 initrd ==> 内核启动 ==> initrd 启动 => 下载 grub.cfg 中指定的 ks.cfg ==> 根据 ks.cfg 中指定的 url 获取 install.img ==> switch-root ==> install.img 启动 ==> anaconda 启动 ==> 根据 ks.cfg 配置设置并安装。

下面以 aarch64 UEFI 引导为例说明部署过程：

**关闭防火墙**

```
systemctl disable firewalld
systemctl stop firewalld
```


**清空 iptables 规则**

```
iptables -F
```


**关闭 selinux**

修改 /etc/selinux/config 中 SELINUX 值为 disabled，如下，修改后需要重启系统生效：

```
...
SELINUX=disabled
...
```


**部署 DHCP 服务器**

1、安装 dhcp-server 软件包，命令如下：

```
dnf install dhcp-server
```


2、添加 /etc/dhcp/dhcpd.conf 配置文件，参考示例如下：

```
default-lease-time 600;
max-lease-time 7200;
log-facility local7;
# 指定 TFTP 服务器及 grub 引导程序
next-server 10.211.55.4;
filename "pxe/grubaa64.efi";
subnet 10.211.55.0 netmask 255.255.255.0 {
option routers 10.211.55.1; # 网关
option subnet-mask 255.255.255.0; # 子网掩码
range dynamic-bootp 10.211.55.100 10.211.55.200; # 分配 IP 范围
}
```


注意：上述的 TFTP、网关、子网掩码等需要根据部署环境修改。

3、启动 dhcp 服务器，命令如下：

```
systemctl enable dhcpd
systemctl start dhcpd
```


**部署 TFTP 服务器**

1、安装 tftp-server 软件包，命令如下：

```
dnf install tftp-server
```


2、启动 tftp 服务，命令如下：

```
systemctl enable tftp.socket
systemctl start tftp.socket
```


3、拷贝引导文件到 tftp 目录下：

命令参考如下（需要预先下载 everything.iso）：

```
mount OpenCloudOS-Stream-23-20230530-aarch64-everything.iso /mnt
mkdir -p /var/lib/tftpboot/pxe
chmod 755 /var/lib/tftpboot/pxe
cp /mnt/EFI/BOOT/grubaa64.efi /var/lib/tftpboot/pxe
cp /mnt/images/pxeboot/vmlinuz /var/lib/tftpboot/pxe/
cp /mnt/images/pxeboot/initrd.img /var/lib/tftpboot/pxe/
chmod 755 /var/lib/tftpboot/pxe/grubaa64.efi
chmod 644 /var/lib/tftpboot/pxe/vmlinuz
chmod 644 /var/lib/tftpboot/pxe/initrd.img
```


4、添加 grub.cfg 文件到 /var/lib/tftpboot/pxe 目录下，内容参考如下：

```
set default="1"
function load_video {
if [ x$feature_all_video_module = xy ]; then
insmod all_video
else
insmod efi_gop
insmod efi_uga
insmod ieee1275_fb
insmod vbe
insmod vga
insmod video_bochs
insmod video_cirrus
fi
}
load_video
set gfxpayload=keep
insmod gzio
insmod part_gpt
insmod ext2
set timeout=10
### END /etc/grub.d/00_header ###
search --no-floppy --set=root -l 'OpenCloudOS'
### BEGIN /etc/grub.d/10_linux ###
menuentry 'Install OpenCloudOS Stream 23 (PXE)' --class red --class gnu-linux --class gnu --class os {
set root=(tftp,10.211.55.4)
linux /pxe/vmlinuz kdump_addon=on console=tty0 ro inst.ks=http://10.211.55.4/ks.cfg
initrd /pxe/initrd.img
}
```


其中，"set timeout=10" 语句设置 GRUB 界面超时时间，如果需要批量化部署，可以设置为 0，则 GRUB 界面不显示直接启动安装。

**部署 nginx 服务器**

安装 nginx 软件包：

```
dnf install nginx
```


修改 nginx 配置：

根据需要修改根目录，这里修改为 /data；添加 autoindex on; 条目（允许查看目录），参考如下（只显示修改部分）：

```
...
http {
...
server {
...
root /data;
autoindex on;
...
}
}
...
```


启动 nginx：

```
systemctl enable nginx
systemctl start nginx
```


在 /data 目录下创建 repo 目录，重新挂载 everything.iso 到 /data/repo 目录下。也可以拷贝 everything.iso 中所有内容到 /data/repo 目录下，everything.iso 中有隐藏文件 .treeinfo，需要复制到 /data/repo 下。

```
/home/OpenCloudOS-Stream-23-20230530-aarch64-everything.iso /data/repo/
```


将示例中的 ks.cfg 文件复制到 /data 目录下（如果需要安装完成后自动重启，可以在 ks.cfg 文件最后添加 reboot）。

**启动自动化安装**

DHCP、TFTP、nginx 服务部署完成后，同一网络环境下从网卡启动待安装机器即可，示例如下：

1、从网卡启动：需要在固件设置界面选择，参考示例如下：

选择后可以看到 ">>>Start PXE over IPv4" 打印。

2、进入 GRUB 界面，参考示例如下：

手动选择或倒计时结束后，则启动进入安装界面，安装过程自动开始，安装完成后停留在如下界面：

### 3.8. 安装调测

#### 3.8.1. 终端切换

如果图形界面安装过程中出现问题，可以通过 Alt + Ctrl + F1 ~ F6 切换终端，查看后台日志，说明如下：

Alt + Ctrl + F1（tty1）：文本安装时，命令行交互界面显示在 tty1，图形界面安装时，主要显示 anaconda 进程的部分输出，如下：

Alt + Ctrl + F2（tty2）：命令行 shell 终端

Alt + Ctrl + F3（tty3）：命令行 shell 终端

Alt + Ctrl + F4（tty4）：日志终端，主要输出日志

Alt + Ctrl + F5（tty5）：命令行 shell 终端

Alt + Ctrl + F6（tty6）：文本安装时为命令行 shell 终端，图形界面安装时为图形安装界面

如果文本安装或者图形安装出现问题可以切换到命令行终端查看日志，问题解决后切换会对应的终端继续操作。

#### 3.8.2. 安装日志说明

切换到 shell 终端后，可以在 /tmp 目录下查看日志：

```
$ ls /tmp/
X.log journal.log systemd-private-35137562ffd54490a5b6346c77082bc4-chronyd.service-pATIgt
anaconda.log lvm.log systemd-private-35137562ffd54490a5b6346c77082bc4-colord.service-EnACoz
at-spi packaging.log systemd-private-35137562ffd54490a5b6346c77082bc4-dbus-broker.service-P37po5
bus program.log systemd-private-35137562ffd54490a5b6346c77082bc4-systemd-hostnamed.service-HPr1H4
dbus.log storage.log systemd-private-35137562ffd54490a5b6346c77082bc4-systemd-logind.service-tUvQBc
dnf.cache storage.state systemd-private-35137562ffd54490a5b6346c77082bc4-systemd-resolved.service-k0cT4M
dnf.librepo.log syslog tmux-0
hawkey.log systemd
```


X.log：xorg 日志，图形界面启动问题可以查看此日志

journal.log：systemd 服务日志

anaconda.log：anaconda 运行日志

lvm.log：逻辑卷相关日志

packaging.log、dnf.librepo.log：软件包安装相关日志

program.log：anaconda 调用的部分命令日志

storage.log：存储相关日志

syslog：系统日志

#### 3.8.3. 向社区报告 bug

如果无法解决安装问题，可以对安装界面进行截图，并切换到后台 /tmp 目录下日志，提交 bug 到 OpenCloudOS 社区 bugzilla 网站：[https://bugs.opencloudos.tech/](https://bugs.opencloudos.tech/)。

如果环境没有网络，可以通过挂盘等方式重新安装复现问题后，在后台将 /tmp 目录下日志复制到添加的盘上。如果环境有网络，可以配置 ip 后，通过 scp 传输日志。