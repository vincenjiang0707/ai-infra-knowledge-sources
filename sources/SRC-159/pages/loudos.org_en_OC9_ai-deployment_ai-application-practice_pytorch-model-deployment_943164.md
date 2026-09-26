source: https://docs.opencloudos.org/en/OC9/ai-deployment/ai-application-practice/pytorch-model-deployment/

# PyTorch大模型部署指南

PyTorch 是一个 Python 工具包，其核心特性包含两方面：一方面提供类似 NumPy 的张量计算功能，并具备强大的 GPU 加速能力；另一方面构建基于反向传播自动求导系统的深度学习神经网络。该工具包支持与 NumPy、SciPy 和 Cython 等常用 Python 科学计算库无缝衔接，便于根据需求扩展功能。

本文档将展示如何在 OpenCloudOS 9 操作系统上，通过一键安装脚本和容器镜像拉取，快速启动 PyTorch 框架和相关推理服务。

## 1.安装容器依赖

### 一键安装容器依赖

脚本下载地址：[点击下载执行脚本](https://ocweb-1319394267.cos.ap-guangzhou.myqcloud.com/docs/scripts/auto_install_vllm.sh)

```
sudo ./auto_install.sh
```


## 2.启动 PyTorch 框架镜像

执行如下命令启动 PyTorch 框架镜像，此命令会自动从 Dokcer Hub 拉取镜像。

```
sudo docker run -itd --privileged --gpus all --name=opencloudos9-pytorch opencloudos/opencloudos9-pytorch:2.8.0
```


容器启动后可以通过命令 sudo docker ps 看到已经启动的容器，容器 ID 请以实际为准。

```
[root@VM-0-250-opencloudos ~]# docker ps
CONTAINER ID IMAGE COMMAND CREATED STATUS PORTS NAMES
3ae21170922b opencloudos/opencloudos9-pytorch:2.8.0 "bash" 4 minutes ago Up 4 minutes opencloudos9-pytorch
```


可以使用以下命令进入此运行中的 Docker 容器：

** 方法1：使用 docker exec（推荐）**

```
sudo docker exec -it opencloudos9-pytorch bash
# 或者使用容器ID, 容器 ID 请以实际为准
sudo docker exec -it 3ae21170922b bash
```


方法2：使用 docker attach

```
sudo docker attach opencloudos9-pytorch
```


注意：使用 attach 命令时，如果容器中的 bash 会话退出，容器也会停止。

## 3.启动训练示例

容器的默认工作目录为 /workspace ，在此目录下已经准备好 PyTorch 官方的 examples 仓库。

通过如下命令启动 MNIST 训练示例：

```
# 多 GPU 环境注意设置环境变量，例如 CUDA_VISIBLE_DEVICES=2 python examples/mnist/main.py
[root@3ae21170922b workspace]# python examples/mnist/main.py
100.0%
100.0%
100.0%
100.0%
Train Epoch: 1 [0/60000 (0%)] Loss: 2.280212
Train Epoch: 1 [640/60000 (1%)] Loss: 1.254460
Train Epoch: 1 [1280/60000 (2%)] Loss: 0.844103
Train Epoch: 1 [1920/60000 (3%)] Loss: 0.667977
Train Epoch: 1 [2560/60000 (4%)] Loss: 0.496642
Train Epoch: 1 [3200/60000 (5%)] Loss: 0.508742
```


## 4.结果展示

该示例包含 14 轮 Epoch，最终结果如下：

```
...
Train Epoch: 14 [55680/60000 (93%)] Loss: 0.012501
Train Epoch: 14 [56320/60000 (94%)] Loss: 0.000175
Train Epoch: 14 [56960/60000 (95%)] Loss: 0.069470
Train Epoch: 14 [57600/60000 (96%)] Loss: 0.042674
Train Epoch: 14 [58240/60000 (97%)] Loss: 0.005742
Train Epoch: 14 [58880/60000 (98%)] Loss: 0.009076
Train Epoch: 14 [59520/60000 (99%)] Loss: 0.052920
Test set: Average loss: 0.0274, Accuracy: 9919/10000 (99%)
```


## 5.清理环境

退出容器后，通过如下命令停止运行容器。

```
# 停止容器但保留容器文件系统
docker stop opencloudos9-pytorch
# 或者使用容器 ID, 容器 ID 请以实际为准
docker stop 3ae21170922b
```


若停止容器运行后需要删除容器，请执行如下命令。

```
# 删除容器
docker rm opencloudos9-pytorch
# 或者使用容器 ID, 容器 ID 请以实际为准
docker rm 3ae21170922b
```