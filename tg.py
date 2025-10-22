
from telebot import types

import telebot
bot = telebot.TeleBot("8212863055:AAE5L_CwLpE6MxaQ-pLMsWyztauFoLr57X8")


@bot.message_handler(commands=['start'])
def handle_photo(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)  # коробка
    btn1 = types.KeyboardButton("О проекте")  # кнопка
    markup.add(btn1)  # кладём кнопку в коробку
      # текст + кнопка



bot.polling(none_stop=True)



