# [Issue #3909] [Performance]: Segmentation fault in `asio` `epoll_reactor` when frequently recreating read-only RealClient under extreme network timeout

source: https://github.com/kvcache-ai/Mooncake/issues/3909
state: closed | updated: 2026-09-14T08:02:50Z
labels: 

## 正文

### Describe your performance question

# Overview
In large‑scale high‑throughput read‑only Mooncake workload, when simulating poor network with extremely short RPC timeout, tearing‑down and recreating read‑only RealClient after consecutive RPC timeouts triggers SIGSEGV null‑pointer crash. The service runs stable with normal MC_RPC_TIMEOUT_MS=400.
Hypothesis: Race between in‑flight coro‑rpc TCP async coroutine requests and client close / object destruction. According to coro_rpc doc, only send_request is thread‑safe; connect / close / object destruction must not run concurrently with unfinished RPC. Short timeout amplifies the race window. Resumed coroutine access already‑freed socket descriptor_data and causes segfault.
# Deployment and Configuration
Cluster has 200 Mooncake storage nodes. Dataset is split into 200 partitions and fully persisted on local SSD without in‑memory read cache. Each storage node runs one `mooncake_master` plus one storage‑side RealClient; master only manages local RealClient. SSD offload & disk eviction enabled, promotion‑on‑hit disabled.

Read‑side host with 8 GPUs, per rank process:

1. One shared `TransferEngine`
2. 200 read‑only `RealClient` instances, one‑to‑one connect to 200 remote storage nodes, read‑only workload, `global_segment_size=0`
3. Business logic: use `batch_get_into` for batch read. After **5 consecutive rpc\_timeout failures**: invoke `tearDownAll()`, reset client object, later rebuild via `setup_internal`.

Per host scale: 8 ranks, total `200 * 8` read‑only RealClient, high‑throughput random read pattern.

