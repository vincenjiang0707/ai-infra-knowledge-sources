# [Issue #2430] [Bug] Kuberay can not start when enableBatchScheduler=true

source: https://github.com/ray-project/kuberay/issues/2430
state: closed | updated: 2026-09-23T07:00:32Z
labels: bug, stale

## 正文

### Search before asking

- [X] I searched the [issues](https://github.com/ray-project/kuberay/issues) and found no similar issues.


### KubeRay Component

ray-operator

### What happened + What you expected to happen

When i start the controller with 
```
            "args": [
                "--kubeconfig=/Users/yueming/.kube/config", 
                "--enable-leader-election=false",
                "--leader-election-namespace=default",
                "--enable-batch-scheduler=true",
            ]
```
in vscode. The controller is blocked by cache syncing:

```
{"level":"error","ts":"2024-10-09T19:35:37.389+0800","logger":"controller-runtime.source.EventHandler","msg":"if kind is a CRD, it should be installed before calling Start","kind":"PodGroup.scheduling.volcano.sh","error":"no matches for kind \"PodGroup\" in version \"scheduling.volcano.sh/v1beta1\"","stacktrace":"sigs.k8s.io/controller-runtime/pkg/internal/source.(*Kind).Start.func1.1\n\t/Users/yueming/go/src/gitlab.alibaba-inc.com/eml/kuberay/ray-operator/vendor/sigs.k8s.io/controller-runtime/pkg/internal/source/kind.go:63\nk8s.io/apimachinery/pkg/util/wait.loopConditionUntilContext.func2\n\t/Users/yueming/go/src/gitlab.alibaba-inc.com/eml/kuberay/ray-operator/vendor/k8s.io/apimachinery/pkg/util/wait/loop.go:87\nk8s.io/apimachinery/pkg/util/wait.loopConditionUntilContext\n\t/Users/yueming/go/src/gitlab.alibaba-inc.com/eml/kuberay/ray-operator/vendor/k8s.io/apimachinery/pkg/util/wait/loop.go:88\nk8s.io/apimachinery/pkg/util/wait.PollUntilContextCancel\n\t/Users/yueming/go/src/gitlab.alibaba-inc.com/eml/kuberay/ray-operator/vendor/k8s.io/apimachinery/pkg/util/wait/poll.go:33\nsigs.k8s.io/controller-runtime/pkg/internal/source.(*Kind).Start.func1\n\t/Users/yueming/go/src/gitlab.alibaba-inc.com/eml/kuberay/ray-operator/vendor/sigs.k8s.io/controller-runtime/pkg/internal/source/kind.go:56"}
```

Finally, the controller failed：
```
{"level":"error","ts":"2024-10-09T19:35:57.493+0800","logger":"setup","msg":"problem running manager","error":"failed to wait for raycluster caches to sync: timed out waiting for cache to be synced for Kind *v1beta1.PodGroup","stacktrace":"main.exitOnError\n\t/Users/yueming/go/src/gitlab.alibaba-inc.com/eml/kuberay/ray-operator/main.go:270\nmain.main\n\t/Users/yueming/go/src/gitlab.alibaba-inc.com/eml/kuberay/ray-operator/main.go:247\nruntime.main\n\t/opt/homebrew/Cellar/go/1.22.5/libexec/src/runtime/proc.go:271"}
```

*There is no PodGroup CRD in my cluster.*

After I remove the code https://github.com/ray-project/kuberay/blob/bf21d2d01cf1c931136d869d2c8168aed07bc68c/ray-operator/controllers/ray/batchscheduler/volcano/volcano_scheduler.go#L184-L186, the controller can be started.

### Reproduction script

```
{
    // 使用 IntelliSense 了解相关属性。 
    // 悬停以查看现有属性的描述。
    // 欲了解更多信息，请访问: https://go.microsoft.com/fwlink/?linkid=830387
    "version": "0.2.0",
    "configurations": [
        {
            "name": "Launch Package",
            "type": "go",
            "request": "launch",
            "mode": "auto",
            "program": "ray-operator/main.go",
            "cwd": "${workspaceFolder}",
            "args": [
                "--kubeconfig=xxx", 
                "--enable-leader-election=false",
                "--leader-election-namespace=default",
                "--enable-batch-scheduler=true",
            ]
        }
    ]
}
```


### Anything else

_No response_

### Are you willing to submit a PR?

- [ ] Yes I am willing to submit a PR!

## 评论 (14)

### kevin85421 · 2024-10-09

You should install the Volcano scheduler.

### KunWuLuan · 2024-10-11

I just want to enable the batch scheduler. And I have not submit any job using volcano scheduler. I still need to install volcano  even if I just want to use yunikorn?

### andrewsykim · 2024-10-11

If you want to use Yunikorn, you should use `--batch-scheduler=yunikorn` and not `--enable-batch-scheduler`. We deprecated `--enable-batch-scheduler=true` in favor of `--batch-scheduler=yunikorn|volcano` when we added yunikorn support: https://github.com/ray-project/kuberay/pull/2300

### KunWuLuan · 2024-10-11

Thanks for reply @andrewsykim . If I enable `--batch-scheduler=yunikorn` when using ray-operator, I can still set `ray.io/scheduler-name=volcano` on RayJob, right? What will happen in this scenario?

### andrewsykim · 2024-10-11

> If I enable --batch-scheduler=yunikorn when using ray-operator, I can still set ray.io/scheduler-name=volcano on RayJob, right?

No I don't think so, KubeRay only supports one batch scheduler at a time. What is your use-case? Are you trying to use both Yunikorn and Volcano?

### kadisi · 2024-10-11

> > If I enable --batch-scheduler=yunikorn when using ray-operator, I can still set ray.io/scheduler-name=volcano on RayJob, right?
> 
> No I don't think so, KubeRay only supports one batch scheduler at a time. What is your use-case? Are you trying to use both Yunikorn and Volcano?

@andrewsykim If we set kuberay to the `--batch-scheduler` parameter, there is no need for the user to set the raycluster label `ray.io/scheduler-name=***`.  Judging from the latest code, it's still the old logic。  If we enable --batch-scheduler=yunikorn when can still using ray-operator, I can still set `ray.io/scheduler-name=volcano`

### KunWuLuan · 2024-10-11

We provide managed ray-operator for our users. Submitting RayJob is the job of our users, they may make mistakes, and no event is sent when the wrong schedulerName is set on the RayJobs. Once we only support one batch scheduler, why we let user choose scheduler on RayJob by  `ray.io/scheduler-name`? Maybe they just need to use label like `ray.io/enable-batch-scheduler` on RayJob. 
How do you think?

### kevin85421 · 2024-10-19

cc @MortalHappiness can you take a look?

### MortalHappiness · 2024-10-19

@kevin85421 I was wondering if we should take this opportunity to go ahead and remove this deprecated `--enable-batch-scheduler=true` flag?


### MortalHappiness · 2024-10-19

If we don't remove it, we'll need to define the exact behavior required here. What if `--enable-batch-scheduler=true` was set and `volcano` was initially not installed but installed later?

### kevin85421 · 2024-10-24

By the way, RayJob currently doesn't support Volcano and YuniKorn. At the moment, Volcano and YuniKorn are only supported in RayCluster. If you want to use advanced scheduling for RayJob / RayCluster, you should use Kueue for now. cc @KunWuLuan @kadisi 

> We provide managed ray-operator for our users. Submitting RayJob is the job of our users, they may make mistakes, and no event is sent when the wrong schedulerName is set on the RayJobs. Once we only support one batch scheduler, why we let user choose scheduler on RayJob by ray.io/scheduler-name? Maybe they just need to use label like ray.io/enable-batch-scheduler on RayJob.

`enable-batch-scheduler` was deprecated in KubeRay v1.2. If it is specified, Volcano will always be used, regardless of the value of `ray.io/scheduler-name` or whether `ray.io/scheduler-name` is specified based on: https://github.com/ray-project/kuberay/blob/8b61b73bc57d7776ccac8b88b215df22aefaabbd/ray-operator/controllers/ray/batchscheduler/schedulermanager.go#L73

The issue is that the RBAC in the KubeRay v1.2.2 Helm chart doesn't update correctly. As a result, if `enable-batch-scheduler` is not set, the RBAC for PodGroup will not be installed.

### kevin85421 · 2024-10-24

* Install KubeRay operator
  ```sh
  helm install kuberay-operator kuberay/kuberay-operator --version 1.2.2 --set batchScheduler.enabled=true
  ```

* Install RayCluster with `ray.io/scheduler-name: abc`
  ```yaml
  apiVersion: ray.io/v1
  kind: RayCluster
  metadata:
   name: test-cluster-0
   labels:
     ray.io/scheduler-name: abc
  spec:
   rayVersion: '2.9.0'
   headGroupSpec:
     rayStartParams: {}
     template:
       spec:
         containers:
         - name: ray-head
           image: rayproject/ray:2.9.0
           resources:
             limits:
               cpu: "1"
               memory: "2Gi"
             requests:
               cpu: "1"
               memory: "2Gi"
   workerGroupSpecs: []
  ```

* Check whether PodGroup is created correctly or not.

### github-actions[bot] · 2026-09-22

This issue has been automatically marked as stale because it has not had
any activity for 120 days. It will be closed in 14 days if no further activity occurs.

If you'd like to keep this issue open, just leave any comment, and the stale label will be removed.
If you'd like to get more attention on this issue, please tag one of the KubeRay maintainers.

You can always ask for help on [Ray's public Slack channel](https://github.com/ray-project/kuberay#getting-involved).

### KunWuLuan · 2026-09-23

Closing this issue. The reported behavior is expected: `--enable-batch-scheduler=true` implies Volcano, so the operator blocks on the Volcano `PodGroup` CRD until Volcano is installed. This flag is deprecated — use `--batch-scheduler=volcano|yunikorn` and install the matching scheduler instead (see #2300). For advanced scheduling of RayJob/RayCluster, Kueue is the recommended path (tracked in #4344).
