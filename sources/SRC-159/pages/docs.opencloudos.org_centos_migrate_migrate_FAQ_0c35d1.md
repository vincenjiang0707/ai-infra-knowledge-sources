source: https://docs.opencloudos.org/centos_migrate/migrate_FAQ/

# 迁移与升级常见问题FAQ

**Q: 从CentOS7 到 OpenCloudOS 8/9是否支持跨大版本迁移?**

**A** :目前支持从CentOS7到OpenCloudOS8的迁移，详细流程请[访问该篇文档](https://docs.opencloudos.org/centos_migrate/migrate_CentOS7_to_OC8/#3)

*备注说明：但由于二者在内核、基础软件包和工具链方面都有较大变化，尤其用户态方面不兼容，因此直接迁移仍会存在风险，官方建议在业务环境允许的情况下，跨大版本升级最好采用重新安装部署新OS及二进制包重编译的方式，从而降低迁移风险和失败率。*

**Q: 使用migrate2opencloudos或leapp工具迁移到OpenCloudOS 8版本，是默认迁移到该版本下当前最高版本吗？是否可以指定迁移至某个小版本（例如8.6/8.8）？**

**A** :如果从CentOS 8 迁移到 OpenCloudOS 8，默认迁移到该版本下最高版本。如果从CentOS 7迁移到OpenCloudOS 8，目前暂时仅支持迁移到 8.6 版本，如需升级至 8.8 或 8.10，可在 /etc/yum.repos.d/OpenCloudOS.repo 中设置 baseurl 的 `$releasever`

为 8.8 或 8.10。
例如： `https://mirrors.opencloudos.tech/opencloudos/8.10/BaseOS/x86_64/os/`

（注：baseurl 格式为

**Q: 跨大版本迁移存在哪些风险？**

**A** :OpenCloudOS 8 相比 CentOS 7，无论在内核，还是用户态软件包方面，都有版本更新，可能会存在一些兼容性风险。分析认为迁移面临的关键问题和风险可能有：

**1. 硬件与新 OS 兼容性问题**

CentOS 7 到 OpenCloudOS 8的迁移，由于内核、基础软件包和工具链的较大变化，可能存在兼容性问题。例如，某些依赖于特定内核特性或硬件驱动的应用程序可能无法在TencentOS3上正常运行。

**2. 已有软件是否可以在新系统运行，包括软件安装与功能是否存在问题**

**3. 已经做过的相关配置是否可以继承到新 OS**

尽管迁移工具尽量保持系统配置不变，但在迁移过程中仍有可能出现配置变更，需要在迁移后进行验证和调整。

**4. 应用系统依赖的基础软件包和三方库是否在新系统中存在且无冲突运行。比如可能会存在部分不支持迁移的安装包，这里分几种情况：**

1）部分特定的包在迁移过程中会终止迁移进程。例如不支持迁移的模块相关的包有：


idM服务器功能相关的包，这部分包括ipa相关的包，389-ds相关的包，和softhsm相关的包

高可用服务器功能相关的包，这部分包括mvapich2相关的包

制作安装包用的安装包，包括pki相关的安装包

2） 存在与之对应的新版本或者新旧版本之间存在冲突，例如Debug和Devel的包

3）重启之后会影响新系统生成的安装包，如lvm2-cluster，acpica-tools，mksh


**迁移实施需要注意以下几点：**

-
1）可能对现网业务有影响，请提前规划时间窗口和资源。

-
2）迁移工具不支持回滚，迁移失败无法恢复到迁移初始状态，迁移前务必做好系统备份和现网数据备份。

-
3）现网业务建议专业人员实施迁移，迁移建议灰度执行。

-
4）迁移后建议进行功能、稳定性、性能、压力等测试，保障迁移前后业务的连续性和稳定性。


**Q: 就地迁移失败是否可回滚？**

**A** :迁移工具不支持回滚，迁移失败无法恢复到迁移初始状态，迁移前务必做好系统备份和现网数据备份。

**Q: 怎么从OpenCloudOS 8.8升级到该系列下的最新小版本？**

**A** :在OC8的系列版本中，缺省情况下用户执行yum update就可以使用最新版本。执行命令

`yum upgrade opencloudos-release`

并通过
`cat /etc/opencloudos-release`

可验证是否已升级到最新版本。

**Q: 是否支持 OpenCloudOS 8 直接升级到 OpenCloudOS 9？**

**A** :目前我们推荐的是通过Leapp工具实现从OpenCloudOS 8到OpenCloudOS 9的跨版本升级方案，并且本方案支持用户高效对多台 OpenCloudOS 8.x 机器进行批量升级。
详细方案可访问[该篇指导文档](https://docs.opencloudos.org/centos_migrate/OC8toOC9/)。

**Q: 如果现在使用OpenCloudOS 9.2，是否支持回退至OpenCloudOS 9？**

**A** :通常情况下，不建议用户将新版本操作系统回退到旧版本，一方面旧版本不一定能支持现有应用和服务，另一方面回退后的系统配置不一定兼容，需要进行详细的风险评估。