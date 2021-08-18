import requests
import json
from bot_config import *


def get_notes_list(user_id):
    url = f"https://practice-2abd.restdb.io/rest/notes?filter={user_id}"
    response = requests.request("GET", url, headers=headers)
    notes_list = json.loads(response.text)
    return notes_list


def get_formatted_notes_text(user_id):
    notes = get_notes_list(user_id)
    if notes:
        formatted_text = ""
        for note in notes:
            formatted_text += f"Название: {note['Title']}\n"\
                                f"Описание: {note['Description']} \n\n"
        return formatted_text
    else:
        return "У вас нет заметок"

