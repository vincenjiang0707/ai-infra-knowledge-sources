source: https://docs.opencloudos.org/contribution/oc9-port-dev/

# OpenCloudOS V9 应用移植开发文档

本文档旨在指导用户在 OpenCloudOS 系统上完成 **Visual Studio Code (VSCode)** 和 **PyCharm** 的安装及基础环境配置。

## 一、VSCode 安装

Visual Studio Code（简称 VSCode）是微软推出的一款支持 Mac OS、Windows 与 Linux 的跨平台源码编辑器，适用于现代 Web 与云应用的开发。

### 1.下载 RPM 安装包

-
访问 VSCode 官网：下载.rpm 文件,


### 2. 安装 RPM 包

- 在下载目录打开终端，执行如下命令进行安装：

sudo dnf install code-1.105.1-1760482588.el8.x86_64.rpm

- 安装完成后，即可在系统开始菜单中找到 VSCode。主界面展示如下：

## 二、VSCode 环境配置

### 1、安装 C/C++ 插件

- 通过左侧边栏 Extensions 搜索并安装 C/C++ 插件，安装过程如下图：

### 2、建立工程

-
VSCode 以文件夹为粒度管理工程，推荐新建一个项目文件夹，例如 hello，

-
然后使用 VSCode 打开该文件夹：


- 新建 main.cpp，编写简单程序：

### 3、配置调试（launch.json）

-
点击左侧 Debug，选择 “Add configuration”，选择 “C++ (gdb) Launch”，系统将自动生成 launch.json：

-
生成的默认配置如下：


-
生成的默认 json 文件如下：

`{ ` `// Use IntelliSense to learn about possible attributes. ` `// Hover to view descriptions of existing attributes. ` `// For more information, visit: https://go.microsoft.com/fwlink/?linkid=830387 ` `"version": "0.2.0", ` `"configurations": [ ` `{ ` `"name": "(gdb) Launch", ` `"type": "cppdbg", ` `"request": "launch", ` `"program": "enter program name, for example ${workspaceFolder}/a.out", ` `"args": [], ` `"stopAtEntry": false, ` `"cwd": "${fileDirname}", ` `"environment": [], ` `"externalConsole": false, ` `"MIMode": "gdb", ` `"setupCommands": [ ` `{ ` `"description": "Enable pretty-printing for gdb", ` `"text": "-enable-pretty-printing", ` `"ignoreFailures": true ` `}, ` `{ ` `"description": "Set Disassembly Flavor to Intel", ` `"text": "-gdb-set disassembly-flavor intel", ` `"ignoreFailures": true ` `} ` `] ` `} ` `] }`

-
注意:这里需要将 program 项的内容改为调试时运行的程序，将其改为 main.out即可。

- 具体更改如下：

```
"program": "enter program name, for example
${workspaceFolder}/a.out",
```


```
"program": "${workspaceFolder}/main.out",
```


### 4、添加构建任务（tasks.json）

-
为方便编译运行，可将 g++ 命令定义为任务。

-
使用快捷键 Ctrl+Shift+P，输入 Tasks: Run task，首次执行会提示：


No task to run found. configure tasks...

- 回车，然后依次选择如下：

Configure a Task

Create tasks.json file from template

Others Example to run an arbitrary external command.

-
生成默认的 tasks.json 文件如下：

`{ ` `// See https://go.microsoft.com/fwlink/?LinkId=733558 ` `// for the documentation about the tasks.json format ` `"version": "2.0.0", ` `"tasks": [ ` `{ ` `"label": "echo", ` `"type": "shell", ` `"command": "echo Hello" ` `} ` `] }`

-
这里的 label 为任务名，我们将”label"= "echo"改为”label"= "build"。

-
由于我们的指令是 g++，这里将”command“=”echo Hello“为”command“=”g++“。

-
然后添加 g++的参数 args。如果我们的 g++指令为：g++ -g main.cpp，这里可

-
以把参数设置为如下：

`{ "tasks": [ { "label": "build", "type": "shell", "command": "g++", "args": ["-g", "${file}"] } ]}`

-
如果我们想配置 g++指令为：g++ -g main.cpp -std=c++11 -o main.out，则参数可设置为：

`{ "tasks": [ { "label": "build", "type": "shell", "command": "g++", "args": ["-g", "${file}", "-std=c++11", "-o", "${fileBasenameNoExtension}.out"] } ]}`

-
我们可以通过举一反三来配置不同的 g++指令。完整的 tasks.json 文件可参考附录。


### 5、简单断点调试

经过上述配置之后就可以对我们写的程序进行简单的配置。在进行下面的操作

前，我们应当保证 launch.json 和 tasks.json 的正确性并且已经成功保存。

使用快捷键 ctrl+shift+p 调出命令行，输入 Tasks: Run task 选择执行我们的

