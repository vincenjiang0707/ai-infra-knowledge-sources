# [Issue #12] [Issue]: amdsmi does not work on Windows due to missing dll

source: https://github.com/ROCm/amdsmi/issues/12
state: closed | updated: 2024-04-26T16:05:50Z
labels: 

## 正文

### Problem Description

I ran `amdsmi.exe` on Windows, but it cannot load the dynamic lib because it's missing:

```
PS C:\Windows\System32> .\amdsmi.exe --version
Traceback (most recent call last):
  File "PyInstaller\loader\pyimod03_ctypes.py", line 53, in __init__
  File "ctypes\__init__.py", line 376, in __init__
FileNotFoundError: Could not find module 'libsmi_host.dll' (or one of its dependencies). Try using the full path with constructor syntax.

The above exception was the direct cause of the following exception:

Traceback (most recent call last):
  File "main.py", line 25, in <module>
  File "<frozen importlib._bootstrap>", line 1178, in _find_and_load
  File "<frozen importlib._bootstrap>", line 1149, in _find_and_load_unlocked
  File "<frozen importlib._bootstrap>", line 690, in _load_unlocked
  File "PyInstaller\loader\pyimod02_importers.py", line 352, in exec_module
  File "exceptions.py", line 22, in <module>
  File "<frozen importlib._bootstrap>", line 1178, in _find_and_load
  File "<frozen importlib._bootstrap>", line 1149, in _find_and_load_unlocked
  File "<frozen importlib._bootstrap>", line 690, in _load_unlocked
  File "PyInstaller\loader\pyimod02_importers.py", line 352, in exec_module
  File "amdsmi_import\__init__.py", line 73, in <module>
  File "<frozen importlib._bootstrap>", line 1178, in _find_and_load
  File "<frozen importlib._bootstrap>", line 1149, in _find_and_load_unlocked
  File "<frozen importlib._bootstrap>", line 690, in _load_unlocked
  File "PyInstaller\loader\pyimod02_importers.py", line 352, in exec_module
  File "amdsmi_import\amdsmi_host\gpuvsmi_package\amdsmi\__init__.py", line 24, in <module>
  File "<frozen importlib._bootstrap>", line 1178, in _find_and_load
  File "<frozen importlib._bootstrap>", line 1149, in _find_and_load_unlocked
  File "<frozen importlib._bootstrap>", line 690, in _load_unlocked
  File "PyInstaller\loader\pyimod02_importers.py", line 352, in exec_module
  File "amdsmi_import\amdsmi_host\gpuvsmi_package\amdsmi\smi_interface.py", line 30, in <module>
  File "<frozen importlib._bootstrap>", line 1178, in _find_and_load
  File "<frozen importlib._bootstrap>", line 1149, in _find_and_load_unlocked
  File "<frozen importlib._bootstrap>", line 690, in _load_unlocked
  File "PyInstaller\loader\pyimod02_importers.py", line 352, in exec_module
  File "amdsmi_import\amdsmi_host\gpuvsmi_package\amdsmi\smi_wrapper.py", line 160, in <module>
  File "PyInstaller\loader\pyimod03_ctypes.py", line 55, in __init__
pyimod03_ctypes.install.<locals>.PyInstallerImportError: Failed to load dynlib/dll 'libsmi_host.dll'. Most likely this dynlib/dll was not found when the application was frozen.
[24972] Failed to execute script 'main' due to unhandled exception!
```

