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

## Python Syntax Cheat Sheet — (), [], {}

### Parentheses () — CALL functions and methods

print("Hello")
len(articles)
articles.append(article_data)
feed.get("status")

### Square Brackets [] — ACCESS items

article["link"]      # Dictionary key
article["title"]     # Dictionary key
articles[0]          # First list item
articles[:5]         # First 5 list items

### Curly Braces {} — CREATE dictionaries and sets

article = {
    "title": "Python News",
    "link": "https://example.com"
}

### Common Mistakes

❌ article("link")      # Tries to call a dictionary
✅ article["link"]      # Accesses dictionary value

❌ articles.append{article}
✅ articles.append(article)

❌ feed.get["status"]
✅ feed.get("status")

### Memory Trick

() = DO something (call)
[] = GET something (access)
{} = BUILD something (dictionary/set)

REMEMBER:
A dictionary is accessed with [].
A method is called with ().

These both work, but behave differently when a key is missing:
article["link"]       # Raises KeyError if missing
article.get("link")    # Returns None if missing

### Dictionary Keys — Handling Missing Values

| Code | Missing Key Result |
|---|---|
| `article["published"]` | ❌ Raises `KeyError` |
| `article.get("published")` | Returns `None` |
| `article.get("published", "Unknown")` | ✅ Returns `"Unknown"` |

**Memory Trick:**

`.get()` is like asking politely. If the key isn't there,
Python gives you the fallback instead of throwing a fit. 😂

**Remember:**
- `[]` accesses dictionary keys directly.
- `.get()` safely retrieves values.
- The second argument to `.get()` is the fallback value.

## Lists Containing Dictionaries

### Accessing values

fresh_articles[0]["score"]

Breakdown:
- fresh_articles = List of article dictionaries
- [0] = First dictionary in the list
- ["score"] = Value stored under the "score" key

### Common Mistakes

❌ fresh_articles[0].article["score"]
✅ fresh_articles[0]["score"]

❌ article[score]
✅ article["score"]

### Adding or Updating Values

article["score"] = score

- "score" = Dictionary key (string)
- score = Variable containing a number

### Memory Trick

List → Item → Key → Value

[] = ACCESS
() = CALL
{} = CREATE

### Safety Check

if fresh_articles:
    print(fresh_articles[0]["score"])

Always check that a list contains items before using [0].

## Sorting Lists

### Sorting numbers

scores = [3, 1, 5, 2]

scores.sort()
# [1, 2, 3, 5]

scores.sort(reverse=True)
# [5, 3, 2, 1]

### Sorting dictionaries by a value

def get_score(article):
    return article["score"]

fresh_articles.sort(key=get_score, reverse=True)

- .sort() changes the original list
- key=get_score tells Python which value to sort by
- reverse=True puts the highest values first
- get_score has no () because we're passing the function itself

### Lists of Dictionaries

fresh_articles[0]["score"]

- [0] selects the first dictionary
- ["score"] accesses its score

### Checking Lists

if fresh_articles:
    # List contains something

if not fresh_articles:
    # List is empty

if article in fresh_articles:
    # A specific article exists in the list