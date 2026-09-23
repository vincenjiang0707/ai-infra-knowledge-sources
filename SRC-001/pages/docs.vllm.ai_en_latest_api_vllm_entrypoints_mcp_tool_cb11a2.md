source: https://docs.vllm.ai/en/latest/api/vllm/entrypoints/mcp/tool/
lastmod: 2026-09-23

class HarmonyPythonTool(Tool):
def __init__(self):
self.enabled = True
try:
validate_gpt_oss_install()
from gpt_oss.tools.python_docker.docker_tool import PythonTool
except ImportError as e:
self.enabled = False
logger.warning_once(
"gpt_oss is not installed properly (%s), code interpreter is disabled",
e,
)
return
self.python_tool = PythonTool()
async def validate(self):
if not self.enabled:
return
try:
message = Message(
author=Author(role=Role.ASSISTANT),
content=[TextContent(text="print('Hello, world!')")],
channel="analysis",
recipient="python",
content_type="code",
)
msgs = []
async for msg in self.python_tool.process(message):
msgs.append(msg)
assert msgs[0].content[0].text == "Hello, world!\n"
except Exception as e:
self.enabled = False
logger.warning_once(
"Code interpreter tool failed to initialize (%s), code "
"interpreter is disabled",
e,
)
return
logger.info_once("Code interpreter tool initialized")
async def get_result(self, context: "ConversationContext") -> Any:
from vllm.entrypoints.openai.responses.context import HarmonyContext
assert isinstance(context, HarmonyContext)
last_msg = context.messages[-1]
tool_output_msgs = []
async for msg in self.python_tool.process(last_msg):
tool_output_msgs.append(msg)
return tool_output_msgs
async def get_result_parsable_context(self, context: "ConversationContext") -> Any:
"""This function converts parsable context types to harmony and
back so we can use GPTOSS demo python tool
"""
from vllm.entrypoints.openai.responses.context import ParsableContext
assert isinstance(context, ParsableContext)
last_msg = context.response_messages[-1]
args = json.loads(last_msg.arguments)
last_msg_harmony = Message(
author=Author(role="assistant", name=None),
content=[TextContent(text=args["code"])],
channel="analysis",
recipient="python",
content_type="code",
)
tool_output_msgs = []
async for msg in self.python_tool.process(last_msg_harmony):
processed = ResponseFunctionToolCallOutputItem(
id=f"fco_{random_uuid()}",
type="function_call_output",
call_id=f"call_{random_uuid()}",
output=msg.content[0].text,
status="completed",
)
tool_output_msgs.append(processed)
return tool_output_msgs
@property
def tool_config(self) -> Any:
return self.python_tool.tool_config