source: https://docs.mthreads.com/playbook/playbook-doc-online/hello-docker

# 【中级】Hello Docker：手把手带你学习容器开发

## 更新日志[](https://docs.mthreads.com#更新日志)

| 版本 | 日期 | 变更描述 |
|---|---|---|
| 1.0.0 | 2026-01-30 | 初始版本，包含在 AI 算力本 MTT AIBOOK(型号 A141) 上容器化开发的完整学习指南。 |

## 1. 项目简介[](https://docs.mthreads.com#1-项目简介)

本教程旨在带您掌握基本的 Docker 核心概念与实操技能，学习如何在 MTT AIBOOK 设备上安装 Docker，拉取并运行镜像，构建自己的容器化 Python Web 应用，使用 VS Code 在容器中开发调试，最终将镜像发布到 Docker Hub。

**难度：中级，适合有编程基础的开发者体验**

**Docker 简介：** Docker 是一个开源的容器化平台，能够把应用程序及其依赖打包到一个标准化的单元中，并在任何支持 Docker 的环境中快速、稳定地运行。它的优势在于轻量、可移植、一致性强，非常适合开发、测试、部署现代应用。Docker 容器与虚拟机之间最大的区别就是，Docker 容器之间共用一个系统内核，而每个虚拟机都包含一个操作系统的完整内核，所以 Docker 比虚拟机更轻、更小，运行更快。

## 2. 前置条件[](https://docs.mthreads.com#2-前置条件)

在开始本教程之前，请确保您已满足以下所有条件：

**硬件:**- AI 算力本 MTT AIBOOK，型号 A141

**软件:**- MTT AIBOOK 操作系统 AIOS(1.3.1-B15) 及以上版本
- 设备已配置管理员权限（可使用 sudo 命令）
- VS Code 代码编辑器


## 3. 环境部署[](https://docs.mthreads.com#3-环境部署)

本章节描述如何在 MTT AIBOOK 上安装 Docker 并完成基础配置。

### 3.1 安装 Docker Engine[](https://docs.mthreads.com#31-安装-docker-engine)

AI 算力本 MTT AIBOOK 基于 ARM 架构，运行 Linux（Ubuntu 系统）。Docker 通常来说，是基于 Linux 系统的容器化技术，我们可以选择使用 Docker Desktop 或 Docker Engine。但考虑到 Linux 系统对 Docker Engine 的原生支持，以及其轻量、高性能、无需额外虚拟化层的优势，更适合我们的开发环境和资源管理需求，因此我们选择安装和使用 Docker Engine CE，以便更高效地进行本地容器化开发。

#### 安装 Docker[](https://docs.mthreads.com#安装-docker)

-
安装必要的依赖。

sudo apt-get install -y iptables arptables ebtablessudo apt install -y apt-transport-https ca-certificates curl software-properties-common -
添加 Docker 的官方 GPG 密钥。

curl -fsSL https://download.docker.com/linux/ubuntu/gpg | sudo gpg --dearmor -o /usr/share/keyrings/docker-archive-keyring.gpg -
设置 Docker 的稳定版仓库。

echo "deb [arch=$(dpkg --print-architecture) signed-by=/usr/share/keyrings/docker-archive-keyring.gpg] https://download.docker.com/linux/ubuntu $(lsb_release -cs) stable" | sudo tee /etc/apt/sources.list.d/docker.list -
更新 APT 包索引。

sudo apt update -
安装 Docker。

sudo apt install docker-ce=5:27.5.0-1~ubuntu.22.04~jammy \docker-ce-cli=5:27.5.0-1~ubuntu.22.04~jammy \containerd.io注意此处锁定 Docker 版本以确保教程一致性。如果安装失败，请尝试移除

`=...`

部分以安装最新版本。 -
配置 iptables 使用 legacy 模式。

sudo update-alternatives --set iptables /usr/sbin/iptables-legacysudo update-alternatives --set ip6tables /usr/sbin/ip6tables-legacysudo update-alternatives --set arptables /usr/sbin/arptables-legacysudo update-alternatives --set ebtables /usr/sbin/ebtables-legacy -
验证 Docker 安装。

sudo systemctl status dockerdocker --version若能够输出正确的版本号则证明安装成功。

-
将当前用户添加到 docker 组。

sudo usermod -aG docker $USER**重要提示：**执行此命令后，请重启系统以使更改生效，后续无需使用 sudo 运行 Docker 命令。


