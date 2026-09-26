# [Issue #1810] LARS missing in str2optimizer32bit

source: https://github.com/bitsandbytes-foundation/bitsandbytes/issues/1810
state: closed | updated: 2026-02-20T19:34:04Z
labels: Optimizers

## 正文

### System Info
Ubuntu 24.04.2 LTS
NVIDIA Driver Version: 550.144.03
CUDA Version: 12.4
GPU A100 (80GB PCIE)
Python 3.12.3
bitsandbytes 0.48.2


### Description
I initially posted this as a [discussion forum question](https://github.com/bitsandbytes-foundation/bitsandbytes/discussions/1801), but I think it is more appropriate as an issue.

I am using bitsandbytes (version 0.48.2) and I am trying to run use LARS in my torch code. Strangely I can get other bitsandbytes optimizers including LAMB running, but LARS wont run.

Error message:
> <PATH2PROJECT>.venv/lib/python3.12/site-packages/bitsandbytes/backends/cuda/ops.py", line 635, in optimizer_update_32bit_impl
>     raise ValueError(
> ValueError: Unsupported optimizer name: lars. Supported optimizers: ['adam', 'momentum', 'rmsprop', 'lion', 'adagrad', 'ademamix']
> 

Looking at `bitsandbytes/backends/cuda/ops.py` it seems to be because
`optim_fns = str2optimizer32bit.get(optimizer_name, None)` has value `None`, because `str2optimizer32bit` does not have a case for lars. Here is a [link to the relevant lines](https://github.com/bitsandbytes-foundation/bitsandbytes/blob/63f538a4e492017dd4a52edfde142c4ca818d401/bitsandbytes/backends/cuda/ops.py#L543-L577). The error message is also incorrect as it lists the supported 8bit optimizers instead of the supported 32bit optimizers. 

**TLDR:**
- `"lars"` is not handled by `str2optimizer32bit `in `bitsandbytes/backends/cuda/ops.py`?
- The error message displays the keys of `str2optimizer8bit_blockwise `instead of the keys of `str2optimizer32bit `as the list of supported optimizers.

**Sidenote**: It looks like LAMB maps to cadam kernels. Is this because the same kernels can be used for both methods?

**Related issues:**
- https://github.com/bitsandbytes-foundation/bitsandbytes/issues/1118
- https://github.com/Nerogar/OneTrainer/issues/390

### Reproduction
```
import torch
import torch.nn as nn
import bitsandbytes as bnb

device = "cuda"

# Dummy model
class SimpleModel(nn.Module):
    def __init__(self):
        super().__init__()
        self.lin = nn.Linear(10, 2)

    def forward(self, x):
        return self.lin(x)

model = SimpleModel().to(device)

# Fake batch on GPU
x = torch.randn(4, 10, device=device)
y = torch.randint(0, 2, (4,), device=device)

criterion = nn.CrossEntropyLoss().to(device)

# bitsandbytes LARS optimizer on GPU
optimizer = bnb.optim.LARS(
    model.parameters(),
    lr=1e-3,
    momentum=0.9,
    weight_decay=1e-4,
)

# Training step
optimizer.zero_grad()
pred = model(x)
loss = criterion(pred, y)
loss.backward()
optimizer.step()
```

### Expected behavior

Running the script will lead to a ValueError.   

>   File "<PATH2PROJECT>/.venv/lib/python3.12/site-packages/bitsandbytes/backends/cuda/ops.py", line 635, in _optimizer_update_32bit_impl
>     raise ValueError(
> ValueError: Unsupported optimizer name: lars. Supported optimizers: ['adam', 'momentum', 'rmsprop', 'lion', 'adagrad', 'ademamix']

## 评论 (1)

### matthewdouglas · 2025-11-18

Hi,

Thank you for reporting.

Admittedly I'm not very familiar with the LARS or LAMB optimizers. However, my understanding is that they're indeed meant to reuse the kernel implementations of Adam (in the case of LAMB) and Momentum (in the case of LARS), with maybe some additional parameters.

In general it looks like LARS is missing the 32bit implementation, and both are missing the 8bit blockwise implementations.

You're right that the error message is incorrect as well.  

Will look into it!
