source: https://docs.nvidia.com/cuda/gpudirect-rdma/contents.html

1. Overview
2. Change log
3. Design Considerations
4. How to Perform Specific Tasks
5. References
6. Notices
GPUDirect RDMA
»
Contents
v13.4 |
PDF
|
Archive
Contents
1. Overview
1.1. How GPUDirect RDMA Works
1.2. Standard DMA Transfer
1.3. GPUDirect RDMA Transfers
2. Change log
2.1. Changes in CUDA 13.0
2.1.1. Deprecation Notice: NV-P2P API Support
2.1.2. Device Attribute Updates
2.1.3. 2.1.3. Platform Notes: Orin (L4T)
2.1.4. Known Issues
2.2. Changes in CUDA 12.2
2.3. Changes in CUDA 11.4
2.4. Changes in CUDA 11.2
2.5. Changes in CUDA 10.1
2.6. Changes in CUDA 8.0
2.7. Changes in CUDA 7.0
2.8. Changes in CUDA 6.0
3. Design Considerations
3.1. Lazy Unpinning Optimization
3.2. Registration Cache
3.3. Unpin Callback
3.4. Supported Systems
3.5. PCI BAR sizes
3.6. Tokens Usage
3.7. Synchronization and Memory Ordering
3.8. CUDA Features Not Supported on Tegra
4. How to Perform Specific Tasks
4.1. Displaying GPU BAR space
4.2. Pinning GPU memory
4.3. Unpinning GPU memory
4.4. Handling the free callback
4.5. Buffer ID Tag Check for A Registration Cache
4.6. Linking a Kernel Module against nvidia.ko
4.7. Using nvidia-peermem
5. References
5.1. Basics of UVA CUDA Memory Management
5.2. Userspace API
5.3. Kernel API
5.4. Porting to Tegra
5.4.1. Changing the allocator
5.4.2. Modification to Kernel API
5.4.3. Other highlights
5.5. Porting strategy for device drivers based on nv-p2p
6. Notices
6.1. Notice
6.2. OpenCL
6.3. Trademarks