# [Issue #4459] [Issue] lmdeploy 0.12.2 has a dependency to 'tilelang'

source: https://github.com/InternLM/lmdeploy/issues/4459
state: closed | updated: 2026-04-07T09:09:00Z
labels: 

## 正文

I see that lmdeploy version 0.12.2 has introduced a dependency to the 'tilelang' package. 
This wasn't the case with version 0.12.1.

The problem is, 'tilelang' is very painful to build on Windows, and furthermore its 'compile' function demands that a C++ compiler is present on the system (wich cannot be assumed on a Windows system).

Is there a new component in 'lmdeploy' which absolutely needs 'tilelang' ?
Otherwise, it might be good to get rid of that dependency.

## 评论 (4)

### lvhan028 · 2026-03-26

Thank you for bringing this to our attention.
We can add a platform condition for tilelang installation, similar to how we handle triton.
```
triton<=3.6.0,>=3.0.0; sys_platform == "linux" and "aarch64" not in platform_machine and "arm" not in platform_machine
```

### hfassold · 2026-03-26

Thanks 

### davidfungf · 2026-04-07

I meet the same issue during the installation of 'tilelang' on Windows. Is it fixed?

### lvhan028 · 2026-04-07

@davidfungf Yes. You can build lmdeploy from source using latest main
