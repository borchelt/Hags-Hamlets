#!/usr/bin/env python3
import location
import player
from prints import printr
from prints import prints
import console
from item import item
#from dialogue import *
from tutorial import * 
#from npcs import *
from intro import *
from ascii_art import * 
import enemy
import weapon
import combat
from npcs import *
from random import *
from asciiNameFetch import nameFetch
import music
import musicPlayer

from map import *
#setup


print("Loading...")

#set up the inital player and locations

""" 
weap = weapon("old bone club", -1, 3, "swings")
"""

local = location.Location("","","",[],[map.cemetery])
sword = weapon("sword", 1, 0, "slash")

shield = weapon("old shield", -1, 0, "swing") 


player1 = player.Player("", "It's you", 50, 10, 10, [item("Dread", "It festers.")], [sword, shield], map.cemetery, rat_king)




def main():
    gameEnd = False
    intro = True
    for i in (range(1,100)):
            print("")
    printsl("---------------------------------------------------------------------------------------------------------------", .5)
    printsl("        -------------------------------------------------------------------------------------------------------", .5)
    printsl("              _______  _______  _______      __               _______  _______  _        _______ _________ _______", .5)
    printsl("    |\     /|(  ___  )(  ____ \(  ____ \    /__\    |\     /|(  ___  )(       )( \      (  ____ \\__   __/(  ____ \\", .5)
    printsl("    | )   ( || (   ) || (    \/| (    \/   ( \/ )   | )   ( || (   ) || () () || (      | (    \/   ) (   | (    \/", .5)
    printsl("    | (___) || (___) || |      | (_____     \  /    | (___) || (___) || || || || |      | (__       | |   | (_____ ", .3)
    printsl("    |  ___  ||  ___  || | ____ (_____  )    /  \/\  |  ___  ||  ___  || |(_)| || |      |  __)      | |   (_____  )", .3)
    printsl("    | (   ) || (   ) || | \_  )      ) |   / /\  /  | (   ) || (   ) || |   | || |      | (         | |         ) |", .3)
    printsl("    | )   ( || )   ( || (___) |/\____) |  (  \/  \  | )   ( || )   ( || )   ( || (____/\| (____/\   | |   /\____) |", .3)
    printsl("    |/     \||/     \|(_______)\_______)   \___/\/  |/     \||/     \||/     \|(_______/(_______/   )_(   \_______)", .2)
    printsl("                                                                                                                   ", .2)
    printsl("                       #######################################################################################     ", .2)
    printsl("                       ########################################################################################    ", .2)
    printsl("Darkness overcomes you ##########################################################################                  ", .1)
    printsl("          .            ########################################################                                    ", .5)
    printsl("                       ########################################################  A Text Adventure                  ", .5)
    printsl("and you feel yourself  ############################################                      by                        ", .3)
    printsl("          .            ###################################                       Wolfgang Borchelt                 ", .3)
    printsl("begin                  ########################                                          &                         ", .2)
    printsl("          .            #########                                                    Bryan Exley                    ", .2)
    printsl("                       ########                                                                                    ", .2)
    printsl("              to fall. ######            . - .                  . - .                       . - .                  ", .3)
    printsl("          .            ###             /      \               /        \                  /       \                ", .5)
    printsl("                       ##             |  RIP   |             |   RIP    |                |   RIP   |               ", .3)
    printsl("Deeper    .            #              |        |             |          |                |         |               ", .2)
    printsl("      ....and deeper...#              |        |             |          |                |         |               ", .2)
    printsl("#.....................#               |        |             |          |                |         |               ",  2)
    printsl("##$%K#:$%K#LK%#:L%K#L:$K%.......#:K%$:.........$%K#$%K:LK#...............K#L$JK%#LKJ%LK%J............#K%L:#:L$%K$#:",  2)
    printsl("#####$%#$%#$%#$#@@$", .2)
    printsl("@$@$@$$%^$%^#@%#$@" , .2)
    printsl("#$%$%^#@$@#       " , .2)
    printsl("@$#@$             " , .2)
    printsl("@@                " , .2)
    printsl(".") 
    vol = input(printr("The current volume is 5, please enter a number to change the volume, or press any other button to continue: "))
    try:
        vol = int(vol)/10
        music.setvol(vol)
        musicPlayer.setvol(vol)
        print(vol)
    except ValueError:
        pass

    hasDoneTut = False

    while gameEnd == False:
        map.ref(map)
        if intro == False:
            for i in (range(1,100)):
                print("")
                intro = False

        prints("Hags & Hamlets is an unforgiving game, if you wish, you may be spared this hardship.")
        godMode = input(printr("GODMODE? Y/N >> ")).lower()

        if godMode == "y" or godMode == "yes":
            player1.hp = randint(100, 200)
            player1.maxHp = player1.hp
            player1.dex = randint(100, 100)
            player1.ac = 500 + player1.dex
            player1.str = 10000 - player1.dex + randint(3000, 5000) 
            player1.dead = False
            player1.location = local
            player1.equipped = [sword, shield]
        else:
            player1.hp = randint(25,50)
            player1.maxHp = player1.hp
            player1.dex = randint(0, 10)
            player1.ac = 5 + player1.dex
            player1.str = 10 - player1.dex + randint(3, 5) 
            player1.dead = False
            player1.location = local
            player1.equipped = [sword, shield]
        #runtime1


        
        

        prints("Hags & Hamlets is a dark world full of danger. are you sure you want to continue?", 1)
        prints("1. Yes, I'm ready.",1)
        prints("2. No, let me out!",1)
        quitCheck = False
        while quitCheck == False:
            quitVal = input((printr("> "))).lower()
            
            if quitVal == "1" or quitVal == "y" or quitVal == "yes":
                pass
                quitCheck = True
            elif quitVal == "2" or quitVal == "n" or quitVal == "no":
                exit()
            else:
                prints("This is a yes or no question")
        player1.name = input(printr("Hello ADVENTURER! What is your name? >>> "))

        # if player1.name == "debug":
        #     con = console.console(player1)
        #     con.move("go to the graveyard")
        #     con.start()
        #     continue

        prints(f"OH! So you're {player1.name}, huh? Well, it's great to meet you.")
        
        #border_left = ["#|.  ||     ", "#| . ||     ", "#|.  ||     ", "#| . ||     "]
        border_right = ["        ||  .|#", "        || . |#", "        ||  .|#", "        || . |#"] 



         


        
        
        intro = True  

        tutorial_needed = False

        need_tutorial = input(printr("Would you like to play through the tutorial? Y/N >>>> " )).lower()
        if need_tutorial == "yes" or need_tutorial == "y":
            prints(" --- ### You will play through the tutorial. ### --- ") 
            tutorial_needed = True 

        else:
            prints("You don't need the tutorial, huh? Tough guy. Good luck!")
            tutorial_needed = False 
        
        if intro == True:
            pass
            #play_intro()

        if tutorial_needed == True: 
            tutorial()  
            combat_tutorial_zone()
            dialogue_tutorial(player1)
            prints("Remember: you can type \"help\" at any time for a list of commands")
            name = nameFetch()
            name.hamlet_title_ascii()
            player1.location = map.tavern
            map.tavern.look()
            

        
    


        #start up the console
        
        
        con = console.console(player1)
        con.quitB = False
        con.move("go to the graveyard")
        con.start()
    
    


if __name__ == "__main__":
    main()    

    
                                                                                                               







