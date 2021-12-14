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

    prints(f"Suddenly, you are awake. You feel your head thump against the ground as you are being dragged. ", 3)
    prints("",.3)


    prints("\"You're awake! Oh! That's incredible. Just incredible...\" ",3)
    prints("",.3)
    prints("...The voice pauses, coughing and grunting as he lets go of your leg. ", 3)
    prints("",.3)
    prints("\"Forgive me friend, I thought you were dead! You understand...\" ", 2)
    prints("",.3)
    prints("You feel a hand reach down and hoist you two your feet. You're a little caught off guard! ", 3)
    prints("",.3)
    prints(f"\"Wait...no...it can't be! Are you?...????? " , 4)
    prints("",.3)


    #old_greg_dialogue()
