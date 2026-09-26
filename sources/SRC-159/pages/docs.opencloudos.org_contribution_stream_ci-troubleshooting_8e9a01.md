source: https://docs.opencloudos.org/contribution/stream/ci-troubleshooting/

# 门禁排查手册

门禁管理员：cunshunxia、wynnfeng、zoedong

## CI 门禁

pr 提交后，CI 会进行一系列检查，包括：编译构建测试、安装/卸载测试、安全合规检验

### Pull Request 文件检查

为避免开发者误上传源码包到 git 仓库，会检查 pull request 中是否包含压缩文件，如包含则会上传到 lookaside 并返回评论提示开发者删除相关压缩包，也是当前为开发者上传源码包的一种解决方案

### 编译构建测试

为确保提交软件包质量，提交 pull request 后会触发编译构建测试，根据提交的代码在 x86_64 以及 aarch64 机器上进行编译构建

- 编译构建测试于koji平台触发：https://build.stream.opencloudos.tech/koji/
- 编译构建测试测结果由 ocs-bot 评论于对应 pull request

### 安装/卸载测试

为确保提交软件包能够正常使用，通过编译构建测试后会在 x86_64 以及 aarch64 机器上对生成的二进制软件包依次进行安装卸载测试。

- 安装/卸载测试结果由 ocs-bot 评论于对应 pull request

### 安全合规

为了确保项目的安全性和合规性，引入新软件包后我们还会进行以下安全合规相关检查：

- 安全漏洞扫描：通过识别可能存在的安全漏洞和弱点，有助于及早发现并解决潜在的安全风险。
- 敏感信息扫描：确保不包含敏感信息，如密码、密钥、API 凭证等。保护项目和用户的敏感数据，防止泄露和滥用。
- 合规扫描：确保新软件包符合项目所采用的开源协议要求，包括许可证声明和版权信息的正确性。确保项目的合法性和合规性。

通过进行这些扫描和检查，我们可以最大程度地降低引入新软件包可能带来的安全风险，并确保项目的合规性。我们鼓励所有贡献者和团队成员积极参与这些扫描和检查过程，以共同维护项目的安全和合规标准。

## 1. 门禁流程简介

相关指导文档：

- OpenCloudOS 社区版本贡献指南: https://docs.opencloudos.org/contribution/how-to-contribute-oc/
- 软件包管理原则：https://docs.opencloudos.org/contribution/software-package-management-principles/
- 软件包打包指导：https://docs.opencloudos.org/contribution/software-packaging-guide/

## 2. 门禁常用操作

### 2.1 门禁支持命令列表

门禁支持在pull request页面输入对应命令，触发门禁不同功能，具体命令如下：

| 类型 | 命令 | |
|---|---|---|
| pull request | /retest | 触发门禁测试 |
| /agree | 开发者同意CI门禁兼容性检查结果，仅限于《兼容性确认(contributor)》阶段 | |
| /disagree items1 items2 ... | 开发者不认同CI门禁兼容性检查某项结果，例如：/disagree ability abi, 仅限于《兼容性确认(contributor)》阶段使用，且该命令会改变后续测试重编包列表 | |
| /type pr_type | 设置PR标签（标签可以为：security, bugfix, other） 例如：/type bugfix | |
| /agree /type pr_type | 组合命令，表示既认同CI门禁兼容性检查结果，又设置PR标签，例如：/agree /type bugfix ；详情参考上述单个命令 | |
| /disagree items1 items2 ... /type pr_type | 组合命令，表示既不认同CI门禁兼容性检查某项结果，同时又设置PR标签，例如：/disagree ability abi /type bugfix；详情参考上述单个命令 | |
| /compat-mistake item1 item2 ... | 类似/disagree, 表示不认同CI门禁兼容性检查某项结果（一般用于reviewer想修改门禁CI的兼容性检查某项结果, 且该命令会改变后续测试重编包列表），例如：/compat-mistake abi api | |
| /approve | 同意 pull request 并合并，仅限于《合并PR(reviewer)》阶段使用 | |
| /resubmit task_id1 task_id2 | 对测试重编某项编译进行重新koji编译 | |
| /resubmit all | 对测试重编所有项进行重新koji编译 | |
| /compat-reset | 重置兼容性确认结果（此命令通常用于：不认同contributor对于检查项的误报操作，想重置恢复到《门禁CI检查》阶段） | |
| /help | 显示帮助信息 |

