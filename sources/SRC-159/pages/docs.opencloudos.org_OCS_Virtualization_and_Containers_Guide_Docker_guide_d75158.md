source: https://docs.opencloudos.org/OCS/Virtualization_and_Containers_Guide/Docker_guide/

# 1. 基础介绍

容器技术是一种虚拟化技术，它可以将应用程序及其依赖项打包到一个独立的运行环境中，以便于在不同的计算机上运行。容器技术可以提供更高的资源利用率、更快的应用程序启动时间和更好的可移植性。

容器技术主要由以下组成部分组成：

- 容器镜像：容器镜像是一个只读的文件系统，包含了应用程序及其依赖项和运行时环境等。
- 容器运行时：容器运行时是一个负责启动和管理容器的软件，可以提供容器隔离、容器网络和容器存储等功能。
- 容器编排工具：容器编排工具是一个负责管理多个容器的软件，可以提供容器自动化部署、容器扩展和容器负载均衡等功能。

# 2. 安装容器

目前系统已支持docker engine，可通过如下命令安装

```
# dnf install docker
或
# dnf install moby
```


docker 是 moby 提供的能力，因此安装 moby 包即可

安装完成后通过以下命令启动docker服务：

```
# systemctl start docker
```


另外，也通过 EPOL 源的形式提供了 podman，EPOL 源默认使能，用户可按需安装，命令如下：

```
# dnf install podman
```


# 3. 配置容器

通常情况下，通过daemon.json文件来配置docker守护进程。Docker守护进程是Docker的核心组件，负责管理Docker容器、镜像、网络等资源，以及提供Docker API接口供其他程序调用。在Docker守护进程启动时，会读取daemon.json文件中的配置信息，并根据配置信息来初始化Docker守护进程。通过修改daemon.json文件中的配置信息，可以改变Docker守护进程的行为，例如配置镜像加速器、设置日志级别、配置存储驱动等。

常用参数如下：

- registry-mirrors

作用：配置Docker镜像加速器地址，加速镜像下载速度。

示例：

```
"registry-mirrors": ["https://mirror.ccs.tencentyun.com"]
```


- log-driver

作用：配置Docker容器的日志驱动，用于将容器的日志输出到文件或者标准输出中。 配置这个参数时，需要先删除/etc/sysconfig/docker配置内的--log-driver=journald，否则会因为冲突报错。 示例：

```
"log-driver": "json-file"
```


- log-opts

作用：配置Docker容器的日志选项，例如日志文件的最大大小、最多保留的日志文件数等。

示例：

```
"log-opts": {
"max-size": "10m",
"max-file": "3"
}
```


- storage-driver

作用：配置Docker容器的存储驱动，用于管理容器的文件系统。

示例：

```
"storage-driver": "overlay2"
```


- bip

作用：配置Docker网桥的IP地址，用于容器之间的通信。

示例：

```
"bip": "172.16.0.1/24"
```


- fixed-cidr

作用：配置Docker网桥的子网地址，用于容器之间的通信。

示例：

```
"fixed-cidr": "172.16.0.0/24"
```


- mtu

作用：配置Docker网桥的MTU值，用于容器之间的通信。

示例：

```
"mtu": 1500
```


- live-restore

作用：配置Docker是否启用容器的实时恢复功能，用于在Docker守护进程崩溃或重启时自动恢复容器。

示例：

```
"live-restore": true
```


- default-ulimits

作用：配置Docker容器的默认资源限制，例如CPU、内存、文件描述符等。

示例：

```
"default-ulimits": {
"nofile": {
"Name": "nofile",
"Hard": 65536,
"Soft": 65536
}
}
```


完整示例

```
# cat /etc/docker/daemon.json
{
"registry-mirrors": ["https://mirror.ccs.tencentyun.com"],
"log-driver": "json-file",
"log-opts": {
"max-size": "10m",
"max-file": "3"
},
"storage-driver": "overlay2"
}
```


