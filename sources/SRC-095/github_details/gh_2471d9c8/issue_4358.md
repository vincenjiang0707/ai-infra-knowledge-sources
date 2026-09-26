# [Issue #4358] [Test] Some test always fail in my environment

source: https://github.com/ray-project/kuberay/issues/4358
state: closed | updated: 2026-09-23T07:02:16Z
labels: enhancement, stale

## 正文

### Search before asking

- [x] I had searched in the [issues](https://github.com/ray-project/kuberay/issues) and found no similar feature requirement.


### Description

TestRayClusterAutoscalerMaxReplicasUpdate/Create_a_RayCluster_with_autoscaling_enabled(Scale_down_maxReplicas_from_2_to_1) 
and 
TestRayClusterAutoscalerMaxReplicasUpdate/Create_a_RayCluster_with_autoscaler_v2_enabled(Scale_down_maxReplicas_from_2_to_1)

always fail in my environment

### Use case

_No response_

### Related issues

```
➜  test git:(aliyun/v1.5.1) ✗ KUBERAY_TEST_ARCH=amd64 go test -v ./e2eautoscaler -run TestRayClusterAutoscalerMaxReplicasUpdate
=== RUN   TestRayClusterAutoscalerMaxReplicasUpdate
=== RUN   TestRayClusterAutoscalerMaxReplicasUpdate/Create_a_RayCluster_with_autoscaling_enabled(Scale_up_maxReplicas_from_2_to_3)
    core.go:87: [2026-01-08T20:17:43+08:00] Executing command: [python /home/ray/test_scripts/create_detached_actor.py actor0]
    core.go:100: [2026-01-08T20:17:44+08:00] Command stdout: 
    core.go:101: [2026-01-08T20:17:44+08:00] Command stderr: 2026-01-08 04:17:43,777    INFO worker.py:1696 -- Using address 127.0.0.1:6379 set in the environment variable RAY_ADDRESS
        2026-01-08 04:17:43,779 INFO worker.py:1837 -- Connecting to existing Ray cluster at address: 10.210.194.221:6379...
        2026-01-08 04:17:43,787 INFO worker.py:2014 -- Connected to Ray cluster. View the dashboard at 10.210.194.221:8265 
        /home/ray/anaconda3/lib/python3.10/site-packages/ray/_private/worker.py:2062: FutureWarning: Tip: In future versions of Ray, Ray will no longer override accelerator visible devices env var if num_gpus=0 or num_gpus=None (default). To enable this behavior and turn off this error message, set RAY_ACCEL_ENV_VAR_OVERRIDE_ON_ZERO=0
          warnings.warn(
    core.go:87: [2026-01-08T20:17:44+08:00] Executing command: [python /home/ray/test_scripts/create_detached_actor.py actor1]
    core.go:100: [2026-01-08T20:17:46+08:00] Command stdout: 
    core.go:101: [2026-01-08T20:17:46+08:00] Command stderr: 2026-01-08 04:17:45,250    INFO worker.py:1696 -- Using address 127.0.0.1:6379 set in the environment variable RAY_ADDRESS
        2026-01-08 04:17:45,251 INFO worker.py:1837 -- Connecting to existing Ray cluster at address: 10.210.194.221:6379...
        2026-01-08 04:17:45,260 INFO worker.py:2014 -- Connected to Ray cluster. View the dashboard at 10.210.194.221:8265 
        /home/ray/anaconda3/lib/python3.10/site-packages/ray/_private/worker.py:2062: FutureWarning: Tip: In future versions of Ray, Ray will no longer override accelerator visible devices env var if num_gpus=0 or num_gpus=None (default). To enable this behavior and turn off this error message, set RAY_ACCEL_ENV_VAR_OVERRIDE_ON_ZERO=0
          warnings.warn(
    core.go:87: [2026-01-08T20:17:46+08:00] Executing command: [python /home/ray/test_scripts/create_detached_actor.py actor2]
    core.go:100: [2026-01-08T20:17:48+08:00] Command stdout: 
    core.go:101: [2026-01-08T20:17:48+08:00] Command stderr: 2026-01-08 04:17:46,933    INFO worker.py:1696 -- Using address 127.0.0.1:6379 set in the environment variable RAY_ADDRESS
        2026-01-08 04:17:46,935 INFO worker.py:1837 -- Connecting to existing Ray cluster at address: 10.210.194.221:6379...
        2026-01-08 04:17:46,951 INFO worker.py:2014 -- Connected to Ray cluster. View the dashboard at 10.210.194.221:8265 
        /home/ray/anaconda3/lib/python3.10/site-packages/ray/_private/worker.py:2062: FutureWarning: Tip: In future versions of Ray, Ray will no longer override accelerator visible devices env var if num_gpus=0 or num_gpus=None (default). To enable this behavior and turn off this error message, set RAY_ACCEL_ENV_VAR_OVERRIDE_ON_ZERO=0
          warnings.warn(
    test.go:114: [2026-01-08T20:17:56+08:00] Retrieving Pod Container test-ns-bjh58/ray-cluster-head-z5d6l/ray-head logs
    test.go:102: [2026-01-08T20:17:56+08:00] Creating ephemeral output directory as KUBERAY_TEST_OUTPUT_DIR env variable is unset
    test.go:105: [2026-01-08T20:17:56+08:00] Output directory has been created at: /var/folders/_4/7rb65yt93ls_mllcrr35544r0000gp/T/TestRayClusterAutoscalerMaxReplicasUpdateCreate_a_RayCluster_wi1839831825/001
    test.go:114: [2026-01-08T20:17:56+08:00] Retrieving Pod Container test-ns-bjh58/ray-cluster-head-z5d6l/autoscaler logs
    test.go:114: [2026-01-08T20:17:56+08:00] Retrieving Pod Container test-ns-bjh58/ray-cluster-test-group-worker-6btvz/ray-worker logs
    test.go:114: [2026-01-08T20:17:56+08:00] Retrieving Pod Container test-ns-bjh58/ray-cluster-test-group-worker-bxt98/ray-worker logs
    test.go:114: [2026-01-08T20:17:56+08:00] Error getting logs from container test-ns-bjh58/ray-cluster-test-group-worker-bxt98/ray-worker
    test.go:114: [2026-01-08T20:17:56+08:00] Retrieving Pod Container test-ns-bjh58/ray-cluster-test-group-worker-zbr4m/ray-worker logs
    test.go:114: [2026-01-08T20:17:56+08:00] Error getting logs from container test-ns-bjh58/ray-cluster-test-group-worker-zbr4m/ray-worker
=== RUN   TestRayClusterAutoscalerMaxReplicasUpdate/Create_a_RayCluster_with_autoscaling_enabled(Scale_down_maxReplicas_from_2_to_1)
    core.go:87: [2026-01-08T20:18:22+08:00] Executing command: [python /home/ray/test_scripts/create_detached_actor.py actor0]
    core.go:100: [2026-01-08T20:18:24+08:00] Command stdout: 
    core.go:101: [2026-01-08T20:18:24+08:00] Command stderr: 2026-01-08 04:18:23,040    INFO worker.py:1696 -- Using address 127.0.0.1:6379 set in the environment variable RAY_ADDRESS
        2026-01-08 04:18:23,041 INFO worker.py:1837 -- Connecting to existing Ray cluster at address: 10.206.28.110:6379...
        2026-01-08 04:18:23,052 INFO worker.py:2014 -- Connected to Ray cluster. View the dashboard at 10.206.28.110:8265 
        /home/ray/anaconda3/lib/python3.10/site-packages/ray/_private/worker.py:2062: FutureWarning: Tip: In future versions of Ray, Ray will no longer override accelerator visible devices env var if num_gpus=0 or num_gpus=None (default). To enable this behavior and turn off this error message, set RAY_ACCEL_ENV_VAR_OVERRIDE_ON_ZERO=0
          warnings.warn(
    core.go:87: [2026-01-08T20:18:24+08:00] Executing command: [python /home/ray/test_scripts/create_detached_actor.py actor1]
    core.go:100: [2026-01-08T20:18:26+08:00] Command stdout: 
    core.go:101: [2026-01-08T20:18:26+08:00] Command stderr: 2026-01-08 04:18:24,717    INFO worker.py:1696 -- Using address 127.0.0.1:6379 set in the environment variable RAY_ADDRESS
        2026-01-08 04:18:24,719 INFO worker.py:1837 -- Connecting to existing Ray cluster at address: 10.206.28.110:6379...
        2026-01-08 04:18:24,729 INFO worker.py:2014 -- Connected to Ray cluster. View the dashboard at 10.206.28.110:8265 
        /home/ray/anaconda3/lib/python3.10/site-packages/ray/_private/worker.py:2062: FutureWarning: Tip: In future versions of Ray, Ray will no longer override accelerator visible devices env var if num_gpus=0 or num_gpus=None (default). To enable this behavior and turn off this error message, set RAY_ACCEL_ENV_VAR_OVERRIDE_ON_ZERO=0
          warnings.warn(
    raycluster_autoscaler_test.go:423: 
        Timed out after 60.001s.
        Expected
            <int32>: 2
        to equal
            <int32>: 1
    test.go:114: [2026-01-08T20:19:27+08:00] Retrieving Pod Container test-ns-x9fh6/ray-cluster-head-vxk5l/ray-head logs
    test.go:102: [2026-01-08T20:19:27+08:00] Creating ephemeral output directory as KUBERAY_TEST_OUTPUT_DIR env variable is unset
    test.go:105: [2026-01-08T20:19:27+08:00] Output directory has been created at: /var/folders/_4/7rb65yt93ls_mllcrr35544r0000gp/T/TestRayClusterAutoscalerMaxReplicasUpdateCreate_a_RayCluster_wi185238848/001
    test.go:114: [2026-01-08T20:19:27+08:00] Retrieving Pod Container test-ns-x9fh6/ray-cluster-head-vxk5l/autoscaler logs
    test.go:114: [2026-01-08T20:19:27+08:00] Retrieving Pod Container test-ns-x9fh6/ray-cluster-test-group-worker-zs8f8/ray-worker logs
=== RUN   TestRayClusterAutoscalerMaxReplicasUpdate/Create_a_RayCluster_with_autoscaler_v2_enabled(Scale_up_maxReplicas_from_2_to_3)
    core.go:87: [2026-01-08T20:19:54+08:00] Executing command: [python /home/ray/test_scripts/create_detached_actor.py actor0]
    core.go:100: [2026-01-08T20:19:56+08:00] Command stdout: (raylet) There are tasks with infeasible resource requests that cannot be scheduled. See https://docs.ray.io/en/latest/ray-core/scheduling/index.html#ray-scheduling-resources for more details. Possible solutions: 1. Updating the ray cluster to include nodes with all required resources 2. To cause the tasks with infeasible requests to raise an error instead of hanging, set the 'RAY_enable_infeasible_task_early_exit=true'. This feature will be turned on by default in a future release of Ray.
    core.go:101: [2026-01-08T20:19:56+08:00] Command stderr: 2026-01-08 04:19:55,108    INFO worker.py:1696 -- Using address 127.0.0.1:6379 set in the environment variable RAY_ADDRESS
        2026-01-08 04:19:55,110 INFO worker.py:1837 -- Connecting to existing Ray cluster at address: 10.210.194.219:6379...
        2026-01-08 04:19:55,118 INFO worker.py:2014 -- Connected to Ray cluster. View the dashboard at 10.210.194.219:8265 
        /home/ray/anaconda3/lib/python3.10/site-packages/ray/_private/worker.py:2062: FutureWarning: Tip: In future versions of Ray, Ray will no longer override accelerator visible devices env var if num_gpus=0 or num_gpus=None (default). To enable this behavior and turn off this error message, set RAY_ACCEL_ENV_VAR_OVERRIDE_ON_ZERO=0
          warnings.warn(
    core.go:87: [2026-01-08T20:19:56+08:00] Executing command: [python /home/ray/test_scripts/create_detached_actor.py actor1]
    core.go:100: [2026-01-08T20:19:57+08:00] Command stdout: 
    core.go:101: [2026-01-08T20:19:57+08:00] Command stderr: 2026-01-08 04:19:56,552    INFO worker.py:1696 -- Using address 127.0.0.1:6379 set in the environment variable RAY_ADDRESS
        2026-01-08 04:19:56,553 INFO worker.py:1837 -- Connecting to existing Ray cluster at address: 10.210.194.219:6379...
        2026-01-08 04:19:56,561 INFO worker.py:2014 -- Connected to Ray cluster. View the dashboard at 10.210.194.219:8265 
        /home/ray/anaconda3/lib/python3.10/site-packages/ray/_private/worker.py:2062: FutureWarning: Tip: In future versions of Ray, Ray will no longer override accelerator visible devices env var if num_gpus=0 or num_gpus=None (default). To enable this behavior and turn off this error message, set RAY_ACCEL_ENV_VAR_OVERRIDE_ON_ZERO=0
          warnings.warn(
    core.go:87: [2026-01-08T20:19:57+08:00] Executing command: [python /home/ray/test_scripts/create_detached_actor.py actor2]
    core.go:100: [2026-01-08T20:19:59+08:00] Command stdout: 
    core.go:101: [2026-01-08T20:19:59+08:00] Command stderr: 2026-01-08 04:19:58,243    INFO worker.py:1696 -- Using address 127.0.0.1:6379 set in the environment variable RAY_ADDRESS
        2026-01-08 04:19:58,244 INFO worker.py:1837 -- Connecting to existing Ray cluster at address: 10.210.194.219:6379...
        2026-01-08 04:19:58,262 INFO worker.py:2014 -- Connected to Ray cluster. View the dashboard at 10.210.194.219:8265 
        /home/ray/anaconda3/lib/python3.10/site-packages/ray/_private/worker.py:2062: FutureWarning: Tip: In future versions of Ray, Ray will no longer override accelerator visible devices env var if num_gpus=0 or num_gpus=None (default). To enable this behavior and turn off this error message, set RAY_ACCEL_ENV_VAR_OVERRIDE_ON_ZERO=0
          warnings.warn(
    test.go:114: [2026-01-08T20:20:07+08:00] Retrieving Pod Container test-ns-p8r27/ray-cluster-head-q22hb/ray-head logs
    test.go:102: [2026-01-08T20:20:07+08:00] Creating ephemeral output directory as KUBERAY_TEST_OUTPUT_DIR env variable is unset
    test.go:105: [2026-01-08T20:20:07+08:00] Output directory has been created at: /var/folders/_4/7rb65yt93ls_mllcrr35544r0000gp/T/TestRayClusterAutoscalerMaxReplicasUpdateCreate_a_RayCluster_wi1390403243/001
    test.go:114: [2026-01-08T20:20:07+08:00] Retrieving Pod Container test-ns-p8r27/ray-cluster-head-q22hb/autoscaler logs
    test.go:114: [2026-01-08T20:20:07+08:00] Retrieving Pod Container test-ns-p8r27/ray-cluster-test-group-worker-6z6xg/ray-worker logs
    test.go:114: [2026-01-08T20:20:07+08:00] Retrieving Pod Container test-ns-p8r27/ray-cluster-test-group-worker-njzjb/ray-worker logs
    test.go:114: [2026-01-08T20:20:07+08:00] Error getting logs from container test-ns-p8r27/ray-cluster-test-group-worker-njzjb/ray-worker
    test.go:114: [2026-01-08T20:20:07+08:00] Retrieving Pod Container test-ns-p8r27/ray-cluster-test-group-worker-tkxvh/ray-worker logs
    test.go:114: [2026-01-08T20:20:07+08:00] Error getting logs from container test-ns-p8r27/ray-cluster-test-group-worker-tkxvh/ray-worker
=== RUN   TestRayClusterAutoscalerMaxReplicasUpdate/Create_a_RayCluster_with_autoscaler_v2_enabled(Scale_down_maxReplicas_from_2_to_1)
    core.go:87: [2026-01-08T20:20:34+08:00] Executing command: [python /home/ray/test_scripts/create_detached_actor.py actor0]
    core.go:100: [2026-01-08T20:20:36+08:00] Command stdout: 
    core.go:101: [2026-01-08T20:20:36+08:00] Command stderr: 2026-01-08 04:20:35,207    INFO worker.py:1696 -- Using address 127.0.0.1:6379 set in the environment variable RAY_ADDRESS
        2026-01-08 04:20:35,208 INFO worker.py:1837 -- Connecting to existing Ray cluster at address: 10.210.194.217:6379...
        2026-01-08 04:20:35,216 INFO worker.py:2014 -- Connected to Ray cluster. View the dashboard at 10.210.194.217:8265 
        /home/ray/anaconda3/lib/python3.10/site-packages/ray/_private/worker.py:2062: FutureWarning: Tip: In future versions of Ray, Ray will no longer override accelerator visible devices env var if num_gpus=0 or num_gpus=None (default). To enable this behavior and turn off this error message, set RAY_ACCEL_ENV_VAR_OVERRIDE_ON_ZERO=0
          warnings.warn(
    core.go:87: [2026-01-08T20:20:36+08:00] Executing command: [python /home/ray/test_scripts/create_detached_actor.py actor1]
    core.go:100: [2026-01-08T20:20:37+08:00] Command stdout: 
    core.go:101: [2026-01-08T20:20:37+08:00] Command stderr: 2026-01-08 04:20:36,667    INFO worker.py:1696 -- Using address 127.0.0.1:6379 set in the environment variable RAY_ADDRESS
        2026-01-08 04:20:36,668 INFO worker.py:1837 -- Connecting to existing Ray cluster at address: 10.210.194.217:6379...
        2026-01-08 04:20:36,676 INFO worker.py:2014 -- Connected to Ray cluster. View the dashboard at 10.210.194.217:8265 
        /home/ray/anaconda3/lib/python3.10/site-packages/ray/_private/worker.py:2062: FutureWarning: Tip: In future versions of Ray, Ray will no longer override accelerator visible devices env var if num_gpus=0 or num_gpus=None (default). To enable this behavior and turn off this error message, set RAY_ACCEL_ENV_VAR_OVERRIDE_ON_ZERO=0
          warnings.warn(
    raycluster_autoscaler_test.go:423: 
        Timed out after 60.001s.
        Expected
            <int32>: 2
        to equal
            <int32>: 1
    test.go:114: [2026-01-08T20:21:42+08:00] Retrieving Pod Container test-ns-m26q9/ray-cluster-head-j7scr/ray-head logs
    test.go:102: [2026-01-08T20:21:42+08:00] Creating ephemeral output directory as KUBERAY_TEST_OUTPUT_DIR env variable is unset
    test.go:105: [2026-01-08T20:21:42+08:00] Output directory has been created at: /var/folders/_4/7rb65yt93ls_mllcrr35544r0000gp/T/TestRayClusterAutoscalerMaxReplicasUpdateCreate_a_RayCluster_wi3545858982/001
    test.go:114: [2026-01-08T20:21:42+08:00] Retrieving Pod Container test-ns-m26q9/ray-cluster-head-j7scr/autoscaler logs
    test.go:114: [2026-01-08T20:21:42+08:00] Retrieving Pod Container test-ns-m26q9/ray-cluster-test-group-worker-b9c8x/ray-worker logs
--- FAIL: TestRayClusterAutoscalerMaxReplicasUpdate (336.53s)
    --- PASS: TestRayClusterAutoscalerMaxReplicasUpdate/Create_a_RayCluster_with_autoscaling_enabled(Scale_up_maxReplicas_from_2_to_3) (110.31s)
    --- FAIL: TestRayClusterAutoscalerMaxReplicasUpdate/Create_a_RayCluster_with_autoscaling_enabled(Scale_down_maxReplicas_from_2_to_1) (91.19s)
    --- PASS: TestRayClusterAutoscalerMaxReplicasUpdate/Create_a_RayCluster_with_autoscaler_v2_enabled(Scale_up_maxReplicas_from_2_to_3) (40.01s)
    --- FAIL: TestRayClusterAutoscalerMaxReplicasUpdate/Create_a_RayCluster_with_autoscaler_v2_enabled(Scale_down_maxReplicas_from_2_to_1) (95.02s)
FAIL
FAIL    github.com/ray-project/kuberay/ray-operator/test/e2eautoscaler  336.995s
```

This is the log of the autoscaler: 
```
➜  ~ k logs -n test-ns-m26q9 ray-cluster-head-j7scr -c autoscaler
2026-01-08 04:20:14,978	INFO run_autoscaler.py:52 -- The Ray head is ready. Starting the autoscaler.
2026-01-08 04:20:15,198 - INFO - Refreshing K8s API client token and certs.
2026-01-08 04:20:15,198	INFO node_provider.py:283 -- Refreshing K8s API client token and certs.
2026-01-08 04:20:15,224 - INFO - Calculating hashes for file mounts and ray commands.
2026-01-08 04:20:15,224	INFO config.py:183 -- Calculating hashes for file mounts and ray commands.
2026-01-08 04:20:15,783 - INFO - session_name: session_2026-01-08_04-20-10_046511_1
2026-01-08 04:20:15,783	INFO monitor.py:88 -- session_name: session_2026-01-08_04-20-10_046511_1
2026-01-08 04:20:15,785 - INFO - Starting autoscaler metrics server on port 44217
2026-01-08 04:20:15,785	INFO monitor.py:112 -- Starting autoscaler metrics server on port 44217
2026-01-08 04:20:15,792 - INFO - Using Autoscaling Config:
auth: {}
available_node_types:
  headgroup:
    labels: {}
    max_workers: 0
    min_workers: 0
    node_config: {}
    resources:
      CPU: 0
      memory: 4000000000
  test-group:
    labels: {}
    max_workers: 2
    min_workers: 1
    node_config: {}
    resources:
      CPU: 1
      memory: 1000000000
cluster_name: ray-cluster
cluster_synced_files: []
file_mounts: {}
file_mounts_sync_continuously: false
head_node_type: headgroup
head_setup_commands: []
head_start_ray_commands: []
idle_timeout_minutes: 1.0
initialization_commands: []
max_workers: 2
provider:
  disable_launch_config_check: true
  disable_node_updaters: true
  foreground_node_launch: true
  namespace: test-ns-m26q9
  type: kuberay
  worker_liveness_check: false
setup_commands: []
upscaling_speed: 1000
worker_setup_commands: []
worker_start_ray_commands: []

2026-01-08 04:20:15,792	INFO autoscaler.py:68 -- Using Autoscaling Config:
auth: {}
available_node_types:
  headgroup:
    labels: {}
    max_workers: 0
    min_workers: 0
    node_config: {}
    resources:
      CPU: 0
      memory: 4000000000
  test-group:
    labels: {}
    max_workers: 2
    min_workers: 1
    node_config: {}
    resources:
      CPU: 1
      memory: 1000000000
cluster_name: ray-cluster
cluster_synced_files: []
file_mounts: {}
file_mounts_sync_continuously: false
head_node_type: headgroup
head_setup_commands: []
head_start_ray_commands: []
idle_timeout_minutes: 1.0
initialization_commands: []
max_workers: 2
provider:
  disable_launch_config_check: true
  disable_node_updaters: true
  foreground_node_launch: true
  namespace: test-ns-m26q9
  type: kuberay
  worker_liveness_check: false
setup_commands: []
upscaling_speed: 1000
worker_setup_commands: []
worker_start_ray_commands: []

2026-01-08 04:20:15,912 - INFO - Calculating hashes for file mounts and ray commands.
2026-01-08 04:20:15,912	INFO config.py:183 -- Calculating hashes for file mounts and ray commands.
2026-01-08 04:20:15,913 - INFO - Refreshing K8s API client token and certs.
2026-01-08 04:20:15,913	INFO node_provider.py:283 -- Refreshing K8s API client token and certs.
2026-01-08 04:20:15,936 - INFO - Listing pods for RayCluster ray-cluster in namespace test-ns-m26q9 at pods resource version >= 248623937.
2026-01-08 04:20:15,936	INFO cloud_provider.py:489 -- Listing pods for RayCluster ray-cluster in namespace test-ns-m26q9 at pods resource version >= 248623937.
2026-01-08 04:20:15,943 - INFO - Fetched pod data at resource version 248624971.
2026-01-08 04:20:15,943	INFO cloud_provider.py:507 -- Fetched pod data at resource version 248624971.
2026-01-08 04:20:15,944 - INFO - New instance ALLOCATED (id=2b0c3d07-51a5-40d8-a111-331894a2ea09, type=headgroup, cloud_instance_id=, ray_id=): allocated unmanaged cloud instance :ray-cluster-head-j7scr (HEAD) from cloud provider
2026-01-08 04:20:15,944	INFO instance_manager.py:247 -- New instance ALLOCATED (id=2b0c3d07-51a5-40d8-a111-331894a2ea09, type=headgroup, cloud_instance_id=, ray_id=): allocated unmanaged cloud instance :ray-cluster-head-j7scr (HEAD) from cloud provider
2026-01-08 04:20:15,944 - INFO - New instance ALLOCATED (id=9465a95d-2106-4042-994e-e57b925813f5, type=test-group, cloud_instance_id=, ray_id=): allocated unmanaged cloud instance :ray-cluster-test-group-worker-69r4c (WORKER) from cloud provider
2026-01-08 04:20:15,944	INFO instance_manager.py:247 -- New instance ALLOCATED (id=9465a95d-2106-4042-994e-e57b925813f5, type=test-group, cloud_instance_id=, ray_id=): allocated unmanaged cloud instance :ray-cluster-test-group-worker-69r4c (WORKER) from cloud provider
2026-01-08 04:20:21,007 - INFO - Calculating hashes for file mounts and ray commands.
2026-01-08 04:20:21,007	INFO config.py:183 -- Calculating hashes for file mounts and ray commands.
2026-01-08 04:20:21,026 - INFO - Listing pods for RayCluster ray-cluster in namespace test-ns-m26q9 at pods resource version >= 248623937.
2026-01-08 04:20:21,026	INFO cloud_provider.py:489 -- Listing pods for RayCluster ray-cluster in namespace test-ns-m26q9 at pods resource version >= 248623937.
2026-01-08 04:20:21,033 - INFO - Fetched pod data at resource version 248625778.
2026-01-08 04:20:21,033	INFO cloud_provider.py:507 -- Fetched pod data at resource version 248625778.
2026-01-08 04:20:21,034 - INFO - Update instance ALLOCATED->RAY_RUNNING (id=2b0c3d07-51a5-40d8-a111-331894a2ea09, type=headgroup, cloud_instance_id=ray-cluster-head-j7scr, ray_id=): ray node 5d0150ab70a3397cedd4d63bc97c8947c193c65dcb511b3cc8a7ee39 is IDLE
2026-01-08 04:20:21,034	INFO instance_manager.py:263 -- Update instance ALLOCATED->RAY_RUNNING (id=2b0c3d07-51a5-40d8-a111-331894a2ea09, type=headgroup, cloud_instance_id=ray-cluster-head-j7scr, ray_id=): ray node 5d0150ab70a3397cedd4d63bc97c8947c193c65dcb511b3cc8a7ee39 is IDLE
2026-01-08 04:20:26,064 - INFO - Calculating hashes for file mounts and ray commands.
2026-01-08 04:20:26,064	INFO config.py:183 -- Calculating hashes for file mounts and ray commands.
2026-01-08 04:20:26,089 - INFO - Listing pods for RayCluster ray-cluster in namespace test-ns-m26q9 at pods resource version >= 248626151.
2026-01-08 04:20:26,089	INFO cloud_provider.py:489 -- Listing pods for RayCluster ray-cluster in namespace test-ns-m26q9 at pods resource version >= 248626151.
2026-01-08 04:20:26,097 - INFO - Fetched pod data at resource version 248626525.
2026-01-08 04:20:26,097	INFO cloud_provider.py:507 -- Fetched pod data at resource version 248626525.
2026-01-08 04:20:26,097 - INFO - Update instance ALLOCATED->RAY_RUNNING (id=9465a95d-2106-4042-994e-e57b925813f5, type=test-group, cloud_instance_id=ray-cluster-test-group-worker-69r4c, ray_id=): ray node 3e7213ca7f7f6662c3d6c2946fa79b779adf7bb00fc027dde6af970d is IDLE
2026-01-08 04:20:26,097	INFO instance_manager.py:263 -- Update instance ALLOCATED->RAY_RUNNING (id=9465a95d-2106-4042-994e-e57b925813f5, type=test-group, cloud_instance_id=ray-cluster-test-group-worker-69r4c, ray_id=): ray node 3e7213ca7f7f6662c3d6c2946fa79b779adf7bb00fc027dde6af970d is IDLE
2026-01-08 04:20:31,130 - INFO - Calculating hashes for file mounts and ray commands.
2026-01-08 04:20:31,130	INFO config.py:183 -- Calculating hashes for file mounts and ray commands.
2026-01-08 04:20:31,154 - INFO - Listing pods for RayCluster ray-cluster in namespace test-ns-m26q9 at pods resource version >= 248626151.
2026-01-08 04:20:31,154	INFO cloud_provider.py:489 -- Listing pods for RayCluster ray-cluster in namespace test-ns-m26q9 at pods resource version >= 248626151.
2026-01-08 04:20:31,162 - INFO - Fetched pod data at resource version 248627307.
2026-01-08 04:20:31,162	INFO cloud_provider.py:507 -- Fetched pod data at resource version 248627307.
2026-01-08 04:20:36,194 - INFO - Calculating hashes for file mounts and ray commands.
2026-01-08 04:20:36,194	INFO config.py:183 -- Calculating hashes for file mounts and ray commands.
2026-01-08 04:20:36,219 - INFO - Listing pods for RayCluster ray-cluster in namespace test-ns-m26q9 at pods resource version >= 248626151.
2026-01-08 04:20:36,219	INFO cloud_provider.py:489 -- Listing pods for RayCluster ray-cluster in namespace test-ns-m26q9 at pods resource version >= 248626151.
2026-01-08 04:20:36,226 - INFO - Fetched pod data at resource version 248628052.
2026-01-08 04:20:36,226	INFO cloud_provider.py:507 -- Fetched pod data at resource version 248628052.
2026-01-08 04:20:41,257 - INFO - Calculating hashes for file mounts and ray commands.
2026-01-08 04:20:41,257	INFO config.py:183 -- Calculating hashes for file mounts and ray commands.
2026-01-08 04:20:41,281 - INFO - Listing pods for RayCluster ray-cluster in namespace test-ns-m26q9 at pods resource version >= 248626151.
2026-01-08 04:20:41,281	INFO cloud_provider.py:489 -- Listing pods for RayCluster ray-cluster in namespace test-ns-m26q9 at pods resource version >= 248626151.
2026-01-08 04:20:41,287 - INFO - Fetched pod data at resource version 248628839.
2026-01-08 04:20:41,287	INFO cloud_provider.py:507 -- Fetched pod data at resource version 248628839.
2026-01-08 04:20:41,302 - INFO - Adding 1 node(s) of type test-group.
2026-01-08 04:20:41,302	INFO event_logger.py:76 -- Adding 1 node(s) of type test-group.
2026-01-08 04:20:41,303 - INFO - New instance QUEUED (id=6903e619-63f5-4541-9dde-f6e4084aee9c, type=test-group, cloud_instance_id=, ray_id=): queuing new instance of test-group from scheduler
2026-01-08 04:20:41,303	INFO instance_manager.py:247 -- New instance QUEUED (id=6903e619-63f5-4541-9dde-f6e4084aee9c, type=test-group, cloud_instance_id=, ray_id=): queuing new instance of test-group from scheduler
2026-01-08 04:20:41,303 - INFO - Update instance QUEUED->REQUESTED (id=6903e619-63f5-4541-9dde-f6e4084aee9c, type=test-group, cloud_instance_id=, ray_id=): requested to launch test-group with request id 37ba289d-aedf-4960-8cb7-0a046130ecc1
2026-01-08 04:20:41,303	INFO instance_manager.py:263 -- Update instance QUEUED->REQUESTED (id=6903e619-63f5-4541-9dde-f6e4084aee9c, type=test-group, cloud_instance_id=, ray_id=): requested to launch test-group with request id 37ba289d-aedf-4960-8cb7-0a046130ecc1
2026-01-08 04:20:41,327 - INFO - Listing pods for RayCluster ray-cluster in namespace test-ns-m26q9 at pods resource version >= 248626151.
2026-01-08 04:20:41,327	INFO cloud_provider.py:489 -- Listing pods for RayCluster ray-cluster in namespace test-ns-m26q9 at pods resource version >= 248626151.
2026-01-08 04:20:41,336 - INFO - Fetched pod data at resource version 248628887.
2026-01-08 04:20:41,336	INFO cloud_provider.py:507 -- Fetched pod data at resource version 248628887.
2026-01-08 04:20:41,337 - INFO - Submitting a scale request: KubeRayProvider.ScaleRequest(desired_num_workers=defaultdict(<class 'int'>, {'test-group': 2}), workers_to_delete=defaultdict(<class 'list'>, {}), worker_groups_without_pending_deletes=set(), worker_groups_with_pending_deletes=set())
2026-01-08 04:20:41,337	INFO cloud_provider.py:358 -- Submitting a scale request: KubeRayProvider.ScaleRequest(desired_num_workers=defaultdict(<class 'int'>, {'test-group': 2}), workers_to_delete=defaultdict(<class 'list'>, {}), worker_groups_without_pending_deletes=set(), worker_groups_with_pending_deletes=set())
2026-01-08 04:20:46,383 - INFO - Calculating hashes for file mounts and ray commands.
2026-01-08 04:20:46,383	INFO config.py:183 -- Calculating hashes for file mounts and ray commands.
2026-01-08 04:20:46,419 - INFO - Listing pods for RayCluster ray-cluster in namespace test-ns-m26q9 at pods resource version >= 248626151.
2026-01-08 04:20:46,419	INFO cloud_provider.py:489 -- Listing pods for RayCluster ray-cluster in namespace test-ns-m26q9 at pods resource version >= 248626151.
2026-01-08 04:20:46,425 - INFO - Fetched pod data at resource version 248629620.
2026-01-08 04:20:46,425	INFO cloud_provider.py:507 -- Fetched pod data at resource version 248629620.
2026-01-08 04:20:46,426 - INFO - Update instance REQUESTED->ALLOCATED (id=6903e619-63f5-4541-9dde-f6e4084aee9c, type=test-group, cloud_instance_id=, ray_id=): allocated unassigned cloud instance ray-cluster-test-group-worker-b9c8x
2026-01-08 04:20:46,426	INFO instance_manager.py:263 -- Update instance REQUESTED->ALLOCATED (id=6903e619-63f5-4541-9dde-f6e4084aee9c, type=test-group, cloud_instance_id=, ray_id=): allocated unassigned cloud instance ray-cluster-test-group-worker-b9c8x
2026-01-08 04:20:46,426 - INFO - Update instance RAY_RUNNING->TERMINATED (id=9465a95d-2106-4042-994e-e57b925813f5, type=test-group, cloud_instance_id=ray-cluster-test-group-worker-69r4c, ray_id=3e7213ca7f7f6662c3d6c2946fa79b779adf7bb00fc027dde6af970d): cloud instance ray-cluster-test-group-worker-69r4c no longer found
2026-01-08 04:20:46,426	INFO instance_manager.py:263 -- Update instance RAY_RUNNING->TERMINATED (id=9465a95d-2106-4042-994e-e57b925813f5, type=test-group, cloud_instance_id=ray-cluster-test-group-worker-69r4c, ray_id=3e7213ca7f7f6662c3d6c2946fa79b779adf7bb00fc027dde6af970d): cloud instance ray-cluster-test-group-worker-69r4c no longer found
2026-01-08 04:20:51,459 - INFO - Calculating hashes for file mounts and ray commands.
2026-01-08 04:20:51,459	INFO config.py:183 -- Calculating hashes for file mounts and ray commands.
2026-01-08 04:20:51,480 - INFO - Listing pods for RayCluster ray-cluster in namespace test-ns-m26q9 at pods resource version >= 248626151.
2026-01-08 04:20:51,480	INFO cloud_provider.py:489 -- Listing pods for RayCluster ray-cluster in namespace test-ns-m26q9 at pods resource version >= 248626151.
2026-01-08 04:20:51,486 - INFO - Fetched pod data at resource version 248630472.
2026-01-08 04:20:51,486	INFO cloud_provider.py:507 -- Fetched pod data at resource version 248630472.
2026-01-08 04:20:56,520 - INFO - Calculating hashes for file mounts and ray commands.
2026-01-08 04:20:56,520	INFO config.py:183 -- Calculating hashes for file mounts and ray commands.
2026-01-08 04:20:56,546 - INFO - Listing pods for RayCluster ray-cluster in namespace test-ns-m26q9 at pods resource version >= 248626151.
2026-01-08 04:20:56,546	INFO cloud_provider.py:489 -- Listing pods for RayCluster ray-cluster in namespace test-ns-m26q9 at pods resource version >= 248626151.
2026-01-08 04:20:56,553 - INFO - Fetched pod data at resource version 248631203.
2026-01-08 04:20:56,553	INFO cloud_provider.py:507 -- Fetched pod data at resource version 248631203.
2026-01-08 04:20:56,554 - INFO - Update instance ALLOCATED->RAY_RUNNING (id=6903e619-63f5-4541-9dde-f6e4084aee9c, type=test-group, cloud_instance_id=ray-cluster-test-group-worker-b9c8x, ray_id=): ray node e01bf94f958b92a7fcf0d731c4e6128046c7fc68031e337100d1d8f4 is RUNNING
2026-01-08 04:20:56,554	INFO instance_manager.py:263 -- Update instance ALLOCATED->RAY_RUNNING (id=6903e619-63f5-4541-9dde-f6e4084aee9c, type=test-group, cloud_instance_id=ray-cluster-test-group-worker-b9c8x, ray_id=): ray node e01bf94f958b92a7fcf0d731c4e6128046c7fc68031e337100d1d8f4 is RUNNING
2026-01-08 04:21:01,587 - INFO - Calculating hashes for file mounts and ray commands.
2026-01-08 04:21:01,587	INFO config.py:183 -- Calculating hashes for file mounts and ray commands.
2026-01-08 04:21:01,619 - INFO - Listing pods for RayCluster ray-cluster in namespace test-ns-m26q9 at pods resource version >= 248626151.
2026-01-08 04:21:01,619	INFO cloud_provider.py:489 -- Listing pods for RayCluster ray-cluster in namespace test-ns-m26q9 at pods resource version >= 248626151.
2026-01-08 04:21:01,627 - INFO - Fetched pod data at resource version 248631983.
2026-01-08 04:21:01,627	INFO cloud_provider.py:507 -- Fetched pod data at resource version 248631983.
2026-01-08 04:21:06,660 - INFO - Calculating hashes for file mounts and ray commands.
2026-01-08 04:21:06,660	INFO config.py:183 -- Calculating hashes for file mounts and ray commands.
2026-01-08 04:21:06,681 - INFO - Listing pods for RayCluster ray-cluster in namespace test-ns-m26q9 at pods resource version >= 248626151.
2026-01-08 04:21:06,681	INFO cloud_provider.py:489 -- Listing pods for RayCluster ray-cluster in namespace test-ns-m26q9 at pods resource version >= 248626151.
2026-01-08 04:21:06,688 - INFO - Fetched pod data at resource version 248632729.
2026-01-08 04:21:06,688	INFO cloud_provider.py:507 -- Fetched pod data at resource version 248632729.
2026-01-08 04:21:11,721 - INFO - Calculating hashes for file mounts and ray commands.
2026-01-08 04:21:11,721	INFO config.py:183 -- Calculating hashes for file mounts and ray commands.
2026-01-08 04:21:11,744 - INFO - Listing pods for RayCluster ray-cluster in namespace test-ns-m26q9 at pods resource version >= 248626151.
2026-01-08 04:21:11,744	INFO cloud_provider.py:489 -- Listing pods for RayCluster ray-cluster in namespace test-ns-m26q9 at pods resource version >= 248626151.
2026-01-08 04:21:11,750 - INFO - Fetched pod data at resource version 248633512.
2026-01-08 04:21:11,750	INFO cloud_provider.py:507 -- Fetched pod data at resource version 248633512.
2026-01-08 04:21:16,758 - INFO - Refreshing K8s API client token and certs.
2026-01-08 04:21:16,758	INFO node_provider.py:283 -- Refreshing K8s API client token and certs.
2026-01-08 04:21:16,783 - INFO - Calculating hashes for file mounts and ray commands.
2026-01-08 04:21:16,783	INFO config.py:183 -- Calculating hashes for file mounts and ray commands.
2026-01-08 04:21:16,783 - INFO - Refreshing K8s API client token and certs.
2026-01-08 04:21:16,783	INFO node_provider.py:283 -- Refreshing K8s API client token and certs.
2026-01-08 04:21:16,808 - INFO - Listing pods for RayCluster ray-cluster in namespace test-ns-m26q9 at pods resource version >= 248626151.
2026-01-08 04:21:16,808	INFO cloud_provider.py:489 -- Listing pods for RayCluster ray-cluster in namespace test-ns-m26q9 at pods resource version >= 248626151.
2026-01-08 04:21:16,815 - INFO - Fetched pod data at resource version 248634337.
2026-01-08 04:21:16,815	INFO cloud_provider.py:507 -- Fetched pod data at resource version 248634337.
2026-01-08 04:21:21,847 - INFO - Calculating hashes for file mounts and ray commands.
2026-01-08 04:21:21,847	INFO config.py:183 -- Calculating hashes for file mounts and ray commands.
2026-01-08 04:21:21,868 - INFO - Listing pods for RayCluster ray-cluster in namespace test-ns-m26q9 at pods resource version >= 248626151.
2026-01-08 04:21:21,868	INFO cloud_provider.py:489 -- Listing pods for RayCluster ray-cluster in namespace test-ns-m26q9 at pods resource version >= 248626151.
2026-01-08 04:21:21,875 - INFO - Fetched pod data at resource version 248635116.
2026-01-08 04:21:21,875	INFO cloud_provider.py:507 -- Fetched pod data at resource version 248635116.
2026-01-08 04:21:26,907 - INFO - Calculating hashes for file mounts and ray commands.
2026-01-08 04:21:26,907	INFO config.py:183 -- Calculating hashes for file mounts and ray commands.
2026-01-08 04:21:26,931 - INFO - Listing pods for RayCluster ray-cluster in namespace test-ns-m26q9 at pods resource version >= 248626151.
2026-01-08 04:21:26,931	INFO cloud_provider.py:489 -- Listing pods for RayCluster ray-cluster in namespace test-ns-m26q9 at pods resource version >= 248626151.
2026-01-08 04:21:26,938 - INFO - Fetched pod data at resource version 248635856.
2026-01-08 04:21:26,938	INFO cloud_provider.py:507 -- Fetched pod data at resource version 248635856.
2026-01-08 04:21:31,972 - INFO - Calculating hashes for file mounts and ray commands.
2026-01-08 04:21:31,972	INFO config.py:183 -- Calculating hashes for file mounts and ray commands.
2026-01-08 04:21:31,996 - INFO - Listing pods for RayCluster ray-cluster in namespace test-ns-m26q9 at pods resource version >= 248626151.
2026-01-08 04:21:31,996	INFO cloud_provider.py:489 -- Listing pods for RayCluster ray-cluster in namespace test-ns-m26q9 at pods resource version >= 248626151.
2026-01-08 04:21:32,003 - INFO - Fetched pod data at resource version 248636639.
2026-01-08 04:21:32,003	INFO cloud_provider.py:507 -- Fetched pod data at resource version 248636639.
```

### Are you willing to submit a PR?

- [ ] Yes I am willing to submit a PR!

## 评论 (3)

### KunWuLuan · 2026-01-08

I found the code to scale up base on the minReplicas, but I didn't find the code to scale down based on the maxReplicas in Ray:

```
        # Calculate the desired number of workers by type.
        num_workers_dict = defaultdict(int)
        worker_groups = ray_cluster["spec"].get("workerGroupSpecs", [])
        for worker_group in worker_groups:
            node_type = worker_group["groupName"]
            # Handle the case where users manually increase `minReplicas`
            # to scale up the number of worker Pods. In this scenario,
            # `replicas` will be smaller than `minReplicas`.
            # num_workers_dict should account for multi-host replicas when
            # `numOfHosts`` is set.
            num_of_hosts = worker_group.get("numOfHosts", 1)
            replicas = (
                max(worker_group["replicas"], worker_group["minReplicas"])
                * num_of_hosts
            )

            # The `replicas` field in worker group specs can be updated by users at any time.
            # However, users should only increase the field (manually upscaling the worker group), not decrease it,
            # because downscaling the worker group requires specifying which workers to delete explicitly in the `workersToDelete` field.
            # Since we don't have a way to enforce this, we need to fix unexpected decreases on the `replicas` field by using actual observations.
            # For example, if the user manually decreases the `replicas` field to 0 without specifying which workers to delete,
            # we should fix the `replicas` field back to the number of observed workers excluding the workers to be deleted,
            # otherwise, we won't have a correct `replicas` matches the actual number of workers eventually.
            num_workers_dict[node_type] = max(
                replicas, observed_workers_dict[node_type]
            )

        # Add to launch nodes.
        for node_type, count in to_launch.items():
            num_workers_dict[node_type] += count

        to_delete_instances_by_type = defaultdict(list)
        # Update the number of workers with to_delete_instances
        # and group them by type.
        for to_delete_id in to_delete_instances:
            to_delete_instance = cur_instances.get(to_delete_id, None)
            if to_delete_instance is None:
                # This instance has already been deleted.
                continue

            if to_delete_instance.node_kind == NodeKind.HEAD:
                # Not possible to delete head node.
                continue

            if to_delete_instance.cloud_instance_id in worker_to_delete_set:
                # If the instance is already in the workersToDelete field of
                # any worker group, skip it.
                continue

            num_workers_dict[to_delete_instance.node_type] -= 1
            assert num_workers_dict[to_delete_instance.node_type] >= 0
            to_delete_instances_by_type[to_delete_instance.node_type].append(
                to_delete_instance
            )

        scale_request = KubeRayProvider.ScaleRequest(
            desired_num_workers=num_workers_dict,
            workers_to_delete=to_delete_instances_by_type,
            worker_groups_without_pending_deletes=worker_groups_without_pending_deletes,
            worker_groups_with_pending_deletes=worker_groups_with_pending_deletes,
        )

        return scale_request

```

### github-actions[bot] · 2026-09-22

This issue has been automatically marked as stale because it has not had
any activity for 120 days. It will be closed in 14 days if no further activity occurs.

If you'd like to keep this issue open, just leave any comment, and the stale label will be removed.
If you'd like to get more attention on this issue, please tag one of the KubeRay maintainers.

You can always ask for help on [Ray's public Slack channel](https://github.com/ray-project/kuberay#getting-involved).

### KunWuLuan · 2026-09-23

Closing this issue. The failures were specific to my local environment; my analysis of the Ray autoscaler's worker calculation (minReplicas-based scale-up without a matching maxReplicas-based scale-down path) pointed to a Ray-side behavior difference rather than a KubeRay bug. If this resurfaces with a KubeRay-side cause, I'll reopen with details.
