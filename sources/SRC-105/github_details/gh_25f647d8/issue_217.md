# [Issue #217] export metrics in a passthrough GPU

source: https://github.com/NVIDIA/DCGM/issues/217
state: closed | updated: 2025-03-13T19:51:37Z
labels: 

## 正文

Hi, I am currently using an NVIDIA T4 GPU with passthrough to a virtual machine and am interested in exporting its metrics directly from the host machine. Is it possible to achieve this with DCGM, if so could you guide me on how to set this up?

## 评论 (1)

### nikkon-dev · 2025-03-11

@farashiani-khalil,

It is impossible to collect metrics on the host machine when the GPU is in passthrough mode. In this mode, the GPU is entirely invisible to the host driver because passthrough operates at a lower PCI level.

The only option is to run the DCGM inside the VM. In this case, you can connect to it from the host using the dcgmi CLI.
The nv-hostengine can listen on a TCP port that can be exposed to the host. In future versions, we consider VSOCK support in addition to TCP and Unix domain sockets. 
