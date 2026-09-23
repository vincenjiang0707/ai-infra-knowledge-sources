source: https://docs.vllm.ai/en/latest/examples/features/structured_outputs/
lastmod: 2026-09-23

# Structured Outputs[¶](https://docs.vllm.ai#structured-outputs)

Source [https://github.com/vllm-project/vllm/tree/main/examples/features/structured_outputs](https://github.com/vllm-project/vllm/tree/main/examples/features/structured_outputs).

This script demonstrates various structured output capabilities of vLLM's OpenAI-compatible server. It can run individual constraint type or all of them. It supports both streaming responses and concurrent non-streaming requests.

To use this example, you must start an vLLM server with any model of your choice.

To serve a reasoning model, you can use the following command:

If you want to run this script standalone with `uv`

, you can use the following:

uvx --from git+https://github.com/vllm-project/vllm#subdirectory=examples/features/structured_outputs \
structured-outputs


See [feature docs](https://docs.vllm.ai/features/structured_outputs/) for more information.

Tip

If vLLM is running remotely, then set `OPENAI_BASE_URL=<remote_url>`

before running the script.

## Usage[¶](https://docs.vllm.ai#usage)

Run all constraints, non-streaming:

Run all constraints, streaming:

Run certain constraints, for example `structural_tag`

and `regex`

, streaming:

Run all constraints, with reasoning models and streaming:

## Example materials[¶](https://docs.vllm.ai#example-materials)

## pyproject.toml

## structured_outputs_client.py

# ruff: noqa: E501
# SPDX-License-Identifier: Apache-2.0
# SPDX-FileCopyrightText: Copyright contributors to the vLLM project
import argparse
import asyncio
import enum
import os
from typing import Any, Literal
import openai
import pydantic
from openai.types.chat import ChatCompletionChunk
ConstraintsFormat = Literal[
"choice",
"regex",
"json",
"grammar",
"structural_tag",
]
async def print_stream_response(
stream_response: openai.AsyncStream[ChatCompletionChunk],
title: str,
args: argparse.Namespace,
):
print(f"\n\n{title} (Streaming):")
local_reasoning_header_printed = False
local_content_header_printed = False
async for chunk in stream_response:
delta = chunk.choices[0].delta
reasoning_chunk_text: str | None = getattr(delta, "reasoning", None)
content_chunk_text = delta.content
if args.reasoning:
if reasoning_chunk_text:
if not local_reasoning_header_printed:
print(" Reasoning: ", end="")
local_reasoning_header_printed = True
print(reasoning_chunk_text, end="", flush=True)
if content_chunk_text:
if not local_content_header_printed:
if local_reasoning_header_printed:
print()
print(" Content: ", end="")
local_content_header_printed = True
print(content_chunk_text, end="", flush=True)
else:
if content_chunk_text:
if not local_content_header_printed:
print(" Content: ", end="")
local_content_header_printed = True
print(content_chunk_text, end="", flush=True)
print()
class CarType(str, enum.Enum):
SEDAN = "SEDAN"
SUV = "SUV"
TRUCK = "TRUCK"
COUPE = "COUPE"
class CarDescription(pydantic.BaseModel):
brand: str
model: str
car_type: CarType
PARAMS: dict[ConstraintsFormat, dict[str, Any]] = {
"choice": {
"messages": [
{
"role": "user",
"content": "Classify this sentiment: vLLM is wonderful!",
}
],
"extra_body": {"structured_outputs": {"choice": ["positive", "negative"]}},
},
"regex": {
"messages": [
{
"role": "user",
"content": "Generate an email address for Alan Turing, who works in Enigma. End in .com and new line. Example result: '[[email protected]](https://docs.vllm.ai/cdn-cgi/l/email-protection)\n'",
}
],
"extra_body": {
"structured_outputs": {"regex": r"[a-z0-9.]{1,20}@\w{6,10}\.com\n"},
},
},
"json": {
"messages": [
{
"role": "user",
"content": "Generate a JSON with the brand, model and car_type of the most iconic car from the 90's",
}
],
"response_format": {
"type": "json_schema",
"json_schema": {
"name": "car-description",
"schema": CarDescription.model_json_schema(),
},
},
},
"grammar": {
"messages": [
{
"role": "user",
"content": "Generate an SQL query to show the 'username' and 'email' from the 'users' table.",
}
],
"extra_body": {
"structured_outputs": {
"grammar": """
root ::= select_statement
select_statement ::= "SELECT " column " from " table " where " condition
column ::= "col_1 " | "col_2 "
table ::= "table_1 " | "table_2 "
condition ::= column "= " number
number ::= "1 " | "2 "
""",
}
},
},
"structural_tag": {
"messages": [
{
"role": "user",
"content": """
You have access to the following function to retrieve the weather in a city:
{
"name": "get_weather",
"parameters": {
"city": {
"param_type": "string",
"description": "The city to get the weather for",
"required": True
}
}
}
If a you choose to call a function ONLY reply in the following format:
<{start_tag}={function_name}>{parameters}{end_tag}
where
start_tag => `<function`
parameters => a JSON dict with the function argument name as key and function
argument value as value.
end_tag => `</function>`
Here is an example,
<function=example_function_name>{"example_name": "example_value"}</function>
Reminder:
- Function calls MUST follow the specified format
- Required parameters MUST be specified
- Only call one function at a time
- Put the entire function call reply on one line
- Always add your sources when using search results to answer the user query
You are a helpful assistant.
Given the previous instructions, what is the weather in New York City, Boston,
and San Francisco?""",
},
],
"response_format": {
"type": "structural_tag",
"structures": [
{
"begin": "<function=get_weather>",
"schema": {
"type": "object",
"properties": {"city": {"type": "string"}},
"required": ["city"],
},
"end": "</function>",
}
],
"triggers": ["<function="],
},
},
}
async def cli():
parser = argparse.ArgumentParser(
description="Run OpenAI Chat Completion with various structured outputs capabilities",
)
_ = parser.add_argument(
"--constraint",
type=str,
nargs="+",
choices=[*list(PARAMS), "*"],
default=["*"],
help="Specify which constraint(s) to run.",
)
_ = parser.add_argument(
"--stream",
action=argparse.BooleanOptionalAction,
default=False,
help="Enable streaming output",
)
_ = parser.add_argument(
"--reasoning",
action=argparse.BooleanOptionalAction,
default=False,
help="Enable printing of reasoning traces if available.",
)
args = parser.parse_args()
base_url = os.getenv("OPENAI_BASE_URL", "http://localhost:8000/v1")
client = openai.AsyncOpenAI(base_url=base_url, api_key="EMPTY")
constraints = list(PARAMS) if "*" in args.constraint else list(set(args.constraint))
model = (await client.models.list()).data[0].id
if args.stream:
results = await asyncio.gather(
*[
client.chat.completions.create(
model=model,
max_tokens=1024,
stream=True,
**PARAMS[name],
)
for name in constraints
]
)
for constraint, stream in zip(constraints, results):
await print_stream_response(stream, constraint, args)
else:
results = await asyncio.gather(
*[
client.chat.completions.create(
model=model,
max_tokens=1024,
stream=False,
**PARAMS[name],
)
for name in constraints
]
)
for constraint, response in zip(constraints, results):
print(f"\n\n{constraint}:")
message = response.choices[0].message
if args.reasoning and hasattr(message, "reasoning"):
print(f" Reasoning: {message.reasoning or ''}")
print(f" Content: {message.content!r}")
def main():
asyncio.run(cli())
if __name__ == "__main__":
main()


## structured_outputs_offline.py

# SPDX-License-Identifier: Apache-2.0
# SPDX-FileCopyrightText: Copyright contributors to the vLLM project
"""This file demonstrates the example usage of structured outputs
in vLLM. It shows how to apply different constraints such as choice,
regex, json schema, and grammar to produce structured and formatted
results based on specific prompts.
"""
from enum import Enum
from pydantic import BaseModel
from vllm import LLM, SamplingParams
from vllm.sampling_params import StructuredOutputsParams
MAX_TOKENS = 50
# Structured outputs by Choice (list of possible options)
structured_outputs_params_choice = StructuredOutputsParams(
choice=["Positive", "Negative"]
)
sampling_params_choice = SamplingParams(
structured_outputs=structured_outputs_params_choice
)
prompt_choice = "Classify this sentiment: vLLM is wonderful!"
# Structured outputs by Regex
structured_outputs_params_regex = StructuredOutputsParams(regex=r"\w+@\w+\.com\n")
sampling_params_regex = SamplingParams(
structured_outputs=structured_outputs_params_regex,
stop=["\n"],
max_tokens=MAX_TOKENS,
)
prompt_regex = (
"Generate an email address for Alan Turing, who works in Enigma."
"End in .com and new line. Example result:"
"[[email protected]](https://docs.vllm.ai/cdn-cgi/l/email-protection)\n"
)
# Structured outputs by JSON using Pydantic schema
class CarType(str, Enum):
sedan = "sedan"
suv = "SUV"
truck = "Truck"
coupe = "Coupe"
class CarDescription(BaseModel):
brand: str
model: str
car_type: CarType
json_schema = CarDescription.model_json_schema()
structured_outputs_params_json = StructuredOutputsParams(json=json_schema)
sampling_params_json = SamplingParams(
structured_outputs=structured_outputs_params_json, max_tokens=MAX_TOKENS
)
prompt_json = (
"Generate a JSON with the brand, model and car_type of "
"the most iconic car from the 90's"
)
# Structured outputs by Grammar
simplified_sql_grammar = """
root ::= select_statement
select_statement ::= "SELECT " column " from " table " where " condition
column ::= "col_1 " | "col_2 "
table ::= "table_1 " | "table_2 "
condition ::= column "= " number
number ::= "1 " | "2 "
"""
structured_outputs_params_grammar = StructuredOutputsParams(
grammar=simplified_sql_grammar
)
sampling_params_grammar = SamplingParams(
structured_outputs=structured_outputs_params_grammar,
max_tokens=MAX_TOKENS,
)
prompt_grammar = (
"Generate an SQL query to show the 'username' and 'email' from the 'users' table."
)
def format_output(title: str, output: str):
print(f"{'-' * 50}\n{title}: {output}\n{'-' * 50}")
def generate_output(prompt: str, sampling_params: SamplingParams, llm: LLM):
outputs = llm.generate(prompt, sampling_params=sampling_params)
return outputs[0].outputs[0].text
def main():
llm = LLM(model="Qwen/Qwen2.5-3B-Instruct", max_model_len=100)
choice_output = generate_output(prompt_choice, sampling_params_choice, llm)
format_output("Structured outputs by Choice", choice_output)
regex_output = generate_output(prompt_regex, sampling_params_regex, llm)
format_output("Structured outputs by Regex", regex_output)
json_output = generate_output(prompt_json, sampling_params_json, llm)
format_output("Structured outputs by JSON", json_output)
grammar_output = generate_output(prompt_grammar, sampling_params_grammar, llm)
format_output("Structured outputs by Grammar", grammar_output)
if __name__ == "__main__":
main()