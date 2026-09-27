# [Issue #40] error on setup.py in kernels folder

source: https://github.com/mit-han-lab/llm-awq/issues/40
state: closed | updated: 2024-10-08T14:14:59Z
labels: 

## 正文

(awq) C:\Users\caleb\Desktop\AI stuff\llm-awq\awq\kernels>python -m setup.py install
No CUDA runtime is found, using CUDA_HOME='C:\Program Files\NVIDIA GPU Computing Toolkit\CUDA\v12.1'
running install
C:\Users\caleb\miniconda3\envs\awq\lib\site-packages\setuptools\_distutils\cmd.py:66: SetuptoolsDeprecationWarning: setup.py install is deprecated.
!!

        ********************************************************************************
        Please avoid running ``setup.py`` directly.
        Instead, use pypa/build, pypa/installer, pypa/build or
        other standards-based tools.

        See https://blog.ganssle.io/articles/2021/10/setup-py-deprecated.html for details.
        ********************************************************************************

!!
  self.initialize_options()
C:\Users\caleb\miniconda3\envs\awq\lib\site-packages\setuptools\_distutils\cmd.py:66: EasyInstallDeprecationWarning: easy_install command is deprecated.
!!

        ********************************************************************************
        Please avoid running ``setup.py`` and ``easy_install``.
        Instead, use pypa/build, pypa/installer, pypa/build or
        other standards-based tools.

        See https://github.com/pypa/setuptools/issues/917 for details.
        ********************************************************************************

!!
  self.initialize_options()
running bdist_egg
running egg_info
writing f16s4_gemm.egg-info\PKG-INFO
writing dependency_links to f16s4_gemm.egg-info\dependency_links.txt
writing requirements to f16s4_gemm.egg-info\requires.txt
writing top-level names to f16s4_gemm.egg-info\top_level.txt
C:\Users\caleb\miniconda3\envs\awq\lib\site-packages\torch\utils\cpp_extension.py:476: UserWarning: Attempted to use ninja as the BuildExtension backend but we could not find ninja.. Falling back to using the slow distutils backend.
  warnings.warn(msg.format('we could not find ninja.'))
reading manifest file 'f16s4_gemm.egg-info\SOURCES.txt'
writing manifest file 'f16s4_gemm.egg-info\SOURCES.txt'
installing library code to build\bdist.win-amd64\egg
running install_lib
running build_ext
C:\Users\caleb\miniconda3\envs\awq\lib\site-packages\torch\utils\cpp_extension.py:359: UserWarning: Error checking compiler version for cl: [WinError 2] The system cannot find the file specified
  warnings.warn(f'Error checking compiler version for {compiler}: {error}')
