source: https://docs.opencloudos.org/en/contribution/stream/deprecate-packages/

# 衰退与删除软件包

软件包退出管理原则详见：[软件包退出](https://docs.opencloudos.org/software-package-management-principles/#5)

具体退出分为衰退与删除两种选择，删除软件包属于高危操作，若您分析某个软件包需要从仓库中移除，建议将其衰退，而不进行删除操作。

## 衰退软件包

衰退软件包需要修改 rpm_info/packages.yaml 文件，具体操作如下：

- fork 仓库：
`https://gitee.com/OpenCloudOS/rpm_info`

- clone 仓库：
`git clone git@gitee.com:<username>/rpm_info.git`

- 修改 packages.yaml：
- 软件包：将衰退的软件包移动到 deprecated sig
- 二进制包：将衰退软件包对应的所有二进制软件，从原始列表移到 deprecated.list 中，并确认没有其他二进制包依赖该衰退软件包。
- eg：假设appstream-data这个软件需要衰退，它存在于appstream.list中，那么就需要删除appstream.list中 appstream-data 所有二进制包，添加到 deprecated.list，才算完成 appstream-data 的衰退操作。

- 提交 PR 并
**提供衰退原因** - 审核：是否允许衰退该软件包
- 若接受 PR：流水线自动将该仓库标签修改为
`deprecated`

，相关软件包移入 deprecated repo

## 删除软件包

只有已经衰退，即属于 deprecated sig 的软件包允许删除，不允许直接删除一个软件包。删除仓库都需要修改 rpm_info/packages.yaml 文件，具体操作如下：

- fork 仓库：
`https://gitee.com/OpenCloudOS/rpm_info`

- clone 仓库：
`git clone git@gitee.com:<username>/rpm_info.git`

- 修改 packages.yaml
- 删除：将软件包名所在行删除

- 提交 PR 并
**提供删除原因** - CI 门禁：判断是否满足删除条件
- 审核：是否允许删除该软件包
- 若接受 PR：则该仓库被删除