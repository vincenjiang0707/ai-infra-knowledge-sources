source: https://docs.nvidia.com/deeplearning/nccl/user-guide/docs/nccl4py/parameters.html

# Parameters[](https://docs.nvidia.com#parameters)

Read access to NCCL’s tunable parameters. See [Environment Variables](https://docs.nvidia.com/env.html) for the meaning
of each parameter and how to set it.

```
import nccl.core
nccl.core.params["NCCL_DEBUG"] # value of a single parameter
list(nccl.core.params) # every parameter name
nccl.core.dump_params() # print all parameters to stdout
```

## params[](https://docs.nvidia.com#params)

-
nccl.core.params
[](https://docs.nvidia.com#nccl.core.params) Read-only

`Mapping`

of NCCL parameter names to their current values, backed byand`ncclParamGetParameter()`

. Values are returned as strings. Lookups are live: each access queries NCCL rather than a cached snapshot.`ncclParamGetAllParameterKeys()`


## dump_params[](https://docs.nvidia.com#dump-params)

-
nccl.core.dump_params() None
[](https://docs.nvidia.com#nccl.core.dump_params) Print NCCL parameters to stdout. Set

`NCCL_PARAM_DUMP_ALL=1`

to include internal parameters.