source: https://docs.opencloudos.org/en/OCS/AdministratorGuide/Local_Management/

# 本地化管理

本文将会介绍关于本地化管理的基础知识以及相关配置。通过本地化管理，能够让系统更符合用户所在地区的使用习惯。

本地化管理通常涉及以下内容：

- 语言和地区：设置系统的显示语言、日期和时间格式、货币符号等。
- 时区：设置系统显示的本地时间。
- 键盘布局：不同的国家和地区可能使用不同的键盘布局，如 QWERTY、AZERTY 和 QWERTZ 等。
- 字体：设置系统中文本的显示样式。不同的字体可能支持不同的字符集和排版效果。
- 输入法：允许在系统中输入不同的字符集，如中文、日文等。

## 1. 语言和地区

系统的语言和地区等设置通过 locale 变量控制，locale 环境变量是一组用于控制本地化设置的变量，影响系统中的语言、字符编码、日期等方面，以下是一些主要的 `locale`

环境变量及其作用：

`LANG`

：设置系统的默认语言和字符编码。其他未设置的`LC_*`

变量将使用`LANG`

变量的值。`LC_CTYPE`

：控制字符分类和转换，例如字符的大小写转换、字符集和编码等。它还影响输入法和终端中的字符显示。`LC_NUMERIC`

：控制数字的显示格式，例如小数点符号和千位分隔符等。`LC_TIME`

：控制日期和时间的显示格式，例如星期名、月份名、日期顺序等。`LC_COLLATE`

：控制字符串比较和排序的规则。它影响诸如文件名排序和命令行参数排序等操作。`LC_MONETARY`

：控制货币的显示格式，例如货币符号、正负数表示等。`LC_MESSAGES`

：控制系统消息和提示的语言。它影响程序的错误消息、帮助信息等文本输出。`LC_PAPER`

：控制打印和页面设置的默认纸张尺寸。`LC_NAME`

：控制个人名字的显示格式，例如姓名顺序、姓名缩写等。`LC_ADDRESS`

：控制地址的显示格式，例如国家名、城市名、邮政编码等。`LC_TELEPHONE`

：控制电话号码的显示格式，例如国家代码、区号等。`LC_MEASUREMENT`

：控制度量单位的显示格式，例如公制或英制单位。`LC_IDENTIFICATION`

：控制元数据的显示格式，例如语言代码、国家代码等。

相关命令及常用操作：

- 查看 locale 配置：

locale 配置记录于 `/etc/locale.conf`

文件，可以看到系统默认配置 `LANG="C.UTF-8"`

，在 systemd 初始启动时会读取该文件进行系统环境配置。

也可以通过 `locale`

命令查看相关配置，其他未设置的 `LC_*`

变量都使用 `LANG`

变量的值。

```
>cat /etc/locale.conf
# This is the fallback locale configuration provided by systemd.
LANG="C.UTF-8"
>locale
LANG=C.UTF-8
LC_CTYPE="C.UTF-8"
LC_NUMERIC="C.UTF-8"
LC_TIME="C.UTF-8"
LC_COLLATE="C.UTF-8"
LC_MONETARY="C.UTF-8"
LC_MESSAGES="C.UTF-8"
LC_PAPER="C.UTF-8"
LC_NAME="C.UTF-8"
LC_ADDRESS="C.UTF-8"
LC_TELEPHONE="C.UTF-8"
LC_MEASUREMENT="C.UTF-8"
LC_IDENTIFICATION="C.UTF-8"
LC_ALL=
```


通常使用 `localectl`

命令对语言和地区进行设置，不建议直接修改 `/etc/locale.conf`

文件

- 列出本地所有支持的字符集，主要支持中文、英文以及默认的
`C.UTF-8`