## Storage node: mooncake_master launch args
``` bash
mooncake_master \
--rpc_port=8001 \
--rpc_thread_num=8 \
--rpc_enable_tcp_no_delay=true \
--metrics_port=8007 \
--default_kv_lease_ttl=5000 \
--allow_evict_soft_pinned_objects=true \
--eviction_ratio=0.45 \
--eviction_high_watermark_ratio=0.6 \
--cluster_id=flash_mooncake_cluster \
--allocation_strategy=free_ratio_first \
--quota_bytes=3298534883328 \
--enable_ha=false \
--enable_offload=true \
--offload_on_evict=true \
--offload_force_evict=false \
--enable_disk_eviction=true \
--promotion_on_hit=false
```
## Storage‑side RealClient env & launch
``` bash
MC_IB_PCI_RELAXED_ORDERING                         = 1
MOONCAKE_LOCAL_BUFFER_SIZE                         = 6442450944
MOONCAKE_OFFLOAD_BUCKET_EVICTION_POLICY            = lru
MOONCAKE_OFFLOAD_BUCKET_KEYS_LIMIT                 = 128
MOONCAKE_OFFLOAD_BUCKET_MAX_TOTAL_SIZE             = 3113851289600
MOONCAKE_OFFLOAD_BUCKET_SIZE_LIMIT_BYTES           = 268435456
MOONCAKE_OFFLOAD_CLIENT_BUFFER_GC_INTERVAL_SECONDS = 2
MOONCAKE_OFFLOAD_FILE_STORAGE_PATH                 = /ssd_file/mooncake_cache/
MOONCAKE_OFFLOAD_HEARTBEAT_INTERVAL_SECONDS        = 1
MOONCAKE_OFFLOAD_LOCAL_BUFFER_SIZE_BYTES           = 21474836480
MOONCAKE_OFFLOAD_STORAGE_BACKEND_DESCRIPTOR        = bucket_storage_backend
MOONCAKE_OFFLOAD_TOTAL_SIZE_LIMIT_BYTES            = 3221225472000
MOONCAKE_OFFLOAD_USE_URING                         = 1
mooncake_client \
--master_server_address=<local_node_ip>:8001 \
--host=<local_node_ip> \
--protocol=rdma \
--port=8005 \
--global_segment_size=35GB \
--enable_offload=true \
--threads=8 \
--metadata_server=P2PHANDSHAKE
```
## Read‑only RealClient env
``` bash
MC_STORE_CLIENT_MIN_PORT=12000
MC_STORE_CLIENT_MAX_PORT=30000
MC_STORE_CLIENT_SETUP_RETRIES=2
MC_RPC_TIMEOUT_MS=20 # Simulate extremely poor network
mooncake_client \
--master_server_address=<master_ip>:8001 \
--host=<master_ip> \
--protocol=rdma \
--port=8005 \
--global_segment_size=0 # read‑only client, no local storage
```
## Key code snippet
``` C++
// Establish read‑only client connection
auto rc = real_client_->setup_internal(
    transport_.local_hostname(),
    transport_.metadata_server(),
    0,        // global_segment_size: read‑only client
    0,        // local_buffer_size
    "rdma",
    "",       // rdma devices: auto‑discovery
    remote_addr_,
    shared_transfer_engine,
    "",       // ipc_socket_path unused
    0,        // local rpc port unused
    false,    // enable_ssd_offload disabled
    false,    // start offload rpc server disabled
    "",       // ssd offload path
    "",       // tenant_id
    false,    // enable_client_http_server
    8003      // client_http_port
);

// Read workflow
real_client_->register_buffer(recv_buf_.get(), buf_size_);
std::vector<void*>  bufs(chunk_bufs_.begin(), chunk_bufs_.begin() + batch_sz);
std::vector<size_t> sizes(batch_sz, chunk_size_);
auto ret = real_client_->batch_get_into(batch, bufs, sizes);

// After 5 consecutive rpc_timeout: tear down and recreate
real_client_->unregister_buffer(recv_buf_.get());
real_client_->tearDownAll();
real_client_.reset();
remote_addr_.clear();
// Later call setup_internal() to rebuild client

```
# Crash Backtrace
Crash occurs in TCP coro‑rpc path `BatchGetReplicaList`. Direct cause: `descriptor_data == nullptr`, null‑pointer dereference inside asio epoll\_reactor, SIGSEGV.
``` bash 
#0  asio::detail::epoll_reactor::start_op
      (this=0x7d1083a40380, op_type=1, descriptor=8739,
       descriptor_data=@0x7d0bf2892850: 0x0,   ← nullptr dereference
       op=0x7d0c6fe1e960, is_continuation=<optimized out>)
      at /usr/local/include/asio/detail/impl/epoll_reactor.ipp:245
      descriptor_lock = {mutex_=@0x7d0ca9ee37a8, locked_=true}

#1  asio::detail::reactive_socket_service_base::async_send (…)
      at /usr/local/include/asio/detail/reactive_socket_service_base.hpp:313
      is_continuation=false; slot={handler_=0x0}
      p={h=0x7d0fdf9f8550, v=0x7d0c6fe1e960, p=0x7d0c6fe1e960}

#2  asio::basic_stream_socket<tcp,any_io_executor>::initiate_async_send::operator() (…)
      at /usr/local/include/asio/basic_stream_socket.hpp:1141
#3  asio::detail::completion_handler_async_result<…>::initiate (…)
      at /usr/local/include/asio/async_result.hpp:481
#4  asio::async_initiate<…> (…)
      at /usr/local/include/asio/async_result.hpp:895
#5  asio::basic_stream_socket<…>::async_write_some (…)
      at /usr/local/include/asio/basic_stream_socket.hpp:970
#6  asio::detail::write_op<…>::operator() (ec=<optimized out>, start=1, bytes_transferred=0, this=0x7d0fdf9f8550)
      at /usr/local/include/asio/impl/write.hpp:344
      max_size=65536
#7  asio::detail::start_write_op<…> (…)
      at /usr/local/include/asio/impl/write.hpp:460
#8  asio::detail::initiate_async_write<…>::operator() (…)
      at /usr/local/include/asio/impl/write.hpp:492
#9..#11  asio::async_result / async_initiate / async_write (…)
      at /usr/local/include/asio/async_result.hpp:481 / :895 / impl/write.hpp:568
#12 coro_io::async_write<…> lambda::operator() (socket=<optimized out>, buffer=<optimized out>)
      at /usr/local/include/ylt/coro_io/coro_io.hpp:439
#13 coro_io::async_io<…> lambda::operator() (…)
      at /usr/local/include/ylt/coro_io/coro_io.hpp:281
#14 coro_io::callback_awaitor_base<…>::await_suspend (…)
      at /usr/local/include/ylt/coro_io/coro_io.hpp:81
#15 coro_io::async_io(…Frame*) (…)
      at /usr/local/include/ylt/coro_io/coro_io.hpp:280
#16 operator() (frame_ptr=0x7d0c3f969f00)   ← coroutine resume point
      at /usr/local/include/async_simple/coro/Lazy.h:422
#17 async_simple::coro::detail::LazyBase<vector<expected<GetReplicaListResponse,…>>>::start<…>::operator() (…)
      at /usr/local/include/async_simple/coro/Lazy.h:422
#18 async_simple::coro::detail::LazyBase<…>::start<…> (…)
      at /usr/local/include/async_simple/coro/Lazy.h:427
#19 async_simple::coro::syncAwait<…> (executor=0x0, cond={_M_counter=0})
      at /usr/local/include/async_simple/coro/SyncAwait.h:45
#20 mooncake::MasterClient::invoke_batch_rpc<&WrappedMasterService::BatchGetReplicaList,…>
      (this=0x7d0c9ab46c30, input_size=<optimized out>)
      at /path/to/Mooncake/mooncake-store/src/master_client.cpp:416
      pool = shared_ptr<coro_io::client_pool<…>> (use count 2) = {get()=0x7d0c9b500010}
#21 mooncake::MasterClient::BatchGetReplicaList
      (this=0x7d0c9ab46c30, object_keys=vector(1), tenant_id="default")
      at /path/to/Mooncake/mooncake-store/src/master_client.cpp:559
#22 mooncake::Client::BatchQuery
      (this=0x7d0c9ab46c00, object_keys=vector(1), tenant_id="default")
      at /path/to/Mooncake/mooncake-store/src/client_service.cpp:1198
#24 mooncake::RealClient::batch_get_into_internal
      (this=0x7d0fdc40b700, keys=vector(1), buffers=vector(1), sizes=vector(1))
      at /path/to/Mooncake/mooncake-store/src/real_client.cpp:4870
#27 mooncake::RealClient::batch_get_into
      (this=0x7d0fdc40b700, keys=…, buffers=vector(1), sizes=vector(1))
      at /path/to/Mooncake/mooncake-store/src/real_client.cpp:4519
#28 MooncakeBackend::batch_get_into
      (this=0x7d1875a4e1c0, keys=…, result=…)
      at /path/to/cache_client.cpp:626

```
## Reproduction condition
- Reproduce: `MC_RPC_TIMEOUT_MS=20`
- Stable‑ok: `MC_RPC_TIMEOUT_MS=400`

