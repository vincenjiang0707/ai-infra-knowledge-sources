# [Issue #2280] [Question]: Clarify NCCL_SYM_CTAS

source: https://github.com/NVIDIA/nccl/issues/2280
state: closed | updated: 2026-08-10T00:33:53Z
labels: question

## 正文

### Question

Hi NCCL team,

We tried  NCCL_SYM_CTAS  with symmetric buffer registration ( all_reduce_perf -R 2 ) on GB200 systems and found that it works: setting  NCCL_SYM_CTAS=32  or  64  changes the selected symmetric-kernel  nchannels  and affects performance.

The NCCL version reported by  nccl-tests  is:

NCCL version 2.30.3+cuda13.0
nccl-tests version 2.19.1
nccl-headers=23003
nccl-library=23003

However, I could not find  NCCL_SYM_CTAS  in the public NCCL environment-variable docs. I only found it in source:

NCCL_PARAM(SymCTAs, "SYM_CTAS", 0)

Could you clarify whether  NCCL_SYM_CTAS  is intended to be user-facing, and how it relates to  NCCL_MIN_CTAS  /  NCCL_MAX_CTAS ?

Thanks!

## 评论 (3)

### sjeaugey · 2026-07-09

Some environment variables can be set for system configuration and documented as such in the user guide. Typically the system admin would provide that configuration.

Other environment variables should not be used in production, except for temporary workarounds of known issues. That's because changing default values means you run in a configuration which is not well tested and could lead to bugs.

We may also change the way environment variables work from one version to another, or remove environment variables entirely. Environment variables are not the NCCL API. the NCCL API has compatibility guarantees. Environment variables do not have that guarantee.

In particular for tuning, environment variables can cause more harm than good in the long term. If you find that changing a default setting makes your application faster, great, but keep in mind you may need to re-assess that on every new version. Otherwise, that same env var may actually hurt performance in future versions, or on future platforms. We see a lot of users set those in their scripts and carry their scripts forward on next gen systems. This is a recipe for trouble. In particular, we see a lot of users try to set a lot of env vars, only to come back to their default settings, but leave them in their scripts. For example, something like: `NCCL_NET_GDR_LEVEL=PHB NCCL_ALGO=RING,TREE NCCL_IB_DISABLE=0` which could be what works best for them on their current platform. But if tomorrow you run on a different platform with a newer NCCL, we may need to change the GDR level for better performance, or we may add new algorithms which you won't be able to use, or use a new internal plugin for communication, and disable the IB plugin by default on that platform -- all of which could be defeated by the above example.

Back to NCCL_SYM_CTAS, this could change or even disappear in future versions. We're thinking about unifying the symmetric kernels with the general ones, and that could imply a full rework of those environment variables. So, use it at your own risk on the current version of NCCL, but do not assume those will still be there (or have the same effect) in the long term. If you want to use them for experiments, to analyse NCCL performance, or for development purposes, no problem, that's what they're here for: NCCL developers. Not users, hence that's why they may not be in the user guide.

Also note that there is a proper NCCL API to control the number of SMs we use. The comm config has `minCTAs` and `maxCTAs` fields which should affect all cases.

### xiaofanl-nvidia · 2026-08-10

@baiwei0427 I'm closing this given that we haven't heard from you for 1 month. We assume your original question has been answered. Please open a new issue if you have any follow-up question. 

### baiwei0427 · 2026-08-10

Thank you for the detailed answer! This confirms what I needed to know.
