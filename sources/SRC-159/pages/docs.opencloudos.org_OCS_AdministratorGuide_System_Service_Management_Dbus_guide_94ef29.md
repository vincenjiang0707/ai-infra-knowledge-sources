source: https://docs.opencloudos.org/OCS/AdministratorGuide/System_Service_Management/Dbus_guide/

# dbus机制和使用

### 1. D-Bus 简介

D-Bus 是一种进程间通信机制，它可以让不同进程之间通过消息传递来进行通信。D-Bus 可以用于 Linux 系统中的各种应用程序之间的通信，例如桌面环境中的应用程序、系统服务等。

### 2. D-Bus 命令行工具

Linux 系统中提供了一些 D-Bus 命令行工具，可以用于查看和操作 D-Bus 服务和对象。常用的 D-Bus 命令行工具包括：

- dbus-send：用于向 D-Bus 发送消息。
- dbus-monitor：用于监视 D-Bus 消息。
- dbus-launch：用于启动 D-Bus 会话。
- dbus-daemon：D-Bus 的守护进程。

注：dbus-tools包系统未默认安装，需要自行安装。

### 3. D-Bus 消息格式

D-Bus 消息由三部分组成：消息类型、消息标识符和消息体。消息类型包括方法调用、方法返回、信号等。消息标识符用于标识消息的发送者和接收者。消息体包含了消息的参数和返回值等信息。 以下为例：

```
dbus-send --system --type=method_call --dest=org.freedesktop.UPower /org/freedesktop/UPower/KbdBacklight org.freedesktop.UPower.KbdBacklight.SetBrightness int32:50
```


`--system`

表示使用系统总线，该消息类型为 `method_call`

也就是方法调用，消息标识符为

`--dest=org.freedesktop.UPower`

，表示消息的目标为 `org.freedesktop.UPower`

服务

`/org/freedesktop/UPower/KbdBacklight`

表示接收消息的对象的路径

`org.freedesktop.UPower.KbdBacklight.SetBrightness`

表示消息的调用方法，即 `org.freedesktop.UPower.KbdBacklight`

服务的 `SetBrightness`

方法，参数为 `int32:50`

。

### 4. D-Bus 服务和对象

D-Bus 服务是一组相关的 D-Bus 对象的集合，每个 D-Bus 对象都有一个唯一的对象路径和一个接口。D-Bus 服务和对象可以用于提供各种功能和服务，例如系统设置、音频控制等。 可以通过busctl list查看

```
# busctl list
NAME PID PROCESS USER CONNECTION UNIT SESSION DESCRIPTION
:1.0 680 systemd-oomd systemd-oom :1.0 systemd-oomd.service - -
:1.1 725 systemd-homed root :1.1 systemd-homed.service - -
:1.10 790 NetworkManager root :1.10 NetworkManager.service - -
:1.14 985 systemd root :1.14 user@0.service - -
:1.163940 663881 busctl root :1.163940 session-81798.scope 81798 -
:1.2 707 avahi-daemon avahi :1.2 avahi-daemon.service - -
:1.3 726 systemd-logind root :1.3 systemd-logind.service - -
:1.4 1 systemd root :1.4 init.scope - -
:1.5 731 dbus-broker-lau root :1.5 dbus-broker.service - -
:1.6 790 NetworkManager root :1.6 NetworkManager.service - -
:1.8 800 oddjobd root :1.8 oddjobd.service - -
```


busctl list 命令会输出一个列表，其中包含了所有连接到 D-Bus 系统总线的进程的信息。每个进程的信息包括以下几个部分：

- NAME：对象名。
- PID：进程的 ID。
- PROCESS：进程名
- USER：进程的用户。
- CONNECTION：连接的唯一标识。
- UNIT：进程对应的服务名
- SESSION：进程对应的会话号

通常情况下，dbus服务的名称和注册路径是一致的，即 `org.freedesktop.NetworkManager`

服务，他的注册路径就是 `org/freedesktop/NetworkManager`

。可以通过dbus-send命令查看当前系统中的dbus服务

```
# dbus-send --dest=org.freedesktop.DBus --type=method_call --print-reply /org/freedesktop/DBus org.freedesktop.DBus.ListNames
method return time=1685349424.537811 sender=org.freedesktop.DBus -> destination=:1.8 serial=4294967295 reply_serial=2
array [
string "org.freedesktop.DBus"
string ":1.1"
string ":1.2"
string ":1.7"
string ":1.8"
string "com.example.MyService"
string "org.freedesktop.systemd1"
]
```


如果需要查看系统服务需要加上 `--system`

参数

