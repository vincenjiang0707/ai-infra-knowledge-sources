source: https://docs.opencloudos.org/OCS/DevelopGuide/User_coredump_guide/

# 用户态coredump

## 1. 简介

用户态程序在收到某些异常信号时会产生core信息用于问题定位，用户态coredump默认由**systemd-coredump**处理。

## 2. coredump配置

查看确认coredump的配置:

```
cat /proc/sys/kernel/core_pattern
```


```
sysctl -a | grep core_pattern
```


**|/usr/lib/systemd/systemd-coredump**，则说明coredump由

**systemd-coredump**处理。

```
kernel.core_pattern = |/usr/lib/systemd/systemd-coredump %P %u %g %s %t %c %h
```


```
echo "kernel.core_pattern=core.%p.%e.%s" > /etc/sysctl.d/50-coredump.conf # /usr/lib/sysctl.d/下为发行版默认配置，如果要修改，建议在/etc/sysctl.d/下创建对应配置文件覆盖
/lib/systemd/systemd-sysctl # sysctl -p --load=/etc/sysctl.d/50-coredump.conf 也可以
```


```
sysctl -w kernel.core_pattern="core.%p.%e.%s"
```


**man core**。传统的coredump方式下生成的coredump文件在执行程序的当前目录下。

确认core文件大小限制，默认为unlimited，即大小不受限。

```
ulimit -c
unlimited
```


```
ulimit -S -c 0
```


```
* soft core 0
* hard core 0
```


## 3. systemd-coredump配置

systemd-coredump的配置文件为**/etc/systemd/coredump.conf**。
默认配置如下：

```
#Storage=external
#Compress=yes
#ProcessSizeMax=2G
#ExternalSizeMax=2G
#JournalSizeMax=767M
#MaxUse=
#KeepFree=
```


**man coredump.conf**、

**man systemd-coredump**。

/var/lib/systemd/coredump下的core文件3天后被删除，该配置在**systemd-tmpfiles**的配置文件**/usr/lib/tmpfiles.d/systemd.conf**中，详细信息可以查看**man tmpfiles.d**。

```
d /var/lib/systemd/coredump 0755 root root 3d
```


## 4. coredumpctl使用

由**systemd-coredump**处理的coredump可以使用coredumpctl工具处理。
测试程序如下：

```
#include <stdio.h>
#include <unistd.h>
int main() {
printf("Hello, world!\n");
int a = 0, b = 0;
int c = a / b;
return c;
}
```


```
Hello, world!
Floating point exception (core dumped)
```


```
core.helloworld.0.1a76f79d8ab248a9a448bccbdc58f70b.4805.1684808517000000.zst
```


**coredumpctl list**查看,可以看到core发生时间、产生core的进程号、进程UID/GID、触发core的信号、core文件状态、程序名、core文件大小。（注意：coredumpctl list查不到重启前的core文件）

```
TIME PID UID GID SIG COREFILE EXE SIZE
Tue 2023-05-23 10:21:57 CST 4805 0 0 SIGFPE present /home/helloworld 16.6K
```


使用**coredumpctl debug**调试：

```
coredumpctl debug helloworld # 匹配到最新的helloworld相关的core文件，也可以通过PID等匹配coredumpctl debug 4805
```


也可以先把core信息dump出来，然后用gdb来调试，即传统的coredump调试方式：

```
coredumpctl dump helloworld > core.file
```


```
file core.file
core.file: ELF 64-bit LSB core file, x86-64, version 1 (SYSV), SVR4-style, from './helloworld', real uid: 0, effective uid: 0, real gid: 0, effective gid: 0, execfn: './helloworld', platform: 'x86_64'
```


更多信息可以查看**man coredumpctl**。