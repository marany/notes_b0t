import telebot
from bot_config import *


bot = telebot.TeleBot(bot_token)


@bot.message_handler(content_types=['text'])
def reaction_to_message(message):
    if message.text == "Привет":
        bot.send_message(message.from_user.id, "Привет, я бот, позволяющий создавать список заметок")
    else:
        bot.send_message(message.from_user.id, "Я тебя не понял, напиши /start")


bot.polling(none_stop=True, interval=0)
