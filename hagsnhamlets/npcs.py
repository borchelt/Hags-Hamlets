#!/usr/bin/env python3
import location
import player
from prints import printr
from prints import prints
import console
from item import item
from item_list import * 
from dialogue import *
from ascii_art import *
import pandas as pd  
from weapon import weapon
#setup

def nullOption():
    return 0

class npc():

    def __init__(self, name, imageFunc, introFunc, options, outcomes, tradeNum = -1, tradeOptions = [], questTrades = [], questNum = -1, questFunc = nullOption, questEndNum = -1, questIndex = 0, local = "default", ):
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

        self.questNum = -1

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
    prints("")
    prints("Forgive me for not recognizing you at first... You look like one of them! " ,2)
    prints("",.3)
    prints("The stranger points to your clothing. You're not wearing much. Your body is barely covered by some tattered robes.  ",2)
    prints("",.3)
    prints("You start to wonder why it seems like this stranger isn't afraid of you. More importantly, you're wondering what in the" , 2)
    prints("seven hells is going on! ", 2)
    prints("", .3)
    prints("")

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
    prints("")
    prints("Having safely arrived in town, Old Greg has taken to his usual practice of")
    prints("sitting in the town square, watching the goings on from his favorite bench.")
    prints("He sees you and beckons you over with a lazy wave")
    prints("\"So, how's Mr. Monster fighter doing?\"")
    prints("")

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
    self.setQuest("    ** Turn in Deathcap **", "oh ho ho, this hag aint gonna know what hit her",3, 0)

def town_Greg_endQuest(self):
    prints("    Greg takes the mushroom carefully from your hands, and drops it into his water skin along with some assorted herbs and... items...")
    prints("    He gives it a good shake and hands it over to you. \"I'm sad to see betsy go, but its for a good cause.\"")
    prints("              ----####  YOU GOT THE HAG'S BANE SOUP #####----", 2)

hagsBane = consumable("Hag's Bane Soup", "you're not sure if drinking this will kill you, but greg didnt seem worried", ["hagsBane", 0])
greg_QuestTrades = [[hagsBane, "Deathcap Mushroom", town_Greg_endQuest, 2]]

townGreg = npc("Old Greg", old_greg_ascii, town_Greg_intro, town_Greg_Options, town_Greg_Outcomes, -1, [], greg_QuestTrades, 2, town_Greg_Quest)
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
    prints("",)
    prints("    The large man is engrossed in his work. He continues hammering away, even as you step into the room.",1)
    prints("You make yourself known with a slight cough. He makes a face like he smells something off.",1)
    prints("\"Er...What are you wanting, then?\"",1)
    prints("",1)

def blacksmith_quest(self):
    prints("\"Work?, im afraid to say I aint got much ta pay with, run along now,\" the smith says, turning back to his work.",1)
    prints("After a moment of contemplation, the smith looks back at you,\"Wait..forgive me,\" he says.",1)
    prints("     \"I know yer type, that thing on yer belt you call a weapon tells me all I need",1)
    prints("      to know. I got no work for ye, but I been hearing rumors of something in the",1)
    prints("      Old Mines, North of the Forest Clearing. Some of my suppliers have told me there's",1)
    prints("      a right good bit o silver somewhere in those tunnels. As much as I'd love to make",1)
    prints("      myself something, you saved Ol' Greg. I'm willin ta bet you're gonna need it more",1)
    prints("      than any of the lousy guard around these parts. Bring me the SILVER ORE and I'll",1)
    prints("      a forge you a mighty weapon indeed.\"",1)

    self.setQuest("     **Turn in Silver ore**", "\"You really have the Silver Ore? I thought you'da been dead o'course! Hand it over son!\"", 4, 0)
    prints("",1)


    

