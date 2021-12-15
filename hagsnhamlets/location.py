#!/usr/bin/env python3
from prints import printr
from prints import prints
from item_list import *


class Location(object):

    def __init__(self, name, desc, song, interactables, adj_locations, enemyArr = [], indoors = False, hag = False):

        self.name = name
        self.desc = desc
        self.song = song
        self.interactables = interactables
        self.adj_locations = adj_locations
        self.enemyArr = enemyArr
        self.indoors = indoors
        self.hag = hag

    
    #formatted info about the location
    def look(self):

        if(self.enemyArr != []):
            prints("",.3)
            prints(f"The forces of evil close in on you!",.3)
            for i in range(len(self.enemyArr)):
                prints(f"{i+1}. {self.enemyArr[i].name}, {self.enemyArr[i].desc}",.3)
        prints("",.3)
        prints(f"You are in {self.name}",.3)
        prints(self.desc,.3)
        
        prints("",.3)
        prints("The following items and people are here:  ",.3)
        
        for i in range(len(self.interactables)):
            prints(f"{i+1}. {self.interactables[i].name}",.3)
            
        prints("",.3)
        prints("From your current location, you can travel to:",.3)
        for i in range(len(self.adj_locations)):
            prints(f"{i+1}. {self.adj_locations[i].name}",.3)

            
        
     #once we have a player class: def move(self, dest, player)
        
    def move(self, dest, player):
         for i in range(len(self.adj_location)):
             if dest == self.adj_location[i]:
                 player.current_location = self.adj_locations[i]
 
        

