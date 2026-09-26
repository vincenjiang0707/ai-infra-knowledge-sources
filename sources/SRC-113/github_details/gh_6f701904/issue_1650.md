# [Issue #1650] Tips please - personal project + idea for inference 

source: https://github.com/mlcommons/inference/issues/1650
state: closed | updated: 2026-05-06T00:41:00Z
labels: Stale

## 正文

Hi there, just saw the video from the ai engineer
Inference looks really awesome

I've got this mini project in mind for years now,
Getting a model to tell how full is a glass/bowl/cooking pot/other container in (from a camera stream)

0%-100% from empty to full/overflowing 
Commercially, if this can be achieved from a small model, it could be added to home water units, smart coffee makers, etc,
But for me personally, I want my dog's water bowl to always be full.

Yes this can be done in a bunch of different ways from Arduino ultrasound and others but, a camera+ai approach means that the solution could be generic, and work for all types of glasses and containers, transparent or opaque, small glass or big pot for the dogs. It will only fill if the bowl is positioned mostly center (with accepted margin) taking the bowl/glass away stops the flow. 
Simple metrics, simple rules, operate 1 iot valve,  work generically.

So basically I wanted to ask if anyone could recommend which to use for this application?
OpenCV + clip (+ kalman filter)? Or are there models out there that might be better? Is there a chance to do it from a weak espcam or rpi 0/cm, or will I have to do the inference on a server away from the sensor? I'll appreciate any wisdom you might have 

Thanks a lot and have a good one!

P.s - a bit meta, it would be awesome when there'll be an llm that is always up-to-date with inference, and we could ask it these sort of questions, get best matching models, hone in and choose models that are suited for the hw of choice, and even generate code which pulls from inference to match our mission
Like an inference-assisted issue2repo ai ftw

All the best!

## 评论 (1)

### github-actions[bot] · 2026-05-06

🔒 This issue has been **automatically closed** because it has been open for more than 2 years with no activity.
If this is still relevant, you may **reopen it or create a new one**.
