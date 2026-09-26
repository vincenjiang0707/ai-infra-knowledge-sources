# [Issue #983] 【需求/建议】提供 Paddle 版本 Pretrain / Post-Training 开箱即用的镜像

source: https://github.com/PaddlePaddle/ERNIE/issues/983
state: closed | updated: 2025-10-09T12:00:56Z
labels: 

## 正文

有没有可以直接用的训练镜像？包括 Pretrain / Post-Training 的镜像，使用这个readme 中提供的镜像还是需要安装大量的包，希望能有个开箱即用的镜像，方便微调，谢谢。

ccr-2vdh3abv-pub.cnc.bj.baidubce.com/paddlepaddle/paddle:3.1.0-gpu-cuda12.9-cudnn9.9

python -m pip install -r requirements.txt --force-reinstall

![Image](https://github.com/user-attachments/assets/033fb4e4-fc55-410e-87aa-99d6ad79ea40)



## 评论 (2)

### a31413510 · 2025-07-10

可以参考下面这个pr，使用Dockerfile自行构建镜像，其中提供的Dockerfile已包含ERNIEKIT的全部依赖，同时，你也可以根据自己需求修改Dockerfile，增加其它需要的内容
https://github.com/PaddlePaddle/ERNIE/pull/1007

### nepeplwu · 2025-10-09

The issue has no response for a long time and will be closed. You can reopen or new another issue if are still confused.

---
_From Bot_
