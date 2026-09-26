source: https://docs.opencloudos.org/en/contribution/stream/rpm-dep/

# 1.整体介绍

软件包又称为 RPM 包，它们之间也存在错综复杂的依赖关系，以 glibc 为例，下图节选了一部分相关联的 RPM 包。RPM 包之间的箭头代表着它们的依赖关系，是操作系统的血管与神经，牵一发而动全身。

rpm-dep 是自维护过程中自研 RPM 包依赖分析工具，能够高效梳理软件包错综复杂的依赖，输出成直观易读的文本形式；同时能根据依赖关系对受影响的包列表进行排序，指导CI维护人员精确高效地进行批量构建与自验证。

# 2. 实战场景展示

在版本发布，基础软件升级，RPM 包批量升级等涉及RPM包变更的场景下，需要精确获取受变更影响的RPM包列表，进行批量构建与测试验证；

对于普通开发者，在处理RPM 包增删过程中，需要评估RPM包的变化带来的影响。由于RPM包之间依赖关系错综复杂，产生了如下问题：

1、现有的 yum 和 dnf 命令不足以获取准确的受影响的RPM包列表，相关开发维护人员无法直观地观察到RPM包在依赖链中的具体位置与上下层级关系。

2、受影响的包基于变化的包重新构建时，如果简单全量编译包列表，可能导致重新构建失效。

此时就可以使用 rpm-dep 工具解决上述问题。

## 2.1 精准获受影响 RPM 包列表

