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

from npcs import *
from dialogue import *


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
                ###Combat here!!!
        prints("You're suddenly assaulted by a skeleton! Type \"look skeleton\" to learn more about this enemy.",.3)
                ##skeleton image/desc
        prints("Try to take a swing at the skeleton. Type, \"attack skeleton\" to do battle!")
                #demo successful hit/doesn't kill
                #player gets hit
                #player instructed to block
        prints("Quick! Defend yourself! Type, \"block skeleton\" to try to block its next attack.", .3) 
                #end the fight 
        prints("Try as you might, the Skeleton overpowers you. You try to block its swing, to no avail.",.3)

        prints("...The skeleton delivers a powerful swing to the side of your temple. \n " , 3)
        
        prints("",.3)


        you_have_died()
        prints("",.3)

        #Player should lose this fight and die once so that they can respawn/talk to Old Greg and realize they can't die


        
        prints("", .3)
        prints(" \"My Gods!,\" Old Greg exclaims, \"You're...back! I watched you die!\" ")

        prints("...You were standing there. You felt yourself die, and yet...",.3)

        prints("The skeleton is once again advancing towards you. How is any of this possible?",.3)

        # playeer can kill skeleton now

        prints("\"Well I'll be damned,\" Old Greg exclaims,\"My old heart can't take this kind of excitement.\" ",.3)
        prints("",.3)
        prints("\"Friend, I think you've earned yourself a hot meal. Thanks for saving me.\"",.3)

        #go to tavern


def dialogue_tutorial():
     
    #move to hamlet

        #move to tavern
    
    prints("----LATER AT THE TAVERN---- ", .3)
    prints("",.3)

    prints("####################################################################",.3)
    prints("",.3)

    prints("",.3)
    tavern_title_ascii()
    prints("",.3)
    tavern_ascii()
    prints("##################################################################### ", .3)
    prints("",.3)
    
    prints("",.3)
    prints("    You are terribly confused. You felt yourself die. You felt the light in yourself fade ", .3)
    prints("like a candle blown out by a draft. It was time to seek some answers. More importantly, ",.3)
    prints("you could use a little bit of sustenance.",.3)
    prints("",.3)

    innkeeper_dialogue()


    print("Entering the Tavern!")
    
    the_tavern = location.Location("The Tavern", "A warm and inviting location.", "hnh_forestTheme_conceptQ.mp3",[item("barstool")], ["Upstairs", "Cellar", "The Hamlet"], [])

    