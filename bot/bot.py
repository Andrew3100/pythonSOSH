import telebot
from telebot import types
import smtplib
bot = telebot.TeleBot('1766404211:AAH4mM6J5qOSZvVCSY6TInztk9PFZjkjwgU')

@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
    bot.reply_to(message, f'Я бот. Приятно познакомиться, {message.from_user.first_name}')

    @bot.message_handler(content_types=['text'])
    def get_text_messages(message):
        if message.text.lower():
            item_yes = types.InlineKeyboardButton(text='Принять', callback_data='yes')
            bot.send_message(message.from_user.id, 'Привет!')
            t = message.text
        else:
            bot.send_message(message.from_user.id, 'Не понимаю, что это значит.')
        print(t)



bot.polling(none_stop = True)

