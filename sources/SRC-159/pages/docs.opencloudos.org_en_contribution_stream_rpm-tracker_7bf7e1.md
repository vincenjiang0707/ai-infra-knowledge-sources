source: https://docs.opencloudos.org/en/contribution/stream/rpm-tracker/

# 自动补丁工具

在软件包的稳定维护阶段，主要通过backport补丁的方式进行维护，但软件包的分支、commits信息多。我们设计了rpm-tracker工具通过GraphQL来获取上游commits信息，支持github、gitlab等主流平台；选择专门的大模型，结合微调，对commits进行分类，把bug修复、cve修复等类型的commits识别出来，将 commit 信息写入到 issue 协助开发者跟进社区更新。除了信息展示外，还提供一系列命令进行编译检查，提交 PR。

## 1. 工作流程

### 1.1 识别 commit

工具每天定时触发，筛选前一日的 commit 信息，筛选 bug修复、cve修复等类型的 commit 信息，创建 gitee issue 提醒 maintainer 跟踪，issue 均携带 `COMMIT`

标签便于识别。

### 1.2 分析 commit

maintainer 根据每日更新的 commit 信息分析是否需要合入，提供以下信息供参考：

- branch：跟踪 commit 所在分支
- id：7位 commit id，链接指向完整commit url
- date：commit 出现在社区时间
- message：commit message
- type：分类得到的 commit 类型。人工分类 > 引擎分类 > 大模型分类。其中人工分类可以反馈更新，引擎分类由分析引擎更新，大模型分类在commit信息入库时更新。
- 能否合入：测试当前commit能否自动合入当前版本，只测试单个commit，使用仓库为
`ocs-commit/<repo>`


## 2. 操作手册

### 2.1 分类是否正确

无论 coommit 是否需要合入，都请分析 commit 分类是否正确，这是分析合入的基础

- 无误：无需操作
- 有误：通过
`/update_type`

命令反馈

命令说明：

`/update_type "<commit_id>" <类型>`

：更新commit分类类型，更新数据库信息以及gitee显示，若成功会返回评论反馈

### 2.2 是否需要合入

请分析是否需要合入当前展示的 commit

- 不需要：不需要合入的commit经反馈都不会继续显示在页面中。
- 若commit已经存在当前版本tarball中，通过 /in_tarball 反馈；
- 若是其他原因不需要合入，通过 /hide 反馈；

- 需要：通过
`/pick`

、`/recheck`

、`/pr`

命令选择需要合入的 commit，进行编译兼容性检查，创建 pr，使用仓库为`ocs-commit/<repo>`


命令说明：

`/in_tarball "<commit_id>"`

：经分析位于 tarball，不需要合入该 commit，反馈后不会继续显示在 gitee 前端`/hide "<commit_id>"`

：出于某些原因不需要合入该 commit，反馈后不会继续显示`/pick "<commit_id>"`

：选择commit尝试合入并进行编译、兼容性检查（x86_64架构），仓库位于`ocs-commit/<repo>`

`/recheck`

：pick 后 commit 仍然需要适配修改，修改仓库后，重新执行编译、兼容性检查`/pr "<commit_id>"`

：将 pick 后的 commit 提交pr，将`ocs-commit/<repo>`

仓库直接提交 PR 至 OpencloudOS-Stream 仓库

### 2.3 反馈意见

欢迎随时反馈对工具的建议与意见

- 针对commit 进行反馈：/note
- 针对整个包反馈：在 tracker-feedback 仓库中提交 issue

命令说明：

`/note "<commit_id>"`

：针对某条commit 进行反馈，更新至 tracker-feedback 仓库

## 3. 帮助命令

`/help`

"：获得帮助命令输出

注：目前仅支持当前仓库成员执行自动升级流程，申请加入仓库成为仓库成员，请参考 `软件包权限管理-加入仓库`

章节。