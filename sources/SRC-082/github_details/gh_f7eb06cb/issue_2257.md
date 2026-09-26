# [Issue #2257] [BUG] Can not install neither from source nor from pypi

source: https://github.com/ModelCloud/GPTQModel/issues/2257
state: closed | updated: 2025-12-12T13:35:49Z
labels: bug

## 正文

Steps I did:
1) git clone https://github.com/ModelCloud/GPTQModel.git
2) apt update
3) apt install ninja-build python3-setuptools --upgrade
4) cd GPTQModel && pip install -v . --no-build-isolation

"pip install --upgrade setuptools" does not help
 
I keep getting this output:


configuration error: `project.license` must be valid exactly by one definition (2 matches found):

      - keys:
          'file': {type: string}
        required: ['file']
      - keys:
          'text': {type: string}
        required: ['text']

  DESCRIPTION:
      `Project license <[https://peps.python.org/pep-0621/#license>`_](https://peps.python.org/pep-0621/#license%3E%60_).

  GIVEN VALUE:
      "Apache-2.0"

  OFFENDING RULE: 'oneOf'

  DEFINITION:
      {
          "oneOf": [
              {
                  "properties": {
                      "file": {
                          "type": "string",
                          "$$description": [
                              "Relative path to the file (UTF-8) which contains the license for the",
                              "project."
                          ]
                      }
                  },
                  "required": [
                      "file"
                  ]
              },
              {
                  "properties": {
                      "text": {
                          "type": "string",
                          "$$description": [
                              "The license of the project whose meaning is that of the",
                              "`License field from the core metadata",
                              "<[https://packaging.python.org/specifications/core-metadata/#license>`_](https://packaging.python.org/specifications/core-metadata/#license%3E%60_)."
                          ]
                      }
                  },
                  "required": [
                      "text"
                  ]
              }
          ]
      }
  Traceback (most recent call last):
    File "/usr/local/lib/python3.11/dist-packages/pip/_vendor/pyproject_hooks/_in_process/_in_process.py", line 353, in <module>
      main()
    File "/usr/local/lib/python3.11/dist-packages/pip/_vendor/pyproject_hooks/_in_process/_in_process.py", line 335, in main
      json_out['return_val'] = hook(**hook_input['kwargs'])
                               ^^^^^^^^^^^^^^^^^^^^^^^^^^^^
    File "/usr/local/lib/python3.11/dist-packages/pip/_vendor/pyproject_hooks/_in_process/_in_process.py", line 149, in prepare_metadata_for_build_wheel
      return hook(metadata_directory, config_settings)
             ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
    File "/usr/local/lib/python3.11/dist-packages/setuptools/build_meta.py", line 373, in prepare_metadata_for_build_wheel
      self.run_setup()
    File "/usr/local/lib/python3.11/dist-packages/setuptools/build_meta.py", line 318, in run_setup
      exec(code, locals())
    File "<string>", line 1, in <module>
    File "/usr/local/lib/python3.11/dist-packages/setuptools/__init__.py", line 117, in setup
      return distutils.core.setup(**attrs)
             ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
    File "/usr/local/lib/python3.11/dist-packages/setuptools/_distutils/core.py", line 157, in setup
      dist.parse_config_files()
    File "/usr/local/lib/python3.11/dist-packages/setuptools/dist.py", line 647, in parse_config_files
      pyprojecttoml.apply_configuration(self, filename, ignore_option_errors)
    File "/usr/local/lib/python3.11/dist-packages/setuptools/config/pyprojecttoml.py", line 71, in apply_configuration
      config = read_configuration(filepath, True, ignore_option_errors, dist)
               ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
    File "/usr/local/lib/python3.11/dist-packages/setuptools/config/pyprojecttoml.py", line 139, in read_configuration
      validate(subset, filepath)
    File "/usr/local/lib/python3.11/dist-packages/setuptools/config/pyprojecttoml.py", line 60, in validate
      raise ValueError(f"{error}\n{summary}") from None
  ValueError: invalid pyproject.toml config: `project.license`.
  configuration error: `project.license` must be valid exactly by one definition (2 matches found):

      - keys:
          'file': {type: string}
        required: ['file']
      - keys:
          'text': {type: string}
        required: ['text']

  error: subprocess-exited-with-error
  
  × Preparing metadata (pyproject.toml) did not run successfully.
  │ exit code: 1
  ╰─> See above for output.
  
  note: This error originates from a subprocess, and is likely not a problem with pip.
  full command: /usr/bin/python3 /usr/local/lib/python3.11/dist-packages/pip/_vendor/pyproject_hooks/_in_process/_in_process.py prepare_metadata_for_build_wheel /tmp/tmp4e_76s1n
  cwd: /tmp/pip-install-9q55s3_r/logbar_8a759d7831024fa6beddbd5fa81c8aa3
  Preparing metadata (pyproject.toml) ... error
error: metadata-generation-failed

× Encountered error while generating package metadata.
╰─> See above for output.

note: This is an issue with the package mentioned above, not pip.
hint: See above for details.

## 评论 (5)

### Qubitium · 2025-12-12

@a13xbb Fixed on `main`. We will releaes 5.6.2 patch release today. Please pull main and try again. 

### mcslender97 · 2025-12-12

Any ETA on when the patch is live on PyPi?

### Qubitium · 2025-12-12

> Any ETA on when the patch is live on PyPi?

Within next 3 hours



### Qubitium · 2025-12-12

https://github.com/ModelCloud/GPTQModel/releases/tag/v5.6.2

### a13xbb · 2025-12-12

@Qubitium still does not work for me...
By the way if I do "pip install --upgrade setuptools", I get some other error

Traceback (most recent call last):
    File "/usr/local/lib/python3.11/dist-packages/pip/_vendor/pyproject_hooks/_in_process/_in_process.py", line 389, in <module>
      main()
    File "/usr/local/lib/python3.11/dist-packages/pip/_vendor/pyproject_hooks/_in_process/_in_process.py", line 373, in main
      json_out["return_val"] = hook(**hook_input["kwargs"])
                               ^^^^^^^^^^^^^^^^^^^^^^^^^^^^
    File "/usr/local/lib/python3.11/dist-packages/pip/_vendor/pyproject_hooks/_in_process/_in_process.py", line 280, in build_wheel
      return _build_backend().build_wheel(
             ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
    File "/usr/local/lib/python3.11/dist-packages/setuptools/build_meta.py", line 435, in build_wheel
      return _build(['bdist_wheel', '--dist-info-dir', str(metadata_directory)])
             ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
    File "/usr/local/lib/python3.11/dist-packages/setuptools/build_meta.py", line 423, in _build
      return self._build_with_temp_dir(
             ^^^^^^^^^^^^^^^^^^^^^^^^^^
    File "/usr/local/lib/python3.11/dist-packages/setuptools/build_meta.py", line 404, in _build_with_temp_dir
      self.run_setup()
    File "/usr/local/lib/python3.11/dist-packages/setuptools/build_meta.py", line 317, in run_setup
      exec(code, locals())
    File "<string>", line 877, in <module>
    File "/usr/local/lib/python3.11/dist-packages/setuptools/__init__.py", line 115, in setup
      return distutils.core.setup(**attrs)
             ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
    File "/usr/local/lib/python3.11/dist-packages/setuptools/_distutils/core.py", line 186, in setup
      return run_commands(dist)
             ^^^^^^^^^^^^^^^^^^
    File "/usr/local/lib/python3.11/dist-packages/setuptools/_distutils/core.py", line 202, in run_commands
      dist.run_commands()
    File "/usr/local/lib/python3.11/dist-packages/setuptools/_distutils/dist.py", line 1002, in run_commands
      self.run_command(cmd)
    File "/usr/local/lib/python3.11/dist-packages/setuptools/dist.py", line 1102, in run_command
      super().run_command(command)
    File "/usr/local/lib/python3.11/dist-packages/setuptools/_distutils/dist.py", line 1021, in run_command
      cmd_obj.run()
    File "<string>", line 859, in run
    File "/usr/local/lib/python3.11/dist-packages/setuptools/command/bdist_wheel.py", line 370, in run
      self.run_command("build")
    File "/usr/local/lib/python3.11/dist-packages/setuptools/_distutils/cmd.py", line 357, in run_command
      self.distribution.run_command(command)
    File "/usr/local/lib/python3.11/dist-packages/setuptools/dist.py", line 1102, in run_command
      super().run_command(command)
    File "/usr/local/lib/python3.11/dist-packages/setuptools/_distutils/dist.py", line 1021, in run_command
      cmd_obj.run()
    File "/usr/local/lib/python3.11/dist-packages/setuptools/_distutils/command/build.py", line 135, in run
      self.run_command(cmd_name)
    File "/usr/local/lib/python3.11/dist-packages/setuptools/_distutils/cmd.py", line 357, in run_command
      self.distribution.run_command(command)
    File "/usr/local/lib/python3.11/dist-packages/setuptools/dist.py", line 1102, in run_command
      super().run_command(command)
    File "/usr/local/lib/python3.11/dist-packages/setuptools/_distutils/dist.py", line 1021, in run_command
      cmd_obj.run()
    File "/usr/local/lib/python3.11/dist-packages/setuptools/command/build_ext.py", line 96, in run
      _build_ext.run(self)
    File "/usr/local/lib/python3.11/dist-packages/setuptools/_distutils/command/build_ext.py", line 368, in run
      self.build_extensions()
    File "/usr/local/lib/python3.11/dist-packages/torch/utils/cpp_extension.py", line 1082, in build_extensions
      build_ext.build_extensions(self)
    File "/usr/local/lib/python3.11/dist-packages/setuptools/_distutils/command/build_ext.py", line 484, in build_extensions
      self._build_extensions_serial()
    File "/usr/local/lib/python3.11/dist-packages/setuptools/_distutils/command/build_ext.py", line 510, in _build_extensions_serial
      self.build_extension(ext)
    File "/usr/local/lib/python3.11/dist-packages/setuptools/command/build_ext.py", line 261, in build_extension
      _build_ext.build_extension(self, ext)
    File "/usr/local/lib/python3.11/dist-packages/Cython/Distutils/build_ext.py", line 135, in build_extension
      super(build_ext, self).build_extension(ext)
    File "/usr/local/lib/python3.11/dist-packages/setuptools/_distutils/command/build_ext.py", line 565, in build_extension
      objects = self.compiler.compile(
                ^^^^^^^^^^^^^^^^^^^^^^
    File "/usr/local/lib/python3.11/dist-packages/torch/utils/cpp_extension.py", line 866, in unix_wrap_ninja_compile
      _write_ninja_file_and_compile_objects(
    File "/usr/local/lib/python3.11/dist-packages/torch/utils/cpp_extension.py", line 2223, in _write_ninja_file_and_compile_objects
      _run_ninja_build(
    File "/usr/local/lib/python3.11/dist-packages/torch/utils/cpp_extension.py", line 2614, in _run_ninja_build
      raise RuntimeError(message) from e
  RuntimeError: Error compiling objects for extension
  error: subprocess-exited-with-error
  
  × Building wheel for GPTQModel (pyproject.toml) did not run successfully.
  │ exit code: 1
  ╰─> No available output.
  
  note: This error originates from a subprocess, and is likely not a problem with pip.
  full command: /usr/bin/python3 /usr/local/lib/python3.11/dist-packages/pip/_vendor/pyproject_hooks/_in_process/_in_process.py build_wheel /tmp/tmptv_5t779
  cwd: /kaggle/working/GPTQModel
  Building wheel for GPTQModel (pyproject.toml) ... error
  ERROR: Failed building wheel for GPTQModel
  Running command Building wheel for device-smi (pyproject.toml)
  [12/12/25 12:36:12] WARNING  toml section missing       pyproject_reading.py:215
                               PosixPath('pyproject.toml'
                               ) does not contain a
                               tool.setuptools_scm
                               section
