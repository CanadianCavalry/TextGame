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
        
    def increaseSpirit(self, amount):
        self.spiritualPurity += amount
        
    def decreaseSpirit(self, amount):
        self.spiritualPurity -= amount
        
    def heal(self, healNumber):
        self.hitPoints += healNumber    
        
    def takeDamage(self, damageNumber):
        self.hitPoints -= damageNumber
        
    def addItem(self, itemToAdd):
        if type(itemToAdd) == Item:
            self.inventory[itemToAdd.keywords] = itemToAdd
        
    def removeItem(self, itemToRemove):
        if type(itemToRemove) == Item:
            del self.inventory[itemToRemove.keywords]
        

class Area(object):
    
    def __init__(self, name, description):
        self.name = name
        self.description = description
        self.visited = False
        self.connectedAreas = {}
        self.features = {}
        self.itemsContained = {}
            
    def connect(self, direction, link):
        if type(link) == Link:
            self.connectedAreas[direction] = link
            
    def disconnect(self, direction):
        if type(direction) == str:
            del self.connectedAreas[direction]
    
    def addItem(self, itemToAdd):
        if type(itemToAdd) == Item:
            self.itemsContained[itemToAdd.keywords] = itemToAdd
        
    def removeItem(self, itemToRemove):
        if type(itemToRemove) != Item:
            return
        del self.itemsContained[itemToRemove.keywords]

class Feature(object):
    
    def __init__(self, name, description):
        self.name = name
        self.description = description

class Item(object):
    
    def __init__(self, name, description, seenDescription, quantity, keywords):
        self.name = name
        self.description = description
        self.seenDescription = seenDescription
        self.quantity = quantity
        self.keywords = keywords
    
    def __str__(self):
        return self.description
    
class Weapon(Item):
    
    def __init__(self, name, description, seenDescription, quantity, keywords, damageRating):
        self.damageRating = damageRating
        super(Item, self).__init__(self, name, description, seenDescription, quantity, keywords)
        
class RangedWeapon(Weapon):
    
    def __init__(self, name, description, seenDescription, quantity, keywords, damageRating, capacity):
        self.capacity = capacity
        super(Weapon, self).__init__(self, name, description, seenDescription, quantity, keywords, damageRating)
                            #Me name es Wayne Purkle coz when I nommin' grapes day be PURKLE!!!#  Oh yes it does smeghead
class MeleeWeapon(Weapon):

    def __init__(self, name, description, seenDescription, quantity, keywords, damageRating, accuracy):
        self.accuracy = accuracy
        super(Weapon, self).__init__(self, name, description, seenDescription, quantity, keywords, damageRating)
    
class Consumable(Item):
    
    def __init__(self, name, description, seenDescription, quantity, useDescription):
        self.useDescription = useDescription
        super(Consumable, self).__init__(self, name, description, seenDescription, quantity)
        
class Link(Feature):
    
    def __init__(self, name, description, target):
        self.target = target
        super(Feature, self).__init__(self, name, description)
        
    def getArea(self):
        if type(self.target) == Area:
            return self.target
        
    def getItem(self, player):
        if type(self.target) == Item:
            return self.target