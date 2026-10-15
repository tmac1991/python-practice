# Git and GitHub — practical commands

Git is local version control; GitHub hosts the remote repository. Bash is the Linux shell used to run Git commands; VS Code shows Git status decorations.

```bash
git status
git add lesson_06/mixtape_manager.py
git commit -m "Lesson 6: improve mixtape manager"
git push
```

- `git status`: inspect changes and branch.
- `git add`: stage selected files for the next commit.
- `git commit`: record a local version with a message.
- `git push`: publish your commits to GitHub.
- `git fetch`: check remote history without altering working files.
- `git pull`: retrieve and integrate remote changes.

VS Code Explorer: `M` = modified tracked file; `U` = untracked new file; `A` = added/staged (depending view); `D` = deleted.

**Avoid `git add .` when you only want specific files.** Don't commit `.venv`, secrets, or API keys. Use `.gitignore` appropriately.

## Recall
Does `git commit` upload the change to GitHub? No: `git push` does.
