source: https://docs.mthreads.com/gmc/gmc-doc-online/gpu-debug/

# GPU 故障排查规范

本规范覆盖数据中心 GPU 最常见的异常，汇总设备查询�、MTDCGM、XID、MCCL 和应用调试等文档与实践，帮助系统管理员、应用开发者和 FAE 先判断异常范围，再选择合适的排查路径，尽快恢复服务器运行。

重启设备、重新加载驱动或重启主机前，先保存日志。MTDCGM 二级及以上诊断程序会占用 GPU，只能在排空节点后执行。

## 流程概览[](https://docs.mthreads.com#流程概览)

本规范采用标准化的故障排查流程，帮助您系统性地定位和解决 GPU 相关问题：

虽然本流程保持通用，但可能与系统供应商或集群运维的特定处置流程不一致。涉及供电、散热、PCIe、网络或整机兼容问题时，请尽早联系相应支持方。

## 角色与职责[](https://docs.mthreads.com#角色与职责)

故障处理涉及多个角色。每个角色可能承担多个职责，但每个操作的权限边界应当明确：

| 角色 | 典型身份 | 主要职责 | 不应自行执行的操作 |
|---|---|---|---|
| 工作负载用户 | 运行训练、推理或 HPC 作业的用户 | 记录现象、作业 ID、时间和业务影响；在保留证据前不反复重试或破坏现场 | 重启设备、隔离节点、修改系统配置 |
| 应用/框架开发者 | 自研应用、框架或容器镜像的维护者 | 复现应用错误，检查版本和调用栈，判断是否仅影响某个应用 | 操作调度器、排空节点 |
| 集群管理员 | 集群运维、SRE 或平台工程师 | 维护节点、驱动、监控和日志；执行排空、隔离、重启；管理节点恢复 | 批准硬件 RMA 或修改保修状态 |
| 现场应用工程师（FAE） | 摩尔线程或系统供应商的现场技术接口 | 在客户、系统厂商和 GPU 厂商之间复现与定位根因；指导工具运行并整理证据 | 单方面决定硬件更换 |
| 系统供应商 | 对整机系统交付和保修负责的 OEM/ODM/集成商/云服务商 | BIOS/BMC、PCIe/MTLink 拓扑、电源/散热、固件组合和整机诊断；协调 RMA | 修改 GPU 驱动或 MUSA SDK |

**升级流程：**

`工作负载用户（发现问题）`

→ 应用负责人（判断是否应用本身的问题）

→ 集群管理员（收集证据、诊断、隔离或恢复）

→ FAE / 系统供应商（整�机诊断、硬件兼容性检查、保修服务）

→ 摩尔线程支持（产品缺陷分析、驱动修复）




## 步骤 1：保存现场（30 秒）[](https://docs.mthreads.com#步骤-1保存现场30-秒)

`sudo mthreads-bug-report.sh`



脚本会生成 `*.tgz`

采集包，并自动收集以下系统级信息：

**系统信息：**OS 版本、内核、CPU、内存、硬件 DMI 信息**GPU 状态：**mthreads-gmi 输出、驱动模块参数、PCIe 设备信息、拓扑**日志：**`dmesg -T`

、系统日志、`/var/log/mtgpu*`

和 DKMS 构建日志**调试信息：**`/sys/kernel/debug/musa`

、`/proc/driver/musa`

、环境变量、网络连接

不要立即重启设备，不要重跑失败作业，不要删除日志。

已核验的 KMD reporter 不会自动执行 `journalctl -k -b`

，也不会扫描运行任务目录；部署版本可能不同，请以实际采集包内容为准。运行脚本后，请在重启前保存当前启动周期的完整内核日志：

`sudo journalctl --no-pager -k -b > journalctl-k-b.log 2>&1`



将 `journalctl-k-b.log`

与采集包一并提交。未使用 `--skip-dmesg`

时，脚本会收集 `dmesg -T`

，可作为补充日志来源。如果采集包未包含 `/var/log/mtgpu/event_report/<UUID>/xid_records`

，请在该文件存在且可读时单独保存。

如果故障涉及运行中的作业，还需要记录��以下作业级信息：

- 作业 ID 和 GPU 分配
- 应用版本、框架版本、容器版本
- 完整启动命令和环境变量
- 能否在其他节点复现
- 运行任务目录
- 该目录中已生成的
`*.mudmp`

文件（如存在），包括原始路径、生成时间和文件权限

不要为了生成 `.mudmp`

重新运行失败作业。仅保留故障现场已经生成的文件，并与采集包一并提交。

