source: https://docs.opencloudos.org/en/OCS/DevelopGuide/Luajit_guide/

# Luajit开发指南

## 介绍

LuaJIT 是一个 Just-In-Time 编译器（即时编译器），为 Lua 语言提供高效执行。

### 版本选型

当前系统维护的版本为2.1.x，后续可能升级为更高版本，具体版本信息，请以如下命令查询为准：

```
luajit -v
```


### 安装 LuaJIT

使用以下命令安装 LuaJIT：

```
dnf install -y luajit
```


## 使用介绍

**创建一个 Lua 脚本**

使用文本编辑器（如 nano、vim 等）创建一个简单的 Lua 脚本 "hello_world.lua"，然后将以下 Lua 代码复制到文件中：

```
print("Hello, World!")
```


保存文件并退出编辑器。

**使用 LuaJIT 运行 Lua 脚本**

在终端中，导航到 `hello_world.lua`

文件所在的目录，然后运行以下命令以使用 LuaJIT 执行脚本：

```
luajit hello_world.lua
```


终端将输出以下内容：

```
Hello, World!
```


## 更多参考资料

LuaJIT 官方文档：http://luajit.org/running.html

本地 LuaJIT 帮助文档中提供了更多细节和示例，可以在 `/usr/share/doc/luajit/`

目录中找到。