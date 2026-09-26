source: https://docs.opencloudos.org/OCS/Network_Guide/Network_config/

# 网络配置指南

网络管理有两种常见的网络管理器，一种是传统的 network-scripts，另一种是满足新时代网络需求的 NetworkManager。两种网络管理均可以对网络进行永久配置。 也可以使用其他网络配置工具 ip 或 ifconfig 进行临时配置网络，其配置的网络连接信息在系统重启后会丢失。

## 1 使用 NetworkManager 配置网络

NetworkManager 是默认的网络管理器，支持多种网络配置方式，以下介绍常用的命令行工具 nmcli ，文本界面配置工具 nmtui ，和 ifcfg 文件配置网络。

### 1.1 使用 nmcli 配置网络

#### 1.1.1 查看网络设备

使用以下命令查看网络设备信息：

```
# nmcli device status
DEVICE TYPE STATE CONNECTION
ens18 ethernet connected ens18-connection
lo loopback unmanaged --
```


#### 1.1.2 查看网络连接

使用以下命令查看所有的网络连接：

```
# nmcli connection show
NAME UUID TYPE DEVICE
ens18-connection 3e7f4298-26e4-43db-9200-1e49309bc5a9 ethernet ens18
```


使用以下命令查看某个网络连接的详细信息：

```
# nmcli connection show ens18-connection
connection.id: ens18-connection
connection.uuid: 08e824aa-be05-4964-bae0-928aaac618be
connection.stable-id: --
connection.type: 802-3-ethernet
connection.interface-name: ens18
connection.autoconnect: yes
......
802-3-ethernet.port: --
802-3-ethernet.speed: 0
......
ipv4.method: manual
ipv4.dns: 192.168.1.1
ipv4.dns-search: --
ipv4.dns-options: --
ipv4.dns-priority: 0
ipv4.addresses: 192.168.1.2/24
ipv4.gateway: 192.168.1.1
ipv4.routes: --
......
ipv6.method: auto
ipv6.dns: --
......
```


#### 1.1.3 创建动态 IP 地址的网络连接

使用以下命令创建一个新的动态网络连接：

```
nmcli connection add con-name ens18-connection ifname ens18 type ethernet ipv4.method auto
```


#### 1.1.4 创建静态 IP 地址的网络连接

使用以下命令创建一个新的静态网络连接：

```
nmcli connection add con-name ens18-connection ifname ens18 type ethernet ipv4.method manual ipv4.addr 192.168.1.2/24 ipv4.gateway 192.168.1.1 ipv4.dns 192.168.1.1
```


#### 1.1.5 编辑网络连接

使用以下命令打开交互式编辑器来编辑网络连接：

```
nmcli connection edit ens18-connection
```


```
nmcli> set ipv4.addr 192.168.1.2/24
nmcli> set ipv4.gateway 192.168.1.1
nmcli> set ipv4.dns 192.168.1.1
nmcli> set ipv4.routes 192.168.2.0/24 10.0.0.1
nmcli> save
nmcli> quit
```


用户也可以使用以下非交互式命令编辑网络连接：

```
nmcli connection modify ens18-connection ipv4.addr 192.168.1.2/24
nmcli connection modify ens18-connection ipv4.gateway 192.168.1.1
nmcli connection modify ens18-connection ipv4.dns 192.168.1.1
nmcli connection modify ens18-connection +ipv4.routes "192.168.2.0/24 10.0.0.1"
```


用户也可以直接编辑网络配置文件来编辑网络连接（nmcli命令创建的网络配置文件在 `/etc/NetworkManager/system-connections`

目录下），编辑完成后通过 nmcli 命令应用配置更改。

#### 1.1.6 删除网络连接

使用以下命令删除网络连接：

```
nmcli connection delete ens18-connection
```


#### 1.1.7 应用配置更改

如果编辑网络连接配置创建或更改网络连接后，需要先使用以下命令重新载入网络连接。

```
nmcli connection reload
```


```
nmcli dev reapply ens18
```


#### 1.1.8 激活/断开网络连接

使用以下命令将连接激活，连接到网络：

```
nmcli connection up ens18-connection
```


