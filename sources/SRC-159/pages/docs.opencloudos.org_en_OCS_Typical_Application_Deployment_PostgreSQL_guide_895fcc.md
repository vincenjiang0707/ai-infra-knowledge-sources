source: https://docs.opencloudos.org/en/OCS/Typical_Application_Deployment/PostgreSQL_guide/

# PostgreSQL 服务器搭建指南

PostgreSQL 是一个开源的、企业级的对象关系数据库系统(ORDBMS)，能够在集群中管理大量数据，强调可靠性、可扩展性和功能稳定等特性。

## 1 安装 PostgreSQL

可以通过如下命令安装 PostgreSQL 和相关工具：

```
sudo dnf install postgresql-server
```


查看安装的 PostgreSQL 系列包：

```
rpm -qa | grep postgresql
```


## 2 初始化 PostgreSQL

### 2.1 初始化数据库

在初始化数据库之前，需先通过 `systemctl status postgresql.service`

查看服务状态是否为 `enabled`

。
若非 `enabled`

，请使用以下命令启用 PostgreSQL 服务：

```
sudo systemctl enable postgresql.service
```


然后初始化 PostgreSQL 数据库：

```
sudo postgresql-setup --initdb
```


### 2.2 启动 PostgreSQL 服务

使用以下命令启动 PostgreSQL 服务：

```
sudo systemctl start postgresql.service
```


### 2.3 查看 PostgreSQL 状态

运行以下命令以检查 PostgreSQL 服务是否正在运行：

```
sudo systemctl status postgresql.service
```


如果安装启动成功，您将看到类似于以下内容的输出：

```
● postgresql.service - PostgreSQL database server
Loaded: loaded (/usr/lib/systemd/system/postgresql.service; enabled; v>
Active: active (running) since Fri 2023-05-26 11:18:25 CST; 3s ago
Process: 575849 ExecStartPre=/usr/libexec/postgresql-check-db-dir postg>
Main PID: 575851 (postmaster)
Tasks: 8 (limit: 9169)
Memory: 16.4M
CPU: 50ms
CGroup: /system.slice/postgresql.service
├─575851 /usr/bin/postmaster -D /var/lib/pgsql/data
├─575852 "postgres: logger "
├─575854 "postgres: checkpointer "
├─575855 "postgres: background writer "
├─575856 "postgres: walwriter "
├─575857 "postgres: autovacuum launcher "
├─575858 "postgres: stats collector "
└─575859 "postgres: logical replication launcher "
```


## 3 配置 PostgreSQL

PostgreSQL 的数据和配置文件，默认位于 `/var/lib/pgsql/data/`

路径。

配置文件主要有：

: 用于设置数据库集群参数；`postgresql.conf`

: 用于为 PostgreSQL 数据库配置客户端身份验证。您可以在这里设置各种身份验证方法、使用的 IP 地址范围等；`pg_hba.conf`

: 保存基本的`postgresql.auto.conf`

**PostgreSQL**设置，类似于`postgresql.conf`

. 但是，此文件受服务器控制，由`ALTER SYSTEM`

编辑，**不能手动编辑**；: 用于为 PostgreSQL 定义用户名称映射。这允许将操作系统中的用户（或一组用户）映射到 PostgreSQL 中的用户；`pg_ident.conf`


### 3.1 数据库集群参数配置

在 `postgresql.conf`

文件中，常见参数介绍如下：

**监听地址 (listen_addresses)**- 默认情况下，PostgreSQL 只在本地进行监听。为了让其监听所有可用的 IP 地址，修改如下：

```
listen_addresses = '*'
```


**端口 (port)**- 若要更改服务器监听的端口（默认是 5432），设置如下：

```
port = 5432
```


**连接数 (max_connections)**- 您可以修改此参数以允许的最大连接数。根据可用资源和应用程序需求进行设置：

```
max_connections = 100
```


**共享缓冲区 (shared_buffers)**- 此参数设置 PostgreSQL 使用的共享内存量。这将影响缓存大小，推荐设置为物理内存的 25%：

```
shared_buffers = 2GB
```


### 3.2 客户端身份验证配置

`pg_hba.conf`

文件控制客户端身份认证。这些设置是按行组织，以规则的形式呈现。通常，规则分为四个字段：

**连接类型 (connection type)**- 表明规则适用于何种类型的连接：本地（local）或主机（host）。**数据库 (database)**- 规定哪些数据库应用此规则。可以为"all"、"sameuser" 或逗号分隔的数据库名称列表。**用户 (user)**- 规定哪些用户应用此规则。可以为"all" 或逗号分隔的用户名列表。**身份验证方法 (authentication method)**- 说明身份验证的细节。例如，可以使用 "trust"（免密）、 "md5"（密码）或 "peer"（基于操作系统账户）等方法。

如果要允许特定 IP 地址范围中的所有客户端连接到服务器并使用 md5 加密，则可以使用以下设置：

