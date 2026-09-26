source: https://docs.opencloudos.org/contribution/stream/use-ocspkg-to-build/

# ocspkg 使用指南

ocspkg 是一个与 RPM 打包系统交互的脚本。 在打包过程中，需要 git/koji 账户认证、代码/源码包管理、mock/koji 编译等, ocspkg 基于 rpkg 将 gitee 和 koji 联通起来，从而实现类似 git、koji、mock 一体化工具。

## 安装 ocspkg

```
sudo dnf install ocspkg
```


## 申请账号

freeipa账户注册

## 配置环境

### git配置

```
- gitee公钥配置
- 个人机器，本地用户姓名、邮箱配置：
```


```
# ssh生成本机秘钥，提交公钥到gitee
# 本地姓名、邮箱配置
git config --global user.email <useremail>@tencent.com
git config --global user.name <username>
```


### koji配置

#### 安装

配置kerberos客户端： 安装：

```
dnf install -y krb5-libs krb5-client #安装kerberos认证
dnf install -y mock koji rpm-build #安装koji、mock、rpmbuild
```


注册freeipa账户，注册链接https://accounts.opencloudos.tech/?tab=register

**注：freeipa注册的 账户名, 建议和 gitee的namaspace 保持一致**
gitee的namespace：点击gitee个人主页，网址的末尾名称即 namespace。如主页网址 "https://gitee.com/ocs-bot", 则为 ocs-bot。

#### kinit初始化

注册freeipa后， kinit

#### 配置修改

修改配置文件/etc/krb5.conf，内容如下:

```
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


修改配置文件krb5.conf后，执行 klist 查看：

```
klist //如下输出表明配置完成
Ticket cache: KCM:0:86421
Default principal: <username>@OPENCLOUDOS.TECH
Valid starting Expires Service principal
09/05/22 06:52:18 09/06/22 06:51:58 krbtgt/OPENCLOUDOS.TECH@OPENCLOUDOS.TECH
09/05/22 06:52:42 09/06/22 06:51:58 HTTP/build.opencloudos.tech@OPENCLOUDOS.TECH
# 注：若kinit时报错“kinit: Credential cache directory /run/user/0/krb5cc does not exist while getting default ccache”，可手动创建该缓存目录
# mkdir /run/user/$(id -u)/krb5cc -p
# bash-5.1# chmod 750 /run/user/$(id -u)/krb5cc
# bash-5.1# chown $(id -u):$(id -g) /run/user/$(id -u)/krb5cc
```


修改 /etc/koji.conf

```
[koji]
server = https://build.stream.opencloudos.tech/kojihub
weburl = https://build.stream.opencloudos.tech/koji
topurl = https://build.stream.opencloudos.tech
authtype = kerberos
principal = <username>@OPENCLOUDOS.TECH
```


# 配置文件修改如上，使用 kinit 初始化

```
kinit <username> //输入密码
koji -d hello //出现如下输出表示，koji配置完成，enjoy it
2022-09-05 06:52:42,671 [DEBUG] koji: Opening new requests session
2022-09-05 06:52:42,672 [DEBUG] koji: Opening new requests session
successfully connected to hub
hello, <username>!
You are using the hub at https://build.opencloudos.tech/kojihub
Authenticated via GSSAPI
```


### mock配置

添加mock编译时cfg文件（以x86架构为例），将前文生成 mock.cfg 拷贝到指定目录：

```
cp /path/to/mock.cfg /etc/mock/opencloudosstream-x86_64.cfg
```


## 使用方式

当前支持指令

```
Git-like commands:
- clone
- co: clone alias.
- sources: download tarball.
- upload: upload tarball, append to the sources file.
- new-sources: upload tarball, override in the sources file.
- diff
- commit
- push
Mock-like commands:
- prep
- srpm
- local: locally test run of rpmbuild producing binary RPMs.
- mockbuild: local test build using mock.
Koji-like commands:
- scratch-build
- build --scratch
```


## QA问题

(1) clone仓库失败，gitee账户和freeipa账户不一致怎么办？

ocspkg clone xx时，需要先fork该仓库，并且gitee的 namespace 需要和 koji账户用户名一致，否则 git clone 仓库时找不到正确仓库地址。 因此，建议注册freeipa时，和gitee账户的namespace同名。

如果由于某一账户名已被占用，是在无法保障gitee和freeipa不一致，可使用如下方法：

【解决】 修改 vim /etc/rpkg/ocspkg.conf 文件中的 gitbaseurl = git@gitee.com:%(user)s/%(repo)s.git ，将%(user)s替换为 gitee的namespace名称，保存退出即可。

(2) 上传tarball、执行koji编译时，提示 "Request is unauthorized"

因为kerberos的票据有效期默认为24h，过期后需要重新认证。

【解决】 执行 kinit初始化 重新认证即可。

如果觉得24h有效期太短，也可以修改/etc/krb5.conf文件中的 ticket_lifetime配置项，对过期时间进行调节。