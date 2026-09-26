# [Issue #1370] [Issue]: Running rccl on chameleon (tacc)

source: https://github.com/ROCm/rccl/issues/1370
state: closed | updated: 2024-11-04T11:12:18Z
labels: Under Investigation

## 正文

### Problem Description

I tried to run rccl-tests and rccl integrated tests on the mi100 nodes on the chameleon cloud (tacc). It sometimes worked with one gpu, but never with 2 (nodes have 2 gpus). 
Output of rccl integrated tests : 
================================================================================
 Environment variables:
 - UT_SHOW_NAMES        Show test case names                       (  1) <unset>
 - UT_MIN_GPUS          Minimum number of GPUs to use              (  2) 2
 - UT_MAX_GPUS          Maximum number of GPUs to use              (  2) <unset>
 - UT_POW2_GPUS         Only allow power-of-2 # of GPUs            (  0) <unset>
 - UT_PROCESS_MASK      Whether to run single/multi process        (  3) <unset>
 - UT_VERBOSE           Show verbose unit test output              (  0) <unset>
 - UT_REDOPS            List of reduction ops to test              ( -1) <unset>
 - UT_DATATYPES         List of datatypes to test                  ( -1) <unset>
 - UT_MAX_RANKS_PER_GPU Maximum number of ranks using the same GPU (  1) <unset>
 - UT_PRINT_VALUES      Print array values (-1 for all)            (  0) <unset>
 - UT_SHOW_TIMING       Show timing table                          (  1) <unset>
 - UT_INTERACTIVE       Run in interactive mode                    (  0) <unset>
 - UT_TIMEOUT_US        Timeout limit for collective calls in us   (5000000) <unset>
 - UT_MULTITHREAD       Multi-thread single-process ranks          (  0) <unset>
