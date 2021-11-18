#!/usr/bin/env python3
from prints import prints
from prints import printr
#placeholder
class Player(object):

    def __init__(self, name, desc, level, hp, mag, dex, str, inventory, equipped, location):
        self.name = name
        self.desc = desc
        self.level = level
        self.hp = hp
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

            except ValueError:
                continue

           
    
