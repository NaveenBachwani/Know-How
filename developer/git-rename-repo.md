# Rename Git Repo

## eg Renamed repo from dev-notes to know-how locally
GitHub repo updated from one device; This is how you update Device 2

```bash
cd ~/projects
```

# Rename the local folder
```bash
mv dev-notes know-how
```

```bash
cd know-how
```

# Point Git to the renamed GitHub repository
```bash
git remote set-url origin https://github.com/NaveenBachwani/Know-How.git
```

# Fetch the latest changes
```bash
git fetch origin
```

# Pull the latest commit (which includes the developer/ reorganization)
```bash
git pull
```

# Verify everything
```
git remote -v
git status
```