配置文件编辑完成后，可以使用以下命令重启Docker服务使配置生效：

```
# systemctl restart docker
```


# 4. 容器管理

## 4.1 启停容器

### 4.1.1 直接运行一个容器

以拉起一个busybox镜像为例，执行如下命令，从docker官方的镜像库中下载最新的busybox镜像

```
# docker pull busybox
```


用户可以直接通过 `docker run`

命令运行一个容器，如下：

```
# docker run busybox /bin/echo "Hello world"
Hello world
```


其中 busybox 为镜像名，`/bin/echo "Hello world"`

即容器执行的命令

### 4.1.2 创建交互式容器

此外，用户可以使用 `-it`

选项来创建一个交互式的容器，在交互界面执行命令，如下

```
# docker run -it busybox /bin/sh
```


执行后，即可进入交互界面

```
/ #
/ # ls
bin dev etc home lib lib64 proc root sys tmp usr var
/ # echo "Hello world"
Hello world
```


### 4.1.3 后台运行容器

用户可以通过 `-d`

选项在后台运行容器，命令如下：

```
# docker run -d --name=my_container busybox /bin/sh -c "while true;do echo Hello world;sleep 1;done"
```


### 4.1.4 结束容器

停止容器

```
# docker stop 3586b3a12366
```


或者是kill掉容器

```
# docker kill 3586b3a12366
```


删除容器

```
# docker rm 3586b3a12366
```


## 4.2 容器信息查询

Docker提供了多种查询相关的命令，可以用于查询Docker容器、镜像、网络等信息。以下是一些常用的Docker查询命令及其作用：

- docker ps

用于列出当前正在运行的Docker容器, 查看容器的名称、ID、状态、端口映射等信息。

```
# docker ps
CONTAINER ID IMAGE COMMAND CREATED STATUS PORTS NAMES
cb3435ac0f78 busybox "/bin/sh -c 'while t…" 7 seconds ago Up 5 seconds my_container
```


- docker logs

用于查看Docker容器的日志信息。

```
# # docker logs cb3435ac0f78
Hello world
Hello world
...
Hello world
```


- docker network ls

查看网络的名称、ID、驱动程序等信息。

```
# docker network ls
NETWORK ID NAME DRIVER SCOPE
4500f433c4e2 bridge bridge local
30217a81dce2 host host local
020a952b0758 none null local
```


- docker volume ls

查看卷的名称、驱动程序、挂载点等信息。

```
# docker volume ls
```


- docker stats

查看容器的CPU、内存、网络、磁盘等资源使用情况。

```
# docker stats
CONTAINER ID NAME CPU % MEM USAGE / LIMIT MEM % NET I/O BLOCK I/O PIDS
cb3435ac0f78 my_container 0.00% 496KiB / 3.552GiB 0.01% 1.97kB / 0B 0B / 0B 1
```


## 4.3 容器修改

docker提供了多种命令，用于修改Docker容器：

- 修改容器配置

使用 `docker update`

命令可以修改容器的配置，例如修改容器的CPU和内存限制、添加或删除容器的网络配置等。例如，以下命令可以将容器的CPU限制设置为1个核心：

```
# docker update --cpus 1 <container_name>
```


- 修改容器文件系统

使用 `docker cp`

命令可以将文件复制到容器中，从而修改容器的文件系统。例如，以下命令可以将本地的文件复制到容器的/tmp目录中：

```
# docker cp <local_file> <container_name>:/tmp/
```


- 修改镜像标签

使用 `docker tag`

命令可以为镜像添加或修改标签。例如，以下命令可以将镜像的标签修改为latest：

```
# docker tag <image_name>:<old_tag> <image_name>:latest
```


- 修改镜像元数据

使用 `docker commit`

命令可以修改镜像的元数据，例如修改镜像的作者、描述等。例如，以下命令可以为镜像添加作者信息：

```
# docker commit --author "John Doe" <container_name> <new_image_name>
```


- 修改Docker配置

使用 `docker config`

