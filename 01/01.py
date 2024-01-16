import telebot
from telebot import types
import requests

bot = telebot.TeleBot(token='6174988485:AAEjYdZArdNtM7VUjsFw3hbjegmrrDRxsFk', parse_mode='HTML')


#$ 1. TUTORIAL: Chat Bot com Inteligência Artifical
#$ https://thispersondoesnotexist.com/
@bot.message_handler(commands=['start'])
def handler_start(message):
    markup = types.InlineKeyboardMarkup()
    markup.add(
        types.InlineKeyboardButton('●APLICATIVOS',callback_data='/chatbot generate image'),
        types.InlineKeyboardButton('●ᗰᗩᑌᐯᗩᗞᗩᝪ [ᝪᖴᏆᑕᏆᗩᏞ]', url='https://t.me/+DRxQVrgDJP0zYWUx'),
        types.InlineKeyboardButton('●GRUPO', url='https://t.me/maud4vpn'),
        types.InlineKeyboardButton('Ⓜ️MAUVADAO', url='https://wa.me/message/J3LNJ5UBNVR3B1'),


        row_width=3
    )
    
    bot.send_message(chat_id=message.from_user.id, text='<b>Sr(a) {}</b> escolha uma das opções abaixo:'.format(message.from_user.first_name), reply_markup=markup, reply_to_message_id=message.message_id)


    

bot.polling()