```
# dbus-send --system --dest=org.freedesktop.DBus --type=method_call --print-reply /org/freedesktop/DBus org.freedesktop.DBus.ListNames
method return time=1685349408.666240 sender=org.freedesktop.DBus -> destination=:1.39 serial=4294967295 reply_serial=2
array [
string "org.freedesktop.DBus"
string ":1.0"
string ":1.1"
string ":1.2"
string ":1.3"
string ":1.4"
string ":1.7"
string ":1.11"
string ":1.39"
string "com.redhat.ifcfgrh1"
string "org.freedesktop.Avahi"
string "org.freedesktop.NetworkManager"
string "org.freedesktop.login1"
string "org.freedesktop.systemd1"
]
```


如果要查看某个dbus服务提供了哪些方法，可以查看解析他的xml，例如，要查看 `NetworkManager`

有哪些方法

```
# dbus-send --system --dest=org.freedesktop.NetworkManager --type=method_call --print-reply /org/freedesktop/NetworkManager org.freedesktop.DBus.Introspectable.Introspect
```


返回的XML格式如下

```
<interface name="org.freedesktop.NetworkManager">
<method name="Reload">
<arg type="u" name="flags" direction="in"/>
</method>
<method name="GetDevices">
<arg type="ao" name="devices" direction="out"/>
</method>
...
<method name="GetDeviceByIpIface">
<arg type="s" name="iface" direction="in"/>
<arg type="o" name="device" direction="out"/>
</method>
...
```


这里通过 `<method>`

标签定义了服务的方法：
该DBus接口包含了以下方法：

`Reload`

方法：用于重新加载NetworkManager服务的配置。该方法包含一个参数：`flags`

表示重新加载的标志。`GetDevices`

方法：用于获取NetworkManager服务中所有的网络设备。该方法不包含参数，返回一个数组类型的输出参数`devices`

，其中包含了所有的网络设备对象路径。`GetDeviceByIpIface`

方法：用于根据IP接口名称获取对应的网络设备对象路径。该DBus方法包含了两个参数：`iface`

表示输入参数，类型为字符串，名称为`iface`

，用于指定IP接口名称；`device`

表示输出参数，类型为对象路径，名称为`device`

，用于返回对应的网络设备对象路径。

系统中服务与服务、服务调用自己功能的方式基本都是通过dbus总线传递，如：

```
# dbus-monitor --system --profile
#type timestamp serial sender destination path interface member
# in_reply_to
sig 1685415278.520415 816 :1.1 <none> /org/freedesktop/NetworkManager/DHCP4Config/3 org.freedesktop.DBus.Properties PropertiesChanged
sig 1685415310.519128 817 :1.1 <none> /org/freedesktop/NetworkManager/DHCP4Config/1 org.freedesktop.DBus.Properties PropertiesChanged
sig 1685415310.521757 818 :1.1 <none> /org/freedesktop/NetworkManager/DnsManager org.freedesktop.DBus.Properties PropertiesChanged
...
sig 1685415611.409304 12315 :1.2 <none> /org/freedesktop/systemd1/unit/sysstat_2dcollect_2etimer org.freedesktop.DBus.Properties PropertiesChanged
sig 1685415611.409346 12316 :1.2 <none> /org/freedesktop/systemd1/unit/sysstat_2dcollect_2etimer org.freedesktop.DBus.Properties PropertiesChanged
...
sig 1685415611.409363 12319 :1.2 <none> /org/freedesktop/systemd1 org.freedesktop.systemd1.Manager JobNew
sig 1685415611.431655 12320 :1.2 <none> /org/freedesktop/systemd1/unit/sysstat_2dcollect_2eservice org.freedesktop.DBus.Properties PropertiesChanged
sig 1685415611.431693 12321 :1.2 <none> /org/freedesktop/systemd1/unit/sysstat_2dcollect_2eservice org.freedesktop.DBus.Properties PropertiesChanged
```


在使用 `dbus-monitor`

监听一段时间后，会发现NetworkManager服务会周期性地去更新DHCP、DNS配置。sysstat-collect服务也会周期性的去收集一些系统内信息，这些消息调用都会经过dbus总线，所以我们通过dbus-monitor可以很清楚的检测到系统中的信号传递和方法调用。

### 5. D-Bus API

D-Bus API 是一组用于在应用程序中使用 D-Bus 的函数和接口。D-Bus API 可以用于向 D-Bus 发送消息、接收消息、注册和注销 D-Bus 服务和对象等操作。

### 6. D-Bus 应用程序开发

