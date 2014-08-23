'''
Created on Jul 5, 2014

@author: Thomas
'''
from Main import AreasFeatures

#Jacobs Room

class JacobRoomWindow(AreasFeatures.Feature):
    
    def __init__(self):
        self.description = "A large sliding window. The people who designed these rooms know what they were doing. It lets in a lot of light when it's sunny out, and helps my mood."
        self.keywords = "window,sliding window"
        
    def open(self):
        return "Although it's easy to open, it has a fixed screen over it. "