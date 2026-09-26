# [Issue #6542] [Q] Unexpected performance with multi-thread mode

source: https://github.com/openucx/ucx/issues/6542
state: open | updated: 2026-03-25T14:03:34Z
labels: 

## 正文

Scenario：

Only *one* worker send seq and receive response with multi-thread mode.

```c
worker_params.thread_mode = UCS_THREAD_MODE_MULTI;
```

The worker invokes the `ucp_worker_progress` function in either of the following methods.



1. Main process uses following code to progress the worker.

```c
while(1) {
    count = ucp_worker_progress(g_clientUcxInfo.worker);
}
```

​	While Other processes use `ucp_am_send_nbx` and `ucp_am_recv_data_nbx` to concurrently receive and send messages with multi-thread. 



2. Main process uses a `ucp_worker_wait` function to wakeup the worker.

```c
while(1) {
        count = ucp_worker_progress(g_clientUcxInfo.worker);
        if(count == 0) {
            status = ucp_worker_wait(g_clientUcxInfo.worker);
        }
    }
```

​	While Other processes use `ucp_put_nbx` and `ucp_put_nbx` to concurrently receive and send messages with multi-thread. 

#### Problem:

According to our experience, the first method should be faster than the second method. However, we found the second method is over 100 times faster than the first method. We guess that because some locks are added to the process of calling UCP, which causes the delay\. We want to know whether our guess is right? And is there have a better way to use UCX in our scenario.

And could you help to delete my last incorrect issue?  Thank you. 



## 评论 (3)

### yosefe · 2021-03-23

@javion-z can you pls try UCX_USE_MT_MUTEX=y? it could work better when multiple threads try to acquire the lock at the same time

### javion-z · 2021-03-24

@yosefe Thank you, we'll try that. But we still wonder is there a better way to improve the performance of the first theoretically better method?  We guess that we did't use it in a right way. 

### TheWitness · 2026-03-25

Has there any update on this.  It's been 5 years since it was opened.  Thanks!
