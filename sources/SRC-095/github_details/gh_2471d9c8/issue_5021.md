# [Issue #5021] [Feature] Native support for injecting Secrets via Helm chart values

source: https://github.com/ray-project/kuberay/issues/5021
state: closed | updated: 2026-09-22T21:58:23Z
labels: enhancement

## 正文

### Search before asking

- [x] I had searched in the [issues](https://github.com/ray-project/kuberay/issues) and found no similar feature requirement.


### KubeRay Component

ray-operator

### Description

Today, there's no built-in way to inject sensitive values (private PyPI/pip index credentials, API tokens, cloud credentials, etc.) into Ray head or worker pods through the chart's `values.yaml`.

Because `headGroupSpec` and `workerGroupSpecs` don't expose a way to reference Kubernetes Secrets, the only option today is to patch the rendered manifests with Kustomize to add `env`, `secretKeyRef`, or Secret-backed volumes.

While this works, it adds unnecessary complexity for what feels like a common deployment requirement. It also has a few drawbacks:

- Requires an additional Kustomize layer on top of Helm for a basic configuration need.
- Isn't very discoverable—neither `values.yaml` nor the documentation points users toward this workflow.
- The same patch has to be applied to `headGroupSpec` and every `workerGroupSpec`, which becomes repetitive as deployments grow.
- There's no single place in `values.yaml` to reference Secrets (including those managed by External Secrets Operator) and have them applied consistently across all Ray pods.


### Use case

Many teams need to provide sensitive configuration such as private PyPI/pip index credentials, application API tokens, cloud credentials, or object storage credentials without baking them into container images or committing them as plaintext.

It would be helpful if the chart provided a first-class way to declare Secret-backed environment variables and/or volume mounts once in `values.yaml`, with those settings automatically applied to both head and worker pod templates.

This would:

- Remove the need for Kustomize overlays for a common day-one deployment requirement.
- Make secret configuration easier to discover and maintain.
- Provide a single, consistent place to configure Secrets for all Ray pods.
- Better support common Kubernetes workflows, including Secrets managed by External Secrets Operator.




### Related issues

didnt find any related to it. 

### Are you willing to submit a PR?

- [ ] Yes I am willing to submit a PR!

## 评论 (12)

### akhtarCareem · 2026-07-23

@machichima @win5923 @rueian would love to hear your thoughts. Thanks 🙌 

### Smallfu666 · 2026-07-24

Part of this is actually supported by the `ray-cluster` chart today, though it's easy to miss — `head`, `worker`, and each entry in `additionalWorkerGroups` all expose `envFrom` ([values.yaml L110/L232/L343](https://github.com/ray-project/kuberay/blob/148f70e/helm-chart/ray-cluster/values.yaml)) plus `volumes`/`volumeMounts`, and the templates render them ([raycluster-cluster.yaml L94/L227/L361](https://github.com/ray-project/kuberay/blob/148f70e/helm-chart/ray-cluster/templates/raycluster-cluster.yaml)). So Secret-backed env (including ESO-managed Secrets) works without a Kustomize layer:

```yaml
head:
  envFrom:
    - secretRef:
        name: my-pip-credentials
worker:
  envFrom:
    - secretRef:
        name: my-pip-credentials
```

What the chart genuinely doesn't have is what your last two bullets describe:

1. **A single place applied to all Ray pods** — today the same block must be repeated on `head`, `worker`, and every additional worker group.
2. **Discoverability** — `values.yaml` doesn't hint at this pattern anywhere, so people reach for Kustomize.

Would the maintainers be open to either/both of:

- extending the existing `common.containerEnv` pattern ([values.yaml L54](https://github.com/ray-project/kuberay/blob/148f70e/helm-chart/ray-cluster/values.yaml)) with `common.envFrom` (and possibly `common.volumes`/`common.volumeMounts`) merged into the head and all worker group templates, or
- if adding chart surface isn't desirable, a documented example in `values.yaml` comments covering the Secret/ESO case?

Happy to submit a PR for whichever direction you prefer.


### akhtarCareem · 2026-07-24

@Smallfu666 Thanks for the insights! My main challenge is reading secrets from cloud providers (AWS, Google Cloud, etc.), then creating and populating Kubernetes Secrets. This seems to be a common pattern in production environments, since most teams store their secrets in their cloud provider's secret management service.




### machichima · 2026-07-24

Thank you for opening the issue!

> My main challenge is reading secrets from cloud providers (AWS, Google Cloud, etc.), then creating and populating Kubernetes Secrets

I think in this case `envFrom` is enough? Probably we should add this into document to make it obvious to users.

### akhtarCareem · 2026-07-24

@machichima do we support reading secrets from ESO in charts? right i am using kustomize and secretstore.yaml + externalsecret.yaml to populate k8s secret. 

### machichima · 2026-07-24

> [@machichima](https://github.com/machichima) do we support reading secrets from ESO in charts? right i am using kustomize and secretstore.yaml + externalsecret.yaml to populate k8s secret.

KubeRay charts don't integrate with ESO directly, ESO will produce a native Kubernetes Secret, and anything in the cluster can consume it as-is.

Since you already populate a K8s Secret, you can consume it with the chart's existing `envFrom`. Like mentioned in https://github.com/ray-project/kuberay/issues/5021#issuecomment-5065351067. The only thing that's missing is `common.envFrom` that can apply to all pods within the raycluster, right?

### akhtarCareem · 2026-07-24

@machichima Thanks for the clarification. It would've been great if it could just install the Helm chart and be done. Right now, I still need to maintain a separate Kustomize app just to populate Kubernetes Secrets via ESO. it would've been just 1 ExternalSecret and 1 SecretStore object. 

That said, `common.envFrom` should be sufficient for now. Thanks!


### machichima · 2026-07-25

@akhtarCareem I don't think it's common for operator to embed ESO config into helm, therefore I think your current usage is the correct way.

### machichima · 2026-07-25

@Smallfu666 Are you still interested in helping on adding `common.envFrom`? If so, I will assign this issue to you

### Smallfu666 · 2026-07-25

@machichima  take thanks for confirming the scope.

### akhtarCareem · 2026-07-25

@machichima totally unrelated question: is there a schedule when I can expect the next minor release?

### machichima · 2026-07-26

> [@machichima](https://github.com/machichima) totally unrelated question: is there a schedule when I can expect the next minor release?

The next release (v1.7) will be at around the end of July. This is a smaller change and I think we may be able to merge it before release.
