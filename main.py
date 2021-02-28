# This entrypoint file to be used in development. Start by reading README.md
from RPS_game import play, mrugesh, abbey, quincy, kris, human, random_player
from RPS import player
from unittest import main

import tensorflow as tf
from tensorflow.keras.layers.experimental import preprocessing

import numpy as np
import os
import time

###
plays = open('quincy.txt', 'rb').read().decode(encoding='utf-8')
print('Length of text: {} characters'.format(len(plays)))
vocab = sorted(set(plays))
print('{} unique characters'.format(len(vocab)))

chars = tf.strings.unicode_split(plays, input_encoding='UTF-8')

###
#play(player, quincy, 5000)
#play(player, abbey, 1000)
#play(player, kris, 1000)
#play(player, mrugesh, 1000)

# Uncomment line below to play interactively against a bot:
# play(human, abbey, 20, verbose=True)

# Uncomment line below to play against a bot that plays randomly:
# play(human, random_player, 1000)



# Uncomment line below to run unit tests automatically
#main(module='test_module', exit=False)