# [Issue #5388] Documentation on triton-lang.org is not versioned

source: https://github.com/triton-lang/triton/issues/5388
state: open | updated: 2026-09-01T18:09:34Z
labels: documentation

## 正文

### Describe the bug

`DriverBase` abstract class has the method `get_active_torch_device` but after installation it is giving the error as
```python
DEVICE = triton.runtime.driver.active.get_active_torch_device()
```
```
{
	"name": "AttributeError",
	"message": "'CudaDriver' object has no attribute 'get_active_torch_device'",
	"stack": "---------------------------------------------------------------------------
AttributeError                            Traceback (most recent call last)
Cell In[16], line 1
----> 1 DEVICE = triton.runtime.driver.active.get_active_torch_device()
      2 DEVICE

File /HOME/miniconda3/envs/learn/lib/python3.12/site-packages/triton/runtime/driver.py:24, in LazyProxy.__getattr__(self, name)
     22 def __getattr__(self, name):
     23     self._initialize_obj()
---> 24     return getattr(self._obj, name)

AttributeError: 'CudaDriver' object has no attribute 'get_active_torch_device'"
}
```

### Environment details

Triton: 3.1.0
GPUs: 4xA100 80G

## 评论 (16)

### peterbell10 · 2024-12-10

This means `CudaDriver` is coming from a older install of triton. Try uninstalling any other triton versions in your system.

### SwayamInSync · 2024-12-11

> This means `CudaDriver` is coming from a older install of triton. Try uninstalling any other triton versions in your system.

Hi Peter, thanks for the response
I checked and there is only one triton installation, attaching complete environement below
```
# Name                    Version                   Build  Channel
_libgcc_mutex             0.1                 conda_forge    conda-forge
_openmp_mutex             4.5                       2_gnu    conda-forge
asttokens                 3.0.0              pyhd8ed1ab_1    conda-forge
bzip2                     1.0.8                h4bc722e_7    conda-forge
ca-certificates           2024.8.30            hbcca054_0    conda-forge
comm                      0.2.2              pyhd8ed1ab_1    conda-forge
debugpy                   1.8.9           py310hf71b8c6_0    conda-forge
decorator                 5.1.1              pyhd8ed1ab_1    conda-forge
exceptiongroup            1.2.2              pyhd8ed1ab_1    conda-forge
executing                 2.1.0              pyhd8ed1ab_1    conda-forge
filelock                  3.16.1                   pypi_0    pypi
fsspec                    2024.10.0                pypi_0    pypi
importlib-metadata        8.5.0              pyha770c72_1    conda-forge
ipykernel                 6.29.5             pyh3099207_0    conda-forge
ipython                   8.30.0             pyh707e725_0    conda-forge
jedi                      0.19.2             pyhd8ed1ab_1    conda-forge
jinja2                    3.1.4                    pypi_0    pypi
jupyter_client            8.6.3              pyhd8ed1ab_1    conda-forge
jupyter_core              5.7.2              pyh31011fe_1    conda-forge
keyutils                  1.6.1                h166bdaf_0    conda-forge
krb5                      1.21.3               h659f571_0    conda-forge
ld_impl_linux-64          2.43                 h712a8e2_2    conda-forge
libedit                   3.1.20191231         he28a2e2_2    conda-forge
libffi                    3.4.2                h7f98852_5    conda-forge
libgcc                    14.2.0               h77fa898_1    conda-forge
libgcc-ng                 14.2.0               h69a702a_1    conda-forge
libgomp                   14.2.0               h77fa898_1    conda-forge
liblzma                   5.6.3                hb9d3cd8_1    conda-forge
libnsl                    2.0.1                hd590300_0    conda-forge
libsodium                 1.0.20               h4ab18f5_0    conda-forge
libsqlite                 3.47.2               hee588c1_0    conda-forge
libstdcxx                 14.2.0               hc0a3c3a_1    conda-forge
libstdcxx-ng              14.2.0               h4852527_1    conda-forge
libuuid                   2.38.1               h0b41bf4_0    conda-forge
libxcrypt                 4.4.36               hd590300_1    conda-forge
libzlib                   1.3.1                hb9d3cd8_2    conda-forge
markupsafe                3.0.2                    pypi_0    pypi
matplotlib-inline         0.1.7              pyhd8ed1ab_1    conda-forge
mpmath                    1.3.0                    pypi_0    pypi
ncurses                   6.5                  he02047a_1    conda-forge
nest-asyncio              1.6.0              pyhd8ed1ab_1    conda-forge
networkx                  3.4.2                    pypi_0    pypi
nvidia-cublas-cu12        12.4.5.8                 pypi_0    pypi
nvidia-cuda-cupti-cu12    12.4.127                 pypi_0    pypi
nvidia-cuda-nvrtc-cu12    12.4.127                 pypi_0    pypi
nvidia-cuda-runtime-cu12  12.4.127                 pypi_0    pypi
nvidia-cudnn-cu12         9.1.0.70                 pypi_0    pypi
nvidia-cufft-cu12         11.2.1.3                 pypi_0    pypi
nvidia-curand-cu12        10.3.5.147               pypi_0    pypi
nvidia-cusolver-cu12      11.6.1.9                 pypi_0    pypi
nvidia-cusparse-cu12      12.3.1.170               pypi_0    pypi
nvidia-nccl-cu12          2.21.5                   pypi_0    pypi
nvidia-nvjitlink-cu12     12.4.127                 pypi_0    pypi
nvidia-nvtx-cu12          12.4.127                 pypi_0    pypi
openssl                   3.4.0                hb9d3cd8_0    conda-forge
packaging                 24.2               pyhd8ed1ab_2    conda-forge
parso                     0.8.4              pyhd8ed1ab_1    conda-forge
pexpect                   4.9.0              pyhd8ed1ab_1    conda-forge
pickleshare               0.7.5           pyhd8ed1ab_1004    conda-forge
pip                       24.3.1             pyh8b19718_0    conda-forge
platformdirs              4.3.6              pyhd8ed1ab_1    conda-forge
prompt-toolkit            3.0.48             pyha770c72_1    conda-forge
psutil                    6.1.0           py310ha75aee5_0    conda-forge
ptyprocess                0.7.0              pyhd8ed1ab_1    conda-forge
pure_eval                 0.2.3              pyhd8ed1ab_1    conda-forge
pygments                  2.18.0             pyhd8ed1ab_1    conda-forge
python                    3.10.16         he725a3c_1_cpython    conda-forge
python-dateutil           2.9.0.post0        pyhff2d567_1    conda-forge
python_abi                3.10                    5_cp310    conda-forge
pyzmq                     26.2.0          py310h71f11fc_3    conda-forge
readline                  8.2                  h8228510_1    conda-forge
setuptools                75.6.0             pyhff2d567_1    conda-forge
six                       1.17.0             pyhd8ed1ab_0    conda-forge
stack_data                0.6.3              pyhd8ed1ab_1    conda-forge
sympy                     1.13.1                   pypi_0    pypi
tk                        8.6.13          noxft_h4845f30_101    conda-forge
torch                     2.5.1                    pypi_0    pypi
tornado                   6.4.2           py310ha75aee5_0    conda-forge
traitlets                 5.14.3             pyhd8ed1ab_1    conda-forge
triton                    3.1.0                    pypi_0    pypi
typing_extensions         4.12.2             pyha770c72_1    conda-forge
tzdata                    2024b                hc8b5060_0    conda-forge
wcwidth                   0.2.13             pyhd8ed1ab_1    conda-forge
wheel                     0.45.1             pyhd8ed1ab_1    conda-forge
zeromq                    4.3.5                h3b0a872_7    conda-forge
zipp                      3.21.0             pyhd8ed1ab_1    conda-forge
```

