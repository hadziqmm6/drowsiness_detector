import requests
import os
import json

def send_to_telegram(bot_message):
    bot_token = '928419242:AAH_CzFoPoyFoNCtyExoPBryNsk2YAUvjjE'
    users = "hadziqmm"
    id_bot = "996425882"
    send_text = 'https://api.telegram.org/bot' + bot_token + '/sendMessage?chat_id=' + id_bot + '&parse_mode=Markdown&text=' + bot_message
    response = requests.get(send_text)
    return response.json()





