source: https://docs.opencloudos.org/OCS/DevelopGuide/Java_guide/

# Java开发指南

## 1. Java 简介

### 1.1 Java 简介

Java 是一种面向对象的高级编程语言，Java 应用程序通常会被编译成可以在 Java 虚拟机（JVM）上运行的字节码，而与底层计算机体系架构无关，从而实现编译一次，随处运行。Java 目前广泛应用于客户端-服务器 Web 程序开发。

### 1.2 Java 组件支持情况

当前 OpenCloudOS Stream 集成了三个版本的自研 JDK（Java 运行时和 Java 虚拟机）：TencentKona-17，TencentKona-11 和 TencentKona-8。

### 1.3 安装 JDK

#### 1.3.1 安装 TencentKona-17

可以使用如下命令安装：

```
dnf install java-17-konajdk -y
```


```
java -version
```


```
openjdk 17.0.3-ga 2022-04-19
OpenJDK Runtime Environment TencentKonaJDK (build 17.0.3-ga+1)
OpenJDK 64-Bit Server VM TencentKonaJDK (build 17.0.3-ga+1, mixed mode, sharing)
```


#### 1.3.2 安装 TencentKona-11

可以使用如下命令安装：

```
dnf install java-11-konajdk -y
```


```
java -version
```


```
openjdk 11.0.18-ga 2023-01-17
OpenJDK Runtime Environment TencentKonaJDK (build 11.0.18-ga+1)
OpenJDK 64-Bit Server VM TencentKonaJDK (build 11.0.18-ga+1, mixed mode, sharing)
```


#### 1.3.3 安装 TencentKona-8

可以使用如下命令安装：

```
dnf install java-8-konajdk -y
```


```
java -version
```


```
openjdk version "1.8.0_322"
OpenJDK Runtime Environment (Tencent Kona 8.0.13) (build 1.8.0_322-1)
OpenJDK 64-Bit Server VM (Tencent Kona 8.0.13) (build 25.322-b1, mixed mode, sharing)
```


#### 1.3.4 多版本 JDK 的版本选择

JDK 默认安装在 \/usr/lib/jvm/java-\${major}-konajdk-${version}/ 目录下，/usr/bin/java 通过软连接指向安装目录下的 java。 当环境中存在多个版本 JDK 时，java 指向最先安装的 JDK 版本。可以通过如下命令设置默认的 JDK：

```
alternatives --config java
```


### 1.4 卸载 JDK

#### 1.4.1 卸载 TencentKona-17

可以使用如下命令卸载：

```
dnf remove java-17-konajdk-headless -y
```


#### 1.4.2 卸载 TencentKona-11

可以使用如下命令卸载：

```
dnf remove java-11-konajdk-headless -y
```


#### 1.4.3 卸载 TencentKona-8

可以使用如下命令卸载：

```
dnf remove java-8-konajdk-headless -y
```


## 2. Java 的简单使用

### 2.1 运行 Java 文件

示例代码文件 MyFirstClass.java 如下：

```
public class MyFirstClass {
public static void main(String... args) {
System.out.println("Hello, World!");
}
}
```


```
java MyFirstClass.java
```


### 2.2 运行 Java 类

需要通过 javac 将 java 源码编译生成 java 类，然后运行，步骤如下： 查看 java 版本。

```
java -version
```


```
dnf install java-17-konajdk-devel
```


```
javac MyFirstClass.java
```


```
java MyFirstClass
```


## 3. Java 模块包管理

### 3.1 通过 rpm 包管理模块包

OpenCloudOS Stream 集成了一些基础的 Java 第三方库，打成 rpm 包，通常包名与 jar 包包名相同，可以通过 dnf 命令安装，如：

```
dnf install apache-commons-cli -y
```


### 3.2 通过 maven 管理模块包

maven 是一个基于项目对象模型（POM）概念的软件项目管理工具。

#### 3.2.1 安装 maven

maven 包已经打成 rpm 包，前 OpenCloudOS Stream 支持多个版本的 JDK，如果需要使用特定版本，还需要指定 maven-openjdkX 的版本，如：

```
dnf install maven maven-openjdk17 -y
```


```
mvn -v
```


```
Apache Maven 3.8.6 (OpenCloudOS 3.8.6-3)
Maven home: /usr/share/maven
Java version: 17.0.3-ga, vendor: Tencent Company, runtime: /usr/lib/jvm/java-17-konajdk-17.0.3-7.ocs23
Default locale: zh_CN, platform encoding: UTF-8
OS name: "linux", version: "6.1.26-2303.1.0.ocs23.aarch64", arch: "aarch64", family: "unix"
```


#### 3.2.2 创建 maven 项目

创建一个 maven 项目，命令如下：

```
mvn archetype:generate -DgroupId=com.testmaven.myfirstapp -DartifactId=myfirstapp -DarchetypeArtifactId=maven-archetype-quickstart -DarchetypeVersion=1.4 -DinteractiveMode=false
```


项目目录结构如下：

```
myfirstapp/
├── pom.xml
└── src
├── main
│ └── java
│ └── com
│ └── testmaven
│ └── myfirstapp
│ └── App.java
└── test
└── java
└── com
└── testmaven
└── myfirstapp
└── AppTest.java
```


`pom.xml`

