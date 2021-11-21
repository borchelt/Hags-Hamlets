#!/usr/bin/env python3

from os import name
from prints import printr
from prints import prints
#from playsound import playsound
import item

class console(object):
    def __init__(self, player):
        self.player = player
    
    #gets a player and prompts them to do things, the main controller of the game
    def start(self):

        p1 = self.player
        #playsound(p1.location.song, False)
        bigList = [p1.location.interactables]
        everything = []
        for sub in bigList:
            for i in sub:
                everything.append(i)
        everything.append(p1.location)
        everything.append(p1)

        quitB = False
        while quitB == False:
            action = input(printr("> ")).lower()

            #actions for player management

            #quits the program
            if action == "quit":
                quitB = True
            
            if(action == "inventory" or action == "open inventory" or action == "i"):
                p1.inven()
            #save method goes here once that is implemented

            #actions for looking at stuff

            #look around the area
            if(action == "look around"):
                prints(p1.location.look())
            #look at yourself
            elif(action == "look at myself" or action == "look at self"): 
                prints(p1.desc)
            #look at any object in your inventory or the area 
            elif("look at" in action): 
                target = action.replace("look at ", '')
                for i in everything:
                    if i.name.lower() == target:
                        prints(i.desc)

            #actions for picking stuff up

            if("pick up" in action): 
                target = action.replace("pick up ", '')
                if target == "all":
                    for i in everything:
                        if type(i) is item.item:
                            if(i.pickup):
                                p1.inventory.append(i)
                                p1.location.interactables.remove(i)
                                prints(f"You got the {i.name}")


                for i in everything:
                    if i.name.lower() == target:
                        if type(i) is item.item:
                            if(i.pickup):
                                p1.inventory.append(i)
                                p1.location.interactables.remove(i)
                                prints(f"You got the {i.name}")


                