使用以下命令断开连接：

```
nmcli connection down ens18-connection
```


#### 1.1.9 配置 NetworkManager 管理或忽略设备

对于非受 NetworkManager 管理设备，使用以下命令临时配置设备为 NetworkManager 管理：

```
nmcli device set ens18 managed yes
```


对于 NetworkManager 管理的设备，使用以下将设备临时配置为 NetworkManager 非受管设备：

```
nmcli device set ens18 managed no
```


此命令配置为临时配置，重启 NetworkManager 服务或系统后，配置会丢失。

### 1.2 使用 nmtui 配置网络

nmtui 提供了一个基于文本的用户界面。它提供了一个简单而直观的基于菜单的界面。 用户可以使用 nmtui 创建和修改网络连接，而不必记住复杂的命令或选项。

nmtui 默认不安装，使用 nmtui 需要先安装 NetworkManager-tui 软件包：

```
dnf install -y NetworkManager-tui
```


nmtui 基本操作：

- 使用光标键导航。
- 选择按钮并按
**Enter**键来按按钮。 - 使用
**Space**选择或取消选择复选框。

#### 1.2.1 创建动态 IP 地址的网络连接

- 如果不知道新添加网络连接需要使用的网络设备名称，可以先使用 nmcli 查看网络设备信息，找到可用的设备
- 在命令行中执行 nmtui。
- 在界面中按
`Edit a connection`

。 - 按
`Add`

。 - 从网络类型列表中选择并按
`Ethernet`

。 - 可选：为要创建的网络连接输入一个自定义名称。
- 在
`Device`

字段中输入网络设备名称。 - 按
`OK`

按钮创建并自动激活新连接。 - 按
`Cancal`

按钮返回到主菜单。 - 按
`Quit`

关闭 nmtui 应用程序。

#### 1.2.2 创建静态 IP 地址的网络连接

- 如果不知道新添加网络连接需要使用的网络设备名称，可以先使用 nmcli 查看网络设备信息，找到可用的设备
- 在命令行中执行 nmtui。
- 在界面中按
`Edit a connection`

。 - 按
`Add`

。 - 从网络类型列表中选择并按
`Ethernet`

。 - 可选：为要创建的网络连接输入一个自定义名称。
- 在
`Device`

字段中输入网络设备名称。 - 在
`IPv4 CONFIGURATION`

和`IPv6 CONFIGURATION`

中配置 IPv4 和 IPv6 地址：- 按
`Automatic`

，然后从显示的列表中选择`Manual`

。 - 按要配置的协议旁边的
`show`

按钮，已显示其他字段 - 在
`Address`

输入 IP 地址和子网掩码。如果没有指定子网掩码，NetworkManager 会为 IPv4 地址设置 /32 子网掩码，为 IPv6 地址设置/64子网掩码。 - 在
`Gateway`

输入默认网关的地址。 - 在
`DNS Servers`

输入 DNS 服务器地址。 - 在
`Search domains`

输入 DNS 搜索域。

- 按
- 按
`OK`

按钮创建并自动激活新连接。 - 按
`Cancal`

按钮返回到主菜单。 - 按
`Quit`

关闭 nmtui 应用程序。

#### 1.2.3 编辑网络连接

- 在命令行中执行 nmtui。
- 在界面中按
`Edit a connection`

- 选择并按需要编辑的网络连接。
- 编辑网络连接。
- 按
`OK`

按钮更新并自动激活新连接。 - 按
`Cancal`

按钮返回到主菜单。 - 按
`Quit`

关闭 nmtui 应用程序

#### 1.2.4 激活和断开网络连接

- 在命令行中执行 nmtui。
- 在界面中按
`Activate a connection`

- 选择并按需要激活或者断开的网络连接，并按右侧的
`Activate`

激活，或按`Deactivate`

断开。 - 按
`Back`

按钮返回到主菜单。 - 按
`Quit`

关闭 nmtui 应用程序。

### 1.3 使用 ifcfg 文件配置网络

NetworkManager 还兼容支持 network-scripts 的 ifcfg 类型配置文件。 使用 ifcfg 文件配置的网络连接，也可以被 nmcli 和 nmtui 识别并进行配置。

