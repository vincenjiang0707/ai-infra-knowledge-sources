source: https://docs.opencloudos.org/en/OCS/Install_Guide/ocs-desktop/

# 桌面安装

## 1. gnome桌面安装

当前提供gnome 43桌面。

- 查看rpm包group：

```
dnf group list
Last metadata expiration check: 0:31:30 ago on Wed May 31 19:04:32 2023.
Available Environment Groups:
Server with GUI
Server
Minimal Install
```


- 安装GUI group：

```
dnf group install "Server with GUI" -y
```


- 设置系统为图形模式，并重启：

```
systemctl set-default graphical.target
reboot
```


- 系统启动后，确认显示服务状态：

```
systemctl status gdm.service
● gdm.service - GNOME Display Manager
Loaded: loaded (/usr/lib/systemd/system/gdm.service; enabled; vendor preset: enabled)
Active: active (running) since Wed 2023-05-31 19:42:47 CST; 42s ago
Main PID: 979 (gdm)
```


- 桌面启动成功，登录桌面。