```
>localectl list-locales
C.UTF-8
en_AU.UTF-8
en_BW.UTF-8
en_CA.UTF-8
en_DK.UTF-8
en_GB.UTF-8
en_HK.UTF-8
en_IE.UTF-8
en_NZ.UTF-8
en_PH.UTF-8
en_SC.UTF-8
en_SG.UTF-8
en_US.UTF-8
en_ZA.UTF-8
en_ZW.UTF-8
zh_CN.UTF-8
zh_HK.UTF-8
zh_SG.UTF-8
zh_TW.UTF-8
```


locale 命名规则为：<语言>_<地区>.<字符集编码> ，常见的中文和英文locale定义如下：

`zh_CN.UTF-8`

：表示语言为中文`zh`

，地区为中国大陆`CN`

，字符集编码为`UTF-8`


`en_US.UTF-8`

：表示语言为英文`en`

，地区为美国`US`

，字符集编码为`UTF-8`


- 显示当前的语言和地区设置

`System Locale`

指明系统使用的默认 `Lang`

值，默认使用 `C.UTF-8`


```
>localectl status
System Locale: LANG=C.UTF-8
VC Keymap: n/a
X11 Layout: n/a
```


`C.UTF-8`

的提出已经有多年历史，直到 glibc-2.35 发布正式提供 `C.UTF-8`

，随后 systemd 将其设置为默认 locale。本系统使用 `C.UTF-8`

作为默认 locale。

不像 `zh_CN.UTF-8`

、`en_US.UTF-8`

代表某个地区使用的语言环境，`C.UTF-8`

采用标准 C 作为语言环境，但字符编码为 UTF-8。字符串排序和比较是基于字节值的，而不是基于特定语言的规则。日期、时间和数字格式等也使用基本的英语表示。使用 `C.UTF-8`

不依赖于特定的本地化设置，可以确保程序在不同系统之间具有更好的兼容性和可移植性。

- 设置系统的本地化字符集为简体中文

```
>sudo localectl set-locale zh_CN.UTF-8
```


- 重启应用设置

```
>reboot
```


- 如果需要查看更多参数以及信息：
`localectl --help`

、`man localectl(1)`

、`man locale.conf(5)`


## 2. 时区

时区是用于表示计算机的本地时间与协调世界时（UTC）之间的差异。正确设置时区对于确保系统时间准确、计划任务和日志记录等功能正常运行非常重要。

- 世界协调时 UTC（Universal Time Coordinated）：最主要的世界时间标准，以原子时的秒长为基础，与时区无关。
- 时区：基于用户所在地区的时间标准。

timedatectl 与 date 都是Linux系统中用于管理和显示日期和时间的命令，但它们的功能和用途有所不同。

-
timedatectl：systemd工具，侧重于管理系统时钟和时区设置；可以修改系统时间和硬件时间。

-
date：UNIX 工具，主要用于查看和设置当前日期和时间；只会修改系统时间，需要配合 hwlock 修改硬件时间。


硬件时钟 与 系统时钟

-
硬件时钟（Real-Time Clock, RTC）：像时钟一样输出实际时间的电子设备，由物理层面的主板上电池供电的时钟，系统电源掉电后仍然能够正常运行。

-
系统时钟（System Clock）：在系统中的时钟，系统启动过程中会根据硬件时钟计算系统时钟的初始值，启动后系统时钟独立于硬件时钟运行。


### 2.1 使用 timedatectl

- 列出当前可用时区

```
>timedatectl list-timezones
Africa/Abidjan
Africa/Accra
Africa/Addis_Ababa
Africa/Algiers
Africa/Asmara
Africa/Asmera
...
```


- 显示系统当前的日期和时间

```
>timedatectl status
Local time: Mon 2023-05-08 16:19:13 CST // 本地时间
Universal time: Mon 2023-05-08 08:19:13 UTC // UTC 时间
RTC time: Mon 2023-05-08 08:19:13 // RTC 时间
Time zone: Asia/Beijing (CST, +0800) // 时区
System clock synchronized: no // NTP 同步情况
NTP service: active // NTP 启用状态
RTC in local TZ: no // RTC 是否使用本地时间
```


