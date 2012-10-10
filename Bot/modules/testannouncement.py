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
    _bot.write_packet(ID.HON_CS_WHISPER, 'auph', 'TESTTESTTEST')
	#_bot.write_packet(ID.HON_CS_GLOBAL_MESSAGE,'Greetings! Kick an early start into ^oHalloween^* with ^079Hook Madman^* and ^079Karabas Barabas Puppet Master^* at just ^y390 Gold Coins^* each! Grab them from my Store now!')
    # 10 = 10 seconds #
    threading.Timer(3600, periodic).start()

def announce(bot,input):
    if not input.admin:
        return False
    bot.write_packet(ID.HON_CS_GLOBAL_MESSAGE,input.group(2))
announce.commands = ['announce']
