# [Issue #60] AttributeError: module 'torch_npu' has no attribute '_npu_rotary_embedding'

source: https://github.com/Ascend/pytorch/issues/60
state: open | updated: 2025-03-24T07:11:46Z
labels: 

## 正文

torch-npu in /usr/local/python3.10.2/lib/python3.10/site-packages (2.4.0.post2)

如题，有版本带有这个'_npu_rotary_embedding‘嘛？

## 评论 (1)

### zhangsan5213 · 2025-03-04

```
wget https://pytorch-package.obs.cn-north-4.myhuaweicloud.com/pta/Daily/v2.5.1/20250226.4/pytorch_v2.5.1_py310.tar.gz
tar -xvf pytorch_v2.5.1_py310.tar.gz
pip install ./torch_npu-2.5.1.dev20250226-cp310-cp310-manylinux_2_17_aarch64.manylinux2014_aarch64.whl
```

还需要nnal
```
wget https://ascend-repo.obs.cn-east-2.myhuaweicloud.com/CANN/CANN%208.0.0/Ascend-cann-nnal_8.0.0_linux-aarch64.run
chmod +x ./Ascend-cann-nnal_8.0.0_linux-aarch64.run
./Ascend-cann-nnal_8.0.0_linux-aarch64.run --install
```

然后在你的~/.bashrc加上这个
```
source /usr/local/Ascend/nnal/atb/set_env.sh
```
