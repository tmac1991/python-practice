# Python basics — Lessons 1–2

## Variables and types
A **variable** is a name pointing to a value: `artist = "Gucci Mane"`. Common types: `str` (text), `int` (whole number), `float` (decimal), `bool` (`True` or `False`). Use `type(x)` to inspect a value.

```python
artist = "Gucci Mane"
rating = 9
print(f"{artist}: {rating}/10")
```

## Input and normalization
`input()` returns text (`str`), even if the user types 9. Use `int()` when numerical comparison is needed; wrap conversion with error handling if users can enter nonsense.

```python
artist = input("Artist: ").strip().lower()
rating = int(input("Rating: "))
```

`strip()` removes *leading and trailing* whitespace; `lower()` makes letters lowercase. `f"...{variable}..."` inserts a value into a string.

## Arithmetic
`+` add; `-` subtract; `*` multiply; `/` divide (returns float); `//` floor divide; `%` remainder.

## Recall
- Can you explain why `"10"` and `10` behave differently?
- What's the difference between the label `artist` and the value `"Gucci Mane"`?
