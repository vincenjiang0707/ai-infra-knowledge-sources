source: https://docs.opencloudos.org/contribution/stream/Software-package-permission-management/

# 软件包权限管理

## 软件包权限介绍

由于 OpenCloudOS 社区的代码仓库托管在 Gitee 进行管理，参考 Gitee 的成员管理 OpenCloudOS-Stream 为每个仓库划分了以下几个角色：

-
管理者：默认仅有 ocs-bot，用于对仓库执行自动化操作

-
开发者：软件包责任人

-
观察者：软件包所属领域的责任人


参与社区开发的步骤都通过命令行实现，因此仓库角色分配主要影响责任关系：

-
PR 创建者：创建 PR 时会识别创建者，如果是自动升级/自动补丁/自动重编这一类由 ocs-bot 自动创建的 PR，也会识别触发用户为创建者

-
PR 审查人员：根据“开发者 -> 观察者”顺序识别到非 PR 创建者的成员，自动则将其设置为 PR 审查人员

-
ISSUE 责任人：创建 ISSUE 时若没有指定责任人，根据“开发者 -> 观察者”顺序识别到成员设置为 ISSUE 责任人


## 如何加入仓库

我们欢迎并鼓励开发者参与我们的仓库开发，若您想参与社区仓库的维护工作，或体验自动升级、自动补丁工具，您需先申请成为仓库成员。为此，我们通过`collaborators.yaml`

文件将社区开发者添加为仓库成员。

要申请成为仓库开发者，请按照以下步骤操作：

- fork 仓库：
`https://gitee.com/OpenCloudOS/rpm_info`

- clone 仓库：
`git clone git@gitee.com:<username>/rpm_info.git`

- 编辑
`collaborators.yaml`

文件，添加您的信息。请确保正确填写您的 gitee 账号ID、邮箱和希望加入的仓库名称。 - 提交 pull request 并
**提供修改原因**

第一次申请加入仓库时，需要填写 Gitee 账户名称，请以该模板为参考，在 `collaborators.yaml`

文件末尾追加以下内容：

```
- 账号ID: xxx
仓库:
- xxx
- xxx
```


示例：

```
- 账号ID: gitee-bot
仓库:
- setup
```


字段说明：

`账号ID`

：Gitee 账户名称，**请务必保证与 gitee 账号ID一致**，否则无法正确为您修改权限。以[gitee-bot](https://gitee.com/gitee-bot)用户为例，个人主页中，左上角个人介绍中`@gitee-bot`

表示该账号ID为`gitee-bot`

，与个人空间地址一致，而`Gitee GPG Bot`

则是账户昵称，非唯一标识。`仓库`

：申请加入的仓库列表。

注意事项：

- 在修改
`collaborators.yaml`

文件时，**请不要修改其他成员的信息。**；若团队参与贡献，也可直接联系我们申请仓库权限 - 如有任何疑问或需要帮助，请随时与我们联系。