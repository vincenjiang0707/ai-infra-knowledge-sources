# [Issue #1644] UCCL backend build fails: uccl_engine_connect is called with int gpu_index instead of const char*

source: https://github.com/ai-dynamo/nixl/issues/1644
state: closed | updated: 2026-07-02T11:31:58Z
labels: Network

## 正文

Building the UCCL backend fails in src/plugins/uccl/uccl_backend.cpp inside loadRemoteConnInfo.

Failure:
```
[155/232] Compiling C++ object src/plugins/uccl/libplugin_UCCL.so.p/uccl_backend.cpp.o
FAILED: [code=1] src/plugins/uccl/libplugin_UCCL.so.p/uccl_backend.cpp.o
../src/plugins/uccl/uccl_backend.cpp:241:56: error: invalid conversion from ‘int’ to ‘const char*’ [-fpermissive]
  241 |     conn = uccl_engine_connect(engine_, ip_addr.get(), gpu_index, port);
      |                                                        ^~~~~~~~~
      |                                                        |
      |                                                        int
/home/manojgop/install/uccl/include/uccl_engine.h:54:46: note: initializing argument 3 of ‘uccl_conn_t* uccl_engine_connect(uccl_engine_t*, const char*, const char*, int, bool)’
   54 |                                  char const* remote_gpu, int remote_port,
      |                                  ~~~~~~~~~~~~^~~~~~~~~~
```

Root cause:
uccl_engine_connect expects remote_gpu as a const char* but gpu_index is passed as an int.

Proposed fix:
```
+    std::string gpu_index_str = std::to_string(gpu_index);
-    conn = uccl_engine_connect(engine_, ip_addr.get(), gpu_index, port);
+    conn = uccl_engine_connect(engine_, ip_addr.get(), gpu_index_str.c_str(), port);
```

## 评论 (3)

### praveingk · 2026-05-15

@manojgop Please use https://github.com/ai-dynamo/nixl/pull/1428 for now, due to breaking API changes

### brminich · 2026-05-27

@manojgop can you pls verify the issue is fixed?
#1428 is merged

### manojgop · 2026-05-27

> [@manojgop](https://github.com/manojgop) can you pls verify the issue is fixed? [#1428](https://github.com/ai-dynamo/nixl/pull/1428) is merged

Verified. This issue is fixed. This issue can be closed
