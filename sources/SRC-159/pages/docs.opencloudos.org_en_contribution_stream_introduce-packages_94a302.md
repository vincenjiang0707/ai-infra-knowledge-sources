source: https://docs.opencloudos.org/en/contribution/stream/introduce-packages/

# 软件包引入操作

软件包引入原则详见：[软件包引入原则](https://docs.opencloudos.org/software-package-management-principles/#3)

软件包选型原则详见：[软件包选型](https://docs.opencloudos.org/software-package-management-principles/#6)

OpenCloudOS Stream 的所有软件包均记录于：[OpenCloudOS/packages.yaml](https://gitee.com/OpenCloudOS/rpm_info/blob/master/packages.yaml)。

该文件以 sig 为单位进行划分，每个 sig 包含 sig 介绍、sig reviewer 和 sig packages。所有软件包都有且仅有一个所属 sig。

该文件提供一个 default sig。如果新增软件包不确定应该分类到哪个 sig，则应选择 default sig。

新增仓库、修改仓库 sig/衰退仓库、删除仓库都需要修改 rpm_info/packages.yaml 文件实现，具体操作如下：

- fork 仓库：
`https://gitee.com/OpenCloudOS/rpm_info`

- clone 仓库：
`git clone git@gitee.com:<username>/rpm_info.git`

- 修改 packages.yaml：将新增软件包名添加到合适的 sig-packages 列表尾端
- 提交 pull request 并
**提供修改原因** - 流水线判断：是否允许修改并返回评论，若流水线因为网络原因等执行失败，在评论区评论 /retest 可以重新触发流水线
- 新增：判断是否存在

- 人工审核：是否允许新增该软件包
- 接受 pull request：触发流水线自动执行相应操作：若流水线因为网络原因等执行失败，在评论区评论 /done 可以重新触发流水线
- 新增：新建仓库，创建README.md，进行初始化设置（设为公开仓库、根据sig设置reviewer、设置允许轻量级pr等）