# [Issue #91] 昇腾 910B 训练效率显著低于英伟达 A100

source: https://github.com/Ascend/pytorch/issues/91
state: open | updated: 2025-11-18T12:49:46Z
labels: 

## 正文

使用 [RAGEN](https://github.com/mll-lab-nu/RAGEN) 框架进行 RL 训练，在相同实验配置下，华为昇腾 910B 的训练耗时明显高于英伟达 A100。在4个任务上进行200step训练，耗时情况如下（单位min），华为昇腾910B平均耗时约为英伟达A100的2至3倍：
| actor_loss | critic_loss | think | bandit (nvidia) | bandit (huawei) | sokoban (nvidia) | sokoban (huawei) | frozenlake (nvidia) | frozenlake (huawei) | countdown (nvidia) | countdown (huawei) |
|-------------|--------------|--------|------------------|------------------|------------------|------------------|---------------------|---------------------|---------------------|---------------------|
| 1.00E-05 | 9.00E-06 | no  | 11.25 | 33.19 | 20.00 | 52.21 | 15.82 | 35.71 | 14.59 | 28.93 |
| 1.00E-05 | 9.00E-06 | yes | 16.06 | 47.35 | 19.80 | 51.21 | 17.45 | 40.20 | 18.00 | 46.89 |
| 1.00E-06 | 9.00E-06 | no  | 11.20 | 28.51 | 20.04 | 49.84 | 13.80 | 27.40 | 14.31 | 34.50 |
| 1.00E-06 | 9.00E-06 | yes | 12.84 | 35.58 | 20.56 | 51.12 | 14.98 | 32.68 | 16.19 | 34.15 |
| 1.00E-07 | 9.00E-06 | no  | 13.49 | 30.64 | 18.23 | 46.04 | 15.16 | 33.01 | 16.10 | 40.38 |
| 1.00E-07 | 9.00E-06 | yes | 15.87 | 37.69 | 19.14 | 48.87 | 16.66 | 38.12 | 17.41 | 40.26 |

## 评论 (1)

### yunyiyun · 2025-11-18

可参考资料进行性能调优
https://www.hiascend.com/document/detail/zh/Pytorch/720/ptmoddevg/trainingmigrguide/performance_tuning_0001.html
