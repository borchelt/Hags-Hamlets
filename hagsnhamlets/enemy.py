#!/usr/bin/env python3
from prints import *
from random import *
from math import floor, trunc

hags = 0
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
        self.gold = hp*randint(1, 3)
    
    
    def hit(self, aPack, player, drop = True):
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
                player.gold += self.gold
                for i in self.drops:
                    self.local.interactables.append(i)
                    prints(f"It drops a {i.name}!")
                prints("You feel your coin purse grow a bit heavier")
                self.local.enemyArr.remove(self)


    def attack(self, player):
        prints(f"The {self.name} {self.weapon[0].type} at you with it's {self.weapon[0].name}")
        player.hit([randrange(1, 21) + self.weapon[0].toHit,randrange(1, 7) + self.weapon[0].dmg], "")

    def attack2(self, player):
        prints(f"The {self.name} {self.weapon[1].type} at you with it's {self.weapon[1].name}")
        player.hit([randrange(1, 21) + self.weapon[1].toHit, randrange(1, 7) + self.weapon[1].dmg], "")

    def attack3(self, player):
        prints(f"The {self.name} {self.weapon[2].type} at you with it's {self.weapon[2].name}")
        player.hit([randrange(1, 21) + self.weapon[2].toHit, randrange(1, 7) + self.weapon[2].dmg], "")

class hag(enemy):

    def __init__(self, name, desc, hp, weapons, ac, drops, death, local):
        super().__init__(name, desc, hp, weapons, ac, drops, death, local)


    def hit(self, aPack, drop=True):
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
                    prints(f"She drops a {i.name}!")
                self.local.hag = True
                self.local.enemyArr.remove(self)
    
    def attack(self, player):
        prints(f"{self.name} {self.weapon[0].type} at you with her {self.weapon[0].name}")
        player.hit([randrange(1, 21) + self.weapon[0].toHit,randrange(1, 7) + self.weapon[0].dmg], "")

    def attack2(self, player):
        prints(f"{self.name} {self.weapon[1].type} at you with her {self.weapon[1].name}")
        player.hit([randrange(1, 21) + self.weapon[1].toHit, randrange(1, 7) + self.weapon[1].dmg], "")

    def attack3(self, player):
        prints(f"{self.name} {self.weapon[2].type} at you with her {self.weapon[2].name}")
        player.hit([randrange(1, 21) + self.weapon[2].toHit, randrange(1, 7) + self.weapon[2].dmg], "")

class hag4(hag):

    def __init__(self, name, desc, hp, weapons, ac, drops, death, local):
        super().__init__(name, desc, hp, weapons, ac, drops, death, local)
    
    def hit(self, aPack, drop=True):
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
                    prints(f"She drops a {i.name}!")
                self.local.hag = True
                self.local.enemyArr.remove(self)

                prints("The winds pick up, spinning at incredible speeds. A tornado forms, reaching a long tendril down towards Mefilda, who screams.", 2)
                prints("Try as she might, she cannot escape. With a terrible cry, she is lifted from the ground and swallowed by the sky.", 2)
                prints("Shortly thereafter, the sky clears and villagers begin spilling out from their hiding places. Most stare in stunned silence,", 2)
                prints("until a few begin to cheer. It is said that many miles away, in neighboring villages, folks could hear the triumphant", 2)
                prints("cries of the Hamlet. They chant your name, sing your praises, and hold a feast in your honor. You have saved the Hamlet,", 2)
                prints("and perhaps the world, as it were. For years to come, your name will exist as legend. For the present,", 2)
                prints("                                  -----##### YOU ARE A HERO #####----", 2)

                    
                prints("                    _______               _______  _______  _______   ")
                prints("          |\     /|(  ___  )|\     /|    (  ___  )(  ____ )(  ____ \" ")
                prints("          ( \   / )| (   ) || )   ( |    | (   ) || (    )|| (    \/  ")
                prints("          \ (_) / | |   | || |   | |    | (___) || (____)|| (__       ")
                prints("           \   /  | |   | || |   | |    |  ___  ||     __)|  __)      ")
                prints("            ) (   | |   | || |   | |    | (   ) || (\ (   | (         ")
                prints("            | |   | (___) || (___) |    | )   ( || ) \ \__| (____/\"  ")
                prints("            \_/   (_______)(_______)    |/     \||/   \__/(_______/   ")
                prints("                                                                      ")
                prints("              _______                 _______  _______  _______       ")
                prints("             (  ___  )      |\     /|(  ____ \(  ____ )(  ___  )      ")
                prints("             | (   ) |      | )   ( || (    \/| (    )|| (   ) |      ")
                prints("             | (___) |      | (___) || (__    | (____)|| |   | |      ")
                prints("             |  ___  |      |  ___  ||  __)   |     __)| |   | |      ")
                prints("             | (   ) |      | (   ) || (      | (\ (   | |   | |      ")
                prints("             | )   ( |      | )   ( || (____/\| ) \ \__| (___) |      ")
                prints("             |/     \|      |/     \|(_______/|/   \__/(_______)      ")
                cont = input(printr("You have won. There is nothing more for you do do here. Tress anything to continue", 3))
                exit()


