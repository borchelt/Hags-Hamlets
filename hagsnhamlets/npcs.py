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

    def __init__(self, name, imageFunc, introFunc, options, outcomes, tradeNum = -1, tradeOptions = [], questTrades = [], questNum = -1, questFunc = nullOption, questEndNum = -1, questIndex = -1, local = "default", ):
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
        self.local = local
        

    
    
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
    prints("seven hells is going on! ", 2)
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

def town_Greg_intro():
    prints("Having safely arrived in town, Old Greg has taken to his usual practice of")
    prints("sitting in the town square, watching the goings on from his favorite bench.")
    prints("He sees you and beckons you over with a lazy wave")
    prints("\"So, how's Mr. Monster fighter doing?\"")

town_Greg_Options = [
    "    What's... going on?",
    "    What am I?",
    "    *** QUEST *** What can I do to help?",
    "    Goodbye."
]

town_Greg_Outcomes = [
    "    \"Well, bout a year ago the hags came into town and put thier curse on this land, ever since it's been notin' but doom and gloom.\"",
    "    \"Im about as sure as you are, but if I had to guess, I'd wager on some sort of ghoul given your sorry looks.\"",
    "    \"Well, Ol' Greg might know a bit more than the hags think he does...",
    "    \"Be safe!"
]

def town_Greg_Quest(self):
    prints("    \"Digging the graves, the ghosts whisper to ya,\"")
    prints("    \"They want out of this town as much as the rest of us ya see,\"")
    prints("    \"and I think I know just how to help those ghosts out.\"")
    prints("    \"The youngest hag has a weakness, I'm not sure why, but she's powerless against\"")
    prints("    \"anyone that has partaken of her cooking, and one o' my ghastly friends gave me a recipe.\"")
    prints("    \"I would mix it up for you, but im missing one key ingredient: A Deathcap Mushroom.\"")
    self.setQuest("** Turn in Deathcap **", "oh ho ho, this hag aint gonna know what hit her",2, 0)

def town_Greg_endQuest():
    prints("    Greg takes the mushroom carefully from your hands, and drops it into his water skin along with some assorted herbs and... items...")
    prints("    He gives it a good shake and hands it over to you. \"I'm sad to see betsy go, but its for a good cause.\"")
    prints("              ----####  YOU GOT THE HAG'S BANE SOUP #####----", 1)

hagsBane = consumable("Hag's Bane Soup", "you're not sure if drinking this will kill you, but greg didnt seem worried", ["hagsBane", 0])
greg_QuestTrades = [[hagsBane, "Deathcap Mushroom", town_Greg_endQuest]]

townGreg = npc("Old Greg", old_greg_ascii, town_Greg_intro, town_Greg_Options, town_Greg_Outcomes, -1, [], [greg_QuestTrades], 2, town_Greg_Quest)
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
    prints("\"Work?, im afraid to say I aint got much ta pay with, run along now,\" the smith says, turning back to his work.")
    prints("After a moment of contemplation, the smith looks back at you,\"Wait..forgive me,\" he says.")
    prints("    \"I know yer type, that thing on yer belt you call a weapon tells me all I need")
    prints("      to know. I got no work for ye, but I been hearing rumors of something in the")
    prints("      Old Mines, North of the Forest Clearing. Some of my suppliers have told me there's")
    prints("      a right good bit o silver somewhere in those tunnels. As much as I'd love to make")
    prints("      myself something, you saved Ol' Greg. I'm willin ta bet you're gonna need it more")
    prints("      than any of the lousy guard around these parts. Bring me the SILVER ORE and I'll")
    prints("      a forge you a mighty weapon indeed.\"")

    self.setQuest("     **Turn in Silver ore**", "\"You got it? hand it over son!\"", 4, 0)
    prints("")


    

