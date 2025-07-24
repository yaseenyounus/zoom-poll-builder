import os
import requests

from auth import get_access_token
from dotenv import load_dotenv

load_dotenv()


ACCESS_TOKEN = get_access_token()
MEETING_ID = os.getenv("ZOOM_MEETING_ID")


headers = {
    "Authorization": f"Bearer {ACCESS_TOKEN}",
    "Content-Type": "application/json",
}

polls_url = f"https://api.zoom.us/v2/meetings/{MEETING_ID}/polls"
response = requests.get(polls_url, headers=headers)

if response.status_code != 200:
    print(f"Failed to fetch polls: {response.status_code}")
    print(response.text)
    exit()

polls = response.json().get("polls", [])
print(f"Found {len(polls)} polls to delete.")

for poll in polls:
    poll_id = poll["id"]
    delete_url = f"https://api.zoom.us/v2/meetings/{MEETING_ID}/polls/{poll_id}"
    delete_response = requests.delete(delete_url, headers=headers)

    if delete_response.status_code == 204:
        print(f"Deleted poll: {poll_id}")
    else:
        print(f"Failed to delete poll {poll_id}: {delete_response.status_code}")
        print(delete_response.text)
