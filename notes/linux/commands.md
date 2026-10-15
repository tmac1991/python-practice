# WSL / Ubuntu / Bash — practical commands

Repository: `~/projects/python-practice`. Virtual environment: `.venv`.

```bash
cd ~/projects/python-practice
source .venv/bin/activate
cd lesson_06
pwd
ls
python mixtape_manager.py
cd ..
```

- `pwd`: current working directory.
- `ls`: show files.
- `cd folder`: enter a folder.
- `cd ..`: go up one folder.
- `mkdir -p notes`: make a directory if missing.
- `clear` or `Ctrl+L`: clear terminal view; does not delete files.
- `cat mixtapes.json`: print a file's contents.
- `cp source dest`: copy; `mv old new`: move/rename; `rm`: delete (use with care).

**Linux path separators** use `/`, unlike Windows-style `\`. `(.venv)` at the prompt indicates an activated Python virtual environment.

## Recall
Why did a JSON file go missing even though it existed? Relative paths depend on the current terminal directory. #review
