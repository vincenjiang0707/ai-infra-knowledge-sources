# [Issue #3345] [Bug] AttributeError: module 'qwix' has no attribute 'QArray' crashes MaxText on import

source: https://github.com/AI-Hypercomputer/maxtext/issues/3345
state: closed | updated: 2026-05-01T22:16:48Z
labels: bug

## 正文

### Bug report



###  Bug Report: `AttributeError: module 'qwix' has no attribute 'QArray'` crashes MaxText on import

**Description:**
When attempting to `import MaxText` or run checkpoint conversion in a custom TPU container, the script fatally crashes. `tokamax` relies on a `QArray` attribute from the `qwix` library, but dependency resolution during container build results in a version of `qwix` where this attribute is missing.

**The Trigger (Context):**
This bug appears specifically when we optimize our Dockerfile to install the CPU-only version of PyTorch prior to installing `vllm-tpu` and `maxtext` (to prevent `pip` from pulling 4GB+ of useless NVIDIA CUDA binaries onto a Google TPU container).

Forcing the PyTorch CPU wheel changes `pip`'s dependency resolution, causing it to pull a version of `qwix` (likely an older stable release from PyPI) that does not expose `qwix.QArray` at the top level.

**To Reproduce:**

1. Set up an environment/container and explicitly install CPU PyTorch first:
`pip install torch torchvision torchaudio --index-url [https://download.pytorch.org/whl/cpu](https://download.pytorch.org/whl/cpu)`
2. Install `vllm-tpu` and `maxtext` from `main`.
3. Run a script with:
```python
import MaxText

```

### Logs/Output

**Traceback:**

```text
Traceback (most recent call last):
  File "/usr/local/lib/python3.12/site-packages/MaxText/__init__.py", line 39, in <module>
    from maxtext.models import models
  # ... [skipping internal maxtext paths for brevity] ...
  File "/usr/local/lib/python3.12/site-packages/tokamax/_src/ops/attention/base.py", line 34, in <module>
    from tokamax._src import quantization
  File "/usr/local/lib/python3.12/site-packages/tokamax/_src/quantization.py", line 26, in <module>
    QArray = qwix.QArray
AttributeError: module 'qwix' has no attribute 'QArray'

```

### Environment Information


**Environment:**

* **Hardware:** TPU v5e / v5p
* **Python:** 3.12
* **Installation:** Installed via `pip install ".[tpu]"` from the `main` branch.


### Additional Context


**Current Workaround:**
We were able to bypass the crash by injecting a mock `QArray` object into `sys.modules` immediately before importing MaxText:

```python
import sys, types
try:
    import qwix
    if not hasattr(qwix, 'QArray'): 
        qwix.QArray = type('QArray', (object,), {})
except ImportError:
    qwix = types.ModuleType('qwix')
    qwix.QArray = type('QArray', (object,), {})
    sys.modules['qwix'] = qwix

# Now imports safely
import MaxText 

```

## 评论 (3)

### khatwanimohit · 2026-03-06

can you try installing maxtext deps with `uv pip install -e .[tpu] --resolution=lowest` as mentioned in https://maxtext.readthedocs.io/en/latest/install_maxtext.html#from-source. This should install `qwix>=0.1.4` which is required for MaxText

### SurbhiJainUSC · 2026-04-27

@karajendran - Could you please confirm if the installation method mentioned by @khatwanimohit resolves the issue?

### sarunsingla11722 · 2026-05-01

Closing this as its no longer a valid issue.
