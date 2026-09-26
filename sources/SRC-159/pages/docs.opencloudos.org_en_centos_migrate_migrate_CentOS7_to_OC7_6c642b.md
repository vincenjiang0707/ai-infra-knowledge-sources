source: https://docs.opencloudos.org/en/centos_migrate/migrate_CentOS7_to_OC7/

# CentOS7迁移到OpenCloudOS7

CentOS 7 迁移到 OpenCloudOS 7.9

### 操作场景

CentOS 官方计划停止维护 CentOS Linux 项目，CentOS 8 及 CentOS 7 维护情况如下表格。如需了解更多信息，请参见 [CentOS 官方公告](https://blog.centos.org/2020/12/future-is-centos-stream/?spm=a2c4g.11174386.n2.3.348f4c07hk46v4)。

| 操作系统版本 | 停止维护时间 | 使用者影响 |
|---|---|---|
| CentOS 8 | 2022年01月01日 | 停止维护后将无法获得包括问题修复和功能更新在内的任何软件维护和支持。 |
| CentOS 7 | 2024年06月30日 | 停止维护后将无法获得包括问题修复和功能更新在内的任何软件维护和支持。 |

针对以上情况，若您正在使用 CentOS 实例，则可参考本文替换为 OpenCloudOS。

### 版本说明

**源端主机支持操作系统版本**：

- 支持 CentOS 7 系列操作系统版本：
- CentOS 7.1 64位、CentOS 7.2 64位、CentOS 7.3 64位、CentOS 7.4 64位、CentOS 7.5 64位、CentOS 7.6 64位、CentOS 7.7 64位、CentOS 7.8 64位、CentOS 7.9 64位。


**目标主机建议操作系统版本**：

- CentOS 7 系列建议迁移至 OpenCloudOS 7.9 。
- CentOS 8 系列建议迁移至 OpenCloudOS 8 。
**注意：**CentOS 7.2、CentOS 7.3 公共镜像可能默认包含了 32 位的软件包，需要手动移除后再执行升级操作。

### 注意事项

- 目前仅支持 X86_64 架构。
- 以下情况不支持迁移：
- 安装了图形界面。
- 安装了 i686 的 rpm 包。

- 对于安装了 i686 的 rpm 包的系统，可通过下列方式之一处理：
- 创建快照，卸载 32 位的软件包，执行迁移命令。

- 以下情况可能会影响业务在迁移后无法正常运行：
- 业务程序安装且依赖了第三方的 rpm 包。
- 业务程序依赖于某个固定的内核版本，或者自行编译了内核模块。
- 迁移后的目标版本是 5.4 的内核。该版本较 CentOS 7 及 CentOS 8 的内核版本更新，一些较旧的特性在新版本可能会发生变化。建议强依赖于内核的用户了解所依赖的特性。
- 业务程序依赖某个固定的 gcc 版本。
- 目前 OpenCloudOS 7.9 默认安装 gcc 4.8.5。

- 迁移结束后，需重启才能进入 OpenCloudOS 内核。
- 迁移不影响数据盘，仅 OS 层面的升级，不会对数据盘进行任何操作。

### 资源要求

- 空闲内存大于 4GB。
- 系统盘剩余空间大于 20GB。

### 操作步骤

#### 迁移准备

- 迁移操作不可逆，为保障业务数据安全，建议您在执行迁移前备份系统盘数据。
- 检查并手动卸载 i686 的 rpm 包。

#### 执行迁移

- 执行以下命令，安装 Python 3

```
yum install -y python3
```


- 执行以下命令，获取迁移工具。

```
wget https://mirrors.opencloudos.tech/opencloudos/7/migration/x86_64/os/Packages/migrate2opencloudos-0.7-1.el7.noarch.rpm
```


- 执行以下命令，安装迁移工具。该命令会在 /usr/sbin 下创建 migrate2opencloudos.py。

```
rpm -ivh migrate2opencloudos-0.7-1.el7.noarch.rpm
```


- 执行以下命令，开始迁移。

```
python3 /usr/sbin/migrate2opencloudos.py -v 7.9
```


-
重启。

-
检查迁移结果。

6.1 执行以下命令，检查 os-release。

返回如下图所示信息：`cat /etc/os-release`

6.2 执行以下命令，检查内核。

返回如下图所示信息(内核默认为 yum 最新版本，请以您的实际返回结果为准，本文以图示版本为例。:)`uname -r`

6.3 执行以下命令，检查 yum。

返回如下图所示信息：`yum makecache`