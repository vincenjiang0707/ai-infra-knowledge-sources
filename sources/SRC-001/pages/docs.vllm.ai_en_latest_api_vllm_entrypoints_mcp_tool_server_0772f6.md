source: https://docs.vllm.ai/en/latest/api/vllm/entrypoints/mcp/tool_server/
lastmod: 2026-09-24

#

`vllm.entrypoints.mcp.tool_server`

[¶](https://docs.vllm.ai#vllm.entrypoints.mcp.tool_server)

Classes:

##

`ToolServer`

[¶](https://docs.vllm.ai#vllm.entrypoints.mcp.tool_server.ToolServer)

Bases: [ABC](https://docs.python.org/3/library/abc.html#abc.ABC)

Methods:

-
–[get_tool_description](https://docs.vllm.ai#vllm.entrypoints.mcp.tool_server.ToolServer.get_tool_description)Return the tool description for the given tool name.

-
–[has_tool](https://docs.vllm.ai#vllm.entrypoints.mcp.tool_server.ToolServer.has_tool)Return True if the tool is supported, False otherwise.

-
–[new_session](https://docs.vllm.ai#vllm.entrypoints.mcp.tool_server.ToolServer.new_session)Create a session for the tool.


## Source code in `vllm/entrypoints/mcp/tool_server.py`


###

`get_tool_description(tool_name, allowed_tools=None)`

`abstractmethod`

[¶](https://docs.vllm.ai#vllm.entrypoints.mcp.tool_server.ToolServer.get_tool_description)

Return the tool description for the given tool name. If the tool is not supported, return None.