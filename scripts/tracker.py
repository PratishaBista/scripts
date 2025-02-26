import os
import datetime

today = datetime.date.today()

if os.path.exists("last_trace.txt"):
    with open("last_trace.txt", "r") as file:
        last_commit_date = datetime.date.fromisoformat(file.read().strip())
else:
    last_commit_date = None

if last_commit_date == today - datetime.timedelta(days=1):
    with open("tracker.txt", "r") as file:
        tracker_count = int(file.read().strip().replace("🔥", ""))
    tracker_count += 1
elif last_commit_date == today:
    with open("tracker.txt", "r") as file:
        tracker_count = int(file.read().strip().replace("🔥", ""))
else:
    tracker_count = 1

with open("tracker.txt", "w") as file:
    file.write(f"{tracker_count}🔥" if tracker_count > 0 else "")

with open("last_trace.txt", "w") as file:
    file.write(str(today))

print(f"Updated tracker: {tracker_count}🔥")
