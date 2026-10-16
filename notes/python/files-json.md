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