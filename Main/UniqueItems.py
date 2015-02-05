'''
Created on Jan 23, 2015

@author: CanadianCavalry
'''
import Items

class Scalpal(Items.MeleeWeapon):
    
    def __init__(self):
        super(Scalpal, self).__init__("Scalpel", "I could almost reach it if I stretched...", 
                                      "A scalpal is lying on the ground.", "The scalpel is closest to me...", 1, "scalpal", 5, 11, 1, 60, 15, 0)
        self.makeInAccessible("You suddenly jerk forward and try to grab the scalpel, but the man grabs your hand and stops you. \"No, no exorcist!\" he says. \That's my toy, not yours!\"")