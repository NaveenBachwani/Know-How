import os
import zipfile
import glob
from datetime import datetime
import json

# ==========================================
# --- CONFIGURATION MODULE ---
# ==========================================
# Source directory to be backed up (the know-how repo)
SOURCE_DIR = os.path.expanduser("~/projects/know-how")

# Destination directory for zip archives and state files
BACKUP_DIR = os.path.expanduser("~/projects/know-how/backups")

# Prefix for generated zip files
ZIP_PREFIX = "know-how"

# Number of local zip archives to retain
RETENTION_COUNT = 10

# Directories to exclude from the zip archive
EXCLUDE_DIRS = {'venv', '.git', '__pycache__', 'node_modules', 'dist', 'build', '.vscode', '.idea'}
# ==========================================

# --- DERIVED PATHS ---
_STATE_DIR = os.path.join(BACKUP_DIR, ".state")
TRACKER_FILE_PATH = os.path.join(_STATE_DIR, "last_backup_date.txt")
BACKUP_STATE_FILE_PATH = os.path.join(_STATE_DIR, "backup_state.json")

TIMESTAMP = datetime.now().strftime("%Y%m%d_%H%M%S")
TODAY_STR = datetime.now().strftime("%Y-%m-%d")
ZIP_FILENAME = f"{ZIP_PREFIX}_{TIMESTAMP}.zip"
ZIP_FILEPATH = os.path.join(BACKUP_DIR, ZIP_FILENAME)


def check_execution_lock():
    if os.path.exists(TRACKER_FILE_PATH):
        with open(TRACKER_FILE_PATH, "r") as f:
            if f.read().strip() == TODAY_STR:
                return True
    return False


def mark_execution_success():
    os.makedirs(os.path.dirname(TRACKER_FILE_PATH), exist_ok=True)
    with open(TRACKER_FILE_PATH, "w") as f:
        f.write(TODAY_STR)


# --- STATE MANAGEMENT ---
def load_backup_state():
    state_file = BACKUP_STATE_FILE_PATH
    if os.path.exists(state_file):
        try:
            with open(state_file, 'r') as f:
                state_data = json.load(f)
                return state_data
        except (json.JSONDecodeError, IOError) as e:
            print(f"Warning: Could not read backup state file {state_file}: {e}. Starting fresh.")
            return {}
    return {}


def save_backup_state(current_state, status="backed_up"):
    state_file = BACKUP_STATE_FILE_PATH
    os.makedirs(os.path.dirname(state_file), exist_ok=True)
    state_to_save = {"status": status, "files": current_state, "timestamp": datetime.now().strftime("%Y-%m-%d %H:%M:%S")}
    try:
        with open(state_file, 'w') as f:
            json.dump(state_to_save, f, indent=4)
    except IOError as e:
        print(f"Error: Could not write backup state file {state_file}: {e}")


def get_current_file_states():
    current_states = {}
    for root, dirs, files in os.walk(SOURCE_DIR):
        dirs[:] = [d for d in dirs if d not in EXCLUDE_DIRS]

        for file in files:
            if file.endswith('.zip'):
                continue
            file_path = os.path.join(root, file)
            try:
                arcname = os.path.relpath(file_path, SOURCE_DIR)
                mtime = os.path.getmtime(file_path)
                current_states[arcname] = mtime
            except OSError as e:
                print(f"Warning: Could not get info for file {file_path}: {e}")
    return current_states


def has_changes(previous_states, current_states):
    for path, prev_mtime in previous_states.items():
        if path not in current_states or current_states[path] != prev_mtime:
            return True
    if len(current_states) > len(previous_states):
        return True
    return False


def create_zip():
    os.makedirs(BACKUP_DIR, exist_ok=True)
    print(f"Creating archive locally in {BACKUP_DIR}...")

    with zipfile.ZipFile(ZIP_FILEPATH, 'w', zipfile.ZIP_DEFLATED) as zipf:
        for root, dirs, files in os.walk(SOURCE_DIR):
            dirs[:] = [d for d in dirs if d not in EXCLUDE_DIRS]

            for file in files:
                if file.endswith('.zip'):
                    continue
                file_path = os.path.join(root, file)
                arcname = os.path.relpath(file_path, SOURCE_DIR)
                zipf.write(file_path, arcname)

    print(f"Archive successfully created: {ZIP_FILEPATH}")


def enforce_retention():
    query = os.path.join(BACKUP_DIR, f"{ZIP_PREFIX}_*.zip")
    existing_backups = sorted(glob.glob(query), key=os.path.getctime)

    while len(existing_backups) > RETENTION_COUNT:
        oldest = existing_backups.pop(0)
        print(f"Retention Policy Triggered: Deleting oldest local backup -> {oldest}")
        try:
            os.remove(oldest)
        except OSError as e:
            print(f"Error deleting file {oldest}: {e}")


def main():
    if not os.path.exists(SOURCE_DIR):
        print(f"Critical Error: Source directory '{SOURCE_DIR}' does not exist. Halting execution.")
        return

    if check_execution_lock():
        print(f"Backup process already initiated for {TODAY_STR}. Skipping further execution.")
        return

    mark_execution_success()

    try:
        previous_states = load_backup_state()
        current_states = get_current_file_states()

        if has_changes(previous_states, current_states):
            print("Changes detected. Proceeding with backup...")
            create_zip()
            enforce_retention()
            save_backup_state(current_states, status="backed_up")
            print("Backup successfully created and state updated.")
        else:
            print("No changes detected since the last backup. Skipping archive creation.")
            save_backup_state(current_states, status="skipped")
            print("Backup state updated to 'skipped'.")

    except Exception as e:
        print(f"Backup process encountered an error: {e}")


if __name__ == "__main__":
    main()