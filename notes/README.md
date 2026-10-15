# Python Academy — Study Library

Use this alongside the `lesson_06` project. No extra apps required.

## Jump to a topic
- [Python fundamentals](python/basics.md)
- [Lists & dictionaries](python/collections.md)
- [Conditions & loops](python/loops.md)
- [Functions](python/functions.md)
- [Files & JSON](python/files-json.md)
- [Error handling](python/errors.md)
- [Git & GitHub](git/commands.md)
- [Linux & WSL](linux/commands.md)
- [Mistakes and solutions](troubleshooting/common-mistakes.md)
- [Resume the course](NEXT_SESSION.md)

## One simple routine
1. **During a lesson:** add `#review` beside a concept you want to revisit, in a topic note or session note.
2. **After the lesson:** copy `templates/session-note.md` to `sessions/YYYY-MM-DD-topic.md`; fill in only what matters.
3. **Low-energy day:** run `python scripts/review.py -r 3` from your repository root, or read one concept page.
4. **When it sticks:** change `#review` to `#done` in the relevant note.
5. **At a checkpoint:** commit the notes alongside the lesson; `git push` backs them up.

The Markdown notes are the source of truth; no second manually maintained queue. The review script finds tags wherever they appear in the topic and session notes. Don't add secrets, API keys, or private credentials to Git.

**Useful VS Code shortcuts:** `Ctrl+Shift+V` previews Markdown; `Ctrl+Shift+F` searches across files; `Ctrl+J` toggles the terminal.
