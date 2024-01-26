# quiet

Suppress the output of any Python function.

## Usage

```python
def add(x: int, y: int) -> int:
    """Add two numbers."""

    z = x + y

    print(f'{x} + {y} = {z}')

    return z
```

```python
>>> add(1, 2)  # Returns 3.
1 + 2 = 3
```

```python
>>> from quiet import quiet

>>> quiet(add)(1, 2)  # Returns 3.
```
