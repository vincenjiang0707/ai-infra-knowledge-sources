# [Issue #1418] Support predictive autoscaling for LLM inference

source: https://github.com/vllm-project/aibrix/issues/1418
state: open | updated: 2026-09-24T14:24:18Z
labels: area/autoscaling, priority/important-soon, kind/feature

## 正文

### 🚀 Feature Description and Motivation

We used to do a lot of work around reactive autoscaling, however, the model bootstrap still take looks long time. Instead of traditional autoscaling, we want to provide another option - the time series prediction method to solve the latency issue. 

### Use Case

LLM autoscaling

### Proposed Solution

_No response_

## 评论 (12)

### Belyenochi · 2025-08-14

Hi @Jeffwan! I'm very interested in this predictive autoscaling feature. 

I have experience with time series forecasting (using Prophet/LSTM) and Kubernetes autoscaling. I understand the pain point of model bootstrap latency in LLM inference.

I'd like to work on this issue. My approach would be:
1. Design a time series prediction module for traffic forecasting
2. Integrate with existing autoscaling mechanisms
3. Add configuration options for prediction parameters

Could I be assigned to this issue? I estimate it would take 3-4 weeks to deliver a solution.

### Jeffwan · 2025-08-18

thanks for driving this effort. @Belyenochi I just assign this issue to you

### Belyenochi · 2025-08-18

Hi @Jeffwan,
Thanks for assigning this to me! I'm excited to work on #1418.

I've been researching how Netflix Scryer and Google Cloud handle predictive autoscaling, and I'm curious about your thoughts on applying these approaches to LLM workloads.

*From what I found, there seem to be two main philosophies:*

*Netflix Scryer:*
- Scale-up: Aggressive predictive expansion, reactive can supplement
- Scale-down: Predictive sets safety floor, prevents over-contraction  
- Philosophy: "Better to over-provision than under-serve"

*Google Cloud:*
- Scale-up: Confidence-driven blending of predictive + reactive signals
- Scale-down: Predictive-driven with reactive override for emergencies
- Philosophy: "Optimize for cost efficiency while maintaining SLO"

*Initial thoughts for LLM scenarios:*

Given the LLM cold start challenges (5-8min model loading), I'm thinking a Netflix-style asymmetric approach might work well:

*Scale-Up Strategy:*
- What do you think about proactive expansion based on predicted traffic patterns?
- Decision logic could be: `max(predicted_need, reactive_suggestion)`
- The rationale being that cold starts are so expensive for LLMs that reactive scaling might be too late

*Scale-Down Strategy:*
- I'm wondering if we should use predictive floor protection to prevent over-aggressive scale-down
- Maybe something like: `max(predicted_minimum, reactive_suggestion)`
- This could help avoid those painful cold start delays when traffic picks back up

*Technical Implementation Questions:*

Currently AIBRIX pulls metrics directly from vLLM pods. For predictive capabilities, I'm thinking we could:
- *Add Prometheus integration*: Query historical metrics for pattern analysis - does this align with your API refactor plans?
- *Implement Netflix Scryer-style prediction*:
 - Weekly periodicity analysis (they use same-weekday patterns since Tuesday vs Tuesday is more similar than Tuesday vs Wednesday)
 - 8-12 weeks lookback window with time-decay weighting 
 - 10-minute aggregation windows for pattern detection
- *Extend PodAutoscaler*: Add predictive metricSource alongside existing reactive ones

Do you think this approach makes sense for our use cases? I'm curious about:
- Whether our production workloads show clear weekly/daily patterns that would benefit from this kind of prediction
- Any constraints from the API refactor that might influence the design
- Your thoughts on the Netflix vs Google philosophy for our scenarios
- Whether Prometheus as the single data source would be sufficient for this

References:
- Netflix Scryer: http://techblog.netflix.com/2013/11/scryer-netflixs-predictive-auto-scaling.html
- Netflix Scryer Part 2: https://netflixtechblog.com/scryer-netflixs-predictive-auto-scaling-engine-part-2-bb9c4f9b9385
- Google Cloud predictive autoscaling: https://cloud.google.com/compute/docs/autoscaler/predictive-autoscaling

Perfect timing on the API refactor - having a clean, well-designed autoscaling API will make integrating the predictive component much smoother! While we wait for the new baseline, I can start working on the predictive algorithm design and Prometheus integration.