## 4. 最佳实践[](https://docs.mthreads.com#4-最佳实践)

本章节指导您完成 Docker 的核心操作流程，从拉取镜像到本地构建和发布镜像。

### 场景 1: 拉取和查看镜像[](https://docs.mthreads.com#场景-1-拉取和查看镜像)

学习如何从 Docker Hub 拉取镜像并查看本地镜像列表：

-
**理解镜像命名规则**。Docker 镜像的完整名称格式为：

`[registry/][namespace/] 镜像名：标签`

部分 说明 示例 registry 仓库的注册表地址 `docker.io`

（Docker Hub，可省略）namespace 命名空间 `dong413`

（作者名），`library`

（官方命名空间）镜像名 镜像名称 `simple-python-app`

标签 版本标签 `latest`

（不写则表示最新版本） -
**拉取镜像**。docker pull dong413/simple-python-app:latest此命令会从 Docker Hub 拉取一个简单的 Flask Web 应用镜像。

拉取过程：

latest: Pulling from dong413/simple-python-app37259e733066: Pull complete6e88b4602d85: Pull complete...Status: Downloaded newer image for dong413/simple-python-app:latest -
**查看本地镜像**。docker images输出示例：

REPOSITORY TAG IMAGE ID CREATED SIZEdong413/simple-python-app latest be349c17d241 7 months ago 171MB**小知识：Docker Hub**是 Docker 的官方镜像仓库，里面存放成千上万的镜像。registry+ 命名空间 + 镜像名 组合起来叫做 repository（镜像库），一个镜像库用来存放同一镜像的不同版本。

### 场景 2: 创建和运行容器[](https://docs.mthreads.com#场景-2-创建和运行容器)

学习如何从镜像创建容器并运行应用：

-
**理解容器概念**。概念 说明 比喻 **镜像（Image）**一个只读的模板，�包含运行应用所需要的一切 像是做好的菜谱 **容器（Container）**镜像运行之后的实例，是一个真正可执行的、正在运行的应用环境 像是照着菜谱做出来的一道菜 -
**创建并运行容器**。docker run -d -p 5000:5000 dong413/simple-python-app:latest**参数说明：**参数 说明 `-d`

后台运行容器 `-p 5000:5000`

端口映射，将容器的 5000 端口映射到宿主机的 5000 端口 `dong413/simple-python-app:latest`

要运行的镜像名称 -
**查看运行中的容器**。docker ps此命令会显示当前正在运行的容器列表。 输出示例：

CONTAINER ID IMAGE COMMAND CREATED STATUS PORTS NAMES367f16b7f92d dong413/simple-python-app:latest "python app.py" 7 seconds ago Up 6 seconds 0.0.0.0:5000->5000/tcp modest_wu -
**测试容器**。在浏览器中打开

`http://localhost:5000`

如果网页可以正常打开，说明容器可正常运行。

**常用命令说明：**

| 命令 | 说明 |
|---|---|
`docker run` | 运行容器 |
`docker ps` | 查看正在运行的容器 |
`docker run -p [HOST_PORT]:[CONTAINER_PORT]` | 端口映射，让宿主机可以访问容器内的服务 |
`docker run -v [宿主机路径]:[容器内路径]` | 挂载数据卷或目录映射，实现数据持久化 |

### 场景 3: 使用 VS Code Dev Containers 开发[](https://docs.mthreads.com#场景-3-使用-vs-code-dev-containers-开发)

场景二中，我们"直接运行一个现成的应用"，类似于安装一个别人写好的软件。而本场景，是让我们"进入开发模式"。

虽然在上一步，我们拉取应用镜像，但为获得最干净最灵活的开发体验，我们将利用 VS Code 的自动化能力，启动一个全新的基础环境镜像，并将本地的代码挂载进去。这种方式兼顾开发效率与环境一致性，是现代容器化开发的主流做法。

-
**安装 Dev Containers 插件**。-
打开 VS Code

-
安装扩展：

**Dev Containers**（微软官方出品）

-
-
**创建 Dev Container 配置**。- 新建文件夹并在 VS Code 中打开。
- 在根目录下创建
`.devcontainer`

文件夹。 - 创建
`devcontainer.json`

文件。

项目结构：

.└── .devcontainer/└── devcontainer.json -
**配置 devcontainer.json**。{"name": "Python Dev","image": "python:3.10","workspaceFolder": "/app","mounts": ["source=${localWorkspaceFolder},target=/app,type=bind"],"settings": {"terminal.integrated.defaultProfile.linux": "bash"},"extensions": ["ms-python.python"]}**配置说明：**配置项 说明 `"image"`

