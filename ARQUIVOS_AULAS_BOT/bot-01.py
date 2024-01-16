import telebot, csv
# from decouple import config
from telebot import types
import requests

bot = telebot.TeleBot(token='SEU_TOKEN_TELEGRAM', parse_mode='HTML')


def salvar(id_telegram):
    with open('ids_telegram.csv', 'a') as ids:
        e = csv.writer(ids)
        e.writerow([id_telegram])

@bot.message_handler(commands=['start', 'inicio', 'menu'])
def start(message):
    salvar(message.from_user.id)
    bot.send_message(message.chat.id, 'Olá, tudo bom ?')

@bot.message_handler(commands=['download'])
def download(message):
    doc = open('teste.pdf', 'rb')
    bot.send_document(message.chat.id, doc)

bot.polling()
