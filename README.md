# crac-protobuf
Library for gRPC contracts and Servicer

# Install Dependencies and Configure environment

We are using Poetry as a dependency management and packaging
Go to https://python-poetry.org/ and install it

```
poetry shell
poetry install
```

# Generate boilerplates

```
$ python generate_proto_code.py
```

# Compile and create package

```
$ poetry build
```
