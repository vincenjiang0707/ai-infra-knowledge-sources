source: https://docs.vllm.ai/en/latest/deployment/frameworks/cerebrium/
lastmod: 2026-09-23

# Cerebrium[¶](https://docs.vllm.ai#cerebrium)

vLLM can be run on a cloud based GPU machine with [Cerebrium](https://www.cerebrium.ai/), a serverless AI infrastructure platform that makes it easier for companies to build and deploy AI based applications.

To install the Cerebrium client, run:

Next, create your Cerebrium project, run:

Next, to install the required packages, add the following to your cerebrium.toml:

[cerebrium.deployment]
docker_base_image_url = "nvidia/cuda:12.1.1-runtime-ubuntu22.04"
[cerebrium.dependencies.pip]
vllm = "latest"


Next, let us add our code to handle inference for the LLM of your choice (`mistralai/Mistral-7B-Instruct-v0.1`

for this example), add the following code to your `main.py`

:

## Code

from vllm import LLM, SamplingParams
llm = LLM(model="mistralai/Mistral-7B-Instruct-v0.1")
def run(prompts: list[str], temperature: float = 0.8, top_p: float = 0.95):
sampling_params = SamplingParams(temperature=temperature, top_p=top_p)
outputs = llm.generate(prompts, sampling_params)
# Print the outputs.
results = []
for output in outputs:
prompt = output.prompt
generated_text = output.outputs[0].text
results.append({"prompt": prompt, "generated_text": generated_text})
return {"results": results}


Then, run the following code to deploy it to the cloud:

If successful, you should be returned a CURL command that you can call inference against. Just remember to end the url with the function name you are calling (in our case `/run`

)

## Command

You should get a response like:

## Response

{
"run_id": "52911756-3066-9ae8-bcc9-d9129d1bd262",
"result": {
"result": [
{
"prompt": "Hello, my name is",
"generated_text": " Sarah, and I'm a teacher. I teach elementary school students. One of"
},
{
"prompt": "The president of the United States is",
"generated_text": " elected every four years. This is a democratic system.\n\n5. What"
},
{
"prompt": "The capital of France is",
"generated_text": " Paris.\n"
},
{
"prompt": "The future of AI is",
"generated_text": " bright, but it's important to approach it with a balanced and nuanced perspective."
}
]
},
"run_time_ms": 152.53663063049316
}


You now have an autoscaling endpoint where you only pay for the compute you use!