注意：/disagree和/compat-mistake都会影响测试重编的包列表，例如： 情况1：CI门禁结果显示abi检查项不通过，该检查项导致10个软件包需要正式/测试重编，此时您/disagree abi或者/compat-mistake abi, 会将这10个软件包从正式/测试重编列表中删除； 情况2：CI门禁结果显示abi检查项通过，但您认为该项存在兼容性差异，不应该通过，此时您/disagree abi或者/compat-mistake abi，将会导致所有编译/运行依赖该PR对应的包的其他受影响包，加入测试重编


### 2.2 重试

门禁测试正常由PR触发，后续如果由新commit推送，会自动触发重试
如果需要手动重新执行门禁测试，请评论`/retest`

。

## 3. 门禁检查项以及问题排查

### 3.1 检查项介绍

| 测试项名称 | 子测试项 | 主要检查内容 | SUCCESS | WARNING | FAILED |
|---|---|---|---|---|---|
| spec | 检查spec文件里changelog和version,release是否规范 | 成功 | / | changelog格式不对或者version, release没有递增 | |
| source | 获取source文件中的源码包 | 成功 | / | 从文件服务器获取源码包失败 | |
| srpmbuild | 生成source rpm包 | 成功 | / | 制作srpm包失败 | |
| rpmbuild | rpm编译 | 成功 | / | 编译失败 | |
| install | 安装测试 | 成功 | / | 安装失败 | |
| compatibility | subrpmlist | 子包数量变化 | 无变化 | 子包增加 | 子包减少 |
| filelist | 包含文件列表变化 | 无变化 | 包文件发生增加 | 包文件发生减少 | |
| ability | 包提供的requires/provides等能力变化 | 无变化 | REQUIRES/CONFLICTS/OBSOLETES/RECOMMENDS变化、PROVIDES增加 | PROVIDES减少 | |
| abi | ABI差异 | 无变化 | / | 软件包ABI发生变化并且影响ABI兼容性 | |
| api | API差异 | 无变化 | / | 软件包API发生变化并且影响API兼容性 | |
| executable | 可执行文件执行输出差异 | 无变化 | / | 包中可执行文件运行输出发生变化 | |
| conf | 配置文件配置项差异 | 无变化 | 其余配置文件发生变化 | 宏、系统关键路径配置文件变化 |

### 3.2 rpm-check 工具介绍

CI检查结果来自 `rpm-check`

工具，rpm-check 工具为基于开源 ABICC 项目研发的支持多语言多维度软件兼容性检查工具。
当前支持检查项包括：

- filelist
- ability
- abi
- api
- conf
- executable

分别对应上述提到的CI中的检查项。如果对CI结果有疑问，可以在本地使用 `rpm-check`

工具重新检查以及定位问题。

#### 3.2.1 安装方法

工具当前尚未开源，如需体验请联系@rockerzhu

#### 3.2.2 使用方法

当前支持的选项如下，可以通过 `--help`

查看。

```
[root@localhost ~]# rpm-check --help
usage: ./rpm-check.py [options] [local_rpm|local_library] [target_rpm|target_library]
Options:
--help Print this message and then exit.
--version Print the current version of rpm-check
--checkconf Check the configurations diff in given rpms.
--checkabi Check the ABI consistency between two rpms/libraries
--d1 devel/debuginfo pkg path for old rpm.
--d2 devel/debuginfo pkg path for new rpm.
(i.e., ./rpm-check.py --checkabi a b --d1 c --d2 d)
--dir1 Directory with old rpms and debuginfo
--dir2 Directory with new rpms and debuginfo
--with-symbol Used along with checkabi, find affected rpms with specific symbols and types
--multi-packages Used along with checkabi, search given dirs which has sub dirs(one pkg one dir).
--local Check affected symbols with local databse, used along with --with-symbol.
--checkfile Check file list
--checkability Check requires/provides differences
--verbose Execute in verbose mode and preserve all outputs during execution.
target_rpm:
-- If not specified, compare with the rpm in repo.
```


日志等级说明： 工具输出日志分为四个等级： ERROR（红色）、WARNING（紫色）、INFO（蓝色）、DEBUG（黄色）

默认输出日志等级可以在/etc/rpm-check.conf中通过default_log_level值调整。也可以直接命令中--verbose参数启用DEBUG日志。