def blacksmith_questEnd():
    prints("He looks over the ore you hand him, inspecting it carefully.")
    prints("    \"Well now,\" the Blacksmith says, obviously impressed, \"It must have been")
    prints("     quite the feat for you to get this out of that Mine. I hope it wasn't too")
    prints("     much trouble.\"")
    prints("")
    prints("    He begins his work, heating the forge and hammering away for hours without rest")
    prints("occasionally you fetched more water or would pass the Blacksmith a bit of food")
    prints("or drink. It was the least you could do. Eventually the ore began to take shape.")
    prints("With every strike of the Blacksmith's hammer, the ore was transformed into something")
    prints("more and more like a sword. For many hours he continued on, sweating and laboring")
    prints("over his task. Eventually, the ore became a blade. Later, a sword. Lastly, a treaure")
    prints("worthy of a Hero. At last the Blacksmith hands you the weapon, a slight grin on his")
    prints("otherwise expressionless face.")
    prints("    \"Here lad, take this. You'll need it to bring peace to these people.\"")
    prints("")
    prints("              ----####  YOU GOT THE SILVER SWORD #####----", 1)
    prints("")


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


smith = npc("Blacksmith", blacksmith_ascii, blacksmith_intro, smith_dialogue_options, smith_dialogue_outcomes, 0, smith_trades, smith_questTrades, 3, blacksmith_quest)



def librarian_intro():
    prints("")
    prints("The libarian is preocciuped with a stack of yellowing papers, strewn across her desk. She is so caught up")
    prints("in her study, in fact, that she hardly notices your approach. \"Uhm...Hello?\" you manage to ask meekly.")
    prints("She looks up at you in shock. You can't tell if it is your appearance, or shock at seeing another person in the library.")
    prints("")



def librarian_quest(self):
    prints("\"You're...what? You're looking for an amulet?,\" Regina asks as she stops shuffling papers around her desk.")
    prints("\"The AMULET!\" she cries out, \"OF COURSE!\", she exclaims.")
    prints("")
    prints("        Suddenly Regina's eyes narrow and she lowers her head. With very serious intonation in her voice, she explains,")
    prints("    \"The monks that looked after this library wrote at length about the Amulet. During an excavation in a far off land,")
    prints("    they were able to secure what is referred to as the \"Blood of Shadows\". Pretty cool name, right? Anyway, the Monks")
    prints("    sough to protect the Blood of Shadows, this Ruby, from the prying hands of evildoers. They chose this hamlet.")
    prints("    The only trouble with their plan were the hags. One day a monk of the order was travelling to a neighboring village when")
    prints("    he came across one fot he Hag sisters. They tortured him to find out where the Blood of Shadows was being kept.")
    prints("    With the right ritual, that Ruby can take in any and all shadows. Considering the Hags are pure evil, I don't know why")
    prints("    they'd want the Ruby unless it was somehow their weakness. The Ruby was last seen in the hands of the Hag, Mefilda Rottenbough.")
    prints("    I can't find any mention of that name anywhere though! Maybe you should talk to somoene who has been living here longer?")
    prints("    Bring me the ruby and I think I'll be able to recreate the spell from what I have in my notes.")
    prints("")
    self.setQuest("     **Turn in Ruby**", "\"May I see it?\"", 6, 0)
    prints("")


def librarian_questEnd():
    prints("")

librarian_dialogue_options = [
"     *** TRADE *** Do you have anything for sale?",
"     Who are you? ", 
"     What are doing right now?", 
"     Where are we?",
"     What can you tell me about the Hags' Curse?",
"     *** QUEST *** Is there something I can do?",
"     Goodbye."
]

librarian_dialogue_outcome = [
    "   \"Of course!",
    "   \"Regina Quillspeth, at your service. Are you here because you're actually interested in books?\" ", 
    "   \"I was studying old magical texts until you came along. Not that I mind the company. No one ever comes here.\" Regina sighs and sits back in her chair a little bit, pouting. ",
    "   \"Where does it look like you are? This is the hamlet library. The monks that once ran this place left behind so much knowledge.\" ",
    "   \"Well, I know that the monks all ran away or were murdered by the Hags. Now it's just me, left to look after all of their years of hard work. Uh...they're evil?\" ",
    "   \"Come back and visit me some time!"

        ]


blood_of_shadows = item("Ruby Amulet", "An amulet, infused with the power to take in or dispel shadows.")
librarian_trade = [ [time_book, 25], [pamphlet, 5], [book_of_spells, 75] ]
librarian_questTrades = [[blood_of_shadows, "The Hangman's Ruby", librarian_questEnd, 4]]

librarian = npc("Librarian", librarian_ascii, librarian_intro, librarian_dialogue_options, librarian_dialogue_outcome, 0, librarian_trade, librarian_questTrades, 5, librarian_quest)



