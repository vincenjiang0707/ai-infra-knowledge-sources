# Visible Watermarking with Gradio

source: https://huggingface.co/blog/watermarking-with-gradio
published: Mon, 15 Sep 2025 00:00:00 GMT

📱 2k

#### QR Code AI Art Generator

QR Code AI Art Generator Blend QR codes with AI Art

Last year, we shared a
[blogpost on watermarking](https://huggingface.co/blog/watermarking), explaining what it means to watermark generative AI content, and why it's important. The need for watermarking has become even more critical as people all over the world have begun to generate and share AI-generated images, video, audio, and text. Images and video have become so realistic that they’re nearly impossible to distinguish from what you’d see captured by a real camera. Addressing this issue is multi-faceted, but there is one, clear, low-hanging fruit 🍇:


In order for people to know what's real and what's synthetic, use visible watermarks.

To help out, we at Hugging Face have made visible watermarking trivially easy: Whenever you [create a Space like an app or a demo](https://huggingface.co/new-space), you can use our in-house app-building library Gradio to display watermarks with a single command.

For images and video, simply add the `watermark`

parameter, like so:

```
gr.Image(my_generated_image, watermark=my_watermark_image)
```


```
gr.Video(my_generated_video, watermark=my_watermark_image)
```



[See a demonstration of this in action:][check out our example image and video watermarking Space].

Watermarks can be specified as filenames, and for images we additionally support open images or even numpy arrays, to work best with how you want to set up your interface. One option I particularly like is QR watermarks, which can be used to get much more information about the content, [and can even be matched to the style of your image or video](https://huggingface.co/spaces/huggingface-projects/QR-code-AI-art-generator).

You can also add custom visible watermarks for AI-generated text, so that whenever it is copied, the watermark will appear. Like so:

```
gr.Chatbot(label=my_model_name, watermark=my_watermark_text, type="messages", show_copy_button=True, show_copy_all_button=True)
```



[See a demonstration of this in action:][check out our example chatbot watermarking Space].

This automatically adds attribution when users copy text from AI responses, further aiding in AI transparency and disclosure for text generation.

Try it all out today, build your own watermark, have fun!

Happy Coding!

*Acknowledgements: Abubakar Abid and Yuvraj Sharma collaborated on this work and blog post.*

very cool, good step towards transparency! 🤗

I encourage the development community to adopt watermarks and a comprehensive policy related to identifying AI-generated images and video. If not, I believe there will be legislation and legal "incentives" enforcing such a policy. We must take initiative instead of waiting to respond to a negative event.

7\

A very useful article! Indeed, it is becoming increasingly difficult to distinguish generated content from reality, and visible watermarks in Gradio are an excellent solution for transparency. However, sometimes you get tired of this digital race and just want to experience real luck and emotions. If you're looking for a way to switch gears after coding, I recommend checking out [VegasHero](https://vegashero-casino.ca/) — there's no need for watermarks there, just pure excitement.