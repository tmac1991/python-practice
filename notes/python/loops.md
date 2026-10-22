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

- `while True`: A loop that continues executing indefinitely because its condition is always `True`.
- `break`: Immediately exits the nearest enclosing loop. In our menu, it runs when the user selects option `"4"`.
- Why our menu uses both: `while True` allows the user to make multiple selections without restarting the program. `break` provides a way to exit the loop when the user is finished.

## Counting Items That Match a Condition

relevant_count = 0

for article in fresh_articles:
    if article["score"] > 0:
        relevant_count += 1

- Start the counter at 0
- Loop through the items
- Check a condition
- Increase the counter when the condition is true

IMPORTANT:
Code inside a loop runs each iteration.
Code outside the loop runs after it finishes.