#### 1.3.1 创建动态 IP 地址的网络连接

用户可以在 `/etc/sysconfig/network-scripts/`

目录下编辑网络配置文件为某个网络设备配置静态 IP 地址。
如编辑 ifcfg-ens18 文件，并添加以下内容：

```
DEVICE=ens18
BOOTPROTO=dhcp
PEERDNS=yes
ONBOOT=yes
```


如果要使用特定 DNS 服务器，而不是从 DHCP 服务器获得的 DNS 服务器地址，请将PEERDNS修改为PEERDNS=no，并添加以下行添加到 ifcfg 文件中：

```
DNS1=192.168.1.1
DNS2=192.168.2.1
```


文件保存后，使用 nmcli 命令应用网络配置，或重启 NetworkManager 以应用网络配置。

#### 1.3.2 创建静态 IP 地址的网络连接

用户可以在 `/etc/sysconfig/network-scripts/`

目录下创建网络配置文件为某个网络设备配置静态 IP 地址。
如编辑 ifcfg-ens18 文件，并添加以下内容：

```
DEVICE=ens18
BOOTPROTO=static
IPADDR=192.168.1.2
NETMASK=255.255.255.0
GATEWAY=192.168.1.1
DNS1=192.168.1.1
DNS2=192.168.2.1
ONBOOT=yes
```


文件保存后，使用 nmcli 命令应用网络配置，或重启 NetworkManager 以应用网络配置。

#### 1.3.3 配置静态路由

若想要将静态路由配置为在系统重启后永久保留，用户可以在 `/etc/sysconfig/network-scripts/`

下创建路由配置文件，文件名格式为 `route-xxx`

，route- 后的字符需要与网络配置文件名 ifcfg- 后的字符保持一致，如网络配置文件名 ifcfg-ens18，路由配置文件名则为 route-ens18。

在路由配置文件中添加如下行：

```
ADDRESS0=192.168.2.1
NETMASK0=255.255.255.255
GATEWAY0=10.0.0.1
ADDRESS1=192.168.2.0
NETMASK1=255.255.255.0
GATEWAY1=10.0.0.1
```


`ADDRESS0=192.168.2.1`

是要访问的远程网络或主机的网络地址。`NETMASK0=255.255.255.255`

是使用`ADDRESS0=192.168.2.1`

定义的网络地址的子网掩码。`GATEWAY0=10.0.0.1`

是网关。

后续静态路由必须按顺序编号，且不得跳过任何值。例如： `ADDRESS0`

、 `ADDRESS1`

、 `ADDRESS2`

等。

### 1.4 NetworkManager 服务配置

#### 1.4.1 网络设备管理

除 lo 设备和 udev 设备管理器配置 NM_UNMANAGED 为 "1" 或 "true" 的特殊网络设备外，其他网络设备均默认由 NetworkManager 管理。由 NetworkManager 管理的设备使用 NetworkManager 配置网络才会生效。

NM_UNMANAGED 配置信息在

`/usr/lib/udev/rules.d/85-nm-unmanaged.rules`

文件中。

lo设备通常用于本地通信，不需要网络配置。udev设备管理器默认配置为非受 NetworkManager 管理的特殊设备也各有原因。不建议将默认的 NetworkManager 非受管设备修改为 NeworkManager 管理。如果明确确认需要修改，可以通过 nmcli 命令临时配置。

对于 NetworkManager 管理的设备，可以通过 nmcli 命令临时配置为非受 NetworkManager 管理。若需要永久配置，用户可以使用以下内容创建 `/etc/NetworkManager/conf.d/99-unmanaged-devices.conf`

文件：

- 要将特定网络设备配置为非受管，请添加：
`[keyfile] unmanaged-devices=interface-name:ens18`

- 要将特定 MAC 地址的网络设备配置为非受管，请添加：
`[keyfile] unmanaged-devices=mac:xx:xx:xx:xx:xx:xx`

- 要将特定类型的所有网络设备配置为为非受管，请添加：
`[keyfile] unmanaged-devices=type:ethernet`


