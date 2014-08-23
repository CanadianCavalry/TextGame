'''
Created on Jul 5, 2014

@author: Thomas
'''
import Items
import AreasFeatures

class Axe(Items.MeleeWeapon):
    
    def __init__(self):
        super(Axe, self).__init__("Axe", "A long handled fire axe, probably intended for emergency use. The current situation probably qualifies.",
                                   "A fire axe.", 1, "axe,fire axe,weapon", 11, 15, 2, 75)
        
class Knife(Items.MeleeWeapon):
    
    def __init__(self):
        super(Knife, self).__init__("Knife", "A 12 inch chefs knife. You know what they say: 'Guns are for show, knives are for pro.'",
                                   "A knife.", 1, "knife,chef knife,weapon", 9, 14, 1, 65)
class Handgun(Items.RangedWeapon):
    
    def __init__(self):
        super(Handgun, self).__init__("Handgun", "A small calibur handgun. It holds 10 rounds.", "A small handgun",
                                      1, "gun,handgun,pistol", 20, 30, 1, 60, 10, 10)

class LeatherJacket(Items.Armor):
    
    def __init__(self):
        super(LeatherJacket, self).__init__("Leather Jacket", "An old, faded brown leather jacket. I've had this for longer than I can remember.", "A faded leather jacket", 1, "armor,jacket,leather jacket", 5)

class Alchohol(Items.Drinkable):
    
    def __init__(self, name, description, seenDescription, quantity, keywords, useDescription, alcoholAmount):
        self.alcoholAmount = alcoholAmount
        super(Alchohol, self).__init__(name, description, seenDescription, quantity, keywords, useDescription)
        
    def drink(self, player):
        player.increaseIntox(self.alcoholAmount)
        player.decreaseSpirit(self.alcoholAmount / 2)
        player.removeItem(self)
        return self.useDescription,True
    
class Key(Items.Usable):
    
    def use(self):
        return "Use the key on what?"
    
    def useOn(self, recipient):
        if (isinstance(recipient, AreasFeatures.Door)) or (isinstance(recipient, AreasFeatures.Container)):
            return recipient.unlock(self)
        else:
            return "You cannot use the key on that."
        
class Note(Items.Readable):
    
    def __init__(self, name, description, seenDescription, quantity, keywords, contents):
        self.contents = contents
        super(Note, self).__init__(name, description, seenDescription, quantity, keywords)
    
    def read(self):
        return self.contents,True
    
class Book(Items.Readable):
    
    def __init__(self, name, description, seenDescription, quantity, keywords):
        self.pages = []
        super(Book, self).__init__(name, description, seenDescription, quantity, keywords)
        
    def read(self):
        for page in self.pages:
            print page.contents
            raw_input("Press Enter to continue...")
        return "That's the last page.",True
            
    def addPage(self, page):
        self.pages.append(page)
        
class Page(object):
    
    def __init__(self,contents):
        self.contents = contents