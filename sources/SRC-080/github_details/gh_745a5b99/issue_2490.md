# [Issue #2490] Consolidate Intermediate Offloading

source: https://github.com/vllm-project/llm-compressor/issues/2490
state: closed | updated: 2026-09-24T00:39:32Z
labels: enhancement, good follow-up issue, keep-open, Refactor

## 正文

we have a class [IntermediatesCache](https://github.com/vllm-project/llm-compressor/blob/cf3bd6463e8d471ad6c8cc20a6a9b053c178e555/src/llmcompressor/pipelines/cache.py#L33) which has a bunch of features for on/offloading intermeidates needed in various modifiers/transforms but then we have a few places doing adhoc offloading logic too

AWQ, [smooth_activation_stats](https://github.com/vllm-project/llm-compressor/blob/main/src/llmcompressor/modifiers/awq/base.py#L658-L661) is manually moved to cpu when not being used and device when it is

GPTQ, [hessian offloading](https://github.com/vllm-project/llm-compressor/blob/main/src/llmcompressor/modifiers/gptq/base.py#L253-L269) has its own offloading stuff

the reason for this is the IntermediatesCache does both on/off loading and list-like access logic

for this task i'm looking for someone to

1) change intermediatesCache to be for cacheing a single tensor onloading/offloading -> IntermediateCache
2) change existing usage of intermediatesCache to e.g. use a list of IntermediateCache rather than the cache itself behaving like a list `list.append(IntermediateCache(Tensor))`
3) update existing cached tensors to use IntermediatesCache
4) take the sequential prefetch code and move it to a function that checks the state to do/not do prefetch and the update usage to something like:    

for x in maybe_prefetch(batches_of_stuff)

## 评论 (14)

### menogrey · 2026-03-26

Hi @HDCharles , i would love to work on this. I have checked the code and make some changes locally, and i have some confusion about the point 1. The class `IntermediatesCache` has an attr `batch_intermediates: list[IntermediateValues]`, you want to change it to `batch_intermediate: IntermediateValues` or just delete the dict of `IntermediateValue` to use `intermediate: tensor`?



### HDCharles · 2026-03-27

Yeah the intermediate value abstraction is kinda pointless with this refactor, feel free to remove it

### HDCharles · 2026-04-08

The PR revealed a major issue, the abstraction that i outlined loses the nice UX with automatic onloading since we can no longer steal the `__iter__` as the onloading point.

We need to go back to the drawing board: (@kylesayrs  @brian-dellabetta )

i guess high level the question is a design that can do all of...

A) automatically handle on/offloading
B) work well with prefetch
C) can support singletons without just using a batch with size 0.

Maybe this is workable in the following way:

# option 0 (current main)
we just use cache[0] for singletons

# option 1 (the PR)
1) we have to use IntermediateCache.fetch() whenever we want to onload the actual element so cache_list[batch].fetch() when its a list or cache.fetch() for individual elements

# option 1
1) we keep your new IntermediateCache but name it SingletonCache or something like that, recreate IntermediatesCache which uses SingletonCache for its internals
2) we return the code that previously used IntermediatesCache back to what it was
3) we use SingletonCache in the places where we need a singleton and just accept we have to do cache.fetch()

# option 2 
1) leave IntermediatesCache as it was but add a SingletonCache that uses IntermediatesCache under the hood (abstracting away the single batch handling)
2) still need to use cache.fetch()

# option 3
1) our IntermediatesCache is basically handling the list abstraction and uses that to automatically onload, we could add a IntermedaitesCacheDict to do the same for dicts, which would handle the singletons since those are usually dicts at the top level? 

# option 4
1) do option 1
2) do option 3 but using SingletonCache as the internals

thoughts?

### menogrey · 2026-04-09

When I was working on this PR, I was indeed struggling with the original batch processing logic, so as I understand this issue, I retained the original batch processing logic using some standalone functions. When applying the SingletonCache to the existing cached tensor, it doesn't actually look better, okay at least it appears to use a consistent type..

