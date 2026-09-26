# [Issue #260] How to run nccl test in vm without nvswitch passthroughed?

source: https://github.com/NVIDIA/nccl-tests/issues/260
state: open | updated: 2026-03-27T09:00:10Z
labels: 

## 正文

Hi,
We are trying to run 4 vms in a host with 8 H100s, and each vm with 2 GPUs.
We found that the nvswitches can only be passthroughed into a single vm, and the rest vms got none. In this case, vms without nvswitch cannot run nccl test. The error is like blow.
![image](https://github.com/user-attachments/assets/21f497fc-83cd-44c1-8288-de717721cefe)
Then, it came to my mind that maybe disabling nvlink would help to find the path with pcie. So, I tried to set NCCL_P2P_DISABLE=1, but still not working.
![image](https://github.com/user-attachments/assets/f7a16504-4b31-4eaa-b4af-b17da77d7db9)
I don't know if there is any way to make through?

## 评论 (2)

### joydchh · 2024-11-05

Any insights on this?

### ArtoriaKawaii · 2026-03-27

Check https://docs.nvidia.com/datacenter/tesla/fabric-manager-user-guide/index.html#shared-nvswitch-virtualization-model
