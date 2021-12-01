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

def blacksmith_dialogue():

    blacksmith_ascii()
    prints("")

    dialogue_options = [
    "     *** TRADE *** What do you have for sale?", 
    "     What is your name?", 
    "     What can you tell me about the Hamlet?",
    "     *** QUEST *** Looking for work."
    "     Goodbye."
    ]

    dialogue_outcome = [
        "   \"I have plenty of wares for sale. That is, of course, supposing you've got the coin.\" ", 
        "   \"Sebastien Steelscraper's the name. Pleasure to meet you...er...person.\" ",
        "   \"Well the whole place has gone to shite since the Hags came and lay their curse upon us. Before that we were just a bunch of quiet folk.\" ",
        "   \"The only kind of work I've got right now is less than pleasant. Would you like to hear about it? (Y/N) \" ", 

        "   \"See you later! \" "
            ]
        
        #if player has quest item

        #option
        #"  I have something for you, Sebastien.",
        #outcome 
        #"  My oh my! The silver ore. You must have gone through a lot of trouble to retrieve this. I'll get right to work making the breastplate!"
        
    dialogue(dialogue_options, dialogue_outcome)

def librarian_dialogue():

    librarian_ascii()
    prints("",.3)
    dialogue_options = [
    "     Who are you? ", 
    "     What are doing right now?", 
    "     Where are we?",
    "     What can you tell me about the Hags' Curse?"
    "     Goodbye."
    ]

    dialogue_outcome = [
        "   \"Regina Quillspeth, at your service. Are you here because you're actually interested in books?\" ", 
        "   \"I was studying old magical texts until you came along. Not that I mind the company. No one ever comes here.\" Regina sighs and sits back in her chair a little bit, pouting. ",
        "   \"Where does it look like you are? This is the hamlet library. The monks that once ran this place left behind so much knowledge.\" ",
        "   \"Well, I know that the monks all ran away or were murdered by the Hags. Now it's just me, left to look after all of their years of hard work. Uh...they're evil?\" ",
        "   \"Come back and visit me some time!"

        #gets quest to learn about potion
        #talks to librarian and gets another option

        #"  INSERT NAME told me that you might know where to find a potion recipe? Could you help me?"
        
        #outcome
        #"  \"YES!!!!,\" Regina cheers, jumping from her chair, "I've been waiting for someone to ask me for help like this!\" "

            ]
        
    dialogue(dialogue_options, dialogue_outcome)

def merchant_dialogue():

    merchant_ascii()
    prints("",.3)


    dialogue_options = [
    "     *** TRADE ***  What are you selling, friend? ", 
    "     What is your name?", 
    "     Where are you from?",
    "     What do you know about the Hags' Curse?",
    "     Goodbye."
    ]

    dialogue_outcome = [
        "   \"Many curious things, for the right price.\" ", 
        "   \"My name is Azni.\" ",
        "   \"A place far beyond the borders of the woods.\" ",
        "   \"Curse? What curse?\" Azni looks you up and down, gauging your reaction. He bursts into laughter, \"Hah! They're terrible, but I still must laugh.\" ",
        "   \"Come back anytime, friend. \" "
            ]
        
    dialogue(dialogue_options, dialogue_outcome)

def general_store_owner_dialogue():

    general_store_owner_ascii()
    prints("",.3)

    dialogue_options = [
    "     *** TRADE *** I'd like to see your wares.", 
    "     What is your name?", 
    "     How is business?",
    "     *** QUEST *** Is there anything that you need help with?",
    "     Goodbye."
    ]

    dialogue_outcome = [
        "   \"Of course! I've the best crafting materials in the land.\" ", 
        "   \"Mr. Barry Barrelpine, humbly at your service. Anything you need, anything at all, I will sell it to you!\" ",
        "   \"Fine. Why do you ask? Who have you been talking to?\" ",
        "   \"Okay. Listen...I shouldn't be talking about this, but I owe a lot of money to Hank in the Secret Speakeasy in the Sewers. Could you see about settling my debt for me?\""
        "   \"See you later! \" "
            ]
        
    dialogue(dialogue_options, dialogue_outcome)

def farmer_dialogue():

    farmer_ascii()
    prints("",.3)

    dialogue_options = [
    "     Wait! Stop running! What has happened to you?", 
    "     What is your name?", 
    "     Where is your house?",
    "     What can I do?",
    "     Goodbye."
    ]

    dialogue_outcome = [
        "   \"AHHHH!!! My house! Our house! She came...d-d-destroyed it all! What am I going to do?\" ", 
        "   \"P-P-P-Podrick Pebbleton, s-s-sir. \" ",
        "   \"Back...th-through the fi-field...Over the brook, down the trail past the old Oak for a bit.\" ",
        "   \"Why? Are you some kind of hero? I-I...I...\" Podrick breaks into tears, \"I just want my house back!\" ",
        "   \"I'll be alone in this world forever, it seems.\" "
            ]
        
    dialogue(dialogue_options, dialogue_outcome)

