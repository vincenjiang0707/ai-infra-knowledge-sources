# [Issue #57] Unsupported SOC version: Ascend310B4

source: https://github.com/Ascend/pytorch/issues/57
state: open | updated: 2025-02-05T06:22:39Z
labels: 

## 正文

System environment:
CANN=7.0.RC1 inner_version=V100R001C13SPC005B246
python=3.10
torch=2.1.0
torch_npu=2.1.0rc1

Code example:
```python
def grid_computing_ascend(longitude, latitude, height, vertices):
    """
    使用Ascend PyTorch加速的网格内部碰撞计算（Ascend GPU）
    """
    import torch_npu
    # 将输入数据转换为PyTorch张量，并迁移到Ascend设备
    x_tensor = torch.tensor(longitude, dtype=torch.float32).npu()
    y_tensor = torch.tensor(latitude, dtype=torch.float32).npu()
    h_tensor = torch.tensor(height, dtype=torch.float32).npu()
    vertices_tensor = torch.tensor(vertices, dtype=torch.float32).npu()
    query_points = torch.stack((x_tensor, y_tensor, h_tensor), dim=1)
    distances = torch.norm(query_points.unsqueeze(1) - vertices_tensor, dim=2)
    is_safe = distances > settings.COLLISION.SAFE_RADIUS
    return torch.all(is_safe)
```

