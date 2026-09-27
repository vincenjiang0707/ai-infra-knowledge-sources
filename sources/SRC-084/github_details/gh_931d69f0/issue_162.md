# [Issue #162] perpare_for_inference issues

source: https://github.com/dropbox/hqq/issues/162
state: closed | updated: 2025-08-13T12:48:38Z
labels: 

## 正文

Hi,

first of all thanks to the authors for open-sourcing and maintaining this awesome quantization tool!

I'm trying out the different inference backends, and now have  a few questions regarding the `prepare_for_inference` function (https://github.com/mobiusml/hqq/blob/9b1deea4d735938289bbfebaabaa4d7e860f574d/hqq/utils/patching.py#L127):
1. When using Marlin, the function seems to check if BitBlas is installed and not Marlin (see https://github.com/mobiusml/hqq/blob/9b1deea4d735938289bbfebaabaa4d7e860f574d/hqq/utils/patching.py#L154). Is this intentional?
2. The link for installing BitBlas backend (https://github.com/mobiusml/bitblas/ - given in https://github.com/mobiusml/hqq/blob/9b1deea4d735938289bbfebaabaa4d7e860f574d/hqq/utils/patching.py#L143C147-L143C183) seems to be dead. Is this the correct repo for that backend? https://github.com/microsoft/BitBLAS
3. When trying to use a backend that is not properly set up, a `RunTimeError` exception is raised. However, this exception does not seem to exist? E.g.:
```
raise RunTimeError('Marlin backend is not available. Check if marlin is correctly installed if you want to use the Marlin backend (https://github.com/IST-DASLab/marlin).')
          ^^^^^^^^^^^^
NameError: name 'RunTimeError' is not defined. Did you mean: 'RuntimeError'?
```

I'm happy about any feedback regarding those matters!


## 评论 (4)

### mobicham · 2025-08-13

Hey! Sorry for the confusion, `Marlin` is deprecated, you should use the `gemlite` backend.
Updated the readme: https://github.com/mobiusml/hqq?tab=readme-ov-file#optimized-inference

### DominikHil · 2025-08-13

Hi, thanks for the quick response and clarification! Could you please also take a look at matter 2 (the Bitblas issue)? Is BitBlas deprecated as well? 

### mobicham · 2025-08-13

No it should work with BitBlas, just try `pip install bitblas`, lemme if there's an issue with that! Better to just use `gemlite`since it's faster in many situations and lightweight

### DominikHil · 2025-08-13

Got it, many thanks for the help :D
