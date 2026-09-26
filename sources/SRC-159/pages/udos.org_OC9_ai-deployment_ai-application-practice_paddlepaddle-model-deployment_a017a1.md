source: https://docs.opencloudos.org/OC9/ai-deployment/ai-application-practice/paddlepaddle-model-deployment/

# PaddlePaddle大模型部署指南

飞桨（PaddlePaddle）是一个功能完备、开源开放的产业级深度学习平台。该平台集成了核心框架、基础模型库、端到端开发套件与丰富工具组件，为开发者提供了从模型研发到推理部署的全流程支持。

本文档将展示如何在 OpenCloudOS 9 操作系统上，通过一键安装脚本和容器镜像拉取，快速启动 PaddlePaddle 框架和相关推理服务。

## 1.安装容器依赖

### 一键安装容器依赖

脚本下载地址：[点击下载执行脚本](https://ocweb-1319394267.cos.ap-guangzhou.myqcloud.com/docs/scripts/auto_install_vllm.sh)

```
sudo ./auto_install.sh
```


## 2.启动 PaddlePaddle 框架镜像

执行如下命令启动 PaddlePaddle 框架镜像，此命令会自动从 Dokcer Hub 拉取镜像。

```
sudo docker run -itd --privileged --gpus all --name=opencloudos9-paddlepaddle opencloudos/opencloudos9-paddlepaddle
```


容器启动后可以通过命令 sudo docker ps 看到已经启动的容器，容器 ID 请以实际为准。

```
[root@VM-227-31-opencloudos ~]# docker ps
CONTAINER ID IMAGE COMMAND CREATED STATUS PORTS NAMES
a99e2188b74b opencloudos/opencloudos9-paddlepaddle:latest "/bin/bash" 12 seconds ago Up 11 seconds opencloudos9-paddlepaddle
```


可以使用以下命令进入此运行中的 Docker 容器：

** 方法1：使用 docker exec（推荐）**

```
sudo docker exec -it opencloudos9-paddlepaddle bash
# 或者使用容器ID, 容器 ID 请以实际为准
sudo docker exec -it a99e2188b74b bash
```


方法2：使用 docker attach

```
sudo docker attach opencloudos9-paddlepaddle
```


注意：使用 attach 命令时，如果容器中的 bash 会话退出，容器也会停止。

## 3.启动训练示例

容器的默认工作目录为 /workspace ，在此目录下已存在一个 MNIST 训练示例 python 脚本 paddlepaddle_demo.py。 下方展示省略了部份提醒用途或类似重复日志。

```
[root@61289711e2eb workspace]# python paddle_demo.py
download training data and load training data
Cache file /root/.cache/paddle/dataset/mnist/train-images-idx3-ubyte.gz not found, downloading https://dataset.bj.bcebos.com/mnist/train-images-idx3-ubyte.gz
Begin to download
item 2421/2421 [============================>.] - ETA: 9.230970747796576e-06s - 371us/item
Download finished
...
Cache file /root/.cache/paddle/dataset/mnist/t10k-labels-idx1-ubyte.gz not found, downloading https://dataset.bj.bcebos.com/mnist/t10k-labels-idx1-ubyte.gz
Begin to download
item 2/2 [===========================>..] - ETA: 2.5882734917104244e-05s - 238us/item
Download finished
load finished
...
```


## 4.结果展示

该示例包含 2 轮 Epoch，最终结果如下：

```
...
Epoch 2/2
step 938/938 [==============================] - loss: 0.0243 - acc: 0.9827 - 7ms/step
Eval begin...
step 157/157 [==============================] - loss: 4.7322e-04 - acc: 0.9863 - 6ms/step
Eval samples: 10000
```


## 5.清理环境

退出容器后，通过如下命令停止运行容器。

```
# 停止容器但保留容器文件系统
docker stop opencloudos9-paddlepaddle
# 或者使用容器 ID, 容器 ID 请以实际为准
docker stop a99e2188b74b
```


若停止容器运行后需要删除容器，请执行如下命令。

```
# 删除容器
docker rm opencloudos9-paddlepaddle
# 或者使用容器 ID, 容器 ID 请以实际为准
docker rm a99e2188b74b
```