'''
Created on Jun 30, 2014

@author: Thomas
'''
import BaseClasses
from Main import StandardFeatures

INTRO = "You step into a small room with blue walls. There are two doors, one to the west and one to the east."

firstRoom = BaseClasses.Area("First Room", "You are standing in a blue room. There is a door to the east and a door to the north.")        #This is test code
secondRoom = BaseClasses.Area("Second Room", "You are standing in a red room. There is a door to the west. A small nightstand is sitting in the middle of the room for some reason.")
thirdRoom = BaseClasses.Area("Third Room", "You are standing in a teal room. There is a door to the south.")

rustyKey = BaseClasses.Key("rusty key", "This key has seen better days.", "An old rusty key.", 1, "key,rusty key,old key", "With some force, the key turns in the lock with a satisfying click.")
nightStand = StandardFeatures.StandardNightStand()
nightStand.addItem(rustyKey)

secondRoom.addFeature(nightStand)

link100A = StandardFeatures.StandardOpenDoor("A fairly flimsy wooden door. It's painted pink.", "east,door,east door,pink door,wood door")
link100B = StandardFeatures.StandardOpenDoor("A flimsy looking wood door. The pink paint has mostly faded.", "west,door,west door,pink door,wood door")

link101A = StandardFeatures.StandardLockedDoor("A heavy looking steel door. It's dark grey. The words 'South Side' have been carved into it.", "north,door,north door,grey door,steel door", rustyKey)
link101B = StandardFeatures.StandardLockedDoor("A heavy looking steel door. It's dark grey. The words 'North Side' have been carved into it.", "south,door,south door,grey door,steel door", rustyKey)
link101A.makeSibling(link101B)

firstRoom.connect(secondRoom, link100A)
secondRoom.connect(firstRoom, link100B)

firstRoom.connect(thirdRoom, link101A)
thirdRoom.connect(firstRoom, link101B)

player = BaseClasses.Player(firstRoom)   #Create the user and set his location