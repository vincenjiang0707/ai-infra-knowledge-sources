# Unlock the power of images with AI Sheets

source: https://huggingface.co/blog/aisheets-unlock-images
published: Tue, 21 Oct 2025 00:00:00 GMT

Viewer • Updated • 14 • 16 • 1

# Unlock the power of images with AI Sheets

[Update on GitHub](https://github.com/huggingface/blog/blob/main/aisheets-unlock-images.md)

This article is also available in Chinese [简体中文](https://huggingface.co/blog/zh/aisheets-unlock-images).

🧭TL;DR: Hugging Face AI Sheets is an open-source tool forsupercharging datasets with AI models, no code required.Now with vision support: extract data from images (receipts, documents), generate visuals from text, and edit images—all in a spreadsheet. Powered by thousands of open models via Inference Providers.

We are excited to release a massive update to [Hugging Face AI Sheets](https://github.com/huggingface/aisheets), the open-source tool for building, transforming, and enriching data with open AI models. AI Sheets leverages [Inference Providers](https://huggingface.co/docs/inference-providers/index), which means you can use thousands of open models powered by the best inference providers on the planet.

The [first version of AI Sheets](https://huggingface.co/blog/aisheets) made structuring and enriching textual content a breeze. **Now, we're adding vision to AI Sheets.**

Images are everywhere—product photos, receipts, screenshots, diagrams, charts, logos. These documents contain structured information waiting to be extracted, analyzed, and transformed. Today, you can finally work with visual content directly in AI Sheets: view images, analyze them, extract information, generate new ones, and even edit them in real-time —all in the same workflow.

##
[
](https://huggingface.co#your-images-have-stories-to-tell)
Your images have stories to tell

Images contain valuable information—product catalogs, support tickets, research archives, receipts, documents. Now you can upload images directly or use datasets with images, and use vision models to extract, analyze, and structure the information inside them.

**What you can do:**

**Describe and categorize images**- Generate captions for product photos, classify document types, or tag images by content**Extract structured data**- Pull line items from receipts, data from charts, or text from scanned documents**Add context and metadata**- Automatically label images with relevant attributes, quality scores, or custom annotations

Just like text columns, you can iterate on prompts, manually edit outputs, and use thumbs-up to teach the model what you want. Your feedback becomes few-shot examples for better results.

**Example: From receipts to structured expenses**

Imagine you're back from a trip with a stack of receipts. Upload them to AI Sheets and create a column with a prompt like: `Extract the merchant name, date, total amount, and expense category from this receipt`


AI Sheets processes each receipt and gives you a clean table with all the details extracted. You can edit any mistakes, validate good results with thumbs-up, and regenerate to improve the rest. Export the final dataset as CSV or Parquet for your expense tracking tool.

Or maybe you're digitizing handwritten recipes from old family notebooks. Create columns to extract ingredients, cooking time, and cuisine type—turning your personal archive into a searchable, structured dataset.

##
[
](https://huggingface.co#generate-and-transform-text-and-images-in-the-same-flow)
Generate and transform text and images in the same flow

Need visuals for your content? AI Sheets can generate and edit images directly in your spreadsheet using AI models, keeping your entire content creation workflow in one place.

What you can do:

- Generate images from text - Create social media graphics, thumbnails, or illustrations that match your content
- Edit and transform existing images - Modify uploaded images or generated visuals—change styles, add elements, adjust compositions
- Create variations at scale - Generate multiple versions or styles to test what resonates with your audience
- Build visual content libraries - Produce consistent branded assets across large content campaigns

**Example: Creating a content calendar with visuals**

Imagine you're planning a month of social media posts about healthy recipes. You have a spreadsheet with post titles and descriptions, but no images yet.

Create an image column with a prompt like: Generate an appetizing food photo for: {{title}}. Style: bright, overhead shot, natural lighting.

AI Sheets generates a unique image for each post. Not quite right? Create another column to edit them: Transform the image to have a rustic wooden background and add fresh herbs as garnish.

You can iterate on generation and editing prompts and try different approaches. Your entire content calendar—copy and visuals—lives in one spreadsheet, ready to schedule or export.

##
[
](https://huggingface.co#step-by-step-guide)
Step-by-step guide

Now let’s see AI Sheets in action. We will use open models to unlock the knowledge within handwritten recipes like the ones you could find from your grandma.

###
[
](https://huggingface.co#upload-your-data)
Upload your data

We have a folder with photos that we can simply upload to the app.

The result is a spreadsheet like this:

###
[
](https://huggingface.co#understanding-ai-actions)
Understanding AI actions

Each column in your spreadsheet can be transformed, extracted from, queried, and anything you can imagine using AI actions.

To see this in action, click on the overlay on top of any column:

Image columns come with image operations like extracting text, asking the image, object detection, colorization, adding text, and any custom action you can think of.

Text columns include summarization, keyword extraction, translation, and custom actions.

A prompt and a model define every AI action. Let’s see what we can do with our handwritten recipes dataset!

###
[
](https://huggingface.co#extract-text-from-images)
Extract text from images.

AI Sheets comes with a template to extract text from images:

The result of this action is an AI-generated column with the transcribed text. Let’s see an example:

For the above image, the extracted text is as follows:

```
MEMORANDUM:
From
To
1 Box Duncan Hines Yellow Cake Mix
1 Box instant lemon pudding
2/3 cups water
1/2 cup Mozola oil
4 eggs
Lemon flavoring to taste.
Put in mixing bowl and beat for 10 min.
and REMEMBER... for Quality PRINTING
CALL OR WRITE
Gatling & Pierce
PRINTERS
TELEPHONE 332-2579
22 YEARS OF SERVICE IN NORTHEASTERN CAROLINA
```


Not bad! But we see it has included printed text for the header and footer, and we’re interested in the recipe text. The reason this text is included is that we have used the default template for text extraction, which is as follows:

`Extract and transcribe all visible text from the image, including signs, labels, documents, or any written content`


Let’s now try a custom prompt.

Here is the extracted recipe details:

- 1 box Duncan Hines Yellow Cake Mix

- 1 box instant lemon pudding

- 2/3 cups water

- 1/2 cup Mazola oil

- 4 eggs

- Lemon flavoring to taste

- Put in mixing bowl and beat for 10 minutes

This is great! But what about more complex images? By default, AI Sheets uses models with a good balance of speed and accuracy, but you can experiment with thousands of models. The above example uses the default vision language model `Qwen/Qwen2.5-VL-7B-Instruct`

.

Let’s test a SoTA reasoning model, `Qwen/Qwen3-VL-235B-A22B-Reasoning`

, with a more challenging image.

Here’s the comparison between the models:

| Qwen/Qwen2.5-VL-7B-Instruct | Qwen/Qwen3-VL-235B-A22B-Reasoning |
|---|---|
| in large bowl combine meat, onion, bread crumbs 1/2 nutmeg & cheese - as you add sprinkle around. Then blend - Last sprinkle blend again Bake in large pan for 10-15 min. at 350. Let stand 5 min before serving. | in lg bowl combine meat, onion, bread crumbs 1/4 nutmeg & cheese - as you add sprinkle around. then blend - last spinach blend again. Bake in lg pan for 50-60 min. @ 350 - let stand 5 min before serving |

Both models produce very similar outputs, but with two subtle but important details (**in bold**): the temperature and a key ingredient: spinach.

###
[
](https://huggingface.co#clean-transform-and-enrich-text)
Clean, transform, and enrich text

Once we are satisfied with the extracted text, we can further transform and enrich it. We need to perform an AI action with the new column as follows:

We now have a beautifully structured HTML page for each recipe:

###
[
](https://huggingface.co#edit-and-transform-images)
Edit and transform images.

Finally, AI Sheets integrates image-to-image models like Qwen-Image-Edit. This means you can run AI actions to transform and enrich your images.

For example, let’s say you want to give your recipes and old-looking style, you need to go to the column and use the B&W template like so:

Result:

###
[
](https://huggingface.co#export-your-dataset)
Export your dataset

Once you're happy with your new dataset, export it to the Hub! You can export it to an organization, your personal profile or make it private if you don't want to share it with the community.

You can check out [the dataset](https://huggingface.co/datasets/aisheets/unlocked-recipes) we have just created.

##
[
](https://huggingface.co#whats-next)
What's next?

You can [try AI Sheets](https://huggingface.co/spaces/aisheets/sheets) without installing or downloading and deploying it locally from the [GitHub repo](https://github.com/huggingface/aisheets). To run locally and get the most out of it, we recommend you subscribe to PRO and get 20x monthly inference usage.

If you have questions or suggestions, let us know in the Community tab or by [opening an issue on GitHub](https://github.com/huggingface/aisheets).