Looking forward to discussing this further!

Thanks!

### Jeffwan · 2025-08-19

@Belyenochi Great start! I love this rough design. Here’s how I’d evaluate and shape predictive autoscaling for LLM workloads in AIBrix.

- I think both the Netflix and Google philosophies are valuable, and the choice between them is mostly a strategy question If I understand correctly. I do not have strong preference at this moment. I will learn and give some comments later
- Unified entry point: expose predictive and reactive as sources within the same API, so users just declare whether they want prediction enabled, not learn a different CRD or controller. Let's try to what changes need to be done in https://github.com/vllm-project/aibrix/blob/main/api/autoscaling/v1alpha1/podautoscaler_types.go. If the API is totally different, we could consider to use a new one.  
- Bytedance used to work on intelligent HPA in project katalyst. I linked the reference there. My original ideas is to bring the code back to AIBrix to save some efforts since we are from same team. :D Please help evaluate the ihpa and see whether we can save some efforts if we build a new solution on top of it. 
- Model specific metrics: Most time-series prediction solution requires x days traffic to be able to provide prediction, let me know anything I can support your development work

references:
- https://dl.acm.org/doi/pdf/10.1145/3342195.3387524 Google's autopilot paper
- https://github.com/kubewharf/katalyst-api/blob/main/pkg/apis/autoscaling/v1alpha2/ihpa.go
- https://github.com/kubewharf/katalyst-core/tree/main/pkg/controller/ihpa



### Belyenochi · 2025-08-19

Hi @Jeffwan,

Thanks for the detailed feedback! After analyzing the katalyst iHPA implementation, I have some findings and would like to discuss the best path forward:

## Current State Analysis

