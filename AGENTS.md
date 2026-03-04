# AGENTS.md - Development Guide for CRAC Protobuf

This document provides comprehensive guidelines for any agent or developer working on the CRAC Protobuf codebase. It is designed to be the single point of truth for contract definitions and code generation.

## 1. Project Overview
CRAC Protobuf is the core library containing the gRPC service definitions and message contracts for the entire CRAC ecosystem. It ensures that the Server, Client, and Cloud components speak the same language.

### Main Technologies
- **Language:** Python 3.9+
- **Protocol Buffers:** [Proto3](https://developers.google.com/protocol-buffers).
- **gRPC:** Python code generation via `grpcio-tools`.
- **Dependency Management:** [uv](https://github.com/astral-sh/uv) (Migrated from Poetry).

---

## 2. Commands (using uv)

### Installation
```bash
# Sync dependencies
uv sync
```

### Code Generation
Run the generation script after any change to the `.proto` files:
```bash
# This generates *_pb2.py and *_pb2_grpc.py in the crac_protobuf/ folder
uv run python generate_proto_code.py
```

---

## 3. Project Structure

```
crac-protobuf/
├── interfaces/             # SOURCE: .proto files
│   ├── roof.proto
│   ├── telescope.proto
│   ├── ...
│   └── geographic.proto
├── crac_protobuf/          # GENERATED: Python gRPC modules (DO NOT EDIT MANUALLY)
├── generate_proto_code.py  # Automation script for protoc
└── pyproject.toml          # Project metadata and dependencies
```

---

## 4. Development Standards & Best Practices

### Contract-First Development 🔴 MANDATORY
All communication changes MUST start here.
1. Modify the relevant `.proto` file in `interfaces/`.
2. Run `generate_proto_code.py`.
3. Test the generated code locally using the "editable" path in the Server or Client.

### Backward Compatibility
- **Never delete or renumber fields**: Use `reserved` if a field is no longer needed.
- **Consistency**: Follow the existing naming conventions (e.g., `TelescopeStatus`, `EquatorialCoords`).
- **GUI Standardization**: Aim for `repeated ButtonGui buttons = N;` in responses to support flexible UIs (see `REVISION_GUIDE.md`).

### Generation Script
- The `generate_proto_code.py` script uses absolute paths and `sys.executable` to ensure it works across different environments and OSs.

---

## 5. Deployment & Versioning
---

## 6. Agent Autonomy & Safeguards

To ensure efficiency and safety, the following rules apply to AI agents working on this project:

- **Autonomy**: Once a high-level plan is approved by the user, the agent is authorized to proceed through **Plan -> Act -> Validate** cycles without per-step confirmation.
- **Git User Email**: Always verify that `git config user.email` is set to `alkcxy@gmail.com` before making any commit.
- **No Remote Push**: Agents are **strictly forbidden** from executing `git push`. This action is reserved for the human user.
- **Mandatory Testing**: A commit can only be made if all relevant unit tests pass. 
- **Autonomous Fixes**: If tests fail after a modification, the agent should attempt up to **3 iterations** of autonomous fixing before stopping to consult the user.
- **Atomic Commits**: Prefer small, descriptive commits over large "catch-all" updates.
- **Strict Scope**: I am strictly forbidden from modifying any files or directories outside the explicitly authorized project directories without confirmation. I must NEVER delete an entire directory outside the work projects.
