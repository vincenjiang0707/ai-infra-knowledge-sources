# [Issue #1048] loss_mask 在训练时候出现问题，nonetype object is not  subscriptable

source: https://github.com/PaddlePaddle/ERNIE/issues/1048
state: closed | updated: 2025-10-23T12:00:49Z
labels: 

## 正文

![Image](https://github.com/user-attachments/assets/cfaffc66-adf4-40f6-897e-36f807a613a7)


使用ms-swift训练时候模型loss_mask部分出现问题，如图：

transformers==4.52.4

peft==0.15.2

deepspeed==0.15.2

ms-swift==3.6.2

## 评论 (2)

### nepeplwu · 2025-07-24

@xiaochounikuaixiao ms-swift代码不由我们维护，可以到他们仓库里提问下，也可以试试直接用我们的代码进行训练：
https://github.com/PaddlePaddle/ERNIE/blob/develop/docs/erniekit.md

### nepeplwu · 2025-10-23

The issue has no response for a long time and will be closed. You can reopen or new another issue if are still confused.

---
_From Bot_
