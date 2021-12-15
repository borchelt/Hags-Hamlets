#!/usr/bin/env python3
import location
import player
from prints import printr
from prints import prints
import console
from item import item
from you_have_died import *

from dialogue import *
from npcs import npc
from ascii_art import * 
import enemy
#from console import * 
#setup


def tutorial():
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
    prints(" \"In all my years, I've never see anything like— \"", .3)
    prints(".....", 1)
    prints(".........", 1)
    prints(" \"AHHHHHHHHHHHHHH!!!!!,\" Old Greg screams as several corpses start writhing in the pile behind you.", .3)
    prints(" ")

def combat_tutorial_zone():
        
        prints(f" \"Well, I sure hope you're able to fight!,\" he calls to you. ", .3)
        prints(" \"Quick! Grab a weapon or neither of us are making it back to the hamlet!", .3)
        
        prints("##### WELCOME TO THE COMBAT TUTORIAL. Here you will learn how to be a great warrior!",.3)
        prints("",.3)
        prints("        ##### At the beginning of each combat, you'll be facing off against an enemy.")
    
        prints("You're suddenly assaulted by a skeleton!",.3)
        prints("    ##### Type \"look skeleton\" to learn more about this enemy.",.3)

        
        def examine_enemy():

            look_skeleton = input(printr(">> "))

            if look_skeleton == "look skeleton" or "look at skeleton": 
                for i in range(0,20):
                    print("")
                skeleton_ascii()
                
                #HOW TO READ INFO ABOUT ENEMIES
                prints("Here you can learn all you need to know about the skeleton.")
                prints("1. it doesn't bleed")
                prints("2. you can still kill it")

            else:
                prints("Type \"look skeleton\" to learn more about this enemy.",.3)
                examine_enemy()
        
        examine_enemy()

        prints("You'll need a weapon to defeat the skeleton. You see a spear sticking into an old stump.",.3)
        prints("Try to take the Old Spear.",.3)
        prints("    #### Type \'take the old spear\' to take it.",.3)

        def take_spear():
            take_the_spear = input(printr(">> "))
            if take_the_spear == "take the old spear":
                print("You've taken the spear.")
        take_spear()
        prints("",.3)
        prints("Now you'll want to equip the spear.")
        prints("    #### Type \'equip old spear\' to equip it.")
        prints("",.3)

        def babys_first_weapon():
            equip_spear = input(printr(">> "))
            if equip_spear == "equip old spear":
                print("You have equipped the spear.")
            else:
                print("Equip the weapon to fight the skeleton. Type \'equip old spear' to equip it.")
                babys_first_weapon()
        
        babys_first_weapon()


        prints("Try to take a swing at the skeleton. ",.3)
        prints("    #### Type, \"attack skeleton\" to do battle!",.3)

        def first_attack():
            first_swing = input(printr(">> "))
            if first_swing == "attack skeleton":
                prints("You thrust your old spear at the skeleton.")
                prints("...",.3)
                prints("...It hits! You deal 4 damage.",.3)
            else:
                prints("Do battle! Type \'attack skeleton\' to defeat your foe.")
                first_attack()
        
        first_attack()

        prints("The skeleton is not deterred. It swipes at your feet!")
        prints("...",.3)
        prints("...It hits! The skeleton deals 3 damage to you.")
        prints("",.3)
        


                #demo successful hit/doesn't kill
                #player gets hit
                #player instructed to block
        prints("Quick! Defend yourself! ",.3)
        prints("    #### Type, \"block\" to try to block its next attack.", .3) 
        def first_block():
            block = input(printr(">> "))
            if block == "block":
                prints("you focus on blocking this next attack")            
            else:
                prints("Type \"block\" to block the incoming attack")
                first_block()
        first_block()
        prints("",.3)
        prints("The skeleton lunges at you with it's bone shard.",.3)
        prints("...")
        prints("...You successfully blocked the attack!",.3)
        prints("",.3)


        
        

        prints("",.3)
                #end the fight
        
        def lose_the_fight():

            prints("Try as you might, the Skeleton overpowers you.",.3)
            prints("...The skeleton delivers a powerful swing to the side of your temple. \n " , 3)
            
            prints("",.3)
            you_have_died()
            prints("",.3)
        
        lose_the_fight()



        #Player should lose this fight and die once so that they can respawn/talk to Old Greg and realize they can't die


        
        prints("", .3)
        prints(" \"My Gods!,\" Old Greg exclaims, \"You're...back! I watched you die!\" ")

        prints("...You were standing there. You felt yourself die, and yet...",.3)
        prints("",.3)
        prints("The skeleton is once again advancing towards you. How is any of this possible?",.3)
        prints("",.3)
        prints("You aren't able to let yourself remain confused for long. Several more shapes begin to emerge from the fog.",.3)
        prints("Several skeletons have joined the other. They are all coming towards you, shambling and making all sorts of horrid sounds.",.3)
        
        prints("",.3)

        prints("Old Greg screams, \"Oh my Gods! Run lad, run!!!\" No sooner, Old Greg is sprinting down the path out of the graveyard.",.3)
        prints("      #### Type 'flee' to escape the skeleton horde.")

        def first_runaway():
            run = input(printr(">> "))
            if run == "flee":
                prints("The skeletons swipe at you, but miss. You follow Old Greg down the path.")
            else:
                prints("Escape with Old Greg. Type \"run away\" to flee the skeleton horde.",.3)
        
        first_runaway()

        prints("\"Well I'll be damned,\" Old Greg exclaims,\"My old heart can't take this kind of excitement.\" ",.3)
        prints("You both take a moment to catch your breath.",.3)
        prints("",.3)
        prints("\"Friend, I think you've earned yourself a hot meal. Thanks for saving me.\"",.3)

        #go to tavern


