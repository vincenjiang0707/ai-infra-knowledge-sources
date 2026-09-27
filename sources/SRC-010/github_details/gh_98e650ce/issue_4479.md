# [Issue #4479] [Bug] 为什么qwen3VL的logits、last_hidden_state不支持返回呢？

source: https://github.com/InternLM/lmdeploy/issues/4479
state: open | updated: 2026-04-20T02:57:50Z
labels: 

## 正文

### Checklist

- [ ] 1. I have searched related issues but cannot get the expected help.
- [ ] 2. The bug has not been fixed in the latest version.
- [ ] 3. Please note that if the bug-related issue you submitted lacks corresponding environment info and a minimal reproducible demo, it will be challenging for us to reproduce and resolve the issue, reducing the likelihood of receiving feedback.

### Describe the bug

```
gen_config=GenerationConfig(
        temperature=0.0,
        top_k = 1,
        output_logits='generation',
        output_last_hidden_state='generation',
        max_new_tokens=2048)
    
    # pipe = pipeline(args.model_path, backend_config=backend_config)
    pipe = pipeline(args.model_path)

    response = pipe(['Hi, pls intro yourself', 'Shanghai is'],
                gen_config=gen_config)
    hidden_states = [x.last_hidden_state for x in response]
    logits = [x.logits for x in response]

    # pdb.set_trace()
    print(hidden_states)
    print(logits)
```

### Reproduction

```
gen_config=GenerationConfig(
        temperature=0.0,
        top_k = 1,
        output_logits='generation',
        output_last_hidden_state='generation',
        max_new_tokens=2048)
    
    # pipe = pipeline(args.model_path, backend_config=backend_config)
    pipe = pipeline(args.model_path)

    response = pipe(['Hi, pls intro yourself', 'Shanghai is'],
                gen_config=gen_config)
    hidden_states = [x.last_hidden_state for x in response]
    logits = [x.logits for x in response]

    # pdb.set_trace()
    print(hidden_states)
    print(logits)
```

### Environment

```Shell
官方环境
```

### Error traceback

```Shell

```

## 评论 (0)
