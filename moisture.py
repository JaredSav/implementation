#!/usr/bin/python3

from random import *

def moisture():             # best range is between .4 and .5
    global M
    items = [.2, .3, .4, .5, .6, .7, .8]
    X = sample(items, 1)  #Get random number from the items list
    M = X[0]
    return M           # return current Soil moisture level

moisture()

