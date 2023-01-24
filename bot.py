import os

import telebot
import config
from telebot import types

from transfer import nst_model
from transfer_gan import create_net, msg_net_processing

bot = telebot.TeleBot(config.TOKEN)
msg_net = create_net()

src_output = os.path.join(os.getcwd(), 'media', 'output_image.jpg')
src_style = os.path.join(os.getcwd(), 'media', 'style_input.jpg')
src_input = os.path.join(os.getcwd(), 'media', 'content_input.jpg')


@bot.message_handler(commands=['start'])
def welcome(message):
    sti = open('welcome.webp', 'rb')
    bot.send_sticker(message.chat.id, sti)

    bot.send_message(message.chat.id,
                     'Hello, my friend! \n I\'m - {1.first_name}! \n'.format(message.from_user, bot.get_me()),
                     parse_mode='html')
    bot.send_message(message.chat.id, 'I can transfer styles from one image to another')
    choice(message)


def choice(message):
    moon = types.InlineKeyboardMarkup(row_width=1)
    man1 = types.InlineKeyboardButton('Getting started with the first nst model', callback_data='start1')
    man2 = types.InlineKeyboardButton('Getting started with the second msg_net model', callback_data='start2')
    man3 = types.InlineKeyboardButton('See an example', callback_data='look')

    moon.add(man1, man2, man3)

    bot.send_message(message.chat.id, 'You can see an example, or get started', reply_markup=moon)


@bot.callback_query_handler(func=lambda call: True)
def callback_worker(call):
    if call.data == 'start1' or call.data == 'start2':
        bot.send_message(call.message.chat.id, 'Upload the first picture')
        bot.register_next_step_handler(call.message, handle_photo_content, call.data)
    elif call.data == 'look':
        bot.send_message(call.message.chat.id, 'The bot asks \'Upload the first picture\'. We upload a picture on which we want to apply a new style')
        bot.send_photo(call.message.chat.id, photo=open("media/example_content_img.jpg", 'rb'))
        bot.send_message(call.message.chat.id, 'Next, the bot asks \'Upload a style picture\'. We upload the second image already with the style')
        bot.send_photo(call.message.chat.id, photo=open("media/example_style_img.jpg", 'rb'))
        bot.send_message(call.message.chat.id, 'After some waiting, the bot displays a picture with the transferred style to us')
        bot.send_photo(call.message.chat.id, photo=open("media/example_output_img.jpg", 'rb'))
        bot.send_message(call.message.chat.id, 'That all')
        choice(call.message)


@bot.message_handler(content_types=['photo'])
def handle_photo_content(message, command):
    file_info = bot.get_file(message.photo[-1].file_id)
    downloaded_file = bot.download_file(file_info.file_path)
    src = os.path.join(os.getcwd(), 'media', 'content_input.jpg')
    with open(src, 'wb') as new_file:
        new_file.write(downloaded_file)
    bot.send_message(message.chat.id, "Upload a style picture")
    bot.register_next_step_handler(message, handle_photo_style, command)


def handle_photo_style(message, command):
    file_info = bot.get_file(message.photo[-1].file_id)
    downloaded_file = bot.download_file(file_info.file_path)
    src = os.path.join(os.getcwd(), 'media', 'style_input.jpg')
    with open(src, 'wb') as new_file:
        new_file.write(downloaded_file)
    bot.send_message(message.chat.id, "The process has started...")
    if command == 'start1':
        nst_model()
        bot.send_photo(message.chat.id, photo=open(src_output, 'rb'))
    if command == 'start2':
        msg_net_processing(msg_net=msg_net, content=src_input, style=src_style, image=src_output)
        bot.send_photo(message.chat.id, photo=open(src_output, 'rb'))
    choice(message)


# RUN
bot.polling(none_stop=True, interval=0)
