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
from ascii_art import * 
import enemy
import weapon
import combat

#setup


print("Loading...")

#set up the inital player and locations
weap = weapon.weapon("old bone club", 
                                   -1, 
                                    3, 
                            "swings")

spear = weapon.weapon("old spear", 
                                1, 
                                0, 
                                "stab")

sword = weapon.weapon("sword", 
                            1, 
                            0, 
                        "slash")

shield = weapon.weapon("old shield", 
                                 -1, 
                                  0, 
                            "swing")

                            
startLocal = location.Location("Woods", "They are dark, and run deep.", "hnh_forestTheme_conceptQ.mp3", 
[item("old stump", "a stump", False), spear, item("dread")], ["The Tavern", "More Woods", "More Woods"], [])
player1 = player.Player("", "It's you", 1, 10, 10, 0, 10, [item("nothing")], [sword, shield], startLocal)

skele = enemy.enemy("Skeleton","A pile of bones, held together only by the will of the dead.", 5, 
                    [weap,weap,weap], 10, [item("bone shard")], "The Skeleton crumbles to dust.", startLocal)
#strange_spirit = enemy.enemy("Strange Spirit", "A frightening spectre.", 666, [], 666, [item("Hag's Soul")], "The Hag Queen screeches as she disintegrates into thousdands of dark particles.", startLocal)
#startLocal.enemyArr = [skele, strange_spirit]
startLocal.enemyArr = [skele]

def main():
    #runtime

    #clear the console
    for i in (range(1,100)):
        print("")
    
    #all this is for show
    
    player1.name = input("Hello ADVENTURER! What is your name? >>> ")

    if player1.name == "debug":
        con = console.console(player1)
        con.start()
        exit()

    print(f"\nOH! So you're {player1.name}, huh? Well, it's great to meet you.")
    
    #border_left = ["#|.  ||     ", "#| . ||     ", "#|.  ||     ", "#| . ||     "]
    border_right = ["        ||  .|#", "        || . |#", "        ||  .|#", "        || . |#"] 




    """   print(f"\nWell {player1.name}, I can't promise this world will be incredibly kind to you. Regardless, WELCOME TO")
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

    press_anything = input("Press anything to continue >>>> ")
    
    skip_intro = input("Would you like to skip the intro? Y/N >>>> " ).lower()
    if skip_intro == "yes" or skip_intro == "y":
        intro = False 
    else:
        intro = True  

    need_tutorial = input("Would you like to play through the tutorial? Y/N >>>> " ).lower()
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
    con.start()
    
    


if __name__ == "__main__":
    main()    

    
                                                                                                               