`--with-symbol`

参数用来根据变化的符号在repo源里查找受影响的软件包（如果无变化符号则无影响）。

`--multi-packages`

参数用来批量进行软件包兼容性检查，一般用在需要对整个系统进行兼容性检查场景。

`--local`

参数启用本地缓存，加快符号检索效率。

其他选项使用见下面问题排查方式中。

### 3.3 问题排查方式

#### 3.3.1 spec失败

请打开build_info，确认其错误信息，也可以参考spec检查项相应备注栏信息

一、changelog相关失败(build_info中)

- 错误：
`changelog must start with *`

: 说明changelog 没有以`*`

开头 - 错误：
`bad mailbox in changelog:`

: 说明邮箱格式不对 - 错误：
`cannot extract date from changelog`

: 说明changelog缺少日期，或者提取失败 - 错误：
`bad date in changelog:`

: 日期格式不正确 - 错误：
`bogus date in changelog`

: 存在虚假日期 - 错误：
`spec's version or release not consistant with changelog`

: spec的版本号和changelog不一致 - 警告：
`changelog format error`

: changelog的内容格式不对，应该具有`[Type]`

和`[DESC]`

两个字段

其中对于`changelog format error`

，请参考如下changelog 格式:

**注意：Type字段只能是bugfix, security, other**

```
* Thu Oct 12 2023 wynnfeng <wynnfeng@tencent.com> - 0.16-6
- [Type] bugfix
- [DESC] fix xxx problem
```


- 错误：
`version xxx is not greater than xxx`

: 说明spec的Version比旧包的小 - 错误：
`release xxx is not greater than xxx`

: 说明Version一致, spec的Release比旧包小 - 错误：
`release xxx is not 1`

: 说明Version增加, Release应为1

#### 3.3.2 source失败

rpm仓库的源码包存放在文件服务器中，通过在仓库中的`sources`

文件中配置文件名和HASH值确定。

```
SHA512 (systemd-253.tar.gz) = 3bbc431a292ab590b70d3b490a528f71d30ccf478ddfa66d1c210f40c260ef49ac30651c19f2d073acf38d68398a4a6fbf95391f0e3ea0333d94b9d4e81d514f
```


如果该步骤失败，需要确认以下情况

- 是否已将源码文件上传到文件服务器中
- sources文件中是否配置了正确的文件名和SHA512值

例如，出现以下报错和日志，说明spec文件中的`Source0`

字段指定的源码压缩包文件缺失，需要修改sources文件中的对应内容。

```
2024-05-16 09:48:31,567 - [32mINFO[0m - beakerlib - BuildSRPM output: RPM build errors:
2024-05-16 09:48:31,567 - [31mERROR[0m - beakerlib - Failed to build beakerlib SRPM
2024-05-16 09:48:31,567 - [31mERROR[0m - beakerlib - BuildSRPM error: error: Bad file: /home/jenkins_worker/jenkins_workspace/workspace/OCS-Gitee-Gate-CI/5910/rpmbuild/SOURCES/1.29.3.tar.gz: No such file or directory
Bad file: /home/jenkins_worker/jenkins_workspace/workspace/OCS-Gitee-Gate-CI/5910/rpmbuild/SOURCES/1.29.3.tar.gz: No such file or directory
```


如果排除上述问题后，该项仍然失败，请联系门禁管理员。

#### 3.3.3 srpmbuild检查失败

source rpm制作是编译的前序步骤，可以通过本地执行进行问题排查。 srpm包制作流程参考以下命令：

```
rpmdev-setuptools
cd your-project
cp *spec ~/rpmbuild/SPECS/
cp * ~/rpmbuild/SOURCES/
rpmbuild -bs ~/rpmbuild/SPECS/your-project.spec
```


#### 3.3.4 rpmbuild失败

该步骤为使用上一步骤生成的srpm包提交给koji执行编译任务。 如果该步骤失败，可以点击下图中的链接进入koji任务查看

#### 3.3.5 install失败

该步骤会将编译出来的rpm包进行dnf安装测试，如果该步骤失败，通过以下步骤查找日志：

- 点击install检查的详情链接

#### 3.3.6 compatibility失败

该项检查目前主要分为七个子检查，主要检查当前提交的版本与上一个版本之间的兼容性差异。 每一个子检查都对应具体的详细日志的链接，如下图红框：

##### 3.3.6.1 subrpmlist失败

