# [Issue #2370] [RFE]: Make Thrust support iterators with proxy references

source: https://github.com/NVIDIA/nccl/issues/2370
state: closed | updated: 2026-08-25T14:29:37Z
labels: enhancement

## 正文

### Please provide the below details to ensure we understand your needs

I am developing a library that heavily relies on proxy objects. 
(For example, a row of a 2D array is a proxy object "reference" but not a language reference.)

It turns out that Thrust is a bit hostile to the conventions it carries.
I wouldn't say it is a bug, so I am simply proposing that Thrust support this.

This is the reproducer (with no dependencies): https://godbolt.org/z/M9sxc43TM

(In the reproducer, I can add the ".get" method to the fancy pointer to "make" it compile but it fails at runtime.)

I typically work around Thrust limitations by adding overloads, but in this case I wasn't able to.

Apparently, this would be a valid patch to Thrust:

```cpp
template<typename T>
 __host__ __device__
 typename detail::raw_reference<T>::type
   raw_reference_cast(T &ref)
 {
-  return *thrust::raw_pointer_cast(&ref);
+  if constexpr (!detail::is_unwrappable<T>::value) { return ref; }
+  else { return *thrust::raw_pointer_cast(&ref); }
 }
 
 template<typename T>
 __host__ __device__
 typename detail::raw_reference<const T>::type
   raw_reference_cast(const T &ref)
 {
-  return *thrust::raw_pointer_cast(&ref);
+  if constexpr (!detail::is_unwrappable<T>::value) { return ref; }
+  else { return *thrust::raw_pointer_cast(&ref); }
 }
```

## 评论 (3)

### sjeaugey · 2026-08-25

How is this request related to NCCL? It looks like a request for the Thrust project? @correaa let us know if this was simply a "bad project" mistake, or this is actually related to NCCL. Thanks!

### correaa · 2026-08-25

Sorry, I meant to file this to CCCL. Please ignore it.

On Tuesday, August 25, 2026, Sylvain Jeaugey ***@***.***>
wrote:

> *sjeaugey* left a comment (NVIDIA/nccl#2370)
> <https://github.com/NVIDIA/nccl/issues/2370#issuecomment-5407684196>
>
> How is this request related to NCCL? It looks like a request for the
> Thrust project? @correaa <https://github.com/correaa> let us know if this
> was simply a "bad project" mistake, or this is actually related to NCCL.
> Thanks!
>
> —
> Reply to this email directly, view it on GitHub
> <https://github.com/NVIDIA/nccl/issues/2370?email_source=notifications&email_token=AAXICU6KT7PKY5X6KENPQJL5LVFY3A5CNFSNUABFM5UWIORPF5TWS5BNNB2WEL2JONZXKZKDN5WW2ZLOOQXTKNBQG43DQNBRHE3KM4TFMFZW63VHNVSW45DJN5XKKZLWMVXHJLDGN5XXIZLSL5RWY2LDNM#issuecomment-5407684196>,
> or unsubscribe
> <https://github.com/notifications/unsubscribe-auth/AAXICU5VOL24OU3BGYWM3C35LVFY3AVCNFSNUABEKJSXA33TNF2G64TZHM2DMMJVGM4DSMR3JFZXG5LFHM2TENBSGYYTKMBWGKQXMAQ>
> .
> You are receiving this because you were mentioned.Message ID:
> ***@***.***>
>


### correaa · 2026-08-25

Submitted to the right project, **C**CCL, not NCCL. https://github.com/NVIDIA/cccl/issues/10999 . (Sorry for the global shortage of acronyms)
