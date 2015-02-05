'''
Created on Jan 23, 2015

@author: CanadianCavalry
'''
import Enemies

class BentHost201(Enemies.Enemy):
    
    def __init__(self):
        name = "Bent Host"
        description = "This huge, fat man wears a large, bloodstained apron and is looking at you with a deeply unsettling expression. You're quite certain he's possessed.."
        seenDescription = "A grinning maniac stands next to your bed, smiling at you."
        keywords = "demon,red demon,winged demon"
        maxHealth = 30
        minDamage = 5
        maxDamage = 7
        accuracy = 40
        speed = 1
        dodgeChance = 5
        armor = 0
        super(BentHost201, self).__init__(name, description, seenDescription, keywords, maxHealth, minDamage, maxDamage, accuracy, speed, dodgeChance, armor)

    