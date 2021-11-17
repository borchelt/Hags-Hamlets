#!/usr/bin/env python3

class Location:

    def __init__(self, name, desc, song, interactables, adj_locations):

        self.name = name
        self.desc = desc
        self.song = song
        self.interactables = interactables
        self.adj_locations = adj_locations

    def look(self):
        print(f"You are in the {self.name}")
        print(f"The {self.name} looks like:")
        print(self.desc)
        
        print("The following items are here:  ")
        for i in range(len(self.interactables)):
            print(f"{i}. {self.interactables[i]}")
        
        print("From your current location, you can travel to ")
        for i in range(len(self.adj_locations)):
            print(f"{i}. {self.adj_locations}")
        
    #once we have a player class: def move(self, dest, player)
        
    def move(self, dest, player):
        for i in range(len(self.adj_location)):
            if dest == self.adj_location[i]:
                player.current_location = self.adj_location[i]
    
local = Location("Woods", "The Woods are lovely", "song", ["a","b","c"], ["1","2","3"])

what_do_you_do = input("What do you want to do?  ")

if what_do_you_do == "look":
    local.look()
if what_do_you_do == "move":
    dest = input("Where do you want to move?  ")
    local.move(dest)