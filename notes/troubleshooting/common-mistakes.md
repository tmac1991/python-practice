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
