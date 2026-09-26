source: https://docs.opencloudos.org/en/release/v8.8/

# OpenCloudOS v8.8 版本说明

## 概述

2021年12月22日，开源操作系统社区OpenCloudOS正式宣布成立，腾讯及宝德、北京初心、北京红旗、飞腾、浪潮、龙芯中科、OPPO、先进开源、中电科申泰、中科方德、兆芯等20余家操作系统生态厂商及用户成为首批创始单位。

开源操作系统社区OpenCloudOS是完全中立、全面开放、安全稳定、高性能的操作系统及生态。成立之初，OpenCloudOS就决定成为完全开放中立的开源社区，并已经通过开放原子开源基金会的TOC评议，确认接受社区项目捐赠。后续在基金会托管和监督下，OpenCloudOS将以标准开源社区模式运作，与社区参与单位共治共建。

操作系统是核心基础软件，其重要性已是业界共识。但对相关厂商及个人用户来说，当前供应链的潜在风险已不容小觑，2021年底，业界主流的操作系统软件CentOS将停止维护，这使得大量用户陷于安全风险中。在此背景下，腾讯与合作伙伴共同倡议发起操作系统开源社区OpenCloudOS。

作为国产开源操作系统社区，OpenCloudOS沉淀了腾讯及多家厂商在软件和开源生态的优势，在云原生、稳定性、性能、硬件支持等方面均有坚实支撑，可以平等全面地支持所有硬件平台。

OpenCloudOS V8版本用户态保持与RHEL 8版本100%二进制兼容，内核采用OpenCloudOS社区研发的5.4 LTS版本，提供更优性能。

## 下载链接

下载 OpenCloudOS V8.8，请访问：
- [https://mirrors.opencloudos.tech/opencloudos/8.8/](https://mirrors.opencloudos.tech/opencloudos/8.8/)

## 主要更新


### 1.安全性

**内核中的 FIPS 模式**设置已被调整，以符合联邦信息处理标准(FIPS) 140-3。这个更改对许多加密算法、功能和密码套件引入了严格的设置。**Libreswan**IPsec 实现已 rebase 到版本 4.9。- 使用
软件框架，您现在可以过滤 RPM 数据库。`fapolicyd`

**OpenSCAP**安全合规工具已 rebase 到版本 1.3.7。**Rsyslog**TLS 加密的日志现在支持多个 CA 文件。`systemd-socket-proxyd`

服务现在因为 SELinux 策略的更新在自己的 SELinux 域中运行。

### 2.动态编程语言、网页和数据库服务器

以下应用程序流的后续版本现在可用：

-
**Python 3.11** -
**nginx 1.22** -
**PostgreSQL 15**

以下组件已升级：

-
**Git**升级到版本 2.39.1 -
**Git LFS**升级到版本 3.2.0

### 3.编译器和开发工具

#### 更新了性能工具和调试器

OC 8.8 中更新了以下性能工具和调试器：

-
**Valgrind 3.19** -
**SystemTap 4.8** -
**elfutils 0.188**

#### 更新了性能监控工具

OC 8.8 中更新了以下性能监控工具：

-
**PCP 5.3.7** -
**Grafana 7.5.15**


#### 更新了编译器工具集

OC 8.8 中更新了以下编译器工具集：

-
**GCC Toolset 12** -
**LLVM Toolset 15.0.7** -
**Rust Toolset 1.66** -
**Go Toolset 1.19.4**


#### 内核更新

OC 8.8 中更新内核版本：

-
**多个驱动程序版本更新** -
**修复了多个x86, ARM, FS, KVM等模块的缺陷** -
**添加了多个飞腾平台的驱动支持** -
**单独提供了intel SPRCPU支持内核**


#### OC8 中的 Java 实现

OC 8 AppStream 软件仓库包括：

-
`java-17-openjdk`

软件包，提供 OpenJDK 17 Java 运行时环境和 OpenJDK 17 Java 软件开发组件。 -
`java-11-openjdk`

软件包，提供 OpenJDK 11 Java 运行时环境和 OpenJDK 11 Java 软件开发组件。 -
`java-1.8.0-openjdk`

软件包，提供 OpenJDK 8 Java 运行时环境和开源 JDK 8 Java 软件开发组件。


## 漏洞管理

OpenCloudOS的bug追踪系统：

使用OpenCloudOS 发行版本遇到和任何问题，诚挚欢迎社区的用户、开发者朋友多提宝贵建议。我们还有很多需要改进和完善的地方。

## 源代码

所有 OpenCloudOS 8 的源代码均托管在gitee：

## 致谢

感谢社区每位伙伴成员的努力，参与和支持。没有你们辛勤的付出，我们不可能在这么短时间里发布一个完善的发行版本。