## 步骤 2：定位故障范围[](https://docs.mthreads.com#步骤-2定位故障范围)

### 第一步：检查 GPU 可见性[](https://docs.mthreads.com#第一步检查-gpu-可见性)

-
查询 mthreads-gmi。它是 GPU 可见性和掉卡判断的主工具：

mthreads-gmi -
根据

`mthreads-gmi`

结果选择下一步：结果 下一步 未发现 GPU 或数量异常 检查驱动和内核日志。参见 [S3000](https://docs.mthreads.com/driver-linux-server/driver-linux-server-doc-online/MTT_S3000/install_guide)或[S5000](https://docs.mthreads.com/driver-linux-server/driver-linux-server-doc-online/MTT_S5000/install_guide)安装指南；保存完整`mthreads-gmi`

输出。GPU 可见且设备标识正常 继续按现象和影响范围分流。

### 第二步：按现象和影响范围选择排查路径[](https://docs.mthreads.com#第二步按现象和影响范围选择排查路径)

-
根据现象选择路径： 运行以下命令查看现象：

mthreads-gmisudo journalctl --no-pager -k -b | grep -i "mtgpu\|xid" | tail -20sudo dmesg -T | grep -i "mtgpu\|xid" | tail -20根据现象选择路径：

- GPU 不可见、XID、健康检查失败、温度/功耗异常：
[检查硬件、驱动和 DCGM](https://docs.mthreads.com#%E6%AD%A5%E9%AA%A4-3%E6%A3%80%E6%9F%A5%E7%A1%AC%E4%BB%B6%E9%A9%B1%E5%8A%A8%E5%92%8C-dcgm) - MCCL 通信失败、带宽异常：
[检查 MCCL 通信](https://docs.mthreads.com#%E6%AD%A5%E9%AA%A4-4%E6%A3%80%E6%9F%A5-mccl-%E9%80%9A%E4%BF%A1) - 应用崩溃、内�存错误、API 错误：
[调试应用](https://docs.mthreads.com#%E6%AD%A5%E9%AA%A4-5%E8%B0%83%E8%AF%95%E5%BA%94%E7%94%A8) - 应用变慢、核函数耗时异常：
[调试应用](https://docs.mthreads.com#%E6%AD%A5%E9%AA%A4-5%E8%B0%83%E8%AF%95%E5%BA%94%E7%94%A8)（多节点同时检查 MCCL）

- GPU 不可见、XID、健康检查失败、温度/功耗异常：
-
根据影响范围进一步判断：


### 处理 XID[](https://docs.mthreads.com#处理-xid)

-
优先检查当前启动周期的内核日志中是否有 XID：

sudo journalctl --no-pager -k -b | grep -i "MTGPU.*XID\|XID"同时保留步骤 1 生成的完整

`journalctl-k-b.log`

，不要只提交过滤后的行。若系统未启用 journald 或无法读取 journal，请使用以下命令补充检查，并在提交信息中说明原因：sudo dmesg -T | grep -i "MTGPU.*XID\|XID" -
记录以下信息：

- XID 编号
- GPU 标识
- 时间
- 相关日志
- 作业是否失败

-
按

[XID 指南](https://docs.mthreads.com/gmc/gmc-doc-online/dcgm/xid_guide)中的处置措施执行。不要仅凭 XID 判断根因。 -
出现以下情况时，停止诊断程序：

- GPU 持续不可见
- 多 GPU/节点同时异常
- XID 要求隔离

停止后，保存证据并提交诊断信息。更多详情，参见

[步骤 6：提交诊断信息](https://docs.mthreads.com#%E6%AD%A5%E9%AA%A4-6%E6%8F%90%E4%BA%A4%E8%AF%8A%E6%96%AD%E4%BF%A1%E6%81%AF)。

### 检查互连状态和 AXI 类 XID[](https://docs.mthreads.com#检查互连状态和-axi-类-xid)

MTLink down 和 AXI 类 XID 属于设备或互连事件，不局限于 MCCL 场景。发现 PCIe/MTLink 链路异常、多 GPU 同时异常或下表中的 XID 时，请先保存现场，不要反复运行通信测试。

-
保存 MTLink 状态和 GPU 拓扑：

mthreads-gmi mtlink -smthreads-gmi topo -m -
保存完整的

`journalctl-k-b.log`

，记录 AXI、MTLink 和 XID 的完整文本、时间及 GPU 标识。 -
将异常节点与正常节点的拓扑、链路状态和作业结果进行对照。

-
按

[XID 指南](https://docs.mthreads.com/gmc/gmc-doc-online/dcgm/xid_guide)中对应错误码的处置措施执行。恢复或重启前先完成证据采集。

重点检查以下 XID：

| XID | 含义 |
|---|---|
`0x02000007` | AXI Error |
`0x07000001` | MTLink Down |
`0x07000003` | MTLink Unrecoverable Error |
`0x07000004` | MTLink Downgrade |

## 步骤 3：检查硬件、驱动和 DCGM[](https://docs.mthreads.com#步骤-3检查硬件驱动和-dcgm)

### 检查温度、功耗和频率[](https://docs.mthreads.com#检查温度功耗和频率)

-
查询温度和功耗：

mthreads-gmi --query -d TEMPERATURE,POWER,CLOCK -
与同节点基线比较，重点关注以下异常情况：

- 温度快速升高或达到上限
- 功耗异常或功耗限制
- PCIe/风扇/ECC 异常
- BMC 报告的硬件事件

-
高负载才出问题时：停止压力测试，保存日志，联系系统管理员。不要修改 BIOS、BMC 或电源策略。


### 查询 GPU 状态[](https://docs.mthreads.com#查询-gpu-状态)

-
查询指定 GPU（例如 GPU 0）：

mthreads-gmi --query -i 0 -
如需 MTDCGM 诊断详情，可选执行以下命令；该输出不用于判定 GPU 是否可见：

dcgmi discovery --gpuid 0 -v -
检查以下关键指标，判断 GPU 运行状态：

- GPU 数量和设备标识
- 温度/功耗/频率/显存使用
- 占用进程
- PCIe 链路
- ECC 和错误事件


更多参数详情，参见 [ mthreads-gmi 用户指南](https://docs.mthreads.com/gmc/gmc-doc-online/gmi/user_manual)。

### 检查健康状态[](https://docs.mthreads.com#检查健康状态)

-
启用全部监控：

dcgmi health -s a -
等待 ≥60 秒或完成一次故障复现。

-
检查是否有错误：

dcgmi health -c

`dcgmi health -f`

仅显示当前监控项，不能作为健康结论。健康检查不会对 GPU 施加额外压力，只反映采集到的问题。

### 运行诊断程序[](https://docs.mthreads.com#运行诊断程序)

-
首次检查运行一级诊断程序（快速检查）：

dcgmi diag -r 1 --debugLogFile ./dcgmi-diag.log -
仅诊断指定 GPU（例如 GPU 0）：

dcgmi diag -r 1 -i 0 -
以 JSON 格式输出结果：

dcgmi diag -r 1 -j备注二级及以上诊断程序（扩展验证、硬件诊断、深度诊断）只能在排空节点后执行。诊断级别详见 MTDCGM 诊断指南。

-
根据诊断结果选择下一步：

结果 下一步 无法启动 检查权限、依赖、配置和 Host Engine 日志 失败 保存测试名、GPU 标识、错误信息和日志，检查 XID 和节点状态 通过 结合复现、日志和监控继续分析；一次诊断通过不能排除所有故障 -
停止诊断程序的条件：

- 节点有业务作业
- GPU 持续不可见且日志报错
- 多 GPU 异常
- 节点无响应
- 涉及供电/散热/PCIe/BIOS

停止后，保存证据并提交诊断信息。



## 步骤 4：检查 MCCL 通信[](https://docs.mthreads.com#步骤-4检查-mccl-通信)

本步骤仅在涉及多 GPU/多节点或通信带宽时运行。运行前，确认不与业务作业争用资源。

如果通信异常同时出现 MTLink down 或 AXI/MTLink 类 XID，请先按[检查互连状态和 AXI 类 XID](https://docs.mthreads.com#%E6%A3%80%E6%9F%A5%E4%BA%92%E8%BF%9E%E7%8A%B6%E6%80%81%E5%92%8C-axi-%E7%B1%BB-xid)保存设备和互连证据。这类错误不局限于 MCCL。

### 验证通信[](https://docs.mthreads.com#验证通信)

-
测试单卡通信：

all_reduce_perf -b 1M -e 1024M -f 2 -g 1 -
测试多卡通信：

all_reduce_perf -b 1M -e 1024M -f 2 -g 8 -
与正常节点比较。

GPU 数量不同的节点不要直接比较绝对带宽。


### 收集日志[](https://docs.mthreads.com#收集日志)

-
通信异常时启用警告日志：

export MCCL_DEBUG=WARN -
需要更详细的初始化信息时，启用完整日志：

export MCCL_DEBUG=INFOexport MCCL_TOPO_DUMP_FILE=/tmp/mccl-topo.xml -
指定网络接口（如有多个）：

export MCCL_SOCKET_IFNAME=eth0

### 判断问题范围[](https://docs.mthreads.com#判断问题范围)

根据测�试结果，按以下分类定位问题范围：

- 单机多卡失败：检查 GPU P2P、PCIe/MTLink、共享内存、容器配置
- 单机通过、跨节点失败：检查网络接口、RDMA、端口、防火墙、节点间差异
- 测试通过但应用通信失败：检查应用 MCCL 参数、进程映射、启动器配置
- 出现
`MCCL WARN`

：参见[MCCL 文档](https://docs.mthreads.com/musa-sdk/musa-sdk-doc-online/libraries/mccl/)

不要直接禁用 ACS、修改 BIOS 或更换网络配置，这些操作需要系统管理员确认。


## 步骤 5：调试应用[](https://docs.mthreads.com#步骤-5调试应用)

### 记录详细步骤并准备最小复现[](https://docs.mthreads.com#记录详细步骤并准备最小复现)

提交复现信息时，既要记录可重复执行的完整步骤，也要尽量构造最小用例。完整步骤用于还原现场，最小用例用于减少无关变量。

-
记录环境基线：

- GPU 型号、数量、节点和拓扑
- OS、内核、驱动、MUSA Toolkit、框架、应用和容器版本
- 运行任务目录和输入数据说明

-
记录可直接重放的复现步骤：

- 前置条件和准备操作
- 完整启动命令、参数、环境变量和执行顺序
- 预期结果、实际结果、发生时间和复现频率
- 受影响的 GPU、节点和作业 ID

-
在保留故障特征的前提下，依次减少输入规模、GPU 数量、节点数量和非必要依赖。记录每次删减及其结果，避免把不能触发问题的用例标记为最小复现。

-
保留原始错误输出、退出状态码、应用日志和任务目录中已生成的

`*.mudmp`

文件。

### 诊断应用问题[](https://docs.mthreads.com#诊断应用问题)

根据应用的具体现象，选择对应的诊断工具：

-
**非法内存访问、显存泄漏、API 错误**：使用 MUSA Compute Sanitizer：mt-compute-sanitizer ./app更多详情，参见

[MUSA Compute Sanitizer 用户指南](https://docs.mthreads.com/mooreperf/mooreperf-doc-online/musa_compute_sanitizer/user_guide)。 -
**应用卡住、需查看时间线**：使用 Moore Perf System：msys profile --trace=musa,osrt -o report.msys-rep ./app更多详情，参见

[Moore Perf System 用户指南](https://docs.mthreads.com/mooreperf/mooreperf-doc-online/moore_perf_system/user_guide)。 -
**核函数性能异常**：使用 Moore Perf Compute：mcu -o my_report ./app更多详情，参见

[Moore Perf Compute 用户指南](https://docs.mthreads.com/mooreperf/mooreperf-doc-online/moore_perf_compute/user_guide)。 -
**保存诊断结果**：无论使用哪个工具，都必须保存以下诊断信息，以便后续分析和提交给技术支持：

**错误详情**：错误类型、错误地址、出错的核函数名称**调用信息**：完整的调用栈，用于定位问题代码路径**运行状态**：退出状态码和完整日志输出


### 根据复现结果[](https://docs.mthreads.com#根据复现结果)

根据复现情况，选择下一步的排查方向：

- 仅该应用复现：继续检查应用、框架和输入
- 多应用在同一 GPU 失败：
[检查硬件、驱动和 DCGM](https://docs.mthreads.com#%E6%AD%A5%E9%AA%A4-3%E6%A3%80%E6%9F%A5%E7%A1%AC%E4%BB%B6%E9%A9%B1%E5%8A%A8%E5%92%8C-dcgm) - 仅在特定 GPU/节点出现：保存位置和拓扑差异，检查对应设备
- 仅多节点作业失败：分别验证各节点，再检查通信


## 步骤 6：提交诊断信息[](https://docs.mthreads.com#步骤-6提交诊断信息)

### 提交内容[](https://docs.mthreads.com#提交内容)

向摩尔线程技术支持提交诊断信息时，请包含以下内容，帮助技术人员快速定位问题：

| 类别 | 内容 |
|---|---|
| 问题摘要 | 现象、时间、频率、影响范围、业务影响 |
| 环境 | OS、内核、驱动、MTDCGM、MUSA Toolkit、固件版本 |
| GPU 状态 | 标识、PCI 信息、温度、功耗、显存、链路、进程 |
| 作业 | 作业 ID、节点、GPU 分配、启动命令、环境变量、运行任务目录和 `*.mudmp` 文件路径（如存在） |
| 日志 | 内核、XID、Host Engine、应用、MCCL、调试工具、诊断 |
| 记录 | 操作时间线、命令和结果、复现信息、节点对比 |

运行以下命令生成诊断报告，并将输出附加到提交信息中：

`mthreads-gmi > mthreads-gmi.log 2>&1`

dcgmi diag -r 1 --debugLogFile ./dcgmi-diag.log



提交前删除密码、令牌和客户数据，保留时间、设备标识和错误字段。

### 联系谁[](https://docs.mthreads.com#联系谁)

根据问题的性质，联系相应的技术支持方：

| 问题 | 提交给 |
|---|---|
| 单个应用/框架 | 应用维护者 |
| 驱动、MTDCGM、MUSA 工具 | 摩尔线程技术支持或 FAE |
| MCCL/多节点通信 | 系统管理员 + 摩尔线程技术支持 |
| PCIe/供电/散热/BIOS | 服务器厂商或系统集成商 |

通常应优先联系系统供应商，因为多数 GPU 错误涉及整机边界。

## 步骤 7：恢复与验证[](https://docs.mthreads.com#步骤-7恢复与验证)

### 恢复操作[](https://docs.mthreads.com#恢复操作)

按以下表格选择适当的恢复操作：

| 操作 | 何时用 | 前置条件 | 失败时 |
|---|---|---|---|
重启应用 | 应用级错误 | 已保存应用日志 | 若跨节点可复现，则上报 |
重启 Host Engine | MTDCGM 连接问题 | 已排空节点 | 若问题复发，则上报 |
排空/隔离节点 | 节点影响其他作业 | 调度器权限，已通知用户 | 若诊断持续失败，则上报 |
重启设备 | GPU 状态异常 | 已保存证据，无进程使用设备 | 若重启失败或事件复发，则上报 |
主机重启 | 所有其他方法失败 | 节点已排空，证据已归档 | 若重启后仍失败，则上报 |

**不应将重启设备作为首要操作。** 重启设备前先完成：(1) 保存内核日志和 Host Engine 日志；(2) 保存 XID 序列和诊断结果；(3) 确认所有进程已释放设备；(4) 记录拓扑和设备发现结果。重启设备后，以上证据将永久丢失。

### 恢复验证（全部通过方可上线）[](https://docs.mthreads.com#恢复验证全部通过方可上线)

执行以下检查清单，确认系统已完全恢复并可以承载业务：

`mthreads-gmi`

— GPU 数量和设备标识正确- 如已启用 MTDCGM，
`dcgmi health -c`

— 无新错误或警告 - 运行受控工作负载 — 故障不复现
- 记录恢复操作和验证结果

满足以下任一条件，将故障设备/主机从系统中隔离并上报：原因不明且无法恢复、故障在重启后复发、GPU 持续不可见、多 GPU/节点同时异常、涉及供电/散热/PCIe/BIOS/BMC。

## 相关文档[](https://docs.mthreads.com#相关文档)

本规范涉及的工具和流程详见以下文档：

：mthreads-gmi 命令参考和 GPU 状态监控[MTGMI](https://docs.mthreads.com/gmc/gmc-doc-online/gmi/user_manual)：dcgmi 命令参考、诊断和健康检查[MTDCGM](https://docs.mthreads.com/gmc/gmc-doc-online/dcgm/get_started)：XID 错误码分类和处置措施[XID](https://docs.mthreads.com/gmc/gmc-doc-online/dcgm/xid_guide)：多卡通信故障排除[MCCL](https://docs.mthreads.com/musa-sdk/musa-sdk-doc-online/libraries/mccl/mccl_user_guide_2.4/troubleshooting/troubleshooting)：应用内存和 API 错误调试[MUSA Compute Sanitizer](https://docs.mthreads.com/mooreperf/mooreperf-doc-online/musa_compute_sanitizer/user_guide)：系统性能分析和时间线追踪[Moore Perf System](https://docs.mthreads.com/mooreperf/mooreperf-doc-online/moore_perf_system/user_guide)：核函数性能分析[Moore Perf Compute](https://docs.mthreads.com/mooreperf/mooreperf-doc-online/moore_perf_compute/user_guide)