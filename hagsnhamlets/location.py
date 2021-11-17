#!/usr/bin/env python3
from prints import printr
from prints import prints
class Location(object):

    def __init__(self, name, desc, song, interactables, adj_locations):

        self.name = name
        self.desc = desc
        self.song = song
        self.interactables = interactables
        self.adj_locations = adj_locations

    #formatted info about the location
    def look(self):
        prints(f"\nYou are in the {self.name}")
        prints(self.desc)
        
        prints("\nThe following items are here:  ")
        for i in range(len(self.interactables)):
            prints(f"{i+1}. {self.interactables[i].name}")
        
        prints("\nFrom your current location, you can travel to ")
        for i in range(len(self.adj_locations)):
            prints(f"{i+1}. {self.adj_locations[i]}")
        
    #once we have a player class: def move(self, dest, player)
        
    def move(self, dest, player):
        for i in range(len(self.adj_location)):
            if dest == self.adj_location[i]:
                player.current_location = self.adj_locations[i]
