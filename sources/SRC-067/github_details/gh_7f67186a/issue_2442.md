# [Issue #2442] [Wheel] Pre-built flash_attn v2.8.3 for CUDA 13 + PyTorch 2.11 (Python 3.12)

source: https://github.com/Dao-AILab/flash-attention/issues/2442
state: open | updated: 2026-08-07T01:14:37Z
labels: 

## 正文

An official wheel does not exist for CUDA 13 + PyTorch 2.11 yet. Here is a community-built wheel for flash_attn v2.8.3.

### Compatibility

- **CUDA**: 13.0
- **PyTorch**: 2.11
- **Python**: 3.12
- **Platform**: Linux x86_64
- **CXX11 ABI**: TRUE

### Install

```bash
pip install "https://github.com/adithyaxx/flash-attention/releases/download/v2.8.3/flash_attn-2.8.3+cu13torch2.11cxx11abiTRUE-cp312-cp312-linux_x86_64.whl"

## 评论 (3)

### DrAculaMD · 2026-04-26

Any for Python 3.13?

### cooperdk · 2026-07-02

> Any for Python 3.13?

Yes, there's something called Google ;)

### drstakc · 2026-08-07

Googling for Python 3.13 is what brought me here
