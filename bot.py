from keyboard import get_main_keyboard
import telebot
from bot_config import *
from keyboard import *
from database import *

bot = telebot.TeleBot(bot_token)


@bot.callback_query_handler(func=lambda call: True)
def reaction_to_button(call):
    if call.data == "show_notes":
        bot.send_message(call.from_user.id, get_all_notes(call.from_user.id))



@bot.message_handler(content_types=['text'])
def reaction_to_message(message):
    print(message.from_user.id)
    if message.text == "Привет":
        bot.send_message(message.from_user.id, "Привет, я бот, позволяющий создавать список заметок")
        bot.send_message(message.from_user.id, text="Выбери действие", reply_markup=get_main_keyboard())
    else:
        bot.send_message(message.from_user.id, "Я тебя не понял, напиши /start")


bot.polling(none_stop=True, interval=0)
