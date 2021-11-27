#!/usr/bin/env python3
import location
import player
from prints import printr
from prints import prints
import console
from item import item
from dialogue import *
from tutorial import *
from ascii_art import *
import pandas as pd  
#setup


def old_greg_dialogue():

    def old_greg_image():
            
        prints("@@@&@&&@@&&@&@@&@&@@@@&@@@&@@@@@& .    .     .       .      %@@@@@@@@&&@&&@@&&&&")
        prints("&&&&&@&&@&&@&&@@@&@&@&&@&&@&&@@@&  . .     . .. ....       . &&&&&@@&&@&&&&&@@&@")
        prints("&@&&&@&&@&&&&&@&&&@&&&&&%&&&@@@&&. . .            . .      .   . /*/*/*//*/////(")
        prints("&&&&&@&&&@&&&&@&&&&&&&.*************#&#%###(**,, ..    .   .%%//////*///*///////")
        prints("&@@&@@&&&@&&&&&@&***,*/********/(%&#%#(#####%%%##%#%#%(###%%%###((/******/*/////")
        prints("@@&&&&@&@&@&&,***,**,***,**,**(((##&#%(###%%##%#%###((/%%####%%((///*******/((&@")
        prints("&&&&&&&&&&&&@//*******/*//*/*(#(/#%%%%(((##(####(((#(((((###((##(//*//*/*//&&@&&")
        prints("&&&&&&&&&&&%&@/*************/%%#/#%&%(#(//(((((#(/((((//##(#/#((%/*/*///(&&&&&&@")
        prints("&&&&&&&&&&&&&@&&&&&/**/*/***//#%*/#(/*/(///(((((**///(//*/#((*/(//&&&&&@&&&&&&@@")
        prints("&&&&&&@&&&&&&&@&&&&&&&(/(**//*/((////(///*//**//*,/,*****,,*(,/&@&@&&&@&&&&@@@@&")
        prints("@&&&&&&&&&&&&&@&&@&&&&&&&&&/////(//(/(//*//(%/*/**/**%/*,**(*/&&&&&&&&&@&&&&&@@@")
        prints("%&&&&%&@&&&&&&&&&&&&&&@&&&&&&&&&&(((*//*/(((#(#((////#%(/*/#&@@&@&@@@@@&&&@&&&&&")
        prints("&&&&&&&&&&&&@&&&@&&&@&@@&&&&&&&&&&&%*(*#(##@&&#((((#%#(%(*/&&@&@@@@&&&@@&&&&&@&&")
        prints("&&&&&&&&&&&&&&&&&&&&&@&&&&&&&&&&&&&&&/*/*(/((/(/((**/**//*&@&&&&@&&&@&&&&&&@@&&&")
        prints("&&%&&&&&&&&&&&&&&&&&@&&&&@&&&&&@&&&&,%/*//////*/********,.. *&&&&&@&@&@@@@@&@&&&")
        prints("&&%%&&&&&&&&&&&@&&&&&%&&&&&&&&&&&&.../&##%*/(//(///**((..   . .   /&&&&&&@&&&&&&")
        prints("&&&&&&%&&&&&&&&&%&&&&&&&%&&#...........&%%###%%%&%#%....   . .   ..    .&@@&&%&&")
        prints("%&&&&&&&&&&&&&&&&&&&&&%... . ....... .. .#%#&&%&&%..    .         ..      .  (&&")
        prints("%%&&&%%&&&&&&&&&&%.... ....... .  ......  . #&%,.  .      .  .    .    .   . . (")
        prints("&&&&%%&&&&&%&%& . . . ..  ... ...  ...   ..  %*       .                .        ")
        prints("%%%&%&&&%&&&.. .  . ..      .....    .      ..                       .     .    ")
        prints("#R#$%$#%$#%%                                                                    ")
        prints("#$#$%$%#$%#$                             OLD GREG                               ")

    old_greg_image()
    
    #Common questions
    common_qs = ["Who are you?", "Where are you from?", "What are you doing here?"]

    prints("Forgive me for not recognizing you at first... You look like one of them! " ,2)
    prints("",.3)
    prints("The stranger points to your clothing. You're not wearing much. Your body is barely covered by some tattered robes.  ",2)
    prints("",.3)
    prints("You start to wonder why it seems like this stranger isn't afraid of you. More importantly, you're wondering what in the" , 2)
    prints("seven hells is going! ", 2)
    prints("", .3)
    
    dialogue_options = [
    "     Why aren't you afraid of me?", 
    "     Who are you?", 
    "     Where are we?",
    "     Goodbye."
    ]

    dialogue_outcome = [
        "   \"Should I be, lad? You look ghastly.\" ", 
        "   \"My name is Old Greg. I'm the gravekeeper for the people of the hamlet.\" ",
        "   \"Not far from the hamlet. This here's an outcropping of woods just beyond our borders.\" ",
        "   \"See you later! \" "
            ]
        
    dialogue(dialogue_options, dialogue_outcome)

def innkeeper_dialogue():

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
    innkeeper_image()
    prints("",.3)

    dialogue_options = [
    "   What is your name?",
    "   What do you do here?",
    "   Is something wrong with my face?",
    "   Old Greg mentioned I might be able to help you.",
    "   I have another question...",
    "   Goodbye."

    ]

    dialogue_outcome = [
        "   \"My name is Bremilda Aleheart, stranger. Please to...er...meet you.\" ",
        "   \"What does it look like I do here! I run this inn. It's a lot of work.\" ",
        "   \"Well I didn't want to be the one to tell you! You don't look...great...\" ",
        "   \"There have been plenty of things gone wrong around here lately. Where to even start? \" ",
        "   \"I might have another answer...\" ",
        "   \"Please enjoy your stay! No loitering. Order or get out! \" "

    ]
    

    dialogue(dialogue_options, dialogue_outcome)


def trade(target_npc):

    if target_npc == "innkeeper":
        prints("",.3)
        prints("We've got all kinds of things.")
        prints("",.3)

            
    
    trade_inv = {
    "LEVEL": [1, 1, 2, 1],
    "HP": [0, 0, 0, 0],
    "MAG": [1, 0, 0, 0],
    "DEX": [1, 0, 0, 0],
    "GP": [5, 5, 10, 4]

    }

    trade_df = pd.DataFrame(trade_inv, index = ["Sword", "Tower Shield", "Leather Armor", "Leather Helmet"])

    prints(trade_df, .3) 


#old_greg_dialogue()
#innkeeper_dialogue()

#old_greg_dialogue()
#innkeeper_dialogue()
