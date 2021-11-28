#import location
#import player
from prints import printr
from prints import prints
import console
#from dialogue import * 
#from item import item
from ascii_art import *
#import weapon
import pandas as pd

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
        "HP": [0],
        "AP": [0],
        "ATK": [0],
        "MAG": [0],
        "DEX": [0],

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
        "Quest Item": [ f"True", f"  .  ", f"  .  ", f"  .  ",]
        }

    char_inv_table = pd.DataFrame(char_inv_table_data, index = ["ITEM 1", "ITEM 2", "ITEM 3", "AND SO ON..."])
    """ for i in range(len(char_inv_table.index())):
        char_inv_table.index[i].append(f"{i}. {char_inv_table.index[i]}")
    """
    print(char_inv_table)

art()
character_pd()






