import telebot

bot = telebot.TeleBot(token='SEU_TOKEN_TELEGRAM', parse_mode='HTML')


bot.send_message(ID_USUARIO, ' Opa, tudo certo ?\n \
Olhe os preços que tenho pra você')

bot.send_message(ID_USUARIO, text='🔰CLOUDFRONT OFF❌️🔰 \
\nVIVO 🔵 \
\nTIM  🔵 \
\nCLARO 🔴❌️❌️❌️ \
\nFLUK🟡 ⁉️⁉️ \
\nVALOR DO PAINEL  ACESSO POR MÊS . \
\n• 🛒5 LONGS  25,00$🇧🇷 \
\n• 🛒10 LONGS  35,00$🇧🇷 \
\n• 🛒20 LONGS  45,00$🇧🇷 \
\n• 🛒30 LONGS  50,00$🇧🇷 \
\n• 🛒50 LONGS   60,00$ 🇧🇷 \
\n• 🛒60 LONGS   70,00$🇧🇷 \
\n• 🛒70 LONGS   80,00$🇧🇷 \
\n• 🛒80 LONGS   90,00$🇧🇷 \
\n• 🛒100LONGS 100,00$🇧🇷 \
\n• 🛒130LONGS 130,00$🇧🇷 \
\n• 🛒160LONGS 160,00$🇧🇷 \
\n• 🛒200LONGS 220,00$🇧🇷 \
\n• 🛒250LONGS 230,00$🇧🇷 \
\n• 🛒300LONGS 250,00$🇧🇷 \
\n• (+100 Login Ganha App com seu tema e sua logo) \
                     \n\nEi!!!\nTu gostou \nMe chama pra contratar: @mauvadao')






#  fazendo download de um arquivo 

bot.send_message(ID_USUARIO, 'Baixe o aplicativo e crie um tese')
doc = open('teste.pdf', 'rb')
bot.send_document(ID_USUARIO, doc)
