import telebot
from conf import *
from gen import *
bot = telebot.TeleBot(token)
@bot.message_handler(commands=['help', 'start', 'gen'])
def send_welcome(message):
    bot.reply_to(message, "hello")
    # prompt = message.text
    # api = Text2ImageAPI(fus, ap, secret)
    # api.conv(prompt)
    # img = open('C:\Users\user\Desktop\AtomAll\LVL3\M6L1\decoded.jpg', 'rb')
    # bot.send_photo(message.chat.id, img)
@bot.message_handler(func=lambda message: True)
def echo_message(message):
    prompt = message.text
    api = Text2ImageAPI(fus, ap, secret)
    api.conv(prompt)
    img = open('decoded.jpg', 'rb')
    bot.send_photo(message.chat.id, img)
bot.infinity_polling()