#!/usr/bin/env python3
from item import armor, consumable
from prints import prints
from prints import printr
from random import *
from math import floor
import weapon
#placeholder
class Player(object):

    def __init__(self, name, desc, hp, dex, str, inventory, equipped, location, rat, armor = [], hb = False, bloat = 0, luck = 0, gold = 0):
        self.name = name
        self.desc = desc
        self.ac = 5 + dex
        self.hp = hp
        self.maxHp = hp
        self.dex = dex
        self.str = str
        self.inventory = inventory
        self.equipped = equipped
        self.location = location
        self.gold = gold
        self.bloat = bloat
        self.rat = rat
        self.luck = luck
        self.hb = hb
        self.dead = False
        self.armor = armor
    
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
                    if type(self.inventory[add-1]) == weapon:
                        prints("--------------")
                        prints(f"\033[1m{self.inventory[add-1].name}\033[0m")
                        prints("~~~~~~~~~~~~~~")
                        prints(f"\x1B[3m{self.inventory[add-1].desc}\x1B[0m")
                        prints("~~~~~~~~~~~~~~")
                        prints(f"[+{self.inventory[add-1].toHit} | {self.inventory[add-1].dmg} Damage]")
                        prints("~~~~~~~~~~~~~~")
                        prints("--------------")
                    elif type(self.inventory[add-1]) == armor:
                        prints("--------------")
                        prints(f"\033[1m{self.inventory[add-1].name}\033[0m")
                        prints("~~~~~~~~~~~~~~")
                        prints(f"\x1B[3m{self.inventory[add-1].desc}\x1B[0m")
                        prints("~~~~~~~~~~~~~~")
                        prints(f"[+{self.inventory[add-1].toHP} HP | +{self.inventory[add-1].toAC} AC]")
                        prints("~~~~~~~~~~~~~~")
                        prints("--------------")
                    else:
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

                        if "drink" in num or "eat" in num or "use" in num or num == "u":
                            if type(self.inventory[add-1]) == consumable:
                                self.inventory[add-1].consume(self)
                                quitC = True
                                quitB = True
                                

                        if "equip" in num or num == "e":
                            if type(self.inventory[add-1]) == armor:
                                if self.armor == []:
                                    self.armor = [self.inventory[add-1]]
                                    self.hp += self.inventory[add-1].toHP
                                    self.maxHp += self.inventory[add-1].toHP
                                    self.ac += self.inventory[add-1].toAC
                                    prints("equipped!")
                                    for i in range(len(self.inventory)):
                                        prints(f"{i+1}. {self.inventory[i].name}")
                                    quitC = True
                                else:
                                    self.hp -= self.armor[0].toHP
                                    self.maxHp -= self.armor[0].toHP
                                    self.ac -= self.armor[0].toAC
                                    prints(f"Unequipped {self.armor[0].name}")
                                    self.armor = [self.inventory[add-1]]
                                    self.hp += self.inventory[add-1].toHP
                                    self.maxHp += self.inventory[add-1].toHP
                                    self.ac += self.inventory[add-1].toAC
                                    for i in range(len(self.inventory)):
                                        prints(f"{i+1}. {self.inventory[i].name}")
                                    quitC = True

                                    prints("equipped!")
                            if len(self.equipped) >= 2:
                                if type(self.inventory[add-1]) == weapon.weapon:
                                    prints(f"1. {self.equipped[0].name}")
                                    prints(f"2. {self.equipped[1].name}")
                                    acc = int(input(printr("Which item do you want to unequip first? ")))-1
                                    self.inventory.append(self.equipped[acc])
                                    self.equipped[acc] = self.inventory[add-1]
                                    self.inventory.remove(self.equipped[acc])
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
    def attack(self, weap, enemy, player, ready = False):
        prints(f"You {weap.type} your {weap.name} at the {enemy.name}")
        prints("...", .3)
        if ready:
            enemy.hit([randint(1, 20) + weap.toHit + self.str , (randint(1, 6) + weap.dmg + self.str) *3], player)
        else:
            enemy.hit([randint(1, 20) + weap.toHit + self.str, randint(1, 6) + weap.dmg + self.str], player)

    def hit(self, aPack, player):
        roll = aPack[0]
        damage = aPack[1]
        prints("...",.3)
        if roll > self.ac:
            self.hp -= damage
            prints(f"It connects! You take {damage} damage.",.3)
            prints(f"You have {self.hp}/{self.maxHp} HP remaining.",.3)
        else:
            prints("...It misses!",.3)
        if self.hp <= 0:
            self.die()

    def die(self):
        for i in range(len(self.inventory)):
            if not [self.inventory[i-1], 100] in self.rat.tradeOptions:
                print("gaveItem")
                self.rat.tradeOptions.append([self.inventory[i-1], 100])
        for i in range(len(self.equipped)):
            if not [self.equipped[i-1], 100] in self.rat.tradeOptions:
                print("gaveWeap")
                self.rat.tradeOptions.append([self.equipped[i-1], 100])
        
        self.inventory = []

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
        prints("",.3)
        prints("",.3)
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
        self.dead = True
    
    def sheet(self):
        prints("")
        prints("")
        prints(f"\033[1m{self.name}\033[0m")
        prints("---------------------------------")
        prints(f"HP:        {self.hp}/{self.maxHp}")
        prints(f"AC:        {floor(self.ac)}")
        prints(f"Strength:  {self.str}")
        prints(f"Dexterity: {self.dex}")
        prints(f"Gold:      {self.gold}")
        prints("---------------------------------")
        prints("\x1B[3mEquipped Items:\x1B[0m")
        for i in range(len(self.equipped)):
            prints(f"{i+1}. {self.equipped[i].name}")
        if self.armor != []:
            prints(f"{len(self.equipped)+1}. {self.armor[0].name}")
        quitB = False
        while quitB == False:
            prints("Open Inventory? Y/N")
            cont = input(printr("> ")).lower()
            if cont == "y" or cont == "yes":
                self.inven()
                quitB = True
            elif cont == "n" or cont == "no":
                quitB = True
            else:
                prints("This is a yes or no question")



    def heal(self, amount):
        self.hp += amount
        if(self.hp > self.maxHp):
            self.hp = self.maxHp