================================================================================
[==========] Running 64 tests from 13 test suites.
[----------] Global test environment set-up.
[----------] 6 tests from AllGather
[ RUN      ] AllGather.OutOfPlace
^[[0;31m[ ERROR    ] ^[[0mChild 0 reports failure
/home/cc/rccl/test/common/TestBed.cpp:183: Failure
Expected equality of these values:
  response
    Which is: 1
  TEST_SUCCESS
    Which is: 0
^[[0;31m[ ERROR    ] ^[[0mChild process 0 fails NCCL call ncclGroupEnd with code 1
^[[0;31m[ ERROR    ] ^[[0mChild 0 failed on command [INIT_COMMS]:
[  FAILED  ] AllGather.OutOfPlace (1529 ms)
[ RUN      ] AllGather.OutOfPlaceGraph
^[[0;31m[ ERROR    ] ^[[0mChild 0 reports failure
/home/cc/rccl/test/common/TestBed.cpp:183: Failure
Expected equality of these values:
  response
    Which is: 1
  TEST_SUCCESS
    Which is: 0
^[[0;31m[ ERROR    ] ^[[0mChild process 0 fails NCCL call ncclGroupEnd with code 1
^[[0;31m[ ERROR    ] ^[[0mChild 0 failed on command [INIT_COMMS]:
[  FAILED  ] AllGather.OutOfPlaceGraph (1496 ms)
[ RUN      ] AllGather.InPlace
^[[0;31m[ ERROR    ] ^[[0mChild 0 reports failure
/home/cc/rccl/test/common/TestBed.cpp:183: Failure
Expected equality of these values:
  response
    Which is: 1
  TEST_SUCCESS
    Which is: 0
^[[0;31m[ ERROR    ] ^[[0mChild process 0 fails NCCL call ncclGroupEnd with code 1
^[[0;31m[ ERROR    ] ^[[0mChild 0 failed on command [INIT_COMMS]:
[  FAILED  ] AllGather.InPlace (1500 ms)
[ RUN      ] AllGather.InPlaceGraph
^[[0;31m[ ERROR    ] ^[[0mChild 0 reports failure
/home/cc/rccl/test/common/TestBed.cpp:183: Failure
Expected equality of these values:
  response
    Which is: 1
  TEST_SUCCESS
    Which is: 0
^[[0;31m[ ERROR    ] ^[[0mChild process 0 fails NCCL call ncclGroupEnd with code 1
^[[0;31m[ ERROR    ] ^[[0mChild 0 failed on command [INIT_COMMS]:
[  FAILED  ] AllGather.InPlaceGraph (1504 ms)
[ RUN      ] AllGather.ManagedMem
^[[0;31m[ ERROR    ] ^[[0mChild 0 reports failure
/home/cc/rccl/test/common/TestBed.cpp:183: Failure
Expected equality of these values:
  response
    Which is: 1
  TEST_SUCCESS
    Which is: 0
^[[0;31m[ ERROR    ] ^[[0mChild process 0 fails NCCL call ncclGroupEnd with code 1
^[[0;31m[ ERROR    ] ^[[0mChild 0 failed on command [INIT_COMMS]:
[  FAILED  ] AllGather.ManagedMem (1500 ms)
[ RUN      ] AllGather.ManagedMemGraph
^[[0;31m[ ERROR    ] ^[[0mChild 0 reports failure
/home/cc/rccl/test/common/TestBed.cpp:183: Failure
Expected equality of these values:
  response
    Which is: 1
  TEST_SUCCESS
    Which is: 0
^[[0;31m[ ERROR    ] ^[[0mChild process 0 fails NCCL call ncclGroupEnd with code 1
^[[0;31m[ ERROR    ] ^[[0mChild 0 failed on command [INIT_COMMS]:
[  FAILED  ] AllGather.ManagedMemGraph (1527 ms)
[----------] 6 tests from AllGather (9057 ms total)

[----------] 8 tests from AllReduce
[ RUN      ] AllReduce.OutOfPlace
^[[0;31m[ ERROR    ] ^[[0mChild 0 reports failure
/home/cc/rccl/test/common/TestBed.cpp:183: Failure
Expected equality of these values:
  response
    Which is: 1
  TEST_SUCCESS
    Which is: 0
^[[0;31m[ ERROR    ] ^[[0mChild process 0 fails NCCL call ncclGroupEnd with code 1
^[[0;31m[ ERROR    ] ^[[0mChild 0 failed on command [INIT_COMMS]:
[  FAILED  ] AllReduce.OutOfPlace (1511 ms)
[ RUN      ] AllReduce.OutOfPlaceGraph
^[[0;31m[ ERROR    ] ^[[0mChild 0 reports failure
/home/cc/rccl/test/common/TestBed.cpp:183: Failure
Expected equality of these values:
  response
    Which is: 1
  TEST_SUCCESS
    Which is: 0
^[[0;31m[ ERROR    ] ^[[0mChild process 0 fails NCCL call ncclGroupEnd with code 1
^[[0;31m[ ERROR    ] ^[[0mChild 0 failed on command [INIT_COMMS]:
[  FAILED  ] AllReduce.OutOfPlaceGraph (1504 ms)
[ RUN      ] AllReduce.InPlace
^[[0;31m[ ERROR    ] ^[[0mChild 0 reports failure
/home/cc/rccl/test/common/TestBed.cpp:183: Failure
Expected equality of these values:
  response
    Which is: 1
  TEST_SUCCESS
    Which is: 0
^[[0;31m[ ERROR    ] ^[[0mChild process 0 fails NCCL call ncclGroupEnd with code 1
^[[0;31m[ ERROR    ] ^[[0mChild 0 failed on command [INIT_COMMS]:
[  FAILED  ] AllReduce.InPlace (1499 ms)
[ RUN      ] AllReduce.InPlaceGraph
^[[0;31m[ ERROR    ] ^[[0mChild 0 reports failure
/home/cc/rccl/test/common/TestBed.cpp:183: Failure
Expected equality of these values:
  response
    Which is: 1
  TEST_SUCCESS
    Which is: 0
^[[0;31m[ ERROR    ] ^[[0mChild process 0 fails NCCL call ncclGroupEnd with code 1
^[[0;31m[ ERROR    ] ^[[0mChild 0 failed on command [INIT_COMMS]:
[  FAILED  ] AllReduce.InPlaceGraph (1508 ms)
[ RUN      ] AllReduce.ManagedMem
^[[0;31m[ ERROR    ] ^[[0mChild 0 reports failure
/home/cc/rccl/test/common/TestBed.cpp:183: Failure
Expected equality of these values:
  response
    Which is: 1
  TEST_SUCCESS
    Which is: 0
^[[0;31m[ ERROR    ] ^[[0mChild process 0 fails NCCL call ncclGroupEnd with code 1
^[[0;31m[ ERROR    ] ^[[0mChild 0 failed on command [INIT_COMMS]:
[  FAILED  ] AllReduce.ManagedMem (1507 ms)
[ RUN      ] AllReduce.Channels
[       OK ] AllReduce.Channels (289 ms)
[ RUN      ] AllReduce.ManagedMemGraph
^[[0;31m[ ERROR    ] ^[[0mChild 0 reports failure
/home/cc/rccl/test/common/TestBed.cpp:183: Failure
Expected equality of these values:
  response
    Which is: 1
  TEST_SUCCESS
    Which is: 0
^[[0;31m[ ERROR    ] ^[[0mChild process 0 fails NCCL call ncclGroupEnd with code 1
^[[0;31m[ ERROR    ] ^[[0mChild 0 failed on command [INIT_COMMS]:
[  FAILED  ] AllReduce.ManagedMemGraph (1525 ms)
[ RUN      ] AllReduce.PreMultScalar
^[[0;31m[ ERROR    ] ^[[0mChild 0 reports failure
/home/cc/rccl/test/common/TestBed.cpp:183: Failure
Expected equality of these values:
  response
    Which is: 1
  TEST_SUCCESS
    Which is: 0
[ INFO     ] SP 2-ranks AllReduce (custom-scalar Mode 0 ncclFloat32)
^[[0;31m[ ERROR    ] ^[[0mChild 0 pipe closed unexpectedly

### Operating System

Ubuntu 22.04 LTS (Jammy Jellyfish)

### CPU

AMD EPYC 7763 64-Core Processor

### GPU

AMD Instinct MI100

### ROCm Version

ROCm 6.2.0

### ROCm Component

rccl

### Steps to Reproduce

sudo apt update
sudo apt install "linux-headers-$(uname -r)" "linux-modules-extra-$(uname -r)"
sudo usermod -a -G render,video $LOGNAME # Add the current user to the render and video groups
wget https://repo.radeon.com/amdgpu-install/6.2.2/ubuntu/noble/amdgpu-install_6.2.60202-1_all.deb
sudo apt install ./amdgpu-install_6.2.60202-1_all.deb
sudo apt update
sudo apt install amdgpu-dkms rocm
$ git clone --recursive https://github.com/ROCm/rccl.git
$ cd rccl
./install.sh -d -i -t
cd build/release/test/
UT_MIN_GPUS=2 ./rccl-UnitTests

### (Optional for Linux users) Output of /opt/rocm/bin/rocminfo --support

_No response_

### Additional Information

........................................................................................
          RocmBandwidthTest Version: 2.6.0

          Launch Command is: rocm-bandwidth-test (rocm_bandwidth -a + rocm_bandwidth -A)


          Device: 0,  AMD EPYC 7763 64-Core Processor
          Device: 1,  AMD EPYC 7763 64-Core Processor
          Device: 2,  AMD Instinct MI100,  GPU-4a6fa69c0466a0f6,  23:0.0
          Device: 3,  AMD Instinct MI100,  GPU-7d83d710d99c6228,  83:0.0

          Inter-Device Access

          D/D       0         1         2         3         

          0         1         1         1         1         

          1         1         1         1         1         

          2         1         1         1         1         

          3         1         1         1         1         


          Inter-Device Numa Distance

          D/D       0         1         2         3         

          0         0         32        20        52        

          1         32        0         52        20        

          2         20        52        0         72        

          3         52        20        72        0         


          Unidirectional copy peak bandwidth GB/s

          D/D       0           1           2           3           

          0         N/A         N/A         28.349      26.813      

          1         N/A         N/A         24.861      28.351      

          2         28.527      25.018      925.889     48.902      

          3         11.283      28.531      49.920      887.683     


          Bidirectional copy peak bandwidth GB/s

          D/D       0           1           2           3           

          0         N/A         N/A         51.807      26.001      

          1         N/A         N/A         24.885      51.804      

          2         51.807      24.885      N/A         97.678      

          3         26.001      51.804      97.678      N/A         



## 评论 (3)

### ppanchad-amd · 2024-10-28

Hi @monsieurconan. Internal ticket has been created to investigate your issue. Thanks!

### tcgu-amd · 2024-10-30

Hi @monsieurconan, thanks for reaching out! Could you elaborate a bit more on what you mean by "sometimes works" on one GPU? Also, to provide us with more context, could you try running the tests with the environmental variable `NCCL_DEBUG=INFO`? Thanks!

### monsieurconan · 2024-11-04

Hello, the issue has been resolved thanks to an update by the chameleon team, it was probably an issue with the booting script. What I meaned by "sometimes working on on GPU" was that collectives operations (but not sendrecv) would work on one gpu, but only if rocm was installed with the package manager, and with ubuntu24 (not 22).
