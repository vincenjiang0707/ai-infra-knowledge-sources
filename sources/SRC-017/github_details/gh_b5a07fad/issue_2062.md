# [Issue #2062] [Issue]: Potential BUG: Memory Visibility and Race Condition in bootstrapNetInit (Identified by RustCC)

source: https://github.com/NVIDIA/nccl/issues/2062
state: closed | updated: 2026-08-03T20:12:35Z
labels: 

## 正文

### How is this issue impacting you?

Data corruption

### Share Your Debug Logs

I have developed a Rust C/C++ library that applies Rust abstractions on CC code. 

### Steps to Reproduce the Issue

_No response_

### NCCL Version

NCCL 2.28.7 (package revision 1)

### Your platform details

Title: [Potential Bug] Memory Visibility and Race Condition in bootstrapNetInit (Identified by RustCC)

Description:
A potential concurrency risk was identified in src/bootstrap.cc during a scan by RustCC (a specialized C++ profiler/static analysis tool based on Rust-style memory safety rules). The implementation of bootstrapNetInit uses a Double-Checked Locking (DCL) pattern that lacks the necessary atomic synchronization required by the C++11 (and later) memory model.

Location:
File: src/bootstrap.cc
Lines: 86-96

C++
86  static char bootstrapNetIfName[MAX_IF_NAME_SIZE+1];
87  static union ncclSocketAddress bootstrapNetIfAddr;
88  static int bootstrapNetInitDone = 0;  // <--- Risk: Plain int
...
94  if (bootstrapNetInitDone == 0) {
95      std::lock_guard<std::mutex> lock(bootstrapNetMutex);
96      if (bootstrapNetInitDone == 0) {
Technical Analysis:
The variable bootstrapNetInitDone is a plain int accessed outside the mutex at line 94. While this pattern is common, it poses two significant risks in modern C++:

Instruction Reordering: Without std::atomic and proper memory barriers, the compiler or CPU could reorder the store bootstrapNetInitDone = 1 before the actual initialization of bootstrapNetIfName or bootstrapNetIfAddr. A concurrent thread could see bootstrapNetInitDone == 1, skip the lock, and attempt to use uninitialized networking data.

Memory Visibility: On non-x86 architectures (e.g., ARM64/Grace-Hopper), the update to bootstrapNetInitDone might not be immediately visible to other cores without an explicit memory barrier, leading to unnecessary contention.

Tool Report (RustCC):

Rule: TCC-CONC-001 (Unsynchronized Access in DCL)

Confidence: HIGH

Interpretation: Violation of memory safety policy. The code relies on implicit hardware ordering which is not guaranteed across all supported NCCL platforms.

Suggested Fix:
Refactor bootstrapNetInitDone to use std::atomic<int> with acquire/release semantics to ensure proper synchronization without sacrificing performance.

C++
static std::atomic<int> bootstrapNetInitDone{0};

ncclResult_t bootstrapNetInit() {
    if (bootstrapNetInitDone.load(std::memory_order_acquire) == 0) {
        std::lock_guard<std::mutex> lock(bootstrapNetMutex);
        if (bootstrapNetInitDone.load(std::memory_order_relaxed) == 0) {
            // ... Initialization Logic ...
            bootstrapNetInitDone.store(1, std::memory_order_release);
        }
    }
    return ncclSuccess;
}

### Error Message & Behavior

yunqu.liu@gmail.com

## 评论 (9)

### yunquleonliu · 2026-03-23

RustCC reported over 1000 Concurrent riskes, but likely 99.99% were protected well with Mutex.

### AddyLaddy · 2026-03-24

/mirror


### yunquleonliu · 2026-03-24

To clarify, this report is from RustCC static analysis rather than from a runtime containerized workload, so I do not have a Docker/container reproducer to share. The finding is source-level in `src/bootstrap.cc`:

### ankohuu · 2026-05-10

TSAN can also report this issue， a small test code with replacing bootstrap.o with TSAN=1 in libnccl.

```
setarch "$(uname -m)" -R /tmp/nccl_bootstrap_net_init_test                                                                             23:40:28 [41/68]
==================
WARNING: ThreadSanitizer: data race (pid=837040)
  Write of size 4 at 0x555557532768 by thread T1 (mutexes: write M0):
    #0 bootstrapNetInit() /home/ankohuu/Project/nccl/src/bootstrap.cc:136 (nccl_bootstrap_net_init_test+0x6f974) (BuildId: 31755828bf15fc7ae312ec49d3f43a797801946f)
    #1 main::{lambda()#1}::operator()() const <null> (nccl_bootstrap_net_init_test+0x685c7) (BuildId: 31755828bf15fc7ae312ec49d3f43a797801946f)
    #2 void std::__invoke_impl<void, main::{lambda()#1}>(std::__invoke_other, main::{lambda()#1}&&) <null> (nccl_bootstrap_net_init_test+0x693e8) (BuildId: 31755828bf15fc7
ae312ec49d3f43a797801946f)
    #3 std::__invoke_result<main::{lambda()#1}>::type std::__invoke<main::{lambda()#1}>(main::{lambda()#1}&&) <null> (nccl_bootstrap_net_init_test+0x6935f) (BuildId: 31755
828bf15fc7ae312ec49d3f43a797801946f)
    #4 void std::thread::_Invoker<std::tuple<main::{lambda()#1}> >::_M_invoke<0ul>(std::_Index_tuple<0ul>) <null> (nccl_bootstrap_net_init_test+0x692c0) (BuildId: 31755828
bf15fc7ae312ec49d3f43a797801946f)
    #5 std::thread::_Invoker<std::tuple<main::{lambda()#1}> >::operator()() <null> (nccl_bootstrap_net_init_test+0x69266) (BuildId: 31755828bf15fc7ae312ec49d3f43a797801946
f)
    #6 std::thread::_State_impl<std::thread::_Invoker<std::tuple<main::{lambda()#1}> > >::_M_run() <null> (nccl_bootstrap_net_init_test+0x6921c) (BuildId: 31755828bf15fc7a
e312ec49d3f43a797801946f)
    #7 <null> <null> (libstdc++.so.6+0xecdb3) (BuildId: 753c6c8608b61d4e67be8f0c890e03e0aa046b8b)

  Previous read of size 4 at 0x555557532768 by thread T2:
    #0 bootstrapNetInit() /home/ankohuu/Project/nccl/src/bootstrap.cc:108 (nccl_bootstrap_net_init_test+0x6f74e) (BuildId: 31755828bf15fc7ae312ec49d3f43a797801946f)
    #1 main::{lambda()#1}::operator()() const <null> (nccl_bootstrap_net_init_test+0x685c7) (BuildId: 31755828bf15fc7ae312ec49d3f43a797801946f)
    #2 void std::__invoke_impl<void, main::{lambda()#1}>(std::__invoke_other, main::{lambda()#1}&&) <null> (nccl_bootstrap_net_init_test+0x693e8) (BuildId: 31755828bf15fc7
ae312ec49d3f43a797801946f)
    #3 std::__invoke_result<main::{lambda()#1}>::type std::__invoke<main::{lambda()#1}>(main::{lambda()#1}&&) <null> (nccl_bootstrap_net_init_test+0x6935f) (BuildId: 31755
828bf15fc7ae312ec49d3f43a797801946f)
    #4 void std::thread::_Invoker<std::tuple<main::{lambda()#1}> >::_M_invoke<0ul>(std::_Index_tuple<0ul>) <null> (nccl_bootstrap_net_init_test+0x692c0) (BuildId: 31755828
bf15fc7ae312ec49d3f43a797801946f)
    #5 std::thread::_Invoker<std::tuple<main::{lambda()#1}> >::operator()() <null> (nccl_bootstrap_net_init_test+0x69266) (BuildId: 31755828bf15fc7ae312ec49d3f43a797801946
f)
    #6 std::thread::_State_impl<std::thread::_Invoker<std::tuple<main::{lambda()#1}> > >::_M_run() <null> (nccl_bootstrap_net_init_test+0x6921c) (BuildId: 31755828bf15fc7a
e312ec49d3f43a797801946f)
    #7 <null> <null> (libstdc++.so.6+0xecdb3) (BuildId: 753c6c8608b61d4e67be8f0c890e03e0aa046b8b)

  Location is global 'bootstrapNetInitDone' of size 4 at 0x555557532768 (nccl_bootstrap_net_init_test+0x1fde768)
```

### AddyLaddy · 2026-05-29

The static analysis of that function in isolation may be correct but `bootstrapNetInit()` is called from `initOnceFunc()`, and `ncclInit()` invokes that through `std::call_once(initOnceFlag, initOnceFunc)`
So this race condition will not be experienced by the NCCL code.

### yunquleonliu · 2026-06-03

> The static analysis of that function in isolation may be correct but `bootstrapNetInit()` is called from `initOnceFunc()`, and `ncclInit()` invokes that through `std::call_once(initOnceFlag, initOnceFunc)` So this race condition will not be experienced by the NCCL code.

Hi Addy,

The issue is not only an x86-vs-ARM problem; it is a C++ memory model problem too. 

In the code, the bootstrapNetInitDone is a non-atomic variable that is read outside the mutex and written inside the mutex. Under the C++ standard, that constitutes a data race and therefore undefined behavior.

On x86, strong TSO ordering and cache coherence make the bug extremely difficult to observe in practice. Most executions will appear correct because stores become visible in a relatively predictable order. However, the C++ compiler is still FREE TO OPTIMIZE AROUND the unsynchronized load, so correctness is not guaranteed by the language.

On ARM and other weakly ordered architectures, the lack of acquire/release synchronization has a higher probability of exposing the problem because visibility and ordering of writes are less restrictive. A thread may observe bootstrapNetInitDone == 1 before all initialization writes are guaranteed visible.

Therefore, ankohuu is correct that the code is formally racy and non-portable. David, you are correct too that on current x86 systems, this may never reproduce reliably. The disagreement is about language-level correctness versus observed behavior

So, using std::atomic or std::call_once would remove the ambiguity. 

From my point of view, I used this to demo that RustCC (a Rust abstraction profiler for CC) could find memory errors, data races, and data ownership checks.

C++26 is moving towards that direction officially. So, thanks to Rust, but sticks with CC :-)

### yunquleonliu · 2026-06-03

I would close this issue @AddyLaddy if that is clear and clean enough

### sjeaugey · 2026-06-04

@yunquleonliu please read Addy's response again; I think you missed the point.

Yes, the `bootstrapNetInitDone = 1;` line is problematic, as there is no memory ordering enforced to ensure this is only done after all other setup. This should, in theory, be fixed to add a memory fence before, or acquire semantics. Sure, that issue doesn't apply to x86 but on arm and ppc, this would be an issue.

So we acknowledge the problem in the code.

But all that being said, the bootstrapNetInit() function is actually called inside a lock itself, which prevents any thread concurrency. So this issue cannot happen in practice since we added a `std::call_once` around `initOnceFunc()`.


### leliucurtiss · 2026-06-04

@sjeaugey Well said. On the same page now. the issue is closed.

Again, this is just a test for RustCC (A Rust inspired CC check profiler). Now, C++26 is going that way already. I am sure C++ will be  and shall be as safe as Rust. 

However, it made me curiously again. How about C? Is there some method to enhance C memory safety without the Smart Pointer, container etc. One may think that as impossible. But SmallTalk also said Class in C was impossible. 

The issue is closed. 