I examined the katalyst iHPA code ([ihpa.go](https://github.com/kubewharf/katalyst-api/blob/main/pkg/apis/autoscaling/v1alpha2/ihpa.go) and [controller](https://github.com/kubewharf/katalyst-core/tree/main/pkg/controller/ihpa) and found that **the current iHPA doesn't have time-series prediction capabilities yet**. It's essentially a wrapper around standard Kubernetes HPA with enhanced integration for SPD (Service Profile Descriptor) and VirtualWorkload management.

## Proposed Approach

Given your suggestion to leverage existing katalyst work, I'm thinking the most beneficial approach would be:

### Phase 1: Enhance katalyst iHPA with Predictive Capabilities

Since katalyst is an open source project, I'd like to contribute the predictive autoscaling implementation directly to iHPA. This would benefit the entire cloud-native community and align perfectly with the goals of Issue #1418.

**Proposed API Extension for katalyst iHPA:**
```go
// In katalyst-api/pkg/apis/autoscaling/v1alpha2/ihpa.go
type IntelligentHorizontalPodAutoscalerSpec struct {
    // Existing fields...
    Autoscaler AutoscalerSpec `json:"autoscaler"`
    
    // New: Predictive scaling configuration
    // +optional
    PredictiveConfig *PredictiveConfig `json:"predictiveConfig,omitempty"`
}

type PredictiveConfig struct {
    Enabled bool `json:"enabled"`
    LookAheadMinutes *int32 `json:"lookAheadMinutes,omitempty"`
    HistoryDays *int32 `json:"historyDays,omitempty"`
}
```

### Phase 2: AIBrix Integration with Enhanced iHPA

Once katalyst iHPA has predictive capabilities, AIBrix could integrate it seamlessly:

**AIBrix PodAutoscaler API Changes:**
```go
// In aibrix/api/autoscaling/v1alpha1/podautoscaler_types.go
type PodAutoscalerSpec struct {
    // Existing AIBrix fields
    ScaleTargetRef corev1.ObjectReference `json:"scaleTargetRef"`
    MinReplicas *int32 `json:"minReplicas,omitempty"`
    MaxReplicas int32 `json:"maxReplicas"`
    MetricsSources []MetricSource `json:"metricsSources,omitempty"`
    ScalingStrategy ScalingStrategyType `json:"scalingStrategy"`
    
    // New: Predictive scaling delegation to iHPA
    // +optional
    PredictiveScaling *PredictiveScaling `json:"predictiveScaling,omitempty"`
}

type PredictiveScaling struct {
    Enabled bool `json:"enabled"`
    LookAheadMinutes *int32 `json:"lookAheadMinutes,omitempty"`
    HistoryDays *int32 `json:"historyDays,omitempty"`
}
```

## Predictive Autoscaling Logic (Netflix-Style)

**Core Philosophy: "Better to over-provision than under-serve"**

```go
// Netflix-style predictive autoscaling implementation
type PredictiveScaler interface {
    // Predict required replica count based on historical patterns
    PredictReplicas(ctx context.Context, 
                   currentState WorkloadState,
                   historicalData []MetricPoint,
                   lookAheadMinutes int32) (int32, error)
}

// Main scaling decision logic - Netflix approach
func (r *PodAutoscalerController) calculateDesiredReplicas(
    pa *PodAutoscaler) (int32, string, error) {
    
    if pa.Spec.PredictiveScaling != nil && pa.Spec.PredictiveScaling.Enabled {
        // Netflix style: Trust the prediction algorithm
        predictedReplicas, err := r.predictiveScaler.PredictReplicas(
            r.getCurrentState(pa),
            r.getHistoricalMetrics(pa),
            *pa.Spec.PredictiveScaling.LookAheadMinutes,
        )
        
        if err != nil {
            // Only fallback when prediction completely fails
            return r.calculateReactiveReplicas(pa), "reactive-fallback", nil
        }
        
        // Netflix philosophy: Aggressive predictive expansion
        // Reactive supplements upward when current load exceeds prediction
        reactiveReplicas := r.calculateReactiveReplicas(pa)
        
        // Take maximum - better to over-provision than under-serve
        return max(predictedReplicas, reactiveReplicas), "predictive", nil
    }
    
    // Pure reactive scaling (traditional HPA behavior)
    return r.calculateReactiveReplicas(pa), "reactive", nil
}

// Traditional HPA-style calculation for reactive scaling
func (r *PodAutoscalerController) calculateReactiveReplicas(pa *PodAutoscaler) int32 {
    currentMetrics := r.getCurrentMetrics(pa)
    targetValue := r.getTargetValue(pa)
    currentReplicas := pa.Status.CurrentReplicas
    
    // Standard HPA formula
    return int32(math.Ceil(float64(currentReplicas) * currentMetrics / targetValue))
}
```

## Architecture & Usage Example

**Netflix-Style Decision Flow:**
```
┌─────────────────────┐
│ Historical Data     │
│ Collection          │
└─────────────────────┘
          │
          ▼
┌─────────────────────┐
│ Predictive          │ ──► Predicted Replica Count
│ Algorithm           │     (aggressive expansion)
└─────────────────────┘
          │
          ▼
┌─────────────────────┐
│ Algorithm Success?  │
└─────────────────────┘
        │
    ┌───┴───┐
    ▼       ▼
Success   Failure
    │       │
    ▼       ▼
┌────────┐ ┌──────────────┐
│Use     │ │Fallback to   │
│Predict │ │Reactive Only │
└────────┘ └──────────────┘
    │
    ▼
┌─────────────────────┐
│ Reactive Check      │ ──► Current load calculation
│ (Supplementation)   │     
└─────────────────────┘
    │
    ▼
┌─────────────────────┐
│ max(predicted,      │ ──► Netflix: Better to over-provision
│     reactive)       │     
└─────────────────────┘
    │
    ▼
┌─────────────────────┐
│ Apply Safety Bounds │
│ (min/max replicas)  │
└─────────────────────┘
```

**For LLM workloads in AIBrix:**
```yaml
apiVersion: autoscaling.aibrix.io/v1alpha1
kind: PodAutoscaler
metadata:
  name: llm-service-autoscaler
spec:
  scaleTargetRef:
    apiVersion: apps/v1
    kind: Deployment
    name: llm-service
  minReplicas: 2          # Safety floor
  maxReplicas: 20         # Safety ceiling  
  scalingStrategy: APA    # AIBrix Predictive Algorithm
  metricsSources:
  - metricSourceType: pod
    protocolType: http
    path: /metrics
    targetMetric: "kv_cache_utilization"
    targetValue: "70"
  predictiveScaling:
    enabled: true
    lookAheadMinutes: 480  # 8 minutes for LLM cold start
    historyDays: 14        # Capture weekly business patterns
```

**Example Scenario - Morning Preparation:**
```
Time: 09:30
• current_replicas: 5
• current_kv_cache_utilization: 45%
• predicted_replicas: 12 (algorithm forecasts 10am meeting rush)
• reactive_replicas: 5 * 45% / 70% = 4 (current need)

Netflix Decision:
• Use prediction: 12 replicas (trust the algorithm)
• Reactive check: max(12, 4) = 12
• Action: Aggressive pre-scaling to 12 replicas

Result: LLM service ready before traffic spike hits
```

**Example Scenario - Unexpected Load:**
```
Time: 14:30
• current_replicas: 8 (from earlier prediction)
• current_kv_cache_utilization: 95% (viral content causes spike)
• predicted_replicas: 6 (normal afternoon pattern)
• reactive_replicas: 8 * 95% / 70% = 11 (current overload)

Netflix Decision:
• Prediction suggests: 6 replicas
• Current load needs: 11 replicas
• max(6, 11) = 11 replicas
• Action: Reactive scaling supplements prediction

Result: System handles unexpected load gracefully
```

## Benefits of This Netflix-Style Approach

1. **Simple & Effective**: No complex confidence thresholds - trust the prediction
2. **Over-provision Philosophy**: Better to waste some resources than lose service quality
3. **Predictive-Led**: Proactive scaling prevents performance degradation
4. **Reactive Safety Net**: Handles scenarios the prediction didn't anticipate
5. **Production Proven**: Based on Netflix's battle-tested approach at scale
6. **LLM-Optimized**: Accounts for long cold start times and capacity planning needs

## Discussion Points
1. **Contribution Strategy**: Does contributing predictive capabilities to katalyst iHPA align with the project's roadmap?
2. **Implementation Timeline**: Should me prioritize the katalyst enhancement first?
3. **Algorithm Choice**: For LLM workloads, should the predictive algorithm consider GPU utilization, model loading patterns, and request queuing in addition to basic metrics?

I believe this collaborative approach following Netflix's proven methodology could create significant value for both projects and the broader community. Looking forward to your thoughts!

Thanks!

### igor-susic1 · 2025-09-09

What is the update on this issue, is it still expected to stay a priority?

### Jeffwan · 2025-10-13

@igor-susic1 yes. @Belyenochi get some errands recently, we'd like to ship this feature as fast as we can

### igor-susic1 · 2025-10-13

@Jeffwan thanks for the reply. If there is any help needed I would love to contribute I myself would love to get hands on the feature as soon as possible. 

### bolubo · 2026-09-24

I would like to pick this one up.

@Belyenochi the katalyst review you posted earlier is a useful starting point, and I would rather build on the analysis in this thread than start over. If you are still on it, I am glad to coordinate or to take a smaller slice instead. If I do not hear otherwise I will begin with the first piece below, so please do say if you would rather keep it.

Plan, so that predictive and reactive stay inside the same API instead of becoming a new CRD:

1. **API + preview.** Add a `predictive` block to the spec in `api/autoscaling/v1alpha1/podautoscaler_types.go`, with a `mode: Preview | Auto`, borrowing the Preview/Auto idea from katalyst iHPA. In Preview the controller only records the prediction and the replica count it would have chosen into status; it does not touch the workload. This is the same observe-before-act shape that was suggested for #2288. Types, validation, generated artifacts, unit tests.
2. **Predictor.** A predictor interface plus one baseline implementation behind the Preview path, unit tested with fixed inputs.
3. **Auto.** Compose the predictive and reactive recommendations in the existing decision pipeline, defaulting to Preview so nothing changes unless it is opted into.

Two things where your input would help, though I am also happy to pick a direction and adjust later:

- Is a `predictive` sub-block the right shape, or should it be another entry under `metricsSources`? I read "sources within the same API" as the former, but I may have it wrong.
- Settle the up/down philosophy now (a safety floor versus confidence blending), or keep it configurable and decide when we wire the two together?

I will send each piece as its own PR so it stays easy to review.


### bolubo · 2026-09-24

@googs1025 following up on #2804, where you asked to reach a consensus on the API first. Here is the concrete proposal, so we have something specific to agree on before I put more work into the implementation.

Short version: one optional `spec.predictive` block, `Preview` by default, and a `status.predictive` that reports what the projection sees. The constraints from earlier in this thread hold: predictive and reactive stay in the same API, no new CRD, no new controller, and the Preview and Auto modes come from katalyst iHPA.

**Proposed shape**

```yaml
spec:
  predictive:
    mode: Preview        # Preview | Auto, defaults to Preview
    horizonSeconds: 120  # optional, how far ahead the trend is projected; 1 to 3600, defaults to 120
```

**Status**

```yaml
status:
  predictive:
    mode: Preview
    observedValue: "0.62"
    predictedValue: "0.75"
    predictedReplicas: 2
    lastUpdated: ...
```

The numeric values are fixed-precision decimal strings, so a steady series produces an identical status instead of rewriting it on every evaluation.

**What the two modes do**

- Omitted: predictive is off, and existing PodAutoscalers behave exactly as they do today.
- `Preview`, the default: every evaluation computes the projection and writes it to `status.predictive`, meaning the observed value, the projected value, and the replica count the projection alone would ask for. The actual decision is untouched. This is the observe-before-act shape from earlier in this thread.
- `Auto`: the projection joins the decision as a floor on the reactive target. It can only raise the target, never lower it, so it can pull a scale-out forward and keep a scale-in from going too far, but it never scales a workload down on its own. The floor is still bounded by the configured scale-up rate, and the usual replica bounds, schedules and cooldowns apply.
- Turning a projected value into replicas uses the same formula as the reactive path of that strategy, so KPA and APA keep their own semantics.

**Defaults, validation, scope**

- `mode` is `Preview` or `Auto`, and it defaults to `Preview`.
- `horizonSeconds` is optional, from 1 to 3600, and defaults to 120.
- `predictive` together with `scalingStrategy: HPA` is rejected by the validating webhook for now. HPA delegates its decision to the native HorizontalPodAutoscaler resource, which has no channel to receive the projection. KPA and APA are supported.
- The projection comes from the metric history the controller already keeps, limited to the `observeWindowSeconds` window, so there is nothing new to fetch and no need for days of history. It only shows up once the window holds at least three samples spanning at least half of it, so `status.predictive` is empty right after creation.
- With several metric sources, every source gets projected, and the evaluation that asks for the most replicas is the one reported, and the one Auto uses as its floor.
- Removing `spec.predictive` clears `status.predictive`.
- Two things I'd leave out of the first version: prediction-driven scale-down and pluggable predictor algorithms. Both can be added later without changing this shape.

**The two open questions, and where I landed**

1. Should this be a `predictive` sub-block, or another entry under `metricsSources`? I'd go with the sub-block. A metrics source describes a present measurement plus a target value, and every existing consumer folds it into that same calculation. A projection is a forward-looking recommendation, not a present measurement, so mapping it into `metricsSources` would force a special case into every consumer. The earlier guidance was to expose predictive and reactive "as sources within the same API". I read that as two signals feeding the same controller, and the sub-block gives us exactly that without touching the reactive path.
2. Should we settle the up and down philosophy now, or keep it configurable? I'd settle it now, conservatively: the prediction only raises. For LLM serving the costly failure is a late scale-out, since a model load takes minutes, while an over-eager scale-in is the one that hurts. A floor that only raises is one-directional and easy to reason about, and it already covers the safety-floor idea from earlier in this thread. If we later want predictions to take part in scale-down as well, that can be an opt-in field, with no change to this shape. Making it configurable now would mean reviewing two semantics before we have any Preview data.

**Delivery plan**

Once the shape is agreed, I'd do this in two steps. First an API PR with the types, validation, generated artifacts and validation tests. Then a behavior PR with the predictor, the Preview status, the Auto floor, plus the integration and E2E tests you mentioned. #2804 stays in draft and gets reshaped to follow whatever we agree on here.

If this looks right, I'll start on the API PR. Field names and defaults are cheapest to change now. If you'd rather go another way on either question, say so and I'll adjust before opening anything.


### googs1025 · 2026-09-24

> I would like to pick this one up.
> 
> [@Belyenochi](https://github.com/Belyenochi) the katalyst review you posted earlier is a useful starting point, and I would rather build on the analysis in this thread than start over. If you are still on it, I am glad to coordinate or to take a smaller slice instead. If I do not hear otherwise I will begin with the first piece below, so please do say if you would rather keep it.
> 
> Plan, so that predictive and reactive stay inside the same API instead of becoming a new CRD:
> 
> 1. **API + preview.** Add a `predictive` block to the spec in `api/autoscaling/v1alpha1/podautoscaler_types.go`, with a `mode: Preview | Auto`, borrowing the Preview/Auto idea from katalyst iHPA. In Preview the controller only records the prediction and the replica count it would have chosen into status; it does not touch the workload. This is the same observe-before-act shape that was suggested for [Autoscaler-driven elastic expert/data parallelism for MoE #2288](https://github.com/vllm-project/aibrix/issues/2288). Types, validation, generated artifacts, unit tests.
> 2. **Predictor.** A predictor interface plus one baseline implementation behind the Preview path, unit tested with fixed inputs.
> 3. **Auto.** Compose the predictive and reactive recommendations in the existing decision pipeline, defaulting to Preview so nothing changes unless it is opted into.
> 
> Two things where your input would help, though I am also happy to pick a direction and adjust later:
> 
> * Is a `predictive` sub-block the right shape, or should it be another entry under `metricsSources`? I read "sources within the same API" as the former, but I may have it wrong.
> * Settle the up/down philosophy now (a safety floor versus confidence blending), or keep it configurable and decide when we wire the two together?
> 
> I will send each piece as its own PR so it stays easy to review.

  Thanks for driving this. The overall direction makes sense, especially keeping predictive and reactive scaling in the same PodAutoscaler API.

  Before implementation, I would like to clarify a few design points:

  1. What is the concrete purpose of `Preview` mode?

  With no `spec.predictive` block, the existing behavior remains unchanged. With `mode: Preview`, the replica decision also remains unchanged, while the controller only records the prediction.

  Is Preview intended to be a dry-run/observation mode? If so, could the status expose more information, such as:

  - the reactive recommendation;
  - the predicted recommendation;
  - the hypothetical final recommendation in `Auto` mode;
  - whether the prediction would actually change the decision.

  Otherwise, users can see a predicted replica count but cannot tell whether enabling `Auto` would have any practical effect. It may also be worth discussing whether Preview is necessary in the initial API, or whether it should be introduced only after the predictive behavior is more mature.

  2. Can the predictor remain a first-class extension point?

  A linear predictor is a reasonable baseline, but we may eventually need moving average, exponential smoothing, seasonal forecasting, Prophet/LSTM, or an external prediction service.

  I suggest keeping the predictor interface independent from the KPA/APA decision logic:

  ```text
  metric history
      -> predictor
      -> predicted metric value
      -> existing replica calculation
      -> reactive + predictive decision
```

  This would allow new prediction algorithms to be added without changing the autoscaling pipeline or the status contract. The initial version does not necessarily need to expose predictor selection in the public API, but the internal abstraction and status semantics should remain extensible.

  3. How should extreme values and zero values be handled?

  It would be useful to define the behavior for:

  - isolated metric spikes;
  - missing samples;
  - zero-valued history;
  - currentReplicas == 0;
  - zero or invalid target values;
  - negative values;
  - NaN/Inf values;
  - insufficient history;
  - very large fitted slopes.

  For example, is a universal cap such as 4x observed mean appropriate for all metric types? Should Auto require stronger evidence than Preview before applying a prediction?

  4. How is historical data stored and related to the existing autoscaler history?

  As I understand it, the current autoscaler already maintains stable/panic windows and aggregates historical metric samples, including mean values. Should predictive scaling reuse this existing sliding history, or maintain a separate buffer?

  In particular, we should clarify:

  - whether observeWindowSeconds is also the predictive window;
  - how long samples are retained compared with the prediction window;
  - whether prediction uses per-Pod samples or the already aggregated values;
  - how irregular reconcile intervals affect the fit;
  - what happens after controller restart or leader election;
  - whether the history is in-memory only or should eventually come from a persistent source such as Prometheus.

  The distinction between the existing reactive calculation and the predictive calculation should also be explicit:

  reactive:  windowed history -> current aggregate -> current replicas
  predictive: windowed history -> future metric value -> future replicas

  These points seem important to settle before choosing the final API shape, especially because the predictor and history model will determine how extensible the feature is later.


### bolubo · 2026-09-24

Thanks for the detailed review. The direction works for me. Taking the four points in order, here's what the code does today, what I'd change and what I'd keep.

**1. Preview**

Today `Preview` runs the same projection the `Auto` path runs, writes it to `status.predictive`, and leaves the replica decision with the reactive path. The status carries `mode`, `observedValue`, `predictedValue`, `predictedReplicas` and `lastUpdated`, and you're right that it doesn't answer the question a user actually has: would turning on `Auto` change anything for this workload.

I'd add two fields to `status.predictive`:

- `reactiveReplicas`: the replica count the reactive path asked for in this round.
- `wouldBeReplicas`: the count the same round would produce in `Auto`, after the scale-up rate cap, the replica bounds and the cooldown window. In `Auto` it's the applied value, in `Preview` it's what the mode would have done.

`wouldBeReplicas` above `reactiveReplicas` is the answer to whether the prediction changes the decision. If you'd rather read that as a field, I'll add it as one, and the two names are still open.

On dropping `Preview` from the initial API: I'd keep it, and keep it as the default. Without it there's no mode that leaves the workload alone, so the first user of the block is already acting on predictions, and there's no way to see whether the predictor is useful for a given workload before opting in. With the two fields above, `Preview` becomes a faithful dry run of `Auto` rather than an extra mode to maintain, since both go through the same code path.

**2. Predictor as an extension point**

That's already the shape. `pkg/controller/podautoscaler/prediction` defines a `Predictor` interface with a single method that takes the samples, the observation window and the horizon, and returns the projected metric value plus the fit statistics. `Linear` is one implementation. Replica conversion stays in the pipeline, so a predictor can't change how a value becomes replicas or how the status reads. Your sketch is the code, with one step in front:

```
windowed history -> predictor -> predicted metric value -> existing replica calculation -> reactive + predictive decision
```

Adding moving average, exponential smoothing or a seasonal model is a new implementation and a constructor call, with no change to the API or the status contract. I agree about not exposing a predictor selector in v1. One note for an external prediction service: `Predict` is synchronous, so a remote source would need a last known value cache rather than an inline call.

**3. Extreme and zero values**

Most cases are defined, two are not, and I checked the two by running them.

Defined today: a non positive `targetValue` skips the source before any division; fewer than three samples, or samples that don't span half of the window, produce no projection; the projection is clamped at zero and at four times the observed mean; a window of zeros projects to zero, which the pipeline treats as no projection at all; the floor can only raise a decision and is capped by the scale-up rate; at zero replicas the cap keeps a minimum of one, which is the fix from the bot review earlier today.

Not defined, now verified in a scratch run: a `NaN` in the window produces a NaN projection, and it's dropped only because a downstream guard happens to skip a negative replica count rather than by design. A series with negative samples and a mean of zero also slips past the four times cap, because the cap only applies when the observed mean is positive. I used a nine sample window for both.

What I'd change: filter non finite and negative samples before the fit, the way a missing sample is skipped, and cover every case above in the predictor tests. The same window feeds the reactive algorithms, and a `NaN` there turns the window mean into NaN, so I'd also drop non finite values where the samples are recorded. Say the word if you'd rather keep that second part in a separate change.

Two of your questions need a design answer rather than a code answer. The four times cap is a guard against one noisy round, not a target: it bounds how far a single evaluation may raise, and the scale-up rate and `maxReplicas` bound the result after it. It can become per source configuration later if a metric needs it. On `Auto` requiring stronger evidence than `Preview`: I wouldn't separate them in v1. `Auto` can only raise and never lower, and the rate, the bounds and the cooldown all still apply, so the cost of a wrong prediction is a slower scale-in. Keeping the predicate identical is also what makes `Preview` a dry run of `Auto`.

**4. History**

The projection reuses the recorded history instead of adding a buffer. Every reconcile records the mean of the pod metric values into the same stable window the reactive path reads, and the fit reads that series limited to `observeWindowSeconds`, so both calculations see the same samples. Retention is ten times the stable window, which for the default 180 seconds is thirty minutes. The samples are aggregated values, not per pod samples. The fit works from sample timestamps, so irregular reconcile intervals are fine. After a controller restart or a leader election the history is empty because it's in memory, and the projection stays absent until three samples spanning half of the window are recorded again, the same way the reactive windows start empty. A Prometheus backed source is possible behind the predictor interface, not through the API. The two calculations differ only in the middle step:

```
reactive:   windowed history -> current aggregate -> current replicas
predictive: windowed history -> projected aggregate -> future replicas
```

The replica formula is shared, so the two values `Auto` compares are the same kind of number.

I'd fold the status fields and the sample filtering into the API and predictor commits of #2804, with tests, and keep the rest as proposed.

