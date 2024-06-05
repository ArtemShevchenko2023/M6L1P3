import telebot
from conf import *
from gen import *
bot = telebot.TeleBot(token)
@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.reply_to(message, "Привет! Для помощи введи /help")
@bot.message_handler(commands=['help'])
def send_welcome(message):
    bot.reply_to(message, "Вот список моих команд:\n/start - приветствие\n/help - все команды\nНапиши любое сообщение с запросом что хочешь увидеть в изображении!")
@bot.message_handler(func=lambda message: True)
def echo_message(message):
    bot.reply_to(message, "Генерирую картинку...")
    prompt = message.text
    api = Text2ImageAPI(fus, ap, secret)
    api.conv(prompt)
    img = open('decoded.jpg', 'rb')
    bot.send_photo(message.chat.id, img)
bot.infinity_polling()
