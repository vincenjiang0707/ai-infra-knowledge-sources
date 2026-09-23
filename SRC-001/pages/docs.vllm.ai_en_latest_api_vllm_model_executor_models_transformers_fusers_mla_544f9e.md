source: https://docs.vllm.ai/en/latest/api/vllm/model_executor/models/transformers/fusers/mla/
lastmod: 2026-09-23

@dataclass
class MLAFuser(StackedFuser):
"""Fuser for the MLA attention pattern."""
q_proj_name: str | None
q_a_proj_name: str | None
q_a_layernorm_name: str | None
q_b_proj_name: str | None
kv_a_proj_name: str
kv_a_layernorm_name: str
kv_b_proj_name: str
o_proj_name: str | None
merged_name: ClassVar[str] = "fused_qkv_a_proj"
merged_cls_name: ClassVar[str] = "MergedColumnParallelLinear"
def info(self, name: str) -> str:
info_str = (
f"Fused: {name} ({self.source_cls}) -> MLAAttention (attention interface)"
)
if self.q_a_proj_name is not None:
info_str += "; " + super().info(name).removeprefix("Fused: ")
return info_str
@property
def shards(self) -> list[tuple[str, ShardId]]:
"""`q_a_proj` and `kv_a_proj_with_mqa` stack into one down-projection."""
if self.q_a_proj_name is None:
return []
return [(self.q_a_proj_name, 0), (self.kv_a_proj_name, 1)]
@property
def packed_modules_mapping(self) -> dict[str, list[str]]:
if self.q_a_proj_name is None:
return {}
return super().packed_modules_mapping
@classmethod
def match(cls, graph: fx.Graph, module: nn.Module) -> "MLAFuser | None":
# Find all `rms_norm(linear(placeholder))` chains.
chains = []
for node in graph.nodes:
if node.op != "call_module" or is_linear(node, module) or not node.args:
continue
source = upstream_linear(node.args[0], module)
if source is None or not _consumes_placeholder(source):
continue
if not _is_rms_norm(module.get_submodule(node.target)):
continue
chains.append((source, node))
# Tell the chains apart by width.
def is_kv_a(chain) -> bool:
source, rms_norm = chain
source_mod = module.get_submodule(source.target)
rms_norm_mod = module.get_submodule(rms_norm.target)
return source_mod.out_features != _norm_size(rms_norm_mod)
kv_a_chains = [chain for chain in chains if is_kv_a(chain)]
q_a_chains = [chain for chain in chains if not is_kv_a(chain)]
# Exactly one KV chain is MLA's signature. The query chain is optional.
if len(kv_a_chains) != 1 or len(q_a_chains) > 1:
return None
kv_a_proj, kv_a_layernorm = kv_a_chains[0]
# Linear children claimed for a role so far; the rest resolve by elimination.
claimed_linears = {kv_a_proj.target}
q_proj_name = q_a_proj = q_a_layernorm = q_b_proj = None
if q_a_chains:
# Find `q_b_proj(q_a_layernorm(q_a_proj(placeholder)))`.
q_a_proj, q_a_layernorm = q_a_chains[0]
q_b_proj = downstream_linear(q_a_layernorm, module)
if q_b_proj is None:
return None
claimed_linears |= {q_a_proj.target, q_b_proj.target}
else:
# Find `q_proj(placeholder)`.
placeholder_linears = {
node.target
for node in graph.nodes
if is_linear(node, module) and _consumes_placeholder(node)
}
if len(q_proj_candidates := placeholder_linears - claimed_linears) != 1:
return None
q_proj_name = next(iter(q_proj_candidates))
claimed_linears.add(q_proj_name)
# Find `kv_b_proj(kv_a_layernorm(...))`.
kv_b_proj = downstream_linear(kv_a_layernorm, module)
if kv_b_proj is None or kv_b_proj.target in claimed_linears:
return None
claimed_linears.add(kv_b_proj.target)
# Find `o_proj` if it is returned by the forward graph.
o_proj_name = returned_linear(graph, module)
if o_proj_name in claimed_linears:
o_proj_name = None
return cls(
source_cls=type(module).__name__,
q_proj_name=q_proj_name,
q_a_proj_name=q_a_proj.target if q_a_proj else None,
q_a_layernorm_name=q_a_layernorm.target if q_a_layernorm else None,
q_b_proj_name=q_b_proj.target if q_b_proj else None,
kv_a_proj_name=kv_a_proj.target,
kv_a_layernorm_name=kv_a_layernorm.target,
kv_b_proj_name=kv_b_proj.target,
o_proj_name=o_proj_name,
)
def validate(self, module: nn.Module, vllm_config: "VllmConfig") -> bool:
return vllm_config.model_config.use_mla
def update_forward(self, module: nn.Module) -> None:
"""Merge `q_a_proj` and `kv_a_proj` into one fused down proj then split.
Bypass the KV expansion method so the compressed latent reaches the `vllm_mla`
attention interface unexpanded."""
funcdef, fn = recover_forward(type(module))
if (q_a_proj_name := self.q_a_proj_name) is not None:
# q_a_proj is usually inside the `else` of `if self.q_lora_rank is None`.
# The fused call is inserted at the top-level statement preceding both.
names = [q_a_proj_name, self.kv_a_proj_name]
calls = self._unguarded_calls(funcdef, names)
if ast.dump(calls[0].args[0]) != ast.dump(calls[1].args[0]):
raise ValueError("down-projections read different inputs")
indices = [_top_level_index(funcdef, call) for call in calls]
self._check_input_stable(funcdef, module, calls, funcdef.body, indices)
self._splice_merged_split(funcdef, calls, funcdef.body, min(indices))
# Transformers expands the latent into full key/value in a dedicated method.
# `MLAAttention` consumes the latent directly (absorbing `kv_b_proj`),
# so replace the expansion call with its own arguments so `kv_c_normed, k_pe`
# flow to the interface in place of `key, value`.
expand_call = _single_expand_call(funcdef, module, self.kv_b_proj_name)
replace_expr(
funcdef, expand_call, ast.Tuple(elts=list(expand_call.args), ctx=ast.Load())
)
self.fused_forward = compile_forward(funcdef, fn)
def update_attrs(self, module: nn.Module, prefix: str, vllm_config: "VllmConfig"):
quant_config = vllm_config.quant_config
def replace_linear_by_name(name: str, style: Style):
linear = module.get_submodule(name)
replacement = replace_linear_class(
linear, style, quant_config, prefix=maybe_prefix(prefix, name)
)
setattr(module, name, replacement)
log_replacement(maybe_prefix(prefix, name), linear, replacement)
if (q_a_proj_name := self.q_a_proj_name) is not None:
# `match` sets the q-LoRA names together, or none of them
assert self.q_b_proj_name is not None
q_a = module.get_submodule(q_a_proj_name)
kv_a = module.get_submodule(self.kv_a_proj_name)
merged = MergedColumnParallelLinear(
input_size=q_a.in_features,
output_sizes=[q_a.out_features, kv_a.out_features],
bias=q_a.bias is not None,
quant_config=quant_config,
prefix=maybe_prefix(prefix, self.merged_name),
return_bias=False,
disable_tp=True,
)
logger.debug(
"%s: %s, %s: %s -> %s: %s",
q_a_proj_name,
q_a,
self.kv_a_proj_name,
kv_a,
self.merged_name,
merged,
)
setattr(module, self.merged_name, merged)
# The rewritten forward calls the merged projection instead.
delattr(module, q_a_proj_name)
delattr(module, self.kv_a_proj_name)
replace_linear_by_name(self.q_b_proj_name, "colwise")
else:
assert self.q_proj_name is not None
replace_linear_by_name(self.kv_a_proj_name, "replicate")
replace_linear_by_name(self.q_proj_name, "colwise")
replace_linear_by_name(self.kv_b_proj_name, "colwise")
# MLAAttention calls kv_b_proj and expects vLLM's default return_bias=True
module.get_submodule(self.kv_b_proj_name).return_bias = True
if self.o_proj_name is not None:
replace_linear_by_name(self.o_proj_name, "rowwise")