The complete error message is as follows:
Traceback (most recent call last):
  File "/home/HwHiAiUser/.conda/envs/compute/lib/python3.10/runpy.py", line 196, in _run_module_as_main
    return _run_code(code, main_globals, None,
           │         │     └ {'__name__': '__main__', '__doc__': None, '__package__': 'uvicorn', '__loader__': <_frozen_importlib_external.SourceFileLoade...
           │         └ <code object <module> at 0xe7ffd47110b0, file "/home/HwHiAiUser/.vscode/extensions/ms-python.debugpy-2024.14.0-linux-arm64/bu...
           └ <function _run_code at 0xe7ffd4546320>
  File "/home/HwHiAiUser/.conda/envs/compute/lib/python3.10/runpy.py", line 86, in _run_code
    exec(code, run_globals)
         │     └ {'__name__': '__main__', '__doc__': None, '__package__': 'uvicorn', '__loader__': <_frozen_importlib_external.SourceFileLoade...
         └ <code object <module> at 0xe7ffd47110b0, file "/home/HwHiAiUser/.vscode/extensions/ms-python.debugpy-2024.14.0-linux-arm64/bu...

  File "/home/HwHiAiUser/.vscode/extensions/ms-python.debugpy-2024.14.0-linux-arm64/bundled/libs/debugpy/adapter/../../debugpy/launcher/../../debugpy/__main__.py", line 71, in <module>
    cli.main()
    │   └ <function main at 0xe7ffd2ec8f70>
    └ <module 'debugpy.server.cli' from '/home/HwHiAiUser/.vscode/extensions/ms-python.debugpy-2024.14.0-linux-arm64/bundled/libs/d...

  File "/home/HwHiAiUser/.vscode/extensions/ms-python.debugpy-2024.14.0-linux-arm64/bundled/libs/debugpy/adapter/../../debugpy/launcher/../../debugpy/../debugpy/server/cli.py", line 501, in main
    run()
    └ <function run_module at 0xe7ffd2ec8dc0>

  File "/home/HwHiAiUser/.vscode/extensions/ms-python.debugpy-2024.14.0-linux-arm64/bundled/libs/debugpy/adapter/../../debugpy/launcher/../../debugpy/../debugpy/server/cli.py", line 384, in run_module
    run_module_as_main(options.target, alter_argv=True)
    │                  │       └ 'uvicorn'
    │                  └ <debugpy.server.cli.Options object at 0xe7ffd3056d40>
    └ <function _run_module_as_main at 0xe7ffd341eb00>

  File "/home/HwHiAiUser/.vscode/extensions/ms-python.debugpy-2024.14.0-linux-arm64/bundled/libs/debugpy/_vendored/pydevd/_pydevd_bundle/pydevd_runpy.py", line 228, in _run_module_as_main
    return _run_code(code, main_globals, None, "__main__", mod_spec)
           │         │     │                               └ ModuleSpec(name='uvicorn.__main__', loader=<_frozen_importlib_external.SourceFileLoader object at 0xe7ffd1d3f250>, origin='/h...
           │         │     └ {'__name__': '__main__', '__doc__': None, '__package__': 'uvicorn', '__loader__': <_frozen_importlib_external.SourceFileLoade...
           │         └ <code object <module> at 0xe7ffd2ed10b0, file "/home/HwHiAiUser/.conda/envs/compute/lib/python3.10/site-packages/uvicorn/__ma...
           └ <function _run_code at 0xe7ffd341e5f0>

  File "/home/HwHiAiUser/.vscode/extensions/ms-python.debugpy-2024.14.0-linux-arm64/bundled/libs/debugpy/_vendored/pydevd/_pydevd_bundle/pydevd_runpy.py", line 118, in _run_code
    exec(code, run_globals)
         │     └ {'__name__': '__main__', '__doc__': None, '__package__': 'uvicorn', '__loader__': <_frozen_importlib_external.SourceFileLoade...
         └ <code object <module> at 0xe7ffd2ed10b0, file "/home/HwHiAiUser/.conda/envs/compute/lib/python3.10/site-packages/uvicorn/__ma...

  File "/home/HwHiAiUser/.conda/envs/compute/lib/python3.10/site-packages/uvicorn/__main__.py", line 4, in <module>
    uvicorn.main()
    │       └ <Command main>
    └ <module 'uvicorn' from '/home/HwHiAiUser/.conda/envs/compute/lib/python3.10/site-packages/uvicorn/__init__.py'>
  File "/home/HwHiAiUser/.conda/envs/compute/lib/python3.10/site-packages/click/core.py", line 1157, in __call__
    return self.main(*args, **kwargs)
           │    │     │       └ {}
           │    │     └ ()
           │    └ <function BaseCommand.main at 0xe7ffd02ef6d0>
           └ <Command main>
  File "/home/HwHiAiUser/.conda/envs/compute/lib/python3.10/site-packages/click/core.py", line 1078, in main
    rv = self.invoke(ctx)
         │    │      └ <click.core.Context object at 0xe7ffd1d3eb00>
         │    └ <function Command.invoke at 0xe7ffd03041f0>
         └ <Command main>
  File "/home/HwHiAiUser/.conda/envs/compute/lib/python3.10/site-packages/click/core.py", line 1434, in invoke
    return ctx.invoke(self.callback, **ctx.params)
           │   │      │    │           │   └ {'host': '0.0.0.0', 'app': 'main:app', 'port': 8000, 'uds': None, 'fd': None, 'reload': False, 'reload_dirs': (), 'reload_inc...
           │   │      │    │           └ <click.core.Context object at 0xe7ffd1d3eb00>
           │   │      │    └ <function main at 0xe7ffd020eef0>
           │   │      └ <Command main>
           │   └ <function Context.invoke at 0xe7ffd02eeef0>
           └ <click.core.Context object at 0xe7ffd1d3eb00>
  File "/home/HwHiAiUser/.conda/envs/compute/lib/python3.10/site-packages/click/core.py", line 783, in invoke
    return __callback(*args, **kwargs)
                       │       └ {'host': '0.0.0.0', 'app': 'main:app', 'port': 8000, 'uds': None, 'fd': None, 'reload': False, 'reload_dirs': (), 'reload_inc...
                       └ ()
  File "/home/HwHiAiUser/.conda/envs/compute/lib/python3.10/site-packages/uvicorn/main.py", line 412, in main
    run(
    └ <function run at 0xe7ffd0194b80>
  File "/home/HwHiAiUser/.conda/envs/compute/lib/python3.10/site-packages/uvicorn/main.py", line 579, in run
    server.run()
    │      └ <function Server.run at 0xe7ffd0194430>
    └ <uvicorn.server.Server object at 0xe7ffd01e7460>
  File "/home/HwHiAiUser/.conda/envs/compute/lib/python3.10/site-packages/uvicorn/server.py", line 66, in run
    return asyncio.run(self.serve(sockets=sockets))
           │       │   │    │             └ None
           │       │   │    └ <function Server.serve at 0xe7ffd01944c0>
           │       │   └ <uvicorn.server.Server object at 0xe7ffd01e7460>
           │       └ <function run at 0xe7ffd03af250>
           └ <module 'asyncio' from '/home/HwHiAiUser/.conda/envs/compute/lib/python3.10/asyncio/__init__.py'>
  File "/home/HwHiAiUser/.conda/envs/compute/lib/python3.10/asyncio/runners.py", line 44, in run
    return loop.run_until_complete(main)
           │    │                  └ <coroutine object Server.serve at 0xe7ffd01f9070>
           │    └ <function BaseEventLoop.run_until_complete at 0xe7ffd03ad5a0>
           └ <_UnixSelectorEventLoop running=True closed=False debug=False>
  File "/home/HwHiAiUser/.conda/envs/compute/lib/python3.10/asyncio/base_events.py", line 636, in run_until_complete
    self.run_forever()
    │    └ <function BaseEventLoop.run_forever at 0xe7ffd03ad510>
    └ <_UnixSelectorEventLoop running=True closed=False debug=False>
  File "/home/HwHiAiUser/.conda/envs/compute/lib/python3.10/asyncio/base_events.py", line 603, in run_forever
    self._run_once()
    │    └ <function BaseEventLoop._run_once at 0xe7ffd03af010>
    └ <_UnixSelectorEventLoop running=True closed=False debug=False>
  File "/home/HwHiAiUser/.conda/envs/compute/lib/python3.10/asyncio/base_events.py", line 1909, in _run_once
    handle._run()
    │      └ <function Handle._run at 0xe7ffd1dda170>
    └ <Handle <TaskStepMethWrapper object at 0xe7ff88c39810>()>
  File "/home/HwHiAiUser/.conda/envs/compute/lib/python3.10/asyncio/events.py", line 80, in _run
    self._context.run(self._callback, *self._args)
    │    │            │    │           │    └ <member '_args' of 'Handle' objects>
    │    │            │    │           └ <Handle <TaskStepMethWrapper object at 0xe7ff88c39810>()>
    │    │            │    └ <member '_callback' of 'Handle' objects>
    │    │            └ <Handle <TaskStepMethWrapper object at 0xe7ff88c39810>()>
    │    └ <member '_context' of 'Handle' objects>
    └ <Handle <TaskStepMethWrapper object at 0xe7ff88c39810>()>
  File "/home/HwHiAiUser/.conda/envs/compute/lib/python3.10/site-packages/uvicorn/protocols/http/h11_impl.py", line 403, in run_asgi
    result = await app(  # type: ignore[func-returns-value]
                   └ <uvicorn.middleware.proxy_headers.ProxyHeadersMiddleware object at 0xe7ffd1d3f970>
  File "/home/HwHiAiUser/.conda/envs/compute/lib/python3.10/site-packages/uvicorn/middleware/proxy_headers.py", line 60, in __call__
    return await self.app(scope, receive, send)
                 │    │   │      │        └ <bound method RequestResponseCycle.send of <uvicorn.protocols.http.h11_impl.RequestResponseCycle object at 0xe7ff88c392d0>>
                 │    │   │      └ <bound method RequestResponseCycle.receive of <uvicorn.protocols.http.h11_impl.RequestResponseCycle object at 0xe7ff88c392d0>>
                 │    │   └ {'type': 'http', 'asgi': {'version': '3.0', 'spec_version': '2.3'}, 'http_version': '1.1', 'server': ('10.1.162.187', 8000), ...
                 │    └ <fastapi.applications.FastAPI object at 0xe7ffbbf19e70>
                 └ <uvicorn.middleware.proxy_headers.ProxyHeadersMiddleware object at 0xe7ffd1d3f970>
  File "/home/HwHiAiUser/.conda/envs/compute/lib/python3.10/site-packages/fastapi/applications.py", line 1054, in __call__
    await super().__call__(scope, receive, send)
                           │      │        └ <bound method RequestResponseCycle.send of <uvicorn.protocols.http.h11_impl.RequestResponseCycle object at 0xe7ff88c392d0>>
                           │      └ <bound method RequestResponseCycle.receive of <uvicorn.protocols.http.h11_impl.RequestResponseCycle object at 0xe7ff88c392d0>>
                           └ {'type': 'http', 'asgi': {'version': '3.0', 'spec_version': '2.3'}, 'http_version': '1.1', 'server': ('10.1.162.187', 8000), ...
  File "/home/HwHiAiUser/.conda/envs/compute/lib/python3.10/site-packages/starlette/applications.py", line 113, in __call__
    await self.middleware_stack(scope, receive, send)
          │    │                │      │        └ <bound method RequestResponseCycle.send of <uvicorn.protocols.http.h11_impl.RequestResponseCycle object at 0xe7ff88c392d0>>
          │    │                │      └ <bound method RequestResponseCycle.receive of <uvicorn.protocols.http.h11_impl.RequestResponseCycle object at 0xe7ff88c392d0>>
          │    │                └ {'type': 'http', 'asgi': {'version': '3.0', 'spec_version': '2.3'}, 'http_version': '1.1', 'server': ('10.1.162.187', 8000), ...
          │    └ <starlette.middleware.errors.ServerErrorMiddleware object at 0xe7ff9476e8c0>
          └ <fastapi.applications.FastAPI object at 0xe7ffbbf19e70>
  File "/home/HwHiAiUser/.conda/envs/compute/lib/python3.10/site-packages/starlette/middleware/errors.py", line 165, in __call__
    await self.app(scope, receive, _send)
          │    │   │      │        └ <function ServerErrorMiddleware.__call__.<locals>._send at 0xe7ffa16f25f0>
          │    │   │      └ <bound method RequestResponseCycle.receive of <uvicorn.protocols.http.h11_impl.RequestResponseCycle object at 0xe7ff88c392d0>>
          │    │   └ {'type': 'http', 'asgi': {'version': '3.0', 'spec_version': '2.3'}, 'http_version': '1.1', 'server': ('10.1.162.187', 8000), ...
          │    └ <starlette.middleware.cors.CORSMiddleware object at 0xe7ff9476e860>
          └ <starlette.middleware.errors.ServerErrorMiddleware object at 0xe7ff9476e8c0>
  File "/home/HwHiAiUser/.conda/envs/compute/lib/python3.10/site-packages/starlette/middleware/cors.py", line 85, in __call__
    await self.app(scope, receive, send)
          │    │   │      │        └ <function ServerErrorMiddleware.__call__.<locals>._send at 0xe7ffa16f25f0>
          │    │   │      └ <bound method RequestResponseCycle.receive of <uvicorn.protocols.http.h11_impl.RequestResponseCycle object at 0xe7ff88c392d0>>
          │    │   └ {'type': 'http', 'asgi': {'version': '3.0', 'spec_version': '2.3'}, 'http_version': '1.1', 'server': ('10.1.162.187', 8000), ...
          │    └ <starlette.middleware.exceptions.ExceptionMiddleware object at 0xe7ff9476e830>
          └ <starlette.middleware.cors.CORSMiddleware object at 0xe7ff9476e860>
  File "/home/HwHiAiUser/.conda/envs/compute/lib/python3.10/site-packages/starlette/middleware/exceptions.py", line 62, in __call__
    await wrap_app_handling_exceptions(self.app, conn)(scope, receive, send)
          │                            │    │    │     │      │        └ <function ServerErrorMiddleware.__call__.<locals>._send at 0xe7ffa16f25f0>
          │                            │    │    │     │      └ <bound method RequestResponseCycle.receive of <uvicorn.protocols.http.h11_impl.RequestResponseCycle object at 0xe7ff88c392d0>>
          │                            │    │    │     └ {'type': 'http', 'asgi': {'version': '3.0', 'spec_version': '2.3'}, 'http_version': '1.1', 'server': ('10.1.162.187', 8000), ...
          │                            │    │    └ <starlette.requests.Request object at 0xe7ff88c38e80>
          │                            │    └ <fastapi.routing.APIRouter object at 0xe7ff94becc10>
          │                            └ <starlette.middleware.exceptions.ExceptionMiddleware object at 0xe7ff9476e830>
          └ <function wrap_app_handling_exceptions at 0xe7ffbb338d30>
  File "/home/HwHiAiUser/.conda/envs/compute/lib/python3.10/site-packages/starlette/_exception_handler.py", line 42, in wrapped_app
    await app(scope, receive, sender)
          │   │      │        └ <function wrap_app_handling_exceptions.<locals>.wrapped_app.<locals>.sender at 0xe7ff88c31d80>
          │   │      └ <bound method RequestResponseCycle.receive of <uvicorn.protocols.http.h11_impl.RequestResponseCycle object at 0xe7ff88c392d0>>
          │   └ {'type': 'http', 'asgi': {'version': '3.0', 'spec_version': '2.3'}, 'http_version': '1.1', 'server': ('10.1.162.187', 8000), ...
          └ <fastapi.routing.APIRouter object at 0xe7ff94becc10>
  File "/home/HwHiAiUser/.conda/envs/compute/lib/python3.10/site-packages/starlette/routing.py", line 715, in __call__
    await self.middleware_stack(scope, receive, send)
          │    │                │      │        └ <function wrap_app_handling_exceptions.<locals>.wrapped_app.<locals>.sender at 0xe7ff88c31d80>
          │    │                │      └ <bound method RequestResponseCycle.receive of <uvicorn.protocols.http.h11_impl.RequestResponseCycle object at 0xe7ff88c392d0>>
          │    │                └ {'type': 'http', 'asgi': {'version': '3.0', 'spec_version': '2.3'}, 'http_version': '1.1', 'server': ('10.1.162.187', 8000), ...
          │    └ <bound method Router.app of <fastapi.routing.APIRouter object at 0xe7ff94becc10>>
          └ <fastapi.routing.APIRouter object at 0xe7ff94becc10>
  File "/home/HwHiAiUser/.conda/envs/compute/lib/python3.10/site-packages/starlette/routing.py", line 735, in app
    await route.handle(scope, receive, send)
          │     │      │      │        └ <function wrap_app_handling_exceptions.<locals>.wrapped_app.<locals>.sender at 0xe7ff88c31d80>
          │     │      │      └ <bound method RequestResponseCycle.receive of <uvicorn.protocols.http.h11_impl.RequestResponseCycle object at 0xe7ff88c392d0>>
          │     │      └ {'type': 'http', 'asgi': {'version': '3.0', 'spec_version': '2.3'}, 'http_version': '1.1', 'server': ('10.1.162.187', 8000), ...
          │     └ <function Route.handle at 0xe7ffbb33a5f0>
          └ APIRoute(path='/citygis-computing/securitySituationRating/getRatingResults', name='get_rating_results', methods=['POST'])
  File "/home/HwHiAiUser/.conda/envs/compute/lib/python3.10/site-packages/starlette/routing.py", line 288, in handle
    await self.app(scope, receive, send)
          │    │   │      │        └ <function wrap_app_handling_exceptions.<locals>.wrapped_app.<locals>.sender at 0xe7ff88c31d80>
          │    │   │      └ <bound method RequestResponseCycle.receive of <uvicorn.protocols.http.h11_impl.RequestResponseCycle object at 0xe7ff88c392d0>>
          │    │   └ {'type': 'http', 'asgi': {'version': '3.0', 'spec_version': '2.3'}, 'http_version': '1.1', 'server': ('10.1.162.187', 8000), ...
          │    └ <function request_response.<locals>.app at 0xe7ff94bbf7f0>
          └ APIRoute(path='/citygis-computing/securitySituationRating/getRatingResults', name='get_rating_results', methods=['POST'])
  File "/home/HwHiAiUser/.conda/envs/compute/lib/python3.10/site-packages/starlette/routing.py", line 76, in app
    await wrap_app_handling_exceptions(app, request)(scope, receive, send)
          │                            │    │        │      │        └ <function wrap_app_handling_exceptions.<locals>.wrapped_app.<locals>.sender at 0xe7ff88c31d80>
          │                            │    │        │      └ <bound method RequestResponseCycle.receive of <uvicorn.protocols.http.h11_impl.RequestResponseCycle object at 0xe7ff88c392d0>>
          │                            │    │        └ {'type': 'http', 'asgi': {'version': '3.0', 'spec_version': '2.3'}, 'http_version': '1.1', 'server': ('10.1.162.187', 8000), ...
          │                            │    └ <starlette.requests.Request object at 0xe7ff88c391b0>
          │                            └ <function request_response.<locals>.app.<locals>.app at 0xe7ff88c323b0>
          └ <function wrap_app_handling_exceptions at 0xe7ffbb338d30>
  File "/home/HwHiAiUser/.conda/envs/compute/lib/python3.10/site-packages/starlette/_exception_handler.py", line 42, in wrapped_app
    await app(scope, receive, sender)
          │   │      │        └ <function wrap_app_handling_exceptions.<locals>.wrapped_app.<locals>.sender at 0xe7ff88c32440>
          │   │      └ <bound method RequestResponseCycle.receive of <uvicorn.protocols.http.h11_impl.RequestResponseCycle object at 0xe7ff88c392d0>>
          │   └ {'type': 'http', 'asgi': {'version': '3.0', 'spec_version': '2.3'}, 'http_version': '1.1', 'server': ('10.1.162.187', 8000), ...
          └ <function request_response.<locals>.app.<locals>.app at 0xe7ff88c323b0>
  File "/home/HwHiAiUser/.conda/envs/compute/lib/python3.10/site-packages/starlette/routing.py", line 73, in app
    response = await f(request)
                     │ └ <starlette.requests.Request object at 0xe7ff88c391b0>
                     └ <function get_request_handler.<locals>.app at 0xe7ff94bbf640>
  File "/home/HwHiAiUser/.conda/envs/compute/lib/python3.10/site-packages/fastapi/routing.py", line 301, in app
    raw_response = await run_endpoint_function(
                         └ <function run_endpoint_function at 0xe7ffbb2041f0>
  File "/home/HwHiAiUser/.conda/envs/compute/lib/python3.10/site-packages/fastapi/routing.py", line 212, in run_endpoint_function
    return await dependant.call(**values)
                 │         │      └ {'aircraft_list': [Aircraft(code='A8104', coordinates=Coordinates(longitude=121.41819550868193, latitude=31.48668944574648, h...
                 │         └ <function get_rating_results at 0xe7ff94bbc040>
                 └ Dependant(path_params=[], query_params=[], header_params=[], cookie_params=[], body_params=[ModelField(field_info=Body(Pydant...

> File "/home/HwHiAiUser/code/spatial-computing-services/src/routes/security_situation_rating_router.py", line 13, in get_rating_results
    result = security_situation_rating(aircraft_list)
             │                         └ [Aircraft(code='A8104', coordinates=Coordinates(longitude=121.41819550868193, latitude=31.48668944574648, height=168.92432433...
             └ <function security_situation_rating at 0xe7ff94b27d90>

  File "/home/HwHiAiUser/code/spatial-computing-services/src/decorator/timer.py", line 24, in wrapper
    result = func(*args, **kwargs)
             │     │       └ {}
             │     └ ([Aircraft(code='A8104', coordinates=Coordinates(longitude=121.41819550868193, latitude=31.48668944574648, height=168.9243243...
             └ <function security_situation_rating at 0xe7ff94b27d00>

  File "/home/HwHiAiUser/code/spatial-computing-services/src/routes/security_situation_rating/calculation.py", line 63, in security_situation_rating
    results = list(executor.map(bound_worker, aircraft_list))
                   │        │   │             └ [Aircraft(code='A8104', coordinates=Coordinates(longitude=121.41819550868193, latitude=31.48668944574648, height=168.92432433...
                   │        │   └ functools.partial(<function worker at 0xe7ff94b27c70>, aircraft_coordinates_dict={'A8104': [121.41819550868193, 31.4866894457...
                   │        └ <function Executor.map at 0xe7ffd1dd8160>
                   └ <concurrent.futures.thread.ThreadPoolExecutor object at 0xe7ff88c39ba0>

  File "/home/HwHiAiUser/.conda/envs/compute/lib/python3.10/concurrent/futures/_base.py", line 621, in result_iterator
    yield _result_or_cancel(fs.pop())
          │                 │  └ <method 'pop' of 'list' objects>
          │                 └ [<Future at 0xe7ff88c3a1a0 state=finished raised RuntimeError>, <Future at 0xe7ff88c3a320 state=finished raised RuntimeError>]
          └ <function _result_or_cancel at 0xe7ffd1dcb760>
  File "/home/HwHiAiUser/.conda/envs/compute/lib/python3.10/concurrent/futures/_base.py", line 319, in _result_or_cancel
    return fut.result(timeout)
                      └ None
  File "/home/HwHiAiUser/.conda/envs/compute/lib/python3.10/concurrent/futures/_base.py", line 458, in result
    return self.__get_result()
           └ None
  File "/home/HwHiAiUser/.conda/envs/compute/lib/python3.10/concurrent/futures/_base.py", line 403, in __get_result
    raise self._exception
          └ None
  File "/home/HwHiAiUser/.conda/envs/compute/lib/python3.10/concurrent/futures/thread.py", line 58, in run
    result = self.fn(*self.args, **self.kwargs)
             │        │            └ None
             │        └ None
             └ None

  File "/home/HwHiAiUser/code/spatial-computing-services/src/routes/security_situation_rating/calculation.py", line 46, in worker
    return single_aircraft_rating(aircraft, excluded_aircraft_coordinates_dict)
           │                      │         └ {'A8105': [121.41819550868195, 31.48668944574649, 168.9243243327615], 'A8106': [121.41819550868192, 31.48668944574647, 168.92...
           │                      └ Aircraft(code='A8104', coordinates=Coordinates(longitude=121.41819550868193, latitude=31.48668944574648, height=168.924324332...
           └ <function single_aircraft_rating at 0xe7ff94b27e20>

  File "/home/HwHiAiUser/code/spatial-computing-services/src/routes/security_situation_rating/calculation.py", line 79, in single_aircraft_rating
    collision_rating = rate_collision(aircraft, grid_self_code, excluded_aircraft_coordinates_dict)
                       │              │         │               └ {'A8105': [121.41819550868195, 31.48668944574649, 168.9243243327615], 'A8106': [121.41819550868192, 31.48668944574647, 168.92...
                       │              │         └ 'G001133223-033203-002301.100|000000000000000000110010'
                       │              └ Aircraft(code='A8104', coordinates=Coordinates(longitude=121.41819550868193, latitude=31.48668944574648, height=168.924324332...
                       └ <function rate_collision at 0xe7ff94b27f40>

  File "/home/HwHiAiUser/code/spatial-computing-services/src/routes/security_situation_rating/calculation.py", line 98, in rate_collision
    rating = grid_computing(aircraft, grid_self_code, excluded_aircraft_coordinates_dict)
             │              │         │               └ {'A8105': [121.41819550868195, 31.48668944574649, 168.9243243327615], 'A8106': [121.41819550868192, 31.48668944574647, 168.92...
             │              │         └ 'G001133223-033203-002301.100|000000000000000000110010'
             │              └ Aircraft(code='A8104', coordinates=Coordinates(longitude=121.41819550868193, latitude=31.48668944574648, height=168.924324332...
             └ <function grid_computing at 0xe7ff94b256c0>

  File "/home/HwHiAiUser/code/spatial-computing-services/src/routes/security_situation_rating/gpu_accelerated_computing.py", line 85, in grid_computing
    is_safe, nearest_points = grid_computing_ascend(longitude, latitude, height, filtered_coordinates)
                              │                     │          │         │       └ [[121.41819550868195, 31.48668944574649, 168.9243243327615], [121.41819550868192, 31.48668944574647, 168.9243243327613]]
                              │                     │          │         └ 168.9243243327614
                              │                     │          └ 31.48668944574648
                              │                     └ 121.41819550868193
                              └ <function grid_computing_ascend at 0xe7ff94b25cf0>

  File "/home/HwHiAiUser/code/spatial-computing-services/src/routes/security_situation_rating/gpu_accelerated_computing.py", line 140, in grid_computing_ascend
    x_tensor = torch.tensor(longitude, dtype=torch.float32).npu()
               │     │      │                │     └ torch.float32
               │     │      │                └ <module 'torch' from '/home/HwHiAiUser/.conda/envs/compute/lib/python3.10/site-packages/torch/__init__.py'>
               │     │      └ 121.41819550868193
               │     └ <built-in method tensor of type object at 0xe7ffb238cf10>
               └ <module 'torch' from '/home/HwHiAiUser/.conda/envs/compute/lib/python3.10/site-packages/torch/__init__.py'>

  File "/home/HwHiAiUser/.conda/envs/compute/lib/python3.10/site-packages/torch/utils/backend_registration.py", line 153, in wrap_tensor_to
    device_idx = _normalization_device(custom_backend_name, device)
                 │                     │                    └ None
                 │                     └ 'npu'
                 └ <function _normalization_device at 0xe7ffa202ce50>
  File "/home/HwHiAiUser/.conda/envs/compute/lib/python3.10/site-packages/torch/utils/backend_registration.py", line 109, in _normalization_device
    return _get_current_device_index()
           └ <function _normalization_device.<locals>._get_current_device_index at 0xe7ff88c32d40>
  File "/home/HwHiAiUser/.conda/envs/compute/lib/python3.10/site-packages/torch/utils/backend_registration.py", line 103, in _get_current_device_index
    return getattr(getattr(torch, custom_backend_name), _get_device_index)()
                           │      │                     └ 'current_device'
                           │      └ 'npu'
                           └ <module 'torch' from '/home/HwHiAiUser/.conda/envs/compute/lib/python3.10/site-packages/torch/__init__.py'>
  File "/home/HwHiAiUser/.conda/envs/compute/lib/python3.10/site-packages/torch_npu/npu/utils.py", line 50, in current_device
    torch_npu.npu._lazy_init()
    │         │   └ <function _lazy_init at 0xe7ff9476beb0>
    │         └ <module 'torch_npu.npu' from '/home/HwHiAiUser/.conda/envs/compute/lib/python3.10/site-packages/torch_npu/npu/__init__.py'>
    └ <module 'torch_npu' from '/home/HwHiAiUser/.conda/envs/compute/lib/python3.10/site-packages/torch_npu/__init__.py'>
  File "/home/HwHiAiUser/.conda/envs/compute/lib/python3.10/site-packages/torch_npu/npu/__init__.py", line 197, in _lazy_init
    torch_npu._C._npu_init()
    │         │  └ <built-in function _npu_init>
    │         └ <module 'torch_npu._C' from '/home/HwHiAiUser/.conda/envs/compute/lib/python3.10/site-packages/torch_npu/_C.cpython-310-aarch...
    └ <module 'torch_npu' from '/home/HwHiAiUser/.conda/envs/compute/lib/python3.10/site-packages/torch_npu/__init__.py'>

RuntimeError: Unsupported soc version: Ascend310B4

## 评论 (1)

### yunyiyun · 2025-02-05

6.0.RC1之后的torch_npu版本已支持，请按照版本配套关系更新到支持的版本
