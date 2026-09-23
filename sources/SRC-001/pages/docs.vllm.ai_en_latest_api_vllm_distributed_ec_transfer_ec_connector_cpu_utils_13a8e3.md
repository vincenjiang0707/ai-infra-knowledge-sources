source: https://docs.vllm.ai/en/latest/api/vllm/distributed/ec_transfer/ec_connector/cpu/utils/
lastmod: 2026-09-23

#

`vllm.distributed.ec_transfer.ec_connector.cpu.utils`

[¶](https://docs.vllm.ai#vllm.distributed.ec_transfer.ec_connector.cpu.utils)

Supporting utilities for the ECCPUConnector scheduler.

Functions:

-
–[build_block_descs](https://docs.vllm.ai#vllm.distributed.ec_transfer.ec_connector.cpu.utils.build_block_descs)Per-block

`(addr, size, device_id)`

tuples for an`ECSharedRegion`

.

##

`build_block_descs(base_ptr, num_blocks, block_size_bytes, device_id=0)`

[¶](https://docs.vllm.ai#vllm.distributed.ec_transfer.ec_connector.cpu.utils.build_block_descs)

Per-block `(addr, size, device_id)`

tuples for an `ECSharedRegion`

.

Handed to `nixl.get_xfer_descs`

to build a dlist where descriptor `i`

addresses block `i`

in the mmap. This makes a WRITE to block indices `[i1, i2, ...]`

a simple `make_prepped_xfer(..., [i1, i2])`

on both ends — no per-request address math.