要将多个设备设置为非受管，请使用分号分隔 `unmanaged-devices`

参数中的条目。
创建完成后使用 `systemctl reload NetworkManager`

命令重新载入NetworkManager服务。

使用 nmcli 命令查看网络设备信息时发现应默认由 NetworkManager 管理的设备的状态为 unmanaged，则可能是 nmcli 命令临时配置或 NetworkManager 的配置文件永久配置此设备非受 NetworkManager 管理，可以通过以下方法将其修改回 NetworkManager 管理：

- 使用
`systemctl restart NetworkManager`

重启 NetworkManager 服务。 如果重启若设备后自动修改回 NetworkManager 管理，则说明是临时配置导致。 如果重启后仍为 unmanaged 状态，则需要查找并删除 NetworkManager 配置文件中的永久配置。 - 在以下目录和文件中查找将设备配置为非受管的永久配置，并将其删除后使用
`systemctl reload NetworkManager`

重新载入 NetworkManager 服务。`/etc/NetworkManager/conf.d/ /usr/lib/NetworkManager/conf.d/ /etc/NetworkManager/NetworkManager.conf`


#### 1.4.2 DNS 管理

NetworkManager 服务运行时将根据 `/etc/resolv.conf`

文件的情况来选择谁来管理 DNS：

`/etc/resolv.conf`

是指向`/run/systemd/resolve/stub-resolv.conf`

或`/run/systemd/resolve/resolv.conf`

的软链接，由 systemd-resolved 管理 DNS。 当系统安装了 systemd-resolved 且`/etc/resolv.conf`

不存在时，会默认生成此指向的软链接。`/etc/resolv.conf`

时指向`/run/NetworkManager/resolv.conf`

的软链接，由NetworkManager 管理 DNS。`/etc/resolv.conf`

不存在或为普通文件，由NetworkManager 管理 DNS。

DNS 由 systemd-resolved 管理时，DNS 解析路径为用户向 systemd-resolved 提供的本地 DNS 服务发起 DNS 解析请求，systemd-resolved 再根据 NetworkManager 网络连接的 DNS 配置信息将解析请求转发给对应 DNS 服务器进行解析。

DNS 由 NetworkManager 管理时，还可以配置将 DNS 交给 dnsmasq 服务管理或 `/etc/resolv.conf`

文件管理。

**交给 dnsmasq 服务管理 **

- 使用以下命令安装 dnsmasq：
`dnf install dnsmasq`

- 将
`/etc/NetworkManager/NetworkManager.conf`

文件的 [main] 部分中的 dns 参数设置为 dnsmasq：`[main] dns=dnsmasq`

- 确认
`/etc/resolv.conf`

是指向`/run/NetworkManager/resolv.conf`

的软链接，若不是，请使用如下命令生成软链接：`ln -sf /var/run/NetworkManager/resolv.conf /etc/resolv.conf`

- 使用
`systemctl restart NetworkManager`

重启 NetworkManager 服务。

通过以上设置，用户将向 dnsmasq 提供的本地 DNS 服务发起 DNS 解析请求，dnsmasq 根据 NetworkManager 网络连接的 DNS 配置将解析请求转发转发给对应的 DNS 服务器。

**交给 /etc/resolv.conf 文件管理**

- 将
`/etc/NetworkManager/NetworkManager.conf`

文件的 [main] 部分中的 dns 参数设置为 none：`[main] dns=none`

- 确认
`/etc/resolv.conf`

是否为软链接，若为软链接则将其删除。 - 编辑
`/etc/resolv.conf`

文件配置系统全局 DNS 服务器地址信息。 - 使用
`systemctl restart NetworkManager`

重启 NetworkManager 服务。

通过以上设置，DNS 解析请求将发送到 `/etc/resolv.conf`

文件配置的 DNS 服务器。与此同时，使用 NetworkManager 配置 DNS 将不生效。

## 2 使用 network-scripts 配置网络

相比于提供全功能网络管理的 NetworkManager，network-scripts更准确的描述是用于配置网络接口的一套基本工具，而非网络管理器。 network-scripts 不提供图形用户界面，不支持VPN连接，也不支持网络设备的自动检测和配置，难以满足新时代网络需求，且NetworkManager 也兼容支持 network-scripts 的 ifcfg 类型配置文件，不推荐用户使用 network-scripts 来配置网络。

