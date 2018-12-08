#!/usr/bin/python3

from random import *

def temp():             # best growing temps are between 75 and 82 degrees
    global T
    T = randint(65, 90) #Get random number between 65 and 90
    return T            # return current temp

temp()

