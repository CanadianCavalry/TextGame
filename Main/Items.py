'''
Created on Aug 22, 2014

@author: Thomas
'''
import random
import pyglet

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
        return "You pick up the " + self.name + ".",True
    
    def drop(self, player):
        player.removeItem(self)
        player.currentLocation.addItem(self)
        return "You drop the " + self.name,True
    
    def destroy(self, player):
        player.removeItem(self)
    
    def lookAt(self):
        return self.description

class Armor(Item):
    
    def __init__(self, name, description, seenDescription, quantity, keywords, armorRating):
        self.armorRating = armorRating
        super(Armor, self).__init__(name, description, seenDescription, quantity, keywords)
        
    def equip(self, player):
        if player.armor == self:
            return "You are already wearing that."
        
        player.armor = self
        return "You equip the " + self.name + ".",True

        
#This is the older equip command which uses raw_input - Not compatible with the current GUI
#     def equip(self, player):
#         if player.armor:
#             query = "Unequip your " + player.armor.name + " and equip the " + self.name
#             selection = raw_input(query)
#             if (selection == "y") or (selection == "yes"):
#                 player.armor = self
#                 return "You equip the " + self.name + ".",True
#             else:
#                 return "Ok then."
#         else:
#             player.armor = self
#             return "You equip the " + self.name + ".",True
    
class Weapon(Item):
    
    def __init__(self, name, description, seenDescription, quantity, keywords, minDamage, maxDamage, size, critChance):
        self.minDamage = minDamage
        self.maxDamage = maxDamage
        self.critChance = critChance
        self.size = size
        super(Weapon, self).__init__(name, description, seenDescription, quantity, keywords)
        
    def equip(self, player):
        if player.mainHand == self:
            return "That is already equipped."
        if self.size == 1:
            if player.mainHand == player.offHand:
                player.offHand = None
            player.mainHand = self
            return "You equip the " + self.name,True
        elif self.size == 2:
            player.mainHand = self
            player.offHand = self
            return "You equip the " + self.name,True
        
#This is the older equip command which uses raw_input - Not compatible with the current GUI
#     def equip(self, player):
#         if player.mainHand == self:
#             return "That is already equipped."
#         if self.size == 1:
#             if player.mainHand:
#                 return self.changeEquip(player)
#             else:
#                 player.mainHand = self
#                 return "You equip the " + self.name,True
#         else:
#             if player.mainHand or player.offHand:
#                 return self.changeEquip(player)
#             else:
#                 player.mainHand = self
#                 player.offHand = self
#                 return "You equip the " + self.name,True
#                 
#
#     def changeEquip(self, player):
#         if self.size == 1:
#             query = "You are already holding something in your main hand. Unequip the " + player.mainHand.name + " and equip the " + self.name + "?\n"
#             selection = raw_input(query).lower()
#             if (selection == "y") or (selection == "yes"):
#                 if player.mainHand == player.offHand:
#                     player.offHand = None
#                 player.mainHand = self
#                 return "You equip the " + self.name,True
#             else:
#                 return "Ok then."
#         else:
#             query = "You need to have two free hands to equip that. Unequip the"
#             if player.mainHand:
#                 query += " " + player.mainHand.name
#                 if (player.offHand) and (player.mainHand != player.offHand):
#                     query += " and the"
#             if (player.offHand) and (player.offHand != player.mainHand):
#                 query += " " + player.offHand.name
#             query += ", and equip the " + self.name + "?\n"
#             
#             selection = raw_input(query).lower()
#             if (selection == "y") or (selection == "yes"):
#                 player.mainHand = self
#                 player.offHand = self
#                 return "You equip the " + self.name,True
#             else:
#                 return "Ok then."         
        
    def attack(self):
        pass
        
