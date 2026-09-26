# [Issue #219] Package name change

source: https://github.com/deepseek-ai/DeepGEMM/issues/219
state: closed | updated: 2025-10-20T13:26:46Z
labels: 

## 正文

Hi! In 9528451969bba06b67947a31fd9b38126d5e8a73 (which was included in v2.1.1.post1), the name of the library was changed from `deep-gemm` to `deepgemm`. This causes a lot of issues for downstream users of this library that specify it as a dependency (or import it) using the old name, resulting in broken builds and invalid import statements, necessitating expensive workarounds or migrations.

In https://github.com/deepseek-ai/DeepGEMM/pull/217, it was noted that this name change is necessary since the name is already taken on PyPI, but instead of changing the name it might be better to try to reclaim that name in PyPI. You could consider asking the PyPI package owner if they can transfer the package to you, or file a PEP541 support request in https://github.com/pypi/support to use the original name since to prevent name confusion attacks.

Let me know if you need assistance with either of these approaches; I think it would benefit the community to keep the package name the same going forward. Thank you!

## 评论 (6)

### ko3n1g · 2025-10-15

Hey @mprpic, I'm checking. 

Could you share an error message? I'm surprised by this, imports (`import deep_gemm`) shouldb be affected by this. Which scenario are you running into?

### ko3n1g · 2025-10-15

I.e. the following still works fine:

```
root@6ca8e17390fb:/# pip install --no-build-isolation  git+https://github.com/deepseek-ai/DeepGEMM.git
Collecting git+https://github.com/deepseek-ai/DeepGEMM.git
  Cloning https://github.com/deepseek-ai/DeepGEMM.git to /tmp/pip-req-build-6ez6eedc
  Running command git clone --filter=blob:none --quiet https://github.com/deepseek-ai/DeepGEMM.git /tmp/pip-req-build-6ez6eedc
  Resolved https://github.com/deepseek-ai/DeepGEMM.git to commit 2b8a8e24f8964fa2f7a74f435bf2975dea56950a
  Running command git submodule update --init --recursive -q
  Preparing metadata (setup.py) ... done
Building wheels for collected packages: deepgemm
  DEPRECATION: Building 'deepgemm' using the legacy setup.py bdist_wheel mechanism, which will be removed in a future version. pip 25.3 will enforce this behaviour change. A possible replacement is to use the standardized build interface by setting the `--use-pep517` option, (possibly combined with `--no-build-isolation`), or adding a `pyproject.toml` file to the source tree of 'deepgemm'. Discussion can be found at https://github.com/pypa/pip/issues/6334
  Building wheel for deepgemm (setup.py) ... done
  Created wheel for deepgemm: filename=deepgemm-2.1.1+2b8a8e2-cp312-cp312-linux_x86_64.whl size=8507544 sha256=7424195ae68bbafbb2e66ea06851ddc2150ad2f84de1182c6e80ad2c409b1e1f
  Stored in directory: /tmp/pip-ephem-wheel-cache-2w0ekps7/wheels/7c/82/61/6ae0658158d61b3f52b97c7fbde3c7be237f97a2601025fe5c
Successfully built deepgemm
Installing collected packages: deepgemm
Successfully installed deepgemm-2.1.1+2b8a8e2
WARNING: Running pip as the 'root' user can result in broken permissions and conflicting behaviour with the system package manager, possibly rendering your system unusable. It is recommended to use a virtual environment instead: https://pip.pypa.io/warnings/venv. Use the --root-user-action option if you know what you are doing and want to suppress this warning.
root@6ca8e17390fb:/# python
Python 3.12.3 (main, Feb  4 2025, 14:48:35) [GCC 13.3.0] on linux
Type "help", "copyright", "credits" or "license" for more information.
>>> import deep_gemm
>>> 
```

### mprpic · 2025-10-15

Ah, the import statements work indeed, sorry about that. At Red Hat, we use https://github.com/python-wheel-build/fromager to build wheels of certain AI/ML libraries, and the resulting wheel name is thus different so it breaks our build because it expects the old name for a version-unconstrained inclusion of this library in a requirements file. To be able to support the new name, we'd have to maintain two different versions and two different names for the same code in our build definitions for this specific library.

### ko3n1g · 2025-10-15

Oh that's a fair point, system's depending on the wheel-name will have a bad day. Apologies, I'll open a revert right away. I'm a bit pessimistic  on the PyPI transfer but I'll give it a try. 

Thanks for the quick issue!

### mprpic · 2025-10-15

This library has almost 6k stars here on GitHub, so it seems fair that you should own the same package name in PyPI to prevent package name confusion. Let me know if you'd like help with filing the requests to PyPI. Thank you for the quick action!

### mprpic · 2025-10-20

Closing this in favor of: https://github.com/pypi/support/issues/7898
