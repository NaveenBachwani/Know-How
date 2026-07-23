# WSL Safe Delete Setup (Recycle Bin for `rm`)

## Background

Unlike Windows, Linux (and therefore WSL) does **not** have a built-in undelete or Recycle Bin for files deleted using `rm`.

When you run:

```bash
rm myfile.py
```

the file is permanently deleted. There is no built-in undo or undelete mechanism.

If the file was:
- never committed to Git
- not backed up
- not stored by an editor such as VS Code

then recovery is generally **not possible**.

---

# Recommended Solution: `trash-cli`

Instead of permanently deleting files, use a Trash folder similar to the Windows Recycle Bin.

## Install

```bash
sudo apt update
sudo apt install trash-cli
```

---

## Basic Usage

Instead of:

```bash
rm utilities/temp_cleanup.py
```

use:

```bash
trash-put utilities/temp_cleanup.py
```

The file is moved to the Trash instead of being permanently deleted.

---

## List Deleted Files

```bash
trash-list
```

Example:

```
2026-07-23 15:10:32  utilities/temp_cleanup.py
2026-07-21 09:45:18  notes.txt
```

---

## Restore a Deleted File

```bash
trash-restore
```

This displays the contents of the Trash and lets you choose which file to restore.

---

## Empty the Trash

When you're sure you no longer need the deleted files:

```bash
trash-empty
```

You can also remove only files older than a certain number of days:

```bash
trash-empty 30
```

---

# Make `rm` Safe Automatically

The easiest approach is to replace `rm` with `trash-put`.

## Edit your shell configuration

```bash
nano ~/.bashrc
```

Add this line at the end:

```bash
alias rm='trash-put'
```

Save and exit.

Reload the configuration:

```bash
source ~/.bashrc
```

---

## Result

From now on:

```bash
rm file.py
```

actually executes:

```bash
trash-put file.py
```

This means accidental deletions can be recovered.

---

# Permanently Delete a File

Occasionally you'll want the original Linux `rm`.

There are two ways:

```bash
\rm file.py
```

or

```bash
command rm file.py
```

Both bypass the alias and permanently delete the file.

---

# Verify the Alias

Run:

```bash
alias rm
```

Expected output:

```bash
alias rm='trash-put'
```

---

# My Recommended Workflow

For ad hoc scripts and experiments:

- Write the script normally
- Delete it using `rm` (which now goes to Trash)
- Restore it later if required using `trash-restore`

For scripts that took more than a few minutes to write:

- Commit them to Git before deleting
- Git becomes the long-term history
- `trash-cli` protects you from accidental deletions between commits

---

# Summary

| Task | Command |
|------|---------|
| Install | `sudo apt install trash-cli` |
| Delete (to Trash) | `rm file.py` *(after alias)* |
| Direct delete | `trash-put file.py` |
| View Trash | `trash-list` |
| Restore | `trash-restore` |
| Empty Trash | `trash-empty` |
| Permanent delete | `\rm file.py` |
| Check alias | `alias rm` |

---

## Notes

- This protects against accidental `rm` deletions in WSL.
- It does **not** replace Git. Git is still the best way to preserve important code.
- `trash-cli` is lightweight, reliable, and one of the most commonly recommended safety tools for Linux users who prefer a recycle-bin-style workflow.
