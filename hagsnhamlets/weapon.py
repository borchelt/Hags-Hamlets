from item import *

class weapon(item):
    def __init__(self, name, dmg, toHit, type, desc="tempDesc", pickup=True,):
        super().__init__(name, desc=desc, pickup=pickup)
        self.dmg = dmg
        self.toHit = toHit
        self.type = type