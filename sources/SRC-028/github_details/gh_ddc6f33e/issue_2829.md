# [Issue #2829] checkpoint_storage_concurrent_gb flag is only respected when load_parameters_path is passed

source: https://github.com/AI-Hypercomputer/maxtext/issues/2829
state: closed | updated: 2026-04-20T17:53:27Z
labels: bug

## 正文

### Bug report

I set checkpoint_storage_concurrent_gb to 900.

When I run with load_parameters_path set, I see the following logs:
`Created BasePyTreeCheckpointHandler: use_ocdbt=True, use_zarr3=True, pytree_metadata_options=PyTreeMetadataOptions(support_rich_types=False), array_metadata_store=<orbax.checkpoint._src.metadata.array_metadata_store.Store object at 0x7934458b4c50>, enable_pinned_host_transfer=False, save_concurrent_bytes: 900000000000 (838.2 GiB), restore_concurrent_bytes: 900000000000 (838.2 GiB)`

This is as expected. However for runs where A) load_full_state_path is set or B) neither load_full_state_path or load_parameters_path is set, I see the following logs:
`Created BasePyTreeCheckpointHandler: use_ocdbt=True, use_zarr3=False, pytree_metadata_options=PyTreeMetadataOptions(support_rich_types=False), array_metadata_store=<orbax.checkpoint._src.metadata.array_metadata_store.Store object at 0x7f107ea088f0>, enable_pinned_host_transfer=False, save_concurrent_bytes: 96000000000 (89.4 GiB), restore_concurrent_bytes: 96000000000 (89.4 GiB)`


### Logs/Output

_No response_

### Environment Information

orbax-checkpoint version: 0.11.30

### Additional Context

_No response_

## 评论 (3)

### shralex · 2025-12-15

@abhinavclemson can you please take a look

### mkmg · 2026-01-29

Hi folks, any update on this?

### xuefgu · 2026-04-20

Resolved in https://github.com/AI-Hypercomputer/maxtext/pull/3051. Marking as closed.
