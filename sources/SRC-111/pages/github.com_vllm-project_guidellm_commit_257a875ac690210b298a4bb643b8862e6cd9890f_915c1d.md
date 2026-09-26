source: https://github.com/vllm-project/guidellm/commit/257a875ac690210b298a4bb643b8862e6cd9890f

|
| `1` | `+`name: Build Wheels |
| `2` | `+` |
| `3` | `+`on: |
| `4` | `+` workflow_call: {} |
| `5` | `+` |
| `6` | `+`jobs: |
| `7` | `+` build-wheels: |
| `8` | `+` runs-on: ${{ matrix.os }} |
| `9` | `+` strategy: |
| `10` | `+` matrix: |
| `11` | `+` os: [ubuntu-latest, macos-14] |
| `12` | `+` steps: |
| `13` | `+` - name: Checkout code |
| `14` | `+` uses: actions/checkout@3d3c42e5aac5ba805825da76410c181273ba90b1 # v7.0.1 |
| `15` | `+` with: |
| `16` | `+` fetch-depth: 0 |
| `17` | `+` - name: Install Rust toolchain |
| `18` | `+` run: | |
| `19` | `+` curl --proto '=https' --tlsv1.2 -sSf https://sh.rustup.rs | sh -s -- -y |
| `20` | `+` echo "$HOME/.cargo/bin" >> $GITHUB_PATH |
| `21` | `+` - name: Build wheels |
| `22` | `+` uses: pypa/cibuildwheel@1828c10ab37f080699c7b81cea34097c684a7074 # v4.2.0 |
| `23` | `+` env: |
| `24` | `+` CIBW_BUILD: "cp310-* cp311-* cp312-* cp313-*" |
| `25` | `+` CIBW_SKIP: "*-musllinux_* *-win32 *-manylinux_i686" |
| `26` | `+` CIBW_ARCHS_LINUX: "x86_64 aarch64" |
| `27` | `+` CIBW_ARCHS_MACOS: "arm64" |
| `28` | `+` CIBW_BEFORE_ALL_LINUX: > |
| `29` | `+` curl --proto '=https' --tlsv1.2 -sSf https://sh.rustup.rs | sh -s -- -y |
| `30` | `+` CIBW_ENVIRONMENT_LINUX: "PATH=$HOME/.cargo/bin:$PATH" |
| `31` | `+` - name: Upload wheels |
| `32` | `+` uses: actions/upload-artifact@043fb46d1a93c77aae656e7c1c64a875d1fc6a0a # v7.0.1 |
| `33` | `+` with: |
| `34` | `+` name: wheels-${{ matrix.os }} |
| `35` | `+` path: ./wheelhouse/*.whl |
| `36` | `+` |
| `37` | `+` build-sdist: |
| `38` | `+` runs-on: ubuntu-latest |
| `39` | `+` steps: |
| `40` | `+` - name: Checkout code |
| `41` | `+` uses: actions/checkout@3d3c42e5aac5ba805825da76410c181273ba90b1 # v7.0.1 |
| `42` | `+` with: |
| `43` | `+` fetch-depth: 0 |
| `44` | `+` - name: Setup Python with UV |
| `45` | `+` uses: ./.github/actions/python-uv |
| `46` | `+` with: |
| `47` | `+` python-version: "3.10" |
| `48` | `+` - name: Install Rust toolchain |
| `49` | `+` run: | |
| `50` | `+` curl --proto '=https' --tlsv1.2 -sSf https://sh.rustup.rs | sh -s -- -y |
| `51` | `+` echo "$HOME/.cargo/bin" >> $GITHUB_PATH |
| `52` | `+` - name: Install dependencies |
| `53` | `+` run: | |
| `54` | `+` uv pip install --system tox tox-uv |
| `55` | `+` - name: Build sdist |
| `56` | `+` run: | |
| `57` | `+` tox -e build |
| `58` | `+` - name: Upload sdist |
| `59` | `+` uses: actions/upload-artifact@043fb46d1a93c77aae656e7c1c64a875d1fc6a0a # v7.0.1 |
| `60` | `+` with: |
| `61` | `+` name: sdist |
| `62` | `+` path: dist/*.tar.gz |
## 0 commit comments