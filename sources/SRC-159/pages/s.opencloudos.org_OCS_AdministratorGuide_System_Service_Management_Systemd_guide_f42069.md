source: https://docs.opencloudos.org/OCS/AdministratorGuide/System_Service_Management/Systemd_guide/

# systemd工具使用及服务管理

## 1.systemd常用工具

### 1.1 systemctl

最常用的systemd工具

```
status: 查看unit状态
cat: 查看unit配置
start/restart/stop: 控制unit当前状态
set-property: 设置unit配置，例如CPUAccounting、CPUShares等
daemon-reload: 重新加载manager配置
list-units: 列出系统中的unit及其状态
list-dependencies:以树状图展示各个unit之间的依赖关系
enable/disable: 设置/取消unit开机启动，实际等价于创建/删除unit file到/etc/systemd/下面的软连接
mask/unmask: mask与disable类似，但是不同的是，service一旦被mask是无法启动的（即使被别的unit require），等价于创建unit file到/dev/null的链接
```


### 1.2 journalctl

查询systemd日志

```
-u: 按unit查询
-b: 只显示启动日志
-k: 显示内核相关日志
```


例如，需要查看dbus服务相关日志：

```
journalctl -u dbus.service
```


`journalctl -b`

命令只能看到该次启动的日志，如果需要查询之前的启动日志，需要通过以下方式（需要将journald日志切换到磁盘存储，否则每次只能看到当此的启动日志，参考《日志管理》）。

```
# journalctl --list-boots
IDX BOOT ID FIRST ENTRY LAST ENTRY
-9 9d27b37bc8014865b0c20c957429dc31 Wed 2023-01-18 15:44:22 HKT Fri 2023-02-24 10:27:36 HKT
-8 aa28b72e95074434a4a81b623c400e7e Tue 2023-02-28 16:35:24 HKT Tue 2023-02-28 16:45:08 HKT
-7 12a71bb5bd9d4dec993d0e03e0cbe636 Mon 2023-03-06 10:46:43 HKT Mon 2023-03-06 11:07:43 HKT
...
```


然后指定查看哪一次的启动日志

```
journalctl -b -8
```


### 1.3 systemd-analyze

系统启动时间分析工具

```
blame: 分析系统中服务启动时间
plot: 图形化显示系统中服务的启动顺序，可以通过网页或者图形编辑器打开
dump: 查看每个服务的状态，cgroup mask等，比systemctl satus更详细
```


#### 1.3.1 systemd-analyze blame

该命令主要作用是分析系统中当此启动里服务的启动时间，会默认按时间从长到短列出各服务的启动时间顺序。

```
# systemd-analyze blame
8.814s kdump.service
2.442s NetworkManager-wait-online.service
944ms dev-vda1.device
568ms sshd-keygen@rsa.service
295ms initrd-switch-root.service
214ms var-lib-nfs-rpc_pipefs.mount
206ms dnf-makecache.service
194ms dracut-initqueue.service
143ms user@0.service
135ms ipmi.service
118ms initrd-parse-etc.service
103ms chronyd.service
99ms NetworkManager.service
99ms systemd-logind.service
92ms avahi-daemon.service
88ms auditd.service
71ms lvm2-monitor.service
...
```


这里方便优化排查系统的启动时间。找到耗时的服务，再结合该服务自己的日志或者其他排查手段排查服务耗时的原因。 例如上面看到kdump服务的启动时间最久，通过strace工具看到它最耗时的过程其实是加载kdump内核。


#### 1.3.2 systemd-analyze plot

通过该方式生成的图像格式，如果系统没有安装图形界面将无法查看，此时可以通过 `lrzsz`

等工具拷贝出环境，在其他环境查看，如

```
# systemd-analyze plot > boot.svg
# sz boot.svg
Received - boot.svg 2.12 MB/s Spend: 0 seconds
```


浏览器打开后可以很详细的看到各服务的启动顺序以及耗时。

### 1.4 其他工具

```
systemd-cgls: 以树形态查看系统中cgroup的关系结构
systemd-nspawn: 与chroot类似，但是会挂载proc、sys文件系统
```


