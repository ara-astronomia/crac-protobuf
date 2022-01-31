# Install Dependencies and Configure environment

```
$ python -m venv crac
$ source crac/bin/activate  # Linux/macOS only
(crac) $ python -m pip install -r requirements.txt
(crac) $ python -m pip install --upgrade build
```

# Generate boilerplates

```
(crac) $ python -m pip install -e ./
```

# Compile and create package

```
(crac) $ python -m build
```