class RangedWeapon(Weapon):
    
    def __init__(self, name, description, seenDescription, quantity, keywords, minDamage, maxDamage, size, accuracy, capacity, ammoRemaining, fireSound, critChance=10):
        self.accuracy = accuracy
        self.capacity = capacity
        self.ammoRemaining = ammoRemaining
        self.fireSound = fireSound
        self.rangeMod = [0,5,10]
        super(RangedWeapon, self).__init__(name, description, seenDescription, quantity, keywords, minDamage, maxDamage, size, critChance)
                            #Me name es Wayne Purkle coz when I nommin' grapes day be PURKLE!!!
    def attack(self, enemy, player, attackType):
        if attackType == "heavy":
            return "You are not holding a melee weapon."
        
        if self.ammoRemaining <= 0:
            return "You are out of ammo!"
        
        source = pyglet.media.load(self.fireSound, streaming=False)
        source.play()
        
        self.ammoRemaining -= 1
        resultString = "You open fire."
        hitChance = self.accuracy
        hitChance -= enemy.dodgeChance
        
        if enemy.distanceToPlayer == 1:
            hitChance -= self.rangeMod[0]
        elif enemy.distanceToPlayer == 2:
            hitChance -= self.rangeMod[1]
        elif enemy.distanceToPlayer == 3:
            hitChance -= self.rangeMod[2]
            
        if player.intoxication > 75:
            hitChance -= 25
        elif player.intoxication > 60:
            hitChance -= 15
        elif player.intoxication > 40:
            hitChance -= 10
        elif player.intoxication > 25:
            hitChance -= 5
        elif player.intoxication > 10:
            hitChance += 8
        elif player.intoxication > 1:
            hitChance += 5
        elif player.intoxication > 60:
            hitChance -= 5
            
        if enemy.stunnedTimer > 0:
            hitChance += 10
            
        if hitChance < 5:
            hitChance = 5
            
        attackRoll = random.randint(0, 100)
        if attackRoll <= hitChance:
            resultString += "\n" + enemy.takeHit(self, "ranged")
        else:
            resultString += "\nYou miss!"
        return resultString, True
    
    
    def shoot(self, enemy, player):
        return self.attack(enemy, player)
    
    def reload(self, player):
        for item in player.inventory.itervalues():
            try:
                weaponType = item.weaponType
            except AttributeError:
                continue
            
            if self.name == weaponType:
                self.ammoRemaining = self.capacity
                item.destroy(player)
                return "You reload the " + self.name + ".",True
            
        return "You don't have any ammo."
        
    def lookAt(self):
        resultString = self.description + "\n"
        resultString += "It has " + str(self.ammoRemaining) + " shots remaining."
        return resultString
        
class MeleeWeapon(Weapon):

    def __init__(self, name, description, seenDescription, quantity, keywords, minDamage, maxDamage, size, accuracy, critChance=10, stunLength=2):
        self.accuracy = accuracy
        self.stunLength = stunLength
        super(MeleeWeapon, self).__init__(name, description, seenDescription, quantity, keywords, minDamage, maxDamage, size, critChance)   

    def attack(self, enemy, player, attackType):
        resultString = "You swing your weapon."
        
        hitChance = self.accuracy
        hitChance -= enemy.dodgeChance
        
        if player.intoxication > 75:
            hitChance -= 25
        elif player.intoxication > 60:
            hitChance -= 15
        elif player.intoxication > 40:
            hitChance -= 10
        elif player.intoxication > 25:
            hitChance -= 5
        elif player.intoxication > 10:
            hitChance += 8
        elif player.intoxication > 1:
            hitChance += 5
        elif player.intoxication > 60:
            hitChance -= 5
            
        if attackType == "heavy":
            hitChance -= 10
        
        if enemy.stunnedTimer > 0:
            hitChance += 15
        
        if hitChance < 5:
            hitChance = 5
        attackRoll = random.randint(0, 100)
        if attackRoll <= hitChance:
            resultString += "\n" + enemy.takeHit(self, attackType)
        else:
            resultString += "\nYou miss!"
        return resultString, True

class Ammo(Item):
    
    def __init__(self, name, description, seenDescription, quantity, keywords, weaponType):
        self.weaponType = weaponType
        super(Ammo, self).__init__(name, description, seenDescription, quantity, keywords)
    
class Usable(Item):
    
    def __init__(self, name, description, seenDescription, quantity, keywords, useDescription):
        self.useDescription = useDescription
        super(Usable, self).__init__(name, description, seenDescription, quantity, keywords)
        
class Drinkable(Usable):
    
    def __init__(self, name, description, seenDescription, quantity, keywords, useDescription):
        super(Drinkable, self).__init__(name, description, seenDescription, quantity, keywords, useDescription)
        
class Readable(Item):
    
    def __init__(self, name, description, seenDescription, quantity, keywords):
        super(Readable, self).__init__(name, description, seenDescription, quantity, keywords)
            
    def read(self):
        pass
        