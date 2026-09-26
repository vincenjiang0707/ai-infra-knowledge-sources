# [Issue #154] [Bug]: torch.compile在编译时会出现硬件访问超时问题

source: https://github.com/Ascend/pytorch/issues/154
state: open | updated: 2026-07-28T07:28:13Z
labels: 

## 正文

> 该问题同步于GitCode社区，参考：https://gitcode.com/Ascend/pytorch/issues/3067

## 环境信息
环境问题如下

```
- 操作系统：ubuntu22.04
- 昇腾硬件信息：Ascend950PR_9579
- CANN软件版本：CANN 9.0.0
- 安装的对应软件版本 torch 2.10.0，torch_npu（v2.10.0源码编译），triton-ascend 3.2.1
```

其中torch_npu源码版本如下（使用源码编译而非官方release版本是由于另一个bug，参考：https://gitcode.com/Ascend/pytorch/issues/3066）

```
commit 3e81424f0b0f131f64032bdb4173292303257bea (grafted, HEAD -> v2.10.0, origin/v2.10.0)
Author: Dring <17737727613@163.com>
Date:   Mon Jul 20 14:46:52 2026 +0800
```

## 最小复现脚本

```
"""可调参数量的最小 GPT 多 NPU torch.compile 测试。"""

import argparse
import os
import time

import torch
import torch.distributed as dist
import torch.nn as nn
import torch.nn.functional as F
# 导入后会为 PyTorch 注册 NPU backend。
import torch_npu  # noqa: F401


class Block(nn.Module):
    def __init__(self, width, heads):
        super().__init__()
        self.heads = heads
        self.norm1 = nn.RMSNorm(width)
        self.qkv = nn.Linear(width, 3 * width, bias=False)
        self.proj = nn.Linear(width, width, bias=False)
        self.norm2 = nn.RMSNorm(width)
        self.mlp = nn.Sequential(
            nn.Linear(width, 4 * width, bias=False),
            nn.GELU(),
            nn.Linear(4 * width, width, bias=False),
        )

    def forward(self, x):
        batch, seq, width = x.shape
        q, k, v = self.qkv(self.norm1(x)).chunk(3, dim=-1)
        shape = (batch, seq, self.heads, width // self.heads)
        q, k, v = (tensor.view(shape).transpose(1, 2) for tensor in (q, k, v))
        attention = F.scaled_dot_product_attention(q, k, v, is_causal=True)
        x = x + self.proj(attention.transpose(1, 2).contiguous().view(batch, seq, width))
        return x + self.mlp(self.norm2(x))


class GPT(nn.Module):
    def __init__(self, layers, width, heads, vocab_size, seq_len):
        super().__init__()
        self.token = nn.Embedding(vocab_size, width)
        self.position = nn.Embedding(seq_len, width)
        self.blocks = nn.ModuleList([Block(width, heads) for _ in range(layers)])
        self.norm = nn.RMSNorm(width)
        self.head = nn.Linear(width, vocab_size, bias=False)

    def forward(self, tokens, targets):
        positions = torch.arange(tokens.size(1), device=tokens.device)
        x = self.token(tokens) + self.position(positions)
        for block in self.blocks:
            x = block(x)
        logits = self.head(self.norm(x))
        return F.cross_entropy(logits.flatten(0, 1).float(), targets.flatten())


parser = argparse.ArgumentParser(description=__doc__)
parser.add_argument("--layers", type=int, default=4)
parser.add_argument("--width", type=int, default=256)
parser.add_argument("--heads", type=int, default=4)
parser.add_argument("--vocab-size", type=int, default=32768)
parser.add_argument("--seq-len", type=int, default=128)
parser.add_argument("--batch-size", type=int, default=2)
args = parser.parse_args()
assert args.width % args.heads == 0, "width 必须能被 heads 整除"

rank = int(os.environ["RANK"])
local_rank = int(os.environ["LOCAL_RANK"])
device = torch.device("npu", local_rank)
torch.npu.set_device(device)
dist.init_process_group(backend="hccl", device_id=device)
torch.manual_seed(0)

model = GPT(args.layers, args.width, args.heads, args.vocab_size, args.seq_len)
model = model.to(device=device, dtype=torch.bfloat16).train()
tokens = torch.randint(args.vocab_size, (args.batch_size, args.seq_len), device=device)
targets = torch.randint_like(tokens, args.vocab_size)

if rank == 0:
    parameters = sum(parameter.numel() for parameter in model.parameters())
    print(f"GPT parameters: {parameters:,} ({parameters / 1e6:.1f}M)", flush=True)
    print(f"config: {vars(args)}", flush=True)

# 所有 rank 同时进入首次 forward/backward 编译。
dist.barrier()
torch.npu.synchronize()
started = time.monotonic()

model = torch.compile(model)
loss = model(tokens, targets)
loss.backward()

torch.npu.synchronize()
print(
    f"rank {rank}: forward+backward compile={time.monotonic() - started:.2f}s, "
    f"loss={loss.item():.4f}",
    flush=True,
)
dist.destroy_process_group()

```

