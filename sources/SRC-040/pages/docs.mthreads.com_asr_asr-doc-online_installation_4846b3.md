source: https://docs.mthreads.com/asr/asr-doc-online/installation

# 离线语音识别服务端安装指南

本文档将指导您在目标机器（如 aibook）上安装必要的依赖、配置 Docker 环境，并部署本地 ASR（自动语音识别）服务。

## 1. 环境准备[](https://docs.mthreads.com#1-环境准备)

在部署服务之前，需要先安装和配��置 Docker 以及相关的系统依赖。

### 1.1 替换 APT 软件源（可选）[](https://docs.mthreads.com#11-替换-apt-软件源可选)

如果您的服务器无法访问外网或访问速度较慢，建议将 Ubuntu 源替换为阿里云源，以加速下载过程。如果您的网络可以正常访问外网，可跳过此步骤。

`# 备份原来的软件源配置文件`

sudo cp /etc/apt/sources.list /etc/apt/sources.list.bak


# 替换为阿里云源（适用于 Ubuntu 16.04 Xenial，请根据实际系统版本调整）

sudo tee /etc/apt/sources.list > /dev/null <<'EOF'

deb https://mirrors.aliyun.com/ubuntu-ports/ xenial main restricted universe multiverse

deb https://mirrors.aliyun.com/ubuntu-ports/ xenial-updates main restricted universe multiverse

deb https://mirrors.aliyun.com/ubuntu-ports/ xenial-backports main restricted universe multiverse

deb https://mirrors.aliyun.com/ubuntu-ports/ xenial-security main restricted universe multiverse

# 如果需要源码包，可以取消下面注释：

# deb-src https://mirrors.aliyun.com/ubuntu-ports/ xenial main restricted universe multiverse

EOF


# 更新 APT 软件包缓存

sudo apt-get update



### 1.2 安装 Docker 前置依赖[](https://docs.mthreads.com#12-安装-docker-前置依赖)

配置 Docker 的官方 GPG 密钥和稳定版仓库，并安装相关依赖。

`# 安装必要的依赖工具`

sudo apt install -y apt-transport-https ca-certificates curl software-properties-common


# 添加 Docker 的官方 GPG 密钥

curl -fsSL https://download.docker.com/linux/ubuntu/gpg | sudo gpg --dearmor -o /usr/share/keyrings/docker-archive-keyring.gpg


# 设置 Docker 的稳定版仓库

echo "deb [arch=$(dpkg --print-architecture) signed-by=/usr/share/keyrings/docker-archive-keyring.gpg] https://download.docker.com/linux/ubuntu $(lsb_release -cs) stable" | sudo tee /etc/apt/sources.list.d/docker.list


# 再次更新 APT 软件包缓存

sudo apt update



### 1.3 安装 Docker 及网络工具[](https://docs.mthreads.com#13-安装-docker-及网络工具)

`# 安装 Docker 引擎及 CLI`

sudo apt install -y docker-ce docker-ce-cli containerd.io


# 安装所需网络工具（用于解决部分网络兼容性问题）

sudo apt install -y arptables ebtables


# 确保系统使用 iptables-legacy 而不是 nftables

sudo update-alternatives --set iptables /usr/sbin/iptables-legacy

sudo update-alternatives --set ip6tables /usr/sbin/ip6tables-legacy

sudo update-alternatives --set arptables /usr/sbin/arptables-legacy

sudo update-alternatives --set ebtables /usr/sbin/ebtables-legacy



### 1.4 启动与配置 Docker[](https://docs.mthreads.com#14-启动与配置-docker)

安装完成后，启动 Docker 服务并配置当前用户权限，避免每次执行 docker 命令都需要加 sudo。

`# 启动 Docker 服务`

sudo systemctl start docker


# 检查 Docker 运行状态和版本，验证是否安装成功

sudo systemctl status docker

docker --version


# 将当前用户添加到 docker 用户组中

sudo usermod -aG docker $USER




注意：修改用户组后，需要重启系统（或注销并重新登录）才能使更改完全生效：

sudo reboot

## 2. 模型镜像部署与启动[](https://docs.mthreads.com#2-模型镜像部署与启动)

环境准备完毕后，可以开始获取并运行本地 ASR 服务的 Docker 镜像。

### 2.1 获取并加载服务端镜像[](https://docs.mthreads.com#21-获取并加载服务端镜像)

`# 下载离线 ASR 服务端镜像文件`

wget -O m1000_local_asr_server.tar "https://mtai-speech.tos-cn-shanghai.volces.com/zhenlinliang/local_asr/m1000_local_asr_server.tar"


# 将镜像加载到本地 Docker 中

docker load -i m1000_local_asr_server.tar



### 2.2 启动服务容器[](https://docs.mthreads.com#22-启动服务容器)

使用以下命令运行 ASR 服务容器。如果您需要修改挂载目录，请调整 `-v`

参数。

`sudo docker run --name local_asr_server \`

-v /data:/data \

--ipc=host \

--ulimit memlock=-1 \

--ulimit stack=67108864 \

-it sh-harbor.mthreads.com/mt-ai/local_asr_server:1.0 bash



### 2.3 启动 ASR 服务进程[](https://docs.mthreads.com#23-启动-asr-服务进程)

进入容器后，执行以下命令以启动 WebSocket 语音识别服务：

`cd /workspace/FunASR/runtime `


/workspace/FunASR/runtime/websocket/build/bin/funasr-wss-server-2pass \

--certfile /workspace/FunASR/runtime/ssl_key/server.crt \

--decoder-thread-num 4 \

--io-thread-num 1 \

--itn-dir /workspace/models/thuduj12/fst_itn_zh \

--keyfile /workspace/FunASR/runtime/ssl_key/server.key \

--lm-dir /workspace/models/damo/speech_ngram_lm_zh-cn-ai-wesp-fst \

--model-dir /workspace/models/damo/speech_paraformer-large-vad-punc_asr_nat-zh-cn-16k-common-vocab8404-onnx \

--model-thread-num 1 \

--online-model-dir /workspace/models/damo/speech_paraformer-large_asr_nat-zh-cn-16k-common-vocab8404-online-onnx \

--port 10199 \

--punc-dir /workspace/models/damo/punc_ct-transformer_zh-cn-common-vad_realtime-vocab272727-onnx \

--vad-dir /workspace/models/damo/speech_fsmn_vad_zh-cn-16k-common-onnx




常见问题排查：

- 服务启动后，调用地址中的
`host`

为对应的服务器 IP，端口为启动服务时指定的`--port`

（此处示例为`10199`

）。如果您是在宿主机外访问，请确保启动镜像容器时使用`-p`

参数正确映射了该端口（或者使用如示例中的 host 模式网络）。- 如果启动时提示
`Address already in use`

，请检查`10199`

端口是否已被其他进程占用，可以通过`netstat -tunlp | grep 10199`

查找，并`kill`

掉对应进程后重新启动服务。