- 修改系统时区

```
>timedatectl set-timezone [TIMEZONE]
```


- 修改系统时间

```
>timedatectl set-time YYYY-MM-DD
>timedatectl set-time HH:MM:SS
```


- 设置系统时间NTP同步，会修改 NTP service 的值

```
>timedatectl set-ntp [BOOL]
```


网络时间协议NTP（Network Time Protocol）：用来使客户端和服务器之间进行时钟同步。NTP服务器从权威时钟源（例如原子钟、GPS）接收精确的世界协调时UTC，客户端再从服务器请求和接收时间。

### 2.2 使用 date、hwclock

- 显示本地时间

```
>date
```


- 显示 UTC 时间

```
>date --utc
```


- 通过
`date +"format"`

自定义日期输出格式，关于 format 格式详细内容可通过命令 man date 在手册中查看：

```
>date +%y%m%d
230508
>date +"%D %H:%M:%S"
05/08/23 17:48:31
```


- 修改系统时间

```
>date --set YYYY-MM-DD
>date --set HH:MM:SS
```


- 显示当前硬件的日期和时间

```
>hwclock
```


- 修改当前硬件的日期和时间

```
>hwclock --set --date "MM/DD/YYYY HH:MM"
```


- 如果硬件时间与系统时间不一致，可以通过互相同步进行修改：

将硬件时间同步到系统时间

```
>hwclock --hctosys
```


将系统时间同步到硬件时间

```
>hwclock --systohc
```


-
FAQ：如果使用虚拟机启动之后，本地时间被当成UTC时间导致时间显示错误。 查看虚拟机硬件时间是否正确，可能是因为虚拟机将本地时间当成UTC时间，进行了错误的硬件时间设置，从而影响了系统时间。通过修改硬件时间，并同步到系统时间即可恢复

-
如果需要查看更多参数以及信息：

`timedatectl --help`

、`man timedatectl(1)`

、`man date(1)`

、`man hwclock(8)`


## 3. 键盘布局

不同的国家和地区可能使用不同的键盘布局，通过 localectl 可以设置当前系统的键盘布局

- 列出本地所有支持的键盘布局

```
>localectl list-keymaps
al
al-plisi
at
at-mac
at-nodeadkeys
az
ba
...
```


- 显示当前的键盘设置

```
>localectl status
System Locale: LANG=en_US.UTF-8
VC Keymap: n/a
X11 Layout: n/a
```


- 设置系统的键盘布局，root用户运行

```
>sudo localectl set-keymap us
```


## 4. 字体

通过设置字体可以设置系统中文本的显示样式

### 4.1 下载字体

本章节介绍如何安装中文字体并使用 `fontconfig`

进行字体管理

- 安装 fontconfig 软件包

```
>yum install fontconfig
```


- 查看可用字体

```
>fc-list
```


- 查看可用的中文字体

```
>fc-list :lang=zh
```


- 列出可下载的简体中文字体

```
>dnf list *cjk-sc*
Last metadata expiration check: 3:44:09 ago on Thu May 25 13:03:02 2023.
Available Packages
# 简体中文无衬线字体
google-noto-sans-cjk-sc-fonts.noarch 20201206-4.ocs23 AppStream
# 简体中文等宽字体
google-noto-sans-mono-cjk-sc-fonts.noarch 20201206-4.ocs23 AppStream
# 简体中文衬线字体
google-noto-serif-cjk-sc-fonts.noarch 20201206-4.ocs23 AppStream
```


- 以下载简体中文无衬线字体为例进行下载

```
>dnf install google-noto-sans-cjk-sc-fonts.noarch
```


- 检验是否下载对应字体

```
>fc-list :lang=zh
```


### 4.2 下载第三方字体

如果系统没有提供所需字体，也可以自行获取所需字体