def merchant_intro():
    prints("")
    prints("The merchant's wagon is a beautiful site, adorned with many colors. The whole area around the wagon")
    prints("smelled of the most delicious of incenses. The merchant smiles at you from behind their stand, \"Greetings, friend.\"")
    prints("")



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

coldest_beer = item("Coldest Beer", "The stein somehow still has frost on it. Perhaps it has been magically cooled.")
merchant_trade = [ [small_health_chest, 25], [medium_health_chest, 50], [large_health_chest, 100], [small_armor_chest, 25], [medium_armor_chest, 50], [large_armor_chest, 100], [small_weapon_chest, 25], [medium_weapon_chest, 50], [large_weapon_chest, 100], [coldest_beer, 150]]



merchant_questTrades = []

merchant = npc("Merchant", merchant_ascii, merchant_intro, merchant_dialogue_options, merchant_dialogue_outcome, 0, merchant_trade)

def general_store_intro():
    prints("")
    prints("The soft chime of a bell alerts the owner to your presence. They turn around, leaning")
    prints("the broom they had been sweeping with against a column. \"Greetings, traveler!\"")
    prints("the owner addresses you jovially, \"Welcome! Welcome!")
    prints("")

def gen_quest(self):
    prints("")
    prints("Barry walks around the counter, briefly pausing to look out the front window as if he")
    prints("was afraid of being watched. He turns his back to the door as he turned the lock.")
    prints("    \"The Thief King runs a speakeasy in the sewers below the Hamlet.")
    prints("     I kind of got mixed up in some...irresponsible spending. I owe the")
    prints("     Thief King something like 5,000 gold. I don't have that kind of money!")
    prints("     No one lives in this town!\", he says. After a pause, and a wary look")
    prints("     around, he containues, \"You look like you're no stranger to a fight.")
    prints("     I don't care how you handle it, but settle my debt and I'll give you the")
    prints("     discount of a lifetime.\"")
    self.setQuest("     **Hand over the papers**", "\"You.. you actually did it!\"", 3, 0)
    prints("")

def gen_questEnd():
    prints("")

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
    "   \"Okay. Listen...I shouldn't be talking about this, but I owe a lot of money to Hank in the Secret Speakeasy in the Sewers. Could you see about settling my debt for me?\"",
    "   \"See you later! \" "
        ]


gen_trade = [ [wine, 3], [loaf_of_bread, 5], [kidney_beans, 3], [throwing_spear, 10], [sickle, 50], [artichokes, 3], [asiago_cheese, 50], [time_book2, 100] ],

permanent_discount = item("Permanent Discount", "10 percent off of everything in the General Store, forever!")
gen_questTrades = [ [permanent_discount, "Debt Settled Papers", librarian_questEnd, 3]  ]

general_store_owner = npc("General Store Owner", general_store_owner_ascii, general_store_intro, general_store_owner_dialogue_options, general_store_dialogue_outcome, 0, gen_trade, gen_questTrades, 3, gen_quest)



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


def thief_king_quest(self):
    prints("")
    prints("    \"Get the Rat King to sign a treaty. I'm tired of losing good men to that animal.\"")
    prints("    The Thief King spits to their left, \"Bunch of mangy rodents. Have him sign it,")
    prints("    or kill them all. I don't care how it's done. The sewers already stink enough, so")
    prints("    what's a few more bodies.\"")
    self.setQuest("     **    Give him the treaty**", "\"Well done.\"", 4, 0)
    prints("")


def thief_king_questEnd():
    prints("")
    prints("    \"I can't believe you pulled it off. Fine. As promised,\" the Thief King")
    prints("says, handing you a sealed envelope.")
    prints("")
    prints("            ----#### YOU'VE SETTLED BARRY'S DEBT! ####---- ")
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

proof_of_debt_settled = item("Debt Settled Papers", "Proof that the debt between Barry Barrelpine and the Thief King was settled.")

signed_rat_king_treaty = item("Signed Treaty", "A treaty that promises an end to the violence between the Rat King and the Thief King.")
thief_king_questTrades = [ [proof_of_debt_settled, "Signed Treaty", thief_king_questEnd, 4 ] ]

thief_king = npc("Thief King", thief_king_ascii, thief_king_intro, thief_king_dialogue_options, thief_king_dialogue_outcome, -1, [], thief_king_questTrades, thief_king_quest, 4)





