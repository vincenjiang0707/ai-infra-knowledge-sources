source: https://docs.opencloudos.org/OCS/DevelopGuide/GO_guide/

# Go 使用指南

# 1 Go 简介

Go 语言（Golang）是谷歌推出的一种编译型、静态类型、并发级别高、垃圾回收的开源编程语言。其简洁、性能高效、并发支持强大，广泛应用于云计算、Web 开发和网络编程。

# 2 Go 安装

## 2.1 dnf 安装

用户可以直接通过如下命令安装系统提供的 golang 包，基于此进行 Go 开发

```
dnf install -y golang
```


安装完成后可通过如下命令确认安装版本

```
go version
go version go1.19 linux/amd64
```


## 2.2 自定义安装

如果用户想自定义安装，可以参考如下步骤使用官网提供的二进制文件

1 下载官方二进制，本例使用的是与 2.1 小节相同的版本，用户也可以按需选择

```
wget https://go.dev/dl/go1.19.linux-amd64.tar.gz
sha256sum go1.19.linux-amd64.tar.gz
```


```
mkdir -p /usr/local/my_go/
tar -C /usr/local/my_go/ -xzf go1.19.linux-amd64.tar.gz
```


`PATH`

环境变量中
```
echo "export PATH=$PATH:/usr/local/my_go/go/bin" >> ~/.bashrc
source ~/.bashrc
```


```
go version
go version go1.19 linux/amd64
```


# 3 Go 使用

## 3.1 直接运行 Go

Go 程序可以直接通过 `go run`

命令运行，如下demo所示：

```
cat hello.go
package main
import "fmt"
func main() {
fmt.Println("Hello, OpenCloudOS!")
}
```


用户可以直接运行此代码

```
go run hello.go
Hello, OpenCloudOS!
```


## 3.2 创建 Go 项目

对于涉及依赖关系的复杂 Go 代码，可用通过创建一个 Go 项目来开发

假设用户的项目目录为 `$HOME/go`

，则通过如下命令创建项目目录

```
mkdir -p $HOME/go/{src,bin,pkg}
```


其中：

`src`

：包含源代码文件的目录`bin`

：包含可执行文件的目录`pkg`

：包含编译后的包依赖的对象文件的目录

设置环境变量

```
export GOPATH=$HOME/go
```


初始化一个新的 Go 项目，创建一个名为 `my_project`

的项目，用于随机生成人名。创建该项目并切换到该项目目录下：

```
mkdir -p ${GOPATH}/src/my_project
cd ${GOPATH}/src/my_project
```


创建一个名为 `main.go`

的文件，添加以下代码：

```
package main
import (
"fmt"
"github.com/Pallinder/go-randomdata"
)
func main() {
for i := 1; i <= 5; i++ {
randomName := randomdata.FirstName(randomdata.RandomGender) + " " + randomdata.LastName()
fmt.Printf("Person %d: %s\n", i, randomName)
}
}
```


初始化 Go module 并安装依赖：

```
go mod init example.com/my_project
go mod tidy
```


编译项目

```
go build
```


使用 `go install`

命令安装可执行文件

```
go install
```


此时 `bin`

目录下将生成一个名为 `my_project`

的可执行文件，可以直接运行

```
$HOME/go/bin/my_project
Person 1: Sofia Martin
Person 2: Emily Anderson
Person 3: Elizabeth Taylor
Person 4: Emma Miller
Person 5: Isabella Smith
```


此时，一个完整的 Go 项目目录树如下：

```
cd ~/go
tree -L 3
.
├── bin
│ └── my_project
├── pkg
│ ├── mod
│ │ ├── cache
│ │ ├── github.com
│ │ └── golang.org
│ └── sumdb
│ └── sum.golang.org
└── src
└── my_project
├── go.mod
├── go.sum
└── main.go
```


## 3.3 调测功能

### 3.3.1 `fmt.Println`


在开发阶段，打印变量值和程序中某些点的执行状态是最简单且常见的调试方法。可以使用 Go 的 `fmt.Println()`

在程序中输出调试信息

`Println`

这个名字是由 "Print" 和 "ln"（换行）两部分组成，表示在打印完成后会自动添加一个换行符

用户可以将任意数量和类型的参数传递给 `fmt.Println`