#### 1.3.3 systemd-cgls

systemd-cgls命令用于显示systemd控制组（cgroup）的层次结构。

```
systemd-cgls
Control group /:
-.slice
├─user.slice (#1203)
│ → user.invocation_id: 90e555a5089c481bbffcc9bbb8e48019
│ → trusted.invocation_id: 90e555a5089c481bbffcc9bbb8e48019
│ └─user-0.slice (#9785)
│ → user.invocation_id: e4a4009795694a7ca82ad4344ac7e713
│ → trusted.invocation_id: e4a4009795694a7ca82ad4344ac7e713
│ ├─session-22.scope (#10065)
│ │ → user.invocation_id: 183a492473c94efe8e3c4b1e1745f0b0
│ │ → trusted.invocation_id: 183a492473c94efe8e3c4b1e1745f0b0
│ │ ├─33878 sshd: root [priv]
│ │ ├─33892 sshd: root@pts/0
│ │ ├─33893 -bash
│ │ ├─35517 systemd-cgls
│ │ └─35518 less
│ └─user@0.service … (#9865)
│ → user.delegate: 1
│ → trusted.delegate: 1
│ → user.invocation_id: 63e944859fa04569817e2847cedca029
│ → trusted.invocation_id: 63e944859fa04569817e2847cedca029
│ └─init.scope (#9905)
│ ├─33882 /usr/lib/systemd/systemd --user
│ └─33885 (sd-pam)
├─init.scope (#25)
│ └─1 /usr/lib/systemd/systemd --switched-root --system --deserialize 31
└─system.slice (#65)
├─rngd.service (#2661)
│ → user.invocation_id: 4cc6fb282cc54f9bbb09055d771f1dde
│ → trusted.invocation_id: 4cc6fb282cc54f9bbb09055d771f1dde
│ └─685 /usr/sbin/rngd -f -x pkcs11 -x nist
├─irqbalance.service (#2581)
│ → user.invocation_id: 5c40d8f7f503434483342f781b534ad3
│ → trusted.invocation_id: 5c40d8f7f503434483342f781b534ad3
│ └─683 /usr/sbin/irqbalance --foreground
```


相比直接去cgroup目录下查看，`systemd-cgls`

会把每个cgroup里的进程都列出来，并且各个层级的关系更加清晰。
所以推荐使用 `systemd-cgls`

来查看系统中的cgroup层级。

#### 1.3.4 systemd-nspawn

和 `chroot`

使用方式类似，但是进入的目录需要是一个 `OS tree`

形式。否则，会有如下提示：

```
# systemd-nspawn -D ./rootfs
Directory /root/rootfs doesn't look like it has an OS tree (/usr/ directory is missing). Refusing.
```


如果目录是正确的 `OS tree`

形式，如下

```
# ls rootfs/
bin boot data dev etc home lib lib64 lost+found media mnt opt proc root run sbin srv sys tmp usr var
```


那就可以通过 `systemd-nspawn`

创建一个轻量级容器。

```
# systemd-nspawn -D ./rootfs
Spawning container rootfs on /root/rootfs.
Press ^] three times within 1s to kill container.
[root@rootfs ~]#
```


如果需要模拟真实环境，还可以加上 `-b`

选项在容器中启动systemd。

## 2. systemd服务

### 2.1 服务开机启动

systemd在启动时，会根据 `/usr/lib/systemd/system-preset/`

以及 `/usr/lib/systemd/user-preset/`

下的preset文件。
当前系统主要默认配置了以下几个配置文件：

| 文件名 | 作用 |
|---|---|
| 90-default.preset | 控制默认启动的系统服务 |
| 99-default-disable.preset | 默认禁用所有服务 |
| 85-display-manager.preset | 控制桌面相关的服务是否需要自启动 |

preset文件按照文件名决定执行顺序，后执行的会覆盖前面的配置，前面的数字越小，优先级越高，越后执行，所以在 `99-default-disable.preset`

里即便disable了所有的服务，还是可以在 `90-default.preset`

