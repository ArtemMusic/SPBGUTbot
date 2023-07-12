import telebot
from telebot import types

TOKEN = '6375662273:AAHyS-beLvfVSOq0hzDpIeOkeT-nJeCyCRY'
bot = telebot.TeleBot(TOKEN)
URL = 'https://api.telegram.org/bot'

keyboard = types.ReplyKeyboardMarkup(row_width=2)
translate_button = types.KeyboardButton('Переводчик')
weather_button = types.KeyboardButton('Узнать погоду')
calculator_button = types.KeyboardButton('Калькулятор')
mems_button = types.KeyboardButton('Мемы про IT')
keyboard.add(translate_button, weather_button, calculator_button, mems_button)
