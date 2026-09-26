source: https://docs.opencloudos.org/en/OCS/Install_Guide/ocs-docker/

# OpenCloudOS 容器镜像使用指南

本指南介绍如何获取并使用 OpenCloudOS 提供的容器镜像资源，适用于开发、测试、生产等多种容器化部署场景。

## 1. 镜像类型概览

| 版本 | 镜像类型 | 提供形式 | 导入方式 | 说明 |
|---|---|---|---|---|
| ocs23 | mini | rootfs.tar | docker import | 极简系统，仅含 dnf 和 vi，可定制构建 |
| oc9 | 基础镜像（minimal、microdnf、init 等) | Docker Hub / tar.xz | docker pull / docker load -i | 多种小型化基础镜像，支持离线或在线使用 |
| oc9 | runtime 镜像（Java、Python、PHP 等） | Docker Hub | docker pull | 运行时环境镜像，适合快速部署应用 |

## 2. OpenCloudOS Stream 23（ocs23）

目前仅提供 mini 镜像，以 rootfs tar 包形式提供，适合自定义构建基础镜像。

### 下载地址

- https://mirrors.opencloudos.tech/opencloudos-stream/releases/23/images/x86_64/

示例文件：

- OpenCloudOS-Stream-23-20241104-mini-docker-x86_64.tar

### 导入镜像（使用 docker import）

```
docker import OpenCloudOS-Stream-23-20230301-x86_64-mini-docker.tar ocs23:latest
```


### 运行容器

```
docker run -it ocs23:latest /bin/bash
```


说明：该镜像为极简环境，仅包含 dnf 和 vi，建议进入后使用 dnf 安装所需工具。


## 3. OpenCloudOS 9（oc9）

OpenCloudOS Stream 9 提供多种基础镜像和 runtime 镜像，支持在线拉取或离线导入。

### 在线拉取镜像（Docker Hub）

Docker Hub 地址：

- https://hub.docker.com/u/opencloudos

拉取示例：

```
docker pull opencloudos/oc9-minimal:latest
docker pull opencloudos/oc9-microdnf:latest
docker pull opencloudos/oc9-init:latest
docker pull opencloudos/oc9-busybox:latest
docker pull opencloudos/opencloudos9-rt-java17
docker pull opencloudos/opencloudos9-rt-python3.11
docker pull opencloudos/opencloudos9-rt-dotnet7.0
docker pull opencloudos/opencloudos9-rt-php8.2
docker pull opencloudos/opencloudos9-rt-nodejs18
docker pull opencloudos/opencloudos9-rt-static
```


运行示例：

```
docker run -it opencloudos/oc9-minimal:latest
```


### 离线导入基础镜像（tar.xz 文件）

OpenCloudOS 提供通过 docker save 导出的 .tar.xz 镜像包，可用于离线环境。

下载地址：

- https://mirrors.opencloudos.tech/opencloudos/9/images/docker/x86_64/20250514.1/

示例文件：

- OpenCloudOS-Container-Minimal-9.4-20250514.1.x86_64.tar.xz

导入镜像（Docker 20.10+ 支持直接加载 .tar.xz）：

```
docker load -i OpenCloudOS-Container-Minimal-9.4-20250514.1.x86_64.tar.xz
```


运行容器（导入后镜像名称为 opencloudos-container-minimal-9.4-20250514.1.x86_64:latest）：

```
docker run -it opencloudos-container-minimal-9.4-20250514.1.x86_64:latest
```


### 基础镜像

OpenCloudOS 9 提供多种小型化基础镜像，覆盖从极简 busybox 到完整 systemd 支持等多个使用场景，满足用户对镜像大小、功能、可扩展性等方面的不同需求。

#### 可用基础镜像列表

| 镜像类型 | 镜像名称 | 镜像大小 | 镜像特点 |
|---|---|---|---|
基础镜像 |
opencloudos9-minimal | 约 150MB | 使用 dnf 作为包管理器，包含 coreutils 等常用 Linux 工具集。是功能完整的最小系统镜像，适合作为通用基础镜像使用。 |
| opencloudos9-microdnf | 约 100MB | 使用轻量级 microdnf 包管理器，体积更小。不支持 dnf 的插件、历史记录等高级功能，适合对镜像大小敏感且有包管理器需求的场景。 | |
| opencloudos9-init | 约 190MB | 在 minimal 基础上增加 systemd，默认以 systemd 为启动进程，支持 systemctl 管理服务，适用于需要在容器中运行多个服务的场景。 | |
| opencloudos9-busybox | 约 27MB | 极简镜像，无包管理器，使用 busybox 替代 coreutils，适合构建工具容器、健康检查探针等对体积要求极高的场景。 |

