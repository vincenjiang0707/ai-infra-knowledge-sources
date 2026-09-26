# [Issue #4] samples/cplusplus/level2_simple_inference/0_data_process/vdecandvenc aclrtContext not created

source: https://github.com/Ascend/samples/issues/4
state: closed | updated: 2022-04-20T19:37:58Z
labels: 

## 正文

video_decode.cpp:125:
```cpp
aclRet = aclrtGetCurrentContext(&context_);
```
returns error 107002 because no context has been created yet, so `VideoDecode::Open()` fails

## 评论 (1)

### ascendhuawei · 2021-09-24

Thanks, we will look into the issue and keep you updated 
