from item import item

class weapon(item):
    def __init__(self, name, dmg, toHit, type, desc="tempDesc", pickup=True,):
        super().__init__(name, desc=desc, pickup=pickup)
        self.dmg = dmg
        self.toHit = toHit
        self.type = type
    


    #WEAPONS
    forest_weapons = [


    ]

    old_mines_weapons = [ 

    ]

    sewers_weapons = [

    ]

        
    #ARMOR

    forest_armor = [ 

    ]

    old_mines_armor = [ 

    ]

    sewers_armor = [ 

    ]

