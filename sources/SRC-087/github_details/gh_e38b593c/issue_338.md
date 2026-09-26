# [Issue #338] [RFC]: support sp ulysses to optimize memory usage

source: https://github.com/vllm-project/speculators/issues/338
state: closed | updated: 2026-07-09T18:43:56Z
labels: stale, RFC

## 正文

### Motivation.

In long-sequence scenarios, we are confronted with excessive memory consumption on Ascend device, which eventually results in OOM errors. Similarly, memory usage on GPU deviceis also operating at the extreme limit. When we plan to integrate eagle3 to RL, there will be cases of 128k long sequences, which cannot be supported by the current memory capacity.

### Proposed Change.

## Core Functionality
This commit primarily implements support for Sequence Parallelism Ulysses (SP Ulysses) , used for parallel processing of long sequences in distributed training.

### 1. Distributed Training Framework Refactoring (distributed.py)
- New maybe_setup_distributed() function : Initializes distributed training environment
  
  - Supports both SP Ulysses and SP Ring parallel strategies
  - Creates device_mesh for managing draft_dp and sp dimensions
  - Sets up Ulysses process groups (size=4) and Ring process groups (size=1)
- New all-gather operation functions : all_gather_tensor() and Gather custom autograd functions for distributed tensor aggregation
- New gather_outputs_and_unpad() function : Collects outputs along sequence dimension and removes padding
### 2. Eagle3 Model Core Modifications (core.py)
- New prepare_usp_input() method : Prepares input for Ulysses sequence parallelism, chunking full input along SP dimension
- Modified forward() method :
  
  - Calls prepare_usp_input() on hidden_states and input_ids for sharding
  - Supports conversion from global input to local shards
  - Processes sharded input in each TTT (Test-Time Training) step
- New sequence parallelism related attributes :
  
  ```
  self.sp_ring_degree = torch.distributed.get_world_size(get_sp_ring_group())
  self.sp_ulysses_degree = torch.distributed.get_world_size(get_sp_ulysses_group
  ())
  self.sp_world_size = self.sp_ring_degree * self.sp_ulysses_degree
  self.sp_rank = torch.distributed.get_rank() % self.sp_world_size
  ```
### 3. Eagle3 Attention Layer USP Implementation (model_definitions.py)
Core class LlamaUSPFlashAttention : Implements Flash Attention supporting both Ulysses SP and Ring SP

- Initialization parameters :
  
  - Gets Ring and Ulysses process groups
  - Sets number of heads, head dimensions, position encoding, etc.
- Forward propagation forward() :
  
  1. Projects Q/K/V and reshapes
  2. Uses SeqAllToAll4D to exchange sequence and head dimensions within Ulysses group
  3. Applies RoPE position encoding (supports sharded sequences)
  4. Calls ring_attention_hybrid_masked() to execute Ring Attention
  5. Uses SeqAllToAll4D again to restore tensor shapes
  6. Output projection
- Ring Attention implementation ring_attention_hybrid_masked() :
  
  - Loops within Ring process group to compute attention
  - Supports KV Cache accumulation
  - Uses Online Softmax algorithm for numerically stable computation
  - Supports attention masks
- Auxiliary function all_to_all_4D() : Implements all-to-all communication for 4D tensors, used for Ulysses SP
### 4. Utility Functions Update (utils.py)
- Removes import and definition of maybe_setup_distributed and maybe_destroy_distributed functions
- Keeps apply_fully_sharded() function for FSDP sharding
### 5. Training Script Update (train.py)
- Modifies import statement to import distributed functions from speculators.train.distributed (instead of speculators.train.utils )

### Any Other Things.

related pr: https://github.com/vllm-project/speculators/pull/298

## 评论 (2)

### github-actions[bot] · 2026-06-08

This issue has been automatically marked as stale because it has not had any activity within 90 days. It will be automatically closed if no further activity occurs within 30 days. Leave a comment if you feel this issue should remain open. Thank you!

### github-actions[bot] · 2026-07-09

This issue has been automatically closed due to inactivity. Please feel free to reopen if you feel it is still relevant. Thank you!
