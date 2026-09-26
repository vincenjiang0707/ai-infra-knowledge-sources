# [Issue #356] Out of bounds values FAILED when running hypercube_perf with 4 GPUs (0,1,2,3)

source: https://github.com/NVIDIA/nccl-tests/issues/356
state: closed | updated: 2025-11-13T01:31:28Z
labels: 

## 正文

Hi,

When I run hypercube_perf with 2 GPUs, everything works correctly.
For example, the following combinations produce normal results:

` ./hypercube_perf -b 8 -e 8g -f 2 -g 2 -d 0,1` 
` ./hypercube_perf -b 8 -e 8g -f 2 -g 2 -d 0,2` 
` ./hypercube_perf -b 8 -e 8g -f 2 -g 2 -d 0,3 ` 


All of them show:

` Out of bounds values : 0 OK` 


However, when I run the same test with 4 GPUs:

` ./hypercube_perf -b 8 -e 8g -f 2 -g 4 -d 0,1,2,3` 


I get the following error:

` Out of bounds values : 56 FAILED` 


Could you please help identify what might be causing this issue?

System Information:

OS: Ubuntu 22.04.5

NCCL Version: 2.28.3 + CUDA 13.0

GPU : NVIDIA GeForce RTX 5090

Command used:

./hypercube_perf -b 8 -e 8g -f 2 -g 4


Additional Notes:

The error only occurs when using 4 GPUs.

2-GPU tests consistently pass without any “Out of bounds values” failure.

Thanks in advance for your help and time!

## 评论 (2)

### sjeaugey · 2025-11-03

Just to set expectations, this test is not as reliable as the others, doesn't support all numbers of ranks.. and is not a test we use often ourselves.

So if all other tests work fine on your machine, it could well be a bug in the test itself.

### Dazui-Wang · 2025-11-13

Ok, I verify that the other child items do not have this phenomenon. Thank you for your reply.

> Just to set expectations, this test is not as reliable as the others, doesn't support all numbers of ranks.. and is not a test we use often ourselves.需要说明的是，这个测试的可靠性不如其他测试，不支持所有进程数量，而且我们自己也不常使用。
> 
> So if all other tests work fine on your machine, it could well be a bug in the test itself.因此，如果其他测试在您的机器上都能正常运行，那很可能是这个测试本身存在缺陷。


