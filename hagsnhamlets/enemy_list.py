from enemy import *
from item import * 
from weapon import * 


weap = weapon.weapon("old bone club", 
                                   -1, 
                                    3, 
                            "swings")

#should always be able to run from, but always take 1 damage getting away and be forced out unless they leave the squirrel king a treat. 
squirrels = enemy.enemy("Swarm of Squirrels","You have unwittingly stepped into the glade of the Squirrel King, ChitterScritch the 4th, blessings upon them. You should leave an offering or run.", 666, 
                    [weap], 10, [item("King ChitterScritch's Crown"), item("Strange Gem")], "The unspeakable has happened. The squirrels have all died. How have wrought such death?", PathBehindTheCottage)

bandit = enemy.enemy("Bandit","A thug with no conscience. It's hard to believe there are people out here acting this way, despite the Hags presence.", 8, 
                    [weap], 10, [item("gold purse"), item("rapier"), item("strange document")], "You can tell that the bandit realized their mistake, just as it was too late. You saw the look in their eyes as they fail to dodge your killing blow. They collapse.", Outskirts)


drunkard = enemy.enemy("Angry Drunkard"," \"You're not wise, picking a fight with me! Get 'im boys!", 3, 
                    [weap], 10, [item("bottle")], "Your attack connects and the bats fall harshly, splattering on the ground.", Tavern, Sewers, Speakeasy)

goblin = enemy.enemy("goblin","An angry, fiesty goblin. While not dangerous alone, goblins in numbers are problen. Where there is one, there are bound to be more.", 3, 
                    [weap,weap,weap], 10, [item("goblin bow")], "The goblin howls in pain before going limp, collapsing to the ground and twitching.", GoblinCamp)

skele = enemy.enemy("Skeleton","A pile of bones, held together only by the will of the dead.", 5, 
                    [weap,weap,weap], 10, [item("bone shard")], "The Skeleton crumbles to dust.", startLocal)

bat = enemy.enemy("Swarm of Bats","A swarm of bats clouds your vision. The sound is incredible as wings fly past your face and around your head.", 1, 
                    [weap], 10, [item("bat's wings")], "Your attack connects and the bats fall harshly, splattering on the ground.", OldMine)

giant_spider = enemy.enemy("Giant Spider","A hulking, fierce insect. This is no time to be act idley. Look out!", 15, 
                    [weap], 10, [item("venomous sac"), item("spider eyes"), item("giant spider mandible")], "The spider crumples into a bent, twisted shape as it hugs its wounds. It dies, shortly after", OldMine)


angry_spirit = enemy.enemy("Angry Spirit","Suddenly a spectacularly spooky spectre swiftly swims through the air towards you. Oh my!", 3, 
                    [weap], 10, [item("ectoplasm"), item("ghostly blade")], "The spectre is spooped. They dissipate into nothingness, returning to the void.", OldMine, graveyard)


zombie = enemy.enemy("Zombie","A ghoulish fiend approaches. They limber towards you, flesh hanging from their bones. Gross!", 5, 
                    [weap], 10, [item("rotten body parts")], "The zombie trips towards you. As it stumbles, it catches your attack and is decapitated in an excessive display of gore.", graveyard)

