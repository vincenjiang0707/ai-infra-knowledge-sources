source: https://docs.opencloudos.org/en/OCS/Virtualization_and_Containers_Guide/CCP_Hygon_UserGuide/

# 1. 介绍

机密计算主要功能是对内存进行加密。依托特定的加密硬件，每个虚拟机可以生成自己的密钥对自己的内存进行加密，这样 host 不持有密钥的话也 无法访问 guest 被密钥加密的内存，确保了就算虚拟机发生了逃逸拿到了host的权限也无法访问其他的虚拟机.

# 2. 环境要求

| 要求 | 参考命令 | |
|---|---|---|
| 海光CPU | 2代及以上(72xx,73xx,74xx)，1代不行(71xx) | grep -i "model name" /proc/cpuinfo | sort | uniq |
| 操作系统 | 确保自己使用的物理机OC 9.2 以上 | cat /etc/os-release |
| 内核 | 6.6.x 内核以上 | uname -r |
| BIOS 设置 | HYGON CBS -> Moksha Common Options 中设置 ASID Space Limit 为 1，设置 SMEE Control 为 Enabled | N/A |
| BIOS 设置 | Setup Utility -> Advanced -> HYGON CBS -> NBIO Common Options | N/A |

# 3. 证书安装

注意:证书必须安装,主板cmos断电可能会重置证书。

## 3.1. Hygon_Devkit安装

要先参考[ftp安装方式](https://docs.opencloudos.org/User%20Guide/Hygon_Devkit/)安装devkit里面的hag软件。也可以通过如下方式安装hygon-devkit

```
sudo chmod a+w /opt
cd /opt/
git clone --depth 1 https://gitee.com/anolis/hygon-devkit.git
mv hygon-devkit hygon
cd /opt/hygon/common/install/
# install hag to /opt/hygon/bin folder
sudo ./install_hag.sh
sudo cp /opt/hygon/bin/hag /usr/bin
```


## 3.2. 导入证书

### 3.2.1. 在线导入

如果能链接外网可以直接在线导入

```
sudo /opt/hygon/bin/hag general hgsc_import
```


### 3.2.2 离线导入

针对不能链接互联网的情况，可以选择离线导入，首先进入[离线证书导入网站](https://cert.hygon.cn/hgsc)，
下载名字类似于 *“hygon-hgsc-certchain-v1.0-NUFAG24060405.bin”* 的证书，然后使用如下命令导入

```
/opt/hygon/bin/hag general hgsc_import -offline -in ./hygon-hgsc-certchain-v1.0-NUFAG24060405.bin
```


### 3.2.3 检查证书

证书导入后通过如下命令检测证书

```
sudo /opt/hygon/bin/hag csv platform_status
```


## 3.3 csv虚拟机测试内存加密

目前oc官方源的软件已经合入了海光机密相关的patch，可以直接使用

### 3.3.1 安装依赖软件

```
# 安装依赖软件
sudo dnf install -y livirt qemu python-pip telnet
pip instsall qmp snowland-smx
sudo systemctl start libvirtd
sudo systemctl enable libvirtd
```


从sftp下载ovfm,并解压

```
tar -xvf ovmf.tar.gz
```


准备UEFI启动的qcow镜像

### 3.3.2. 启动一个普通虚拟机

```
qemu-system-x86_64 -name normal-vm --enable-kvm -cpu host \
-m 2048 -hda ocvm.qcow2 \
-drive if=pflash,format=raw,unit=0,file=/root/vm/ovmf/OVMF_CODE.fd,readonly=on \
-drive if=pflash,format=raw,unit=1,file=/root/vm/ovmf/OVMF_VARS.fd \
-qmp tcp:127.0.0.1:1111,server,nowait -vnc 0.0.0.0:0 \
-nographic
```


可以通过qmp导出虚拟机的内存数据

```
# 首先进入telnet
telnet 127.0.0.1 1111
# 再输入如下命令
{ "execute" : "qmp_capabilities" }
{ "execute": "pmemsave", "arguments": {"val": 0, "size": 256, "filename": "normal.txt"} }
# 执行完后可以通过先输入 ctrl+B 再输入 quit退出
hexdump --no-squeezing normal.txt
```


### 3.3.3 启动一个CSV机密虚拟机

```
qemu-system-x86_64 -name csv-vm --enable-kvm -cpu host \
-m 2048 -hda ts4-uefi-csv.qcow2 \
-object sev-guest,id=sev0,policy=0x1,cbitpos=47,reduced-phys-bits=5 \
-machine memory-encryption=sev0 \
-drive if=pflash,format=raw,unit=0,file=ovmf/OVMF_CODE.fd,readonly=on \
-drive if=pflash,format=raw,unit=1,file=ovmf/OVMF_VARS.fd \
-qmp tcp:127.0.0.1:2222,server,nowait -vnc 0.0.0.0:1 \
-nographic
```


通过telnet dump出内存数据

```
# 首先进入telnet
telnet 127.0.0.1 2222
{ "execute" : "qmp_capabilities" }
{ "execute": "pmemsave", "arguments": {"val": 0, "size": 256, "filename": "csv.txt"} }
# 执行完后可以通过先输入 ctrl+B 再输入 quit退出
hexdump --no-squeezing csv.txt
```


可以看到内存已经被加密