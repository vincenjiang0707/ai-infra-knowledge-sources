# [Issue #1392] Nixl register/deregister_memory slowing down after repeated calls

source: https://github.com/ai-dynamo/nixl/issues/1392
state: closed | updated: 2026-04-21T18:57:55Z
labels: 

## 正文

nixl_register_memory seems to progressively slow down after repeatedly calling nixl_register_memory and nixl_deregister_memory for large amounts of data. I profiled memory registration overhead using a dummy workload where I register 2GB (10000 tensor views where each view has a size of 200KB). I repeatedly register/deregister the memory for these tensor views, and I found that the memory registration time started increasing very heavily, almost exponentially. After 55 ~ 60 register/deregister loops, it pretty much got stuck. I did this on an A100 and A10G GPU, and my nixl version is 0.10.1.

## 评论 (17)

### Sparks0219 · 2026-03-04

@mkhazraee would you be able to take a look and is this a known issue? We're getting around this in Ray by keeping the memory registration around for repeated transfers of the same data instead of deregistering it, but I feel like this should just work without doing this. 

### tvegas1 · 2026-03-06

Can you please provide your reproducer?

### mkhazraee · 2026-03-11

Hmm, so the exact same registrations are taking longer? I can see the very first few being faster, and over time registration/deregisterations causing hash collisions or due to the number take slightly more time, but exponential rise is interesting. As Thomas said, let's take a look with a reproducer.

That being said, that's not a good usage pattern in general. Each registration/deregistration is a kernel call, and it would go through several layers. We always advice to do minimal number of registrations, the larger each of them the better, as it's just giving permission to the NIC to access that memory region. Doing it per small tensor and several of them, will increase the time to search over them, and make the most recent use optimization in lower layers impractical. 

This is inherent to one-sided communication, where you directly access application memory. In two sided communication, you practically copy to a bounce buffer which was registered, which you can also do here if the registration is unavoidable and you're fine with some memory overhead. Can you elaborate some on the use case, that needs a lot of small registration/deregistrations that cannot be merged?

Moein

### tvegas1 · 2026-03-13

@Sparks0219, kind reminder, you would be able to provide reproducer?

### Sparks0219 · 2026-03-30

Sorry for the delay @tvegas1 @mkhazraee took a bit to get just a pure NIXL repro. 

Some background context is that for RDT (Ray Direct Transport) we initially integrated NIXL by just individually registering the tensor which as you pointed is pretty bad. We did an optimization a while back where in the case a user passes us a list of pytorch tensors, we'll register the underlying storage block all at once instead of registering them one by one. Here's the place where we changed our registration logic: https://github.com/ray-project/ray/pull/60999/changes#diff-cc96bcffc37ccf8f15a13c4bcc0f982277b2e8d39d6a17f34c84f6830b6dcbd2R365

I think registering the underlying storage block fixes this performance degradation, but rather than an anti-pattern it seems pretty breaking and easy to trigger. Here's my repro: 

```python
"""
Repro for https://github.com/ai-dynamo/nixl/issues/1392
"""
import time
import torch
from nixl._api import nixl_agent, nixl_agent_config
ROW_SIZE_BYTES = 200 * 1024  # 200KB per row
NUM_ROWS = 10_000
USE_STORAGE_REGISTRATION = True  # Toggle: False = per-view (old), True = storage-level (new)
cols = ROW_SIZE_BYTES // 2  # float16 = 2 bytes
device = torch.device("cuda:0")
matrix = torch.zeros(NUM_ROWS, cols, dtype=torch.float16, device=device)
torch.cuda.synchronize()
views = [matrix[i] for i in range(NUM_ROWS)]
print(f"Matrix shape: {matrix.shape}  ({matrix.numel() * matrix.element_size() / 1e6:.2f} MB)")
print(f"Number of views: {len(views)}")
print(f"View shape: {views[0].shape}  ({views[0].numel() * views[0].element_size() / 1e3:.1f} KB each)")
print(f"Mode: {'storage-level (1 registration)' if USE_STORAGE_REGISTRATION else 'per-view (N registrations)'}")
print()
sender = nixl_agent("sender-agent", nixl_agent_config(backends=["UCX"]))
iteration = 0

while True:
    iteration += 1
    if USE_STORAGE_REGISTRATION:
        # Current RDT path: one registration for the entire storage
        t0 = time.perf_counter()
        reg_desc = sender.register_memory(
            [(matrix.untyped_storage().data_ptr(), matrix.untyped_storage().nbytes(), matrix.get_device(), "")],
            mem_type="cuda",
        )
        t_reg = time.perf_counter()
        sender.deregister_memory(reg_desc)
        t_dereg = time.perf_counter()
    else:
        # Old RDT path: one registration per view
        reg_descs = []
        t0 = time.perf_counter()
        for v in views:
            reg_desc = sender.register_memory([v])
            reg_descs.append(reg_desc)
        t_reg = time.perf_counter()
        for reg_desc in reg_descs:
            sender.deregister_memory(reg_desc)
        t_dereg = time.perf_counter()
      print(
          f"iter {iteration:>4d}  |  "
          f"register {(t_reg - t0)*1000:9.3f}ms  |  "
          f"deregister {(t_dereg - t_reg)*1000:9.3f}ms  |  "
          f"total {(t_dereg - t0)*1000:9.3f}ms"
      )
```

