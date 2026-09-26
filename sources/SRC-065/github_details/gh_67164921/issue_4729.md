# [Issue #4729] /usr/bin/ld: cannot find -lNVGPUIR: No such file or directory

source: https://github.com/triton-lang/triton/issues/4729
state: closed | updated: 2026-09-03T23:33:30Z
labels: 

## 正文

I want to compile libtriton.so on my own for subsequent development,but I encountered the following error while running make:

[ 59%] Built target TritonGPUToLLVM
[ 60%] Building TritonCombine.inc...
[ 60%] Built target TritonCombineIncGen
[ 62%] Building Passes.h.inc...
[ 62%] Built target TritonTransformsIncGen
[ 63%] Building CXX object lib/Dialect/Triton/Transforms/CMakeFiles/TritonTransforms.dir/Combine.cpp.o
[ 63%] Building CXX object lib/Dialect/Triton/Transforms/CMakeFiles/TritonTransforms.dir/LoopUnroll.cpp.o
[ 64%] Building CXX object lib/Dialect/Triton/Transforms/CMakeFiles/TritonTransforms.dir/ReorderBroadcast.cpp.o
[ 64%] Building CXX object lib/Dialect/Triton/Transforms/CMakeFiles/TritonTransforms.dir/RewriteTensorPointer.cpp.o
[ 64%] Built target TritonTransforms
[ 65%] Building Passes.h.inc...
[ 65%] Built target LLVMIRIncGen
[ 66%] Building CXX object lib/Target/LLVMIR/CMakeFiles/TritonLLVMIR.dir/LLVMDIScope.cpp.o
[ 66%] Building CXX object lib/Target/LLVMIR/CMakeFiles/TritonLLVMIR.dir/LLVMIRBreakPhiStruct.cpp.o
[ 66%] Built target TritonLLVMIR
[ 66%] Building CXX object CMakeFiles/triton.dir/python/src/main.cc.o
[ 67%] Building CXX object CMakeFiles/triton.dir/python/src/ir.cc.o
[ 67%] Building CXX object CMakeFiles/triton.dir/python/src/passes.cc.o
[ 67%] Building CXX object CMakeFiles/triton.dir/python/src/llvm.cc.o
[ 68%] Linking CXX shared library libtriton.so
/usr/bin/ld: cannot find -lNVGPUIR: No such file or directory
collect2: error: ld returned 1 exit status
make[2]: *** [CMakeFiles/triton.dir/build.make:492: libtriton.so] Error 1
make[1]: *** [CMakeFiles/Makefile2:2004: CMakeFiles/triton.dir/all] Error 2
make: *** [Makefile:146: all] Error 2


My environment is as follows:
cmake version 3.30.2

nvcc: NVIDIA (R) Cuda compiler driver
Copyright (c) 2005-2023 NVIDIA Corporation
Built on Fri_Sep__8_19:17:24_PDT_2023
Cuda compilation tools, release 12.3, V12.3.52
Build cuda_12.3.r12.3/compiler.33281558_0



I would greatly appreciate your help in resolving this issue

## 评论 (1)

### peterbell10 · 2026-09-03

closing as stale
