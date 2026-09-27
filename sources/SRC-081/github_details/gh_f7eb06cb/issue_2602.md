# [Issue #2602] GPTQModel should not change the seed

source: https://github.com/ModelCloud/GPTQModel/issues/2602
state: closed | updated: 2026-03-24T18:37:23Z
labels: 

## 正文

I think these lines should be removed:

https://github.com/ModelCloud/GPTQModel/blob/775d49b1576beea2b19801c334fcfc8892944792/gptqmodel/models/auto.py#L159-L162

Otherwise, setting a seed for reproducibility is useless as GPTQModel will just globally override it. If you need a fixed seed, please create an RNG instance and use that. It cost me 5 hours to debug why my script was not reproducible.

## 评论 (3)

### Qubitium · 2026-03-24

@BenjaminBossan Sorry. I think we were using to make our own ci tests (`generation`) more stable. But in your case, you had another wrapper/env outside that also did fixed `seeds`? lol. Sorry about that. Will fix. 

### BenjaminBossan · 2026-03-24

Thanks for the quick update.

### Qubitium · 2026-03-24

@BenjaminBossan  Please avoid using `main` right now.  There is a lot of refractoring going on and currently unstable. Hopefully in a few days I can get things sorted and ci are clear again. 