命令可以修改Docker的配置，例如修改Docker的日志级别、修改Docker的存储驱动等。例如，以下命令可以修改Docker的日志级别为debug：

```
# docker config set log-level debug
```


# 5. rootless容器

在docker中可以使用rootless模式运行docker deamon和容器，在该模式下不需要root权限。docker在20.10版本之后正式支持该模式。rootless模式利用user namespace将容器的root用户与docker守护进程用户映射到宿主机的非特权用户范围内，这样就提升了容器的安全隔离性。

## 5.1 环境准备

假设容器环境已经配置完全，为运行rootless容器，还需安装以下组件

```
# dnf install -y shadow-utils fuse-overlayfs iptables
```


```
# wget https://download.docker.com/linux/static/stable/x86_64/docker-rootless-extras-20.10.21.tgz
# tar -xf docker-rootless-extras-20.10.21.tgz
# cd docker-rootless-extras && cp ./* /usr/bin/.
```


```
# useradd rootlesstest
# loginctl enable-linger rootlesstest
```


```
# cat /etc/subuid
rootlesstest:231072:65536
# cat /etc/subgid
rootlesstest:231072:65536
```


## 5.2 运行rootless dockerd守护进程和rootless容器

启动容器deamon

```
# dockerd-rootless-setuptool.sh install
# ps -ef | grep dockerd
rootles+ 1737 1630 0 20:16 ? 00:00:00 rootlesskit --net=vpnkit --mtu=1500 --slirp4netns-sandbox=auto --slirp4netns-seccomp=auto --disable-host-loopback --port-driver=builtin --copy-up=/etc --copy-up=/run --propagation=rslave /usr/bin/dockerd-rootless.sh
rootles+ 1745 1737 0 20:16 ? 00:00:00 /proc/self/exe --net=vpnkit --mtu=1500 --slirp4netns-sandbox=auto --slirp4netns-seccomp=auto --disable-host-loopback --port-driver=builtin --copy-up=/etc --copy-up=/run --propagation=rslave /usr/bin/dockerd-rootless.sh
rootles+ 1777 1745 0 20:16 ? 00:00:00 dockerd
rootles+ 1799 1777 0 20:16 ? 00:00:00 containerd --config /run/user/1002/docker/containerd/containerd.toml --log-level info
```


```
# docker pull busybox
# docker run -tid busybox sh
b371390eaeaf45677ddb6de17c54df9f78fba0d513f715fb50f0c7edb80cc89e
# docker inspect -f "{{.State.Pid}}" b371390ea
2376
# ps -ef | grep 2376
rootles+ 2376 2353 0 21:06 pts/0 00:00:00 sh
# docker exec b371390ea sh -c "whoami"
root
```


# 6. 镜像管理

在Docker中，镜像是一种轻量级、可移植的打包格式，用于存储和传输Docker容器的文件系统和应用程序。镜像包含了一个完整的文件系统，包括操作系统、应用程序、库文件、配置文件等，以及一些元数据，例如镜像的名称、标签、版本号等。

## 6.1 镜像操作命令

Docker提供了多种命令，用于管理Docker镜像，包括增加、删除、修改和查询等操作。以下是一些常用的Docker镜像管理命令及其功能：

- docker images

docker images命令用于列出本地的Docker镜像。使用docker images命令可以查看镜像的名称、标签、大小等信息。

```
# docker images
REPOSITORY TAG IMAGE ID CREATED SIZE
busybox latest 7cfbbec8963d 7 weeks ago 4.86MB
```


- docker pull

docker pull命令用于从Docker镜像仓库中拉取一个新的Docker镜像。使用docker pull命令可以指定镜像的名称、标签等参数。

- docker push

docker push命令用于将一个本地的Docker镜像推送到Docker镜像仓库中。以下是其使用场景：

首先，需要在 Docker Hub 或其他 Docker 镜像仓库中创建一个新的仓库，用于存储 Docker 镜像。假设用户已创建了一个名为 mywork 的账户，并在账户中创建了一个 myimage 的仓库。

