source: https://docs.opencloudos.org/OCS/Network_Guide/DHCP_config/

# DHCP服务配置指南

## 1 DHCP 服务配置

动态主机配置协议(DHCP)是一种网络协议，可以自动向客户端分配 IP 信息。 配置 DHCP 服务，需先安装 dhcp-server 软件包。

```
dnf install dhcp-server
```


- DCHPv4
- 配置文件：
`/etc/dhcp/dhcpd.conf`

- 服务名称： dhcpd

- 配置文件：
- DCHPv6
- 配置文件：
`/etc/dhcp/dhcpd6.conf`

- 服务名称： dhcpd6

- 配置文件：

可以根据需要单独或同时运行 dhcpd 或 dhcpd6 服务。

配置文件修改完成后，需要使用以下命令启动 dhcpd 或 dhcpd6 ：

```
systemctl start dhcpd
systemctl start dhcpd6
```


```
systemctl restart dhcpd
systemctl restart dhcpd6
```


```
systemctl enable dhcpd
systemctl enable dhcpd6
```


### 1.1 简单配置

编辑 `/etc/dhcp/dhcpd.conf`

配置文件，使用以下简单配置让 DHCP 服务器在网络中分配 IPv4 地址。

```
default-lease-time 600;
max-lease-time 7200;
option domain-name "example.com";
option domain-name-servers 192.168.1.1;
option broadcast-address 192.168.1.255;
option routers 192.168.1.1;
option subnet-mask 255.255.255.0;
subnet 192.168.1.0 netmask 255.255.255.0
{
range 192.168.1.10 192.168.1.20;
range 192.168.1.100 192.168.1.200;
}
```


配置文件的内容可以分为参数、选项和声明三个类型。

**参数：**参数可以定义为全局，对没有定义对应参数的声明生效。也可以在定义在子网等声明中，只对当前声明生效。

`default-lease-time`

默认租赁时间，单位为秒。客户端设备在未请求特定租赁时间时，DHCP服务器默认分配的IP地址的使用时间。`max-lease-time`

客户端设备可以申请使用由DHCP服务器分配的IP地址的最长时间，单位为秒。

**选项：**选项可以定义为全局，对没有定义对应选项的声明生效。也可以在定义在子网等声明中，只对当前声明生效。

`option domain-name`

指定分配给客户端的域（domain-search）。`option domain-name-servers`

指定分配给客户端DNS 服务器地址，最多指定三个值，以逗号隔开`option broadcast-address`

指定分配给客户端的广播地址。`option routers`

，指定分配给客户端的默认网关。`option subnet-mask`

，指定分配给客户端的网络掩码。

**声明：**

`subnet`

声明子网`range`

子网中分配给客户端的 IP 地址的地址范围


更多配置方法参考 `/usr/share/doc/dhcp-server/dhcpd.conf.example`

示例配置文件

### 1.2 为主机分配静态地址

可以添加 `host`

声明，来为主机的 MAC 地址分配固定 IP 地址。

```
host server.example.com {
hardware ethernet 62:10:6d:36:aa:cf;
fixed-address 192.168.1.2
}
```


`host`

声明主机，主机名称可以设置为不与其它`host`

声明匹配的任何字符串`hardware ethernet`

主机的MAC地址`fixed-address`

分配给具有主机MAC地址的IP


### 1.3 为其他子网提供 DHCP 服务

可以添加 `shared-network`

声明，来为不能直接连接的其他子网提供 DHCP 服务。

```
subnet 192.168.1.0 netmask 255.255.255.0 {
}
shared-network example {
...
subnet 192.168.2.0 netmask 255.255.255.0 {
range 192.168.2.20 192.168.2.100;
option domain-name-servers 192.168.2.1;
option routers 192.168.2.1;
}
subnet 192.168.100.0 netmask 255.255.255.0 {
range 192.168.100.20 192.168.100.100;
option domain-name-servers 192.168.100.1;
option routers 192.168.100.1;
}
...
}
```


`shared-network`

中指定的远程子网。`shared-network`