如果subrpmlist失败，说明相比于上一个版本，该次提交的版本造成了子包的增加或者删除，在`rpmlist`

日志中会找到如下日志

```
[2023-11-02T09:32:27.781Z] 旧包的包列表：4, 详情：['mockito-3.12.4-4.ocs23.noarch.rpm', 'mockito-inline-3.12.4-4.ocs23.noarch.rpm', 'mockito-3.12.4-4.ocs23.src.rpm', 'mockito-javadoc-3.12.4-4.ocs23.noarch.rpm']
[2023-11-02T09:32:27.781Z] 新包的包列表：5, 详情：['mockito-javadoc-3.12.4-5.ocs23.noarch.rpm', 'mockito-inline-3.12.4-5.ocs23.noarch.rpm', 'mockito-3.12.4-5.ocs23.noarch.rpm', 'mockito-3.12.4-5.ocs23.src.rpm', 'mockito-junit-jupiter-3.12.4-5.ocs23.noarch.rpm']
[2023-11-02T09:32:27.781Z] 2023-11-02 17:32:27,757 - [31mERROR[0m - mockito - check_subrpmlist failed
```


`packages`

字段来排查，例如
```
%package libs
```


##### 3.3.6.2 filelist失败

该项检查如果失败，说明相同rpm包中打包的文件发生了变化，在`filelist_rpmdiff`

日志中会找到如下日志

可以搜索 `list files are removed`

/ `list files are added`

字段匹配到具体日志。
打包的文件通常是由spec文件中的`files`

字段指定，例如

```
%files devel
```


对应的 `rpm-check`

检查命令为

```
rpm-check --checkfile /path/A.rpm /path/B.rpm
or
rpm-check --checkfile --dir1 old/ --dir2 new/
```


`rpmdiff.log`

中，会存在以下几种情况：
- 新增文件,
`list files are added`

- 删除文件,
`list files are removed`

- 版本变化,
`version of list files is changed`


例如： https://gitee.com/opencloudos-stream/mockito/pulls/1

##### 3.3.6.3 ability失败

该项检查如果告警或者失败，说明相比于上一个版本，该rpm包所提供的能力发生了变化，在`ability_rpmdiff`

日志中会找到如下日志

可以搜索`list requires/provides are in`

字段匹配到具体日志
也可以本地通过`rpm -qR`

或者`rpm -qP`

命令检查确认

对应的 `rpm-check`

检查命令为

```
rpm-check --checkability /path/A.rpm /path/B.rpm
or
rpm-check --checkability --dir1 old/ --dir2 new/
```


`rpmdiff.log`

中，会存在以下几种情况：
- 新增能力，
`list requires/provides are added`

- 删除能力，
`list requires/provides are removed`


##### 3.3.6.4 abi失败

该项检查如果失败，说明rpm包中的动态库发生了兼容性变化，在`summary`

日志中会找到如下日志，打印了ABI变化的的动态库以及变化比例，`Binary compatibility`

不为100%即认为ABI不兼容。

```
[2023-11-06T03:55:18.047Z] Preparing, please wait ...
[2023-11-06T03:55:18.047Z] Comparing ABIs ...
[2023-11-06T03:55:18.047Z] Comparing APIs ...
[2023-11-06T03:55:18.047Z] Creating compatibility report ...
[2023-11-06T03:55:18.047Z] Binary compatibility: 75%
[2023-11-06T03:55:18.047Z] Source compatibility: 100%
[2023-11-06T03:55:18.047Z] Total binary compatibility problems: 1, warnings: 0
[2023-11-06T03:55:18.047Z] Total source compatibility problems: 0, warnings: 0
[2023-11-06T03:55:18.047Z] Report: compat_reports/filter-aaaa.so/9.18.18-2.ocs23_to_9.18.18-3.ocs23/compat_report.xml
[2023-11-06T03:55:18.047Z] ======================================== bind-9.18.18-2.ocs23.x86_64.rpm ========================================
```


动态库名`filter-aaaa.so`

在路径中可以看到，最后分割线中的为所属的rpm包名。

对应的 `rpm-check`

检查命令为