Option 0,1,2 is clear, can you explain more about option3? I don't know how to automatically onload it.
Take llm-compressor/src/llmcompressor/modifiers/awq/base.py::_smooth_activation_stats as an example.
```
# IntermediatesCacheDict
class IntermediatesCacheDict:
    def __init__(self):
        self._cache_dict ={}

    def update(self, key, value: Tensor, offload_device: device):
        self._cache_dict[key] = offload(value, offload_device)

    def get(self, key):
        return onload(self._cache_dict[key])


# define
_smooth_activation_stats : IntermediatesCacheDict

# init
if smooth_name not in self._smooth_activation_stats:
    self._smooth_activation_stats.update(smooth_name, {"xsum":torch.zeros_like(new_sum), "count":torch.zeros_like(new_count)}, self.offload_device)

# get: onload it
x_sum = self._smooth_activation_stats.get(smooth_name).get("xsum")
count = self._smooth_activation_stats.get(smooth_name).get("count")

# update
x_sum += new_sum
count += new_count
self._smooth_activation_stats.update(smooth_name, {"xsum":x_sum, "count":count}, self.offload_device)

# or use a context manager
with self._smooth_activation_stats.on_loaded(smooth_name) as tmp:
    tmp["xsum"] += new_sum
    tmp["count"] += new_count

```


### brian-dellabetta · 2026-04-09

Can we have IntermediatesCache be typed, `IntermedatesCache[T]` where if T is iterable we allow for an `__iter__` method? And even if it's not iterable, we wrap it in a list to not fail out? To reduce the number of classes we would have to carry around (SingletonCache, IntermediatesCacheDict, etc.)

### menogrey · 2026-04-13

I think we need to strip away the logic of the original IntermediatesCache and see what we can reassemble, and what should be reused. There are roughly these parts: 

* recursive structure support. No need for singleton, for original batch.
* CRUD operations.
* list index queries. Associated with CRUD. Maybe we can move the wrap list out of class.
* dictionary filtering. Associated with CRUD and the iterative prefetching.
* iterative prefetching. Depends on sequence structure, if we want to move list out of class, the prefetch should be a standalone function.
* from dataloader.
* shared tensor offload map.

If we use a unified `IntermedatesCache`, the list index queries and dictionary filtering (especially for module forward arguments) should be moved outside class.

For original cache use:
```
caches = list(Cache)
# fetch with filter:
fetched = caches[idx].fetch()
filtered = {
    key: value
    for key, value in fetched.items()
    if key in filter_keys
}
```

Cache class holds: 
* recursive structure support.
* CRUD:
* shared tensor offload map.
* from dataloader.

Standalone function:
* prefetch


### menogrey · 2026-04-13

@HDCharles  @brian-dellabetta  Based on the above ideas, I have a new commit and I hope you can give me your feedback. https://github.com/vllm-project/llm-compressor/commit/f7935630743817fac45b239f58d52f9ad00c52f5#diff-9f52aa2e44c1087d967cb879e165728c01a4d8cddec353fd8e6a0d6c91198c00

### brian-dellabetta · 2026-04-14

Hi @menogrey , I'm following what you're doing but it just seems weird to me that the user of IntermediatesCache will be doing things like this:
```
    _parent_args_cache: dict[Module, list[IntermediatesCache]] = PrivateAttr(
        default_factory=dict
    )
    # Dict[smooth layer name, [activation sums, activation counts]]
    _smooth_activation_stats: dict[str, IntermediatesCache] = PrivateAttr(
        default_factory=dict
    )
```
I would think it would be more understandable as
```
    _parent_args_cache: dict[Module, IntermediatesCache[list[torch.Tensor]]] = PrivateAttr(
        default_factory=dict
    )
    # Dict[smooth layer name, [activation sums, activation counts]]
    _smooth_activation_stats: dict[str, IntermediatesCache[torch.Tensor]] = PrivateAttr(
        default_factory=dict
    )
```
and we can keep the `iter_prefetch` method directly on the class. @HDCharles what do you think?

### HDCharles · 2026-04-14

hey sorry if i dont respond after a day or so, reach out to me in the vllm slack.

about option 3, i was just noticing that most of the time the stuff we want to cache is in a dict,

` _parent_args_cache: dict[Module, IntermediatesCache] -> _parent_args_cache: IntermediatesDict[Module, Iterator]`
usage could be 

`for activation in _parent_args_cache[cur_module]:`

and we make IntermediatesDict return an iterator whose fetch behavior does the onloading and/or sequential prefetch

but can also be something like 

`_hessians: dict[Module, torch.Tensor] -> _hessians: IntermediatesDict[Module, torch.Tensor] ` and onload as soon as the tensor is accessed?

