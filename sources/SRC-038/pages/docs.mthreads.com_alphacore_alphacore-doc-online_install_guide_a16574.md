source: https://docs.mthreads.com/alphacore/alphacore-doc-online/安装指导/install_guide

# 安装指导

## 申请试用[](https://docs.mthreads.com#申请试用)

目前我们的Catalyst FX 还处于内部申请测试阶段，请发送邮件至 [alphacore@mthreads.com](mailto:alphacore@mthreads.com) 留下您的联系方式，我们会尽快联系您。

`姓名：`

联系方式：

公司：

所属行业：

软硬件操作系统环境：

其它备注信息（选填）：



## Houdini Install[](https://docs.mthreads.com#houdini-install)

### 1 Windows[](https://docs.mthreads.com#1-windows)

Windows Houdini 版本我们提供19.0.720, 19.5.303, 19.5.368, 19.5.493, 20.0.547等版本。如果您有其他版本需求可随时发送邮件与我们联系。

您可以直接使用安装包下的`AlphaCoreHoudiniSetup.exe`

安装AlphaCore-Houdini，也可以通过手动安装的方式进行安装。

#### 1.1 安装包安装[](https://docs.mthreads.com#11-安装包安装)

-
解压安装包，并运行

`AlphaCoreHoudiniSetup.exe`

安装程序。 -
选择houdini版本号。

-
Houdini 版本默认会安装到

`C:\Users\用户名\Documents\houdiniXX.X\`

目录下。如果您有特殊需求，可以勾选CustomPath选项，并修改安装目录。但是您需要确保Houdini在启动的时候会加载该目录下的dso和otls文件。 -
点击Setup按钮安装，拷贝

`dso`

和`otls`

文件到指定目录下。 -
启动Houdini，即可在Houdini中使用AlphaCore-Houdini。


#### 1.2 手动安装[](https://docs.mthreads.com#12-手动安装)

-
解压安装包，找到Houdini版本对应的目录，例如

`AlphaCoreHoudini_Windows_Cuda\19.0.720`

。 -
将

`AlphaCoreHoudini_Windows_Cuda\19.0.720\`

目录下的`dso`

和`otls`

文件夹拷贝到`C:\Users\用户名\Documents\houdiniXX.X\`

目录下，或者您可以拷贝到自定义目录，但是您需要确保Houdini在启动的时候会加载该目录下的dso和otls文件。 -
启动Houdini，即可在Houdini中使用AlphaCore-Houdini。


### 2 Linux[](https://docs.mthreads.com#2-linux)

Linux Houdini 版本我们提供19.0.620, 19.0.720, 19.5.303, 20.0.653等版本。如果您有其他版本需求可随时发送邮件与我们联系。

您可以直接使用安装包下的`AlphaCoreHoudiniSetup.install`

脚本安装AlphaCore-HDK，也可以通过手动安装的方式进行安装。

#### 2.1 脚本自动安装[](https://docs.mthreads.com#21-脚本自动安装)

- 运行
`unzip ./AlphaCoreHoudini_XXX_XXXX_Linux_XXXX_.zip ./`

解压安装包。 - 运行
`cd AlphaCoreHoudini_Linux_Cuda`

进入安装包目录。 - 运行
`sudo chmod -R 777 ./AlphaCoreHoudiniSetup.install`

，给予脚本执行权限。 - 运行
`./AlphaCoreHoudiniSetup.install`

安装脚本。 - 输入
`1`

，选择houdini版本号。 - 输入
`2`

，选择安装路径，输入`3`

使用默认安装路径。 - 输入
`I`

，进行安装。

#### 2.2 手动安装[](https://docs.mthreads.com#22-手动安装)

- 运行
`unzip ./AlphaCoreHoudini_XXX_XXXX_Linux_XXXX_.zip ./`

解压安装包。 - 运行
`cd AlphaCoreHoudini_Linux_Cuda`

进入安装包目录。 - 找到Houdini版本对应的目录，例如
`AlphaCoreHoudini_Linux_Cuda\19.0.720`

。运行`cd 19.0.720`

进入该目录。 - 运行
`cp -r ./dso /home/用户名/houdini19.0/dso`

和`cp -r ./otls /home/用户名/houdini19.0/otls`

拷贝`dso`

和`otls`

。 - 启动Houdini，即可在Houdini中使用AlphaCore-HDK。