Here's some timings that I got. Note that it isn't cumulative, for example iter 10 just means how long registration/deregistration took at the 10 iteration, meaning we registered/deregistered the same tensors 9 times before. 

```
1000 rows
200KB tensors
Registering individual tensors
iter    1  |  register   857.315ms  |  deregister   220.120ms  |  total  1077.435ms
iter    2  |  register   199.465ms  |  deregister     2.830ms  |  total   202.296ms
iter   10  |  register   211.290ms  |  deregister     2.824ms  |  total   214.114ms
iter   50  |  register   303.108ms  |  deregister     3.757ms  |  total   306.865ms
iter  100  |  register   378.834ms  |  deregister     3.016ms  |  total   381.850ms

10000 rows 
200KB tensors
Registering individual tensors
iter    1  |  register 10449.209ms  |  deregister  3113.972ms  |  total 13563.181ms
iter    2  |  register  2854.300ms  |  deregister   160.786ms  |  total  3015.086ms
iter    5  |  register  3170.992ms  |  deregister   162.709ms  |  total  3333.701ms
iter   10  |  register  3894.398ms  |  deregister   166.288ms  |  total  4060.686ms
iter   15  |  register  4621.953ms  |  deregister   166.923ms  |  total  4788.876ms
iter   20  |  register  5463.795ms  |  deregister   176.255ms  |  total  5640.050ms

1000 rows
2MB tensors 
iter    1  |  register  1361.092ms  |  deregister   262.175ms  |  total  1623.266ms
iter    2  |  register   208.880ms  |  deregister     2.933ms  |  total   211.813ms
iter   10  |  register   215.993ms  |  deregister     2.975ms  |  total   218.968ms
iter   50  |  register   293.870ms  |  deregister     3.167ms  |  total   297.036ms
iter  100  |  register   363.835ms  |  deregister     3.094ms  |  total   366.929ms

10000 rows
200KB tensors 
Registering underlying storage tensor (so one 2GB registration)
iter    1  |  register    10.570ms  |  deregister     0.015ms  |  total    10.584ms
iter    2  |  register     0.219ms  |  deregister     0.003ms  |  total     0.223ms
iter 1000  |  register     0.179ms  |  deregister     0.002ms  |  total     0.180ms
iter 5000  |  register     0.176ms  |  deregister     0.002ms  |  total     0.177ms
iter 10000  |  register     0.180ms  |  deregister     0.002ms  |  total     0.182ms
```

So it seems like what you said @mkhazraee where the size of the memory regions being registered is pretty inconsequential, but the number of registrations is what kills you. However the same registrations/deregistrations continue to increase in time per iteration, scaling with the number of different memory regions. Hence for many small tensor views, it gets pretty bad. Please let me know what your thoughts are!

Also while creating this benchmark I think I found a different issue where if cols % 4096 != 0, the registration just seems to hang? Like I did cols = cols + 1 for the 10k rows/200KB tensor/registering individual tensor benchmark and it was stuck for 10 minutes on the memory registration for iteration 1 before I killed it. Not sure what's going on with that, like it seems to imply that if adjacent tensors share pages then something seems to break, would you have any thoughts on this as well? Thanks!

### Sparks0219 · 2026-03-30

I did all my testing on an AWS p4d.24xlarge instance which has A100 GPUs

