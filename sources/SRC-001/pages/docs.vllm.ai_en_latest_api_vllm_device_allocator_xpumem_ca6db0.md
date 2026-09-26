source: https://docs.vllm.ai/en/latest/api/vllm/device_allocator/xpumem/
lastmod: 2026-09-24

class XpuMemAllocator:
"""A singleton pluggable allocator helper for XPU.
Note:
Sleep will offload selected payloads to CPU or discard and unmap XPU
physical memory. Wake-up remaps physical memory back to the same
reserved virtual address and restores payload.
"""
instance: "XpuMemAllocator | None" = None
default_tag: str = "default"
@staticmethod
def get_instance() -> "XpuMemAllocator":
assert xpumem_available, "xpumem allocator is not available"
if XpuMemAllocator.instance is None:
XpuMemAllocator.instance = XpuMemAllocator()
# Ensure MemPool/allocator wrappers are released before interpreter
# finalization tears down XPU runtime internals.
atexit.register(XpuMemAllocator._shutdown_singleton)
return XpuMemAllocator.instance
@staticmethod
def _shutdown_singleton() -> None:
instance = XpuMemAllocator.instance
if instance is None:
return
try:
instance.release_pools()
except Exception:
logger.exception("XpuMemAllocator singleton shutdown failed")
def __init__(self):
self.pointer_to_data: dict[int, AllocationData] = {}
self.current_tag: str = XpuMemAllocator.default_tag
self.allocator_and_pools: dict[str, Any] = {}
self.python_malloc_callback = self._python_malloc_callback
self.python_free_callback = self._python_free_callback
def _python_malloc_callback(self, allocation_handle: HandleType) -> None:
ptr = allocation_handle[2]
self.pointer_to_data[ptr] = AllocationData(allocation_handle, self.current_tag)
logger.debug(
"Allocated %s bytes for %s at %s",
allocation_handle[1],
self.current_tag,
ptr,
)
def _python_free_callback(self, ptr: int) -> HandleType:
data = self.pointer_to_data.pop(ptr)
data.cpu_backup_tensor = None
logger.debug("Freed %s bytes for %s at %s", data.handle[1], data.tag, ptr)
return data.handle
def sleep(self, offload_tags: tuple[str, ...] | str | None = None) -> None:
if offload_tags is None:
offload_tags = (XpuMemAllocator.default_tag,)
elif isinstance(offload_tags, str):
offload_tags = (offload_tags,)
assert isinstance(offload_tags, tuple)
total_bytes = 0
backup_bytes = 0
has_policy_conflict = False
for ptr, data in self.pointer_to_data.items():
if data.is_asleep:
requests_offload = data.tag in offload_tags
was_offloaded = data.cpu_backup_tensor is not None
if requests_offload != was_offloaded:
has_policy_conflict = True
continue
size_in_bytes = data.handle[1]
total_bytes += size_in_bytes
if data.tag not in offload_tags:
unmap_and_release(data.handle)
data.is_asleep = True
continue
backup_bytes += size_in_bytes
device, _, _, _ = data.handle
cpu_backup_tensor = torch.empty(
size_in_bytes,
dtype=torch.uint8,
device="cpu",
pin_memory=PIN_MEMORY,
)
cpu_ptr = cpu_backup_tensor.data_ptr()
_xpu_memcpy_sync(
cpu_ptr,
ptr,
size_in_bytes,
MEMCPY_DEVICE_TO_HOST,
device,
)
data.cpu_backup_tensor = cpu_backup_tensor
unmap_and_release(data.handle)
data.is_asleep = True
logger.info(
"XpuMemAllocator: sleep freed %.2f GiB memory in total, of which "
"%.2f GiB is backed up in CPU and the rest %.2f GiB is discarded "
"directly.",
total_bytes / 1024**3,
backup_bytes / 1024**3,
(total_bytes - backup_bytes) / 1024**3,
)
if has_policy_conflict:
logger.warning(
"XpuMemAllocator: sleep cannot change the policy of "
"already-asleep allocations; the existing policy was kept."
)
gc.collect()
xpu_empty_cache = getattr(torch.xpu, "empty_cache", None)
if callable(xpu_empty_cache):
xpu_empty_cache()
def discard(self, tags: tuple[str, ...] | str) -> None:
"""Discard mapped allocations with the given tags without CPU backup."""
if isinstance(tags, str):
tags = (tags,)
discarded_bytes = 0
has_policy_conflict = False
for data in self.pointer_to_data.values():
if data.tag not in tags:
continue
if data.is_asleep:
if data.cpu_backup_tensor is not None:
has_policy_conflict = True
continue
torch.accelerator.synchronize(data.handle[0])
unmap_and_release(data.handle)
data.is_asleep = True
discarded_bytes += data.handle[1]
logger.info(
"XpuMemAllocator: discarded %.2f GiB for tags %s.",
discarded_bytes / 1024**3,
tags,
)
if has_policy_conflict:
logger.warning(
"XpuMemAllocator: discard cannot change the policy of "
"already-asleep allocations; the existing policy was kept."
)
def wake_up(self, tags: list[str] | None = None) -> None:
for ptr, data in self.pointer_to_data.items():
if not data.is_asleep:
continue
if tags is not None and data.tag not in tags:
continue
create_and_allocate(data.handle)
data.is_asleep = False
cpu_backup_tensor = data.cpu_backup_tensor
if cpu_backup_tensor is None:
continue
device, size_in_bytes, _, _ = data.handle
_xpu_memcpy_sync(
ptr,
cpu_backup_tensor.data_ptr(),
size_in_bytes,
MEMCPY_HOST_TO_DEVICE,
device,
)
data.cpu_backup_tensor = None
def release_pools(self) -> None:
"""Drop Python references to MemPool/pluggable allocators eagerly.
This prevents pool destruction from being deferred to interpreter
finalization, which can happen after parts of XPU runtime are already
torn down.
"""
if not self.allocator_and_pools:
return
# Note: keep allocators alive while MemPool objects are destroyed.
# MemPool teardown may invoke allocator virtual methods (e.g. raw_delete)
# when releasing cached blocks. If allocator wrappers are dropped first,
# C++ can hit "pure virtual method called" during shutdown.
pool_entries = list(self.allocator_and_pools.values())
self.allocator_and_pools.clear()
mem_pools = [entry[0] for entry in pool_entries]
allocators = [entry[1] for entry in pool_entries]
pool_entries.clear()
xpu_sync = getattr(torch.xpu, "synchronize", None)
if callable(xpu_sync):
try:
xpu_sync()
except Exception:
logger.debug("torch.xpu.synchronize() failed during release_pools")
# Phase 1: drop MemPool refs while allocators are still strongly held.
mem_pools.clear()
gc.collect()
# Phase 2: now it is safe to release allocator wrappers.
allocators.clear()
@contextmanager
def use_memory_pool(self, tag: str | None = None):
if tag is None:
tag = XpuMemAllocator.default_tag
old_tag = self.current_tag
self.current_tag = tag
try:
with use_memory_pool_with_allocator(
self.python_malloc_callback,
self.python_free_callback,
) as data:
self.allocator_and_pools[tag] = data
yield
finally:
self.current_tag = old_tag
def get_current_usage(self) -> int:
total = 0
for data in self.pointer_to_data.values():
total += data.handle[1]
return total