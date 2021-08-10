from keyboard import get_main_keyboard
import telebot
from bot_config import *
from keyboard import *
from database import *

bot = telebot.TeleBot(bot_token)

message_for_reply = None


@bot.callback_query_handler(func=lambda call: True)
def reaction_to_button(call):
    user_id = call.from_user.id
    if call.data == "show_notes":
        bot.send_message(user_id, get_all_notes(user_id))
        bot.send_message(user_id, text="Выбери действие", reply_markup=get_main_keyboard())
    elif call.data == "add_note":
        ask_note_title(user_id)

      

def ask_note_title(user_id):
    global message_for_reply
    message_for_reply = bot.send_message(user_id, "Введите название добавляемой заметки")
     


@bot.message_handler(content_types=['text'])
def reaction_to_message(message):
    if message.text == "Привет":
        bot.send_message(message.from_user.id, "Привет, я бот, позволяющий создавать список заметок")
        bot.send_message(message.from_user.id, text="Выбери действие", reply_markup=get_main_keyboard())

    elif message.reply_to_message != None:
        if message.reply_to_message.message_id == message_for_reply.message_id:
            print("Ответили на вопрос")




    


bot.polling(none_stop=True, interval=0)
