source: https://docs.opencloudos.org/contribution/how-to-contribute-oc/

# OpenCloudOS 社区版本贡献指南

## 源码管理

### 代码托管仓库

OpenCloudOS 包含多个 Organization:

- OpenCloudOS RPMS https://gitee.com/organizations/src-opencloudos-rpms/projects
- OpenCloudOS Modules https://gitee.com/src-opencloudos-modules
- OpenCloudOS 超凡桌面 https://gitee.com/opencloudos-exnde
- OpenCloudOS FoundUI https://gitee.com/opencloudos-foundui

其中 OpenCloudOS RPMS 为所有普通软件包（非 Module 包）代码存放位置，以下规范均以 OpenCloudOS RPMS 为例列举，其他 Organization 由于代码目的不同可有细微区别。

### 分支管理

OpenCloudOS 目前存在两个大版本 OpenCloudOS 8 & OpenCloudOS 9，所以在 OpenCloudOS RPMS 仓库中软件包主要存在三个分支: master、oc8、oc9（部分软件包可能不存在 oc9 分支）。其中，master 分支只存放软件包相关的 README.md 文件，oc8 和 oc9 分支分别对应 OpenCloudOS 的不同版本。

### 代码目录结构

OpenCloudOS RPMS 中每个仓库包含构建一个软件包所有信息，包括 spec 文件、patch 文件、配置文件及源码 tarball 压缩包。其中，由于源码 tarball 及部分二进制包过大且不可查看不适宜存放在 gitee 仓库管理，对于这些大文件我们**只在 gitee 仓库中存放它的索引文件**。以下以 authselect 软件包为例介绍一下代码仓库的目录结构：

authselect 软件包仓库 oc8 分支：https://gitee.com/src-opencloudos-rpms/authselect/tree/oc8/

- 目录结构：

```
# tree -a authselect/
authselect/
├── .authselect.metadata # 源码压缩包索引文件
├── .gitignore
├── SOURCES # 存放除了spec文件之外的文件（patch/配置文件）
│ ├── 0001-po-update-translations.patch
│ ├── 0901-rhel8-remove-mention-of-Fedora-Change-page-in-compat.patch
│ ├── 0902-rhel8-remove-ecryptfs-support.patch
│ ├── 0903-rhel8-Revert-profiles-add-support-for-resolved.patch
│ └── 0904-rhel8-Revert-yescrypt.patch
└── SPECS # 存放spec文件
└── authselect.spec
```


- 源码压缩包索引文件

在OpenCloudOS RPMS 中源码压缩包并不直接存放在 gitee 仓库中，而是用一个.metadata 结尾的索引文件代替，真实的压缩包存放在 source lookaside 系统中（后续会讲到），构建时构建系统根据这个索引去获取对应的源码文件。索引文件中每一行对应一个源码文件，每一行由 "`sha1sum $tarball_name | awk '{print $1}'`

SOURCES/$tarball_name" 构成。

```
# cat .authselect.metadata
9c2bb483de9209a00df4f69368245fdf3b8f635c SOURCES/authselect-1.2.6.tar.gz
```


```
# tarball_name=authselect-1.2.6.tar.gz
# echo "`sha1sum $tarball_name | awk '{print $1}'` SOURCES/$tarball_name"
9c2bb483de9209a00df4f69368245fdf3b8f635c SOURCES/authselect-1.2.6.tar.gz
```


### Gitee 贡献流程

- 注册gitee账号;
- 定位感兴趣项目；
- "Fork" 项目至个人空间；
- Fork出的项目在个人空间 edit & push；
- 发起Pull Request 到 Organizition仓库指定分支；

commit message 请按照 “[%version-%release] %changelog ” 的格式填写，方便之后查看。 eg. [0.63.0-14.oc8.1] fix module platform compatibility

【Tips】加入组织请联系 maxonxie@opencloudos.tech

## 用户认证（kerberos）

- 提供开发者邮箱，昵称；

联系 lianhaifu@opencloudos.tech 开通开发者账户，获取账号密码。

- 开发者认证配置

```
# dnf install -y krb5-libs
# vim /etc/krb5.conf
#File modified by ipa-client-install
includedir /etc/krb5.conf.d/
[libdefaults]
default_realm = OPENCLOUDOS.TECH
dns_lookup_realm = false
dns_lookup_kdc = false
rdns = false
dns_canonicalize_hostname = false
ticket_lifetime = 24h
forwardable = true
udp_preference_limit = 0
[realms]
OPENCLOUDOS.TECH = {
kdc = freeipa.opencloudos.tech:88
master_kdc = freeipa.opencloudos.tech:88
admin_server = freeipa.opencloudos.tech:749
kpasswd_server = freeipa.opencloudos.tech:464
default_domain = opencloudos.tech
pkinit_anchors = FILE:/var/lib/ipa-client/pki/kdc-ca-bundle.pem
pkinit_pool = FILE:/var/lib/ipa-client/pki/ca-bundle.pem
}
[domain_realm]
.opencloudos.tech = OPENCLOUDOS.TECH
opencloudos.tech = OPENCLOUDOS.TECH
build.opencloudos.tech = OPENCLOUDOS.TECH
```


- 获取认证session

```
kinit maxonxie
```


## 编译构建

### 构建系统

-
Kojihub https://build.opencloudos.tech/koji/

-
MBS https://mbs.opencloudos.tech/


| Name | 备注 | |
|---|---|---|
| 陶松桥 | joeytao@opencloudos.tech | ReleaseEng Manager |
| 谢仲天 | maxonxie@opencloudos.tech | Infrastructure Manager |
| 杨佳鑫 | jiaxinyyang@tencent.com | BuildSystem Manager |
| 练海富 | lianhaifu@opencloudos.tech | IDM Manager（用户认证） |

