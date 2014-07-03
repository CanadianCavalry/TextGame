'''
Created on Jun 30, 2014

@author: Thomas
'''
import BaseClasses
import World

INTRO = "You step into a small room with blue walls. There are two doors, one to the west and one to the east."

firstRoom = BaseClasses.Area("First Room", "You are standing in a blue room. There is a door to the east and a door to the west.")        #This is test code
secondRoom = BaseClasses.Area("Second Room", "You are standing in a red room. There is a door to the east.")
thirdRoom = BaseClasses.Area("Third Room", "You are standing in a teal room. There is a door to the west.")

secondRoom.addItem(BaseClasses.Item("rusty key", "This key has seen better days.", "An old rusty key lying on the ground.", 1, "key,rusty key,old key"))

firstRoom.connect("west",BaseClasses.Link("west door", "A fairly flimsy wooden door. It's painted pink", "door,west door, pink door, wood door",secondRoom))
secondRoom.connect("east",BaseClasses.Link(firstRoom))

firstRoom.connect("east",BaseClasses.Link(thirdRoom))
thirdRoom.connect("west",BaseClasses.Link(firstRoom))

player = BaseClasses.Player(firstRoom)   #Create the user and set his location