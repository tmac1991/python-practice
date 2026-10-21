# Files and JSON — Lessons 5 & 6

## File modes
- `"r"`: read existing file; missing file raises `FileNotFoundError`.
- `"w"`: create or **overwrite immediately**. Be careful.
- `"a"`: append to the end; use `"\n"` to start a new line.
- `with open(...) as file:` automatically closes the file afterward.

```python
with open("lyrics.txt", "a") as file:
    file.write("\nSWOUP!")
```

## JSON
Use `import json`. **`json.dump(data, file, indent=4)` saves** Python data to a JSON file. **`json.load(file)` loads** JSON into Python data. Python Boolean `True` becomes JSON `true`.

```python
import json
with open("mixtapes.json", "r") as file:
    mixtapes = json.load(file)
mixtapes.append({"artist": "Dirt Nasty", "title": "Example", "rating": 8})
with open("mixtapes.json", "w") as file:
    json.dump(mixtapes, file, indent=4)
```

## Why order matters
Load old albums **before** appending a new one. Otherwise starting with `mixtapes = []` discards past entries *in memory*, and the subsequent save may replace the file with only the newest album.

## Path gotcha #review
Relative names like `"mixtapes.json"` are resolved against your terminal's **current working directory**, not necessarily the script's directory. Run `pwd` to check where you are. Later, learn `pathlib` for script-relative paths.

### Loading JSON Before a Menu Loop

Loading JSON before `while True` reads the saved data once when
the program starts, rather than rereading it after every menu selection.

Relative file paths are resolved from the current working directory,
not automatically from the location of the Python script.

## RSS Feeds and HTTP Requests

### RSS Feeds

RSS (Really Simple Syndication) lets programs retrieve
updates and articles from websites automatically.

Python libraries:
- feedparser: Parses RSS and Atom feeds.
- requests: Downloads web content using HTTP.

Example:
- requests.get(url, timeout=10) retrieves a feed.
- feedparser.parse(response.content) parses the downloaded data.
- feed.entries contains the articles.
- article.title retrieves an article's headline.

### HTTP Requests and Error Handling

Common HTTP status codes:
- 200: Success
- 404: Resource not found
- 429: Too many requests
- 500: Internal server error
- 502: Bad gateway

Error handling:
- try: Runs code that might fail.
- except: Catches specific exceptions.
- else: Runs only if no exception occurs.
- requests.exceptions.Timeout: Catches request timeouts.
- requests.exceptions.ConnectionError: Catches connection failures.

Useful checks:
- response.status_code == 200: HTTP request succeeded.
- not feed.bozo: RSS parsing succeeded.
- timeout=10: Limits how long requests waits for network activity.