# [Issue #660] Building  rccl v5.4.0 hang on src/collectives/device/all_reduce.cpp

source: https://github.com/ROCm/rccl/issues/660
state: closed | updated: 2022-12-09T17:56:48Z
labels: 

## 正文

Building rccl v5.4.0 hang on step "src/collectives/device/all_reduce.cpp"

PS. But building rccl v5.3.3 was succesful with same enviroment and tool from rocm v5.4.0 stack.

## 评论 (1)

### perestoronin · 2022-12-09

My bug, because I removed deprecated flag --hipcc-func-supp from build. But build with flag --hipcc-func-supp resolve my own trouble building rccl v5.4.0.
