source: https://docs.mthreads.com/musa-deploy/musa-deploy-doc-online/user_guide/integrated_machine_multi_gpu_deploy

# DeepSeek 一体机部署-满血版多机部署

本节介绍利用 **musa-deploy/musa-deploy-ansible** 工具在多台服务器快速部署满血版 DeepSeek 推理服务的步骤。满血版 DeepSeek 大模型推理服务是基于摩尔线程推出的 **vLLM-MUSA** 产品部署的。需注意，**vLLM-MUSA** 和前面章节[单机部署](https://docs.mthreads.com/musa-deploy/musa-deploy-doc-online/user_guide/integrated_machine_deploy)提到的 [vLLM-MTT](https://docs.mthreads.com/mtt/mtt-doc-online/) 不是一个推理后端，不是同一个产品。

阅读本章节前，建议用户先仔细阅读前面 [demo](https://docs.mthreads.com/musa-deploy/musa-deploy-doc-online/user_guide/demo) 章节。

## 主要部署思路[](https://docs.mthreads.com#主要部署思路)

- 利用 musa-deploy-ansible 工具，在多台服务器上部署基础 MUSA 开发环境，包括安装驱动，安装 Container_toolkit；如果每台服务器上基础 MUSA 环境已经搭建好，那么可以跳过此步骤。
- 利用 docke swarm 建立一个小的集群，确定 leader 节点（对应 ray 集群的 master 节点）；
- 利用 musa-deploy-ansible 工具启动推理服务，在 leader 节点和 worker 节点分别自动拉起容器来部署服务。

下面会介绍部署的详细步骤。

## 1. 设置免密登陆（仅初次部署时需执行 1 次）[](https://docs.mthreads.com#1-设置免密登陆仅初次部署时需执行-1-次)

确定一台可以连接服务器的机器作为控制节点， 登录该控制节点机器执行如下步骤：

- 安装 musa-deploy 工具(
[安装方法](https://docs.mthreads.com/musa-deploy/musa-deploy-doc-online/installation))； - 新建 hostfile 文�件，内容是服务器的 ip，用户名和密码，格式如下面示例所示；
192.168.x.x server0_username xxxxxxx192.168.x.x server1_username xxxxxxx192.168.x.x server2_username xxxxxxx192.168.x.x server3_username xxxxxxx192.168.x.x server4_username xxxxxxx
- 设置免密登录，命令如下：
sudo musa-deploy-ansible --hostfile hostfile --ssh-copy-id

建议以一台非部署推理服务的机器作为控制节点，因为在安装驱动的过程中会重启机器，可能导致执行命令中断。


执行结果示例图如下，如果已经配置过免密登陆，那么会自动跳过：


## 2. 部署基础 MUSA 开发环境（仅初次部署时需执行 1 次）[](https://docs.mthreads.com#2-部署基础-musa-开发环境仅初次部署时需执行-1-次)

### 2.1 调整 systemd 任务数限制[](https://docs.mthreads.com#21-调整-systemd-任务数限制)

为防止因系统任务数限制导致 MUSA 相关服务异常，确保系统在高负载场景下的稳定性，需要检验每台机器 systemed 配置:

`# 1. 编辑配置文件：`

sudo vim /etc/systemd/system.conf


# 2. 找到或添加以下行（如果已存在则修改，否则新增）：

DefaultTasksMax=70%


# 3. 保存并退出，然后重新加载 systemd 配置

sudo systemctl daemon-reload

sudo systemctl restart docker



70% 为推荐值��，可根据实际负载调整


### 2.2 检查 Docker 守护进程配置[](https://docs.mthreads.com#22-检查-docker-守护进程配置)

在部署多机推理服务前，需确保每台机器未启用 `live-restore`

，以避免 Docker 守护进程重启后容器继续运行造成状态不一致。

**1. 检查当前 live-restore 状态**

`docker info | grep -i 'Live Restore Enabled'`



如果结果为：

`Live Restore Enabled: true`



则需修改 Docker Daemon 配置，禁用该功能。

**2. 修改 Daemon 配置**

`# 1. 修改配置文件`

sudo vim /etc/docker/daemon.json


# 将 "live-restore": true 配置删除或者改为 "live-restore": false


# 2. 重启 docker 服务

sudo systemctl restart docker



💡

`Live Restore Enabled`

是 Docker 守护进程（dockerd）的运行时状态配置。若启用（true），容器会在 dockerd 重启时继续运行；禁用（false）时，dockerd 重启将中断所有运行中的容器（默认行为）。

### 2.3 配置基础 MUSA 环境[](https://docs.mthreads.com#23-配置基础-musa-环境)

在启动服务之前，需为每台服务器部署 MUSA 开发环境, 可使用以下命令进行一键部署:

`sudo musa-deploy-ansible --hostfile hostfile --demo vllm_musa`



首次部署注意事项：


- 需要从在线源下载 SDK 和 container_toolkit 等组件，过程可能耗时数分钟，请耐心等待；
- 安装驱动后会自动重启服务器以加载驱动。重启期间会出现含
unreachable的日志，这是正常现象。几分钟后服务器将自动恢复连接。

## 3. 初始化 docker swarm 集群[](https://docs.mthreads.com#3-初始化-docker-swarm-集群)

### 3.1 初始化集群[](https://docs.mthreads.com#31-初始化集群)

拉起服务前，需要先建立一个 docker swarm 集群，命令如下：

`sudo musa-deploy-ansible --hostfile hostfile --init-cluster`



下图显示的是 5 台服务器集群创建过程。其中 1 台是 docker swarm 集群的 leader 节点，这个 **leader 节点对应 hostfile 文件中的第一行 ip 服务器**。

执行完成后，可以登陆 **leader** 节点，执行下述命令查看 docker swarm 集群状态：

`docker node ls`



### 3.2 清除集群配置[](https://docs.mthreads.com#32-清除集群配置)

当以下情况发生时，可使用以下命令清除已有的 Docker Swarm 集群配置：

- 建立 Swarm 集群失败；
- 需要终止并清除已部署的服务。

`sudo musa-deploy-ansible --hostfile hostfile --reset-cluster`



清除集群后，在原 leader 节点再次执行 `docker node ls`

命令， 如下图所示，表明集群清除成功。此时如果需要重新创建集群或者部署服务，需要再次**初始化集群**。

## 4. 拉起vllm-musa多机推理服务[](https://docs.mthreads.com#4-拉起vllm-musa多机推理服务)

### 4.1 模型准备[](https://docs.mthreads.com#41-模型准备)

- 模型下载：
[DeepSeek-R1-BF16](https://modelscope.cn/models/MooreThreads/DeepSeek-R1-BF16/) - 模型存放：
**确保每台服务器上模型文件位于相同的目录路径**，或将模型文件统一挂载到同一个目录中。下面示例中，模型文件默认存放在`/data/DeepSeek-R1-BF16`

中。

### 4.2 拉起4机满血版deepseek推理服务[](https://docs.mthreads.com#42-拉起4机满血版deepseek推理服务)


**1. 起推理服务**

`sudo musa-deploy-ansible \`

--hostfile hostfile \

--cluster-demo vllm_musa \

--task deepseek-r1-671b \

--tp-size 8 \

--pp-size 4 \

--pp-layer-partition 16,15,15,15 \

--model-path /home/model/DeepSeek-R1-BF16/ \

-v /data:/home/model



注：


- 请确保 hostfile 文件中 4 台服务器每台都包含 8 张 GPU, 可使用命令
`mthreads-gmi`

查看每台服务器 GPU 卡数；`-v`

中，路径`/data`

为宿主机中模型文件所在父级目录，可根据实际路径做调整，`/home/model`

为容器路径，一般不做修改；`--model-path`

为容器中路径，故容器模型路径`/home/model/<ModelPath>/`

中模型目录名`ModelPath`

需要和宿主机模型路径`/data/<ModelPath>`

中模型目录名`ModelPath`

保持一致。

启动命令的结果示例如下:

**2. 检验集群服务状态**

登陆 leader 节点，查看到集群中启动服务状态：

`docker service ls`



- vllm-musa 服务：以
`registry.mthreads.com/public/kuae/vllm-mp22-py310:0415-dev`

镜像起的服务是部署 vllm-musa 用的，每个物理节点只会拉起一个 vllm-musa 服务容器。示例中 hostfile 中包含 5 台服务器，所以这里拉起了 5 个服务容器，对于 4 机部署实际运行时只用到了 4 个节点服务容器。对于 4 机部署，hostfile 中至少包含 4 个服务器 ip。 - kuae-chat 服务：以
`mthreads-cn-beijing.cr.volces.com/kuaecloud/kuae-cloud-core-web:prod_ds_0.0.3`

镜像起的服务是部署 kuae-chat 用的。

**3. 查看模型加载过程**

`# 1. 获取正在运行的 vLLM 服务容器（COMMAND 为 "/bin/sh -c 'service…" 对应容器）`

docker ps | grep deepseek


# 示例输出

# 15ee3100ce41 registry.mthreads.com/public/kuae/vllm-mp22-py310:0415-dev "/bin/sh -c 'service…" 11 seconds ago Up 10 seconds deepseek-r1-671b_task2.1.fijwcxhky19nrnnwdpedkgxbc

# 2a80d5444884 mthreads-cn-beijing.cr.volces.com/kuaecloud/kuae-cloud-core-web:prod_ds_0.0.3 "docker-entrypoint.s…" 14 seconds ago Up 13 seconds deepseek-r1-671b_task3.1.ime1th3cpk6zwn9jo25q6tkc8


# 2. 连接到 vLLM 服务容器，查看模型加载或初始化日志（即使终端窗口关闭服务也不会停止）

docker attach 15ee3100ce41



**3. 访问 kuae-chat 服务**

vLLM 服务起来后，访问 kuae-chat 服务：

`http://x.x.x.x:3000/playground/chat`

# 这里的x.x.x.x是对应hostfile第一行的ip



如果链接无法访问，说明 kuae-chat 服务没有正确启动，此时可以手动拉起服务：

`# 设置宿主机端口。注意：如果该端口已被占用，服务将启动失败，请更换为一个未被占用的端口`

HOST_PORT=3000 # 可根据实际情况修改为未占用端口

docker run -d \

-p ${HOST_PORT}:3000 \

-v /tmp/kuae-chat-public:/app/public/models/ \

registry.mthreads.com/mcconline/kuae-chat:1.0


# 再次访问 URL，此时 URL 中端口应改为实际的 HOST_PORT

# http://x.x.x.x:<HOST_PORT>/playground/chat



### 4.3 拉起5机满血版deepseek推理服务[](https://docs.mthreads.com#43-拉起5机满血版deepseek推理服务)

`sudo musa-deploy-ansible \`

--hostfile hostfile \

--cluster-demo vllm_musa \

--task deepseek-r1-671b \

--tp-size 8 \

--pp-size 5 \

--pp-layer-partition 13,12,12,12,12 \

--model-path /home/model/DeepSeek-R1-BF16/ \

-v /data:/home/model



拉起 5 机推理服务和 4 机步骤一致，区别是 `hostfile`

和 `pp-size`

，`pp-layer-partition`

参数配置不一样。


`--model-path`

和`-v`

参数配置注意事项参看[4.2.1 起推理服务]注释部分。

### 4.4 参数解释[](https://docs.mthreads.com#44-参数解释)

| parameter | 解释 |
|---|---|
| --hostfile | 必选，指定服务器的ip，用户名，密码 |
| --cluster-demo | 必选，仅支持‘vllm_musa’ |
| --task | 必选，指定推理模型的名称，‘deepseek-r1-671b’ |
| --tp-size | 必选，tensor并行size |
| --pp-size | 必选，pipeline并行size |
| --pp-layer-partition | 必选，pipeline并行层数切分方法 |
| --max-model-len | 可选，指定最大上下文长度，默认是1024 |
| --model-path | 必选，容器内模型路径 |
| --disable-kuae-chat | 可选，默认会拉起kuae-chat服务，如果不想拉起kuae-chat服务，可以使用该参数 |
| -v | 必选，将host目录映射进容器内，务必将host目录下模型路径映射进容器内，具体用法同docker |
| -e | 可选，指定容器内环境变量，用法同docker |