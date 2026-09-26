source: https://docs.vllm.ai/en/latest/api/vllm/model_executor/model_loader/weight_cache/protocol/
lastmod: 2026-09-24

#

`vllm.model_executor.model_loader.weight_cache.protocol`

[¶](https://docs.vllm.ai#vllm.model_executor.model_loader.weight_cache.protocol)

WeightCacheKey fingerprinting and socket protocol for the weight cache daemon.

The protocol uses pickle over a Unix domain socket and is only intended for communication between trusted local processes owned by the same user. The sockets live in a per-user private directory (mode 0700) and the daemon restricts the socket file permissions to the owner (0600). Both the daemon and the engine verify that the directory and socket are owned by the current user and are not group/world accessible before trusting them, so a different local user cannot pre-plant a malicious socket at a predictable path.

Classes:

-
–[CacheConfigMismatchError](https://docs.vllm.ai#vllm.model_executor.model_loader.weight_cache.protocol.CacheConfigMismatchError)Raised when the daemon's cached weights don't match the engine.

-
–[TensorEntry](https://docs.vllm.ai#vllm.model_executor.model_loader.weight_cache.protocol.TensorEntry)A single cached tensor.

-
–[UnsupportedPlatformForIPCError](https://docs.vllm.ai#vllm.model_executor.model_loader.weight_cache.protocol.UnsupportedPlatformForIPCError)Raised when the current platform cannot share CUDA IPC handles.

-
–[UnsupportedQuantForIPCError](https://docs.vllm.ai#vllm.model_executor.model_loader.weight_cache.protocol.UnsupportedQuantForIPCError)Raised when a quantization method is not verified for IPC weight sharing.

-
–[WeightCacheKey](https://docs.vllm.ai#vllm.model_executor.model_loader.weight_cache.protocol.WeightCacheKey)Fingerprint of the cached weights.

-
–[WeightCacheState](https://docs.vllm.ai#vllm.model_executor.model_loader.weight_cache.protocol.WeightCacheState)Client-side decode of a daemon's get_state response payload.

-
–[WeightCacheUnavailableError](https://docs.vllm.ai#vllm.model_executor.model_loader.weight_cache.protocol.WeightCacheUnavailableError)Raised when no weight cache daemon is reachable or usable.


Functions:

-
–[check_ipc_platform_support](https://docs.vllm.ai#vllm.model_executor.model_loader.weight_cache.protocol.check_ipc_platform_support)Hard-error unless the current platform can share CUDA IPC handles.

-
–[check_ipc_quant_support](https://docs.vllm.ai#vllm.model_executor.model_loader.weight_cache.protocol.check_ipc_quant_support)Hard-error unless every quant method supports pre-processed weights.

-
–[ensure_private_socket_dir](https://docs.vllm.ai#vllm.model_executor.model_loader.weight_cache.protocol.ensure_private_socket_dir)Create the socket directory (if needed) locked down to the owner.

-
–[get_current_device_uuid](https://docs.vllm.ai#vllm.model_executor.model_loader.weight_cache.protocol.get_current_device_uuid)UUID of the physical GPU backing the current accelerator device.

-
–[get_socket_dir](https://docs.vllm.ai#vllm.model_executor.model_loader.weight_cache.protocol.get_socket_dir)Return the directory that holds the daemon sockets.

-
–[get_socket_path](https://docs.vllm.ai#vllm.model_executor.model_loader.weight_cache.protocol.get_socket_path)Socket path of a daemon group;

`is_draft=False`

is the target. -
–[hash_checkpoint](https://docs.vllm.ai#vllm.model_executor.model_loader.weight_cache.protocol.hash_checkpoint)Fingerprint checkpoint content from local safetensors metadata.

-
–[verify_peer_is_owner](https://docs.vllm.ai#vllm.model_executor.model_loader.weight_cache.protocol.verify_peer_is_owner)Best-effort check that the connecting peer runs as the current user.

-
–[verify_private_dir](https://docs.vllm.ai#vllm.model_executor.model_loader.weight_cache.protocol.verify_private_dir)Verify a directory is a real dir owned by us and not world/group readable.

-
–[verify_socket_owner](https://docs.vllm.ai#vllm.model_executor.model_loader.weight_cache.protocol.verify_socket_owner)Verify the socket lives in a private dir and is owned by the current user.


##

`CacheConfigMismatchError`

[¶](https://docs.vllm.ai#vllm.model_executor.model_loader.weight_cache.protocol.CacheConfigMismatchError)

##

`TensorEntry`

`dataclass`

[¶](https://docs.vllm.ai#vllm.model_executor.model_loader.weight_cache.protocol.TensorEntry)

A single cached tensor.

CUDA tensors are exported as `torch.multiprocessing`

reduction args (CUDA IPC handles); non-CUDA tensors are shipped by value.

Attributes:

## Source code in `vllm/model_executor/model_loader/weight_cache/protocol.py`


###

`kind`

`instance-attribute`

[¶](https://docs.vllm.ai#vllm.model_executor.model_loader.weight_cache.protocol.TensorEntry.kind)

Either "param" or "buffer".

##

`UnsupportedPlatformForIPCError`

[¶](https://docs.vllm.ai#vllm.model_executor.model_loader.weight_cache.protocol.UnsupportedPlatformForIPCError)

##

`UnsupportedQuantForIPCError`

[¶](https://docs.vllm.ai#vllm.model_executor.model_loader.weight_cache.protocol.UnsupportedQuantForIPCError)

##

`WeightCacheKey`

`dataclass`

[¶](https://docs.vllm.ai#vllm.model_executor.model_loader.weight_cache.protocol.WeightCacheKey)

Fingerprint of the cached weights.

Any mismatch between the daemon's and the engine's fingerprint means the cached weights cannot be reused and the engine must load from disk.

Methods:

-
–[from_model_config](https://docs.vllm.ai#vllm.model_executor.model_loader.weight_cache.protocol.WeightCacheKey.from_model_config)Build the fingerprint for a model configuration.


Attributes:

## Source code in `vllm/model_executor/model_loader/weight_cache/protocol.py`


###

`is_draft = False`

`class-attribute`

`instance-attribute`

[¶](https://docs.vllm.ai#vllm.model_executor.model_loader.weight_cache.protocol.WeightCacheKey.is_draft)

Daemon group the weights come from; False is the target model.

###

`from_model_config(model_config, tp_size, tp_rank, *, is_draft=False, dp_size=1, dp_rank=0)`

`classmethod`

[¶](https://docs.vllm.ai#vllm.model_executor.model_loader.weight_cache.protocol.WeightCacheKey.from_model_config)

Build the fingerprint for a model configuration.

Must be called before weight loading: process_weights_after_loading may mutate hf_config.quantization_config, which would change the hash between the daemon and the engine.

The checkpoint is identified by a hash of its safetensors metadata when the weights are available locally, so a daemon and engine referencing identical weights in different directories still match; otherwise it falls back to the model path.

## Source code in `vllm/model_executor/model_loader/weight_cache/protocol.py`


##

`WeightCacheState`

[¶](https://docs.vllm.ai#vllm.model_executor.model_loader.weight_cache.protocol.WeightCacheState)

Bases: [NamedTuple](https://docs.python.org/3/library/typing.html#typing.NamedTuple)

Client-side decode of a daemon's get_state response payload.

Attributes:

-
([aliases](https://docs.vllm.ai#vllm.model_executor.model_loader.weight_cache.protocol.WeightCacheState.aliases)

) –[dict](https://docs.python.org/3/builtins/stdtypes.html#dict)[[str](https://docs.python.org/3/builtins/stdtypes.html#str),[str](https://docs.python.org/3/builtins/stdtypes.html#str)]Duplicate (tied) weight names aliased to their canonical entry.

-
([attrs](https://docs.vllm.ai#vllm.model_executor.model_loader.weight_cache.protocol.WeightCacheState.attrs)

) –[dict](https://docs.python.org/3/builtins/stdtypes.html#dict)[[str](https://docs.python.org/3/builtins/stdtypes.html#str),[bool](https://docs.python.org/3/builtins/functions.html#bool)]Python-side flags set by load_weights, e.g. EAGLE ownership flags.

-
([entries](https://docs.vllm.ai#vllm.model_executor.model_loader.weight_cache.protocol.WeightCacheState.entries)

) –[dict](https://docs.python.org/3/builtins/stdtypes.html#dict)[[str](https://docs.python.org/3/builtins/stdtypes.html#str),[TensorEntry](https://docs.vllm.ai#vllm.model_executor.model_loader.weight_cache.protocol.TensorEntry)]Model tensors, exported as CUDA IPC handles or shipped by value.


## Source code in `vllm/model_executor/model_loader/weight_cache/protocol.py`


##

`WeightCacheUnavailableError`

[¶](https://docs.vllm.ai#vllm.model_executor.model_loader.weight_cache.protocol.WeightCacheUnavailableError)

##

`_safetensors_header(path)`

[¶](https://docs.vllm.ai#vllm.model_executor.model_loader.weight_cache.protocol._safetensors_header)

Return the raw safetensors header (length prefix + JSON) of a file.

The header carries tensor names, dtypes, shapes and byte offsets, so it is a content fingerprint of the shard without reading any weight bytes.

## Source code in `vllm/model_executor/model_loader/weight_cache/protocol.py`


##

`check_ipc_platform_support()`

[¶](https://docs.vllm.ai#vllm.model_executor.model_loader.weight_cache.protocol.check_ipc_platform_support)

Hard-error unless the current platform can share CUDA IPC handles.

Only CUDA/ROCm tensors get a real IPC handle from `TensorEntry`

; other platforms (e.g. XPU) would silently ship every tensor by value instead.

Raises:

-

–[UnsupportedPlatformForIPCError](https://docs.vllm.ai#vllm.model_executor.model_loader.weight_cache.protocol.UnsupportedPlatformForIPCError)If the current platform is not CUDA/ROCm.


## Source code in `vllm/model_executor/model_loader/weight_cache/protocol.py`


##

`check_ipc_quant_support(model)`

[¶](https://docs.vllm.ai#vllm.model_executor.model_loader.weight_cache.protocol.check_ipc_quant_support)

Hard-error unless every quant method supports pre-processed weights.

Parameters:

Raises:

-

–[UnsupportedQuantForIPCError](https://docs.vllm.ai#vllm.model_executor.model_loader.weight_cache.protocol.UnsupportedQuantForIPCError)If any quant method does not declare

`supports_pre_processed_weights`

.

## Source code in `vllm/model_executor/model_loader/weight_cache/protocol.py`


##

`ensure_private_socket_dir(directory, strict_perms=True)`

[¶](https://docs.vllm.ai#vllm.model_executor.model_loader.weight_cache.protocol.ensure_private_socket_dir)

Create the socket directory (if needed) locked down to the owner.

Called by the daemon before binding. Existing directories are re-checked and, for the auto-derived path, tightened so a pre-existing world-writable directory is rejected.

## Source code in `vllm/model_executor/model_loader/weight_cache/protocol.py`


##

`get_current_device_uuid()`

[¶](https://docs.vllm.ai#vllm.model_executor.model_loader.weight_cache.protocol.get_current_device_uuid)

UUID of the physical GPU backing the current accelerator device.

##

`get_socket_dir(socket_dir=None)`

[¶](https://docs.vllm.ai#vllm.model_executor.model_loader.weight_cache.protocol.get_socket_dir)

Return the directory that holds the daemon sockets.

When no explicit directory is given, use a per-user private directory under the system temp dir so its path is unpredictable to other users and can be locked down to mode 0700.

## Source code in `vllm/model_executor/model_loader/weight_cache/protocol.py`


##

`get_socket_path(gpu_uuid, socket_dir=None, *, is_draft=False)`

[¶](https://docs.vllm.ai#vllm.model_executor.model_loader.weight_cache.protocol.get_socket_path)

Socket path of a daemon group; `is_draft=False`

is the target.

The GPU uuid is hashed to keep the name well under the AF_UNIX path limit (~108 bytes) even with the draft role suffix.

## Source code in `vllm/model_executor/model_loader/weight_cache/protocol.py`


##

`hash_checkpoint(model)`

[¶](https://docs.vllm.ai#vllm.model_executor.model_loader.weight_cache.protocol.hash_checkpoint)

Fingerprint checkpoint content from local safetensors metadata.

Hashes each shard's safetensors header so a daemon and an engine pointing at identical weights in different directories produce the same key. Returns None when local safetensors files can't be located (e.g. an undownloaded Hugging Face repo id), leaving the caller to fall back to the model path.

## Source code in `vllm/model_executor/model_loader/weight_cache/protocol.py`


##

`verify_peer_is_owner(conn)`

[¶](https://docs.vllm.ai#vllm.model_executor.model_loader.weight_cache.protocol.verify_peer_is_owner)

Best-effort check that the connecting peer runs as the current user.

Uses SO_PEERCRED where available (Linux). Silently returns on platforms that do not expose peer credentials.

## Source code in `vllm/model_executor/model_loader/weight_cache/protocol.py`


##

`verify_private_dir(directory, strict_perms=True)`

[¶](https://docs.vllm.ai#vllm.model_executor.model_loader.weight_cache.protocol.verify_private_dir)

Verify a directory is a real dir owned by us and not world/group readable.

When `strict_perms`

is False the group/world permission bits are not checked; this is used for directories the operator explicitly configured (they own the trust decision), while the auto-derived per-user directory is always checked strictly.

## Source code in `vllm/model_executor/model_loader/weight_cache/protocol.py`


##

`verify_socket_owner(socket_path, strict_perms=True)`

[¶](https://docs.vllm.ai#vllm.model_executor.model_loader.weight_cache.protocol.verify_socket_owner)

Verify the socket lives in a private dir and is owned by the current user.

Called by the engine before connecting so it never talks to a socket a different user could have planted.