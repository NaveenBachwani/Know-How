# Everyday Git — quick reference

A compact, opinionated cheat-sheet for daily Git tasks. These commands are safe starting points for beginners — read the short explanation next to each command to avoid surprises.

Table of contents
- Status & local changes
- Staging & commit
- Branching & switching
- Updating & publishing
- History & inspection
- Undoing & recovery
- Useful shortcuts & config
- For beginners: quick checklist

---

## Status & local changes

```bash
# Show working tree status (what's modified, staged, untracked)
git status
```

```bash
# Show concise changes in tracked files
git diff
```

---

## Staging & commit

```bash
# Stage all changes (tracked + untracked)
git add -A
# Or stage only tracked changes:
git add .
```

```bash
# Commit staged changes with a message
git commit -m "Short, descriptive message"
# Commit changes to tracked files (skip separate add)
git commit -am "Update: ... "
```

```bash
# Amend last commit (careful: rewrites history)
git commit --amend --no-edit
```

---

## Branching & switching

```bash
# List local branches
git branch

# List all branches (local + remote)
git branch -a
```

```bash
# Create and switch to a new branch
git checkout -b feature/xyz
# Alternative newer command
git switch -c feature/xyz
```

```bash
# Switch to an existing branch
git checkout main
# or
git switch main
```

---

## Updating & publishing

```bash
# Fetch remote refs and merge into current branch
git pull
# Safer: fetch then rebase
git pull --rebase
```

```bash
# Download remote changes without merging
git fetch --all --prune
```

```bash
# Push current branch to origin
git push
# Safe force-push (prefer --force-with-lease)
git push --force-with-lease
```

---

## History & inspection

```bash
# Compact commit history with graph
git log --oneline --graph --decorate --all
```

```bash
# Show a file's history
git log -- path/to/file
```

```bash
# Show diff of last commit
git show HEAD
```

```bash
# Blame lines in a file to see last change per line
git blame path/to/file
```

---

## Undoing & recovery (be careful)

```bash
# Unstage a file
git restore --staged path/to/file
# Discard unstaged local changes
git restore path/to/file
```

```bash
# Reset branch to previous commit (dangerous)
git reset --hard HEAD~1
```

```bash
# Revert a specific commit (creates a new commit that undoes it)
git revert <commit-hash>
```

```bash
# Stash local changes (save for later)
git stash push -m "WIP: short note"
git stash pop
```

Notes:
- Avoid `git reset --hard` and force-push on shared branches unless you understand the consequences.
- Prefer `git revert` for undoing public history.

---

## Useful shortcuts & config

Add to `~/.gitconfig`:

```ini
[alias]
  st = status
  co = checkout
  br = branch
  ci = commit
  lg = log --oneline --graph --decorate --all
```

Set name/email:

```bash
git config --global user.name "Your Name"
git config --global user.email you@example.com
```

---

## For beginners: quick checklist

- Always run `git status` to see where you are before making changes.
- Use small, focused commits with clear messages.
- Push to a feature branch; open a PR for code review rather than pushing to shared branches directly.
- If unsure, run `git fetch` and inspect changes before `git pull`.
- Before force-pushing, coordinate with teammates; prefer `--force-with-lease`.

---

Further reading
- Pro Git book: https://git-scm.com/book/en/v2