镜像来源：Docker Hub


镜像前缀：docker.io/opencloudos/

#### 基础镜像使用示例

*· opencloudos9-microdnf*

opencloudos9-microdnf 镜像使用 microdnf 作为包管理器，coreutils 作为 Linux 工具集，支持用户自行安装和构建其他镜像，microdnf 不依赖 python，因此容器体积极小。不依赖 python 以及对容器体积要求高的，优先考虑。

示例：以 opencloudos9-microdnf 镜像为基础镜像制作 C 程序的 builder 镜像

```
FROM opencloudos/opencloudos9-microdnf
RUN microdnf install -y gcc
CMD [ "/bin/bash" ]
```


*· opencloudos9-minimal*

opencloudos9-minimal 镜像使用 dnf/yum 作为包管理器，coreutils 作为 Linux 工具集，支持用户自行安装和构建其他镜像。

示例：以 opencloudos9-minimal 镜像为基础镜像制作 conda 支持软件多版本环境容器镜像

```
FROM opencloudos/opencloudos9-minimal
RUN yum install -y conda
CMD [ "/bin/bash" ]
```


*· opencloudos9-init*

opencloudos9-init 镜像以 systemd:/sbin/init 为1号进程，coreutils 作为 Linux 工具集，支持服务类型应用使用。镜像中为了安全考虑已经禁止登录以及 mount 特殊文件系统，并且以"37"(halt.target)作为容器stop信号。

示例：基于 opencloudos9-init 镜像部署 httpd 服务程序搭建 Web 网站

```
FROM opencloudos/opencloudos9-init
RUN dnf -y install httpd; dnf clean all; systemctl enable httpd;
RUN echo "Successful Web Server Test" > /var/www/html/index.html
RUN mkdir /etc/systemd/system/httpd.service.d/; echo -e '[Service]\nRestart=always' > /etc/systemd/system/httpd.service.d/httpd.conf
EXPOSE 80
CMD [ "/sbin/init" ]
```


**注意**，基于 init 镜像构建的镜像，运行时需要赋予特权模式才可运行，使用 docker 启动容器时需要增加 --privileged 参数，示例如下：

```
docker run -itd --privileged opencloudos9-init
```


*· opencloudos9-busybox*

opencloudos9-busybox 镜像以 busybox 作为精简 Linux 工具集，不支持包管理器，具有极小的容器体积以及 Linux 工具集的特点，满足业务对工具集和容器体积的要求。

示例：基于opencloudos9-busybox 镜像制作探测mysql服务器的容器

```
FROM opencloudos/opencloudos9-busybox
CMD ["sh", "-c", "until ping 192.168.90.14 -c 1 ; do echo waiting for mysql...; sleep 2; done;"]
```


### 应用 runtime 镜像

OpenCloudOS 9 提供多种轻量化的应用运行时（runtime）镜像，具备以下通用优势：

- ✅ 更小：只包含应用运行所需的最小依赖，不包含任何不必要的系统工具或库。需要 shell 调试时，可在 runtime 镜像上叠加基础镜像（如 opencloudos9-busybox）构建 debug 镜像。
- ✅ 更安全：镜像仅包含最小运行时环境，减少潜在攻击面，提升容器安全性。
- ✅ 更高效：运行时镜像只加载必要组件，启动时间短，运行效率高。

#### 可用 runtime 镜像列表

| 镜像名称 | 镜像大小 | 镜像特点 |
|---|---|---|
| opencloudos9-rt-java17 | 约 250MB | 基于 KonaJDK 构建，适用于部署 Java 17 应用，兼容性强，运行稳定。 |
| opencloudos9-rt-python3.11 | 约 50MB | 内置 Python 3.11 运行环境，适合运行脚本、微服务、AI 推理等场景。 |
| opencloudos9-rt-dotnet7.0 | 约 130MB | 支持 .NET 7.0，适合部署 ASP.NET Core 应用或 .NET CLI 工具。 |
| opencloudos9-rt-php8.2 | 约 60MB | 内置 PHP 8.2 运行环境，适合部署 Laravel、ThinkPHP 等 PHP Web 应用。 |
| opencloudos9-rt-nodejs18 | 约 80MB | 内置 Node.js 18，适合部署前端 SSR 服务、Node 后端应用等。 |
| opencloudos9-rt-static | 约 5MB | 极简静态运行时，适合部署静态编译的 Go、C 应用，包含基础配置、CA 证书等。 |

