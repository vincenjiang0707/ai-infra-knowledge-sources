# [Issue #521] The question: is there an example of direct GPU-to-GPU send and receive operations?

source: https://github.com/ROCm/rccl/issues/521
state: closed | updated: 2022-04-01T11:51:16Z
labels: 

## 正文

Hello!
Thank you, colleagues, for a great library!

I'd like to try to work with a direct GPU-to-GPU send and receive operations. Is there any example (or test) in the repository?

## 评论 (3)

### gilbertlee-amd · 2022-03-31

Hi, 
Aside from the description of ncclSend/ncclRecv in the header file, there is a minor example that you can see here: https://github.com/ROCmSoftwarePlatform/rccl/blob/develop/test/common/TestBedChild.cpp#L461, which arises from the unit test here: https://github.com/ROCmSoftwarePlatform/rccl/blob/develop/test/SendRecv_SinglePairs.cpp



### gilbertlee-amd · 2022-03-31

There's also an example within the AllToAll collective, which uses ncclSend/ncclRecv under the hood:
https://github.com/ROCmSoftwarePlatform/rccl/blob/develop/src/collectives/all_to_all_api.cc#L28

### vasslavich · 2022-04-01

Great. Thanks @gilbertlee-amd ! It looks like I need.
