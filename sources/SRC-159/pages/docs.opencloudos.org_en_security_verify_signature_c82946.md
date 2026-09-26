source: https://docs.opencloudos.org/en/security/verify_signature/

# 镜像签名验证指南

## 下载镜像

从 [OpenCloudOS镜像源](https://mirrors.opencloudos.tech/) 下载需要验证的镜像和哈希值，例如：

```
$ wget https://mirrors.opencloudos.tech/opencloudos/9.2/isos/x86_64/OpenCloudOS-9.2-20240513.0-x86_64-boot.iso
$ wget https://mirrors.opencloudos.tech/opencloudos/9.2/isos/x86_64/OpenCloudOS-9.2-20240513.0-x86_64-boot.iso.sha256
```


使用 `sha256sum`

校验镜像的完整性，返回 OK 表示镜像与哈希值文件匹配：

```
$ sha256sum -c OpenCloudOS-9.2-20240513.0-x86_64-boot.iso.sha256
OpenCloudOS-9.2-20240513.0-x86_64-boot.iso: OK
```


## 获取 PGP 公钥

### 方法一：从 OpenPGP Key Server 下载

使用以下命令从 [keys.openpgp.org](https://keys.openpgp.org/) 直接下载并导入公钥：

```
$ gpg --keyserver keys.openpgp.org --recv-keys 7A556C4804B196CD87F1FB9CE6BCD4FE7B7BAC04
```


返回如下字段表示成功：

```
gpg: key E6BCD4FE7B7BAC04: public key "OCSIRT <security@opencloudos.tech>" imported
gpg: Total number processed: 1
gpg: imported: 1
```


### 方法二：从 OpenCloudOS 软件源下载

先下载公钥到本地：

```
$ wget https://mirrors.opencloudos.tech/opencloudos/keys/oc-sign.key
```


再使用 `gpg`

命令导入：

```
$ gpg --import oc-sign.key
```


## 执行验签

首先确认公钥已被正确导入：

```
$ gpg --list-keys --fingerprint E6BCD4FE7B7BAC04
pub rsa4096 2025-02-13 [SC]
7A55 6C48 04B1 96CD 87F1 FB9C E6BC D4FE 7B7B AC04
uid [ unknown] OCSIRT <security@opencloudos.tech>
```


下载签名文件，并对哈希值文件验签：

```
$ wget https://mirrors.opencloudos.tech/opencloudos/9.2/isos/x86_64/OpenCloudOS-9.2-20240513.0-x86_64-boot.iso.sha256.gpg
$ gpg --verify OpenCloudOS-9.2-20240513.0-x86_64-boot.iso.sha256.gpg OpenCloudOS-9.2-20240513.0-x86_64-boot.iso.sha256
```


如果返回 Good signature 字样，即表示签名验证成功。

## FAQ

### 公钥是否有有效期？

OpenCloudOS 社区公钥有效期为 10 年，生效日期是 2025.2.13。