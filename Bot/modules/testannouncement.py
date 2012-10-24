# -*- coding: utf8 -*-
from hon.packets import ID
import time, threading
_bot = None

def setup(bot):
    global _bot
    _bot = bot
    #start sending messages after 30 seconds
    threading.Timer(30, periodic).start()

def periodic():
    global _bot
    #_bot.write_packet(ID.HON_CS_GLOBAL_MESSAGE,'We are having an Urgent Maintenance to fix the connectivity issues players are currently experiencing. Game service will not be available until further notice. We apologize for the inconvenience and are working to restore the game service as soon as possible.')
    #_bot.write_packet(ID.HON_CS_WHISPER, 'auph', 'TESTTESTTEST')
    # 10 = 10 seconds #
    threading.Timer(3600, periodic).start()

def announce(bot,input):
    if not input.admin:
        return False
    bot.write_packet(ID.HON_CS_GLOBAL_MESSAGE,input.group(2))
announce.commands = ['announce']
