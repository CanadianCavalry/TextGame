import os
import pyglet
import Commands
import Parser
import Builder
import AreasFeatures
import Enemies
import jsonpickle
import GUI
import StateControl

class Player(object):

    def __init__(self):
        self.currentLocation = None
        self.inventory = {}
        self.health = 100
        self.spiritualStrength = 100
        self.intoxication = 0
        self.mainHand = None
        self.offHand = None
        self.dodgeChance = 0
        self.armor = None
        self.isDefending = False

    def increaseSpirit(self, amount):
        self.spiritualStrength += amount
        
    def decreaseSpirit(self, amount):
        self.spiritualStrength -= amount
        
    def heal(self, healNumber):
        self.health += healNumber    
        
    def takeDamage(self, damageNumber):
        self.health -= damageNumber
        return "You are " + self.getCondition() + "."
        
    def increaseIntox(self, amount):
        self.intoxication += amount
        self.setDodgeChance(self.calcDodgeChance())
        
    def decreaseIntox(self, amount):
        self.intoxication -= amount
        self.setDodgeChance(self.calcDodgeChance())
        
    def setDodgeChance(self, dodgeChance):
        self.dodgeChance = dodgeChance
        
    def addItem(self, itemToAdd):
        for item in self.inventory:
            if item != itemToAdd:
                continue
            
            item.quantity += 1
            return
            
        self.inventory[itemToAdd.keywords] = itemToAdd
        return
        
    def removeItem(self, itemToRemove):
        if self.mainHand == itemToRemove:
            self.mainHand = None
        if self.offHand == itemToRemove:
            self.offHand = None
        if self.armor == itemToRemove:
            self.armor = None
            
        for item in self.inventory:
            if item != itemToRemove:
                continue
            
            item.quantity -= 1
            if item.quantity < 1:
                del self.inventory[itemToRemove.keywords]
            return
            
        del self.inventory[itemToRemove.keywords]
        return
        
    def attack(self, enemy):
        try:
            return self.mainHand.attack(enemy)
        except AttributeError:
            return "You are not holding a weapon."
        
    def shoot(self, enemy):
        try:
            return self.mainHand.shoot(enemy)
        except AttributeError:
            return "You are not holding a gun."
        
    def reload(self):
        if self.mainHand:
            try:
                return self.mainHand.reload(self)
            except AttributeError:
                return "You are not holding a gun."
        else:
            return "You are not holding anything."
            
        
    def defend(self):
        self.isDefending = True
        return "You take a defensive stance.", True
        
    def advance(self, enemy):
        if enemy.distanceToPlayer > 1:
            enemy.distanceToPlayer -= 1
            resultString = "You move towards the" + enemy.name, True
        else:
            resultString = "You are already right in front of the enemy."
            
        return resultString
    
    def retreat(self, enemy):
        if enemy.distanceToPlayer < 3:
            enemy.distanceToPlayer += 1
            resultString = "You move away from the" + enemy.name, True
        else:
            resultString = "You are already as far away as you can get."
            
        return resultString
        
    def wait(self):
        return "You wait.", True
        
    def getCondition(self):
        healthString = ""
        if self.health >= 95:
            healthString += "Unhurt"
        elif self.health >= 85:
            healthString += "Bruised and Scratched"
        elif self.health >= 60:
            healthString += "Slightly Injured"
        elif self.health >= 35:
            healthString += "Seriously Injured"
        elif self.health >= 10:
            healthString += "Grievously Wounded"
        elif self.health >= 1:
            healthString += "Dying"
        
        return healthString    

    def getSpirit(self):
        spiritString = ""
        if self.spiritualStrength >= 90:
            spiritString += "Saint Like"
        elif self.spiritualStrength >= 75:
            spiritString += "Pious"
        elif self.spiritualStrength >= 68:
            spiritString += "Faithful"
        elif self.spiritualStrength >= 59:
            spiritString += "Good"
        elif self.spiritualStrength >= 50:
            spiritString += "Lukewarm"
        elif self.spiritualStrength >= 40:
            spiritString += "Impure"
        elif self.spiritualStrength >= 30:
            spiritString += "Sinful"
        elif self.spiritualStrength >= 20:
            spiritString += "Evil"
        elif self.spiritualStrength >= 1:
            spiritString += "Diabolical"
        elif self.spiritualStrength == 0:
            spiritString += "Satanic"
            
        return spiritString

    def getIntoxication(self):
        intoxicationString = ""
        if self.intoxication == 0:
            intoxicationString += "Sober"
        elif self.intoxication < 10:
            intoxicationString += "Tipsy"
        elif self.intoxication < 25:
            intoxicationString += "Buzzed"
        elif self.intoxication < 40:
            intoxicationString += "Drunk"
        elif self.intoxication < 60:
            intoxicationString += "Very Drunk"
        elif self.intoxication < 80:
            intoxicationString += "Hammered"
        elif self.intoxication < 90:
            intoxicationString += "Blacked Out"
        elif self.intoxication < 100:
            intoxicationString += "Near Lethal"
            
        return intoxicationString

    def calcDodgeChance(self):
        return self.dodgeChance
        
    def beginTurn(self):
        self.isDefending = False
        
def launch():
    window = GUI.Window(Player())      #start the GUI
    pyglet.app.run()
    
launch()