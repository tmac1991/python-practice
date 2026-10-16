# Conditions and loops — Lessons 2, 3, 4 & 6

## `if` / `elif` / `else`
`if` chooses a branch when a condition is true. `==` compares values; `=` assigns a value. Other comparisons: `>=`, `<=`, `>`, `<`, `!=`.

## `for` versus `while`
**`for` = play every record in the crate.** Loop through each item in a collection once per execution.
**`while True` = keep accepting new requests.** Repeat a process until you explicitly exit it.

## `break` versus `continue`
`break` leaves the nearest loop. `continue` skips the rest of the current iteration and begins the next.

```python
while True:
    choice = input("Rating or quit: ").strip().lower()
    if choice == "quit":
        break
    try:
        minimum = int(choice)
    except ValueError:
        print("That ain't a number, mane!")
        continue
    found_match = False
    for mixtape in mixtapes:
        if mixtape["rating"] >= minimum:
            print(mixtape["artist"])
            found_match = True
    if not found_match:
        print("Ain't no matches!")
```

`found_match = False` **must reset for every new search**. Its final check belongs *after* the `for` loop, but *inside* the `while` loop.

## Common snag #review
Indentation determines which code belongs to which loop. If the search loop is outside `while True`, it won't repeat each time you enter a rating.

## Recall
- Is `except` what stops the loop, or `break`?
- Does `continue` exit the loop?

### Interactive Menu Loops

- `while True`: a type of loop that continues to execute indefinitely because of the boolean True.
- `break`: responsible for ending the while loop, when the user inputs 4 in this case.
- Why a menu needs both: The lack of break leads to a menu that can't be exited. The lack of while True only allows one input.