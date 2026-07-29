# Bash Commands — quick reference

A concise list of common shell commands and short notes. Some commands differ across systems (macOS vs Linux) — notes included. This file focuses on safe, practical commands for beginners with brief explanations.

Table of contents
- Navigation & listing
- File & directory operations
- Searching & viewing
- Permissions & ownership
- Networking & transfers
- Archiving & compression
- Shell tips & history
- Shortcuts & aliases
- For beginners: safety & next steps

---

## Navigation & current directory

```bash
pwd        # Print working directory
cd /path/to/dir
cd -       # Go to previous directory
ls          # list files in current directory
```

Tips for beginners:
- Use `ls -la` to show hidden files (those starting with a dot).
- `cd -` toggles between your last two directories and is handy when moving back and forth.

---

## List files

```bash
# Long listing, human-readable, show hidden
ls -la
# 'll' is commonly an alias to 'ls -la' but not guaranteed on every system
# You can add an alias to your shell rc file if you like it:
alias ll='ls -laF'
```

Note: On some systems `ll` isn't defined by default (Ubuntu sometimes defines it in interactive shells). Adding it to `~/.bashrc` or `~/.zshrc` makes it permanent.

---

## Create / remove / move / copy

```bash
mkdir -p path/to/dir    # create directory and parents
rm -rf folder-name      # DANGEROUS: deletes recursively; double-check
rm -ri folder-name      # interactive safer alternative
touch file.txt
cp source dest
mv oldname newname
```

Safety note: always double-check `rm -rf` paths. Consider enabling `rm -i` or using a trash utility (e.g., `trash-cli`) that moves files to the system recycle bin instead of deleting permanently.

---

## View file contents

```bash
cat file.txt
less file.txt
head -n 50 file.txt
tail -f log.txt         # follow appended content
```

Beginner tip: Use `less` for large files — it lets you page, search (press `/`), and quit with `q`.

---

## Search & text processing

```bash
# Search for string in history
history | grep git

# Search inside files
grep -R --line-number "pattern" .

# Find files
find . -name "*.py"

# Replace or transform text (simple)
sed -n '1,200p' file.txt
awk '{print $1}'
```

Beginner tip: start with `grep -n "pattern" file.txt` on a single file before running recursive searches.

---

## Permissions & ownership

```bash
chmod +x script.sh      # make executable
chmod 644 file.txt
chown user:group file
```

Note: You usually only need to change ownership with `sudo` if you are the system administrator.

---

## Networking & file transfer

```bash
curl -O https://example.com/file.tar.gz
wget https://example.com/file.tar.gz
scp user@host:/path/to/file .
rsync -avz src/ dest/
```

Beginner tip: Use `curl -O` to download files to the current directory. For synchronizing directories between machines, `rsync` is safe and efficient.

---

## Archiving & compression

```bash
tar -czvf archive.tar.gz folder/
tar -xvzf archive.tar.gz
zip -r archive.zip folder/
unzip archive.zip
```

---

## Shell tips & environment

```bash
# Show path to executable
which git
type git

# Export environment variable for current session
export VARIABLE=value
# Persist by adding to ~/.bashrc or ~/.zshrc

# Reverse-search in history
# Press Ctrl+R and type part of the command
```

Beginner tip: Add frequently used environment variables and aliases to your `~/.bashrc` or `~/.zshrc` so they load for every new terminal.

---

## Shortcuts & useful aliases

Add to your shell rc file (~/.bashrc or ~/.zshrc):

```bash
alias ll='ls -laF'
alias gs='git status'
alias gp='git push'
alias gl='git pull --rebase'
```

---

## For beginners: safety & next steps

- Be very careful with `rm -rf` and `sudo` — test commands without the dangerous parts first (e.g., `ls` the path first).
- Use `--dry-run` options (when available) for tools like `rsync` (`rsync --dry-run ...`).
- Practice using the shell in a safe directory (create a sandbox folder) until you feel comfortable.
- Learn to read `man` pages: `man command` (e.g., `man rsync`).
- Bookmark resources: TLDR pages (https://tldr.sh/) and explainshell (https://explainshell.com/) help decode command flags.

If you'd like, I can also add a short section showing how to customize `PS1` prompt and how to install `trash-cli` for safer deletions.