和 `85-display-manager.preset`

中开启部分所需要的服务。

### 2.2 systemd unit种类

#### 2.2.1 service

这是最常接触的unit，控制系统中的进程运行（包括daemon进程），例如dbus.serivce、docker.serivce等，通常会通过ExecStart=指定程序运行的动作，ExecReload=指定systemctl reload的动作，ExecStop=指定停止unit的动作。

```
[root@localhost ~]# systemctl cat dbus.service
# /usr/lib/systemd/system/dbus-broker.service
[Unit]
Description=D-Bus System Message Bus
Documentation=man:dbus-broker-launch(1)
DefaultDependencies=false
After=dbus.socket
Before=basic.target shutdown.target
Requires=dbus.socket
Conflicts=shutdown.target
[Service]
Type=notify
Sockets=dbus.socket
OOMScoreAdjust=-900
LimitNOFILE=16384
ProtectSystem=full
PrivateTmp=true
PrivateDevices=true
ExecStart=/usr/bin/dbus-broker-launch --scope system --audit
ExecReload=/usr/bin/busctl call org.freedesktop.DBus /org/freedesktop/DBus org.freedesktop.DBus ReloadConfig
[Install]
Alias=dbus.service
```


通过systemctl status dbus.service可以看到service的一些状态信息，然后接着会打印一些该服务相关journal日志

```
systemctl status sshd
● sshd.service - OpenSSH server daemon
Loaded: loaded (/usr/lib/systemd/system/sshd.service; enabled; vendor preset: enabled)
Active: active (running) since Fri 2023-04-21 11:52:56 CST; 2 weeks 4 days ago
Docs: man:sshd(8)
man:sshd_config(5)
Main PID: 1208 (sshd)
Tasks: 1 (limit: 9183)
Memory: 8.7M
CPU: 199ms
CGroup: /system.slice/sshd.service
└─1208 "sshd: /usr/sbin/sshd -D [listener] 0 of 10-100 startups"
```


- 服务名前面的点("●")，有不同的颜色和形状，简单表示了该服务当前的状态。如下表格所示

| 点的颜色形状 | 表示的状态 |
|---|---|
| "○" | "inactive" 或者 "maintenance" |
| "●"（绿色） | "active" |
| "●"（白色） | "deactivating" |
| "×" | "failed" 或者 "error" |
| "↻" | "reloading" |

- “Loaded:“这一行，显示该服务是否被加载进内存，如果是则会显示"loaded"，加载失败会显示"error"，未找到unit file会显示"not-found"，如果unit file里配置错误则会显示"bad-setting"，如果服务被mask则会显示"masked"。
- 后面的路径为加载的unit file的路径
- 再后面为当前该服务是否设置开机启动（enabled），而 “vendor preset” 则表示发行版厂商是否将该服务预设为开机启动
- “Active:"这一行，显示该服务的运行状态，
- 括号前的为当前状态，它可以是以下几种状态之一：
- active：表示 unit 正在运行。
- inactive：表示 unit 已经停止运行。
- activating：表示 unit 正在启动中。
- deactivating：表示 unit 正在停止中。
- failed：表示 unit 启动失败。

- 括号里的为子状态，它可以是以下几种状态之一：
- running：表示 unit 正在运行。
- exited：表示 unit 已经停止运行。
- waiting：表示 unit 正在等待某些条件的发生，例如网络连接、文件系统挂载等等。
- start-pre：表示 unit 正在启动前的准备工作。
- start-post：表示 unit 启动后的工作。
- stop-pre：表示 unit 停止前的准备工作。
- stop-post：表示 unit 停止后的工作。

- 后面的时间为该服务最后一次启动的时间

#### 2.2.2 timer

定时器，在固定的时间去触发激活其他的unit(默认是同名的service)，通常通过[Timer]字段中的OnActiveSec=/OnCalendar=等配置项控制触发时间（详细可参考man systemd.timer），sysstat-collect中配置的*:00/10意思就是整点开始，每10分钟触发一次

