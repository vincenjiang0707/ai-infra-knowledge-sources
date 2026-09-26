# [Issue #69] If metrics yaml files are missing, rocprofv3 segfaults.

source: https://github.com/ROCm/rocprofiler-sdk/issues/69
state: closed | updated: 2025-08-07T18:25:46Z
labels: 

## 正文

I had a bug in my packaging script which was excluding the metrics yaml files. The result was a SEGFAULT. It looks like this code is trying to abort with a nice error, but is crashing on file not found before the error checking:

```
    auto reload_func = [&]() {
        auto counters_path = findViaEnvironment("counter_defs.yaml");
        ROCP_FATAL_IF(!common::filesystem::exists(counters_path))
            << "metric xml file '" << counters_path << "' does not exist";
        return std::make_shared<counter_metrics_t>(loadYAML(counters_path, add_metric));
    };
```

Stack trace:

```
Thread 1 "hipblaslt-test" received signal SIGSEGV, Segmentation fault.
0x00007ffff3b560b8 in std::basic_ostream<char, std::char_traits<char> >::sentry::sentry(std::basic_ostream<char, std::char_traits<char> >&) () from /lib/x86_64-linux-gnu/libstdc++.so.6
(gdb) bt
#0  0x00007ffff3b560b8 in std::basic_ostream<char, std::char_traits<char> >::sentry::sentry(std::basic_ostream<char, std::char_traits<char> >&) () from /lib/x86_64-linux-gnu/libstdc++.so.6
#1  0x00007ffff3b56c3f in std::basic_ostream<char, std::char_traits<char> >& std::__ostream_insert<char, std::char_traits<char> >(std::basic_ostream<char, std::char_traits<char> >&, char const*, long) ()
   from /lib/x86_64-linux-gnu/libstdc++.so.6
#2  0x00007ffff3b5713c in std::basic_ostream<char, std::char_traits<char> >& std::operator<< <std::char_traits<char> >(std::basic_ostream<char, std::char_traits<char> >&, char const*) () from /lib/x86_64-linux-gnu/libstdc++.so.6
#3  0x00007ffff774cc4b in operator() (__closure=__closure@entry=0x7fffffffce28) at /home/stella/rock/TheRock/profiler/rocprofiler-sdk/source/lib/rocprofiler-sdk/counters/metrics.cpp:285
#4  0x00007ffff774d5ce in operator() (__closure=<optimized out>) at /home/stella/rock/TheRock/profiler/rocprofiler-sdk/source/lib/rocprofiler-sdk/counters/metrics.cpp:290
#5  rocprofiler::counters::loadMetrics (reload=reload@entry=false, add_metric=std::optional [no contained value]) at /home/stella/rock/TheRock/profiler/rocprofiler-sdk/source/lib/rocprofiler-sdk/counters/metrics.cpp:290
#6  0x00007ffff774d926 in rocprofiler::counters::getMetricsForAgent (agent="gfx1100") at /home/stella/rock/TheRock/profiler/rocprofiler-sdk/source/lib/rocprofiler-sdk/counters/metrics.cpp:331
#7  0x00007ffff7286cdc in rocprofiler_iterate_agent_supported_counters (agent_id=..., cb=0x7ffff7b73f40 <_FUN(rocprofiler_agent_id_t, rocprofiler_counter_id_t*, size_t, void*)>, user_data=0x5555559969f8)
    at /usr/include/c++/13/bits/basic_string.tcc:242
#8  0x00007ffff7b705aa in rocprofiler::tool::metadata::init (this=0x555555996990) at /home/stella/rock/TheRock/profiler/rocprofiler-sdk/source/lib/output/metadata.cpp:167
#9  0x00007ffff7aae801 in tool_init (fini_func=<optimized out>, tool_data=0x0) at /home/stella/rock/TheRock/profiler/rocprofiler-sdk/source/lib/rocprofiler-sdk-tool/tool.cpp:1689
#10 0x00007ffff729e964 in rocprofiler::registration::(anonymous namespace)::invoke_client_initializers () at /home/stella/rock/TheRock/profiler/rocprofiler-sdk/source/lib/rocprofiler-sdk/registration.cpp:554
#11 operator() (__closure=<optimized out>) at /home/stella/rock/TheRock/profiler/rocprofiler-sdk/source/lib/rocprofiler-sdk/registration.cpp:689
#12 0x00007ffff36a1ed3 in __pthread_once_slow (once_control=0x7ffff79973b0 <rocprofiler::registration::initialize()::_once>, init_routine=0x7ffff3aeb420 <__once_proxy>) at ./nptl/pthread_once.c:116
#13 0x00007ffff7299c84 in __gthread_once (__func=<optimized out>, __once=0x7ffff79973b0 <rocprofiler::registration::initialize()::_once>) at /usr/include/x86_64-linux-gnu/c++/13/bits/gthr-default.h:700
#14 std::call_once<rocprofiler::registration::initialize()::<lambda()> > (__once=..., __f=...) at /usr/include/c++/13/mutex:907
#15 rocprofiler::registration::initialize () at /home/stella/rock/TheRock/profiler/rocprofiler-sdk/source/lib/rocprofiler-sdk/registration.cpp:678
#16 0x00007ffff724ebdb in rocprofiler::shared_library::(anonymous namespace)::lifetime::lifetime (
    this=0x7ffff79b6138 <rocprofiler::common::static_object<rocprofiler::shared_library::(anonymous namespace)::lifetime, rocprofiler::common::(anonymous namespace)::anonymous>::m_buffer>)
    at /home/stella/rock/TheRock/profiler/rocprofiler-sdk/source/lib/rocprofiler-sdk/shared_library.cpp:49
#17 rocprofiler::common::static_object<rocprofiler::shared_library::(anonymous namespace)::lifetime, rocprofiler::common::(anonymous namespace)::anonymous>::construct<>(void) ()
    at /home/stella/rock/TheRock/profiler/rocprofiler-sdk/source/lib/common/static_object.hpp:132
#18 0x00007ffff724ecf9 in rocprofiler::shared_library::(anonymous namespace)::get_lifetime () at /home/stella/rock/TheRock/profiler/rocprofiler-sdk/source/lib/rocprofiler-sdk/shared_library.cpp:67
#19 0x00007ffff7fca71f in call_init (l=<optimized out>, argc=argc@entry=1, argv=argv@entry=0x7fffffffdaf8, env=env@entry=0x7fffffffdb08) at ./elf/dl-init.c:74
#20 0x00007ffff7fca824 in call_init (env=<optimized out>, argv=<optimized out>, argc=<optimized out>, l=<optimized out>) at ./elf/dl-init.c:120
#21 _dl_init (main_map=0x7ffff7ffe2e0, argc=1, argv=0x7fffffffdaf8, env=0x7fffffffdb08) at ./elf/dl-init.c:121
#22 0x00007ffff7fe45a0 in _dl_start_user () from /lib64/ld-linux-x86-64.so.2
#23 0x0000000000000001 in ?? ()
#24 0x00007fffffffdeea in ?? ()
#25 0x0000000000000000 in ?? ()
(gdb)
```

Repro:
* Delete `rm ../share/rocprofiler-sdk/*.yaml`
* `./rocprofv3 -r -- ./hipblaslt-test` (or some other workload)

## 评论 (1)

### systems-assistant[bot] · 2025-08-07

This issue has been migrated to: https://github.com/ROCm/rocm-systems/issues/135
