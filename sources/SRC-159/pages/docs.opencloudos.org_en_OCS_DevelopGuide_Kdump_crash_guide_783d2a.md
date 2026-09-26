source: https://docs.opencloudos.org/en/OCS/DevelopGuide/Kdump_crash_guide/

# kdump/crash

## 1. 简介

kdump作为linux系统关键的问题定位调测技术，默认安装并激活（Anaconda安装时也已默认勾选kdump）。

## 2. kdump安装

查看确认kdump状态：

```
systemctl status kdump.service
```


如果显示**active**，则说明kdump服务处于激活状态：

```
● kdump.service - Crash recovery kernel arming
Loaded: loaded (/usr/lib/systemd/system/kdump.service; enabled; vendor preset: enabled)
Active: active (exited)
```


如果在安装时禁用了kdump，则可以通过以下步骤安装、激活kdump服务：

```
sudo dnf install kexec-tools
sudo systemctl start kdump.service
sudo systemctl status kdump.service
```


## 3. kdump配置

kdump的配置主要有3部分。

**配置预留内存**

预留内存是为了在系统crash时crashkernel能正常工作而预留的内存，与物理内存大小以及系统实际使用的物理内存大小都有关系。一般的，物理内存越大、被使用的物理内存越多，需要为crashkernel预留更多的内存。
如果kdump服务状态正常，但发生crash时没成功生成crash core，则就要考虑预留是否内存不足导致kdump工作异常。

kexec-tools软件包的kdump安装脚本根据不同的架构给出不同的配置，可以看到不同的物理内存大小设置不同的预留内存值：

```
if [[ $_arch == "x86_64" ]] || [[ $_arch == "s390x" ]]; then
_ck_cmdline="1G-4G:192M,4G-64G:256M,64G-:512M"
elif [[ $_arch == "aarch64" ]]; then
_ck_cmdline="2G-:448M"
```


修改该配置，可以通过**kdumpctl estimate**命令估算crashkernel预留内存值，可能不准确，可作为设置适当的crashkernel预留内存值的参考。

```
sudo vim /etc/default/grub
```


```
GRUB_CMDLINE_LINUX="i8042.noaux quiet console=ttyS0,115200 console=tty0 crashkernel=512M-64G:256M,64G-128G:512M,128G-:768M biosdevname=0 net.ifnames= 0 intel_idle.max_cstate=1 intel_pstate=disable"
```


```
sudo grub2-mkconfig -o /boot/efi/EFI/opencloudos/grub.cfg
```


```
sudo grubby --update-kernel ALL --args "crashkernel=自定义值”
```


**reboot**来使配置生效。

**配置转储目标**

crashkernel将已经发生crash的内核的内存等信息转储出来，以供后续的分析定位，转储相关的设置在配置文件**/etc/kdump.conf**中。

默认以文件形式转储在本地文件系统目录/var/crash中，并进行了内存过滤、压缩存储：

```
path /var/crash
core_collector makedumpfile -l --message-level 7 -d 31
```


**man makedumpfile**查看。

**kdump内核配置**

crashkernel启动时的命令行参数在配置文件**/etc/sysconfig/kdump**中。
设置后，通过如下命令来配置生效：

```
sudo systemctl restart kdump.service
```


## 4. 测试kdump配置

通过如下命令触发内核crash确认kdump配置正常：

```
su - root
echo c > /proc/sysrq-trigger
```


**/var/crash**）下可以看到生成的vmcore文件以及vmcore-dmesg.txt等日志文件。

## 5. crash

vmcore生成后，可以通过crash工具进行解析、定位问题。

### 5.1 安装

安装crash工具：

```
sudo dnf install crash
```


解析vmcore文件，需要有调试符号表文件，系统安装的内核一般都去除了调试符号，因此需要安装调试符号表文件。

```
sudo dnf debuginfo-install kernel
file /usr/lib/debug/lib/modules/$(uname -r)/vmlinux
```


```
/usr/lib/debug/lib/modules/6.1.26-2303.1.0.ocs23.x86_64/vmlinux: ELF 64-bit LSB executable, x86-64, version 1 (SYSV), statically linked, BuildID[sha1]=cc33cfbef9122f72d0ebbec283ebf6ffcfe9c06e, with debug_info, not stripped
```


### 5.2 运行crash工具

运行crash工具需要2个参数：带调试符号表的内核和vmcore文件。

```
sudo crash /usr/lib/debug/lib/modules/$(uname -r)/vmlinux vmcore
```


**help**命令查看crash支持的命令：

```
crash> help
* files mod sbitmapq union
alias foreach mount search vm
ascii fuser net set vtop
bpf gdb p sig waitq
bt help ps struct whatis
btop ipcs pte swap wr
dev irq ptob sym q
dis kmem ptov sys
eval list rd task
exit log repeat timer
extend mach runq tree
crash version: 8.0.2-3.ocs23 gdb version: 10.2
For help on any command above, enter "help <command>".
For help on input options, enter "help input".
For help on output options, enter "help output".
```


**man crash**了解更多信息。