the issue is we'd have to support the dict part and this weird iterator thing. I was hoping we'd be able to just do one.

--------

@brian-dellabetta yeah i think thats option 0, right? the issue being that for something like 

`_hessians: dict[Module, IntermediatesCache]`

you have to do self._hessians[module][0] to access rather than self._hessians[module].

That may just be the best option.

### menogrey · 2026-04-15

Okay, I will try to give a new implement according to your advice.

### menogrey · 2026-04-17

Hi @brian-dellabetta @HDCharles ,  I carefully checked the existing cache data types and found we should support the following [T]:
Existed:
```
_parent_args_cache: dict[Module, IntermediatesCache] -> IntermediatesCache[list[dict[str, Any | Tensor]]]
activations: IntermediatesCache.from_dataloader -> IntermediatesCache[list[dict[str, Any | Tensor]]]
```
Want to update:
```
_smooth_activation_stats: dict[str, list[torch.Tensor]] -> IntermediatesCache[list[Tensor]]
_hessians: Dict[torch.nn.Module, torch.Tensor] -> IntermediatesCache[Tensor]
```

The existed IntermediatesCache is actually the specific `IntermediatesCache[list[dict[str, Any | Tensor]]]`, and the `fetch()` `update()` you have to pass the related dict key.

So option 0 I am not sure how to make it compatible. Otherwise we make `_hessians: dict[Module, IntermediatesCache[list[dict[str, Any | Tensor]]]]` ,  and access with `cache.fetch(0)["hessian"]`, this looks strange and you have to construct the redundant structure of it.

Also the related operator about IntermediatesCache.

Existed:
```
IntermediatesCache[list[dict[str, Any | Tensor]]]

append and offload : cache.append(dict[str, Any | Tensor])
iter and prefetch: cache.iter_prefetch(filtered_keys)  and this also filter the dict keys
fetch with list index and the dict keys : cache.fetch(list_idx, filtered_keys)
update with list index and the updated dict: cache.update(list_idx, updated_dict)
delete with list index and the dict keys : cache.delete(list_idx, deleted_keys)
```

Want to update:
```
IntermediatesCache[list[Tensor]]

fetch with list index: cache.fetch(0)
update with list index: tensor=cache.fetch(0) tensor+=new_tensor  cache.update(0, tensor)

IntermediatesCache[Tensor]

fetch: cache.fetch()
update: cache.update(new_tensor)
```

So, the `IntermediatesCache[list[dict[str, Any | Tensor]]]` is more complicated. And I think if want to make them unified, have to make IntermediatesCache easy to access every level of the structure, and when you want to update only cache[1]["foo"], you don't have to onload and offload the whole list. So I think the recursive structure is needed, and also the update/delete/get interfaces for every level of it. 

I have a new version but not sure about it and hope you give some advices.

https://github.com/vllm-project/llm-compressor/compare/main...menogrey:llm-compressor:refactor_intermediate_cache5?diff=unified&w

### brian-dellabetta · 2026-04-20

I feel like we're adding a lot of complexity to the types here that are going to confuse users:
```python
_parent_args_cache: dict[Module, IntermediatesCache] -> _parent_args_cache: dict[Module, IntermediatesCache[list[dict[str, torch.Tensor]]]]
```
at the end of the day we want a look-up table for an arbitrary, user-defined key to an offloaded tensor, so for parent args cache I'm proposing we flatten all this into a single key (which can be composite)
```python
BatchIdx = int
TKey = tuple[Module, BatchIdx, str]
_parent_args_cache: IntermediatesCache[TKey]
```
so that we allow for a key entirely defined by the user. And the value returned is always a torch.Tensor that gets onloaded during get and offloaded during set.
That way we can allow users to fetch singleton values without indexing, by calling `.fetch()` instead of `fetch(key)`, and also to prefetch iterables, by passing in a list of keys
```python
prefetched = _parent_args_cache.iter_prefetch((module, batch_idx, "hessian") for batch_idx in range(n_batches))
```

### github-actions[bot] · 2026-07-20

This issue has been automatically marked as stale because it has not had any activity within 90 days. It will be automatically closed if no further activity occurs within 30 days. Leave a comment if you feel this issue should remain open. Thank you!

### kylesayrs · 2026-09-24

Closed now that GPTQ hessian offloading has been removed
