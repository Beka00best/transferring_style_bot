import telebot
import config
from telebot import types
from telebot import apihelper

bot = telebot.TeleBot(config.TOKEN)


@bot.message_handler(commands=['start'])
def welcome(message):
    sti = open('/home/bekzat/Beka/transferring_style_bot/welcome.webp', 'rb')
    bot.send_sticker(message.chat.id, sti)

    bot.send_message(message.chat.id, 'Добро пожаловать! \n Я - {1.first_name}! \n Напиши что-нибудь и следуй за '
                                      'инструкциями'.format(message.from_user, bot.get_me()),
                     parse_mode='html')


# RUN
bot.polling(none_stop=True, interval=0)
