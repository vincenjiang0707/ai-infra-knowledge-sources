source: https://docs.opencloudos.org/en/OCS/DevelopGuide/RUST_guide/

# Rust使用指南

## 1. Rust 简介

Rust 是一款高效、可靠的通用高级语言，主打“安全、并发、实用”。Cargo 是 Rust 的构建系统和包管理器。

## 2. Rust 安装

### 2.1 dnf 方式

在 OpenCloudOS 中， 运行以下命令来安装 Rust-toolset 软件包：

```
sudo dnf install rust-toolset
```


安装完毕后可通过如下指令检查是否正确安装了 Rust，此时能看到当前安装的版本号、哈希值和提交日期：

```
rustc -V
cargo -V
```


### 2.2 rustup 方式

除了 dnf 安装方式以外，也可以通过 rustup 进行安装，简要安装指令如下：

```
sudo dnf install rustup
# 优先使用 rustup-init 安装
rustup-init
# 按需使用 toolchain 安装
# rustup toolchain install stable
```


安装成功后，同样可执行 `cargo -V`

验证安装结果，此时能看到最新发布的稳定版本的版本号、提交哈希值和提交日期。

如果安装时出现如下报错，可尝试从 root 用户切换为普通用户后，重新执行 `rustup toolchain install stable`

安装：

```
rustup toolchain install stable
info: syncing channel updates for 'stable-x86_64-unknown-linux-gnu'
stable-x86_64-unknown-linux-gnu unchanged - rustc 1.69.0 (84c898d65 2023-04-16)
error: rustup is not installed at '/root/.cargo'
```


更多 rustup 使用，请参照附录中的 rustup 官方指导。

## 3. Rust 使用

Cargo 是 Rust 编译器的构建工具和依赖项管理器。可以通过它声明有特定版本限制的依赖关系、解析完整的依赖关系图、下载包、构建以及测试整个Rust项目。

Rust 开发者常用 Cargo 来管理 Rust项目和获取所依赖的库。

### 3.1 创建项目

#### 3.1.1 项目类型

Cargo通过执行 `cargo new`

指令，可以一键构建Rust项目，譬如新建一个经典项目：

```
cargo new hello_world --bin # 早期cargo必须设置--bin，以指定创建bin类型项目
cargo new hello_world # 作用同上
```


新建一个Rust库：

```
cargo new --lib hello_lib
```


注：**Rust 项目主要分为两个类型： bin 和 lib ，前者是一个可运行的项目，后者是一个依赖库项目**。


早期的 `cargo`

在创建项目时，必须添加 `--bin`

的参数。我们**当前提供版本 cargo 默认创建 bin 类型的项目**，故无需显示指定


`--bin`

参数。#### 3.1.2 项目结构

项目创建后，查看项目结构：

```
tree
.
├── Cargo.toml
└── src
└── main.rs
```


此时项目目录结构较为简单，更多情况下可能包含其他目录结构，相关解读如下：
- Cargo.toml： `Cargo`

特有的**项目描述文件**或**manifest**元清单，它包含了 Cargo 编译项目所需的所有元数据；
- Cargo.lock：`Cargo.lock`

文件是 `Cargo`

工具根据同一项目的 `toml`

文件生成的**项目依赖详细清单**，一般无需修改；
- src目录：源代码存放位置；
- src/main.rs：主可执行文件，编辑项目代码时修改 `main.rs`

并将新的源文件添加到 `src`

子目录；
- benches目录：基准测试 benchmark存放目录；
- examples目录：示例代码存放目录；
- tests目录：集成测试代码存放目录；

Cargo.toml 文件中格式解读如下：

```
[package]: 定义项目( package )的元信息
name: 项目名称
version: 项目版本
authors: 项目作者
edition: 当前使用的Rust大版本
rust-version: Rust最低要求
description: 项目描述
documentation: 文档
readme: README文件
homepage: 主页
repository: 源代码仓库
license: 开源协议License.
license-file: License文件
keywords: 项目关键词
categories: 项目分类
workspace: 工作空间 workspace
build: 脚本编译路径
links: 本地链接库的名称
exclude: 发布时排除文件
include: 发布时包含文件
publish: 用于阻止项目的发布
metadata: 额外的配置信息，用于提供给外部工具
default-run: [cargo run] 所使用的默认可执行文件( binary )
autobins: 禁止可执行文件的自动发现
autoexamples: 禁止示例文件的自动发现
autotests: 禁止测试文件的自动发现
autobenches: 禁止 bench 文件的自动发现
resolver: 设置依赖解析器( dependency resolver)
```


