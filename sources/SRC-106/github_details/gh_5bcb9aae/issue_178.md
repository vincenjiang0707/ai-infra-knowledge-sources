# [Issue #178] [Feature]: Make future versions of amdsmi C library backward-compatible

source: https://github.com/ROCm/amdsmi/issues/178
state: closed | updated: 2026-03-11T14:30:48Z
labels: Feature Request, status: triage

## 正文

### Suggestion Description

While amdsmi is relatively stable, its API and ABI have been broken several times (e.g. by adding fields to a structure, by changing the parameters of functions, etc.). This is worrisome for building software with it, because it makes supporting multiple versions of ROCm much harder than it needs to be. In particular, using the new header with an older version of the amdsmi library installed on the node (or vice-versa) can lead to severe UB.

Would it be possible to provide backward-compatibility in the C library? I'm thinking about the following possibilities (they may be complimentary):
1. When a function or struct needs to change, _keep the old version intact_, and add a new one with a different name, e.g. `amdsmi_something_v2`. This is what NVML does, and it works quite well. Software can detect which functions are available at runtime, without risking undefined behavior.
2. Include more information in (new) structures to make them forward and backward-compatible, like in the Linux kernel. Example for a structure that is given as a parameter of a function:
```c
// v1
struct S {
    uint8_t size;
    uint32_t some_param;
};

// v2
struct S {
    uint8_t size;
    uint32_t some_param;
    uint32_t new_param; // new field, does nothing when set to zero
};

// structure initialization that works in v1 and v2
struct S params = {0}; // init everything to zero
params.size = sizeof(S); // set size
params.some_param = 1234;
function_that_uses_s(params);

// A "version" field could also be used, instead of storing the size.
```

### Operating System

_No response_

### GPU

_No response_

### ROCm Component

amdsmi

## 评论 (1)

### darren-amd · 2026-03-11

Hi @TheElectronWill,

Thanks for the detailed suggestion, I understand how ABI/API changes can make it difficult to support multiple ROCm versions. I had a chat with the amd-smi team and relayed your concerns. For minor version changes (7.1 -> 7.2), we try to maintain backward compatibility, including when extending APIs. However, for major version bumps such as ROCm 7 -> 8, there may be cases where breaking changes are unavoidable, but we'll publish guidance and deprecation notices in our documentation so users are adequately informed. We'll keep your suggestion in mind when making changes.
