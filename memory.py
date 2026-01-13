import json
import os

FILE_PATH = "data/reminders.json"

def load_reminders():
    if not os.path.exists(FILE_PATH):
        return []
    with open(FILE_PATH, "r") as f:
        return json.load(f)

def save_reminder(task):
    reminders = load_reminders()
    reminders.append(task)
    with open(FILE_PATH, "w") as f:
        json.dump(reminders, f, indent=4)
