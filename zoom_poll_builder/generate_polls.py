import os
import requests

from auth import get_access_token
from dotenv import load_dotenv
from questions import questions_data
from time import sleep

load_dotenv()


ACCESS_TOKEN = get_access_token()
MEETING_ID = os.getenv("ZOOM_MEETING_ID")

zoom_api_polls_url = f"https://api.zoom.us/v2/meetings/{MEETING_ID}/polls"

headers = {
    "Authorization": f"Bearer {ACCESS_TOKEN}",
    "Content-Type": "application/json",
}

for x in questions_data:
    payload = {
        "title": f"{x['name'][:50]}",
        "questions": [
            {
                "name": x["name"],
                "type": x["type"],  # single or multiple
                "answers": x["answers"],
            }
        ],
    }

    response = requests.post(zoom_api_polls_url, headers=headers, json=payload)
    if response.status_code == 201:
        print("Poll created successfully!")
        print(f"{response.json()}\n")
    else:
        print("Failed to create poll:")
        print(response.status_code, response.text)

    sleep(0.5)
