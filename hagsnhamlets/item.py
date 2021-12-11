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
        
class consumable(item):
    def __init__(self, name, desc, affectArr, pickup=True):
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
            prints("You close your eyes as you chug the bitter potion, when they open, you are in:")
            player.location = amount
            #name = nameFetch()
            #name.printName(amount.name,amount)
            amount.look()
        elif type == "hagsBane":
            player.hb = True
        
        player.bloat += 1
        self = None
