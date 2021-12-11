#!/usr/bin/env python3
import location
import player
from prints import printr
from prints import prints
import console
from item import item
from item_list import * 
from dialogue import *
from tutorial import *
from ascii_art import *
import pandas as pd  
from weapon import weapon
#setup

def nullOption():
    return 0

class npc():

    def __init__(self, name, imageFunc, introFunc, options, outcomes, tradeNum = -1, tradeOptions = [], questTrades = [], questNum = -1, questFunc = nullOption, questEndNum = -1, questIndex = -1,):
        self.name = name
        self.imageFunc = imageFunc
        self.introFunc = introFunc
        self.options = options
        self.outcomes = outcomes
        self.tradeNum = tradeNum
        self.tradeOptions = tradeOptions
        self.questTrades = questTrades
        self.questNum = questNum
        self.questFunc = questFunc
        self.questEndNum = questEndNum
        self.questIndex = questIndex
        

    
    
    def talk(self, player):
        self.imageFunc()
        self.introFunc()
        dialogue(self.options, self.outcomes, self, player)

    def trade(self, player):
        prints("")
        for i in range(len(self.tradeOptions)):
            prints(f"{i+1}. {self.tradeOptions[i][0].name}. Cost: {self.tradeOptions[i][1]}")
        prints(f"{len(self.tradeOptions)+1}. Quit")

        quitB = False
        while not quitB:
            selection = input(printr("> "))
            num = int(selection)
            if(num-1 < len(self.tradeOptions)):
                if(player.gold > self.tradeOptions[num-1][1]):
                    player.gold -= self.tradeOptions[num-1][1]
                    player.inventory.append(self.tradeOptions[num-1][0])
                    prints("Sold!")
                else:
                    prints("Not enough gold")
            else:
                quitB = True
    def setQuest(self, option, outcome, index, questIndex):

        if(self.questEndNum != -1):
            self.options.remove(self.options[self.questEndNum])
            self.outcomes.remove(self.outcomes[self.questEndNum])

        self.options.insert(index, option)
        self.outcomes.insert(index, outcome)
        self.questEndNum = index
        self.questIndex = questIndex

                    
            

        

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



#Common questions
common_qs = ["Who are you?", "Where are you from?", "What are you doing here?"]

def old_greg_intro():
    prints("Forgive me for not recognizing you at first... You look like one of them! " ,2)
    prints("",.3)
    prints("The stranger points to your clothing. You're not wearing much. Your body is barely covered by some tattered robes.  ",2)
    prints("",.3)
    prints("You start to wonder why it seems like this stranger isn't afraid of you. More importantly, you're wondering what in the" , 2)
    prints("seven hells is going! ", 2)
    prints("", .3)

#greg options
greg_dialogue_options = [
"     Why aren't you afraid of me?", 
"     Who are you?", 
"     Where are we?",
"     Goodbye."
]

greg_dialogue_outcomes = [
    "   \"Should I be, lad? You look ghastly.\" ", 
    "   \"My name is Old Greg. I'm the gravekeeper for the people of the hamlet.\" ",
    "   \"Not far from the hamlet. This here's an outcropping of woods just beyond our borders.\" ",
    "   \"See you later! \" "
        ]
    
greg = npc("Old Greg", old_greg_ascii, old_greg_intro, greg_dialogue_options, greg_dialogue_outcomes)

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

def inkeeper_intro():
    prints("She smiles somewhat uncomfortably at you as you step over to the bar", 1)
    prints("\"well, stranger, what can I get for ya? You saved my Pa. You can have damn well whatever you please!\"", 2)


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