maven 项目配置文件，包含了项目的基本信息、依赖关系、构建方式等。
`src/main/java`

存放项目源码

`src/main/java`

存在项目测试源码

#### 3.2.3 pom 配置

pom.xml 的一个简单示例如下：

```
<?xml version="1.0" encoding="UTF-8"?>
<project xmlns="http://maven.apache.org/POM/4.0.0" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
xsi:schemaLocation="http://maven.apache.org/POM/4.0.0 http://maven.apache.org/xsd/maven-4.0.0.xsd">
<modelVersion>4.0.0</modelVersion>
<groupId>com.testmaven.myfirstapp</groupId>
<artifactId>myfirstapp</artifactId>
<version>1.0-SNAPSHOT</version>
<name>myfirstapp</name>
<!-- FIXME change it to the project's website -->
<url>http://www.example.com</url>
<properties>
<project.build.sourceEncoding>UTF-8</project.build.sourceEncoding>
<maven.compiler.source>1.7</maven.compiler.source>
<maven.compiler.target>1.7</maven.compiler.target>
</properties>
<dependencies>
<dependency>
<groupId>junit</groupId>
<artifactId>junit</artifactId>
<version>4.11</version>
<scope>test</scope>
</dependency>
</dependencies>
<build>
<pluginManagement><!-- lock down plugins versions to avoid using Maven defaults (may be moved to parent pom) -->
<plugins>
<!-- clean lifecycle, see https://maven.apache.org/ref/current/maven-core/lifecycles.html#clean_Lifecycle -->
<plugin>
<artifactId>maven-clean-plugin</artifactId>
<version>3.1.0</version>
</plugin>
...
</plugins>
</pluginManagement>
</build>
</project>
```


`project`

项目根标签。
`modelVersion`

模型版本标签。

`groupId`

项目组标识标签。

`artifactId`

项目标识标签。

`version`

项目版本标签。

`properties`

项目构建属性标签。

`dependencies`

项目依赖根标签。

`build`

项目构建根标签。

#### 3.2.4 构建 maven 项目

执行如下命令构建：

```
mvn package
```


```
[INFO] Scanning for projects...
[INFO]
[INFO] ----------------< com.testmaven.myfirstapp:myfirstapp >-----------------
[INFO] Building myfirstapp 1.0-SNAPSHOT
[INFO] --------------------------------[ jar ]---------------------------------
[INFO]
[INFO] --- maven-resources-plugin:3.0.2:resources (default-resources) @ myfirstapp ---
[INFO] Using 'UTF-8' encoding to copy filtered resources.
[INFO] skip non existing resourceDirectory /home/myfirstapp/src/main/resources
...
[INFO] -------------------------------------------------------
[INFO] T E S T S
[INFO] -------------------------------------------------------
[INFO] Running com.testmaven.myfirstapp.AppTest
[INFO] Tests run: 1, Failures: 0, Errors: 0, Skipped: 0, Time elapsed: 0.02 s - in com.testmaven.myfirstapp.AppTest
[INFO]
[INFO] Results:
[INFO]
[INFO] Tests run: 1, Failures: 0, Errors: 0, Skipped: 0
[INFO]
[INFO]
[INFO] --- maven-jar-plugin:3.0.2:jar (default-jar) @ myfirstapp ---
[INFO] ------------------------------------------------------------------------
[INFO] BUILD SUCCESS
[INFO] ------------------------------------------------------------------------
[INFO] Total time: 1.197 s
[INFO] Finished at: 2023-05-26T11:59:51+08:00
[INFO] ------------------------------------------------------------------------
```


## 4. Java 程序调测

可以通过 jdb 命令运行 java 程序，进入调试模式：

```
jdb MyFirstClass.java
```


```
[root@localhost new]# jdb MyFirstClass.java
Initializing jdb ...
> stop in MyFirstClass.main
Deferring breakpoint MyFirstClass.main.
It will be set after the class is loaded.
> run
run MyFirstClass.java
Set uncaught java.lang.Throwable
Set deferred uncaught java.lang.Throwable
>
VM Started: Set deferred breakpoint MyFirstClass.main
Breakpoint hit: "thread=main", MyFirstClass.main(), line=4 bci=0
4 System.out.println("Hello, World!");
main[1] where
[1] MyFirstClass.main (MyFirstClass.java:4)
[2] jdk.internal.reflect.NativeMethodAccessorImpl.invoke0 (native method)
[3] jdk.internal.reflect.NativeMethodAccessorImpl.invoke (NativeMethodAccessorImpl.java:77)
[4] jdk.internal.reflect.DelegatingMethodAccessorImpl.invoke (DelegatingMethodAccessorImpl.java:43)
[5] java.lang.reflect.Method.invoke (Method.java:568)
[6] com.sun.tools.javac.launcher.Main.execute (Main.java:419)
[7] com.sun.tools.javac.launcher.Main.run (Main.java:192)
[8] com.sun.tools.javac.launcher.Main.main (Main.java:132)
main[1]
```


`stop in`

命令设置了断点在 `main`

函数处，然后 `run`

运行程序，程序在断点处暂停，又通过了 `where`

打印了当前调用栈。
更多命令可以通过 jdb 交互界面输入 `help`

命令查看。

## 5. 更多参考资料

- https://dev.java/learn/getting-started/
- https://maven.apache.org/index.html