镜像来源：Docker Hub


镜像前缀：docker.io/opencloudos/

#### runtime 镜像使用示例

*· opencloudos9-rt-java17*

分两个阶段构建一个运行 java 程序的镜像,示例如下：

- build-venv： 设置编译 java 代码的构建环境，并将代码编译打包成 jar 包。
- 输出：复制 jar 包到 runtime 镜像中，构建最终镜像。

```
# build-venv
FROM opencloudos/opencloudos9-microdnf AS build-env
RUN microdnf install -y java-17-konajdk-devel
COPY . /app/examples
WORKDIR /app
RUN javac examples/*.java
RUN jar cfe main.jar examples.SSLCertificateTest examples/*.class
# final image
FROM opencloudos/opencloudos9-rt-java17
COPY --from=build-env /app /app
WORKDIR /app
CMD ["main.jar"]
```


*· opencloudos9-rt-python3.11*

没有第三方依赖的 python 应用，直接拷贝 py 代码文件到 runtime 镜像中，示例如下：


```
FROM opencloudos/opencloudos9-rt-python3.11
COPY . /app
WORKDIR /app
CMD ["hello.py"]
```


有第三方依赖的 python 应用，分三个阶段构建镜像，示例如下：

1. build： 创建可安装第三方依赖的 Python 虚拟环境，推荐使用 opencloudos9-microdnf 镜像安装 python3-virtualenv 来创建虚拟环境。

2. build-venv：在 Python 虚拟环境中使用 pip 安装 requirements.txt 中的依赖，后续 requirements.txt 变化时只需要重新构建这个阶段，而不用构建 build。

3. 输出：复制 venv 环境和代码到 runtime 镜像中，构建最终镜像。

```
# build
FROM opencloudos/opencloudos9-microdnf AS build
RUN microdnf install -y python3-virtualenv && \
python3 -m venv /venv
# build-venv
# 增加此构建阶段，后续 requirements.txt 变化时只需要重新构建这个阶段，而不用构建 build
FROM build AS build-venv
COPY requirements.txt /requirements.txt
RUN /venv/bin/pip install --disable-pip-version-check -r /requirements.txt
# final image
FROM opencloudos/opencloudos9-rt-python3.11
COPY --from=build-venv /venv /venv
COPY . /app
WORKDIR /app
# 需要修改入口点为虚拟环境中的 python 解释器
ENTRYPOINT ["/venv/bin/python3", "psutil_example.py"]
```


build 阶段推荐使用 python3-virtualenv 创建虚拟环境而不是 conda，原因是 python3-virtualenv 创建的虚拟环境会使用系统中的基础库并且拷贝系统的 python 解释器，从而节省空间，而 conda 创建的虚拟环境则会下载独立的基础库。

*· opencloudos9-rt-dotnet7.0*

分两个阶段构建镜像，示例如下：

1. build-venv： 设置编译 dotnet 代码的构建环境，复制项目文件和代码，编译项目并发布。

2. 输出：复制发布的应用到 runtime 镜像中，构建最终镜像。

```
# build-venv
FROM opencloudos/opencloudos9-microdnf AS build-env
RUN microdnf install -y dotnet-sdk-7.0
WORKDIR /app
# 将项目文件复制到工作目录，还原依赖
COPY *.csproj .
RUN dotnet restore
# 将源代码复制到工作目录，编译项目并发布
COPY . .
RUN dotnet publish -c Release -o out
# final image
FROM opencloudos/opencloudos9-rt-dotnet7.0
COPY --from=build-env /app/out /app/
WORKDIR /app
# 设置 dotnet 应用程序为入口点
ENTRYPOINT ["/app/HttpClient"]
```


*· opencloudos9-rt-static*

opencloudos9-rt-static 提供基础文件和目录结构、基本配置、时区信息和CA证书，可适用于静态编译的各类应用，如静态编译的 C 应用，不依赖 C 库的 go 应用等。

