source: https://docs.opencloudos.org/User%20Guide/Hygon_Devkit/

# hygon-devkit

## 介绍

hygon-devkit是海光平台的开发套件，包括海光安全功能和性能优化两大块。其中安全部分有机密计算CSV、可信计算、密码技术HCT；性能优化有编译器、高性能计算库、内存库、性能分析工具hpt、JDK等。

## 开发套件二进制下载

由于二进制文件较多，我们将二进制保存在了SFTP服务器，以供下载。

### SFTP访问方法

下面以`FileZilla`

为例进行说明，使用其他如`winscp`

等`sftp工具`

都可以实现相同的功能。

#### 下载安装FileZilla

从[FileZilla - The free FTP solution](https://filezilla-project.org/)官网，下载对应的Windows、Linux、MAC的客户端并安装

#### 连接到海光SFTP服务器

如图所示，输入`主机`

、`用户名`

、`密码`

信息后，点击`快速连接`

即可

```
主机：sftp://58.241.21.90
用户名：p_devkit
密码：EQS7vH&t5#
```


#### 下载文件到本地

左侧选择想要下载到的目录，右侧找到想要下载的文件，右键选择下载。如图以`hag`

为例进行下载。

### SFTP二进制目录说明

```
├── 4.0 ---- devkit二进制的根目录
│ ├── 2025-01-01 ---- 2025-01-01是一个特殊版本，保存了最为完整的二进制包，但版本较老
| | ├── compiler
| | ├── hml
| | └── hjdk
| ├── 2025-04-20 ---- 2025-04-20开始，是每周自动化测试通过的版本，但是二进制不全，陆续添加中
| └── 2025-04-26 ---- 以2025-04-26为例，进行展开说明
| ├── ISO ---- 这里保存一个已经集成了海光devkit二进制的ubuntu ISO
| | ├── ubuntu-18.04.4-server-ss-20250426.iso
| | └── ubuntu-18.04.4-server-ss-20250426.iso.md5
| └── Packages ---- 这里保存所有的二进制文件
| ├── KylinV10SP3 ---- 与操作系统有依赖的二进制存放在各操作系统对应的目录中
| ├── OpenEuler23.09
| ├── Ubuntu18.04
| ├── hag ---- 与操作系统无依赖的版本，保存在Packages根目录
| ├── hct-2.1.0-2025-0427-release.x86_64.deb
| ├── hct-2.1.0-2025-0427-release.x86_64.rpm
| └── ovmf.tar.gz
└── latest ---- 指向最新版本的软链接，当前指向4.0/2025-04-26
```


## 重要开发套件下载路径

| 套件 | SFTP路径 |
|---|---|
| hgcc | /hygon-devkit/4.0/2025-01-01/compiler/hgcc/1.3.6/hgcc-1.3.6-release.x86_64.rpm |
| hcc1plugin | /hygon-devkit/4.0/2025-01-01/compiler/hgcc/1.3.6/hcc1plugin-1.3.6-release.x86_64.rpm |
| hceph | /hygon-devkit/4.0/2025-01-01/hceph/1.1.0/hceph-1.1.0.rpm |
| hc | /hygon-devkit/4.0/2025-01-01/hc/1.0.0/libhc-1.0.0.rpm |
| hjdk | /hygon-devkit/4.0/2025-01-01/hjdk/hjdk-8.0.3/hjdk-1.8.0-release.x86_64.rpm |
| hjemalloc | /hygon-devkit/4.0/2025-01-01/alloc-libs/libhjemalloc-1.0.0-1.x86_64.rpm |
| htcmalloc | /hygon-devkit/4.0/2025-01-01/alloc-libs/libhtcmalloc-1.0.0-1.x86_64.rpm |