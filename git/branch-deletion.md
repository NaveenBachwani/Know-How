# Git Branch Deletion Cheat Sheet

## 1. Switch away from the branch you want to delete

You cannot delete the branch you're currently on.

```bash
git switch main
```

---

## 2. Delete a local branch

### Safe delete (only if already merged)

```bash
git branch -d branch-name
```

### Force delete (whether merged or not)

```bash
git branch -D branch-name
```

---

## 3. Delete the branch from the remote (`origin`)

```bash
git push origin --delete branch-name
```

---

## 4. Delete both local and remote

```bash
git branch -D branch-name
git push origin --delete branch-name
```

Replace `-D` with `-d` if you only want to delete merged branches.

---

## 5. List branches

### Local branches

```bash
git branch
```

### Remote branches

```bash
git branch -r
```

### Local + Remote branches

```bash
git branch -a
```

---

## 6. Remove stale remote-tracking branches

If a branch has already been deleted on GitHub but still appears locally:

```bash
git fetch --prune
```

or

```bash
git remote prune origin
```

Both commands clean up obsolete `origin/<branch>` references.

---

## Example

Delete a feature branch named `maintenance/pipeline-hardening`:

```bash
git switch main
git branch -D maintenance/pipeline-hardening
git push origin --delete maintenance/pipeline-hardening
git fetch --prune
```
