source: https://docs.opencloudos.org/en/OCS/DevelopGuide/QT_guide/

# 1 Qt 简介

Qt 是一个跨平台的 C++ 应用框架，可以用于开发图形用户界面 (GUI) 程序和命令行工具。具有功能丰富的 API 和强大的开发工具。

# 2 Qt 开发环境安装

Qt 作为开发图形界面的软件，用户需要预先使能环境的图形化界面，部分命令只能在图形化界面执行。关于使能图形化界面，本文不展开介绍，用户可以参考《安装启动指南》中的”桌面安装“章节。

## 2.1 `dnf`

安装

用户可以直接使用如下命令安装：

```
dnf install -y qt5-qtbase qt5-qtbase-devel
```


## 2.2 自定义安装

如果用户期望自定义安装，可以参考如下步骤，从 Qt 官网获取 online 安装器进行安装：

1 预装安装器的依赖包

```
dnf install -y xcb-util-wm xcb-util-image xcb-util-keysyms xcb-util-renderutil
```


```
wget https://download.qt.io/archive/online_installers/4.5/qt-unified-linux-x64-4.5.2-online.run
chmod +x qt-unified-linux-x64-4.5.2-online.run
```


```
./qt-unified-linux-x64-4.5.2-online.run
```


执行后会出现 Qt 的安装界面，用户按照指引一步步安装即可

# 3 Qt 简单使用

在 Qt 项目中，工程结构是文件和目录组织的方式，以便于开发、构建和部署 Qt 应用程序。以下是一个典型的 Qt 工程结构：

```
my_project/
├── my_project.pro // Qt 项目文件，描述项目的构建信息
├── src/ // 存放源代码文件的目录
│ ├── main.cpp // 应用程序入口点
│ ├── mainwindow.cpp // 主窗口类实现文件
│ ├── mainwindow.h // 主窗口类头文件
│ ├── widgets.cpp // 其他组件类的实现文件
│ └── widgets.h // 其他组件类的头文件
├── resources/ // 资源文件目录，如图标、图片等
│ ├── images/ // 图像文件目录
│ ├── icons/ // 图标文件目录
│ └── qml/ // 存放 QML 文件的目录（如果使用 Quick 或 QML）
├── forms/ // 存放 UI 文件（.ui）的目录
│ ├── mainwindow.ui // 主窗口 UI 设计文件
│ └── widget.ui // 其他组件 UI 设计文件
└── tests // 单元测试目录
├── reverse_test.cpp // 单元测试源码
└── tests.pro // 单元测试项目文件，描述项目的构建信息
```


为了便于理解，以一个简单的例子来介绍 Qt 项目，这个 demo 最终将在图形界面打开一个窗口，输出 "Hello OpenCloudOS!"

## 3.1 创建项目

参考上文中关于目录结构的介绍，创建如下文件和目录：

```
cd hello_opencloudos/
tree -L 3
.
├── hello_opencloudos.pro
├── src
│ ├── main.cpp
│ ├── mainwindow.cpp
│ ├── mainwindow.h
│ └── utils.h
└── tests
├── reverse_test.cpp
└── tests.pro
```


源代码如下：

`hello_opencloudos.pro`

文件内容：

```
TEMPLATE = app
QT += widgets
TARGET = hello_opencloudos
CONFIG += console
SOURCES += src/main.cpp \
src/mainwindow.cpp \
HEADERS += src/mainwindow.h \
src/utils.h
```


`src/main.cpp`

文件内容：

```
#include <QApplication>
#include "mainwindow.h"
int main(int argc, char *argv[])
{
QApplication app(argc, argv);
MainWindow mainWindow;
mainWindow.setWindowTitle("Hello OpenCloudOS!");
mainWindow.show();
return app.exec();
}
```


`src/mainwindow.h`

文件内容：

```
#pragma once
#include <QWidget>
class MainWindow : public QWidget
{
Q_OBJECT
public:
MainWindow();
};
```


`src/mainwindow.cpp`

文件内容：

```
#include "mainwindow.h"
#include "utils.h"
#include <QWidget>
#include <QVBoxLayout>
#include <QLabel>
MainWindow::MainWindow()
{
QVBoxLayout *layout = new QVBoxLayout(this);
QLabel *label = new QLabel("Hello OpenCloudOS!", this);
layout->addWidget(label);
setLayout(layout);
}
```


`src/utils.h`

文件内容：

```
#pragma once
#include <QString>
// Reverse returns a reversed copy of a QString.
static inline QString Reverse(const QString &s)
{
auto r = s;
std::reverse(r.begin(), r.end());
return r;
}
```


`tests/tests.pro`

文件内容：

```
TEMPLATE = app
CONFIG += console
CONFIG -= app_bundle
QT += testlib
TARGET = reverse_test
DEPENDPATH += ../src
INCLUDEPATH += ../src
SOURCES += reverse_test.cpp
```