### peterbell10 · 2024-12-11

Oh I see the issue, `get_active_torch_device` has been added recently on the main branch and isn't in a released version but the docs on the website were updated to match main.  The website should probably have docs from the latest released version instead.

As a workaround you can replace with:
```python
DEVICE = "cuda"
```

### SwayamInSync · 2024-12-11

That make sense, closing this now
Thanks @peterbell10 

### peterbell10 · 2024-12-11

The docs being for an unreleased version is a real issue though.

### wa008 · 2024-12-26

`DEVICE = torch.device("cuda:0")` works for colab.

### noklam · 2025-03-05

Run into the same issue. Would the team open to PR to make the documentations host on ReadTheDocs so that it's versioned?

### MostHumble · 2025-04-05

good old webarchive to the rescue:  https://web.archive.org/ 

### Freed-Wu · 2025-05-16

3.2.0 still `AttributeError: 'CudaDriver' object has no attribute 'get_active_torch_device'`

### NirZabari · 2025-06-01

Does anyone have any idea which version works with the tutorials?
It looks like building from source doesn’t work either

### tcapelle · 2025-06-02

same issues...

### jlqibm · 2025-07-11

See above.  You can work around this with
`DEVICE = torch.device("cuda:0")`

### vidigoat · 2026-05-30

I looked into this, and the versioning machinery is actually already configured — `sphinx_multiversion` is in `extensions` in `docs/conf.py`, with `smv_branch_whitelist = '^main$'` and `smv_tag_whitelist = '^(v3.7.0)$'`. The gap is in the build step: `make docs-only` (used by `.github/workflows/documentation.yml`) runs a single-version build —

```
cd docs; python -m sphinx . _build/html/main
```

— so it only builds the current checkout into `html/main` and never invokes `sphinx-multiversion`. That's why the published site only reflects `main`, and users on a released version hit missing symbols like `get_active_torch_device`.

Two ways to resolve it, depending on what you'd prefer:

1. **Wire up the existing config**: switch the docs build to `sphinx-multiversion` and update the deploy in `documentation.yml` to publish the multi-output tree plus a default-version redirect, keeping `smv_tag_whitelist` current per release. This is the "real" fix but touches the deploy workflow.
2. **Lighter-weight**: keep the single-version build but add a banner to the docs noting the site tracks the development branch, linking to install-from-source / the matching release. Minimal, and unblocks the user confusion immediately.

Happy to put up a PR for either — which direction would you prefer?


### peterbell10 · 2026-05-30

I think we do want to use sphinx-multiversion. A PR would be welcome.

### vidigoat · 2026-05-30

Opened #10424 implementing option 1 (sphinx-multiversion). It adds a `docs-multiversion` make target, switches the Documentation workflow to it, fixes a duplicate `html_sidebars` that was hiding the version switcher, and pins `sphinx<8` (sphinx-multiversion isn't compatible with Sphinx 8+). I verified the multiversion build + the "Other Versions" switcher on a minimal sphinx-rtd-theme reproduction; details in the PR.

### LeonxLJX · 2026-09-01

I'd like to take this one (`Documentation on triton-lang.org is not versioned`). I'll look into the root cause and follow up with a PR. (claiming via @LeonxLJX)
