# 

source: https://www.together.ai/blog/deepgram-speech-to-text-and-voice-models-now-available-natively-on-together-ai
published: Thu, 02 Apr 2026 00:00:00 GMT

- Deepgram
**Nova-3**,**Nova-3 Multilingual**,**Flux**, and**Aura-2**now run natively on Together AI Dedicated Model Inference - Deepgram covers both ends of the voice pipeline, from transcription to synthesis, in one model lineup
- Together AI gives teams a single production surface for real-time voice agents, with STT, LLM, and TTS on one platform
- Enterprise controls include zero data retention, SOC 2 Type II, HIPAA-ready support, and data residency options

Real-time voice agents often fail when speech is treated as transcription rather than conversation. Getting the words right is only part of the challenge: the system also has to detect turn boundaries, handle interruptions and overlap, and respond quickly enough to keep the exchange feeling natural. When teams try to patch those gaps with endpointing logic, routing layers, and extra providers, they often add latency and operational fragility right back into the system. Deepgram’s models are purpose-built for that layer, where transcription, turn-taking, and responsiveness have to work together in real time.

Deepgram’s STT and TTS model lineup now runs natively on Together AI, the AI Native Cloud for building real-time voice agents, so teams can pair Deepgram transcription and synthesis with any LLM in the Together catalog and run the full voice pipeline on one production platform. For the broader architecture, see our[ real-time voice agents announcement](https://www.together.ai/blog/build-real-time-voice-agents-on-together-ai).

“Voice agents live or die by latency, and every network hop between providers is a place where the experience breaks down. By hosting Deepgram’s STT and TTS natively on Together AI’s infrastructure, we’re giving developers production-grade transcription without the tradeoff. Fast, accurate, and co-located with the rest of the pipeline.”

- Abe Pursell, VP of Partnerships, Deepgram

**Flux: Conversational STT with turn detection**

Accurate transcription is only part of the job. A voice agent also has to know when the speaker is actually finished, because if it misreads the turn, it either talks over the caller or waits too long and feels unresponsive.

[Flux](https://www.together.ai/models/flux) is Deepgram’s conversational STT model for real-time agents, built not just to transcribe speech but to produce turn signals from conversational context rather than silence alone. That matters because many teams still rely on extra endpointing logic to bridge this gap, which adds complexity and makes latency harder to control. Flux simplifies that part of the stack and helps keep turn-taking more predictable in production with 250ms end-of-turn detection.

**Nova-3: Production transcription for real-world audio**

Production audio is messier than benchmark audio. Calls come with background noise, overlapping speakers, accents, telephony compression, and interruptions, and the model still has to return text the rest of the pipeline can trust.[ Nova-3](https://www.together.ai/models/nova-3) is built for those conditions, with support for vocabulary customization so teams can improve recognition of domain-specific terms without retraining.

[Nova-3 Multilingual](https://www.together.ai/models/nova-3-multilingual) extends that approach across multiple languages, which matters in deployments where callers switch languages mid-conversation.

**Aura-2: Enterprise TTS for production voice agents**

[Aura-2](https://www.together.ai/models/aura-2) covers the synthesis side of the pipeline for business environments where clarity and consistency matter. Teams can use Deepgram STT and TTS together while keeping output stable for domain-specific terms and structured entities.

That difference shows up in delivery. The voice has to stay clear, direct, and reliable when it reads structured information or specialized language back to the user. A voice that sounds fine in a demo is not enough if it starts to stumble once the interaction becomes operational.

**Use cases**

**Contact center voice agents**

Contact centers are inherently messy environments. Call quality varies, speakers overlap, interruptions are constant, and latency still has to stay low enough for natural back-and-forth. Deepgram’s models help agents stay in flow through those conditions, keeping conversations responsive and intelligible instead of letting them break down into delays, missed turns, or unclear responses.

**Healthcare voice agents**

Healthcare voice agents need accurate transcription of medication names, procedure terms, and clinical language, along with output that stays clear when reading the same terms back to patients. A transcription error at the start of the pipeline can surface later as a fluent but incorrect response, which is exactly the kind of failure these systems cannot afford. Nova-3 helps teams adapt recognition to clinical language, while Aura-2 keeps patient-facing output clear and consistent.

**Financial services**

Financial voice systems depend on precision. Account numbers, routing numbers, trade confirmations, and structured financial language need to be captured correctly the first time, because a single transcription miss can create a failed transaction, compliance issue, or broken customer interaction. Deepgram’s speech models give teams a stronger foundation for these regulated workflows.

**Multilingual customer support**

Global support teams need speech models that hold up when callers move between languages and accents in the same interaction.[ Nova-3 Multilingual](https://www.together.ai/models/nova-3-multilingual) helps teams serve those conversations without building separate STT pipelines for every market, which makes multilingual support easier to scale and easier to operate.

**Production infrastructure on Together AI**

Deepgram models run on Together AI Dedicated Model Inference alongside LLM and TTS workloads on isolated capacity. Keeping transcription, reasoning, and synthesis in the same production environment makes real-time systems easier to operate and gives teams tighter control over performance as they scale.

Together AI is the AI Native Cloud for production inference, and Dedicated Model Inference gives teams the control and reliability they need to run voice agents at scale.

Together AI supports a broad voice catalog in one place, so teams can mix and match across the pipeline without adding vendors. That includes open-source and proprietary models deployed alongside the LLMs that power agent reasoning.

See the[ Together AI voice solutions](https://www.together.ai/solutions/voice)

**Get started**

- Deepgram’s
[announcement](https://deepgram.com/learn/together-ai-deepgram-voice-partnership) - Read
[STT documentation](https://docs.together.ai/docs/speech-to-text) - Read
[TTS documentation](https://docs.together.ai/docs/text-to-speech) - Read the
[voice agents announcement](https://www.together.ai/blog/build-real-time-voice-agents-on-together-ai) [Contact Sales](https://www.together.ai/contact-sales)for dedicated endpoint deployment and volume pricing