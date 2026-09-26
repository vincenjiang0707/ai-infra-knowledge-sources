source: https://docs.opencloudos.org/faq/

# 常见问题

**Q: OpenCloudOS 各发行版生命周期如何规划的？**

**A** : 生命周期规划如下表所示：

| 社区发行版本（OC version） | 发布日期（Release date） | 完整支持至（Full updates） | 维护支持至（Maintenance updates） |
|---|---|---|---|
| OpenCloudOS V7 | 2023年12月 | 2024年12月 | 2025年12月 |
| OpenCloudOS V8 | 2022年1月26日 | 2027年5月31日 | 2029年5月31日 |
| OpenCloudOS V9 | 2023年3月31日 | 2030年3月31日 | 2033年3月31日 |

**Q: OpenCloudOS 和软硬件的兼容性做的如何？**

**A** : OpenCloudOS 7 和 OpenCloudOS 8 的用户态分别与 CentOS 7 和 CentOS 8 100% 兼容，OpenCloudOS 9 为社区全自研版本，从内核到软件包均为自主选型和自主维护，BaseOS 和 Appstream 仓库 3000+ 包，OpenCloudOS 9 的 EPOL9 未来会扩展至 6500+ ，软件仓库总体数量达到 1W+，确保为系统提供丰富的软件生态，提升 OpenCloudOS 9 的易用性和好用性。

EPOL 仓库地址：https://mirrors.opencloudos.tech/epol/9/

同时，OpenCloudOS 社区会不定期且持续更新软件和硬件兼容性列表，同时我们有一套标准社区适配流程。截至 2024 年 6 月，OpenCloudOS 兼容适配硬件 904 款、开源软件 37401 款、商业软件 343 款，认证生态覆盖 177 个合作品牌。

软件兼容性可参考： https://docs.opencloudos.org/adaptation/adaptation_sw/ 以及 https://docs.opencloudos.org/adaptation/adaptation_oss/

硬件兼容性可参考 https://docs.opencloudos.org/adaptation/adaptation_hw/

生态认证流程详情参见 https://docs.opencloudos.org/adaptation/adaptation_process/

**Q：OpenCloudOS 安装推荐配置是怎样的？**

**A** ：
磁盘空间：推荐大于 50 GB
内存：推荐大于 4 GB
版本编译支持 CPU v2 微架构指令，因此需要在支持 v2 及以上微架构的物理机、虚拟机部署
使用 docker 部署时，版本需要 > 20.10.9，如果小于等于上述版本，会出现 dnf install 无法解析等涉及 clone 系统调用的问题

**Q：OpenCloudOS 8 里是否预置了 epel 的源，是默认打开的吗？**

**A** ：OpenCloudOS 8 可以通过 Yum 源安装 epel-release 包来开启 epel 源。
要在 OpenCloudOS 8 及其衍生发行版上安装 EPEL 软件仓库，您可以按照以下步骤操作：

1、打开终端，输入以下命令以安装EPEL软件仓库：

`sudo dnf install epel-release`


2、安装完成后，更新软件包缓存：

`sudo dnf makecache`


**Q：在 OpenCloudOS 8/9 里无法通过 yum 安装（缺少）xxx软件包，请问如何解决？**

**A** ：

● OpenCloudOS 8 提供的包可以在 https://mirrors.tencent.com/opencloudos/8/ 下各目录中进行查找；如果找不到建议安装 epel 源，sudo dnf install epel-release， 然后 `dnf search PackageName`

来查找；

● OpenCloudOS 9 提供的包可以在 https://mirrors.tencent.com/opencloudos/9/各目录中进行查找；如果找不到建议安装 epol 源（epol 源是 OpenCloudOS 社区提供的软件仓库，注意拼写）`sudo dnf install epol-release`


以上方式如果都没有找到，那很可能这个包的开源协议或者因为其他的原因 OpenCloudOS 社区无法官方分发，请开发者、用户在相关软件项目的官网获得支持。

**Q：代码库找不到源码包怎么办？**

**A** ：

● 源代码的 git 仓库地址：

```
## 这里包含 OC 9 版本和 EPOL 9 版本所有的源码项目名称
https://gitee.com/opencloudos-stream/
```


● 也可以在官方包构建系统上去 search

```
https://build.opencloudos.tech/koji/index
```


**Q：OpenCloudOS 系统里怎么打系统漏洞补丁呢？**

**A** ：可以根据漏洞编号，查找影响的软件包，通过 dnf 或 yum 命令升级相应的软件包即可。

可以查看社区的漏洞管理机制和安全公告，了解您想要获取的漏洞补丁编号及情况：

OpenCloudOS 安全公告：https://security.opencloudos.tech/cve/oc8.xml

关于 OpenCloudOS 漏洞管理机制：https://www.opencloudos.org/ospages/community/vulnerability

**Q：请问 M1 芯片的 MAC 安装 OpenCloudOS 8（aarch64）时会出现闪退，是因为不支持吗？**

**A** ：闪退原因是因为 CentOS 8 的 aarch64 的版本里面，操作系统内核 pagesizemac 超过 M1 操作系统底层支持的最大 pagesize 规格导致的。解决闪退问题，需要在安装过程加载内核时将「initrd.gz」和「vmlinuz」修改为 4K 的参数，同时加载安装时加载的 install.img，以及进入安装系统以后内核 rpm 包都调整参数，上面的步骤完成以后，打的新的 iso 就是可以正常在 M1 下运行的 ISO 了。

定制 iso 下载链接：https://pan.baidu.com/s/1-UBAAco0GQTDKLrQtl8IMA?pwd=x9bp 提取码: x9bp

**Q：SCP 命令在 OpenCloudOS 9 系统出现 bug 是什么原因？**

**A** ：目前因 SCP 协议已有几十年的历史，并带来了许多的安全风险和问题。所以 OpenCloudOS 9 中，OpenSSH 最重要的安全变化之一是 SCP 协议被废弃。

目前已实施的更改如下： 1、SCP 命令默认使用的是 SFTP 协议进行文件传输（SFTP协议涵盖大部分 SCP 的用法，所以切换SFTP协议是有意义的）。 2、可添加 -O 参数强制使用 SCP 协议。 3、在系统上可以完全禁用 SCP 协议。如果系统上存在 /etc/ssh/disable_scp 文件，则无法使用 SCP 协议。

**Q：OpenCloudOS 9 支持的 Python 版本是什么？为什么修改 Python 版本会导致 yum 报错？**

**A** ：OpenCloudOS 9 默认 systemd 为 Python 3.11 版本，可通过软件源安装 Python 3.12 版本，yum/dnf 的运行需要 Python 3.11 环境的支持。
如需运行其他 Python 版本建议使用 Python 虚拟环境。

**Q：新支点超凡桌面在 OpenCloudOS 上如何下载或使用？**

**A** ：超凡桌面（EX-NDE）是由新支点操作系统与 OpenCloudOS 社区共同打造的，一个超融合轻量级桌面环境，目前支持 OpenCloudOS 8，后续将支持 OpenCloudOS 9。用户可以在 v8 版本上通过如下命令下载和启用：

```
dnf install exnde-release
dnf groupinstall exnde
systemctl enable sddm
systemctl set-default graphical.target
```


**Q：OpenCloudOS U 盘安装，启动U盘制作方式和工具推荐**

**A** ：如果您熟悉 linux 平台，熟练使用 dd 命令，我们建议您是 dd 命令的方式制作。
大多数情况下，社区建议您在图形桌面系统上使用 etcher 工具制作：Linux 图形系统 、macOS 或者 Windows 建议下载使用 https://www.balena.io/etcher/ 工具制作引导盘。