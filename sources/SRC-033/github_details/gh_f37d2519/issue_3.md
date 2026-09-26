# [Issue #3] Can't compile samples/cplusplus/level2_simple_inference/0_data_process/vdecandvenc

source: https://github.com/Ascend/samples/issues/3
state: closed | updated: 2022-04-20T19:37:33Z
labels: 

## 正文

Does not compile, following the instructions. I don't see any code in src/CMakeLists.txt that would include `samples/cplusplus/common/presenteragent/...` which explains the error:
```
/.../inc/object_detect.h:24:10: fatal error: presenter/agent/presenter_channel.h: No such file or directory
 #include "presenter/agent/presenter_channel.h"
```

## 评论 (3)

### ascendhuawei · 2021-09-22

Hi, reyoda,
In the readme, it specifies a wrong directory for compile, which should be:

cd $HOME/samples/cplusplus/level2_simple_inference/0_data_process/vdecandvenc
mkdir -p build/intermediates/host

Please check if this is the possible cause

### reyoda · 2021-09-23

That's what I did. What are the prerequisites for being able to compile vdecandvenc? 

Is src/CMakeLists.txt correct? It doesn't seem to include presenteragent in any way. 

I also tried removing references to presenteragent from the sample code, but then acl could not be found. I've installed Ascend as root user in /usr/local/Ascend as per the instructions

### ascendhuawei · 2021-09-23

It is because the presenter server is a dependency of the 'Atlas Utils', which is under the 'common' folder, although it is not used in this project.
To resolve the issue, please add following lines after line 56 of samples/cplusplus/level2_simple_inference/0_data_process/vdecandvenc/src/CMakeLists.txt 
```
../../../../common/presenteragent/include/ 
../../../../common/presenteragent/include/ascenddk
```