使用的 Docker 镜像（可替换为您自己拉的镜像） `"mounts"`

将当前本地代码挂载到容器中的 `/app`

`"workspaceFolder"`

VS Code 在容器中的默认目录 `"extensions"`

自动为容器安装 Python 插件 -
**启动 Dev Container**。-
点击 VS Code 左下角按钮

`><`

。 -
选择：

**"Reopen in Container"**。VS Code 会根据配置自动拉取指定镜像、挂载代码，并在容器中打开开发环境。


-
-
**开发与调试**。现在可以像在本地一样开发了，比如运行一个简单的 hello world 程序：

print("Hello, World!")

**容器开发的优点：**

| 优点 | 说明 |
|---|---|
| 一致性 | 容器中运行环境和部署环境一致 |
| 便捷性 | 编辑器 + 终端 + 容器集成，体验良好 |
| 清洁 | 不污染本机系统环境 |
| 易于团队共享 | `.devcontainer` 可上传至 Git 仓库，团队成员一键进入容器开发环境 |

### 场景 4: 构建自定义镜像[](https://docs.mthreads.com#场景-4-构建自定义镜像)

学习如何编写 Dockerfile 并构建自己的镜像：

这一章让你将本地项目封装成一个可移植的镜像，包含代码和全部运行环境，最终能够交给别人运行。

-
**准备项目代码**。git clone https://gitee.com/mthreadsacademy/project100.gitcd docker-simple-app或按照示例代码创建项目。

-
**编写 Dockerfile**。Dockerfile 是镜像构建的配方，Docker 会根据这个文件帮您打包镜像。

# 使用官方 Python 运行时作为基础镜像FROM python:3.11-slim# 设置工作目录WORKDIR /app# 将 requirements.txt 复制到容器中COPY requirements.txt .# 安装 Python 依赖RUN pip install --no-cache-dir -r requirements.txt# 将应用代码复制到容器中COPY app.py .# 暴露端口 5000EXPOSE 5000# 设置环境变量ENV FLASK_APP=app.pyENV FLASK_RUN_HOST=0.0.0.0# 运行应用CMD ["python", "app.py"]**Dockerfile 指令说明：**指令 说明 `FROM`

指定基础镜像 `WORKDIR`

设置容器内的工作目录 `COPY`

将文件从主机复制到容器 `RUN`

在构建时执行命令（如安装依赖） `EXPOSE`

声明容器监听的端口 `ENV`

设置环境变量 `CMD`

容器启动时执行的默认命令 -
**创建 .dockerignore 文件**。`.dockerignore`

类似于`.gitignore`

，用来排除不需要打包进镜像的文件，可以减小镜像体积，避免敏感文件，提高构建速度。# Python 缓存和字节码文件__pycache__/*.py[cod]*$py.class*.so# 虚拟环境ai_image_env/venv/env/ENV/# Git 相关.git/.gitignore# IDE 和编辑器文件.vscode/.idea/*.swp*.swo*~# 操作系统文件.DS_StoreThumbs.db# 日志文件*.log# 临时文件*.tmp*.temp# 环境配置文件（安全考虑，不打包到镜像中）.env.env.local.env.production.env.*# 测试文件test_**_test.py# 构建文件build/dist/*.egg-info/ -
**构建镜像**。docker build -t simple-python-app:latest .**命令说明：**参数 说明 `-t simple-python-app:latest`

指定镜像名称和标签 `.`

使用当前目录作为构建上下文 -
**验证镜像构建**。# 查看本地镜像docker images# 查看镜像详细信息docker inspect simple-python-app:latest# 测试运行docker run -d -p 5000:5000 --name my-app simple-python-app

### 场景 5: 发布镜像到 Docker Hub[](https://docs.mthreads.com#场景-5-发布镜像到-docker-hub)

学习如何将构建好的镜像推送到 Docker Hub 并分享给他人使用：

-
**登录 Docker Hub**。docker login根据提示输入您的 Docker Hub 用户名和密码。

-
**为镜像打标签**。Docker Hub 镜像命名格式为：

`<你的用户名>/<镜像名>:<标签>`

。# 方法 1：构建时直接指定正确的标签docker build -t your-username/simple-python-app:latest .# 方法 2：为现有镜像添加新标签docker tag simple-python-app:latest your-username/simple-python-app:latest# 添加版本标签docker tag simple-python-app:latest your-username/simple-python-app:v1.0提示请将

