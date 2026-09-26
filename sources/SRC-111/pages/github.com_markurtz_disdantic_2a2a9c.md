source: https://github.com/markurtz/disdantic

*The missing polymorphic engine for Pydantic.*

[Documentation](https://markurtz.github.io/disdantic/) |
[Roadmap](https://github.com/markurtz/disdantic/milestones) |
[Issues](https://github.com/markurtz/disdantic/issues) |
[Discussions](https://github.com/markurtz/disdantic/discussions)

`disdantic`

is a lightweight Python toolkit designed to simplify Pydantic subclass registries, dynamic polymorphic unions, and automatic model discovery. By eliminating the manual boilerplate of maintaining union types and tracking child class imports, it allows you to build clean, extensible, and self-updating polymorphic domain models.

**Decoupled Registries:**Fully isolated subclass tracking namespaces prevent collisions between distinct model domains.**Dynamic Tagged Unions:**Automatic core schema generation dynamically routes incoming JSON payload validation based on a customizable discriminator key.**Topological Schema Rebuilding:**Dynamic subclass registrations trigger cascade schema reloading up the dependent parent MRO trees.**Automatic Discovery & Auto-Import:**Traverses folders recursively to discover and import submodules, ensuring subclasses register themselves without manual imports.**Robust Object Introspection:**Extracts slots, properties, and attributes into sanitized primitives, handling circular references and lazy loader proxies safely.**CLI Diagnostics Suite:**Scans, lists, validates compilation integrity, and exports schemas.

| Feature | Pure Pydantic v2 | Pydantic + `disdantic` |
|---|---|---|
Union Type Definitions |
Manual list (e.g., `Union[A, B, C]` ) |
Automatic tagged union via registry base class |
New Subclass Adding |
Modify parent union type and import | Register via decorator; schema cascades automatically |
Dynamic Import Scanning |
Manual `importlib` boilerplate |
Declarative packages scan via `AutoImporterMixin` |
Integrity Auditing |
Manual script validation | Programmatic and CLI-based diagnostics |
Schema Generation |
`model_json_schema()` on static types |
Command-line extraction via `disdantic schema` |

`pip install disdantic`

For advanced features like YAML serialization, install the optional package extra:

`pip install disdantic[yaml]`

```
from typing import Literal
from disdantic import PydanticClassRegistryMixin
from pydantic import BaseModel
# 1. Define a polymorphic base registry class
class Message(PydanticClassRegistryMixin):
schema_discriminator = "msg_type" # Custom tag field name
msg_type: str
# 2. Register subclass implementations dynamically
@Message.register("text")
class TextMessage(Message):
msg_type: Literal["text"] = "text"
content: str
@Message.register("image")
class ImageMessage(Message):
msg_type: Literal["image"] = "image"
url: str
caption: str | None = None
# 3. Parents automatically rebuild to accommodate new subtypes
class ChatRoom(BaseModel):
room_name: str
messages: list[Message] # Polymorphic union field
# 4. Incoming payloads validate dynamically to correct subclass types
payload = {
"room_name": "General Chat",
"messages": [
{"msg_type": "text", "content": "Hello world!"},
{"msg_type": "image", "url": "https://placehold.co/150.png", "caption": "Logo"}
]
}
room = ChatRoom.model_validate(payload)
assert isinstance(room.messages[0], TextMessage)
assert isinstance(room.messages[1], ImageMessage)
# 5. Full marshalling flow (serialization and deserialization)
room_data = room.model_dump()
# msg_type is automatically included in the serialized output!
assert room_data["messages"][0]["msg_type"] == "text"
assert room_data["messages"][1]["msg_type"] == "image"
restored_room = ChatRoom.model_validate(room_data)
assert isinstance(restored_room.messages[0], TextMessage)
assert isinstance(restored_room.messages[1], ImageMessage)
```

`src/disdantic/`

: Library package containing runtime implementations.`registry.py`

: Core`RegistryMixin`

,`PydanticClassRegistryMixin`

, and global`RegistryManager`

.`model.py`

: Abstract`ReloadableBaseModel`

enabling topological cascading rebuilds.`diagnose.py`

: Registry integrity check orchestrator and compile validation check.`introspection.py`

: Recursively maps complex objects to primitives via`InfoMixin`

.`loading.py`

: Thread-safe deferred instantiation with`LazyLoader`

and`LazyProxy`

.`settings.py`

: Centralized`Settings`

utilizing Pydantic Settings.

`tests/`

: Multi-tiered testing suite (`python/unit/`

,`python/integration/`

, and`e2e/`

).`docs/`

: Markdown files compiled using Zensical static site generator.`examples/`

: Self-contained runnable scripts demonstrating configurations.

For detailed information on configuration settings, custom handlers, CLI commands, and operational guides, visit the [Documentation Site](https://markurtz.github.io/disdantic/).

We welcome contributions! Please see [CONTRIBUTING.md](https://github.com/markurtz/disdantic/blob/main/CONTRIBUTING.md) for guidelines and [DEVELOPING.md](https://github.com/markurtz/disdantic/blob/main/DEVELOPING.md) for development setup instructions.

Ensure you adhere to our [Code of Conduct](https://github.com/markurtz/disdantic/blob/main/CODE_OF_CONDUCT.md) in all community interactions.

- For help and general questions, see
[SUPPORT.md](https://github.com/markurtz/disdantic/blob/main/SUPPORT.md). - To report a security vulnerability, please refer to our
[Security Policy](https://github.com/markurtz/disdantic/blob/main/SECURITY.md).

Licensed under the Apache License 2.0. See the [LICENSE](https://github.com/markurtz/disdantic/blob/main/LICENSE) file for details.

If you use this repository or the resulting software in your research, please cite it using the following BibTeX entry:

```
@software{disdantic,
author = {markurtz},
title = {disdantic},
year = 2026,
url = {https://github.com/markurtz/disdantic}
}
```