### 本地构建

使用koji导出的config文件进行mock build，测试通过后再提交koji build

- mock 配置。

x86_64 下的 mock 配置文件

```
# cat dist-oc8-mock-x86_64.cfg
config_opts['basedir'] = '/var/lib/mock'
config_opts['chroot_setup_cmd'] = 'groupinstall build'
config_opts['chroothome'] = '/builddir'
config_opts['dnf_warning'] = False
config_opts['package_manager'] = 'dnf'
config_opts['root'] = 'dist-oc8-build-repo_14403'
config_opts['rpmbuild_networking'] = False
config_opts['rpmbuild_timeout'] = 86400
config_opts['target_arch'] = 'x86_64'
config_opts['use_host_resolv'] = False
config_opts['yum.conf'] = '[main]\ncachedir=/var/cache/yum\ndebuglevel=1\nlogfile=/var/log/yum.log\nreposdir=/dev/null\nretries=20\nobsoletes=1\ngpgcheck=0\nassumeyes=1\nkeepcache=1\ninstall_weak_deps=0\nstrict=1\n\n# repos\n\n[build]\nname=build\nbaseurl=https://build.opencloudos.tech/kojifiles/repos/dist-oc8-build/14403/x86_64\nmodule_hotfixes=1\n'
config_opts['plugin_conf']['ccache_enable'] = False
config_opts['plugin_conf']['root_cache_enable'] = False
config_opts['plugin_conf']['yum_cache_enable'] = False
config_opts['macros']['%_host'] = 'x86_64-koji-linux-gnu'
config_opts['macros']['%_host_cpu'] = 'x86_64'
config_opts['macros']['%_rpmfilename'] = '%%{NAME}-%%{VERSION}-%%{RELEASE}.%%{ARCH}.rpm'
config_opts['macros']['%_topdir'] = '/builddir/build'
config_opts['macros']['%distribution'] = 'Koji Testing'
config_opts['macros']['%packager'] = 'Koji'
config_opts['macros']['%vendor'] = 'Koji'
```


```
# cat dist-oc8-mock-aarch64.cfg
config_opts['basedir'] = '/var/lib/mock'
config_opts['chroot_setup_cmd'] = 'groupinstall build'
config_opts['chroothome'] = '/builddir'
config_opts['dnf_warning'] = False
config_opts['package_manager'] = 'dnf'
config_opts['root'] = 'dist-oc8-build-repo_14417'
config_opts['rpmbuild_networking'] = False
config_opts['rpmbuild_timeout'] = 86400
config_opts['target_arch'] = 'aarch64'
config_opts['use_host_resolv'] = False
config_opts['yum.conf'] = '[main]\ncachedir=/var/cache/yum\ndebuglevel=1\nlogfile=/var/log/yum.log\nreposdir=/dev/null\nretries=20\nobsoletes=1\ngpgcheck=0\nassumeyes=1\nkeepcache=1\ninstall_weak_deps=0\nstrict=1\n\n# repos\n\n[build]\nname=build\nbaseurl=https://build.opencloudos.tech/kojifiles/repos/dist-oc8-build/14417/aarch64\nmodule_hotfixes=1\n'
config_opts['plugin_conf']['ccache_enable'] = False
config_opts['plugin_conf']['root_cache_enable'] = False
config_opts['plugin_conf']['yum_cache_enable'] = False
config_opts['macros']['%_host'] = 'aarch64-koji-linux-gnu'
config_opts['macros']['%_host_cpu'] = 'aarch64'
config_opts['macros']['%_rpmfilename'] = '%%{NAME}-%%{VERSION}-%%{RELEASE}.%%{ARCH}.rpm'
config_opts['macros']['%_topdir'] = '/builddir/build'
config_opts['macros']['%distribution'] = 'Koji Testing'
config_opts['macros']['%packager'] = 'Koji'
config_opts['macros']['%vendor'] = 'Koji'
```


PS: 以上配置文件也可以在配置了koji用户的机器上通过 `koji mock-config --tag="dist-oc8-build" -a <arch>`

生成

- 本地mock构建：

```
mock -r mock-oc8-x86_64.cfg --rebuild xxx.src.rpm 或 mock -r mock-oc8-aarch64.cfg --rebuild xxx.src.rpm
```


- lookaside 服务链接

https://git.opencloudos.tech/sources/

【Tips】路径结构是 <包名>/<分支名>/

- 上传 tarball 方法：
上传tarball需要通过统一认证，
`curl --negotiate -u : https://git.opencloudos.tech/sources/upload.cgi --form "name=test-pkg" --form "branch=oc8" --form "sha1sum=cc93e3e69d026a19de87d9456a469e306d66225b" --form "file=@test.tar.gz"`

`kinit UserName`


## Bugzilla 缺陷管理

- 访问链接 https://bugs.opencloudos.tech/
- 文档
[Bugzilla使用手册 - OpenCloudOS](https://docs.opencloudos.tech/opencloudos-8.5-lts/yong-hu-fan-kui/bugzilla-shi-yong-shou-ce)

## CI 测试系统

- 访问链接
[Dashboard [Jenkins]](https://qa.opencloudos.tech) - 说明文档 https://docs.qq.com/doc/DRXl1U2FSZEl3SnRT

## 沟通渠道

- 微信群 OpenCloudOS技术社区交流群
- 邮件列表

## CLA 贡献者许可协议

签署链接：http://cla.opencloudos.tech:8080/