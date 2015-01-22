'''
Created on Jul 5, 2014

@author: Thomas
'''
import AreasFeatures

#Jacobs Room

class JacobRoomWindow(AreasFeatures.Feature):
    
    def __init__(self):
        self.description = "A large sliding window. The people who designed these rooms know what they were doing. It lets in a lot of light when it's sunny out, and helps my mood."
        self.keywords = "window,sliding window"
        
    def open(self, player):
        return "Although it's easy to open, it has a fixed screen over it. "
    
class ResidentsWingDoorsFirstFloor(AreasFeatures.Feature):
    
    def __init__(self):
        description = "All of the doors look pretty much identical. Thick wooden slabs painted a dull blue, with brass room numbers on their front. This door is closed."
        keywords = "door 101,door 102,door 103,door 105,door 107,door 108,door 109,door 110" + \
        "room 101,room 102,room 103,room 105,room 107,room 108,room 109,room 110"
        AreasFeatures.Feature.__init__(self, description, keywords)
    
    def open(self, player):
        return "The door to this room is closed. The House's is really strict about the privacy of its residents and has a 'closed door, do not disturb policy'."

class ResidentsWingDoorsSecondFloor(AreasFeatures.Feature):
    
    def __init__(self):
        description = "All of the doors look pretty much identical. Thick wooden slabs painted a dull blue, with brass room numbers on their front. This door is closed."
        keywords = "door 202,door 203,door 204,door 206,door 207,door 208,door 209,door 210" + \
        "room 202,room 203,room 204,room 206,room 207,room 208,room 209,room 210"
        AreasFeatures.Feature.__init__(self, description, keywords)
    
    def open(self, player):
        return "The door to this room is closed. The House's is really strict about the privacy of its residents and has a 'closed door, do not disturb policy'."

class ResidentsWingDoorsThirdFloor(AreasFeatures.Feature):
    
    def __init__(self):
        description = "All of the doors look pretty much identical. Thick wooden slabs painted a dull blue, with brass room numbers on their front. This door is closed."
        keywords = "door 301,door 302,door 303,door 304,door 305,door 306,door 307,door 309,door 310" + \
        "room 301,room 302,room 303,room 304,room 305,room 306,room 307,room 309,room 310"
        AreasFeatures.Feature.__init__(self, description, keywords)
    
    def open(self, player):
        return "The door to this room is closed. The House's is really strict about the privacy of its residents and has a 'closed door, do not disturb policy'."
    
class mainLobby109ExteriorDoor(AreasFeatures.Feature):
    
    def __init__(self):
        description = "A heavy pair of steel and glass security doors. The panes which cover most of each door are glazed, preventing your from seeing outside."
        keywords = "door,doors,steel door,steel door,metal door,front door,south,south door"
        AreasFeatures.Feature.__init__(self, description, keywords)
        
    def open(self, player):
        return "One of the guards approaches you as you move towards the door.\"Heading out, Jacob? I'm pretty sure you've got a couple hours of visiting time left \
for this week - just let me check your ID card and I'll make sure.\" You inform her that you might go out later, but you don't have time right now as you need to get to Father Malachi's talk."