# [Issue #1001] Why spent more than 20 minutes when rebuilding the RCCL project?

source: https://github.com/ROCm/rccl/issues/1001
state: closed | updated: 2024-01-11T23:40:08Z
labels: 

## 正文

Hi Dear developper,
I found that when rebuing the RCCL project by modifing such as the common.h, the whole compiling procedure will last for more than 20 minusts, it will reduce debugging efficiency, can you give me some comments to accelerate the compile speed?
Thanks a lot!

Leo

## 评论 (5)

### BertanDogancay · 2023-12-04

Hello, 

Common.h is used in various places in RCCL and If modified, all files including it must be recompiled. For faster build times, I would suggest using the '-l' (compile only for local gpu architecture) flag that can be found in the install script when building RCCL from scratch or even '--fast' if MSCCL is not needed . This way, when a file is modified, incremental build should also be faster.

### shanleo2024 · 2023-12-05

Hi Bertan,
Thank you for your suggestion, I wander how to use '-l' or '--fast' when rebuing?
Just make -l?
I usually buind the RCCL project using the following steps according the README.md:
$ cd rccl
$ mkdir build
$ cd build
$ CXX=/opt/rocm/bin/hipcc cmake -DCMAKE_PREFIX_PATH=/opt/rocm/ ..
$ **make -j 16**      # Or some other suitable number of parallel jobs

Can you give me an example how to use the ‘-l’ to increace the build speed, thanks a lot!

Leo

### BertanDogancay · 2023-12-05

**Two Options to build RCCL:**
1. Manual build: (local gpu arch only flag passed in)
 ``` command
cd rccl
mkdir build
cd build
CXX=/opt/rocm/bin/hipcc cmake -DCMAKE_PREFIX_PATH=/opt/rocm/ -DBUILD_LOCAL_GPU_TARGET_ONLY=ON ..
make -j 16
 ```
2. Via install.sh script: (with local gpu arch flag)
```command
cd rccl
./install.sh -l
```

if you do ./install.sh --help you can see the list of flags that can be passed in when building RCCL and for manual build, you can always try to do make -j $(nproc) instead of make -j 16. That way, it will try to use all the number of processors available in the system while compiling.

### shanleo2024 · 2023-12-05

Hi Bertan @BertanDogancay 
Thank you for your kind commentes, it is usful for me, I will try it later.
And I have another question, I cannot make break points through hipgdb in RCCL kernel functions, it only work for the functions which can run on the CPU.
So can you give me some comments once more about how to use the hipgdb on the RCCL kernel functions?
The CXX command as follows:

CXX=hipcc /home/shanxs/cmake/cmake_install/cmake-3.27.5-linux-x86_64/bin/cmake -DCMAKE_INSTALL_PREFIX=/home/shanxs/RCCL_code/install -DAMDGPU_TARGETS="gfx926" -DBUILD_TESTS=OFF -DCMAKE_BUILD_TYPE=**Debug** ..

Thank you.

Leo



### akolliasAMD · 2024-01-11

@shanleo1986 
We build this way and we normally use rocgdb. You can find documentation for it here: https://rocm.docs.amd.com/projects/ROCgdb/en/latest/ROCgdb/gdb/doc/gdb/index.html 
When I use it with rccl I use the following flags, you might find them useful:
set detach-on-fork off
set non-stop on
set amdgpu precise-memory on
set follow-fork-mode child

Closing this as an issue so the conversation does not get out of context here!
Thanks, Aristotle
