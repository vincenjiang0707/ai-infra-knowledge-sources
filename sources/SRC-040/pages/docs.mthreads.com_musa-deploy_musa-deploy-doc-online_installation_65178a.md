source: https://docs.mthreads.com/musa-deploy/musa-deploy-doc-online/installation

# 安装指导

## 安装步骤[](https://docs.mthreads.com#安装步骤)

`sudo pip install musa-deploy`


# 如果安装过程中出现超时报错，或者安装预估时间过长，可以尝试指定清华源：

# sudo pip install musa-deploy -i https://mirrors.tuna.tsinghua.edu.cn/pypi/web/simple



提示

- 该工具目前仅支持摩尔线程发布的 s70，s80，s3000，s4000 GPU 设备，后续版本会支持更多摩尔线程 GPU 设备。
- 如果安装时没有添加
**sudo**，执行 musa-deploy 命令时却加了**sudo**，可能会无法找到该命令。如果报错无法找到该命令，需要用 musa-deploy 命令的绝对路径来执行，或者`sudo env PATH=$PATH musa-deploy`

。不用**sudo**安�装时:- 如果是 conda 管理 python 环境，命令可能会安装到
`/home/xxx_用户/miniconda3/envs/xxx_conda_环境/bin/`

。 - 如果是非 conda 环境，命令可能会安装到
`/home/xxx_用户/.local/bin`

下。

- 如果是 conda 管理 python 环境，命令可能会安装到