接下来，需要使用 docker tag 命令为本地的 Docker 镜像添加标签，以便将其推送到 Docker 镜像仓库中，格式如下：

```
# docker tag <image_name>:<tag> mywork/<image_name>:<tag>
```


其中，`<tag>`

是本地的Docker镜像标签。

例如，以下命令可以为本地的Docker镜像添加 myrepo 的标签：

```
# docker tag busybox mywork/myimage:1.0
```


然后，需要使用docker login命令登录到Docker镜像仓库中。例如，以下命令可以登录到Docker Hub中：

```
# docker login
```


最后，使用docker push命令将本地的Docker镜像推送到Docker镜像仓库中。例如，以下命令可以将本地的Docker镜像推送到 mywork 仓库中：

```
# docker push mywork/myimage:1.0
```


- docker build

docker build命令用于从Dockerfile构建一个新的Docker镜像。使用docker build命令可以指定Dockerfile的路径、镜像的名称、标签等参数。

- docker tag

docker tag命令用于为一个本地的Docker镜像添加或修改标签。使用docker tag命令可以指定镜像的名称、标签等参数。

- docker rmi

docker rmi命令用于删除一个本地的Docker镜像。使用docker rmi命令可以删除镜像的文件系统、元数据等资源。

- docker inspect

docker inspect命令用于查看Docker镜像的详细信息。使用docker inspect命令可以查看镜像的元数据、配置、状态等信息。

- docker history

docker history命令用于查看Docker镜像的历史记录。使用docker history命令可以查看镜像的每一层的构建信息、大小等信息。

```
# docker history 7cfbbec8963d
IMAGE CREATED CREATED BY SIZE COMMENT
7cfbbec8963d 7 weeks ago /bin/sh -c #(nop) CMD ["sh"] 0B
<missing> 7 weeks ago /bin/sh -c #(nop) ADD file:27beb116a0bcfe544… 4.86MB
```


## 6.2 Dockerfile配置

Docker镜像构建是指通过Dockerfile文件定义Docker镜像的构建过程和配置信息，然后使用docker build命令将Dockerfile文件构建成一个Docker镜像。Dockerfile文件是Docker镜像构建的核心文件，用于定义Docker镜像的构建过程和配置信息。Dockerfile文件是一个文本文件，其中包含了一系列的指令和参数，用于指定Docker镜像的构建过程和配置信息。

以下是Docker镜像构建的基本流程：

- 编写Dockerfile文件

以下为一个示例：

```
# 使用腾讯云镜像源
FROM ccr.ccs.tencentyun.com/library/opencloudos:latest
# 安装必要的软件包
RUN yum update -y && \
yum install -y nginx
# 复制配置文件
COPY nginx.conf /etc/nginx/nginx.conf
# 暴露端口
EXPOSE 80
# 启动Nginx服务
CMD ["nginx", "-g", "daemon off;"]
```


- 构建Docker镜像

使用docker build命令构建Docker镜像。在构建Docker镜像时，Docker会根据Dockerfile文件中的指令和参数，自动执行一系列的操作，包括下载基础镜像、安装软件包、配置环境变量、添加文件等操作，最终生成一个完整的Docker镜像。

以下是一个示例docker build命令：

```
# docker build -t myimage:latest .
```


在这个命令中，-t参数指定了镜像的名称为myimage，:latest表示使用最新版本的标签，.表示Dockerfile文件所在的目录。

- 上传Docker镜像

使用docker push命令将Docker镜像上传到Docker Hub或者其他的Docker镜像仓库中，以便其他人可以使用该镜像。

以下是一个示例docker push命令：

```
# docker push myimage:latest
```


在这个命令中，myimage:latest是要上传的镜像名称。

# 7. 维护

## 7.1 容器的备份和恢复

在Docker中，容器的备份和恢复是非常重要的操作，可以快速地恢复容器的状态，避免数据丢失和应用程序中断。

