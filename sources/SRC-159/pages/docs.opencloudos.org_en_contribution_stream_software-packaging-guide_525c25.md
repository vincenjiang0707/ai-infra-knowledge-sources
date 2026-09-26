source: https://docs.opencloudos.org/en/contribution/stream/software-packaging-guide/

# 软件包打包指导

## 1. 文档说明

本文档对OpenCloudOS社区软件包打包操作进行说明，指导社区开发者按照社区规范进行软件包打包，提升软件包打包质量。

## 2. SPEC文件

SPEC文件各tags、sections说明详见：https://rpm-software-management.github.io/rpm/manual/spec.html。

### 2.1. SPEC文件布局

SPEC文件尽量按照如下格式、布局进行编写：

```
%global xxx #全局变量定义
%undefine xxx #全局变量定义
%bcond_with xxx #条件控制
Summary:
Name:
Version:
Release: #即使代码没变，但由于spec调整、依赖变化、编译工具链变化等原因的重编都需要+1
License:
URL:
Source0: #虽然写Source也没错，但建议统一写Source0
Source1:
......
Patch0001: #补丁编号，详见后面的说明
Patch0002:
......
BuildArch: #如果是noarch，需明确指出
BuildRequires: #建议按软件包归类、分行，比如基础编译工具链相关的gcc、make、autoconf等放一行
BuildRequires: #直接编译依赖尽量写全，间接编译依赖（即直接编译依赖的运行依赖）不需要写
Requires: #建议按软件包归类、分行；每行的多个包建议统一用空格或者逗号分隔，不要空格、逗号混用
Requires： #如果软件包有版本号要求，建议一个包一行
Provides: #详见https://ftp.osuosl.org/pub/rpm/max-rpm/s1-rpm-depend-manual-dependencies.html
Conflicts: #主要用于路径或者功能冲突
Obsoletes: #主要用于软件包替代或者重命名
%description #主包描述，包的名字为Name，前面的BuildRequires、Requires等都是对主包的说明
%package 子包 #子包
Summary:
Requires:
Provides:
%description 子包 #子包描述
......
%prep #准备阶段，包括源码包解压、打补丁等动作
.....
%build #编译阶段
......
%install #安装阶段，将编译出的目标文件安装到虚拟的根目录；
...... #建议一个目录一个目录处理，或者一类一类文件（配置、bins、动态库等）处理
%check #测试阶段
......
%pre #按需添加scriptlets，对rpm包安装、卸载、升级动作执行前后的动作进行说明
%post
%preun
%postun
%triggerin #按需添加triggers
%triggerun
%triggerpostun
%files #打包阶段，打包主包
%files 子包 #打包子包
%changelog
* Mon Dec 26 2022 XXXX <XXX@YYY> - version-release
- initial build
```


### 2.2. SPEC文件风格

建议在编写SPEC时就像写其他代码一样，形成一定的编写风格、逻辑，包括适当的空行分段、适当的空格对齐、 同一个或者同类型的操作用同一种写法等，形成干净、简洁的SPEC文件

## 3. N-V-R

软件包的Name、Version跟上游社区保持一致，release号从1开始、并与changelog中的release号保持一致。 如果version变化，release号从1重新开始。

## 4. URL和Source

URL、Source中的地址确保可以访问，确保来源可靠、合规。

## 5. License

通过上游社区的主页说明、README文件、License文件、COPYING文件以及文件头等地方确认涉及的License、Copyright等声明， 确保SPEC中的License声明正确、全面。

如果有多个License，则用and 连接。 如果license不友好或者非标准的经OSI认证的开源协议，谨慎引入。

## 6. 补丁名称和编号

为了方便补丁的管理，例如社区基础平台的自动化升级工具在尝试升级新版本时，如果遇到补丁冲突，会根据补丁编号尝试去掉来之上游社区的补丁，提升开发维护效率，因此将补丁分为三类： - 来之上游社区或者基于上游社区新代码自己做的补丁，从0001开始编号，即Patch0001、Patch0002等。 - 来之其他发行版的补丁，从3000开始编号，即Patch3000、Patch3001等。 - 自定义补丁，没被上游社区接纳，从5000开始编号，即Patch5000、Patch5001等。

补丁名称尽可能描述出修改的问题的关键信息，补丁名称不要求带补丁编号，带的话，维护性更好些。

## 7. %check

软件包自带测试用例作为保证软件包质量的关键措施，无特殊原因不能disable。

## 8. %install和%files

%install阶段，建议按照目录一个一个处理，形成一定的逻辑性，避免来回跳转、不利于后期维护。如果要生成目录，建议目录生成之后，就处理该目录下的安装。

### 8.1. 打包顺序

%files打包阶段，先打主包，然后打子包，子包顺序与前面的%package顺序一致。 同时建议%package和%files按照子包间的依赖关系、重要程度来排序，比如主包、libs子包、utils子包、devel子包、doc子包等。

不成熟的、业界很少使用的能力（如sudo的logserver功能）不建议打包提供。

打包时，建议按照目录或者文件类型一个一个处理，形成一定的逻辑性，避免来回跳转、不利于后期维护。 建议先license、doc、配置文件，然后主程序（命令、动态库等），最后man、info等。

## 9. %changelog

changelog log 尽量与commit log一致，简洁，说明关键的修改点

## 10. 其他参考

关于SPEC文件更详细的说明，可以参考： - https://ftp.osuosl.org/pub/rpm/max-rpm/index.html - https://rpm.org/documentation.html