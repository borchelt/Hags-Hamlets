#!/usr/bin/env python3
import location
import player
from prints import printr
from prints import prints
import console
from item import item
#setup


print("Loading...")

#set up the inital player and locations
startLocal = location.Location("Woods", "They are dark, and run deep.", "hnh_forestTheme_conceptQ.mp3", 
[item("old stump"), item("old spear"), item("dread")], ["More Woods", "More Woods", "More Woods"])
player1 = player.Player("", "It's you", 1, 10, 10, 10, 10, [item("nothing")], ["Rusty Sword", "Old Shield"], startLocal)



def main():
    #runtime

    #clear the console
    for i in (range(1,100)):
        print("")
    
    #all this is for show
    prints("")
    player1.name = input("Hello ADVENTURER! What is your name? >>> ")

    if player1.name == "debug":
        con = console.console(player1)
        con.start()
        exit()

    prints(f"\nOH! So you're {player1.name}, huh? Well, it's great to meet you.")

    prints(f"\nWell {player1.name}, I can't promise this world will be incredibly kind to you. Regardless, welcome to", 3)
    prints("---------------------------------------------------------------------------------------------------------------",3)
    prints("        -------------------------------------------------------------------------------------------------------", 3)
    prints("          _______  _______  _______      __               _______  _______  _        _______ _________ _______ ",3)
    prints("|\     /|(  ___  )(  ____ \(  ____ \    /__\    |\     /|(  ___  )(       )( \      (  ____ \\__   __/(  ____ \\",.5)
    prints("| )   ( || (   ) || (    \/| (    \/   ( \/ )   | )   ( || (   ) || () () || (      | (    \/   ) (   | (    \/",.5)
    prints("| (___) || (___) || |      | (_____     \  /    | (___) || (___) || || || || |      | (__       | |   | (_____ ",.3)
    prints("|  ___  ||  ___  || | ____ (_____  )    /  \/\  |  ___  ||  ___  || |(_)| || |      |  __)      | |   (_____  )",.3)
    prints("| (   ) || (   ) || | \_  )      ) |   / /\  /  | (   ) || (   ) || |   | || |      | (         | |         ) |")
    prints("| )   ( || )   ( || (___) |/\____) |  (  \/  \  | )   ( || )   ( || )   ( || (____/\| (____/\   | |   /\____) |")
    prints("|/     \||/     \|(_______)\_______)   \___/\/  |/     \||/     \||/     \|(_______/(_______/   )_(   \_______)")
    prints("Darkness overcomes you ##########################################################################", 2)
    prints("                       ########################################################")
    prints("and you feel yourself  ############################################", 2)
    prints("          .            ###################################")
    prints("begin                  ########################",2)
    prints("          .            #########")
    prints("              to fall. ######", 2)
    prints("          .            ###", 2)
    prints("                       ##",2)
    prints("Deeper    .            #", 2)
    prints("      ....and deeper...#", 2)
    prints(".......................#", 2 )


    need_tutorial = input("Would you like to play through the tutorial? Y/N >>>> " )
    if need_tutorial == "yes":
        print("Okay. We'll start with the tutorial.")
    else:
        print("No tutorial huh, tough guy?")
    
    for i in (range(1,160)):
        if i < 33:
            prints("O")
        elif(i < 66):
            prints("o",)
        elif(i<99):
            prints(".",)
        else:
                prints("", .1, False)

    print(".")
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

    prints(f"Suddenly, you are awake. You feel your head thump against the ground as you are being dragged. \n", 3)

    prints("\"You're awake! Oh! That's incredible. Just incredible...\" \n",3)

    prints("...The voice pauses, coughing and grunting as he lets go of your leg. \n", 3)

    prints("\"Forgive me friend, I thought you were dead! You understand...\" \n", 2)

    prints("You feel a hand reach down and hoist you two your feet. You're a little caught off guard! \n", 3)

    prints(f"\"Wait...no...it can't be! Are you?... {player1.name}????? \n" , 4)
    
    


    prints("Forgive me for not recognizing you at first... You look like one of them! \n" ,2)

    prints("The stranger points to your clothing. You're not wearing much. Your body is barely covered by some tattered robes. \n ",2)

    prints("---###     TAKE A MOMENT TO EXAMINE YOURSELF...TRY ENTERING THE COMMAND \"look at self\"     ###---",2)

    prints(" ---###      Hags & Hamlets is played by entering console commands.      ###---\n", 2)


    prints("\"Wow, so this is definitely a first,\" the stranger says. \n", 2)
    prints("The old man sits down on an old stump, pondering you. \n", 2) 

    prints("I don't know how you've done it, but you're still here. I wonder what it means. \n", 2)
    prints("You're not gonna to kill me are you...?,\" he asks, backing up slightly, \"I'm sorry for trying to bury you!", 2)
    
    #this question should unlock after first death/opens up a choice for random weapon/item/armor from previous lives
    
    #prints("Do you rememeber anything about yourself? ")
    
    prints("\"I wonder if you'd remember anything about me., \" the man asks with a queer look in his eyes\n", 3)
    prints("and scratching his chin. There is definitely something familiar about him, but you can't quite place it. \n", 3)

    prints("\"We'll have to get you back to the hamlet. \n", 2)



    #start up the console
    
    con = console.console(player1)
    con.start()
    





if __name__ == "__main__":
    main()    

    
                                                                                                               







