## Developer Workstation Bootstrap Guide
Version: 1.0 | Last Updated: 2026-07-25

---

## Purpose

This document is the master reference for setting up a new development machine to match my existing AI development environment.

Target platforms:

- Windows 11
- WSL (Ubuntu)
- Linux Mint

---

## Recommended Installation Order

Do **not** install randomly. Follow this order.

### 1 – Operating System

- Windows Update
- Install WSL (Ubuntu)
- Update Ubuntu

```bash
sudo apt update
sudo apt upgrade -y
```

---

### 2 – Essential Development Tools

### Git

Windows

https://git-scm.com/download/win

Ubuntu

```bash
sudo apt install git -y
```

Verify

```bash
git --version
```

---

### GitHub CLI

Windows

https://cli.github.com/

Ubuntu

```bash
(type -p wget >/dev/null || sudo apt install wget -y)

wget -qO- https://cli.github.com/packages/githubcli-archive-keyring.gpg \
| sudo dd of=/usr/share/keyrings/githubcli-archive-keyring.gpg

sudo chmod go+r /usr/share/keyrings/githubcli-archive-keyring.gpg

echo \
"deb [arch=$(dpkg --print-architecture) signed-by=/usr/share/keyrings/githubcli-archive-keyring.gpg] https://cli.github.com/packages stable main" \
| sudo tee /etc/apt/sources.list.d/github-cli.list >/dev/null

sudo apt update

sudo apt install gh -y
```

Verify

```bash
gh --version
```

---

### 3 – Python

Install Python 3.12 or newer.

Ubuntu

```bash
sudo apt install python3 python3-pip python3-venv -y
```

Verify

```bash
python3 --version
pip3 --version
```

---

### 4 – pipx

```bash
sudo apt install pipx -y

pipx ensurepath
```

Verify

```bash
pipx --version
```

---

### 5 – uv

Install

```bash
pipx install uv
```

Verify

```bash
uv --version
```

---

### 6 – VS Code

Windows

https://code.visualstudio.com/

Verify

```bash
code --version
```

---

###  7 – VS Code Extensions

Install

- Python
- GitHub Copilot
- Continue
- Roo Code
- Cline

Verify

```bash
code --list-extensions
```

---

### 8 – Ollama

Windows

https://ollama.com

Linux

```bash
curl -fsSL https://ollama.com/install.sh | sh
```

Verify

```bash
ollama --version
```

---

### 9 – Download Local Models

Primary

```bash
ollama pull qwen3:4b
```

Optional

```bash
ollama pull qwen3:8b
```

List installed models

```bash
ollama list
```

---

### 10 – Linux Utilities

Install

```bash
sudo apt install \
tree \
zip \
unzip \
curl \
wget \
trash-cli \
ffmpeg \
jq -y
```

Verify

```bash
tree --version

zip -v

curl --version

trash-put --version
```

---

### 11 – Node.js (Recommended)

Install latest LTS.

Verify

```bash
node --version

npm --version
```

---

### 12 – Global Python Packages

Useful

```bash
pip install

requests

pandas

openai

python-dotenv

gspread

google-auth

yt-dlp

youtube-transcript-api
```

Verify

```bash
pip list
```

---

### 13 – Git Configuration

```bash
git config --global user.name "Your Name"

git config --global user.email "you@example.com"
```

Verify

```bash
git config --list
```

---

### 14 – GitHub Authentication

```bash
gh auth login
```

Verify

```bash
gh auth status
```

---

### 15 – OpenAI / OpenRouter

Store API keys as environment variables.

Never hardcode API keys into code.

---

## Recommended Tool Inventory

### Required

- Git
- GitHub CLI
- Python
- pip
- python3-venv
- pipx
- uv
- VS Code
- Ollama
- curl
- wget
- tree
- zip
- unzip

---

### Strongly Recommended

- Continue
- Roo Code
- Cline
- GitHub Copilot
- ffmpeg
- jq
- trash-cli

---

### Optional

- Docker
- Docker Compose
- PostgreSQL
- SQLite CLI

---

## Upgrade Commands

Ubuntu

```bash
sudo apt update

sudo apt upgrade -y
```

Python packages

```bash
pip install --upgrade pip

pip list --outdated

pip install -U package_name
```

uv

```bash
pipx upgrade uv
```

pipx packages

```bash
pipx upgrade-all
```

Ollama

```bash
ollama pull qwen3:4b
```

GitHub CLI

```bash
sudo apt update

sudo apt install gh
```

---

## Recovery Utilities

Safe delete

```bash
trash-put filename
```

Restore

```bash
trash-list
```

Empty trash

```bash
trash-empty
```

---
