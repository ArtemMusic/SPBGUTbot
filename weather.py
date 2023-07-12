from constant import *
import requests

WEATHER_API_KEY = '1ce32dd7ed35e3bde9621673dccc4c4f'


def get_weather(message):
    city = message.text.strip()
    weather_data = fetch_weather(city)

    if weather_data:
        response = f"Погода в {city}:\n"
        response += f"Температура: {weather_data['main']['temp']} °C\n"
        response += f"Давление: {weather_data['main']['pressure']} hPa\n"
        response += f"Скорость ветра: {weather_data['wind']['speed']} м/с\n"
        response += f"Статус: {weather_data['weather'][0]['description']}\n"
    else:
        response = "Город не найден."

    bot.send_message(message.chat.id, response)
    bot.send_message(message.chat.id, "-------------\nВоспользуйтесь панелью команд, чтобы выбрать действие",
                     reply_markup=keyboard)


def fetch_weather(city):
    try:
        url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={WEATHER_API_KEY}&units=metric"
        response = requests.get(url)
        weather_data = response.json()
        if weather_data["cod"] != "404":
            return weather_data
    except:
        pass
    return None
