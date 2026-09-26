# [Issue #21] [Question] API stability and versioning

source: https://github.com/ROCm/amdsmi/issues/21
state: closed | updated: 2024-05-01T00:52:41Z
labels: 

## 正文

First of all, thanks for building this. This is much needed.
I'm building a Python-based tool that has NVIDIA GPU support, and I'm adding AMD GPU support as well.
I hope the tool to be generic over multiple ROCm versions, so I wanted to ask about API stability and versioning plans for `amdsmi`.

- How is `amdsmi` versioned? Does it simply follow ROCm?
- How stable are `amdsmi` APIs? Can I expect it to not change that much across ROCm versions? Or is it in active development and should I expect a lot of changes? If it's the latter I'll have to switch on the user's current ROCm versions when calling specific APIs.
- Will the in-tree python bindings in each release always be kept in sync with API changes?

Thanks a lot!


## 评论 (2)

### marifamd · 2024-05-01

@jaywonchung Thanks for reaching out! This is a new tool, so it is under regular development. 

While the CLI tool will be subject to change, the C and Python Libraries should not experience any drastic changes and if they do we are doing our best to post all new updates (CLI Tool and Libraries) in the [CHANGELOG](https://github.com/ROCm/amdsmi/blob/develop/CHANGELOG.md). 

We release stable versions aligning to the ROCm release schedule (and within ROCm), but we have a Tool version and a Library version. Our versioning is based on Year, Major(Month), Minor, and Release.  We also print out whatever the active version of ROCm you have active on your system.

You can check the version via the tool:
```shell
$ amd-smi version
AMDSMI Tool: 24.5.1+881920c | AMDSMI Library version: 24.5.1.0 | ROCm version: 6.1.0
``` 
or by calling the API :
```python
$ python3
python 3.10.12 (main, Nov 20 2023, 15:14:05) [GCC 11.4.0] on linux
Type "help", "copyright", "credits" or "license" for more information.
>>> import amdsmi
>>> amdsmi.amdsmi_init()
>>> tool_version = amdsmi.__version__
>>> library_version = amdsmi.amdsmi_get_lib_version()
>>> tool_version
'24.5.1+881920c'
>>> library_version
{'year': 24, 'major': 5, 'minor': 1, 'release': 0, 'build': '2'}
```

Regarding the python bindings, we intend to keep the [python bindings ](https://github.com/ROCm/amdsmi/blob/develop/py-interface/README.md) upto date with C++ API changes. If you find that and C++ API's are not reflected in the python bindings, please file another issue and we will handle it accordingly. 


Thanks for the appreciation,
Maisam


### jaywonchung · 2024-05-01

Thanks a lot for the kind response! All questions resolved.