def thief_king_dialogue():

    thief_king_ascii()
    prints("",.3)

    
    dialogue_options = [
    "     Are you the one they call the Thief King?", 
    "     Why do you live in the Sewers?", 
    "     Are you going to let me live?",
    "     Are you working for the Hags?",
    "     *** QUEST *** Any jobs you that need doing?",
    "     Goodbye."
    ]

    dialogue_outcome = [
        "   \"...Is the name not obvious enough?\" ", 
        "   \"I like the way it smells,\" he says with scowl, \"The people of the hamlet don't take kindly to thieves walking about.\" ",
        "   \"Give me a good reason to and I might.\" ",
        "   \"Don't be ridiculous. They can sod right off.\" "
        "   \"There's always work for willing hands. Are you sure you're up to it?",
        "   \"I'll be here.\"."
            ]
        
    dialogue(dialogue_options, dialogue_outcome)

def hunter_dialogue():

    hunter_ascii()
    prints("",.3)

    
    dialogue_options = [
    "     Who are you?", 
    "     What are you doing out here?", 
    "     What do you know about the Hags' Curse?",
    "     *** QUEST *** You look troubled. Can I help you in some way?"
    "     Goodbye."
    ]

    dialogue_outcome = [
        "   \"The name is Arthur. Arthur Edenbough. \" ", 
        "   \"I thought I was going to finally fell that buck. Now you're here.\" ",
        "   \"I've never seen one of them personally, but these woods are teeming with monsters. I don't past the brambles. It's too dark.\" ",
        "   \"I'm so terribly thirsty. If you could bring me a cold beer, I'd be more than happy to share my map with you.\" ", 
        "   \"Happy hunting!\" "
            ]
        
    dialogue(dialogue_options, dialogue_outcome)

def drunkard_dialogue():

    drunkard_ascii()
    prints("",.3)


    dialogue_options = [
    "     Try to wake the drunkard."
    "     Pour his beer on him."
    "     Knock on the table."
    "     Clap loudly."
    "     Leave."
    ]

    dialogue_outcome = [
        "   He keeps snoring. There's no difference. ", 
        "   The drunkard is wet now, but they're still out like a light. ",
        "   You've knocked on the table. The drunkard flatulates loudly, wipes his nose, and keeps sleeping."
        "   The drunkard, in his sleep, claps back."
        "   The drunkard wakes up briefly, and looks around with squinted vision. Seconds later, he falls asleep again. "
            ]
        
    dialogue(dialogue_options, dialogue_outcome)

def dwarven_miner_dialogue():

    dwarven_miner_ascii()
    prints("",.3)


    dialogue_options = [
    "     What is your name?", 
    "     Are you in danger?", 
    "     What can you tell me about these mines?",
    "     *** QUEST *** Would you like my help?"
    "     Goodbye."
    ]

    dialogue_outcome = [
        "   \"Ztolo Zan I my name, stranger. Pleased to make your acquaintance. \" ", 
        "   \"Not particularly. I was, not long ago. Damned cave in....\" ",
        "   \"These mines are some of the oldest in all the land. The tunnels reach all the way to Urzal-ka!\" ",
        "   \"Are you serious? Well, there's been a giant spider causing cave ins lately. Slows up production. Want to make a little money?"
        "   \"See you later! \" "
            ]
        
    dialogue(dialogue_options, dialogue_outcome)

def guard_dialogue():

    guard_ascii(),
    prints("",.3)

    dialogue_options = [
    "     I'm friendly! I swear!", 
    "     What are you doing out here?", 
    "     What can you tell me about where we are?",
    "     Goodbye."
    ]

    dialogue_outcome = [
        "   \"How should we know? Keep your hands off those weapons.\" ", 
        "   \"We are the last of the guard. All of the others have been killed off.\" ",
        "   \"This is our last defense from the outside world. Having the Hags in here with us is hard enough!\" ",
        "   \"See you later! \" "
            ]
        
    dialogue(dialogue_options, dialogue_outcome)
    
global tradable_npcs
tradable_npcs = ["innkeeper", "blacksmith", "librarian", "merchant", "general store owner", "farmer", "thief king", "hunter", "dwarven miner"]
    #if target npc is non-merchant type and player does not have correct quest item, trade option should not appear 

def trade(target_npc):

    

    if target_npc == "innkeeper":
        prints("",.3)
        prints("We've got all kinds of things.")
        prints("",.3)

        npc_inventory = {
        "GP": [1, 3, 5],
        "HP": [ f"+{1}", f"+{4}", f"+{8}" ]
        }

        innkeeper_shop = pd.DataFrame(npc_inventory, index = ["Ale", "Bread", "Cheese"])

        print(innkeeper_shop)
    
    if target_npc == "blacksmith":
        prints("",.3)
        prints(" \"Sure! What is it you were needin',\" the blacksmith smiles, pausing to look up at you.",.3)
        prints("",.3)

        npc_inventory = {
        "GP": [     4,         8,      12   ],
        "AP": [ f"+{5}", f"+{0}", f"+{0}"   ],
        "ATK": [ f"+{0}", f"+{1}", f"+{+0}" ],
        "MAG": [ f"+{5}", f"+{0}", f"+{1}"  ],
        "DEX": [ f"+{0}", f"+{0}", f"+{5}"  ],
        }

        innkeeper_shop = pd.DataFrame(npc_inventory, index = ["Wizard's Robes", "Soldier's Sword", "Comfortable Shoes"])

        print(innkeeper_shop)
        

#old_greg_dialogue()
#innkeeper_dialogue()
