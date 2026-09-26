# [Issue #908] rccl tests failing on ncclGroupEnd

source: https://github.com/ROCm/rccl/issues/908
state: closed | updated: 2024-07-18T21:39:32Z
labels: 

## 正文

Hi, When I tried to run the tests for building rccl(`NCCL_DEBUG=WARN ./install.sh --run_tests_all --verbose`), I got this error output

```
[==========] Running 7 tests from 1 test suite.
[----------] Global test environment set-up.
[----------] 7 tests from AllReduce
[ RUN      ] AllReduce.OutOfPlace
[ INFO     ] Calling PIPE_READ to Child 0

sharbox-ultra:204802:204802 [0] /home/elias/rccl/build/release/hipify/src/init.cc:125 NCCL WARN Missing "amd_iommu=on" from kernel command line which can lead to system instablity or hang!

sharbox-ultra:204802:204802 [0] /home/elias/rccl/build/release/hipify/src/init.cc:127 NCCL WARN Missing "iommu=pt" from kernel command line which can lead to system instablity or hang!

sharbox-ultra:204802:204802 [0] /home/elias/rccl/build/release/hipify/src/init.cc:132 NCCL WARN Missing "HSA_FORCE_FINE_GRAIN_PCIE=1" from environment which can lead to low RCCL performance, system instablity or hang!
[ INFO     ] Got PIPE_READ 128 from Child 0
[ INFO     ] Calling PIPE_READ to Child 0
[ INFO     ] Got PIPE_READ 4 from Child 0
[ INFO     ] Calling PIPE_READ to Child 0
RCCL version 2.18.3+hip5.5 develop:6ecf771+

sharbox-ultra:204802:204836 [1] /home/elias/rccl/build/release/hipify/src/transport/p2p.cc:220 NCCL WARN hipIpcGetMemHandle failed : invalid argument

sharbox-ultra:204802:204836 [1] /home/elias/rccl/build/release/hipify/src/transport/p2p.cc:222 NCCL WARN Cuda failure 'invalid argument'

sharbox-ultra:204802:204836 [1] /home/elias/rccl/build/release/hipify/src/proxy.cc:1524 NCCL WARN [Proxy Service 1] Failed to execute operation Setup from rank 1, retcode 1

sharbox-ultra:204802:204837 [0] /home/elias/rccl/build/release/hipify/src/transport/p2p.cc:220 NCCL WARN hipIpcGetMemHandle failed : invalid argument

sharbox-ultra:204802:204837 [0] /home/elias/rccl/build/release/hipify/src/transport/p2p.cc:222 NCCL WARN Cuda failure 'invalid argument'

sharbox-ultra:204802:204837 [0] /home/elias/rccl/build/release/hipify/src/proxy.cc:1524 NCCL WARN [Proxy Service 0] Failed to execute operation Setup from rank 0, retcode 1

sharbox-ultra:204802:204835 [1] /home/elias/rccl/build/release/hipify/src/misc/socket.cc:57 NCCL WARN socketProgress: Connection closed by remote peer sharbox-ultra<48295>

sharbox-ultra:204802:204835 [1] /home/elias/rccl/build/release/hipify/src/proxy.cc:1148 NCCL WARN Socket recv failed while polling for opId=0x7fe95066b760

sharbox-ultra:204802:204834 [0] /home/elias/rccl/build/release/hipify/src/misc/socket.cc:57 NCCL WARN socketProgress: Connection closed by remote peer sharbox-ultra<35867>

sharbox-ultra:204802:204834 [0] /home/elias/rccl/build/release/hipify/src/proxy.cc:1148 NCCL WARN Socket recv failed while polling for opId=0x7fe958288240
[ ERROR    ] Child process 0 fails NCCL call ncclGroupEnd with code 3
[ ERROR    ] Child 0 failed on command [INIT_COMMS]:
[ INFO     ] Got PIPE_READ 4 from Child 0
[ ERROR    ] Child 0 reports failure
/home/elias/rccl/test/common/TestBed.cpp:178: Failure
Expected equality of these values:
  response
    Which is: 1
  TEST_SUCCESS
    Which is: 0
[  FAILED  ] AllReduce.OutOfPlace (665 ms)
```

Do you have any idea of what could be causing this crash?  I'm confused why its invoking an error in nccl and not rccl.  Could I be missing a dependency?

## 评论 (6)

### nusislam · 2024-01-05

Do you see this issue with the latest rccl code? Which GPU are you using?

### haripriyaayyalasomayajula · 2024-04-29

@Eliasj42  - Is this still an issue? Did you try @nusislam's suggestions above? 

### Eliasj42 · 2024-04-29

> @Eliasj42 - Is this still an issue? Did you try @nusislam's suggestions above?

Sorry this isnt an issue anymore

### Eliasj42 · 2024-04-29

closed

### tmh97 · 2024-07-18

Hey @Eliasj42, I'm running into a similar issue! Would you mind sharing what your fix was?

### tmh97 · 2024-07-18

@haripriya-amd  @nusislam I noticed someone in the rccl-tests repo is also having the same issue https://github.com/ROCm/rccl-tests/issues/56. 

And here as well https://github.com/ROCm/rccl/issues/876

Is there a recommended fix for hangs in `ncclGroupEnd`?

