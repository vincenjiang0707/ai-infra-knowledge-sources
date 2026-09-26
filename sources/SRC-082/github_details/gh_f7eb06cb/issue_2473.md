# [Issue #2473] [BUG] pyproject.toml license format incompatible with setuptools 71+

source: https://github.com/ModelCloud/GPTQModel/issues/2473
state: closed | updated: 2026-03-13T08:54:04Z
labels: bug

## 正文

Installing from git fails with setuptools 71+ due to invalid license format in pyproject.toml:

`ValueError: invalid pyproject.toml config: `project.license`.
GIVEN VALUE: "Apache-2.0"`

**Fix**: Change `license = "Apache-2.0"` to `license = {text = "Apache-2.0"}` per PEP 621.

Environment:

Python 3.12
setuptools 71.0.0+
Windows

## 评论 (6)

### Qubitium · 2026-03-12

@CSY-ModelCloud 

### Qubitium · 2026-03-12

@erm14254 setuptools in your env is too old. Please update. I think pip packaging fails to install/update to the latest setuptools due to circular dependency so you have to manually update setuptools before installing gptqmodel. We will test if we can force gptqmodel installer to auto detect/installest `setuptools`

```
pip install -U setuptools
```

it's a pain we know but this is caused by `pip` `setuptool` packaging updates and license property changes that is required for 2026 pypi releases.

### Qubitium · 2026-03-12

https://github.com/ModelCloud/GPTQModel/pull/2474

### Qubitium · 2026-03-12

Closed with #2474 and #2475

### erm14254 · 2026-03-12

> [@erm14254](https://github.com/erm14254) setuptools in your env is too old. Please update. I think pip packaging fails to install/update to the latest setuptools due to circular dependency so you have to manually update setuptools before installing gptqmodel. We will test if we can force gptqmodel installer to auto detect/installest `setuptools`
> 
> ```
> pip install -U setuptools
> ```
> 
> it's a pain we know but this is caused by `pip` `setuptool` packaging updates and license property changes that is required for 2026 pypi releases.

The issue seemed to have been unrelated to setuptool because today I just went ahead and upaded GPTQModel without updating setuptool and it worked like a charm now.

Plus another thing, now I just ran `pip install -U setuptools`

And I got this:

`Requirement already satisfied: setuptools in .\Lib\site-packages (82.0.1)`

So it wasn't even old?

### Qubitium · 2026-03-13

> > [@erm14254](https://github.com/erm14254) setuptools in your env is too old. Please update. I think pip packaging fails to install/update to the latest setuptools due to circular dependency so you have to manually update setuptools before installing gptqmodel. We will test if we can force gptqmodel installer to auto detect/installest `setuptools`
> > ```
> > pip install -U setuptools
> > ```
> > 
> > 
> >     
> >       
> >     
> > 
> >       
> >     
> > 
> >     
> >   
> > it's a pain we know but this is caused by `pip` `setuptool` packaging updates and license property changes that is required for 2026 pypi releases.
> 
> The issue seemed to have been unrelated to setuptool because today I just went ahead and upaded GPTQModel without updating setuptool and it worked like a charm now.
> 
> Plus another thing, now I just ran `pip install -U setuptools`
> 
> And I got this:
> 
> `Requirement already satisfied: setuptools in .\Lib\site-packages (82.0.1)`
> 
> So it wasn't even old?

The latest gptqmodel actually would force system to update `setuptools` but here it the catch. 

pip install uses `setuptools` so it loads gptqmodel and gptqmodel tells pip to update setuptools, it does, except it is already loaded by pip so pip is still running a older version of setuptools and might fail. You run pip again, and magic, setuptools is updated. 

So I am not exactly sure but very likely you had an very old version of setuptools and your recent install of gptqmodel forced update. 
