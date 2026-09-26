source: https://docs.nvidia.com/cupti/api/structCUpti__GraphData.html

# 7.139. CUpti_GraphData[#](https://docs.nvidia.com#cupti-graphdata)

-
struct CUpti_GraphData
[#](https://docs.nvidia.com#_CPPv415CUpti_GraphData) CUDA graphs data passed into a resource callback function.

CUDA graphs data passed into a resource callback function as the

`cbdata`

argument to[CUpti_CallbackFunc](https://docs.nvidia.com/group__CUPTI__CALLBACK__API.html#group__cupti__callback__api_1ga21bab4f7f7e04488b0e7edcea9f5a49c). The`cbdata`

will be this type for`domain`

equal to CUPTI_CB_DOMAIN_RESOURCE. The graph data is valid only within the invocation of the callback function that is passed the data. If you need to retain some data for use outside of the callback, you must make a copy of that data.Public Members

-
CUgraph graph
[#](https://docs.nvidia.com#_CPPv4N15CUpti_GraphData5graphE) CUDA graph.


-
CUgraph originalGraph
[#](https://docs.nvidia.com#_CPPv4N15CUpti_GraphData13originalGraphE) The original CUDA graph from which.

- Param graph:
is cloned



-
CUgraphNode node
[#](https://docs.nvidia.com#_CPPv4N15CUpti_GraphData4nodeE) CUDA graph node.


-
CUgraphNode originalNode
[#](https://docs.nvidia.com#_CPPv4N15CUpti_GraphData12originalNodeE) The original CUDA graph node from which.

- Param node:
is cloned



-
CUgraphNodeType nodeType
[#](https://docs.nvidia.com#_CPPv4N15CUpti_GraphData8nodeTypeE) Type of the.

- Param node:


-
CUgraphNode dependency
[#](https://docs.nvidia.com#_CPPv4N15CUpti_GraphData10dependencyE) The dependent graph node.


-
CUgraphExec graphExec
[#](https://docs.nvidia.com#_CPPv4N15CUpti_GraphData9graphExecE) CUDA executable graph.


-
CUgraph graph