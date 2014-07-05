'''
Created on Jun 29, 2014

@author: Thomas
'''
import BaseClasses

class StandardOpenDoor(BaseClasses.Door):
    
    def __init__(self, description, keywords):
        super(StandardOpenDoor, self).__init__(description, keywords, True, "", "You open the door and step through.")

        
class StandardLockedDoor(BaseClasses.Door):
    
    def __init__(self, description, keywords, itemToOpen):
        self.itemToOpen = itemToOpen
        super(StandardLockedDoor, self).__init__(description, keywords, False, "The door is locked. It won't budge.", "You open the door and step through.")
        
    def unlock(self, usedItem):
        if usedItem == self.itemToOpen:
            self.isAccessible = True
            return usedItem.useDescription
        else:    
            return "The key does not appear to work for this door."
    
class StandardNightStand(BaseClasses.Container):
    
    def __init__(self):
        description = "A small wooden nightstand. The top is littered with a manner of small items such as pens, books and bits of paper."
        keywords = "night stand,nightstand,drawer"
        super(StandardNightStand, self).__init__(description, keywords, False, True, "")