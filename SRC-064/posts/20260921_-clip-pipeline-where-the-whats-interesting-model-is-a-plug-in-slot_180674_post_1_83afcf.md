# Local clip pipeline where the "what's interesting" model is a plug-in slot

source: https://discuss.huggingface.co/t/local-clip-pipeline-where-the-whats-interesting-model-is-a-plug-in-slot/180674#post_1
published: Mon, 21 Sep 2026 20:11:28 +0000

I maintain an open-source app that turns long streams into vertical clips

entirely on the user’s machine. Sharing it here for one specific reason: the

part that decides which moments matter is deliberately swappable, and I would

rather other people fill it than guess at it myself.

What runs today: YOLOv8 finds people, OpenCV Haar cascades find the face

inside each person box, and TalkNet-ASD decides which face is actually

speaking so the 16:9 to 9:16 crop follows the speaker.

That last model earns its place. The intuitive approach is to follow whichever

mouth is moving, and it does not work. On a real two-person clip, mouth-region

pixel motion scored the speaker 0.0746 and the listener 0.0801, a 7%

difference in the wrong direction, while their on-screen sizes differed by

45%. Pixel motion measures movement, not speech, so anything built on it

follows whoever is nearest the camera.

The open slot is the scoring side. Which moments become clips is decided by

per-second signals that get percentile-ranked and scanned for peaks. A

detector that emits a confidence over the timeline becomes one more signal

and its peaks become candidate clips, with nothing in the scorer changing.

So if you have a model for footage this was never tuned for, sports, gaming,

reactions, lectures, wildlife, it can drive clip selection without rewriting

the pipeline. I am not building any of those. I would rather the seam exist

and other people use it.

Contract, the file to copy and the performance trap:

AGPL-3.0, Windows, nothing leaves the machine.