# [Issue #949] VIT Packed sequence轮转划分算法

source: https://github.com/PaddlePaddle/ERNIE/issues/949
state: closed | updated: 2025-09-30T12:01:07Z
labels: 

## 正文

”在 ViT 编码器的数据并行组中，按 token 数升序排列所有 packed sequence。然后，采用轮转划分算法，将这些 sequence 分配至各个设备，使每个设备上的总 token 数尽量均衡”
![Image](https://github.com/user-attachments/assets/dffb81bb-254c-43ef-8120-72ad0fff8717)

这里会导致DP15的token数大于DP0，更改一下分配算法会不会好一点， 第一轮DP0、DP1......DP14、DP15， 第二轮DP15、DP14......DP1、DP0，第三轮DP0、DP1......DP14、DP15

## 评论 (3)

### jerrywgz · 2025-07-01

你提的轮转方式是可行的，之前有尝试过对整体性能提升较小。这个策略是粗粒度的保障大卡训练过程中不同DP的token数均衡，但是训练过程中的几张极大图，会导致不同DP还是存在不均衡问题，不同的轮转方式差异不明显

### jerrywgz · 2025-07-01

另外还有一种情况是训练过程中会出现图像数量无法被DP整除的情况，这样顺序轮转的方式也会相对更均衡些 总之这个策略是以图像维度的，由于图像数量和大小差异较大，所以只是先做了粗粒度均衡

### nepeplwu · 2025-09-30

The issue has no response for a long time and will be closed. You can reopen or new another issue if are still confused.

---
_From Bot_