### tvegas1 · 2026-03-30

Thanks for the reproducer, can you please check if #1469 fixes the issue? Also please note that `LIBFABRIC` plugin is the recommended plugin for AWS/EFA.

### Sparks0219 · 2026-03-30

Thanks @tvegas1 I'll try rerunning the benchmarks later this week. 

Just to confirm, you're saying to replace UCX with LIBFABRIC in the backends section of the nixl agent config? Ray is agnostic of the type of instance we run on, hence we could be running on AWS/GCP/Azure, etc. Is there a list of recommended plugins for each provider, and does NIXL itself do smart discovery of what is appropriate? 

Also would you have any ideas on why this benchmark hangs if I bump cols by 1? My initial guess is it might have something to do with page alignment (adjacent tensors in memory sharing pages on the boundaries), but not sure... 

### tvegas1 · 2026-03-31

Only for AWS/EFA, `LIBFABRIC` is NIXL agent backend config to use. Else UCX should be used, NIXL will not do smart discovery. Tried cols = cols + 1 but no repro, it's possible that this would be fixed #1469, although I did also try without the fix.

### Sparks0219 · 2026-03-31

Gotcha thanks @tvegas1. Also it might be easier if you reran the benchmark on your setup, could you check if #1469 fixes the issue? Sorry I'm a bit backed up this week hence getting through the setup might take a bit. 

### Sparks0219 · 2026-03-31

Hi @tvegas1 I talked to my team and we we're a bit confused since UCX should also support LIBFABRIC, is there any particular reason why we should use the NIXL LIBFABRIC plugin? Also is there some python nixl API that we could use to query if EFA devices are available on the current instance, I saw that NIXL does this in C++ https://github.com/ai-dynamo/nixl/blob/e0524ea3b5d9563c439a195b0b2e43aa2db97e99/src/utils/common/hw_info.cpp#L80 but couldn't find a python API to grab the hwInfo struct. 

### tvegas1 · 2026-04-01

UCX does not support libfabric. LIBFABRIC plugin would have better support for various topologies with EFA. For querying I am not aware of official python way to check, you could use similar approach or check `fi_info -p efa`, `/sys/class/net/efa*`.

### Sparks0219 · 2026-04-01

Sorry to keep bothering you @tvegas1 but just to make sure I follow, do you mean this is deprecated/not currently used then https://ofiwg.github.io/libfabric/main/man/fi_ucx.7.html ? 

### tvegas1 · 2026-04-02

You are now referring to libfabric supporting UCX as a provider. This would be for use-case (1) below which is not relevant for NIXL. NIXL LIBFABRIC plugin use-case is AWS/EFA.

(1) `Application (MPI / custom app) → Libfabric API → fi_ucx provider → UCX → Network hardware`

### Sparks0219 · 2026-04-03

Ahh I see that makes sense, thanks!

### mkhazraee · 2026-04-06

Can you recap the current state regarding the bug? Did those fixes help with the increasing registration time? I can see a little bit of increase, let's say slight linear increase as number of registrations increase due to larger internal state, but not a sudden jump, which seemed to be the case before.

Regarding UCX with Libfabric, generally NIXL is vendor agnostic. Now that Libfabric provided a backend to NIXL and is maintained by AWS themselves, it would be more comprehensive and they know exactly the underneath hardware, so would be more performant. As we mentioned in NIXL blog, we are working with Google Cloud to add both RDMA and GPUDirect-TCPXO networking. So in future that becomes available.

One way would be to instantiate all of the backends, and tell NIXL a priority list. As of now that's implemented based on the order of backend registrations, the earlier the higher the priority. That being said, doesn't some other parts of the Ray ecosystem need to know the cloud that it's being run on to do some configurations accordingly? Can't that pass that info to the NIXL relevant component? To me that sounds much cleaner, the orchestrator knows where things are being run, and each time NIXL doesn't need to try every possible scenario. 

### tvegas1 · 2026-04-09

>Can you recap the current state regarding the bug? Did those fixes help with the increasing registration time? I can see a little bit of increase, let's say slight linear increase as number of registrations increase due to larger internal state, but not a sudden jump, which seemed to be the case before.

Fixed by #1469, failing to remove self remote sections on `deregisterMem()` was causing forever increasing ordered list size (stale descriptors).
