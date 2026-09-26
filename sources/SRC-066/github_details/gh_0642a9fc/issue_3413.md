# [Issue #3413] [BUG] Using CuTe DSL in REPL crashes Python

source: https://github.com/NVIDIA/cutlass/issues/3413
state: closed | updated: 2026-09-22T06:42:42Z
labels: bug, ? - Needs Triage, inactive-30d, CuTe DSL

## 正文

### Which component has the problem?

CuTe DSL

### Bug Report

**Describe the bug**
Trying to use CuTe DSL in the Python REPL causes an `[Internal Error]` and crashes the interpreter.

**Steps/Code to reproduce bug**
```
$ CUTE_DSL_SHOW_STACKTRACE=1 python3
Python 3.12.3 (main, Jun 19 2026, 12:46:00) [GCC 13.3.0] on linux
Type "help", "copyright", "credits" or "license" for more information.
>>> from cutlass import cute
>>> @cute.jit
... def run(f):
...     f()
...
>>> run(lambda: 0); print("ran")
Traceback (most recent call last):
  File "/usr/local/lib/python3.12/dist-packages/nvidia_cutlass_dsl/dsl_packages/cutlass/base_dsl/ast_preprocessor.py", line 764, in transform_function
    lines, start_line = inspect.getsourcelines(function_pointer)
                        ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/usr/lib/python3.12/inspect.py", line 1260, in getsourcelines
    lines, lnum = findsource(object)
                  ^^^^^^^^^^^^^^^^^^
  File "/usr/lib/python3.12/inspect.py", line 1089, in findsource
    raise OSError('could not get source code')
OSError: could not get source code

During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
  File "/usr/local/lib/python3.12/dist-packages/nvidia_cutlass_dsl/dsl_packages/cutlass/base_dsl/dsl.py", line 866, in jit_wrapper
    BaseDSL._preprocess_and_replace_code(func)
  File "/usr/local/lib/python3.12/dist-packages/nvidia_cutlass_dsl/dsl_packages/cutlass/base_dsl/dsl.py", line 833, in _preprocess_and_replace_code
    fcn_ptr = func._dsl_object.run_preprocessor(
              ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/usr/local/lib/python3.12/dist-packages/nvidia_cutlass_dsl/dsl_packages/cutlass/base_dsl/dsl.py", line 2372, in run_preprocessor
    return self._run_preprocessor_impl(
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/usr/local/lib/python3.12/dist-packages/nvidia_cutlass_dsl/dsl_packages/cutlass/base_dsl/dsl.py", line 2388, in _run_preprocessor_impl
    transformed_ast = preprocessor_session.transform(
                      ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/usr/local/lib/python3.12/dist-packages/nvidia_cutlass_dsl/dsl_packages/cutlass/base_dsl/ast_preprocessor.py", line 1016, in transform
    transformed_tree = self.transform_function(
                       ^^^^^^^^^^^^^^^^^^^^^^^^
  File "/usr/local/lib/python3.12/dist-packages/nvidia_cutlass_dsl/dsl_packages/cutlass/base_dsl/ast_preprocessor.py", line 790, in transform_function
    raise DSLRuntimeError(
cutlass.base_dsl.common.DSLRuntimeError:
[Internal Error] The compiler hit a problem it could not trace back to your code.
This is a bug in the DSL, not a mistake in your kernel.

Detail: Failed to parse function run

What to do:
  Please report this with the snippet above and your kernel.
  Re-run with CUTE_DSL_SHOW_STACKTRACE=1 to include the full technical detail.

====================================================================================================
$ 
```


**Expected behavior**
I would expect either a successful run or a clear error message, whichever is the intended behavior in this case. In either case, Python shouldn't crash.

**Environment details (please complete the following information):**
 - Environment location: [Docker] 

**Additional context**
No additional context.


## 评论 (2)

### github-actions[bot] · 2026-08-27

This issue has been labeled `inactive-30d` due to no recent activity in the past 30 days. Please close this issue if no further response or action is needed. Otherwise, please respond with a comment indicating any updates or changes to the original issue and/or confirm this issue still needs to be addressed. This issue will be labeled `inactive-90d` if there is no activity in the next 60 days.

### brandon-yujie-sun · 2026-09-22

For record, this landed in 4.8
