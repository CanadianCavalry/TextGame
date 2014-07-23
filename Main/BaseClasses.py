'''
Created on Jun 29, 2014

@author: Thomas
'''
class GameState(object):
    
    def __init__(self):
        self.player = None
        self.areaList = list()
        self.turnCount = 0
        
    def addArea(self, area):
        self.areaList.append(area)
        
    def removeArea(self, area):
        self.areaList.remove(area)
        
    def addPlayer(self, player):
        self.player = player

class Player(object):

    def __init__(self, currentLocation):
        self.currentLocation = currentLocation
        self.inventory = {}
        self.health = 100
        self.spiritualStrength = 100
        self.intoxication = 0
        self.mainHand = None
        self.offHand = None
        self.armor = None
        
    def increaseSpirit(self, amount):
        self.spiritualStrength += amount
        
    def decreaseSpirit(self, amount):
        self.spiritualStrength -= amount
        
    def heal(self, healNumber):
        self.health += healNumber    
        
    def takeDamage(self, damageNumber):
        self.health -= damageNumber
        
    def increaseIntox(self, amount):
        self.intoxication += amount
        
    def decreaseIntox(self, amount):
        self.intoxication -= amount
        
    def addItem(self, itemToAdd):
        self.inventory[itemToAdd.keywords] = itemToAdd
        
    def removeItem(self, itemToRemove):
        if self.mainHand == itemToRemove:
            self.mainHand = None
        if self.offHand == itemToRemove:
            self.offHand = None
        if self.armor == itemToRemove:
            self.armor = None
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
        desc = self.name
        desc += "\n" + self.description
        if self.itemsContained:
            desc += "\nThings you see here:"
            for item in self.itemsContained.itervalues():    #Display all the visible items
                desc += "\n" + item.seenDescription
        return desc
        
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
        
    def addFeature(self, featureToAdd):
        self.features[featureToAdd.keywords] = featureToAdd
        
    def removeFeature(self, featureToRemove):
        del self.features[featureToRemove.keywords]

class Item(object):
    
    def __init__(self, name, description, seenDescription, quantity, keywords):
        self.name = name
        self.description = description
        self.seenDescription = seenDescription
        self.quantity = quantity
        self.keywords = keywords
        
    def get(self, holder, player):
        player.addItem(self)
        holder.removeItem(self)
        return "You pick up the " + self.name + "."
    
    def drop(self, player):
        player.removeItem(self)
        player.currentLocation.addItem(self)
        return "You drop the " + self.name
    
    def lookAt(self):
        return self.description
    
    def use(self):
        return "You can't use that item."
    
    def useOn(self, recipient):
        return "You can't use that."
    
    def drink(self):
        return "You can't drink that."
    
    def equip(self):
        return "You can't equip that."

class Armor(Item):
    
    def __init__(self, name, description, seenDescription, quantity, keywords, armorRating):
        self.armorRating = armorRating
        super(Armor, self).__init__(name, description, seenDescription, quantity, keywords)
        
    def equip(self, player):
        if player.armor:
            query = "Unequip your " + player.armor.name + " and equip the " + self.name
            selection = raw_input(query)
            if (selection == "y") or (selection == "yes"):
                player.armor = self
                return "You equip the " + self.name + "."
            else:
                return "Ok then."
        else:
            player.armor = self
            return "You equip the " + self.name + "."
    
class Weapon(Item):
    
    def __init__(self, name, description, seenDescription, quantity, keywords, damageRating, size):
        self.damageRating = damageRating
        self.size = size
        super(Weapon, self).__init__(name, description, seenDescription, quantity, keywords)
        
    def equip(self, player):
        if player.mainHand == self:
            return "That is already equipped."
        if self.size == 1:
            if player.mainHand:
                return self.changeEquip(player)
            else:
                player.mainHand = self
                return "You equip the " + self.name
        else:
            if player.mainHand or player.offHand:
                return self.changeEquip(player)
            else:
                player.mainHand = self
                player.offHand = self
                return "You equip the " + self.name
        
    def changeEquip(self, player):
        if self.size == 1:
            query = "You are already holding something in your main hand. Unequip the " + player.mainHand.name + " and equip the " + self.name + "?\n"
            selection = raw_input(query).lower()
            if (selection == "y") or (selection == "yes"):
                if player.mainHand == player.offHand:
                    player.offHand = None
                player.mainHand = self
                return "You equip the " + self.name
            else:
                return "Ok then."
        else:
            query = "You need to have two free hands to equip that. Unequip the"
            if player.mainHand:
                query += " " + player.mainHand.name
                if (player.offHand) and (player.mainHand != player.offHand):
                    query += " and the"
            if (player.offHand) and (player.offHand != player.mainHand):
                query += " " + player.offHand.name
            query += ", and equip the " + self.name + "?\n"
            
            selection = raw_input(query).lower()
            if (selection == "y") or (selection == "yes"):
                player.mainHand = self
                player.offHand = self
                return "You equip the " + self.name
            else:
                return "Ok then."         
        
