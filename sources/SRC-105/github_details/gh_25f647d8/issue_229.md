# [Issue #229] DCGM discovery isn't working correctly on H100 SXMs

source: https://github.com/NVIDIA/DCGM/issues/229
state: open | updated: 2025-05-21T16:23:55Z
labels: 

## 正文

Hello,

I'm seeing something weird when I run `dcgmi discovery -l` and also `dcgmi discovery -c`:

```
:dcgmi discovery -l --host unix:///var/run/dcgm.sock                                 
4 GPUs found.                                                                             
+--------+----------------------------------------------------------------------+         
| GPU ID | Device Information                                                   |         
+--------+----------------------------------------------------------------------+         
| 0      | Name: <<<NULL>>>                                                     |         
|        | PCI Bus ID: 00000000:4C:00.0                                         |         
|        | Device UUID: GPU-d6a2c177-4cd8-8d01-0310-79f2720f37de                |         
+--------+----------------------------------------------------------------------+         
| 1      | Name: <<<NULL>>>                                                     |         
|        | PCI Bus ID: 00000000:5D:00.0                                         |         
|        | Device UUID: GPU-75c4ee16-a840-6f6c-9a7b-5ed8f41598b8                |         
+--------+----------------------------------------------------------------------+         
| 2      | Name: <<<NULL>>>                                                     |         
|        | PCI Bus ID: 00000000:CC:00.0                                         |         
|        | Device UUID: GPU-879a110e-54dc-22fe-9699-5babde1d450e                |         
+--------+----------------------------------------------------------------------+         
| 3      | Name: <<<NULL>>>                                                     |         
|        | PCI Bus ID: 00000000:DC:00.0                                         |         
|        | Device UUID: GPU-5ea04b20-4cc3-4d84-0bb2-e4143be8e874                |         
+--------+----------------------------------------------------------------------+         
0 NvSwitches found.                                                                       
+-----------+                                                                             
| Switch ID |                                                                             
+-----------+                                                                             
+-----------+                                                                             
```
```
:dcgmi discovery -c --host unix:///var/run/dcgm.sock                                 
+-------------------+--------------------------------------------------------------------+
| Instance Hierarchy                                                                     |
+===================+====================================================================+
+-------------------+--------------------------------------------------------------------+
```
But, there's actually MIG on one of the GPUs:
```
:nvidia-smi -L                                                               
GPU 0: NVIDIA H100 80GB HBM3 (UUID: GPU-d6a2c177-4cd8-8d01-0310-79f2720f37de)
GPU 1: NVIDIA H100 80GB HBM3 (UUID: GPU-75c4ee16-a840-6f6c-9a7b-5ed8f41598b8)
GPU 2: NVIDIA H100 80GB HBM3 (UUID: GPU-879a110e-54dc-22fe-9699-5babde1d450e)
GPU 3: NVIDIA H100 80GB HBM3 (UUID: GPU-5ea04b20-4cc3-4d84-0bb2-e4143be8e874)
  MIG 2g.20gb     Device  0: (UUID: MIG-55d07ceb-ef71-58e0-87c2-0477d96fa03f)
```

Any idea why this is happening?

I'm on DCGM 3.1.7. Thanks in advance!

## 评论 (3)

### bergentruckung · 2025-05-14

Hi, any thoughts on this?

### bergentruckung · 2025-05-15

Has anyone seen this before?

### bstollenvidia · 2025-05-21

Can you capture debug logs from the nv-hostengine process and attach them?
https://docs.nvidia.com/datacenter/dcgm/latest/user-guide/debugging-and-troubleshooting.html
