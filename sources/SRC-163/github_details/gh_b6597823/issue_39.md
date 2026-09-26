# [Issue #39] Error: Peer-to-peer access is unsupported on this platform

source: https://github.com/LLMServe/DistServe/issues/39
state: closed | updated: 2024-08-12T17:23:43Z
labels: 

## 正文

Hi, the problem is:

(ParaWorker pid=1955026) Error: Peer-to-peer access is unsupported on this platform.
(ParaWorker pid=1955026) In the current version of distserve, it is necessary to use a platform that supports GPU P2P access.
(ParaWorker pid=1955026) Exiting... 

I face a problem like this, but I actually checked the P2P connection between the two GPUs, and I tried the following codes for testing the P2P connection between GPUs:

    tensor_a = torch.randn(10, device="cuda:0")
    try:
        # Attempt to directly copy tensor_a from GPU 0 to GPU 1
        tensor_b = tensor_a.to("cuda:1")
        print("Successfully copied tensor from GPU 0 to GPU 1 using P2P.")
    except RuntimeError as e:
        print("Failed to copy tensor from GPU 0 to GPU 1 using P2P. Error:", e)

and the output is:

Successfully copied tensor from GPU 0 to GPU 1 using P2P.

and the GPU topo is:

<img width="176" alt="image" src="https://github.com/user-attachments/assets/ed34bc1b-c534-49fd-8131-e59a4442b4de">
<img width="882" alt="image" src="https://github.com/user-attachments/assets/f1230e45-0e64-4eb8-a6b8-2e95280cffbb">

can you provide any suggestions?

thank you!

## 评论 (2)

### Youhe-Jiang · 2024-08-12

The GPUs I use are RTX 4090s

### Youhe-Jiang · 2024-08-12

Yeah I solved the problem, seems that RTX 4090/PCIe connections cannot support DistServe, we run DistServe successfully on A100 machines with NVLINKs.
