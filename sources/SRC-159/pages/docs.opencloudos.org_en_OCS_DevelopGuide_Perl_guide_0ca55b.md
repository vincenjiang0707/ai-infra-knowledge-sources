source: https://docs.opencloudos.org/en/OCS/DevelopGuide/Perl_guide/

# Perl开发指南

## 1. Perl 简介

### 1.1 Perl 简介

Perl 是一门通用编程语言，最初是为文本处理而开发的，现在被用于各种任务，包括系统管理、网络编程、Web 开发、GUI 开发等。 Perl 的主要特点是易用性强、支持过程式和面向对象编程，具有内置的强大文本处理功能，同时也拥有大量的第三方模块库。

### 1.2 安装 Perl

可以使用如下命令安装 Perl：

```
dnf install perl -y
```


```
perl --version
```


### 1.3 卸载 Perl

可以通过如下命令卸载 Perl：

```
dnf remove perl-interpreter -y
```


## 2. Perl 简单使用

### 2.1 直接通过命令行执行

可以使用命令行执行简单的 perl 代码，格式如下：

```
perl -e commandline
```


```
perl -e 'print "Hello, Perl!\n"'
```


### 2.2 执行 .pl 脚本

复杂的 perl 程序可以写到脚本文件中，格式如下：

```
perl program.pl
```


```
#!/usr/bin/env perl
```


示例如下： hello.pl 内容如下：

```
#!/usr/bin/env perl
print "Hello, Perl!\n";
```


```
perl hello.pl
```


```
chmod 755 hello.pl
./hello.pl
```


## 3. Perl 模块包管理

### 3.1 通过 rpm 包管理模块包

Perl 的一个重要特点是其具有庞大的第三方模块库，当前 OpenCloudOS Stream 集成了一些基础的模块包，打成 rpm 包，包名通常是 perl-modulename 的形式，可以通过 dnf 命令进行安装，如下：

```
dnf install perl-modulename -y
```


### 3.2 通过 cpan 管理模块包

OpenCloudOS Stream 仅集成了一些基础的 Perl 模块包，其他的模块包可以通过 CPAN 管理。 需要安装 CPAN 模块包，命令如下：

```
dnf install perl-CPAN -y
```


可以使用如下命令安装模块包：

```
cpan AAA::BBB::CCC
```


```
cpan App::cpanminus
```


## 4. Perl 程序调测

通过 perl 命令行执行 perl 代码或者 perl 脚本文件时，可以添加 -d 参数进入调试模式，形式如下：

```
perl -d <programfile>
```


```
#!/usr/bin/perl -d
```


```
[root@VM-76-60-centos home]# ./test.pl
Loading DB routines from perl5db.pl version 1.73
Editor support available.
Enter h or 'h h' for help, or 'man perldebug' for more help.
main::(./test.pl:3): $num = 5;
DB<1>
```


`l`

打印当前代码
`T`

打印调用栈

`s`

单步调试，会进入子函数

`n`

单步调试，跳过子函数

`b`

设置断点

`p`

查看变量值

`h`

显示帮助

更多调试命令请查看帮助文档。

## 5. 更多参考资料

- https://www.perl.org/learn.html
- https://www.perl.org/docs.html
- https://www.cpan.org/