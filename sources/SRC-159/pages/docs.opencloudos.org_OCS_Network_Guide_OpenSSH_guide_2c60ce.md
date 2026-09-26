source: https://docs.opencloudos.org/OCS/Network_Guide/OpenSSH_guide/

# OpenSSH 使用指南

SSH(Secure Shell)是一种加密网络协议，用于确保两个联网设备之间的通信安全。常用于远程访问服务器和其他网络设备，允许用户安全地登录并在远程系统上执行命令和文件传输。 OpenSSH 是 Linux 的默认 SSH 实现，它包括以下服务端和客户端工具：

`sshd`

OpenSSH 服务端守护进程。接受来自任何其他主机的 SSH 连接。可以自定义配置限制谁可以访问，以及允许哪些身份验证方法。`ssh`

用于启动到远程主机的 SSH 连接的客户端命令。`scp`

安全的远程文件复制程序。`sftp`

安全的文件传输程序。`ssh-agent`

缓存和管理用户的私钥或密码到内存中，用于公钥身份验证。`ssh-add`

为`ssh-agent`

添加私钥身份。`ssh-keygen`

生成和管理验证密钥。`ssh-copy-id`

将公钥安全地传输到远程主机，以设置公钥身份验证。

## 1 配置 sshd

sshd 附带一个可用的默认服务器配置文件 `/etc/ssh/sshd_config`

，其默认值都是注释掉的，可以输入自定义配置项来覆盖默认项。
更改配置后，执行 `sshd -t`

命令运行语法检查器，检查配置的语法是否正确。
然后执行以下命令重新加载配置。

```
systemctl reload sshd
```


重要：配置时保持对远程 SSH 服务器的访问 对任何 SSH 服务器进行更改时，要么具有对机器的物理访问权限，要么保持活动的 SSH 会话打开直到测试了更改并且一切正常，确保在修改出现问题时，可以还原或更正更改。


### 1.1 修改侦听地址和端口

sshd 的默认监听地址和端口为 0.0.0.0:22，可以配置指定的侦听地址和端口。

```
#Port 22
Port 2022
#ListenAddress 0.0.0.0
ListenAddress 192.168.1.2
```


### 1.2 允许 root 登录

最佳做法是保持默认配置，禁止 root 用户登录，以非特权用户身份登录远程计算机，然后通过 sudo 命令以 root 用户身份运行命令，或执行 `sudo su -`

切换到 root 用户。
如果真的想允许 root 登录，可以按照如下配置允许根用户通过公钥认证验证登录。

```
#PermitRootLogin no
PermitRootLogin prohibit-password PasswordAuthentication
```


如果需要允许根用户使用任何身份验证方法(包括密码)通过SSH登录。这比前面的选项更不安全，因为它允许根用户使用潜在的弱密码或受损密码登录，不建议使用这种方式。

```
#PermitRootLogin no
PermitRootLogin yes
```


### 1.3 禁用基于密码的身份验证

禁用密码身份验证来强制进行基于密钥的身份验证，可减少安全攻击面。要在 OpenSSH 服务器中禁用基于密码的验证，请编辑 sshd_config 并将 `PasswordAuthentication`

选项改为 `no`

。

```
#PasswordAuthentication yes
PasswordAuthentication no
```


### 1.4 限制对特定用户、组群的访问

sshd_config 配置文件中的 `AllowUsers`

和 `AllowGroups`

指令可只允许某些用户、域或组连接到 OpenSSH 服务器。可以组合 `AllowUsers`

和 `Allow Groups`

来更准确地限制访问，例如：

```
AllowUsers *@192.168.1.*,*@10.0.0.*,!*@192.168.1.10
AllowGroups example-group
```


*和 10.0.0.*子网中所有用户的连接，但 192.168.1.10 地址的系统除外。所有用户都必须在

`example-group`

组中。
## 2 OpenSSH 客户端使用

### 2.1 登录远程服务器

#### 2.1.1 密码验证登录

使用密码身份验证，需要远程服务器上具有 SSH 访问权限的用户登录名和密码。

```
ssh user@remote.example.com
```


如果远程服务器修改了 sshd 默认的监听端口 22，需要使用 -p 参数指定端口。

```
ssh -p 2022 user@remote.example.com
```


还可以使用以下命令在远程服务器上运行非交互式命令 。

```
ssh user@remote.example.com "df -h && du -sh"
ssh user@remote.example.com "sudo vim /etc/ssh/sshd_config"
```


当

`sudo`

在远程服务器上运行时，系统会提示用户输入`sudo`

密码。

#### 2.1.2 公钥认证登录

使用用户密钥进行认证，需要先在在本地系统上创建用户 SSH 密钥对。 然后，使用如下命令通过密码身份认证的方式将公钥复制到要访问的远程服务器上。需要远程服务器上具有 SSH 访问权限的用户登录名和密码，才能通过网络复制它。

