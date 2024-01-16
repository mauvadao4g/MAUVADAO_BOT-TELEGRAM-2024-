#!/bin/bash


while true
do

clear
echo "Enviando Notificações via Telegram"
echo ""



#    ENVIANDO AS MSG VIA TELEGRAM
TOTAL=$(cat ids.txt | sort -u | wc -l)



for LISTA in $(cat ids.txt | sort -u)
do

# sed 's/ENVIAR_MSG/'$LISTA'/g' enviar.py > send.py && python3 send.py

sed 's/ENVIAR_MSG/'$LISTA'/g' enviar.py | python3

sleep 0.5



if echo "$LISTA" 
  then
	echo "$LISTA: Enviado"
else
	echo "$LISTA: Erro no envio"
fi



done
#          FIM AO ENVIAR AS MSG



sleep 3
done
