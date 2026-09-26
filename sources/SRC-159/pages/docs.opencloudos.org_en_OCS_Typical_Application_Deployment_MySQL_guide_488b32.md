source: https://docs.opencloudos.org/en/OCS/Typical_Application_Deployment/MySQL_guide/

# MySQL 服务器搭建指南

MySQL 是一个开源的数据库管理系统 ，在 WEB 应用等方面是业界最流行的RDBMS (Relational Database Management System，关系数据库管理系统)之一。

本文将从安装、配置、备份及恢复等方面，介绍 MySQL 服务器的搭建和使用。

## 1 安装 MySQL

MySQL 不在系统预装范围内，需要通过如下命令安装 MySQL Server：

```
sudo yum -y install mysql-server
```


安装完毕后，可以执行如下指令验证安装结果：

```
mysql --version
```


如果显示 MySQL 版本号等信息，则说明安装成功。

```
mysql Ver 8.0.32 for Linux on x86_64 (Source distribution)
```


## 2 初始化 MySQL

### 2.1 MySQL 服务启动

安装完毕后，可手动启用 `mysqld`

服务：

```
sudo systemctl start mysqld.service
```


但手动启用后，系统重启后会关闭该服务。如果想要 `mysqld`

服务开机时自行启动，需要执行：

```
sudo systemctl enable mysqld.service
```


### 2.2 MySQL 服务初始化

首次启动服务后，需要进行初始化设置。 为了提升安装时的安全性，建议您通过以下方式初始化 MySQL 数据库：

```
sudo mysql_secure_installation
```


执行该命令后，会以交互方式提示配置过程的每个步骤：

- 选择密码强度，为 root 用户设置密码；
- 禁止匿名账户访问；
- 禁用 root 远程登录；
- 清理测试用的 test 数据库；

建议按照提示设置一个强壮的 root 密码。此外，请删除匿名帐户，禁用远程 root 登录并删除测试数据库。

### 2.3 MySQL 服务关闭

服务启动后，您也可以按需关闭 `mysqld`

服务：

```
sudo systemctl stop mysqld.service
```


## 3 配置 MySQL

