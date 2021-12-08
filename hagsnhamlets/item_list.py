from item import *
import random
from new_container import container

from weapon import weapon 
from weapon_list import *
from food_list import *
from armor_list import *


#QUEST STUFF
drop_of_hope = item("A Drop of Hope", "A wondrous find! The vial glows with a pale yellow hue. This is a Hagsbane potion ingredient.")
deathcap = item("Deathcap Mushroom", "Such a small vessel for such enourmous destructive ability.")
ruby = item("The Hangman's Ruby", "It glimmers with more than just light.")
toadEye = item("Eye of Toad", "A Jar With the eye of a toad inside, it seems to look past you.")
herbs = item("Bitter Herbs", "They never knew what they were supposed to taste like.")
doll = item("Old Doll", "There were children at play here... once.")
noose = item("Hangman's Rope", "Better not to think what this was used for.")
tombStone = item("Unsure Tombstone", "You're never quite sure who's name is engraved on it")
riverGlass = item("River Glass", "Worn smooth by too much time and too much water")

#POTIONS

old_bones_potion = item("Old Bones", "A potion ingredient")
dwarfs_hair = item("Dwarf's Hair", "A potion ingredient")
nasty_herb = item("Nasty Herb", "A potion ingredient.")
tunnel_sludge= item("tunnel Sludge", "A potion ingredient")
fingernail = item("Somebody's fingernail", "A potion ingredient")
old_bark = item("Old Bark", "A potion ingredient.")
empty_flask = item("Empty Flask", "Stores Potions")
heart_potion = item("Heart Potion", "Heals damage on use.")
despising_potion = item("Potion of Despising", "Buffs your damage for a short period of time.")
dumb_luck_elixir = item("Dumb Luck Elixir", "Helps you win the speakeasy games more easily.")
wondrous_bow = item("Wondrous Brew", "This potion will randomly buff one stat permanently.")





#Trinkets

doll = item("Old Doll", "Found in the cottage. While you hold this item, Shadows in the Deep Woods will grant you XP.")
hangmans_rope = item("Hangman's Rope", "Found at the Hangman's Tree. While held, you deal bonus damage to undead creatures.")
rat_pack = item("Rat's Pack", "Dropped by the Rat King. This pack grants the player additional inventory space.")
hags_eye = item("Hag's Eye", "Dropped by any defeated Hag. Staring into it may allow you to glimpse the future. Be warned!")
unsure_tombstone = item("Unsure Tombstone", "This tombstone...It lists all of your previous lives. Would you like to read it?", False)
soul = item("The Soul", "You are finally able to rest.")
last_kernel = item("The Last Kernel", "Traded to you by the farmer. This item grants the holder bonus health.")
dark_cloak = item("Dark Cloak", "Traded to you by the Thief King. The wearer is granted the ability to avoid unwanted encounters.")
broken_watch = item("A Broken Watch", "Tells you when to leave and when to come back to the game. Doing so gives you a bonus to luck.")

#MISC
bottle = item("Bottle","A glass bottle.")
wine_glass = item("Glass", "A simple wine glass.")
silver_fork = item("Silver  Fork", "An eating utensil.")
fine_plate =item("Fine Plate", "A decorative, elegant plate.")
bed = item("Bed", "A comfy looking bed.", False),
bones = item("bones", "An assortment of bones")
tongs = item("Tongs", "A pair fo metal tongs")




#BOOKS

time_book = item("The Test of Time", "The author's name has faded away. Most of the pages are tattered.")
time_book2 = item("If You Could Turn Back Time", "The author of this volume rambles on about time travel for 300 pages.")
easter_egg_book = item("The Art of Game Design: A Book of Lenses, Third Edition.", "An interesting read.")
pamphlet = item("Pamphlet", "A tattered pamphlet that has somehow withstood the test of time.")
book_of_spells = item("The Book of Spells", "Traded to you by the librarian. Casting spells from this book results in a random spell being cast.")

book_list = [time_book, time_book2, easter_egg_book, pamphlet, book_of_spells] 


#FURNITURE

armoire = item("Armoire", "A large, beautiful armoire.", False)
comfy_bed = item("Comfy Bed", "The bed looks so soft and enticing. Were that you were able to sleep!", False)
rug = item("Rug", "A weathered rug", False)
window = item("Window", "Sunlight streams in through the windows here.", False)
mantle = item("Fireplace Mantle", "A mantle with various decorative pieces adorning it.", False)


#DOORS
wooden_door = item("Wooden Door", "A simple wooden door.", False)



newGrave = item("New Tombstone", "It says: \"R.I.P Wolfgang Borchelt.\"", False)
medGrave = item("Old Tombstone", "It says: \"R.I.P Bryan Exley.\"", False)
ancGrave = item("Ancient Tombstone", "It says: \"R.I.P Matthew Krause.\"", False)

