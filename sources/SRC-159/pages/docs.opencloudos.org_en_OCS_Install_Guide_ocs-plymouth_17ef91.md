source: https://docs.opencloudos.org/en/OCS/Install_Guide/ocs-plymouth/

# 1. plymouth 简介

Plymouth 是一个在启动过程的早期运行的应用程序（甚至在安装根文件系统之前），它为启动过程在后台进行时提供图形启动动画，增强的视觉体验。此外，plymouth 还提供可用于调试的内置引导日志记录功能。 可以通过从各种静态或者动画图形主体中选择一个来自定义引导屏幕的外观，可以根据现有的主题创建新主题。

## 1.1 安装plymouth

```
dnf install plymouth -y
```


## 1.2 显示当前默认的plymouth主题

```
plymouth-set-default-theme
```


## 1.3 查看plymouth相关开机主题

```
>ls /usr/share/plymouth/themes/
details text tribar
```


或者执行

```
>plymouth-set-default-theme --list
details
text
tribar
```


## 1.4 更改默认的plymouth主题（从已安装里选择）

```
plymouth-set-default-theme tribar -R
```


由于 Plymouth 是通过引导加载程序启用的，因此有必要使用 -R 选项重新生成初始 ramdisk (initrd)。这样做将确保新的默认主题可以在引导过程中正确加载。

# 2 安装plymouth主题

## 2.1 从yum源上查找可用主题

```
>dnf search plymouth-theme*
Last metadata expiration check: 0:38:00 ago on Mon May 22 09:19:09 2023.
========================================================================================================== Name Matched: plymouth-theme* ==========================================================================================================
plymouth-theme-charge.x86_64 : Plymouth "Charge" plugin
plymouth-theme-fade-in.x86_64 : Plymouth "Fade-In" theme
plymouth-theme-script.x86_64 : Plymouth "Script" plugin
plymouth-theme-solar.x86_64 : Plymouth "Solar" theme
plymouth-theme-spinfinity.x86_64 : Plymouth "Spinfinity" theme
plymouth-theme-spinner.x86_64 : Plymouth "Spinner" theme
[root@localhost output_20230522_093245]# dnf search plymouth-theme
Last metadata expiration check: 0:38:12 ago on Mon May 22 09:19:09 2023.
```


使用 `dnf install -y`

安装即可

## 2.2 安装外部其他主题

先安装 `script`

plymouth 插件

```
dnf install plymouth-plugin-script
```


再 `git clone`

外部主题下来

```
git clone https://github.com/adi1090x/plymouth-themes
```


安装lone主题

```
cp plymouth-themes/pack_3/lone/ /usr/share/plymouth/themes/ -r
```


检查安装是否生效

```
> plymouth-set-default-theme -l
bgrt
details
lone
spinner
text
tribar
```


2.3 将安装的外来 plymouth主题设置为默认主题

将开机主题修改为 `lone`


```
plymouth-set-default-theme lone
```


修改结果可以在 `/etc/plymouth/plymouth.conf`

中查看到

```
>cat /etc/plymouth/plymouthd.conf
# Administrator customizations go in this file
[Daemon]
Theme=lone
```


为使得修改结果生效，执行：

```
dracut -f --kver $(uname -r)
```


或者执行

```
plymouth-set-default-theme -R lone
```


重启 `reboot -f`

，即可看到修改生效，开机动画如下所示

# 3. 附录

更多使用方法，请参考 https://gitlab.freedesktop.org/plymouth/plymouth/-/wikis/home