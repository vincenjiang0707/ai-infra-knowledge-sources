source: https://docs.opencloudos.org/OCS/Network_Guide/Email_guide/

# 邮件服务使用指南

## 1. 基本概念

### 1.1 postfix

Postfix 是一个邮件传输代理（MTA），用于在服务器之间传输电子邮件。采用模块化、简单易懂的设计，强调安全性和可控性。

### 1.2 电子邮件系统

电子邮件系统由以下几个组件组成：

- 邮件用户代理（MUA，Mail User Agent）：用户用于收发邮件的客户端程序，使用IMAP或POP3协议与服务器通信。常用MUA：thunderbird、mutt 等。
- 邮件传输代理（MTA，Mail Transfer Agent）：接收来自 MUA 的邮件，将邮件转发给远程服务器上的另一个 MTA，或将其传递给 MDA 交付，使用SMTP协议。常用MTA：sendmail、postfix
- 邮件交付代理（MDA，Mail Deliver Agent）：接收电子邮件并存储在用户的邮箱中，会对邮件进行扫描分类，具有过滤等功能。常用MDA：dovecot、procmail

常用协议如下：

- SMTP（Simple Mail Transfer Protocol）：发送邮件使用的标准协议
- IMAP（Internet Message Access Protocol）：接收邮件使用的标准协议，允许电子邮件客户端下载服务器上的邮件，但是在客户端的操作（如移动邮件、标记已读等），不会反馈到服务器上。
- POP3（Post Office Protocol 3）：提供服务器与电子邮件客户端之间的双向通信，客户端的操作都会反馈到服务器上，对邮件进行的操作，服务器上的邮件也会做相应的动作。

## 2. 检查环境

### 2.1 检查 MTA

在同一台服务器上安装多个 MTA 可能会导致冲突，因此需要检查是否存在其他 MTA，以 sendmail 为例：

- 检查是否安装 sendmail

```
>rpm -q sendmail
```


- 如果已经安装 sendmail，检查其服务状态

```
>systemctl status sendmail
```


- 如果 sendmail 服务状态为
`active (running)`

，则在安装和配置 postfix 之前需要停止 sendmail 服务

```
>systemctl stop sendmail
```


- 确保没有设置开机启动

```
>systemctl disable sendmail
```


### 2.2 检查防火墙

如果启用了防火墙服务，请配置相关防火墙服务允许 postfix 服务及对应端口；如果不确定是否启用防火墙服务，请依次检查 firewalld、iptables、nftables 状态，以 firewalld 为例：

- 检查是否安装 firewalld

```
>rpm -q firewalld
```


- 如果已经安装 firewalld，检查 firewalld 状态

```
>systemctl status firewalld
```


```
>sudo firewall-cmd --add-service=smtp --permanent
```


## 3. 配置 postfix

### 3.1 安装并启动 postfix 服务

- 检查系统是否已经安装 postfix

```
>rpm -qa | grep postfix
```


- 如果尚未安装首先需要安装 postfix，已经安装则可跳过该步骤

```
>sudo dnf install postfix
```


- 启动 Postfix 服务

```
>sudo systemctl start postfix
```


- 设置开机时自动启动 postfix 服务

```
>sudo systemctl enable postfix
```


- 检查 Postfix 状态，此时 postfix 服务状态应该为
`active (running)`


```
>sudo systemctl status postfix
```


### 3.2 配置 postfix

配置 postfix 可以通过直接修改配置文件 `/etc/postfix/main.cf`

，也可以通过命令行工具 `postconf`

进行修改。

- 如果需要修改多个配置参数，或者希望查看整个配置文件的上下文，编辑
`/etc/postfix/main.cf`

较为方便 - 如果需要快速修改或查询单个配置参数，使用
`postconf`

较为方便

```
# 查询配置参数
>postconf <parameter_name>
# 设置配置参数
>sudo postconf -e '<parameter_name> = <value>'
```


初次配置需要修改多项内容，使用直接修改配置文件 `/etc/postfix/main.cf`

的方法修改以下配置：

- myhostname：设置邮件服务器的主机名，格式是 host.domain.extension

```
myhostname = main.opencloudos.com
```


- mydomain：设置邮件系统的域名，格式是 host.domain.extension

```
mydomain = opencloudos.com
```


- myorigin：设置发件人地址的域名，通常与 mydomain 相同

```
myorigin = $mydomain
```


- inet_interfaces：设置监听的网络接口，通常设置为
`all`

以便监听所有可用的网络接口。

```
inet_interfaces = all
```


- mydestination：定义了哪些域名的邮件应该被视为本地邮件。通常设置为主机名、域名以及本地域名

```
mydestination = $myhostname, localhost.$mydomain, localhost, $mydomain
```


- mynetworks：定义邮件服务器可信任的发件人，值通常是一个以逗号分隔的 IP 地址和子网掩码列表。

```
mynetworks = 127.0.0.0/8
```


- home_mailbox：定义了用户的邮件存储位置，通常设置为
`Maildir/`


```
home_mailbox = Maildir/
```


默认设置为空，邮件存储于 `/var/spool/mail/username`

文件

设置值为 `Maildir/`

，邮件存储于 `/home/username/Maildir`

目录

- 修改配置后需要重新加载 Postfix 服务：

```
>sudo systemctl reload postfix
```


- 查看邮件服务器日志，可以看到成功启动 postfix 服务

```
>head /var/log/maillog
2023-05-30T11:00:56.049431+08:00 localhost postfix/postfix-script[4882]: starting the Postfix mail system
2023-05-30T11:00:56.057701+08:00 localhost postfix/master[4884]: daemon started -- version 3.7.2, configuration /etc/postfix
```


### 3.3 使用telnet测试配置是否有效

- 创建测试用户 sender、receiver

```
>useradd sender
>passwd sender
>useradd receiver
>passwd receiver
```


- 使用 telnet 测试

```
>telnet localhost smtp
Trying ::1...
Connected to localhost.
Escape character is '^]'.
220 main.opencloudos.com ESMTP Postfix
ehlo localhost // 向服务器发送问候信息，并请求服务器返回支持的邮件传输协议和扩展功能
250-main.opencloudos.com
250-PIPELINING
250-SIZE 10240000
250-VRFY
250-ETRN
250-STARTTLS
250-ENHANCEDSTATUSCODES
250-8BITMIME
250-DSN
250-SMTPUTF8
250 CHUNKING
mail from:sender // 填写发件人
250 2.1.0 Ok
rcpt to:receiver // 填写收件人
250 2.1.5 Ok
data // 开始输入邮件正文
354 End data with <CR><LF>.<CR><LF>
. // 结束输入邮件正文
250 2.0.0 Ok: queued as E89E340145
quit // 退出
221 2.0.0 Bye
Connection closed by foreign host.
```


- 查看接收到的邮件

```
>cat /home/receiver/Maildir/new/1685451254.Vfc01I20030M722181.localhost.localdomain
Return-Path: <sender@opencloudos.com>
X-Original-To: receiver
Delivered-To: receiver@opencloudos.com
Received: from localhost (localhost [IPv6:::1])
by main.opencloudos.com (Postfix) with ESMTP id E89E340145
for <receiver>; Tue, 30 May 2023 20:53:17 +0800 (CST)
Message-Id: <20230530125402.E89E340145@main.opencloudos.com>
Date: Tue, 30 May 2023 20:53:17 +0800 (CST)
From: sender@opencloudos.com
```


- 查看邮件服务器日志获取更多信息：

```
>tail /var/log/maillog
```


- 更多阅读：
`man postfix(1)`

、`man postconf(1)`

、`man postconf(5)`