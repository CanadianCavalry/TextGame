'''
Created on Jan 23, 2015

@author: CanadianCavalry
'''
import Enemies
from random import randint

class BentHost201(Enemies.Enemy):
    
    def __init__(self):
        self.busyStateDesc = ["Your tormentor is wrestling with Joe."]
        self.busyTimer = 0
        name = "Bent Host"
        description = "This huge, fat man wears a large, bloodstained apron and is looking at you with a deeply unsettling expression. You're quite certain he's possessed.."
        seenDescription = "A grinning maniac stands next to your bed, smiling at you."
        keywords = "maniac,man,bent host,host,enemy"
        maxHealth = 30
        minDamage = 5
        maxDamage = 7
        accuracy = 40
        speed = 1
        dodgeChance = 5
        armor = 0
        self.minorTortures = []
        self.majorTortures = []
        super(BentHost201, self).__init__(name, description, seenDescription, keywords, maxHealth, minDamage, maxDamage, accuracy, speed, dodgeChance, armor)
        
        self.addMinorTorture(self.minorTortureOne)
        self.addMinorTorture(self.minorTortureTwo)
        self.addMinorTorture(self.minorTortureThree)
        self.addMajorTorture(self.minorTortureOne)
        self.setDistance(1)
        self.setExorciseDialogue(["You roar out. \"GO BACK TO THE FILTH AND MISERY OF HELL!\")","\"IN THE NAME OF CHRIST JESUS, DEPART THIS MAN AT ONCE!\", you scream with righteous fury.", "\"COME OUT, WORTHLESS PARASITE!\", you roar."])
                                     
    def attack(self, player):
        if self.enemyState == 2:
            return self.basicAttack(player)
        
        elif self.enemyState == 1:
            result = self.busyStateDesc[self.busyTimer]
            self.busyTimer += 1
            if self.busyTimer == 5:
                self.setState(2)
            return result
        
        elif self.enemyState == 0:
            if player.health <= 50:
                self.enemyState += 1
                return self.attack(player)
            if player.lastAction in ["get","attack"]:
                return self.performMajorTorture(player)
            else:
                return self.performMinorTorture(player)
        
    def playerAdvances(self):
        if self.enemyState == 0:
            return "I'm still tied to this damn table."
        if self.distanceToPlayer <= 1:
            return "You are already right in front of it!"
        else:
            self.distanceToPlayer -= 1
            return "You advance on the " + self.name, True
        
    def playerRetreats(self):
        if self.enemyState == 0:
            return "I'm still tied to this damn table."
        if self.distanceToPlayer >= 3:
            return "Your back is to the wall."
        else:
            self.distanceToPlayer -= 1
            return "You retreat from the " + self.name, True
            
    def performMinorTorture(self, player):
        return self.minorTortures[randint(0,len(self.minorTortures) - 1)](player)
    
    def performMajorTorture(self, player):
        return self.majorTortures[randint(0,len(self.minorTortures) - 1)](player)
    
    def addMinorTorture(self, method):
        self.minorTortures.append(method)
        
    def addMajorTorture(self, method):
        self.majorTortures.append(method)
        
    def removeMinorTorture(self, index):
        del self.minorTortures[index]
    
    def removeMajorTorture(self, index):
        del self.majorTortures[index]
    
    def execute(self, player):
        player.takeDamage(100)
        return "The demon writhes in pain and screams out, \"STOP TORTURING US, SON OF MAN!\". However it quickly recovers. \"FUCK YOUR FUCKING GOD!\", he roars at you. \
He falls upon you like a hurricane, completely enraged. \"YOU DIE HERE, FALSE PRIEST!\" he roars. As he wraps his meaty hands around your throat and begins to choke you, you can feel him kneeing you in the groin again and again and biting you so hard he actually takes chunks out of your body. Mercifully, you die quickly."
        
    def minorTortureOne(self, player):
        player.takeDamage(10)
        return "Using the pliers, the maniac pulls off one of your fingernails, smiling at you the entire time."
    
    def minorTortureTwo(self, player):
        player.takeDamage(10)
        return "You scream as the man carves a deep slice on your torso with the knife. The sound makes him giggle."
    
    def minorTortureThree(self, player):
        player.takeDamage(10)
        return "The lunatic slams you across the skull with the trephine."
    
    def majorTortureOne(self, player):
        player.takeDamage(20)
        return "He sticks one of the fish hooks into you, then rips it out, taking out a large chunk of flesh."
    
    def majorTortureTwo(self, player):
        player.takeDamage(20)
        return "You howl in agony as he wraps the serrated metal wire around your torso and pulls with all his might!"
    
    def exorciseAttempt(self, player):
        if self.enemyState == 0:
            resultString = "You take a ragged breath and muster what faith you can.\n" + self.exorciseDialogue[randint(0, len(self.exorciseDialogue) - 1)] + "\n"
            resultString += self.execute(player)
            return resultString
        
        resultString = "You draw upon your faith to banish the demon. You yell out:\n" + self.exorciseDialogue[randint(0, len(self.exorciseDialogue) - 1)] + "\n"
        
        hitChance = self.baseExorciseChance
        hitChance += (player.spirit - 50)
        attackRoll = randint(0, 100)
        if attackRoll <= hitChance:
            resultString += self.takeExorcise()
            return resultString
        else:
            resultString += "It doesn't seem to have any effect."
            return resultString