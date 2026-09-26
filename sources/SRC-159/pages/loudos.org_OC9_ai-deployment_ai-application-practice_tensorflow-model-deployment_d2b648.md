source: https://docs.opencloudos.org/OC9/ai-deployment/ai-application-practice/tensorflow-model-deployment/

# TensorFlow大模型部署指南

TensorFlow 是一个端到端的开源机器学习平台，它拥有全面而灵活的工具、库及社区资源生态系统，助力研究人员推动机器学习技术的前沿发展，并使开发者能够轻松构建和部署由机器学习驱动的应用程序。

本文档将展示如何在 OpenCloudOS 9 操作系统上，通过一键安装脚本和容器镜像拉取，快速启动 TensorFlow 框架和相关推理服务。

## 1.安装容器依赖

### 一键安装容器依赖

脚本下载地址：[点击下载执行脚本](https://ocweb-1319394267.cos.ap-guangzhou.myqcloud.com/docs/scripts/auto_install_vllm.sh)

```
sudo ./auto_install.sh
```


## 2.启动 TensorFlow 框架镜像

执行如下命令启动 TensorFlow 框架镜像，此命令会自动从 Dokcer Hub 拉取镜像。

```
sudo docker run -itd --privileged --gpus all --name=opencloudos9-tensorflow opencloudos/opencloudos9-tensorflow
```


容器启动后可以通过命令 sudo docker ps 看到已经启动的容器，容器 ID 请以实际为准。

```
[root@VM-227-31-openlcoudos ~]# docker ps
CONTAINER ID IMAGE COMMAND CREATED STATUS PORTS NAMES
78ab8e99b4d2 opencloudos/opencloudos9-tensorflow:latest "/bin/bash" 12 seconds ago Up 11 seconds opencloudos9-tensorflow
```


可以使用以下命令进入此运行中的 Docker 容器：

** 方法1：使用 docker exec（推荐）**

```
sudo docker exec -it opencloudos9-tensorflow bash
# 或者使用容器ID, 容器 ID 请以实际为准
sudo docker exec -it 78ab8e99b4d2 bash
```


方法2：使用 docker attach

```
sudo docker attach opencloudos9-tensorflow
```


注意：使用 attach 命令时，如果容器中的 bash 会话退出，容器也会停止。

## 3.启动训练示例

容器的默认工作目录为 /workspace ，在此目录下已存在一个 MNIST 训练示例 python 脚本 tensorflow_demo.py。

下方展示省略了部份提醒用途的日志。

```
[root@78ab8e99b4d2 workspace]# python tensorflow_demo.py
...
Downloading data from https://storage.googleapis.com/tensorflow/tf-keras-datasets/mnist.npz
11490434/11490434 ━━━━━━━━━━━━━━━━━━━━ 2s 0us/step
...
Epoch 1/5
...
1875/1875 ━━━━━━━━━━━━━━━━━━━━ 5s 2ms/step - accuracy: 0.9155 - loss: 0.2914
...
```


## 4.结果展示

该示例包含 5 轮 Epoch，最终结果如下：

```
...
Epoch 4/5
1875/1875 ━━━━━━━━━━━━━━━━━━━━ 3s 2ms/step - accuracy: 0.9729 - loss: 0.0883
Epoch 5/5
1875/1875 ━━━━━━━━━━━━━━━━━━━━ 3s 2ms/step - accuracy: 0.9768 - loss: 0.0753
313/313 - 1s - 4ms/step - accuracy: 0.9798 - loss: 0.0669
```


## 5.清理环境

退出容器后，通过如下命令停止运行容器。

```
# 停止容器但保留容器文件系统
docker stop opencloudos9-tensorflow
# 或者使用容器 ID, 容器 ID 请以实际为准
docker stop 78ab8e99b4d2
```


若停止容器运行后需要删除容器，请执行如下命令。

```
# 删除容器
docker rm opencloudos9-tensorflow
# 或者使用容器 ID, 容器 ID 请以实际为准
docker rm 78ab8e99b4d2
```