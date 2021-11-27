#!/usr/bin/env python3
import location
import player
from prints import printr
from prints import prints
import console
from item import item
from dialogue import *
from you_have_died import *
#from console import * 
#setup


def tutorial():
    prints(" \"In all my years, I've never see anything like— \"", .3)
    prints(".....", 1)
    prints(".........", 1)
    prints(" \"AHHHHHHHHHHHHHH!!!!!,\" Old Greg screams as several corpses start writhing in the pile behind you. \n ", .3)
    prints("")

def combat_tutorial_zone():
        
        prints(f" \"Well, I sure hope you're able to fight!,\" he calls to you. ", .3)
        prints(" \"Quick! Grab a weapon or neither of us are making it back to the hamlet!", .3)
        
        #equip

        #attack

            #choose move
                #slash
                #stab
                #lunge
                #parry/riposte
                #defend


                
            #deal damage

            #recieve damage


        #stats









        prints("")
        prints("------##### INSERT COMBAT HERE ##### ------", 3)

        prints("You're suddenly assaulted by a skeleton! Type \"look skeleton\" to learn more about this enemy.",.3)
        
        prints("")

        prints("...The skeleton delivers a powerful swing to the side of your temple. \n " , 3)

        you_have_died()
        prints("",.3)
    
        #Player should lose this fight and die once so that they can respawn/talk to Old Greg and realize they can't die

        prints("", .3)
        prints(" \"My Gods!,\" Old Greg exclaims, \"You're...back! I watched you die!\" ")

