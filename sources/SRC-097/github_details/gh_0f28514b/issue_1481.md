# [Issue #1481] nixl-sys: remote XferRequest cleanup uses corrupted remote_agent name, causing invalidateRemoteMD NIXL_ERR_NOT_FOUND

source: https://github.com/ai-dynamo/nixl/issues/1481
state: open | updated: 2026-03-31T22:30:43Z
labels: 

## 正文

What I observed:

  - The remote G3PB transfer only works after lib/llm/src/block_manager/block/transfer/nixl.rs stops targeting the local agent and instead uses the remote agent name.
  - But after success, NIXL logs:
      - invalidateRemoteMD: error invalidating remote metadata for agent '53…' with status NIXL_ERR_NOT_FOUND
  - The agent string is corrupted-looking, which is the important clue.

  Why this points at nixl-sys / wrapper ownership:

  - In the Rust binding, create_xfer_req builds a temporary CString from remote_agent and passes remote_agent.as_ptr() into C:
      - /root/.cargo/registry/src/index.crates.io-1949cf8c6b5b557f/nixl-sys-0.10.1/src/agent.rs:841
  - In the C++ wrapper, that pointer is turned into a temporary std::string(remote_agent) and passed into createXferReq(...):
      - /root/.cargo/registry/src/index.crates.io-1949cf8c6b5b557f/nixl-sys-0.10.1/wrapper.cpp:1468
  - The wrapper request handle stores only req, not the remote agent string:
      - /root/.cargo/registry/src/index.crates.io-1949cf8c6b5b557f/nixl-sys-0.10.1/wrapper.cpp:91

  That is consistent with:

  - transfer setup works
  - later cleanup/invalidation uses stale or lost remote-agent identity

  So the likely issue to file is:

  - nixl-sys C API wrapper may not preserve the remote_agent lifetime across XferRequest cleanup/release
  - successful transfer later fails in invalidateRemoteMD with corrupted remote agent name / NIXL_ERR_NOT_FOUND

  Important nuance:
  - I cannot prove from outside whether the bug is in nixl-sys wrapper or deeper in core NIXL.
  - But the wrapper is a very plausible culprit and is the narrowest reproducible layer to report.

  A good issue summary would be:
  - Remote transfer request succeeds
  - Later invalidateRemoteMD runs with corrupted agent name
  - Repro uses remote peer transfer, not local transfer
  - Suspect create_xfer_req wrapper does not retain remote_agent identity for the full request lifetime

  Suggested issue contents:

  1. Environment: nixl-sys 0.10.1
  2. Symptom:
      - remote transfer succeeds
      - cleanup logs corrupted agent name
      - invalidateRemoteMD ... NIXL_ERR_NOT_FOUND
  3. Relevant wrapper code:
      - temporary CString in src/agent.rs
      - temporary std::string(remote_agent) in wrapper.cpp
      - request wrapper stores only req
  4. Minimal expectation:
      - if remote_agent is needed after createXferReq, wrapper/request handle should own stable storage for it

## 评论 (1)

### michaelfeil · 2026-03-31

```
Your hypothesis is PARTIALLY CORRECT but the root cause is different.
What I Found:
1. The wrapper DOES properly preserve the remote_agent - The nixlXferReqH class stores remoteAgent as a const std::string member (transfer_request.h:63), so it's properly owned for the lifetime of the request.
2. The real bug is in the Rust code - Looking at /workspace/model-performance/michael131/mfdynamo/lib/llm/src/block_manager/block/transfer/nixl.rs line 123:
      &nixl_agent.name(),  // This passes the LOCAL agent name, not the remote!
   
   This should be passing the remote peer's agent name, not the local agent's name.
3. Why you see the error after "fixing" it - When you changed it to use the remote agent name, the transfer works, but the invalidateRemoteMD error suggests there may be a separate issue with how the remote agent metadata is being managed or cleaned up.
Verification:
The wrapper code at wrapper.cpp:1491 is correct:
std::string(remote_agent)  // Creates a temporary, passed by const ref to createXferReq
And createXferReq copies it into the nixlXferReqH object which stores it as a member variable.
Your hypothesis about wrapper ownership is NOT the bug - the wrapper correctly preserves the remote_agent. The actual bug is the API misuse in the Rust code passing the wrong agent name.
```
