# [Issue #1198] GDS benchmark partial faild

source: https://github.com/ai-dynamo/nixl/issues/1198
state: open | updated: 2026-05-14T11:06:23Z
labels: 

## 正文

I use the nixlbench  to test GDS and find when the max-block-size execeed 1M,the test will failed, the below is the full log
 
the dir /home/remote_nvme is a nvme-of disk 

<img width="1166" height="218" alt="Image" src="https://github.com/user-attachments/assets/61f8bdc7-ebbc-4164-84a4-651d630e20c2" />

<img width="1151" height="718" alt="Image" src="https://github.com/user-attachments/assets/3c814d77-2e0e-43e1-a940-23d92c7fe248" />

does the GDS backend have some linit in max block size?

## 评论 (2)

### jgoldsch12 · 2026-03-02

The GDS plugin has a maximum transfer limit of 16MB.  To avoid this failure, max_block_size must be set to 1648576.

### alokprasad · 2026-05-14

@iceCreeam is this PCIe Gen 4 SSD or Gen 5
