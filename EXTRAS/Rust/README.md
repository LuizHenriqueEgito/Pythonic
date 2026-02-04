# Iniciando um projeto
```bash
cargo init nome_do_projeto
```

# Primeiros passos
1. Abra o arquivo `Cargo.toml` e adicione em dependencias:
```toml
[dependencies]
pyo3 = {version="0.21", features=["extension-module"]}
```
2. Adicione também a lib no arquivo `Cargo.toml`:
```toml
[lib]
name = "rusty_snek"  # Deve ser o mesmo nome do seu cargo init ___
crate-type = ["cdylib"]  # TODO: Pra que serve esse cara?
```
3. Crie na pasta `src` o arquivo `lib.rs` e coloque nele todo seu código.
4. Use a lib pyo3
```rust
use pyo3::prelude::*;
```
5. Após criar sua lógica crie o arquivo `pyproject.toml` e adicione as bibliotecas:
```toml
[build-system]
requires = {"maturin>=1.0,<2.0"}
build-backend = "maturin"

[project]
name = "rusty-snek"
version = "0.1.0"
requires-python = ">=3.7"

```
6. Ao final compile tudo com:
```bash
maturin develop
```