首先创建存放字体文件目录，并将要安装的字体上传到该文件夹下

- 为所有用户安装的字体，建议将字体文件复制到
`/usr/local/share/fonts/`

目录下

```
>mkdir -p /usr/local/share/fonts/new_fonts
>cp example.ttf /usr/local/share/fonts/new_fonts
```


- 为某个用户安装字体，建议将字体文件复制到用户的主文件夹
`~/.fonts`

中

```
>mkdir -p ~/.local/share/fonts/new_fonts
>cp example.ttf ~/.local/share/fonts/new_fonts
```


- 更新字体缓存

```
>fc-cache
```


- 检查新添加的字体是否列在可用字体中

```
>fc-list | grep -i new_fonts
```


- 返回第一个匹配的字体

```
>fc-match Font-Name
```


- 如果需要查看更多参数以及信息：
`fc-list --help`

、`man fc-list(1)`

、`man fonts-conf(5)`


## 5. 输入法

本节介绍如何通过 IBus（Intelligent Input Bus）输入法框架在图形界面使用拼音输入法和五笔输入法。

- 首先安装图形界面，如果当前已经是图形界面则跳过

```
>dnf groupinstall 'Server with GUI'
```


- 设置图形模式为默认启动目标

```
>systemctl set-default graphical.target
```


- 重启应用设置

```
>reboot
```


- 安装拼音输入法

```
>dnf install ibus-libpinyin
```


- 安装五笔输入法，系统提供了“海峰五笔”以及“极点五笔”两种五笔输入法，根据需要选择安装

```
>dnf install ibus-table-chinese-wubi-haifeng
>dnf install ibus-table-chinese-wubi-jidian
```


- 重启应用设置

```
>reboot
```


-
进入系统设置界面，选择“键盘”中的“输入源”，点击“+” 添加输入法，选择

`Chinese(China)`

，添加所需输入法。gnome 在菜单栏上会显示当前选择的输入源，默认切换输入法快捷键为`Super + 空格`

，其中`Super`

键通常为`Windows键（徽标键）`

-
查看支持的中文输入法：


```
>dnf list ibus-table-chinese*
Last metadata expiration check: 2:34:07 ago on Thu May 25 13:03:02 2023.
Available Packages
ibus-table-chinese.noarch 1.8.11-3.ocs23 AppStream
# 行列输入法
ibus-table-chinese-array.noarch 1.8.11-3.ocs23 AppStream
# 仓颉输入法
ibus-table-chinese-cangjie.noarch 1.8.11-3.ocs23 AppStream
# 广东话输入法
ibus-table-chinese-cantonese.noarch 1.8.11-3.ocs23 AppStream
# 基于耶鲁拼音的粤语输入法
ibus-table-chinese-cantonyale.noarch 1.8.11-3.ocs23 AppStream
# 轻松输入法
ibus-table-chinese-easy.noarch 1.8.11-3.ocs23 AppStream
# 二笔输入法
ibus-table-chinese-erbi.noarch 1.8.11-3.ocs23 AppStream
# 速成输入法
ibus-table-chinese-quick.noarch 1.8.11-3.ocs23 AppStream
# 快速仓颉输入法
ibus-table-chinese-scj.noarch 1.8.11-3.ocs23 AppStream
# 笔顺五码输入法
ibus-table-chinese-stroke5.noarch 1.8.11-3.ocs23 AppStream
# 上海吳语注音输入法
ibus-table-chinese-wu.noarch 1.8.11-3.ocs23 AppStream
# 海峰五笔输入法
ibus-table-chinese-wubi-haifeng.noarch 1.8.11-3.ocs23 AppStream
# 极点五笔86输入法 极爽词库 6.0
ibus-table-chinese-wubi-jidian.noarch 1.8.11-3.ocs23 AppStream
# 永码输入法
ibus-table-chinese-yong.noarch 1.8.11-3.ocs23 AppStream
```