# [Issue #1423] [Issue]: RCCL hangs during initialization  with `port error`

source: https://github.com/ROCm/rccl/issues/1423
state: closed | updated: 2024-12-09T16:42:54Z
labels: Under Investigation

## 正文

### Problem Description

Hi folks, I am trying to run a distributed workload between 2 MI300X VMs and the RCCL just hangs infinitely during initialization. You can find details below. If I run it within a single node under the same setting it works well. Any suggestions how I can debug this? Thank you

System Info:
```
OS:
NAME="Ubuntu"
VERSION="20.04.6 LTS (Focal Fossa)"
CPU: 
model name	: Intel(R) Xeon(R) Platinum 8480C
GPU:
  Name:                    Intel(R) Xeon(R) Platinum 8480C    
  Marketing Name:          Intel(R) Xeon(R) Platinum 8480C    
  Name:                    Intel(R) Xeon(R) Platinum 8480C    
  Marketing Name:          Intel(R) Xeon(R) Platinum 8480C    
  Name:                    gfx942                             
  Marketing Name:          AMD Instinct MI300X VF             
      Name:                    amdgcn-amd-amdhsa--gfx942:sramecc+:xnack-
  Name:                    gfx942                             
  Marketing Name:          AMD Instinct MI300X VF             
      Name:                    amdgcn-amd-amdhsa--gfx942:sramecc+:xnack-
  Name:                    gfx942                             
  Marketing Name:          AMD Instinct MI300X VF             
      Name:                    amdgcn-amd-amdhsa--gfx942:sramecc+:xnack-
  Name:                    gfx942                             
  Marketing Name:          AMD Instinct MI300X VF             
      Name:                    amdgcn-amd-amdhsa--gfx942:sramecc+:xnack-
  Name:                    gfx942                             
  Marketing Name:          AMD Instinct MI300X VF             
      Name:                    amdgcn-amd-amdhsa--gfx942:sramecc+:xnack-
  Name:                    gfx942                             
  Marketing Name:          AMD Instinct MI300X VF             
      Name:                    amdgcn-amd-amdhsa--gfx942:sramecc+:xnack-
  Name:                    gfx942                             
  Marketing Name:          AMD Instinct MI300X VF             
      Name:                    amdgcn-amd-amdhsa--gfx942:sramecc+:xnack-
  Name:                    gfx942                             
  Marketing Name:          AMD Instinct MI300X VF             
      Name:                    amdgcn-amd-amdhsa--gfx942:sramecc+:xnack-

```

Please see log in the attached file as it exceeds the comment length limit

