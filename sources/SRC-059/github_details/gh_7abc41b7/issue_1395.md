# [Issue #1395] Adding characters

source: https://github.com/PaddlePaddle/ERNIE/issues/1395
state: closed | updated: 2025-12-18T03:51:44Z
labels: 

## 正文

i am trying to fine-tune paddleocr-vl-0.9b for devanagari text recognition using erniekit, and i need to add some characters to the dictionary, how can i do that? Which file do i need to modify? 

## 评论 (2)

### Sunting78 · 2025-12-17

You most likely do NOT need to modify any dictionary file. Since `PaddleOCR-VL-0.9b` is a Vision-Language Model, it works  a **Tokenizer** which supports **Byte Fallback**. Even if the specific Devanagari character is not in the `vocab.json` or `tokenizer.model`, the model will represent it as a sequence of bytes (e.g., `[224, 164, 133]`). The model can learn to recognize these byte sequences effectively during fine-tuning.

Before trying to modify the model, run this Python script to check how the model sees Devanagari text.

```python
from transformers import AutoTokenizer

# Load the tokenizer for PaddleOCR-VL-0.9b
# (Replace with your actual model path)
model_path = "Path/To/PaddleOCR-VL-0.9b" 
tokenizer = AutoTokenizer.from_pretrained(model_path, trust_remote_code=True)

# Test with Devanagari text
text = "नमस्ते"  # Namaste
ids = tokenizer.encode(text, add_special_tokens=False)
tokens = tokenizer.convert_ids_to_tokens(ids)

print(f"Text: {text}")
print(f"Token IDs: {ids}")
print(f"Tokens: {tokens}")

# Check for [UNK]
if tokenizer.unk_token_id in ids:
    print("CRITICAL: The tokenizer produced [UNK]. You MUST add characters.")
else:
    print("GOOD: No [UNK] detected. The model is using Byte Fallback. You do NOT need to edit the dictionary.")
```

*   **If the output shows multiple tokens/bytes but NO `[UNK]`**: You are good to go. Just start fine-tuning with your dataset.
*   **If the output shows `[UNK]`**: Only then do you need to add tokens.

If you absolutely MUST add tokens, you need to modify as follow: 

1.  **Load Tokenizer & Model**:
    ```python
    tokenizer = AutoTokenizer.from_pretrained(model_path, trust_remote_code=True)
    model = AutoModelForCausalLM.from_pretrained(model_path, trust_remote_code=True)
    ```

2.  **Add Tokens**:
    ```python
    # List of unique Devanagari characters from your dataset
    new_chars = ["अ", "आ", "इ", "ई", ...] 
    
    # Add to tokenizer
    num_added = tokenizer.add_tokens(new_chars)
    ```

3.  **Resize Model Embeddings (Crucial Step)**:
    If you don't do this, the shapes won't match, and training will crash.
    ```python
    model.resize_token_embeddings(len(tokenizer))
    ```

4.  **Save the new Tokenizer**:
    You must save this modified tokenizer so you can use it for inference later.
    ```python
    tokenizer.save_pretrained("./output_dir_with_new_vocab")
    ```


### DOOMBOT0 · 2025-12-18

@Sunting78 , thank you for taking your time to answer my question.
I ran the script and it seems that i dont need to add characters.

