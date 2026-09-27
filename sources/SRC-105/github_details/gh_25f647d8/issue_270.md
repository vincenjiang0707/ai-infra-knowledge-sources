# [Issue #270] dcgmi health check error,but temp is ok

source: https://github.com/NVIDIA/DCGM/issues/270
state: open | updated: 2025-12-30T03:35:48Z
labels: 

## 正文

**I want to know the reason why temp not high 75°C，but dcgm health log has slowdown？**
This is dcgm error message:
`ERROR [1514002:1514004] [[Health]] Detected a WARNING in health system Thermal: 'Detected clocks event due to thermal violation in GPU 2. Verify that the cooling on this machine is functional, including external, thermal material interface, fans, and any other components.`

## 评论 (1)

### WaterAndBread · 2025-12-30

The fan might not be installed
