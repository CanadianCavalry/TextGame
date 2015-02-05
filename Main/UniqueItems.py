'''
Created on Jan 23, 2015

@author: CanadianCavalry
'''
import Items

class Scalpal201(Items.MeleeWeapon):
    
    def __init__(self):
        super(Scalpal201, self).__init__("Scalpel", "I could almost reach it if I stretched...", 
                                      "A scalpal is lying on the ground.", "The scalpel is closest to me...", 1, "scalpal", 5, 11, 1, 60, 15, 0)
        self.makeInAccessible("You suddenly jerk forward and try to grab the scalpel, but the man grabs your hand and stops you. \"No, no exorcist!\" he says. \That's my toy, not yours!\"")
        
class TortureTools201(Items.Item):
    
   def __init__(self):
        name = "Tools"
        description = "The tools are rusty and smeared with dark stains."
        seenDescription = "The collection of implements includes pliers, fish hooks, a long serrated wire, a trephine, and a scalpel, which is almost within reach."
        initDesc = "The collection of implements includes pliers, fish hooks, a long serrated wire, a trephine, and a scalpel, which is almost within reach."
        quantity = 1
        keywords = "tools,tool,tray,pliers,hooks,fish hook,wire,serreted wire,trephine"
        Items.Item.__init__(self, name, description, seenDescription, initDesc, quantity, keywords)