在 Linux 系统中，可以使用各种编程语言来开发 D-Bus 应用程序，例如 C、C++、Python 等。开发 D-Bus 应用程序需要了解 D-Bus 的消息格式、服务和对象的概念、D-Bus API 等内容。 要创建并注册一个 D-Bus 服务，需要完成以下几个步骤：

- 定义 D-Bus 接口：首先，需要定义一个 D-Bus 接口，用于描述服务提供的方法和属性。D-Bus 接口通常使用 XML 文件来定义，其中包含接口名称、方法、信号和属性等信息。
- 实现 D-Bus 接口：接下来，需要实现定义的 D-Bus 接口，即编写服务的实际代码。在实现 D-Bus 接口时，需要使用 D-Bus API 提供的方法来注册服务和处理来自客户端的请求。
- 注册 D-Bus 服务：最后，需要将实现的 D-Bus 接口注册到 D-Bus 系统总线上，以便客户端可以通过 D-Bus 系统总线访问服务。

下面是一些简单的 Python 代码示例：

#### 示例1：

演示了如何创建并注册一个 D-Bus 服务。 创建一个python脚本test.py，来创建并注册一个我们自己的服务。

```
import dbus
import dbus.service
import dbus.mainloop.glib
from gi.repository import GLib
# 定义 D-Bus 接口
class MyService(dbus.service.Object):
def __init__(self):
bus_name = dbus.service.BusName('com.example.MyService', bus=dbus.SessionBus())
dbus.service.Object.__init__(self, bus_name, '/com/example/MyService')
@dbus.service.method('com.example.MyService')
def hello(self):
print('Hello, world!')
# 创建 D-Bus 主循环对象
dbus.mainloop.glib.DBusGMainLoop(set_as_default=True)
# 创建 D-Bus 会话总线对象
bus = dbus.SessionBus()
# 注册 D-Bus 服务
service = MyService()
# 运行 D-Bus 主循环
loop = GLib.MainLoop()
loop.run()
```


执行该python文件后，该dbus服务就已经被创建并注册，处于监听状态了

```
python3 test.py
```


然后我们在另一个窗口，通过 `dbus-send`

命令去访问它

```
# dbus-send --print-reply --dest=com.example.MyService /com/example/MyService com.example.MyService.hello
method return time=1685348486.209346 sender=:1.3 -> destination=:1.5 serial=4 reply_serial=2
```


此时，原来监听的窗口，会打印出 `Hello, world!`


```
# python3 test.py
Hello, world!
```


#### 示例2：

演示了如何通过python脚本使用dbus总线上的对象

```
import dbus
# 创建 D-Bus 系统总线对象
bus = dbus.SystemBus()
# 获取 D-Bus 服务对象
service = bus.get_object('org.freedesktop.DBus', '/org/freedesktop/DBus')
# 获取 D-Bus 接口对象
interface = dbus.Interface(service, 'org.freedesktop.DBus')
# 调用 D-Bus 接口方法
names = interface.ListNames()
# 打印所有名称
print('Names:', names)
```


这个示例代码使用 `org.freedesktop.DBus`

服务的 `ListNames()`

方法列出了所有在 D-Bus 系统总线上注册的名称，并打印了这些名称。

```
# python3 show.py
Names: dbus.Array([dbus.String('org.freedesktop.DBus'), dbus.String(':1.0'), dbus.String(':1.1'), dbus.String(':1.2'), dbus.String(':1.3'), dbus.String(':1.4'), dbus.String(':1.7'), dbus.String(':1.11'), dbus.String(':1.35'), dbus.String('com.redhat.ifcfgrh1'), dbus.String('org.freedesktop.Avahi'), dbus.String('org.freedesktop.NetworkManager'), dbus.String('org.freedesktop.login1'), dbus.String('org.freedesktop.systemd1')], signature=dbus.Signature('s'))
```


#### 示例3：

演示了如何通过 `dbus-send`

命令调用系统中NetworkManager注册的服务的方法：

```
# dbus-send --system --print-reply --dest=org.freedesktop.NetworkManager /org/freedesktop/NetworkManager org.freedesktop.NetworkManager.GetDevices
method return time=1685352906.585352 sender=:1.1 -> destination=:1.41 serial=550 reply_serial=2
array [
object path "/org/freedesktop/NetworkManager/Devices/1"
object path "/org/freedesktop/NetworkManager/Devices/2"
object path "/org/freedesktop/NetworkManager/Devices/3"
object path "/org/freedesktop/NetworkManager/Devices/4"
object path "/org/freedesktop/NetworkManager/Devices/5"
object path "/org/freedesktop/NetworkManager/Devices/6"
]
```


