# crac-protobuf

Python gRPC/protobuf contracts for the CRAC astronomical observatory ecosystem.
Consumed by crac-server, crac-client, and crac-cloud as the shared communication layer.

## Prerequisites

- Python ≥ 3.9
- [uv](https://github.com/astral-sh/uv)

## Install

```bash
uv sync
```

## Modifying contracts

1. Edit or add `.proto` files in `interfaces/`
2. Regenerate the Python bindings:
   ```bash
   uv run python generate_proto_code.py
   ```
3. Bump the version in `pyproject.toml`
4. Commit both the `.proto` source and the regenerated `_pb2*.py` files

> **Never delete or renumber proto fields** — use `reserved` instead.

## Build

```bash
uv build
```

Releases are published to PyPI automatically on GitHub release creation.