`your-username`

替换为您的 Docker Hub 用户名。 -
**推送镜像到 Docker Hub**。# 推送 latest 版本docker push your-username/simple-python-app:latest# 推送特定版本docker push your-username/simple-python-app:v1.0# 推送所有标签docker push your-username/simple-python-app --all-tags -
**验证推送**。在 Docker Hub 网页端查看您的镜像，或使用以下命令测试：

# 删除本地镜像进行测试docker rmi your-username/simple-python-app:latest# 从 Docker Hub 拉取镜像docker pull your-username/simple-python-app:latest# 运行从 Docker Hub 拉取的镜像docker run -d -p 5000:5000 your-username/simple-python-app:latest推送完成后，您可以在网页端查看镜像，并分享给别人使用。


### 常用操作命令[](https://docs.mthreads.com#常用操作命令)

| 操作 | 命令示例 | 说明 |
|---|---|---|
| 查看版本 | `docker --version` | 检查 Docker 是否安装及版本号 |
| 拉取镜像 | `docker pull [镜像名]:[标签]` | 从仓库下载镜像，如 `nginx:latest` |
| 查看本地镜像 | `docker images` | 列出本机已下载的镜像列表 |
| 运行容器 | `docker run -d -p [主机端口]:[容器端口] [镜像名]` | -d: 后台运行 -p: 端口映射 (调试时建议加 `-it` ) |
| 交互式运行 | `docker run -it [镜像名] /bin/bash` | -it: 分配伪终端，用于进入容器内部调试 |
| 查看运行中容器 | `docker ps` | 仅显示正在运行的容器 |
| 查看所有容器 | `docker ps -a` | 包含已停止 (Exited) 的容器 |
| 停止容器 | `docker stop [容器 ID/名称]` | 优雅地停止容器 |
| 删除容器 | `docker rm [容器 ID/名称]` | 删除已停止的容器 (运行中需加 `-f` ) |
| 构建镜像 | `docker build -t [名称]:[标签] .` | 注意末尾的点 `.` ，代表当前目录 |
| 登录仓库 | `docker login` | 登录 Docker Hub 或其他私有仓库 |
| 推送镜像 | `docker push [用户名]/[镜像名]:[标签]` | 将本地镜像上传到仓库 |
| 删除镜像 | `docker rmi [镜像 ID/名称]` | 删除本地镜像 (若有容器占用需先删容器) |

## 5. 附录[](https://docs.mthreads.com#5-附录)

### 5.1 项目特点[](https://docs.mthreads.com#51-项目特点)

**覆盖 Docker 基本使用流程**：从安装、拉取镜像、运行容器到构建与发布全流程教学。**结合 VS Code Dev Containers 开发体验**：介绍了现代主流容器化开发方式。**贴合设备实战**：适配 MTT AIBOOK 的 Linux 开发环境。**提供最佳实践**：包括`.dockerignore`

、环境变量管理、版本标签等。**IO 可扩展性强**：为后续学习 docker-compose、CI/CD、微服务架构打下基础。

### 5.2 小知识：什么是 Docker[](https://docs.mthreads.com#52-小知识什么是-docker)

您可能听说过这样的"玄学定律"：任何在您的机器上能够完美运行的代码，在其他人的机器上必然会失败！面对这样的问题，Docker 就可以帮我们解决。

**Docker 的本质：** Docker 可以帮我们打包代码以及运行代码所需要的一切（如环境变量等）。不仅打包程序，还打包了程序所需的整个环境，让开发、测试、部署变得简单而可靠。也就意味着，有 Docker 之后您就可以在任何计算机上运行您的代码。

**核心概念：**

**镜像（Image）**：一个只读的模板，包含了运行应用所需要的一切，包括操作系统、运行环境、程序代码和依赖。可以把镜像理解为“一份软件快照”，像是做好的菜谱。**容器（Container）**：镜像运行之后的实例，是一个真正可执行的、正在运行的应用环境。容器是隔离的、轻量的，可以快速启动和销毁，不影响宿主机，也不相互干扰。您可以把容器理解为“照着镜像做出来的一道菜”。

### 5.3 进阶建议[](https://docs.mthreads.com#53-进阶建议)

完成本教程，已经掌握了 Docker 的基础使用！接下来如果您希望更进一步，这里为您推荐一些进阶方向与实践内容：

