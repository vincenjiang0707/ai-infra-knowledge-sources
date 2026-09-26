# [Issue #297] Can the results of nccl-tests be different depending on the version of driver

source: https://github.com/NVIDIA/nccl-tests/issues/297
state: open | updated: 2025-03-27T07:56:07Z
labels: question, triaged

## 正文

Test Case 1 
H100 8 GPUs , 4 IB Ports , nvidia-driver 535.183.06
[ result ] 
 mpirun -x NCCL_DEBUG=INFO -H node1:8,node2:8 --map-by slot --mca btl ^openib /root/nccl-tests/build/all_reduce_perf -b 1G -e 30G -n 10 -c 0 -f2
Out of bounds values : 0 OK
Avg bus bandwidth    : 362.198 
debug info log is attached case1.log

Test case 2 
H100 8 GPUs , 4 IB Ports , nvidia-driver 550.144.03 , H100 8 GPUs , 4 IB Ports , nvidia-driver 570.124.06 
[result : regardless of driver version]
mpirun -H node1:8,node2:8 -x NCCL_DEBUG=INFO -map-by slot --mca btl ^openib --mca btl_tcp_if_include eno8403 /root/nccl-tests/build/all_reduce_perf -b 1G -e 30G -f 2 -n 10 -c 0
Out of bounds values : 0 OK
Avg bus bandwidth    : 327.981 
debug info log is attached case2.txt

[case1.log](https://github.com/user-attachments/files/19460387/case1.log)
[case2.txt](https://github.com/user-attachments/files/19460388/case2.txt)

## 评论 (2)

### sjeaugey · 2025-03-26

Well that can always happen, but it could be other things:
 - when changing the driver, you rebooted the node and some setting got lost. Things like GPU clocks, persistence mode, etc. One other way to confirm that would be to reinstall the previous driver and see whether performance  is back to what it was before.
 - performance is unstable on your system run-to-run. Running e.g. 10 times can confirm that. Also, running with `mpirun --bind-to numa` is advised, as it ensures we have enough CPU cores for network progress while avoiding NUMA affinity issues. In your tests your processes may be bound to a single core which can produce sub-par performance.

I looked at the logs and nothing struck me as being different between the two runs. It could be good to compare the pure NVLink performance as well (single node) between the two driver versions, to see whether the regression seems to come from the network or from the GPU/NVLink.

### jk1465kim · 2025-03-27

I tried to test several times , the result same
Driver 535 - average 360 GB /s , 2node 8 GPUs 4 IBs  
Driver 570 or 550 - average 330 GB/s 2node 8 GPUs 4 IBs 

I find a difference between 535 and 550/570 driver. 
it's PCI relaxed ordering on GPU Devices. 
In 535 Driver , PCI Relaxed ordering was enabled on GPU Devices
550 or 570 Driver , PCI Relaxed ordering was disabled on GPU Devices 
Is it possibly impacted?
when I installed 535 driver , RlxdOrd always was enabled in lspci.
but when I installed 550, 570 driver , RlxdOrd always was disabled in lspci.
anyway in case of 550 or 570 driver , I tried to RlxdOrd enabled. the test result was same.
I cant find any other difference point between 535 and 550/570...

535 driver 
![Image](https://github.com/user-attachments/assets/3ece7fbf-65c6-4e89-8117-7df95fd59723)
![Image](https://github.com/user-attachments/assets/067fb61d-f2bc-439e-b86e-7cc4842dd609)

550 or 575 driver 
![Image](https://github.com/user-attachments/assets/d1298dc0-9b78-4a5a-b7d5-4079eefa8c4e)
![Image](https://github.com/user-attachments/assets/6c9212a0-2972-4a13-af7f-3bc1ec19b228)
