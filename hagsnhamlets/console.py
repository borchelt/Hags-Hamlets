#!/usr/bin/env python3

from os import name, read
from prints import printr
from prints import prints
from random import *
from math import degrees, floor, trunc
#from playsound import playsound
from item import *
from ascii_art import * 
from npcs import *
from asciiNameFetch import *
from new_container import container
import re





class console(object):

    def __init__(self, player):
        self.player = player
        self.quitB = False
        self.everything = []
        self.hags = 0
        self.hagWarn = False
        self.hasSword = False
    
    def move(self, action):
        name = nameFetch(self.player.location.song)
        target = action.lower()
        target = target.replace("go to ", '')
        target = target.replace("move to ", '')
        target = target.replace("go ", "")
        target = target.replace("move ", "")
        target = re.sub(r'[^\w\s]', '', target)
        try:
            target = int(target)
            for y in self.player.location.interactables:
                if type(y) == item:
                    if y.pickup == True:
                        self.player.location.interactables.remove(y)
            
            name.printName(self.player.location.adj_locations[target-1].name, self.player.location.adj_locations[target-1], self.player)
            self.player.location = self.player.location.adj_locations[target-1]
            prints(self.player.location.look())
            self.turn = False


        
        except (ValueError, IndexError):

            for i in self.player.location.adj_locations:
                    tar = re.sub(r'[^\w\s]', '', i.name).lower()
                    if tar == target:
                        for y in self.player.location.interactables:
                            if type(y) == item:
                                if y.pickup == True:
                                    self.player.location.interactables.remove(y)
                        self.player.location = i
                        name.printName(i.name, i, self.player)
                        prints(self.player.location.look())
                        self.turn = False
            bigList = [self.player.location.interactables, self.player.location.enemyArr, self.player.inventory]
            for sub in bigList:
                for i in sub:
                    self.everything.append(i)
            self.everything.append(self.player.location)
            self.everything.append(self.player)
                
    #gets a player and prompts them to do things, the main controller of the game
    def start(self):
        turn = False
        p1 = self.player
        #playsound(p1.location.song, False)
        ready = False
        readyWeap = ""
        readyTurn = 0
        blocking = False
        hasWarned = False
        

        self.quitB = False
        while self.quitB == False:
            if p1.dead == True:
                self.quitB = True
                continue
            prints("")
            action = input(printr(">> ")).lower()

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
                prints("")
                prints(p1.location.look())
                prints("")

            #look at yourself
            elif(action == "look at myself" or action == "look at self" or action == "look self"): 
                turn = False
                prints("")
                prints(p1.desc)
                prints("")
                p1.sheet()

            #look at any object in your inventory or the area 
            elif("look at" in action): 
                turn = False
                target = action.replace("look at ", '')
                target = re.sub(r'[^\w\s]', '', target).lower()
                for i in self.everything:
                    name = re.sub(r'[^\w\s]', '', i.name).lower()
                    if name == target:
                        prints(i.desc)
            

            #actions for picking stuff up

            elif("pick up" in action):
                
                bigList = [p1.location.interactables, p1.location.enemyArr, p1.inventory]
                self.everything = []
                for sub in bigList:
                    for i in sub:
                        self.everything.append(i)
                self.everything.append(p1.location)
                self.everything.append(p1)
                turn = True
                target = action.replace("pick up ", '')
                target = re.sub(r'[^\w\s]', '', target).lower()
                if target == "all":
                    for i in self.everything:
                        if type(i) is item or issubclass(type(i), item):
                            if(i.pickup):
                                p1.inventory.append(i)
                                p1.location.interactables.remove(i)
                                prints(f"You got the {i.name}")


                for i in self.everything:
                    name = re.sub(r'[^\w\s]', '', i.name).lower()
                    if name == target:
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
                for i in self.everything:
                    if type(i) == container:
                        if i.name.lower() == target:
                            i.open(p1)
                            break 

            #actions for combat 
            elif "flee" in action or "run" in action:

                if randint(0, 1) == 1:
                    prints("You find yourself running away from the fight. Whether you were scared or in a hurry, who is to say.")
                    self.move(f"go to {p1.location.adj_locations[randrange(0, len(p1.location.adj_locations))].name}")
            
            elif "block" in action:
                turn = True
                p1.ac += p1.str
                blocking = True
                prints("you focus on blocking this next attack")
            elif "ready" in action or "charge" in action:
                turn = True

                

                if action == "ready" or action == "charge":
                    prints("you wind up for a larger attack")
                    p1.ac /= 2
                    ready = True
                    readyWeap = p1.equipped[0]
                target = action.replace("ready my ", "")
                target = target.replace("ready ", "")
                target = target.replace("charge ", "")
                target = target.replace("charge my ", "")
                print(target)

                if "main" in target:
                    prints("you wind up for a larger attack")
                    p1.ac /= 2
                    ready = True
                    readyWeap = p1.equipped[0]

                if "offhand" in target:
                    prints("you wind up for a larger attack")
                    p1.ac /= 2
                    ready = True
                    readyWeap = p1.equipped[1]
                
                for i in p1.equipped:
                    if target == i.name:
                        print("ready" + i.name)
                        p1.ac /= 2
                        ready = True
                        readyWeap = i
                        
            elif "attack" in action:
                turn = True
                target = action.replace("attack the ", '')
                target = target.replace("attack ", '')
                target = target.replace("attack", "")

                if ready:
                    if action == "attack":
                        if len(p1.location.enemyArr) >= 1:
                            p1.attack(readyWeap, p1.location.enemyArr[0], p1, ready)
                        else:
                            p1.attack(readyWeap, p1, p1, ready)

                    else:
                        for i in p1.location.enemyArr:
                            if i.name.lower() == target: 
                                self.player.attack(readyWeap, i, p1, ready)
                    
                    ready = False
                    p1.ac *= 2
                    readyTurn = 0

                elif action == "attack":
                    if len(p1.location.enemyArr) >= 1:
                        p1.attack(p1.equipped[0], p1.location.enemyArr[0], p1)
                    else:
                        p1.attack(p1.equipped[0], p1, p1)

                else:
                    for i in p1.location.enemyArr:
                        if i.name.lower() == target: 
                            self.player.attack(self.player.equipped[0], i, p1)
               
            
            elif "go" in action or "move" in action:
                turn = True
                if(p1.location.enemyArr == []):
                    
                    self.move(action)
            
            #consumables from console
            elif "equip" in action:
                target = action.replace("equip the ", "")
                target = target.replace("equip ", "")
                target = re.sub(r'[^\w\s]', '', target).lower()
                done = False

                for i in p1.location.interactables:
                    name1 = re.sub(r'[^\w\s]', '', i.name).lower()
                    if name1 == target:
                        done = True

                        if type(i) == armor:
                                    if  p1.armor == []:
                                        p1.armor = [i]
                                        p1.hp += i.toHP
                                        p1.maxHp += i.toHP
                                        p1.ac += i.toAC
                                        p1.location.interactrables.remove(i)
                                        prints("equipped!")

                                    else:
                                        p1.hp -= p1.armor[0].toHP
                                        p1.maxHp -= p1.armor[0].toHP
                                        p1.ac -= p1.armor[0].toAC
                                        prints(f"Unequipped {p1.armor[0].name}")
                                        p1.armor = [i]
                                        p1.hp += i.toHP
                                        p1.maxHp += i.toHP
                                        p1.ac += i.toAC
                                        p1.location.interactrables.remove(i)
                                        prints("equipped!")
                        if len(p1.equipped) >= 2:
                            if type(i) == weapon:
                                prints(f"1. {p1.equipped[0].name}")
                                prints(f"2. {p1.equipped[1].name}")
                                quitB = False
                                while not quitB:
                                    acc = (input(printr("Which item do you want to unequip first? ")))
                                    try:
                                        acc = int(acc)-1
                                        p1.inventory.append(p1.equipped[acc])
                                        p1.equipped[acc] = i
                                        p1.location.interactables.remove(i)
                                        prints("equipped!")
                                        quitB = True
                                    except ValueError:
                                        continue
                                    


                        else:
                            if type(i) == weapon:
                                p1.equipped.append(i)
                                p1.location.interactables.remove(i)
                                prints("equipped!")
                    if not done:
                        for i in p1.inventory:
                            name1 = re.sub(r'[^\w\s]', '', i.name).lower()
                            if name1 == target:

                                if type(i) == armor:
                                            if  p1.armor == []:
                                                p1.armor = [i]
                                                p1.hp += i.toHP
                                                p1.maxHp += i.toHP
                                                p1.ac += i.toAC
                                                p1.inventory.remove(i)
                                                prints("equipped!")

                                            else:
                                                p1.hp -= p1.armor[0].toHP
                                                p1.maxHp -= p1.armor[0].toHP
                                                p1.ac -= p1.armor[0].toAC
                                                prints(f"Unequipped {p1.armor[0].name}")
                                                p1.armor = [i]
                                                p1.hp += i.toHP
                                                p1.maxHp += i.toHP
                                                p1.ac += i.toAC
                                                p1.inventory.remove(i)
                                                prints("equipped!")
                                if len(p1.equipped) >= 2:
                                    if type(i) == weapon:
                                        prints(f"1. {p1.equipped[0].name}")
                                        prints(f"2. {p1.equipped[1].name}")
                                        quitB = False
                                        while not quitB:
                                            acc = (input(printr("Which item do you want to unequip first? ")))
                                            try:
                                                acc = int(acc)-1
                                                p1.inventory.append(p1.equipped[acc])
                                                p1.equipped[acc] = i
                                                p1.inventory.remove(i)
                                                prints("equipped!")
                                                quitB = True
                                            except ValueError:
                                                continue
                                            


                                else:
                                    if type(i) == weapon:
                                        p1.equipped.append(i)
                                        p1.inventory.remove(i)
                                        prints("equipped!")
                               
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
                prints("enemy with you main weapon")
                prints("or your readied weapon.")
                prints("------------------------")
                prints("Attack X: attack an enemy")
                prints("with your main weapon")
                prints("or your readied weapon.")
                prints("------------------------")
                prints("ready, charge: ready your")
                prints("main weapon. While readied")
                prints("your AC is cut in half.")
                prints("However, you deal 3x")
                prints("Damage if you hit your")
                prints("next attack")
                prints("------------------------")
                prints("ready X, charge X: ready")
                prints("either your offhand or")
                prints("mainhand weapon. you can")
                prints("call a weapon by name or")
                prints("use \"main\" and \"offhand\"")
                prints("------------------------")
                prints("block")
                prints("adds your strength to your")
                prints("AC.")
                prints("------------------------")
                prints("flee, run: flees to a ")
                prints("nearby area, leaving")
                prints("any enemies behind.")
                prints("------------------------")
                prints(".")

            
            else:
                prints("I'm not sure what you mean, type \"help\" for a list of commands")

            
            #end of turn
            
            if(turn):
                for i in p1.equipped:
                    if i.name == "Silver Sword" and map.hag3_BOSS.hp == 85:
                        prints("The weight of this sword fills you with courage")
                        map.hag3_BOSS.hp = 30
                        self.hasSword = True
                        break
                if self.hasSword == True:
                    for y in p1.equipped:
                        if y.name == "Silver Sword":
                            self.hasSword = True
                            break
                        else:
                            print("no silsword")
                            map.hag3_BOSS.hp = 85
                            self.hasSword = False

                    
                if p1.hb:
                    map.hag1_cleaver.dmg = 3
                    map.hag1_cleaver.toHit = 3
                    map.carriona_call.dmg = 1
                    map.carriona_call.toHit = 1
                    
                if ready:
                    if readyTurn > 0:
                        ready = False
                        readyTurn = 0
                        p1.ac *=2
                        prints("You drop your readied stance")
                    else:
                        readyTurn += 1

                for i in self.player.location.enemyArr:
                    att = randint(0,2)
                    if att == 0:
                        i.attack(self.player)
                    if att == 1:
                        i.attack2(self.player)
                    if att == 2:
                        i.attack3(self.player)
                
                if blocking:
                    p1.ac -= p1.str
                    blocking = False
            if(map.cottage.hag == True and map.deepwoods_HagLair.hag == True and map.dampCave.hag == True and hasWarned == False):
                hasWarned = True
                prints("As the last hag falls, you feel your stomach drop. Something isnt right.", 1)
                map.hamlet.adj_locations = []
                map.hamlet.interactables = [map.hag4]
                map.hag4.local = map.hamlet
                map.hamlet.desc = "  A defeaning scream fills the air and chills your blood. You can hardly resist covering your ears. The Hag Queen has come at last to avenge her fallen sisters. In the distance before you, you spot her, cloaked in shadows. In what seems like milliseconds she blips out of existence and reappears before you, a wild look in her eyes. \"I'll KILL YOU, CHILD! You cannot stop me!\" she screams at you. The world shakes beneath your feet."
            
            
            

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


                  


                       
                
