# [Issue #3984] [Bug]  rayCluster cannot submit a job

source: https://github.com/ray-project/kuberay/issues/3984
state: open | updated: 2026-09-22T16:56:35Z
labels: bug, stale

## 正文

### Search before asking

- [x] I searched the [issues](https://github.com/ray-project/kuberay/issues) and found no similar issues.


### KubeRay Component

Others

### What happened + What you expected to happen

https://www.aidoczh.com/ray/cluster/kubernetes/getting-started/raycluster-quick-start.html

```
kuberay-operator-5699d89f6c-s42kc             1/1     Running   2 (34m ago)   155m
raycluster-kuberay-head-fxpw9                 1/1     Running   1 (34m ago)   104m
raycluster-kuberay-worker-workergroup-8vll6   1/1     Running   0             28m
```

ray job submit --address http://localhost:8265 --working-dir="." --runtime-env-json='{"pip": ["xgboost==2.0.3","xgboost_ray"]}' -- python ray1.py

```
Job submission server address: http://localhost:8265
2025-08-25 14:35:16,455 INFO dashboard_sdk.py:385 -- Package gcs://_ray_pkg_6784fe728284131e.zip already exists, skipping upload.

-------------------------------------------------------
Job 'raysubmit_C2ZjHAVQjU91d3S2' submitted successfully
-------------------------------------------------------

Next steps
  Query the logs of the job:
    ray job logs raysubmit_C2ZjHAVQjU91d3S2
  Query the status of the job:
    ray job status raysubmit_C2ZjHAVQjU91d3S2
  Request the job to be stopped:
    ray job stop raysubmit_C2ZjHAVQjU91d3S2

Tailing logs until the job exits (disable with --no-wait):
```

Always block

log in to raycluster-kuberay-head-fxpw9

pip install xgboost==2.0.3

```
WARNING: Retrying (Retry(total=4, connect=None, read=None, redirect=None, status=None)) after connection broken by 'ConnectTimeoutError(<pip._vendor.urllib3.connection.HTTPSConnection object at 0xffffb1ef69a0>, 'Connection to pypi.org timed out. (connect timeout=15)')': /simple/xgboost/
```


### Reproduction script
```
from collections import Counter
import socket
import time

import ray

# 主要理解分布式异步执行
# ray.init(address='172.17.0.2:6379', _redis_password='5241590000000000')
ray.init()

print('''This cluster consists o    f
    {} nodes in total
    {} CPU resources in total
'''.format(len(ray.nodes()), ray.cluster_resources()['CPU']))


@ray.remote
def f():
    time.sleep(0.001)
    # Return IP address.
    return socket.gethostbyname(socket.gethostname())


object_ids = [f.remote() for _ in range(10000)]
ip_addresses = ray.get(object_ids)

print('Tasks executed')
for ip_address, num_tasks in Counter(ip_addresses).items():
    print('    {} tasks on {}'.format(num_tasks, ip_address))

# 关闭 Ray
ray.shutdown()
```
### Anything else

helm install kuberay-operator kuberay/kuberay-operator --version 1.1.1
helm install raycluster kuberay/ray-cluster --version 1.1.1 --set 'image.tag=2.9.0-aarch64'

### Are you willing to submit a PR?

- [x] Yes I am willing to submit a PR!

## 评论 (4)

### LY-today · 2025-08-25

@epall @ericl @jianyuan please check

### Future-Outlier · 2025-10-11

Hi, @LY-today can you explain more on this issue?
give us a step by step repro guide, thank you!

### alimaazamat · 2026-02-11

@LY-today If you are still running into this issue, based on the logs it seems to be a networking issue trying to download xgboost from pipy.org. It isn't good practice to do runtime pip installs because they are slow and blocking. But regardless your K8s cluster probably doesn't have access to the internet to download the package. Is your cluster private?

### github-actions[bot] · 2026-09-22

This issue has been automatically marked as stale because it has not had
any activity for 120 days. It will be closed in 14 days if no further activity occurs.

If you'd like to keep this issue open, just leave any comment, and the stale label will be removed.
If you'd like to get more attention on this issue, please tag one of the KubeRay maintainers.

You can always ask for help on [Ray's public Slack channel](https://github.com/ray-project/kuberay#getting-involved).
