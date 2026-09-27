# [Issue #184] DCGM Policy Violation Notification channel reporting too many PCIe violations on P5 instance type from AWS EC2 (H100)

source: https://github.com/NVIDIA/DCGM/issues/184
state: open | updated: 2025-12-30T07:16:46Z
labels: 

## 正文

Hi team,

We are observing PCIe violations on p5 happen consistently fromt the time the instance is launched.
We act on this with a terminate and replace instance logic, but that's an expensive operation timewise as well as the instance type being a P5 from EC2. Also, this is a default set threshold and can't be managed by client while subscribing to the policy.

Few asks:

Is there an upstream fix from Nvidia that is planned?
Is there any repercussion of temporarily not subscribing to this policy?
What would go wrong if we let the PCIe errors to keep happening silently?

## 评论 (5)

### nikkon-dev · 2024-08-20

Hi,

This is a known issue that will be resolved in an upcoming release. In short, this diagnostic didn’t correctly normalize the error rates to the PCIe generation throughput.

### haardm · 2025-03-10

Hello, checking if this issue still exists? I am still seeing too many PCIe detections sporadically on my hardware.

### nikkon-dev · 2025-03-11

@haardm, Could you clarify which FieldID you are monitoring or whether you are using health monitoring? I'd like to understand your use case better. It would also be helpful to see the nv-hostengine debug logs: restart nv-hostengine with the following arguments `nv-hostengine -f debug.log --log-level debug`.

We have indeed fixed the PCI error thresholds based on the PCI generation and expected throughput. However, I would like to know if the PCI generation is accurately detected on your system. 

### haardm · 2025-03-11

> FieldID

I didn't find a fieldID for PCI error policy condition https://github.com/NVIDIA/go-dcgm/blob/5f1fc9afaa3194d378193ffd8fc49a271e1afd5c/pkg/dcgm/policy.go#L181,L215

`policyCondition("PCI error")` this is what we subscribe to in our method that calls `ListenForPolicyViolations` [api](https://github.com/NVIDIA/go-dcgm/blob/5f1fc9afaa3194d378193ffd8fc49a271e1afd5c/pkg/dcgm/api.go#L108) 


I do see one for NvlinkPolicy tho, should we be using that to monitor PCI error?



### haardm · 2025-12-30

Hi @nikkon-dev , could you please confirm what is the best mode to proceed here? We still see quite high number of PCI warnings being reported in the H100 GPU.
