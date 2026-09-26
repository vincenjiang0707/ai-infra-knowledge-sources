# [Issue #84] How to use  torch_npu._npu_flash_attention_qlens

source: https://github.com/Ascend/pytorch/issues/84
state: open | updated: 2025-10-14T06:46:39Z
labels: 

## 正文

I'm trying to use `torch_npu._npu_flash_attention_qlens` and I'm confused about its input parameters. ( torch_npu: 2.5.1 )

```python
torch_npu._npu_flash_attention_qlens(
    query=query,
    key_cache=self.key_cache,
    value_cache=self.value_cache,
    block_table=block_tables,
    mask=compress_mask,
    seq_len=self.query_lens_tensor_cpu,
    context_lens=self.seq_lens_tensor_cpu,
    num_kv_heads=self.num_kv_heads,
    num_heads=self.num_heads,
    scale_value=self.scale,
    out=output)
```

Could you please provide details on the specific requirements and usage of the **`query`**, **`block_table`**, **`mask`**, **`seq_len`**, and **`context_lens`** parameters?

Any example code or links to documentation would be helpful. Thanks for your time and help!

## 评论 (1)

### jxj9049 · 2025-10-14

torch_npu._npu_flash_attention_qlens is a non-public interface. For operator documentation and specific parameters, please refer to this link.    https://www.hiascend.com/document/detail/zh/canncommercial/82RC1/API/ascendtbapi/ascendtb_01_0282.html
