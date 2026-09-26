# [Issue #301] NCCL_TESTS_SPLIT_MASK for a single process that manages 8 GPUs in 8 threads

source: https://github.com/NVIDIA/nccl-tests/issues/301
state: closed | updated: 2025-04-25T19:37:12Z
labels: question, triaged

## 正文

Hi nccl-tests maintainers, 

I wonder if it is possible to enable NCCL_TESTS_SPLIT_MASK=0x7 for the case where a single process manages 8 GPUs in 8 threads. 

I find in this case, there will be only two groups created, rather than 8 groups. 
```
mpirun --bind-to none -np 2 -N 1 --host ip1,ip2 -x \
            NCCL_TESTS_SPLIT_MASK=0x7  \
            -b 1K -e 1G -f 2 -w 100 -n 100 -t 8 -g 1
```

Best,
Yang

## 评论 (1)

### sjeaugey · 2025-04-01

Indeed, the split mask group creation system applies on the process rank (MPI rank); it does not work in conjunction with `-t` or `-g`.
