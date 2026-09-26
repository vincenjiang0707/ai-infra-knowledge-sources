# [Issue #446] serializer.deserialize(serialized) duplicate the last dict data

source: https://github.com/vllm-project/guidellm/issues/446
state: closed | updated: 2026-06-24T20:02:39Z
labels: 

## 正文

**Describe the bug**
A clear and concise description of what the bug is.

when i debug xfail ut case: tests/unit/utils/test_encoding.py::TestMessageEncoding::test_encode_decode_generative[dict_serialization_msgpack-obj0]
assertion failure is:

<img width="2173" height="478" alt="Image" src="https://github.com/user-attachments/assets/4557e261-c813-44ae-9e43-5a49f5f7a1e4" />

As screenshot show, the last dict data total_tokens=None is duplicated.

And the problem is serializer.deserialize(serialized) in src/guidellm/utils/encoding.py:

<img width="2196" height="1393" alt="Image" src="https://github.com/user-attachments/assets/5a738080-8d4b-4690-9ad8-e42672507448" />

**Expected behavior**
A clear and concise description of what you expected to happen.

**Environment**
Include all relevant environment information:
1. OS [e.g. Ubuntu 20.04]: conda 25.3.1
2. Python version [e.g. 3.12.2]: guidellm version: 0.4.0.dev0

**To Reproduce**
Exact steps to reproduce the behavior:


**Errors**
If applicable, add a full print-out of any errors or exceptions that are raised or include screenshots to help explain your problem.

**Additional context**
Add any other context about the problem here. Also include any relevant files.


## 评论 (3)

### markurtz · 2025-11-19

@tukwila just confirming that this is happening on main/0.4?

### tukwila · 2025-11-21

> [@tukwila](https://github.com/tukwila) just confirming that this is happening on main/0.4?

Yes, now in main:
guidellm version: 0.5.0.dev10

<img width="2039" height="1302" alt="Image" src="https://github.com/user-attachments/assets/b7d05edd-7c99-4be3-a123-b11d25aa8f8a" />

but we cannot find a solution till now:
<img width="934" height="376" alt="Image" src="https://github.com/user-attachments/assets/24badea1-55af-4355-9e2a-622ba05422cf" />

### SkiHatDuckie · 2026-06-24

I've been messing around with this for a bit and seems like the root cause is in serializer.to_dict_pydantic (encoding.py):

```python
def to_dict_pydantic(self, item: Any) -> Any:
        ...
        return {
            "*PYD*": True,
            "typ": item.__class__.__name__,
            "mod": item.__class__.__module__,
            "dat": item.model_dump(mode="python"),
        }
```

`model_dump()` by default includes computed fields. Those computed fields are then treated as extra fields when calling `model_validate()` (which occurs during the calling of serializer.deserialize(serialized)). More details: [https://github.com/pydantic/pydantic/discussions/8580](https://github.com/pydantic/pydantic/discussions/8580)

Going off of the previous referenced link, the solution might be to somewhere either exclude or ignore extra/computed fields.
