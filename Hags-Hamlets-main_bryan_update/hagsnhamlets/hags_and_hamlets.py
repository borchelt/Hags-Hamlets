#!/usr/bin/env python3
import location
import player
from prints import printr
from prints import prints
import console
from item import item
from dialogue import *
from tutorial import * 
from npcs import *
from intro import *
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

    prints(f"\nWell {player1.name}, I can't promise this world will be incredibly kind to you. Regardless, welcome to", .3)
    prints("---------------------------------------------------------------------------------------------------------------", .3)
    prints("        -------------------------------------------------------------------------------------------------------", .3)
    prints("          _______  _______  _______      __               _______  _______  _        _______ _________ _______ ", .3)
    prints("|\     /|(  ___  )(  ____ \(  ____ \    /__\    |\     /|(  ___  )(       )( \      (  ____ \\__   __/(  ____ \\",.3)
    prints("| )   ( || (   ) || (    \/| (    \/   ( \/ )   | )   ( || (   ) || () () || (      | (    \/   ) (   | (    \/",.5)
    prints("| (___) || (___) || |      | (_____     \  /    | (___) || (___) || || || || |      | (__       | |   | (_____ ",.3)
    prints("|  ___  ||  ___  || | ____ (_____  )    /  \/\  |  ___  ||  ___  || |(_)| || |      |  __)      | |   (_____  )",.3)
    prints("| (   ) || (   ) || | \_  )      ) |   / /\  /  | (   ) || (   ) || |   | || |      | (         | |         ) |")
    prints("| )   ( || )   ( || (___) |/\____) |  (  \/  \  | )   ( || )   ( || )   ( || (____/\| (____/\   | |   /\____) |")
    prints("|/     \||/     \|(_______)\_______)   \___/\/  |/     \||/     \||/     \|(_______/(_______/   )_(   \_______)")
    prints("                       ########################################################################################")
    prints("Darkness overcomes you ##########################################################################", 1)
    prints("                       ########################################################  A Text Adventure", .5)
    prints("and you feel yourself  ############################################                      by      ", .3)
    prints("          .            ###################################                       Wolfgang Borchelt", .3)
    prints("begin                  ########################                                          &         ",.2)
    prints("          .            #########                                                    Bryan Exley" ,  .1)
    prints("              to fall. ######", 2)
    prints("          .            ###", 2)
    prints("                       ##",2)
    prints("Deeper    .            #", 2)
    prints("      ....and deeper...#", 2)
    prints(".......................#", 2 )

    
    skip_intro = input("Would you like to skip the intro? Y/N >>>> " )
    if skip_intro == "yes" or skip_intro == "y":
        intro = False 
    else:
        intro = True  

    need_tutorial = input("Would you like to play through the tutorial? Y/N >>>> " )
    if need_tutorial == "yes" or need_tutorial == "y":
        prints(" --- ### You will play through the tutorial. ### --- ") 
        tutorial_needed = True 
    else:
        prints("You don't need the tutorial, huh? Tough guy. Good luck!")
    
    if intro == True:
        play_intro()

    if tutorial_needed == True: 
        tutorial()  
        combat_tutorial_zone()
    
    print("Try to look around here! \n")

    startLocal = location.Location("The Hamlet", "A small, unassuming hamlet. It is scarce of people, and there is a somber feeling that hangs in the air.", "hnh_forestTheme_conceptQ.mp3", 
    [item("Bucket"), item("Message Board"), item("Sundial")], ["Blacksmith", "The Tavern", "Traveling Merchant's Wagon"])




    #start up the console
    
    con = console.console(player1)
    con.start()
    





if __name__ == "__main__":
    main()    

    
                                                                                                               