调用了NetworkManager的GetDevices方法，该方法回返回NetworkManager服务中所有的网络设备。
如何获取当前注册的服务有哪些方法可以调用，以及参数是什么，可见**第4节 D-Bus 服务和对象**。

### 7. 问题排查手段

dbus信号问题，有几个比较常用的问题定位手段

#### 1. dbus-monitor

dbus-monitor可以监控系统中的所有dbus通信，例如，我们先通过dbus-monitor开启监控，注意，需要监听系统总线的时候使用 `--system`

而会话总线用 `--session`


```
# dbus-monitor --system
signal time=1685361016.664467 sender=org.freedesktop.DBus -> destination=:1.66 serial=4294967295 path=/org/freedesktop/DBus; interface=org.freedesktop.DBus; member=NameAcquired
string ":1.66"
signal time=1685361016.664490 sender=org.freedesktop.DBus -> destination=:1.66 serial=4294967295 path=/org/freedesktop/DBus; interface=org.freedesktop.DBus; member=NameLost
string ":1.66"
```


然后使用dbus-send模拟信号交互发送信号给NetworkManager服务

```
# dbus-send --system --type=method_call --dest=org.freedesktop.NetworkManager /org/freedesktop/NetworkManager org.freedesktop.NetworkManager.GetDevices
```


此时，可以看到dbus-monitor会打印出监控到的通信日志

```
...
method call time=1685361019.018081 sender=:1.67 -> destination=org.freedesktop.NetworkManager serial=2 path=/org/freedesktop/NetworkManager; interface=org.freedesktop.NetworkManager; member=GetDevices
...
method return time=1685361019.018442 sender=:1.1 -> destination=:1.67 serial=591 reply_serial=2
array [
object path "/org/freedesktop/NetworkManager/Devices/1"
object path "/org/freedesktop/NetworkManager/Devices/2"
object path "/org/freedesktop/NetworkManager/Devices/3"
object path "/org/freedesktop/NetworkManager/Devices/4"
object path "/org/freedesktop/NetworkManager/Devices/5"
object path "/org/freedesktop/NetworkManager/Devices/6"
]
```


日志里的 `:1.67`

，就是我们发送信息的终端，可以看到，日志详细记录了通信的双方，通信序号 `serial`

以及通信和返回的内容。

这种方式通过检查发送方和接受方的相关属性是否正确来排查问题。

#### 2. dbus配置

dbus的配置可以控制dbus的消息和连接，dbus的配置文件在 `/etc/dbus-1/`

下，一些rpm包如果需要控制自己的dbus消息，会在该目录下放置自己的配置文件。
例如，本系统中默认会有以下三个dbus配置

```
avahi-dbus.conf oddjob.conf org.selinux.conf
```


以稍简单的 `org.selinux.conf`

为例：

```
<?xml version="1.0" encoding="UTF-8"?> <!-- -*- XML -*- -->
<!DOCTYPE busconfig PUBLIC
"-//freedesktop//DTD D-BUS Bus Configuration 1.0//EN"
"http://www.freedesktop.org/standards/dbus/1.0/busconfig.dtd">
<busconfig>
<!-- Only root can own the service -->
<policy user="root">
<allow own="org.selinux"/>
</policy>
<!-- Allow anyone to invoke methods on the interfaces,
authorization is performed by PolicyKit -->
<policy context="default">
<allow send_destination="org.selinux"/>
</policy>
</busconfig>
```


该配置中

`<policy user="root">`

此配置节指定了 root 用户的访问权限策略。`<allow own="org.selinux"/>`

这表示 root 用户被允许拥有服务名称 “org.selinux”。`<policy context="default">`

此配置节定义了默认访问策略。`<allow send_destination="org.selinux"/>`

这表示任何用户默认情况下都可以向服务 “org.selinux” 发送方法调用。此配置假定 PolicyKit 将对方法调用授权，以便提高安全性。

除此之外，还有 `max_incoming_bytes`

和 `max_outgoing_bytes`

等资源限制配置会导致dbus信息传递异常，所以，dbus配置文件是一个非常重要的排查方向。
如果确定为dbus配置导致的问题，可以在 `/etc/dbus-1/system.conf`

文件中调整dbus配置。

#### 3. 环境压力

当环境存在CPU 占用率、内存占用率和 I/O压力过大时，也可能出现dbus消息堵塞或者丢失的情况。这种情况，dbus本身不会报错，但是可能会出现消息卡死、消息丢失等问题，所以需要通过其他定位手段来排查，如top、iostat等。

#### 4. d-feet工具

该工具目前还未支持，后续会更新支持。