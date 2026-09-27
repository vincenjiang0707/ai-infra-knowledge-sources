# [Issue #209] nv-hostengine stops responding after 2/3 days of continuous run, dcgmi hangs.

source: https://github.com/NVIDIA/DCGM/issues/209
state: open | updated: 2025-01-13T09:12:46Z
labels: 

## 正文

```$ nvidia-smi
Mon Jan 13 01:00:56 2025
+-----------------------------------------------------------------------------------------+
| NVIDIA-SMI 560.35.03              Driver Version: 560.35.03      CUDA Version: 12.6     |
|-----------------------------------------+------------------------+----------------------+
| GPU  Name                 Persistence-M | Bus-Id          Disp.A | Volatile Uncorr. ECC |
| Fan  Temp   Perf          Pwr:Usage/Cap |           Memory-Usage | GPU-Util  Compute M. |
|                                         |                        |               MIG M. |
|=========================================+========================+======================|
|   0  NVIDIA RTX A6000               Off |   00000000:B4:00.0 Off |                  Off |
| 30%   33C    P8             30W /  300W |       5MiB /  49140MiB |      0%      Default |
|                                         |                        |                  N/A |
+-----------------------------------------+------------------------+----------------------+
|   1  NVIDIA RTX A6000               Off |   00000000:B5:00.0 Off |                  Off |
| 30%   32C    P8             40W /  300W |       5MiB /  49140MiB |      0%      Default |
|                                         |                        |                  N/A |
+-----------------------------------------+------------------------+----------------------+

+-----------------------------------------------------------------------------------------+
| Processes:                                                                              |
|  GPU   GI   CI        PID   Type   Process name                              GPU Memory |
|        ID   ID                                                               Usage      |
|=========================================================================================|
|  No running processes found                                                             |
+-----------------------------------------------------------------------------------------+
$ dcgmi --version

dcgmi  version: 3.3.9
```
nv-hostengine shows following errors in logs:
```2025-01-12 18:20:08.932 ERROR [2285225:2285227] GetLatestSample returned No data is available for entityId 1 groupId 1 fieldId 230 [/workspaces/dcgm-rel_dcgm_3_3-postmerge/dcgmlib/src/DcgmCacheManager.cpp:4628] [DcgmCacheManager::GetMultipleLatestSamples]```

## 评论 (2)

### ajoshi-vi · 2025-01-13

[nv-hostengine.log.gz](https://github.com/user-attachments/files/18394576/nv-hostengine.log.gz)

### ajoshi-vi · 2025-01-13

We are using DCGM go APIs for GPU data collection.Sequence of DCGM calls as follows:
Init:
```
```json
	cleanup, err := dcgm.Init(dcgm.Standalone, nvhengine, "0")
	fieldsGroupId, err = dcgm.FieldGroupCreate(fieldGroupName, deviceFields)
	gpucount, err = dcgm.GetAllDeviceCount()
	for counter := uint(0); counter < gpucount; counter++ {
		_, err = dcgm.WatchFields(counter, fieldsGroupId, groupName)
	}
```
```
At regular intervals:
```	nvhengine := getNvHostEngineURL()
```go
	cleanup, err := dcgm.Init(dcgm.Standalone, nvhengine, "0")
	err = dcgm.UpdateAllFields()
	var allGpuUsageInfo []GpuUsageInfo
	for gpunum := 0; gpunum < int(totalGPUs); gpunum++ {
		values, err := dcgm.GetLatestValuesForFields(uint(gpunum), deviceFields)
		//assignment from values to return structure vars 
		}
```