```
host all all 192.168.0.0/24 md5
```


### 3.3 用户映射配置（可选）

`pg_ident.conf`

配置文件用于为 PostgreSQL 定义用户名称映射。这允许将操作系统中的用户（或一组用户）映射到 PostgreSQL 中的用户。这对于受到限制的环境和增强安全性的场景很有用。

该文件由多个映射组成，每个映射都有一个映射名称。每个映射包含一个或多个映射规则。

映射规则由以下字段组成：

**映射名称 (map name)**- 唯一名称，用于识别身份验证规则。**系统用户名 (system username)**- 操作系统中的用户**PostgreSQL 用户名 (PostgreSQL username)**- PostgreSQL 中映射到操作系统用户的用户

例如，要将操作系统中名为 "osuser" 的用户映射到 PostgreSQL 中名为 "pguser" 的用户，请在 `pg_ident.conf`

文件中添加以下映射：

```
mapname system_username pg_username
example_map osuser pguser
```


然后，为了应用这个映射，您需要在 `pg_hba.conf`

中进行相应调整。将身份验证方法更改为 "ident" 并设置 "map" 选项：

```
local dbname pguser ident map=example_map
```


### 3.4 配置生效

确保修改后保存文件，然后重新启动 PostgreSQL 服务以使更改生效：

```
sudo systemctl restart postgresql.service
```


## 4 使用 PostgreSQL

### 4.1 创建用户和数据库

切换到 `postgres`

用户：

```
sudo su - postgres
```


输入 `psql`

打开 PostgreSQL 交互终端：

```
psql (14.3)
Type "help" for help.
```


然后可键入 `\conninfo`

查看详细信息：

```
postgres=# \conninfo
You are connected to database "postgres" as user "postgres" via socket in "/var/run/postgresql" at port "5432".
```


通过运行以下命令创建一个新用户 `test_user`

， 其密码为 `mypasswd`

，赋予其 `CREATEROLE CREATEDB`

权限：

```
postgres=# CREATE USER test_user WITH PASSWORD 'mypasswd' CREATEROLE CREATEDB;
```


然后创建一个名为 `test_db`

的数据库：

```
CREATE DATABASE test_db;
```


退出交互终端：

```
\q
```


退出 `postgres`

用户：

```
exit
```


### 4.2 配置远程连接和密码验证

打开 `/var/lib/pgsql/data/pg_hba.conf`

文件，在文件末尾添加以下行以允许通过密码验证来接受外部连接：

```
host all all 0.0.0.0/0 scram-sha-256
```


然后编辑 `/var/lib/pgsql/data/postgresql.conf`

文件，以便从任何地址都可以连接数据库：

```
#listen_addresses = 'localhost'
#password_encryption = scram-sha-256 # scram-sha-256 or md5
```


取消注释并将其更改为：

```
listen_addresses = '*'
password_encryption = scram-sha-256 # scram-sha-256 or md5
```


**重新启动 PostgreSQL 服务，使配置生效**：

```
sudo systemctl restart postgresql.service
```


### 4.3 登录数据库

通过以下命令，使用 `test_user`

登录到 `test_db`

数据库：

```
psql -U test_user -h 127.0.0.1 -d test_db
```


输入用户密码并按 Enter。如果一切正常，您应该看到如下输出：

```
Password for user test_user:
psql (14.3)
Type "help" for help.
```


键入 `\conninfo`

可看到以下输出：

```
test_db-> \conninfo
You are connected to database "test_db" as user "test_user" on host "127.0.0.1" at port "5432".
```


## 5 加密 PostgreSQL

通常 PostgreSQL 服务器的连接并未经过加密，存在一定安全风险。为了使数据库传输更安全可靠，您可以为 PostgreSQL 服务器配启用TLS 加密。

### 5.1 生成证书和私钥

首先，需要生成一份服务器证书和私钥，可以使用自签名证书或购买商业证书。 这里为示范，故生成并采用自签名证书：

-
首先，确保已安装了 OpenSSL。如果尚未安装，请使用以下命令进行安装：

`sudo dnf install openssl`

-
接下来，进入默认 Postgres 数据目录：

`cd /var/lib/pgsql/data`

-
生成服务器私钥：

`sudo openssl genrsa -out server.key 2048`

-
生成自签名证书：

`sudo openssl req -new -x509 -key server.key -out server.crt -days 3650 -subj "/CN=<your_domain>"`

**注意**：将`<your_domain>`

替换为您的服务器域名。如果没有域名，可以使用服务器的 IP 地址。 -
为证书和私钥设置正确的所有者和权限，使其私钥只能由所有者读取：

`sudo chown postgres:postgres /var/lib/pgsql/data/server.{key,crt} sudo chmod 0400 /var/lib/pgsql/data/server.key`


### 5.2 配置 PostgreSQL 服务器使用 TLS 加密