def blacksmith_ascii():
                                                                                  
                                                                                    
    prints("          &&&&                                                         ")
    prints("           @&@@@%#%%/&.  &#####(#/                                     ")       
    prints("              (((&#@@@** @&(((%###                                     ")         
    prints("             %##,/%//*/&@%##@&&###,                                    ") 
    prints("           ,##(#.   	  @@@&@@@                                      ") 
    prints("         ##(###(,.     . &&@&&@@&&@@                                   ") 
    prints("        #(/*/**/. * .*/.@%((/((#(#(%@&@&#                              ")
    prints("       %#(((((###,&&&@@@@@%#/,@&%&&#.,@@&%                             ")
    prints("      #/*#/(/*(**(* @@@@&&%&@(##&&#//.@@/@&                            ")
    prints("       ###,/**/**(&&&.#@@&(,,,*,//*&@@&&@&                             ")
    prints("        .%/***@%#///&&//@@@%%%&##%%&@&%&&@                             ")
    prints("         .%(%(*(%%&//(%%%@&%%@#%@@&%&&%@&@&                            ")
    prints("        .(/#**/##(*#/@@@%@%#%%@&%@&@@&&%///*****//*                    ")
    prints("   	((*/#**/*/(%@%%@&%&@%%@@&@&@@&%((#(/########/..                    ")
    prints("  	#*/*/(*(&#&%@@&%&@%%@@#%%@@///(///(/*(/#%##%###/.                  ")
    prints("   		(##*,.,#@&&/##(#@%#/*(*(*(,/*//(((##(/((#%#%##)                ")
    prints("    		  &%%&&@&%&&&%###@@%##@#$**,/,*(*(*(*#//(%**/(%&#          ")
    prints("     		%((%###%(//%%(((#%%&&#$%#$#***,**,,*,**,,,*,**&@#\         ")
    prints("     		%(((////////#(((/(##&%##$%$%/,*,*,*****,/,,%@*,,**\        ")
    prints("     		((/////*/((//(///(%#&########*/,/*,**,/,/,*&.,,*,*(*,((    ")
    prints("    		((/*//////*/*(//((##&%*3$#$#$#$%////%##%%*%**%,(&,#%##%%.. ")
    prints("    		##/(///*******/////#%#$%#$%$#%#$%%#(/(*##/*@@&@&&*(#%,#%%%%")
    prints("   		((//*/********////(#$%#$%#$#$%#$%%%(/&@@@&&&%/#%%/%&@%%&%#%,#( ")
    prints("   ##################################################\*(#/&@@@*#%@/%#@%")
    prints("    (#&@@@@&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&@@@@@@@@@&@&&@@@&@@&&@@")
    prints("    ./%@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@&@@&&&&@@@@@&&")     
    prints("        *%@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@&&&&@@@&&&&&")     
    prints("        .  (&&%&%&&@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@&@@@@@@@&#")      
    prints("          , .,//#&&@@&&%@@@@@@@@@@@@@@@@@@@@@@@@@@&&%@&@@@@@&&@@@&%*/..")      
    prints("                  ,(#(((.   .*&&@@@@@&,* *,(%####* .,(%*#.. ,/#*#(#    ")       
    prints("                              ..            *(                   .     ")  

def blacksmith_intro():
    prints("the man is engrossed in his work, continuing to hammer away as you step inside the small forge area")
    prints("you make yourself known and he quickly looks up, obviously annoyed by this interuption")
    prints("\"What?\"")

def blacksmith_quest(self):
    prints("\"Work?, im afraid to say I aint got much ta pay with, run along now\"")
    prints("\"Wait.. I know yer type, that thing on yer belt you call a weapon tells me all I need ta know\"")
    prints("\"I got no work for ye, but I been hearing rumors of something in the old mines\"")
    prints("\"some of my er.. contacts been telling me there's a right good bit o silver somewhere in those tunnels\"")
    prints("\"as much as i'd love to make myself something, seeing as yer the one that saved ol' greg, not me,")
    prints("I'm willin ta bet you're gonna need it more than I\"")
    prints("\"bring it here, and I'll make somethin out of it flat\"")
    self.setQuest("     **Turn in Silver ore**", "\"You got it? hand it over son!\"", 4, 0)

    

def blacksmith_questEnd():
    prints("He looks over the ore you hand him, inspecting it carefully")
    prints("\"This'll do, good work\"")
    prints("He begins his work, heating the forge and hammering away for hours without rest")
    prints("Eventually, the ore begins to resemble a fine blade, then a fine sword")
    prints("Finally, the weapon is done. he hands it to you, clearly proud of his work")
    prints("You got the Silver Sword!", 1)

smith_dialogue_options = [
"     *** TRADE *** What do you have for sale?", 
"     What is your name?", 
"     What can you tell me about the Hamlet?",
"     *** QUEST *** Looking for work.",
"     Goodbye."
]

smith_dialogue_outcomes = [
    "   \"I got plenty o wares for sale. That is, of course, supposing you've got the coin.\" ", 
    "   \"Sebastien Steelscraper's the name. Pleasure to meet you...er...person.\" ",
    "   \"Well the whole place has gone to shite since the Hags came and lay their curse on us. Before that we were just a bunch of quiet folk.\" ",
    "   He looks up at you with attention for the first time, finally taking you at least somewhat seriously", 
    "   \"See you later! \" "
        ]