```
[root@localhost ~]# systemctl cat sysstat-collect.timer
# /usr/lib/systemd/system/sysstat-collect.timer
# /usr/lib/systemd/system/sysstat-collect.timer
# (C) 2014 Tomasz Torcz <tomek@pipebreaker.pl>
#
# sysstat-12.6.0 systemd unit file:
# Activates activity collector every 10 minutes
[Unit]
Description=Run system activity accounting tool every 10 minutes
[Timer]
OnCalendar=*:00/10
[Install]
WantedBy=sysstat.service
```


timer定时器是服务中一个很重要的机制，通过 `systemctl status`

可以看到它相比service，多了Trigger和Triggers字段。Trigger指的是下次触发的时间，以及还有多久到达，Triggers则是显示了该计时器所激活的服务。

```
systemctl status sysstat-collect.timer
● sysstat-collect.timer - Run system activity accounting tool every 10 minutes
Loaded: loaded (/usr/lib/systemd/system/sysstat-collect.timer; enabled; vendor preset: disabled)
Active: active (waiting) since Thu 2023-05-11 20:04:47 CST; 1 week 0 days ago
Until: Thu 2023-05-11 20:04:47 CST; 1 week 0 days ago
Trigger: Thu 2023-05-18 20:40:00 CST; 8min left
Triggers: ● sysstat-collect.service
```


该例子中，该timer触发的服务是sysstat-collect.service，8分钟后再次触发。

#### 2.2.3 mount

控制系统中的挂载点，通常通过[Mount]字段中的Where=/What=/Type=去控制挂载的位置、设备和类型，正常只需要配置/etc/fstab就行了，systemd-fstab-generator会自动将配置的fstab中的挂载点生成对应的mount unit。

```
[root@localhost ~]# systemctl cat mnt.mount
# /run/systemd/generator/mnt.mount
# Automatically generated by systemd-fstab-generator
[Unit]
Documentation=man:fstab(5) man:systemd-fstab-generator(8)
SourcePath=/etc/fstab
Before=local-fs.target
Requires=systemd-fsck@dev-vdb1.service
After=systemd-fsck@dev-vdb1.service
After=blockdev@dev-vdb1.target
[Mount]
What=/dev/vdb1
Where=/mnt
Type=ext4
Options=noatime,acl,user_xattr
```


例如，在/etc/fstab中配置了如下挂载项

```
# cat /etc/fstab
/dev/vdc1 /data/ ext4 noatime,acl,user_xattr 1 1
```


那重启（systemd-fstab-generator会在启动时候执行）后，系统中就可以看到有对应的mount服务，服务配置与fstab中配置相对应。

```
# systemctl list-units -a | grep data
data.mount loaded active mounted /data
# systemctl cat data.mount
# /run/systemd/generator/data.mount
# Automatically generated by systemd-fstab-generator
[Unit]
Documentation=man:fstab(5) man:systemd-fstab-generator(8)
SourcePath=/etc/fstab
Before=local-fs.target
Requires=systemd-fsck@dev-vdc1.service
After=systemd-fsck@dev-vdc1.service
After=blockdev@dev-vdc1.target
[Mount]
What=/dev/vdc1
Where=/data
Type=ext4
Options=noatime,acl,user_xattr
```


#### 2.2.4 automount

和mount类似，区别是automount仅会在用户访问对应目录的时候去挂载它，而不是像mount一样从启动后一直挂载。
可以通过 `autofs`

使用automount能力。当前环境没有默认安装。下面例子介绍如何使用automount服务。

1 安装autofs服务

```
dnf install -y autofs
```


2 然后在 `/etc/auto.master`

文件中配置 `automount`

服务。

```
vim /etc/auto.master
```


在文件末尾添加以下内容：

```
/mnt/ /etc/auto.devices --timeout=10
```


其中， `/mnt/`

是挂载点所在的路径（不是设备挂载点）， `/etc/auto.devices`

是设备挂载配置文件的路径， `--timeout=10`

表示设备挂载超时时间为10秒。

3 在 `/etc/auto.devices`

