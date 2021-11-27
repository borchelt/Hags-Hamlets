#!/usr/bin/env python3
import location
import player
from prints import printr
from prints import prints
import console
from item import item
from you_have_died import *

from dialogue import *
from npcs import * 
from ascii_art import * 
import enemy
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
        
        prints("##### WELCOME TO THE COMBAT TUTORIAL. Here you will learn how to be a great warrior!",.3)
        prints("",.3)
        prints("        ##### At the beginning of each combat, you'll be facing off against an enemy.")
    
        prints("You're suddenly assaulted by a skeleton!",.3)
        prints("    ##### Type \"look skeleton\" to learn more about this enemy.",.3)

        
        def examine_enemy():

            look_skeleton = input()

            if look_skeleton == "look skeleton" or "look at skeleton": 
                for i in range(0,20):
                    print("")
                skeleton_ascii()
                
                #HOW TO READ INFO ABOUT ENEMIES
                prints("Here you can learn all you need to know about the skeleton.")
                prints("ALL THESE THINGS ABOUT SKELETONS")

            else:
                prints("Type \"look skeleton\" to learn more about this enemy.",.3)
                examine_enemy()
        
        examine_enemy()

        prints("You'll need a weapon to defeat the skeleton. Try to take the Old Spear.")

        
        def take_spear():
            take_the_spear = input()
            if take_the_spear == "take the spear":
                print("You've taken the spear.") 

        prints("Try to take a swing at the skeleton. ",.3)
        prints("    #### Type, \"attack skeleton\" to do battle!",.3)
        prints("",.3)
                #demo successful hit/doesn't kill
                #player gets hit
                #player instructed to block
        prints("Quick! Defend yourself! ",.3)
        prints("    #### Type, \"block skeleton\" to try to block its next attack.", .3) 
        prints("",.3)
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
        prints("",.3)
        prints("The skeleton is once again advancing towards you. How is any of this possible?",.3)

        # playeer can kill skeleton now

        prints("\"Well I'll be damned,\" Old Greg exclaims,\"My old heart can't take this kind of excitement.\" ",.3)
        prints("",.3)
        prints("\"Friend, I think you've earned yourself a hot meal. Thanks for saving me.\"",.3)

        #go to tavern


def dialogue_tutorial():

    prints("Old Greg leads you back to the Hamlet and the nearby Tavern.",.3)
    prints("You can't help but to take in some of the sights on your path.")
    prints("####Type \'look at the hamlet\' to get your first glimpse of your surroundings.")

    def look_hamlet():
        look_at_hamlet = input()    
        if "look" in look_at_hamlet and "hamlet" in look_at_hamlet:
            prints("The hamlet is a quaint place. There are a few things around you.")
            #full description of hamlet, and teach to examine
            #provides goals
        else:
            prints("Please look at your surroundings. Type \'look at the hamlet\'",.3)
            look_hamlet()

    look_hamlet()
    prints("",.3)
    prints("You arrive at the Tavern.")

    prints("####################################################################",.3)
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

    prints("You approach the bartop, Old Greg in tow. You feel your shoulders drop as you collapse onto the stool.",.3)
    prints("The innkeeper turns around to face you. \"Good heavens stranger! You look a little beat up, don't ya?\" ",.3)
    prints("",.3)
    prints("You should try to talk to the innkeeper. Type \"talk to innkeeper\" to speak with her.")
    
    #player should try to talk to innkeeper
    talk = input()
        
    if talk == "talk to innkeeper":
        prints("You start talking to the innkeeper.")
    
    #innkeeper_dialogue()



    #the_tavern = location.Location("The Tavern", "A warm and inviting location.", "hnh_forestTheme_conceptQ.mp3",[item("barstool")], ["Upstairs", "Cellar", "The Hamlet"], [])

    