# [Issue #1514] LIBFABRIC backend: Add thread pool support to LIBFABRIC backend's postXfer for parallel descriptor posting

source: https://github.com/ai-dynamo/nixl/issues/1514
state: closed | updated: 2026-06-26T23:46:44Z
labels: 

## 正文

**ISSUE**
The LIBFABRIC backend posts RDMA descriptors synchronously in a single-threaded loop within postXfer(). When KV cache block fragmentation prevents NIXL's descriptor merging, the descriptor count can grow from ~160 to ~18,880 for a single transfer (Llama-70B, TP=8, 80 layers × 2 K/V × 118 blocks). Each descriptor requires a separate fi_writedata()/fi_read() call, resulting in ~46ms of CPU time on the calling thread. This blocks the vLLM worker thread from running model forward, stalling all in-flight decode requests. Such high post times are actually dominating the overall KV transfer latencies.

The UCX backend solves this to some extent with nixlUcxThreadPoolEngine, which splits descriptors across a configurable thread pool (num_threads). The LIBFABRIC backend has no equivalent mechanism and does not consume the num_threads configuration parameter.


**WHAT NEEDS TO BE IMPLEMENTED**
The LIBFABRIC backend shall support multi-threaded descriptor posting in postXfer(), handling fi_writedata()/fi_read() calls across a configurable number of worker threads.

The LIBFABRIC backend shall consume the existing num_threads configuration parameter from nixl_agent_config, consistent with how other backends are using it.

**Code snippets**
libfabric_backend.cpp
~~~

// Core transfer submission to process each descriptor with direct submission
  for (int desc_idx = 0; desc_idx < desc_count; ++desc_idx) {
    auto *local_md = static_cast<nixlLibfabricPrivateMetadata *>(local[desc_idx].metadataP);
    auto *remote_md = static_cast<nixlLibfabricPublicMetadata *>(remote[desc_idx].metadataP);
    if (!local_md || !remote_md || !remote_md->conn_) {
      NIXL_ERROR << "Invalid metadata pointers for descriptor " << desc_idx;
      return NIXL_ERR_INVALID_PARAM;
    }

    // Validate connection for this descriptor
    if (remote_md->conn_ != conn_it->second) {
      NIXL_ERROR << "Connection mismatch for descriptor " << desc_idx;
      return NIXL_ERR_MISMATCH;
    }
    // Get transfer info for THIS descriptor
    void *transfer_addr = (void *)local[desc_idx].addr;
    size_t transfer_size = local[desc_idx].len;
    int device_id = local[desc_idx].devId;

    NIXL_DEBUG << "Processing descriptor " << desc_idx << " device " << device_id
          << " local_addr: " << transfer_addr << " size=" << transfer_size
          << " remote_addr=" << (void *)remote[desc_idx].addr;

    NIXL_DEBUG << "DEBUG: remote_agent='" << remote_agent << "' localAgent='" << localAgent
          << "'";

    // Prepare and submit transfer for remote agents
    // Use descriptor's specific target address
    uint64_t remote_target_addr = remote[desc_idx].addr;

    uint64_t remote_registered_base = remote_md->remote_buf_addr_;

    size_t submitted_count = 0;
    nixl_status_t status = rail_manager.prepareAndSubmitTransfer(
      op_type,
      transfer_addr,
      transfer_size,
      remote_target_addr,
      remote_registered_base,
      local_md->selected_rails_,
      local_md->rail_mr_list_,
      remote_md->rail_remote_key_list_,
      remote_md->remote_selected_endpoints_,
      conn_it->second->rail_remote_addr_list_,
      conn_it->second->agent_index_,
      backend_handle->post_xfer_id,
      [backend_handle]() {
        backend_handle->increment_completed_requests();
      }, // Completion callback
      submitted_count);
~~~

ucx_backend.cpp

~~~
nixl_status_t
nixlUcxThreadPoolEngine::sendXferRange(const nixl_xfer_op_t &operation,
                    const nixl_meta_dlist_t &local,
                    const nixl_meta_dlist_t &remote,
                    const std::string &remote_agent,
                    nixlBackendReqH *handle,
                    size_t start_idx,
                    size_t end_idx) const {
  nixlUcxBackendH *int_handle = static_cast<nixlUcxBackendH *>(handle);
  if (!int_handle->isComposite()) {
    return nixlUcxEngine::sendXferRange(
      operation, local, remote, remote_agent, handle, start_idx, end_idx);
  }

  nixlUcxCompositeBackendH *comp_handle = static_cast<nixlUcxCompositeBackendH *>(int_handle);
  comp_handle->startXfer();
  size_t chunk_size = comp_handle->getChunkSize();
  NIXL_TRACE << "sending " << *comp_handle;

  std::promise<void> promise;
  std::future<void> future = promise.get_future();
  std::atomic<size_t> remaining{comp_handle->getNumChunks()};
  std::atomic<nixl_status_t> status{NIXL_SUCCESS};

  for (size_t i = 0; i < comp_handle->getNumChunks(); i++) {
    io_->post([&, i]() {
      auto thread = nixlUcxDedicatedThread::getDedicatedThread();
      NIXL_ASSERT(thread != nullptr);

      nixlUcxChunkBackendH *chunk_handle =
        comp_handle->startChunk(i, thread->getWorkers()[0], thread->getWorkerId());
      NIXL_TRACE << "dedicated " << *thread << " starting " << *chunk_handle;

      size_t start_idx = i * chunk_size;
      size_t end_idx = std::min(start_idx + chunk_size, (size_t)local.descCount());
      nixl_status_t ret = nixlUcxEngine::sendXferRange(
        operation, local, remote, remote_agent, chunk_handle, start_idx, end_idx);
      if (ret != NIXL_SUCCESS) {
        status.store(ret);
        chunk_handle->complete(ret);
      } else {
        NIXL_TRACE << "dedicated " << *thread << " sent " << *chunk_handle;
        thread->addRequest(chunk_handle);
      }

      if (remaining.fetch_sub(1) == 1) {
        promise.set_value();
      }
    });
  }

  future.wait();
  NIXL_TRACE << "sent " << *comp_handle << " with status: " << status.load();
  return status.load();
}

~~~


## 评论 (2)

### aknvda · 2026-04-24

PR: https://github.com/ai-dynamo/nixl/pull/1581

### aknvda · 2026-06-06

POSIX changes are merged via https://github.com/ai-dynamo/nixl/pull/1605 was today. LIBFABRIC changes are in PR: https://github.com/ai-dynamo/nixl/pull/1581 and are currently being reviewed.