文件中配置需要挂载的设备。可以使用以下命令打开 `/etc/auto.devices`

文件：

```
vim /etc/auto.devices
```


在文件中添加需要挂载的设备信息，例如：

```
mymnt -fstype=auto :/dev/vdb
```


其中， `mymnt`

是挂载的目录， `-fstype=auto`

表示自动检测设备文件系统类型， `:/dev/vdb`

是设备的路径。

4 重启 `autofs`

服务

```
systemctl restart autofs
```


5 现在，当需要访问 `mymnt`

设备时，只需要访问 `/mnt/`

目录下的 `mymnt`

的目录， `automount`

服务会自动将 `/dev/vdb`

设备挂载到这个目录下。
**这里需要注意，进入 /mnt目录时，是看不到 mymnt目录的，并且也无法通过tab补全，但是你可以直接访问它**


```
cd /mnt/mymnt
```


当访问 `/mnt/mymnt`

目录时， `automount`

服务会自动将 `/dev/vdb`

设备挂载到这个目录下。

```
# lsblk
NAME MAJ:MIN RM SIZE RO TYPE MOUNTPOINTS
sr0 11:0 1 18.8M 0 rom
zram0 251:0 0 8G 0 disk [SWAP]
vda 252:0 0 100G 0 disk
└─vda1 252:1 0 100G 0 part /
vdb 252:16 0 200G 0 disk /mnt/mymnt
vdc 252:32 0 300G 0 disk
└─vdc1 252:33 0 300G 0 part /data
```


如果一段时间内没有访问该目录， `automount`

服务会自动卸载设备，以释放系统资源。

#### 2.2.5 target

target unit和上面几个unit不太一样，它本身不执行任何操作，仅仅只是一个“代表”，代表了一个群组的unit，target靠Requires=/After=等unit的依赖配置来控制每个群组unit的依赖关系和启动顺序，通过systemctl list-dependencies可以看到。

```
multi-user.target
● ├─acpid.service
● ├─arpwatch.service
● ├─atd.service
● ├─auditd.service
● ├─avahi-daemon.service
● ├─chrony-wait.service
● ├─chronyd.service
● ├─crond.service
● ├─gssproxy.service
```


系统启动时就是通过一个一个的target服务，来按顺序拉起各个子系统所依赖的具体服务。
例如，启动时系统只需要拉起 `default.target`

（本系统中为 `multi-user.target`

或 `graphical.target`

），其他的各个target只要在他们的unit file中指定

```
[Install]
WantedBy=multi-user.target
```


就可以实现在 `multi-user.target`

启动前启动。

#### 2.2.6 path

和timer unit类似，主要作用是当监控的路径改变时，触发同名的service，在[Path]字段中的DirectoryNotEmpty=/PathChanged=等去控制监控的路径以及对应的模式。

```
[root@localhost ~]# systemctl cat systemd-ask-password-console.path
# /usr/lib/systemd/system/systemd-ask-password-console.path
# SPDX-License-Identifier: LGPL-2.1-or-later
#
# This file is part of systemd.
#
# systemd is free software; you can redistribute it and/or modify it
# under the terms of the GNU Lesser General Public License as published by
# the Free Software Foundation; either version 2.1 of the License, or
# (at your option) any later version.
[Unit]
Description=Dispatch Password Requests to Console Directory Watch
Documentation=man:systemd-ask-password-console.path(8)
DefaultDependencies=no
Conflicts=shutdown.target emergency.service
After=plymouth-start.service
Before=paths.target shutdown.target cryptsetup.target
ConditionPathExists=!/run/plymouth/pid
[Path]
DirectoryNotEmpty=/run/systemd/ask-password
MakeDirectory=yes
```


以下以实例介绍path服务如何使用。

1 创建一个新的 `.path`

单元文件。在 `/etc/systemd/system`

目录下创建一个新文件，例如 `my-path-monitor.path`

。在这个文件中，定义要监视的路径和触发条件。例如：

```
[Unit]
Description=Monitor changes in /data/testpath directory
[Path]
PathModified=/data/testpath
Unit=my-triggered-service.service
[Install]
WantedBy=multi-user.target
```


