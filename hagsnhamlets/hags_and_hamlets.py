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

from map import *
#setup


print("Loading...")

#set up the inital player and locations

""" 
weap = weapon("old bone club", -1, 3, "swings")
"""

spear = weapon("old spear", 1, 3,"stab")

sword = weapon("sword", 1, 0, "slash")

shield = weapon("old shield", -1, 0, "swing") 

silOre = item("Silver Ore", "it glitters with potential")
                            
local = location.Location("","","",[],[map.cemetery],[])
player1 = player.Player("", "It's you", 50, 10, 10, [item("Dread", "It festers.")], [sword, shield], local, rat_king)




def main():
    gameEnd = False

    while gameEnd == False:

        for i in (range(1,100)):
            print("")

        prints("dwfgirygidwegflleiagfliudwegafeugdwaouifgowkliugfiuywderggfy iyegfioyergyfiorgfsoigdiuirwegsfiurwgifgwaiugfiuywaregfiywaergfrigwiealgfriuywergfigwsgfwiluegfiwufgilwefgi")
        player1.hp = randint(25,50)
        player1.maxHp = player1.hp
        player1.dex = randint(0, 10)
        player1.ac = 50 + player1.dex
        player1.str = 100 - player1.dex + randint(3, 5) 
        player1.dead = False
        player1.location = local
        player1.equipped = [sword, shield]
        #runtime1

        #clear the console
        
        
        #all this is for show
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

        if player1.name == "debug":
            con = console.console(player1)
            con.move("go to the graveyard")
            con.start()
            continue

        prints(f"OH! So you're {player1.name}, huh? Well, it's great to meet you.")
        
        #border_left = ["#|.  ||     ", "#| . ||     ", "#|.  ||     ", "#| . ||     "]
        border_right = ["        ||  .|#", "        || . |#", "        ||  .|#", "        || . |#"] 



        """ 
        print(f"\nWell {player1.name}, I can't promise this world will be incredibly kind to you. Regardless, WELCOME TO")
        prints("---------------------------------------------------------------------------------------------------------------         ||  .|#", .5)
        prints("        -------------------------------------------------------------------------------------------------------         || . |#", .5)
        prints("          _______  _______  _______      __               _______  _______  _        _______ _________ _______          ||  .|#", .5)
        prints("    |\     /|(  ___  )(  ____ \(  ____ \    /__\    |\     /|(  ___  )(       )( \      (  ____ \\__   __/(  ____ \\      || . |#", .5)
        prints("    | )   ( || (   ) || (    \/| (    \/   ( \/ )   | )   ( || (   ) || () () || (      | (    \/   ) (   | (    \/     ||  .|#", .5)
        prints("    | (___) || (___) || |      | (_____     \  /    | (___) || (___) || || || || |      | (__       | |   | (_____      ||  .|#", .3)
        prints("    |  ___  ||  ___  || | ____ (_____  )    /  \/\  |  ___  ||  ___  || |(_)| || |      |  __)      | |   (_____  )     || . |#", .3)
        prints("    | (   ) || (   ) || | \_  )      ) |   / /\  /  | (   ) || (   ) || |   | || |      | (         | |         ) |     ||  .|#", .3)
        prints("    | )   ( || )   ( || (___) |/\____) |  (  \/  \  | )   ( || )   ( || )   ( || (____/\| (____/\   | |   /\____) |     || . |#", .3)
        prints("    |/     \||/     \|(_______)\_______)   \___/\/  |/     \||/     \||/     \|(_______/(_______/   )_(   \_______)     ||  .|#", .2)
        prints("                                                                                                                        || . |#", .2)
        prints("                       #######################################################################################          ||  .|#", .2)
        prints("                       ########################################################################################         || . |#", .2)
        prints("Darkness overcomes you ##########################################################################                       ||  .|#", .1)
        prints("          .            ########################################################                                         || . |#", .5)
        prints("                       ########################################################  A Text Adventure                       ||  .|#", .5)
        prints("and you feel yourself  ############################################                      by                             || . |#", .3)
        prints("          .            ###################################                       Wolfgang Borchelt                      ||  .|#", .3)
        prints("begin                  ########################                                          &                              || . |#", .2)
        prints("          .            #########                                                    Bryan Exley                         ||  .|#", .2)
        prints("                       ########                                                                                         ||  .|#", .2)
        prints("              to fall. ######            . - .                  . - .                       . - .                       || . |#", .3)
        prints("          .            ###             /      \               /        \                  /       \                     ||  .|#", .5)
        prints("                       ##             |  RIP   |             |   RIP    |                |   RIP   |                    || . |#", .3)
        prints("Deeper    .            #              |        |             |          |                |         |                    ||  .|#", .2)
        prints("      ....and deeper...#              |        |             |          |                |         |                    || . |#", .2)
        prints("#.....................#               |        |             |          |                |         |                    ||  .|#",  2)
        prints("##$%K#:$%K#LK%#:L%K#L:$K%.......#:K%$:.........$%K#$%K:LK#...............K#L$JK%#LKJ%LK%J............#K%L:#:L$%K$#:%K#% || . |#",  2)
        prints("#####$%#$%#$%#$#@@$", .2)
        prints("@$@$@$$%^$%^#@%#$@" , .2)
        prints("#$%$%^#@$@#       " , .2)
        prints("@$#@$             " , .2)
        prints("@@                " , .2)
        prints(".") """

        press_anything = input(printr("Press anything to continue >>>> "))
        
        skip_intro = input(printr("Would you like to skip the intro? Y/N >>>> " )).lower()
        if skip_intro == "yes" or skip_intro == "y":
            intro = False 
        else:
            intro = True  

        need_tutorial = input(printr("Would you like to play through the tutorial? Y/N >>>> " )).lower()
        if need_tutorial == "yes" or need_tutorial == "y":
            prints(" --- ### You will play through the tutorial. ### --- ") 
            tutorial_needed = True 
        else:
            prints("You don't need the tutorial, huh? Tough guy. Good luck!")
            tutorial_needed = False 
        
        if intro == True:
            play_intro()

        if tutorial_needed == True: 
            tutorial()  
            combat_tutorial_zone()
            dialogue_tutorial()

        
    


        #start up the console
        
        
        con = console.console(player1)
        con.quitB = False
        con.move("go to the graveyard")
        con.start()
    
    


if __name__ == "__main__":
    main()    

    
                                                                                                               