axe = weapon("Woodsman's Axe", 4, 0, "cleave", "a fine axe, heavy but balanced well")
sword = weapon("Steel Sword", 2, 2, "slash", "why would a small town blacksmith have such practice making weapons of war?")
hammer = weapon("Spare Hammer", 3, 1, "swing", "It's worn from use, but no less effective")

silSword = weapon("Silver Sword", 3, 3, "expertly slash", "a masterwork weapon, it gleams in even the darkest corner")
smith_trades = [[axe, 35], [sword, 50], [hammer, 25]]
smith_questTrades = [[silSword, "Silver Ore", blacksmith_questEnd, 3]]


smith = npc("blacksmith", blacksmith_ascii, blacksmith_intro, smith_dialogue_options, smith_dialogue_outcomes, 0, smith_trades, smith_questTrades, 3, blacksmith_quest)



def librarian_intro():
    prints("")
    prints("The libarian is preocciuped with a stack of yellowing papers, strewn across her desk. She is so caught up")
    prints("in her study, in fact, that she hardly notices your approach. \"Uhm...Hello?\" you manage to ask meekly.")
    prints("She looks up at you in shock. You can't tell if it is your appearance, or shock at seeing another person in the library.")


librarian_dialogue_options = [
"     Who are you? ", 
"     What are doing right now?", 
"     Where are we?",
"     What can you tell me about the Hags' Curse?",
"     *** QUEST *** Is there something I can do?",
"     Goodbye."
]

librarian_dialogue_outcome = [
    "   \"Regina Quillspeth, at your service. Are you here because you're actually interested in books?\" ", 
    "   \"I was studying old magical texts until you came along. Not that I mind the company. No one ever comes here.\" Regina sighs and sits back in her chair a little bit, pouting. ",
    "   \"Where does it look like you are? This is the hamlet library. The monks that once ran this place left behind so much knowledge.\" ",
    "   \"Well, I know that the monks all ran away or were murdered by the Hags. Now it's just me, left to look after all of their years of hard work. Uh...they're evil?\" ",
    "   \"Come back and visit me some time!"

        ]

def librarian_quest():
    prints("\"You're...what? You're looking for an amulet?,\" Regina asks as she stops shuffling papers around her desk.")
    prints("\"The AMULET!\" she cries out, \"OF COURSE!\", she exclaims.")
    prints("    Suddenly Regina's eyes narrow and she lowers her head. With very serious intonation in her voice, she explains,")
    prints("    \"The monks that looked after this library wrote at length about the Amulet. During an excavation in a far off land,")
    prints("    they were able to secure what is referred to as the \"Blood of Shadows\". Pretty cool name, right? Anyway, the Monks")
    prints("    sough to protect the Blood of Shadows, this Ruby, from the prying hands of evildoers. They chose this hamlet.")
    prints("    The only trouble with their plan were the hags. One day a monk of the order was travelling to a neighboring village when")
    prints("    he came across one fot he Hag sisters. They tortured him to find out where the Blood of Shadows was being kept.")
    prints("    With the right ritual, that Ruby can take in any and all shadows. Considering the Hags are pure evil, I don't know why")
    prints("    they'd want the Ruby unless it was somehow their weakness. The Ruby was last seen in the hands of th eHag, Mefilda Rottenbough.")
    prints("    I can't find any mention of that name anywhere though! Maybe you should talk to somoene who has been living here longerR?")
    prints("    Bring me the ruby and I think I'll be able to recreate the spell from what I have in my notes.")

librarian_trade = [ [time_book, 25], [pamphlet, 5], [book_of_spells, 75] ]

librarian = npc("Librarian", librarian_ascii, librarian_intro, librarian_dialogue_options, librarian_dialogue_outcome, -1, librarian_trade, [], 4, librarian_quest)



def merchant_intro():
    prints("")
    prints("The merchant's wagon is a beautiful site, adorned with many colors. The whole area around the wagon")
    prints("smelled of the most delicious of incenses. The merchant smiles at you from behind their stand, \"Greetings, friend.\"")


merchant_dialogue_options = [
"     *** TRADE ***  What are you selling, friend? ", 
"     What is your name?", 
"     Where are you from?",
"     What do you know about the Hags' Curse?",
"     Goodbye."
]

