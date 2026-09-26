source: https://docs.opencloudos.org/en/OCS/Typical_Application_Deployment/SQLite_guide/

# SQLite 使用指南

SQLite 是一个 C 语言编写的轻量级数据库引擎，适用于嵌入式应用程序、客户端应用程序以及对性能、可移植性和轻量级要求较高的场景。

## 1 安装 SQLite

使用以下命令以来安装 `sqlite`

软件包：

```
sudo dnf install sqlite -y
```


安装完成后，通过终端输入以下命令来查看 SQLite 的版本：

```
sqlite3 --version
```


## 2 使用 SQLite

### 2.1 创建数据库

要创建新的 SQLite 数据库，只需运行以下命令，将 `my_database.db`

替换为您希望使用的数据库名：

```
sqlite3 my_database.db
```


此命令将在当前目录下创建一个名为 `my_database.db`

的 SQLite 数据库文件。如果文件不存在，SQLite 会自动创建它。

### 2.2 在数据库中创建表

首先，通过运行以下命令进入 SQLite 交互式终端：

```
sqlite3 my_database.db
```


然后执行以下 SQL 语句来创建一个名为 `users`

的表：

```
CREATE TABLE users (
id INTEGER PRIMARY KEY,
name TEXT NOT NULL,
age INTEGER
);
```


完成后，请输入 `.tables`

命令，查看数据库中的所有表：

```
.tables
```


上述指令为 SQLite 的点命令（dot command），是特定于 SQLite 的内置命令，以点（.）开头，用于执行特定功能。

SQLite 中常见命令汇总如下：

`.databases`

：显示当前连接到的所有数据库和附加的数据库。`.tables`

：显示当前数据库的所有表格。你也可以添加一个可选字符串用于模糊匹配表名：`.tables %pattern%`

。`.schema [table_name]`

：显示指定表格的创建语句和结构。如果未提供`table_name`

，则显示当前数据库的所有表模式。`.indices [table_name]`

：显示指定表的所有索引。如果未提供`table_name`

，则显示所有表的所有索引。`.header on|off`

：控制查询结果的表头（字段名）显示。设置为`on`

时，显示表头；设置为`off`

时，隐藏表头。`.mode MODE`

：设置输出结果的显示模式。`MODE`

值可以为 ascii, csv, column, html, insert , line, list, quote, tabs, 或 tcl 。`.backup ?DB? FILE`

：将当前数据库或指定的数据库（`DB`

）备份到指定的`FILE`

。`.restore ?DB? FILE`

：从一个文件中恢复数据到当前数据库或给定名称的数据库（`DB`

）。`.read FILE`

：从给定的文件中读取和执行 SQLite 命令或 SQL 语句。例如，`.read my_script.sql`

。`.timer on|off`

：打开/关闭 SQL 语句执行计时器。设置为`on`

时，显示执行时间；设置为`off`

时，隐藏执行时间。`.import FILE TABLE`

：将给定文件中的数据导入到指定的表中。例如，`.import data.csv employees`

。`.output ?FILE?`

：可以指定一个文件名 FILE 作为输出目标。接下来运行的 SELECT 查询将把结果写入到指定的文件中，而不是在屏幕上显示。`.exit`

：退出 SQLite 命令行工具。

### 2.3 向表中插入数据

要添加新数据到 `users`

表中，请在 SQLite 交互式终端中执行以下命令：

```
INSERT INTO users (name, age) VALUES ('John Doe', 30);
INSERT INTO users (name, age) VALUES ('Mike Doe', 28);
```


### 2.4 查询数据

要从 `users`

表中查询数据，请执行以下 SQL 语句：

```
SELECT * FROM users;
```


您可以根据需求修改查询条件：

```
SELECT * FROM users WHERE age > 25;
```


如果您想要导出查询结果，请使用以下命令：

```
.mode csv
.output data.csv
SELECT * FROM users;
```


这将以 CSV 格式将结果导出到文件 `data.csv`

中。

### 2.5 更新和删除数据

要更新特定数据，请使用以下 SQL 语句：

```
UPDATE users SET age = 31 WHERE name = 'John Doe';
```


要从表中删除特定数据，请执行以下 SQL 语句：

```
DELETE FROM users WHERE name = 'Mike Doe';
```


### 2.6 退出 SQLite

要从 SQLite 交互式终端退出，请输入以下命令：

```
.exit
```


## 3 备份 SQLite

### 3.1 备份数据库

备份数据库：

```
sqlite3 my_database.db ".backup my_database_backup.db"
```


### 3.2 恢复数据库

恢复数据库：

```
sqlite3 my_database_backup.db ".restore my_database.db"
```


## 4 常见问题

### 4.1 无法删除 SQLite 数据库文件？

删除数据库文件时，可能仍有连接到该文件的应用程序。请确保已关闭所有使用此数据库的应用程序，然后重试删除操作。

### 4.2 如何重置 SQLite 自增序列？

使用以下命令重置表的自增序列：

```
DELETE FROM sqlite_sequence WHERE name = 'your_table_name';
```


### 4.3 可否将 SQLite 数据库更改为其他类型的数据库？

可以。通过将 SQLite 数据库数据导出为 SQL 脚本，然后在新的数据库中运行相应的数据导入操作来实现，例如 MySQL 或 PostgreSQL。不过，需要注意 SQL 语法和数据类型之间的差异。

## 5 附录

SQLite 快速上手：https://sqlite.org/quickstart.html SQLite 命令行使用：https://sqlite.org/cli.html SQLite C/C++ 接口：https://sqlite.org/cintro.html