系统默认安装 NetworkManager，不安装 network-scripts，如果确定要使用 network-scripts，用户可以在已安装 NetworkManager 的情况下安装和使用 network-scripts。

### 2.1 确定运行模式

network-scripts 有以下两种运行模式:

**使用 NetworkManager 兼容 network-scripts 模式配置网络: **

在已安装 NetworkManager 的情况下安装和使用 network-scripts，系统默认不会生成 network 服务，网络还是由 NetworkManager 服务管理，NetworkManager 服务会兼容支持 network-scripts 的脚本命令。用户可以使用 network-scripts 的脚本命令配置网络。

**完全使用 network-scripts 配置网络: **

如果确认要完全使用 network-scripts，而非 NetworkManager，可以使用以下命令将网络管理服务切换为 network-scripts 的 network 服务。禁用 NetworkManager 管理服务后，NetworkManager 的网络配置会失效。

```
systemctl stop NetworkManager
systemctl disable NetworkManager
systemctl enable network
systemctl start network
```


### 2.2 配置网络

确定 network-scripts 的运行模式后，使用 ifcfg 类型配置文件配置网络，文件的编辑方法见 NetworkManager 使用 ifcfg 文件配置网络章节。

配置文件保存后，使用以下 network-scripts 命令禁用网络设备后重新启用网络设备，以应用网络配置。

```
ifdown ens18
ifup ens18
```


## 3 使用 ip 命令配置网络

可以使用 ip 命令配置临时网络连接，但其配置的网络连接信息在系统重启后丢失。

### 3.1 查看网络设备的 IP 地址

使用以下命令查看网络设备的 IP 地址：

```
ip addr show dev ens18
```


### 3.2 为网络设备分配 IP 地址

使用以下命令查为网络设备分配 IP 地址：

```
ip addr add 192.168.1.2/24 dev ens18
```


分配地址的 ip 命令可以重复多次，以分配多个地址。

### 3.3 删除网络设备上的 IP 地址

```
ip addr del 192.168.1.2/24 dev ens18
```


### 3.4 配置默认网关和静态路由

使用以下命令配置默认网关：

```
ip route add default via 192.168.1.1 dev ens18
```


使用以下命令添加静态路由：

```
ip route add 192.168.2.1 via 10.0.0.1 dev ens18
ip route add 192.168.2.0/24 via 10.0.0.1 dev ens18
```


使用以下命令删除静态路由：

```
ip route del 192.168.2.1
ip route del 192.168.2.0/24
```


### 3.5 启用/禁用网络设备

使用以下命令启用网络设备：

```
ip link set ens18 up
```


使用以下命令禁用网络设备：

```
ip link set ens18 down
```


## 4 使用 ifconfig 命令配置网络

可以使用 ifconfig 配置临时网络连接，但其配置的网络连接信息在系统重启后丢失。 ip 命令具有更多的功能和选项，建议使用 ip 命令进行配置临时网络连接，不推荐使用 ifconfig。

### 4.1 查看网络设备的 IP 地址：

使用以下命令查看网络设备的 IP 地址：

```
ifconfig ens18
```


### 4.2 设置网络设备的 IP 地址

使用以下命令设置网络设备的IP地址：

```
ipconfig ens18 192.168.1.2 netmask 255.255.255.0
```


### 4.3 配置默认网关或静态路由

使用以下命令配置默认网关：

```
route add default gw 192.168.1.1 dev ens18
```


使用以下命令添加静态路由：

```
route add -host 192.168.2.1 gw 10.0.0.1 dev ens18
route add -net 192.168.2.0/24 gw 10.0.0.1 dev ens18
```


使用以下命令删除静态路由：

```
route del 192.168.2.1
route del 192.168.2.0/24
```


### 4.4 启用/禁用网络设备

使用以下命令启用网络设备：

```
ifconfig ens18 up
```


使用以下命令禁用网络设备：

```
ifconfig ens18 down
```