# [Issue #2425] [PyPcre/Compat] Windows pip install issue on a python 3.12 venv

source: https://github.com/ModelCloud/GPTQModel/issues/2425
state: closed | updated: 2026-03-11T22:03:50Z
labels: in-progress

## 正文

Trying to install using `pip install gptqmodel --no-build-isolation` on a python 3.12 venv, in windows 11.
It gets stuck at `pypcre-0.2.9`. The PC has Visual Studio 2026 (including C++ deps), cmake, CUDA 13.0, RTX 4070. 

Output:
Collecting gptqmodel
  Using cached gptqmodel-5.7.0.tar.gz (668 kB)
  Preparing metadata (pyproject.toml) ... done
Requirement already satisfied: accelerate>=1.10.1 in .\.venv\Lib\site-packages (from gptqmodel) (1.12.0)
Collecting numpy==2.2.6 (from gptqmodel)
  Using cached numpy-2.2.6-cp312-cp312-win_amd64.whl.metadata (60 kB)
Requirement already satisfied: torch>=2.8.0 in .\.venv\Lib\site-packages (from gptqmodel) (2.9.1+cu130)
Requirement already satisfied: safetensors>=0.6.2 in .\.venv\Lib\site-packages (from gptqmodel) (0.7.0)
Requirement already satisfied: transformers>=4.57.1 in .\.venv\Lib\site-packages (from gptqmodel) (5.2.0)
Collecting threadpoolctl>=3.6.0 (from gptqmodel)
  Using cached threadpoolctl-3.6.0-py3-none-any.whl.metadata (13 kB)
Requirement already satisfied: packaging>=24.2 in .\.venv\Lib\site-packages (from gptqmodel) (26.0)
Collecting device-smi>=0.5.3 (from gptqmodel)
  Using cached device_smi-0.5.3.tar.gz (18 kB)
  Preparing metadata (pyproject.toml) ... done
Requirement already satisfied: protobuf>=6.32.0 in .\.venv\Lib\site-packages (from gptqmodel) (6.33.5)
Requirement already satisfied: pillow>=11.3.0 in .\.venv\Lib\site-packages (from gptqmodel) (12.0.0)
Requirement already satisfied: hf_transfer>=0.1.9 in .\.venv\Lib\site-packages (from gptqmodel) (0.1.9)
Requirement already satisfied: huggingface_hub>=0.34.4 in .\.venv\Lib\site-packages (from gptqmodel) (1.4.1)
Collecting tokenicer>=0.0.6 (from gptqmodel)
  Using cached tokenicer-0.0.6.tar.gz (9.8 kB)
  Preparing metadata (pyproject.toml) ... done
Collecting logbar>=0.2.1 (from gptqmodel)
  Using cached logbar-0.2.1.tar.gz (34 kB)
  Preparing metadata (pyproject.toml) ... done
Collecting maturin>=1.9.4 (from gptqmodel)
  Using cached maturin-1.12.4-py3-none-win_amd64.whl.metadata (16 kB)
