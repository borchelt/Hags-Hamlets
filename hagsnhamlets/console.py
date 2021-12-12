#!/usr/bin/env python3

from os import name
from prints import printr
from prints import prints
from random import *
from math import degrees, floor
#from playsound import playsound
from item import *
from ascii_art import * 
from npcs import *
from asciiNameFetch import *
from new_container import container


global action 

class console(object):
    def __init__(self, player):
        self.player = player
        self.quitB = False
    
    def move(self, action):
        name = nameFetch()
        target = action.lower()
        target = target.replace("go to ", '')
        target = target.replace("move to ", '')
        target = target.replace("go ", "")
        target = target.replace("move ", "")
        self.turn = False
        for i in self.player.location.interactables:
            if type(i) == item:
                if i.pickup == True:
                    print("removed " + i.name)
                    self.player.location.interactables.remove(i)
        for i in self.player.location.adj_locations:
                if i.name.lower() == target:
                    self.player.location = i
                    name.printName(i.name, i)
                    prints(self.player.location.look())
                    self.turn = False
                
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

        self.quitB = False
        while self.quitB == False:
            if p1.dead == True:
                self.quitB = True
                continue
            action = input(printr("> ")).lower()

            #actions for player management

            #quits the program
            if action == "quit":
                turn = False
                exit()
            
            elif action == "menu":
                turn = False
                self.quitB = True
            
            elif(action == "inventory" or action == "open inventory" or action == "i"):
                turn = False
                p1.inven()
            #save method goes here once that is implemented

            #actions for looking at stuff

            #look around the area
            elif(action == "look around"):
                turn = False
                prints(p1.location.look())
            #look at yourself
            elif(action == "look at myself" or action == "look at self" or action == "look self"): 
                turn = False
                prints(p1.desc)
                p1.sheet()

            #look at any object in your inventory or the area 
            elif("look at" in action): 
                turn = False
                target = action.replace("look at ", '')
                for i in everything:
                    if i.name.lower() == target:
                        prints(i.desc)
            

            #actions for picking stuff up

            elif("pick up" in action):
                
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
                        if type(i) is item or issubclass(type(i), item):
                            if(i.pickup):
                                p1.inventory.append(i)
                                p1.location.interactables.remove(i)
                                prints(f"You got the {i.name}")


                for i in everything:
                    if i.name.lower() == target:
                        if type(i) is item or issubclass(type(i), item):
                            if(i.pickup):
                                p1.inventory.append(i)
                                p1.location.interactables.remove(i)
                                prints(f"You got the {i.name}")
            
            #open containers
            elif "open" in action or "look in" in action:
                turn = False
                target = action
                target = target.replace("open the ", "")
                target = target.replace("open ", "")
                target = target.replace("look in the ", "")
                target = target.replace("look in ", "")
                for i in everything:
                    if type(i) == container:
                        if i.name.lower() == target:
                            i.open(p1)

            #actions for combat 
            elif "flee" in action or "run" in action:

                if randint(0, 1) == 1:
                    prints("you run like the coward you are")
                    self.move(f"go to {p1.location.adj_locations[randrange(0, len(p1.location.adj_locations))].name}")
                        
            elif "attack" in action:
                turn = True
                target = action.replace("attack the ", '')
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
                else:
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
                                print(target)
                                if y.name.lower() == target[1]:
                                    weapon = y
                    if(enemy and weapon):
                        self.player.attack(weapon, i)
            
            elif "go" in action or "move" in action:
                if(p1.location.enemyArr == []):
                    turn = False
                    self.move(action)
            
            #consumables from console

            elif "drink" in action or "eat" in action or "use" in action:
                turn = True
                drank = False
                target = action
                target = target.replace("eat the ", "")
                target = target.replace("drink the ", "")
                target = target.replace("use the ", "")
                target = target.replace("eat ", "")
                target = target.replace("drink ", "")
                target = target.replace("use ", "")

                for i in p1.location.interactables:
                    if(drank == False):
                        if i.name.lower() == target:
                            if type(i) is consumable:
                                local = p1.location
                                i.consume(p1)
                                local.interactables.remove(i)
                                drank = True

                for i in p1.inventory:
                    if(drank == False):
                        if i.name.lower() == target:
                            if type(i) is consumable:
                                i.consume(p1)
                                p1.inventory.remove(i)
                                drank = True
 
            #actions for dialogue
            elif "talk" in action:
                turn = True 
                target = action
                target = target.replace("talk to the ", "")
                target = target.replace("talk with the ", "")
                target = target.replace("talk to ", '')
                target = target.replace("talk with ", '')
                for i in p1.location.interactables:
                    if i.name.lower() == target and type(i) == npc:
                        i.talk(p1)

            elif "help" in action:
                turn = False
                prints("Actions in Hags & Hamlets:")
                prints(".")
                prints("------------------------")
                prints("------Meta actions------")
                prints("------------------------")
                prints("quit: quits the game.")
                prints("------------------------")
                prints("menu: quits to the") 
                prints("main menu.")
                prints("------------------------")
                prints("inventory, i: opens")
                prints("your inventory.")
                prints("------------------------")
                prints(".")
                cont = input(printr("Continue? Y/N")).lower
                if(cont == "n" or cont == "no"):
                    break
                prints("------------------------")
                prints("------Information-------")
                prints("------------------------")
                prints("look at X: looks at") 
                prints("something, you can look") 
                prints("at yourself or other")
                prints("enemeies, npcs or objects.")
                prints("------------------------")
                prints("look around: gives you")
                prints("the lay of the land,")
                prints("very important for ")
                prints("remembering where you") 
                prints("are and where you can go.")
                prints("------------------------")
                prints(".")
                cont = input(printr("Continue? Y/N")).lower
                if(cont == "n" or cont == "no"):
                    break
                prints("------------------------")
                prints("------Interaction-------")
                prints("------------------------")
                prints("pick up X: pick up an")
                prints("item, you can use pick up")
                prints("all to pick up every item")
                prints("near you.")
                prints("------------------------")
                prints("Open X, Look in X: some")
                prints("items are containers, you")
                prints("can look inside them with")
                prints("this command.")
                prints("------------------------")
                prints("Eat X, Drink X, Use X:")
                prints("consumable items are vital")
                prints("to adventuring in Hags &")
                prints("Hamlets. You can store")
                prints("them in your inventory or")
                prints("use any that are nearby.")
                prints("------------------------")
                prints("Talk to X: the denezens")
                prints("of the hamlet are full")
                prints("of useful information, it")
                prints("is wise to commune with")
                prints("them.")
                prints("------------------------")
                prints(".")
                cont = input(printr("Continue? Y/N")).lower
                if(cont == "n" or cont == "no"):
                    break
                prints("------------------------")
                prints("-------Movement---------")
                prints("------------------------")
                prints("go to X, move to X")
                prints("you can move between ")
                prints("locations, but only ones")
                prints("nearby. You might want")
                prints("to bring a map.")
                prints("------------------------")
                prints(".")
                cont = input(printr("Continue? Y/N")).lower
                if(cont == "n" or cont == "no"):
                    break
                prints("------------------------")
                prints("--------Combat----------")
                prints("------------------------")
                prints("Attack: attacks the first")
                prints("enemy with you main weapon.")
                prints("------------------------")
                prints("Attack X: attack an enemy")
                prints("with your main weapon.")
                prints("------------------------")
                prints("Attack X with Y: attack an")
                prints("enemy with either your")
                prints("main or off-hand weapon.")
                prints("------------------------")
                prints("flee, run: flees to a ")
                prints("nearby area, leaving")
                prints("any enemies behind.")
                prints("------------------------")
                prints(".")

            
            else:
                prints("I'm not sure what you mean, type \"help\" for a list of commands")

            #end of turn: enemies attack
            if(turn):
                for i in self.player.location.enemyArr:
                    att = randint(0,2)
                    if att == 0:
                        i.attack(self.player)
                    if att == 1:
                        i.attack2(self.player)
                    if att == 2:
                        i.attack3(self.player)
            
            
            

            # if "give" in action:
            #     turn = True
            #     target = action
            #     target = target.replace("give the ", '')
            #     target = target.replace("give ", '')
            #     target = target.replace(" to", '')
            #     target = target.split(" ")
            #     if(len(target) > 2):
            #         print(target)
            #         target[0] += " "
            #         target[0] = target[0]+target[1]
            #         target.remove(target[1])
            #         print(target)   
            #     for i in p1.location.interactables:
            #         if i.name.lower() == target[1] and type(i) == npc:
            #             print("foundNPC")
            #             for y in p1.inventory:
            #                 if target[0] == y.name.lower():
            #                     print("foundItem")
            #                     for l in i.questTrades:
            #                         print(l)
            #                         if l[1] == y.name:
            #                             print("foundTrade")
            #                             p1.inventory.append(l[0])
            #                             l[2]()


                  


                       
                



