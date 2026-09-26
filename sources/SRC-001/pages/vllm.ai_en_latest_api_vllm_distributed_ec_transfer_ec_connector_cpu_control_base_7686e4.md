source: https://docs.vllm.ai/en/latest/api/vllm/distributed/ec_transfer/ec_connector/cpu/control/base/
lastmod: 2026-09-24

Bases: [ABC](https://docs.python.org/3/library/abc.html#abc.ABC)


Bidirectional message channel to a single remote peer.

All I/O is non-blocking: send enqueues without blocking; recv drains all buffered inbound messages since the last call.

Methods:

-
[close](#vllm.distributed.ec_transfer.ec_connector.cpu.control.base.ControlConnection.close)

– Release all resources. Idempotent.

-
[mark_dead](#vllm.distributed.ec_transfer.ec_connector.cpu.control.base.ControlConnection.mark_dead)

– Signal that the peer disconnected. Sets alive to False.

-
[recv](#vllm.distributed.ec_transfer.ec_connector.cpu.control.base.ControlConnection.recv)

– Drain and return all buffered inbound messages.

-
[send](#vllm.distributed.ec_transfer.ec_connector.cpu.control.base.ControlConnection.send)

– Enqueue msg for delivery. Must not block.


Attributes:

-
[alive](#vllm.distributed.ec_transfer.ec_connector.cpu.control.base.ControlConnection.alive)

([bool](https://docs.python.org/3/builtins/functions.html#bool)

) – True if the connection is still usable.


## Source code in `vllm/distributed/ec_transfer/ec_connector/cpu/control/base.py`


| class ControlConnection(ABC):
"""Bidirectional message channel to a single remote peer.
All I/O is non-blocking: send enqueues without blocking; recv drains
all buffered inbound messages since the last call.
"""
@property
@abstractmethod
def alive(self) -> bool:
"""True if the connection is still usable."""
@abstractmethod
def send(self, msg: bytes) -> None:
"""Enqueue msg for delivery. Must not block."""
@abstractmethod
def recv(self) -> list[bytes]:
"""Drain and return all buffered inbound messages."""
@abstractmethod
def mark_dead(self) -> None:
"""Signal that the peer disconnected. Sets alive to False."""
@abstractmethod
def close(self) -> None:
"""Release all resources. Idempotent."""
|

###

`alive`

`abstractmethod`

`property`


True if the connection is still usable.

###

`close()`

`abstractmethod`


Release all resources. Idempotent.

## Source code in `vllm/distributed/ec_transfer/ec_connector/cpu/control/base.py`


| @abstractmethod
def close(self) -> None:
"""Release all resources. Idempotent."""
|

###

`mark_dead()`

`abstractmethod`


Signal that the peer disconnected. Sets alive to False.

## Source code in `vllm/distributed/ec_transfer/ec_connector/cpu/control/base.py`


| @abstractmethod
def mark_dead(self) -> None:
"""Signal that the peer disconnected. Sets alive to False."""
|

###

`recv()`

`abstractmethod`


Drain and return all buffered inbound messages.

## Source code in `vllm/distributed/ec_transfer/ec_connector/cpu/control/base.py`


| @abstractmethod
def recv(self) -> list[bytes]:
"""Drain and return all buffered inbound messages."""
|

###

`send(msg)`

`abstractmethod`


Enqueue msg for delivery. Must not block.

## Source code in `vllm/distributed/ec_transfer/ec_connector/cpu/control/base.py`


| @abstractmethod
def send(self, msg: bytes) -> None:
"""Enqueue msg for delivery. Must not block."""
|