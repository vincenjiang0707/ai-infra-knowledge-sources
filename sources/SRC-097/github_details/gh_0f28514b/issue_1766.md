# [Issue #1766] [BUG] In file-path mode, a double free can occur

source: https://github.com/ai-dynamo/nixl/issues/1766
state: closed | updated: 2026-06-22T07:46:31Z
labels: 

## 正文

Path mode from PR https://github.com/ai-dynamo/nixl/pull/1635 introduces a path to a bug.  If two exact same regions get registered twice: they collapse to the same sort keys so the sequence: register(A), register(A), deregister(A), deregister(A) causes a double free on the second deregister.

The bug:

```
nixlBlobDesc file1, file2;

file1.addr = 0;
file1.size=4096;
file1.metaInfo = std::string("rw:file1.bin");
file2.addr = 0;
file2.size = 4096;
file2.metainfo = std::string("rw:file2.bin");

nixl_reg_dlist_t file_descs(FILE_SEG)
file_descs.addDesc(file1);
file_descs.addDesc(file2);

agent.registerMem(file_descs);

agent.deregisterMem(file_descs); <-- will cause a double free of file1
```

The workaround:
```
nixlBlobDesc file1, file2;

file1.devId = 1;
file1.addr = 0;
file1.size=4096;
file1.metaInfo = std::string("rw:file1.bin");
file2.devId = 2; <-- unique devId per file
file2.addr = 0;
file2.size = 4096;
file2.metainfo = std::string("rw:file2.bin");

nixl_reg_dlist_t file_descs(FILE_SEG)
file_descs.addDesc(file1);
file_descs.addDesc(file2);

agent.registerMem(file_descs);

agent.deregisterMem(file_descs);
```


The workaround is to use a unique devId per file.  This will keep the io descriptors unique so the behavior will not occur.

## 评论 (1)

### lluki · 2026-06-17

Note, this is a bit more generic, i described the impact on different backends here: https://github.com/ai-dynamo/nixl/issues/1792


