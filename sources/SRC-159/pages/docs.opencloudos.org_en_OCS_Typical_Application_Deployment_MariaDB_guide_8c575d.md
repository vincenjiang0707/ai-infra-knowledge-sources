source: https://docs.opencloudos.org/en/OCS/Typical_Application_Deployment/MariaDB_guide/

# MariaDB 服务器搭建指南

MariaDB 服务器是一个基于 MySQL 技术的开源快速且强大的数据库服务器。

本文将从安装、配置、备份及恢复等方面，介绍 MariaDB 服务器的搭建和使用。

## 1 安装 MariaDB

MariaDB 不在系统预装范围内，需要通过如下命令安装 MariaDB Server：

```
sudo dnf -y install mariadb-server
```


安装完毕后，可以执行如下指令验证安装结果：

```
mariadb --version
```


如果显示 MariaDB 版本号等信息，则说明安装成功。

```
mariadb Ver 15.1 Distrib 10.11.4-MariaDB, for Linux (x86_64) using EditLine wrapper
```


## 2 初始化 MariaDB

### 2.1 MariaDB 服务启动

安装完毕后，可手动启用 `mariadb`

服务：

```
sudo systemctl start mariadb.service
```


但手动启用后，系统重启后会关闭该服务。如果想要 `mariadb`

服务开机时自行启动，需要执行：

```
systemctl enable mariadb.service
```


### 2.2 MariaDB 服务初始化

首次启动服务后，需要进行初始化设置。

为了提升安装时的安全性，建议您通过以下方式初始化 MariaDB 数据库：

```
sudo mariadb-secure-installation
```


执行该命令后，会以交互方式提示配置过程的每个步骤：

- 选择密码强度，为 root 用户设置密码；
- 禁止匿名账户访问；
- 禁用 root 远程登录；
- 清理测试用的 test 数据库；
- 加载特权表；

建议按照提示设置一个强壮的 root 密码。此外，请删除匿名帐户，禁用远程 root 登录并删除测试数据库。

### 2.3 MariaDB 服务关闭

服务启动后，您也可以按需关闭 `mariadb`

服务：

```
sudo systemctl stop mariadb.service
```


## 3 配置 MariaDB

MariaDB 支持配置网络选项，可以通过编辑 `/etc/my.cnf.d/mariadb-server.cnf`

文件修改配置：

```
bind-address=127.0.0.1
port = 3306
skip-networking=1
```


各选项说明如下：

`bind-address`

：服务器监听地址，支持本地、IPv4、IPv6地址；`port`

：服务器监听的 TCP/IP 连接端口，默认为3306；`skip-networking`

：控制服务器是否监听 TCP/IP 连接。值为0表示监听所有客户端，值为1表示仅监听本地；

更多命令选项和系统变量，可执行以下指令查看：

```
mariadbd --verbose --help
```


该命令生成所有 mariadbd 选项和可配置系统变量 的列表。它的输出包括默认选项和变量值，示例如下：

```
abort-slave-event-count 0
activate-all-roles-on-login FALSE
admin-address (No default value)
admin-port 33062
admin-ssl TRUE
admin-ssl-ca (No default value)
admin-ssl-capath (No default value)
...
updatable-views-with-limit YES
upgrade AUTO
validate-config FALSE
validate-user-plugins TRUE
verbose TRUE
wait-timeout 28800
windowing-use-high-precision TRUE
xa-detach-on-prepare TRUE
```


## 4 使用 MariaDB

### 4.1 连接到 MariaDB 服务器

打开终端，输入以下命令以 root 身份连接到 MariaDB 服务器：

```
mysql -u root -p
```


根据提示，输入您在执行 `mariadb-secure-installation`

时设置的 root 密码。

### 4.2 创建数据库和表

下面的示例演示了如何创建数据库、表，并插入、查询数据。假设我们要创建一个简单的用户管理系统。连接到 MySQL 后，执行以下操作：

-
创建数据库：

`CREATE DATABASE user_manager;`

-
切换到该数据库：

`USE user_manager;`

-
创建

`users`

表：`CREATE TABLE users ( id INT AUTO_INCREMENT PRIMARY KEY, username VARCHAR(50) NOT NULL UNIQUE, email VARCHAR(255) NOT NULL UNIQUE, password_hash CHAR(60) NOT NULL, created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP );`

-
插入一些用户：

`INSERT INTO users (username, email, password_hash) VALUES ('Alice', 'alice@example.com', 'securehash1'), ('Bob', 'bob@example.com', 'securehash2');`


### 4.3 查询数据

查询所有用户：

```
SELECT * FROM users;
```


查询特定用户名的用户：

```
SELECT * FROM users WHERE username = 'Alice';
```


查询特定邮件地址的用户：

```
SELECT * FROM users WHERE email = 'alice@example.com';
```


### 4.4 更新数据

将 Bob 的电子邮件更新为新的电子邮件：

```
UPDATE users
SET email = 'newbob@example.com'
WHERE username = 'Bob';
```


