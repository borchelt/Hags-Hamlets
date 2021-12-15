#!/usr/bin/env python3
import location
import player
from prints import printr
from prints import prints
import console
from item import item
from dialogue import *
from tutorial import *
from npcs import * 
#setup
        

def play_intro():

    for i in (range(1,160)):
        if i < 33:
            prints("O")
        elif(i < 66):
            prints("o",)
        elif(i<99):
            prints(".",)
        else:
                prints("", .1, False)


    prints(".")
    prints("_", 1)
        
    prints("....", 1)
    prints(".....THUMP!!!...",.1)
    prints(".......", 1)
    prints("..........", 1)
    prints("............THUMP!!!...", 1)
    prints("..............")
    prints("........")
    prints(".....")
    prints("..")
    prints(".")




    #old_greg_dialogue()
