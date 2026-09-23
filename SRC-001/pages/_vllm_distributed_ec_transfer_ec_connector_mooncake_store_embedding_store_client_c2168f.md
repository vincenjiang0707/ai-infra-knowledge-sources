source: https://docs.vllm.ai/en/latest/api/vllm/distributed/ec_transfer/ec_connector/mooncake_store_embedding/store_client/
lastmod: 2026-09-23

class MooncakeEmbeddingStoreClient:
"""Wraps Mooncake object and buffer APIs used by embedding transfer."""
def __init__(
self,
store: Any,
replicate_config: Any | None = None,
*,
read_buffer_bytes: int = 128 * 1024**2,
):
self._lifetime_lock = threading.Lock()
self._unsafe_owners: list[Any] = []
self._poisoned = False
self.store = store
self.replicate_config = replicate_config
self._read_buffer_bytes = read_buffer_bytes
self._read_buffer: torch.Tensor | None = None
self._put_header: ctypes.Array[ctypes.c_char] | None = None
def _check_healthy(self) -> None:
if self._poisoned:
raise EmbeddingStoreError(
"Mooncake I/O completion is unconfirmed; worker must exit"
)
def _poison(self, owners: list[Any]) -> None:
with self._lifetime_lock:
self._unsafe_owners.extend(owners)
if not self._poisoned:
self._poisoned = True
_UNSAFE_CLIENTS.append(self)
@contextmanager
def _registered_io(
self,
buffers: list[tuple[Any, int, int]],
) -> Iterator[Callable[[int], None]]:
self._check_healthy()
registered = []
submitted = False
confirmed = False
def confirm(result: int) -> None:
nonlocal confirmed
if type(result) is not int or (
result < 0 and result not in _SAFE_PUT_REJECTIONS
):
raise EmbeddingStoreError(
"Mooncake I/O completion is unconfirmed; retaining buffers"
)
confirmed = True
try:
for owner, addr, size in buffers:
ret = self.store.register_buffer(addr, size)
if ret != 0:
raise EmbeddingStoreOperationError(
f"Failed to register embedding buffer: {ret}"
)
registered.append(addr)
submitted = True
yield confirm
except BaseException as error:
if submitted and not confirmed:
self._poison([owner for owner, _, _ in buffers])
raise EmbeddingStoreError(
"Mooncake I/O completion is unconfirmed; retaining buffers"
) from error
raise
finally:
if not submitted or confirmed:
try:
for addr in reversed(registered):
self._unregister_buffer(addr)
except BaseException:
self._poison([owner for owner, _, _ in buffers])
raise
def close(self) -> None:
"""Close the supported Mooncake binding after all I/O is drained."""
self._check_healthy()
if self._read_buffer is not None:
try:
self._unregister_buffer(self._read_buffer.data_ptr())
except BaseException:
self._poison([self._read_buffer])
raise
self._read_buffer = None
if self._put_header is not None:
try:
self._unregister_buffer(ctypes.addressof(self._put_header))
except BaseException:
self._poison([self._put_header])
raise
self._put_header = None
ret = self.store.close()
if ret != 0:
raise EmbeddingStoreError(
f"failed to close embedding Mooncake Store: {ret}"
)
def exists(self, pool_key: str) -> bool:
return self.batch_exists([pool_key])[0]
def batch_exists(self, keys: list[str]) -> list[bool]:
self._check_healthy()
if not keys:
return []
states = self.store.batch_is_exist(keys)
if len(states) != len(keys):
raise RuntimeError(
"Mooncake Store returned an unexpected number of lookup results"
)
return [state == 1 for state in states]
def load_tensors(
self, expected: Mapping[str, TensorSpec], device: torch.device | str
) -> dict[str, torch.Tensor]:
"""Synchronously load runner inputs into independently owned tensors."""
self._check_healthy()
device = torch.device(device)
loaded: dict[str, torch.Tensor] = {}
chunk: dict[str, TensorSpec] = {}
chunk_bytes = 0
for key, spec in expected.items():
size = _MOONCAKE_TENSOR_HEADER.size + spec.nbytes
if size > self._read_buffer_bytes:
logger.warning(
"Skipping Store GET for %s: object bytes=%d exceed read buffer=%d",
key,
size,
self._read_buffer_bytes,
)
continue
if chunk_bytes + size > self._read_buffer_bytes:
loaded.update(self._load_chunk(chunk, device))
chunk = {}
chunk_bytes = 0
chunk[key] = spec
chunk_bytes += size
if chunk:
loaded.update(self._load_chunk(chunk, device))
return loaded
def _load_chunk(
self, expected: dict[str, TensorSpec], device: torch.device
) -> dict[str, torch.Tensor]:
self._check_healthy()
if self._read_buffer is None:
buffer = torch.empty(
self._read_buffer_bytes,
dtype=torch.uint8,
device="cpu",
pin_memory=device.type == "cuda",
)
ret = self.store.register_buffer(buffer.data_ptr(), buffer.nbytes)
if ret != 0:
raise EmbeddingStoreOperationError(
f"Failed to register embedding read buffer: {ret}"
)
self._read_buffer = buffer
buffer = self._read_buffer
base = buffer.data_ptr()
sizes = [
_MOONCAKE_TENSOR_HEADER.size + spec.nbytes for spec in expected.values()
]
offsets: list[int] = []
end = 0
for size in sizes:
offsets.append(end)
end += size
try:
results = self.store.batch_get_into(
list(expected), [base + offset for offset in offsets], sizes
)
if not _batch_get_completed_safely(results, sizes):
raise EmbeddingStoreError("Unsafe batch GET results")
except BaseException as error:
self._poison([buffer])
raise EmbeddingStoreError(
"Mooncake I/O completion is unconfirmed; retaining read buffer"
) from error
valid: list[tuple[str, TensorSpec, int]] = []
for (key, spec), offset, size, result in zip(
expected.items(), offsets, sizes, results, strict=True
):
if result != size:
logger.warning(
"Store GET skipped for %s: result=%d, expected bytes=%d",
key,
result,
size,
)
continue
try:
_validate_mooncake_tensor_metadata(
key,
ctypes.string_at(base + offset, _MOONCAKE_TENSOR_HEADER.size),
spec,
)
except EmbeddingStoreOperationError as error:
logger.warning("Store GET skipped for %s: %s", key, error)
continue
valid.append((key, spec, offset + _MOONCAKE_TENSOR_HEADER.size))
if not valid:
return {}
# Allocate every destination before submitting any asynchronous copy.
targets = {
key: torch.empty(
spec.shape,
dtype=getattr(torch, spec.dtype.removeprefix("torch.")),
device=device,
)
for key, spec, _ in valid
}
ready = torch.Event() if device.type == "cuda" else None
try:
for key, spec, offset in valid:
targets[key].view(torch.uint8).view(-1).copy_(
buffer[offset : offset + spec.nbytes],
non_blocking=ready is not None,
)
if ready is not None:
ready.record(torch.accelerator.current_stream(device))
ready.synchronize()
except BaseException as error:
if ready is not None:
self._poison([buffer, *targets.values(), ready])
raise EmbeddingStoreError(
"Embedding copy completion is unconfirmed; retaining buffers"
) from error
raise
return targets
def put_tensor(self, pool_key: str, tensor: torch.Tensor) -> None:
self._check_healthy()
if not tensor.is_contiguous():
raise EmbeddingStoreOperationError("embedding tensor must be contiguous")
metadata = _encode_mooncake_tensor_metadata(tensor)
# The single publisher reuses this header only after PUT completion.
if self._put_header is None:
header = ctypes.create_string_buffer(len(metadata))
ret = self.store.register_buffer(ctypes.addressof(header), len(metadata))
if ret != 0:
raise EmbeddingStoreOperationError(
f"Failed to register embedding header: {ret}"
)
self._put_header = header
header_ptr = ctypes.addressof(self._put_header)
ctypes.memmove(header_ptr, metadata, len(metadata))
data_size = tensor.numel() * tensor.element_size()
buffers = [
(tensor, tensor.data_ptr(), data_size),
]
with self._registered_io(buffers) as confirm:
[result] = self.store.batch_put_from_multi_buffers(
[pool_key],
[[header_ptr, tensor.data_ptr()]],
[[len(metadata), data_size]],
self.replicate_config,
)
confirm(result)
if result < 0:
raise EmbeddingStoreOperationError(
f"failed to put embedding tensor for {pool_key}"
)
def _unregister_buffer(self, addr: int) -> None:
try:
ret = self.store.unregister_buffer(addr)
except Exception as error:
raise EmbeddingStoreError(
f"could not confirm buffer unregistration addr={addr:#x}"
) from error
if ret != 0:
raise EmbeddingStoreError(
f"failed to unregister embedding buffer addr={addr:#x}: {ret}"
)