def blacksmith_questEnd(self):
    prints("He looks over the ore you hand him, inspecting it carefully.",1)
    prints("    \"Well now,\" the Blacksmith says, obviously impressed, \"It must have been",1)
    prints("     quite the feat for you to get this out of that Mine. I hope it wasn't too",1)
    prints("     much trouble.\"")
    prints("")
    prints("    He begins his work, heating the forge and hammering away for hours without rest",1)
    prints("    occasionally you fetched more water or would pass the Blacksmith a bit of food",1)
    prints("    or drink. It was the least you could do. Eventually the ore began to take shape.",1)
    prints("    With every strike of the Blacksmith's hammer, the ore was transformed into something",1)
    prints("    more and more like a sword. For many hours he continued on, sweating and laboring",1)
    prints("    over his task. Eventually, the ore became a blade. Later, a sword. Lastly, a treaure",1)
    prints("    worthy of a Hero. At last the Blacksmith hands you the weapon, a slight grin on his",1)
    prints("    otherwise expressionless face.",1)
    prints("    \"Here lad, take this. You'll need it to bring peace to these people.\"",1)
    prints("",1)
    prints("              ----####  YOU GOT THE SILVER SWORD #####----", 1)
    prints("",1)


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
spear = weapon("Spear", 2, 15, "stab", "A long, pointy boi. Watch out!")
silSword = weapon("Silver Sword", 3, 3, "expertly slash", "a masterwork weapon, it gleams in even the darkest corner")
smith_trades = [[axe, 35], [sword, 50], [hammer, 25], [spear, 30]]
smith_questTrades = [[silSword, "Silver Ore", blacksmith_questEnd, 3]]


smith = npc("Blacksmith", blacksmith_ascii, blacksmith_intro, smith_dialogue_options, smith_dialogue_outcomes, 0, smith_trades, smith_questTrades, 3, blacksmith_quest)



def librarian_intro():
    prints("")
    prints("The libarian is preocciuped with a stack of yellowing papers, strewn across her desk. She is so caught up",1)
    prints("in her study, in fact, that she hardly notices your approach. \"Uhm...Hello?\" you manage to ask meekly.",1)
    prints("She looks up at you in shock. You can't tell if it is your appearance, or shock at seeing another person in the library.",1)
    prints("")



def librarian_quest(self):
    prints("\"You're...what? You're looking for an amulet?,\" Regina asks as she stops shuffling papers around her desk.",1)
    prints("\"The AMULET!\" she cries out, \"OF COURSE!\", she exclaims.",1)
    prints("")
    prints("        Suddenly Regina's eyes narrow and she lowers her head. With very serious intonation in her voice, she explains,",1)
    prints("    \"The monks that looked after this library wrote at length about the Amulet. During an excavation in a far off land,",1)
    prints("    they were able to secure what is referred to as the \"Blood of Shadows\". Pretty cool name, right? Anyway, the Monks",1)
    prints("    sough to protect the Blood of Shadows, this Ruby, from the prying hands of evildoers. They chose this hamlet.",1)
    prints("    The only trouble with their plan were the hags. One day a monk of the order was travelling to a neighboring village when",1)
    prints("    he came across one fot he Hag sisters. They tortured him to find out where the Blood of Shadows was being kept.",1)
    prints("    With the right ritual, that Ruby can take in any and all shadows. Considering the Hags are pure evil, I don't know why",1)
    prints("    they'd want the Ruby unless it was somehow their weakness. The Ruby was last seen in the hands of the Hag, Mefilda Rottenbough.",1)
    prints("    I can't find any mention of that name anywhere though! Maybe you should talk to somoene who has been living here longer?",1)
    prints("    Bring me the ruby and I think I'll be able to recreate the spell from what I have in my notes.",1)
    prints("")
    self.setQuest("     **Turn in Ruby**", "\"May I see it?\"", 6, 0)
    prints("")


def librarian_questEnd(self):
    prints("")
    prints("    Regina practically snatches the Ruby from your hands, due to excitement. Like a whirlwind she runs back",1)
    prints("to her desk and begins unfurling a large scroll. \"Yes...it's right here...,\" she mutters to herself.",1)
    prints("Before long she is chanting in strange, ancient languages that you can't begin to comprehend. The room dims,",1)
    prints("your heart begins to pound within your chest, and the shadows all around you seem to come alive.",1)
    prints("Her voice rises, growing stronger and louder as she continues the spell. She looks to you with a satisfied eye,",1)
    prints("obviously proud of her work.",1)
    prints("....",1)
    prints(".........",.3)
    prints("                                    SUDDENLY THE WINDOWS BURST INWARDS",.3)
    prints("CRASH!!! BANG!!!!! ooooOOOOOOOOOOooooooOOOOOOOOOOoooooOOOOOOOOOOOOooooo.....")
    prints("")
    prints("oooooOOOOOOOOOOoooooOOOOOOOOOOoooooooo.....")
    prints("")
    prints("                        AND SHADOWS SEEM TO BLOT OUT THE SUN",.3)
    prints("                                              oooooOOOooooooOOOOOOOOOOOOOooooo")
    prints("")
    prints("THE WIND WHIPS AROUND YOU")
    prints("                                AND ALL BECOMES DARKNESS.")
    prints("")
    prints("",.3)
    prints("",.3)
    prints("    The wind calms itself. Broken glass is scattered everywhere. The sunlight glints off the glass dust",1)
    prints("that remains on the various books, scroll and papers lying about. Regina is doubled over, holding herself",1)
    prints("up on the table with a single arm. \"We did it,\" she grins, \"I made the Blood of Shadows.\"",1)
    prints("")
    prints("\"Here,\" she says, \"You take this...You'll need it to defeat the Hags.\"",1)
    prints("")
    prints("")
    prints("              ----####  YOU GOT THE BLOOD OF SHADOWS #####----", 1)
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