这个 `.path`

单元文件将监视 `/data/testpath`

目录的更改。当该目录发生更改时，它将触发名为 `my-triggered-service.service`

的服务。

2 创建一个与 `.path`

单元关联的服务单元。在本例中，需要创建一个名为 `my-triggered-service.service`

的服务文件。在 `/etc/systemd/system`

目录下创建一个新文件，并定义服务的行为。例如：

```
[Unit]
Description=Service triggered by path changes
[Service]
Type=oneshot
ExecStart=/usr/bin/echo "123"
```


这个服务将在 `.path`

单元触发时执行 `echo 123`

脚本。

3 重新加载 `systemd`

配置以识别新的单元文件：

```
systemctl daemon-reload
```


4 启动 `.path`

单元：

```
systemctl start my-path-monitor.path
```


5 现在，修改或者删除这个目录

```
rm -r /data/testpath
```


6 然后查看 `my-triggered-service.service`

日志，你会发现，该服务被path服务触发了

```
# systemctl status my-triggered-service.service
○ my-triggered-service.service - Service triggered by path changes
Loaded: loaded (/etc/systemd/system/my-triggered-service.service; static)
Active: inactive (dead) since Mon 2023-05-29 03:09:15 UTC; 9s ago
TriggeredBy: ● my-path-monitor.path
Process: 1227670 ExecStart=/usr/bin/echo 123 (code=exited, status=0/SUCCESS)
Main PID: 1227670 (code=exited, status=0/SUCCESS)
CPU: 1ms
May 29 03:09:15 localhost.localdomain systemd[1]: Starting my-triggered-service.service - Service triggered by path changes...
May 29 03:09:15 localhost.localdomain echo[1227670]: 123
May 29 03:09:15 localhost.localdomain systemd[1]: my-triggered-service.service: Deactivated successfully.
May 29 03:09:15 localhost.localdomain systemd[1]: Finished my-triggered-service.service - Service triggered by path changes.
```


#### 2.2.7 socket

socket unit和timer/path一样，也是配合service unit使用的，通过socket unit指定systemd监听的socket，当socket有写入的时候systemd唤醒该unit对应的service unit。

```
[root@localhost ~]# systemctl cat acpid
# /usr/lib/systemd/system/acpid.service
[Unit]
Description=ACPI Event Daemon
Documentation=man:acpid(8)
Requires=acpid.socket
[Service]
StandardInput=socket
EnvironmentFile=/etc/sysconfig/acpid
ExecStart=/usr/sbin/acpid -f $OPTIONS
[Install]
Also=acpid.socket
WantedBy=multi-user.target
```


```
[root@localhost ~]# systemctl cat acpid.socket
# /usr/lib/systemd/system/acpid.socket
[Unit]
Description=ACPID Listen Socket
Documentation=man:acpid(8)
[Socket]
8ListenStream=/run/acpid.socket
[Install]
WantedBy=sockets.target
```


下面以一个实例介绍如何使用socket服务

1 安装 `nc`

工具

```
dnf install nc -y
```


2 为 Python 应用程序创建一个 `systemd`

服务单元文件。在 `/etc/systemd/system`

目录下创建一个名为 `socket_server.service`

的文件，并添加以下内容：

```
[Unit]
Description=Socket Server
[Service]
ExecStart=nc -l 12345
User=nobody
Group=nobody
```


3 创建一个 `systemd`

socket 单元文件。在 `/etc/systemd/system`

目录下创建一个名为 `socket_server.socket`

的文件，并添加以下内容：

```
[Unit]
Description=Socket Server Socket
[Socket]
ListenStream=12345
Accept=yes
[Install]
WantedBy=sockets.target
```


这个 `.socket`

单元文件将在 12345 端口上创建一个 TCP 套接字，并在接收到连接请求时激活 `socket_server.service`

。

4 重新加载 `systemd`

配置以识别新的单元文件：

```
systemctl daemon-reload
```


5 启动 `.socket`

单元：

