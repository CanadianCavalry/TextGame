'''
Created on Sep 12, 2014

@author: Thomas
'''
import AreasFeatures
import StandardItems
import StandardFeatures
import UniqueNPCs

class MainLobby109(AreasFeatures.Area):
    
    def __init__(self):
        self.name = "Main Lobby"
        self.description = ["The lobby features an elegant water fountain near the entrance and a large reception desk in the middle of it. A woman standing \
in front of the reception desk appears quite agitated, and is arguing with the two receptionists on duty. Two security guards \
standing at either end of the receptionist desk look irritated with her. NORTH of you is the door to the Quarters area of the \
Residential Wing. At the SOUTH end of the lobby is the exit that leads out to the rest of the city. Two security guards in front of it.",
"The lobby features an elegant water fountain near the entrance and a large reception desk in the middle of it. Two security guards \
stand at either end of the reception desk. NORTH of you is the door to the Quarters area of the \
Residential Wing. At the SOUTH end of the lobby is the exit that leads out to the rest of the city. Two security guards are in front of it."]
        self.visited = False
        self.connectedAreas = {}
        self.features = {}
        self.itemsContained = {}
        self.enemies = {}
        self.NPCs = {}
        self.roomState = 0

