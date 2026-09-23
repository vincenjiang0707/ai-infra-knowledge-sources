# Continuous batching from first principles

source: https://huggingface.co/blog/continuous_batching
published: Tue, 25 Nov 2025 00:00:00 GMT

#
[
](https://huggingface.co#continuous-batching)
Continuous batching

[Update on GitHub](https://github.com/huggingface/blog/blob/main/continuous_batching.md)


*TL;DR: in this blog post, starting from attention mechanisms and KV caching, we derive continuous batching by optimizing for throughput.*

If you've ever used Qwen, Claude, or any other AI chatbot, you've probably noticed something: it takes a while for the first word of the response to appear, and then words appear one-by-one on your screen with (hopefully) a regular and fast-paced frequency. That's because at the heart of it, all LLMs are just fancy next token predictors. An LLM first processes your entire prompt to produce one new token. Then it keeps adding tokens one by one, each time reading everything that came before, until it decides generation is over.

This generation process is computationally expensive: it requires passing the input through billions of parameters for each token generated. To make these models practical for real-world applications, particularly when serving many users simultaneously, researchers and engineers have developed a range of efficient inference techniques.

One of the most impactful optimizations is **continuous batching**, which attempts to maximize performance by processing multiple conversations in parallel and swapping them out when they are done.

To understand how continuous batching works and why it's so effective in high-load serving scenarios, we'll build up from the fundamentals of how LLMs process tokens.

##
[
](https://huggingface.co#attention)
Attention

The attention mechanism is the central piece of how LLMs work. A language model processes text by breaking it down into pieces that we call tokens. We can conceptually think of "tokens" as "words", but sometimes a word might be composed of several tokens. For each token sequence, the network computes a prediction of what the next token should be.

Many operations in the network are **token-wise**: each token is processed independently, and the output for a given token depends only on that token's content, not on any other tokens in the sequence. Operations like this include layer normalization or matrix multiplication. However, to create connections between words in a sentence, we need operations where tokens can influence each other.

This is where attention comes in. **Attention layers are the only place where different tokens interact with each other**. Understanding how a network connects tokens together means understanding attention.

Let's see how this works in practice, in the case where there is only one input prompt.

Consider the initial prompt `I am sure this project`

, tokenized as 7 tokens: `[<bos>, I, am, sure, this, pro, ject]`

. The `<bos>`

, or "Beginning of Sequence", is a special token we add at the start of the prompt to tell the language model that a new conversation starts here.

Each token is represented inside the network with a vector of length `d`

(the *hidden dimension*). Therefore, the seven incoming tokens form a tensor with shape . `1`

is the number of sequences, or batch size, which is just one in our case. `7`

is the sequence length, and `d`

is the hidden dimension, or the size of each token representation. Going forward, we'll use instead of `7`

as the sequence length.

Input tensor is then projected by three matrices: the query projection , the key projection and the value projection . This produces three tensors , and , all of shape , where is the dimension of the attention head. We call them the **query, key and value states,** respectively. This is represented on the left in the figure below.

Next, tensors and are multiplied together to measure similarity between tokens, producing a tensor of shape . This is why we say that attention has quadratic complexity in sequence length. Computing requires operations, so the cost is a square of the sequence length. It is represented on the right in the figure above.

We then apply a boolean **attention mask** to to control which tokens can interact, as represented in the figure below. In this figure, the attention mask is a **causal mask**, meaning each token only interacts with tokens that came before it. This follows the intuition that a cause must come before its consequence, hence the name causal mask. The attention mask is crucial because it dictates all token interactions in the network. **Set all attention mask values to False and no token will ever interact with another in the whole network.** We'll examine attention masks more closely in a few paragraphs.

Finally, after applying the attention mask, we take a token-wise softmax (which is the same as saying a row-wise softmax) and multiply the result by the value projection to get the output of one attention head, of shape . We offer a visual summary of the whole process in the following figure.

We are going to use a lot of attention visualization in this post, so to simplify things, we are going to condense the figure above just a bit.

**Why this matters:** In continuous batching, , , and can have different numbers of tokens because, as we'll see, we'll be processing different stages (prefill and decode) at the same time. To make it more general, let's say has shape , has shape , and has shape .

The attention scores then have shape , and the attention mask has the same shape since it's applied point-wise to the scores.

After applying the attention mask and row-wise softmax, we multiply by . Since we're multiplying a matrix of shape by one of shape , the inner dimensions must match: . This means and always have the same length, so we can simplify our visualizations by only showing .

Don't worry if this seems abstract: the figures will make it concrete.

Furthermore, since we know that the attention mask is applied to , we know they have the same shape. Instead of representing the attention scores, we will represent the attention mask in its place. Finally, since , and are direct projections of , no need to represent . This gives the simplified figure where we only represent , and the attention mask:

This representation also underlines how we can **read an attention mask.**

We read the mask row-by-row, which is the same as reading token-by-token: each row corresponds to one token's attention computation. A **green square** at position (row i, column j) means `True`

: token j can influence token i. A **white square** means `False`

: no interaction allowed.

For example, look at the third row for token "*am*". The "*I*" column is green, so "*I*" influences the computation of "*am*". The "*pro*" column is white, so "*pro*" doesn't influence "*am*" . This is causal masking at work: future tokens can't affect past ones.

The last layer of the model outputs a token prediction for each input token. In our context, generating the continuation of a single prompt, we only care about the next token prediction from the last token. The last token is "*ject*" in the figure above, and the associated prediction is "*will*".

The process we just described, where we take an entire input sequence, pass it through multiple attention layers and compute a score for the next token, is called **prefill**. This is because, as we'll see in a moment, much of the computation we performed can be cached and reused – hence, we are *prefilling* the cache. Thanks to the use of this cache, sequence generation can proceed using much less compute in a phase called **decoding**. In the decoding phase, generating one new token will be much faster than the initial full-sequence computation. Let's see why.

To continue generation, we begin a new forward pass, which would naively look like this:

To compute the attention scores of the new token, we still need the key and value projections of the previous tokens. So we need to repeat the matrix multiplication of the old tokens (in grey in the figure above) with and to retrieve a result that was already computed once before. In other terms, we are wasting compute. Let's see how we can avoid that.

##
[
](https://huggingface.co#kv-cache)
KV-cache

Right off the bat, we notice that the last token does not impact the attention calculation of the other tokens:

This follows the idea of the causal mask: since "*will*" comes after all previous tokens, it does not change their attention calculation.
For text generation, causal attention is by far the most common, so we will focus on that case from now on. Keep in mind that non-causal attention schemes can also be used, especially when dealing with images.
Considering we only need the next-token prediction for the "*will*" token, we can simplify the attention mechanism by only computing the output for this token.

Moreover, we already computed the and states for the tokens "*<bos>*", … , "*ject*" during the previous forward pass: if they have been stored, we do not need to recompute them again. This is the **KV cache**: the list of key and value states created during generation. It essentially allows one to reduce the compute cost of generating token from to by avoiding recomputation of key and value projections, while paying a memory cost of .

In the figure above, only the tokens in white are computed: instead of computing the keys and values for 8 tokens, we compute them for 1. You can see that through KV caching, a lot of compute is saved.

You can check [this post](https://huggingface.co/blog/not-lain/kv-caching) for more visualizations of KV caching, or [this one](https://huggingface.co/blog/kv-cache) for a practical implementation example.

Let's be a bit more specific about the cache size, because it's a good opportunity to examine the shapes present in our model. For a model with attention layers and attention heads with head dimension , the total cache size needed to store one token will be with a factor of to account for both and .

For instance, Llama-2-7B with layers, heads, and requires values per token per layer. With `float16`

precision, this takes bytes KB in memory.

KV caching is useful when we want to generate the next token, which is a stage we call **decoding**. But it can also be useful in the **prefill** stage, when we process the initial prompt and have many input tokens. Especially when there are large initial prompts that don't fit in GPU memory all at once.

##
[
](https://huggingface.co#chunked-prefill)
Chunked prefill

Up till now, we have looked at an example of prefill where we have tokens, but in practice initial prompts can be much longer. For instance, when using Cursor, you can add your repository to the prompt, where it acts as context: this significantly increases the prompt size. In such cases, the memory needed to store the activations for tokens can be larger than the available memory on the GPU. Thus we cannot perform prefill in a single forward pass: we have to split the prefill in chunks. This is called **chunked prefill**, and it's going to be one of the components needed to enable efficient inference.

Let's pretend that the available memory is very constrained, and that we can only pass tokens per forward pass. If we have an initial prompt with tokens, we need to split it in chunks (rounding up 7/4 = 1.75 to 2). We illustrate the example below using the same and notations:

We can do that thanks to the KV cache. We store the KV states during the first prefill split, and during the second prefill split, we prepend the stored KV states to the new KV states. We also adapt the attention mask accordingly. Visually, it looks like we split the non-chunked prefill in the middle.

The key insight: cached KV states let us process the prompt incrementally without losing information.

Although we showed here an example where we split the prefill into 2 chunks, chunked prefill can be used to split the prefill in any way we want, adapting flexibly to memory constraints.

We are now finally equipped with all the tools we need to understand Continuous Batching.

##
[
](https://huggingface.co#continuous-batching-1)
Continuous batching

In our previous examples we have only considered the case of batch size one, i.e. we only generate tokens for one prompt at a time. In the context of evaluation or model serving, we want to generate tokens for a large number of prompts. To increase the **throughput**, which is the number of tokens generated per second, the best course of action is to generate tokens in parallel for a batch of several prompts.

To batch prompts together, the naive way is to add an axis to both input tensors: token sequence and attention mask. However, this comes with a constraint on the shape of the inputs: we need all prompts to have the same length, because tensors must be rectangular. To achieve this, we usually add padding on the left so the new token prediction always comes from the rightmost token. We also modify the attention mask of each prompt accordingly, as shown below:

where the padding tokens `<pad>`

are coloured in orange. Then we can perform the forward pass as we used to, with the added dimension of the batch size. This is called **batched generation**: efficient for same-length prompts, but wasteful when lengths vary.

It is illustrated below, through 4 steps of generation: one prefilling step (at the top) and 3 decoding steps (below each "Forward pass" lines).

where `<eos>`

means "End Of Sequence", this is a special token to indicate the model has reached the end of generation for the corresponding sequence.

The drawback of batched generation is that if one prompt finishes generation before the other one by generating an `<eos>`

token, all further generated tokens are useless. And this goes on until the longest request of the batch finishes. Of course, we can remove the prompts that have reached an `<eos>`

token from the batch and save some compute and memory, but saving resources is not the goal here: throughput is.

Instead of just removing the finished prompt from the batch, we can replace it with a prompt that's waiting for generation. We will call this **dynamic scheduling**, or dynamic batching. Dynamic scheduling is great to maintain throughput while ensuring any token generated by a forward pass is relevant. But because of the way we batched prompts together, it has a major drawback: we need a lot of padding when swapping prompts. That's because the newly-inserted prompt needs to go through prefill while the other prompts are decoding one token at a time. So there is almost as much padding as there are tokens in the newly-inserted prompt.

The problem becomes even worse when batch size increases and initial prompts are long. The padding cost grows quadratically with both batch size and prompt length. If we have a batch of prompts that are in decoding phase and one finishes, dynamically introducing a prompt of initial tokens in the batch requires padding tokens. For instance, with and , we'd need padding tokens!

Furthermore, practical optimizations like CUDA graphs or `torch.compile`

require static tensor shapes. This forces us to pad all prompts to a fixed maximum length, dramatically increasing the padding waste.

At this point, our main problem is padding, which is a consequence of the axis we added to batch sentences together. Thus, the ideal would be to get rid of this axis entirely, a radical rethinking of batching. If we do so, the only way to batch prompts together is to concatenate them:

But we don't want tokens from prompt 0 to interact with the tokens of prompt 1! Luckily for us, we have a way to control how tokens interact with one another: the attention mask. How we do this is displayed below:

Although we use different tints of green to illustrate the different parts of the attention mask, this is still a boolean mask with only greens for `True`

and white for `False`

.
This way of batching prompts together is called **ragged batching** (because sequence lengths are 'ragged' or uneven), and it offers the benefit of added throughput without introducing the need for padding tokens.

In the figure above, we use ragged batching to combine two full prompts together, but we can batch as many as memory allows. The only limit is , the number of tokens we can fit in a batch, with depending on the available memory on the GPU.

Ragged batching is one of the key components of continuous batching. To maximize throughput, we can combine prefill and decoding sequences following an algorithm like this:

- We try to always reach our memory budget of tokens per batch
- We first add all the prompts in decoding phase to the batch, each accounting for 1 token
- We fill the remaining space with prefill phase prompts, relying on the flexibility of chunked prefill to split inputs as needed

Dynamic scheduling is the final piece that contributes to the *continuous batching* technique: we remove finished prompts from the batch as soon as they are done, and replace them with new chunked prompts that correspond to incoming requests.

This combination of ragged batching and dynamic scheduling is called **continuous batching**, and it's the technique that powers modern LLM serving systems.

##
[
](https://huggingface.co#conclusion)
Conclusion

Continuous batching combines three key techniques to maximize throughput in LLM serving:

**KV caching**to avoid recomputing past token representations**Chunked prefill**to handle variable-length prompts within memory constraints**Ragged batching with dynamic scheduling**to eliminate padding waste and keep the GPU fully utilized

By removing the batch dimension and using attention masks to control token interactions, continuous batching allows mixing prefill and decode phases in the same batch, dramatically improving efficiency for serving multiple requests. This is why services like ChatGPT can handle thousands of concurrent users efficiently.

In the next article in this series, we make continuous batching much more efficient by introducing **asynchronous batching**. [Read it here!](https://huggingface.co/blog/continuous_async)

If you'd like to see a deep dive on other continuous batching topics, please let us know in the comments!

*Acknowledgement: thanks to Arthur Zucker for producing the initial concept for the figures used in this article. And thanks to Arthur Zucker, Luc Georges, Lysandre Debut, Merve Noyan and Pedro Cuenca for all providing helpful reviews.*