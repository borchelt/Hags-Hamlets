from prints import printr
from prints import prints
from map import *
import random
class nameFetch():
    def woods_title_ascii(self):

        prints("_____ _            __    __                _     ")
        prints("/__   | |__   ___  / / /\ \ \___   ___   __| |___ ")
        prints("  / /\| '_ \ / _ \ \ \/  \/ / _ \ / _ \ / _` / __|")
        prints(" / /  | | | |  __/  \  /\  | (_) | (_) | (_| \__ \ ")
        prints(" \/   |_| |_|\___|   \/  \/ \___/ \___/ \__,_|___/")

    def hamlet_title_ascii(self):
                                                        
        prints(" _____ _                                  _      _   ")
        prints("/__   | |__   ___    /\  /\__ _ _ __ ___ | | ___| |_ ")
        prints("  / /\| '_ \ / _ \  / /_/ / _` | '_ ` _ \| |/ _ | __|")
        prints(" / /  | | | |  __/ / __  | (_| | | | | | | |  __| |_ ")
        prints(" \/   |_| |_|\___| \/ /_/ \__,_|_| |_| |_|_|\___|\__|")
                                                            
    def well_title_ascii(self):
            
        prints("_____ _            __    __     _ _ ")
        prints("/__   | |__   ___  / / /\ \ \___| | |")
        prints("  / /\| '_ \ / _ \ \ \/  \/ / _ | | |")
        prints(" / /  | | | |  __/  \  /\  |  __| | |")
        prints("\/   |_| |_|\___|   \/  \/ \___|_|_|")

    def tavern_title_ascii(self):
            
        prints(" _____ _            _____                           ")
        prints("/__   | |__   ___  /__   \__ ___   _____ _ __ _ __  ")
        prints(" / /\| '_ \ / _ \   / /\/ _` \ \ / / _ | '__| '_ \ ")
        prints("/ /  | | | |  __/  / / | (_| |\ V |  __| |  | | | |")
        prints("\/   |_| |_|\___|  \/   \__,_| \_/ \___|_|  |_| |_|")
                                                        

    def library_title_ascii(self):
            
        prints("_____ _              __ _ _                          ")
        prints("/__   | |__   ___    / /(_| |__  _ __ __ _ _ __ _   _ ")
        prints(" / /\| '_ \ / _ \  / / | | '_ \| '__/ _` | '__| | | |")
        prints(" / /  | | | |  __/ / /__| | |_) | | | (_| | |  | |_| |")
        prints(" \/   |_| |_|\___| \____|_|_.__/|_|  \__,_|_|   \__, |")
        prints("                                                |___/")
                                                    

    def travel_merch_title_ascii(self):
                                                        
        prints("                     _ _                                    _                 _         ")
        prints("/__   \_ __ __ ___   _____| (_)_ __   __ _    /\/\   ___ _ __ ___| |__   __ _ _ __ | |_ ")
        prints("  / /\| '__/ _` \ \ / / _ | | | '_ \ / _` |  /    \ / _ | '__/ __| '_ \ / _` | '_ \| __|")
        prints(" / /  | | | (_| |\ V |  __| | | | | | (_| | / /\/\ |  __| | | (__| | | | (_| | | | | |_ ")
        prints(" \/   |_|  \__,_| \_/ \___|_|_|_| |_|\__, | \/    \/\___|_|  \___|_| |_|\__,_|_| |_|\__|")
        prints("                                    |___/                                               ")


    def blacksmith_title_ascii(self):
            
        prints(" _____ _              ___ _            _                  _ _   _     ")
        prints("/__   | |__   ___    / __| | __ _  ___| | _____ _ __ ___ (_| |_| |__  ")
        prints("  / /\| '_ \ / _ \  /__\/| |/ _` |/ __| |/ / __| '_ ` _ \| | __| '_ \ ")
        prints(" / /  | | | |  __/ / \/  | | (_| | (__|   <\__ | | | | | | | |_| | | |")
        prints(" \/   |_| |_|\___| \_____|_|\__,_|\___|_|\_|___|_| |_| |_|_|\__|_| |_|")
                                                                            

    def sundial_title_ascii(self):
            
        prints(" _____ _            __                 _ _       _ ")
        prints("/__   | |__   ___  / _\_   _ _ __   __| (_) __ _| |")
        prints("  / /\| '_ \ / _ \ \ \| | | | '_ \ / _` | |/ _` | |")
        prints("/ /  | | | |  __/ _\ | |_| | | | | (_| | | (_| | |")
        prints(" \/   |_| |_|\___| \__/\__,_|_| |_|\__,_|_|\__,_|_|")
                                                    

    def forest_title_ascii(self):
            
        prints("_____ _              ___                  _   ")
        prints("/__   | |__   ___    / _____  _ __ ___ ___| |_ ")
        prints(" / /\| '_ \ / _ \  / _\/ _ \| '__/ _ / __| __|")
        prints("/ /  | | | |  __/ / / | (_) | | |  __\__ | |_ ")
        prints(" \/   |_| |_|\___| \/   \___/|_|  \___|___/\__|")


    def deep_woods_title_ascii(self):
        prints("   ___                  __    __                _     ")
        prints("  /   \___  ___ _ __   / / /\ \ \___   ___   __| |___ ")
        prints(" / /\ / _ \/ _ | '_ \  \ \/  \/ / _ \ / _ \ / _` / __|")
        prints("/ /_/|  __|  __| |_) |  \  /\  | (_) | (_) | (_| \__ \ ")
        prints("/___,' \___|\___| .__/    \/  \/ \___/ \___/ \__,_|___/")
        prints("                |_|                                    ")

    def abandoned_cottage_title_ascii(self):
        prints("  _   _                     _                      _     ___      _   _                   ")
        prints("  /_\ | |__   __ _ _ __   __| | ___  _ __   ___  __| |   / __\___ | |_| |_ __ _  __ _  ___ ")
        prints(" //_\\| '_ \ / _` | '_ \ / _` |/ _ \| '_ \ / _ \/ _` |  / /  / _ \| __| __/ _` |/ _` |/ _ \ ")
        prints("/  _  | |_) | (_| | | | | (_| | (_) | | | |  __| (_| | / /__| (_) | |_| || (_| | (_| |  __/")
        prints("\_/ \_|_.__/ \__,_|_| |_|\__,_|\___/|_| |_|\___|\__,_| \____/\___/ \__|\__\__,_|\__, |\___|")
        prints("                                                                               |___/       ")

                                                
    def clearing_title_ascii(self):
        prints("_____ _              ___ _                 _             ")
        prints("/__   | |__   ___    / __| | ___  __ _ _ __(_)_ __   __ _ ")
        prints(" / /\| '_ \ / _ \  / /  | |/ _ \/ _` | '__| | '_ \ / _` |")
        prints("/ /  | | | |  __/ / /___| |  __| (_| | |  | | | | | (_| |")
        prints("\/   |_| |_|\___| \____/|_|\___|\__,_|_|  |_|_| |_|\__, |")
        prints("                                                   |___/ ")


    def hunters_camp_title_ascii(self):
        prints("                  _            _        ___                     ") 
        prints(" /\  /\_   _ _ __ | |_ ___ _ __( ___    / __\__ _ _ __ ___  _ __  ")
        prints("/ /_/ | | | | '_ \| __/ _ | '__|/ __|  / /  / _` | '_ ` _ \| '_ \ ")
        prints("/ __  /| |_| | | | | ||  __| |   \__ \ / /__| (_| | | | | | | |_) |")
        prints(" /_/  \__,_|_| |_|\__\___|_|   |___/ \____/\__,_|_| |_| |_| .__/   ")
        prints("                                                            |_|    ")


    def old_mine_title_ascii(self):
            
        prints("_____ _              ___ _     _          _            ")
        prints("/__   | |__   ___    /___| | __| |   /\/\ (_)_ __   ___ ")
        prints(" / /\| '_ \ / _ \  //  /| |/ _` |  /    \| | '_ \ / _ \ ")
        prints("/ /  | | | |  __/ / \_//| | (_| | / /\/\ | | | | |  __/")
        prints("\/   |_| |_|\___| \___/ |_|\__,_| \/    \|_|_| |_|\___|")
                                                            

    def sewers_title_ascii(self):
            
        prints("_____ _            __                            ")
        prints("/__   | |__   ___  / _\ _____      _____ _ __ ___ ")
        prints(" / /\| '_ \ / _ \ \ \ / _ \ \ /\ / / _ | '__/ __|")
        prints("/ /  | | | |  __/ _\ |  __/\ V  V |  __| |  \__ \ ")
        prints("\/   |_| |_|\___| \__/\___| \_/\_/ \___|_|  |___/")
                                                        

    def thieves_den_title_ascii(self):
        prints("  ___                    __   _____ _     _                    ")
        prints(" /   \___ _ __     ___  / _| /__   | |__ (_) _____   _____ ___ ")
        prints("/ /\ / _ | '_ \   / _ \| |_    / /\| '_ \| |/ _ \ \ / / _ / __|")
        prints("/ /_/|  __| | | | | (_) |  _|  / /  | | | | |  __/\ V |  __\__ \ ")
        prints("/___,' \___|_| |_|  \___/|_|    \/   |_| |_|_|\___| \_/ \___|___/")


    def speakeasy_title_ascii(self):
            
        prints(" _____ _            __                  _                        ")
        prints("/__   | |__   ___  / _\_ __   ___  __ _| | _____  __ _ ___ _   _ ")
        prints(" / /\| '_ \ / _ \ \ \| '_ \ / _ \/ _` | |/ / _ \/ _` / __| | | |")
        prints(" / /  | | | |  __/ _\ | |_) |  __| (_| |   |  __| (_| \__ | |_| |")
        prints("\/   |_| |_|\___| \__| .__/ \___|\__,_|_|\_\___|\__,_|___/\__, |")
        prints("                     |_|                                  |___/ ")

    def rat_kings_nest_title_ascii(self):
                            
        prints(" _____ _              __       _           _             _          __         _   ")
        prints("/__   | |__   ___    /__\ __ _| |_    /\ /(_)_ __   __ _( ___    /\ \ \___ ___| |_ ")
        prints(" / /\| '_ \ / _ \  / \/// _` | __|  / //_| | '_ \ / _` |/ __|  /  \/ / _ / __| __|")
        prints("/ /  | | | |  __/ / _  | (_| | |_  / __ \| | | | | (_| |\__ \ / /\  |  __\__ | |_ ")
        prints("\/   |_| |_|\___| \/ \_/\__,_|\__| \/  \/|_|_| |_|\__, ||___/ \_\ \/ \___|___/\__|")
        prints("                                                  |___/                           ")
                                                

    def outskirts_title_ascii(self):
            
        prints("_____ _              ___       _       _    _      _       ")
        prints("__   | |__   ___    /___\_   _| |_ ___| | _(_)_ __| |_ ___ ")
        prints(" / /\| '_ \ / _ \  //  /| | | | __/ __| |/ | | '__| __/ __|")
        prints("/ /  | | | |  __/ / \_//| |_| | |_\__ |   <| | |  | |_\__ \ ")
        prints("\/   |_| |_|\___| \___/  \__,_|\__|___|_|\_|_|_|   \__|___/")
                                                                
    def graveyard_title_ascii(self):
            
        prints("_____ _              ___                                         _ ")
        prints("/__   | |__   ___    / _ \_ __ __ ___   _____ _   _  __ _ _ __ __| |")
        prints(" / /\| '_ \ / _ \  / /_\| '__/ _` \ \ / / _ | | | |/ _` | '__/ _` |")
        prints("/ /  | | | |  __/ / /_\\| | | (_| |\ V |  __| |_| | (_| | | | (_| |")
        prints(" \/   |_| |_|\___| \____/|_|  \__,_| \_/ \___|\__, |\__,_|_|  \__,_|")
        prints("                                             |___/                 ")

    def hangman_tree_title_ascii(self):
        prints("                                             _      _____               ")
        prints(" /\  /\__ _ _ __   __ _ _ __ ___   __ _ _ __( ___  /__   \_ __ ___  ___ ")
        prints(" / /_/ / _` | '_ \ / _` | '_ ` _ \ / _` | '_ |/ __|   / /\| '__/ _ \/ _ \ ")
        prints("/ __  | (_| | | | | (_| | | | | | | (_| | | | \__ \  / /  | | |  __|  __/")
        prints("\/ /_/ \__,_|_| |_|\__, |_| |_| |_|\__,_|_| |_|___/  \/   |_|  \___|\___|")
        prints("                  |___/                                                 ")

    def printName(self, name, local):
        if(name == "The Clearing"):
            self.clearing_title_ascii()
            map.populate_enemies(0, local, map.skel1)
        elif name == "The Forest":
            self.forest_title_ascii()
            map.populate_enemies(2, local, map.wolf1)
        elif name == "The Northern Woods" or name == "The Northwestern Woods" or name == "The Southern Woods" or name == "The Southeastern Woods" or name == "The Southwestern Woods" or name =="The Southeastern-er Woods" or name == "The Northeastern Woods":
            self.woods_title_ascii()
            map.populate_enemies(2, local, map.skel1)
        elif name == "The Graveyard":
            self.graveyard_title_ascii()
            map.populate_enemies(2, local, map.skel1)
        elif name == "The Outskirts":
            self.outskirts_title_ascii()
            map.populate_enemies(1, local, map.bandit)
        elif name == "The Old Gate":
            self.outskirts_title_ascii()
            map.populate_enemies(0, local, map.skel1)
        elif name == "The Hangman's Tree":
            self.hangman_tree_title_ascii()
            map.populate_enemies(2, local, map.angry_spirit)
        elif name == "The Waterfall":
            self.woods_title_ascii()
            map.populate_enemies(0, local, map.skel1)
        elif name == "The Cove":
            self.woods_title_ascii()
            map.populate_enemies(1, local, map.skel1)
        elif name == "The Twisted Path":
            self.woods_title_ascii()
            map.populate_enemies(0, local, map.skel1)
        elif name == "The Hunter's Camp":
            self.hunters_camp_title_ascii()
            map.populate_enemies(0, local, map.skel1)
        elif name == "The Old Cottage":
            self.abandoned_cottage_title_ascii()
            map.populate_enemies(0, local, map.skel1)
        elif name == "Old Mines: Entrance" or name == "Old Mines: First Chamber" or name =="Old Mines: Center Chamber" or name =="Old Mines" or name =="Old Mines: Supply Cache" or name =="Old Mines: The Forge" or name =="Old Mines: The Armory":
            self.old_mine_title_ascii()
            if random.randint(0,1) == 0:
                map.populate_enemies(2, local, map.bat)
            else:
                map.populate_enemies(2, local, map.goblin)
        elif name ==  "Old Mines: Webbed Path" or name == "Spiders' Lair":
            self.old_mine_title_ascii()
            map.populate_enemies(3, local, map.hatchling_spider)
        else:
            self.hamlet_title_ascii