Requirement already satisfied: datasets>=3.6.0 in .\.venv\Lib\site-packages (from gptqmodel) (4.5.0)
Requirement already satisfied: pyarrow>=21.0 in .\.venv\Lib\site-packages (from gptqmodel) (23.0.1)
Requirement already satisfied: dill>=0.3.8 in .\.venv\Lib\site-packages (from gptqmodel) (0.4.0)
Collecting pypcre>=0.2.9 (from gptqmodel)
  Using cached pypcre-0.2.9.tar.gz (118 kB)
  Preparing metadata (pyproject.toml) ... error
  error: subprocess-exited-with-error

  × Preparing metadata (pyproject.toml) did not run successfully.
  │ exit code: 1
  ╰─> [66 lines of output]
      Cloning into 'C:\...\AppData\Local\Temp\pip-install-fkjp7s9v\pypcre_01516d8e076440e99de2d45cad90e331\pcre_ext\pcre2-10.46'...
      warning: refs/tags/pcre2-10.46 56c87ccac13b01c3c1ecdf71e4fc2fedccea50a2 is not a commit!
      Note: switching to 'b2bd4254b379b9d7dc9a3dda060a7e27009ccdff'.

      You are in 'detached HEAD' state. You can look around, make experimental
      changes and commit them, and you can discard any commits you make in this
      state without impacting any branches by switching back to a branch.

      If you want to create a new branch to retain commits you create, you may
      do so (now or later) by using -c with the switch command. Example:

        git switch -c <new-branch-name>

      Or undo this operation with:

        git switch -

      Turn off this advice by setting config variable advice.detachedHead to false

      Submodule 'deps/sljit' (https://github.com/zherczeg/sljit.git) registered for path 'deps/sljit'
      Cloning into 'C:/.../AppData/Local/Temp/pip-install-fkjp7s9v/pypcre_01516d8e076440e99de2d45cad90e331/pcre_ext/pcre2-10.46/deps/sljit'...
      From https://github.com/zherczeg/sljit
       * branch            e51eabbfb8eabc6526f56e4e88b29fb10d1ee048 -> FETCH_HEAD
      Submodule path 'deps/sljit': checked out 'e51eabbfb8eabc6526f56e4e88b29fb10d1ee048'
      Found CMake candidates:
        - C:\Program Files\CMake\bin\cmake.exe
      Validated CMake executable at C:\Program Files\CMake\bin\cmake.exe
      Using CMake at C:\Program Files\CMake\bin\cmake.exe
      CMake Error at CMakeLists.txt:116 (project):
        Generator

          Visual Studio 17 2022

        could not find any instance of Visual Studio.



      -- Configuring incomplete, errors occurred!
      PyPcre build: using CMake executable at C:\Program Files\CMake\bin\cmake.exe (cmake version 4.2.3)
      Traceback (most recent call last):
        File "C:\...\AppData\Local\Temp\pip-install-fkjp7s9v\pypcre_01516d8e076440e99de2d45cad90e331\setup_utils.py", line 585, in _prepare_pcre2_source
          subprocess.run(cmake_args, cwd=destination, env=env, check=True)
        File "C:\...\AppData\Local\Programs\Python\Python312\Lib\subprocess.py", line 571, in run
          raise CalledProcessError(retcode, process.args,
      subprocess.CalledProcessError: Command '['C:\\Program Files\\CMake\\bin\\cmake.exe', '-S', 'C:\\...\\AppData\\Local\\Temp\\pip-install-fkjp7s9v\\pypcre_01516d8e076440e99de2d45cad90e331\\pcre_ext\\pcre2-10.46', '-B', 'C:\\...\\AppData\\Local\\Temp\\pip-install-fkjp7s9v\\pypcre_01516d8e076440e99de2d45cad90e331\\pcre_ext\\pcre2-10.46\\build', '-DPCRE2_SUPPORT_JIT=ON', '-DPCRE2_BUILD_PCRE2_8=ON', '-DPCRE2_BUILD_TESTS=OFF', '-DPCRE2_BUILD_PCRE2GREP=OFF', '-DPCRE2_BUILD_PCRE2TEST=OFF', '-DBUILD_SHARED_LIBS=OFF', '-G', 'Visual Studio 17 2022', '-A', 'x64', '-DCMAKE_MSVC_RUNTIME_LIBRARY=MultiThreadedDLL']' returned non-zero exit status 1.        

      The above exception was the direct cause of the following exception:

      Traceback (most recent call last):
        File "D:\...\.venv\Lib\site-packages\pip\_vendor\pyproject_hooks\_in_process\_in_process.py", line 389, in <module>
          main()
        File "D:\...\.venv\Lib\site-packages\pip\_vendor\pyproject_hooks\_in_process\_in_process.py", line 373, in main
          json_out["return_val"] = hook(**hook_input["kwargs"])
                                   ^^^^^^^^^^^^^^^^^^^^^^^^^^^^
        File "D:\...\.venv\Lib\site-packages\pip\_vendor\pyproject_hooks\_in_process\_in_process.py", line 175, in prepare_metadata_for_build_wheel
          return hook(metadata_directory, config_settings)
                 ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
        File "D:\...\.venv\Lib\site-packages\setuptools\build_meta.py", line 380, in prepare_metadata_for_build_wheel
          self.run_setup()
        File "D:\...\.venv\Lib\site-packages\setuptools\build_meta.py", line 317, in run_setup
          exec(code, locals())
        File "<string>", line 308, in <module>
        File "<string>", line 126, in collect_build_config
        File "C:\...\AppData\Local\Temp\pip-install-fkjp7s9v\pypcre_01516d8e076440e99de2d45cad90e331\setup_utils.py", line 593, in _prepare_pcre2_source
          raise RuntimeError(
      RuntimeError: Failed to build PCRE2 from source using CMake; see the output above for details
      [end of output]

  note: This error originates from a subprocess, and is likely not a problem with pip.
error: metadata-generation-failed

× Encountered error while generating package metadata.
╰─> pypcre

note: This is an issue with the package mentioned above, not pip.
hint: See above for details.
==================== 

Is it possible to use GPTQModel in windows? If so, please a solution to this.

_Originally posted by @sbhmajum369 in https://github.com/ModelCloud/GPTQModel/discussions/2424_

## 评论 (9)

### Qubitium · 2026-03-02

@sbhmajum369  We have released udpdated `pypcre` pkg which resolves the visual studio 2026 issue. 

https://github.com/ModelCloud/PyPcre/releases

Please do `pip install -U pypcre` and reinstall gptqmodel

### Qubitium · 2026-03-02

https://github.com/ModelCloud/PyPcre/pull/64/changes

please set your windows `env` `CMAKE_GENERATOR` to your correct visual studio 2026 and the compile issue should go away. We will try to add code to auto detect VS studio version for cmake in the future. 

### Qubitium · 2026-03-02

@sbhmajum369 

PyPcre v0.2.11 has been released with auto `visual studio` version detection. Please test. I will close this issue as it is completed. If you have more issues, please open an issue and @ me in the pypcre repo.

https://github.com/ModelCloud/PyPcre/releases/tag/v0.2.11



### Colony-tizer · 2026-03-09

> please set your windows env CMAKE_GENERATOR to your correct visual studio 2026 and the compile issue should go away

Unfortunately the hint was unclear to me.
Setting the enviroment variable CMAKE_GENERATOR to "Visual Studio 18 2026" fixed the problem.
Basically, set variable value to "Visual Studio {id} {year}" (use code and year combination from this map:
https://github.com/ModelCloud/PyPcre/commit/da1c8888458b265e3f426dda3687502031d20616#diff-efec160b8a32e22abfaa4dcd32aa9b2aca681ddb098054aff49ee4e863ab4bbbR511)

### Qubitium · 2026-03-10

@Colony-tizer Latest pypcre should alsready auto detect your installed Visual Studio so you don't hhave to manually set this:

```
pip install -U pypcre
```

If you get error without manually setting env `CMAKE_GENERATOR` please let us know your Windows os version and installed visual studio version. Thanks.

### Colony-tizer · 2026-03-10

@Qubitium I ran that command earlier but still got the issue.
Details: Win 11 25H2 26200.7840, Visual Studio Community 2026 18.3.2 and Insiders 11519.219

### Qubitium · 2026-03-10

> [@Qubitium](https://github.com/Qubitium) I ran that command earlier but still got the issue. Details: Win 11 25H2 26200.7840, Visual Studio Community 2026 18.3.2 and Insiders 11519.219

@CSY-ModelCloud  Check this. 

### Qubitium · 2026-03-11

@Colony-tizer  We have releaed v0.2.13 to fix this issue. Please confirm without having to manually set `CMAKE_GENERATOR`:

```
pip install -U pypcre
```

thanks!

### Colony-tizer · 2026-03-11

@Qubitium Thanks, the issue has been fixed!