，输出时，参数间使用空格进行分隔。示例如下：

```
fmt.Println("Hello, OpenCloudOS!")
fmt.Println("The value is:", 42)
fmt.Println("Name:", "John", "Age:", 30)
```


`fmt.Println`

函数用于打印值，但不支持格式化字符串输出。要进行字符串输出，请使用 `fmt.Printf`

（或 `fmt.Sprintf`

）函数。这些函数提供更多的格式化选项，如占位符（`%d`

、`%f`

、`%s`

等），和输出控制功能（如字段宽度、精度和填充字符等）。

### 3.3.2 `debug.PrintStack()`


`debug.PrintStack()`

函数可以将当前程序的堆栈以文本形式抛出到标准错误输出，要使用此工具，需要适当修改代码

首先，需要导入 `runtime/debug`


```
import (
...
"runtime/debug"
...
)
```


然后在需要打印调用栈的地方加入如下代码：

```
...
debug.PrintStack()
...
```


运行修改后的代码即可打出调用栈。

### 3.3.3 pprof

pprof 是用于 Go 的可视化调测工具，侧重于性能数据的分析，要使用此工具，需要适当修改代码

首先，需要导入 pprof 包

```
import (
...
"runtime/pprof"
...
)
```


接下来，需要创建 pprof 文件，如：

```
f, err := os.Create("cpu.pprof")
```


然后，调用了 `pprof.StartCPUProfile()`

函数来开始记录 CPU 配置文件

```
pprof.StartCPUProfile(f)
```


在执行程序一段时间后，使用 `pprof.StopCPUProfile()`

函数停止记录 CPU 配置文件

```
defer pprof.StopCPUProfile()
```


如此设置后，执行完程序会生成 `cpu.pprof`

这个文件，使用如下命令即可进入交互界面进行详细分析

```
go tool pprof cpu.pprof
File: main
Type: cpu
Time: May 29, 2023 at 7:17pm (CST)
Duration: 609.33ms, Total samples = 440ms (72.21%)
Entering interactive mode (type "help" for commands, "o" for options)
(pprof) top
Showing nodes accounting for 440ms, 100% of 440ms total
flat flat% sum% cum cum%
440ms 100% 100% 440ms 100% main.fibonacci
0 0% 100% 440ms 100% main.main
0 0% 100% 440ms 100% runtime.main
```


# 4 Go 包管理

除了使用系统提供的 `dnf`

命令管理 Go 相关的包，用户也可以使用 Go 提供的 Go Modules 包管理系统，用于处理项目及其依赖项

## 4.1 初始化 Go Modules

要在项目中启用 Go Modules，请在项目根目录下执行以下命令。此命令将创建一个名为 `go.mod`

的文件，其中包含项目的模块名称和当前 Go 版本

```
go mod init <module-path>
```


例如上文中创建项目用到的命令

```
go mod init example.com/my_project
cat go.mod
module example.com/my_project
go 1.19
```


## 4.2 安装和更新依赖项

要添加或更新依赖项，请使用以下命令。这将下载缺失的依赖项并更新 `go.mod`

和 `go.sum`

文件。

```
go mod tidy
```


上文中的例子执行完上述命令后，会在 `go.mod`

文件中新增依赖的包

```
cat go.mod
module example.com/my_project
go 1.19
require github.com/Pallinder/go-randomdata v1.2.0
require golang.org/x/text v0.9.0 // indirect
```


若要获取特定版本的依赖项，请使用以下命令。此命令将更新 `go.mod`

文件，并获取请求的版本。

```
go get <dependency_path>@<version>
```


如想使用 v1.1.0 版本的 go-randomdata

```
go get github.com/Pallinder/go-randomdata@v1.1.0
cat go.mod
module example.com/my_project
go 1.19
require github.com/Pallinder/go-randomdata v1.1.0
require golang.org/x/text v0.9.0 // indirect
```


此时 `go.mod`

文件被更新

另外，也可以使用特定的 git commit，如：

