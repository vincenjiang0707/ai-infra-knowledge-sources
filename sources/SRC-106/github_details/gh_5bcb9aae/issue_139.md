# [Issue #139] `power_limit` vs. `power_cap`

source: https://github.com/ROCm/amdsmi/issues/139
state: closed | updated: 2025-11-19T05:49:37Z
labels: status: triage

## 正文

Hi, I was just wondering how the two things are different:
- `amdsmi_get_power_info(handle)["power_limit"]`
- `amdsmi_get_power_cap_info(handle)["power_cap"]`

Which one aligns best with `nvmlDeviceGetPowerManagementLimit`?

## 评论 (4)

### adityas-amd · 2025-11-17

power_cap returned by `amdsmi_get_power_cap_info()` is closer to `nvmlDeviceGetPowerManagementLimit()`
it uses `rsmi_dev_power_cap_get`, that reports the actual enforced power management limit (along with min/max/default values) https://github.com/ROCm/amdsmi/blob/4ff9527d41f581ce9399201f5129d1f348fe06cf/src/amd_smi/amd_smi.cc#L3515C1-L3555C2
In contrast, `amdsmi_get_power_info()->power_limit` calls smi_amdgpu_get_power_cap() with sensor index 0 and doesn’t expose the full power-cap configuration.https://github.com/ROCm/amdsmi/blob/4ff9527d41f581ce9399201f5129d1f348fe06cf/src/amd_smi/amd_smi.cc#L4544-L4593

### jaywonchung · 2025-11-17

Thanks @adityas-amd! Right, I was curious about sensor indices as well.

`amdsmi_set_power_cap` requires us to pass a sensor index as well.

If I were to make it behave like `nvmlDeviceSetPowerManagementLimit`, should I be calling `amdsmi_set_power_cap` once for each available sensor index? Or, does sensor 0 hit the core compute part?

### adityas-amd · 2025-11-19

just use sensor index 0, you do not need to set every sensor index

On AMD GPUs, sensor 0 corresponds to the primary power-cap domain (used internally for enforcing the board power limit). 

### jaywonchung · 2025-11-19

Thanks!
