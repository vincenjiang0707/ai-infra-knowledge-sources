source: https://docs.vllm.ai/en/latest/api/vllm/compilation/base_static_graph/
lastmod: 2026-09-23

#

`vllm.compilation.base_static_graph`

[¶](https://docs.vllm.ai#vllm.compilation.base_static_graph)

Classes:

-
–[AbstractStaticGraphWrapper](https://docs.vllm.ai#vllm.compilation.base_static_graph.AbstractStaticGraphWrapper)StaticGraphWrapper interface that allows platforms to wrap a callable


##

`AbstractStaticGraphWrapper`

[¶](https://docs.vllm.ai#vllm.compilation.base_static_graph.AbstractStaticGraphWrapper)

Bases: [Protocol](https://docs.python.org/3/library/typing.html#typing.Protocol)

StaticGraphWrapper interface that allows platforms to wrap a callable to be captured as a static graph.

Methods:

-
–[__call__](https://docs.vllm.ai#vllm.compilation.base_static_graph.AbstractStaticGraphWrapper.__call__)Executes the wrapped callable.

-
–[__init__](https://docs.vllm.ai#vllm.compilation.base_static_graph.AbstractStaticGraphWrapper.__init__)Initializes the StaticGraphWrapper class with graph capturing and


## Source code in `vllm/compilation/base_static_graph.py`


###

`__call__(*args, **kwargs)`

[¶](https://docs.vllm.ai#vllm.compilation.base_static_graph.AbstractStaticGraphWrapper.__call__)

Executes the wrapped callable.

If the current runtime mode in the ForwardContext matches the runtime mode of this instance, it replays the CUDAGraph or captures it using the callable if it hasn't been captured yet. Otherwise, it calls the original callable directly.

Parameters:

-

(`*args`

[¶](https://docs.vllm.ai#vllm.compilation.base_static_graph.AbstractStaticGraphWrapper.__call__(*args))

, default:[Any](https://docs.python.org/3/library/typing.html#typing.Any)`()`

) –Variable length input arguments to be passed into the callable.

-

(`**kwargs`

[¶](https://docs.vllm.ai#vllm.compilation.base_static_graph.AbstractStaticGraphWrapper.__call__(**kwargs))

, default:[Any](https://docs.python.org/3/library/typing.html#typing.Any)`{}`

) –Keyword arguments to be passed into the callable.


Returns:

-
(`Any`


) –[Any](https://docs.python.org/3/library/typing.html#typing.Any)Output of the executed callable.


## Source code in `vllm/compilation/base_static_graph.py`


###

`__init__(runnable, vllm_config, runtime_mode, **kwargs)`

[¶](https://docs.vllm.ai#vllm.compilation.base_static_graph.AbstractStaticGraphWrapper.__init__)

Initializes the StaticGraphWrapper class with graph capturing and execution-related configurations.

Parameters:

-

(`runnable`

[¶](https://docs.vllm.ai#vllm.compilation.base_static_graph.AbstractStaticGraphWrapper.__init__(runnable))

) –[Callable](https://docs.python.org/3/library/collections.abc.html#collections.abc.Callable)The callable to be wrapped and captured.

-

(`vllm_config`

[¶](https://docs.vllm.ai#vllm.compilation.base_static_graph.AbstractStaticGraphWrapper.__init__(vllm_config))

) –[VllmConfig](https://docs.vllm.ai/config/#vllm.config.VllmConfig)Global configuration for vLLM.

-

(`runtime_mode`

[¶](https://docs.vllm.ai#vllm.compilation.base_static_graph.AbstractStaticGraphWrapper.__init__(runtime_mode))

) –[CUDAGraphMode](https://docs.vllm.ai/config/#vllm.config.CUDAGraphMode)The style of the static graph runtime. See CUDAGraphMode in vllm/config.py. Note that only the subset enum

`NONE`

,`PIECEWISE`

and`FULL`

are used as concrete runtime mode for cudagraph dispatching.

Other Parameters:

-
(`kwargs`


) –[Any](https://docs.python.org/3/library/typing.html#typing.Any)Additional keyword arguments for platform-specific configurations.