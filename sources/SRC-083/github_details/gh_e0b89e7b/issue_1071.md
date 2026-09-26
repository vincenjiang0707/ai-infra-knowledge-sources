# [Issue #1071] FPE in quantize_blockwise

source: https://github.com/bitsandbytes-foundation/bitsandbytes/issues/1071
state: closed | updated: 2026-02-21T20:10:01Z
labels: Low Priority, x64 CPU

## 正文

### System Info

Distributor ID: Ubuntu
Description:    Ubuntu 22.04.4 LTS
Release:        22.04
Codename:       jammy
Python 3.10.12

### Reproduction

```python
import bitsandbytes as bnb
from bitsandbytes import functional as F
import torch

bnb.nn.Linear8bitLt(1, 2, bias=True, has_fp16_weights=False, threshold=6.0)

A1 = torch.zeros(0, 0, 0, device='cpu')
A1 = torch.ones(1, 1, 1, device='cpu')
C, S = F.quantize_blockwise(A1, blocksize=2**64)
print(C)
```

crash backtrace

```

Thread 1 "python3" received signal SIGFPE, Arithmetic exception.
0x00007fffd7e035a6 in quantize_cpu(float*, float*, float*, unsigned char*, long long, long long) () from /usr/local/lib/python3.10/dist-packages/bitsandbytes/libbitsandbytes_cpu.so
[ Legend: Modified register | Code | Heap | Stack | String ]
────────────────────────────────────────────────────────────────────────────────────────────────────────────────────── registers ────
$rax   : 0x1
$rbx   : 0x00007fffffffd9b0  →  0x0000003000000028 ("("?)
$rcx   : 0x0000555558055440  →  0x0000555557f24900  →  "_\.]?[0-9]*)?          # dev release\n            [...]"
$rdx   : 0x0
$rsp   : 0x00007fffffffd740  →  0x0000000000000001
$rbp   : 0x00007fffffffd840  →  0x00007fffffffd880  →  0x00007fffffffd890  →  0x0000000000000006
$rsi   : 0x0000555557fba540  →  0x000000003f800000
$rdi   : 0x00005555580feb40  →  0xbf7a9999bf800000
$rip   : 0x00007fffd7e035a6  →  <quantize_cpu(float*,+0> idiv QWORD PTR [rbp-0xf8]
$r8    : 0x0
$r9    : 0x1
$r10   : 0x0
$r11   : 0x00007fffd7e052c3  →  <cquantize_blockwise_cpu_fp32+0> push rbp
$r12   : 0x8
$r13   : 0x00007fffffffd9f0  →  0x00007fffffffdab0  →  0x00007ffff7705570  →  0x0000000000000008
$r14   : 0x00007ffff7705570  →  0x0000000000000008
$r15   : 0x00007ffff7582110  →  0xffffb400ffffb3ac
$eflags: [zero carry parity adjust sign trap INTERRUPT direction overflow RESUME virtualx86 identification]
$cs: 0x33 $ss: 0x2b $ds: 0x00 $es: 0x00 $fs: 0x00 $gs: 0x00
────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────── stack ────
0x00007fffffffd740│+0x0000: 0x0000000000000001   ← $rsp
0x00007fffffffd748│+0x0008: 0x0000000000000000
0x00007fffffffd750│+0x0010: 0x0000555558055440  →  0x0000555557f24900  →  "_\.]?[0-9]*)?          # dev release\n            [...]"
0x00007fffffffd758│+0x0018: 0x0000555557faea80  →  0x0000555500000000
0x00007fffffffd760│+0x0020: 0x0000555557fba540  →  0x000000003f800000
0x00007fffffffd768│+0x0028: 0x00005555580feb40  →  0xbf7a9999bf800000
0x00007fffffffd770│+0x0030: 0x00007fffffffd950  →  0x0000555555c49060  →  0x0000000000000014
0x00007fffffffd778│+0x0038: 0x0000000000000001
──────────────────────────────────────────────────────────────────────────────────────────────────────────────────── code:x86:64 ────
   0x7fffd7e03599 <quantize_cpu(float*,+0> movss  DWORD PTR [rax], xmm0
   0x7fffd7e0359d <quantize_cpu(float*,+0> mov    rax, QWORD PTR [rbp-0x100]
   0x7fffd7e035a4 <quantize_cpu(float*,+0> cqo
 → 0x7fffd7e035a6 <quantize_cpu(float*,+0> idiv   QWORD PTR [rbp-0xf8]
   0x7fffd7e035ad <quantize_cpu(float*,+0> mov    QWORD PTR [rbp-0x40], rax
   0x7fffd7e035b1 <quantize_cpu(float*,+0> mov    rax, QWORD PTR [rbp-0x100]
   0x7fffd7e035b8 <quantize_cpu(float*,+0> cqo
   0x7fffd7e035ba <quantize_cpu(float*,+0> idiv   QWORD PTR [rbp-0xf8]
   0x7fffd7e035c1 <quantize_cpu(float*,+0> mov    rax, rdx
[!] Command 'context' failed to execute properly, reason: 'threads'
gef➤  bt
#0  0x00007fffd7e035a6 in quantize_cpu(float*, float*, float*, unsigned char*, long long, long long) () from /usr/local/lib/python3.10/dist-packages/bitsandbytes/libbitsandbytes_cpu.so
#1  0x00007fffd7e05309 in cquantize_blockwise_cpu_fp32 () from /usr/local/lib/python3.10/dist-packages/bitsandbytes/libbitsandbytes_cpu.so

```

### Expected behavior

execute normally without any crash

## 评论 (2)

### matthewdouglas · 2024-02-23

I can reproduce this behavior. We get a division by zero because `blocksize` is a 64-bit `long long` and overflows.

Is there a practical reason or need for `blocksize` that large?

### TimDettmers · 2026-02-21

Closing this issue. The crash is caused by passing `blocksize=2**64`, which overflows the 64-bit integer used in the C kernel's division operation. No practical workload would use a blocksize this large. If you'd like to see a bounds check added to produce a clean error instead of a SIGFPE, a PR would be welcome — but the underlying behavior is not a bug in normal usage.

If you're still experiencing issues with realistic blocksize values on the latest bitsandbytes, please open a new issue.
