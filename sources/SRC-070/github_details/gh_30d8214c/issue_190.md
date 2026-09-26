# [Issue #190] [Bug]TMA Multicast code issue

source: https://github.com/deepseek-ai/DeepGEMM/issues/190
state: closed | updated: 2025-09-15T01:44:51Z
labels: 

## 正文

in file `/sgl-workspace/DeepGEMM/csrc/jit_kernels/heuristics/common.hpp:213-226`
This piece of code logic seems not correct:
```
    // Decide the number of TMA multicasts and whether broadcast on A
    MulticastConfig best_multicast_config = {1, true};
    const auto& [is_legal_on_a, is_legal_on_b] = ArchSpec::get_multicast_legality(gemm_type, m, n, best_block_m, best_block_n, num_sms);
    const bool is_legal[2] = {is_legal_on_a, is_legal_on_b};
    bool order[2] = {false, true};
    if (best_block_m > best_block_n)
        std::swap(order[0], order[1]);
    for (const bool& is_multicast_on_a: order) {
        if (m >= 512 and is_legal[static_cast<int>(is_multicast_on_a)]) {
            best_multicast_config = {2, is_multicast_on_a};
            break;
        }
    }
```
When the `best_block_m` bigger than `best_block_n` the `order` vector is swapped. The `is_multicast_on_a` is ture now. In the `if` condition `is_legal[static_cast<int>(is_multicast_on_a)]` will access the `is_legal[1]` which is actually checking the `is_legal_on_b` instead. 



## 评论 (1)

### yukuai26 · 2025-09-12

Hi, @afei6 . Thank you for pointing this out. In fact, we also happened to discover this issue yesterday. This is the fix for this.
#193 

