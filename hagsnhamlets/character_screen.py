#import location
#import player
from prints import printr
from prints import prints
from player import Player
from console import * 
#from dialogue import * 
#from item import item
from ascii_art import *
#import weapon
import pandas as pd
from hags_and_hamlets import player1



def art():
    prints("—#|||#|||#|||#|||#|||#|||#|||#|||#|||#|||#|||#|||#|||#|||#|||#|||#—")
    prints("",.3)

    character_screen_ascii()

    prints("",.3)
    prints("—#|||#|||#|||#|||#|||#|||#|||#|||#|||#|||#|||#|||#|||#|||#|||#|||#—")
    prints("",.3)

    sword_ascii()

def character_pd():
    prints("", .3)
    prints("    ### CHARACTER STATS ###     ")
    prints("",.3)

    char_stats_data = {
        "HP": [player1.hp],
        "AC": [player1.ac],
        "MAG": [player1.mag],
        "DEX": [player1.dex],
        "STR": [player1.str],

    }
    char_stats_table = pd.DataFrame(char_stats_data, index = ['STATS:   '])

    print(char_stats_table)


    prints("",.3)
    prints("    #### YOU RIFLE THROUGH YOUR BACKPACK ###    ")
    prints("",.3)
        
    char_inv_table_data = {
        "Value (GP)": [     5,         10,      15,      20   ],
        "AP": [ f"+{0}", f"+{0}", f"+{0}", f"+{0}"],
        "ATK":[ f"+{0}", f"+{0}", f"+{0}", f"+{0}"],
        "MAG": [ f"+{0}", f"+{0}", f"+{0}", f"+{0}"],
        "DEX":[ f"+{0}", f"+{0}", f"+{0}", f"+{0}"],
        #"Quest Item": [ f"True", f"  .  ", f"  .  ", f"  .  ",]
        }

    char_inv_table = pd.DataFrame(char_inv_table_data, index = [])
    for i in range(len(player1.inventory)):
        char_inv_table.index.append(player1.inventory[i])
    


    """ for i in range(len(char_inv_table.index())):
        char_inv_table.index[i].append(f"{i}. {char_inv_table.index[i]}")
    """
    print(char_inv_table)

art()
character_pd()