build 任务,选择 continue without scanning the task output（进入到main.cpp文件页面，再run task），build 成功后，点击开始调试。 - 具体操作如下：

- 值得注意的是，这里如果每次更改了程序需要重新 build，然后再进行调试；

如果直接进行调试则运行的是上次 build 的结果。通过在 launc.json 作如下更改可以使得每次调试之前会自动进行 build：

这里在 launch.json 文件中添加了”preLaunchTask“=”build"，也就是添加一

个 launch 之间的任务，任务名为 build，这个 build 就是我们在 tasks.json 中设置的任务名。

## 三、PyCharm 安装

### 1、下载官方安装包

打开浏览器访问：[https://www.jetbrains.com/pycharm/download/?section=linux](https://www.jetbrains.com/pycharm/download/?section=linux)

找到 Linux 对应安装包并下载。

### 2、进入下载目录

一般安装包默认保存在 ~/下载/，执行：。

cd ~/下载

### 3、解压安装包

tar -xvf pycharm-2025.2.4.tar.gz

### 4、进入解压后的目录

cd pycharm-2025.2.4/

### 5、执行启动脚本

- 进入 bin 目录：

cd bin/

- 启动 PyCharm：

./pycharm.sh

- 运行该命令后，PyCharm 将会启动，并进入初始化配置界面。这一步可能需要一些时间，请耐心等待。

### 6、初始配置

首次运行 PyCharm 时，会出现一个初始设置向导，您可以选择以下内容：

-
导入设置：如果之前使用过 PyCharm，可以选择导入原有设置。

-
UI 外观设置：选择 PyCharm 的主题（如深色模式或浅色模式）。

-
插件安装：可以选择安装一些实用插件，如 Python Docstring、Markdown Support 等。


## 四、Pycharm常用配置

### 1、添加 PyCharm 至 PATH（可选）

避免反复进入 bin 目录运行：

在设置中勾选 “Add to PATH” 或手动添加。

### 2、创建桌面快捷方式

- 编辑配置文件：

`nano ~/.local/share/applications/pycharm.desktop`


-
拷贝以下内容到文件里（根据本机情况修改）

`<a name="_toc27891"></a>[Desktop Entry] Type=Application Name=PyCharm GenericName=Python IDE Comment=PyCharm Professional IDE Exec=/home/sun/下载/pycharm-2025.2.4/bin/pycharm.sh Icon=/home/sun/下载/pycharm-2025.2.4/bin/pycharm.png Terminal=false Categories=Development;IDE; StartupNotify=true`

-
更新 GNOME 应用列表：


update-desktop-database ~/.local/share/applications/

- 刷新后即可在桌面环境看到快捷启动图标。

## 五、PyCharm创建Python项目

### 1、创建新项目

- 打开 PyCharm 后，您将看到一个欢迎界面，点击 "New Project" 按钮创建一个新项目。
- 设置项目位置：选择新项目的存储路径，例如 /home/sun/PycharmProjects/PythonProject。
- 选择 Python 解释器：PyCharm 支持虚拟环境，您可以选择使用系统的 Python 解释器或者创建新的虚拟环境。
- 建议为每个项目创建独立的虚拟环境以保证项目之间互不干扰。

### 2、编写第一个 Python 程序

- 右键项目目录 → New → Python File，命名为：

hello_world.py

- 编辑hello demo：

print("Hello, PyCharm!")

### 3、运行程序

- 右键运行或点击右上绿色箭头，输出示例：

## 六、附录

这里给出一个较完整的配置文件和任务文件，该配置仅供参考！ ### 1、launch.json

```
{
// Use IntelliSense to learn about possible attributes.
// Hover to view descriptions of existing attributes.
// For more information, visit:
https://go.microsoft.com/fwlink/?linkid=830387
"version": "0.2.0",
"configurations": [
{
"name": "(gdb) Launch",
"type": "cppdbg",
"request": "launch",
"program":
"${workspaceFolder}/${fileBasenameNoExtension}.out",
"args": [],
"stopAtEntry": false,
"cwd": "${workspaceFolder}",
"environment": [],
"externalConsole": true,
"MIMode": "gdb",
"preLaunchTask": "build",
"setupCommands": [
{
"description": "Enable pretty-printing for gdb",
"text": "-enable-pretty-printing",
"ignoreFailures": true
}
]
}
]}
```


### 2、tasks.json

```
{
// See https://go.microsoft.com/fwlink/?LinkId=733558
// for the documentation about the tasks.json format
"version": "2.0.0",
"tasks": [
{
"label": "build",
"type": "shell",
"command": "g++",
"args": ["-g", "${file}", "-std=c++11", "-o",
"${fileBasenameNoExtension}.out"]
}
]}
```