## 报错信息

在2卡NPU上进行测试，结果如下：

```
ubuntu@ascend950:~/workspace/nanochat-ascend$ ASCEND_RT_VISIBLE_DEVICES=6,7 timeout 300s torchrun   --standalone   --nproc_per_node=2   test_gpt_compile.py   --layers 4   --width 256   --heads 4   --seq-len 128   --batch-size 2   2>&1 | tee gpt-compile-small.log
W0721 14:40:58.569000 3203689 torch/distributed/run.py:852] 
W0721 14:40:58.569000 3203689 torch/distributed/run.py:852] *****************************************
W0721 14:40:58.569000 3203689 torch/distributed/run.py:852] Setting OMP_NUM_THREADS environment variable for each process to be 1 in default, to avoid your system being overloaded, please further tune the variable for optimal performance in your application as needed. 
W0721 14:40:58.569000 3203689 torch/distributed/run.py:852] *****************************************
[rank0]:[W721 14:41:05.320600730 NPUCachingAllocator.cpp:204] Warning: The current CANN and HDK(driver) versions require processing for 32 padding size, with memory allocation. (function operator())
GPT parameters: 19,958,016 (20.0M)
config: {'layers': 4, 'width': 256, 'heads': 4, 'vocab_size': 32768, 'seq_len': 128, 'batch_size': 2}
/home/ubuntu/workspace/nanochat/.venv/lib/python3.12/site-packages/torch_npu/op_plugin/meta/_meta_registrations.py:2227: UserWarning: CAUTION: On Ascend950, when npu_fusion_attention is compiled by torch.compile, the seed, offset, and numels may be optimized, which can cause results to differ from eager mode when the random seed is set. This issue will be fixed in later version.
  _warn_npu_fusion_attention_compile_once()
[rank0]:W0721 14:41:59.823000 3204242 torch/_inductor/debug.py:518] [0/0] model__0_forward_1 debug trace: /home/ubuntu/workspace/nanochat-ascend/torch_compile_debug/run_2026_07_21_14_41_09_079998-pid_3204242/torchinductor/model__0_forward_1.0
2026-07-21 14:42:03,388 - WARNING - [256*x1 + y0, x1 + 32768*y0] low_dims is null, {0, 1}, {0, 1}
2026-07-21 14:42:03,440 - WARNING - [1024*x1 + y0, x1 + 256*y0] low_dims is null, {0, 1}, {0, 1}
2026-07-21 14:42:03,470 - WARNING - [256*x1 + y0, x1 + 1024*y0] low_dims is null, {0, 1}, {0, 1}
2026-07-21 14:42:03,517 - WARNING - [256*x1 + y0, x1 + 256*y0] low_dims is null, {0, 1}, {0, 1}
2026-07-21 14:42:03,567 - WARNING - [256*x1 + y0, x1 + 768*y0] low_dims is null, {0, 1}, {0, 1}
2026-07-21 14:42:03,606 - WARNING - [1024*x1 + y0, x1 + 256*y0] low_dims is null, {0, 1}, {0, 1}
2026-07-21 14:42:03,627 - WARNING - [256*x1 + y0, x1 + 1024*y0] low_dims is null, {0, 1}, {0, 1}
2026-07-21 14:42:03,662 - WARNING - [256*x1 + y0, x1 + 256*y0] low_dims is null, {0, 1}, {0, 1}
2026-07-21 14:42:03,699 - WARNING - [256*x1 + y0, x1 + 768*y0] low_dims is null, {0, 1}, {0, 1}
2026-07-21 14:42:03,735 - WARNING - [1024*x1 + y0, x1 + 256*y0] low_dims is null, {0, 1}, {0, 1}
2026-07-21 14:42:03,754 - WARNING - [256*x1 + y0, x1 + 1024*y0] low_dims is null, {0, 1}, {0, 1}
2026-07-21 14:42:03,791 - WARNING - [256*x1 + y0, x1 + 256*y0] low_dims is null, {0, 1}, {0, 1}
2026-07-21 14:42:03,827 - WARNING - [256*x1 + y0, x1 + 768*y0] low_dims is null, {0, 1}, {0, 1}
2026-07-21 14:42:03,862 - WARNING - [1024*x1 + y0, x1 + 256*y0] low_dims is null, {0, 1}, {0, 1}
2026-07-21 14:42:03,883 - WARNING - [256*x1 + y0, x1 + 1024*y0] low_dims is null, {0, 1}, {0, 1}
2026-07-21 14:42:03,919 - WARNING - [256*x1 + y0, x1 + 256*y0] low_dims is null, {0, 1}, {0, 1}
2026-07-21 14:42:03,955 - WARNING - [256*x1 + y0, x1 + 768*y0] low_dims is null, {0, 1}, {0, 1}
[rank1]:W0721 14:42:21.497000 3204244 torch/_inductor/debug.py:518] [0/0] model__0_forward_1 debug trace: /home/ubuntu/workspace/nanochat-ascend/torch_compile_debug/run_2026_07_21_14_41_09_011532-pid_3204244/torchinductor/model__0_forward_1.0
2026-07-21 14:42:24,867 - WARNING - [256*x1 + y0, x1 + 32768*y0] low_dims is null, {0, 1}, {0, 1}
2026-07-21 14:42:24,917 - WARNING - [1024*x1 + y0, x1 + 256*y0] low_dims is null, {0, 1}, {0, 1}
2026-07-21 14:42:24,948 - WARNING - [256*x1 + y0, x1 + 1024*y0] low_dims is null, {0, 1}, {0, 1}
2026-07-21 14:42:24,994 - WARNING - [256*x1 + y0, x1 + 256*y0] low_dims is null, {0, 1}, {0, 1}
2026-07-21 14:42:25,044 - WARNING - [256*x1 + y0, x1 + 768*y0] low_dims is null, {0, 1}, {0, 1}
2026-07-21 14:42:25,083 - WARNING - [1024*x1 + y0, x1 + 256*y0] low_dims is null, {0, 1}, {0, 1}
2026-07-21 14:42:25,103 - WARNING - [256*x1 + y0, x1 + 1024*y0] low_dims is null, {0, 1}, {0, 1}
2026-07-21 14:42:25,139 - WARNING - [256*x1 + y0, x1 + 256*y0] low_dims is null, {0, 1}, {0, 1}
2026-07-21 14:42:25,175 - WARNING - [256*x1 + y0, x1 + 768*y0] low_dims is null, {0, 1}, {0, 1}
2026-07-21 14:42:25,211 - WARNING - [1024*x1 + y0, x1 + 256*y0] low_dims is null, {0, 1}, {0, 1}
2026-07-21 14:42:25,230 - WARNING - [256*x1 + y0, x1 + 1024*y0] low_dims is null, {0, 1}, {0, 1}
2026-07-21 14:42:25,266 - WARNING - [256*x1 + y0, x1 + 256*y0] low_dims is null, {0, 1}, {0, 1}
2026-07-21 14:42:25,302 - WARNING - [256*x1 + y0, x1 + 768*y0] low_dims is null, {0, 1}, {0, 1}
2026-07-21 14:42:25,337 - WARNING - [1024*x1 + y0, x1 + 256*y0] low_dims is null, {0, 1}, {0, 1}
2026-07-21 14:42:25,358 - WARNING - [256*x1 + y0, x1 + 1024*y0] low_dims is null, {0, 1}, {0, 1}
2026-07-21 14:42:25,393 - WARNING - [256*x1 + y0, x1 + 256*y0] low_dims is null, {0, 1}, {0, 1}
2026-07-21 14:42:25,430 - WARNING - [256*x1 + y0, x1 + 768*y0] low_dims is null, {0, 1}, {0, 1}
[rank0]:W0721 14:42:54.653000 3204242 torch/_inductor/debug.py:518] [0/0] model__0_backward_3 debug trace: /home/ubuntu/workspace/nanochat-ascend/torch_compile_debug/run_2026_07_21_14_41_09_079998-pid_3204242/torchinductor/model__0_backward_3.1
rank 0: forward+backward compile=110.46s, loss=10.5788
^[[A^[[A^[[ATerminated
```

> 最后是通过ctrl+c中断任务

目前看来一个20.0M的参数量的GPT模型，在rank0进行了110s的编译时间。

不过没遇到npu-smi info的命令卡死问题，使用命令后发现rank1的进程消失了😂。推测原因可能时超时或者别的原因导致了挂掉。

## 评论 (1)

### ShaohonChen · 2026-07-28

感谢 [@Akiy](https://github.com/Akiyamaice)大神提供的解决方案：https://gitcode.com/Ascend/pytorch/issues/3067?ref=&did=3385bc5e9d78edb6005805dc0f5f68dabe75ff7f#tid-181334773

不过在较大参数量下（1.5B）仍会出现超时，原因暂未排查到
