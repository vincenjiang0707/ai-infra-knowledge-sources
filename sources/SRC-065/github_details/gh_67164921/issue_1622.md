# [Issue #1622] compilation is too slow when using the tl.store

source: https://github.com/triton-lang/triton/issues/1622
state: closed | updated: 2026-09-01T18:09:37Z
labels: help wanted

## 正文

Hi，I have a  problem with compliation. I find that the compilation process is extremely  time-comsuming(about half hour and even hours sometimes) when using the tl.store. Once I comment "tl.store",  compilation will be finished soon. I do not understand why is this happening. 

Note that, I run bellow code four times in loop,  the test time is as follow(the unit is second):
![image](https://user-images.githubusercontent.com/32443088/236497466-d5867d61-c857-4bc4-a7ba-f79f7b493bb8.png)
When commenting "tl.store" in kernel function, the test time is shorter than above:
![1683299588131](https://user-images.githubusercontent.com/32443088/236497922-8af5180b-9f04-4992-a31f-1290ec5a74cc.png)  

I provide my code and hardware information here.

Brief hareware Infomation:
CPU  x86_64, 64 cores
GPU  NVIDIA 3090
Memory 256GB

```
import torch
import numpy as np
import triton
import triton.language as tl
import triton.testing
import argparse 
from pathlib import Path

@triton.jit
def kernel(A,
           area_size,
           max_pixeldist_5m, 
           stride_A_M,
           stride_A_N,
           stride_om,
           stride_on,
           d2r,
           out, 
           RadioM,
           PixS,
           angles,
        BLOCK_SIZE:tl.constexpr):
    
    pid = tl.program_id(0)
    
    anchors_size_M = area_size * 2 + 1  #offset area
    anchors_size_N = anchors_size_M     #offset area
    # calculate initial memory address
    pid_m = pid // anchors_size_M
    pid_n = pid % anchors_size_N
    poi_x = pid_n + max_pixeldist_5m - 1
    poi_y = pid_m + max_pixeldist_5m - 1
    
    pixel_dist_5m = tl.arange(0, BLOCK_SIZE)  
    pixel_dist_5m = pixel_dist_5m + 1
  
    rad_cos = tl.cos((tl.arange(0, BLOCK_SIZE) * 0.5) * d2r) #angles, [0,720] is useful but must satisfy 1024
    rad_sin = tl.sin((tl.arange(0, BLOCK_SIZE) * 0.5) * d2r) # refer to above comment

    delta_y = rad_cos[:, None] * pixel_dist_5m[None, :] # shape is [1024,1024]
    delta_x = rad_sin[:, None] * pixel_dist_5m[None, :]
    

    poi_y_inter = poi_y - delta_y  #float coordinates, shape is [1024,1024]
    poi_x_inter = poi_x + delta_x
    poi_x_min = poi_x_inter.to(tl.int32) #convert  float to int, truncate the fraction
    poi_y_min = poi_y_inter.to(tl.int32)
    poi_x_max = poi_x_min + 1
    poi_y_max = poi_y_min + 1
   
    mask_col = pixel_dist_5m < max_pixeldist_5m
    mask_row = tl.arange(0, BLOCK_SIZE) < (angles + 1)
    # when interpolating, we only preverse the top-left area with shape [721, 599]
    mask = mask_row[:, None] & mask_col[None, :]

    left_top_addr = A + poi_y_min * stride_A_M + poi_x_min * stride_A_N
    left_top_val = tl.load(left_top_addr, mask=mask, other=-float('inf'))
 
    offset_out = tl.arange(0, BLOCK_SIZE)
    output_addr = out + offset_out[:, None] * stride_om + offset_out[None, :] * stride_on
    tl.store(output_addr, left_top_val)
    


def calculate(A, area_size, max_pixeldist_5m, RadioM):
    assert A.is_contiguous(), "Matrix A must be contiguous"
    assert A.is_cuda, "Maxtrix A must be on GPU"
    stride_m = A.stride(0)
    stride_n = A.stride(1)
    n_rows = (area_size * 2 + 1) ** 2
    out = torch.empty((n_rows, 1024), device=A.device, dtype=A.dtype).contiguous()
    stride_om = out.stride(0)
    stride_on = out.stride(1)
    angles= 720
    d2r = np.pi / 180
    PixS = 10
    BLOCK_SIZE = triton.next_power_of_2(max_pixeldist_5m)
    kernel[(1,)](A,   #shape is 1239 by 1239
           area_size, max_pixeldist_5m, 
           stride_m, stride_n,
           stride_om, stride_on,
           d2r, 
           out,
           angles=angles,
           RadioM=RadioM,
           PixS=PixS,
           BLOCK_SIZE=BLOCK_SIZE)
 
    return out

def main(opt) -> None:
    #load data
    data = dict(np.load(opt.input, allow_pickle=True))
    A = data['A'].astype(np.float32)
    poi = data['poi']
    area_size = int(data['area_size'])
    max_pixeldist_5m = int(data['max_pixeldist_5m'])
    
    RadioM = 1737100.0 
    device = torch.device(f"cuda:{opt.device}")
    A = torch.from_numpy(A).to(device)
    
    import time 
    for _ in range(4):
        t1 = time.time()
        output = calculate(A, area_size, max_pixeldist_5m, RadioM)
        t2 = time.time()
        print(t2-t1)
    print(output[:, :])
    return 
```

Hey, Anyone knows the reason? It is really wired. If neccesary, I can provide data and complete code to help you reproduce the problem.




## 评论 (6)

### Jokeren · 2023-05-05

Without providing the `opt` argument, we are not able to run the code.

### Iipython · 2023-05-06

Hi, Thanks your help. Here is a version that you can execute on your computer.

```
import torch
import numpy as np
import triton
import triton.language as tl
import argparse 




@triton.jit
def kernel(A,
           area_size,
           max_pixeldist_5m, 
           stride_A_M,
           stride_A_N,
           stride_om,
           stride_on,
        #    len_offset,
           d2r,
           out, 
           RadioM,
           PixS,
           angles,
        #    arange_max_5m:tl.constexpr,
        BLOCK_SIZE:tl.constexpr):
    
    pid = tl.program_id(0)
    
    anchors_size_M = area_size * 2 + 1  #offset area
    anchors_size_N = anchors_size_M     #offset area
    # calculate initial memory address
    pid_m = pid // anchors_size_M
    pid_n = pid % anchors_size_N
    
    # compute on different angles , note the top-left coordinate of computed area of A equals (pid_m, pid_n)
    # row corresponds to y, col corresponds to x
    poi_x = pid_n + max_pixeldist_5m - 1
    poi_y = pid_m + max_pixeldist_5m - 1
    
    #interpolation scope, the reason the max value is set as 1025 is triton only supports the length with power of 2 
    pixel_dist_5m = tl.arange(0, BLOCK_SIZE)  
    pixel_dist_5m = pixel_dist_5m + 1
    
    
    rad_cos = tl.cos((tl.arange(0, BLOCK_SIZE) * 0.5) * d2r) #angles, [0,720] is useful but must satisfy 1024
    rad_sin = tl.sin((tl.arange(0, BLOCK_SIZE) * 0.5) * d2r) # refer to above comment

    delta_y = rad_cos[:, None] * pixel_dist_5m[None, :] # shape is [1024,1024]
    delta_x = rad_sin[:, None] * pixel_dist_5m[None, :]
    

    # # tl.printf("", delta_x)
    poi_y_inter = poi_y - delta_y  #float coordinates, shape is [1024,1024]
    poi_x_inter = poi_x + delta_x
    # # tl.printf("", poi_x_inter)
    poi_x_min = poi_x_inter.to(tl.int32) #convert  float to int, truncate the fraction
    poi_y_min = poi_y_inter.to(tl.int32)
    # # tl.printf("", poi_x_min)
    poi_x_max = poi_x_min + 1
    poi_y_max = poi_y_min + 1
   
    mask_col = pixel_dist_5m < max_pixeldist_5m
    mask_row = tl.arange(0, BLOCK_SIZE) < (angles + 1)
    # when interpolating, we only preverse the top-left area with shape [721, 599]
    mask = mask_row[:, None] & mask_col[None, :]

    left_top_addr = A + poi_y_min * stride_A_M + poi_x_min * stride_A_N
    left_top_val = tl.load(left_top_addr, mask=mask, other=-float('inf'))
    
    offset_out = tl.arange(0, BLOCK_SIZE)
    output_addr = out + offset_out[:, None] * stride_om + offset_out[None, :] * stride_on
    # tl.store(output_addr, left_top_val)


def calculate(A, area_size, max_pixeldist_5m, RadioM):
    assert A.is_contiguous(), "Matrix A must be contiguous"
    assert A.is_cuda, "Maxtrix A must be on GPU"
    stride_m = A.stride(0)
    stride_n = A.stride(1)
    
    #create output 
    n_rows = (area_size * 2 + 1) ** 2
    out = torch.empty((n_rows, 1024), device=A.device, dtype=A.dtype).contiguous()
    # import pdb
    # pdb.set_trace()
    stride_om = out.stride(0)
    stride_on = out.stride(1)
    #side length
    # len_offset = (max_pixeldist_5m - 1) * 2 + 1
    #degree to radians rate
    angles= 720
    d2r = np.pi / 180
    PixS = 10
    BLOCK_SIZE = triton.next_power_of_2(max_pixeldist_5m)
    kernel[(1,)](A, 
           area_size, max_pixeldist_5m, 
           stride_m, stride_n,
           stride_om, stride_on,
        #    len_offset,
           d2r, 
           out,
           angles=angles,
           RadioM=RadioM,
        #    arange_max_5m=max_pixeldist_5m,
           PixS=PixS,
           BLOCK_SIZE=BLOCK_SIZE)
    
    return out

def main(opt) -> None:
    #load data
    A = np.random.randn(1239, 1239) * 1000
    A = A.astype(np.float32)
    area_size = 20
    max_pixeldist_5m = 600
    RadioM = 1737100.0 
    #move data from cpu dram to gpu global memory
    device = torch.device(f"cuda:{opt.device}")
    A = torch.from_numpy(A).to(device)
    
    import time 
    for _ in range(4):
        t1 = time.time()
        output = calculate(A, area_size, max_pixeldist_5m, RadioM)
        t2 = time.time()
        print(t2-t1)
    print(output[:, :])
    return 

def parse_args():
    parser = argparse.ArgumentParser(description="parse")
    parser.add_argument("--device", type=int, default='0', help="gpu id")
    opt = parser.parse_args()
    return opt
    
if __name__ == "__main__":
    opt = parse_args()
    main(opt)
```

### Jokeren · 2023-05-06

Here's what I got

> ValueError('numel (1048576) exceeds triton maximum tensor numel (131072)')

I think the tensor size is probably too large

### LeonxLJX · 2026-09-01

I'd like to take this one (`compilation is too slow when using the tl.store`). I'll look into the root cause and follow up with a PR. (claiming via @LeonxLJX)

### LeonxLJX · 2026-09-01

I'd like to take this one (`compilation is too slow when using the tl.store`). I'll look into the root cause and follow up with a PR. (claiming via @LeonxLJX)

### peterbell10 · 2026-09-01

Commenting out the store makes the kernel optimize to a no-op.
