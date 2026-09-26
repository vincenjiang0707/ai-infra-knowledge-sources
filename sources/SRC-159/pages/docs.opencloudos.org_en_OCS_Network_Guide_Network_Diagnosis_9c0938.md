source: https://docs.opencloudos.org/en/OCS/Network_Guide/Network_Diagnosis/

# 网络诊断指南

## 1. 使用 ping 命令测试网络连接

在 Linux 中，可以使用 `ping`

命令来测试网络连接。该命令可以向指定的 IP 地址或域名发送 ICMP 请求，并显示响应时间和丢包率等信息。以下是一个简单的例子，用于测试与 `www.google.com`

的网络连接：
`ping www.google.com`

如果网络连接正常，你将看到类似以下的输出：

```
PING www.google.com (172.217.6.196) 56(84) bytes of data.
64 bytes from lga25s62-in-f4.1e100.net (172.217.6.196): icmp_seq=1 ttl=116 time=10.5 ms
64 bytes from lga25s62-in-f4.1e100.net (172.217.6.196): icmp_seq=2 ttl=116 time=10.5 ms
64 bytes from lga25s62-in-f4.1e100.net (172.217.6.196): icmp_seq=3 ttl=116 time=10.5 ms
...
```


`ping: www.google.com: Name or service not known`

或者：
`ping: connect: Network is unreachable`

## 2. 使用 traceroute 命令跟踪网络路径

在 Linux 中，可以使用 `traceroute`

命令来跟踪网络路径。该命令可以显示从本地主机到目标主机的网络路径，以及每个路由器的 IP 地址和响应时间等信息。以下是一个简单的例子，用于跟踪到 `www.google.com`

的网络路径：
`traceroute www.google.com`

如果网络连接正常，你将看到类似以下的输出：

```
traceroute to www.google.com (172.217.6.196), 30 hops max, 60 byte packets
1 gateway (192.168.1.1) 1.000 ms 1.000 ms 1.000 ms
2 10.10.10.1 (10.10.10.1) 10.000 ms 10.000 ms 10.000 ms
3 172.16.1.1 (172.16.1.1) 20.000 ms 20.000 ms 20.000 ms
4 172.16.2.1 (172.16.2.1) 30.000 ms 30.000 ms 30.000 ms
5 172.16.3.1 (172.16.3.1) 40.000 ms 40.000 ms 40.000 ms
6 172.16.4.1 (172.16.4.1) 50.000 ms 50.000 ms 50.000 ms
......
```


```
traceroute to www.google.com (172.217.6.196), 30 hops max, 60 byte packets
1 gateway (192.168.1.1) 1.000 ms 1.000 ms 1.000 ms
2 * * *
3 * * *
4 * * *
5 * * *
```


## 3. 使用 netstat 命令查看网络连接状态

在 Linux 中，可以使用 `netstat`

命令来查看网络连接状态。该命令可以显示当前系统中的网络连接信息，包括本地 IP 地址、远程 IP 地址、连接状态等。以下是一个简单的例子，用于显示当前系统中的网络连接信息：
`netstat -a`

如果网络连接正常，你将看到类似以下的输出：

```
Active Internet connections (servers and established)
Proto Recv-Q Send-Q Local Address Foreign Address State
tcp 0 0 0.0.0.0:22 0.0.0.0:* LISTEN
tcp 0 0 192.168.1.100:22 192.168.1.101:12345 ESTABLISHED
tcp 0 0 192.168.1.100:22 192.168.1.102:54321 ESTABLISHED
...
```


```
Active Internet connections (servers and established)
Proto Recv-Q Send-Q Local Address Foreign Address State
tcp 0 0 0.0.0.0:22 0.0.0.0:* LISTEN
tcp 0 0 192.168.1.100:22 192.168.1.101:12345 TIME_WAIT
tcp 0 0 192.168.1.100:22 192.168.1.102:54321 TIME_WAIT
...
```


## 4. 使用 ss 命令查看网络连接状态

ss（socket statistics，套接字统计）是一款 Linux 系统下的网络工具，可以用于监控和调试网络连接。与传统的 netstat 命令相比，ss 在性能和信息提供方面更优秀。

