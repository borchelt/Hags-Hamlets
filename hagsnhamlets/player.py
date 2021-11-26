#!/usr/bin/env python3
from prints import prints
from prints import printr
from random import *
from math import floor
import weapon
#placeholder
class Player(object):

    def __init__(self, name, desc, level, hp, mag, dex, str, inventory, equipped, location):
        self.name = name
        self.desc = desc
        self.level = level
        self.ac = 10 + dex
        self.hp = hp
        self.maxHp = hp
        self.mag = mag
        self.dex = dex
        self.str = str
        self.inventory = inventory
        self.equipped = equipped
        self.location = location
    
    def inven(self):

        if len(self.inventory) == 0:
            prints("you truly have nothing")

        prints("You shuffle around your pack. You have the following items")
        for i in range(len(self.inventory)):
            prints(f"{i+1}. {self.inventory[i].name}")
        quitB = False

        while not quitB:
            num = input(printr("enter the appropriate number to select an item, or enter \"q\" to quit: "))

            if "q" in num.lower()[0]:
                prints("You look up from your bag")
                break

            try:
                add = int(num)
                
                if(add-1 < len(self.inventory)):
                    prints("--------------")
                    prints(f"\033[1m{self.inventory[add-1].name}\033[0m")
                    prints("~~~~~~~~~~~~~~")
                    prints(f"\x1B[3m{self.inventory[add-1].desc}\x1B[0m")
                    prints("~~~~~~~~~~~~~~")
                    prints("--------------")
                    quitC = False
                    while(not quitC):
                        num = input(printr("what will you do with this? "))
                        
                        if "q" in num.lower()[0]:
                            for i in range(len(self.inventory)):
                                prints(f"{i+1}. {self.inventory[i].name}")
                            break
                        if("drop" in num or num == "d"):
                            self.location.interactables.append(self.inventory[add-1])
                            self.inventory.remove(self.inventory[add-1])

                            if len(self.inventory) == 0:
                                prints("you truly have nothing now")
                            for i in range(len(self.inventory)):
                                prints(f"{i+1}. {self.inventory[i].name}")
                            break

                        if "equip" in num or num == "e":
                            
                            if len(self.equipped) >= 2:
                                if type(self.inventory[add-1]) == weapon.weapon:
                                    prints(f"1. {self.equipped[0].name}")
                                    prints(f"2. {self.equipped[1].name}")
                                    acc = int(input(printr("Which item do you want to unequip first? ")))-1
                                    self.inventory.append(self.equipped[acc])
                                    self.equipped[acc] = self.inventory[add-1]
                                    self.inventory.remove(self.equipped[add-1])
                                    prints("equipped!")
                                    for i in range(len(self.inventory)):
                                        prints(f"{i+1}. {self.inventory[i].name}")
                                    quitC = True

                            else:
                                if type(self.inventory[add-1]) == weapon.weapon:
                                    self.equipped.append(self.inventory[add-1])
                                    self.inventory.remove(self.inventory[add-1])
                                    prints("equipped!")
                                    for i in range(len(self.inventory)):
                                        prints(f"{i+1}. {self.inventory[i].name}")
                                    quitC = True

                            
            except ValueError:
                continue
    def attack(self, weap, enemy):
        prints(f"You {weap.type} your {weap.name} at the {enemy.name}")
        prints(".", .5)
        enemy.hit([floor(randrange(1, 20) + weap.toHit + self.str), floor(randrange(1, 6) + weap.dmg + self.str)])

    def hit(self, aPack):
        roll = aPack[0]
        damage = aPack[1]
        if roll > self.ac:
            self.hp -= damage
            prints(f"It connects! You take {damage} damage.")
            prints(f"You have {self.hp}/{self.maxHp} HP remaining.")
        else:
            prints("It misses!")
        if self.hp <= 0:
            self.die()
        
    def die(self):
        prints("                   ___________________                     ",.3)
        prints("                 / ..,.,...,. .,.,...,.\                   ",.3)
        prints("                /               #####$$ \                  ",.3)
        prints("               /.,.                 ,,,..\                 ",.3)
        prints("              /.,.                   ,...||                ",.3)
        prints("              .      You Have Died      ..|                ",.3)
        prints("              |   ..$                     |                ",.3)
        prints("              ####                        |                ",.3)
        prints("              |   ###@$$2                 |                ",.3)
        prints("              |@$$#@#@                    |                ",.3)
        prints("              |                     ##### |                ",.3)
        prints("              |   ...                     |                ",.3)
        prints("              |        ...      #####     |                ",.3)
        prints("              | .......             ...   |                ",.3)
        prints("..............|___________________________|..............  ",.3)
        prints("@#$@#^$&^$%&$#%#$%#$^&$&^#$%@%@$#^@@$@@@#$@$#@#$@#$@#$@#$@@",.3)
        prints("@@$@$@#^$^%$&$%#%@#$%#&$#$@$$#^#@@@#$@##$#@#$@#$@#$#@$@#$#@",.3)
        prints("")
        prints("")
        prints("        Within minutes of your passing, a swarm            ", .3)
        prints("    of rats is upon your corpse. Soon there is nothing     ", .3)
        prints("    left of your mortal remains. Your weapons have been    ", .3)
        prints("    carted off to the Rat King's Nest, where they will     ", .3)
        prints("    remain until one who is worthy comes to claim them.    ", .3)
        prints("                                                            ", .3)
        prints("                                                            ", .3)
        prints("^%$&%^*%^$&$^W$#&$%*&^&(^%$#$%^#$$%@$#%^&$^%*&%^&$^#$%#$%@##", .3)
        prints("@#^%*^&*^%&$%^#%#$&%*^&$%%^$*^&&$%^#$^$%&%^*^&*^&%$^^#^#%#%@00", .3)
        input(printr("Press any key to continue:"))
        exit()
