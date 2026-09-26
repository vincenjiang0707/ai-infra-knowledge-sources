source: https://docs.opencloudos.org/en/contribution/stream/rpm-upgrade/

# 自动升级工具

stream 版本提供自动升级工具，对于需要升级的软件包，开发者可以在对应仓库下创建升级 issue，一条命令触发自动升级流水线，完成升级以及相关检查。

## 操作指南

具体流程如下：

-
**创建升级 issue**：点击 “新建 issue”，默认创建 “升级” 类型 issue，根据模板指引创建 issue，填写升级原因； -
**触发升级**：评论`/upgrade [version]`

可触发指定版本升级；也可评论`/upgrade`

默认使用最新版本升级； -
**流水线结果**：-
流水线首先返回升级信息，若升级成功则继续触发编译构建及兼容性检查；

-
若流水线因网络等偶发原因失败，请评论

`/upgrade`

重新触发升级流程； -
若需要修改代码，则根据提示修改

`ocs-upgrade/<repo>`

仓库，流水线自动授予触发升级的用户该仓库的`push`

权限：`git clone git@gitee.com:ocs-upgrade/<repo>.git`


-
-
**修改与检查**：每次对仓库进行修改后，请评论`/recheck`

重新进行编译构建及兼容性检查 -
**结论**：兼容性工具检查结果供参考，请根据 Release Note/ Changelog 及代码，分析并确认兼容性，决定是否进行升级-
升级：评论

`/pr`

即可正式提交 pr -
无需升级：请在侧边栏将状态修改为

`已拒绝`

，关闭当前 issue； -
延迟升级：请评论

`/TBD [days]`

命令挂起本次升级，若不指定挂起天数，会在下次大规模升级时统一触发，若指定天数，则在下次大规模升级时，只有达到该天数才会触发升级；

-
-
**反馈**：若升级失败或需要反馈意见，可通过`/note <反馈类型> <反馈意见>`

命令反馈升级失败原因，必要时对仓库代码进行调整，方便后续版本进行自动升级。 -
**帮助命令**：评论`/help`

可以获得帮助命令输出

注：目前仅支持当前仓库成员执行自动升级流程，申请加入仓库成为仓库成员，请参考 `软件包权限管理-加入仓库`

章节。

## 升级问题手册

rpm-upgrade 自动升级CI流水线旨在用于自动升级时，修改spec中 Version/Release/Changelog，sources文件，下载/上传 tarball，尝试处理补丁冲突。下面对 CI 升级时常见问题进行分类，并附上相应处理步骤。

**影响自动升级CI**

在此过程中，Source获取、跟踪仓库 等是必须成功项，因此出现此类问题时视为 自动升级失败，必须修正。

**Source修正**：Source下载链接固定、Source链接需要更新等。- 解决：需要修正spec文件中的Source链接。修改主仓库Source链接 合入PR后，重新发起/upgrade。

**跟踪仓库有误**：该包yaml文件跟踪仓库有误，需更新。-
**自定义脚本**：如：Source源码包无法直接获取，需要编写脚本生成；版本号无法直接获取，需要脚本生成 等。上述场景，均需编写自定义脚本，接入CI完成升级。- 解决：需要编写自定义脚本，见 rpm-upgrade指南-自定义脚本升级。主仓库新增脚本 合入PR后，重新发起/upgrade。

-
**不影响自动升级CI**

如果 koji编译失败、补丁冲突等 是CI尽力处理项，让CI尽可能帮助开发者完成升级时的机械化动作。因此出现问题时，不视为自动升级失败。

**编译失败**：koji编译失败，如：prep、build、install 阶段代码需调整，%files 阶段文件新增、删除、更名等。- 解决：升级时maintainer介入处理。修改spec后 /recheck。

**补丁冲突**：发行版补丁、上游补丁冲突，需maintainer介入调整。- 解决：升级时maintainer介入处理。修改spec后 /recheck。

**系列包升级**：该包为系列包，需按顺序升级。- 解决：顺序升级即可。

**无需自动升级**：软件包版本固定、spec修改繁杂 等，需人工升级，因此不进行自动升级。- 解决：人工升级。

**Changelog链接更新**：issue中给出的Changelog不准确or衰退，可指定具体的Changelog发布网址。- 解决：在yaml文件新增changelog_url 字段即可。详见：yaml字段介绍；yaml修改示例；


## 自定义脚本升级

