# Scaleway on Hugging Face Inference Providers 🔥

source: https://huggingface.co/blog/inference-providers-scaleway
published: Fri, 19 Sep 2025 00:00:00 GMT

Text Generation • 31B • Updated • 550k • 1.25k

#
[
](https://huggingface.co#scaleway-on-hugging-face-inference-providers-🔥)
Scaleway on Hugging Face Inference Providers 🔥

[Update on GitHub](https://github.com/huggingface/blog/blob/main/inference-providers-scaleway.md)


We're thrilled to share that **Scaleway** is now a supported Inference Provider on the Hugging Face Hub!
Scaleway joins our growing ecosystem, enhancing the breadth and capabilities of serverless inference directly on the Hub’s model pages. Inference Providers are also seamlessly integrated into our client SDKs (for both JS and Python), making it super easy to use a wide variety of models with your preferred providers.

This launch makes it easier than ever to access popular open-weight models like [gpt-oss](https://huggingface.co/openai/gpt-oss-120b?inference_provider=scaleway), [Qwen3](https://huggingface.co/Qwen/Qwen3-Coder-30B-A3B-Instruct?inference_provider=scaleway), [DeepSeek R1](https://huggingface.co/deepseek-ai/DeepSeek-R1-Distill-Llama-70B?inference_provider=scaleway), and [Gemma 3](https://huggingface.co/google/gemma-3-27b-it?inference_provider=scaleway) — right from Hugging Face. You can browse Scaleway's org on the Hub at [https://huggingface.co/scaleway](https://huggingface.co/scaleway) and try trending supported models at [https://huggingface.co/models?inference_provider=scaleway&sort=trending](https://huggingface.co/models?inference_provider=scaleway&sort=trending).

*Scaleway Generative APIs* is a fully managed, serverless service that provides access to frontier AI models from leading research labs via simple API calls. The service offers competitive pay-per-token pricing starting at €0.20 per million tokens.

The service runs on secure infrastructure located in European data centers (Paris, France), ensuring data sovereignty and low latency for European users. The platform supports advanced features including structured outputs, function calling, and multimodal capabilities for both text and image processing.

Built for production use, Scaleway's inference infrastructure delivers sub-200ms response times for first tokens, making it ideal for interactive applications and agentic workflows. The service supports both text generation and embedding models. You can learn more about Scaleway's platform and infrastructure at [https://www.scaleway.com/en/generative-apis/](https://www.scaleway.com/en/generative-apis/).

Read more about how to use Scaleway as an Inference Provider in its dedicated [documentation page](https://huggingface.co/docs/inference-providers/providers/scaleway).

See the list of supported models [here](https://huggingface.co/models?inference_provider=scaleway&sort=trending).

##
[
](https://huggingface.co#how-it-works)
How it works

###
[
](https://huggingface.co#in-the-website-ui)
In the website UI

- In your user account settings, you are able to:

- Set your own API keys for the providers you’ve signed up with. If no custom key is set, your requests will be routed through HF.
- Order providers by preference. This applies to the widget and code snippets in the model pages.

- As mentioned, there are two modes when calling Inference Providers:

- Custom key (calls go directly to the inference provider, using your own API key of the corresponding inference provider)
- Routed by HF (in that case, you don't need a token from the provider, and the charges are applied directly to your HF account rather than the provider's account)

- Model pages showcase third-party inference providers (the ones that are compatible with the current model, sorted by user preference)

###
[
](https://huggingface.co#from-the-client-sdks)
From the client SDKs

####
[
](https://huggingface.co#from-python-using-huggingface_hub)
from Python, using huggingface_hub

The following example shows how to use OpenAI's gpt-oss-120b using Scaleway as the inference provider. You can use a [Hugging Face token](https://huggingface.co/settings/tokens) for automatic routing through Hugging Face, or your own Scaleway API key if you have one.

Note: this requires using a recent version of `huggingface_hub`

(>= 0.34.6).

```
import os
from huggingface_hub import InferenceClient
client = InferenceClient(
provider="scaleway",
api_key=os.environ["HF_TOKEN"],
)
messages = [
{
"role": "user",
"content": "Write a poem in the style of Shakespeare"
}
]
completion = client.chat.completions.create(
model="openai/gpt-oss-120b",
messages=messages,
)
print(completion.choices[0].message)
```


####
[
](https://huggingface.co#from-js-using-huggingfaceinference)
from JS using @huggingface/inference

```
import { InferenceClient } from "@huggingface/inference";
const client = new InferenceClient(process.env.HF_TOKEN);
const chatCompletion = await client.chatCompletion({
model: "openai/gpt-oss-120b",
messages: [
{
role: "user",
content: "Write a poem in the style of Shakespeare",
},
],
provider: "scaleway",
});
console.log(chatCompletion.choices[0].message);
```


##
[
](https://huggingface.co#billing)
Billing

Here is how billing works:

For direct requests, i.e. when you use the key from an inference provider, you are billed by the corresponding provider. For instance, if you use a Scaleway API key you're billed on your Scaleway account.

For routed requests, i.e. when you authenticate via the Hugging Face Hub, you'll only pay the standard provider API rates. There's no additional markup from us; we just pass through the provider costs directly. (In the future, we may establish revenue-sharing agreements with our provider partners.)

**Important Note** ‼️ PRO users get $2 worth of Inference credits every month. You can use them across providers. 🔥

Subscribe to the [Hugging Face PRO plan](https://hf.co/subscribe/pro) to get access to Inference credits, ZeroGPU, Spaces Dev Mode, 20x higher limits, and more.

We also provide free inference with a small quota for our signed-in free users, but please upgrade to PRO if you can!

##
[
](https://huggingface.co#feedback-and-next-steps)
Feedback and next steps

We would love to get your feedback! Share your thoughts and/or comments here: [https://huggingface.co/spaces/huggingface/HuggingDiscussions/discussions/49](https://huggingface.co/spaces/huggingface/HuggingDiscussions/discussions/49)