```
# ssh-copy-id -i ~/.ssh/id_remote.pub user@remote.example.com
/usr/bin/ssh-copy-id: INFO: Source of key(s) to be installed: "/root/.ssh/id_remote.pub"
/usr/bin/ssh-copy-id: INFO: attempting to log in with the new key(s), to filter out any that are already installed
```


ssh-copy-id 的 -i 参数指定的是公钥文件，若不指定则将使用匹配 `~/.ssh/id*.pub`

的访问时间最近的文件。
如果远程服务器禁用基于密码的身份验证，则可以通过其他方式，如 usb 拷贝，手动将公钥复制到远程用户的 `~/.ssh/authorized_keys`

文件中。
然后尝试使用以下命令登录远程服务器：

```
ssh -i ~/.ssh/id_remote user@remote.example.com
```


`~/.ssh/id_rsa`

, `~/.ssh/id_ecdsa`

, `~/.ssh/id_ecdsa_sk`

, `~/.ssh/id_ed25519`

, `~/.ssh/id_ed25519_sk`

或 `~/.ssh/id_dsa`

。
如果密钥对在创建时时没有输入密码，将直接成功登录。
如果密钥对在创建时指定了私钥密码，将被要求输入私钥密码，而非用户帐户的密码。可以使用 `ssh-agent`

来避免每次发起 SSH 连接时输入私钥密码。

#### 2.1.3 使用 SSH 跳板机登录

使用 -J 参数指定跳板机的主机名或 IP 地址、用户名、以及端口，通过跳板机登录远程服务器：

```
ssh user@remote.example.com -J user@jump1.example.com:22
```


`,`

分割，按照顺序依次跳板机1、跳板机2等，最终到达目标主机：
```
ssh user@remote.example.com -J user1@jump1.example.com:22,user2@jump2.example.com:22
```


也可以编辑 `~/.ssh/config`

配置文件定义跳板机

-
定义跳板主机：

`Host jump-server HostName jump1.example.com User user Port 22`

`Host`

跳板机的名称或别名。可以匹是真实的主机名，也可以是任意字符串。`HostName`

跳板机的主机名或 IP 地址。`User`

跳板机的用户名`Port`

跳板机的 ssh 端口。

-
定义远程服务器使用

`ProxyJump`

：`Host remote-server HostName remote.example.com port 22 ProxyJump jump-server1`

`Host`

远程服务器的名称或别名。可以匹是真实的主机名，也可以是任意字符串。`HostName`

远程服务器的主机名或 IP 地址。`User`

远程服务器的用户名`Port`

远程服务器的 ssh 端口。`ProxyJump`

登录远程服务器所使用的跳板机器名称

-
通过跳板机连接到远程服务器：

`ssh remote-server`


#### 2.1.4 通过 ssh-agent 使用 SSH 密钥登录

为了避免在每次发起 SSH 连接时输入私钥密钥，可以使用 `ssh-agent`

工具缓存 SSH 私钥。
使用前需要先生成 SSH 密钥对，并将公钥传送到远程服务器。
`ssh-agent`

使用方法：

- 启动
`ssh-agent`

。`# eval $(ssh-agent) Agent pid 12039`

- 将密钥添加到
`ssh-agent`

。`# ssh-add ~/.ssh/id_rsa Enter passphrase for /root/.ssh/id_rsa: Identity added: /root/.ssh/id_rsa (user@host)`

- 使用 SSH 登录主机机器。
`# ssh user@remote.example.com Last login: Fri May 20 12:56:37 2023`


### 2.2 管理用户和主机加密密钥

在SSH中，有两种类型的密钥：用户密钥和主机密钥。

- 用户密钥用于用户身份验证，对每个用户都是唯一的。它们由公钥和私钥组成，用于对远程系统的用户进行身份验证。当用户使用SSH连接到远程系统时，客户端将用户的公钥发送给服务器，服务器使用该公钥验证用户的身份。用户密钥通常存储在用户主目录的
`~/.ssh`

中。在大多数情况下，私人用户密钥应该有强密码。 - 主机密钥用于主机身份验证，并且对于每个SSH服务器都是唯一的。它们由公钥和私钥组成，用于向用户验证远程系统。当用户使用SSH连接到远程系统时，服务器将其公钥发送给客户机，客户机使用该公钥验证服务器的身份。主机密钥通常存储在服务器的
`/etc/ssh`

目录中。主机密钥没有密码。

有多种密钥加密算法可供选择：DSA、RSA、ECDSA、ECDSA-SK、Ed25519 和 Ed25519-SK。 其中 DSA 在当前 OpenSSH 版本中已被禁用。RSA 是最通用也是默认的密钥类型，但在当前的 OpenSSH 版本不推荐 RSA 作为主机密钥。

#### 2.2.1 创建用户 SSH 密钥对

可以按照以下方法在本地系统中生成 SSH 密钥对：