def drunkard_intro():
    prints("")
    prints("You almost feel bad for this sorry mess of a human. The bartender takes a coin")
    prints("from the pile in front of the man, placing a large bottle down in front of him.")
    prints("\"Sober up, you dolt!\", the bartender chastizes the drunkard.")
    prints("")

drunkard_dialogue_options = [
"     Try to wake the drunkard.",
"     Pour his beer on him.",
"     Knock on the table.",
"     Clap loudly.",
"     Leave.",
]

drunkard_dialogue_outcome = [
    "   He keeps snoring. There's no difference. ", 
    "   The drunkard is wet now, but they're still out like a light. ",
    "   You've knocked on the table. The drunkard flatulates loudly, wipes his nose, and keeps sleeping.",
    "   The drunkard, in his sleep, claps back.",
    "   The drunkard wakes up briefly, and looks around with squinted vision. Seconds later, he falls asleep again. ",
        ]

drunkard = npc("Drunkard", drunkard_ascii, drunkard_intro, drunkard_dialogue_options, drunkard_dialogue_outcome)



def dwarven_miner_intro():
    prints("")
    prints("One of the miners approaches you, their pickaxe resting gently on their shoulders.")
    prints("\"Hail, friend,\" they call to you, \"Best not be traversing the mines!")
    prints("they say the place is just swarmin' with monsters today. Especially the deep caverns!\"")
    prints("")


dwarven_miner_dialogue_options = [
"     What is your name?", 
"     Are you in danger?", 
"     What can you tell me about these mines?",
#"     *** QUEST *** Would you like my help?",
"     Goodbye."
]

dwarvern_miner_dialogue_outcome = [
    "   \"Ztolo Zan be my name, stranger. Pleased to make your acquaintance. \" ", 
    "   \"Not particularly. I was, not long ago. Damned cave in....\" ",
    "   \"These mines are some of the oldest in all the land. The tunnels reach all the way to Urzal-ka!\" ",
    #"   \"Are you serious? Well, there's been a giant spider causing cave ins lately. Slows up production. Want to make a little money?"
    "   \"See you later! \" "
        ]

dwarven_miner = npc("Dwarven Miner",  dwarven_miner_ascii, dwarven_miner_intro, dwarven_miner_dialogue_options, dwarvern_miner_dialogue_outcome)
    

def guard_intro():
    prints("")
    prints("\"HALT!,\" You are commanded. A burly man with a large chest and tall spear approaches you.")
    prints("He takes off his helmet as the other members of his unit keep their weapons trained on you until")
    prints("he bid them relax. \"It's alright lads, this one just seems a bit lost.\"")
    prints("")

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




def rat_king_intro():
    prints("")
    prints("    The Rat King was an intimidating creature. You thought that for sure that you were")
    prints("prepared for this, but find yourself speechless in it's presence. The large, almost humanoid")
    prints("shuffles towards you, waving the guards to the side. It is obvious that it does not consider")
    prints("you a threat.")
    prints("")


def rat_king_quest(self):
    prints("Kill... One... Of.. Them")
    self.setQuest("     **    Hand it the finger**", "\"...\"", 4, 0)

def rat_king_questEnd():
    prints("    A treaty is haned to you by one of it's retainers, signed by the rat king.")
    prints("                    --- #### YOU'VE GOT THE Signed Treaty #### ---")
    prints("")

rat_king_options = [
"   *** TRADE *** Do you have anything here that might be useful to me?",
"   You must be the Rat King.",
"   Why do you live here?",
"   What do you think of the Thief King?",
"   *** QUEST *** Is there anything that troubles you?",
"   Goodbye for now."
]

rat_king_outcomes = [ 
"   Of...course...I save them...for you...for Us.",
"   Is....it...that....obvious?",
"   Do...think...Hamlet...like...rats?",
"   A...simple...evil...creature.",
"   The...Hags...They...stronger. Rats fight. Rats losing.",
"   ...See...you...soon."
]

rat_trades = [ ]
treaty = item("Signed Treaty", "The handwriting is surprisingly eligant")
rat_questTrades = [treaty, "Hag's Finger", rat_king_questEnd]

rat_king = npc("The Rat King", rat_king_ascii, rat_king_intro, rat_king_options, rat_king_outcomes, 0, rat_trades, rat_questTrades, 4, rat_king_quest, 4)






