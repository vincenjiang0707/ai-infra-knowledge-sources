# [Issue #35] [New feature] llama.cpp support

source: https://github.com/FasterDecoding/Medusa/issues/35
state: open | updated: 2025-12-23T04:19:23Z
labels: enhancement

## 正文

We are currently running out of bandwidth. Contributors to help integrate Medusa into llama.cpp would be greatly appreciated :)

## 评论 (8)

### kalomaze · 2023-09-18

What type of skills would be needed? Any specific grunt work in mind? My skillset is probably too narrow if it involves any heavier math but if you can lay it out I might be able to attempt something

### kalomaze · 2023-09-18

It looks like a lot of the groundwork is being laid out here with the parallel decoding implementation:
https://github.com/ggerganov/llama.cpp/pull/3228

### ctlllll · 2023-09-18

> It looks like a lot of the groundwork is being laid out here with the parallel decoding implementation: [ggerganov/llama.cpp#3228](https://github.com/ggerganov/llama.cpp/pull/3228)

Yeah, that's also what I thought. The tree attention implementation in llama.cpp should be very helpful for integrating Medusa. And I guess the main challenge is the familiarity with their codebase.

### JianbangZ · 2023-09-26

We are almost done in supporting medusa in llama.cpp. now working on attention mask part and few other things. 

### kalomaze · 2023-10-07

I would like to help with finalizing the support for this. Is there any place where I can contact the group behind this project and ask questions?

### ctlllll · 2023-10-09

> I would like to help with finalizing the support for this. Is there any place where I can contact the group behind this project and ask questions?

Hi @kalomaze , that would be great, just sent a friend request on Discord :) (I assumed your user name is kalomaze right?)

### kalomaze · 2023-10-28

> > I would like to help with finalizing the support for this. Is there any place where I can contact the group behind this project and ask questions?
> 
> Hi @kalomaze , that would be great, just sent a friend request on Discord :) (I assumed your user name is kalomaze right?)

Sorry, what was your tag? I'm coming back to this now, I figured GitHub would have sent a notification.

### openconstruct · 2025-12-23

Was this indeed implemented?
