source: https://docs.opencloudos.org/OCS/AdministratorGuide/Software_Management/

# 1 软件包管理介绍

包括本系统在内的 Linux 发行版本质上都是由包括 kernel 在内的软件包 (package) 通过一定的组织形式构成的。软件包管理工具的作用就是安全高效地管理这些软件包。

目前本系统仅支持 rpm 这一类软件包格式，支持 dnf 和 yum 两种包管理软件，这里强烈推荐用户更多地使用 dnf。

# 2 软件源介绍

包管理工具都是从可用的软件包源中下载用户指定的软件包以及其依赖包，然后进行安装、升级等操作，因此需要提供可靠的软件源。

## 2.1 在线软件源

目前系统已默认配置好基础的 repo 源，如下所示，用户无需再额外配置。

需要注意的是，仅 `[BaseOS]`

和 `[AppStream]`

两项是默认使能的，因此用户想使用其它几项的源，需要手动调整 `enabled=1`


```
cat /etc/yum.repos.d/OpenCloudOS-Stream.repo
[BaseOS]
name=BaseOS $releasever - $basearch
baseurl=https://mirrors.opencloudos.tech/opencloudos-stream/releases/$releasever/BaseOS/$basearch/Packages/
gpgcheck=1
enabled=1
gpgkey=file:///etc/pki/rpm-gpg/RPM-GPG-KEY-OpenCloudOS-Stream
[AppStream]
name=AppStream $releasever - $basearch
baseurl=https://mirrors.opencloudos.tech/opencloudos-stream/releases/$releasever/AppStream/$basearch/Packages/
gpgcheck=1
enabled=1
gpgkey=file:///etc/pki/rpm-gpg/RPM-GPG-KEY-OpenCloudOS-Stream
[BaseOS-debuginfo]
name=BaseOS-debuginfo $releasever - $basearch
baseurl=https://mirrors.opencloudos.tech/opencloudos-stream/releases/$releasever/BaseOS/$basearch/debug/
gpgcheck=1
enabled=0
gpgkey=file:///etc/pki/rpm-gpg/RPM-GPG-KEY-OpenCloudOS-Stream
[AppStream-debuginfo]
name=AppStream-debuginfo $releasever - $basearch
baseurl=https://mirrors.opencloudos.tech/opencloudos-stream/releases/$releasever/AppStream/$basearch/debug/
gpgcheck=1
enabled=0
gpgkey=file:///etc/pki/rpm-gpg/RPM-GPG-KEY-OpenCloudOS-Stream
[BaseOS-source]
name=BaseOS-source $releasever
baseurl=https://mirrors.opencloudos.tech/opencloudos-stream/releases/$releasever/BaseOS/source/
gpgcheck=1
enabled=0
gpgkey=file:///etc/pki/rpm-gpg/RPM-GPG-KEY-OpenCloudOS-Stream
[AppStream-source]
name=AppStream-source $releasever
baseurl=https://mirrors.opencloudos.tech/opencloudos-stream/releases/$releasever/AppStream/source/
gpgcheck=1
enabled=0
gpgkey=file:///etc/pki/rpm-gpg/RPM-GPG-KEY-OpenCloudOS-Stream
```


此外，我们还提供了 EPOL 源，EPOL 是 Extra Packages for OpenCloudOS Linux 的缩写，旨在提供更多增强功能，EPOL 源默认已配置，但是如果发生缺失的情况，用户可以通过如下命令安装 EPOL 源的 repo 文件：

```
dnf install -y opencloudos-stream-epol-repos
```


安装完成之后即可访问 EPOL 中的 rpm 包。

## 2.2 搭建本地软件源

除了使用官方的在线源之外，对于需要离线使用软件源的场景，用户可以自己搭建本地软件源，具体步骤如下：

1 创建目录

```
mkdir -p /mnt/myiso # 创建放置 iso 的目录，位置随意，确保存储空间充足
mkdir -p /mnt/my_yum # 创建挂载 iso 的目录，位置随意，确保存储空间充足
```


```
cd /mnt/myiso
wget https://mirrors.opencloudos.tech/opencloudos-stream/releases/23/images/x86_64/OpenCloudOS-Stream-23-20230301-x86_64-everything.iso
```


**注：示例中的版本号仅作为演示，用户需要按需填写自己的版本的路径**

3 挂载 iso

