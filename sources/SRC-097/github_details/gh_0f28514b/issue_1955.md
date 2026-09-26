# [Issue #1955] [BUG] POSIX releaseXferReq() causes use-after-free

source: https://github.com/ai-dynamo/nixl/issues/1955
state: open | updated: 2026-09-11T15:17:37Z
labels: cancellation

## 正文

The POSIX backend deletes an active request without removing its pending queue entries. A later queue poll can invoke a callback through the freed request handle leading to use-after-free.

This code path is possible:

1. `postXferReq()` queues POSIX I/O entries. Each entry stores the backend request handle as its callback context.
2. The user calls `releaseXferReq()` while the transfer is still `NIXL_IN_PROG`.
3. The agent calls the backend's `releaseReqH()` ([call site](https://github.com/ai-dynamo/nixl/blob/main/src/core/nixl_agent.cpp#L1305-L1328)).
4. POSIX unconditionally deletes the handle and returns `NIXL_SUCCESS` ([implementation](https://github.com/ai-dynamo/nixl/blob/main/src/plugins/posix/posix_backend.cpp#L341-L345)).
5. The queued/in-flight I/O entries remain in the shared backend queue. A later `poll()`, possibly for another transfer, reaps one and calls `ioDoneClb()` with the freed context.

This can cause a use-after-free. Returning success is also unsafe because the kernel may still be using buffers or file descriptors that the caller is now allowed to release.

### Expected behavior

If POSIX cannot abort an active transfer, `releaseXferReq()` should return an error and keep the request alive and pollable. Release should succeed only after all entries referencing the request have completed or been canceled.

### Additional potential problem with THREAD_SYNC_RW

With `NIXL_THREAD_SYNC_RW`, two threads may concurrently release request A and poll request B. Both requests share the same I/O queue. If A remains in progress, `releaseReqH()` deletes its handle without taking `io_queue_lock_` or draining/canceling its I/Os. A subsequent poll through B can reap A’s completion and invoke `ioDoneClb()` using the freed handle stored in `ctx_`, causing memory corruption or a crash.

### Fix

After some internal discussion we reached an agreement that `releaseReqH` should follow the following pseudocode:
```
releaseReqH() {
	if(no outstanding requests){
	   delete handle;
	   return SUCCESS;
	} else {
	   // Optional: Cancel (synchronous) outstanding operations
	   // Optional: Initiate asynchronous cancellation, correct clients keep polling in this case on checkXfer. Reap cancel completions there.
	   return ERR; 
	}
}
```

-> quarantined collection should not be necessary anymore as the backend can be written assuming that the handle stays alive.
-> Incorrect clients that do not check the return value will leak memory, but that's ok, better than uncoditional delete and use-after-free
-> This pattern is not yet very prevalent in the codebase, but we will work towards it.

This is separate from the error-recovery PR (#1942 and following): it concerns user-requested release of a normal active transfer.

## 评论 (1)

### lluki · 2026-09-11

*Updated the suggested fix, this is the approach we will take:*

After some internal discussion we reached an agreement that `releaseReqH` should follow the following pseudocode:
```
releaseReqH() {
	if(no outstanding requests){
	   delete handle;
	   return SUCCESS;
	} else {
	   // Optional: Cancel (synchronous) outstanding operations
	   // Optional: Initiate asynchronous cancellation, correct clients keep polling in this case on checkXfer. Reap cancel completions there.
	   return ERR; 
	}
}
```

-> quarantined collection should not be necessary anymore as the backend can be written assuming that the handle stays alive.
-> Incorrect clients that do not check the return value will leak memory, but that's ok, better than uncoditional delete and use-after-free
-> This pattern is not yet very prevalent in the codebase, but we will work towards it.



Eventually, we want clients to perform cancellation as follows. The PR fixing this bug is not expected to make it 

```
# Note: This is pseudocode, not python. Python raises an exception on NIXL_ERR_REPOST 


  request = agent.create_xfer_request(...)
  agent.post_xfer_request(request)
  ....
  # Initiate cancellation.
  status = agent.release_xfer_request(request)

  if status == NIXL_ERR_REPOST_ACTIVE:
      status = agent.get_xfer_status(request)
      while status == NIXL_IN_PROG:
          time.sleep(0.001)
          status = agent.get_xfer_status(request)

      agent.release_xfer_request(request) # = Success
```
