source: https://docs.mthreads.com/musa-deploy/musa-deploy-doc-online/user_guide/check

# Check

musa-deploy 工具可以对 MUSA 软件栈进行检查。如果检查的组件失败，该工具会依次回溯检查依赖的组件，直至找到问题根因。 检查命令形式如下：

`sudo musa-deploy -c|--check <组件名>`



可选组件名： **host**, **driver**, **container_toolkit**, **torch_musa**, **musa**, **smartio**, **ib**

## 1. 检查host环境[](https://docs.mthreads.com#1-检查host环境)

主要检查物理机器上基础软硬件信息，如 CPU 型号，操作系统，PCIE 版本等。注意，如果不加 **sudo**，有一些信息可能无法查看到，如 PCIE 版本信息。

`sudo musa-deploy -c host`



示例结果如下图：

## 2. 检查驱动信息[](https://docs.mthreads.com#2-检查驱动信息)

`# 参数缺省时，默认是检查driver`

sudo musa-deploy -c [driver]



示例结果如下图：

## 3. 检查容器套件[](https://docs.mthreads.com#3-检查容器套件)

如果需要在 docker 容器中使用 GPU 设备，需要绑定摩尔线程容器运行时容器运行时到 Docker，下面命令检查容器运行时套件状态：

`sudo musa-deploy -c container_toolkit`



示例结果如下图：

## 4. 检查musa环境[](https://docs.mthreads.com#4-检查musa环境)

用于检查 musa_toolkits 套件是否可用，经常在容器环境中被用到。该命令可验证套件与驱动的版本匹配状态，检查 MUSA 环境是否正常。

`sudo musa-deploy -c musa`



容器中执行命令示例结果如下图：

## 5. 检查torch_musa环境[](https://docs.mthreads.com#5-检查torch_musa环境)

`sudo musa-deploy -c torch_musa`



一般用于检查容器中 torch_musa 环境是否可用。

下面给出两个示例检测截图，其中一个 torch_musa 安装正常，另一个 torch_musa 未安装：


## 6. 检查SmartIO[](https://docs.mthreads.com#6-检查smartio)

`sudo musa-deploy -c smartio`



## 7. 检查IB[](https://docs.mthreads.com#7-检查ib)

`sudo musa-deploy -c ib`