目前通过 [rpm-check](https://mp.weixin.qq.com/s/-nHwRK7HNj3GzvD9oHnp6A) 工具对兼容性变更的识别，当后者识别到兼容变更时，可以通过 rpm-dep 工具确认变更影响了哪些包。

这里仍以文中的 ffmpeg 包为例，假设某用户需要升级 ffmpeg 包，但是不清楚该包升级后会对环境中的其他依赖 ffmpeg 的包产生什么影响。rpm-check 工具后端调用了 rpm-dep 的反向依赖查询功能，获取到受影响包列表如下，然后逐个包判断调用关系，最终得出 ffmpeg 包的变更影响情况。

```
$ rpm-dep -I ffmpeg
Dependency Statistics Report for:
pkg name: ffmpeg
src name: ffmpeg
┏━━━━━━━┳━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━━━━┓
┃ Level ┃ Pkg numbers ┃ Source pkg numbers ┃
┡━━━━━━━╇━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━━━━┩
│ 2 │ 10 │ 3 │
└───────┴─────────────┴────────────────────┘
[INFO] max query level: 2
[INFO] detail report: dep_tree__ffmpeg__install.json
$ cat dep_tree__ffmpeg__install.json
{
"level": 1,
"pkg_name": "ffmpeg",
"src_name": "ffmpeg",
"next": [
{
"level": 2,
"pkg_name": "SDL2",
"src_name": "SDL2",
"next": []
},
{
"level": 2,
"pkg_name": "glibc",
"src_name": "glibc",
"next": []
},
{
"level": 2,
"pkg_name": "libavcodec",
"src_name": "ffmpeg",
"next": []
},
{
"level": 2,
"pkg_name": "libavdevice",
"src_name": "ffmpeg",
"next": []
},
{
"level": 2,
"pkg_name": "libavfilter",
"src_name": "ffmpeg",
"next": []
},
{
"level": 2,
"pkg_name": "libavformat",
"src_name": "ffmpeg",
"next": []
},
{
"level": 2,
"pkg_name": "libavutil",
"src_name": "ffmpeg",
"next": []
},
{
"level": 2,
"pkg_name": "libpostproc",
"src_name": "ffmpeg",
"next": []
},
{
"level": 2,
"pkg_name": "libswresample",
"src_name": "ffmpeg",
"next": []
},
{
"level": 2,
"pkg_name": "libswscale",
"src_name": "ffmpeg",
"next": []
}
]
}
```


## 2.2 受影响包按优先级处理

例如 hivex 软件包发生了兼容性变更，通过 rpm-dep 工具获取到了受影响的包列表。由于受影响的包直接也可能存在依赖关系，高优先级的需要优先处理，因此可以使用 rpm-dep 作为扩展功能提供的排序能力，最终得到如下表，可以看出，libguestfs 被 guestfs-tools 依赖，要先于 guestfs-tools 被处理。

# 3. 功能介绍

rpm-dep 的功能图如下所示，初始化阶段会解析 OS repo 源的 repodata 文件，建立依赖关系表，为了提高查表速度，会保存到 Redis 中，rpm-dep 维护一个服务用于响应用户的查询请求。

用户可以通过如下命令安装 rpm-dep，并启动对应的服务

```
# 配置 yum 源
## 安装 yum-config-manager，也可以直接手动配置如下源
dnf install dnf-utils
## x86_64
yum-config-manager --add-repo https://mirrors.opencloudos.tech/opencloudos-stream/releases/23/binary/x86_64/Packages/
## aarch64
yum-config-manager --add-repo https://mirrors.opencloudos.tech/opencloudos-stream/releases/23/binary/aarch64/Packages/
# 安装 rpm 包
dnf install rpm-dep
# 启动服务
systemctl enable rpm-depd
systemctl start rpm-depd
```


## 3.1 依赖查询

构建 / 安装一个 RPM 包，需要额外安装一些依赖包，这中依赖类型称为“编译 / 安装依赖”。

rpm-dep 提供了简单的命令来查询这些依赖，使用方式如下

```
# 查询编译依赖
rpm-dep --build / -b $pkg_name
# 查询安装依赖
rpm-dep --install / -i $pkg_name
```


一个 RPM 包也可能被其它的软件包编译 / 安装依赖，这种依赖类型称为“反向编译 / 安装依赖”。

可以使用如下方式查询此类依赖

```
# 查询反向编译依赖
rpm-dep --build_by / -B $pkg_name
# 查询反向安装依赖
rpm-dep --install_by / -I $pkg_name
```


无论哪种类型查询，默认显示 1 层依赖，如果期望查询多层，通过 rpm-dep 的 --level 选项指定层数即可。

## 3.2 依赖包排序

对于CI维护人员来说，仅获取 RPM 包的依赖关系是不够的，查询的结果不同层级、同一层级之间都存在依赖关系，需要结合依赖关系进行排序，区分优先级。优先级高的RPM包先处理（如重新编译），优先级低RPM包的基于高优先级包的处理结果后处理。为此，可以使用 rpm-dep 工具集提供的如下命令行进行排序

```
# 为 $pkg_name_list 列表中的包参考编译依赖关系进行排序
rpm-unfold --build $pkg_name_list
# 为 $pkg_name_list 列表中的包参考编译和安装依赖关系进行排序
rpm-unfold --requires $pkg_name_list
```


用户将得到根据优先级排列的 json 文件，从而由高到低处理对应的 RPM 包。

# 4. 代码实现

rpm-dep 的整体架构如下图所示，其中：

1 为 rpm-depd 服务

2 为 rpm-dep 依赖查询命令

3 为 rpm-unfold 依赖排序命令

rpm-depd 初始化阶段，从在线的操作系统 repo 源中下载 repodata 文件并解析，构造出依赖符号表，将依赖相关的符号与包名构造成 key - value 的形式。

如下图，rpm-depd 获取查询请求时，根据请求的类型，获取待查询 RPM 包的对应符号，然后以此符号为 key 查找对应的 value 从而获取目标 RPM 包。

如果用户指定了层数，则以当前层数的目标 RPM 包为入参，通过 BFS 算法继续遍历，直到无法遍历或者识别到循环依赖则停止查询。

rpm-unfold 排序的原理如下图所示。图中存在需要进行 4 层的依赖关系。 level 2有 B 和 C 两个包，同时在 level 3 也存在 C 与 level 2 的 B有依赖关系。 level 3有C、D 和 E 三个包，同时在 level 4 也存在 D 与 level 3 的 C 有依赖关系， 在 level 4 也存在 E 与 level 3 的 D 有依赖关系。

这里使用了拓扑排序的思想，把依赖树中的每个包视作一个节点，在同一层, 遍历每一个节点，判断该节点是否为其它节点的后代，把不是任何节点后代的节点汇总起来得到一组，对剩下的节点重复上面的操作，直到不再剩余节点，对于重复的节点添加去重即可。