### 4.5 删除数据

删除名为 Alice 的用户：

```
DELETE FROM users WHERE username = 'Alice';
```


### 4.6 创建用户和授权

为了确保安全性，不建议使用 root 用户进行日常操作。我们可以创建一个新用户并给予合适的权限。

-
创建新用户（在这里，我们将创建名为

`myuser`

的用户，并使用`12345678`

作为密码）：`CREATE USER 'myuser'@'localhost' IDENTIFIED BY '12345678';`

注：在设置密码时若收到提示 “ERROR 1819 (HY000): Your password does not satisfy the current policy requirements”，则可能是密码强度与当前密码不匹配；

可执行

`SHOW VARIABLES LIKE 'validate_password%';`

查看`validate_password.policy`

密码强度，令您的密码与强度匹配即可。 如果您确认您当前的密码满足安全需要，对密码强度不需要太高，则可以通过以下方式降低密码强度；`SET GLOBAL validate_password.policy=LOW;`

-
授予新用户访问

`user_manager`

数据库的所有权限：`GRANT ALL PRIVILEGES ON user_manager.* TO 'myuser'@'localhost';`

-
使权限生效：

`FLUSH PRIVILEGES;`


现在，可以使用新用户 `myuser`

连接到 MySQL 服务器。

## 5 TLS加密

默认情况下，MariaDB 使用未加密的连接。**为了安全连接，请在MariaDB** 服务器上启用 TLS 支持并配置客户端以建立加密连接。

### 5.1 生成证书和私钥

首先，需要生成一份服务器证书和私钥，可以使用自签名证书或购买商业证书。 这里为示范，故生成并采用自签名证书：

-
首先，确保已安装了 OpenSSL。如果尚未安装，请使用以下命令进行安装：

`sudo dnf install openssl`

-
生成CA证书和密钥：

`openssl genrsa -out ca-key.pem 2048 openssl req -new -x509 -key ca-key.pem -out ca.pem -days 3650 -subj "/CN=Your_CA_Name"`

将

`Your_CA_Name`

替换为你选择的CA名称。 -
生成服务器证书请求和密钥：

`openssl req -newkey rsa:2048 -days 365 -nodes -keyout server-key.pem -out server-req.pem -subj "/CN=<your_domain>"`

-
使用CA证书和密钥签署服务器证书请求，生成服务器证书：

`openssl x509 -req -in server-req.pem -days 365 -CA ca.pem -CAkey ca-key.pem -set_serial 01 -out server-cert.pem`


现在，你应该在当前目录中看到以下文件： `ca.pem`

、 `ca-key.pem`

、 `server-key.pem`

、 `server-req.pem`

和 `server-cert.pem`

。

### 5.2 配置 TLS 加密

现在我们已经有了证书和私钥，下一步是为 MariaDB 服务器启用 TLS 。

-
将 CA 和服务器证书存储在

`/etc/pki/tls/certs/`

目录中：`mv server-cert.pem /etc/pki/tls/certs/ mv ca.pem /etc/pki/tls/certs/`

-
设置 CA 和服务器证书的权限，使 MariaDB 服务器能够读取文件：

`chmod 644 /etc/pki/tls/certs/server-cert.pem /etc/pki/tls/certs/ca.pem`

由于证书是建立安全连接之前通信的一部分，因此任何客户端都可以在无需身份验证的情况下检索它们。因此，您不需要对CA和服务器证书文件设置严格的权限。

-
将服务器的私钥存储在

`/etc/pki/tls/private/`

目录中：`mv server-key.pem /etc/pki/tls/private/`

-
设置服务器私钥的安全权限：

`chmod 640 /etc/pki/tls/private/server-key.pem chgrp mysql /etc/pki/tls/private/server-key.pem`

如果未经授权的用户可以访问私钥，则与 MariaDB 服务器的连接将不再安全。

-
恢复 SELinux 上下文：

`restorecon -Rv /etc/pki/tls/`


### 5.3 配置 MariaDB 服务端加密

拥有证书、密钥后，可以在 MariaDB 服务器启用 TLS。

首先创建 `/etc/my.cnf.d/mariadb-server-tls.cnf`

文件，添加以下内容配置私钥、服务器和CA证书的路径：

```
[mariadb]
ssl_key = /etc/pki/tls/private/server.example.com.key.pem
ssl_cert = /etc/pki/tls/certs/server.example.com.crt.pem
ssl_ca = /etc/pki/tls/certs/ca.crt.pem
```


- 如果您有证书吊销列表 (CRL)，请配置 MariaDB 服务器以使用它：

```
ssl_crl = /etc/pki/tls/certs/example.crl.pem
```


- 可选：拒绝不加密的连接尝试。要启用此功能，请附加：

```
require_secure_transport = on
```


- 可选：设置服务器应支持的 TLS 版本，默认支持 TLS 1.1、TLS 1.2 和 TLS 1.3。例如，要支持 TLS 1.2 和 TLS 1.3，请附加：

