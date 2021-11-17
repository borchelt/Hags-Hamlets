#!/usr/bin/env python3
import time
import location
import player
from prints import printr
from prints import prints
import console
from item import item
from playsound import playsound
#setup


print("Loading...")

#set up the inital player and locations
startLocal = location.Location("Woods", "They are dark, and run deep.", "hnh_forestTheme_conceptQ.mp3", 
[item("old stump"), item("a spear in the ground"), item("your sense of dread")], ["More Woods"])
player1 = player.Player("", "It's you", 1, 10, 10, 10, 10, [item("nothing")], ["Rusty Sword", "Old Shield"], startLocal)



def main():
    #runtime

    #clear the console
    for i in (range(1,100)):
        print("")
    
    #all this is for show
    player1.name = input("What is your name, adventurer? ")

    if player1.name == "debug":
        con = console.console(player1)
        con.start()

    prints(f"\nOH! So you're {player1.name}, huh? Well, it's great to meet you.")

    prints(f"\nWell {player1.name}, I can't promise this world will be incredibly kind to you. Regardless, welcome to", 3)
    prints("          _______  _______  _______      __               _______  _______  _        _______ _________ _______ ",3)
    prints("|\     /|(  ___  )(  ____ \(  ____ \    /__\    |\     /|(  ___  )(       )( \      (  ____ \\__   __/(  ____ \\",.5)
    prints("| )   ( || (   ) || (    \/| (    \/   ( \/ )   | )   ( || (   ) || () () || (      | (    \/   ) (   | (    \/",.5)
    prints("| (___) || (___) || |      | (_____     \  /    | (___) || (___) || || || || |      | (__       | |   | (_____ ",.3)
    prints("|  ___  ||  ___  || | ____ (_____  )    /  \/\  |  ___  ||  ___  || |(_)| || |      |  __)      | |   (_____  )",.3)
    prints("| (   ) || (   ) || | \_  )      ) |   / /\  /  | (   ) || (   ) || |   | || |      | (         | |         ) |")
    prints("| )   ( || )   ( || (___) |/\____) |  (  \/  \  | )   ( || )   ( || )   ( || (____/\| (____/\   | |   /\____) |")
    prints("|/     \||/     \|(_______)\_______)   \___/\/  |/     \||/     \||/     \|(_______/(_______/   )_(   \_______)")

    for i in (range(1,160)):
        if i < 33:
            prints("O")
        elif(i < 66):
            prints("o",)
        elif(i<99):
            prints(".",)
        else:
            prints("", .1, False)
    prints("", 1)
    prints(f"you wake up.", 3)

    #start up the console
    con = console.console(player1)
    con.start()

if __name__ == "__main__":
    main()    

    
                                                                                                               







