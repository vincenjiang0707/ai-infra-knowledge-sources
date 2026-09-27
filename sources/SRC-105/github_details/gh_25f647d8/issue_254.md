# [Issue #254] pcie diagnostic fails on driver 580 with CUDA 12 support packages

source: https://github.com/NVIDIA/DCGM/issues/254
state: open | updated: 2026-01-23T17:25:52Z
labels: 

## 正文

We are using DCGM 4.4.1 on V100 and driver 580.65.06. The Pre-Requisites part of the Getting Started section in the DCGM user guide suggests to install DCGM's CUDA 12 support packages for Volta units "rather than DCGM packages targeting major version 13", even when using driver 580. However, in our experience, the pcie diagnostic always fails in this constellation:

```
$ dcgmi diag -i 0,1,2,3 -v -r 2
+---------------------------+------------------------------------------------+                                                                                                                                                               
| Diagnostic                | Result                                         |                                                                                                                                                               
+===========================+================================================+                                                                                                                                                               
|-----  Metadata  ----------+------------------------------------------------|                                        
| DCGM Version              | 4.4.1                                          |                                                                                                                                                               
| Driver Version Detected   | 580.65.06                                      |                                        
| GPU Device IDs Detected   | 1db1, 1db1, 1db1, 1db1                         |                                                                                                                                                               
...
+-----  Integration  -------+------------------------------------------------+
| pcie                      | Fail                                           |
| Warning                   | There was an internal error during the test:   |
|                           | 'A child process (2378806) exited with non-ze  |
|                           | ro status 1' Check DCGM and system logs for e  |
|                           | rrors. Reset GPU. Restart DCGM. Rerun diagnos  |
|                           | tics.                                          |
```

Inspecting the logs, we find that the diagnostic tries to run a helper program that is part of the CUDA 13 support packages:

```
2025-09-08 08:20:25.436 DEBUG [2378729:2378729] [[pcie]] External command stdout: Could not exec '/usr/libexec/datacenter-gpu-manager-4/plugins/cuda13/BwChecker_13'. Error: (2) No such file or directory
```

If we install the CUDA 13 support packages in addition to the CUDA 12 support packages, the pcie diagnostic passes. However, that doubles the installation footprint, since the CUDA 12 support packages also seem to be necessary, at least on V100. Here is what happens if we remove the CUDA 12 support packages:

```
$ dcgmi diag -i 0,1,2,3 -v -r 3
Error: Unable to complete diagnostic for entities 0,1,2,3. Return: (-30) : DCGM GPU Diagnostic returned an error
Error: Cannot load plugins. Unable to change to the plugin dir '/usr/libexec/datacenter-gpu-manager-4/plugins/cuda12/': 'No such file or directory'
```

It seems like in general, DCGM special cases Volta and requires the CUDA 12 support packages on that architecture even on driver R580, but that logic does not extend to the pcie diagnostic which additionally requires the CUDA 13 support packages.

## 评论 (1)

### ColtonPaul · 2026-01-23

This still occurs on DCGM 4.4.2 (on V100 + driver 580.105.08).
