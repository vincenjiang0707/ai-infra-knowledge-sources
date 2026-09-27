# [Issue #94] bitblas introduces dependency on CUDA version

source: https://github.com/dropbox/hqq/issues/94
state: closed | updated: 2024-07-18T08:42:33Z
labels: 

## 正文

I was trying to apply `torchao_int4` to a model, and got the following Error when running`from hqq.utils.patching import prepare_for_inference`:

```
File ~/******/python3.10/site-packages/hqq/utils/patching.py:11
      9 from ..backends.torchao import patch_hqq_to_aoint4
     10 from ..backends.marlin import patch_hqq_to_marlin
---> 11 from ..backends.bitblas import patch_hqq_to_bitblas
     14 def patch_linearlayers(model, fct, patch_param=None, verbose=False):
     15     base_class = model.base_class if (hasattr(model, "base_class")) else AutoHQQHFModel
..........
File ~/******/python3.10/site-packages/bitblas/3rdparty/tvm/python/tvm/_ffi/base.py:64, in _load_lib()
     62     for path in libinfo.get_dll_directories():
     63         os.add_dll_directory(path)
---> 64 lib = ctypes.CDLL(lib_path[0], ctypes.RTLD_GLOBAL)
     65 lib.TVMGetLastError.restype = ctypes.c_char_p
     66 return lib, os.path.basename(lib_path[0]);

File ~/******/python3.10/ctypes/__init__.py:374, in CDLL.__init__(self, name, mode, handle, use_errno, use_last_error, winmode)
    371 self._FuncPtr = _FuncPtr
    373 if handle is None:
--> 374     self._handle = _dlopen(self._name, mode)
    375 else:
    376     self._handle = handle

OSError: libnvrtc.so.12: cannot open shared object file: No such file or directory
```

Unfortunately it is not applicable for me to upgrade the CUDA version due to not in control of the environment and compatibility issues from other packages.
Would it be possible to make faster backends such as torchao and bitblas as optional dependencies to avoid similar problem?

**Related**:
bitblas has plans to make compatible wheels for more CUDA versions but not yet finished.
https://github.com/microsoft/BitBLAS/issues/62



## 评论 (3)

### mobicham · 2024-07-16

Hey! Thanks for pointing this out! We mainly test with the nightly torch build which requires CUDA 12.2, since it offers the best optimization for `torch.compile`. 
I removed the bitblas dependency and added a check (same for Marlin), it should work fine now:
https://github.com/mobiusml/hqq/commit/e57104fdcac92bab2a3eed01e75bd30a837c1cfe

### LeiWang1999 · 2024-07-18

Thanks for your attention,  we just released 0.0.1.dev13 on pypi, the dependency for cuda 12 has been removed, please feel free to test with:

```bash
pip install bitblas==0.0.1.dev13
```

### mobicham · 2024-07-18

Thanks @LeiWang1999 , will test it !
