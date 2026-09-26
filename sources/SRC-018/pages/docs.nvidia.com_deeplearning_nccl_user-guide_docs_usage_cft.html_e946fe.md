source: https://docs.nvidia.com/deeplearning/nccl/user-guide/docs/usage/cft.html

# Compute Fabric Transport[](https://docs.nvidia.com#compute-fabric-transport)

Starting with NCCL 2.31, the Device API includes Compute Fabric Transport (CFT) helpers for kernels that communicate through CUDA fabric logical endpoints. CFT is useful when an application launches custom device-side communication kernels on CFT-capable systems and needs direct fabric put, get, reduction, or barrier operations.

## Requirements[](https://docs.nvidia.com#requirements)

CFT kernels require hardware, driver, and CUDA Toolkit support for fabric logical endpoints and fabric PTX instructions. In this release, the example CFT barrier program documents the practical requirements as CUDA Toolkit 13.3 and SM_100 architectures.

Before using CFT in an application:

Allocate and register symmetric memory windows with NCCL.

Create a device communicator with CFT capabilities in

.`ncclDevCommRequirements`

Use CFT team helpers to address peers by CFT team rank.

Query logical endpoint IDs and offsets before issuing CFT operations.

Match the number of requested CFT barriers to the number of barrier slots used by the kernel.


## Device Communicator Setup[](https://docs.nvidia.com#device-communicator-setup)

The host code requests CFT capability when creating the device communicator.

```
ncclDevComm devComm;
ncclDevCommRequirements reqs = NCCL_DEV_COMM_REQUIREMENTS_INITIALIZER;
reqs.cftCaps = NCCL_CFT;
reqs.cftBarrierCount = nCTAs;
NCCLCHECK(ncclDevCommCreate(comm, &reqs, &devComm));
```

