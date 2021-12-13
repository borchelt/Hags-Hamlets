from time import strptime
from location import Location
from item import *
from item import consumable
from dialogue import *
from tutorial import * 
from npcs import *
from intro import *
from ascii_art import * 
import enemy
from weapon import weapon
import random 
import copy

from item_list import *




class map():

    def populate_enemies(max_enemies, where, who):
        
        for i in range(0, max_enemies):
            enemy_chance = random.randint(0,10)
            if enemy_chance % 2 == 0:
                enemy = copy.deepcopy(who)
                enemy.local = where
                where.enemyArr.append(enemy)



    
    cemetery = Location("The Graveyard", "A cold and unfeeling feild of stone.", "hnh_forestTheme_conceptQ.mp3",[], [], [])
    outskirts = Location("The Outskirts", "Rollng hills of what might once have been grass", "hnh_forestTheme_conceptQ.mp3", [], [], [])
    gates = Location("The Old Gate", "The two humaniod statues tower above any tree in the forest, they seem to watch as you as you pass by."
                    ,"hnh_forestTheme_conceptQ.mp3", [],[],[])
    tree = Location("The Hangman's Tree", "A solitary tree stands in defiance of the both the feilds and the woods.", [],[],[])

    clearing = Location("The Clearing", "a small pocket of open air, constantly assulted by the opressive weight of the forest surrounding it."
                    ,"hnh_forestTheme_conceptQ.mp3", [],[],[])
    woodsN = Location("The Northern Woods", "They are dark, and run deep.", "hnh_forestTheme_conceptQ.mp3", [], [], [])
    woodsNW = Location("The Northwestern Woods", "They are dark, and run deep.", "hnh_forestTheme_conceptQ.mp3", [], [], [])
    woodsS = Location("The Southern Woods", "They are dark, and run deep.", "hnh_forestTheme_conceptQ.mp3", [], [], [])
    woodsSE = Location("The Southeastern Woods", "They are dark, and run deep.", "hnh_forestTheme_conceptQ.mp3", [], [], [])
    woodsSW = Location("The Southwestern Woods", "They are dark, and run deep.", "hnh_forestTheme_conceptQ.mp3", [], [], [])
    woodsDeadN = Location("The Northeastern Woods", "A dead end, the trees grow too dense and the shadows too dark.", "hnh_forestTheme_conceptQ.mp3", [], [], [])
    woodsDeadS = Location("The Southeastern-er Woods", "A dead end, the trees grow too dense and the shadows too dark.", "hnh_forestTheme_conceptQ.mp3", [], [], [])
    waterfall1 = Location("The Waterfall", "Murky water cascades over the falls and into the pool below. You stop for a moment, taking in the view, when you think you see a flash of light from behind the falls.", "hnh_forestTheme_conceptQ.mp3", [],[],[])
    dampCave = Location("The Cove", "The deafening roar of the waterfall falls surprisingly quiet beyond the veil of foam and murk", "hnh_forestTheme_conceptQ.mp3", [], [],[], True)
    path = Location("The Twisted Path", "A small, twisting path beckons you deeper into the woods.","hnh_forestTheme_conceptQ.mp3", [], [],[])
    camp = Location("The Hunter's Camp", "Whatever fire was once here has long since died out. A raggedy tent is haphazardly nested between two large daggerlike stones. ","hnh_forestTheme_conceptQ.mp3", [], [],[])

    forest = Location("The Forest", "The Hamlet eventually gives way to the forest, the trees press close, and the fog closer.","hnh_forestTheme_conceptQ.mp3", [], [],[])
    cottage = Location("The Old Cottage", "a small stream cuts directly through the sagging cottage, you swear you can hear faint music from inside.", "hnh_forestTheme_conceptQ.mp3", [], [],[])
    farm = Location("The Barn", "a faded barn stands amidst the trees","hnh_forestTheme_conceptQ.mp3", [], [],[])
    glade = Location("The Glade", "perhaps the only truly beautiful place left, you swear you can just barely see the sun up there", "hnh_forestTheme_conceptQ.mp3", [],[],[])


    #cottage.enemyArr[hag1]
    
     #OLD MINES
    old_mines_entrance = Location("Old Mines: Entrance", "Once a great mine, the resources have been mostly used up. The dwarven miners that still work here must fight to keep it clear of enemies in the absence of more capable fighters.","hnh_forestTheme_conceptQ.mp3", [],[],[], True)
    old_mines_main_chamber = Location("Old Mines: First Chamber", "The Old Mine is dimly lit by torches. Several groups of dwarves are huddled. Some are tending to wounds, others eating lunch.","hnh_forestTheme_conceptQ.mp3", [],[],[], True)
    old_mines_floor1_NW = Location("Old Mines room 1", "A dimly lit corridor. Various scraps of metal and other tools litter the area. Someone left in a hurry.","hnh_forestTheme_conceptQ.mp3", [],[],[], True)
    old_mines_floor1_N = Location("Old Mines room 2", "An old mine cart lay here, toppled on its side.","hnh_forestTheme_conceptQ.mp3", [],[],[], True)
    old_mines_floor1_NE = Location ("Old Mines room 3", "Following the tracks, you see that the corridor ahead leads deeper into the mines.","hnh_forestTheme_conceptQ.mp3", [], [], [], True)
    old_mines_floor2 = Location("Old Mines room 4", "Before you is a great Iron door. Bloody handprints have left rusty colored marks on the wood. The bar blocking the door has been bent from the force of something large hitting it.","hnh_forestTheme_conceptQ.mp3", [], [], [], True)
    old_mines_floor2_W = Location("Old Mines room 5", "The dwarves have warned you that the path ahead would not be easy. The way forward requires that you pass through an impressive number of cobwebs.","hnh_forestTheme_conceptQ.mp3", [],[],[], True)
    old_mines_floor2_W2 = Location("Old Mines: Supply Cache", "A small chamber dedicated to storing supplies.","hnh_forestTheme_conceptQ.mp3", [], [], [],True)
    old_mines_center_chamber = Location("Old Mines: Center Chamber", "A large chamber with a statue of the famous dwarf, Mozal Mon. A locked chest rests at the Statue's feet.","hnh_forestTheme_conceptQ.mp3", [],[],[], True)
    old_mines_floor2_W3 = Location("Old Mines room 6", "The enormous webs grow thicker here.", [],[],[],True)
    old_mines_floor2_wN = Location("Old Mines: The Forge", "This forge hasn't been operational for some time. There are bones and webs everywhere.","hnh_forestTheme_conceptQ.mp3", [],[],[],True)
    old_mines_floor2_wN2 = Location("Old Mines: The Armory", "This place was surely wondrous some time ago. Now various weapons and armor lay discarded on the stone, forgotten or abandoned by dwarves desparate to escape.","hnh_forestTheme_conceptQ.mp3", [],[],[],True)
    old_mines_floor2_wN2_W = Location("Old Mines: Webbed Path", "You're not sure you should be here. The entirety of the corridor is covered with webs. The decaying husks of the spiders' victims hang from the ceiling.", [],[],[],True)
    old_mines_floor2_wN2_W2 = Location("Old Mines room 7", "The webs are next to impassable here, but just ahead you can a clearer space.","hnh_forestTheme_conceptQ.mp3",[], [], [],True)
    old_mines_spider_lair = Location("Spiders' Lair", "A large cavern littered with bodies, bones and webs. Hundreds of spider eggs cling to the floor, walls and ceiling of the cavern.","hnh_forestTheme_conceptQ.mp3", [],[],[],True)
    
    #OLD MINES FLOOR 1 DIRECTIONAL 
    old_mines_entrance.adj_locations = [old_mines_main_chamber, woodsN]
    old_mines_main_chamber.adj_locations = [old_mines_floor1_NW, old_mines_floor1_N, old_mines_floor1_NE]
    old_mines_floor1_NW.adj_locations = [old_mines_main_chamber, old_mines_floor1_N] 
    old_mines_floor1_N.adj_locations = [old_mines_main_chamber, old_mines_floor1_NE, old_mines_floor1_NE]
    old_mines_floor1_NE.adj_locations = [old_mines_main_chamber, old_mines_floor1_N, old_mines_floor2]

    #OLD MINES FLOOR 2 DIRECTIONAL 
    old_mines_floor2.adj_locations = [old_mines_floor1_NE, old_mines_floor2_W]
    old_mines_floor2_W.adj_locations = [old_mines_floor2, old_mines_floor2_W2, old_mines_floor2_wN]
    old_mines_floor2_W2.adj_locations = [old_mines_floor2_W3, old_mines_floor2_W, old_mines_center_chamber]
    old_mines_center_chamber.adj_locations = [old_mines_floor2_W2]
    old_mines_floor2_W3.adj_locations = [old_mines_spider_lair]
    old_mines_floor2_wN.adj_locations = [old_mines_floor2_W, old_mines_floor2_wN2]
    old_mines_floor2_wN2.adj_locations = [old_mines_floor2_wN, old_mines_floor2_wN2_W]
    old_mines_floor2_wN2_W.adj_locations = [old_mines_floor2_wN2, old_mines_floor2_wN2_W2]
    old_mines_floor2_wN2_W2.adj_locations = [old_mines_spider_lair]
    old_mines_spider_lair.adj_locations = [old_mines_floor2_wN2_W2, old_mines_floor2_W2]
    
    #OLD MINES ENEMIES 
    bite = weapon("Teeth", 3, 1, "bites")
    bat = enemy.enemy("Bats","A swarm of bats clouds your vision. The sound is incredible as wings fly past your face and around your head.", 1, 
                        [bite, bite, bite], 10, [item("bat's wings", "A severed bat's wing")], "Your attack connects and the bats fall harshly, splattering on the ground.", old_mines_floor1_N)
    hatchling_spider = enemy.enemy("Spider Hatchling", "While this spider is not as big as it will eventually be, it is much larger than you are comfortable being close to.", 3, [bite, bite, bite], 5, [], "", old_mines_floor2_W)
    giant_spider = enemy.enemy("Giant Spider","A hulking, fierce insect. This is no time to be act idley. Look out!", 15, 
                        [bite, bite, bite], 10, [item("venomous sac", "A foul smelling sac that you've retrieved from the spider. Probably worth keeping for a potion."), item("spider eyes", "The soft, gushy eyeballs of the spider stare back at you lifelessly."), item("giant spider mandible", "A spider's mandible."), item("An Ornate Key", "Amazing that the spider didn't digest this. You wonder what lock it might fit.")], "The spider crumples into a bent, twisted shape as it hugs its wounds. It dies, shortly after", old_mines_spider_lair)
    
    #OLD MINES ENEMY POPULATION 

    old_mines_floor1_NW.enemyArr = [bat]
    old_mines_floor1_N.enemyArr = [bat]
    old_mines_floor1_NE.enemyArr = [bat]

    old_mines_floor2_W.enemyArr = [hatchling_spider]
    old_mines_floor2_W2.enemyArr = [hatchling_spider,hatchling_spider]
    old_mines_floor2_wN.enemyArr = [hatchling_spider, hatchling_spider]
    old_mines_center_chamber.enemyArr = [hatchling_spider, hatchling_spider, bat]
    old_mines_floor2_wN2.enemyArr = [hatchling_spider, hatchling_spider]
    old_mines_floor2_wN2_W.enemyArr = [hatchling_spider]
    old_mines_floor2_wN2_W2.enemyArr = [hatchling_spider, hatchling_spider]
    old_mines_spider_lair.enemyArr = [giant_spider]

    old_mines_entrance.interactables = [dwarven_miner]
    old_mines_floor1_N.interactables = [small_health_chest]
    old_mines_floor1_NE.interactables = []
    old_mines_floor1_NW.interactables = []
    old_mines_floor2.interactables = [small_armor_chest]
    old_mines_floor2_W.interactables = []
    old_mines_floor2_W2.interactables = [medium_armor_chest, large_weapon_chest]

    #SILVER ORE NEEDS TO GO HERE 
    silOre = item("Silver Ore", "it glitters with potential")
    old_mines_center_chamber.interactables = [large_health_chest,silOre]
    old_mines_floor2_W3.interactables = []
    old_mines_floor2_wN.interactables = []
    old_mines_floor2_wN2.interactables = [small_health_chest]
    old_mines_floor2_wN2_W.interactables = []
    old_mines_floor2_wN2_W2.interactables = [small_health_chest]
    old_mines_spider_lair.interactables = [large_health_chest]
    
    

    deepwoods_mid = Location("The Deepwoods", "The shadows creep in and the trees loom over you", "deepwoods.mp3", [], [], [])
    deepwoods_branch_1 = Location("The Northern(?) Deepwoods", "The shadows creep in and the trees loom over you", "deepwoods.mp3", [], [], [])
    deepwoods_branch_2 = Location("The Southern(?) Deepwoods", "The shadows creep in and the trees loom over you", "deepwoods.mp3", [], [], [])
    deepwoods_branch_3 = Location("The Western(?) Deepwoods", "The shadows creep in and the trees loom over you", "deepwoods.mp3", [], [], [])
    deepwoods_branch_4 = Location("The Western(?) Deepwoods", "The shadows creep in and the trees loom over you", "deepwoods.mp3", [], [], [])
    deepwoods_HagLair = Location("The Core of the Deepwoods", "This is deeper than you've ever been before. you can barely see your hand infront of your face.", [],[],[])

    

    dwList = [deepwoods_mid, deepwoods_branch_1, deepwoods_branch_2, deepwoods_branch_3,deepwoods_branch_4, woodsDeadN]

    shadowyGrasp = weapon("Shadowy Grasp", 5, 5, "claws")
    scream = weapon("Wretched Scream", 10, -3, "howls")
    stare = weapon("Empty Stare", -3, 10, "looks")
    shade = enemy.enemy("Shade", "a formless thing of hate and rage, it shimmers as if underwater", 15, [shadowyGrasp, scream, stare], 16,[], "It hisses like a forged sword in oil as it evaporates before you", deepwoods_mid)
    #CURRENTLY NOT IN USE 
    """ 
    
    populate_enemies(1, old_mines_floor1_NW, bat)
    populate_enemies(2, old_mines_floor1_N, bat)
    populate_enemies(2, old_mines_floor1_NE, bat)
    #door room has no enemies
    populate_enemies(3, old_mines_floor2_W, giant_spider) """

    hamlet = Location("The Hamlet", "The center of this once bustling hamlet now lies quiet and defeated", "hnh_forestTheme_conceptQ.mp3", [], [],[])
    store = Location("The General Store", "A dusty counter sits at the back of this one room shop, the only other furnature being a small shelf laden with baubles","hnh_forestTheme_conceptQ.mp3", [], [],[],True)
    sundial = Location("The Sundial", "A stone slab marked with anchient runes sits inbetween two small houses, nobody but you seems to even relize its there.","hnh_forestTheme_conceptQ.mp3", [], [],[])
    tavern = Location("The Tavern", "Perhaps the only place in the hamlet with any life still inside, you even hear the occasional chuckle coming from inside","hnh_forestTheme_conceptQ.mp3", [], [],[],True)
    QBoard = Location("The Message Board", "A Wooden board with a few slips of parchment halfheartedly nailed to it.","hnh_forestTheme_conceptQ.mp3", [], [],[])
    blacksmith = Location("The Smithy", "the soft glow of the embers and the rythmic ringing of the hammer on metal is almost soothing.","hnh_forestTheme_conceptQ.mp3", [], [],[],True)
    library = Location("The Library","Most of the books have been overrun by mold, but you may still be able to find something usefull","hnh_forestTheme_conceptQ.mp3", [], [],[],True)
    wagon = Location("The Merchant Wagon", "The small covered wagon smells of incense and dust.","hnh_forestTheme_conceptQ.mp3", [], [],[],True)
    well = Location("The Well", "you cant see the bottom of the well, but for some reason, you can hear running water below.","hnh_forestTheme_conceptQ.mp3", [], [],[],True)

    hamlet.adj_locations = [store, tavern, blacksmith, library, wagon, well, forest]
    hamlet.interactables = [small_weapon_chest, large_health_chest, townGreg]

    store.adj_locations = [hamlet]
    store.interactables = [general_store_owner]

    sundial.adj_locations = [store, tavern, QBoard, blacksmith, library, wagon, well]
    sundial.interactables = []

    tavern.adj_locations = [hamlet, forest]
    tavern.interactables = [innkeeper, small_health_chest, beer, beer, beer, chicken, beef, plate, plate, silver_fork, wine, wine_glass]

    QBoard.adj_locations = [store, tavern, sundial, blacksmith, library, wagon, well, forest]
    QBoard.interactables = []

    library.adj_locations = [hamlet]
    library.interactables = [librarian, small_health_chest, pamphlet, glass, ]

    wagon.adj_locations = [store, tavern, sundial, blacksmith, library, QBoard, well,]
    wagon.interactables = [merchant]

   

     #SEWERS 
    sewers = Location("Sewer Entrance", "It definitely smells like a sewer. With some effort, you would be able to move the cover and enter. It seems dark.", "", [],[],[])
    sewer_tunnels = Location("Sewer Tunnels", "A disgusting smell assaults your senses every second that you spend here.", "", [],[],[],True)
    sewer_tunnelsN = Location("North Sewer Tunnels", "The path widens. This looks like a maintenance tunnel.", "", [],[],[],True)
    sewer_tunnelsE = Location("East Sewer Tunnels", "The path opens into a large room. There are two doors here. "", You can hear the sounds of clinking glasses. One door is guarded by a large, hooded man.", [],[],[],True)
    sewer_tunnelsW = Location("West Sewer Tunnels", "Faint chittering sounds echo down the tunnel towards you.", "", [],[],[],True)
    
    well.adj_locations = [hamlet, sewers]
    well.interactables = [small_health_chest, small_weapon_chest]

    sewer_tunnels.enemyArr = []
    sewer_tunnelsN.enemyArr = []
    sewer_tunnelsE.enemyArr = []
    sewer_tunnelsW.enemyArr = []

    sewer_tunnels.interactables = [bottle, bottle,]
    sewer_tunnelsN.interactables = [bottle, throwing_knife]
    sewer_tunnelsE.interactables = [small_armor_chest] 
    sewer_tunnelsW.interactables = [small_health_chest]


    speakeasy = Location("The Speakeasy", "A place for seedier types to relax and try to forget about the Hags' Curse.", "placeholder", [],[],[], True)
    speakeasy.interactables = [drunkard, beer, beer, beer, beer, wine, plate, small_weapon_chest, bottle]

    thieves_den = Location("Thieves' Den", "This place is well hidden beneath the Hamlet. It seems odd that such a remote space in the world would be home to such a place.", "placeholder", [],[],[],True)
    thieves_den.interactables = [thief_king, drunkard]

    rat_kings_nest = Location("The Rat King's Nest", "This place is a mess of trinkets, weapons, armor and scraps of paper. You're not sure which smells worse- the sewers or the nest.", "placeholder", [],[],[], True)
    rat_kings_nest.interactables = [rat_king]
    
    sewers.adj_locations = [sewer_tunnels]
    sewer_tunnels.adj_locations = [sewers, sewer_tunnelsN, sewer_tunnelsW]
    sewer_tunnelsN.adj_locations = [sewer_tunnels, sewer_tunnelsE]
    sewer_tunnelsE.adj_locations =[sewer_tunnelsN, speakeasy, thieves_den]
    sewer_tunnelsW.adj_locations = [sewer_tunnels, rat_kings_nest]
    thieves_den.adj_locations = [sewer_tunnelsE]
    speakeasy.adj_locations = [sewer_tunnelsE]
    

    cemetery.adj_locations = [outskirts]
    outskirts.adj_locations = [cemetery, gates, tree]
    tree.adj_locations = [outskirts]
    gates.adj_locations = [clearing, outskirts]
    clearing.adj_locations = [gates, woodsN, woodsS, path]
    woodsN.adj_locations = [woodsNW, clearing, woodsDeadN, old_mines_entrance] #old mines once they start
    woodsNW.adj_locations = [woodsN, path]
    woodsDeadN.adj_locations = [woodsN, deepwoods_mid]
    woodsS.adj_locations = [woodsSE, woodsSW, clearing]
    woodsSW.adj_locations = [path, woodsSE, woodsS, waterfall1]
    woodsSE.adj_locations = [woodsSW, woodsS, woodsDeadS]
    woodsDeadS.adj_locations = [woodsSE]
    waterfall1.adj_locations = [woodsSW]
    dampCave.adj_locations = [waterfall1]
    path.adj_locations = [woodsSW, woodsNW, clearing, forest, camp]
    camp.adj_locations = [path]

    forest.adj_locations = [path, farm, cottage, hamlet] #town when its done
    farm.adj_locations = [forest]
    cottage.adj_locations = [forest, glade]
    glade.adj_locations = [cottage]

    deathcap = item("Deathcap Mushroom", "Such a small vessel for such enourmous destructive ability.")
    ruby = item("The Hangman's Ruby", "It glimmers with more than just light.")
    toadEye = item("Eye of Toad", "A Jar With the eye of a toad inside, it seems to look past you.")
    herbs = item("Bitter Herbs", "They never knew what they were supposed to taste like.")
    doll = item("Old Doll", "There were children at play here... once.")
    noose = item("Hangman's Rope", "Better not to think what this was used for.")
    tombStone = item("Unsure Tombstone", "You're never quite sure who's name is engraved on it")
    riverGlass = item("River Glass", "Worn smooth by too much time and too much water")
    telePotion = consumable("Strange Potion", "it has a bluish, milky glow about it", ["tp", hamlet])
    hpPotion = consumable("Red Potion", "It glitters like a ruby in the sun, you hope it tastes that way as well.", ["hp", 5])
    dexPotion = consumable("White Potion", "Despite it's apperance, it smells of coffee.", ["dex", 10])
    strPotion = consumable("Black Potion", "A tar-like sludge, it seems to cling to the glass in an unnerving way", ["str", 5])

    oldSpear = weapon("Old Spear", 0, 1, "stab", "It's seen better days")
    oldSword = weapon("Old Sword", 1, 0, "slash", "It's seen better days")
    oldHammer = weapon("Old Hammer", 2, -1, "swing", "It's seen better days")

    newGrave = item("New Tombstone", "It says: \"R.I.P Wolfgang Borchelt.\"", False)
    medGrave = item("Old Tombstone", "It says: \"R.I.P Bryan Exley.\"", False)
    ancGrave = item("Ancient Tombstone", "It says: \"R.I.P Matthew Krause.\"", False)

    stump = item("The Stump", "Given more light, and more time, you might be able to count the rings.", False)

    boneShard = item("Bone Shard", "You can feel the hate within.")
    hide = item("Wolf Pelt", "No animal in this forest can keep a healthy coat, these hides are proof.")



    #cemetery_box = populate_container(cemetery_containers, cemetery_item_list, 5)

    #cemetery.interactables = [newGrave, medGrave, ancGrave, greg, smith, cemetery_box]
    
    
    cemetery.interactables = [newGrave, medGrave, ancGrave, greg, smith, small_health_chest, small_weapon_chest, small_armor_chest, telePotion, dexPotion, strPotion, hpPotion] 

    
    outskirts.interactables = [oldSpear, tombStone, small_health_chest]
    tree.interactables = [ruby, noose, small_health_chest]
    woodsN.interactables = [herbs]
    woodsDeadN.interactables = [stump, oldHammer]
    woodsSE.interactables = [herbs]
    woodsNW.interactables = [deathcap]
    woodsDeadS.interactables = [oldSword]
    waterfall.interactables = [riverGlass]
    gates.interactables = [guard, small_health_chest]

    claw = weapon("Claws", 1, 4, "swipes")
    bite = weapon("Teeth", 3, 1, "bites")
    
    bone = weapon("old bone club", -1, 3, "swings")

    skel1 = enemy.enemy("Skeleton", "A pile of bones, held together only by the will of the dead.", 5, 
                    [bone, bone, bone,], 10, [boneShard], "The Skeleton crumbles to dust.", woodsNW)
    skel2 = enemy.enemy("Skeleton", "A pile of bones, held together only by the will of the dead.", 5, 
                    [bone, bone, bone,], 10, [boneShard], "The Skeleton crumbles to dust.", woodsNW)
    skel3 = enemy.enemy("Skeleton", "A pile of bones, held together only by the will of the dead.", 5, 
                    [bone, bone, bone,], 10, [boneShard], "The Skeleton crumbles to dust.", woodsSW)
    skel4 = enemy.enemy("Skeleton", "A pile of bones, held together only by the will of the dead.", 5, 
                    [bone, bone, bone,], 10, [boneShard], "The Skeleton crumbles to dust.", woodsSE)
    skel5 = enemy.enemy("Skeleton", "A pile of bones, held together only by the will of the dead.", 5, 
                    [bone, bone, bone,], 10, [boneShard], "The Skeleton crumbles to dust.", woodsDeadS)
    
    skel6 = enemy.enemy("Skeleton", "A pile of bones, held together only by the will of the dead.", 5, 
                    [bone, bone, bone,], 10, [boneShard], "The Skeleton crumbles to dust.", dampCave)
    skel7 = enemy.enemy("Skeleton", "A pile of bones, held together only by the will of the dead.", 5, 
                    [bone, bone, bone,], 10, [boneShard], "The Skeleton crumbles to dust.", dampCave)
    skel8 = enemy.enemy("Skeleton", "A pile of bones, held together only by the will of the dead.", 5, 
                    [bone, bone, bone,], 10, [boneShard], "The Skeleton crumbles to dust.", dampCave)
    skel9 = enemy.enemy("Skeleton", "A pile of bones, held together only by the will of the dead.", 5, 
                    [bone, bone, bone,], 10, [boneShard], "The Skeleton crumbles to dust.", dampCave)
    
    wolf1 = enemy.enemy("Wolf", "A large, mangey beast eyes you hungrily as it stalks towards you.", 10, 
                    [claw, claw, bite], 13, [hide], "The wolf wimpers as it falls.", forest)
    wolf2 = enemy.enemy("Wolf", "A mangy beast, it eyes you hungrily", 10, 
                    [claw, claw, bite], 13, [hide], "The wolf wimpers as it falls.", woodsS)
    wolf3 = enemy.enemy("Wolf", "A mangy beast, it eyes you hungrily", 10, 
                    [claw, claw, bite], 13, [hide], "The wolf wimpers as it falls.", woodsDeadN)
    
    weap = weapon("old bone club", 
                                   -1, 
                                    3, 
                            "swings")

    squirrel_bow = weapon("Squirrel Bow", 1, 1, "shoots")
    squirrel_spear = weapon("Squirrel Spear", 1, 1, "throws")
    squirrel_dag = weapon("Squirrel Dagger", 1, 1, "stabs")

    #should always be able to run from, but always take 1 damage getting away and be forced out unless they leave the squirrel king a treat
    squirrels = enemy.enemy("The Squirrel king", "A number of ferocious looking squirrels approach you in miniature armor.", 666,
                        [squirrel_bow, squirrel_spear, squirrel_dag], 10, [item("King ChitterScritch's Crown", "A beautiful crown made with bits of acorn shells."), item("Strange Gem","Looks valuable.")], "The unspeakable has happened. The squirrels have all died. How have wrought such death?", glade)
    king_chitterscritch = enemy.enemy("King ChitterScritch the 4th", "The other squirrels obviously revere this most impressive Squirrel.", 100, [squirrel_bow, squirrel_spear, squirrel_dag], 10, item("King ChitterScritch's Wand", "An ornate wand covered in small bits of shell, vine and precious stones.", pickup=True), "The mighty King lay fallen. Are you content now, murderer?", glade),

    dagger = weapon("Common Dagger", 2, 3, "stabs")
    shortsword = weapon("Shortsword", 3, 3, "lunges")
    basic_bow = weapon("Common Bow", 2, 3, "fires")

    bandit = enemy.enemy("Bandit","A thug with no conscience. It's hard to believe there are people out here acting this way, despite the Hags presence.", 8, 
                        [dagger, dagger, shortsword], 10, [item("gold purse", "A small coin purse."), item("rapier", "A sharp looking blade."), item("strange document", "It's written in a language that you can't read just yet.")], "You can tell that the bandit realized their mistake, just as it was too late. You saw the look in their eyes as they fail to dodge your killing blow. They collapse.", outskirts)
    bandit2 = enemy.enemy("Bandit","A thug with no conscience. It's hard to believe there are people out here acting this way, despite the Hags presence.", 8, 
                        [basic_bow, basic_bow, basic_bow], 10, [item("gold purse", "A small coin purse.")], "You can tell that the bandit realized their mistake, just as it was too late. You saw the look in their eyes as they fail to dodge your killing blow. They collapse.", outskirts)

    broken_bottle = weapon("Broken Bottle", 1, 1, "slashes")

    drunkard = enemy.enemy("Drunkard"," \"You're not wise, picking a fight with me! Get 'im boys!", 3, 
                        [broken_bottle, broken_bottle, broken_bottle], 10, [item(" broken bottle", "The top half of a broken beer bottle.")], "You hear a crunching sound as the drunkard falls face first into the edge of the table at velocity. He drops.", tavern)

    goblin_pike = weapon("Goblin Pike", 1, 3, "stabs")
    goblin_bow = weapon("Goblin Bow", 2, 3, "fires")
    goblin_axe = weapon("Goblin Axe", 3, 2, "swings")
    goblin = enemy.enemy("goblin","An angry, fiesty goblin. While not dangerous alone, goblins in numbers are problen. Where there is one, there are bound to be more.", 3, 
                        [goblin_pike, goblin_bow, goblin_axe], 10, [item("Grog", "A skin full of a foul smelling, dark drink.")], "The goblin howls in pain before going limp, collapsing to the ground and twitching.", sundial)

    
    bat = enemy.enemy("Bats","A swarm of bats clouds your vision. The sound is incredible as wings fly past your face and around your head.", 1, 
                        [bite, bite, bite], 10, [item("bat's wings", "A severed bat's wing")], "Your attack connects and the bats fall harshly, splattering on the ground.", sundial)

    
    giant_spider = enemy.enemy("Spider","A hulking, fierce insect. This is no time to be act idley. Look out!", 15, 
                        [bite, bite, bite], 10, [item("venomous sac", "A foul smelling sac that you've retrieved from the spider. Probably worth keeping for a potion."), item("spider eyes", "The soft, gushy eyeballs of the spider stare back at you lifelessly."), item("giant spider mandible", "A spider's mandible.")], "", sundial)

    phantasmal_scream = weapon("Phantasmal Scream", 2, 3, "shrieks")
    angry_spirit = enemy.enemy("Spirit","Suddenly a spectacularly spooky spectre swiftly swims through the air towards you. Oh my!", 3, 
                        [phantasmal_scream, phantasmal_scream, phantasmal_scream], 10, [item("ectoplasm", "Colors you can't even begin to describe seem to emanate from the goo."), weapon("ghostly blade", 5, 3, "slash", "A nasty looking blade from another realm. Best be careful handling this.")], "", tree)

    rusted_blade = weapon("Rusted Blade", 1, 2, "slowly swings")
    grab = weapon("hands", 0, 3, "grabs")
    zombie = enemy.enemy("Zombie","A ghoulish fiend approaches. They limber towards you, flesh hanging from their bones. Gross!", 5, 
                        [rusted_blade, rusted_blade, grab], 10, [item("rotten body parts", "You can't forsee a use for these.")], "failed", cemetery)
    
    def enemy_description_flavor(what_enemy, enemy_desc):
      rand_desc = random.randint(0, (len(enemy_desc) -1))
      what_enemy.desc = enemy_desc[rand_desc]


    def death_flavor(what_enemy, death_desc):
        rand_death = random.randint(0, ( len(death_desc) -1 ))
        
        what_enemy.death = death_desc[rand_death]

    zombie_descs = [  "You wonder how the Zombie can sense your location, as it seems its eyes have been pecked out by birds.",
                      "A jawless, one armed Zombie limbers towards you. It moans as it extends a rotting hand towards you.",
                      "You almost didn't notice the legless Zombie crawling towards you, grabbing at your ankles."

                   ]
        
    zombie_deaths = [ "The Zombie trips towards you. As it stumbles, it catches your attack and is decaptiated in an excessive display of gore.",
                    "The Zombie takes the full force of your attack, its chest exploding.",
                    "The Zombie's slow movements cost it dearly. Before it could think to react, you land a fatal blow. It collapses."
                    ]

    skel1_descs = [ "A member of the ranks of the undead. This skeleton soldier still wears armor.",
                    "The chattering of bones alerts you to the presence of the Skeleton moving towards you."
                    "You swear that you can almost see a small light glowing in the empty eye sockets of the Skeleton."
                   ]


    skel1_deaths = [ 
                    "The Skeleton explodes into a cloud of dust and fragments of bone.",
                    "The unmistkable sound of bones scattering to the ground informs you that the skeleton has been defeated.",
                    "Fragments of bone fly past your face as the skeleton is obliterated."
                    
                    ]

    skel2_descs = [
                          "The Skeleton explodes into a cloud of dust and fragments of bone.",
                    "The unmistkable sound of bones scattering to the ground informs you that the skeleton has been defeated.",
                    "Fragments of bone fly past your face as the skeleton is obliterated."


                   ]       

    skel2_death =[ "The Skeleton explodes into a cloud of dust and fragments of bone.",
                    "The unmistkable sound of bones scattering to the ground informs you that the skeleton has been defeated.",
                    "Fragments of bone fly past your face as the skeleton is obliterated."
                    ]
    skel3_descs = [
                          "The Skeleton explodes into a cloud of dust and fragments of bone.",
                    "The unmistkable sound of bones scattering to the ground informs you that the skeleton has been defeated.",
                    "Fragments of bone fly past your face as the skeleton is obliterated."

                   ]
    skel3_death =[ "The Skeleton explodes into a cloud of dust and fragments of bone.",
                    "The unmistkable sound of bones scattering to the ground informs you that the skeleton has been defeated.",
                    "Fragments of bone fly past your face as the skeleton is obliterated."
                    ]
    skel4_descs = [
                          "The Skeleton explodes into a cloud of dust and fragments of bone.",
                    "The unmistkable sound of bones scattering to the ground informs you that the skeleton has been defeated.",
                    "Fragments of bone fly past your face as the skeleton is obliterated."

                   ]
    skel4_death =[ "The Skeleton explodes into a cloud of dust and fragments of bone.",
                    "The unmistkable sound of bones scattering to the ground informs you that the skeleton has been defeated.",
                    "Fragments of bone fly past your face as the skeleton is obliterated."
                    ]
    skel5_descs = [
                    "The Skeleton explodes into a cloud of dust and fragments of bone.",
                    "The unmistkable sound of bones scattering to the ground informs you that the skeleton has been defeated.",
                    "Fragments of bone fly past your face as the skeleton is obliterated."
                   ]
    skel5_death = [ "The Skeleton explodes into a cloud of dust and fragments of bone.",
                    "The unmistkable sound of bones scattering to the ground informs you that the skeleton has been defeated.",
                    "Fragments of bone fly past your face as the skeleton is obliterated."
                    ]
    bat_descs = [ "A swarm of bats clouds your vision. The sound is incredible as wings fly past your face and around your head.",
                  "Suddenly you are surrounding by a flurry of wings and shrieking sounds. Bats!",
                  "You have disturbed a colony of bats. All at once, they begin aggressively biting at your face, neck and hands."
                   ]

    bat_deaths = [ "With a painful shriek, the bat explodes. Dark blood splatters the ground.",
                    "Despite it being a wild swing, you catch one of the bats flying by your head. It is obliterated, and the rest fly off.",
                    "When your attacks begin to thin their numbers, the bats flee in search of easier prey."
    ]
    
    giant_spider_descs = [ "A hulking, fierce insect approaches you. This is no time to be act idley. Look out!",
                           "With a thunderous sound, a Giant Spider erupts from the shadows. It's mandibles clack loudly as its beady eyes lock onto you.",
                           "A Giant Spider descends from a web above you. It rears back on it's hind legs, ready to attack.",

                   ]
    giant_spider_deaths = [ "The Giant Spider crumples into a bent, twisted shape as it hugs its wounds. It dies, shortly after",
                            "The enormous foe struggles against the inevitable. Its wounds are too great. It sways unsteadily on its legs before collapsing, dead.",
                            "The Giant Spider had once dominated this section of the mines, but no longer. It lay still, aside from some involuntary twitching. "
                          ]
    hatchling_spider_descs = [ "Several Hatchling Spiders land on the ground around you, hurriedly moving towards you.",
                              "Hundreds of tiny eyes scan you from the darkness. One by one, they start launching themselves at you.",
                              "The presence of the webs should have been enough to prepare you. Hatchling Spiders begin to surround you!",
                              "While this spider is not as big as it will eventually be, it is much larger than you are comfortable being close to."

                   ]                          
    hatchling_spider_deaths = [ "A sickly squishing noise and a hiss erupts from the spider.",
                                "Your attack connects with the spider, producing an unpleasant ...CRUNCH!,",
                                "You nearly feel ill seeing the the spider evicerated. Pieces of the arachnid's limbs and dark green blood paint the room."  
                              ]
    goblin_descs = [ "A nasty looking Goblin with a scar under his right eye points angrily at you. \"MEAT!\" it shrieks.",
                    " A chubby looking Goblin stops draining its mug of grog just long enough to howl in your direction, alerting the others.",
                    "A fairly intimidating Goblin, armed to the teeth, face covered in pustules approaches, cracking its neck.",
                     "An angry, fiesty goblin. While not dangerous alone, goblins in numbers are problen. Where there is one, there are bound to be more."


                   ]
    goblin_deaths = [ "'BEAST! YOU BEAST!' the goblin screams as you, clutching its chest, aware that it was dying.",
                      "You have proven yourself the more dangerous foe. The goblin is severed in two by your attack.",
                      "The goblin starts to curse your name, but chokes. Your attack has pierced the goblin's lungs. It collapses and dies."
                    ]

    angry_spirit_descs = [ "Suddenly a spectacularly spooky spectre swiftly swims through the air towards you. Oh my!",
                           "The air around you chills over, and the hair on the back of your neck stands up. A ghost appears!",
                           "You are caught off your guard when a spectre emerges from the shadows, screaming at you."

                   ]

    angry_spirit_deaths = [ "The spectre is spooped. They dissipate into nothingness, returning to the void.",
                            "'DEATH IS NOT THE END', the spirit hisses as it dissapates.",
                            "'I WILL RETURNNNNNNNnnnnnn....', the spirit screams as it fades out of existence."
                         ]
    wolf_descs = [ "A large, mangey beast eyes you hungrily as it stalks towards you.",
                   "The crunch of leaves gives the wolf's position away. It snarls, and you ready your weapons.",
                   "A large wolf jumps out at you from behind a bush, gnashing its teeth at you."

                   ]

    wolf_deaths = [ "The wolf wimpers as it falls.",
                    "Your attack catches the wolf between its ribs. It trips over itself, sliding across the ground towards you, dead.",
                    "The wolf's powerful jaws snap at you, but your quick reflexes land an attack that strikes it through the muzzle. It collapses, dead."
                  ]

    bandit_descs = [ "\"What have we got here?\" the bandit asks, \"A lil mouse has lost its way.\" You see the bandit unsheathe their weapon.",
                      "A thug with no conscience. It's hard to believe there are people out here acting this way, despite the Hags presence."
                      "This bandit has chosen the wrong protagonist to mess with. While sure of themselves, they are now surely doomed to die."

                   ]

    bandit_deaths = [  "You can tell that the bandit realized their mistake, just as it was too late. You saw the look in their eyes as they fail to dodge your killing blow. They collapse.",
                       "Your stomach wretches as you see the bandit disemboweled by your attack. They drops their weapons, desparately clutching their intestines to their body.",
                       "The bandit paid the price for their profession. Your attack slices through the bandit easily, resulting in a plume of arterial spray."
                    ]
    bandit2_descs = ["\"What have we got here?\" the bandit asks, \"A lil mouse has lost its way.\" You see the bandit unsheathe their weapon.",
                      "A thug with no conscience. It's hard to believe there are people out here acting this way, despite the Hags presence."
                      "This bandit has chosen the wrong protagonist to mess with. While sure of themselves, they are now surely doomed to die."

                   ]

    bandit2_deaths = [  "You can tell that the bandit realized their mistake, just as it was too late. You saw the look in their eyes as they fail to dodge your killing blow. They collapse.",
                        "Your stomach wretches as you see the bandit disemboweled by your attack. They drops their weapons, desparately clutching their intestines to their body.",
                        "The bandit paid the price for their profession. Your attack slices through the bandit easily, resulting in a plume of arterial spray."
                       
                       ]

    hag1_cleaver = weapon("Carriona's Cleaver", 10, 5, "slashes", "A terrible blade. The hilt looks like it was made from a child's bones.")
    carriona_call = weapon("Carriona's Call", 15, 2, "sings", "Carionna's voice echoes in your ears, enchanting you.", pickup=False)
    hag1_BOSS = enemy.enemy("Carriona Bramblebone ", "Carriona is a large, gluttonous being. She smacks her lips greedily, stands and grabs a knife.", 50, 
                    [hag1_cleaver, hag1_cleaver, carriona_call], 15, [hag1_cleaver], "", cottage)
    hag1_deaths = [ "Carriona, youngest of the Hag sisters, has fallen. Her wounds are grievous, and she slumps back into her chair, gasping for one final breath before she passes."]

    hag2_shadow_strike = weapon("Shadow Strike", 12, 6, "pierces", "Shadows swell and stab at the gaps in your armor. Everything is cold.", pickup=False)
    hag2_corruption = weapon("Corruption", 12, 10, "casts", "Enfeebling beams of darkness fly from her fingertips like daggers.", pickup=False)
    heart_of_shadows = item("Heart of Shadows", "A companion gem to the Blood of Shadows. It stinks of evil magic.", pickup=True)
    hag2_BOSS = enemy.enemy("Pumera Prickersnout", "Pumera's eyes peer out at you from the shadows: big, glowing orbs full of hate.", 75, [hag2_shadow_strike, hag2_corruption, hag2_corruption], 15, [heart_of_shadows], "", deepwoods_HagLair)
    
    hag2_deaths = [ "The shadows have been lifted, and sunlight once again returns to this part of the wood. Pumera Prickersnout, secondborn of the Hag sisters, is defeated."]
    
    hag3_needle = weapon("Nefarious Needle", 13, 13, "stabs", "A vicious, sharp implement capable of piercing all but the strongest of armors.", pickup=True)
    hag3_BOSS = enemy.enemy("Jezebella Crowseye", "She appears as a most beautiful woman, wading in the shallow pools behind the waterfall.", 85, [hag3_needle, hag3_needle, hag3_needle], 15, [hag3_needle], "", dampCave)
    
    hag3_deaths = ["Jezebella falls backwards, causing a terrific splash. Her blood flows out from her wounds, tinting the water a deep, awful red."]

    
    ENDING_LOCAL = Location("The Bitter End", "The Hamlet is under seige. All Hell has broken loose.", "", [], [], [])
    hag4_scythe = weapon("Mefilda's Malice", 20, 10, "swings", "Mefilda's Malice is the physical realization of her hatred and contempt for the living.", pickup=True)
    
    hag4_BOSS = enemy.enemy("Mefilda Rottenbough", "Many believed Mefilda to be dead. Vengeance has come, finally, and her name is Mefilda.", 100, [], 15, [hag4_scythe], "", ENDING_LOCAL)
    

    # def end_desc():
    #   prints("The winds pick up, spinning at incredible speeds. A tornado forms, reaching a long tendril down towards Mefilda, who screams.")
    #   prints("Try as she might, she cannot escape. With a terrible cry, she is lifted from the ground and swallowed by the sky.")
    #   prints("Shortly thereafter, the sky clears and villagers begin spilling out from their hiding places. Most stare in stunned silence,")
    #   prints("until a few begin to cheer. It is said that many miles away, in neighboring villages, folks could hear the triumphant")
    #   prints("cries of the Hamlet. They chant your name, sing your praises, and hold a feast in your honor. You have saved the Hamlet,")
    #   prints("and perhaps the world, as it were. For years to come, your name will exist as legend. For the present,")
    #   prints("                                  -----##### YOU ARE A HERO #####----")

            
    #   prints("                    _______               _______  _______  _______   ")
    #   prints("          |\     /|(  ___  )|\     /|    (  ___  )(  ____ )(  ____ \" ")
    #   prints("          ( \   / )| (   ) || )   ( |    | (   ) || (    )|| (    \/  ")
    #   prints("          \ (_) / | |   | || |   | |    | (___) || (____)|| (__       ")
    #   prints("           \   /  | |   | || |   | |    |  ___  ||     __)|  __)      ")
    #   prints("            ) (   | |   | || |   | |    | (   ) || (\ (   | (         ")
    #   prints("            | |   | (___) || (___) |    | )   ( || ) \ \__| (____/\"  ")
    #   prints("            \_/   (_______)(_______)    |/     \||/   \__/(_______/   ")
    #   prints("                                                                      ")
    #   prints("              _______                 _______  _______  _______       ")
    #   prints("             (  ___  )      |\     /|(  ____ \(  ____ )(  ___  )      ")
    #   prints("             | (   ) |      | )   ( || (    \/| (    )|| (   ) |      ")
    #   prints("             | (___) |      | (___) || (__    | (____)|| |   | |      ")
    #   prints("             |  ___  |      |  ___  ||  __)   |     __)| |   | |      ")
    #   prints("             | (   ) |      | (   ) || (      | (\ (   | |   | |      ")
    #   prints("             | )   ( |      | )   ( || (____/\| ) \ \__| (___) |      ")
    #   prints("             |/     \|      |/     \|(_______/|/   \__/(_______)      ")
                                                                

    
    # ending = end_desc()
    # hag4_deaths = [end_desc()]
    

    
    



    enemy_description_flavor(zombie, zombie_descs)
    enemy_description_flavor(skel1, skel1_descs)
    enemy_description_flavor(skel2, skel1_descs)
    enemy_description_flavor(skel3, skel1_descs)
    enemy_description_flavor(skel4, skel1_descs)
    enemy_description_flavor(skel5, skel5_descs)
    enemy_description_flavor(bat, bat_descs)
    enemy_description_flavor(giant_spider, giant_spider_descs)
    enemy_description_flavor(hatchling_spider, hatchling_spider_descs)
    enemy_description_flavor(bandit, bandit2_descs)
    enemy_description_flavor(bandit, bandit_descs)
    enemy_description_flavor(wolf1, wolf_descs)
    enemy_description_flavor(wolf2, wolf_descs)
    enemy_description_flavor(wolf3, wolf_descs)
    enemy_description_flavor(angry_spirit, angry_spirit_descs)
    enemy_description_flavor(goblin, goblin_descs)
    
    

    death_flavor(zombie, zombie_deaths)
    death_flavor(skel1, skel1_deaths)
    death_flavor(skel2, skel2_death)
    death_flavor(skel3, skel3_death)
    death_flavor(skel4, skel4_death)
    death_flavor(bat, bat_deaths)
    death_flavor(giant_spider, giant_spider_deaths)
    death_flavor(hatchling_spider, hatchling_spider_deaths)
    death_flavor(bandit, bandit2_deaths)
    death_flavor(bandit2, bandit2_deaths)
    death_flavor(wolf1, wolf_deaths)
    death_flavor(wolf2, wolf_deaths)
    death_flavor(wolf3, wolf_deaths)
    death_flavor(angry_spirit, angry_spirit_deaths)
    death_flavor(goblin, goblin_deaths) 
    

    """ death_flavor(hag1, hag1_deaths)
    death_flavor(hag2, hag2_deaths)
    death_flavor(hag3, hag3_deaths)
    death_flavor(hag4, hag4_deaths)
     """


            


    outskirts.enemyArr = [bandit]
    outskirts.enemyArr = [bandit, bandit2]
    cemetery.enemyArr = [zombie]
    tree.enemyArr = [angry_spirit]
    glade.enemyArr = [squirrels, king_chitterscritch]
    woodsNW.enemyArr = [skel1, skel2]
    woodsSW.enemyArr = [skel3]
    woodsSE.enemyArr = [skel4]
    woodsDeadS.enemyArr = [skel5]
    dampCave.enemyArr = [skel6,skel7,skel8,skel9]
    forest.enemyArr = [wolf1]


    forest.enemyArr = [wolf1]
    woodsS.enemyArr = [wolf2]
    woodsDeadN.enemyArr = [wolf3]


    def hunter_intro():
      prints("")
      prints("The hunter is a very large person. As soon as they turn to greet you,")
      prints("you realize how small you are in comparison. Though his stature")
      prints("precluded you to believe that he was harsh man, his demeanor led you to believe otherwise.")
      prints("\"Well, I guess that one is getting away.\" He says, hanging his head, feigning disappointment.")
      prints("")

    def hunter_quest(self):
        prints("")
        prints("    The hunter smacks his lips, \"Have you met Aziz? That merchant is rumoured to have")
        prints("    the coldest beer in all the land. It's mighty strong stuff, and tastes fantastic!\"")
        self.setQuest("     **    Hand him the beer**", "\"he looks at it in awe.\"", 3, 0)
        prints("")

    def hunter_questEnd():
        prints("")
        prints("    \"My oh my! Thank you so much,\" the Hunter says as he takes the beer from you.")
        prints("    \"Oh my...It's still cold...How wonderful...\" he manages to say as he sips greedily")
        prints("    from the stein.")
        prints("                    --- #### YOU'VE GOT THE HUNTER'S MAP #### ---")
        prints("")
        map.waterfall1.adj_locations.append(map.dampCave)




    hunter_dialogue_options = [
    "     Who are you?", 
    "     What are you doing out here?", 
    "     What do you know about the Hags' Curse?",
    "     *** QUEST *** You look troubled. Can I help you in some way?",
    "     Goodbye."
    ]

    hunter_dialogue_outcome = [
        "   \"The name is Arthur. Arthur Edenbough. \" ", 
        "   \"I thought I was going to finally fell that buck. Now you're here.\" ",
        "   \"I've never seen one of them personally, but these woods are teeming with monsters. I don't past the brambles. It's too dark.\" ",
        "   \"I'm so terribly thirsty. If you could bring me a cold beer, I'd be more than happy to share my map with you.\" ", 
        "   \"Happy hunting!\" "
            ]

    hunters_map = item("Hunter's Map", "A map given to you by the Hunter. It describes a path that leads one behind the Waterfall.")
    hunter_questTrades = [ [hunters_map, "Coldest Beer", hunter_questEnd, 3] ]

    hunter = npc("Hunter", hunter_ascii, hunter_intro, hunter_dialogue_options, hunter_dialogue_outcome, -1, [], hunter_questTrades, 3, hunter_quest, 3)

    def hag1_intro():
      prints("")
      prints("    As you enter the abdandoned cottage, you see a Hag sitting at the dining table. She")
      prints("is almost too busy picking bits of gristle and bone from her teeth to notice you. the")
      prints("bloodied remains of what look to be several children lie in a heap in the corner. She")
      prints("motions you in, gesturing towards the pile of corpses with her hand.")
      prints("    \"Care for a bite, dearie?\" she cackles. \"What do you think you're here to do, eh?\"")
      prints("")

    hag1_options = [
    "   .....",
    "   You should leave this place.",
    "   I'm here to kill you.",
    "   **Fight** You monster!"
    ]

    hag1_outcomes = [
    "   \"Cat got your tongue? It matters not.\"",
    "   \"Well you're a bold one, aren't you!\" she says, howling with laughter. Prepare yourself!\"",
    "   \"Oh? I don't see a reason I should do that. Prepare yourself, foolish mortal!",
    "   \"How original. Such a pity. You might have made a lovely cook one day."

    ]

    def hagFight(self):
        prints("   The hag seems to grow too big for the room as she stands, looming over you.")
        self.local.enemyArr.append(map.hag1_BOSS)
        self.local.interactables.remove(self)

    hag1 = npc("Hag1", hag1_ascii, hag1_intro, hag1_options, hag1_outcomes, -1, [], [],3, hagFight, -1, -1, cottage)

    def hag2_intro():
        prints("")
        prints("    Shadows emanate from the Hag like creeping vines, crawling across the forest floor,")
        prints("searching for your flesh. A sense of dread washes over you, and you find it hard to steel yourself")
        prints("in the face of such incredible danger.")
        prints("")

    hag2_options = [
    "   I HAVE THE AMULET. You cannot win this fight, you HAG!",
    "   It's over! You cannot stay in the forest!",
    "   Leave the Hamlet or die, you wretched thing!",
    "   **Fight** I will send you to the Hells, Hag!"

    ]

    hag2_outcomes = [
    "   \"You miserable toad. Do you really think that you can defeat me?\"",
    "   \"Pathetic! I hope you've made funerary arrangements for yourself.",
    "   \"Leave?...Why? There are so many people I haven't killed there yet,\" she says, cackling.",
    "   \"Oh child,\" she tuts,\"It's bad manners to trespass. Now you'll pay the price!\""


    ]
    def hag2fight(self):
      prints("  You feel the shadows around you begin to close in, dancing as if possesed")
      self.local.enemyArr.append(map.hag2_BOSS)
      self.local.interactables.remove(self)

    hag2 = npc("hag2", hag2_ascii, hag2_intro, hag2_options, hag2_outcomes, -1, [], [], 3, hag2fight, -1, -1, deepwoods_HagLair)

    def hag3_intro():
        prints("")

        prints("")

    hag3_options = [
    "   You find yourself unable to speak, despite your best efforts.",
    "   Your tongue refuses to move behind your teeth. You cannot speak.",
    "   Your mouth feels as though it has been glued shut. Something is wrong.",
    "   **Fight** You open your mouth, but no sound escapes you."

    ]

    hag3_outcomes = [
    "   \"What's the matter, dearest? Have you never seen such a sight?\" the Hag asks, sporting a malevolent grin.",
    "   \"Oh...Now this is rich!\" she laughs at you, \"Can't even talk to a woman...pathetic.\"",
    "   \"It'll be easier killing you than it was dispatching that silly little thief's wife.\"",
    "   \"You don't have to speak, child. It'll be over soon.\""

    ]

    def hag3fight(self):
      prints("You had no idea something could be this terrifying.")
      prints("she stands.",3) 
      self.local.enemyArr.append(map.hag3_BOSS)
      self.local.interactables.remove(self)


    hag3 = npc("hag3", hag3_ascii, hag3_intro, hag3_options, hag3_outcomes , -1, [], [], 3, hag3fight, -1, -1, dampCave) 

    def hag4_intro():
        prints("")
        prints("    There is chaos. Screams, blood, and death surround you. The Hag Queen has")
        prints("come at last to cull the herd and claim the Hamlet for herself. Citizens of")
        prints("the hamlet scramble to find cover. Some board their windows, praying desparately")
        prints("for a miracle to change this outcome. Those closest to the well, aware of the ")
        prints("goings on beneath the town, descend as quickly as they can manage. Storms appear,")
        prints("the wind picks up and trees are uprooted all around you.")
        prints("    \"SEE NOW, THIS GREAT AND TERRIBLE DEVESTATION")
        prints("     THAT I WILL BRING UPON THEE. PREPARE NOW TO DIE,")
        prints("                    PATHETIC HUMANS!\"")
        prints("")

    hag4_options = [

    "   The battle for the fate of the Hamlet has begun."

    ]

    hag4_outcomes = [

    "   \"What meager peasant plays at being a hero, hm? You shall suffer, mortal!\""

    ]

    def hag4fight(self):
      "she stands before you..."
      self.local.enemyArr.append(map.hag4_BOSS)
      self.local.interactables.remove(self)
      
      

    hag4 = npc("hag4", hag4_ascii, hag4_intro, hag4_options, hag4_outcomes)

    cottage.interactables = [doll, toadEye, small_weapon_chest, hag1]
    dampCave.interactables = [hag3]
    deepwoods_HagLair.interactables.append(hag2)

    death_flavor(hag1_BOSS, hag1_deaths)
    death_flavor(hag2_BOSS, hag2_deaths)
    death_flavor(hag3_BOSS, hag3_deaths)
    #death_flavor(hag4_BOSS, hag4_deaths)