常用命令如下： - 显示所有当前连接：

```
# ss
Netid State Recv-Q Send-Q Local Address:Port Peer Address:Port Process
u_str ESTAB 0 0 /run/systemd/journal/stdout 25077 * 24218
u_str ESTAB 0 0 * 20557 * 592
u_dgr ESTAB 0 0 * 23602 * 13633
......
```


-
显示所有 TCP 连接：

`ss -t`

-
显示所有 UDP 连接：

`ss -u`

-
显示所有监听中的套接字：

`ss -l`

-
显示所有已建立（ESTABLISHED）的连接：

`ss -t state established`

-
按多个状态过滤（例如：已建立且正在关闭的连接）：

`ss -t state established,closing`

-
显示进程信息，要显示哪个进程在使用套接字，请使用 -p 选项：

`ss -t -p`

-
显示更多详细信息，使用 -e 选项显示扩展信息（例如滑动窗口大小、丢包统计等）：

`ss -t -e`

-
显示套接字摘要统计信息，使用 -s 选项显示套接字摘要统计信息，如 TCP/UDP/RAW 以及连接数量等：

`ss -s`

-
结合常用过滤器，如要显示某一特定端口的连接情况，可以结合 grep 进行过滤（例如，查看端口 80 上的所有连接）：

`ss -t -a | grep ':80'`


在日常网络监控和故障排除中，可根据具体需求灵活组合选项。要查看完整的选项列表和详细说明，可访问 ss 的手册（manpage）。

## 5 使用 ethtool 查询和控制网络设备驱动和硬件设置

ethtool 是一个用于查询和控制网络设备驱动和硬件设置的实用工具。若 ethtool 未安装，使用前以下命令安装 ethtool 软件包。

```
dnf install ethtool
```


### 5.1 网络设备速度、双工模式和自动协商查询与设置

查询网络设备速度、双工模式和自动协商查询与设置：

```
# ethtool ens18
Settings for ens18:
......
Speed: 1000Mb/s
Duplex: Full
Auto-negotiation: on
......
```


修改网络设备速度、双工模式和自动协商设置：

```
ethtool -s ens18 speed 100 duplex full autoneg off
```


### 5.2 流量控制设置

查看网络设备的流量控制设置

```
ethtool -a ens18
Pause parameters for eno1:
Autonegotiate: on
RX: off
TX: off
```


修改网络的流量控制设置：

```
ethtool -A ens18 rx on tx off
```


### 5.3 Wake-on-LAN 功能设置

查寻网络设备的Wake-on-LAN 功能：

```
# ethtool ens18
Settings for ens18:
......
Wake-on: g
.....
```


开启网络设备的 Wake-on-LAN 功能：

```
ethtool -s ens18 wol d
```


```
ethtool -s ens18 wol g
ethtool -s ens18 wol d
```


### 5.4 网络设备的硬件特性

查看网络设备的硬件特性：

```
# ethtool -k ens18
Features for ens18:
rx-checksumming: on
tx-checksumming: on
tx-checksum-ipv4: off [fixed]
tx-checksum-ip-generic: on
tx-checksum-ipv6: off [fixed]
......
```


更改网络设备的硬件特性，如启用通用接收分散，通用分组传输：

```
ethtool -K ens18 tso on gso on
```


### 5.5 网络设备的统计信息

使用以下命令查看网络设备的统计信息：

```
# ethtool -S ens18
NIC statistics:
rx_packets: 399566
tx_packets: 257685
rx_bytes: 215936573
tx_bytes: 55115699
rx_broadcast: 9854
tx_broadcast: 92
......
```


### 5.6 网络设备自检

使用以下命令执行网络设备的自检：

```
# ethtool -t ens18
The test result is PASS
The test extra info:
Register test (offline) 0
Eeprom test (offline) 0
Interrupt test (offline) 0
Loopback test (offline) 0
Link test (on/offline) 0
```


## 6. 使用 tcpdump 命令诊断网络问题

