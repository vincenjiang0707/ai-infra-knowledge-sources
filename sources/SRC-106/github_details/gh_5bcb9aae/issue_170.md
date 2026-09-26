# [Issue #170] amdsmi_cli/amdsmi_init.py: Wrong amdgpu module detection when module is built-in

source: https://github.com/ROCm/amdsmi/issues/170
state: closed | updated: 2026-02-05T18:59:47Z
labels: status: triage

## 正文

In file: https://github.com/ROCm/amdsmi/blob/b5522cc8141a7241b22bebab639851074463f00f/amdsmi_cli/amdsmi_init.py#L57

If the amdgpu kernel module is built-in, then the file `sys/module/amdgpu/initstate` does not exist, and `amd-smi` exits with an error.



## 评论 (4)

### darren-amd · 2026-01-14

Hi @rx80,

Thanks for reporting this issue! What ROCm version are you on? Could I have some more details on the error as well as how you are reproducing this issue to investigate further.

### rx80 · 2026-01-14

> Hi [@rx80](https://github.com/rx80),
> 
> Thanks for reporting this issue! What ROCm version are you on? Could I have some more details on the error as well as how you are reproducing this issue to investigate further.

I've been using 7.1 and testing out 7.10. However this problematic code has been the same for 3 years: https://github.com/ROCm/amdsmi/blame/b5522cc8141a7241b22bebab639851074463f00f/amdsmi_cli/amdsmi_init.py#L57

The issue is that if the amdgpu kernel module is built into the kernel (not a loadable module), then the `initstate` file does not exist.

Since the file does not exist, the python code in `amdsmi_init.py` raises an exception and amd-smi reports an error.

This little patch fixes the error and `amd-smi` runs correctly:

```patch
--- a/amdsmi_cli/amdsmi_init.py
+++ b/amdsmi_cli/amdsmi_init.py
@@ -58,6 +58,8 @@
     if amd_gpu_status_file.exists():
         if amd_gpu_status_file.read_text(encoding="ascii").strip() == "live":
             return True
+    elif Path("/sys/module/amdgpu").exists():
+        return True
     return False
```



### darren-amd · 2026-01-19

Thanks @rx80, I'm going to check with the internal team on how we want to address this issue and get back to you.

### darren-amd · 2026-02-05

Hi @rx80,

This has been fixed with: https://github.com/ROCm/rocm-systems/pull/2689, thanks for the report!
