# [Issue #35] Errors in DcgmReaderExample.py 

source: https://github.com/NVIDIA/DCGM/issues/35
state: open | updated: 2025-09-25T18:49:04Z
labels: bug

## 正文

Hi, there is an error when I tried to test `/usr/local/dcgm/sdk_samples/scripts/DcgmReaderExample.py`. Could you help me figure out what's wrong with it?

```
Processing in field order by overriding the CustomerDataHandler() method
type of findBynameid <class 'ctypes.c_void_p'>
c_void_p(12)
Traceback (most recent call last):
  File "DcgmReaderExample.py", line 95, in <module>
    main()
  File "DcgmReaderExample.py", line 88, in main
    cdr.Process()
  File "/usr/local/dcgm/bindings/python3/DcgmReader.py", line 440, in Process
    self.Reconnect()
  File "/usr/local/dcgm/bindings/python3/DcgmReader.py", line 342, in Reconnect
    self.InitializeFromHandle()
  File "/usr/local/dcgm/bindings/python3/DcgmReader.py", line 312, in InitializeFromHandle
    self.GetFieldMetadata()
  File "/usr/local/dcgm/bindings/python3/DcgmReader.py", line 400, in GetFieldMetadata
    self.LogInfo("fieldGroupId: " + findByNameId  + "\n")
TypeError: can only concatenate str (not "c_void_p") to str
```

## 评论 (2)

### bstollenvidia · 2023-02-27

I confirmed this is still present in 3.1.6
https://github.com/NVIDIA/DCGM/blob/4aedfaae1f7c8480e46b8c835ddd5afbd00d57be/testing/python3/DcgmReader.py#L400

### Fjf · 2025-09-25

Maybe no longer relevant for you but I found changing the fieldgroupName when instantiating the DcgmReader to anything other than the base value will solve this. The default is dcgm_fieldgroupData, and I'm not sure what was wrong with that fieldgroupData in my environment, but just changing the name triggered dcgm to create a new group and that makes it return values again.
