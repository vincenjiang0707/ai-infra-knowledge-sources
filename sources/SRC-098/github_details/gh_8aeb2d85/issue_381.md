# [Issue #381] alltoall: NCCL_WIN_COLL_SYMMETRIC incorrectly triggers symk GIN init, causing AlltoAll DevComm GIN connection to be silently skipped

source: https://github.com/NVIDIA/nccl-tests/issues/381
state: open | updated: 2026-05-13T09:30:01Z
labels: 

## 正文

When running AlltoAll with `-D3`/`-D4` and `-R2`, `ncclCommWindowRegister` is called with `NCCL_WIN_COLL_SYMMETRIC`, which unintentionally triggers `ncclSymkInitOnce`. This calls `ncclDevrCommCreateInternal` with a configuration that belongs to the symk path(such as `ginConnectionType = NCCL_GIN_CONNECTION_RAII`), not AlltoAll's configuration. Since `ncclGinConnectOnce` only runs once per comm, the AlltoAll DevComm's own initialization (such as `ginConnectionType=NCCL_GIN_CONNECTION_FULL`) is silently skipped entirely.

This is a latent correctness issue: once the `ginConnectionType` selection logic is updated to honor `reqs.ginConnectionType` directly (instead of falling back to `nccl_cross_nic`), AlltoAll will still behave incorrectly — because GIN connections were already established under the wrong `RAIL` configuration before the DevComm path even ran.

GIN initialization should be owned entirely by the DevComm creation path , not from an unrelated code path.

## 评论 (6)

### YeSho-cpp · 2026-05-13

this is the [pr](https://github.com/NVIDIA/nccl-tests/pull/382)

@sjeaugey  Can you help have a look at this?

### sjeaugey · 2026-05-13

We do want to pass the NCCL_WIN_COLL_SYMMETRIC flag, so that running the non-device-API cases with -R 2 would show better performance, leveraging the internal symmetric kernels.

If we wanted to remove that flag, we'd need to check that we are running with a device implementation.

Now, setting that flag should not be an issue: we will create the GIN common infrastructure (gin->connect()) according to the cross_nic setting, but then we will only connect to the required peers (rail or full) according to the devComm requirement. 


### YeSho-cpp · 2026-05-13

> We do want to pass the NCCL_WIN_COLL_SYMMETRIC flag, so that running the non-device-API cases with -R 2 would show better performance, leveraging the internal symmetric kernels.
> 
I understand your point. Therefore, I constrained the condition as `int winFlags = (ncclTestEngine.runTest == AlltoAllRunTest) ? NCCL_WIN_DEFAULT : NCCL_WIN_COLL_SYMMETRIC`;. The implemented entries in ncclSymkImplemented only include `ncclFuncAllGather`, `ncclFuncAllReduce`, and `ncclFuncReduceScatter`. AlltoAll should not use NCCL_WIN_COLL_SYMMETRIC since it is not a collective operation. There is no need to call ncclSymkInitOnce for AlltoAll. I believe this PR is not a removal but an adjustment. With this adjustment, non-device-API cases running with -R 2 will still use NCCL_WIN_COLL_SYMMETRIC.
> If we wanted to remove that flag, we'd need to check that we are running with a device implementation.
> 
> Now, setting that flag should not be an issue: we will create the GIN common infrastructure (gin->connect()) according to the cross_nic setting, but then we will only connect to the required peers (rail or full) according to the devComm requirement.

On this point, has the overhead of the GIN general infrastructure been taken into account, and will a full QP be created when cross_nic=2 and I only need the connection type of rail?

### sjeaugey · 2026-05-13

> Therefore, I constrained the condition as int winFlags = (ncclTestEngine.runTest == AlltoAllRunTest)

Ah, right, that would work. Today at least. In the long term though, the day we implement a symmetric alltoall kernel, we'd need to change that code.

> On this point, has the overhead of the GIN general infrastructure been taken into account, and will a full QP be created when cross_nic=2 and I only need the connection type of rail?

True, creating a full GIN group when we only end up connecting ranks on the same rail could incur a small overhead, as the allgather operation to get all handles from other ranks would communicate Nx more data. That being said, I'm not sure it would be visible.

### YeSho-cpp · 2026-05-13

> True, creating a full GIN group when we only end up connecting ranks on the same rail could incur a small overhead, as the allgather operation to get all handles from other ranks would communicate Nx more data. That being said, I'm not sure it would be visible.

I believe GinConnectionType can be analogous to comm->initAlgoChannels[algo], and Lazy Connection Setup can be adopted. ncclGinConnectOnce can also be called multiple times. GinConnectionType[0] is set to NCCL_GIN_CONNECTION_FULL and GinConnectionType[1] to NCCL_GIN_CONNECTION_RAIL. If a devcomm contains both connections of type NCCL_GIN_CONNECTION_RAIL and NCCL_GIN_CONNECTION_FULL, it can work perfectly well. Meanwhile, there will be no redundant creation overhead when only rail-type connections are required.

The design of Lazy Connection Setup refers to the following logic:
```c++
if (comm->runtimeConn && comm->initAlgoChannels[task->algorithm] == false) {
    comm->initAlgoChannels[task->algorithm] = true;
    algoNeedConnect[task->algorithm] = true;
    *needConnect = true;
}
```
The above is just my suggestion.

### sjeaugey · 2026-05-13

This is indeed an option which may be implemented in future NCCL versions. We're also considering keeping multiple GIN backends so that different devComms can request different backends, which is in the same vein of retaining a set of different GIN comms with different properties.