def dialogue_tutorial(player):
    
    def innkeeper_image():
        prints("................................................................................")
        prints(".......................... . . . . . . . . . . .................................")
        prints("............... ..                ##%%%&&%%%##(.          ......................")
        prints("***//(///*,,....   ... . .     /%%%#%&%%&&&%(####/,      . . ...................")
        prints("(((((((((((((/**,....         ,%&%%##((((#%&%(###(#/.      .....,,***//(/((/////")
        prints("((((((((((((((((((//*,,...    #%##((//******#%#*(#(#((,,,,,**/(((((#############")
        prints("((((((((((((((((//////((/*,,*#&%%((///*****,*(%((#((#((((((((((((((#############")
        prints("((((((((((((((/(((((/(//////#%&%%((//******,*/####/###/(((((((((((##############")
        prints("((((((((((//////////////(((#%&&&%#(///(#/**/((#%(#/##%(#(((((((((((#############")
        prints("///////////***************#&&&@&#((##((((**/(#&&(##%%&&%#**/////((((((((((((((((")
        prints("////////////*************(#&&&@&%(/***/(/*,**/#%#(#(%@%&%/*******///////////////")
        prints("///////////********,,,,,*(%%&@@@@((/*/(#((//**/#%((%&&&&%%(,,**************/*///")
        prints("***************,,,,,,,,,*(%&&@@@@((/////(//***/#&&%%&&%&%&/,,*******************")
        prints("****************,,,,,,,,,*#%&@@@@@(((//(///***(%&&&&&%%%&#*******************///")
        prints("******************,,,,,,,,,,(#(//(((#((//*,*/(@@@@&&&%%%%%****************//////")
        prints("********************,,,,,,,,,,,,,,(#(######%&&@@&&%&%%%%***************/////////")
        prints("///////*****************,,,,,,,,*(((((((###%%&&&&%%&@%***************///////////")
        prints("////////////*************&&&&&#((((((((((((#((//(/**************////////////////")
        prints("////////////////**%&&&&&&&&&&&&&(((((((//////************(@%%%(///////////////((")
        prints("///////////////&&&&&&&&&&&&&&&&&&(////***/********,,,,,,,/(%&&%%%(///////(/(((((")
        prints("((((/////////#&&&&&&&&&&&&&&&&&&&&&(***********,,,,,,,,,,*&&&&&&&&#(((((((((((((")
        prints("((((((((((((/&&&&&&&&&&&&&&&&&&&&&&&&&******,,,,,,,,,,,,/&&&&&&&&&&#((((((((((((")
        prints("")


    def inkeeper_intro():
        prints("")
        prints("She smiles somewhat uncomfortably at you as you step over to the bar", 1)
        prints("\"well, stranger, what can I get for ya? You saved my Pa. You can have damn well whatever you please!\"", 2)
        prints("")


    keep_dialogue_options = [
    "   What is your name?",
    "   What do you do here?",
    "   Is something wrong with my face?",
    "   Old Greg mentioned I might be able to help you.",
    "   I have another question...",
    "   Goodbye."

    ]

    keep_dialogue_outcomes = [
        "   \"My name is Bremilda Aleheart, stranger. Please to...er...meet you.\" ",
        "   \"What does it look like I do here! I run this inn. It's a lot of work.\" ",
        "   \"Well I didn't want to be the one to tell you! You don't look...great...\" ",
        "   \"There have been plenty of things gone wrong around here lately. Where to even start? \" ",
        "   \"I might have another answer...\" ",
        "   \"Please enjoy your stay! No loitering. Order or get out! \" "

    ]

    innkeeper = npc("Innkeeper", innkeeper_image, inkeeper_intro, keep_dialogue_options, keep_dialogue_outcomes)

    prints("Old Greg leads you back to the Hamlet and the nearby Tavern.",.3)
    prints("You can't help but to take in some of the sights on your path.")
    prints("####Type \'look at the hamlet\' to get your first glimpse of your surroundings.")

    def look_hamlet():
        look_at_hamlet = input(printr(">> "))   
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
    prints("You should try to talk to the innkeeper.")
    prints("    ### Type \"talk to the innkeeper\" to speak with them.",.3)
    
    #player should try to talk to innkeeper
    
    def babys_first_words():
        talk1 = input(printr(">> ")).lower()
            
        if talk1 == "talk to the inkeeper":
            prints("You start talking to the innkeeper.")
            innkeeper.talk(player)
            
        else: 
            prints("Try talking to the innkeeper. Type \"talk to innkeepeer\" to speak with them.",.3)
            babys_first_words()



    babys_first_words()

 
    

    