```
# ssh-keygen
Generating public/private rsa key pair.
Enter file in which to save the key (/root/.ssh/id_rsa):
Enter passphrase (empty for no passphrase):
Enter same passphrase again:
Your identification has been saved in /root/.ssh/id_rsa
Your public key has been saved in /root/.ssh/id_rsa.pub
The key fingerprint is:
SHA256:MLuRZfL79OMqsHJ0fKX1PiyYZMNg1iG+OYTeg2n7Okc user@host
The key's randomart image is:
+---[RSA 3072]----+
| |
| . . |
| +ooo . |
| .X* . o |
| .+OS= + . |
| BoE.B . |
| o.*.*.+ o |
| . = ooo.o + |
| o.=..oooo . |
+----[SHA256]-----+
1. No.1.1
```


- 指定密钥的保存位置和密钥文件名称，如果不指定默认会在
`~/.ssh/`

目录下生成名为`id_密钥算法`

的私钥，和名为`id_密钥算法.pub`

的公钥。 - 指定私钥密钥，如果不指定默认为空，在大多数情况下，用户应该设置私钥密钥，并且应为强密码。

可以使用 `-t`

参数指定密钥算法，`-b`

参数指定密钥长度。

```
ssh-keygen -t ecdsa -b 384
```


`-f`

参数自定义名称（如果不使用 `-f`

指定，则会在在密钥生成过程中要求用户指定或确认使用默认名称）和 `-C`

参数添加可选的注释。这些可以帮助用户记住每个密钥对的用途。
```
ssh-keygen -f test-key -C "for test"
```


#### 2.2.2 创建 SSH 服务器主机密钥

SSH主机密钥是用于验证SSH服务器身份的一种机制。当客户端首次连接到 SSH 服务器时，服务器会生成一对密钥（公钥和私钥），并将公钥发送给客户端。客户端会将该公钥存储在本地的`~/.ssh/known_hosts`

文件中，并在后续连接时，客户端会使用该文件中存储的公钥来验证服务器身份的真实性。
主机密钥没有私钥密码，密钥对存储在 `/etc/ssh`

，OpenSSH 在安装时会自动生成一组主机密钥，包默认包含ECDSA，Ed25519，RSA三种密钥类型。

```
# ls -l /etc/ssh/
total 536
-rw-r--r--. 1 root root 505489 Apr 28 21:47 moduli
-rw-r--r--. 1 root root 1921 Apr 28 21:47 ssh_config
drwxr-xr-x. 2 root root 4096 Apr 28 21:49 ssh_config.d/
-rw-------. 1 root root 3550 May 4 17:32 sshd_config
drwx------. 2 root root 4096 Apr 28 21:49 sshd_config.d/
-rw-r-----. 1 root ssh_keys 492 May 4 17:13 ssh_host_ecdsa_key
-rw-r--r--. 1 root root 162 May 4 17:13 ssh_host_ecdsa_key.pub
-rw-r-----. 1 root ssh_keys 387 May 4 17:13 ssh_host_ed25519_key
-rw-r--r--. 1 root root 82 May 4 17:13 ssh_host_ed25519_key.pub
-rw-r-----. 1 root ssh_keys 2578 May 4 17:13 ssh_host_rsa_key
-rw-r--r--. 1 root root 554 May 4 17:13 ssh_host_rsa_key.pub
```


```
rm /etc/ssh/ssh_host*
ssh-keygen -A
```


### 2.3 使用 SCP 复制文件

要使用 SCP 传输文件，请指定远程服务器的 IP 地址或主机名以及希望它将文件或目录复制到的目标路径 。SCP 使用与 SSH 相同的用户名和凭据，不需要其他凭据。如果文件已存在于目的地，SCP 将替换或覆盖内容。

可以使用以下命令复制文件：

```
scp file1 user@remote.example.com:/home/user
```


`/home/user/`

目录。
也可以使用 -r 参数复制目录。要复制名为 dirctory1 的目录 ，请使用：
```
scp -r dirctory1 user@remote.example.com:/home/user
```


```
scp -P 2022 file1 user@remote.example.com:/home/user
```


```
scp -i ~/.ssh/id_remote file1 user@remote.example.com
```


### 2.4使用 SFTP 传输文件

SFTP 是一种安全的文件传输程序，它依赖于 SSH 并且是交互式的，使用与 SSH 相同的用户名和凭据。该工具类似于 FTP，但它使用的是 sshd 的监听端口，而非 FTP 端口。
当启动 SFTP 连接时，它会连接到其目的地并在远程服务器上进入交互模式。然后，使用 `get`

、 `put`

、 `cd`

、 `rmdir`

等命令传输文件。

要建立 SFTP 连接，请使用：

```
sftp user@remote.example.com
```


```
sftp -P 2022 user@remote.example.com
```


```
sftp -i ~/.ssh/id_remote user@remote.example.com
```


进入到 sftp 交互式界面后，使用 cd 命令切换本地系统当前工作目录，使用 put 命令上传文件，get 命令下载文件，在 put 命令后加 `-r`

参数上传目录，在 get 命令后加 `-r`

参数下载目录。

```
$ sftp user@remote.example.com
sftp> cd /etc
sftp> put /etc/file1
sftp> cd /opt;
sftp> get file2
sftp> put -r new_folder
sftp> get -r folder_from_remote
sftp> quit
```