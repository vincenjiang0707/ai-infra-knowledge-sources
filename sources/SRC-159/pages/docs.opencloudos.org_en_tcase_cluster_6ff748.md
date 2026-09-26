source: https://docs.opencloudos.org/en/tcase/cluster/

OpenCloudOS Documentation
新增集群
中文
English
Initializing search
Gitee
About
Releases
Guide
Adaptation
Migration
Security
FAQ
Test
Contributing
OpenCloudOS Documentation
Gitee
About
About
组织架构
社区准则
社区SIG
社区SIG
SIG总览
镜像源地址
邮件列表
Releases
Releases
OpenCloudOS 版本介绍
OpenCloudOS v8.8发行说明
OpenCloudOS v8.6发行说明
OpenCloudOS v9.0发行说明
OpenCloudOS v9.2发行说明
OpenCloudOS v9.4发行说明
OpenCloudOS v9.6发行说明
OpenCloudOS Stream 发行说明
OpenCloudOS Stream 发行说明
OpenCloudOS Stream 23 发行说明
OCS23 Loongarch64 版本发行说明
Guide
Guide
OpenCloudOS 8 用户文档
OpenCloudOS 8 用户文档
快速入门
基础配置
系统管理
内核更新
系统状态监控
安全加固
存储管理
存储管理
文件系统
逻辑卷管理
可用的存储选项
网络管理
网络管理
网络使用指南
导入镜像到云
导入镜像到云
导入镜像到华为云
OpenCloudOS 9/Stream 用户文档
OpenCloudOS 9/Stream 用户文档
OC9 快速入门
安装启动指南
安装启动指南
PXE 无人值守系统安装指南
使用Anaconda_ISO镜像安装
使用虚拟机镜像安装
使用容器镜像安装
桌面安装
系统引导管理
UEFI引导启动项管理
initramfs制作
plymouth(系统启动动画)
安全启动
系统管理指南
系统管理指南
本地化管理
用户管理
软件包管理
日志管理
系统和服务管理
系统和服务管理
systemd工具使用及服务管理
dbus机制和使用
udev机制和使用
资源控制管理
资源控制管理
cgroup使用
网络管理指南
网络管理指南
网络配置指南
网络诊断指南
OpenSSH使用指南
DHCP服务配置指南
NTP配置指南
邮件服务使用指南
存储和文件系统管理指南
存储和文件系统管理指南
磁盘和分区管理
文件系统管理
逻辑卷管理
RAID 管理
网络存储管理
开发与调测指南
开发与调测指南
GCC开发指南
LLVM/Clang
GO开发指南
RUST开发指南
Python开发指南
Perl开发指南
Java开发指南
dotnet开发指南
Luajit开发指南
QT开发指南
Glibc可调参数使用指南
kdump/crash
用户态coredump
ftrace
perf使用指南
eBPF及工具bcc和bpftrace
容器和虚拟化指南
容器和虚拟化指南
容器用户指南
虚拟化用户指南
OpenStack Wallaby 版本部署指南
OpenStack Zed 版本部署指南
Kubernetes部署指南
机密计算-海光用户指南
导入镜像到云
导入镜像到云
导入镜像到阿里云
典型应用部署
典型应用部署
MySQL服务器搭建指南
MariaDB服务器搭建指南
PostgreSQL服务器搭建指南
SQLite使用指南
HA(PCS)部署文档
Hadoop使用指南
MariaDB集群部署搭建指南
OC AI镜像
OC AI镜像
AI镜像概述
AI镜像列表
基于OC AI的最佳实践
基于OC AI的最佳实践
AI应用实践
AI应用实践
vLLM大模型部署指南
SGLang大模型部署指南
PyTorch大模型部署指南
TensorFlow大模型部署指南
PaddlePaddle大模型部署指南
TensorRT-LLM大模型部署指南
Transformers+Deepspeed大模型部署指南
Youtu-agent大模型部署指南
WeKnora大模型部署指南
Browser-use部署指南
GPU部署实践
GPU部署实践
NVIDIA环境
AMD环境
海光环境
沐曦环境
昇腾环境
Adaptation
Adaptation
Adaptation Process
软件兼容性测试指标
硬件兼容性测试指标
Adaptation Lists
Adaptation Lists
Hardware Adaptation
Commercial Software Adaptation
OpenSouce Software Adaptation
Adaptation FAQ
Migration
Migration
CentOS停服背景与应对方案
CentOS8迁移到OpenCloudOS8
CentOS7迁移到OpenCloudOS8
CentOS7迁移到OpenCloudOS7
OpenCloudOS8升级OpenCloudOS9
迁移与升级常见问题FAQ
Security
Security
安全事件处置说明
镜像签名验证指南
漏洞数据API文档
FAQ
Test
Test
一、项目管理
二、用例管理
二、用例管理
编写用例
提取用例
导入用例
用例集
三、执行环境
三、执行环境
新增节点
新增集群
四、任务管理
四、任务管理
创建任务
执行任务
Contributing
Contributing
贡献须知
如何参与文档贡献
如何参与文档贡献
文档库贡献指南
Documentation format guide
如何参与代码贡献
如何参与代码贡献
OpenCloudOS Stream
OpenCloudOS Stream
0. 文档说明
1. 软件包管理原则
2. 软件包权限管理
3. 编译构建指南
3. 编译构建指南
编译构建指南
ocspkg使用指南
4. 引入软件包
4. 引入软件包
新增软件包指南
软件包打包指导
5. 维护软件包
5. 维护软件包
CI 门禁流程
门禁排查手册
6. 开发工具
6. 开发工具
跟踪社区 Release
跟踪社区 Commit
依赖分析工具
7. 衰退与删除软件包
OpenCloudOS
OpenCloudOS
OpenCloudOS 社区版本贡献指南
Kernel Development Guide
系统开发文档
系统开发文档
内核驱动移植开发
应用移植开发参考文档
API文档
Contribution License Agreement
新增集群
创建集群后，任务可以在多个节点上执行。 集群可以按照标签自动关联节点，也可以手动添加特定节点
Back to top