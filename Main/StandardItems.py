'''
Created on Jul 5, 2014

@author: Thomas
'''
import BaseClasses

class Axe(BaseClasses.MeleeWeapon):
    
    def __init__(self):
        super(Axe, self).__init__("Axe", "A long handled fire axe, probably intended for emergency use. The current situation probably qualifies.",
                                   "A fire axe.", 1, "axe,fire axe,weapon", 5, 2, 75)
        
class Knife(BaseClasses.MeleeWeapon):
    
    def __init__(self):
        super(Knife, self).__init__("Knife", "A 12 inch chefs knife. You know what they say: 'Guns are for show, knives are for pro.'",
                                   "A knife.", 1, "knife,chef knife,weapon", 3, 1, 60)

class LeatherJacket(BaseClasses.Armor):
    
    def __init__(self):
        super(LeatherJacket, self).__init__("Leather Jacket", "An old, faded brown leather jacket. I've had this for longer than I can remember.", "A faded leather jacket", 1, "armor,jacket,leather jacket", 5)

class Alchohol(BaseClasses.Drinkable):
    
    def __init__(self, name, description, seenDescription, quantity, keywords, useDescription, alcoholAmount):
        self.alcoholAmount = alcoholAmount
        super(Alchohol, self).__init__(name, description, seenDescription, quantity, keywords, useDescription)
        
    def drink(self, player):
        player.increaseIntox(self.alcoholAmount)
        player.decreaseSpirit(self.alcoholAmount / 2)
        player.removeItem(self)
        return self.useDescription
    
class Key(BaseClasses.Usable):
    
    def __init__(self, name, description, seenDescription, quantity, keywords, useDescription):
        super(Key, self).__init__(name, description, seenDescription, quantity, keywords, useDescription)
        
    def use(self):
        return "Use the key on what?"
    
    def useOn(self, recipient):
        if (isinstance(recipient, BaseClasses.Door)) or (isinstance(recipient, BaseClasses.Container)):
            return recipient.unlock(self)
        else:
            return "You cannot use the key on that."