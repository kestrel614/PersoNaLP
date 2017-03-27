#!/usr/bin/env python

# -*- coding: utf-8 -*-
"""

This script is a barebone demo of the Python library ChatterBot (http://chatterbot.readthedocs.io/en/stable/).

"""

from chatterbot import ChatBot
from chatterbot.trainers import ChatterBotCorpusTrainer
from chatterbot.trainers import ListTrainer
#import sys;reload(sys);sys.setdefaultencoding('utf8')

basicBot = ChatBot("JonDoe")
basicBot.set_trainer(ChatterBotCorpusTrainer)
basicBot.train("chatterbot.corpus.english")
basicBot.set_trainer(ListTrainer)

basicBot.train([
    "My God, you're shot.",
    "Yes.",
    "Who did this to you?",
    "I did, I think.",
])

print(basicBot.get_response("Hello"))
print(basicBot.get_response("Who did this to you?"))
