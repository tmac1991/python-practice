# Lists and dictionaries — Lessons 3 & 6

## List — `[]`
An ordered collection, accessed by zero-based position: `artists[0]`. Use a list to hold many albums. `.append(x)` adds one item to the end. `len(artists)` counts items.

## Dictionary — `{}`
Stores **key: value** pairs. Use when an item has named fields like artist/title/rating.

```python
artist = "The Diplomats"     # a variable
album = {"artist": artist, "title": "Diplomatic Immunity", "rating": 9}
mixtapes = []
mixtapes.append(album)
print(mixtapes[0]["artist"])
```

- `"artist"` (quoted, on the left) is a dictionary key.
- `artist` (unquoted, on the right) is a variable containing user input.
- Rating must be numeric (`9`, not `"9"`) to compare with another integer.

## Lists of dictionaries
`for mixtape in mixtapes:` gives you each dictionary, one at a time. `mixtape["rating"]` accesses its rating.

## Recall
- Why does `print(mixtapes)` show `[]` around dictionaries?
- What happens if a rating is the string `"10"` and you compare it to integer `9` with `>=`?

### Iterating Through Lists of Dictionaries

- A list of dictionaries is: multiple dictionaries in the same collection. 
- `for mixtape in mixtapes:` means: mixtape is a temporary variable, mixtapes is the list where our json is stored. go through the mixtapes list one item at a time, calling each item mixtape
- `mixtape["artist"]` retrieves: the value stored under the "artist" key in that mixtape’s dictionary.
- An f-string is useful here because: An f-string is useful here because it allows us to insert values retrieved from dictionaries into a readable, formatted string.

### Empty Collections and Truthiness

- An empty list evaluates to: `False` in a condition (it is "falsy").
- A nonempty list evaluates to: `True` in a condition (it is "truthy").
- `if not mixtapes:` means: run the indented code when `mixtapes` is empty.
- Why checking for an empty list is useful: it lets a program handle the no-data case, such as telling the user there are no mixtapes to display instead of trying to process or display any.