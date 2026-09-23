source: https://docs.vllm.ai/en/latest/api/vllm/compilation/passes/fusion/matcher_utils/
lastmod: 2026-09-23

#

`vllm.compilation.passes.fusion.matcher_utils`

[¶](https://docs.vllm.ai#vllm.compilation.passes.fusion.matcher_utils)

Classes:

-
–[MatcherCustomOp](https://docs.vllm.ai#vllm.compilation.passes.fusion.matcher_utils.MatcherCustomOp) -
–[MatcherRMSNormGated](https://docs.vllm.ai#vllm.compilation.passes.fusion.matcher_utils.MatcherRMSNormGated)Matches RMSNormGated with norm_before_gate=True and group_size=None.


##

`MatcherCustomOp`

[¶](https://docs.vllm.ai#vllm.compilation.passes.fusion.matcher_utils.MatcherCustomOp)

Bases: [ABC](https://docs.python.org/3/library/abc.html#abc.ABC)

Methods:

-
–[inputs](https://docs.vllm.ai#vllm.compilation.passes.fusion.matcher_utils.MatcherCustomOp.inputs)Utility for inputs to the pattern.


## Source code in `vllm/compilation/passes/fusion/matcher_utils.py`


##

`MatcherRMSNormGated`

[¶](https://docs.vllm.ai#vllm.compilation.passes.fusion.matcher_utils.MatcherRMSNormGated)

Bases: [MatcherCustomOp](https://docs.vllm.ai#vllm.compilation.passes.fusion.matcher_utils.MatcherCustomOp)

Matches RMSNormGated with norm_before_gate=True and group_size=None.