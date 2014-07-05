'''
Created on Jun 29, 2014

@author: Thomas
'''

class Player(object):

    def __init__(self, currentLocation):
        self.currentLocation = currentLocation
        self.inventory = {}
        self.hitPoints = 100
        self.spiritualPurity = 100
        self.leftHand = None
        self.rightHand = None
        
    def increaseSpirit(self, amount):
        self.spiritualPurity += amount
        
    def decreaseSpirit(self, amount):
        self.spiritualPurity -= amount
        
    def heal(self, healNumber):
        self.hitPoints += healNumber    
        
    def takeDamage(self, damageNumber):
        self.hitPoints -= damageNumber
        
    def addItem(self, itemToAdd):
        self.inventory[itemToAdd.keywords] = itemToAdd
        
    def removeItem(self, itemToRemove):
        del self.inventory[itemToRemove.keywords]
        

class Area(object):
    
    def __init__(self, name, description):
        self.name = name
        self.description = description
        self.visited = False
        self.connectedAreas = {}
        self.features = {}
        self.itemsContained = {}
        
    def lookAt(self):
        return self.description
        
    def connect(self, area, link):
        link.setDestination(area)
        self.connectedAreas[link.keywords] = link
            
    def disconnect(self, link):
        del self.connectedAreas[link.keywords]
        link.destination = None
    
    def addItem(self, itemToAdd):
        self.itemsContained[itemToAdd.keywords] = itemToAdd
        
    def removeItem(self, itemToRemove):
        del self.itemsContained[itemToRemove.keywords]

class Item(object):
    
    def __init__(self, name, description, seenDescription, quantity, keywords):
        self.name = name
        self.description = description
        self.seenDescription = seenDescription
        self.quantity = quantity
        self.keywords = keywords
        
    def get(self, player):
        player.addItem(self)
        player.currentLocation.removeItem(self)
        return "You pick up the " + self.name
    
    def drop(self, player):
        player.removeItem(self)
        player.currentLocation.addItem(self)
        return "You drop the " + self.name
    
    def lookAt(self):
        return self.description
    
    def use(self):
        return "You cannot use that item."
    
class Weapon(Item):
    
    def __init__(self, name, description, seenDescription, quantity, keywords, damageRating, size):
        self.damageRating = damageRating
        self.size = size
        super(Weapon, self).__init__(name, description, seenDescription, quantity, keywords)
        
class RangedWeapon(Weapon):
    
    def __init__(self, name, description, seenDescription, quantity, keywords, damageRating, size, capacity):
        self.capacity = capacity
        super(RangedWeapon, self).__init__(name, description, seenDescription, quantity, keywords, damageRating)
                            #Me name es Wayne Purkle coz when I nommin' grapes day be PURKLE!!!#  Oh yes it does smeghead
class MeleeWeapon(Weapon):

    def __init__(self, name, description, seenDescription, quantity, keywords, damageRating, size, accuracy):
        self.accuracy = accuracy
        super(MeleeWeapon, self).__init__(name, description, seenDescription, quantity, keywords, damageRating)
    
class Usable(Item):
    
    def __init__(self, name, description, seenDescription, quantity, keywords, useDescription):
        self.useDescription = useDescription
        super(Usable, self).__init__(name, description, seenDescription, quantity, keywords)
        
    def use(self):
        pass
    
    def useOn(self):
        pass
        
class Key(Usable):
    
    def __init__(self, name, description, seenDescription, quantity, keywords, useDescription):
        super(Key, self).__init__(name, description, seenDescription, quantity, keywords, useDescription)
        
    def use(self):
        return "Use the key on what?"
    
    def useOn(self, recipient):
        if isinstance(recipient, Door):
            return recipient.unlock(self)
        else:
            return "You cannot use the key on that."
        
class Feature(object):
    
    def __init__(self, name, description, keywords):
        self.description = description
        self.keywords = keywords
        
    def lookAt(self):
        return self.description
    
    def use(self):
        return "You cannot do that."
    
    def useOn(self,):
        return "You cannot do that."
    
class Container(Feature):
    
    def __init__(self, description, keywords, isOpen):
        self.itemsContained = {}
        self.isOpen = isOpen
        super(Container, self).__init__(description, keywords)
        
    def addItem(self, item):
        self.itemsContained[item.keywords] = item
        
    def lookAt(self):
        desc = self.description
        if self.isOpen:
            desc += " The drawer is open. Inside you see:\n"
            for item in self.itemsContained:
                desc += item.name + "\n"
        return desc
    
    def open(self):
        if self.isOpen:
            return "The drawer is already open."
        else:
            self.isOpen = True
            desc = "The drawer opens easily. Inside you see:"
            for item in self.itemsContained:
                desc += item.name + "\n"
        return desc
        
    
    def close(self, player):
        if self.isOpen:
            return "The drawer is already closed."
        else:
            self.isOpen = False
            return "You slide the drawer closed."
            
class Link(object):
    
    def __init__(self, description, keywords):
        self.description = description
        self.destination = None
        self.keywords = keywords
        
    def lookAt(self):
        return self.description
        
    def travel(self, player):
            player.currentLocation = self.destination
            return True
            
    def setDestination(self, area):
        self.destination = area
        
    def open(self, player):
        return "You can't open that."
    
class Door(Link):
    
    def __init__(self, description, keywords, isAccessible, blockedDesc):
        self.isAccessible = isAccessible
        self.blockedDesc = blockedDesc
        super(Door, self).__init__(description, keywords)
        
    def lookAt(self):
        desc = self.description
        desc += " It seems to be "
        if self.isAccessible:
            desc += "unlocked."
        else:
            desc += "locked."
        return desc
        
    def unlock(self, usedItem):
        return "That door does not have a lock."
    
    def open(self, player):
        self.travel(player)