stump = item("The Stump", "Given more light, and more time, you might be able to count the rings.", False)

boneShard = item("Bone Shard", "You can feel the hate within.")
hide = item("Wolf Pelt", "No animal in this forest can keep a healthy coat, these hides are proof.")



#ITEMS BY LOCATION 

#Death is mad at the Hag's and will loan you his scythe if X for Y time 
#reapers_scythe = weapon("Reaper's Scythe", 666, 666, "slash", "Death's very own.")

cemetery_item_list = [boneShard, boneShard, boneShard, boneShard, bones, bones, bones]


#Town Items

town_item_list = []


#Old Mine Items

old_mine_item_list = []

#Forest Items
forest_item_list = [] 
#Sewer Items

sewer_item_list = []

#Containers
                    
wooden_box = container("Box", "A wooden box", [])
barrel = container("Wooden Barrel", "A wooden barrel", [])
iron_chest = container("Iron Chest", "A heavy iron chest", [], False)
elaborate_chest = container("Elaborate Chest", "A heavy, ornately designed chest.",  [], False)
weapon_rack = container("Weapon Rack", "A rack for dwarven weaponry, abandoned some time ago.", [])
mine_cart = container("Mine Cart", "A dwarven mining cart.", []),
egg_sac = container("Egg Sac", "A disgusting egg sac", [])
sus_tree = container("Suspicious Tree", "A tree with a large knot in it.",  [])
berry_bush = container("Berry bush", "A bush full of delicious looking berries",  [])
pile_of_refuse = container("Pile of refuse", "A large pile of garbage.",  [])
loose_stone = container("Loose stone", "You spot some loose stones.", [])

all_containers = [wooden_box, barrel, iron_chest, elaborate_chest, weapon_rack, mine_cart, egg_sac, sus_tree, berry_bush, pile_of_refuse, loose_stone]

cemetery_containers = [loose_stone, wooden_box, barrel]

#town containers
town_container = [wooden_box, barrel] 

#old mine containers
old_mine_containers = [wooden_box, barrel, iron_chest, weapon_rack, mine_cart, egg_sac]

#forest container
forest_container = [sus_tree, berry_bush]

#sewer container 
sewer_container = [pile_of_refuse, loose_stone]



def populate_container(what_container_list, item_list, num_items, unlocked = True):
    
    max_container_length = len(what_container_list)
    #print(f"I've chosen {what_container_list}, {item_list}, {num_items}, {unlocked} as my container.")
    #print(f"Max length is {max_container_length}")

    chosen_container_index = random.randint(1, max_container_length)

    chosen_container = what_container_list[chosen_container_index]
    print(f"I've chosen {chosen_container.name}")
    
    new_container = chosen_container
    
    max_item_list_length = len(item_list)
    for i in range(1, num_items):
        rand_item = random.randint(1, max_item_list_length)
        new_container.contents.append(item_list[rand_item])

    return new_container




""" startingChest = populate_container(all_containers, armor_list, 5)

print("The contents of startingChest are:")
for i in range(len(startingChest.contents)):
    print(startingChest.contents[i])
 """

def populate_mixed_container(what_container_list, item_lists, num_items, unlocked = True):
    
    max_container_length = len(what_container_list)
    chosen_container_index = random.randint(0, max_container_length)
    chosen_container = what_container_list[chosen_container_index]
    new_container = chosen_container

    max_items = num_items
    global current_items
    current_items = 0

    def fill_first_round():
        global current_items
        for i in range(len(item_lists)):
            max_list_length = 0 
            max_list_length = len(item_lists[i])
            rand_item = random.randint(0, max_list_length)
            rand_item = item_lists[i][rand_item]
            new_container.contents.append(rand_item)
            current_items +=1
    fill_first_round()
    print(f"Current item count = {current_items}")
    needed_items = max_items - current_items
    print(f"Neeed {needed_items} more items")
    
    def fill_second_round():
        global current_items
        for i in range(0, needed_items):
            max_list_length = 0
            max_list_length = len(item_lists[i])
            rand_item = random.randint(0, max_list_length)
            rand_item = item_lists[i][rand_item]
            new_container.contents.append(rand_item)
            current_items +=1
    
    if current_items < max_items:
        print("Need more items")
        fill_second_round()


    if current_items == max_items:
        print("max items hit")

    return new_container



mixed_container = populate_mixed_container(all_containers, [food_list, armor_list, weapon_list], 5)

food_container = populate_mixed_container(all_containers, [food_list, food_list, weapon_list], 5)

def print_container_contents(container):

    for i in range(len(container.contents)):
        print(container.contents[i])
        

print_container_contents(food_container)