blood_of_shadows = qItem("Ruby Amulet", "An amulet, infused with the power to take in or dispel shadows.")
librarian_trade = [ [time_book, 25], [pamphlet, 5], [book_of_spells, 75] ]
librarian_questTrades = [[blood_of_shadows, "The Hangman's Ruby", librarian_questEnd, 4]]

librarian = npc("Librarian", librarian_ascii, librarian_intro, librarian_dialogue_options, librarian_dialogue_outcome, 0, librarian_trade, librarian_questTrades, 5, librarian_quest)



def merchant_intro():
    prints("")
    prints("The merchant's wagon is a beautiful site, adorned with many colors. The whole area around the wagon",1)
    prints("smelled of the most delicious of incenses. The merchant smiles at you from behind their stand, \"Greetings, friend.\"",1)
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

coldest_beer = qItem("Coldest Beer", "The stein somehow still has frost on it. Perhaps it has been magically cooled.")
merchant_trade = [ [small_health_chest, 25], [medium_health_chest, 50], [large_health_chest, 100], [small_armor_chest, 25], [medium_armor_chest, 50], [large_armor_chest, 100], [small_weapon_chest, 25], [medium_weapon_chest, 50], [large_weapon_chest, 100], [coldest_beer, 150]]



merchant_questTrades = []

merchant = npc("Merchant", merchant_ascii, merchant_intro, merchant_dialogue_options, merchant_dialogue_outcome, 0, merchant_trade)

def general_store_intro():
    prints("")
    prints("The soft chime of a bell alerts the owner to your presence. They turn around, leaning",1)
    prints("the broom they had been sweeping with against a column. \"Greetings, traveler!\"",1)
    prints("the owner addresses you jovially, \"Welcome! Welcome!",1)
    prints("")

def gen_quest(self):
    prints("")
    prints("Barry walks around the counter, briefly pausing to look out the front window as if he",1)
    prints("was afraid of being watched. He turns his back to the door as he turned the lock.",1)
    prints("    \"The Thief King runs a speakeasy in the sewers below the Hamlet.",1)
    prints("     I kind of got mixed up in some...irresponsible spending. I owe the",1)
    prints("     Thief King something like 5,000 gold. I don't have that kind of money!",1)
    prints("     No one lives in this town!\", he says. After a pause, and a wary look",1)
    prints("     around, he containues, \"You look like you're no stranger to a fight.",1)
    prints("     I don't care how you handle it, but settle my debt and I'll give you the",1)
    prints("     discount of a lifetime.\"",1)
    self.setQuest("     **Hand over the papers**", "\"You.. you actually did it!\"", 3, 0)
    prints("")

gen_trade = [ [wine, 3], [loaf_of_bread, 5], [kidney_beans, 3], [throwing_spear, 10], [sickle, 50], [artichokes, 3], [asiago_cheese, 50], [time_book2, 100] ]

def gen_questEnd(self):
    self.tradeOptions = [ [wine, 1], [loaf_of_bread, 2], [kidney_beans, 1], [throwing_spear, 5], [sickle, 25], [artichokes, 1], [asiago_cheese, 25], [time_book2, 50] ]
    prints("")
    prints("    From the moment the bell chimes, Barry is staring you down.",1)
    prints("\"Well? Have you done it? Is he finally going to stop harassing me?\" Barry asks,",1)
    prints("looking around nervously. You respond and tell him of your adventures down in the sewers.",1)
    prints("He pauses, scratching his chin and listening to you. \"So you're sure, that's it?\"",1)
    prints("You motion for him to calm down, setting his mind at ease.",1)
    prints("...",1)
    prints("\"Thank you so very much, stranger! Thank you! I swear I'll stop gambling.\"",1)
    prints("...Barry looks around abashedly. \"Ah...I almost forgot. Here you go!\" he says",1)
    prints("as he pulls out a large certificate. \"Your reward!\"",1)
    prints("")
    prints("")
    prints("  ----#### YOU'VE RECIEVED A PERMANENT DISCOUNT FOR THE GENERAL STORE! ####---- ",1)
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


