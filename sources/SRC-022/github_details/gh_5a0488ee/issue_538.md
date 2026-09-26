# [Issue #538] Does RCCL support the Infinity Fabric?

source: https://github.com/ROCm/rccl/issues/538
state: closed | updated: 2022-05-01T07:30:24Z
labels: 

## 正文

Hello!
I have MI100 GPUs are interconnected via Infinity Fabric and I'd like to use it with RCCL. The tool TransferBench give me only 27.5 Gbytes per second. Perhaps, does RCCL has any options to turn on Infinity Fabric?
Thanks!

## 评论 (7)

### gilbertlee-amd · 2022-04-25

RCCL will automatically use Infinity Fabric if detected.  Does TransferBench with no arguments show XGMI connections between the MI100s?


### vasslavich · 2022-04-28

TransferBench with no arguments shows _PCIE_
And, I looked at kfd configuration, the type is _1_:
`
$ cat /sys/class/kfd/kfd/topology/nodes/0/io_links/5/properties
type 1
....
`


### gilbertlee-amd · 2022-04-28

Hi @vasslavich, are you sure your GPUs to one another via Infinity Fabric?

### gilbertlee-amd · 2022-04-28

Could you post the outout of /opt/rocm/bin/rocm-smi --showtopo?
Thanks


### vasslavich · 2022-04-29

Hello!
Thanks, @gilbertlee-amd !
I attached the output below, and I has new questions about it:
1. What are the **weight** and **hops**?
2. How can I use **topo_expl** tool with my topology (MI100 GPUs)?

The output:
`$ /opt/rocm/bin/rocm-smi --showtopo


======================= ROCm System Management Interface =======================
=========================== Weight between two GPUs ============================
       GPU0         GPU1         GPU2         GPU3         
GPU0   0            72           40           72           
GPU1   72           0            72           40           
GPU2   40           72           0            72           
GPU3   72           40           72           0            

============================ Hops between two GPUs =============================
       GPU0         GPU1         GPU2         GPU3         
GPU0   0            3            2            3            
GPU1   3            0            3            2            
GPU2   2            3            0            3            
GPU3   3            2            3            0            

========================== Link Type between two GPUs ==========================
       GPU0         GPU1         GPU2         GPU3         
GPU0   0            PCIE         PCIE         PCIE         
GPU1   PCIE         0            PCIE         PCIE         
GPU2   PCIE         PCIE         0            PCIE         
GPU3   PCIE         PCIE         PCIE         0            

================================== Numa Nodes ==================================
GPU[0]		: (Topology) Numa Node: 7
GPU[0]		: (Topology) Numa Affinity: 7
GPU[1]		: (Topology) Numa Node: 1
GPU[1]		: (Topology) Numa Affinity: 1
GPU[2]		: (Topology) Numa Node: 7
GPU[2]		: (Topology) Numa Affinity: 7
GPU[3]		: (Topology) Numa Node: 1
GPU[3]		: (Topology) Numa Affinity: 1
============================= End of ROCm SMI Log ==============================
`

### gilbertlee-amd · 2022-04-29

Based on this output, it looks like your GPUs are connected to one another via PCIe, not Infinity Fabric.  
Hops refers to the number of intermediate steps, which in this case are likely PCIe switchs along the path from one GPU to another.  Weights are somewhat similar to hop values in measuring "distance".  

The topo_expl tool is used to understand how RCCL will establish connections for collectives (e.g. how rings are built) for various (hard-coded) topologies.  Running with no arguments will show supported models, which can be passed in via ./topo_expl -m <mode_id>.

### vasslavich · 2022-05-01

Hello, @gilbertlee-amd! Thank you!
