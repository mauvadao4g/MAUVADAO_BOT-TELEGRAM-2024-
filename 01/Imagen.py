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
        types.InlineKeyboardButton('🖼 Gerar Imagem de Pessoa Que Não Existe',callback_data='/chatbot generate image'),
        types.InlineKeyboardButton('Acesse: https://thispersondoesnotexist.com/', url='https://thispersondoesnotexist.com/'),
        row_width=1
    )
    
    bot.send_message(chat_id=message.from_user.id, text='<b>Sr(a) {}</b> escolha uma das opções abaixo:'.format(message.from_user.first_name), reply_markup=markup, reply_to_message_id=message.message_id)


@bot.callback_query_handler(func=lambda call: True)
def callback_handler(call):
    if call.data == '/chatbot generate image':
        #$ ChatAction: Typing(Digitando...)
        bot.send_chat_action(chat_id=call.from_user.id, action='typing')
        bot.delete_message(chat_id=call.from_user.id, message_id=call.message.message_id)
        
        imagem = open('{}_person.png'.format(call.from_user.id),'wb')
        request = requests.get('https://thispersondoesnotexist.com/')
        imagem.write(request.content)
        
        markup = types.InlineKeyboardMarkup()
        markup.add(
            types.InlineKeyboardButton('⬅️ Voltar', callback_data='/chatbot voltar')
        )
        
        bot.send_photo(chat_id=call.from_user.id, photo=open('{}_person.png'.format(call.from_user.id),'rb'),caption='<b>Sr(a) {}</b> Imagem Gerada com Inteligência Artificial'.format(call.from_user.first_name), reply_markup=markup)
    elif call.data == '/chatbot voltar':
        #$ ChatAction: Typing(Digitando...)
        bot.send_chat_action(chat_id=call.from_user.id, action='typing')
        bot.delete_message(chat_id=call.from_user.id, message_id=call.message.message_id)
        
        markup = types.InlineKeyboardMarkup()
        markup.add(
            types.InlineKeyboardButton('🖼 Gerar Imagem de Pessoa Que Não Existe',callback_data='/chatbot generate image'),
            types.InlineKeyboardButton('Acesse: https://thispersondoesnotexist.com/', url='https://thispersondoesnotexist.com/'),
            row_width=1
        )
        
        bot.send_message(chat_id=call.from_user.id, text='<b>Sr(a) {}</b> escolha uma das opções abaixo:'.format(call.from_user.first_name), reply_markup=markup)

        
        
    

bot.polling()