```
## 批量检查（**推荐**）
rpm-check --checkabi --dir1 old/ --dir2 new/
## 通过debuginfo包（推荐）
rpm-check --checkabi A.rpm B.rpm --d1 A-debuginfoXXX.rpm --d2 B-debuginfoXXX.rpm
## 通过devel包
rpm-check --checkabi A.rpm B.rpm --d1 A-develXXX.rpm --d2 B-develXXX.rpm
## 指定符号粒度检查变化影响范围 (查找范围为yum源内软件包，需要配置yum源)
rpm-check --checkabi --dir1 old/ --dir2 new/ --with-symbol
## 直接通过url链接检查
rpm-check --checkabi http://9.135.76.60/var/lib/mock/tss-1-master-build-repo_latest/root/home/webkitgtk/javascriptcoregtk4.0-2.38.2-5/javascriptcoregtk4.0-2.38.2-5.ocs23.x86_64.rpm http://9.135.76.60/var/lib/mock/tss-1-master-build-repo_latest/root/home/webkitgtk/javascriptcoregtk4.0-2.38.2-5/javascriptcoregtk4.0-2.41.6-1.ocs23.x86_64.rpm --d1 http://9.135.76.60/var/lib/mock/tss-1-master-build-repo_latest/root/home/webkitgtk/javascriptcoregtk4.0-2.38.2-5/javascriptcoregtk4.0-debuginfo-2.38.2-5.ocs23.x86_64.rpm --d2 http://9.135.76.60/var/lib/mock/tss-1-master-build-repo_latest/root/home/webkitgtk/javascriptcoregtk4.0-2.38.2-5/javascriptcoregtk4.0-debuginfo-2.41.6-1.ocs23.x86_64.rpm
## 指定动态库检查
rpm-check --checkabi libssh-0.9.6-1.ocs23.x86_64.rpm_extracted/usr/lib64/libssh.so.4.8.7 libssh-0.10.4-1.ocs23.x86_64.rpm_extracted/usr/lib64/libssh.so.4.9.4 --d1 libssh-debuginfo-0.9.6-1.ocs23.x86_64.rpm --d2 libssh-debuginfo-0.10.4-1.ocs23.x86_64.rpm
```


下面解释`summary.log`

中出现下面几种情况的日志以及对应的含义

###### 有变化且有影响

1 外部符号变化，有影响包

如果有如下日志，说明当前包中的ABI发生了变化，并且此变化对外部其他依赖他的软件包产生了影响

```
Following packages are affected by ABI difference:
+------------------+---------------------------------------+-------------------------------------------+
| Package Name | Related file | Symbol |
+------------------+---------------------------------------+-------------------------------------------+
| mod_proxy_html | mod_proxy_html.so | htmlCreatePushParserCtxt@@LIBXML2_2.4.30 |
+------------------+---------------------------------------+-------------------------------------------+
| nghttp2 | nghttp | htmlCreatePushParserCtxt@@LIBXML2_2.4.30 |
+------------------+---------------------------------------+-------------------------------------------+
| php-xml | dom.so | htmlCtxtUseOptions@@LIBXML2_2.6.0 |
+------------------+---------------------------------------+-------------------------------------------+
```


2 动态库soname变化

如果有如下日志，说明当前包中的动态库soname发生变化，只要有软件包依赖当前库，就一定会有兼容性问题

```
[WARNING] Library soname version changed from [libbfd-2.38.so] to [libbfd-2.40.so]
```


###### 有变化但无影响

1 外部符号变化，但无影响包

如果有如下日志，说明当前包对外暴露的符号发生了变化，但是未找到受影响的软件包，需要结合CI重编来确认影响

```
No packages found affected by changed symbols.
```


2 内部符号变化

```
ABI affected Symbols are in private header files. They can only be used internally
```


###### 特殊情况

1 debuginfo包缺失

如果有如下日志，说明当前包无debuginfo包，无法进行兼容性检查，需要人工确认兼容性

```
No debug info of {file} in given .debug, please use devel pkg.
```


2 旧包中的库未在新包中找到

如果有如下日志，说明当前包中有库删除或者重命名，需要通过CI重编确认影响

```
is not found in new rpm. If the name of library is not changed, please contact the administrator.
```


3 动态库软连接被破坏

如果有如下日志，说明当前包中有库的软连接被破坏，需要人工确认兼容性

```
Library {file_b_lib} changes to a broken symlink in {file_b}
```


4 无法区分对外对内符号

如果有如下日志，说明当前包无devel包，无法区分受影响的符号是内部使用还是外部使用，需要通过CI测试重编确认影响