分两个阶段构建镜像，示例如下：

- build-venv： 设置可以安装 go 或 gcc 依赖的构建环境，复制代码到环境中进行静态编译。
- 输出：复制静态编译的二进制程序到 runtime 镜像中，构建最终镜像。

```
# build-venv
FROM opencloudos/opencloudos9-microdnf AS build-env
RUN microdnf install -y go
WORKDIR /go/src/app
COPY . .
RUN go mod download
RUN go vet -v
RUN go test -v
RUN CGO_ENABLED=0 go build -o /go/bin/app
# final image
FROM opencloudos/opencloudos9-rt-static
COPY --from=build-env /go/bin/app /
CMD ["/app"]
```


*· opencloudos9-rt-php8.2*

没有第三方依赖的 php 应用，直接拷贝 php 代码文件到 runtime 镜像中，示例如下：

```
FROM opencloudos-runtime/opencloudos9-rt-php8.2
COPY . /app
WORKDIR /app
CMD ["hello.php"]
```


- build-venv：设置 php composer 安装器所需环境，并使用 composer 下载依赖。
- 输出：复制依赖文件和代码到 runtime 镜像中，构建最终镜像。

```
# build-venv
FROM opencloudos/opencloudos9-microdnf AS build-env
RUN microdnf install -y php php-cli git
WORKDIR /app
COPY . .
# 安装 composer，并使用 composer 下载所需依赖
RUN curl -sS https://getcomposer.org/installer | php
RUN php composer.phar update && php composer.phar install
# final image
FROM opencloudos/opencloudos9-rt-php8.2
COPY --from=build-env /app /app
WORKDIR /app
CMD ["httpclient.php"]
```


*· opencloudos9-rt-nodejs18*

分两个阶段构建镜像，示例如下：

- build-venv： 设置可以安装 nodejs 依赖的构建环境，复制代码到环境中并使用 npm 命令安装依赖项。
- 输出：复制代码和依赖性到 runtime 镜像中，构建最终镜像。

```
# build-venv
FROM opencloudos/opencloudos9-microdnf AS build-env
RUN microdnf install -y nodejs
COPY . /app
WORKDIR /app
RUN npm ci --omit=dev
# final image
FROM opencloudos/opencloudos9-rt-nodejs18
COPY --from=build-env /app /app
WORKDIR /app
CMD ["httpclient.js"]
```


#### 使用同基础镜像调试 runtime 镜像

应用 runtime 镜像与基础镜像会一起发布，因此可以叠加相同 tag 的基础镜像来作为debug镜像。

叠加方法为在应用镜像 Dockfile 的头部添加 FROM 基础镜像，然后将基础镜像的文件复制到应用镜像中。示例如下：

```
FROM opencloudos/opencloudos9-microdnf AS debug
# 应用镜像构建相关内容
....
....
....
# 复制基础镜像的文件复制到应用镜像
COPY --from=debug / /
```


**注意**：为防止与应用镜像设置的应用运行相关的 CMD 或者 ENTPOINT 冲突，debug 镜像不能重新设置 CMD 或者 ENTPOINT。进入 debug 镜像启动的容器时需要手动添加诸如 "/bin/bash" 的 command。

#### 应用 runtime 镜像设置 nonroot 用户

应用 runtime 镜像提供 root、nobody、nonroot 用户及用户组，对应用户配置如下：

/etc/passwd:


```
root:x:0:0:root:/root:/sbin/nologin
nobody:x:65534:65534:nobody:/nonexistent:/sbin/nologin
nonroot:x:65532:65532:nonroot:/home/nonroot:/sbin/nologin
```


```
root:x:0:
nobody:x:65534:
nonroot:x:65532:
```


```
FROM opencloudos/opencloudos9-microdnf AS build-env
RUN microdnf install -y nodejs
COPY . /app
WORKDIR /app
RUN npm ci --omit=dev
FROM opencloudos/opencloudos9-rt-nodejs
# 设置运行用户为 nonroot
USER nonroot
# 拷贝 app 目录到 runtime 镜像 /home/nonroot ，并设置 app 目录所属用户及用户组为 nonroot
COPY --from=build-env --chown=nonroot:nonroot /app /home/nonroot/app
WORKDIR /home/nonroot/app
CMD ["httpclient.js"]
```


## 4. 注意事项

Docker 版本需要高于 **20.10.9** 版本。