class RangedWeapon(Weapon):
    
    def __init__(self, name, description, seenDescription, quantity, keywords, damageRating, size, capacity):
        self.capacity = capacity
        super(RangedWeapon, self).__init__(name, description, seenDescription, quantity, keywords, damageRating)
                            #Me name es Wayne Purkle coz when I nommin' grapes day be PURKLE!!!
class MeleeWeapon(Weapon):

    def __init__(self, name, description, seenDescription, quantity, keywords, damageRating, size, accuracy):
        self.accuracy = accuracy
        super(MeleeWeapon, self).__init__(name, description, seenDescription, quantity, keywords, damageRating, size)   

class Usable(Item):
    
    def __init__(self, name, description, seenDescription, quantity, keywords, useDescription):
        self.useDescription = useDescription
        super(Usable, self).__init__(name, description, seenDescription, quantity, keywords)
        
class Drinkable(Usable):
    
    def __init__(self, name, description, seenDescription, quantity, keywords, useDescription):
        super(Drinkable, self).__init__(name, description, seenDescription, quantity, keywords, useDescription)
        
class Feature(object):
    
    def __init__(self, description, keywords):
        self.description = description
        self.keywords = keywords
        
    def lookAt(self):
        return self.description
    
    def use(self):
        return "You cannot do that."
    
    def useOn(self,):
        return "You cannot do that."
    
class Container(Feature):
    
    def __init__(self, description, keywords, isOpen, isAccessible, blockedDesc, openDesc, closeDesc):
        self.itemsContained = {}
        self.isOpen = isOpen
        self.isAccessible = isAccessible
        self.blockedDesc = blockedDesc
        self.openDesc = openDesc
        self.closeDesc = closeDesc
        super(Container, self).__init__(description, keywords)
        
    def addItem(self, item):
        self.itemsContained[item.keywords] = item
        
    def removeItem(self, item):
        del self.itemsContained[item.keywords]
        
    def lookAt(self):
        desc = self.description
        if self.isOpen:
            desc += " It is open. " 
            if self.itemsContained:
                desc += "Inside you see:\n"
                for item in self.itemsContained.itervalues():
                    desc += item.seenDescription + "\n"
        return desc
    
    def unlock(self, usedItem):
        return "It does not have a lock."
    
    def open(self, player):
        if not self.isAccessible:
            return self.blockedDesc
        elif self.isOpen:
            return "It is already open."
        else:
            self.isOpen = True
            desc = self.openDesc + " "
            if self.itemsContained:
                desc += "Inside you see:\n"
                for item in self.itemsContained.itervalues():
                    desc += item.seenDescription + "\n"
            else:
                desc += "It appears to be empty."
        return desc

    def close(self, player):
        if not self.isOpen:
            return "It is already closed."
        else:
            self.isOpen = False
            return self.closeDesc
            
class Link(object):
    
    def __init__(self, description, keywords, isAccessible, blockedDesc, travelDesc):
        self.description = description
        self.keywords = keywords
        self.isAccessible = isAccessible
        self.blockedDesc = blockedDesc
        self.travelDesc = travelDesc
        self.destination = None
        self.siblingLink = None
        
    def lookAt(self):
        return self.description
        
    def travel(self, player):
        if self.isAccessible == False:
            return self.blockedDesc
        
        desc = self.travelDesc + "\n\n"
        player.currentLocation = self.destination
        if player.currentLocation.visited == False:
            player.currentLocation.visited = True
            desc += player.currentLocation.lookAt()
        return desc
            
    def makeSibling(self, sibling):
        self.siblingLink = sibling
        sibling.siblingLink = self
        
    def setDestination(self, area):
        self.destination = area
        
    def open(self, player):
        return "You can't open that."
    
class Door(Link):
    
    def __init__(self, description, keywords, isAccessible, blockedDesc, travelDesc):
        super(Door, self).__init__(description, keywords, isAccessible, blockedDesc, travelDesc)
        
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
        return self.travel(player)
    
    def close(self, player):
        return "The door is already closed."