MySQL 支持配置网络选项，可以通过编辑 `/etc/my.cnf.d/mysql-server.cnf`

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
mysqld --verbose --help
```


[ 该命令生成所有mysqld](https://dev.mysql.com/doc/refman/8.0/en/mysqld.html)选项和可配置系统变量 的列表。它的输出包括默认选项和变量值，示例如下：

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


## 4 使用 MySQL

### 4.1 连接到 MySQL 服务器

打开终端，输入以下命令以 root 身份连接到 MySQL 服务器：

```
mysql -u root -p
```


根据提示，输入您在执行 `mysql_secure_installation`

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

注：在设置密码时若收到提示 “ERROR 1819 (HY000): Your password does not satisfy the current policy requirements”，则可能 是密码强度与当前密码不匹配； 可执行

`SHOW VARIABLES LIKE 'validate_password%';`

查看`validate_password.policy`

密码强度， 令您的密码与强度匹配即可。 如果您确认您当前的密码满足安全需要，对密码强度不需要太高，则可以通过以下方式降低密码强度；`SET GLOBAL validate_password.policy=LOW;`

-
授予新用户访问

`user_manager`

数据库的所有权限：`GRANT ALL PRIVILEGES ON user_manager.* TO 'myuser'@'localhost';`

-
使权限生效：

`FLUSH PRIVILEGES;`


现在，可以使用新用户 `myuser`

连接到 MySQL 服务器。

## 5 备份和恢复

这里介绍 MySQL 数据库的两种备份方法：

**逻辑备份**：备份恢复数据所需的 SQL 语句，不包括日志和配置文件。数据可以在其他硬件配置、MySQL版本或数据库管理系统 (DBMS) 上恢复，可移植性和灵活性更高；**物理备份**：备份存储文件及目录，包括日志和配置文件。备份和恢复速度更快，但必须在未运行或数据库中的所有表都被锁定时进行，以防止在备份期间更改。

### 5.1 mysqldump 逻辑备份

#### 5.1.1 mysqldump 工具备份

使用 `mysqldump`

工具备份 `user_manager`

数据库，执行以下命令：

```
mysqldump -u root -p --databases user_manager > user_manager_backup.sql
```


输入 root 密码，备份文件 `user_manager_backup.sql`

将包含用于恢复数据的 SQL 语句。

备份 user_manager2 等多个数据库：

```
mysqldump -u root -p --databases user_manager1 [user_manager2 ...] > user_managers_backup.sql
```


备份所有数据库：

```
mysqldump -u root -p --all-databases > user_all.sql > all_backup.sql
```


#### 5.1.2 mysqldump 工具恢复

在需要恢复数据的情况下，您可以使用以下命令将备份导入到数据库中：

```
mysql -u root -p user_manager < user_manager_backup.sql
```


输入 root 密码，之后备份文件 `user_manager_backup.sql`

中包含的 SQL 语句将被执行，恢复数据。

### 5.2 文件系统备份

创建 MySQL 数据库的文件系统备份时，可将 MySQL 的数据、配置、日志等内容都拷贝到备份位置。

首先，关闭 `mysqld`

服务：

`systemctl stop mysqld.service`


拷贝数据、配置、日志文件等：

```
cp -r /var/lib/mysql /back_path
cp -r /etc/my.cnf /etc/my.cnf.d /back_path/configuration
cp /var/log/mysql/* /back_path/logs
```


备份完毕后，执行 `systemctl start mysqld.service`

启动 `mysqld`

服务。

当备份恢复时，将备份数据从备份位置加载到 `/var/lib/mysql`

目录时，需确保 `mysql:mysql`

是 `/var/lib/mysql`

所有文件的所有者 ：

`chown -R mysql:mysql /var/lib/mysql`


## 6 MySQL 复制

MySQL复制提供了各种配置选项，下面我们展示一种基于事务的方法，使用全局事务标识符 (GTID) 在新安装的 MySQL 服务器上进行复制。

我们先假设两台服务器均已成功安装了 MySQL。

### 6.1 配置主服务器

-
打开 MySQL 主服务器的配置文件

`/etc/my.cnf.d/mysql-server.cnf`

。 -
在

`[mysqld]`

部分中添加配置参考如下：`[mysqld] server-id=1 bind-address=0.0.0.0 log_bin=/var/log/mysql/mysql-bin.log expire_logs_days=7 binlog_format=ROW gtid_mode=ON enforce-gtid-consistency=ON`

`server-id`

：服务器ID，必须是唯一的；`bind-address`

：从副本到源的连接需要此选项；`log_bin`

：启用二进制日志，定义源服务器 的二进制日志文件的路径；`expire_logs_days`

： 表示二进制日志文件被保留的时间（以天为单位）；`binlog_format`

： 设置复制的格式，可以是`ROW`

、`STATEMENT`

或`MIXED`

，建议使用`ROW`

；`gtid_mode`

：在服务器上启用全局事务标识符 (GTID)；`enforce-gtid-consistency`

：服务器通过只允许执行可以使用 GTID 安全记录的语句来强制执行 GTID 一致性；

-
重启服务：

`systemctl restart mysqld.service`


### 6.2 创建复制用户并授权

在主服务器上，创建一个用于复制的专用用户，并授予权限，允许该用户从从服务器进行读取操作。使用以下命令连接到 MySQL 服务器并执行 SQL 命令：

```
mysql> CREATE USER 'repl_user'@'%' IDENTIFIED BY 'your_password';
mysql> GRANT REPLICATION SLAVE ON *.* TO 'repl_user'@'%';
```


请确保使用安全的密码替换 `your_password`

。

重新加载MySQL数据库 中的授权表，并将主服务器设置为只读状态：

```
mysql> FLUSH PRIVILEGES;
mysql> SET @@GLOBAL.read_only = ON;
```


### 6.3 配置从服务器

-
在从服务器上打开 MySQL 配置文件

`/etc/my.cnf.d/mysql-server.cnf`

。 -
在

`[mysqld]`

部分中添加以下配置：`[mysqld] server-id=2 relay-log=/var/log/mysql/mysqld-relay-bin.log log_bin=/var/log/mysql/mysql-bin.log gtid_mode=ON enforce-gtid-consistency=ON log-replica-updates=ON skip-replica-start=ON`

在这个例子中，我们将从服务器的

`server-id`

设置为`2`

，以确保它是唯一的。 -`relay-log`

：用于设置从服务器的中继日志文件名，中继日志是MySQL副本服务器在复制过程中创建的一组日志文件； -`log-replica-updates`

：确保从源服务器接收的更新记录在副本的二进制日志中； -`skip-replica-start`

：确保副本服务器在副本服务器启动时不会启动复制线程； -
重启 MySQL 服务器：

`sudo systemctl restart mysqld.service`


### 6.4 启动从服务器复制

要启动从服务器的复制，请使用以下 SQL 命令：

将从服务器设置为只读状态：

```
mysql> SET @@GLOBAL.read_only = ON;
```


配置复制源：

```
mysql> CHANGE MASTER TO
MASTER_HOST='<MASTER_HOST>',
MASTER_USER='repl_user',
MASTER_PASSWORD='your_password',
MASTER_LOG_FILE='mysql-bin.000001',
MASTER_LOG_POS=0;
```


`<MASTER_HOST>`

是主服务器的主机名或 IP 地址，`your_password`

是前面创建的 `repl_user`

的密码。`MASTER_LOG_FILE`

和 `MASTER_LOG_POS`

指定从服务器开始复制的二进制日志文件和位置。

最后，启动从服务器的复制进程：

```
mysql> START SLAVE; # 或执行START REPLICA;
```


在主从服务器上取消设置只读状态：

```
mysql> SET @@GLOBAL.read_only = OFF;
```


### 6.5 验证复制状态

要验证复制是否正常工作，可以在主服务器和从服务器上都执行一些 SQL 操作，并观察数据变化是否同步。

此外，您还可以在从服务器上执行以下命令查看从服务器的状态：

```
mysql> SHOW SLAVE STATUS;
```


注意主要输出的 `Slave_IO_State`

和 `Seconds_Behind_Master`

。如果显示为 `Waiting for master to send event`

，复制正在正常运行；如果 `Seconds_Behind_Master`

的值较小或为零，说明从服务器与主服务器之间的同步延迟较低。