- 备份容器

要备份一个Docker容器，可以使用docker export命令将容器导出为一个tar文件。以下是备份容器的命令：

```
# docker export <container_name> > <backup_file>.tar
```


其中，

- 恢复容器

要恢复一个Docker容器，可以使用docker import命令将备份文件导入为一个新的Docker镜像。然后使用docker run命令启动一个新的容器。以下是恢复容器的命令：

```
# docker import <backup_file>.tar <new_image_name>:<tag>
# docker run -it --name <new_container_name> <new_image_name>:<tag>
```


其中，`<tag>`

是新的Docker镜像标签，

需要注意的是，恢复容器时需要先将备份文件导入为一个新的Docker镜像，然后再使用docker run命令启动一个新的容器。

## 7.2 容器的监控和日志管理

在Docker中，容器的监控和日志管理是非常重要的操作，可以实时监控容器的状态，及时发现和解决问题。以下一些基础的维测命令：

- 监控容器

要监控一个Docker容器，可以使用docker stats命令查看容器的实时资源使用情况。以下是监控容器的命令：

```
# docker stats <container_name>
```


其中，

- 查看容器日志

要查看一个Docker容器的日志，可以使用docker logs命令查看容器的标准输出和标准错误输出。以下是查看容器日志的命令：

```
# docker logs <container_name>
```


其中，

- 导出容器日志

要导出一个Docker容器的日志，可以使用docker cp命令将容器的日志文件复制到本地文件系统中。以下是导出容器日志的命令：

```
# docker cp <container_name>:/var/log/<log_file> <local_path>
```


其中，

## 7.3 容器安全和权限管理

在Docker中，容器的安全和权限管理是非常重要的操作，可以保护容器和应用程序的安全性。以下是一个使用场景示例：

- 创建用户组

要创建一个Docker容器的用户组，可以使用groupadd命令创建一个新的用户组。以下是创建用户组的命令：

```
# groupadd <group_name>
```


其中，

- 创建用户

要创建一个Docker容器的用户，可以使用useradd命令创建一个新的用户，并将其添加到用户组中。以下是创建用户的命令：

```
# useradd -g <group_name> <user_name>
```


其中，

- 启动容器时指定用户

要在启动一个Docker容器时指定用户，可以使用--user选项指定容器的用户和用户组。以下是启动容器时指定用户的命令：

```
# docker run -it --user <user_name>:<group_name> <image_name> --cap-add <capabilities> --cap-drop <capabilities>
```


其中，`<capabilities>`

指用来控制容器权限的能力集。

默认情况 Docker 容器内的进程将以 root 用户运行的，因此指定用户可以提高容器安全性。

关于能力集可以使用如下命令查询

```
# man capabilities
```


以下是一些常见的capabilities及其作用：

```
CAP_CHOWN
允许进程修改任意文件的所有者和组。
CAP_DAC_OVERRIDE
允许进程忽略文件的DAC（Discretionary Access Control）权限，即忽略文件的所有者和组权限。
CAP_DAC_READ_SEARCH
允许进程读取任意文件和目录，即使该文件或目录的权限不允许读取。
CAP_FOWNER
允许进程修改任意文件的所有者。
CAP_NET_RAW
允许进程使用原始套接字，即可以发送和接收任意类型的网络数据包。
CAP_NET_ADMIN
允许进程进行网络管理操作，例如配置网络接口、修改路由表等。
CAP_SYS_ADMIN
允许进程进行系统管理操作，例如挂载文件系统、修改系统时间等。
CAP_SYS_CHROOT
允许进程使用chroot系统调用，即将进程的根目录切换到指定的目录。
CAP_SYS_PTRACE
允许进程使用ptrace系统调用，即可以跟踪和修改其他进程的执行状态。
CAP_SYS_RESOURCE
允许进程修改系统资源限制，例如进程的CPU时间、内存使用量等。
```


## 7.4 容器配置健康检查

