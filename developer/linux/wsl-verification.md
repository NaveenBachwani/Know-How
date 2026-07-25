## WSL (Ubuntu) Developer Environment
### Installation, Verification & Upgrade Reference

> Tested for Ubuntu 22.04/24.04 running under WSL2.

---

## 1. Update Ubuntu

### Install / Update

```bash
sudo apt update
sudo apt upgrade -y
sudo apt autoremove -y
```

### Verify

```bash
lsb_release -a
uname -a
```

---

## 2. Git

### Install

```bash
sudo apt install git -y
```

### Verify

```bash
git --version
```

### Upgrade

```bash
sudo apt update
sudo apt install git
```

---

## 3. GitHub CLI (gh)

### Install

```bash
(type -p wget >/dev/null || sudo apt install wget -y)

wget -qO- https://cli.github.com/packages/githubcli-archive-keyring.gpg \
| sudo dd of=/usr/share/keyrings/githubcli-archive-keyring.gpg

sudo chmod go+r /usr/share/keyrings/githubcli-archive-keyring.gpg

echo "deb [arch=$(dpkg --print-architecture) signed-by=/usr/share/keyrings/githubcli-archive-keyring.gpg] https://cli.github.com/packages stable main" \
| sudo tee /etc/apt/sources.list.d/github-cli.list >/dev/null

sudo apt update

sudo apt install gh -y
```

### Verify

```bash
gh --version
gh auth status
```

### Upgrade

```bash
sudo apt update
sudo apt install gh
```

---

## 4. Python

### Install

```bash
sudo apt install python3 python3-pip python3-venv -y
```

### Verify

```bash
python3 --version
pip3 --version
```

### Upgrade

```bash
sudo apt update
sudo apt install python3 python3-pip python3-venv
```

---

## 5. pipx

### Install

```bash
sudo apt install pipx -y
pipx ensurepath
```

Restart the terminal.

### Verify

```bash
pipx --version
```

### Upgrade

```bash
sudo apt update
sudo apt install pipx
```

---

## 6. uv

### Install

```bash
pipx install uv
```

### Verify

```bash
uv --version
```

### Upgrade

```bash
pipx upgrade uv
```

---

## 7. Ollama

### Install

```bash
curl -fsSL https://ollama.com/install.sh | sh
```

### Verify

```bash
ollama --version
ollama list
```

### Upgrade

```bash
curl -fsSL https://ollama.com/install.sh | sh
```

---

## 8. Ollama Models

### Install

```bash
ollama pull qwen3:4b
```

Optional

```bash
ollama pull qwen3:8b
```

### Verify

```bash
ollama list
```

### Upgrade

```bash
ollama pull qwen3:4b
ollama pull qwen3:8b
```

---

## 9. tree

### Install

```bash
sudo apt install tree -y
```

### Verify

```bash
tree --version
```

### Upgrade

```bash
sudo apt install tree
```

---

## 10. curl

### Install

```bash
sudo apt install curl -y
```

### Verify

```bash
curl --version
```

### Upgrade

```bash
sudo apt install curl
```

---

## 11. wget

### Install

```bash
sudo apt install wget -y
```

### Verify

```bash
wget --version
```

### Upgrade

```bash
sudo apt install wget
```

---

## 12. zip

### Install

```bash
sudo apt install zip unzip -y
```

### Verify

```bash
zip -v
unzip -v
```

### Upgrade

```bash
sudo apt install zip unzip
```

---

## 13. jq

### Install

```bash
sudo apt install jq -y
```

### Verify

```bash
jq --version
```

### Upgrade

```bash
sudo apt install jq
```

---

## 14. ffmpeg

### Install

```bash
sudo apt install ffmpeg -y
```

### Verify

```bash
ffmpeg -version
```

### Upgrade

```bash
sudo apt install ffmpeg
```

---

## 15. trash-cli

### Install

```bash
sudo apt install trash-cli -y
```

### Verify

```bash
trash-put --version
```

### Upgrade

```bash
sudo apt install trash-cli
```

---

## 16. Node.js (LTS)

### Install

```bash
sudo apt install nodejs npm -y
```

### Verify

```bash
node --version
npm --version
```

### Upgrade

```bash
sudo apt install nodejs npm
```

---

## 17. Global Python Packages

### Install

```bash
pip install \
openai \
requests \
pandas \
python-dotenv \
gspread \
google-auth \
yt-dlp \
youtube-transcript-api
```

### Verify

```bash
pip list
```

### Upgrade All

```bash
pip list --outdated
pip install --upgrade pip
```

Upgrade a specific package:

```bash
pip install -U <package-name>
```

---

## 18. Git Configuration

### Configure

```bash
git config --global user.name "Your Name"
git config --global user.email "you@example.com"
```

### Verify

```bash
git config --list
```

---

## 19. GitHub Authentication

### Login

```bash
gh auth login
```

### Verify

```bash
gh auth status
```

---

## 20. Full System Upgrade

```bash
sudo apt update
sudo apt upgrade -y
sudo apt autoremove -y

pipx upgrade-all

pip list --outdated
```

---

### Quick Health Check

```bash
git --version
gh --version
python3 --version
pip3 --version
pipx --version
uv --version
node --version
npm --version
ollama --version
ollama list
tree --version
curl --version
wget --version
jq --version
ffmpeg -version
trash-put --version
```
