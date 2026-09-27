# [Issue #102] Support on CUDA12.0 for DCGMPROFTESTER

source: https://github.com/NVIDIA/DCGM/issues/102
state: closed | updated: 2025-05-27T09:21:19Z
labels: 

## 正文

Is there support available on CUDA12.0 for DCGMPROFTESTER?

I am getting following error when using,

```
yasir@36gpu7:~$ dcgmproftester12 --no-dcgm-validation -t 1004 -d 120
CacheManager Init Failed. Error: -29
```

and when i use the following there is no outcome,

```
yasir@36gpu7:~$ !124
dcgmproftester11 --no-dcgm-validation -t 1004 -d 120
```

## 评论 (3)

### nikkon-dev · 2023-09-01

@yasirjamal87,

Cuda12 is fully supported, and seeing the -29 error is quite strange here, though. 
It [means](https://github.com/NVIDIA/DCGM/blob/7e1012302679e4bb7496483b32dcffb56e528c92/dcgmlib/dcgm_structs.h#L325) the root is required.

Could you share the dcgmproftester debug logs?

### yasirjamal87 · 2023-09-01

looks like sudo was needed. Thanks
```
yasir@36gpu7:~$ sudo dcgmproftester12 --no-dcgm-validation -d 120
Skipping CreateDcgmGroups() since DCGM validation is disabled
Skipping CreateDcgmGroups() since DCGM validation is disabled
Skipping CreateDcgmGroups() since DCGM validation is disabled
Skipping CreateDcgmGroups() since DCGM validation is disabled
Worker 0:0[1001]: GrActivity: generated 0.000/0.000, dcgm M:{ GPU: 0.000, GI: 0.000, CI: 0.000 } at 1.000 seconds.
Worker 1:0[1001]: GrActivity: generated 0.000/0.000, dcgm M:{ GPU: 0.000, GI: 0.000, CI: 0.000 } at 1.000 seconds.
Worker 0:1[1001]: GrActivity: generated 0.000/0.000, dcgm M:{ GPU: 0.000, GI: 0.000, CI: 0.000 } at 1.000 seconds.
Worker 1:1[1001]: GrActivity: generated 0.000/0.000, dcgm M:{ GPU: 0.000, GI: 0.000, CI: 0.000 } at 1.000 seconds.
Worker 0:0[1001]: GrActivity: generated 0.000/0.008, dcgm M:{ GPU: 0.000, GI: 0.000, CI: 0.000 } at 2.000 seconds.
Worker 1:0[1001]: GrActivity: generated 0.000/0.008, dcgm M:{ GPU: 0.000, GI: 0.000, CI: 0.000 } at 2.000 seconds.
Worker 0:1[1001]: GrActivity: generated 0.000/0.008, dcgm M:{ GPU: 0.000, GI: 0.000, CI: 0.000 } at 2.000 seconds.
```

### isnuryusuf · 2025-05-27

using following deployment

```
apiVersion: v1
kind: Pod
metadata:
  name: dcgmproftester
spec:
  restartPolicy: OnFailure
  containers:
   - name: dcgmproftester12
     image: nvcr.io/nvidia/cloud-native/dcgm:3.3.0-1-ubuntu22.04
     commmand: ["/usr/bin/dcgmproftester12"]
     args: ["--no-dcgm-validation", "-t 1004", "-d 120"]
     resources:
       limits:
         nvidia.com/gpu: 1
     securityContext:
       capabilities:
         add: ["SYS_ADMIN"]
```

will get error:

```
PARSE ERROR: Argument: --no-dcgm-validation
             Couldn't find match for argument

Brief USAGE:
   nv-hostengine  -t -p <PORT> -d <SOCKET_PATH> -n -b <IP_ADDRESS> --pid <FILENAME> --log-level
                  <LEVEL> -f <FILENAME> --log-rotate --denylist-modules <MODULEID[,MODULEID...]>
                  --service-account <USERNAME> --home-dir <Diagnostic home> -- --version -h
For complete USAGE and HELP type:
   nv-hostengine --help
```