Request [ NCCL_CFT_MULTIMEM](https://docs.nvidia.com/api/device_cft.html#c.NCCL_CFT_MULTIMEM) in addition to

[when a kernel uses multicast CFT operations or multimem CFT barriers:](https://docs.nvidia.com/api/device_cft.html#c.NCCL_CFT)

`NCCL_CFT`

```
reqs.cftCaps = NCCL_CFT | NCCL_CFT_MULTIMEM;
```

If a communicator cannot provide the requested CFT capability on all ranks,
[ ncclDevCommCreate()](https://docs.nvidia.com/api/device_setup.html#c.ncclDevCommCreate) fails.

## Teams and Endpoints[](https://docs.nvidia.com#teams-and-endpoints)

CFT operations may address peers through CFT teams rather than directly through
world ranks. Use [ ncclTeamCft()](https://docs.nvidia.com/api/device_cft.html#c.ncclTeamCft) or

[on the host side, and the corresponding device overloads in kernels, to obtain the team layout.](https://docs.nvidia.com/api/device_cft.html#c.ncclTeamCftMultimem)

`ncclTeamCftMultimem()`

Use logical endpoint query helpers to translate a registered window, byte
offset, and peer into the values consumed by [ ncclCft](https://docs.nvidia.com/api/device_cft.html#_CPPv4I0E7ncclCft) operations.
For device-side kernels,

[accepts a CFT-team peer rank and](https://docs.nvidia.com/api/device_cft.html#_CPPv416ncclGetCftLeInfo12ncclWindow_t6size_ti8ncclTeamRK11ncclDevCommP11ncclCftLeIdP6size_t)

`ncclGetCftLeInfo()`

[accepts a world-rank peer.](https://docs.nvidia.com/api/device_cft.html#_CPPv417ncclGetPeerLeInfo12ncclWindow_t6size_tiRK11ncclDevCommP11ncclCftLeIdP6size_t)

`ncclGetPeerLeInfo()`

```
ncclTeam cftTeam = ncclTeamCft(devComm);
ncclCftLeId leId;
size_t leOffset;
ncclGetCftLeInfo(win, byteOffset, peerCft, cftTeam, devComm,
&leId, &leOffset);
```

Host code can use [ ncclGetCftDeviceLeInfo()](https://docs.nvidia.com/api/device_cft.html#c.ncclGetCftDeviceLeInfo),

[, and](https://docs.nvidia.com/api/device_cft.html#c.ncclGetPeerDeviceLeInfo)

`ncclGetPeerDeviceLeInfo()`

[. If host-side endpoint queries are needed before creating a CFT-enabled device communicator, configure](https://docs.nvidia.com/api/device_cft.html#c.ncclGetMultimemDeviceLeInfo)

`ncclGetMultimemDeviceLeInfo()`

`hostCftMode`

in
[during communicator initialization.](https://docs.nvidia.com/api/types.html#c.ncclConfig_t)

`ncclConfig_t`

## CFT Operations[](https://docs.nvidia.com#cft-operations)

A CFT kernel stages data through shared memory, creates a [ ncclCft](https://docs.nvidia.com/api/device_cft.html#_CPPv4I0E7ncclCft)
object, issues operations, and then submits and flushes the work.

```
__global__ void cftPutKernel(ncclDevComm devComm, ncclWindow_t win) {
__shared__ ncclCftSmem cftSmem;
__shared__ alignas(16) char smem[128];
ncclCoopCta coop;
ncclCft<ncclCoopCta> cft{coop, cftSmem};
ncclTeam cftTeam = ncclTeamCft(devComm);
int peer = (cftTeam.rank + 1) % cftTeam.nRanks;
ncclCftLeId leId;
size_t leOffset;
ncclGetCftLeInfo(win, 0, peer, cftTeam, devComm, &leId, &leOffset);
cft.put(coop, leId, leOffset, smem, sizeof(smem));
cft.submit(coop);
cft.flush(coop);
}
```

CFT source and destination shared memory pointers must be 16-byte aligned, and
the byte count must be a multiple of 16. See [Device API - CFT](https://docs.nvidia.com/api/device_cft.html#device-api-cft) for the full
list of put, get, multicast, reduction, and pull-reduce helpers.

## CFT Barriers[](https://docs.nvidia.com#cft-barriers)

CFT barriers synchronize device threads across the CFT team. The common setup is
to request one barrier per CTA and use `blockIdx.x`

as the barrier index.

```
__global__ void cftBarrierKernel(ncclDevComm devComm) {
ncclCoopCta coop;
ncclCftBarrierSession<ncclCoopCta> bar{coop, devComm, blockIdx.x};
bar.sync(coop, cuda::memory_order_acq_rel,
ncclMemProxyType::Generic, ncclMemProxyType::Fabric);
}
```

For multicast CFT barriers, create the device communicator with
[ NCCL_CFT_MULTIMEM](https://docs.nvidia.com/api/device_cft.html#c.NCCL_CFT_MULTIMEM) and pass

`multimem=true`

to the barrier session
constructor.## Examples[](https://docs.nvidia.com#examples)

See the CFT barrier example under
`docs/examples/06_device_api/04_cft_barrier`

for a complete runnable CFT
setup and kernel.

## Cross-proxy Fences[](https://docs.nvidia.com#cross-proxy-fences)

Cross-proxy fences enforce memory ordering between operations issued by different
producer and consumer proxies. The common use case for fence is ordering of data
and flag updates to establish a `happens-before`

relationship between producer
stores and consumer loads to the same memory region. In the following example, the
producer is the Fabric proxy, while the consumer (ommitted) is the Generic proxy.
The consumer polls on the flag using relaxed loads and, after observing the flag
update, issues a fence with memory_order_acquire, Fabric producer, Generic consumer
and memory scope Sys.

```
__global__ void cftPutKernel(ncclDevComm devComm, ncclWindow_t win) {
__shared__ ncclCftSmem cftSmem;
__shared__ alignas(16) char smem[128];
__shared__ alignas(16) int flag[4];
ncclCoopCta coop;
ncclCft<ncclCoopCta> cft{coop, cftSmem};
ncclTeam cftTeam = ncclTeamCft(devComm);
int peer = (cftTeam.rank + 1) % cftTeam.nRanks;
ncclCftLeId leId;
size_t leOffset;
ncclGetCftLeInfo(win, 0, peer, cftTeam, devComm, &leId, &leOffset);
cft.put(coop, leId, leOffset, smem, sizeof(smem));
cft.submit(coop);
cft.flush(coop);
ncclMemFence(coop, cuda::memory_order_release, ncclMemProxyType::Fabric, ncclMemProxyType::Generic, ncclMemFenceScope::Sys);
cft.put(coop, leId, leOffset + flagOffset, flag, 16);
cft.submit(coop);
cft.flush(coop);
}
```

Another use case for fence is ordering accesses to shared memory between the Generic proxy and the Fabric proxy. In the following example, the Generic proxy updates shared memory and makes the updates visible to the Fabric proxy using a fence.

```
__shared__ncclCftSmem cftSmem;
ncclCoopCta coop;
ncclCft<ncclCoopCta> cft{coop, cftSmem};
__shared__ alignas(16) payload[4];
payload[0] = payload[1] = payload[2] = payload[3] = 1;
ncclMemFence(coop, cuda::memory_order_release, ncclMemProxyType::Generic, ncclMemProxyType::Fabric, ncclMemFenceScope::Cta);
cft.put(coop, leId, leOffset, payload, 16);
cft.submit(coop);
cft.flush(coop);
```