```
# mount -o loop /mnt/myiso/OpenCloudOS-Stream-23-20230301-x86_64-everything.iso /mnt/my_yum/
mount: /mnt/my_yum: WARNING: source write-protected, mounted read-only.
```


`/mnt/my_yum`

目录 访问 iso 中的rpm包了
```
cd /mnt/my_yum/
tree -L 2
.
├── AppStream
│ ├── Packages
│ └── repodata
├── BaseOS
│ ├── Packages
│ └── repodata
├── boot
│ └── grub2
├── EFI
│ └── BOOT
└── images
├── efiboot.img
├── eltorito.img
├── install.img
└── pxeboot
12 directories, 3 files
```


```
cat /etc/yum.repos.d/local.repo
[AppStream]
name=AppStream
baseurl=file:///mnt/my_yum/AppStream
priority=1
enabled=1
[BaseOS]
name=BaseOS
baseurl=file:///mnt/my_yum/BaseOS
priority=1
enabled=1
```


可以尝试安装一个软件包，或者查询源中的软件包

## 2.3 搭建临时本地源

除了使用我们官方提供的 iso 搭建本地源之外，用户也可以自行准备 rpm 包，将指定目录制作为临时的本地源，具体步骤如下：

1 创建目录

```
mkdir -p /mnt/local_repo/x86_64/Packages # 目录位置随意，确保存储空间足够即可
```


```
dnf install -y createrepo
```


```
cp *.rpm /mnt/local_repo/x86_64/Packages
```


```
createrepo /mnt/local_repo/x86_64
```


这一步执行完后会在 `/mnt/local_repo/x86_64`

目录下创建 repodata
5 配置本地 repo 源，可以参考如下：

```
cat /etc/yum.repos.d/local.repo
[local]
name=local
baseurl=file:///mnt/local_repo/x86_64
priority=1
enabled=1
```


# 3 包管理配置

系统默认通过 dnf 工具进行软件包管理。dnf 配置分为两部分：dnf 本身的配置和源配置

## 3.1 dnf 配置

本系统默认的配置如下：

```
cat /etc/dnf/dnf.conf
[main]
gpgcheck=1
installonly_limit=3
clean_requirements_on_remove=True
best=True
skip_if_unavailable=False
zchunk=False
```


除了默认的配置之外，用户也可以自己调整 dnf 配置，可以通过 `man`

命令查询

```
man dnf.conf
```


## 3.2 repo 源配置

上文已经列出了环境中默认的 repo 配置，常见的配置说明如下，用户可按需调整

参数 |
值类型 |
默认值 |
说明 |
|---|---|---|---|
| name | string | repo 源的名字 | |
| baseurl | list | 无 | repo 源的 URL 列表 |
| priority | integer | 无 | repo 源的优先级，取值范围 0 - 99，值越小优先级越高 |
| gpgcheck | boolean | 1 | 是否进行 GPG 校验 |
| installonly_limit | integer | 3 | 允许被并行安装的软件包数量 |
| clean_requirements_on_remove | boolean | True | 是否在卸载软件包时同时卸载没有被其他软件包使用的依赖 |
| best | boolean | True | 是否在安装软件包时安装最高版本，如果无法安装则失败。（指定安装包的依赖安装时不受此参数控制） |
| skip_if_unavailable | boolean | False | 安装时会跳过不可用的源 |
| zchunk | boolean | False | 是否通过 zchunk 格式压缩 repo 的元数据 |

# 4 常用包管理命令

## 4.1 安装/卸载/下载软件包

安装源中的软件包

```
dnf install -y pkgname
```


安装用户自己编译的 rpm 包文件

```
dnf localinstall -y pkgname.rpm
```


软件包卸载

```
dnf remove -y pkgname
```


下载源中的 rpm 包

```
dnf download pkgname
```


## 4.2 软件包升/降级

将已安装的 rpm 包升级

```
dnf upgrade pkgname
```


将已安装的 rpm 包降级

```
dnf downgrade pkgname
```


## 4.3 软件包信息查询

列出当前环境所有已安装软件包

```
rpm -qa
```


此命令会列出系统全量安装的包列表，因此一般配合 grep 命令使用

查询指定软件包信息

```
rpm -qi pkgname
```


查询repo源中的软件包，会从包名完全匹配、名字和简介匹配、名字模糊匹配、简介模糊匹配四个方面查找指定字段。

```
dnf search pkgname
```


通过repo源查询指定软件包的依赖关系