```
systemctl start socket_server.socket
```


现在，套接字已经创建并开始监听连接。当有客户端连接到端口 12345 时， `socket_server.service`

将被激活并执行 `nc -l 12345`

。

6 使用 `telnet`

或 `nc`

（netcat）连接到端口 12345：

```
telnet localhost 12345
```


#### 2.2.8 swap

管理swap分区挂载，和mount类似，通常也是通过/etc/fstab配置，然后systemd-fstab-generator自动生成

1 创建一个 swap 文件（如果你还没有一个）：

```
fallocate -l 1G /swapfile
```


2 将文件设置为 swap：

```
mkswap /swapfile
```


3 在 `/etc/fstab`

文件的末尾添加一行，指定 swap 分区或文件的路径、挂载点（使用 `none`

）、文件系统类型（使用 `swap`

）以及挂载选项（使用 `sw`

）。最后，添加两个数字 `0 0`

，表示不需要进行文件系统检查。例如：

```
/swapfile none swap sw 0 0
```


现在，你已经成功地在 `fstab`

中配置了 swap。在每次系统启动时，swap 分区或文件都会自动启用。
重启后看到，已自动创建对应的swap服务

```
# systemctl list-units -a | grep swap
swapfile.swap loaded active active /swapfile
```


你可以使用 `free -h`

或 `swapon --show`

命令查看 swap 的状态。通过 `free`

命令看到

```
# free -h
total used free shared buff/cache available
Mem: 7.5Gi 195Mi 7.1Gi 9Mi 210Mi 7.1Gi
Swap: 1.0Gi 0B 1.0Gi
```


#### 2.2.9 device

是由systemd-udevd根据/sys/和/dev下的设备创建出来的unit，主要作用是控制设备和设备之间以及设备和其他unit之间的依赖关系。

```
[root@localhost ~]# systemctl list-dependencies mnt.mount
mnt.mount
● ├─-.mount
● ├─dev-vdb1.device
● ├─system.slice
○ └─systemd-fsck@dev-vdb1.service
```


#### 2.2.10 slice

slice类似target，也是一组unit的代表，但是不同的是slice用来在cgroup中进行资源控制，正常系统默认将unit分为user.slice（用户会话）/system.slice（系统进程）/machine.slice（容器和虚拟机进程）

```
[root@localhost ~]# tree -d /sys/fs/cgroup/
/sys/fs/cgroup/
├── dev-hugepages.mount
├── dev-mqueue.mount
├── init.scope
├── proc-fs-nfsd.mount
├── proc-sys-fs-binfmt_misc.mount
├── sys-fs-fuse-connections.mount
├── sys-kernel-config.mount
├── sys-kernel-debug.mount
├── sys-kernel-tracing.mount
├── system.slice
│ ├── NetworkManager.service
│ ├── acpid.service
│ ├── arpwatch.service
│ ├── atd.service
│ ├── auditd.service
│ ├── avahi-daemon.service
│ ├── chronyd.service
│ ├── systemd-logind.service
│ ├── systemd-udevd.service
│ │ └── udev
│ ├── systemd-userdbd.service
│ ├── tmp.mount
│ └── var-lib-nfs-rpc_pipefs.mount
└── user.slice
└── user-0.slice
├── session-1702.scope
├── session-22304.scope
```


#### 2.2.11 scope

与slice/target类似，不同的是scope unit仅可以通过systemd dbus的接口去创建，并且scope unit中的进程不会自己去创建子进程。

### 3. unit配置

systemd支持的unit配置参数数量庞大，大部分问题也都和配置有关系，这里以cpu资源控制相关配置举例，cpu的资源控制配置主要由以下几种方式决定：

#### 3.1 default配置

systemd有一个unit配置表ConfigTableItem，表中的配置项都会有默认初始值，如果后续没有去手动配置，则这些属性都会使用代码中初始值，CPUAccounting是false。可以在src/core/main.c文件中查看

```
static int parse_config_file(void) {
const ConfigTableItem items[] = {
{ "Manager", "LogLevel", config_parse_level2, 0, NULL },
{ "Manager", "LogTarget", config_parse_target, 0, NULL },
.....
```


