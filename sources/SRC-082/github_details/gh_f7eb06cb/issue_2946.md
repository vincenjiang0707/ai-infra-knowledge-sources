# [Issue #2946] [BUG] GLM5.2 unsupported

source: https://github.com/ModelCloud/GPTQModel/issues/2946
state: closed | updated: 2026-07-13T18:46:00Z
labels: bug

## 正文

**Describe the bug**

GLM 5.2 is not supported because of the new shared module (prev_topk_indices is missing in the forward).

```
python3.12/site-packages/transformers/models/glm_moe_dsa/modeling_glm_moe_dsa.py", line 418, in forward
    raise ValueError("Shared DSA layers require top-k indices from a previous full indexer layer.")
ValueError: Shared DSA layers require top-k indices from a previous full indexer layer.

```

**Software Info**

Operation System/Version + Python Version

Show output of:
```
GPTQModel @ git+https://github.com/ModelCloud/GPTQModel.git@b11aee07889a7030f80057b9850416b200613d47
```



## 评论 (2)

### CaptainRong · 2026-07-10

We do the same.
  GLM-5.2 introduces IndexShare for DSA: some decoder layers reuse the
  `topk_indices` produced by a previous layer instead of running their own
  indexer. During normal model execution, this state is passed between decoder
  layers as `prev_topk_indices`.

  GPTQModel performs calibration with layer-by-layer replay. We were already
  cross-layer IndexShare state was lost before a shared DSA layer was replayed.

  Our fix is to preserve this auxiliary state per calibration batch:

  1. Run the current decoder layer.
  2. Keep `output[0]` as the next layer's hidden states.
  3. When `output[1]` contains valid `topk_indices`, store it in that batch's
     replay kwargs as `prev_topk_indices`.
  4. Move it to the appropriate calibration/compute device before replaying the
     next layer.

  The same propagation is required in both the serial replay path and the
  automatic forward data-parallel worker path.

preserving GLM-5.2's cross-layer IndexShare state during quantization replay.

You can refer to our patch:`https://gist.github.com/CaptainRong/f4f4a7bcd719709b14faef92718bd71f`

### Qubitium · 2026-07-11

@CaptainRong Can you PR the mod? This way you get this proper credit instead of us basing a PR from your delta.
