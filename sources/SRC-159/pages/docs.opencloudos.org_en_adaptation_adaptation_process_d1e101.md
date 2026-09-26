source: https://docs.opencloudos.org/en/adaptation/adaptation_process/

# OpenCloudOS 社区适配流程手册

OpenCloudOS 作为产品底座支撑海量业务运行，具备完整的适配生态认证体系，在北向软件适配数据库管理系统、中间件、虚拟化云平台、行业应用、AI SDK 等类别产品，在南向硬件适配整机、CPU、GPU/NPU/AI加速卡、网卡、硬盘等类别产品。

欢迎软硬件厂商加入 OpenCloudOS 社区和完成产品适配，帮助产品稳定、正常运行在 OpenCloudOS 操作系统之上，同时可在适配的基础上探索更多交流与合作。

合作接口人：陈晴敏（qingmin0623）


适配与 kernel SIG、Testing SIG、Stream SIG 等小组共同协作

**适配流程图**


## 提交适配申请

-
提交适配需求


联系适配接口人提交适配需求，包括企业名称、产品名称、官网、适配背景等内容 -
建立专项交流群


评估需求后，由社区工作人员主动与适配厂商建立微信沟通群，在群里对后续流程进行专项交流

## 适配流程介绍

#### 安装操作系统

- OpenCloudOS 9【kernel 6.6、内核及用户态软件均基于 upstream 社区独立演进，自主选型和维护，不依赖第三方发行版，建议优先适配】
- OpenCloudOS 8【kernel 5.4、用户态软件兼容 CentOS 8】

**安装方法**

- 方法一：本地安装（ISO 下载）：
[https://opencloudos.org/ospages/download](http://opencloudos.org/ospages/download) - 方法二：云端部署（CVM 镜像 + yum 更新）：请联系接口人，提供 CVM 云服务器环境测试

#### 适配方式

##### 自主测试

如无需操作系统集成代码，可参考《测试报告模板》开展常规测试，包括安装部署、业务/基础功能、性能、稳定性等用例。

测试报告应记录测试对象及产品版本/型号（含配置）、测试环境及工具、测试项及结果、测试结论、测试时间、测试人员与审核人员等信息。测试用例不少于 10 项，完成后提交适配组审核验证。

- 测试报告模板：
[产品互认证测试模板.docx](https://gitee.com/OpenCloudOS/sig-ecological-adaptation/blob/master/doc/test%20report%20template.docx) - 软件建议测试项目：
[https://docs.opencloudos.org/adaptation/testcase_soft](https://docs.opencloudos.org/adaptation/testcase_soft) - 硬件建议测试项目：
[https://docs.opencloudos.org/adaptation/testcase](https://docs.opencloudos.org/adaptation/testcase) - 开源硬件兼容性测试工具（建议同步附加厂商的测试用例）：
[https://gitee.com/opencloudos-stream/oc-hct](https://gitee.com/opencloudos-stream/oc-hct) - OS_smoke 冒烟测试工具（一套专为操作系统设计的轻量级、自动化冒烟测试工具。主要用于在系统镜像构建完成后，第一时间对系统进行全方位的“健康检查”，快速验证内核、基础系统、驱动、开发工具等关键组件是否正常工作）：
[https://gitee.com/OpenCloudOS/os_smoke](http://gitee.com/OpenCloudOS/os_smoke)

##### 内核补丁、硬件驱动适配

- 方法一：内核集成

如果驱动代码量较小（小于200KB），可提交硬件驱动到 OpenCloudOS 社区 Kernel 仓库，集成进 TencentOS/OpenCloudOS 操作系统。在正式发布前，厂商需支持集成测试验证，验证硬件功能是否正常，输出《测试报告》： - 6.6 内核提交至分支（需适配）：

[https://gitee.com/OpenCloudOS/OpenCloudOS-Kernel/tree/linux-6.6/devel](https://gitee.com/OpenCloudOS/OpenCloudOS-Kernel/tree/linux-6.6/devel) -
5.4 内核提交至分支（请先联系适配 SIG）：


[https://gitee.com/OpenCloudOS/OpenCloudOS-Kernel/tree/linux-5.4/devel](https://gitee.com/OpenCloudOS/OpenCloudOS-Kernel/tree/linux-5.4/devel) -
方法二：独立分发（厂商官网下载或 YUM 源集成）


如果整套驱动包含用户态库及内核驱动模块，且整体代码量较大、源码没有内聚在驱动目录下，建议在官网上架适配 OpenCloudOS 版本的驱动安装包，供使用者直接从官网下载已构建好的驱动；也可单独以 RPM 包形式，集成至操作系统 YUM 源中提供使用。

##### 用户态（核外）系统组件优化补丁

- OpenCloudOS 9 用户态补丁提交至（需适配）：

[https://gitee.com/organizations/opencloudos-stream](https://gitee.com/organizations/opencloudos-stream) - OpenCloudOS 8 用户态补丁提交至（请先联系适配 SIG）：

[https://gitee.com/src-opencloudos-rpms](https://gitee.com/src-opencloudos-rpms)

##### 漏扫工具安全公告数据适配

从 OpenCloudOS 社区提供的[漏洞数据 API ](https://docs.opencloudos.org/security_data_api)获取 OpenCloudOS 8 /OpenCloudOS 9 的安全漏洞修复数据。对于评估为不修复或不涉及的漏洞，API 中的漏洞条目会给出相关说明。
- [OpenCloudOS 社区安全公告 ](https://security.opencloudos.tech/advisories)

- [OpenCloudOS 社区漏洞库](https://security.opencloudos.tech/cves)

##### 其他适配场景

请联系适配 SIG 专项支持

#### 颁发认证证书

##### 补充证书内容

在确认测试通过后，OpenCloudOS 社区会为申请者颁发《兼容认证证书》，在沟通群内提供认证证书模板，申请者请在相应位置填加：

- 正文第一段：适配软件名
- 右上角：公司 logo
- 左下角：公司名称 + 认证时间

适配者完成证书补充后，请回传至沟通群内进行审核


##### 证书、测试报告归档

内容确认无误后，厂商先发起盖章，盖章后回传高清扫描件

#### 官网更新

完成证书双签后，适配组将对报告、证书进行归档管理，并更新产品至官网列表：