merchant_dialogue_outcome = [
    "   \"Many curious things, for the right price.\" ", 
    "   \"My name is Azni.\" ",
    "   \"A place far beyond the borders of the woods.\" ",
    "   \"Curse? What curse?\" Azni looks you up and down, gauging your reaction. He bursts into laughter, \"Hah! They're terrible, but I still must laugh.\" ",
    "   \"Come back anytime, friend. \" "
        ]
merchant_trade = [ [small_health_chest, 25], [medium_health_chest, 50], [large_health_chest, 100], [small_armor_chest, 25], [medium_armor_chest, 50], [large_armor_chest, 100], [small_weapon_chest, 25], [medium_weapon_chest, 50], [large_weapon_chest, 100] ]

merchant = npc("Merchant", merchant_ascii, merchant_intro, merchant_dialogue_options, merchant_dialogue_outcome, 0, merchant_trade)

def general_store_intro():
    prints("")
    prints("The soft chime of a bell alerts the owner to your presence. They turn around, leaning")
    prints("the broom they had been sweeping with against a column. \"Greetings, traveler!\"")
    prints("the owner addresses you jovially, \"Welcome! Welcome!")

general_store_owner_dialogue_options = [
"     *** TRADE *** I'd like to see your wares.", 
"     What is your name?", 
"     How is business?",
"     *** QUEST *** Is there anything that you need help with?",
"     Goodbye."
]


general_store_dialogue_outcome = [
    "   \"Of course! I've the best crafting materials in the land.\" ", 
    "   \"Mr. Barry Barrelpine, humbly at your service. Anything you need, anything at all, I will sell it to you!\" ",
    "   \"Fine. Why do you ask? Who have you been talking to?\" ",
    "   \"Okay. Listen...I shouldn't be talking about this, but I owe a lot of money to Hank in the Secret Speakeasy in the Sewers. Could you see about settling my debt for me?\""
    "   \"See you later! \" "
        ]

gen_trade = [ [wine, 3], [loaf_of_bread, 5], [kidney_beans, 3], [throwing_spear, 10], [sickle, 50], [artichokes, 3], [asiago_cheese, 50], [time_book2, 100] ],

general_store_owner = npc("General Store Owner", general_store_owner_ascii, general_store_intro, general_store_owner_dialogue_options, general_store_dialogue_outcome, 0, gen_trade)



def farmer_intro():
    prints("")
    prints("The farmer was an older gentleman. Obviously panicked and in quite some distress,")
    prints("they can barely force words out between gasping for air. Something was terribly wrong.")
    prints("")


farmer_dialogue_options = [
"     Wait! Stop running! What has happened to you?", 
"     What is your name?", 
"     Where is your house?",
"     What can I do?",
"     Goodbye."
]

farmer_dialogue_outcome = [
    "   \"AHHHH!!! My house! Our house! She came...d-d-destroyed it all! What am I going to do?\" ", 
    "   \"P-P-P-Podrick Pebbleton, s-s-sir. \" ",
    "   \"Back...th-through the fi-field...Over the brook, down the trail past the old Oak for a bit.\" ",
    "   \"Why? Are you some kind of hero? I-I...I...\" Podrick breaks into tears, \"I just want my house back!\" ",
    "   \"I'll be alone in this world forever, it seems.\" "
        ]

farmer = npc("Farmer", farmer_ascii, farmer_intro, farmer_dialogue_options, farmer_dialogue_outcome)

def thief_king_intro():
    prints("")
    prints("The Thief King does not appear to be remotely in the realm of toying around.")
    prints("They eye you with shrewd, cold eyes. \"Speak.\" was the only word they ushered")
    prints("from their lips before folding their arms acrossed their chest.")
    prints("")



thief_king_dialogue_options = [
"     Are you the one they call the Thief King?", 
"     Why do you live in the Sewers?", 
"     Are you going to let me live?",
"     Are you working for the Hags?",
"     *** QUEST *** Any jobs you that need doing?",
"     Goodbye."
]

thief_king_dialogue_outcome = [
    "   \"...Is the name not obvious enough?\" ", 
    "   \"I like the way it smells,\" he says with scowl, \"The people of the hamlet don't take kindly to thieves walking about.\" ",
    "   \"Give me a good reason to and I might.\" ",
    "   \"Don't be ridiculous. They can sod right off.\" "
    "   \"There's always work for willing hands. Are you sure you're up to it?",
    "   \"I'll be here.\"."
        ]

