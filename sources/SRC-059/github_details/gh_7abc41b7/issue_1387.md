# [Issue #1387] Prerequisites 环境要求太高了

source: https://github.com/PaddlePaddle/ERNIE/issues/1387
state: open | updated: 2025-12-17T03:21:57Z
labels: 

## 正文

<img width="477" height="286" alt="Image" src="https://github.com/user-attachments/assets/555f8b03-f7d3-4dbe-91ae-342c6df9563e" />

很多公司的物理机 cuda driver 都是在12.1、12.2的，这个版本比较稳定，既然支持的是12.x，为什么不能降低点版本呢，这种方式会把好多潜在用户放弃了，总不能让用户把底层都升级一遍来适配ernie吧，那么多业务在跑，大家只能被逼去友商了

## 评论 (3)

### risemeup1 · 2025-12-02

525.x的驱动也可以用的，你试一下。从 “能否运行” 的角度看，只要用户驱动是 525 或更高，12.3/12.6/12.9 包理论上都能运行的。但从 “最佳性能和稳定性” 的角度看，较新版本 CUDA 最好搭配较新的驱动。

### biandh · 2025-12-03

> 525.x的驱动也可以用的，你试一下。从 “能否运行” 的角度看，只要用户驱动是 525 或更高，12.3/12.6/12.9 包理论上都能运行的。但从 “最佳性能和稳定性” 的角度看，较新版本 CUDA 最好搭配较新的驱动。

CUDA Toolkit: 12.1
CUDA Version: 12.1
CUDA  Driver: 525.x

不是只有Driver，Version也是物理机上的，很难升级的，上面这个配置能否支持呢

### nepeplwu · 2025-12-17

@biandh 可以试着跑下看看，如果有报错我们跟进看下
