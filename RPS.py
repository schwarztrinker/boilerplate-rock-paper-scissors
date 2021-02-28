# The example function below keeps track of the opponent's history and plays whatever the opponent played two plays ago. It is not a very good player so you will need to change the code to pass the challenge.
import tensorflow as tf
from tensorflow.keras.layers.experimental import preprocessing

import numpy as np
import os
import time




    

def player(prev_play, opponent_history=[]):
    opponent_history.append(prev_play)

    #safePlayToFile('quincy.txt', prev_play)

    guess = "R"
    if len(opponent_history) > 2:
        guess = opponent_history[-2]

    return guess


# Function for saving plays of the opponent to a file
def safePlayToFile(filename, prev_play):
    outF = open(filename, "a")
    outF.write(prev_play)
    outF.close()