中的 192.168.2.0/24 和 192.168.100.0/24 子网是不能直接连接的远程子网。这两个子网的 DHCP 中继代理可以将 DHCP 请求转发到此 DHCP 服务来获取 DHCP 服务。
### 1.4 使用 group 声明应用参数

简单配置章节中有说明参数可以定义为全局，对没有定义对应参数的声明生效。也可以在定义在子网等声明中，只对当前声明生效。
如果想要将参数应用到多个主机、子网和共享网络，且不是应用到全局，可以使用 `group`

声明，将多个主机、子网和共享网络放到group 声明中，同时添加需要应用的参数。

```
group {
option domain-name-servers 192.168.1.1;
subnet 192.168.1.0 netmask 255.255.255.0
{
range 192.168.1.10 192.168.1.20;
range 192.168.1.100 192.168.1.200;
}
host server.example.com {
hardware ethernet 62:10:6d:36:aa:cf;
fixed-address 192.168.1.2
}
shared-network example {
...
subnet 192.168.2.0 netmask 255.255.255.0 {
range 192.168.2.20 192.168.2.100;
option routers 192.168.2.1;
}
subnet 192.168.100.0 netmask 255.255.255.0 {
range 192.168.100.20 192.168.100.100;
option routers 192.168.100.1;
}
...
}
}
```


### 1.5 租期数据库

`/var/lib/dhcpd/dhcpd.leases`

是 DHCP 服务器用于存储已分配 IP 地址租约信息的文件，记录了从服务器分配给网络中客户端设备的 IP 地址和租期。

可以通过运行以下命令查看文件的内容：

```
# cat /var/lib/dhcpd/dhcpd.leases
authoring-byte-order little-endian;
lease 192.168.1.10 {
starts 2 2023/05/23 10:52:46;
ends 2 2023/05/23 11:02:46;
tstp 2 2023/05/23 11:02:46;
cltt 2 2023/05/23 10:52:46;
binding state free;
hardware ethernet b2:f2:3b:b6:02:a7;
uid "\001\262\362;\266\002\247";
}
server-duid "\000\001\000\001+\377J8b\020m6\252\317";
```


- lease：已分配的 IP 地址。
- starts：租约分配时间。
- ends：租约到期时间。
- tstp： 有效终止时间。不一定等于租约到期时间。客户端释放租约或服务器撤销租约时，租约可能在到期时间之前终止。
- cltt：客户端上次更新时间，客户端设备最近执行的租约更新、续租或其他操作的时间。用于跟踪客户端在租约生命周期内的租约活动。
- binding state 租约的当前状态
- active：租约当前处于活动状态，表示已分配给正在使用的客户端设备。
- free：租约处于空闲状态，表示该 IP 地址在租期结束后未被重新分配，现在可用于分配给其他设备。
- expired：租约已过期，该 IP 地址可能会被回收并重新分配给其他客户端。
- abandoned：由于先前的 IP 地址冲突或其他问题而被遗弃的租约。服务器将不再主动分配此类租约。

- hardware ethernet：客户端设备的 MAC 地址。

租期数据库中的所有时间都是统一的通用时间(UTC)，而不是本地时间。

## 2 DHCP 转发代理配置

DHCP 中继代理可以将来自没有 DHCP 服务器的子网的 DHCP 请求中继到其他子网上的一个或多个 DHCP 服务器。当 DHCP 客户端请求信息时，DHCP 转发代理会将该请求转发到指定的 DHCP 服务器列表。当 DHCP 服务器返回一个回复时，DHCP 转发代理会将此请求转发给客户端。

配置 DHCP 转发代理，需要先安装 `dhcp-relay`

软件包。

```
dnf install dhcp-relay
```


- 复制 dhcrelay.service 文件到
`/etc/systemd/system/`

。`cp /lib/systemd/system/dhcrelay.service /etc/systemd/system/`

- 编辑
`/etc/systemd/system/dhcrelay.service`

文件，并追加`-i interface`

参数以及负责该子网的 DHCPv4 服务器的 IP 地址列表。如dhcrelay 会侦听 enp1s0 接口上的 DHCPv4 请求，并将它们转发到 IP 为 192.168.1.1 的 DHCP 服务器的示例如下：`ExecStart=/usr/sbin/dhcrelay -d --no-pid -i enp1s0 192.168.1.1`

