import requests
import json
from bot_config import *

def get_all_notes(user_id):
    url = f"https://practice-2abd.restdb.io/rest/notes?filter={user_id}"
    response = requests.request("GET", url, headers=headers)
    notes = json.loads(response.text)
    formatted_text = ""
    for note in notes:
        formatted_text += f"Название: {note['Title']}\n"\
                          f"Описание: {note['Description']} \n\n"
    return formatted_text

