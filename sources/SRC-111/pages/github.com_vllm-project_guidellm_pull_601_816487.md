source: https://github.com/vllm-project/guidellm/pull/601

# Containerfile: ensure that HOME can be used by any user ID - #601

## Conversation

OpenShift Pods can't use the cache otherwise Fix: 600 Signed-off-by: Kevin Pouget <kpouget@redhat.com>


**reviewed**

[dbutenhof](https://github.com/dbutenhof)Feb 17, 2026

###
**
**[dbutenhof](https://github.com/dbutenhof)
left a comment

**left a comment**

[dbutenhof](https://github.com/dbutenhof)

There was a problem hiding this comment.

I think I find the "can be used by any user" a bit misleading since this assumes we're running in GID 0 (setting `$HOME`

group to 0 and copying user mode bits to group). That covers both the OpenShift and standalone container use cases, but the wording suggests something more universal. I think it's "interesting" that you're copying user mode bits rather than just assigning something "known good" like `g=rwX`

; although it's probably safe to assume that the `$HOME`

user mode bits are good by default ...

[Containerfile](https://github.com/vllm-project/guidellm/pull/601/files/c6607e2c6592fc8aebbcbbd04ce76e20c56af353#diff-5fcdf9b4580789697d834d1456a22bcfaa236d668fc180cad4775afc36ed5914)Outdated

|
the command and comment (
|

Signed-off-by: Kevin Pouget <kpouget@redhat.com>

Huh. Well, "arbitrary user in group 0", anyway; but if that's a quote from the documentation I guess I can't complain to you. 😆 |


**approved these changes**

[dbutenhof](https://github.com/dbutenhof)Feb 17, 2026

[Learn more about bidirectional Unicode characters](https://github.co/hiddenchars)

OpenShift Pods can't use the cache otherwise

Resolves: 600

## Use of AI

`## WRITTEN BY AI ##`

)