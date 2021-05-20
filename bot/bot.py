import telebot
from telebot import types
import smtplib
import os
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders
from platform import python_version
bot = telebot.TeleBot('1766404211:AAH4mM6J5qOSZvVCSY6TInztk9PFZjkjwgU')

@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
    bot.reply_to(message, f'Я бот. Приятно познакомиться, {message.from_user.first_name}')

    @bot.message_handler(content_types=['text'])
    def get_text_messages(message):
        if message.text.lower():
            bot.send_message(message.from_user.id, 'Привет!')
            t = message.text
        else:
            bot.send_message(message.from_user.id, 'Не понимаю, что это значит.')
        print(t)



bot.polling(none_stop = True)

