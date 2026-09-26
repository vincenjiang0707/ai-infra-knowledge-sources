source: https://docs.opencloudos.org/en/OCS/DevelopGuide/Dotnet_guide/

[toc]

# 1. dotnet简介

## 1.1 dotnet(.NET)简介

.NET 是一个通用开发平台，它带有自动内存管理和现代编程语言。使用 .NET，您可以有效地构建高质量的应用程序。

.NET 提供以下功能：

- 能够遵循基于微服务的方法，其中某些组件使用 .NET 构建，其他组件使用 Java 构建。
- 可以在 OpenCloudOS 或 Windows 服务器上部署和运行应用程序。
- 一个异构的数据中心，底层基础结构可以在不需要依赖 Windows 服务器的情况下运行 .NET 应用程序。

OpenCloudOS提供了dotnet6.0和dotnet7.0，本文以dotnet7.0为例，介绍使用

## 1.2 dotnet安装

运行以下命令来安装 dotnet-sdk-7.0 软件包：

```
sudo dnf install dotnet-sdk-7.0 -y
```


安装完毕后可通过如下指令检查是否正确安装了dotnet7.0，此时能看到系统安装dotnet7.0后的版本号、提交commit、运行环境等：

```
dotnet --info
```


# 2. 使用dotnet7.0创建应用程序

## 2.1 创建项目

在名为 `my-app`

的目录中创建一个新的 Console 应用程序（目录不存在会自动创建目录）：

```
dotnet new console --output my-app
```


输出返回：

```
欢迎使用 .NET 7.0!
---------------------
SDK 版本: 7.0.100
----------------
已安装 ASP.NET Core HTTPS 开发证书。
若要信任该证书，请运行 "dotnet dev-certs https --trust" (仅限 Windows 和 macOS)。
了解 HTTPS: https://aka.ms/dotnet-https
----------------
编写你的第一个应用: https://aka.ms/dotnet-hello-world
查找新增功能: https://aka.ms/dotnet-whats-new
浏览文档: https://aka.ms/dotnet-docs
在 GitHub 上报告问题和查找源: https://github.com/dotnet/core
使用 "dotnet --help" 查看可用命令或访问: https://aka.ms/dotnet-cli
--------------------------------------------------------------------------------------
已成功创建模板“控制台应用”。
正在处理创建后操作...
正在还原 /root/my-app/my-app.csproj:
Determining projects to restore...
Restored /root/my-app/my-app.csproj (in 89 ms).
已成功还原。
```


## 2.2 运行项目

```
dotnet run --project my-app
```


```
Hello, World!
```


# 3. 使用 dotnet7.0 发布应用程序

.NET 7.0 应用程序可以发布到使用共享的系统范围的 .NET 版本，或包含 .NET。 发布 .NET 7.0 应用程序的方法有： - 单文件应用程序 - 应用程序自我包含，可以部署为单个可执行文件，且所有依赖文件都包含在单个二进制文件中。 - 与框架相关的部署(FDD)- 应用程序使用共享的系统范围的 .NET 版本。 - 自我包含的部署(SCD)- 应用程序包括 .NET。此方法使用 Microsoft 构建的运行时。

## 3.1 发布 .NET 应用程序

```
dotnet publish my-app -f net7.0 -c Release
```


```
MSBuild version 17.4.0+18d5aef85 for .NET
Determining projects to restore...
All projects are up-to-date for restore.
my-app -> /root/my-app/bin/Release/net7.0/my-app.dll
my-app -> /root/my-app/bin/Release/net7.0/publish/
```


```
dotnet publish my-app -f net7.0 -c Release -r opencloudos.23-x64 --self-contained false
```


# 4. 附录

更多使用方法，请参照：

- Microsoft官方文档：https://learn.microsoft.com/zh-cn/dotnet/