### 3.2 运行项目

有两种方式可以运行您的 Rust 项目，第一种为手动编译后执行，另一种为一步到位。

#### 3.2.1 分步运行

使用 Cargo 构建工具手动编译：

```
cargo build
```


然后可以看到项目下生成了 target 文件夹，且 target/debug 目录下生成了相应的可执行文件，手动执行即可。

```
# 查看文件类型
file target/debug/hello_world
target/debug/hello_world: ELF 64-bit LSB pie executable, x86-64, version 1 (SYSV), dynamically linked, interpreter /lib64/ld-linux-x86-64.so.2, BuildID[sha1]=c87cf5694fab5ba052821001f3d9c31070543413, for GNU/Linux 3.2.0, with debug_info, not stripped
# 手动运行
./target/debug/hello_world
```


#### 3.2.2 一步运行

对于 C/C++ 等开发者来说，先编译后执行的流程可能再熟悉不过。但是对于 Rust 开发者而言，Cargo 还提供了一键式运行的指令：

```
cargo run
Compiling hello_world v0.1.0 (/root/test/hello_world)
Finished dev [unoptimized + debuginfo] target(s) in 0.25s
Running `target/debug/hello_world`
```


`cargo run`

首先对项目进行编译，然后再运行，因此它实际上等同于运行了两个分步指令，对于使用者而言可以简化操作。

#### 3.2.3 debug/release 模式

不论是手动分步还是一键运行，执行完毕后可以发现 target 下新增了 debug 目录，意味着默认运行的是 `debug`

模式。

```
tree -L 2
.
├── Cargo.lock
├── Cargo.toml
├── src
│ └── main.rs
└── target
├── CACHEDIR.TAG
└── debug # debug模式
```


在 `debug`

模式下，代码编译速度快，开发者可以流畅编译。但同时意味着运行速度会变慢，在发布时会带来负面影响。所以您也可以在发布时，显示指定为 `release`

模式：

```
cargo run --release
cargo build --release
```


同理，target 下会新增相应的 release 目录：

```
tree -L 2
.
├── Cargo.lock
├── Cargo.toml
├── src
│ └── main.rs
└── target
├── CACHEDIR.TAG
├── debug
└── release # release模式
```


### 3.3 检查项目

当 Rust 项目臃肿之后，如果需要检验代码正确性，使用 `cargo run`

和 `cargo build`

会较为耗时。此时，可以通过 `cargo check`

对代码进行快速编译：

```
cargo check
Finished dev [unoptimized + debuginfo] target(s) in 0.02s
```


此外，还可以运行测试 Rust 项目。如果项目中的测试较多，还支持指定运行单个测试、过滤部分测试等。但需注意的是返回类型必须是 `()`

或 `Result<(), E> where E: Error`

。

```
cargo test # debug 模式
cargo test --release # release 模式
```


### 3.4 项目文档

Cargo 还支持从源代码中提取注释以生成文档。但需要注意的是：

- 仅为公共函数、变量和成员提取文档注释；
- 所提取的注释，要使用三个斜线
`///`

对其进行标记；

```
cargo doc --no-deps
```


## 4. Rust 工具介绍—— rustfmt

`rustfmt`

是一个用于格式化 Rust 代码的工具，可以帮助开发者确保代码的整洁、一致性和可读性。使用 `rustfmt`

可以将 Rust 代码自动格式化为符合社区推荐的代码风格，提供一致的代码规范。 `rusftmt`

即可独立使用，也可以与 Cargo 一起使用。

在开始使用 `rustfmt`

之前，请确保安装了 `rustfmt`

。如果尚未安装，可以通过运行以下命令轻松地安装它：

```
dnf install rustfmt
```


成功安装 `rustfmt`

后，您可以按照以下方式使用它：

### 4.1 rusftmt 独立使用

使用 `rustfmt`

命令后，程序将根据默认配置规范格式化指定的Rust源文件。默认情况下， `rustfmt`

会将格式化过的内容直接输出到终端。

```
rustfmt src/test.rs
```


