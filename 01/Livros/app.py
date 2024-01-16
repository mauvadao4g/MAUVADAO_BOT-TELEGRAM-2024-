import telebot
from telebot import types

bot = telebot.TeleBot(token='6174988485:AAEjYdZArdNtM7VUjsFw3hbjegmrrDRxsFk', parse_mode='HTML')


#$ 1. TUTORIAL: Markups
@bot.message_handler(commands=['start'])
def handler_start(message):
    markup = types.InlineKeyboardMarkup()
    markup.add(
        types.InlineKeyboardButton('📚 Livros',callback_data='/chatbot livros'),
        types.InlineKeyboardButton('Acesse: https://lelivros.love/', url='https://lelivros.love/'),
        row_width=1
    )
    bot.send_message(chat_id=message.from_user.id, text='<b>Sr(a) {}</b> bem vindo escolha uma das opções abaixo:'.format(message.from_user.first_name), reply_to_message_id=message.message_id, reply_markup=markup)



#$ 2. TUTORIAL: Callback Data
@bot.callback_query_handler(func=lambda call: True)
def callback_handler(call):
    if call.data == '/chatbot livros':
        #$ Action: Typing(Digitando...)
        bot.send_chat_action(chat_id=call.from_user.id, action='typing')
        bot.delete_message(chat_id=call.from_user.id, message_id=call.message.message_id)
        
        markup = types.InlineKeyboardMarkup()
        markup.add(
            types.InlineKeyboardButton('📚 1. A Unica Coisa - Gary Keller', callback_data='/chatbot "A Unica Coisa - Gary Keller"'),
            types.InlineKeyboardButton('📚 2. Como Fazer Amigos e Influenciar Pessoas Dale Carnegie', callback_data='/chatbot "Como Fazer Amigos e Influenciar Pessoas Dale Carnegie"'),
            row_width=1
        )
        
        bot.send_message(chat_id=call.from_user.id, text='<b>Sr(a) {}</b> escolha uma dos livros abaixo:'.format(call.from_user.first_name), reply_markup=markup)
        
    elif call.data == '/chatbot "A Unica Coisa - Gary Keller"':
        #$ Action: Typing(Digitando...)
        bot.send_chat_action(chat_id=call.from_user.id, action='typing')
        bot.delete_message(chat_id=call.from_user.id, message_id=call.message.message_id)
        
        markup = types.InlineKeyboardMarkup()
        markup.add(
            types.InlineKeyboardButton('⬅️ Voltar', callback_data='/chatbot voltar')
        )
        
        bot.send_document(chat_id=call.from_user.id, document=open('livros/A Unica Coisa - o Foco Pode Tra - Gary Keller.pdf', 'rb'), caption='📚 <b>Livro escolhido:</b> <i>A Unica Coisa - o Foco Pode Tra - Gary Keller.pdf</i>', reply_markup=markup)

    elif call.data == '/chatbot "Como Fazer Amigos e Influenciar Pessoas Dale Carnegie"':
        #$ Action: Typing(Digitando...)
        bot.send_chat_action(chat_id=call.from_user.id, action='typing')
        bot.delete_message(chat_id=call.from_user.id, message_id=call.message.message_id)
        
        markup = types.InlineKeyboardMarkup()
        markup.add(
            types.InlineKeyboardButton('⬅️ Voltar', callback_data='/chatbot voltar')
        )
        
        bot.send_document(chat_id=call.from_user.id, document=open('livros/Como-Fazer-Amigos-e-Influenciar-Pessoas-Dale-Carnegie.pdf', 'rb'), caption='📚 <b>Livro escolhido:</b> <i>Como Fazer Amigos e Influenciar Pessoas Dale Carnegie.pdf</i>', reply_markup=markup)

        

    elif call.data == '/chatbot voltar':
        #$ Action: Typing(Digitando...)
        bot.send_chat_action(chat_id=call.from_user.id, action='typing')
        bot.delete_message(chat_id=call.from_user.id, message_id=call.message.message_id)
        
        markup = types.InlineKeyboardMarkup()
        markup.add(
            types.InlineKeyboardButton('📚 Livros',callback_data='/chatbot livros'),
            types.InlineKeyboardButton('Acesse: https://lelivros.love/', url='https://lelivros.love/'),
            row_width=1
        )
        bot.send_message(chat_id=call.from_user.id, text='<b>Sr(a) {}</b> bem vindo escolha uma das opções abaixo:'.format(call.from_user.first_name), reply_markup=markup)

        
        
bot.polling()

