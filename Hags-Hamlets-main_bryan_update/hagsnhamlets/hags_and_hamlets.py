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
    
    player1.name = input("Hello ADVENTURER! What is your name? >>> ")

    if player1.name == "debug":
        con = console.console(player1)
        con.start()
        exit()

    print(f"\nOH! So you're {player1.name}, huh? Well, it's great to meet you.")
    
    #border_left = ["#|.  ||     ", "#| . ||     ", "#|.  ||     ", "#| . ||     "]
    border_right = ["        ||  .|#", "        || . |#", "        ||  .|#", "        || . |#"] 




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
    prints(".")
    press_anything = input("Press anything to continue >>>> ")
    press_anything
    
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
    
    
    #move to hamlet


    #move to tavern

    prints("----LATER AT THE TAVERN---- ", .3)
    prints("",.3)

    prints("####################################################################",.3)
    prints("",.3)

    prints("",.3)
    tavern_title_ascii()
    prints("",.3)
    tavern_ascii()
    prints("##################################################################### ", .3)
    prints("",.3)
    
    prints("",.3)
    prints("    You are terribly confused. You felt yourself die. You felt the light in yourself fade ", .3)
    prints("like a candle blown out by a draft. It was time to seek some answers. More importantly, ",.3)
    prints("you could use a little bit of sustenance.",.3)
    prints("",.3)

    innkeeper_dialogue()










    #start up the console
    
    con = console.console(player1)
    con.start()





if __name__ == "__main__":
    main()    

    
                                                                                                               







