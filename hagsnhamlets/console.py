#!/usr/bin/env python3

from os import name
from prints import printr
from prints import prints
from random import *
from math import floor
#from playsound import playsound
import item
from ascii_art import * 
from npcs import trade
from npcs import tradable_npcs
from location import * 

global action 

class console(object):
    def __init__(self, player):
        self.player = player
    
    #gets a player and prompts them to do things, the main controller of the game
    def start(self):
        turn = False
        p1 = self.player
        #playsound(p1.location.song, False)
        bigList = [p1.location.interactables, p1.location.enemyArr]
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
                turn = False
                quitB = True
            
            if(action == "inventory" or action == "open inventory" or action == "i"):
                turn = False
                p1.inven()
            #save method goes here once that is implemented

            #actions for looking at stuff

            #look around the area
            if(action == "look around"):
                turn = False
                prints(p1.location.look())
            #look at yourself
            elif(action == "look at myself" or action == "look at self"): 
                turn = False
                prints(p1.desc)

            #look at any object in your inventory or the area 
            elif("look at" in action): 
                turn = False
                target = action.replace("look at ", '')
                for i in everything:
                    if i.name.lower() == target:
                        prints(i.desc)

            #actions for picking stuff up

            if("pick up" in action):
                
                bigList = [p1.location.interactables, p1.location.enemyArr]
                everything = []
                for sub in bigList:
                    for i in sub:
                        everything.append(i)
                everything.append(p1.location)
                everything.append(p1)
                turn = True
                target = action.replace("pick up ", '')
                if target == "all":
                    for i in everything:
                        if type(i) is item.item or issubclass(type(i), item.item):
                            if(i.pickup):
                                p1.inventory.append(i)
                                p1.location.interactables.remove(i)
                                prints(f"You got the {i.name}")


                for i in everything:
                    if i.name.lower() == target:
                        if type(i) is item.item or issubclass(type(i), item.item):
                            if(i.pickup):
                                p1.inventory.append(i)
                                p1.location.interactables.remove(i)
                                prints(f"You got the {i.name}")
            #move action
            if ("move" in action):
                turn = True 
                for i in range(len(p1.location.adj_locations)): 
                    if p1.location.adj_locations[i.name] in action:
                        p1.move(p1.location.adj_locations[i])
                        break 
            else: 
                prints("I don't understand what you are trying to do.")
                

            #actions for combat 
            if action == "flee" or action == "run":

                if floor(random()) == 1:
                    prints("you run like the coward you are")
                    for i in len(self.p1.location.enemyArr):
                        self.p1.location.enemyArr.hit([999, 999], False)
                        
            if "attack" in action:
                turn = True
                target = action.replace("attack the ", '')
                target = action.replace("attack ", '')
                target = target.replace(" with", '')
                target = target.split(" ")
                if(len(target) > 2):
                    target[1] += " "

                if(len(target) == 1):
                    for i in p1.location.enemyArr:
                        if i.name.lower() == target[0]:
                            enemy = i
                    self.player.attack(self.player.equipped[0], i)
                num = 1
                while num < len(target)-1:
                    target[num] += target[num+1]
                    del target[num+1]
                    num += 1
                    
                enemy = False
                weapon = False

                for i in p1.location.enemyArr:
                    if i.name.lower() == target[0]:
                        enemy = i

                        for y in self.player.equipped:
                            if y.name.lower() == target[1]:
                                weapon = y
                if(enemy and weapon):
                    self.player.attack(weapon, i)

            #end of turn: enemies attack
            if(turn):
                for i in self.player.location.enemyArr:
                    att = randrange(0,2)
                    if att == 0:
                        i.attack(self.player)
                    if att == 1:
                        i.attack2(self.player)
                    if att == 2:
                        i.attack3(self.player)
            
            """   #actions for dialogue
                if "talk" in action:
                    turn = True 
                    target = action.replace("talk to ", '')
                    target = target.replace("talk with ", '')
            """      

            #Trade comes from NPCs
        
            if "trade" in action:
                for i in range(len(tradable_npcs)):
                    if tradable_npcs[i] in action:
                        target_npc = tradable_npcs[i]
                    elif i == len(tradable_npcs):
                        prints(f"I can't trade with {action}")
                        return 

                       
                trade(target_npc)    



