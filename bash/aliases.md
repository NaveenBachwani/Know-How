# Bash Aliases

## Reload Bash

```bash
source ~/.bashrc
```

---

## Edit .bashrc

```bash
nano ~/.bashrc
```

---

## My aliases

(Add aliases below)

```
# Others / WSL / Aider

export OPENROUTER_API_KEY="sk-or-v1-xyz"
export GEMINI_API_KEY="AQ.xyz"

# -----------------------------
# Project shortcuts
# -----------------------------

alias raindrop='cd ~/projects/raindrop-li-x-buffer && source venv/bin/activate'
alias proj='cd ~/projects'
alias ll='ls -al'
alias gs='git status'
alias lg='lazygit'
export TZ='Asia/Kolkata'
alias glog='git log --pretty=format:"%C(yellow)%h%Creset | %C(cyan)%ad%Creset | %s" --date=short'

export NVM_DIR="$HOME/.nvm"
[ -s "$NVM_DIR/nvm.sh" ] && \. "$NVM_DIR/nvm.sh"  # This loads nvm
[ -s "$NVM_DIR/bash_completion" ] && \. "$NVM_DIR/bash_completion"  # This loads nvm bash_completion
. "$HOME/.cargo/env"
alias ollama="/mnt/c/Users/navee/AppData/Local/Programs/Ollama/ollama.exe"

# -----------------------------
# Git helpers
# -----------------------------

gsync() {
    echo "=== Fetching from GitHub ==="
    git fetch --all --tags

    echo
    echo "=== Local branches ==="
    git branch -vv

    echo
    echo "=== Repository status ==="
    git status
}

# fzf shell integration
eval "$(fzf --bash)"


# Created by `pipx` on 2026-07-22 11:23:55
export PATH="$PATH:/home/naveen/.local/bin"