#### 1. 学习 docker-compose：管理多容器项目[](https://docs.mthreads.com#1-学习-docker-compose管理多容器项目)

在实际项目中，您的应用通常不止一个容器（例如：前端 + 后端 + 数据库）。这时推荐使用 docker-compose，实现：

- 编排多个服务
- 统一管理网络、环境变量、数据卷
- 使用一个 YAML 文件启动整个系统

**示例任务：** 用 `docker-compose.yml`

同时启动 Flask + Redis + Postgres。

#### 2. 自定义 Dev Container：开发环境版本控制[](https://docs.mthreads.com#2-自定义-dev-container开发�环境版本控制)

您可以通过自定义 `.devcontainer/Dockerfile`

添加更多工具或包：

- 自动安装 lint 工具（如 black, flake8）
- 内置测试框架（如 pytest）
- 安装特定系统工具（如 curl, git）

**示例任务：** 创建一个 Dev Container，自动支持 Python 格式化和调试。

#### 3. 使用私有镜像仓库（Harbor / GitHub Container Registry）[](https://docs.mthreads.com#3-使用私有镜像仓库harbor--github-container-registry)

当您不想将镜像公开发布到 Docker Hub，可以考虑：

- 使用 GitHub 的容器仓库（ghcr.io）
- 搭建自己的私有仓库（如 Harbor）

**示例任务：** 将镜像推送至 GitHub Packages 并部署。

#### 4. 探索 CI/CD 与自动化部署[](https://docs.mthreads.com#4-探索-cicd-与自动化部署)

Docker 非常适合接入自动化部署流程，如 GitHub Actions、GitLab CI 等。您可以：

- 编写
`.yml`

自动构建镜像并部署 - 用 webhook 自动部署到服务器
- 用 Nginx + Docker 实现自动上线

**示例任务：** 通过 GitHub Actions 自动构建并推送 Flask 镜像。

#### 5. 学习容器网络与挂载机制[](https://docs.mthreads.com#5-学习容器网络与挂载机制)

深入理解：

- 容器之间如何通信（Bridge / Host / Overlay）
- 如何将容器挂载本地目录、数据卷
- 使用命名卷持久化数据库数据

**示例任务：** 创建一个数据容器，自动保存容器运行状态和日志。

### 5.4 常见问题[](https://docs.mthreads.com#54-常见问题)

问题描述 | 可能原因 | 解决方案 |
|---|---|---|
Docker 安装失败 | 网络问题或仓库配置错误 | 1. 检查网络连接 2. 确认仓库地址正确 3. 尝试移除版本锁定安装最新版本。 |
docker 命令需要 sudo | 用户未添加到 docker 组 | 1. 执行 `sudo usermod -aG docker $USER` 2. 重启系统使更改生效。 |
容器无法访问网络 | iptables 配置问题 | 1. 确认已配置 iptables-legacy 2. 检查防火墙设置。 |
端口已被占用 | 宿主机端口被其他程序使用 | 1. 查找占用程序：`sudo lsof -i :5000` 2. 终止占用程序或更改映射端口。 |
镜像拉取失败 | 网络问题或镜像不存在 | 1. 检查网络连接 2. 确认镜像名称和标签正确 3. 尝试使用国内镜像源。 |
构建镜像失败 | Dockerfile 语法错误或依赖问题 | 1. 检查 Dockerfile 语法 2. 确认依赖文件存在 3. 查看构建日志定位错误。 |
推送镜像失败 | 未登录或权限不足 | 1. 执行 `docker login` 登录2. 确认镜像标签包含用户名 3. 检查 Docker Hub 账户权限。 |
Dev Container 启动失败 | 配置文件错误或镜像拉取失败 | 1. 检查 `devcontainer.json` 语法2. 确认镜像名称正确 3. 查看 VS Code 输出日志。 |

### 5.5 相关资源[](https://docs.mthreads.com#55-相关资源)

- Docker 官方文档：
[https://docs.docker.com/](https://docs.docker.com/)（了解 Docker 完整功能） - Docker Hub：
[https://hub.docker.com/](https://hub.docker.com/)（镜像仓库） - VS Code Dev Containers 文档：
[https://code.visualstudio.com/docs/devcontainers/containers](https://code.visualstudio.com/docs/devcontainers/containers)（了解容器开发） - Dockerfile 最佳实践：
[https://docs.docker.com/develop/develop-images/dockerfile_best-practices/](https://docs.docker.com/develop/develop-images/dockerfile_best-practices/)（学习编写高效的 Dockerfile）