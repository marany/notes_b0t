from keyboard import get_main_keyboard
import telebot
from bot_config import *
from keyboard import *
from database import *

bot = telebot.TeleBot(bot_token)
users = {}
user_answers = {}


@bot.callback_query_handler(func=lambda button: True)
def reaction_to_button(button):
    user_id = button.from_user.id
    if button.data == "show_notes":
        bot.send_message(user_id, get_formatted_notes_text(user_id))
        bot.send_message(user_id, text="Выбери действие", reply_markup=get_main_keyboard())
    
    if button.data == "add_note":
        msg = bot.send_message(user_id, "Введите название заметки")
        bot.register_next_step_handler(msg, note_title_answer)


def note_title_answer(message):
    print("Title = ", message.text)




    


@bot.message_handler(content_types=['text'])
def reaction_to_message(message):
    if message.text == "Привет":
        bot.send_message(message.from_user.id, "Привет, я бот, позволяющий создавать список заметок")
        bot.send_message(message.from_user.id, text="Выбери действие", reply_markup=get_main_keyboard())




    


bot.polling(none_stop=True, interval=0)