```
devel pkg XXX not found, please check affected symbols which may be in private headers.
```


5 当前不支持检查的软件包

如果有如下日志，说明当前包的语言类型不支持兼容性检查，需要人工确认兼容性

```
{rpm_name} is not supported by ABI check, please review it manully.
```


###### 如何解读abidiff详细日志

在`abidiff`

日志中会打印出具体的变化内容：

```
Processing source report...
Test library: libxml2.so.2.10.4
Test Version: 2.10.4-4.ocs23 VS 2.11.5-1.ocs23
Test Results:
Headers:
- c14n.h
- catalog.h
- chvalid.h
- debugXML.h
- dict.h
- encoding.h
- entities.h
- globals.h
...
...
Libs:
- libxml2.so.2.10.4
Symbols: 1670
Types: 431
Verdict: incompatible
Affected: 3.2
Removed Symbols:
Header: parserInternals.h
Library:
Symbol: xmlErrMemory
Library: libxml2.so.2.10.4
Symbol: __xmlErrEncoding
Header: xmlerror.h Library: libxml2.so.2.10.4
Symbol: __xmlSimpleError
Symbol: __xmlRaiseError
Problems with severity 'High':
Header: entities.h
Type: struct _xmlEntity, Problem: Renamed_Field, Change: Field checked has been renamed to flags.
Affected Symbol: getEntity, Comment: Return value (pointer) has base type struct _xmlEntity.
Affected Symbol: getParameterEntity, Comment: Return value (pointer) has base type struct _xmlEntity.
Affected Symbol: xmlAddDocEntity, Comment: Return value (pointer) has base type struct _xmlEntity.
Affected Symbol: xmlAddDtdEntity, Comment: Return value (pointer) has base type struct _xmlEntity.
Affected Symbol: xmlDumpEntityDecl, Comment: 2nd parameter ent (pointer) has base type struct _xmlEntity.
Affected Symbol: xmlGetDocEntity, Comment: Return value (pointer) has base type struct _xmlEntity.
Affected Symbol: xmlGetDtdEntity, Comment: Return value (pointer) has base type struct _xmlEntity.
Affected Symbol: xmlGetParameterEntity, Comment: Return value (pointer) has base type struct _xmlEntity.
Affected Symbol: xmlGetPredefinedEntity, Comment: Return value (pointer) has base type struct _xmlEntity.
Affected Symbol: xmlHandleEntity, Comment: 2nd parameter entity (pointer) has base type struct _xmlEntity.
```


该文件主要分为几个部分

- Headers 涉及的头文件
- Libs 检查的动态库
- Verdict 是否兼容
- Affected 影响分数
- Removed/Added Symbols 删除/新增的符号
- Problems with severity XXX 变化的符号以及具体变化内容

其中`Problems with severity XXX`

单独介绍，以上面的日志为例：

第一行，兼容性变化等级：ABI/API问题分为4个等级，其中除了`Safe`

等级外，其他的问题都被认为存在兼容性问题，这里等级为High，表示大概率会造成兼容性影响的变化

```
Problems with severity 'Safe':
Problems with severity 'Low':
Problems with severity 'Medium':
Problems with severity 'High':
```


第二行，问题位置：问题存在于头文件`entities.h`

中

```
Header: entities.h
```


第三行，涉及的结构体为`struct _xmlEntity`

，具体的问题是该结构体中有一个成员`checked`

被重命名成了`flags`


```
Type: struct _xmlEntity, Problem: Renamed_Field, Change: Field checked has been renamed to flags.
```


第三行及以后，变化所造成的影响：影响了哪些函数符号，比如`getEntity`

，原因为他的返回值含有`struct _xmlEntity`


```
Affected Symbol: getEntity, Comment: Return value (pointer) has base type struct _xmlEntity.
```


然后结合源码，定位思路一般是：影响的函数符号-->涉及的参数-->变化的结构体成员

注意，这里的变化不一定为当前提交产生，也可能是编译依赖变化导致，可参考https://gitee.com/opencloudos-stream/mod_security/pulls/4

如果对该项检查仍有疑问，请联系门禁管理员。

##### 3.3.6.5 api失败

###### C/C++/JAVA 兼容性检查结果

该项检查如果失败，说明该版本相比于上一个版本，API接口发生了变化，在`summary`

日志中有与ABI检查一样的打印，不同的是，在对动态库的检查中`Source compatibility`