以原地覆盖方式格式化文件 若要让 `rustfmt`

直接修改源文件，以原地覆盖的方式格式化，可以使用 `--emit`

标志：

```
rustfmt --emit files src/test.rs
```


### 4.2 同 Cargo 一起使用

`rustfmt xx.rs`

可以格式化指定文件，而使用 `cargo fmt`

命令则可以自动应用 `rustfmt`

格式化规则，为项目中所有的 `.rs`

文件进行格式化。

```
cargo fmt
```


如果要自定义格式化规则，您需要在项目根目录或任何父目录中创建一个名为 `rustfmt.toml`

的文件。在这个文件中，可以添加省略引号的键值对配置，例如：

```
max_width = 100
reorder_imports = true
```


创建 `rustfmt.toml`

文件后， `rustfmt`

会自动应用其中的配置选项进行格式化。

## 5 常见问题

### 5.1 Cargo.toml 校验

修改 `Cargo.toml`

后，无法通过校验。

```
error: the listed checksum of `/builddir/build/BUILD/gnome-tour-43.0/vendor/glib-macros/Cargo.toml` has changed:
expected: d6e10d3ec19f19b5a32cdcd159567ede9fa1e59ac13f446f0a1e40f99e7e6c1b
actual: ea00aa6587f4f1793c296fd4a18c9989239e13df703c9254906b1c757714d440
directory sources are not intended to be edited, if modifications are required then it is recommended that `[patch]` is used with a forked copy of the source
```


`.cargo-checksum.json`

导致，在该 json 文件中找到 `Cargo.toml`

内容并修改为实际值即可。其余文件的校验错误同理。
```
# 将"Cargo.toml":"d6e10d3ec19f19b5a32cdcd159567ede9fa1e59ac13f446f0a1e40f99e7e6c1b"
# 修改为 "Cargo.toml":"ea00aa6587f4f1793c296fd4a18c9989239e13df703c9254906b1c757714d440"
```


### 5.2 Cargo.lock 指定版本不匹配

`Cargo.toml`

中描述对于版本的要求，`Cargo.lock`

为根据编译时环境自动生成。
譬如查看 gnome-tour-43.0 中的 `Cargo.toml`

文件，可知编译要求 gtk4 版本为 0.4.x。

```
[dependencies]
gtk = { package = "gtk4", version = "0.4", features= ["v4_2"]}
log = "0.4"
gettext-rs = { version = "0.7", features = ["gettext-system"] }
adw = {package = "libadwaita", version = "0.1"}
pretty_env_logger = "0.4"
regex = "1.5"
```


首次生成 `Cargo.lock`

时，编译源中提供 gtk4 版本为 0.4.8，故 `Cargo.lock`

中会锁定版本为 0.4.8。
当后续使用时，源中提供 gtk4 升级为 0.4.9，此时编译会报错：

```
error: failed to select a version for the requirement `gtk4 = "^0.4"` (locked to 0.4.8)
candidate versions found which didn't match: 0.4.9
```


参照 gnome-tour-43.0 中的 `Cargo.toml`

可知，gtk4-0.4.9 其实也满足编译要求，这个报错是不必要的，故需更新 `Cargo.lock`

文件消除该报错。
由于该文件为根据 `Cargo.toml`

自动生成，故一般情况下不建议手动修改 lock 文件，而是应该调整 toml 文件。

此时若 gnome-tour-43.0 的 vendor 目录下，若包含 gtk4 文件夹，则更新 `vendor/gtk4/Cargo.toml`

中 version 为 0.4.9。

```
[package]
edition = "2021"
rust-version = "1.56"
name = "gtk4"
version = "0.4.9"
```


然后在 gnome-tour-43.0 目录执行 `cargo update`

即可，此时会自动更新 `Cargo.lock`

信息：

```
cargo update
Updating gtk4 v0.4.8 -> v0.4.9
```


更新完毕后，即可正常编译。

## 6 附录

更多使用方法，请参照：

- Rust 官方文档：https://doc.rust-lang.org/book/title-page.html
- Cargo 官方文档：https://doc.rust-lang.org/cargo/
- Rustfmt 配置文档：https://rust-lang.github.io/rustfmt/?version=master&search=#
- rustup 官方文档：https://rust-lang.github.io/rustup/index.html