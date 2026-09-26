# Upskill your LLMs With Gradio MCP Servers

source: https://huggingface.co/blog/gradio-mcp-servers
published: Wed, 09 Jul 2025 00:00:00 GMT

🍿 1.76k

#### Chatterbox TTS

Expressive Zeroshot TTS

Well, now it can! In this blog post, I'll show you:

The **Model Context Protocol (MCP)** is an open standard that enables developers to build secure, two-way connections between an LLM and a set of tools. For example, if you create an MCP server that exposes a tool capable of transcribing a video, then you can connect an LLM client (such as Cursor, Claude Code, or Cline) to the server. The LLM will then know how to transcribe videos and use this tool for you depending on your request.

In short, an MCP server is a standard way to upskill your LLM by granting it a new ability. Think of it like the apps on your smartphone. On its own, your smartphone can't edit images, but you can download an app to do this from the app store. Now, if only there were an app store for MCP servers? 🤔

Hugging Face [Spaces](https://hf.co/spaces) is the world's largest collection of AI applications. Most of these spaces perform a specialized task with an AI model. For example:

These spaces are implemented with [Gradio](https://gradio.app), an open source python package for creating AI-powered web servers. As of version `5.28.0`

, **Gradio apps support the MCP protocol.**

That means that Hugging Face Spaces is the one place where you can find thousands of AI-powered abilities for your LLM, aka the **MCP App Store!**

Want to browse the app store? Visit this [link](https://huggingface.co/spaces?filter=mcp-server). Manually, you can filter for `MCP Compatible`

in `https://hf.co/spaces`

.

[Flux.1 Kontext[dev]](https://huggingface.co/spaces/black-forest-labs/FLUX.1-Kontext-Dev) is an impressive model that can edit an image from a plain text prompt. For example, if you ask it to "dye my hair blue" and upload a photo of yourself, the model will return the photo but with you having blue hair!

Let's plug this model as an MCP server into an LLM and have it edit images for us. Follow these steps:

`MCP`

. You may have to scroll down in the page to see it.`Spaces Tools`

. In the search bar, type `Flux.1-Kontext-Dev`

and select the space called `black-forest-labs/Flux.1-Kontext-Dev`

. The page should look like this after you click on it:`Cursor`

icon of the `Setup with your AI assistant`

section. Now, copy that code snippet and place it in your cursor settings file.Using a popular public space as a tool may mean you have to wait longer to receive results. If you visit the space, you can click "Duplicate This Space" to create a private version of the space for yourself. If the space is using "ZeroGPU", you may need to update to a

[PRO]account to duplicate it.

This blog post has walked you through the exciting new capabilities that the Model Context Protocol (MCP) brings to Large Language Models. We've seen how Gradio apps, particularly those hosted on Hugging Face Spaces, are now fully MCP compliant, effectively turning Spaces into a vibrant "App Store" for LLM tools. By connecting these specialized MCP servers, your LLM can transcend basic question-answering and gain powerful new abilities, from image editing to transcription, to anything you can imagine!