`tests/reverse_test.cpp`

文件内容：

```
#include <QtTest>
#include "../src/utils.h"
class TestReverse : public QObject
{
Q_OBJECT
private slots:
void reverse_data();
void reverse();
};
void TestReverse::reverse_data() {
QTest::addColumn<QString>("input");
QTest::addColumn<QString>("expected");
QTest::newRow("empty") << "" << "";
QTest::newRow("single-char") << "a" << "a";
QTest::newRow("odd-length") << "abc" << "cba";
QTest::newRow("even-length") << "abcd" << "dcba";
}
void TestReverse::reverse() {
QFETCH(QString, input);
QFETCH(QString, expected);
QString result = Reverse(input);
QCOMPARE(result, expected);
}
QTEST_MAIN(TestReverse)
#include "reverse_test.moc"
```


## 3.2 构建项目

返回项目根目录，执行如下命令生成 Makefile，本例中，根目录为 `hello_opencloudos/`


```
qmake-qt5
```


完成后会在当前目录下生成 Makefile

```
ls
hello_opencloudos.pro Makefile src tests
```


执行如下命令构建项目

```
make -j
```


构建成功后会在当前目录生成二进制文件

```
tree -L 3
.
├── hello_opencloudos
├── hello_opencloudos.pro
├── main.o
├── mainwindow.o
├── Makefile
├── moc_mainwindow.cpp
├── moc_mainwindow.o
├── moc_predefs.h
├── src
│ ├── main.cpp
│ ├── mainwindow.cpp
│ ├── mainwindow.h
│ └── utils.h
└── tests
├── reverse_test.cpp
└── tests.pro
```


## 3.3 执行

点开图形化界面的 Terminal 工具，在此直接上一步生成的二进制，即可得到预期的打印窗口

## 3.4 单元测试

到 `tests/`

目录下执行如下命令

```
qmake-qt5
make -j
```


会在当前目录生成二进制文件

```
ls -al reverse_test
-rwxr-xr-x 1 root root 23920 May 30 14:56 reverse_test
```


点开图形化界面的 Terminal 工具，执行生成的二进制文件，即可运行用例

# 4 代码调试

## 4.1 通用调测工具

由于代码本身是用 C++ 编写的，用户可以直接使用通用的调测工具进行调试，如：`valgrind, perf, strace, gdb`

等，具体用法本节不多介绍

## 4.2 `qDebug()`

函数

`qDebug()`

函数可以将调试信息直接输出到控制台，在开发阶段也是不错的调测选择，使用方式如下：

```
#include<QDebug>
...
qDebug("x: %d",x);
...
```


# 5 Qt 包管理

系统默认的 `dnf`

包管理工具已经可以处理 Qt 相关软件包的依赖关系。除此之外，Qt 提供了自己的包管理工具 `aqtinstall`

，使用方式如下

使用如下命令安装 `aqtinstall`


```
dnf install -y pip
pip3 install aqtinstall
```


默认情况下命令行工具路径为 `/usr/local/bin/aqt`

，需要添加环境变量

```
export PATH=$PATH:/usr/local/bin
```


之后就可以通过 `aqt`

命令安装 Qt 的软件包，格式如下：

```
aqt install <Qt-version> <host> <target> [--outputdir <install_dir>] [other-options]
```


如：安装一个 gcc_64 到 `~/Qt`

目录下

```
aqt install 5.12.0 linux desktop gcc_64 --outputdir ~/Qt
```


# 6 Qt 工具介绍

## 6.1 `qtpaths`

命令

`qtpaths`

是一个命令行实用程序，用于查询与 Qt 安装相关的路径。它可以提供有关 Qt 安装位置、库、插件、数据文件等的路径信息。在调试 Qt 项目或查找特定组件位置时，`qtpaths`

非常有用。

### 6.1.1 安装 `qtpaths`

命令

执行如下命令即可安装 `qtpaths`

命令

```
dnf install -y qt5-qttools
```


### 6.1.2 `qtpaths`

命令使用

`qtpaths`

命令可以在非图形桌面执行，以下是一些常用选项的示例：

- 获取 Qt 安装路径：

```
qtpaths --install-prefix
```


```
qtpaths --plugin-dir
```


## 6.2 `qtdiag`

命令

`qtdiag`

是一个用于诊断 Qt 安装和配置问题的命令行工具。

### 6.2.1 安装 `qtdiag`

命令

执行如下命令即可安装 `qtdiag`

命令

```
dnf install -y qt5-qttools-devel
```


### 6.2.2 `qtdiag`

命令使用

`qtdiag`

命令需要在图形化界面的 Terminal 工具中执行。

直接执行 `qtdiag`

命令后，会全量打印Qt 版本信息、操作系统信息、已安装图像格式插件、可用字体等。

```
qtdiag
```