# [Issue #279] Weird interactions between CLI filtering args and standalone gui 

source: https://github.com/ROCm/rocprofiler-compute/issues/279
state: closed | updated: 2025-08-06T18:33:59Z
labels: bug

## 正文

E.g., if you launch the gui with:

```
omniperf analyze -p workloads/test/MI300A_A1/ -k 0 -b 16 17 --gui
```

things like the memory chart will break with e.g.:

```
Traceback (most recent call last):
  File "~miniconda/envs/omniperf/lib/python3.12/site-packages/flask/app.py", line 1463, in wsgi_app
    response = self.full_dispatch_request()
               ^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "~miniconda/envs/omniperf/lib/python3.12/site-packages/flask/app.py", line 872, in full_dispatch_request
    rv = self.handle_user_exception(e)
         ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "~miniconda/envs/omniperf/lib/python3.12/site-packages/flask/app.py", line 870, in full_dispatch_request
    rv = self.dispatch_request()
         ^^^^^^^^^^^^^^^^^^^^^^^
  File "~miniconda/envs/omniperf/lib/python3.12/site-packages/flask/app.py", line 855, in dispatch_request
    return self.ensure_sync(self.view_functions[rule.endpoint])(**view_args)  # type: ignore[no-any-return]
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "~miniconda/envs/omniperf/lib/python3.12/site-packages/dash/dash.py", line 1310, in dispatch
    ctx.run(
  File "~miniconda/envs/omniperf/lib/python3.12/site-packages/dash/_callback.py", line 442, in add_context
    output_value = func(*func_args, **func_kwargs)  # %% callback invoked %%
                   ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "~miniconda/envs/omniperf/bin/omniperf_analyze/analysis_webui.py", line 162, in generate_from_filter
    get_memchart(panel_configs[300]["data source"], base_data[base_run])
  File "~miniconda/envs/omniperf/bin/utils/gui_components/memchart.py", line 1954, in get_memchart
    insert_chart_data(mem_data, base_data),
    ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "~miniconda/envs/omniperf/bin/utils/gui_components/memchart.py", line 65, in insert_chart_data
    children=memchart_values["Wavefront Occupancy"],
             ~~~~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^
KeyError: 'Wavefront Occupancy'
```

presumably, because we filtered it out already.  We should _probably_ ignore any filtering arguments for the GUI, since we let you change the filters there?

Don't need to fix for 2.x tho.

## 评论 (2)

### systems-assistant[bot] · 2025-08-06

This issue has been migrated to: https://github.com/ROCm/rocm-systems/issues/67

### amd-hsivasun · 2025-08-06

Imported to ROCm/rocm-systems
