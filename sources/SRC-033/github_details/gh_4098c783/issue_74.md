# [Issue #74] fatal error: 'cstdint' file not found

source: https://github.com/Ascend/pytorch/issues/74
state: closed | updated: 2025-07-23T06:21:06Z
labels: 

## 正文

When I run the folling example in openeuler docker
```
import torch
import torch_npu

x = torch.randn(2, 2).npu()
y = torch.randn(2, 2).npu()
z = x.mm(y)

print(z)
```
I get following error msg.
```
(torch) [HwHiAiUser@ec24358c0133 ~]$ python
Python 3.10.0 (default, Mar  3 2022, 09:51:40) [GCC 10.2.0] on linux
Type "help", "copyright", "credits" or "license" for more information.
>>> import torch
>>> import torch_npu
/home/HwHiAiUser/miniconda3/envs/torch/lib/python3.10/site-packages/torch_npu/utils/collect_env.py:59: UserWarning: Warning: The /usr/local/Ascend/ascend-toolkit/latest owner does not match the current owner.
  warnings.warn(f"Warning: The {path} owner does not match the current owner.")
/home/HwHiAiUser/miniconda3/envs/torch/lib/python3.10/site-packages/torch_npu/utils/collect_env.py:59: UserWarning: Warning: The /usr/local/Ascend/ascend-toolkit/8.0.0/aarch64-linux/ascend_toolkit_install.info owner does not match the current owner.
  warnings.warn(f"Warning: The {path} owner does not match the current owner.")
/home/HwHiAiUser/miniconda3/envs/torch/lib/python3.10/site-packages/torch_npu/__init__.py:248: UserWarning: On the interactive interface, the value of TASK_QUEUE_ENABLE is set to 0 by default.                      Do not set it to 1 to prevent some unknown errors
  warnings.warn("On the interactive interface, the value of TASK_QUEUE_ENABLE is set to 0 by default. \
>>> x = torch.randn(2, 2).npu()
>>> y = torch.randn(2, 2).npu()
>>> z = x.mm(y)
>>> print(z.tolist())
[[0.05088329315185547, 0.2660367488861084], [-0.6694704294204712, -0.039534807205200195]]
>>> print(z)
.[2025-7-23 2:49:25] [ERROR] [ascend310p] fd1f3c4bdc778d7f5070ef57ebf58286c6b1cb73a610b1b9b09d1fdf2acd696b_te In file included from /usr/local/Ascend/ascend-toolkit/8.0.0/opp/built-in/op_impl/ai_core/tbe/impl/dynamic/../ascendc/is_finite/is_finite.cpp:22:
In file included from /usr/local/Ascend/ascend-toolkit/8.0.0/opp/built-in/op_impl/ai_core/tbe/impl/dynamic/../ascendc/is_finite/is_finite.h:24:
In file included from /usr/local/Ascend/ascend-toolkit/8.0.0/aarch64-linux/tikcpp/tikcfw/kernel_operator.h:24:
In file included from /usr/local/Ascend/ascend-toolkit/8.0.0/aarch64-linux/tikcpp/tikcfw/impl/kernel_tpipe_impl.h:23:
In file included from /usr/local/Ascend/ascend-toolkit/8.0.0/aarch64-linux/tikcpp/tikcfw/interface/kernel_tpipe.h:23:
In file included from /usr/local/Ascend/ascend-toolkit/8.0.0/aarch64-linux/tikcpp/tikcfw/impl/kernel_tpipe_base.h:23:
In file included from /usr/local/Ascend/ascend-toolkit/8.0.0/aarch64-linux/tikcpp/tikcfw/impl/kernel_tensor_impl.h:23:
In file included from /usr/local/Ascend/ascend-toolkit/8.0.0/aarch64-linux/tikcpp/tikcfw/interface/kernel_tensor.h:24:
In file included from /usr/local/Ascend/ascend-toolkit/8.0.0/aarch64-linux/tikcpp/tikcfw/impl/kernel_utils.h:23:
In file included from /usr/local/Ascend/ascend-toolkit/8.0.0/aarch64-linux/tikcpp/tikcfw/impl/utils/kernel_utils_macros.h:33:
/usr/local/Ascend/ascend-toolkit/8.0.0/aarch64-linux/tikcpp/tikcfw/impl/kernel_macros.h:24:10: fatal error: 'cstdint' file not found
#include <cstdint>
         ^~~~~~~~~
1 error generated.

Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
  File "/home/HwHiAiUser/miniconda3/envs/torch/lib/python3.10/site-packages/torch/_tensor.py", line 431, in __repr__
    return torch._tensor_str._str(self, tensor_contents=tensor_contents)
  File "/home/HwHiAiUser/miniconda3/envs/torch/lib/python3.10/site-packages/torch/_tensor_str.py", line 664, in _str
    return _str_intern(self, tensor_contents=tensor_contents)
  File "/home/HwHiAiUser/miniconda3/envs/torch/lib/python3.10/site-packages/torch/_tensor_str.py", line 595, in _str_intern
    tensor_str = _tensor_str(self, indent)
  File "/home/HwHiAiUser/miniconda3/envs/torch/lib/python3.10/site-packages/torch/_tensor_str.py", line 347, in _tensor_str
    formatter = _Formatter(get_summarized_data(self) if summarize else self)
  File "/home/HwHiAiUser/miniconda3/envs/torch/lib/python3.10/site-packages/torch/_tensor_str.py", line 138, in __init__
    tensor_view, torch.isfinite(tensor_view) & tensor_view.ne(0)
RuntimeError: InnerRun:build/CMakeFiles/torch_npu.dir/compiler_depend.ts:218 OPS function error: IsFinite, error code is 500002
[ERROR] 2025-07-23-10:49:25 (PID:10534, Device:0, RankID:-1) ERR01100 OPS call acl api failed
[Error]: A GE error occurs in the system.
        Rectify the fault based on the error information in the ascend log.
E40021: [PID: 10534] 2025-07-23-10:49:25.578.073 Failed to compile Op [IsFinite2]. (oppath: [Compile /usr/local/Ascend/ascend-toolkit/8.0.0/opp/built-in/op_impl/ai_core/tbe/impl/dynamic/is_finite.py failed with errormsg/stack: File "/usr/local/Ascend/ascend-toolkit/latest/python/site-packages/tbe/tikcpp/compile_op.py", line 530, in dump_build_log
    raise Exception("An error occurred during compile phases of {}, msg is {}".\
Exception: An error occurred during compile phases of CompileStage.PRECOMPILE, msg is In file included from /usr/local/Ascend/ascend-toolkit/8.0.0/opp/built-in/op_impl/ai_core/tbe/impl/dynamic/../ascendc/is_finite/is_finite.cpp:22:
In file included from /usr/local/Ascend/ascend-toolkit/8.0.0/opp/built-in/op_impl/ai_core/tbe/impl/dynamic/../ascendc/is_finite/is_finite.h:24:
In file included from /usr/local/Ascend/ascend-toolkit/8.0.0/aarch64-linux/tikcpp/tikcfw/kernel_operator.h:24:
In file included from /usr/local/Ascend/ascend-toolkit/8.0.0/aarch64-linux/tikcpp/tikcfw/impl/kernel_tpipe_impl.h:23:
In file included from /usr/local/Ascend/ascend-toolkit/8.0.0/aarch64-linux/tikcpp/tikcfw/interface/kernel_tpipe.h:23:
In file included from /usr/local/Ascend/ascend-toolkit/8.0.0/aarch64-linux/tikcpp/tikcfw/impl/kernel_tpipe_base.h:23:
In file included from /usr/local/Ascend/ascend-toolkit/8.0.0/aarch64-linux/tikcpp/tikcfw/impl/kernel_tensor_impl.h:23:
In file included from /usr/local/Ascend/ascend-toolkit/8.0.0/aarch64-linux/tikcpp/tikcfw/interface/kernel_tensor.h:24:
In file included from /usr/local/Ascend/ascend-toolkit/8.0.0/aarch64-linux/tikcpp/tikcfw/impl/kernel_utils.h:23:
In file included from /usr/local/Ascend/ascend-toolkit/8.0.0/aarch64-linux/tikcpp/tikcfw/impl/utils/kernel_utils_macros.h:33:
/usr/local/Ascend/ascend-toolkit/8.0.0/aarch64-linux/tikcpp/tikcfw/impl/kernel_macros.h:24:10: fatal error: 'cstdint' file not found
#include <cstdint>
         ^~~~~~~~~
1 error generated.

], optype: [IsFinite])
        Solution: See the host log for details, and then check the Python stack where the error log is reported.
        TraceBack (most recent call last):
        Compile op[IsFinite2] failed, oppath[/usr/local/Ascend/ascend-toolkit/8.0.0/opp/built-in/op_impl/ai_core/tbe/impl/dynamic/is_finite.py], optype[IsFinite], taskID[14]. Please check op's compilation error message.[FUNC:ReportBuildErrMessage][FILE:fusion_manager.cc][LINE:367]
        [SubGraphOpt][Compile][ProcFailedCompTask] Thread[281472123728288] recompile single op[IsFinite2] failed[FUNC:ProcessAllFailedCompileTasks][FILE:tbe_op_store_adapter.cc][LINE:1069]
        [SubGraphOpt][Compile][ParalCompOp] Thread[281472123728288] process fail task failed[FUNC:ParallelCompileOp][FILE:tbe_op_store_adapter.cc][LINE:1116]
        [SubGraphOpt][Compile][CompOpOnly] CompileOp failed.[FUNC:CompileOpOnly][FILE:op_compiler.cc][LINE:1190]
        [GraphOpt][FusedGraph][RunCompile] Failed to compile graph with compiler Normal mode Op Compiler[FUNC:SubGraphCompile][FILE:fe_graph_optimizer.cc][LINE:1410]
        Call OptimizeFusedGraph failed, ret:4294967295, engine_name:AIcoreEngine, graph_name:partition0_rank1_new_sub_graph1[FUNC:OptimizeSubGraph][FILE:graph_optimize.cc][LINE:119]
        subgraph 0 optimize failed[FUNC:OptimizeSubGraphWithMultiThreads][FILE:graph_manager.cc][LINE:815]
        build graph failed, graph id:1, ret:4294967295[FUNC:BuildModelWithGraphId][FILE:ge_generator.cc][LINE:1618]
        [Build][SingleOpModel]call ge interface generator.BuildSingleOpModel failed. ge result = 4294967295[FUNC:ReportCallError][FILE:log_inner.cpp][LINE:161]
        [Build][Op]Fail to build op model[FUNC:ReportInnerError][FILE:log_inner.cpp][LINE:145]
        build op model failed, result = 500002[FUNC:ReportInnerError][FILE:log_inner.cpp][LINE:145]

>>> 
```

