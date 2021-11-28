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

class map():
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
    dampCave = Location("The Cove", "The deafaning roar of the waterfall falls surprisingly quiet beyond the veil of foam and murk", "hnh_forestTheme_conceptQ.mp3", [], [],[])
    path = Location("The Twisted Path", "A small, twisting path beckons you deeper into the woods.","hnh_forestTheme_conceptQ.mp3", [], [],[])
    camp = Location("The Hunter's Camp", "whatever fire was once here has long since died out, a raggedy tent sits nested between two large daggerlike stones","hnh_forestTheme_conceptQ.mp3", [], [],[])

    forest = Location("The Forest", "The Hamlet eventually gives way to the forest, the trees press close, and the fog closer.","hnh_forestTheme_conceptQ.mp3", [], [],[])
    cottage = Location("The Old Cottage", "a small stream cuts directly through the sagging cottage, you swear you can hear faint music from inside.", "hnh_forestTheme_conceptQ.mp3", [], [],[])
    farm = Location("The Barn", "a faded barn stands amidst the trees","hnh_forestTheme_conceptQ.mp3", [], [],[])
    glade = Location("The Glade", "perhaps the only truly beautiful place left, you swear you can just barely see the sun up there", "hnh_forestTheme_conceptQ.mp3", [],[],[])

    hamlet = Location("The Town Square", "The center of this once bustling hamlet now lies quiet and defeated", "hnh_forestTheme_conceptQ.mp3", [], [],[])
    store = Location("The General Store", "A dusty counter sits at the back of this one room shop, the only other furnature being a small shelf laden with baubles","hnh_forestTheme_conceptQ.mp3", [], [],[])
    sundial = Location("The Sundial", "A stone slab marked with anchient runes sits inbetween two small houses, nobody but you seems to even relize its there.","hnh_forestTheme_conceptQ.mp3", [], [],[])
    tavern = Location("The Tavern", "Perhaps the only place in the hamlet with any life still inside, you even hear the occasional chuckle coming from inside","hnh_forestTheme_conceptQ.mp3", [], [],[])
    QBoard = Location("The Message Board", "A Wooden board with a few slips of parchment halfheartedly nailed to it.","hnh_forestTheme_conceptQ.mp3", [], [],[])
    blacksmith = Location("The Smithy", "the soft glow of the embers and the rythmic ringing of the hammer on metal is almost soothing.","hnh_forestTheme_conceptQ.mp3", [], [],[])
    library = Location("The Library","Most of the books have been overrun by mold, but you may still be able to find something usefull", [], [],[])
    wagon = Location("The Merchant Wagon", "The small covered wagon smells of incense and dust.", [], [],[])
    well = Location("The Well", "you cant see the bottom of the well, but for some reason, you can hear running water below.", [], [],[])
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

    forest.adj_locations = [path, farm, cottage] #town when its done
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
    hide = item("Wolf Pelt", "No animal in this forest can keep a healthy coat, these hides are proo.f")

    cemetery.interactables = [newGrave, medGrave, ancGrave]
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

    #should always be able to run from, but always take 1 damage getting away and be forced out unless they leave the squirrel king a treat. 
    squirrels = enemy.enemy("Squirrels","You have unwittingly stepped into the glade of the Squirrel King, ChitterScritch the 4th, blessings upon them. You should leave an offering or run.", 666, 
                        [weap,weap,weap], 10, [item("King ChitterScritch's Crown"), item("Strange Gem")], "The unspeakable has happened. The squirrels have all died. How have wrought such death?", glade)

    bandit = enemy.enemy("Bandit","A thug with no conscience. It's hard to believe there are people out here acting this way, despite the Hags presence.", 8, 
                        [weap,weap,weap], 10, [item("gold purse"), item("rapier"), item("strange document")], "You can tell that the bandit realized their mistake, just as it was too late. You saw the look in their eyes as they fail to dodge your killing blow. They collapse.", outskirts)
    bandit2 = enemy.enemy("Bandit","A thug with no conscience. It's hard to believe there are people out here acting this way, despite the Hags presence.", 8, 
                        [weap,weap,weap], 10, [item("gold purse"), item("rapier"), item("strange document")], "You can tell that the bandit realized their mistake, just as it was too late. You saw the look in their eyes as they fail to dodge your killing blow. They collapse.", outskirts)

    drunkard = enemy.enemy("Drunkard"," \"You're not wise, picking a fight with me! Get 'im boys!", 3, 
                        [weap,weap,weap], 10, [item("bottle")], "Your attack connects and the bats fall harshly, splattering on the ground.", tavern)

    goblin = enemy.enemy("goblin","An angry, fiesty goblin. While not dangerous alone, goblins in numbers are problen. Where there is one, there are bound to be more.", 3, 
                        [weap,weap,weap], 10, [item("goblin bow")], "The goblin howls in pain before going limp, collapsing to the ground and twitching.", sundial)

    bat = enemy.enemy("Bats","A swarm of bats clouds your vision. The sound is incredible as wings fly past your face and around your head.", 1, 
                        [weap,weap,weap], 10, [item("bat's wings")], "Your attack connects and the bats fall harshly, splattering on the ground.", sundial)

    giant_spider = enemy.enemy("Spider","A hulking, fierce insect. This is no time to be act idley. Look out!", 15, 
                        [weap,weap,weap], 10, [item("venomous sac"), item("spider eyes"), item("giant spider mandible")], "The spider crumples into a bent, twisted shape as it hugs its wounds. It dies, shortly after", sundial)


    angry_spirit = enemy.enemy("Spirit","Suddenly a spectacularly spooky spectre swiftly swims through the air towards you. Oh my!", 3, 
                        [weap,weap,weap], 10, [item("ectoplasm"), item("ghostly blade")], "The spectre is spooped. They dissipate into nothingness, returning to the void.", tree)


    zombie = enemy.enemy("Zombie","A ghoulish fiend approaches. They limber towards you, flesh hanging from their bones. Gross!", 5, 
                        [weap,weap,weap], 10, [item("rotten body parts")], "The zombie trips towards you. As it stumbles, it catches your attack and is decapitated in an excessive display of gore.", cemetery)

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

    forest.enemeyArr = [wolf1]
    woodsS.enemyArr = [wolf2]
    woodsDeadN.enemyArr = [wolf3]

    


    

