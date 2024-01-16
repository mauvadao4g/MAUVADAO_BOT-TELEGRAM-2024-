import telebot
import requests, json

bot = telebot.TeleBot(token='SEU_TOKEN_TELEGRAM', parse_mode='HTML')


#$ 1. TUTORIAL: --> register_next_step_handler()
@bot.message_handler(commands=['start'])
def handler_start(message):
    bot.send_message(chat_id=message.from_user.id, text='<b>Sr(a) {}</b> digite seu cep abaixo:'.format(message.from_user.first_name),reply_to_message_id=message.message_id)
    bot.register_next_step_handler(message,cep)


def cep(message):
    try:
        cep_digitado_pelo_usuario = int(message.text)
        
        request = requests.get('https://viacep.com.br/ws/{}/json/'.format(str(cep_digitado_pelo_usuario)))
        if request.status_code == 200:
            dicionario = json.loads(request.content.decode('utf-8'))
            
            mensagem = """<b>cep:</b> {},
<b>logradouro:</b> {},
<b>complemento:</b> {},
<b>bairro:</b> {},
<b>localidade:</b> {},
<b>uf:</b> {},
<b>ibge:</b> {},
<b>gia:</b> {},
<b>ddd:</b> {},
<b>siafi:</b> {},


            """
            
            bot.send_message(chat_id=message.from_user.id, text=mensagem.format(dicionario['cep'], 
                                                                                dicionario['logradouro'],
                                                                                '🚫' if dicionario['complemento'] == '' else dicionario['complemento'],
                                                                                '🚫' if dicionario['bairro'] == '' else dicionario['bairro'],
                                                                                '🚫' if dicionario['localidade'] == '' else dicionario['localidade'],
                                                                                '🚫' if dicionario['uf'] == '' else dicionario['uf'],
                                                                                '🚫' if dicionario['ibge'] == '' else dicionario['ibge'],
                                                                                '🚫' if dicionario['gia'] == '' else dicionario['gia'],
                                                                                '🚫' if dicionario['ddd'] == '' else dicionario['ddd'],
                                                                                '🚫' if dicionario['siafi'] == '' else dicionario['siafi']), reply_to_message_id=message.message_id)
        else:
            bot.send_message(chat_id=message.from_user.id, text='🚫 Informações Incorretas, Informa um cep válido...', reply_to_message_id=message.message_id)
    
    except:
        bot.send_message(chat_id=message.from_user.id, text='🚫 Informações Incorretas, Informa um cep válido...', reply_to_message_id=message.message_id)
    


bot.polling()

