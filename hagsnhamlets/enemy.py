#!/usr/bin/env python3
#from hags_and_hamlets.ascii_art import goblin_ascii, skeleton
from prints import *
from random import *
from math import floor
from ascii_art import * 
class enemy():
    def __init__(self,name, desc, hp, weapons, ac, drops, death, local):
        self.name = name
        self.desc = desc
        self.hp = hp
        self.weapon = weapons
        self.ac = ac
        self.drops = drops 
        self.death = death
        self.local = local

    
    def hit(self, aPack, drop = True):
        roll = aPack[0]
        damage = aPack[1]
        if roll > self.ac:
            prints(f"It connects! You deal {damage} damage")
            self.hp -= damage
        else:
            prints("You miss!")
        if self.hp <= 0:
            if(drop):
                prints(self.death)
                for i in self.drops:
                    self.local.interactables.append(i)
                    prints(f"It drops a {i.name}!")
                self.local.enemyArr.remove(self)


    def attack(self, player):
        prints(f"The {self.name} {self.weapon[0].type} at you with it's {self.weapon[0].name}")
        player.hit([floor(randrange(1, 20) + self.weapon[0].toHit), floor(randrange(1, 6) + self.weapon[0].dmg)])

    def attack2(self, player):
        prints(f"The {self.name} {self.weapon[1].type} at you with it's {self.weapon[1].name}")
        player.hit([floor(randrange(1, 20) + self.weapon[1].toHit), floor(randrange(1, 6) + self.weapon[1].dmg)])

    def attack3(self, player):
        prints(f"The {self.name} {self.weapon[2].type} at you with it's {self.weapon[2].name}")
        player.hit([floor(randrange(1, 20) + self.weapon[2].toHit), floor(randrange(1, 6) + self.weapon[2].dmg)])