gen_trade = [ [wine, 3], [loaf_of_bread, 5], [kidney_beans, 3], [throwing_spear, 10], [sickle, 50], [artichokes, 3], [asiago_cheese, 50], [time_book2, 100] ]

permanent_discount = qItem("Permanent Discount", "10 percent off of everything in the General Store, forever!")
gen_questTrades = [ [permanent_discount, "Debt Settled Papers", gen_questEnd, 3]  ]

general_store_owner = npc("General Store Owner", general_store_owner_ascii, general_store_intro, general_store_owner_dialogue_options, general_store_dialogue_outcome, 0, gen_trade, gen_questTrades, 3, gen_quest)



def farmer_intro():
    prints("")
    prints("The farmer was an older gentleman. Obviously panicked and in quite some distress,",1)
    prints("he can barely force words out between gasping for air. Something was terribly wrong.",1)
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
    prints("The Thief King does not appear to be remotely in the realm of toying around.",1)
    prints("They eye you with shrewd, cold eyes. \"Speak.\" was the only word they ushered",1)
    prints("from their lips before folding their arms acrossed their chest.",1)
    prints("")


def thief_king_quest(self):
    prints("")
    prints("    \"Get the Rat King to sign a treaty. I'm tired of losing good men to that animal.\"",1)
    prints("    The Thief King spits to their left, \"Bunch of mangy rodents. Have him sign it,",1)
    prints("    or kill them all. I don't care how it's done. The sewers already stink enough, so",1)
    prints("    what's a few more bodies.\"",1)
    self.setQuest("     **    Give him the treaty**", "\"Well done.\"", 4, 0)
    prints("")


def thief_king_questEnd(self):
    prints("")
    prints("    \"I can't believe you pulled it off. Fine. As promised,\" the Thief King",1)
    prints("says, handing you a sealed envelope.",1)
    prints("",1)
    prints("            ----#### YOU'VE SETTLED BARRY'S DEBT! ####---- ",1)
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

proof_of_debt_settled = qItem("Debt Settled Papers", "Proof that the debt between Barry Barrelpine and the Thief King was settled.")

signed_rat_king_treaty = qItem("Signed Treaty", "A treaty that promises an end to the violence between the Rat King and the Thief King.")
thief_king_questTrades = [ [proof_of_debt_settled, "Signed Treaty", thief_king_questEnd, 4 ] ]

thief_king = npc("Thief King", thief_king_ascii, thief_king_intro, thief_king_dialogue_options, thief_king_dialogue_outcome, -1, [], thief_king_questTrades, 4, thief_king_quest)





def drunkard_intro():
    prints("")
    prints("You almost feel bad for this sorry mess of a human. The bartender takes a coin",1)
    prints("from the pile in front of the man, placing a large bottle down in front of him.",1)
    prints("\"Sober up, you dolt!\", the bartender chastizes the drunkard.",1)
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
    prints("One of the miners approaches you, their pickaxe resting gently on their shoulders.",1)
    prints("\"Hail, friend,\" they call to you, \"Best not be traversing the mines!",1)
    prints("they say the place is just swarmin' with monsters today. Especially the deep caverns!\"",1)
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
    prints("\"HALT!,\" You are commanded. A burly man with a large chest and tall spear approaches you.",1)
    prints("He takes off his helmet as the other members of his unit keep their weapons trained on you until",1)
    prints("he bid them relax. \"It's alright lads, this one just seems a bit lost.\"",1)
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
    prints("    The Rat King was an intimidating creature. You thought that for sure that you were",1)
    prints("prepared for this, but find yourself speechless in it's presence. The large, almost humanoid",1)
    prints("shuffles towards you, waving the guards to the side. It is obvious that it does not consider",1)
    prints("you a threat.")
    prints("")


def rat_king_quest(self):
    prints("Kill... One... Of.. Them",2)
    self.setQuest("     **Hand it the finger**", "\"...\"", 4, 0)

def rat_king_questEnd():
    prints("    A treaty is haned to you by one of it's retainers, signed by the rat king.",1)
    prints("                    --- #### YOU'VE GOT THE Signed Treaty #### ---",1)
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
treaty = qItem("Signed Treaty", "The handwriting is surprisingly eligant")
rat_questTrades = [[treaty, "Hag's Finger", rat_king_questEnd, 4]]

rat_king = npc("Rat King", rat_king_ascii, rat_king_intro, rat_king_options, rat_king_outcomes, 0, rat_trades, rat_questTrades, 4, rat_king_quest)






