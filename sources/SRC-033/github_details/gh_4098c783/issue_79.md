# [Issue #79] ascend 910B multiprocessing error

source: https://github.com/Ascend/pytorch/issues/79
state: open | updated: 2025-08-27T09:28:35Z
labels: 

## 正文

Process ForkServerProcess-4:
Process ForkServerProcess-5:
Process ForkServerProcess-7:
Process ForkServerProcess-8:
Process ForkServerProcess-3:
Process ForkServerProcess-2:
Process ForkServerProcess-6:
Traceback (most recent call last):
Traceback (most recent call last):
Traceback (most recent call last):
Traceback (most recent call last):
Traceback (most recent call last):
Traceback (most recent call last):
Traceback (most recent call last):
Traceback (most recent call last):
  File "/root/miniconda3/envs/trajcrafter/lib/python3.10/multiprocessing/process.py", line 314, in _bootstrap
    self.run()
  File "/root/miniconda3/envs/trajcrafter/lib/python3.10/multiprocessing/process.py", line 314, in _bootstrap
    self.run()
  File "/root/miniconda3/envs/trajcrafter/lib/python3.10/multiprocessing/process.py", line 314, in _bootstrap
    self.run()
  File "/root/miniconda3/envs/trajcrafter/lib/python3.10/multiprocessing/process.py", line 314, in _bootstrap
    self.run()
  File "/root/miniconda3/envs/trajcrafter/lib/python3.10/multiprocessing/process.py", line 314, in _bootstrap
    self.run()
  File "/root/miniconda3/envs/trajcrafter/lib/python3.10/multiprocessing/process.py", line 314, in _bootstrap
    self.run()
  File "/root/miniconda3/envs/trajcrafter/lib/python3.10/multiprocessing/process.py", line 314, in _bootstrap
    self.run()
  File "/root/miniconda3/envs/trajcrafter/lib/python3.10/multiprocessing/process.py", line 314, in _bootstrap
    self.run()
  File "/root/miniconda3/envs/trajcrafter/lib/python3.10/multiprocessing/process.py", line 108, in run
    self._target(*self._args, **self._kwargs)
  File "/root/miniconda3/envs/trajcrafter/lib/python3.10/multiprocessing/process.py", line 108, in run
    self._target(*self._args, **self._kwargs)
  File "/root/miniconda3/envs/trajcrafter/lib/python3.10/multiprocessing/process.py", line 108, in run
    self._target(*self._args, **self._kwargs)
  File "/root/miniconda3/envs/trajcrafter/lib/python3.10/multiprocessing/process.py", line 108, in run
    self._target(*self._args, **self._kwargs)
  File "/root/miniconda3/envs/trajcrafter/lib/python3.10/multiprocessing/process.py", line 108, in run
    self._target(*self._args, **self._kwargs)
  File "/root/miniconda3/envs/trajcrafter/lib/python3.10/multiprocessing/process.py", line 108, in run
    self._target(*self._args, **self._kwargs)
  File "/root/miniconda3/envs/trajcrafter/lib/python3.10/multiprocessing/process.py", line 108, in run
    self._target(*self._args, **self._kwargs)
  File "/root/miniconda3/envs/trajcrafter/lib/python3.10/multiprocessing/process.py", line 108, in run
    self._target(*self._args, **self._kwargs)
  File "/usr/local/Ascend/ascend-toolkit/latest/python/site-packages/tbe/common/repository_manager/route.py", line 65, in wrapper
    raise exp
  File "/usr/local/Ascend/ascend-toolkit/latest/python/site-packages/tbe/common/repository_manager/route.py", line 65, in wrapper
    raise exp
  File "/usr/local/Ascend/ascend-toolkit/latest/python/site-packages/tbe/common/repository_manager/route.py", line 65, in wrapper
    raise exp
  File "/usr/local/Ascend/ascend-toolkit/latest/python/site-packages/tbe/common/repository_manager/route.py", line 65, in wrapper
    raise exp
  File "/usr/local/Ascend/ascend-toolkit/latest/python/site-packages/tbe/common/repository_manager/route.py", line 65, in wrapper
    raise exp
  File "/usr/local/Ascend/ascend-toolkit/latest/python/site-packages/tbe/common/repository_manager/route.py", line 65, in wrapper
    raise exp
  File "/usr/local/Ascend/ascend-toolkit/latest/python/site-packages/tbe/common/repository_manager/route.py", line 62, in wrapper
    func(*args, **kwargs)
  File "/usr/local/Ascend/ascend-toolkit/latest/python/site-packages/tbe/common/repository_manager/route.py", line 62, in wrapper
    func(*args, **kwargs)
  File "/usr/local/Ascend/ascend-toolkit/latest/python/site-packages/tbe/common/repository_manager/route.py", line 65, in wrapper
    raise exp
  File "/usr/local/Ascend/ascend-toolkit/latest/python/site-packages/tbe/common/repository_manager/route.py", line 65, in wrapper
    raise exp
  File "/usr/local/Ascend/ascend-toolkit/latest/python/site-packages/tbe/common/repository_manager/route.py", line 62, in wrapper
    func(*args, **kwargs)
  File "/usr/local/Ascend/ascend-toolkit/latest/python/site-packages/tbe/common/repository_manager/route.py", line 62, in wrapper
    func(*args, **kwargs)
  File "/usr/local/Ascend/ascend-toolkit/latest/python/site-packages/tbe/common/repository_manager/route.py", line 62, in wrapper
    func(*args, **kwargs)
  File "/usr/local/Ascend/ascend-toolkit/latest/python/site-packages/tbe/common/repository_manager/route.py", line 262, in task_distribute
    key, func_name, detail = resource_proxy[TASK_QUEUE].get()
  File "/usr/local/Ascend/ascend-toolkit/latest/python/site-packages/tbe/common/repository_manager/route.py", line 62, in wrapper
    func(*args, **kwargs)
  File "/usr/local/Ascend/ascend-toolkit/latest/python/site-packages/tbe/common/repository_manager/route.py", line 62, in wrapper
    func(*args, **kwargs)
  File "/usr/local/Ascend/ascend-toolkit/latest/python/site-packages/tbe/common/repository_manager/route.py", line 62, in wrapper
    func(*args, **kwargs)
  File "/usr/local/Ascend/ascend-toolkit/latest/python/site-packages/tbe/common/repository_manager/route.py", line 262, in task_distribute
    key, func_name, detail = resource_proxy[TASK_QUEUE].get()
  File "/usr/local/Ascend/ascend-toolkit/latest/python/site-packages/tbe/common/repository_manager/route.py", line 262, in task_distribute
    key, func_name, detail = resource_proxy[TASK_QUEUE].get()
  File "/usr/local/Ascend/ascend-toolkit/latest/python/site-packages/tbe/common/repository_manager/route.py", line 262, in task_distribute
    key, func_name, detail = resource_proxy[TASK_QUEUE].get()
  File "/usr/local/Ascend/ascend-toolkit/latest/python/site-packages/tbe/common/repository_manager/route.py", line 262, in task_distribute
    key, func_name, detail = resource_proxy[TASK_QUEUE].get()
  File "<string>", line 2, in get
  File "/usr/local/Ascend/ascend-toolkit/latest/python/site-packages/tbe/common/repository_manager/route.py", line 262, in task_distribute
    key, func_name, detail = resource_proxy[TASK_QUEUE].get()
  File "/usr/local/Ascend/ascend-toolkit/latest/python/site-packages/tbe/common/repository_manager/route.py", line 262, in task_distribute
    key, func_name, detail = resource_proxy[TASK_QUEUE].get()
  File "<string>", line 2, in get
  File "/usr/local/Ascend/ascend-toolkit/latest/python/site-packages/tbe/common/repository_manager/route.py", line 262, in task_distribute
    key, func_name, detail = resource_proxy[TASK_QUEUE].get()
  File "<string>", line 2, in get
  File "<string>", line 2, in get
  File "<string>", line 2, in get
  File "/root/miniconda3/envs/trajcrafter/lib/python3.10/multiprocessing/managers.py", line 818, in _callmethod
    kind, result = conn.recv()
  File "<string>", line 2, in get
  File "/root/miniconda3/envs/trajcrafter/lib/python3.10/multiprocessing/managers.py", line 818, in _callmethod
    kind, result = conn.recv()
  File "/root/miniconda3/envs/trajcrafter/lib/python3.10/multiprocessing/managers.py", line 818, in _callmethod
    kind, result = conn.recv()
  File "/root/miniconda3/envs/trajcrafter/lib/python3.10/multiprocessing/managers.py", line 818, in _callmethod
    kind, result = conn.recv()
  File "<string>", line 2, in get
  File "<string>", line 2, in get
  File "/root/miniconda3/envs/trajcrafter/lib/python3.10/multiprocessing/connection.py", line 250, in recv
    buf = self._recv_bytes()
  File "/root/miniconda3/envs/trajcrafter/lib/python3.10/multiprocessing/managers.py", line 818, in _callmethod
    kind, result = conn.recv()
  File "/root/miniconda3/envs/trajcrafter/lib/python3.10/multiprocessing/managers.py", line 818, in _callmethod
    kind, result = conn.recv()
  File "/root/miniconda3/envs/trajcrafter/lib/python3.10/multiprocessing/connection.py", line 250, in recv
    buf = self._recv_bytes()
  File "/root/miniconda3/envs/trajcrafter/lib/python3.10/multiprocessing/connection.py", line 250, in recv
    buf = self._recv_bytes()
  File "/root/miniconda3/envs/trajcrafter/lib/python3.10/multiprocessing/connection.py", line 250, in recv
    buf = self._recv_bytes()
  File "/root/miniconda3/envs/trajcrafter/lib/python3.10/multiprocessing/managers.py", line 818, in _callmethod
    kind, result = conn.recv()
  File "/root/miniconda3/envs/trajcrafter/lib/python3.10/multiprocessing/managers.py", line 818, in _callmethod
    kind, result = conn.recv()
  File "/root/miniconda3/envs/trajcrafter/lib/python3.10/multiprocessing/connection.py", line 414, in _recv_bytes
    buf = self._recv(4)
  File "/root/miniconda3/envs/trajcrafter/lib/python3.10/multiprocessing/connection.py", line 250, in recv
    buf = self._recv_bytes()
  File "/root/miniconda3/envs/trajcrafter/lib/python3.10/multiprocessing/connection.py", line 250, in recv
    buf = self._recv_bytes()
  File "/root/miniconda3/envs/trajcrafter/lib/python3.10/multiprocessing/connection.py", line 414, in _recv_bytes
    buf = self._recv(4)
  File "/root/miniconda3/envs/trajcrafter/lib/python3.10/multiprocessing/connection.py", line 414, in _recv_bytes
    buf = self._recv(4)
  File "/root/miniconda3/envs/trajcrafter/lib/python3.10/multiprocessing/connection.py", line 414, in _recv_bytes
    buf = self._recv(4)
  File "/root/miniconda3/envs/trajcrafter/lib/python3.10/multiprocessing/connection.py", line 250, in recv
    buf = self._recv_bytes()
  File "/root/miniconda3/envs/trajcrafter/lib/python3.10/multiprocessing/connection.py", line 250, in recv
    buf = self._recv_bytes()
  File "/root/miniconda3/envs/trajcrafter/lib/python3.10/multiprocessing/connection.py", line 383, in _recv
    raise EOFError
  File "/root/miniconda3/envs/trajcrafter/lib/python3.10/multiprocessing/connection.py", line 414, in _recv_bytes
    buf = self._recv(4)
  File "/root/miniconda3/envs/trajcrafter/lib/python3.10/multiprocessing/connection.py", line 414, in _recv_bytes
    buf = self._recv(4)
  File "/root/miniconda3/envs/trajcrafter/lib/python3.10/multiprocessing/connection.py", line 383, in _recv
    raise EOFError
  File "/root/miniconda3/envs/trajcrafter/lib/python3.10/multiprocessing/connection.py", line 383, in _recv
    raise EOFError
  File "/root/miniconda3/envs/trajcrafter/lib/python3.10/multiprocessing/connection.py", line 383, in _recv
    raise EOFError
  File "/root/miniconda3/envs/trajcrafter/lib/python3.10/multiprocessing/connection.py", line 414, in _recv_bytes
    buf = self._recv(4)
  File "/root/miniconda3/envs/trajcrafter/lib/python3.10/multiprocessing/connection.py", line 414, in _recv_bytes
    buf = self._recv(4)
  File "/root/miniconda3/envs/trajcrafter/lib/python3.10/multiprocessing/connection.py", line 383, in _recv
    raise EOFError
EOFError
  File "/root/miniconda3/envs/trajcrafter/lib/python3.10/multiprocessing/connection.py", line 383, in _recv
    raise EOFError
  File "/root/miniconda3/envs/trajcrafter/lib/python3.10/multiprocessing/connection.py", line 383, in _recv
    raise EOFError
  File "/root/miniconda3/envs/trajcrafter/lib/python3.10/multiprocessing/connection.py", line 383, in _recv
    raise EOFError
EOFError
EOFError
EOFError
EOFError
EOFError
EOFError
EOFError
/root/miniconda3/envs/trajcrafter/lib/python3.10/multiprocessing/resource_tracker.py:224: UserWarning: resource_tracker: There appear to be 30 leaked semaphore objects to clean up at shutdown
  warnings.warn('resource_tracker: There appear to be %d '

## 评论 (1)

### yunyiyun · 2025-08-27

看下plog日志是否报错，如果没有报错，可以看下是否coredump
