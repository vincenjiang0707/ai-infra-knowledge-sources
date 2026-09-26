source: https://docs.vllm.ai/en/latest/api/vllm/distributed/ec_transfer/ec_connector/cpu/worker/
lastmod: 2026-09-24

#

`vllm.distributed.ec_transfer.ec_connector.cpu.worker`

[¶](https://docs.vllm.ai#vllm.distributed.ec_transfer.ec_connector.cpu.worker)

Worker-side of the ECCPUConnector.

Thin, stateless across steps: opens the shared mmap region and uses the per-step connector metadata (`ECCPUConnectorMetadata`

) to decide which blocks to copy in each direction.

Modules:

-
–[descriptor_buffers](https://docs.vllm.ai/descriptor_buffers/#vllm.distributed.ec_transfer.ec_connector.cpu.worker.descriptor_buffers)Reusable pool of (src_ptrs, dst_ptrs, sizes) tensor triples.


Classes:

-
–[ECCPUWorker](https://docs.vllm.ai#vllm.distributed.ec_transfer.ec_connector.cpu.worker.ECCPUWorker)Worker-side delegate for the ECCPUConnector.

-
–[Transfer](https://docs.vllm.ai#vllm.distributed.ec_transfer.ec_connector.cpu.worker.Transfer)A batched copy in flight on a dedicated GPU stream.


##

`ECCPUWorker`

[¶](https://docs.vllm.ai#vllm.distributed.ec_transfer.ec_connector.cpu.worker.ECCPUWorker)

Worker-side delegate for the ECCPUConnector.

- Producer role: copies
`encoder_cache[mm_hash]`

→`mmap[block_ids]`

for each entry in`metadata.saves`

. Descriptor buffers are filled directly in`save_caches`

; the actual DMA is issued as a single batched call in`flush_saves`

. - Consumer role: copies
`mmap[block_ids]`

→`encoder_cache[mm_hash]`

for all entries in`metadata.loads`

via a single`swap_blocks_batch`

call on a dedicated stream. - On
`ec_both`

nodes both paths run back-to-back in a single step.

Every batched copy runs on a stream drawn from a pool so it overlaps the compute stream, bracketed by a start/end event pair. The stream, events, and descriptor buffers are recycled once the end event fires.

Both paths move memory between the two streams, so each buffer is registered against the stream that is not its own: save sources against the save stream, load destinations against the compute stream. Without that, the caching allocator would be free to reissue memory a copy or a queued read still needs, since it only tracks the stream a buffer was allocated on.

Methods:

-
–[build_connector_worker_meta](https://docs.vllm.ai#vllm.distributed.ec_transfer.ec_connector.cpu.worker.ECCPUWorker.build_connector_worker_meta)Report the GPU copies that completed on this rank this step: saved

-
–[flush_saves](https://docs.vllm.ai#vllm.distributed.ec_transfer.ec_connector.cpu.worker.ECCPUWorker.flush_saves)Flush all accumulated saves in a single swap_blocks_batch call.

-
–[save_caches](https://docs.vllm.ai#vllm.distributed.ec_transfer.ec_connector.cpu.worker.ECCPUWorker.save_caches)Fill descriptor buffers directly for batched flush.

-
–[start_load_caches](https://docs.vllm.ai#vllm.distributed.ec_transfer.ec_connector.cpu.worker.ECCPUWorker.start_load_caches)Consumer path: single batched copy of all loads from mmap→GPU.


## Source code in `vllm/distributed/ec_transfer/ec_connector/cpu/worker/__init__.py`


|
|

###

`_collect_finished(inflight, direction)`

[¶](https://docs.vllm.ai#vllm.distributed.ec_transfer.ec_connector.cpu.worker.ECCPUWorker._collect_finished)

Pop transfers whose end event has fired, recycle their stream, events, and buffers, and return their completions.

The front check is conservative: a transfer is reported only once its own end event fires, so completions are always genuinely done, and each is reported exactly once because the transfer is popped as it is reported. A later transfer that happens to finish first simply waits behind the front and is reported on a subsequent poll.

## Source code in `vllm/distributed/ec_transfer/ec_connector/cpu/worker/__init__.py`


###

`_pin_shared_region()`

[¶](https://docs.vllm.ai#vllm.distributed.ec_transfer.ec_connector.cpu.worker.ECCPUWorker._pin_shared_region)

###

`_shutdown_transfer_backend()`

[¶](https://docs.vllm.ai#vllm.distributed.ec_transfer.ec_connector.cpu.worker.ECCPUWorker._shutdown_transfer_backend)

###

`_submit_transfer(bufs, count, direction)`

[¶](https://docs.vllm.ai#vllm.distributed.ec_transfer.ec_connector.cpu.worker.ECCPUWorker._submit_transfer)

Submit a transfer on the current backend stream.

## Source code in `vllm/distributed/ec_transfer/ec_connector/cpu/worker/__init__.py`


###

`build_connector_worker_meta()`

[¶](https://docs.vllm.ai#vllm.distributed.ec_transfer.ec_connector.cpu.worker.ECCPUWorker.build_connector_worker_meta)

Report the GPU copies that completed on this rank this step: saved mm_hashes and loaded transfer ids.

Returns None when nothing finished, so the scheduler sees no payload.

## Source code in `vllm/distributed/ec_transfer/ec_connector/cpu/worker/__init__.py`


###

`flush_saves()`

[¶](https://docs.vllm.ai#vllm.distributed.ec_transfer.ec_connector.cpu.worker.ECCPUWorker.flush_saves)

Flush all accumulated saves in a single swap_blocks_batch call.

Runs the copy on the stream the batch acquired when it opened, gated behind the compute stream that produced the encoder outputs, brackets it with start/end events, and enqueues the batch as in-flight. The stream, events, and descriptor buffers are recycled once the end event fires (see `_collect_finished`

), which is also when the saved mm_hashes become safe to mark ready.

## Source code in `vllm/distributed/ec_transfer/ec_connector/cpu/worker/__init__.py`


###

`save_caches(encoder_cache, mm_hash, connector_metadata)`

[¶](https://docs.vllm.ai#vllm.distributed.ec_transfer.ec_connector.cpu.worker.ECCPUWorker.save_caches)

Fill descriptor buffers directly for batched flush.

Registers `encoder_cache[mm_hash]`

against the stream the copy will run on, so the caching allocator will not hand that memory to another allocation before the copy has read it. The descriptor buffers hold raw addresses, and the caller is free to evict the entry as soon as this step's saves are dispatched.

## Source code in `vllm/distributed/ec_transfer/ec_connector/cpu/worker/__init__.py`


###

`start_load_caches(encoder_cache, connector_metadata)`

[¶](https://docs.vllm.ai#vllm.distributed.ec_transfer.ec_connector.cpu.worker.ECCPUWorker.start_load_caches)

Consumer path: single batched copy of all loads from mmap→GPU.

The destination is registered against the compute stream that consumes it, so the caching allocator will not hand that memory to a later load while reads of it are still queued there.

## Source code in `vllm/distributed/ec_transfer/ec_connector/cpu/worker/__init__.py`


|
|

##

`Transfer`

`dataclass`

[¶](https://docs.vllm.ai#vllm.distributed.ec_transfer.ec_connector.cpu.worker.Transfer)

A batched copy in flight on a dedicated GPU stream.

Its descriptor buffers and stream are held until `end_event`

fires; only then are the buffers and stream safe to recycle and the `completions`

safe to report. `start_event`

/`end_event`

bracket the copy so its elapsed time can be measured on completion.

`completions`

is what the scheduler is told about this copy: mm_hashes for saves, transfer ids for loads.

## Source code in `vllm/distributed/ec_transfer/ec_connector/cpu/worker/__init__.py`


##

`_coalesce_runs(block_ids)`

[¶](https://docs.vllm.ai#vllm.distributed.ec_transfer.ec_connector.cpu.worker._coalesce_runs)

Split block ids into runs that are consecutive in the region.

Returns `(slots, first_blocks, num_blocks)`

, one element per run, where `slots`

is the run's offset in the flat block sequence. Per-descriptor overhead dominates these copies, so describing a run with one descriptor rather than one per block is worth an order of magnitude.

Both callers derive the non-region side of a run from its slot, so that side advances in lockstep with the region and only the region has to be split. `EmbeddingCache`

hands out ascending ids, which is what makes runs findable at all.