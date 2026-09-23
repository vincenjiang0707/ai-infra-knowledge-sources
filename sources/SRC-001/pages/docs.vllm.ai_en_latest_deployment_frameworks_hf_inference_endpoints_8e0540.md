source: https://docs.vllm.ai/en/latest/deployment/frameworks/hf_inference_endpoints/
lastmod: 2026-09-23

# Hugging Face Inference Endpoints[¶](https://docs.vllm.ai#hugging-face-inference-endpoints)

## Overview[¶](https://docs.vllm.ai#overview)

Models compatible with vLLM can be deployed on Hugging Face Inference Endpoints, either starting from the [Hugging Face Hub](https://huggingface.co) or directly from the [Inference Endpoints](https://endpoints.huggingface.co/) interface. This allows you to serve models in a fully managed environment with GPU acceleration, auto-scaling, and monitoring, without managing the infrastructure manually.

For advanced details on vLLM integration and deployment options, see [Advanced Deployment Details](https://docs.vllm.ai#advanced-deployment-details).

## Deployment Methods[¶](https://docs.vllm.ai#deployment-methods)

One-click deploy models from the Hugging Face Hub with ready-made optimized configurations.**Method 1: Deploy from the Catalog.**Instantly deploy models tagged with**Method 2: Guided Deployment (Transformers Models).**`transformers`

from the Hub UI using the**Deploy**button.For models that either use custom code with the**Method 3: Manual Deployment (Advanced Models).**`transformers`

tag, or don’t run with standard`transformers`

but are supported by vLLM. This method requires manual configuration.

### Method 1: Deploy from the Catalog[¶](https://docs.vllm.ai#method-1-deploy-from-the-catalog)

This is the easiest way to get started with vLLM on Hugging Face Inference Endpoints. You can browse a catalog of models with verified and optimized deployment configuration at [Inference Endpoints](https://endpoints.huggingface.co/catalog) to maximize performance.

-
Go to

[Endpoints Catalog](https://endpoints.huggingface.co/catalog)and in the**Inference Server**options, select`vLLM`

.This will display the current list of models with optimized preconfigured options. -
Select the desired model and click

**Create Endpoint**. -
Once the deployment is ready, you can use the endpoint. Update the

`DEPLOYMENT_URL`

with the URL provided in the console, remembering to append`/v1`

as required.[# pip install openai](https://docs.vllm.ai#__codelineno-0-1)[from openai import OpenAI](https://docs.vllm.ai#__codelineno-0-2)[import os](https://docs.vllm.ai#__codelineno-0-3)[client = OpenAI(](https://docs.vllm.ai#__codelineno-0-5)[base_url=DEPLOYMENT_URL,](https://docs.vllm.ai#__codelineno-0-6)[api_key=os.environ["HF_TOKEN"], # https://huggingface.co/settings/tokens](https://docs.vllm.ai#__codelineno-0-7)[)](https://docs.vllm.ai#__codelineno-0-8)[chat_completion = client.chat.completions.create(](https://docs.vllm.ai#__codelineno-0-10)[model="HuggingFaceTB/SmolLM3-3B",](https://docs.vllm.ai#__codelineno-0-11)[messages=[](https://docs.vllm.ai#__codelineno-0-12)[{](https://docs.vllm.ai#__codelineno-0-13)["role": "user",](https://docs.vllm.ai#__codelineno-0-14)["content": [](https://docs.vllm.ai#__codelineno-0-15)[{](https://docs.vllm.ai#__codelineno-0-16)["type": "text",](https://docs.vllm.ai#__codelineno-0-17)["text": "Give me a brief explanation of gravity in simple terms.",](https://docs.vllm.ai#__codelineno-0-18)[}](https://docs.vllm.ai#__codelineno-0-19)[],](https://docs.vllm.ai#__codelineno-0-20)[}](https://docs.vllm.ai#__codelineno-0-21)[],](https://docs.vllm.ai#__codelineno-0-22)[stream=True,](https://docs.vllm.ai#__codelineno-0-23)[)](https://docs.vllm.ai#__codelineno-0-24)[for message in chat_completion:](https://docs.vllm.ai#__codelineno-0-26)[print(message.choices[0].delta.content, end="")](https://docs.vllm.ai#__codelineno-0-27)

Note

The catalog provides models optimized for vLLM, including GPU settings and inference engine configurations. You can monitor the endpoint and update the **container or its configuration** from the Inference Endpoints UI.

### Method 2: Guided Deployment (Transformers Models)[¶](https://docs.vllm.ai#method-2-guided-deployment-transformers-models)

This method applies to models with the [ transformers library tag](https://huggingface.co/models?library=transformers) in their metadata. It allows you to deploy a model directly from the Hub UI without manual configuration.

-
Navigate to a model on

[Hugging Face Hub](https://huggingface.co/models).

For this example we will use themodel. You can verify that the model is compatible by checking the front matter in the`ibm-granite/granite-docling-258M`

[README](https://huggingface.co/ibm-granite/granite-docling-258M/blob/main/README.md), where the library is tagged as`library: transformers`

. -
Locate the

**Deploy**button. The button appears for models tagged with`transformers`

at the top right of the[model card](https://huggingface.co/ibm-granite/granite-docling-258M). -
Click the

**Deploy**button >**HF Inference Endpoints**. You will be taken to the Inference Endpoints interface to configure the deployment. -
Select the Hardware (we choose AWS>GPU>T4 for the example) and Container Configuration. Choose

`vLLM`

as the container type and finalize the deployment pressing**Create Endpoint**. -
Use the deployed endpoint. Update the

`DEPLOYMENT_URL`

with the URL provided in the console (remember to add`/v1`

needed). You can then use your endpoint programmatically or via the SDK.[# pip install openai](https://docs.vllm.ai#__codelineno-1-1)[from openai import OpenAI](https://docs.vllm.ai#__codelineno-1-2)[import os](https://docs.vllm.ai#__codelineno-1-3)[client = OpenAI(](https://docs.vllm.ai#__codelineno-1-5)[base_url=DEPLOYMENT_URL,](https://docs.vllm.ai#__codelineno-1-6)[api_key=os.environ["HF_TOKEN"], # https://huggingface.co/settings/tokens](https://docs.vllm.ai#__codelineno-1-7)[)](https://docs.vllm.ai#__codelineno-1-8)[chat_completion = client.chat.completions.create(](https://docs.vllm.ai#__codelineno-1-10)[model="ibm-granite/granite-docling-258M",](https://docs.vllm.ai#__codelineno-1-11)[messages=[](https://docs.vllm.ai#__codelineno-1-12)[{](https://docs.vllm.ai#__codelineno-1-13)["role": "user",](https://docs.vllm.ai#__codelineno-1-14)["content": [](https://docs.vllm.ai#__codelineno-1-15)[{](https://docs.vllm.ai#__codelineno-1-16)["type": "image_url",](https://docs.vllm.ai#__codelineno-1-17)["image_url": {](https://docs.vllm.ai#__codelineno-1-18)["url": "https://huggingface.co/ibm-granite/granite-docling-258M/resolve/main/assets/new_arxiv.png",](https://docs.vllm.ai#__codelineno-1-19)[},](https://docs.vllm.ai#__codelineno-1-20)[},](https://docs.vllm.ai#__codelineno-1-21)[{](https://docs.vllm.ai#__codelineno-1-22)["type": "text",](https://docs.vllm.ai#__codelineno-1-23)["text": "Convert this page to docling.",](https://docs.vllm.ai#__codelineno-1-24)[},](https://docs.vllm.ai#__codelineno-1-25)[]](https://docs.vllm.ai#__codelineno-1-26)[}](https://docs.vllm.ai#__codelineno-1-27)[],](https://docs.vllm.ai#__codelineno-1-28)[stream=True,](https://docs.vllm.ai#__codelineno-1-29)[)](https://docs.vllm.ai#__codelineno-1-30)[for message in chat_completion:](https://docs.vllm.ai#__codelineno-1-32)[print(message.choices[0].delta.content, end="")](https://docs.vllm.ai#__codelineno-1-33)

Note

This method uses best-guess defaults. You may need to adjust the configuration to fit your specific requirements.

### Method 3: Manual Deployment (Advanced Models)[¶](https://docs.vllm.ai#method-3-manual-deployment-advanced-models)

Some models require manual deployment because they:

- Use custom code with the
`transformers`

tag - Don't run with standard
`transformers`

but are supported by`vLLM`


These models cannot be deployed using the **Deploy** button on the model card.

In this guide, we demonstrate manual deployment using the [ rednote-hilab/dots.ocr](https://huggingface.co/rednote-hilab/dots.ocr) model, an OCR model integrated with vLLM (see vLLM

[PR](https://github.com/vllm-project/vllm/pull/24645)).

-
Start a new deployment. Go to

[Inference Endpoints](https://endpoints.huggingface.co/)and click`New`

. -
Search the model in the Hub. In the dialog, switch to

**Hub**and search for the desired model. -
Choosing infrastructure. On the configuration page, select the cloud provider and hardware from the available options.


For this demo, we choose AWS and L4 GPU. Adjust according to your hardware needs. -
Configure the container. Scroll to the

**Container Configuration**and select`vLLM`

as the container type. -
Create the endpoint. Click

**Create Endpoint**to deploy the model.Once the endpoint is ready, you can use it with the OpenAI Completion API, cURL, or other SDKs. Remember to append

`/v1`

to the deployment URL if needed.

Note

You can adjust the **container settings** (Container URI, Container Arguments) from the Inference Endpoints UI and press **Update Endpoint**. This redeploys the endpoint with the updated container configuration. Changes to the model itself require creating a new endpoint or redeploying with a different model. For example, for this demo, you may need to update the Container URI to the nightly image (`vllm/vllm-openai:nightly`

) and add the `--trust-remote-code`

flag in the container arguments.

## Advanced Deployment Details[¶](https://docs.vllm.ai#advanced-deployment-details)

With the [Transformers modeling backend integration](https://blog.vllm.ai/2025/04/11/transformers-backend.html), vLLM now offers Day 0 support for any model compatible with `transformers`

. This means you can deploy such models immediately, leveraging vLLM’s optimized inference without additional backend modifications.

Hugging Face Inference Endpoints provides a fully managed environment for serving models via vLLM. You can deploy models without configuring servers, installing dependencies, or managing clusters. Endpoints also support deployment across multiple cloud providers (AWS, Azure, GCP) without the need for separate accounts.

The platform integrates seamlessly with the Hugging Face Hub, allowing you to deploy any vLLM- or `transformers`

-compatible model, track usage, and update the inference engine directly. The vLLM engine comes preconfigured, enabling optimized inference and easy switching between models or engines without modifying your code. This setup simplifies production deployment: endpoints are ready in minutes, include monitoring and logging, and let you focus on serving models rather than maintaining infrastructure.

## Next Steps[¶](https://docs.vllm.ai#next-steps)

- Explore the
[Inference Endpoints](https://endpoints.huggingface.co/catalog)model catalog - Read the Inference Endpoints
[documentation](https://huggingface.co/docs/inference-endpoints/en/index) - Learn about
[Inference Endpoints engines](https://huggingface.co/docs/inference-endpoints/en/engines/vllm) - Understand the
[Transformers modeling backend integration](https://blog.vllm.ai/2025/04/11/transformers-backend.html)