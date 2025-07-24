import os
import requests

from dotenv import load_dotenv


load_dotenv()

ZOOM_OAUTH_URL = "https://zoom.us/oauth/token"

ZOOM_ACCOUNT_ID = os.getenv("ZOOM_ACCOUNT_ID")
ZOOM_CLIENT_ID = os.getenv("ZOOM_CLIENT_ID")
ZOOM_CLIENT_SECRET = os.getenv("ZOOM_CLIENT_SECRET")


def get_access_token() -> str:
    headers = {"Content-Type": "application/x-www-form-urlencoded"}
    payload = {
        "grant_type": "account_credentials",
        "account_id": ZOOM_ACCOUNT_ID,
    }
    response = requests.post(
        ZOOM_OAUTH_URL,
        headers=headers,
        data=payload,
        auth=(ZOOM_CLIENT_ID, ZOOM_CLIENT_SECRET),
    )

    if response.status_code == 200:
        return response.json()["access_token"]
    else:
        raise Exception(f"Failed to get token: {response.status_code} {response.text}")
