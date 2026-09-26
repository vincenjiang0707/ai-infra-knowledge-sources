# [Issue #346] Issues regarding https://github.com/NVIDIA/nccl-tests/blob/master/doc/PERFORMANCE.md

source: https://github.com/NVIDIA/nccl-tests/issues/346
state: closed | updated: 2026-05-07T08:20:22Z
labels: 

## 正文

**[AllReduce]:**
Assume,
-  total rank number:   n   
-  each rank with an array of length N (i.e.,  N elements in the array)

For AllReduce with ring algorithm, take the case  of N >= n   &&   N % n == 0,         
e.g.,   N=n=4 ,
-   In ReduceScatter phase :  each rank sends  (N / n) * (n - 1)                            
-   In AllGather phase:            each rank sends  (N / n) * (n - 1)                             

Hence each rank sends  2 * (N / n ) * (n - 1 ) for one AllReduce operation.  
Then all the ranks send  total 2 * ( N / n ) * (n - 1)  * n =  2 * N * (n - 1) for one AllReduce operation.   

Given “each rank has a bandwidth to the outside world of B”,   total TX bandwidth is  n * B. 
Hence , t = 2 * N * (n -1 ) * sizeof (element’s datatype)  / ( n * B) = ( N * sizeof (element’s datatype)  / B )    *    ( 2 * (n -1 ) / n )

**Is above deduction correct for NCCL AllReduce?  Some questions as below.  Could please help  clarify/correct?**

**[Questions]:** 
Compared to  “  t = (S/B) * (2*(n-1)/n) ”,  it looks  S = N * sizeof (element’s datatype).  But it is not the expected value in   [PERFORMANCE.md](https://github.com/NVIDIA/nccl-tests/blob/master/doc/PERFORMANCE.md).
It is saying " Note that here, S is the size in bytes of the total array, which for NCCL is equal to recvcount*sizeof(datatype)*n as the recvcount argument is the count per rank."  It seems that “the count per rank” refers to the length N (of the array).   Then S =  N * sizeof(datatype) * n, which includes all the elements from all the arrays from all ranks.   
With such  “S” , the “t” will be n times of above t.   

According to “algbw = S/t” , it also implies S is equal to all the bytes from all the ranks?


## 评论 (1)

### zxue2 · 2026-05-07

It is due to different ops with different S, i.e.,
S= recvcount*sizeof(datatype)*n  is for ReduceScatter. 
S= N * sizeof(datatype) is for AllReduce.