现在我们已经有了证书和私钥，下一步是为 PostgreSQL 服务器启用 TLS / SSL。

编辑 `/var/lib/pgsql/data/postgresql.conf`

文件，配置以下参数：

```
ssl = on
ssl_cert_file = 'server.crt'
ssl_key_file = 'server.key'
```


这将启用 SSL，并确保 PostgreSQL 使用先前创建的证书和私钥文件。

### 5.3 配置客户端连接的 TLS 加密验证

然后为客户端连接配置 TLS 加密验证，编辑 `/var/lib/pgsql/data/pg_hba.conf`

文件，为所需的用户和数据库将所有 `host`

条目更改为 `hostssl`

。例如：

```
hostssl all all 0.0.0.0/0 scram-sha-256
```


也可以针对指定数据库和用户配置 TLS 加密：

```
hostssl test_db test_user 127.0.0.1/32 scram-sha-256
```


最后，重新启动 PostgreSQL 服务，以使更改生效：

```
sudo systemctl restart postgresql
```


现在，PostgreSQL 服务器上的连接应已启用 TLS 加密。

### 5.4 验证 TLS 加密

执行以下指令并键入密码，以 ·`test_user`

身份登录 `test_db`

：

```
psql -U test_user -h 127.0.0.1 -d test_db
```


可看到如下 TLS 相关打印信息：

```
Password for user test_user:
psql (14.3)
SSL connection (protocol: TLSv1.3, cipher: TLS_AES_256_GCM_SHA384, bits: 256, compression: off)
Type "help" for help.
```


登录后，也可输入 `\conninfo`

，查看到 `protocol: TLSv1.3`

即表明开启成功：

```
test_db=> \conninfo
You are connected to database "test_db" as user "test_user" on host "127.0.0.1" at port "5432".
SSL connection (protocol: TLSv1.3, cipher: TLS_AES_256_GCM_SHA384, bits: 256, compression: off)
```


## 6 备份 PostgreSQL

定期备份数据库是非常重要的，这将使您能够在发生数据丢失或损坏时恢复数据。 在本章中，将介绍两种 PostgreSQL 备份方法：SQL 文件备份和物理文件备份。

### 6.1 SQL 文件备份 (使用 pg_dump)

`pg_dump`

是一种备份 PostgreSQL 数据库的实用工具，它将数据库架构和数据生成为 SQL 脚本文件。在需要恢复数据库时，可以运行这个 SQL 脚本文件。SQL 转储可以不受机器架构、服务器版本限制，运行期间不会阻止数据库的正常运转。

以下是使用 `pg_dump`

备份数据库的方法：

以有访问权限的用户身份进行登录：

```
su - postgres
```


使用 `pg_dump`

备份数据库。将 `<your_database>`

替换为要备份的数据库名称，将 `backup.sql`

替换为要创建的备份文件名：

```
pg_dump <your_database> > backup.sql
```


现在在当前目录下会有一个名为 `backup.sql`

的 SQL 文件，其中包含了数据库的完整备份。

与 `pg_dump`

类似， `pg_dumpall`

也可备份数据。只不过前者用于单个数据库备份，后者可用于数据库集群备份：

```
pg_dumpall > backupall.sql
```


### 6.2 物理文件备份

物理文件备份是直接备份 PostgreSQL 数据库数据目录的整个文件结构，包括所有的表、索引和事务日志。这种方法在恢复时可能更快，但在迁移过程中可能较为复杂。以下是执行物理文件备份的方法：

-
停止 PostgreSQL 服务以确保所有事务已写入磁盘：

`sudo systemctl stop postgresql`

-
备份数据目录。将

`/path/to/backup_folder`

替换为备份最终存储的目录：`sudo cp -R /var/lib/pgsql/data /path/to/backup_folder`

-
重新启动 PostgreSQL 服务：

`sudo systemctl start postgresql`


现在您已经获得了一个名为 `data`

的目录，其中包含物理文件备份。

## 6.3 恢复备份

要恢复 SQL 文件备份，只需运行该 SQL 脚本。首先以超级用户或数据库管理员身份，创建一个新的空数据库。将 `<your_new_database>`

替换为新数据库的名称：

```
createdb <your_new_database>
```


然后，运行以下命令以恢复数据库。将 `<your_new_database>`

替换为已创建的新数据库名称，将 `backup.sql`

替换为备份文件名：

```
psql <your_new_database> < backup.sql
```


若要恢复物理文件备份，请确保首先停止 PostgreSQL 服务，删除或移动数据目录，然后将备份文件复制回数据目录。接着重新启动 PostgreSQL 服务。

备份和恢复是数据库管理员的重要职责。确保您根据业务需求和策略定期创建备份。在执行任何有风险的操作（如升级、迁移等）之前，请务必备份您的数据。

## 7 参考

PostgreSQL 官方文档：https://www.postgresql.org/docs/14/server-start.html