部分软件包无法使用通用的自动升级流水线，需要自定义升级脚本，如 rust系列的vendor处理、npm系列生成tarball 等。

需考虑和CI适配，定义接口or规范等，便于调用脚本，完成升级。

### 脚本规范

如果想在 rpm-upgrade 中，适配自定义脚本，进行自动升级。需要在对应 软件包的 gitee 仓库中，添加以下文件：

- up.yaml文件：该文件存在，表明将结合自定义脚本，进行升级。
- sh/py脚本: 具体的自定义脚本；

up.yaml内容如下：

- name：告知rpm-upgrade，脚本涉及内容，如生成了Source1、Source2到本地。后续rpm-upgrade将其上传到COS、计算sha值等；
- order：脚本的执行方式；

```
Source:
name:
- Source1
- Source2
order:
- sh test.sh -h
- python3 make_tarball.py
Version:
name:
- device_mapper_version
- another_version
order:
- sh get_ver.sh
```


### 使用示例

以下为常见场景脚本示例，如有使用疑问，请联系gordonwwang。

- 通过脚本生成Source

Source包无法直接wget获取，需要执行脚本生成。示例：[rustup生成Source1](https://gitee.com/opencloudos-stream/rustup/commit/0962c3fa36e77e8ad273e90b96f2f38dac62f81d)

注：脚本只需要生成 Source1 的源码包即可，rpm-upgrade工具会根据 up.yaml文件中声明了的Source1，自动将其上传、更新sources文件sha值等。

- 获取版本号

升级lvm2时，发现版本号device_mapper_version也需修改。

示例：[脚本生成device_mapper_version版本号](https://gitee.com/gordonwwang/lvm2/commit/7697158bca0a51a272e1619667ebdf79dddfda67)

## 本地体验

rpm-upgrade自动升级**推荐通过流水线方式触发**，可获得完整的软件包 上游查询、自动升级、兼容性检测、提交代码/PR 等服务。
但如果有调试or自行安装体验需求，也可本地安装rpm包使用，但仅可体验 上游查询、自动升级。

### 安装

通过dnf安装：

```
dnf install rpm-upgrade
```


[镜像源](https://mirrors.opencloudos.tech/opencloudos-stream/releases/23/binary/x86_64/Packages/)查找并手动安装，如：

```
dnf install https://mirrors.opencloudos.tech/opencloudos-stream/releases/23/binary/x86_64/Packages/rpm-upgrade-4.5-2.ocs23.x86_64.rpm
```


### 配置文件

由于需要访问gitee仓库，以便于获取仓库中软件包信息。因此，需要配置gitee私人tocken：

```
# 创建json配置文件
vim ~/.gitee_conf.json
# 在文件中填入以下内容，请替换<gitee_name>、<gitee_token>：
{"user":"<gitee_name>","access_token":"<gitee_token>"}
```


gitee token设置入口：https://gitee.com/profile/personal_access_tokens，建议仅提供查看项目权限即可。

### 上游查询

```
rpm-upgrade rust
rpm-upgrade rust -nv 1.76.0
rpm-upgrade aide -d # 查询当前版本、最新版本的发布日期，两个版本间的发布次数
rpm-upgrade aide -d -c # 查询当前版本、最新版本的发布日期，两个版本间的发布次数。同时查询Release Notes的链接
```


### 自动升级

具体流程包括：

- fork代码到个人仓库
- clone到本地（clone前，将删除本地同名仓库）
- 修改spec/sources；
- 补丁冲突分析；
- tarball上传（默认不上传，可使用-t/--tarball 开启上传源码包）；
- --tarball参数：直接将tarball上传到 lookaside，会出现tarball无效上传。建议个人开发者使用；
- --add_tarball参数：将tarball 添加到 Git仓库，koji编译时不会去lookaside查找，提PR时CI再git rm 该文件；建议CI使用；
- push代码到个人仓库（也可使用--no_push关闭push）；

```
# 自动升级 为 最新版本，未上传tarball，升级结果push到个人仓库（建议使用）
rpm-upgrade fakeroot -u
# 自动升级 为 指定版本，未上传tarball，升级结果push到个人仓库
rpm-upgrade fakeroot -u -nv 1.31
# 自动升级 为 指定版本，并上传源码包
rpm-upgrade fakeroot -u -nv 1.31 -t/--tarball
# 自动升级，但不push代码到remote，仅在本地修改。
rpm-upgrade fakeroot -u --no_push
```