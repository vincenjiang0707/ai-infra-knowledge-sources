# [Issue #96] About the implentation of .cpu()

source: https://github.com/dropbox/hqq/issues/96
state: closed | updated: 2025-04-09T10:59:26Z
labels: 

## 正文

Thanks for your work, may I ask when you expect to implement the .cpu() method of HQQLinear? Or can you please briefly describe how to implement it, I can implement it myself and submit a PR:
https://github.com/mobiusml/hqq/blob/b1a7c0698b2c323bfa55a2b4a110c8f3636fade7/hqq/core/quantize.py#L563

## 评论 (2)

### mobicham · 2024-07-19

Thanks! It should be similar to `.cuda()` but instead would use `.to('cpu')`: https://github.com/mobiusml/hqq/blob/b1a7c0698b2c323bfa55a2b4a110c8f3636fade7/hqq/core/quantize.py#L472-L535
RIght now it is a mess because we support quantizing the scale/zero values and support offloading them to the cpu. 
I think in the future we are gonna remove this which should make things much easier: https://github.com/mobiusml/hqq/pull/93#issuecomment-2230605730

May I ask why would need the `.cpu()` call? If you just want to use `HQQLinear ` with cpu, you can just pass `HQQLinear(...device='cpu')` 

### mobicham · 2025-04-09

This is an old issue, already resolved. 
