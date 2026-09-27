# [Issue #165] Facing error in running sdk_sample DCGMReader.py

source: https://github.com/NVIDIA/DCGM/issues/165
state: open | updated: 2025-09-25T11:04:13Z
labels: 

## 正文

/test1/DCGM/sdk_samples$ cmake .
CMake Error at CMakeLists.txt:18 (install):
  install FILES given no DESTINATION!


-- Configuring incomplete, errors occurred!

Tried exporting DESTINATION variable with a empty directory. Still getting same error.
Can this be run inside container only ?

Please let me know, how to build and run DCGMReader.py.


## 评论 (3)

### nikkon-dev · 2024-05-08

@premalathak12,

DCGM build system is designed to run inside the dcgm build container (the `dcgmbuild` directory provides a way to make it).
Our Cmake does not support in-tree build, and sdk_samples are part of the whole project build - it requires the environment defined in the top-level CMakeLists.txt

### premalathak12 · 2024-05-09

@nikkon-dev I have not builded as i was getting some errors but installed the datacentre-gpu-manager. In the /usr/local/bindings/ able to run dcgm_example.py. Copied the dcgm_readerexampley.py from sdk_samples and tried to run it. I got a error : 
``` File "/usr/local/dcgm/bindings/python3/DcgmReader.py", line 402, in GetFieldMetadata
    self.LogDebug("fieldGroupId: " + findByNameId  + "\n")
TypeError: can only concatenate str (not "c_void_p") to strFile "/usr/local/dcgm/bindings/python3/DcgmReader.py", line 402, in GetFieldMetadata
    self.LogDebug("fieldGroupId: " + findByNameId  + "\n")
TypeError: can only concatenate str (not "c_void_p") to str 
```
So added it as str(findByNameId). That error got resolved. 

Now when i run DCGMreaderexample.py again, i am getting Using custom fields through the dictionary interface...
For gpu 0 field mem_copy_utilization=0
For gpu 0 field gpu_utilization=0
For gpu 0 field power_usage=14.762

```
Processing in field order by overriding the CustomerDataHandler() method
Traceback (most recent call last):
  File "/usr/local/dcgm/bindings/test.py", line 95, in <module>
    main()
  File "/usr/local/dcgm/bindings/test.py", line 88, in main
    cdr.Process()
  File "/usr/local/dcgm/bindings/python3/DcgmReader.py", line 442, in Process
    self.Reconnect()
  File "/usr/local/dcgm/bindings/python3/DcgmReader.py", line 346, in Reconnect
    self.InitializeFromHandle()
  File "/usr/local/dcgm/bindings/python3/DcgmReader.py", line 316, in InitializeFromHandle
    self.GetFieldMetadata()
  File "/usr/local/dcgm/bindings/python3/DcgmReader.py", line 407, in GetFieldMetadata
    self.m_fieldGroups[interval] = pydcgm.DcgmFieldGroup(self.m_dcgmHandle, fieldGroupName, fieldIds)
  File "/usr/local/dcgm/bindings/python3/DcgmFieldGroup.py", line 45, in __init__
    self.fieldGroupId = dcgm_agent.dcgmFieldGroupCreate(self._dcgmHandle.handle, fieldIds, name)
  File "/usr/local/dcgm/bindings/python3/dcgm_agent.py", line 52, in wrapper
    return fn(*newargs, **newkwargs)
  File "/usr/local/dcgm/bindings/python3/dcgm_agent.py", line 289, in dcgmFieldGroupCreate
    dcgm_structs._dcgmCheckReturn(ret)
  File "/usr/local/dcgm/bindings/python3/dcgm_structs.py", line 619, in _dcgmCheckReturn
    raise DCGMError(ret)
dcgm_structs.DCGMError_DuplicateKey: Duplicate key passed to function
```

Is this a valid approach ? Please suggest me a way to resolve this error, So i can see the output of DCGMReaderExample ?


### Fjf · 2025-09-25

@premalathak12 I had the same problem as you and described my solution in this other ticket: https://github.com/NVIDIA/DCGM/issues/35#issuecomment-3333419052