Traceback (most recent call last):
  File "C:\Users\caleb\miniconda3\envs\awq\lib\runpy.py", line 187, in _run_module_as_main
    mod_name, mod_spec, code = _get_module_details(mod_name, _Error)
  File "C:\Users\caleb\miniconda3\envs\awq\lib\runpy.py", line 110, in _get_module_details
    __import__(pkg_name)
  File "C:\Users\caleb\Desktop\AI stuff\llm-awq\awq\kernels\setup.py", line 9, in <module>
    setup(
  File "C:\Users\caleb\miniconda3\envs\awq\lib\site-packages\setuptools\__init__.py", line 107, in setup
    return distutils.core.setup(**attrs)
  File "C:\Users\caleb\miniconda3\envs\awq\lib\site-packages\setuptools\_distutils\core.py", line 185, in setup
    return run_commands(dist)
  File "C:\Users\caleb\miniconda3\envs\awq\lib\site-packages\setuptools\_distutils\core.py", line 201, in run_commands
    dist.run_commands()
  File "C:\Users\caleb\miniconda3\envs\awq\lib\site-packages\setuptools\_distutils\dist.py", line 969, in run_commands
    self.run_command(cmd)
  File "C:\Users\caleb\miniconda3\envs\awq\lib\site-packages\setuptools\dist.py", line 1244, in run_command
    super().run_command(command)
  File "C:\Users\caleb\miniconda3\envs\awq\lib\site-packages\setuptools\_distutils\dist.py", line 988, in run_command
    cmd_obj.run()
  File "C:\Users\caleb\miniconda3\envs\awq\lib\site-packages\setuptools\command\install.py", line 80, in run
    self.do_egg_install()
  File "C:\Users\caleb\miniconda3\envs\awq\lib\site-packages\setuptools\command\install.py", line 129, in do_egg_install
    self.run_command('bdist_egg')
  File "C:\Users\caleb\miniconda3\envs\awq\lib\site-packages\setuptools\_distutils\cmd.py", line 318, in run_command
    self.distribution.run_command(command)
  File "C:\Users\caleb\miniconda3\envs\awq\lib\site-packages\setuptools\dist.py", line 1244, in run_command
    super().run_command(command)
  File "C:\Users\caleb\miniconda3\envs\awq\lib\site-packages\setuptools\_distutils\dist.py", line 988, in run_command
    cmd_obj.run()
  File "C:\Users\caleb\miniconda3\envs\awq\lib\site-packages\setuptools\command\bdist_egg.py", line 164, in run
    cmd = self.call_command('install_lib', warn_dir=0)
  File "C:\Users\caleb\miniconda3\envs\awq\lib\site-packages\setuptools\command\bdist_egg.py", line 150, in call_command
    self.run_command(cmdname)
  File "C:\Users\caleb\miniconda3\envs\awq\lib\site-packages\setuptools\_distutils\cmd.py", line 318, in run_command
    self.distribution.run_command(command)
  File "C:\Users\caleb\miniconda3\envs\awq\lib\site-packages\setuptools\dist.py", line 1244, in run_command
    super().run_command(command)
  File "C:\Users\caleb\miniconda3\envs\awq\lib\site-packages\setuptools\_distutils\dist.py", line 988, in run_command
    cmd_obj.run()
  File "C:\Users\caleb\miniconda3\envs\awq\lib\site-packages\setuptools\command\install_lib.py", line 11, in run
    self.build()
  File "C:\Users\caleb\miniconda3\envs\awq\lib\site-packages\setuptools\_distutils\command\install_lib.py", line 111, in build
    self.run_command('build_ext')
  File "C:\Users\caleb\miniconda3\envs\awq\lib\site-packages\setuptools\_distutils\cmd.py", line 318, in run_command
    self.distribution.run_command(command)
  File "C:\Users\caleb\miniconda3\envs\awq\lib\site-packages\setuptools\dist.py", line 1244, in run_command
    super().run_command(command)
  File "C:\Users\caleb\miniconda3\envs\awq\lib\site-packages\setuptools\_distutils\dist.py", line 988, in run_command
    cmd_obj.run()
  File "C:\Users\caleb\miniconda3\envs\awq\lib\site-packages\setuptools\command\build_ext.py", line 84, in run
    _build_ext.run(self)
  File "C:\Users\caleb\miniconda3\envs\awq\lib\site-packages\setuptools\_distutils\command\build_ext.py", line 345, in run
    self.build_extensions()
  File "C:\Users\caleb\miniconda3\envs\awq\lib\site-packages\torch\utils\cpp_extension.py", line 499, in build_extensions
    _check_cuda_version(compiler_name, compiler_version)
  File "C:\Users\caleb\miniconda3\envs\awq\lib\site-packages\torch\utils\cpp_extension.py", line 383, in _check_cuda_version
    torch_cuda_version = packaging.version.parse(torch.version.cuda)
  File "C:\Users\caleb\miniconda3\envs\awq\lib\site-packages\pkg_resources\_vendor\packaging\version.py", line 52, in parse
    return Version(version)
  File "C:\Users\caleb\miniconda3\envs\awq\lib\site-packages\pkg_resources\_vendor\packaging\version.py", line 195, in __init__
    match = self._regex.search(version)
TypeError: expected string or bytes-like object





I can't figure out why the setup.py thing won't work, I can't finish installing this repo because of this error.

## 评论 (6)

### calebmor460 · 2023-07-19

nevermind, turns out it installed the wrong version of torch

### ShobhaRajanna · 2024-10-07

> nevermind, turns out it installed the wrong version of torch

which version have you installed?

### calebmor460 · 2024-10-07

I forget, it's been over a year now and the computer I was using when I made that post has since had to be factory reset

### ShobhaRajanna · 2024-10-08

> I forget, it's been over a year now and the computer I was using when I made that post has since had to be factory reset

Are you still working on this project?

### ShobhaRajanna · 2024-10-08

> > I forget, it's been over a year now and the computer I was using when I made that post has since had to be factory reset
> 
> Are you still working on this project?

I am trying to build the awq_inference_engine on a system with Tesla V100 GPUs, but I'm encountering errors related to CUDA architecture compatibility. Specifically, the build fails with errors such as Feature 'ldmatrix' requires .target sm_75 or higher when compiling gemm_cuda_gen.cu.

Steps to reproduce:

Clone the repository.
Set up the environment (CUDA 11.7, Tesla V100 GPUs).
Run python setup.py install.
Compilation fails with the errors listed below.
ptxas /tmp/tmpxft_00022ba1_00000000-6_gemm_cuda_gen.ptx, line 596; error : Feature 'ldmatrix' requires .target sm_75 or higher
ptxas /tmp/tmpxft_00022ba1_00000000-6_gemm_cuda_gen.ptx, line 604; error : Modifier '.m8n8' requires .target sm_75 or higher

Environment:

GPU: Tesla V100-SXM2
CUDA Version: 11.7
PyTorch Version: 2.x
Operating System: Ubuntu 18.04
I tried modifying the setup.py to include the -gencode arch=compute_70,code=sm_70 flags and conditionally compiling the CUDA code, but the issue persists. Is there a recommended way to disable features requiring sm_75 for older GPUs like the V100?

### calebmor460 · 2024-10-08

> > I forget, it's been over a year now and the computer I was using when I made that post has since had to be factory reset
> 
> Are you still working on this project?
I am not
