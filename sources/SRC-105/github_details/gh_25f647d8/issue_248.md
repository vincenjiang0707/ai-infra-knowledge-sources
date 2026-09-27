# [Issue #248] dcgmi dmon doesn't work properly with different MIG instances

source: https://github.com/NVIDIA/DCGM/issues/248
state: open | updated: 2025-08-05T17:40:44Z
labels: 

## 正文

HI,

I have encountered a problem with the dcgmi dmon command output when my GPU is sliced into MIG instances with different profiles.

As i can see, there is already an issue with similar problem -   #138 , but it is still open and doesn't have an answer.


So,  the problem is when i have several MIG instances of different size(e.g., 1g.5gb and 3g.20gb), and run `sudo dcgmproftester12 --no-dcgm-validation -t 1001 -d 600 -i 0 --target-max-value` in one console and type `dcgmi dmon -e 1002,1005 -i 0,i:0,i:1` in another, i get the  following output:


<img width="852" height="151" alt="Image" src="https://github.com/user-attachments/assets/4555eca8-ed9c-46d9-93f6-beddec8484ba" />

GPU-I 1 here is 3g.20gb. The larger instance in the output is always limited to the smaller instance. By this i mean if smaller instance has 1 sm controller and larger has 3, larger will have only 1/3 sm usage in the output.

When i run this on 2 mig instances: 3g.20gb and 3g.20gb, i will get this:

<img width="675" height="152" alt="Image" src="https://github.com/user-attachments/assets/5db1b8ae-e1d4-450c-97d1-f171a7196c3b" />

Smaller instance is the same size as others, so no limited mig instances in the output.



When i run this on another 2 mig instances: 3g.20gb and 4g.20gb, i will get this:

<img width="897" height="150" alt="Image" src="https://github.com/user-attachments/assets/2dc54f3e-6eef-4a54-bfef-87c13a58c8f7" />
GPU-I 1 here is 4g.20gb. Here smaller instance has 3 sm controllers, while larger has 4, thats why larger shows only 3/4 sm usage


---

More details:
GPU card: NVIDIA A100-PCIE-40GB

For example with 2 mig instances: 3g.20gb and 4g.20gb 

1) `nvidia-smi` output is:

<img width="831" height="596" alt="Image" src="https://github.com/user-attachments/assets/8dfe3cf4-d155-47d3-9430-85812abf97e7" />

2) `nvidia-smi mig -lci` output:

<img width="661" height="179" alt="Image" src="https://github.com/user-attachments/assets/9666bb6d-c374-49df-a2ee-e79b5cc12de5" />

3) `nvidia-smi mig -lgi` output:

<img width="543" height="161" alt="Image" src="https://github.com/user-attachments/assets/b437f319-70ae-4f71-be72-fa136fdbf7c5" />

4) `dcgmi discovery -c` output







## 评论 (2)

### 1KONSTANT1 · 2025-08-05

dcgmi discovery -c output:

<img width="881" height="164" alt="Image" src="https://github.com/user-attachments/assets/97cc02b7-c237-4d0c-82cb-d23bcd66a787" />

Also i have tested by running scripts, that get NO MIG GPU utilization at 100%, output of dcgmi dmon with different migs is still limited.


### 1KONSTANT1 · 2025-08-05

OS - Rocky linux 9
dcgmi  version: 4.3.0

Installed using guides here - https://docs.nvidia.com/datacenter/dcgm/latest/user-guide/getting-started.html#installation:~:text=X-,Installation,-%EF%83%81
