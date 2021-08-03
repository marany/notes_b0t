import requests
from bot_config import *

def get_all_notes(user_id):
    url = f"https://practice-2abd.restdb.io/rest/notes?filter={user_id}"
    response = requests.request("GET", url, headers=headers)
    notes = response.text
    return notes