tcpdump 是一个非常有用的工具，它可以捕获网络数据包并显示其内容。
以下是一些使用 `tcpdump`

的经典示例：

### 6.1 按目标主机捕获数据包

使用以下命令捕获特定目标主机的数据包：

```
tcpdump -i eth0 host www.google.com
```


`-i`

参数指定要捕获的网络接口， `host`

参数指定要捕获的目标主机。如果网络连接正常，会有类似以下的输出：
```
# tcpdump -i eth0 src host 192.168.1.100 and dst host www.google.com
tcpdump: verbose output suppressed, use -v or -vv for full protocol decode
listening on eth0, link-type EN10MB (Ethernet), capture size 262144 bytes
14:23:45.678901 IP 192.168.1.100.12345 > 172.217.6.196.80: Flags [S], seq 123456789, win 65535, options [mss 1460,nop,nop,sackOK], length 0
14:23:45.789012 IP 172.217.6.196.80 > 192.168.1.100.12345: Flags [S.], seq 987654321, ack 123456790, win 65535, options [mss 1460,nop,nop,sackOK], length 0
14:23:45.890123 IP 192.168.1.100.12345 > 172.217.6.196.80: Flags [.], ack 1, win 65535, length 0
14:23:45.901234 IP 192.168.1.100.12345 > 172.217.6.196.80: Flags [P.], seq 1:101, ack 1, win 65535, length 100
14:23:46.012345 IP 172.217.6.196.80 > 192.168.1.100.12345: Flags [.], ack 101, win 65535, length 0
...
```


```
# tcpdump -i eth0 src host 192.168.1.100 and dst host www.google.com
tcpdump: verbose output suppressed, use -v or -vv for full protocol decode
listening on eth0, link-type EN10MB (Ethernet), capture size 262144 bytes
14:23:45.678901 IP 192.168.1.100.12345 > 172.217.6.196.80: Flags [S], seq 123456789, win 65535, options [mss 1460,nop,nop,sackOK], length 0
14:23:45.789012 IP 172.217.6.196.80 > 192.168.1.100.12345: Flags [R.], seq 0, ack 123456790, win 0, length 0
```


`R`

标志表示连接被重置，这意味着网络连接存在问题。
### 6.2 按网段捕获数据包

使用以下命令捕获指定网段的的数据包：

```
tcpdump -i eth0 net 192.168.1.0/24
```


`eth0`

的 192.168.1.0/24 网络的数据包。
### 6.3 按端口捕获数据包

使用以下命令捕获通过 eth0 的 HTTP（端口 80）流量：

```
cpdump -i eth0 port 80
```


### 6.4 按指定协议捕获数据包

使用以下命令捕获 `icmp`

协议的流量：

```
tcpdump -i eth0 'icmp'
```


`icmp`

替换为要监视的其他协议（如 `tcp`

或 `udp`

）。
### 6.5 指定协议和端口捕获 DNS 或 DHCP 数据包

DNS 通常使用 UDP 协议的 53 端口进行请求。要捕获 DNS 数据包，可以运行以下命令：

```
tcpdump -i eth0 'udp port 53'
```


DHCP 请求和响应通常使用 UDP 协议的 67 和 68 端口进行通信。要捕获与 DHCP 相关的数据包，可以运行以下命令：

```
tcpdump -i eth0 'udp port 67 or udp port 68'
```


### 6.6 捕获 TCP 三次握手的数据包

可以使用以下命令捕获 TCP 三次握手（SYN、SYN-ACK、ACK）过程中的数据包：

```
tcpdump -i eth0 'tcp[tcpflags] & (tcp-syn|tcp-ack) != 0'
```


`-i`

参数指定要捕获的网络接口为 eth0，过滤器部分 `'tcp[tcpflags] & (tcp-syn|tcp-ack) != 0'`

用于检测具有 “SYN” 和 “ACK” 标志的 TCP 数据包。
### 6.7 限制捕获的数据包数量

使用 `-c`

参数指定要捕获的数据包数量：

```
tcpdump -i eth0 -c 10
```


`eth0`

