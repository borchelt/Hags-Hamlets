#!/usr/bin/env python3

from os import name
from prints import printr
from prints import prints
from random import *
from math import floor, trunc
#from playsound import playsound
import item
from asciiNameFetch import *

class console(object):
    turn = False
    def __init__(self, player):
        self.player = player
    
    def move(self, action):
        name = nameFetch()
        target = action.lower()
        target = target.replace("go to ", '')
        target = target.replace("move to ", '')
        target = target.replace("go ", "")
        target = target.replace("move ", "")
        for i in self.player.location.adj_locations:
                if i.name.lower() == target:
                    self.player.location = i
                    self.turn = False
                    name.printName(i.name)
                    prints(self.player.location.look())


        

    #gets a player and prompts them to do things, the main controller of the game
    def start(self):
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
                self.turn = False
                quitB = True
            
            if(action == "inventory" or action == "open inventory" or action == "i"):
                self.turn = False
                p1.inven()
            #save method goes here once that is implemented

            #actions for looking at stuff

            #look around the area
            if(action == "look around"):
                self.turn = False
                prints(p1.location.look())
            #look at yourself
            elif(action == "look at myself" or action == "look at self"): 
                self.turn = False
                prints(p1.desc)

            #look at any object in your inventory or the area 
            elif("look at" in action): 
                self.turn = False
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
                self.turn = True
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

            #actions for combat 
            if "flee" in action or "run" in action:
                self.turn = True
                print(randrange(0,2))
                if randrange(0,2) == 1:
                    prints("you run like the coward you are")
                    self.move(f"go to {p1.location.adj_locations[randrange(0, len(p1.location.adj_locations))].name}")
                        
            if "attack" in action:
                self.turn = True
                target = action
                target = target.replace("attack the ", '')
                target = target.replace("attack ", '')
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
                        if(len(target) == 2):
                            for y in self.player.equipped:
                                if y.name.lower() == target[1]:
                                    weapon = y
                if(enemy and weapon):
                    self.player.attack(weapon, i)
            
            if "go" in action or "move" in action:
                if(p1.location.enemyArr == []):
                    self.move(action)

            #end of turn: enemies attack
            if(self.turn):
                for i in self.player.location.enemyArr:
                    att = randrange(0,2)
                    if att == 0:
                        i.attack(self.player)
                    if att == 1:
                        i.attack2(self.player)
                    if att == 2:
                        i.attack3(self.player)

    


                