```
dnf repoquery --whatrequires pkgname
dnf repoquery --requires pkgname
```


查询repo源中指定软件包信息

```
dnf info pkgname
```


查询源中哪些包提供了指定文件或能力

```
dnf whatprovides name
```


# 5 常见报错处理

## 5.1 install 失败

具体日志大致如下， 完整如下图所示

```
You have enabled checking of packages via GPG keys. This is a good thing.
However, you do not have any GPG public keys installed. You need to download
the keys for packages you wish to install and install them.
You can do that by running the command:
rpm --import public.gpg.key
```


此问题多发生于配置额外源的时候，可以编辑 `/etc/yum.conf`

文件，将 gpgcheck 选项改为 `gpgcheck=0`

即可

## 5.2 Database environment version mismatch

详细报错信息如下

```
error: db5 error(-30969) from dbenv->open: BDB0091 DB_VERSION_MISMATCH: Database environment version mismatch
error: cannot open Packages index using db5 - (-30969)
error: cannot open Packages database in /var/lib/rpm
```


多见于强制结束 yum 导致 rpm 数据库损坏，处理策略为：

1 删除损坏的 rpmdb 文件

```
rm -f /var/lib/rpm/__**
```


```
rpm --rebuilddb
```


```
yum clean all
```


如此即可

## 5.3 容器部署时dnf install失败

现象如下：

且配置了 dns 仍无法解决，dig 命令显示 `Operation not permitted`


如果有如上现象，则可能与 dnf 包管理无关，请确认 host 的 doker 版本与 docker image 中 glibc 的版本，如果 docker image 的 `glibc > 2.34`

，则需使 host 的 `docker >= 20.10.9`


## 5.4 软件包冲突

如果不同的软件包提供了相同的能力或者相同的文件，则会产生软件包冲突，这是正常现象，我们以 mariadb 和 mysql 为例：

```
rpm -qa | grep mariadb
mariadb-connector-c-config-3.3.1-4.ocs23.noarch
mariadb-common-10.5.16-4.ocs23.x86_64
mariadb-connector-c-3.3.1-4.ocs23.x86_64
mariadb-10.5.16-4.ocs23.x86_64
dnf install -y mysql
Last metadata expiration check: 3:01:01 ago on Fri 26 May 2023 01:02:52 PM CST.
Error:
Problem: problem with installed package mariadb-10.5.16-4.ocs23.x86_64
- package mariadb-10.5.16-4.ocs23.x86_64 conflicts with mysql provided by mysql-8.0.32-3.ocs23.x86_64
- package mysql-8.0.32-3.ocs23.x86_64 conflicts with mariadb provided by mariadb-10.5.16-4.ocs23.x86_64
- conflicting requests
(try to add '--allowerasing' to command line to replace conflicting packages or '--skip-broken' to skip uninstallable packages or '--nobest' to use not only best candidate packages)
```


由于 mariadb 和 mysql 提供了相近的数据库能力，因此会产生 conflicts，用户需要自行斟酌保留哪个，如果需要 mysql，则要在已知影响的情况下移除已安装的 mariadb。

另外，当源里面存在多个待安装的冲突包版本时（如下有多个版本的 mysql），冲突日志会有所不同，处理方式相同。

```
dnf prov mysql
Last metadata expiration check: 0:15:01 ago on Fri 26 May 2023 11:51:52 PM CST.
mysql-8.0.32-2.ocs23.x86_64 : MySQL client programs and shared libraries
Repo : build0
Matched from:
Provide : mysql = 8.0.32-2.ocs23
mysql-8.0.32-3.ocs23.x86_64 : MySQL client programs and shared libraries
Repo : build0
Matched from:
Provide : mysql = 8.0.32-3.ocs23
dnf install -y mysql
Last metadata expiration check: 0:14:33 ago on Fri 26 May 2023 11:51:52 PM CST.
Error:
Problem: problem with installed package mariadb-10.5.16-4.ocs23.x86_64
- package mariadb-10.5.16-4.ocs23.x86_64 conflicts with mysql provided by mysql-8.0.32-3.ocs23.x86_64
- package mysql-8.0.32-3.ocs23.x86_64 conflicts with mariadb provided by mariadb-10.5.16-4.ocs23.x86_64
- cannot install the best candidate for the job
(try to add '--allowerasing' to command line to replace conflicting packages or '--skip-broken' to skip uninstallable packages or '--nobest' to use not only best candidate packages)
```