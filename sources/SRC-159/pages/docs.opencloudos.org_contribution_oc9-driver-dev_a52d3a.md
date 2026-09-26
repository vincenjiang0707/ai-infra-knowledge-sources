source: https://docs.opencloudos.org/contribution/oc9-driver-dev/

[
](https://gitee.com/opencloudos/Document/edit/master/docs/contribution/oc9-driver-dev.md)
[
](https://gitee.com/opencloudos/Document/raw/master/docs/contribution/oc9-driver-dev.md)
# 基于 OpenCloudOS 9 的内核驱动开发参考文档

## 1、项目简介

本项目旨在保障OpenCloudOS 9各版本的第三方驱动兼容性，核心职责是持续引入对新硬件与外设的支持。我们严格遵循“先上游，后下游”的集成原则：所有驱动均需先合入OpenCloudOS 社区，再回归至 OpenCloudOS 9。

## 2、上游驱动基线

### 2.1、背景

OpenCloudOS 9 作为一款面向企业级应用场景的稳定、高效、安全的操作系统，始终以构建健全的硬件兼容性生态为重要任务。目前，在不同业务场景及下游衍生版本中存在的驱动版本不一致问题，导致了明显的碎片化现象。为了整合各方力量、形成协同效应，OpenCloudOS 9 联合生态合作伙伴，建立了针对主流驱动的统一上游基线，并配套构建了标准化的研发与验证体系。预期将带来以下收益：

**对OpenCloudOS用户而言**：统一的驱动版本将显著简化系统部署与运维中的问题定位和解决流程，减少因驱动差异引发的兼容性问题，提升系统整体的稳定性和可维护性。
**对合作伙伴而言**：合作伙伴将在测试、集成与使用过程中获得统一的技术支持，有利于共同推进驱动功能的完善与问题闭环，增强业务运行的稳定性和可靠性。
**对第三方驱动厂商而言**：一旦完成对OpenCloudOS 9 统一基线的适配，即可兼容其多个下游版本与衍生环境，无需针对不同版本进行重复适配，有助于提升开发效率并扩展硬件生态的覆盖范围。

**2.2、驱动基线**

我们对部分内核驱动进行了更新，使用厂商提供的商业驱动进行替换，如下为驱动基线列表：

**分类** |
**驱动** |
**描述** |
**是否内核原生驱动** |
**商业驱动版本号** |
**仓库** |
| Storage |
megaraid_sas |
Broadcom Raid卡驱动 |
否 |
07.732.03.00 |
[OpenCloudOS-Kernel: OpenCloudOS-Kernel is the kernel of OpenCloudOS release, which has been fully optimized.If you would like to get more information, please read the wiki page of this project. - Gitee.com](https://gitee.com/OpenCloudOS/OpenCloudOS-Kernel/tree/linux-6.6/release/drivers/thirdparty/release-drivers/megaraid_sas) |
|
mpt3sas |
Broadcom HBA卡驱动 |
否 |
51.00.00.00 |
[OpenCloudOS-Kernel: OpenCloudOS-Kernel is the kernel of OpenCloudOS release, which has been fully optimized.If you would like to get more information, please read the wiki page of this project. - Gitee.com](https://gitee.com/OpenCloudOS/OpenCloudOS-Kernel/tree/linux-6.6/release/drivers/thirdparty/release-drivers/mpt3sas) |
|
mpi3mr |
Broadcom 96 系列 Raid&HBA 卡驱动 |
否 |
8.12.1.0.0 |
[OpenCloudOS-Kernel: OpenCloudOS-Kernel is the kernel of OpenCloudOS release, which has been fully optimized.If you would like to get more information, please read the wiki page of this project. - Gitee.com](https://gitee.com/OpenCloudOS/OpenCloudOS-Kernel/tree/linux-6.6/release/drivers/thirdparty/release-drivers/mpi3mr) |
|
smartpqi |
Microchip RAID 卡 &HBA 卡驱动 |
是 |
N/A |
N/A |
|
nvme |
NVMe本地盘驱动 |
是 |
N/A |
N/A |
| Ethernet |
mellanox/mlx5 |
Nvidia Mellanox 网卡驱动 |
否 |
24.10-3.2.5.0 |
[https://content.mellanox.com/ofed/MLNX_OFED-24.10-3.2.5.0/MLNX_OFED_LINUX-24.10-3.2.5.0-rhel9.4-x86_64.tgz](https://content.mellanox.com/ofed/MLNX_OFED-24.10-3.2.5.0/MLNX_OFED_LINUX-24.10-3.2.5.0-rhel9.4-x86_64.tgz) |
|
bnxt_en |
Broadcom 网卡驱动 |
否 |
1.10.3-233.0.152.14 |
[OpenCloudOS-Kernel: OpenCloudOS-Kernel is the kernel of OpenCloudOS release, which has been fully optimized.If you would like to get more information, please read the wiki page of this project. - Gitee.com](https://gitee.com/OpenCloudOS/OpenCloudOS-Kernel/tree/linux-6.6/release/drivers/thirdparty/release-drivers/bnxt) |
|
ice |
Intel E810 网卡 PF 驱动 |
是 |
N/A |
N/A |
|
i40e |
Intel X710 系列网卡驱动 |
是 |
N/A |
N/A |
|
iavf |
Intel 网卡的 VF 驱动 |
是 |
N/A |
N/A |
|
ixgbe |
Intel 82599/X550 网卡驱动 |
是 |
N/A |
N/A |
|
ixgbevf |
Intel 82599/X550 网卡的VF驱动 |
是 |
N/A |
N/A |
|
ngbe |
网迅网卡驱动 |
否 |
1.2.5.3 |
[OpenCloudOS-Kernel: OpenCloudOS-Kernel is the kernel of OpenCloudOS release, which has been fully optimized.If you would like to get more information, please read the wiki page of this project. - Gitee.com](https://gitee.com/OpenCloudOS/OpenCloudOS-Kernel/tree/linux-6.6/release/drivers/net/ethernet/wangxun/ngbe) |
|
txgbe |
网迅网卡驱动 |
否 |
2.1.1 |
[OpenCloudOS-Kernel: OpenCloudOS-Kernel is the kernel of OpenCloudOS release, which has been fully optimized.If you would like to get more information, please read the wiki page of this project. - Gitee.com](https://gitee.com/OpenCloudOS/OpenCloudOS-Kernel/tree/linux-6.6/release/drivers/net/ethernet/wangxun/txgbe) |
|
hns |
华为海思网卡驱动 |
是 |
N/A |
N/A |
|
hns3 |
华为海思网卡驱动 |
是 |
N/A |
N/A |
|
hiraid |
华为SP686C-M-16i 2G系列RAID卡驱动 |
是 |
N/A |
N/A |
|
sfc |
AMD-Xilinx-Solarflare 的网卡驱动 |
是 |
N/A |
N/A |
| RDMA |
mellanox |
Nvidia Mellanox 网卡驱动(RDMA) |
否 |
24.10-3.2.5.0 |
[https://content.mellanox.com/ofed/MLNX_OFED-24.10-3.2.5.0/MLNX_OFED_LINUX-24.10-3.2.5.0-rhel9.4-x86_64.tgz](https://content.mellanox.com/ofed/MLNX_OFED-24.10-3.2.5.0/MLNX_OFED_LINUX-24.10-3.2.5.0-rhel9.4-x86_64.tgz) |
|
bnxt_re |
Broadcom RDMA网卡驱动 |
是 |
N/A |
N/A |
|
irdma |
Intel 的网卡 RDMA 驱动 |
是 |
N/A |
N/A |
| FC |
lpfc |
Emulex 的 FC 卡驱动 |
是 |
N/A |
N/A |
|
qla2xxx |
Qlogic 的 FC 卡驱动 |
是 |
N/A |
N/A |
|
ast |
Aspeed 显卡驱动。 |
是 |
N/A |
N/A |
| Other |
intel-qat |
intel qat 加速器内核驱动 |
是 |
N/A |
N/A |

## 3、第三方驱动集成方法

### 3.1、第三方驱动集成形式（Intree 或 Out-of-tree）

第三方驱动的集成形式：

- 第一种是集成到内核里面，与内核版本同步迭代，称为 intree ；
- 第二种是第三方厂商独立维护驱动源码、发布OpenCloudOS各版本对应的驱动RPM包，如某些GPU驱动，称为 out-of-tree(OOT) 。

两种集成形式的判定原则为：

- 若第三方驱动与 OpenCloudOS 9 内核中的现有代码存在冲突，可选择采用 out-of-tree 方式、或者集成到内核drivers/thirdparty/源码目录并替代掉原始内核驱动；如果选择使用drivers/thirdparty/驱动，则需要先通过第三方兼容性测试。
- 若第三方驱动处于开发活跃阶段，版本发布节奏与 OpenCloudOS 9 不一致，建议采用 out-of-tree 方式。
- 对于使用广泛、已在其他主流操作系统内核中实现 intree 支持的驱动，OpenCloudOS 9 将优先考虑以 intree 形式集成。
- 最终是否采用 intree 方式，将综合考量硬件厂商意愿及多方技术评估意见后决定。

### 3.2、第三方驱动集成流程

intree 和 out-of-tree，分别走不同的合入流程：

**合入流程** |
**详细步骤** |
**Intree** |
第三方厂商合入驱动，具体操作参考本文“提 PR(Pull Request) ” |
**Out-of-tree** |
由第三方厂商自行维护发布对应OpenCloudOS版本的驱动RPM包 |

### 3.3、提交PR(Pull Request)

#### 3.3.1、提PR的要求

- 需在本地完成编译、自验证；特别是对于新硬件支持的PR/MR，必需有自验证结果（比如跑通厂商已有的功能测试套），因为OC可能没有相关新硬件，没有验证条件。提交Pull/Merge Request时，需简述下自验证结果；。
- 对于一个驱动，需要有CONFIG控制；硬件厂商在哪种架构平台(x86/arm64/loongarch/riscv)完成了测试，才在对应架构的config上，开启这个驱动相关的CONFIG；未完成测试的架构平台，不要开启对应的CONFIG。
- 对于驱动，原则上：能做成内核模块的，需模块化（CONFIG要配置成m）。

#### 3.3.2、代码规范

- 往OpenCloudOS-kernel合入的代码，要遵从linux kernel的代码规范
- 开发者开发完代码后，可以通过内核源码树下的 scripts/checkpatch.pl 来check自己开发的代码，是否符合代码规范
- 从社区backport的代码，commit log中必需添加社区的commit id（以便跟踪社区是否有Fixes commit），类似如下格式：

commit 469693d8f62299709e8ba56d8fb3da9ea990213c upstream.

[ Upstream commit 12f371e2b6cb4b79c788f1f073992e115f4ca918 ]

- Bugfix patch commit log 中提供目标BUG的commit id， 例如： ‘Fixes: 1a94e38d254b ("netfilter: nf_tables: add NFTA_RULE_ID attribute")'

#### 3.3.3、提交PR（Pull Request）

- 申请一个gitee账号，即可往OpenCloudOS-Kernel仓库合入代码。
- 开发代码时，先fork OpenCloudOS-kernel，将开发的代码commit、push到自己fork的分支；然后通过点击"Pull Requests" --> "新建 Pull Request" 往OpenCloudOS-kernel仓库的目标分支提交Pull/Merge Request。

### 3.4、OOT驱动

#### 参考《OpenCloudOS Server产品适配文档》