source: https://github.com/vllm-project/guidellm/commit/84a0eb73b07dee22304dacd2c5474ef79cbd0ac0

|
`2` | `2` |
|
`3` | `3` | GuideLLM is designed to evaluate and optimize large language model (LLM) deployments by simulating real-world inference workloads. The architecture is modular, enabling flexibility and scalability. Below is an overview of the core components and their interactions.
|
`4` | `4` |
|
`5` |
| `-```` |
`6` |
| `-`+------------------+ +------------------+ +------------------+ |
`7` |
| `-`| DatasetCreator | ---> | RequestLoader | ---> | Scheduler | |
`8` |
| `-`+------------------+ +------------------+ +------------------+ |
`9` |
| `-` / | \ |
`10` |
| `-` / | \ |
`11` |
| `-` / | \ |
`12` |
| `-` v v v |
`13` |
| `-` +------------------+ +------------------+ |
`14` |
| `-` | RequestsWorker | | RequestsWorker | |
`15` |
| `-` +------------------+ +------------------+ |
`16` |
| `-` | | |
`17` |
| `-` v v |
`18` |
| `-` +------------------+ +------------------+ |
`19` |
| `-` | Backend | | Backend | |
`20` |
| `-` +------------------+ +------------------+ |
`21` |
| `-` | | |
`22` |
| `-` v v |
`23` |
| `-` +---------------------------------------+ |
`24` |
| `-` | BenchmarkAggregator | |
`25` |
| `-` +---------------------------------------+ |
`26` |
| `-` | |
`27` |
| `-` v |
`28` |
| `-` +------------------+ |
`29` |
| `-` | Benchmarker | |
`30` |
| `-` +------------------+ |
| `5` | `+````mermaid |
| `6` | `+`flowchart BT |
| `7` | `+` subgraph benchmark [benchmark] |
| `8` | `+` direction TB |
| `9` | `+` BM[Benchmarker] |
| `10` | `+` PF[profiles] |
| `11` | `+` AC[accumulator] |
| `12` | `+` OT[outputs] |
| `13` | `+` PF -->|"strategy + constraints"| BM |
| `14` | `+` BM -->|"compiled benchmark"| PF |
| `15` | `+` BM -->|"request updates"| AC |
| `16` | `+` AC -->|"report"| OT |
| `17` | `+` end |
| `18` | `+`
|
| `19` | `+` subgraph pipeline [" "] |
| `20` | `+` direction LR |
| `21` | `+` EXT_DS(["Datasets (external)"]) |
| `22` | `+` subgraph data [data] |
| `23` | `+` direction TB |
| `24` | `+` LD[loaders] |
| `25` | `+` subgraph datagen [" "] |
| `26` | `+` direction TB |
| `27` | `+` DS[deserializers] |
| `28` | `+` CM[column-mapper] |
| `29` | `+` PP[preprocessors] |
| `30` | `+` FZ[finalizers] |
| `31` | `+` DS --> CM --> PP --> |"N"| PP --> FZ |
| `32` | `+` end |
| `33` | `+` datagen --> LD |
| `34` | `+` end |
| `35` | `+`
|
| `36` | `+` subgraph scheduler [scheduler] |
| `37` | `+` direction TB |
| `38` | `+` SC[Scheduler] |
| `39` | `+` WG[worker_group] |
| `40` | `+` CT[constraints] |
| `41` | `+` ST[strategies] |
| `42` | `+` WK[worker] |
| `43` | `+` SC <--> |"1..N"| WG |
| `44` | `+` WG -.->|"manages"| ST |
| `45` | `+` WG -.->|"manages"| CT |
| `46` | `+` WG <-->|"1..N"| WK |
| `47` | `+` ST --> WK |
| `48` | `+` CT --> WK |
| `49` | `+` end |
| `50` | `+`
|
| `51` | `+` subgraph backends [backends] |
| `52` | `+` BE[Backend] |
| `53` | `+` end |
| `54` | `+` EXT_LLM(["LLM (external)"]) |
| `55` | `+`
|
| `56` | `+` EXT_DS --> data --> |"iter(conversations)"| scheduler --> |"request data"| backends <--> |"request\nresponse"| EXT_LLM |
| `57` | `+` backends --> |"request updates"| scheduler |
| `58` | `+` end |
| `59` | `+`
|
| `60` | `+` benchmark -.->|"manages"| pipeline |
| `61` | `+` pipeline --> |"request updates"| benchmark |
| `62` | `+`
|
| `63` | `+`classDef configurable fill:#D6E6FD,stroke:#498CF5,stroke-width:2px,color:#1a1a1a |
| `64` | `+`class LD,DS,CM,PP,FZ,PF,CT,OT,BE configurable |
`31` | `65` | ```
|
`32` | `66` |
|
`33` | `67` | ## Core Components
|
|
## 0 commit comments