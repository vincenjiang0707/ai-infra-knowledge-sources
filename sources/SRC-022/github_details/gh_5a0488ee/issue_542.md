# [Issue #542] Is need use a paired ncclSend/ncclRecv call?

source: https://github.com/ROCm/rccl/issues/542
state: closed | updated: 2022-04-28T15:45:40Z
labels: 

## 正文

Hello!
I have the questions)

**Q1**
I use a P2P collective. GPUs are connected via Infinity Fabric. 
I want to send data from GPU 0 to GPU 1. I have a misunderstanding here:
  A) Is only one call of ncclSend(...peer=1...) enough on side GPU 0 (or ncclRecv(...peer=0...) on side GPU 1)?
  B) Or sould I do a couple of paired collective?:
        * on GPU 0: ncclSend( ...peer=1...)
        * on GPU 1: ncclRecv( ...peer=0...)

It looks like TransferBench uses a single launch of GpuCopyKernel (https://github.com/ROCmSoftwarePlatform/rccl/blob/685bcea1275c5fd400b1784c393791a2ee11c947/tools/TransferBench/TransferBench.cpp#L1021) to copy from GPU 0 to GPU 1.

**Q2**
Something will change if I change Infinity Fabric to PCIE?

Thanks in advance for any information!


## 评论 (2)

### gilbertlee-amd · 2022-04-28

A1)  If you would like to just use RCCL to send data from GPU 0 to GPU 1, then yes - you will need option B - the pair of ncclSend and ncclRecv.  TransferBench is a standalone tool that runs only on a single process and uses a different method than RCCL for performing copies.  

B2) You won't need to change that code if you change how hardware is connected.  RCCL will automatically choose the a suitable transport based on the detected topology.

### vasslavich · 2022-04-28

@gilbertlee-amd thank you!
