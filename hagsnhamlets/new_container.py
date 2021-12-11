from prints import *
from weapon import weapon
class container():
    
    def __init__(self, name, desc, contents = [], unlocked = True):

        self.name = name
        self.desc = desc
        self.contents = contents
        self.unlocked = unlocked
    
    def open(self, player):
        if len(self.contents) == 0:
            prints("It's Empty")

        prints(f"You shuffle around the {self.name}. Inside, you find the following items")
        for i in range(len(self.contents)):
            prints(f"{i+1}. {self.contents[i].name}")
        prints(f"{len(self.contents)+1}. Store items in this container")
        quitB = False

        while not quitB:
            num = input(printr("enter the appropriate number to select an item, or enter \"q\" to quit: "))

            if num == "q" or "quit" in num:
                prints(f"You look up the {self.name}")
                break

            try:
                add = int(num)
                
                if(add-1 == len(self.contents)):
                    add += 999
                    for i in range(len(player.inventory)):
                        prints(f"{i+1}. {player.inventory[i].name}")
                    prints("which item do you want to store here?")
                    inp = input(printr("enter the appropriate number to select an item, or enter \"q\" to quit: ")).lower()

                    if inp =="q" or "quit" in inp:
                        for i in range(len(self.contents)):
                            prints(f"{i+1}. {self.contents[i].name}")
                        prints(f"{len(self.contents)+1}. Store items in this container")
                        break

                    try:
                        index = int(inp)
                        if(index-1 < len(player.inventory)):
                            prints("--------------")
                            prints(f"\033[1m{player.inventory[index-1].name}\033[0m")
                            prints("~~~~~~~~~~~~~~")
                            prints(f"\x1B[3m{player.inventory[index-1].desc}\x1B[0m")
                            prints("~~~~~~~~~~~~~~")
                            prints("--------------")
                            quitC = False
                            while(not quitC):
                                num = input(printr("Do you want to store this item? Y/N: ")).lower()

                                if num == "y" or "yes" in num:
                                    self.contents.append(player.inventory[index-1])
                                    player.inventory.remove(player.inventory[index-1])
                                    if len(self.contents) == 0:
                                        prints("It's Empty")
                                    for i in range(len(self.contents)):
                                        prints(f"{i+1}. {self.contents[i].name}")
                                    prints(f"{len(self.contents)+1}. Store items in this container")
                                    break
                                   
                                elif num == "n" or "no" in num:
                                    if len(self.contents) == 0:
                                        prints("It's Empty")
                                    for i in range(len(self.contents)):
                                        prints(f"{i+1}. {self.contents[i].name}")
                                    prints(f"{len(self.contents)+1}. Store items in this container")
                                    break

                                    


                    
                    except ValueError:
                        continue
                

                if(add-1 < len(self.contents)):
                    prints("--------------")
                    prints(f"\033[1m{self.contents[add-1].name}\033[0m")
                    prints("~~~~~~~~~~~~~~")
                    prints(f"\x1B[3m{self.contents[add-1].desc}\x1B[0m")
                    prints("~~~~~~~~~~~~~~")
                    prints("--------------")
                    quitC = False
                    while(not quitC):
                        num = input(printr("what will you do with this? ")).lower()
                        
                        if "q" in num.lower()[0] or "quit" in num:
                            for i in range(len(self.contents)):
                                prints(f"{i+1}. {self.contents[i].name}")
                            break
                        if("take" in num or num == "t"):
                            player.inventory.append(self.contents[add-1])
                            prints(f"You got the {self.contents[add-1].name}")
                            self.contents.remove(self.contents[add-1])


                            if len(self.contents) == 0:
                                prints("It's Empty")
                            for i in range(len(self.contents)):
                                prints(f"{i+1}. {self.contents[i].name}")
                            break

                        if "equip" in num or num == "e":
                            
                            if len(player.equipped) >= 2:
                                if type(self.contents[add-1]) == weapon.weapon:
                                    prints(f"1. {player.equipped[0].name}")
                                    prints(f"2. {player.equipped[1].name}")
                                    acc = int(input(printr("Which item do you want to unequip first? ")))-1
                                    self.contents.append(player.equipped[acc])
                                    player.equipped[acc] = self.contents[add-1]
                                    self.contents.remove(player.equipped[acc])
                                    prints("equipped!")
                                    for i in range(len(self.contents)):
                                        prints(f"{i+1}. {self.contents[i].name}")
                                    quitC = True

                            else:
                                if type(self.contents[add-1]) == weapon.weapon:
                                    player.equipped.append(self.contents[add-1])
                                    self.contents.remove(self.contents[add-1])
                                    prints("equipped!")
                                    for i in range(len(self.contents)):
                                        prints(f"{i+1}. {self.contents[i].name}")
                                    quitC = True
            except ValueError:
                continue
    


    