[log1.txt](https://github.com/user-attachments/files/17758148/log1.txt)


### Operating System

20.04.6 LTS (Focal Fossa)

### CPU

Intel(R) Xeon(R) Platinum 8480C

### GPU

AMD Instinct MI300X VF

### ROCm Version

ROCm 6.2.0

### ROCm Component

_No response_

### Steps to Reproduce

_No response_

### (Optional for Linux users) Output of /opt/rocm/bin/rocminfo --support

```
^[[37mROCk module version 6.8.5 is loaded^[[0m
=====================    
HSA System Attributes    
=====================    
Runtime Version:         1.14
Runtime Ext Version:     1.6
System Timestamp Freq.:  1000.000000MHz
Sig. Max Wait Duration:  18446744073709551615 (0xFFFFFFFFFFFFFFFF) (timestamp count)
Machine Model:           LARGE                              
System Endianness:       LITTLE                             
Mwaitx:                  DISABLED
DMAbuf Support:          YES

==========               
HSA Agents               
==========               
*******                  
Agent 1                  
*******                  
  Name:                    Intel(R) Xeon(R) Platinum 8480C    
  Uuid:                    CPU-XX                             
  Marketing Name:          Intel(R) Xeon(R) Platinum 8480C    
  Vendor Name:             CPU                                
  Feature:                 None specified                     
  Profile:                 FULL_PROFILE                 

### Additional Information

_No response_

## 评论 (6)

### nileshnegi · 2024-11-14

it seems 1 system has 7 active NICs and the other has 8... do you expect 8 NICs on both hosts?
```
[3] MI300X-GRN-1:744139:744139 [0] NCCL INFO NET/IB : Using [0]mlx5_0:1/IB [1]mlx5_1:1/IB [2]mlx5_2:1/IB [3]mlx5_3:1/IB [4]mlx5_4:1/IB [5]mlx5_5:1/IB [6]mlx5_6:1/IB [RO]; OOB eth0:10.10.98.12<0>
[8] MI300X-GRN-2:525248:525248 [0] NCCL INFO NET/IB : Using [0]mlx5_0:1/IB [1]mlx5_1:1/IB [2]mlx5_2:1/IB [3]mlx5_3:1/IB [4]mlx5_4:1/IB [5]mlx5_5:1/IB [6]mlx5_6:1/IB [7]mlx5_7:1/IB [RO]; OOB eth0:10.10.98.8<0>
```

### HeyangQin · 2024-11-14

> it seems 1 system has 7 active NICs and the other has 8... do you expect 8 NICs on both hosts?
> 
> ```
> [3] MI300X-GRN-1:744139:744139 [0] NCCL INFO NET/IB : Using [0]mlx5_0:1/IB [1]mlx5_1:1/IB [2]mlx5_2:1/IB [3]mlx5_3:1/IB [4]mlx5_4:1/IB [5]mlx5_5:1/IB [6]mlx5_6:1/IB [RO]; OOB eth0:10.10.98.12<0>
> [8] MI300X-GRN-2:525248:525248 [0] NCCL INFO NET/IB : Using [0]mlx5_0:1/IB [1]mlx5_1:1/IB [2]mlx5_2:1/IB [3]mlx5_3:1/IB [4]mlx5_4:1/IB [5]mlx5_5:1/IB [6]mlx5_6:1/IB [7]mlx5_7:1/IB [RO]; OOB eth0:10.10.98.8<0>
> ```

@nileshnegi Thanks for the hint! That is very likely the cause because both VMs should have 8 IB NICs. I tried to double-check it from system level and it shows 8 IBs

```
root@MI300X-GRN-1:/home/heyangqin# lspci | grep -i infiniband
0101:00:00.0 Infiniband controller: Mellanox Technologies ConnectX Family mlx5Gen Virtual Function
0102:00:00.0 Infiniband controller: Mellanox Technologies ConnectX Family mlx5Gen Virtual Function
0103:00:00.0 Infiniband controller: Mellanox Technologies ConnectX Family mlx5Gen Virtual Function
0104:00:00.0 Infiniband controller: Mellanox Technologies ConnectX Family mlx5Gen Virtual Function
0105:00:00.0 Infiniband controller: Mellanox Technologies ConnectX Family mlx5Gen Virtual Function
0106:00:00.0 Infiniband controller: Mellanox Technologies ConnectX Family mlx5Gen Virtual Function
0107:00:00.0 Infiniband controller: Mellanox Technologies ConnectX Family mlx5Gen Virtual Function
0108:00:00.0 Infiniband controller: Mellanox Technologies ConnectX Family mlx5Gen Virtual Function
root@MI300X-GRN-1:/home/heyangqin# ls /sys/class/infiniband/
mlx5_0  mlx5_1  mlx5_2  mlx5_3  mlx5_4  mlx5_5  mlx5_6  mlx5_7
```
I wonder how to further debug this?

### nileshnegi · 2024-11-14

you can check if `rdma link` shows `state ACTIVE physical_state LINK_UP` for all NICs on GRN-1

if this shows all 8 as ACTIVE, you may have to try RDMA perftest to see if you can actually transmit data on `mlx5_7`.

### HeyangQin · 2024-11-14

Thank you @nileshnegi. By running `rdma link` I see:
```
link mlx5_7/1 subnet_prefix fe80:0000:0000:0000 lid 3403 sm_lid 1 lmc 0 state DOWN physical_state POLLING
```
Does that suggest a hardware/connection failure or is that still something on the system/software level?

Edit: I try to run `rdma link` again and I see its state changed to
```
link mlx5_7/1 subnet_prefix fe80:0000:0000:0000 lid 3403 sm_lid 1 lmc 0 state DOWN physical_state LINK_UP
```
Then to
```
link mlx5_7/1 subnet_prefix fe80:0000:0000:0000 lid 3403 sm_lid 1 lmc 0 state ACTIVE physical_state LINK_UP
```
So it is kind of unstable

### tcgu-amd · 2024-11-26

Hi @HeyangQin, sorry for the delayed response -- given the intermittent link state, I would suspect that there could be something wrong with the hardware potentially, especially if it is only happening on one of the VM's and both are configured identically. If possible, I would try to use a different VM and see if the issue persists. Thanks!

### tcgu-amd · 2024-12-09

Hi, this issue will be closed for now due to inactivity. Please feel free to reopen for follow ups. Thanks! 
