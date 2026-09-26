source: https://docs.opencloudos.org/OCS/DevelopGuide/Python_guide/

# Python 开发指南

## 1. Python介绍

### 1.1 Python简介

Python是一种简洁但功能强大的面向对象编程语言，广泛应用在系统构建、应用开发特别是深度学习、数据分析领域，同时python也是一门重要的脚本语言，操作系统和应用的很多组件需要依靠python进行粘合。

### 1.2 本系统上的组件支持情况

Python目前共存2和3两个大版本，Python2和Python3的语法互不兼容，其中Python2的官方维护周期截止至2020年1月1日，各发行版和开发者在python2代码迁移到python3上已经取得了很大进步，有鉴于此，**本系统不再支持Python2**，这意味着：

`/usr/bin/python`

指向了Python3；- 不再为操作系统内的某些软件发布python2绑定；
- 如果某些Python软件还没有迁移到Python3，那么会舍弃该软件，或通过six、2to3等方式迁移到Python3；

本系统的Python版本目前为Python3.10，未来可能会进一步升级，具体请以如下命令为准：

```
python --version
```


在某些形式的镜像，`/usr/bin/python`

不存在，如果执行 `python --version`

命令提示报错 **sh: python: command not found**，此时可以执行如下命令安装：

```
dnf install python
```


### 1.3 安装和卸载

如果是标准的系统镜像，Python3是预装的；但在某些小型的系统镜像里没有安装，此时可以通过如下命令安装:

```
dnf install python python3 python3-pip python3-wheel
```


```
python --version
```


## 2. 简单的使用介绍

本章分别展示直接调用Python3模块、调用交互模式、运行.py脚本三个方式，来介绍Python3的常见使用方式。

### 2.1 直接调用模块执行

调用Python3自带的模块http可以搭建一个简单的web服务，进入某一个目录，执行如下命令：

```
python3 -m http.server 80
```


如果您的网络禁止开启80端口，可以换一个端口号；如果省略端口参数，则默认开启8000端口。

### 2.2 Python交互模式

Python3交互模式是一个类似shell的终端界面，可以在里面执行Python3代码。 以下命令为示例：

```
python
```


```
Python 3.10.5 (heads/rpm-build-dirty:331fd56, May 10 2023, 19:10:08) on linux
Type "help", "copyright", "credits" or "license" for more information.
>>> exit()
```


```
# python
Python 3.10.5 (heads/rpm-build-dirty:331fd56, May 10 2023, 19:10:08) [GCC 12.2.0 20220819 (OpenCloudOS 12.2.0-5)] on linux
Type "help", "copyright", "credits" or "license" for more information.
>>> import sys,platform
>>> print("python" + platform.python_version() + ", for " + sys.platform)
python3.10.5, for linux
>>> exit()
```


### 2.3 执行.py文件

.py扩展名的文件，是Python默认的脚本格式文本，本文以hello.py为例，演示执行方式：

```
#!/usr/bin/env python3
from requests_html import HTMLSession
sess = HTMLSession()
url = "https://www.qq.com"
headers = {
"User-Agent": "User-Agent: Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.212 Safari/537.36"
}
def get_qq_top_news(url):
web = sess.get(url)
sel = "li.news-top > a"
r = web.html.find(sel, first=True)
return r.text
print(get_qq_top_news(url))
```


运行步骤如下：

```
pip3 install requests-html
python3 ./hello.py
```


## 3. 包管理

Python的包管理系统称为Pypi，即广为人知的"pip"，可以用于Python软件包的(在线/本地)安装、卸载、升降级、打包等处理，这里只展示两个功能：在线安装软件包和打包。

### 3.1 在线安装软件包

按照如下命令操作即可

```
pip3 install numpy
```


### 3.2 打包

Python软件包的格式为.whl，其本质为zip，这里展示一个用setup.py形式编写的软件包的打包过程：

```
dnf install python3-setuptools
git clone https://github.com/navdeep-G/setup.py.git
cd setup.py
python3 setup.py bdist_wheel
```


## 4. 更多参考资料

- Python官方的《Python初学者手册》，中文版：https://wiki.python.org/moin/BeginnersGuideChinese
- pip官方文档：https://pip.pypa.io/en/stable/getting-started/