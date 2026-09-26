# [Issue #354] Latest Commits Causing Compile Errors for File alltoall.cu

source: https://github.com/NVIDIA/nccl-tests/issues/354
state: open | updated: 2025-10-28T18:35:54Z
labels: 

## 正文

Compiling the nccl repo throws the following errors, all of them in the file `alltoall.cu`. Nothing has changed on our end for our build process.

```
alltoall.cu(218): error: expected a ";"
    ncclBarrierSession<ncclCoopCta> bar { ncclCoopCta(), ncclTeamTagWorld(), gin, blockIdx.x };
                                        ^
alltoall.cu(219): error: name followed by "::" must be a class or namespace name
    bar.sync(ncclCoopCta(), cuda::memory_order_relaxed, ncclGinFenceLevel::Relaxed);
                                                        ^
alltoall.cu(235): error: identifier "ncclGin_SignalInc" is undefined
          size, ncclGin_SignalInc{signalIndex});
                ^
alltoall.cu(235): error: expected a ")"
          size, ncclGin_SignalInc{signalIndex});
                                 ^
alltoall.cu(241): error: identifier "ncclGin_SignalInc" is undefined
          size, ncclGin_SignalInc{signalIndex});
                ^
alltoall.cu(241): error: expected a ")"
          size, ncclGin_SignalInc{signalIndex});
                                 ^
alltoall.cu(258): error: name followed by "::" must be a class or namespace name
    bar.sync(ncclCoopCta(), cuda::memory_order_release, ncclGinFenceLevel::Relaxed);
                                                        ^
22 errors detected in the compilation of "alltoall.cu".
make[1]: *** [Makefile:59: /tmp/nccl-tests/build/alltoall.o] Error 2
make: *** [Makefile:20: src.build] Error 2

```

## 评论 (2)

### AddyLaddy · 2025-10-27

We're actively working on resolving these compilation issues.


### shanedsnyder · 2025-10-28

Should be all resolved now (starting with version 2.17.5)
