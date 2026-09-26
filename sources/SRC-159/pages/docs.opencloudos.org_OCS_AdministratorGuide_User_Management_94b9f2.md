source: https://docs.opencloudos.org/OCS/AdministratorGuide/User_Management/

# 用户管理

## 1 用户管理

### 1.1 用户创建

要创建一个新用户，可以使用 `useradd`

命令。以下是一个示例：

```
sudo useradd -m -s /bin/bash username
```


其中， `-m`

参数表示创建用户的家目录， `-s`

参数表示指定用户的默认 shell， `username`

是新用户的用户名。

### 1.2 用户修改

要修改用户的属性，可以使用 `usermod`

命令。以下是一些常见的示例：

- 修改用户的密码：

```
sudo passwd username
```


其中， `username`

是要修改密码的用户的用户名。
- 修改用户的默认 shell：

```
sudo usermod -s /bin/zsh username
```


其中， `/bin/zsh`

是要设置的新 shell， `username`

是要修改的用户的用户名。
- 修改用户的家目录：

```
sudo usermod -d /home/newhome username
```


其中， `/home/newhome`

是要设置的新家目录， `username`

是要修改的用户的用户名。

### 1.3 用户删除

要删除一个用户，可以使用 `userdel`

命令。以下是一个示例：

```
sudo userdel -r username
```


其中， `-r`

参数表示删除用户的家目录和邮件目录。 `username`

是要删除的用户的用户名。

### 1.4 用户切换

在 root 身份下创建普通用户后，可 su 切换到新用户：

```
su username
```


必要时，切换回 root用户：

```
su -
```


### 1.5 密码管理

要管理用户的密码，可以使用 `passwd`

命令。以下是一些常见的示例：
- 修改当前用户的密码：

```
passwd
```


```
sudo passwd username
```


`username`

是要修改密码的用户的用户名。
- 禁用用户的密码：
```
sudo passwd -l username
```


`-l`

参数表示锁定用户的密码， `username`

是要禁用密码的用户的用户名。
- 解锁用户的密码：
```
sudo passwd -u username
```


`-u`

参数表示解锁用户的密码， `username`

是要解锁密码的用户的用户名。
## 2 用户组管理

### 2.1 用户组创建

创建新用户组，可使用 `groupadd`

命令：

```
sudo groupadd newgroup
```


### 2.2 用户组修改

使用 `groupmod`

命令，可修改现有用户组信息：

```
sudo groupmod -n newgroupname oldgroupname
```


### 2.3 用户组成员管理

- 添加成员

用户组创建完毕后，可通过 `usermod`

命令向组内添加用户成员：

```
sudo usermod -aG groupname username
```


也可使用 `gpasswd`

命令添加：

```
sudo gpasswd -a username groupname
```


- 查看成员

添加后，使用 `groups`

命令验证该用户是否已被正确添加到对应组：

```
groups username
```


也可 `cat /etc/group`

查看该组的所有成员，格式解析如下：

```
组名 : 密码存储 : 组ID : 用户名单
```


- 删除成员

使用 `usermod`

命令，可修改用户所属组：

```
# 查看 test_user所属组
groups test_user
test_user1 : test_user test_group root
# 修改其组，使test_user仅属于 test_group 组
sudo usermod -G test_group test_user
```


也可使用 `gpasswd`

命令，从指定用户组中，删除指定成员：

```
sudo gpasswd -d test_user test_group
```


### 2.4 用户组删除

使用 `groupdel`

，删除现有用户组：

```
sudo groupdel groupname
```


## 3 账户授权

### 3.1 禁止普通用户直接使用 su 命令

禁止普通用户直接使用 `su`

命令，只允许 wheel 组的用户切换到 root 用户。编辑 `/etc/pam.d/su`

文件，找到如下行：

```
#auth required pam_wheel.so use_uid
```


取消注释并保存：

```
auth required pam_wheel.so use_uid
```


### 3.2 添加用户到 wheel 组

普通用户在部分应用场景会需要 root 权限，此时可将其添加到 wheel 组。 wheel 组可用于授予特定用户 sudo 权限的。将用户添加到 wheel 组可以避免授予 root 权限。

首先，编辑 `/etc/sudoers`

文件，取消注释以下行，允许 wheel 组成员具备 sudo 权限：

```
%wheel ALL=(ALL) ALL
```


然后将对应用户添加后 wheel 组：

```
usermod -aG wheel username
```


退出当前会话，并验证 sudo 提权：

```
sudo ls /root/
```