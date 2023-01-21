import os

import telebot
import config
from telebot import types
from telebot import apihelper

bot = telebot.TeleBot(config.TOKEN)


@bot.message_handler(commands=['start'])
def welcome(message):
    sti = open('/home/bekzat/Beka/transferring_style_bot/welcome.webp', 'rb')
    bot.send_sticker(message.chat.id, sti)

    bot.send_message(message.chat.id,
                     'Добро пожаловать! \n Я - {1.first_name}! \n'.format(message.from_user, bot.get_me()),
                     parse_mode='html')
    bot.send_message(message.chat.id, 'Я могу переносить стили из одной картинки на другую')
    moon = types.InlineKeyboardMarkup(row_width=1)
    man1 = types.InlineKeyboardButton('Начать работу', callback_data='start')
    man2 = types.InlineKeyboardButton('Посмотреть пример', callback_data='look')

    moon.add(man1, man2)

    bot.send_message(message.chat.id, 'Можно посмотреть пример, либо начать работу', reply_markup=moon)


@bot.callback_query_handler(func=lambda call: True)
def callback_worker(call):
    if call.data == 'start':
        bot.send_message(call.message.chat.id, 'Загрузи первую картинку')
    elif call.data == 'look':
        bot.send_photo(call.message.chat.id, photo=open("example_content_img.jpg", 'rb'))
        bot.send_message(call.message.chat.id, 'content')
        bot.send_photo(call.message.chat.id, photo=open("example_style_img.jpg", 'rb'))
        bot.send_message(call.message.chat.id, 'style')
        bot.send_photo(call.message.chat.id, photo=open("example_output_img.jpg", 'rb'))
        bot.send_message(call.message.chat.id, 'output')


@bot.message_handler(commands=['example'])
def handle_photo(message):
    file_info = bot.get_file(message.photo[-1].file_id)
    downloaded_file = bot.download_file(file_info.file_path)
    src = os.getcwd() + '/content_input.jpg'
    bot.send_message(message.chat.id, src)
    with open(src, 'wb') as new_file:
        new_file.write(downloaded_file)
    bot.send_photo(message.chat.id, photo=open(src, 'rb'))


@bot.message_handler(content_types=['photo'])
def handle_photo(message):
    file_info = bot.get_file(message.photo[-1].file_id)
    downloaded_file = bot.download_file(file_info.file_path)
    src = os.getcwd() + '/content_input.jpg'
    bot.send_message(message.chat.id, src)
    with open(src, 'wb') as new_file:
        new_file.write(downloaded_file)
    bot.send_photo(message.chat.id, photo=open(src, 'rb'))


# RUN
bot.polling(none_stop=True, interval=0)
