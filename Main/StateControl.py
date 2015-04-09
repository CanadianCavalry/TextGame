'''
Created on Sep 5, 2014

@author: Thomas
'''
import sys
import Builder
import jsonpickle

global SAVEGAME_FILENAME
SAVEGAME_FILENAME = 'save.json'

class GameState(object):
    
    def __init__(self):
        self.player = None
        self.areaList = list()
        self.turnCount = 0
        
    def addArea(self, area):
        self.areaList.append(area)
        
    def removeArea(self, area):
        self.areaList.remove(area)
        
    def addPlayer(self, player):
        self.player = player
        self.player.currentLocation = self.areaList[0]

def newGameState(player):
    state = GameState()
    Builder.buildWorld(state)
    state.addPlayer(player)
    return state

def newSimulationState(player):
    state = GameState()
    Builder.buildCombatSimulator(state)
    state.addPlayer(player)
    return state



# def mainMenu():
#     while True:
#         selection = raw_input("1 - Start a New Game\n2 - Continue your last game\n3 - Start the Combat Simulator\n\n")
#         
#         if selection == "1":
#             print "Loading..."
#             state = newGameState()                       #create a new game state and build the world
#             parser = Parser.Parser()                #set up the parser
#             parser.loadState(state)
#             window = GUI.Window(parser, state)      #start the GUI
#             pyglet.app.run()
#         
#         elif selection == "2":
#             if not os.path.isfile(SAVEGAME_FILENAME):
#                 print "There is no existing saved game."
#                 continue
#             else:
#                 print "Loading saved game..."
#                 state = loadState()
#                 parser = Parser.Parser()
#                 parser.loadState(state)
#                 print "Game loaded"
#                 window = GUI.Window(parser, state)
#                 pyglet.app.run()
#         
#         elif selection == "3":
#             print "Loading..."
#             state = newSimulationState()                 #create a new game state and build the simulator
#             parser = Parser.Parser()                #set up the parser
#             parser.loadState(state)                 #loadState the newly built game state
#             window = GUI.Window(parser, state)      #start the GUI
#             pyglet.app.run()
#     
#         else:
#             print "That is not a valid option."

def save(state):
    with open(SAVEGAME_FILENAME, 'w') as savegame:
        savegame.write(jsonpickle.encode(state))
    return "Game saved."
    
def loadState(player=None):
    with open(SAVEGAME_FILENAME, 'r') as savegame:
        state = jsonpickle.decode(savegame.read())
        return state
    
def quit():
    sys.exit()