The environment
```
(torch) [HwHiAiUser@ec24358c0133 aarch64-openEuler-linux]$ cat /etc/os-release
NAME="openEuler"
VERSION="20.03 (LTS-SP2)"
ID="openEuler"
VERSION_ID="20.03"
PRETTY_NAME="openEuler 20.03 (LTS-SP2)"
ANSI_COLOR="0;31"

(torch) [HwHiAiUser@ec24358c0133 aarch64-openEuler-linux]$ python -V
Python 3.10.0

(torch) [HwHiAiUser@ec24358c0133 aarch64-openEuler-linux]$ pip list
Package                Version
---------------------- ------------
absl-py                2.1.0
addict                 2.4.0
attr                   0.3.2
attrs                  24.2.0
auto_tune              0.1.0
certifi                2024.8.30
charset-normalizer     3.4.0
contourpy              1.2.0
cycler                 0.12.1
Cython                 3.0.11
dataflow               0.0.1
decorator              5.1.1
filelock               3.18.0
fonttools              4.55.0
fsspec                 2025.3.2
grpcio                 1.68.0
grpcio-tools           1.68.0
hccl                   0.1.0
hccl_parser            0.1
hf-xet                 1.1.5
huggingface-hub        0.33.4
idna                   3.10
importlib_metadata     8.7.0
importlib_resources    6.4.5
Jinja2                 3.1.6
kiwisolver             1.4.7
llm_datadist           0.0.1
MarkupSafe             3.0.2
matplotlib             3.9.2
mmcv                   1.7.0
mpmath                 1.3.0
msobjdump              0.1.0
networkx               3.2.1
numpy                  1.26.4
op_compile_tool        0.1.0
op_gen                 0.1
op_test_frame          0.1
opc_tool               0.1.0
opencv-python          4.11.0.86
packaging              24.2
pathlib2               2.3.7.post1
pillow                 11.0.0
pip                    25.1
platformdirs           4.3.7
protobuf               5.29.5
psutil                 6.1.0
pycocotools            2.0.8
pycparser              2.22
pyparsing              3.2.0
python-dateutil        2.9.0.post0
PyYAML                 6.0.2
regex                  2024.11.6
requests               2.32.3
safetensors            0.5.3
schedule_search        0.0.1
scipy                  1.13.1
setuptools             78.1.1
show_kernel_debug_data 0.1.0
six                    1.16.0
sympy                  1.4
te                     0.4.0
tokenizers             0.21.2
tomli                  2.2.1
torch                  2.1.0
torch-npu              2.1.0.post10
tqdm                   4.67.1
transformers           4.53.3
typing_extensions      4.13.2
urllib3                2.2.3
wheel                  0.45.1
yapf                   0.40.1
zipp                   3.21.0

(torch) [HwHiAiUser@ec24358c0133 latest]$ cat /usr/local/Ascend/ascend-toolkit/latest/aarch64-linux/ascend_toolkit_install.info
package_name=Ascend-cann-toolkit
version=8.0.0
innerversion=V100R001C20SPC001B251
compatible_version=[V100R001C15],[V100R001C17],[V100R001C18],[V100R001C19],[V100R001C20]
arch=aarch64
os=linux
path=/usr/local/Ascend/ascend-toolkit/8.0.0/aarch64-linux


(torch) [HwHiAiUser@ec24358c0133 latest]$ gcc -v
Using built-in specs.
COLLECT_GCC=gcc
COLLECT_LTO_WRAPPER=/usr/libexec/gcc/aarch64-openEuler-linux/12/lto-wrapper
GCC_AI4C_ONNX_FDATA=/usr/libexec/gcc/aarch64-openEuler-linux/12/../../onnx.fdata
Target: aarch64-openEuler-linux
Configured with: ../configure --disable-libgcj --without-cloog --enable-languages=c,c++,fortran,objc,obj-c++,lto --prefix=/usr --mandir=/usr/share/man --infodir=/usr/share/info --with-bugurl=https://gitee.com/src-openeuler/gcc/issues --enable-shared --enable-threads=posix --enable-checking=release --enable-multilib --with-system-zlib --enable-__cxa_atexit --disable-libunwind-exceptions --enable-gnu-unique-object --enable-linker-build-id --with-gcc-major-version-only --enable-libstdcxx-backtrace --with-linker-hash-style=gnu --enable-plugin --enable-initfini-array --without-isl --enable-gnu-indirect-function --with-multilib-list=lp64 --enable-bolt --build=aarch64-openEuler-linux
Thread model: posix
Supported LTO compression algorithms: zlib
gcc version 12.3.1 (openEuler 12.3.1-81.oe2503) (GCC) 
(torch) [HwHiAiUser@ec24358c0133 latest]$ g++ -v
Using built-in specs.
COLLECT_GCC=g++
COLLECT_LTO_WRAPPER=/usr/libexec/gcc/aarch64-openEuler-linux/12/lto-wrapper
GCC_AI4C_ONNX_FDATA=/usr/libexec/gcc/aarch64-openEuler-linux/12/../../onnx.fdata
Target: aarch64-openEuler-linux
Configured with: ../configure --disable-libgcj --without-cloog --enable-languages=c,c++,fortran,objc,obj-c++,lto --prefix=/usr --mandir=/usr/share/man --infodir=/usr/share/info --with-bugurl=https://gitee.com/src-openeuler/gcc/issues --enable-shared --enable-threads=posix --enable-checking=release --enable-multilib --with-system-zlib --enable-__cxa_atexit --disable-libunwind-exceptions --enable-gnu-unique-object --enable-linker-build-id --with-gcc-major-version-only --enable-libstdcxx-backtrace --with-linker-hash-style=gnu --enable-plugin --enable-initfini-array --without-isl --enable-gnu-indirect-function --with-multilib-list=lp64 --enable-bolt --build=aarch64-openEuler-linux
Thread model: posix
Supported LTO compression algorithms: zlib
gcc version 12.3.1 (openEuler 12.3.1-81.oe2503) (GCC) 

 

(base) [root@ec24358c0133 12]#npu-smi info
+--------------------------------------------------------------------------------------------------------+
| npu-smi 24.1.rc3.1                               Version: 24.1.rc3.1                                   |
+-------------------------------+-----------------+------------------------------------------------------+
| NPU     Name                  | Health          | Power(W)     Temp(C)           Hugepages-Usage(page) |
| Chip    Device                | Bus-Id          | AICore(%)    Memory-Usage(MB)                        |
+===============================+=================+======================================================+
| 96      310P3                 | OK              | NA           46                0     / 0             |
| 0       0                     | 0000:04:00.0    | 0            1836 / 21527                            |
+===============================+=================+======================================================+
+-------------------------------+-----------------+------------------------------------------------------+
| NPU     Chip                  | Process id      | Process name             | Process memory(MB)        |
+===============================+=================+======================================================+
| No running processes found in NPU 96                                                                   |
+===============================+=================+======================================================+
```

Troubleshooting completed：
1. Confirmed that the versions of gcc and g++ are consistent and unique.
2. Verified that the cstdint header file exists in the gcc include directory.
```
(base) [root@ec24358c0133 12]# ll /usr/include/c++/12/cstdint
-rw-r--r--. 1 root root 2.3K Mar 20 04:13 /usr/include/c++/12/cstdint
```

## 评论 (1)

### unknowed-ER · 2025-07-23

I fix it by settting env manually.
```
export C_INCLUDE_PATH=/usr/local/Ascend/ascend-toolkit/latest/toolkit/toolchain/hcc/aarch64-target-linux-gnu/include/c++/7.3.0/:/usr/local/Ascend/ascend-toolkit/latest/toolkit/toolchain/hcc/aarch64-target-linux-gnu/include/c++/7.3.0/aarch64-target-linux-gnu/
export CPLUS_INCLUDE_PATH=/usr/local/Ascend/ascend-toolkit/latest/toolkit/toolchain/hcc/aarch64-target-linux-gnu/include/c++/7.3.0/:/usr/local/Ascend/ascend-toolkit/latest/toolkit/toolchain/hcc/aarch64-target-linux-gnu/include/c++/7.3.0/aarch64-target-linux-gnu/
```