的前 10 个数据包。
### 6.8 保存或读取数据包

将捕获的数据包保存到.pcap 格式文件：

```
tcpdump -i eth0 -w output.pcap
```


```
tcpdump -r output.pcap
```


## 7. 检测 IP 和 MAC 地址冲突

IP地址冲突表示有两个或更多的设备在同一局域网内分配了相同的IP地址。这种情况通常是因为以下原因之一引起的： - 静态IP地址设置错误：当一个或多个设备静态指定了相同的IP地址时，会发生IP地址冲突。 - 动态主机控制协议（DHCP）问题：例如多个 DHCP 服务器分配相同的地址。

IP地址冲突会导致如下问题： - 影响设备之间的通信，出现连接问题和丢包现象。 - 局域网中的两个设备无法同时访问网络。 - 网络速度变慢、性能降低。

可以使用以下 arping 命令检测局域网中其他服务器的 IP 是否存在地址冲突：

```
# arping -C 2 192.168.1.110
ARPING 192.168.1.110
42 bytes from 02:99:96:a7:27:43 (192.168.1.110): index=0 time=128.403 usec
42 bytes from 62:10:6d:36:aa:cf (192.168.1.110): index=1 time=168.765 usec
```


若要检测在服务器中检测当前服务器的某个网络接口的 IP 是否存在地址冲突，请使用如下命令：

```
# arping -I ens18 -D 192.168.1.110
ARPING 192.168.1.110 from 0.0.0.0 ens18
Unicast reply from 192.168.1.110 [02:99:96:A7:27:43] 0.803ms
Sent 1 probes (1 broadcast(s))
Received 1 response(s)
```


## 8 ARP 老化和永久条目

ARP 老化相关的设置决定了 ARP 缓存中 IP 地址到 MAC 地址映射关系的保留时间。当一个 ARP 条目的存在时间超过了 ARP 老化时间，系统将自动从 ARP 缓存中移除该条目，从而清除无效或不活跃的地址映射，维护了 ARP 缓存的有效性和稳定性。系统中默认的 ARP 老化时间为 60s：

```
# sysctl net.ipv4.neigh.default.gc_stale_time
net.ipv4.neigh.default.gc_stale_time = 60
```


永久 ARP 条目是手动创建的，不会受到 ARP 老化机制的影响，不会被 ARP 老化机制清除。这可以为稳定且不经常变动的设备提供稳定的地址映射关系，从而省去了重复发送 ARP 请求以获取相同的映射关系的过程。

在大多数情况下，使用默认的 ARP 老化设置是符合网络需求的。而 ARP 永久条目应在特定场景下谨慎使用，使用永久条目的设备应确保 IP 地址和 MAC 地址不会发生变化。

可以使用以下命令来查看当前的 ARP 缓存：

```
# arp -n
Address HWtype HWaddress Flags Mask Iface
192.168.1.111 ether 02:99:96:a7:27:43 CM ens18
192.168.2.1 ether c2:fd:0b:bb:a6:9c C ens19
192.168.1.1 ether 86:7a:1c:87:a8:35 C ens18
192.168.2.111 ether 02:1e:16:7d:cc:50 C ens19
```


命令输出将显示 IP 地址到硬件地址（MAC地址）的映射以及 ARP 实体的状态，如 Flags Mask 中 C 表示完全可用，M 表示正在使用的永久条目。 如果发现 ARP 因错误配置为永久条目而导致影射不正确，或要重新获取某个 IP 和 MAC 地址的映射关系，可以使用以下命令删除 ARP 条目

```
sudo arp -d 192.168.1.111
```


`192.168.1.111`

为要从 ARP 缓存中删除的设备的 IP 地址。
如果要创建永久条目， 可以使用以下命令：

```
arp -s 192.168.1.111 02:99:96:a7:27:43
```


`192.168.1.1111`

和 MAC 地址 `02:99:96:a7:27:43`

创建一个永久 ARP 条目。
创建完永久条目后，可以使用 `arp -n`

命令查看 ARP 缓存。将看到该设备的条目标记为 "M"（表示 "永久"）。