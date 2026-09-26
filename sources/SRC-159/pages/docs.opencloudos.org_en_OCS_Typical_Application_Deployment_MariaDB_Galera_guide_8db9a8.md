source: https://docs.opencloudos.org/en/OCS/Typical_Application_Deployment/MariaDB_Galera_guide/

# MariaDB集群部署搭建指南

本搭建文档由 OpenCloudOS 社区用户裴志远编写及共创。

MariaDB 从 10.1 版本开始， 自带 Galera 集群方案插件， 这里我们主要通过 Galera 来实现 MariaDB 的多主集群部署。

## 一、服务器准备

为了便于描述，假设创建三台虚拟机（服务器）作为 MariaDB 集群节点：

192.168.0.11 mariadb-01

192.168.0.12 mariadb-02

192.168.0.13 mariadb-03

## 二、最小化安装 OpenCloudOS 9 系统并升级操作系统至最新版

执行命令，将操作系统更新至最新版：

```
sudo dnf update -y
```


## 三、安装 tar、MariaDB 及 Galera 软件包

MariaDB 不在系统预装范围内，需要通过如下命令安装 MariaDB Server 及 Galera：

```
sudo dnf install -y tar mariadb-server mariadb-server-galera
```


说明：OpenCloudOS 9 默认没有安装 tar，在数据同步中会使用 tar 命令，在数据库服务安装时要同时安装 tar。

## 四、配置 MariaDB 服务器

编辑 MariaDB 配置文件/etc/my.cnf.d/mariadb-server.cnf，添加以下内容：

```
vi /etc/my.cnf.d/mariadb-server.cnf
[galera]
log_bin=mysql-bin
binlog_format=ROW
default-storage-engine=innodb
innodb_autoinc_lock_mode=2
bind-address=0.0.0.0
#节点的名称
wsrep_node_name="192.168.0.11"
#节点的网络地址
wsrep_node_address="192.168.0.11"
#是否启用wsrep复制，默认值为OFF，如果要加入集群，需要开启设置为ON
wsrep_on=ON
#wsrep库的位置，不同系统路径稍有区别
wsrep_provider=/usr/lib64/galera/libgalera_smm.so
#集群的名称，同一集群中所有节点的值都相等
wsrep_cluster_name="my_galera_cluster"
#启动时要连接集群节点的地址
wsrep_cluster_address="gcomm://192.168.0.11,192.168.0.12,192.168.0.13"
#用于进行状态快照传输的方式，默认值rsync
wsrep_sst_method=rsync
```


其他集群服务器只修改 wsrep_node_name、wsrep_node_address 值，其他保持一致。

## 五、配置防火墙

防火墙开发以下端口：

4567：是 Galera 做数据复制的通讯和数据传输端口，需要在防火墙放开 TCP 和 UDP

4568：是 Galera 做增量数据传输使用的端口(Incremental State Transfer, IST)，需要防火墙放开 TCP

4444：是 Galera 做快照状态传输使用的端口(State Snapshot Transfer, SST)，需要防火墙放开 TCP

3306：数据库访问端口，需要防火墙放开 TCP

```
firewall-cmd --permanent --add-port=4567/udp &&
firewall-cmd --permanent --add-port=4567/tcp &&
firewall-cmd --permanent --add-port=4568/tcp &&
firewall-cmd --permanent --add-port=4444/tcp &&
firewall-cmd --permanent --add-port=3306/tcp &&
firewall-cmd --reload
```


## 六、关闭 selinux

需要关闭 selinux，否则主节点同步会出现错误，执行如下命令：

```
vi /etc/selinux/config
```


修改内容：

```
SELINUX=disabled
```


## 七、集群启动

第一个节点设置服务开机自行启动并启动：

```
systemctl enable mariadb
galera_new_cluster
```


其余节点：

```
systemctl enable mariadb
systemctl start mariadb
```


如其余节点启动失败时，先查询 grastate.dat 文件信息：

```
vi /var/lib/mysql/grastate.dat
```


如果文件为空，可先运行一次 galera_new_cluster，启动后停止数据库服务，此时会生成 grastate.dat 文件，修改 seqno 值为 1，safe_to_bootstrap 值为 0。

```
# GALERA saved state
version: 2.1
uuid: f9f2b746-530c-11ef-ae22-97ac8e0e3d4e
seqno: 1
safe_to_bootstrap: 0
```


重新启动：

```
systemctl start mariadb
```


备注：首次加入集群数据库启动时间较长，需耐心等待。建议设置数据库服务自动启动后，重启服务器，等待数据同步后集群服务配置完成。

## 八、测试集群

登录数据库：

```
mysql -u root -p
```


使用 show status like 'wsrep_cluster_size';查看集群节点数：

```
MariaDB [(none)]> show status like 'wsrep_cluster_size';
+--------------------+-------+
| Variable_name | Value |
+--------------------+-------+
| wsrep_cluster_size | 3 |
+--------------------+-------+
```


表示有 3 个节点在运行

## 九、重启集群

集群服务器全部关闭后再次启动，需要修改集群状态文件。在任一主机上，打开 `/var/lib/mysql/grastate.dat`

文件，修改 seqno 值为 1，safe_to_bootstrap 值为 1：

```
vi /var/lib/mysql/grastate.dat
# GALERA saved state
version: 2.1
uuid: f9f2b746-530c-11ef-ae22-97ac8e0e3d4e
seqno: 1
safe_to_bootstrap: 1
```


重新启动集群：

```
galera_new_cluster
```


其他主机修改 seqno 值为 1，safe_to_bootstrap 值为 0：

```
# GALERA saved state
version: 2.1
uuid: f9f2b746-530c-11ef-ae22-97ac8e0e3d4e
seqno: 1
safe_to_bootstrap: 0
```


重新启动：

```
systemctl start mariadb
```