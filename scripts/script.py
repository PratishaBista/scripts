import os
import requests

if os.path.exists("tracker.txt"):
    with open("tracker.txt", "r") as file:
        streak_text = file.read().strip()
else:
    streak_text = "0🔥"

streak_display = f"Stats: Current Streak →→ {streak_text}"

TOKEN = os.getenv("GITHUB_TOKEN")
USERNAME = "F3Alt"

api_url = f"https://api.github.com/user"
headers = {
    "Authorization": f"token {TOKEN}",
    "Accept": "application/vnd.github.v3+json",
}

response = requests.get(api_url, headers=headers)
if response.status_code == 200:
    user_data = response.json()
    current_bio = user_data["bio"] or ""

    if current_bio:
        bio_parts = [part.strip() for part in current_bio.split("│")]
        bio_without_streak = [
            part for part in bio_parts if not part.startswith("Stats: Current Streak")
        ]
        new_bio = f"{streak_display} │ " + " │ ".join(bio_without_streak)
    else:
        new_bio = streak_display

    update_data = {"bio": new_bio}
    update_response = requests.patch(api_url, headers=headers, json=update_data)

    if update_response.status_code == 200:
        print("GitHub streak updated successfully!")
    else:
        print("Failed to update streak:", update_response.json())
else:
    print("Failed to fetch GitHub user data:", response.json())