- 重新加载 systemd 管理器配置：
`systemctl daemon-reload`

- 启动 dhcrelay 服务：
`systemctl start dhcrelay.service`

- 可以使用以下命令配置在系统引导时启动 dhcrelay 服务：
`systemctl enable dhcrelay.service`


## 3 常见 DHCP 问题及解决方法

### 3.1 DHCP IP 冲突问题

DHCP IP 地址冲突问题可能在以下几种情况下发生：

**静态与动态地址重叠**：静态 IP 地址与 DHCP 服务器分配的动态 IP 地址范围重叠。**多个 DHCP 服务器**：当局域网中存在多个 DHCP 服务器且它们分配的 IP 地址范围重叠时，可能为不同的设备分配相同的 IP 地址。**手动分配相同 IP 地址**：管理员人为错误地手动分配相同的 IP 地址给不同设备。

网络中 IP 地址冲突可以使用 arping 工具检测（使用方法参见网络诊断章节）。若检测到 DHCP 分配的 IP 地址冲突，尝试断开发生冲突的设备并重新连接，以触发 DHCP 服务器重新为其分配 IP 地址来临时规避 IP 冲突问题。 如检测到 ens18 网卡上，DHCP 分配的地址存在冲突：

```
# ip addr show ens18
2: ens18: <BROADCAST,MULTICAST,UP,LOWER_UP> mtu 1500 qdisc fq_codel state UP group default qlen 1000
link/ether 62:10:6d:36:aa:cf brd ff:ff:ff:ff:ff:ff
altname enp0s18
inet 192.168.1.110/24 brd 192.168.1.255 scope global noprefixroute ens18
valid_lft forever preferred_lft forever
inet6 fe80::c4da:857e:408b:edc1/64 scope link noprefixroute
valid_lft forever preferred_lft forever
# arping -I ens18 -D 192.168.1.110
ARPING 192.168.1.110 from 0.0.0.0 ens18
Unicast reply from 192.168.1.110 [02:99:96:A7:27:43] 0.803ms
Sent 1 probes (1 broadcast(s))
```


```
# nmcli connection down ens18-connection
Connection 'ens18-connection' successfully deactivated
# nmcli connection up ens18-connection
Connection successfully activated
```


```
# ip addr show ens18
2: ens18: <BROADCAST,MULTICAST,UP,LOWER_UP> mtu 1500 qdisc fq_codel state UP group default qlen 1000
link/ether 62:10:6d:36:aa:cf brd ff:ff:ff:ff:ff:ff
altname enp0s18
inet 192.168.1.111/24 brd 192.168.1.255 scope global noprefixroute ens18
valid_lft forever preferred_lft forever
inet6 fe80::c4da:857e:408b:edc1/64 scope link noprefixroute
valid_lft forever preferred_lft forever
# arping -I ens18 -D 192.168.1.111
ARPING 192.168.2.110 from 0.0.0.0 ens19
Sent 47 probes (47 broadcast(s))
Received 0 response(s)
```


要解决 DHCP IP 地址冲突问题，则要：

**检查静态 IP 分配**：确保局域网中不存在静态 IP 地址与动态 IP 地址的重叠。**规划 DHCP 服务器**：通过合并或正确配置多个 DHCP 服务器的地址分配范围来避免冲突。

### 3.2 DHCP 租期不一致

同一局域网中多个 DHCP 服务器的租期不一致可能导致如下问题：

**不均匀的 IP 地址更新**：客户端设备之间可能会出现不一致的 IP 地址更新周期，这可能会导致不均匀的网络流量。**频繁的更新和续租**：不一致的租期中如果有较短的租期可能会增加续租请求的次数，导致网络上大量的广播请求和响应，从而增加服务器和网络设备的负载。**网络管理复杂性**：具有不同租期的 DHCP 服务器会使网络管理变得更加复杂，管理员需要花费更多精力来处理这些不同租期，以确保客户端能够稳定地使用IP地址。

如果局域网中多个 DHCP 服务器，建议统一 DHCP 服务配置文件中的租期配置，确保所有 DHCP 服务器具有相同的租期设置。