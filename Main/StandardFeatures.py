'''
Created on Jun 29, 2014

@author: Thomas
'''
import BaseClasses

class StandardOpenDoor(BaseClasses.Door):
    
    def __init__(self, description, keywords):
        super(StandardOpenDoor, self).__init__(description, keywords, True, "")
        
class StandardLockedDoor(BaseClasses.Door):
    
    def __init__(self, description, keywords, itemToOpen, blockedDesc):
        self.itemToOpen = itemToOpen
        self.siblingLink = None
        super(StandardLockedDoor, self).__init__(description, keywords, False, blockedDesc)
        
    def makeSibling(self, sibling):
        self.siblingLink = sibling
        sibling.siblingLink = self
        
    def unlock(self, usedItem):
        if usedItem == self.itemToOpen:
            self.isAccessible = True
            return usedItem.useDescription
        else:    
            return "The key does not appear to work for this door."
                
    def travel(self, player):
        if self.isAccessible == False:
            print self.blockedDesc
            return False
        
        player.currentLocation = self.destination
        return True
    
class StandardNightStand(BaseClasses.Container):
    
    def __init__(self, isOpen):
        description = "A small wooden nightstand. The top is littered with a manner of small items such as pens, books and bits of paper."
        keywords = "night stand,nightstand,drawer"
        super(StandardNightStand, self).__init__(description, keywords, isOpen)
        
    