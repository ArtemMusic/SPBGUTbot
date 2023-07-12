from constant import *
from googletrans import Translator
from gtts import gTTS
import os

translator = Translator(service_urls=['translate.google.com'])


def translation(message):
    if message.text:
        translation = translator.translate(message.text,
                                           dest='ru' if translator.detect(message.text).lang == 'en' else 'en')
        translated_text = translation.text
        bot.send_message(message.chat.id, f'Переведенный текст:\n\n{translated_text}')

        # Отправка голосового сообщения
        tts = gTTS(text=translated_text, lang='ru' if translation.dest == 'ru' else 'en')
        audio_file_path = 'translated_audio.mp3'
        tts.save(audio_file_path)
        with open(audio_file_path, 'rb') as audio:
            bot.send_voice(message.chat.id, audio)
        os.remove(audio_file_path)
    else:
        bot.send_message(message.chat.id, 'Введите текст для перевода (на английском или русском)')

    bot.send_message(message.chat.id, "-------------\nВоспользуйтесь панелью команд, чтобы выбрать действие",
                     reply_markup=keyboard)