```
go get github.com/Pallinder/go-randomdata@3e0fbf126b9e6853a5e50951913caab476d650c7
go: downloading github.com/Pallinder/go-randomdata v0.0.0-20181031200937-3e0fbf126b9e
go: downgraded github.com/Pallinder/go-randomdata v1.2.0 => v0.0.0-20181031200937-3e0fbf126b9e
cat go.mod
module example.com/my_project
go 1.19
require github.com/Pallinder/go-randomdata v0.0.0-20181031200937-3e0fbf126b9e
require golang.org/x/text v0.9.0 // indirect
```


## 4.3 查看当前依赖项及其详情

要查看当前项目的所有依赖项的信息以及可更新版本，可以运行以下命令：

```
go list -u -m all
example.com/my_project
github.com/Pallinder/go-randomdata v0.0.0-20181031200937-3e0fbf126b9e [v1.2.0]
golang.org/x/mod v0.8.0 [v0.10.0]
golang.org/x/sys v0.5.0 [v0.8.0]
golang.org/x/text v0.9.0
golang.org/x/tools v0.6.0 [v0.9.1]
```


## 4.4 移除不再使用的依赖项

要移除不再使用的依赖项，首先需要在源代码中注释的不再使用的依赖包：

```
import (
...
// "github.com/Pallinder/go-randomdata"
...
)
```


然后执行如下命令

```
go mod tidy
```


这时已查不到删去的依赖项

```
go list -u -m all
example.com/my_project
```


# 5 Go 工具介绍

## 5.1 go fmt

go fmt 用来自动格式化 Go 源代码文件，以确保代码风格一致，并符合官方编码规范。

比如，创建一个名为 `example.go`

的文件，其内容如下，但代码排列和缩进不规范：

```
package main
import "fmt"
func main() {
fmt.Println("Hello, world!")
list:=[]int{9,7,5,3}
for i, val := range list {
fmt.Printf("Index: %d, Value: %d\n",i,val)
}
}
```


执行如下命令：

```
go fmt example.go
```


执行后代码便实现了规范化：

```
cat example.go
package main
import "fmt"
func main() {
fmt.Println("Hello, world!")
list := []int{9, 7, 5, 3}
for i, val := range list {
fmt.Printf("Index: %d, Value: %d\n", i, val)
}
}
```


## 5.2 go vet

go vet 用来静态检查 Go 源代码中的潜在错误或可疑编码模式。

创建一个名为 `example.go`

的文件，其中有一个错误：在 `Printf`

的占位符和参数之间有一个不匹配：

```
package main
import "fmt"
type Person struct {
FirstName string
LastName string
Age int
}
func main() {
p := Person{
FirstName: "John",
LastName: "Doe",
Age: 30,
}
fmt.Printf("Person: %s %s, age %d, and an extra parameter: %s\n", p.FirstName, p.LastName, p.Age)
}
```


执行此命令后，`go vet`

将报告以下错误：

```
go vet example.go
# command-line-arguments
./example.go:18:2: fmt.Printf format %s reads arg #4, but call has 3 args
```


工具指明了文件 `example.go`

的第 18 行具有额外的参数，但没有相应的格式化指令。

除了对单个文件进行检查之外，要检查包括子目录在内的整个项目中的所有 Go 代码文件，可以在项目的根目录下运行 `go vet`

：

```
go vet ./...
```


## 5.3 go doc

`go doc`

命令从 Go 源代码中提取包、类型、函数和方法的文档注释，并将其以易读的纯文本格式输出到终端。

例如，创建一个名为 `stringutil.go`

的简单字符串处理库，如下：

```
// Package stringutil contains utility functions for manipulating strings.
package stringutil
// Reverse returns a reversed copy of the input string s.
func Reverse(s string) string {
r := []rune(s)
for i, j := 0, len(r)-1; i < len(r)/2; i, j = i+1, j-1 {
r[i], r[j] = r[j], r[i]
}
return string(r)
}
```


导入并使用自定义的 stringutil 包

```
go mod init example.com/stringutil
go mod tidy
```


完成上述配置后，就可以输出包的描述

```
go doc example.com/stringutil
package stringutil // import "example.com/stringutil"
Package stringutil contains utility functions for manipulating strings.
func Reverse(s string) string
```


也可以查询函数的描述

```
go doc example.com/stringutil.Reverse
package stringutil // import "example.com/stringutil"
func Reverse(s string) string
Reverse returns a reversed copy of the input string s.
```