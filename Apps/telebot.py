import time
import telepot

from telepot.loop import MessageLoop

token = 'seu-token-do-telegram'
bot = telepot.Bot(token)
frases = {
    'bom': 'Pq bom?\nO que tem de bom?',
    'ruim': 'WOW, pq esse negativismo cara?',
    'zueira': 'Você acha que é zueiro? Não me conheço'
}


def processa_mensagem(mensagem):
    if 'bom' in mensagem:
        resposta = frases['bom']
    elif 'ruim' in mensagem:
        resposta = frases['ruim']
    elif 'zueira' in mensagem:
        resposta = frases['zueira']
    return resposta


def manipula_mensagem(objeto_mensagem):
    print('\nUpdate recebido > {}'.format(objeto_mensagem))
    
    mensagem = objeto_mensagem['text'].lower()
    id_chat = objeto_mensagem['chat']['id']
    
    print('Mensagem enviada pelo usuário <-- {}'.format(mensagem))
    resposta = processa_mensagem(mensagem)
    bot.sendMessage(id_chat, resposta)


MessageLoop(bot, manipula_mensagem).run_as_thread()

while True:
    time.sleep(1)