thief_king = npc("Thief King", thief_king_ascii, thief_king_intro, thief_king_dialogue_options, thief_king_dialogue_outcome)


def hunter_intro():
    prints("")
    prints("The hunter is a very large person. As soon as they turn to greet you,")
    prints("you realize how small you are in comparison. Though his stature")
    prints("precluded you to believe that he was harsh man, his demeanor led you to believe otherwise.")
    prints("\"Well, I guess that one is getting away.\" He says, hanging his head, feigning disappointment.")
    prints("")


hunter_dialogue_options = [
"     Who are you?", 
"     What are you doing out here?", 
"     What do you know about the Hags' Curse?",
"     *** QUEST *** You look troubled. Can I help you in some way?"
"     Goodbye."
]

hunter_dialogue_outcome = [
    "   \"The name is Arthur. Arthur Edenbough. \" ", 
    "   \"I thought I was going to finally fell that buck. Now you're here.\" ",
    "   \"I've never seen one of them personally, but these woods are teeming with monsters. I don't past the brambles. It's too dark.\" ",
    "   \"I'm so terribly thirsty. If you could bring me a cold beer, I'd be more than happy to share my map with you.\" ", 
    "   \"Happy hunting!\" "
        ]

hunter = npc("Huner", hunter_ascii, hunter_intro, hunter_dialogue_options, hunter_dialogue_outcome)


def drunkard_intro():
    prints("You almost feel bad for this sorry mess of a human. The bartender takes a coin")
    prints("from the pile in front of the man, placing a large bottle down in front of him.")
    prints("\"Sober up, you dolt!\", the bartender chastizes the drunkard.")


drunkard_dialogue_options = [
"     Try to wake the drunkard."
"     Pour his beer on him."
"     Knock on the table."
"     Clap loudly."
"     Leave."
]

drunkard_dialogue_outcome = [
    "   He keeps snoring. There's no difference. ", 
    "   The drunkard is wet now, but they're still out like a light. ",
    "   You've knocked on the table. The drunkard flatulates loudly, wipes his nose, and keeps sleeping."
    "   The drunkard, in his sleep, claps back."
    "   The drunkard wakes up briefly, and looks around with squinted vision. Seconds later, he falls asleep again. "
        ]

drunkard = npc("Drunkard", drunkard_ascii, drunkard_intro, drunkard_dialogue_options, drunkard_dialogue_outcome)



def dwarven_miner_intro():
    prints("One of the miners approaches you, their pickaxe resting gently on their shoulders.")
    prints("\"Hail, friend,\" they call to you, \"Best not be traversing the mines!")
    prints("they say the place is just swarmin' with monsters today. Especially the deep caverns!\"")


dwarven_miner_dialogue_options = [
"     What is your name?", 
"     Are you in danger?", 
"     What can you tell me about these mines?",
"     *** QUEST *** Would you like my help?"
"     Goodbye."
]

dwarvern_miner_dialogue_outcome = [
    "   \"Ztolo Zan I my name, stranger. Pleased to make your acquaintance. \" ", 
    "   \"Not particularly. I was, not long ago. Damned cave in....\" ",
    "   \"These mines are some of the oldest in all the land. The tunnels reach all the way to Urzal-ka!\" ",
    "   \"Are you serious? Well, there's been a giant spider causing cave ins lately. Slows up production. Want to make a little money?"
    "   \"See you later! \" "
        ]

dwarven_miner = npc("Dwarven Miner",  dwarven_miner_ascii, dwarven_miner_intro, dwarven_miner_dialogue_options, dwarvern_miner_dialogue_outcome)
    

def guard_intro():
    prints("\"HALT!,\" You are commanded. A burly man with a large chest and tall spear approaches you.")
    prints("He takes off his helmet as the other members of his unit keep their weapons trained on you until")
    prints("he bid them relax. \"It's alright lads, this one just seems a bit lost.\"")

guard_dialogue_options = [
"     I'm friendly! I swear!", 
"     What are you doing out here?", 
"     What can you tell me about where we are?",
"     Goodbye."
]

guard_dialogue_outcome = [
    "   \"How should we know? Keep your hands off those weapons.\" ", 
    "   \"We are the last of the guard. All of the others have been killed off.\" ",
    "   \"This is our last defense from the outside world. Having the Hags in here with us is hard enough!\" ",
    "   \"See you later! \" "
        ]
    
guard = npc("Guard", guard_ascii, guard_intro, guard_dialogue_options, guard_dialogue_outcome)
