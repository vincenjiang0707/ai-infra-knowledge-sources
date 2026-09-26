source: https://docs.nvidia.com/dynamo/v1.2.1/kubernetes-deployment/cloud-provider-guides/aws/ecs
lastmod: 2026-09-24T19:58:16.636Z

Amazon Elastic Container Service (ECS)


Amazon Elastic Container Service (ECS)

## 1. EC2 Cluster Setup (for vLLM workloads)

- Go to AWS ECS console,
**Clusters**tab and click on**Create cluster**with name`dynamo-GPU`

- Input the cluster name and choose
**AWS EC2 instances**as the infrastructure. This option will create a cluster with EC2 instances to deploy containers. - Choose the ECS-optimized GPU AMI
`Amazon Linux 2 (GPU)`

(Amazon ECS–optimized), which includes NVIDIA drivers and the Docker GPU runtime out of the box. - Choose
`g6e.2xlarge`

as the**EC2 instance type**and add an`SSH Key pair`

so you can log in the instance for debugging purpose. To test with disaggregated serving, we need at least 2 GPUs, so you can choose`g6e.12xlarge`

with 4 GPUs - Set
**Root EBS volume size**as`200`

- For the networking, use the default settings. Make sure the
**security group**has

- an inbound rule which allows “All traffic” from this security group.
- an inbound rule for port 22 and 8000, so that you can ssh into the instance for debugging purpose

- Select
`Turn on`

for**Auto-assign public IP**option. - Click on
**Create**and a cluster will be deployed through cloudformation.

## 2. Fargate Cluster Setup (for ETCD/NATS services)

- Go to AWS ECS console,
**Clusters**tab and click on**Create cluster** - Input the cluster name as
`dynamo-fargate`

- Choose
**AWS Fargate (serverless)**as the infrastructure - For networking, use the same VPC and subnets as the EC2 cluster to ensure connectivity between services
- For the security group, use the same security group as the EC2 cluster. This automatically allows communication between all services.
- Ensure outbound rules allow all traffic (default setting) so the Fargate tasks can download container images and communicate externally
- Click on
**Create**to deploy the Fargate cluster

## 3. ETCD/NATS Task Definitions Setup

Add a task for ETCD and NATS services to run on Fargate. A sample task definition JSON is attached.

### 3.1 Create the ecsTaskExecutionRole (Required)

Before creating the task definitions, you need to create the `ecsTaskExecutionRole`

IAM role. This role allows ECS to pull container images from registries and write logs to CloudWatch on your behalf.

If you create task definitions through the AWS Console’s step-by-step wizard, this role is created automatically. However, when importing task definitions from JSON (as recommended in this guide), you must create this role manually.

Follow the [AWS documentation on creating the task execution IAM role](https://docs.aws.amazon.com/AmazonECS/latest/developerguide/task_execution_IAM_role.html#create-task-execution-role) to create a role named `ecsTaskExecutionRole`

with the `AmazonECSTaskExecutionRolePolicy`

policy attached.

Based on the task definition, you may need to add Amazon CloudWatch permissions and AWS Secrets Manager permissions to the `ecsTaskExecutionRole`

. See details in the [Amazon CloudWatch Logs permissions reference](https://docs.aws.amazon.com/AmazonCloudWatch/latest/logs/permissions-reference-cwl.html) the [AWS Secrets Manager authentication and access control guide](https://docs.aws.amazon.com/secretsmanager/latest/userguide/auth-and-access.html#auth-and-access_secrets)

The role ARN will be `arn:aws:iam::<your-account-id>:role/ecsTaskExecutionRole`

. Make sure to update `<your-account-id>`

in any task definition JSON files with your actual AWS account ID.

### 3.2 Task Definition Configuration

- ETCD container

- Container name use
`etcd`

- Image URL is
`bitnamilegacy/etcd`

and**Yes**for Essential container - Container port

- Environment variable key is
`ALLOW_NONE_AUTHENTICATION`

and value is`YES`


- NATS container

- Container name use
`nats`

- Image URL is
`nats`

and**Yes**for Essential container - Container port

- Docker configuration, add
`-js, --trace`

in**Command**

## 4. vLLM Task Definitions Setup

Ensure you have created the `ecsTaskExecutionRole`

as described in section 3.1 before creating these task definitions.

- Dynamo vLLM Frontend and Decoding Worker Task This task will create vLLM frontend, processors, routers and a decoding worker. Please follow steps below to create this task

- Set container name as
`dynamo-frontend`

and use prebuild[Dynamo container](https://catalog.ngc.nvidia.com/orgs/nvidia/teams/ai-dynamo/containers/vllm-runtime). - Choose
`Amazon EC2 instances`

as the**Launch type**with**Task size**`2 vCPU`

and`40 GB`

memory - Choose
`host`

as the Network mode. - Container name use
`dynamo-vLLM-frontend`

- Add your Image URL (You can use the prebuild
[Dynamo container](https://catalog.ngc.nvidia.com/orgs/nvidia/teams/ai-dynamo/containers/vllm-runtime)) and**Yes**for Essential container. It can be AWS ECR URL or Nvidia NGC URL. If using NGC URL, please also choose**Private registry authentication**and add your Secret Manager ARN or name. - Container port

- Use
`1`

GPU for**Resource allocation limits** - Environment variables settings as below. Will override the
`IP_ADDRESS`

later.

- Docker configuration
Add
`sh,-c`

in**Entry point**and`cd examples/backends/vllm && python -m dynamo.frontend --router-mode kv & python3 -m dynamo.vllm --model Qwen/Qwen3-0.6B --enforce-eager`

in**Command**

- Dynamo vLLM PrefillWorker Task Create the PrefillWorker task same as the frontend worker, except for following changes

- Set container name as
`dynamo-prefill`

- No container port mapping
- Docker configuration with command
`cd examples/backends/vllm && python3 -m dynamo.vllm --model Qwen/Qwen3-0.6B --enforce-eager --disaggregation-mode prefill`


## 5. Task Deployment

You can create a service or directly run the task from the task definition

- ETCD/NATS Task

- Choose the Fargate cluster (
`dynamo-fargate`

) for**Existing cluster**created in step 2. - Select
**Launch type**as`FARGATE`

- In the
**Networking**section, select the same VPC and subnets used for the EC2 cluster - For
**Security group**, select the same security group used by the EC2 cluster - Verify that outbound rules allow all traffic for downloading images and external communication
- Wait for this deployment to finish, and get the
**Private IP**of this task.

- Dynamo Frontend and Decoding Worker Task

- Choose the EC2 cluster (
`dynamo-GPU`

) for**Existing cluster**created in step 1. - In the
**Container Overrides**, use the IP for ETCD/NATS task for the`ETCD_ENDPOINTS`

and`NATS_SERVER`

values. - After the deployment, an aggregated serving endpoint is created and you can test it with scripts in step 6.

- Dynamo PrefillWorker Task

- For disaggregated serving, you can deploy a separate prefill worker on another GPU. Choose the EC2 cluster (
`dynamo-GPU`

) for**Existing cluster**created in step 1 with at least 2 GPUs (`g6e.12xlarge`

for example) - In the
**Container Overrides**, use the IP for ETCD/NATS task for the`ETCD_ENDPOINTS`

and`NATS_SERVER`

values.

## 6. Testing

Find the public IP of the dynamo frontend task from the task page. Run following commands to query the endpoint.

You should be able to see the responses from the hosted endpoint.