Instead, there are only `libamdsmi_host.dll` and `libamdsmi_guest.dll`:
![image](https://github.com/ROCm/amdsmi/assets/8311300/88cc1bea-7c12-411e-bd5f-831b6e8a44b0)

If I copied and rename the `libamdsmi_host.dll` to `libsmi_host.dll`, it raises another error:

```
PS C:\Windows\System32> .\amdsmi.exe --version
Traceback (most recent call last):
  File "main.py", line 25, in <module>
  File "<frozen importlib._bootstrap>", line 1178, in _find_and_load
  File "<frozen importlib._bootstrap>", line 1149, in _find_and_load_unlocked
  File "<frozen importlib._bootstrap>", line 690, in _load_unlocked
  File "PyInstaller\loader\pyimod02_importers.py", line 352, in exec_module
  File "exceptions.py", line 22, in <module>
  File "<frozen importlib._bootstrap>", line 1178, in _find_and_load
  File "<frozen importlib._bootstrap>", line 1149, in _find_and_load_unlocked
  File "<frozen importlib._bootstrap>", line 690, in _load_unlocked
  File "PyInstaller\loader\pyimod02_importers.py", line 352, in exec_module
  File "amdsmi_import\__init__.py", line 73, in <module>
  File "<frozen importlib._bootstrap>", line 1178, in _find_and_load
  File "<frozen importlib._bootstrap>", line 1149, in _find_and_load_unlocked
  File "<frozen importlib._bootstrap>", line 690, in _load_unlocked
  File "PyInstaller\loader\pyimod02_importers.py", line 352, in exec_module
  File "amdsmi_import\amdsmi_host\gpuvsmi_package\amdsmi\__init__.py", line 24, in <module>
  File "<frozen importlib._bootstrap>", line 1178, in _find_and_load
  File "<frozen importlib._bootstrap>", line 1149, in _find_and_load_unlocked
  File "<frozen importlib._bootstrap>", line 690, in _load_unlocked
  File "PyInstaller\loader\pyimod02_importers.py", line 352, in exec_module
  File "amdsmi_import\amdsmi_host\gpuvsmi_package\amdsmi\smi_interface.py", line 30, in <module>
  File "<frozen importlib._bootstrap>", line 1178, in _find_and_load
  File "<frozen importlib._bootstrap>", line 1149, in _find_and_load_unlocked
  File "<frozen importlib._bootstrap>", line 690, in _load_unlocked
  File "PyInstaller\loader\pyimod02_importers.py", line 352, in exec_module
  File "amdsmi_import\amdsmi_host\gpuvsmi_package\amdsmi\smi_wrapper.py", line 1686, in <module>
  File "ctypes\__init__.py", line 389, in __getattr__
  File "ctypes\__init__.py", line 394, in __getitem__
AttributeError: function 'gpuvsmi_init' not found
[27576] Failed to execute script 'main' due to unhandled exception!
```

### Operating System

Windows 10.0.22631

### CPU

AMD Ryzen 7 5800X 8-Core Processor

### GPU

AMD Radeon Pro W6800

### ROCm Version

ROCm 5.7.1

### ROCm Component

amdsmi

### Steps to Reproduce

_No response_

### (Optional for Linux users) Output of /opt/rocm/bin/rocminfo --support

_No response_

### Additional Information

My AMD GPU driver version info are:
```
Driver version
23.30.16-231128a-398955E-INTERNAL-AMD-Software-PRO-Edition
AMD Windows Driver version
31.0.23016.5
```

Hope this helps

## 评论 (3)

### Inokinoki · 2024-03-02

There are some similar symbols:

```
strings /mnt/c/Windows/System32/libamdsmi_host.dll | grep "smi"
libamdsmi_host.dll
amdsmi_event_create
amdsmi_event_destroy
amdsmi_event_read
amdsmi_get_clock_info
amdsmi_get_dfc_fw_table
amdsmi_get_fb_layout
amdsmi_get_fw_error_records
amdsmi_get_fw_info
amdsmi_get_gpu_activity
amdsmi_get_gpu_asic_info
amdsmi_get_gpu_bad_page_info
amdsmi_get_gpu_board_info
amdsmi_get_gpu_device_bdf
amdsmi_get_gpu_device_uuid
amdsmi_get_gpu_driver_version
amdsmi_get_gpu_ras_feature_info
amdsmi_get_gpu_total_ecc_count
amdsmi_get_gpu_vbios_info
amdsmi_get_guest_data
amdsmi_get_num_vf
amdsmi_get_partition_profile_info
amdsmi_get_pcie_link_caps
amdsmi_get_pcie_link_status
amdsmi_get_power_cap_info
amdsmi_get_power_info
amdsmi_get_processor_handle_from_bdf
amdsmi_get_processor_handles
amdsmi_get_processor_type
amdsmi_get_socket_handles
amdsmi_get_socket_info
amdsmi_get_temp_metric
amdsmi_get_vf_bdf
amdsmi_get_vf_data
amdsmi_get_vf_fw_info
amdsmi_get_vf_handle_from_bdf
amdsmi_get_vf_handle_from_idx
amdsmi_get_vf_info
amdsmi_get_vf_partition_info
amdsmi_get_vf_uuid
amdsmi_get_xgmi_info
amdsmi_init
amdsmi_shut_down
```
Are the APIs renamed?

### dmitrii-galantsev · 2024-03-07

@marifamd any clue?

### dmitrii-galantsev · 2024-04-26

Had some internal discussions and confirmed that "AMD SMI for Windows is not supported officially on consumer cards".

We are planning testing and improved support in the future.