#### 3.2 manager配置文件

```
/etc/systemd/system.conf
/etc/systemd/user.conf
/etc/systemd/system.conf.d/*
/etc/systemd/user.conf.d/*
```


#### 3.3 unit file

unit自己的配置文件，一般在 `/usr/lib/systemd/system/`

下。可以通过 `systemctl cat a.service`

查看具体内容（这里要注意可能有除了unit file的额外配置文件，所以通过systemctl cat可以看的更全，
通过 `systemctl set-property`

命令手动设置，这种方式也是最终会在/etc/systemd下面生成对应unit的额外配置文件），如下示例：

```
# systemctl set-property rsyslog.service CPUQuota=50%
# systemctl show rsyslog.service | grep CPUQuota
...
DropInPaths=/etc/systemd/system.control/rsyslog.service.d/50-CPUQuota.conf
```


可以看到最终会生成 `/etc/systemd/system.control/rsyslog.service.d/50-CPUQuota.conf`

这个额外配置文件。

```
# cat /etc/systemd/system.control/rsyslog.service.d/50-CPUQuota.conf
# This is a drop-in unit file extension, created via "systemctl set-property"
# or an equivalent operation. Do not edit.
[Service]
CPUQuota=50%
```


### 4. 服务启动顺序

systemd服务的启动顺序，是通过配置相互依赖关系实现的，unit与unit之间的依赖关系分为多种情况。 首先，systemd unit会自动生成依赖，自动生成的依赖分为两种：隐式依赖（Implicit Dependencies）和默认依赖（Default Dependencies）。

- 隐式依赖通过unit Type和Unit的配置决定，例如dbus.service的Type=dbus，会隐式依赖dbus.socket（等价于Requires= 以及 After=dbus.socket）。
- 默认依赖和隐式依赖差不多，但是可以通过DefaultDependencies=选项控制开关，例如A.target里配置了Wants= 或者 Requires=B，那A会默认被配置一个After=B。另外，所有的target都会默认配置一个Conflicts=shutdown.target和Before=shutdown.target，为了保证在关机前所有target都已退出。Triggers/TriggeredBy则会默认配置在socket/path/mount等他们对应的service里会。

除此之外，显示配置的依赖关系主要有6个（两个放一起因为他们逻辑相同只不过是行为完全相反）：

- Wants/WantedBy：弱依赖，A Wants= B，A启动的时候会尝试拉起B，如果B启动失败，A会继续启动。（除了直接在unit file里面配置外，还可以通过在unit file外创建.wants目录实现同样的效果）。
- Requires/RequiredBy：强依赖，A Requires= B，同Wants一样，A启动的时候会尝试拉起B，如果B启动失败，A不会启动。（同Wants一样，也可以通过创建.requires/目录实现相同效果）。
- BindsTo/BoundBy：更强依赖，与Requires不一样的是，A BindsTo= B，如果A关闭了，B也会关闭，而Requires的话，B不会受影响。
- Before/After：字面意思，例如A Before= B，这样在A启动后，B才能启动，同样，关闭流程则基于启动流程相反，在A Before= B时，如果A和B都需要关闭，那B先关闭，A才会关闭。
- PartOf/ConsistsOf：和Requires相似，不一样的是PartOf只影响关闭和重启动作，例如A PartOf= B，那B被关闭或者重启时，A也会被关闭或者重启。
- Conflicts/ConflictedBy：如字面意思，A Conflicts= B，那启动A就会关闭B。

例如，如果想要查看rsyslog服务是由谁拉起的，可以通过 `list-dependencies`

命令：

```
# systemctl list-dependencies rsyslog --reverse
rsyslog.service
● └─multi-user.target
○ └─graphical.target
```


而之所以有如此依赖关系，是因为rsyslog服务的unit file中有如下配置：

```
systemctl cat rsyslog.service
# /usr/lib/systemd/system/rsyslog.service
[Unit]
...
[Install]
WantedBy=multi-user.target
...
```