目前原生的容器已经支持健康检查的功能，需要用户通过编写 Dockerfile 文件进行设置，本文提供了将分布举例说明

1、编写Dockerfile文件

编写一个Dockerfile文件，用于构建一个包含健康检查脚本的镜像。以下是一个示例Dockerfile文件：

```
FROM ccr.ccs.tencentyun.com/library/opencloudos:latest
COPY healthcheck.sh /usr/local/bin/
RUN chmod +x /usr/local/bin/healthcheck.sh
HEALTHCHECK --interval=5s --timeout=3s \
CMD /usr/local/bin/healthcheck.sh || exit 1
```


在这个Dockerfile文件中，使用COPY指令将健康检查脚本healthcheck.sh复制到镜像中，并使用RUN指令给脚本添加可执行权限。

最后使用HEALTHCHECK指令定义了一个健康检查命令，该命令会每5秒执行一次，超时时间为3秒，如果脚本返回非0状态码，则认为容器不健康。

2、编写健康检查脚本

接下来，需要编写一个健康检查脚本，用于检查容器的健康状态。以下是一个示例健康检查脚本：

```
#!/bin/bash
if curl -s http://localhost:8080/healthcheck | grep -q "OK"; then
exit 0
else
exit 1
fi
```


在这个健康检查脚本中，使用curl命令访问容器中的一个健康检查接口，如果接口返回的内容包含OK，则认为容器健康，否则认为容器不健康。

3、构建镜像

使用以下命令构建镜像：

```
# docker build -t myimage:latest ./Dockerfile
```


在这个命令中，-t参数指定了镜像的名称为myimage，:latest表示使用最新版本的标签。

4、启动容器

使用以下命令启动容器：

```
# docker run -d --name mycontainer -p 8080:8080 myimage:latest
```


在这个命令中，-d参数表示以后台模式启动容器，--name参数指定容器的名称为mycontainer，-p参数指定容器的端口映射，myimage:latest表示使用myimage镜像的最新版本启动容器。

5、检查容器健康状态

使用以下命令检查容器的健康状态：

```
# docker inspect --format='{{json .State.Health}}' mycontainer
```


在这个命令中，--format参数指定了输出格式为JSON，mycontainer是容器的名称。

## 7.5 hook-spec

Docker容器的hook-spec是一种在容器生命周期中执行脚本的机制，可以在容器的不同阶段执行脚本，例如在容器启动前、启动后、停止前、停止后等，本文将分部举例说明：

1、创建hook-spec脚本 可以在容器中创建一个脚本文件，并将其保存在/etc/docker/目录下，如：

```
# cat /etc/docker/hook_name.sh
#!/bin/bash
echo "Container hello_tencent is starting..."
```


2、设置hook-spec脚本权限 要使hook-spec脚本可以执行，需要设置脚本的执行权限。

```
# chmod +x /etc/docker/hook_name.sh
```


3、配置hook-spec 使用 --add-host 选项将hook-spec脚本添加到容器中。以下是配置hook-spec的命令：

```
# docker run -it --add-host <hook_name>:<hook_path> <image_name>
```


其中，

需要注意的是，hook-spec脚本的执行顺序是按照文件名的字母顺序执行的。

同时，hook-spec脚本的执行结果会被记录在容器的日志中。如果hook-spec脚本执行失败，容器将无法启动或停止。因此，在编写hook-spec脚本时，需要谨慎考虑脚本的执行逻辑和错误处理机制。

# 8. 具体问题场景介绍

## 8.1 dnf install失败

具体报错如下，实际上是整个yum源失效，同时伴随着网络问题

结论：

glibc在2.34版本新增了clone3系统调用，如果clone3失败且返回ENOSYS则会重新走到旧的clone调用。然而docker 20.10.9之前的版本对于不识别的clone3，会返回EPERM而非glibc期望的ENOSYS，因此会导致clone失败

使用本系统上的 docker 不会存在问题，避免使用 docker 20.10.9 之前的旧版本环境部署本系统的容器镜像。