不为100%，而不是`Binary compatibility`

。

```
Source compatibility: 97.8%
```


关于API详细变化的日志与ABI一样可以在`abidiff`

中查看。

对应的 `rpm-check`

检查命令与ABI检查相同。

###### Python 兼容性检查结果

如果在`summary`

中发现如下日志，说明该包中的python文件发生了API变化，并且对外部包产生了影响，需要结合CI测试重编确认影响

```
[WARNING] Function django.utils.timezone.*utc found in RPM package: python3-openstack_auth, file: /tmp/tmphzblwo38/python3-openstack_auth/usr/lib/python3.11/site-packages/openstack_auth/utils.py
```


如果需要详细确认python文件变化，需要进入具体的流水线日志查看，进入链接后进入下图位置：

详细的变化会以表格形式打印出

- [Class]前缀表示类
- @前缀表示有装饰器装饰的函数
- *前缀表示变量

```
+------------------------------------------------------------------------+-------------------------------------+-------------------+------------------------------------------+
| File | Added Symbols | Removed Symbols | Changed Symbols |
+------------------------------------------------------------------------+-------------------------------------+-------------------+------------------------------------------+
| usr/lib/python_[pyversion]/site-packages/oslo_concurrency/lockutils.py | AcquireLockFailedException.__str__ | *ReaderWriterLock | internal_lock(2 -> 3) severity:Low |
| | ReaderWriterLock.__init__ | | contextmanager@lock(8 -> 9) severity:Low |
| | AcquireLockFailedException.__init__ | | synchronized(7 -> 8) severity:Low |
| | [Class] ReaderWriterLock | | |
| | [Class] AcquireLockFailedException | | |
+------------------------------------------------------------------------+-------------------------------------+-------------------+------------------------------------------+
```


对应的 `rpm-check`

检查命令与ABI检查相同。

Python兼容性主要检查以下几个维度：

-
类、函数符号变化

-
变量变化

-
参数数量变化

-
文件变化


函数符号变化包括：

-
函数增加

-
函数删除


变量变化包括：

-
函数增加

-
函数删除


参数数量变化检查范围包括：

-
必须参数

-
可选参数


文件变化包括：

- python模块文件新增和删除

##### 3.3.6.6 executable失败

该项检查如果失败，说明该版本中的可执行文件，相比于上一个版本，执行--help/-h/-v命令输出发生了变化

##### 3.3.6.7 conf失败

该项检查如果失败，说明该版本中的配置文件相比于上一个版本发生了变化，配置文件类型主要包括以下：

- .conf后缀文件
- .yaml后缀文件
- .xml后缀文件
- .json后缀文件
- macros.开头文件
- /etc/、/usr/lib/systemd/目录下文件

在`[arch]_conf`

日志中会出现以下日志

```
Configuration file differences for XXX.conf
```


-
以下日志说明配置项 {key} 被删除

`{key} is missing in the second file`

-
以下日志说明配置项 {key} 的值变更，由XXX变为YYY

`{key} has different values: XXX != YYY`

-
以下日志说明 {key} 为新增配置项

`{key} is missing in the first file`

-
以下日志说明 {section} 为新增配置项


```
Section {section} added
```


- 以下日志说明 {section}.{option} 为新增配置项

```
Option {section}.{option} added
```


例如： https://gitee.com/opencloudos-stream/xbean/pulls/1

对应的 `rpm-check`

检查命令为

```
rpm-check --checkconf --dir1 old/ --dir2 new/
```


`confdiff.log`

。
## 4. 重编测试

部分包、库如果发生兼容性变化，会通过重编依赖他们的包的方式检查。 出现下列情况时会触发重编测试：

### 4.1 因兼容性变化

因A兼容性变化，那些编译/运行依赖A包的其他软件包，受到影响需要重编测试

- 包提供能力(provides)删除
- 包ABI发生变化
- 包API发生变化
- 可执行文件输出发生变化(--help/-h/-v)
- 宏文件发生变化

### 4.2 因runtime_require&check导致的重编测试

软件包B运行依赖A，且B的spec文件的%check阶段可能用到A

上述重编测试失败的包，会在PR合入之后自动加入正式重编


## 5. 正式重编

如果包因为ABI变化需要正式重编，CI流水线会创建对应的issue来通知以及跟踪。

## 6. 其余常见问题

待补充