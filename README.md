# Install Dependencies and Configure environment

We are using Poetry as a dependency management and packaging
Go to https://python-poetry.org/ and install it

```
poetry shell
poetry install
```

# Generate boilerplates

```
(crac) $ python generate_proto_code.py
```

# Compile and create package

```
(crac) $ python -m build
```