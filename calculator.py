from constant import *
import math

def calculate(message):
    expression = message.text

    try:
        result = eval(expression)
        bot.send_message(message.chat.id, f'Результат: {result}')
    except (SyntaxError, TypeError, NameError):
        try:
            result = eval(expression, {"__builtins__": None}, math.__dict__)
            bot.send_message(message.chat.id, f'Результат: {result}')
        except (SyntaxError, TypeError, NameError):
            bot.send_message(message.chat.id, 'Ошибка при выполнении вычислений.')

    bot.send_message(message.chat.id, "-------------\nВоспользуйтесь панелью команд, чтобы выбрать действие",
                     reply_markup=keyboard)