```
tls_version = TLSv1.2,TLSv1.3
```


然后重新启动 `mariadb`

服务：

```
systemctl restart mariadb
```


配置完成后，可以通过以下方式继续验证。如果该 `have_ssl`

变量设置为 `YES`

，则表示启用 TLS 加密。

```
mysql -u root -p -e "SHOW GLOBAL VARIABLES LIKE 'have_ssl';"
Enter password:
+---------------+-------+
| Variable_name | Value |
+---------------+-------+
| have_ssl | YES |
+---------------+-------+
```


### 5.4 配置 MariaDB 客户端加密

将CA证书复制到 `/etc/pki/ca-trust/source/anchors/`

目录：

```
cp /etc/pki/tls/certs/ca.pem /etc/pki/ca-trust/source/anchors/
```


设置允许所有用户读取CA证书文件的权限：

```
chmod 644 /etc/pki/ca-trust/source/anchors/ca.pem
```


重建CA信任数据库：

```
update-ca-trust
```


然后创建 `/etc/my.cnf.d/mariadb-client-tls.cnf`

包含以下内容的文件：

```
[client-mariadb]
ssl
ssl-verify-server-cert
```


这些设置定义 MariaDB 客户端使用 TLS 加密 ( `ssl`

)，并且客户端将主机名与服务器证书中的 CN 进行比较 ( `ssl-verify-server-cert`

)。

可以通过以下方式继续验证。

使用主机名连接到服务器，并显示服务器状态。如果 `SSL`

条目包含 `Cipher in use is…`

，则连接已加密。

```
mysql -u root -p -h server.example.com -e status
...
SSL: Cipher in use is TLS_AES_256_GCM_SHA384
```


需要注意的时，在此命令中使用的用户需有权进行远程身份验证。
如果您连接的主机名与服务器 TLS 证书中的主机名不匹配，该 `ssl-verify-server-cert`

参数将导致连接失败。例如，如果您连接到 `localhost`

：

```
mysql -u root -p -h localhost -e status
ERROR 2026 (HY000): SSL connection error: Validation of SSL server certificate failed
```


## 6 备份和恢复

这里介绍 MySQL 数据库的两种备份方法：

**逻辑备份**：备份恢复数据所需的 SQL 语句，不包括日志和配置文件。数据可以在其他硬件配置、MySQL版本或数据库管理系统 (DBMS) 上恢复，可移植性和灵活性更高；**物理备份**：备份存储文件及目录，包括日志和配置文件。备份和恢复速度更快，但必须在未运行或数据库中的所有表都被锁定时进行，以防止在备份期间更改。

### 6.1 mariadb-dump 逻辑备份

#### 6.1.1 mariadb-dump 工具备份

使用 `mysqldump`

工具备份 `user_manager`

数据库，执行以下命令：

```
mariadb-dump -u root -p --databases user_manager > user_manager_backup.sql
```


输入 root 密码，备份文件 `user_manager_backup.sql`

将包含用于恢复数据的 SQL 语句。

备份 user_manager2 等多个数据库：

```
mariadb-dump -u root -p --databases user_manager1 [user_manager2 ...] > user_managers_backup.sql
```


备份所有数据库：

```
mariadb-dump -u root -p --all-databases > user_all.sql > all_backup.sql
```


#### 6.1.2 mariadb-dump 工具恢复

在需要恢复数据的情况下，您可以使用以下命令将备份导入到数据库中：

```
mariadb < user_manager_backup.sql
```


输入 root 密码，之后备份文件 `user_manager_backup.sql`

中包含的 SQL 语句将被执行，恢复数据。

### 6.2 Mariabackup 物理备份

#### 6.2.1 Mariabackup 工具备份

Mariabackup是一个用于执行物理备份的实用程序。它可以备份InnoDB和XtraDB表，还可以备份MyISAM表。要使用Mariabackup备份数据库，请按照以下步骤操作：

安装Mariabackup：

```
sudo dnf install mariadb-backup
```


创建备份目录：

```
sudo mkdir /var/lib/mysql/backup
sudo chown mysql:mysql /var/lib/mysql/backup
```


确保用户拥有 `RELOAD`

、 `LOCK TABLES`

、 和 `REPLICATION CLIENT`

权限，然后执行备份：

```
sudo mariabackup --backup --target-dir=/var/lib/mysql/backup --user=root --password=your_password
```


#### 6.2.2 Mariabackup 工具恢复

首先需关闭 MariaDB 服务：

```
systemctl stop mariadb.service
```


然后执行恢复：

```
# 恢复数据并保留原始备份文件
mariabackup --copy-back --target-dir=/var/mariadb/backup/
# 恢复数据并删除原始备份文件
mariabackup --move-back --target-dir=/var/mariadb/backup/
```


修复文件权限并启动服务：

```
chown -R mysql:mysql /var/lib/mysql/
systemctl start mariadb.service
```