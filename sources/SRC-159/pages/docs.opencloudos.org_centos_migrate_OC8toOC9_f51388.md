source: https://docs.opencloudos.org/centos_migrate/OC8toOC9/

# 1.支持升级路径

源系统版本 |
目标系统版本 |
支持架构 |
|---|---|---|
| OpenCloudOS 8.x（含8.6、8.8、8.10） | OpenCloudOS 9.x(含9.0、9.2、9.4、9.6) | x86_64，aarch64 |

# 2.使用方法

### 2.1 下载安装

迁移工具已上线到软件源中，直接通过yum/dnf命令即可下载：

```
dnf install leapp-upgrade-oc8to9 -y
```


### 2.2 命令及选项

#### 2.2.1 升级预检查

可以使用下面的命令来检查升级过程中存在的风险，问题以及相关的解决方法：

```
leapp preupgrade --opencloudos
```


#### 2.2.2 系统升级

升级可运行下面的命令，在结束之后需要手动重启

```
leapp upgrade --opencloudos
```


如果不想手动重启，可以在后面添加--reboot

即：

```
leapp upgrade --opencloudos --reboot
```


#### 2.2.3 命令选项及含义

含义 |
是否加参数 |
参数格式举例 |
备注 |
|---|---|---|---|
| 升级时，启用目的系统的软件仓库 | 否 | --opencloudos | |
| 目的系统版本（包含小版本号） | 是 | --target 9.6 | |
| 运行升级命令时自动重启系统 | 否 | --reboot | 仅在运行升级命令时有效，预检查时，添加这个命令会报错 |
| 升级过程中不检查签名 | 否 | --nogpgcheck | |
| 系统升级时显示迁移工具debug信息 | 否 | --debug | |
| 系统升级时显示详细日志信息 | 否 | --verbose |

#### 2.2.4默认升级路径

在升级时，可以不在命令行中添加--target 选项，此时会遵守下面的升级路径：

升级路径 |
源系统 |
默认的目的系统 |
|---|---|---|
| 8->9 | OpenCloudOS 8.6 | OpenCloudOS 9.2 |
| 8->9 | OpenCloudOS 8.8 | OpenCloudOS 9.2 |

### 2.3 升级时产生的日志和文件说明

/var/log/leapp/中会保存升级工具在运行时产生的日志和报告文件，具体解释如下：

#### 2.3.1 升级日志文件

运行preupgrade时，会在 /var/log/leapp/中产生leapp-preupgrade.log，这个文件会记录整个升级工具预检查运行的完整流程。

运行upgrade时，会在 /var/log/leapp/中产生leapp-upgrade.log，这个文件会记录整个升级工具升级系统的完整流程。

#### 2.3.2 升级报告

在leapp-report.txt中会记录对系统升级检查的报告，每一条的形式如下：

包含了风险等级，标题名称，问题总结，解决建议等。

```
----------------------------------------
Risk Factor: high
Title: Packages not signed by TencentOS found on the system
Summary: The following packages have not been signed by TencentOS and may be removed during the upgrade process in case TencentOS-signed packages to be removed during the upgrade depend on them:
- MegaCli
- hpssacli
- iser
- isert
- kernel-mft
- knem
- knem-modules
- mlnx-ofa_kernel
- mlnx-ofa_kernel-devel
- mlnx-ofa_kernel-modules
- qemu-guest-agent
- srp
- xpmem
- xpmem-modules
Key: e869f4bf5760fbf3a3eb55921c2ced3c82a7c07d
----------------------------------------
Risk Factor: low
Title: Dosfstools incompatible changes in the next major version
Summary: The automatic alignment of data clusters that was added in 3.0.8 and broken for FAT32 starting with 3.0.20 has been reinstated. If you need to create file systems for finicky devices that have broken FAT implementations use the option -a to disable alignment.
The fsck.fat now defaults to interactive repair mode which previously had to be selected with the -r option.
Remediation: [hint] Please update your scripts to be compatible with the changes.
Key: c75fe5e06c70d9e764703fa2611f917c75946226
----------------------------------------
```


对于可能会造成某个常用软件或者某个关键功能不可用的情况，风险等级会被定义成high。

#### 2.4.3 软件包升级名单

在dnf-plugin-data.txt中记录了软件包的升级，安装和删除的情况。

其中：

- to_install代表新安装的软件包
- to_remove代表移除的软件包
- to_upgrade代表升级的软件包

不在此名单中的，如果也未在下面的白名单中，则会在升级快结束时被从系统中移除。

### 2.4 白名单功能及使用说明

目前迁移工具支持用户将用户本身不想升级的软件包加入到白名单，加入白名单的软件包需要不被其他软件依赖，同时依赖的软件包在升级前后系统中都存在。

使用方法：

在/etc/leapp/whitelist中写入用户想要保留的软件包，每个软件包名占一行，并且前面不能有"#"。如果whitelist这个文件不存在，则需要用户手动去建立。

比如，如果/etc/leapp/whitelist写入下面的内容，则Package1和 Package2则会被保留，Package3则会被升级或者删除

```
# add packages to this file to whitelist them from being removed by leapp
Package1
Package2
#Package3
```


# 3.说明

### 3.1备份与回滚

目前迁移/升级工具暂不支持备份与回滚，请在升级系统前做好备份

### 3.2 迁移环境和时长说明：

- 可在本地虚拟机，CVM（即deploy）和ndeploy（测试环境）上实现升级。
- 上述环境中，升级后，自动开启网络和ssh，不用手动连接。因此可实现远程升级，为后续多节点升级做好准备。
- 多内核升级时由于OC9中的grub和grubby的启动字段顺序对不上，可能不会进入最新内核，需用户手动进入最新内核。单内核不受影响。此处bug和迁移工具表现无关。
- 时长表现：经多次测试，在900-1000个软件包的系统中，重启前（即系统处于可用状态）耗时6-8分钟，具体时间和网络状况相关，因为新系统的软件包从软件源上获取，重启后耗时在4分30秒左右，整个过程在10-12分钟可完成。软件包数量增多时，时长会适当增加，即软件包数量越多，耗时越长，并不是线性增长。下面进行详细说明：
- 整个迁移时长分为三部分：除软件包下载和依赖解析的代码运行时长，软件包下载和安装时长，软件包之间依赖关系解析时长
- 除软件包下载和依赖解析的运行时长几乎固定，这是因为要检查的配置大多数为常见配置，多数系统都有，并且此部分耗时不长。
- 软件包下载和安装时长和软件包数呈正相关，在一定程度上线性增长。较大的软件包在安装和下载时对时长影响较大。
- 依赖解析时长和软件包数量相关，但是不是线性增长。这是因为依赖解析使用的libsolv，使用可满足性（SAT）理论来解决依赖关系，其时间复杂度大于等于O(n)，仅在理想情况下为O(n)。

# 4.部分禁止迁移的情景和解决方法：

### 4.1 显示有问题未确认

这时填写`/var/log/leapp/answerfile`

中问题即可

### 4.2显示禁止升级

禁止升级的情况，在leapp-report.txt中会有相关问题的说明和解决办法的说明，根据说明去操作即可