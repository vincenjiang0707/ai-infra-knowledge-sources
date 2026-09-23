source: https://docs.vllm.ai/en/latest/api/vllm/models/inkling/amd/attention/
lastmod: 2026-09-23

Bases: [Module](https://pytorch.org/docs/stable/generated/torch.nn.Module.html#torch.nn.Module)


Project the per-head relative branch `r`

to per-distance logits.

## Source code in `vllm/models/inkling/amd/attention.py`


| class RelLogitsProj(nn.Module):
"""Project the per-head relative branch ``r`` to per-distance logits."""
def __init__(self, d_rel: int, rel_extent: int) -> None:
super().__init__()
self.d_rel = d_rel
self.rel_extent = rel_extent
self.proj = nn.Parameter(torch.empty(d_rel, rel_extent), requires_grad=False)
def forward(self, r_out: torch.Tensor) -> torch.Tensor:
# r_out: (T, num_heads, d_rel) -> (T, num_heads, rel_extent)
return torch.einsum("thd,de->the", r_out, self.proj)
|