## Analysis & Questions
Reference coro_rpc doc:
https://github.com/alibaba/yalantinglibs/blob/main/website/docs/zh/coro_rpc/coro_rpc_client.md#%E7%BA%BF%E7%A8%8B%E5%AE%89%E5%85%A8

Only partial APIs are thread‑safe for coro\_rpc\_client. `connect / close / object destruction` must not run concurrently with in‑flight `send_request`.

Race flow in our workload:

1. `MC_RPC_TIMEOUT_MS=20`, many RPC timeout rapidly.
2. Upper layer detect consecutive timeouts, immediately call `tearDownAll()` and reset RealClient object.
3. Some coro‑rpc coroutines are still suspended and in‑flight.
4. Coroutine resumes and operates already‑freed socket reactor resource → null‑pointer crash.

# Questions:

1. Is this crash caused purely by race between in‑flight RPC and client destruction?
2. For read‑only `RealClient` (`global_segment_size=0`), should Mooncake add in‑flight request counter / guard to prevent destroying client with outstanding requests?
3. What is the recommended safe pattern to tear‑down & recreate read‑only client on RPC timeout?

### Before submitting a new issue...

- [x] Make sure you already searched for relevant issues and read the [documentation](https://kvcache-ai.github.io/Mooncake/)

## 评论 (4)

### github-actions[bot] · 2026-09-07

Thanks for opening this issue, @waliwali777!

| Field | Value |
|-------|-------|
| **Issue** | #3909 |
| **GitHub user ID** | `51405922` |
| **Reporter** | @waliwali777 |

A maintainer will triage this when possible. To help us respond faster, please include:

- Mooncake version or commit SHA
- Environment (OS, CUDA/driver, RDMA stack if relevant)
- Steps to reproduce and expected vs. actual behavior

Useful links: [Documentation](https://kvcache-ai.github.io/Mooncake/) · [Contributing guide](https://github.com/kvcache-ai/Mooncake/blob/main/CONTRIBUTING.md)

> This message was posted automatically by the issue bot.

### he-yufeng · 2026-09-08

Taking this one. The mechanism chain on current main, read end to end:

- Read-side calls go through `RpcClientPool` (`mooncake-common/include/rpc_client_io_context.h`), which hands out a shared `coro_io::client_pool` per master address and recreates it on address change.
- `MasterClient::~MasterClient()` is `= default` and `RealClient` teardown likewise never drains: the pool shared_ptr just drops while `co_await pool->send_request(...)` coroutines can still be suspended (`master_client.cpp:344/356/388/399`).
- When the last pool reference dies mid-flight, the resumed coroutine touches freed client/connection state — the asio `epoll_reactor` segfault you saw. Short `MC_RPC_TIMEOUT_MS` widens the window exactly as you described, since more requests are in flight at teardown.

Fix shape I am implementing: an in-flight guard around the send_request path plus drain-on-destruct (stop admitting, wait bounded for in-flight to land, then release the pool), so teardown never frees state under a suspended coroutine. I will add a stress regression test that floods short-timeout reads while tearing down the client — red on current main, clean after.


### he-yufeng · 2026-09-08

PR #3943 is up. One honest correction to my plan note above: the stress harness did not reproduce your crash deterministically in-process (your 200-node timing window is much wider than a single-container loop), so the PR verifies by construction against ylt's documented thread-safety contract plus guard-semantics unit tests and a 16-in-flight teardown stress test that is green with the fix. While building it I also found that draining alone is insufficient: ylt's reconnect loop references pool storage across sleeps, which is why the PR also stops freeing pools (process-wide registry per address). If your environment still crashes on this branch, a stack from your side would pin whatever path mine missed.


### waliwali777 · 2026-09-11

Thanks a lot for your fix. I’ve added your PR and reran the test twice with an extremely short RPC timeout. So far I haven’t observed any core dumps. I will post more findings here if we see anything new in subsequent observations.
