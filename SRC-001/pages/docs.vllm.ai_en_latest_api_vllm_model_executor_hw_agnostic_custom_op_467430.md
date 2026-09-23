source: https://docs.vllm.ai/en/latest/api/vllm/model_executor/hw_agnostic/custom_op/
lastmod: 2026-09-23

class CustomOp(nn.Module):
"""Base class for custom ops.
Dispatches the forward method to the appropriate backend.
"""
def __new__(cls, *args, **kwargs):
try:
op_name = cls.__name__
except AttributeError:
raise TypeError(
f"Cannot instantiate '{cls.__name__}': its 'name' attribute "
f"was not set, possibly because it was not decorated with "
f"@CustomOp.register, or it's the CustomOp base class itself."
) from None
if op_name not in op_registry_oot:
op_cls_to_instantiate = cls
else:
op_cls_to_instantiate = op_registry_oot[op_name]
logger.debug(
"Instantiating custom op: %s using %s",
op_name,
str(op_cls_to_instantiate),
)
return super().__new__(op_cls_to_instantiate)
def __init__(self, *, enforce_enable: bool = False, compile_native: bool = False):
super().__init__()
self._enforce_enable = enforce_enable
self._forward_method = self.dispatch_forward(compile_native=compile_native)
def forward(self, *args, **kwargs):
return self._forward_method(*args, **kwargs)
def forward_native(self, *args, **kwargs):
"""PyTorch-native implementation; OOT plugins override via
:meth:`forward_oot`."""
raise NotImplementedError
def forward_oot(self, *args, **kwargs):
# By default, OOT ops fall back to the PyTorch-native implementation.
return self.forward_native(*args, **kwargs)
def dispatch_forward(self, compile_native: bool):
# The hw-agnostic CustomOp dispatches only between forward_native
# (in-tree, used on every platform) and forward_oot (overridden by
# an OOT plugin via register_oot).
compilation_config = get_cached_compilation_config()
# NOTE(shen-shanshan): CustomOp object can be enforce enabled, e.g.,
# enable device-specific kernels in ViT models when enabling graph
# mode. By default, it will follow the compilation_config to determine
# whether enable itself.
# This enforce_enable mechanism will be removed after we adding a
# separate compilation_config for multi-modal part.
enabled = self._enforce_enable or self.enabled()
if enabled:
compilation_config.enabled_custom_ops.update([self.__class__.name])
else:
compilation_config.disabled_custom_ops.update([self.__class__.name])
if not enabled:
# Compile forward_native to avoid eager torch ops if inside
# opaque torch custom op (e.g. fused_moe, unified_attention, etc.)
return self.maybe_compile(self.forward_native, enable=compile_native)
if current_platform.is_out_of_tree():
return self.forward_oot
return self.forward_native
def maybe_compile(self, fn, *, enable: bool = True):
"""Compile fn if compilation enabled.
Useful for CustomOp instances called from within a torch custom op,
meaning the forward call is hidden from the model-level torch.compile.
NOTE: this does not enable fusion across ops, so opaque custom ops
should still be unwrapped wherever possible.
"""
from vllm.config.compilation import CompilationMode
# Do not compile if compilation disabled
if not enable:
return fn
# Do not compile if global compilation disabled
compilation_config = get_cached_compilation_config()
if compilation_config.mode == CompilationMode.NONE:
return fn
# If eager backend is used, do not compile either
if compilation_config.backend == "eager":
return fn
compile_options = maybe_disable_graph_partition(
current_platform.simple_compile_backend
)
backend = current_platform.simple_compile_backend
dynamic_arg_dims = getattr(self.__class__, "_dynamic_arg_dims", None)
if dynamic_arg_dims is not None:
compiled_fn = torch.compile(
fn,
dynamic=False,
backend=backend,
options=compile_options,
)
sig = inspect.signature(fn)
@functools.wraps(fn)
def wrapper(*args, **kwargs):
bound = sig.bind(*args, **kwargs)
bound.apply_defaults()
for name, dims in dynamic_arg_dims.items():
arg = bound.arguments.get(name)
if arg is not None and isinstance(arg, torch.Tensor):
dims_list = [dims] if isinstance(dims, int) else dims
for d in dims_list:
real_d = arg.ndim + d if d < 0 else d
torch._dynamo.mark_dynamic(arg, real_d)
return compiled_fn(*args, **kwargs)
return wrapper
# dynamic=True to avoid recompilations
return torch.compile(
fn,
dynamic=True,
backend=backend,
options=compile_options,
)
@classmethod
def enabled(cls) -> bool:
# if no name, then it was not registered
compilation_config = get_cached_compilation_config()
custom_ops = compilation_config.custom_ops
if not hasattr(cls, "name"):
logger.warning_once(
"Custom op %s was not registered, which means it won't appear "
"in the op registry. It will be enabled/disabled based on the "
"global settings.",
cls.__name__,
)
return CustomOp.default_on()
enabled = f"+{cls.name}" in custom_ops
disabled = f"-{cls.name}" in custom_ops
assert not (enabled and disabled), f"Cannot enable and disable {cls.name}"
return (CustomOp.default_on() or enabled) and not disabled
@staticmethod
def default_on() -> bool:
"""Behavior controlled by `CompilationConfig.custom_ops`: On by default if
'all', off by default if 'none'.
When PyTorch Inductor is used, 'none' is the default value,
otherwise 'all'.
"""
compilation_config = get_cached_compilation_config()
count_none = compilation_config.custom_ops.count("none")
count_all = compilation_config.custom_ops.count("all")
assert count_none + count_all == 1
return not count_none > 0 or count_all > 0
# Decorator to register custom ops.
@classmethod
def register(
cls,
name: str,
dynamic_arg_dims: dict[str, int | list[int]] | None = None,
):
def decorator(op_cls):
assert name not in op_registry, f"Duplicate op name: {name}"
op_cls.name = name
op_cls._dynamic_arg_dims = dynamic_arg_dims
op_registry[name] = op_cls
return op_cls
return decorator
# Decorator to register out-of-tree(oot) custom ops.
# For OOT custom ops:
# if in-tree layer class is registered with an oot_custom_op layer,
# the oot_custom_op layer will be used instead.
# Example:
# - @UnquantizedFusedMoEMethod.register_oot
# class HPUUnquantizedFusedMoEMethod(UnquantizedFusedMoEMethod)
# or
# - @CustomOP.register_oot(name="UnquantizedFusedMoEMethod")
@classmethod
def register_oot(cls, _decorated_op_cls=None, name: str | None = None):
def decorator(op_cls):
reg_name = name if name is not None else cls.__name__
assert reg_name not in op_registry_oot, f"Duplicate op name: {reg_name}"
op_cls.name = reg_name
op_registry_oot[reg_name] = op_cls
return op_cls
if _decorated_op_cls is None:
# Called with parentheses: @CustomOP.register_oot()
# or @CustomOP.register_oot(name="...")
# So, _decorated_op_cls is None.
# We return the actual decorator function.
return decorator
elif isinstance(_decorated_op_cls, type): # Check if it's a class
# Called without parentheses: @CustomOP.register_oot
# The first argument is the class itself.
# We call the 'decorator' function immediately with the class.
return decorator(_decorated_op_cls)
else:
# Handle other unexpected cases if necessary
raise TypeError("Decorator can only be applied to classes.")