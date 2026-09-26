# [Issue #325] SIGFPE when minbytes exceeds GPU memory limit

source: https://github.com/NVIDIA/nccl-tests/issues/325
state: closed | updated: 2025-07-30T06:12:23Z
labels: 

## 正文

I executed with identical minbytes and maxbytes and they both exceeds 1/2 of the device memory size.

it doesn't update `minbytes` here

https://github.com/NVIDIA/nccl-tests/blob/97ee0985165722717d340f1adb7c162bc8a7491d/src/common.cu#L1053

at warm-up for small size

https://github.com/NVIDIA/nccl-tests/blob/97ee0985165722717d340f1adb7c162bc8a7491d/src/common.cu#L349

gets `args->maxbytes < totalnbytes`, then `steps == 0`

https://github.com/NVIDIA/nccl-tests/blob/97ee0985165722717d340f1adb7c162bc8a7491d/src/common.cu#L350

 and `iter % steps` triggers SIGFPE `Floating point exception: integer divide by zero`.

In such case, running with data size out of user specified range may be confusing.
let it fail with some error message would be better than a SIGFPE.



## 评论 (2)

### AddyLaddy · 2025-07-24

I've recently pushed a change that may fix this. Can you give it a try?


### fishautumn · 2025-07-30

Thanks @AddyLaddy for fixing it!

It doesn't fail anymore.
