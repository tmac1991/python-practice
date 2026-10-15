# Functions — Lesson 4

`def` defines reusable behavior. A **parameter** is a named input; an **argument** is the value passed when calling. `return` sends a value back to the caller. `print()` only displays information.

```python
def recommend_model(task):
    if task == "code":
        return "Coding-focused model"
    return "General-purpose model"

recommendation = recommend_model("code")
print(recommendation)
```

## Useful distinction
`result = some_function()` only stores a useful value if the function returns one. A `return` also ends that function call.

## Recall
- What is the difference between `return "hello"` and `print("hello")`?
- Why put repeated logic in a function?
