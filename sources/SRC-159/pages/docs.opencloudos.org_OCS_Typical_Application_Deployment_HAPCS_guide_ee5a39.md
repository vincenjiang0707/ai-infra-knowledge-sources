source: https://docs.opencloudos.org/OCS/Typical_Application_Deployment/HAPCS_guide/

# HA(PCS)部署文档

# 第1章 集群环境搭建

## 1.1 HA简介

```
HA：High Availability,高可用；通过集群来提供服务，从而减少停工时间，保持其服务的高可用性。
```


## 1.2 节点

创建两台子机，作为集群的两个节点,两台子机需要在同一个子网

节点1：

ip：10.0.9.57

hostname: [z1.example.com](http://z1.example.com)

节点2：

ip：10.0.9.60

hostname: z2.example.com

在两台机器的/etc/hosts文件中分别做如下设置：

## 1.3 安装和启动HA软件

（1）安装

安装PCS方式的HA软件组

```
dnf clean all
dnf makecache
dnf update
dnf install -y fence-agents-all pcs pacemaker
```


（2）启动

随后启动pcsd(**两台机器均做，如果有一端不启动pcsd.server，创建集群时会报2224端口连接拒绝**)：

```
systemctl enable pcsd.service
systemctl start pcsd.service
```


## 1.3 配置和创建HA

（1）设置用户 hacluster 的密码,并进行认证(两台机器均做)：

```
passwd hacluster
```


（2）认证

```
pcs host auth -u hacluster -p 密码 z1.example.com z2.example.com
```


效果如下图即为成功：

（3）创建集群

创建名为 my_cluster 且具有一个成员的群集，并检查群集的状态(一台机器下发即可)：

```
pcs cluster setup --enable --start my_cluster z1.example.com z2.example.com
```


效果如下图即为成功：

备注：--enable表示节点启动时，集群自动启动；

（4）查看集群状态

pcs status显示如下信息：

两个节点都是Online状态，说明两个节点都在被pcs管理。

（5）删除集群

```
pcs cluster stop --all
pcs cluster destroy --all
```


备注：

(1) 配置文件：/etc/corosync/corosync.conf

(2) pcs主机名文件：/var/lib/pcsd/known-hosts

(3) 系统主机名文件：/etc/hosts

# 第2章 分配高可用虚拟IP

## 2.1 申请高可用虚拟IP

请向云服务厂商申请高可用虚拟IP网址

申请高可用虚拟IP的所在地域、私有网络与子网需要与子机一致；

本文以虚拟IP 10.0.9.55为例操作

## 2.2 环境设置

stonith-enabled默认为true，初始状态没有创建fence，导致pcs status会出现告警，此时无法分配申请的高可用虚拟IP；

pcs property --all | grep stonith

为了成功创建虚拟IP资源，需要设置stonith-enabled为false，或者创建一个fence（见第4章），这里通过设置stonith-enabled为false来实现分配虚拟IP；

pcs property set stonith-enabled=false

pcs property --all | grep stonith

## 2.3 pcs中创建虚拟IP资源

使用如下命令创建虚拟IP资源：

pcs resource create VirtualIP ocf💓IPaddr2 ip=10.0.9.55 cidr_netmask=32 op monitor interval=30s 可以看到当前申请的高可用虚拟IP资源(IP:10.0.9.55)运行在节点z1.example.com上，该节点IP为10.0.9.57；

# 第3章 主备倒换

在第2章基础上，通过如下命令给节点z1.example.com引入故障：

echo c > /proc/sysrq-trigger

约3秒钟后，此时IP资源迁移到节点z2.example.com上：

节点2上可以看到分配的高可用虚拟IP：10.0.9.55:

当前所属主机为z2.example.com，主备倒换成功。

为了后续章节测试，这里删除VirtualIP资源：

pcs resource delete VirtualIP

# 第4章 节点故障自动重启

略，请咨询各主机厂商