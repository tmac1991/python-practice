# Our actual bugs and what fixed them

- **Wrong working directory:** `FileNotFoundError` on JSON. Check `pwd`, `ls`, and whether the terminal was in `lesson_06`.
- **Old code ran instead:** Save in VS Code with `Ctrl+S` before rerunning.
- **Accidentally commented-out input code:** VS Code `Ctrl+/` toggles comments for selected lines.
- **Confusing labels and values:** `"artist": artist` uses a key (quoted) and a variable (unquoted).
- **Mixing `"10"` and `10`:** `input()` always returns a string until converted; rating comparisons need numeric values.
- **Missing `with`:** `with open(...) as file:` is the normal safe pattern for opening a file.
- **Unexpected loop behavior:** indentation decides whether code runs once or repeats. #review
- **Risk of overwriting corrupt JSON:** catch `json.JSONDecodeError` and re-raise rather than overwrite.
- **Git letters looked like errors:** `M` and `U` are file-status indicators, not warnings.

When you hit a new bug, record: **symptom → cause → fix → how to detect it next time**.

### Empty or Corrupted JSON Files

- Why an empty JSON file causes `JSONDecodeError`: There is no data in the JSON file to read. An empty file contains no valid JSON data for Python to decode.
- What opening a file with `"w"` does: Opens a file for writing, immediately erasing its existing contents. If the file doesn't exist, Python creates it.
- How a backup can prevent data loss: A backup preserves an earlier copy of the data, allowing recovery if the original file is accidentally overwritten, emptied, or corrupted.
