from location import Location
from prints import printr
from prints import prints
from item import item
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
    waterfall = Location("The Waterfall", "Murky water thunders over the fall, what could it be hiding?", "hnh_forestTheme_conceptQ.mp3", [],[],[])
    dampCave = Location("The Cove", "The deafaning roar of the waterfall falls surprisingly quiet beyond the veil of foam and murk", "hnh_forestTheme_conceptQ.mp3", [], [],[], True)
    path = Location("The Twisted Path", "A small, twisting path beckons you deeper into the woods.","hnh_forestTheme_conceptQ.mp3", [], [],[])
    camp = Location("The Hunter's Camp", "whatever fire was once here has long since died out, a raggedy tent sits nested between two large daggerlike stones","hnh_forestTheme_conceptQ.mp3", [], [],[])

    forest = Location("The Forest", "The Hamlet eventually gives way to the forest, the trees press close, and the fog closer.","hnh_forestTheme_conceptQ.mp3", [], [],[])
    cottage = Location("The Old Cottage", "a small stream cuts directly through the sagging cottage, you swear you can hear faint music from inside.", "hnh_forestTheme_conceptQ.mp3", [], [],[])
    farm = Location("The Barn", "a faded barn stands amidst the trees","hnh_forestTheme_conceptQ.mp3", [], [],[])
    glade = Location("The Glade", "perhaps the only truly beautiful place left, you swear you can just barely see the sun up there", "hnh_forestTheme_conceptQ.mp3", [],[],[])


     #OLD MINES
    old_mines_entrance = Location("Old Mines: Entrance", "Once a great mine, the resources have been mostly used up. The dwarven miners that still work here must fight to keep it clear of enemies in the absence of more capable fighters.", [],[],[], True),
    old_mines_main_chamber = Location("Old Mines: First Chamber", "The Old Mine is dimly lit by torches. Several groups of dwarves are huddled. Some are tending to wounds, others eating lunch.", [],[],[], True)
    old_mines_floor1_NW = Location("Old Mines", "A dimly lit corridor. Various scraps of metal and other tools litter the area. Someone left in a hurry.", [],[],[], True)
    old_mines_floor1_N = Location("Old Mines", "An old mine cart lay here, toppled on its side.", [],[],[], True)
    old_mines_floor1_NE = Location ("Old Mines", "Following the tracks, you see that the corridor ahead leads deeper into the mines.", [], [], [], True)
    old_mines_floor2 = Location("Old Mines", "Before you is a great Iron door. Bloody handprints have left rusty colored marks on the wood. The bar blocking the door has been bent from the force of something large hitting it.", [], [], [], True)
    old_mines_floor2_W = Location("Old Mines", "The dwarves have warned you that the path ahead would not be easy. The way forward requires that you pass through an impressive number of cobwebs.", [],[],[], True)
    old_mines_floor2_W2 = Location("Old Mines: Supply Cache", "A small chamber dedicated to storing supplies.", [], [], [],True)
    old_mines_center_chamber = Location("Old Mines: Center Chamber", "A large chamber with a statue of the famous dwarf, Mozal Mon. A locked chest rests at the Statue's feet.", [],[],[], True)
    old_mines_floor2_W3 = Location("Old Mines", "The enormous webs grow thicker here.", [],[],[],True)
    old_mines_floor2_wN = Location("Old Mines: The Forge", "This forge hasn't been operational for some time. There are bones and webs everywhere.", [],[],[],True)
    old_mines_floor2_wN2 = Location("Old Mines: The Armory", "This place was surely wondrous some time ago. Now various weapons and armor lay discarded on the stone, forgotten or abandoned by dwarves desparate to escape.", [],[],[],True)
    old_mines_floor2_wN2_W = Location("Old Mines: Webbed Path", "You're not sure you should be here. The entirety of the corridor is covered with webs. The decaying husks of the spiders' victims hang from the ceiling.", [],[],[],True)
    old_mines_floor2_wN2_W2 = Location("Old Mines", "The webs are next to impassable here, but just ahead you can a clearer space." ,[], [], [],True)
    old_mines_spider_lair = Location("Spiders' Lair", "A large cavern littered with bodies, bones and webs. Hundreds of spider eggs cling to the floor, walls and ceiling of the cavern.", [],[],[],True)

    #OLD MINES FLOOR 1 DIRECTIONAL 
    #old_mines_entrance.adj_locations = [old_mines_main_chamber]
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
    hatchling_spider = enemy.enemy("Spider Hatchling", "While this spider is not as big as it will eventually be, it is much larger than you are comfortable being close to.", 3, [bite, bite, bite], 5, [], "A sickly squishing noise and a hiss erupts from the spider.", old_mines_floor2_W)
    giant_spider = enemy.enemy("Giant Spider","A hulking, fierce insect. This is no time to be act idley. Look out!", 15, 
                        [bite, bite, bite], 10, [item("venomous sac", "A foul smelling sac that you've retrieved from the spider. Probably worth keeping for a potion."), item("spider eyes", "The soft, gushy eyeballs of the spider stare back at you lifelessly."), item("giant spider mandible", "A spider's mandible.")], "The spider crumples into a bent, twisted shape as it hugs its wounds. It dies, shortly after", old_mines_spider_lair)
    
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

    #old_mines_entrance.interactables = []
    old_mines_floor1_N.interactables = []
    old_mines_floor1_NE.interactables = []
    old_mines_floor1_NW.interactables = []
    old_mines_floor2.interactables = []
    old_mines_floor2_W.interactables = []
    old_mines_floor2_W2.interactables = []
    old_mines_center_chamber.interactables = []
    old_mines_floor2_W3.interactables = []
    old_mines_floor2_wN.interactables = []
    old_mines_floor2_wN2.interactables = []
    old_mines_floor2_wN2_W.interactables = []
    old_mines_floor2_wN2_W2.interactables = []
    old_mines_spider_lair.interactables = []
    
    
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
    library = Location("The Library","Most of the books have been overrun by mold, but you may still be able to find something usefull", [], [],[],True)
    wagon = Location("The Merchant Wagon", "The small covered wagon smells of incense and dust.", [], [],[],True)
    well = Location("The Well", "you cant see the bottom of the well, but for some reason, you can hear running water below.", [], [],[],True)

    hamlet.adj_locations = [store, sundial, tavern, QBoard, blacksmith, library, wagon, well]
    hamlet.interactables = []

    store.adj_locations = [hamlet]
    store.interactables = []

    sundial.adj_locations = [store, tavern, QBoard, blacksmith, library, wagon, well,]
    sundial.interactables = []

    tavern.adj_locations = [hamlet]
    tavern.interactables = []

    QBoard.adj_locations = [store, tavern, sundial, blacksmith, library, wagon, well]
    QBoard.interactables = []

    library.adj_locations = [hamlet]
    library.interactables = []

    wagon.adj_locations = [store, tavern, sundial, blacksmith, library, QBoard, well,]
    wagon.interactables = []

    well.adj_locations = [store, sundial, tavern, QBoard, blacksmith, library, wagon]
    well.interactables = []

     #SEWERS 
    sewers = Location("Sewer Entrance", "It definitely smells like a sewer. With some effort, you would be able to move the cover and enter. It seems dark.", [],[],[])
    sewer_tunnels = Location("Sewer Tunnels", "A disgusting smell assaults your senses every second that you spend here.", [],[],[],True)
    sewer_tunnelsN = Location("Sewer Tunnels", "The path widens. This looks like a maintenance tunnel.", [],[],[],True)
    sewer_tunnelsE = Location("Sewer Tunnels", "The path opens into a large room. There are two doors here. You can hear the sounds of clinking glasses. One door is guarded by a large, hooded man.", [],[],[],True)
    sewer_tunnelsW = Location("Sewer Tunnels", "Faint chittering sounds echo down the tunnel towards you.", [],[],[],True)
    

    sewer_tunnels.enemyArr = []
    sewer_tunnelsN.enemyArr = []
    sewer_tunnelsE.enemyArr = []
    sewer_tunnelsW.enemyArr = []

    sewer_tunnels.interactables = []
    sewer_tunnelsN.interactables = []
    sewer_tunnelsE.interactables = [] 
    sewer_tunnelsW.interactables = []


    speakeasy = Location("The Speakeasy", "A place for seedier types to relax and try to forget about the Hags' Curse.", [],[],[], True)
    speakeasy.interactables = []

    thieves_den = Location("Thieves' Den", "This place is well hidden beneath the Hamlet. It seems odd that such a remote space in the world would be home to such a place.", [],[],[],True)
    thieves_den.interactables = []

    rat_kings_nest = Location("The Rat King's Nest", "This place is a mess of trinkets, weapons, armor and scraps of paper. You're not sure which smells worse- the sewers or the nest.", [],[],[], True)
    rat_kings_nest.interactables = []
    
    sewers.adj_locations = [sewer_tunnels]
    sewer_tunnels.adj_locations = [sewers, sewer_tunnelsN, sewer_tunnelsW]
    sewer_tunnelsN.adj_locations = [sewer_tunnels, sewer_tunnelsE]
    sewer_tunnelsE.adj_locations =[sewer_tunnelsN, speakeasy, thieves_den]
    sewer_tunnelsW.adj_locations = [sewer_tunnels, rat_kings_nest],
    thieves_den.adj_locations = [sewer_tunnelsE]
    speakeasy.adj_locations = [sewer_tunnelsE]
    

    cemetery.adj_locations = [outskirts]
    outskirts.adj_locations = [cemetery, gates, tree]
    tree.adj_locations = [outskirts]
    gates.adj_locations = [clearing, outskirts]
    clearing.adj_locations = [gates, woodsN, woodsS, path]
    woodsN.adj_locations = [woodsNW, clearing, woodsDeadN] #old mines once they start
    woodsNW.adj_locations = [woodsN, path]
    woodsDeadN.adj_locations = [woodsN]
    woodsS.adj_locations = [woodsSE, woodsSW, clearing]
    woodsSW.adj_locations = [path, woodsSE, woodsS, waterfall]
    woodsSE.adj_locations = [woodsSW, woodsS, woodsDeadS]
    woodsDeadS.adj_locations = [woodsSE]
    waterfall.adj_locations = [dampCave, woodsSW]
    dampCave.adj_locations = [waterfall]
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
    
    
    cemetery.interactables = [newGrave, medGrave, ancGrave, greg, smith, wooden_box, startingChest] 

    
    outskirts.interactables = [oldSpear, tombStone]
    tree.interactables = [ruby, noose]
    woodsN.interactables = [herbs]
    woodsDeadN.interactables = [stump, oldHammer]
    woodsSE.interactables = [herbs]
    woodsNW.interactables = [deathcap]
    woodsDeadS.interactables = [oldSword]
    waterfall.interactables = [riverGlass]
    cottage.interactables = [doll, toadEye]

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
    
    wolf1 = enemy.enemy("Wolf", "A mangy beast, it eyes you hungrily", 10, 
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
    squirrels = enemy.enemy("A number of ferocious looking squirrels approach you in miniature armor.","You have unwittingly stepped into the glade of the Squirrel King, ChitterScritch the 4th, blessings upon them. You should leave an offering or run.", 666, 
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
                        [bite, bite, bite], 10, [item("venomous sac", "A foul smelling sac that you've retrieved from the spider. Probably worth keeping for a potion."), item("spider eyes", "The soft, gushy eyeballs of the spider stare back at you lifelessly."), item("giant spider mandible", "A spider's mandible.")], "The spider crumples into a bent, twisted shape as it hugs its wounds. It dies, shortly after", sundial)

    phantasmal_scream = weapon("Phantasmal Scream", 2, 3, "shrieks")
    angry_spirit = enemy.enemy("Spirit","Suddenly a spectacularly spooky spectre swiftly swims through the air towards you. Oh my!", 3, 
                        [phantasmal_scream, phantasmal_scream, phantasmal_scream], 10, [item("ectoplasm", "Colors you can't even begin to describe seem to emanate from the goo."), item("ghostly blade","A nasty looking blade from another realm. Best be careful handling this.")], "The spectre is spooped. They dissipate into nothingness, returning to the void.", tree)

    rusted_blade = weapon("Rusted Blade", 1, 2, "slowly swings")
    grab = weapon("hands", 0, 3, "grabs")
    zombie = enemy.enemy("Zombie","A ghoulish fiend approaches. They limber towards you, flesh hanging from their bones. Gross!", 5, 
                        [rusted_blade, rusted_blade, grab], 10, [item("rotten body parts", "You can't forsee a use for these.")], "The zombie trips towards you. As it stumbles, it catches your attack and is decapitated in an excessive display of gore.", cemetery)
 
 

   

            
""" 

    outskirts.enemyArr = [bandit]
    outskirts.enemyArr = [bandit, bandit2]
    cemetery.enemyArr = [zombie]
    tree.enemyArr = [angry_spirit]
    glade.enemyArr = [squirrels]
    woodsNW.enemyArr = [skel1, skel2]
    woodsSW.enemyArr = [skel3]
    woodsSE.enemyArr = [skel4]
    woodsDeadS.enemyArr = [skel5]
    dampCave.enemyArr = [skel6,skel7,skel8,skel9]
    forest.enemyArr = [wolf1]

    forest.enemyArr = [wolf1]
    woodsS.enemyArr = [wolf2]
    woodsDeadN.enemyArr = [wolf3]
 """
    


    

