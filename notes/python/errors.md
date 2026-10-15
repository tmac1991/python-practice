# Exceptions and error handling — Lessons 5 & 6

`try` attempts risky code. `except SomeError` handles that specific exception. `else` on a `try` runs only when the `try` finishes without an exception. `raise` inside a handler re-raises the current exception.

```python
try:
    with open("mixtapes.json", "r") as file:
        mixtapes = json.load(file)
except FileNotFoundError:
    mixtapes = []
except json.JSONDecodeError:
    print("SWOUP! Saved JSON is corrupt; do NOT overwrite it.")
    raise
```

**Common exceptions:** `ValueError` (e.g. `int("SWOUP")`), `FileNotFoundError`, `json.JSONDecodeError`, `TypeError` (e.g. comparing a string rating to an integer).

## Safety rule
For a missing file, an empty collection may be appropriate. For a *corrupt* file, don't silently set `mixtapes = []` and overwrite potentially recoverable information. `raise` is the emergency brake before the cliff.

## Recall #review
What happens if you catch `JSONDecodeError` and print a message but never assign `mixtapes`, yet the program later calls `mixtapes.append(...)`?
