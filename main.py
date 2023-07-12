from translator import *
from calculator import *
from weather import *
import random
import requests


#start/info
@bot.message_handler(commands=['start', 'info'])
def handle_start(message):
    bot.send_message(message.chat.id,
                     'Разработчики:\n<b>Музычук Артем, Юрченко Станислав</b>\nИКПИ-12. Санкт-Петербург 2023 ',
                     parse_mode='HTML', reply_markup=keyboard)

#Переводчик
@bot.message_handler(func=lambda message: message.text == 'Переводчик')
def translate_text(message):
    bot.send_message(message.chat.id, 'Введите текст для перевода (на английском или русском)',
                     reply_markup=types.ReplyKeyboardRemove())
    bot.register_next_step_handler(message, translation)

#Узнать погоду
@bot.message_handler(func=lambda message: message.text == 'Узнать погоду')
def handle_weather(message):
    bot.send_message(message.chat.id, 'Введите название города:', reply_markup=types.ReplyKeyboardRemove())
    bot.register_next_step_handler(message, get_weather)

#Калькулятор
@bot.message_handler(func=lambda message: message.text == 'Калькулятор')
def handle_calculator(message):
    bot.send_message(message.chat.id,
                     'Отправьте мне выражение')
    bot.register_next_step_handler(message, calculate)

#Мемы про IT
@bot.message_handler(func=lambda message: message.text == 'Мемы про IT')
def handle_meme(message):
    img_url = f'https://t.me/itshnik_mem/{random.randint(1, 1000)}'
    request_url = f'{URL}{TOKEN}/sendPhoto?chat_id={message.chat.id}&photo={img_url}'
    requests.get(request_url)

#Команда не найдена
@bot.message_handler(func=lambda message: True)
def handle_unknown_command(message):
    bot.reply_to(message, "Команда не найдена.")


bot.polling()
