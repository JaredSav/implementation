#!/usr/bin/python3

from random import *

def light():
    global L
    L = randint(20000, 90000)   # direct sunlight is between the range of 32k to 100k lux
    return L

light()

