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
