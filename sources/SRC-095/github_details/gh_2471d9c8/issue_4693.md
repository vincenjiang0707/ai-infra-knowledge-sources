# [Issue #4693] Remove OpenShift-specific code once Gateway API is the default

source: https://github.com/ray-project/kuberay/issues/4693
state: open | updated: 2026-09-23T04:42:26Z
labels: stale

## 正文

### Summary
KubeRay's \`RayCluster\` reconciler contains OpenShift-specific logic to create a \`Route\` object for dashboard access, since OpenShift historically didn't support Ingress natively. Now that Gateway API support is maturing, this code path should be removed once it's no longer needed for backward compatibility.
### What to remove
- \`ray-operator/controllers/ray/utils/openshift.go\` — \`IsOpenShiftCluster()\`, \`ShouldUseIngressOnOpenShift()\`, and the \`openShiftAPIGroups\` detection list
- \`ray-operator/controllers/ray/common/openshift.go\` — \`BuildRouteForHeadService()\` and its test file
- \`shouldCreateOpenShiftRoute()\` in \`raycluster_controller.go\` and all related Route reconciliation logic
- \`IsOpenShift\` and \`UseIngressOnOpenShift\` fields from \`RayClusterReconcilerOptions\`
- The \`isOpenShift\` detection call in \`main.go\`
### Pquisites before removing
- [ ] Gateway API support in KubeRay is stable and recommended for production use
- [ ] A reasonable backward compatibility window has passed for OpenShift users still relying on Route creation
- [ ] Any remaining platform-specific behaviour is handled via webhooks, per the [controlled network environment proposal](https://github.com/ray-project/enhancements/pull/63)
### Background
Context was discussed in #4365. The short-term goal of that PR was to clean up the detection logic and isolate all OpenShift-specific code into dedicated files (\`utils/openshift.go\`, \`common/openshift.go\`). This issue tracks the eventual full removal.

## 评论 (1)

### github-actions[bot] · 2026-09-23

This issue has been automatically marked as stale because it has not had
any activity for 120 days. It will be closed in 14 days if no further activity occurs.

If you'd like to keep this issue open, just leave any comment, and the stale label will be removed.
If you'd like to get more attention on this issue, please tag one of the KubeRay maintainers.

You can always ask for help on [Ray's public Slack channel](https://github.com/ray-project/kuberay#getting-involved).
