'''
Created on Aug 3, 2014

@author: Thomas
'''
from random import randint

class Enemy(object):
    
    def __init__(self, name, description, seenDescription, keywords, maxHealth, minDamage, maxDamage, accuracy, speed, dodgeChance, armor):
        self.name = name
        self.description = description
        self.seenDescription = seenDescription
        self.keywords = keywords
        self.maxHealth = maxHealth
        self.minDamage = minDamage
        self.maxDamage = maxDamage
        self.accuracy = accuracy
        self.speed = speed
        self.dodgeChance = dodgeChance
        self.armor = armor
        self.health = maxHealth
        self.distanceToPlayer = 3
        self.currentLocation = None
        self.actionTimer = 1
        self.stunnedTimer = 0
        self.chasing = False
        
    def takeAction(self, player):
        if self.actionTimer == 1:
            if self.distanceToPlayer == 1:
                result = self.attack(player)
                self.actionTimer = self.speed
            else:
                result = self.advance()
                self.actionTimer = self.speed
        else:
            self.actionTimer -= 1
            result = "It does nothing."
        
        return result

    def attack(self, player):
        resultString = "It attacks you.\n"
        hitChance = self.accuracy - player.dodgeChance
        if player.isDefending:
            hitChance -= 20
            
        attackRoll = randint(0,100)
        if attackRoll <= hitChance:
            damageAmount = randint(self.minDamage + 1, self.maxDamage)
            resultString += "It hits you! "
            resultString += player.takeDamage(damageAmount)
        else:
            resultString += "It misses."
            
        return resultString
        
    def advance(self):
        if self.distanceToPlayer > 1:
            self.distanceToPlayer -= 1
            return "It moves towards you.\n" + self.getDistance()
        return "It does nothing."
    
    def retreat(self):
        if self.distanceToPlayer < 3:
            self.distanceToPlayer += 1
            return "It moves away from you.\n" + self.getDistance()
        return "It does nothing."
        
    def takeHit(self, weapon):
        damageAmount = (randint(weapon.minDamage, weapon.maxDamage)) - (self.armor)
        resultString = "You hit it! "
        resultString += self.takeDamage(damageAmount)
        return resultString
        
    def takeDamage(self, damageAmount):
        damageAmount -= self.armor
        self.health -= damageAmount
        if self.health <= 0:
            return self.kill()
        else:
            return self.getCondition()
        
    def kill(self):
        self.currentLocation.killEnemy(self)
        return "It falls to the ground dead."
        
    def setLocation(self, location):
        self.currentLocation = location
    
    def getCondition(self):
        if self.health == self.maxHealth:
            return "It looks unharmed."
        elif self.health > (self.maxHealth * 0.75):
            return "It appears to be slightly injured."
        elif self.health > (self.maxHealth * 0.50):
            return "It appears to be injured."
        elif self.health > (self.maxHealth * 0.25):
            return "It appears to be severely injured."
        elif self.health > (0):
            return "It appears to be nearly dead."
    
    def getDistance(self):
        distanceDescription = ""
        if self.distanceToPlayer == 1:
            distanceDescription = "It is right in front of you."
        if self.distanceToPlayer == 2:
            distanceDescription = "It is a few meters away."
        if self.distanceToPlayer == 3:
            distanceDescription = "It is across the room."
        return distanceDescription
    
    def lookAt(self):
        lookResult = self.description
        lookResult += "\n" + self.getCondition()
        lookResult += "\n" + self.getDistance()
        return lookResult

class TestDemon(Enemy):
    
    def __init__(self):
        name = "Test Demon"
        description = "A slavering, red skinned, bat winged demon. Pretty standard stuff actually."
        seenDescription = "You see a Winged Demon glaring at you menacingly."
        keywords = "demon,red demon,winged demon"
        maxHealth = 50
        minDamage = 9
        maxDamage = 14
        accuracy = 60
        speed = 1
        dodgeChance = 5
        armor = 0
        super(TestDemon, self).__init__(name, description, seenDescription, keywords, maxHealth, minDamage, maxDamage, accuracy, speed, dodgeChance, armor)