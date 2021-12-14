#!/usr/bin/env python3
#from item_list import *
#from console import player
from prints import *
#from asciiNameFetch import nameFetch

class item:
    
    def __init__(self, name, desc, pickup = True):
        self.name = name
        self.desc = desc
        self.pickup = pickup

class qItem(item):
    def __init__(self, name, desc, pickup=True):
        super().__init__(name, desc, pickup=pickup)
        
class consumable(item):
    def __init__(self, name, desc, affectArr, pickup=True, isFood = False):
        super().__init__(name, desc, pickup=pickup)
        self.arr = affectArr
    
    def consume(self, player):
        type = self.arr[0]
        amount = self.arr[1]

        if type == "hp":
            player.heal(amount)
            prints("You feel refreshed")
        elif type == "str":
            player.str += amount
            prints("You feel your geat become lighter")
        elif type == "dex":
            player.dex += amount
            player.ac = player.dex + 10
            prints("The world seems to slow ever so much")
        elif type == "luck":
            player.luck += amount
            prints("You feel nothing")
        elif type == "tp":
            prints("You close your eyes as you chug the bitter potion, when they open:")
            player.location = amount
            amount.look()
        elif type == "hagsBane":
            prints("you gulp it down. It tastes horrible, but you dont feel dead yet.")
            player.hb = True
        
        player.bloat += 1
        self = None

class armor(item):
    def __init__(self, name, toHP, toAC, desc="tempDesc", pickup=True,):
        super().__init__(name, desc=desc, pickup=pickup)
        self.toHP = toHP
        self.toAC = toAC
