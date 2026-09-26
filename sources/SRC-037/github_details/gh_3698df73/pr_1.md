# [PR #1] perf: reduce repeated Triton autotuning for L2Norm

source: https://github.com/Ascend/MindSpeed/pull/1
state: open | updated: 2026-08-26T14:22:17Z
labels: ascend-cla/no

## 正文

修复 L2Norm Triton kernel 在动态 token 数场景下因输入 T/NB 变化反复触发 autotune，导致训练 iteration 耗时异常增长的问题。


动态 shape / 动态 token 数训练时，L2Norm Triton kernel
会随着 T/NB 变化重复执行 autotune。

每次 autotune 需要遍历大量 BT × num_warps 配置，
单次可能耗时 20s+，多次累积导致一个训练 step 超过 10 分钟。

## 评论 (2)

### ascend-robot · 2026-08-26

Hello,

This repo is only a mirror with no active development or maintenance.
All bug reports, questions and code contributions should be submitted via the original repository link below.
Thanks for your interest!

Original Repository Link: https://gitcode.com/Ascend/MindSpeed

### ascend-robot · 2026-08-26

### CLA Signature Guide  

 @Kamleecoder , thanks for your pull request. 

The following commit(s) are not associated with a signed **<font color=green>_Contributor License Agreement (CLA)_</font>**.

| Commit | Reason |
|--|--|
| [484b4e7c  修复 L2Norm Triton kernel 在�...](https://github.com/Ascend/MindSpeed/commit/484b4e7c65f7776b9afb87a081a9f1ecd5bd064e) | the email used in the commit is not linked to a signed CLA! <br>please verify that it matches the email you used when signing the CLA. | 

To sign CLA, [**<ins>click here</ins>**](https://clasign.osinfra.cn/sign-cla/690ca9ddf91c03dee6082ab1/individual). 

To check if your email is configured correctly, refer to the [**<font color=red><ins>_FAQs_</ins></font>**](https://gitcode.com/Ascend/infrastructure/blob/master/docs/cla/cla%E4%BD%BF%E7%94%A8%E6%8C%87%E5%8D%97.md#faq). 

Once you've signed the CLA or updating your email, please comment **`/check-cla`** to revalidate CLA status.
