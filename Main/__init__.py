import os
import pyglet
import Commands
import Parser
import Builder
from Main import AreasFeatures
import Enemies
import jsonpickle

global state
global SAVEGAME_FILENAME
SAVEGAME_FILENAME = 'save.json'
STANDARD_TEXT_ATTRIBUTES = {'color':(255,0,0,1), 'background_color':(255,255,255,1)}

class Player(object):

    def __init__(self, currentLocation):
        self.currentLocation = currentLocation
        self.inventory = {}
        self.health = 100
        self.spiritualStrength = 100
        self.intoxication = 0
        self.mainHand = None
        self.offHand = None
        self.dodgeChance = 0
        self.armor = None
        self.isDefending = False

    def increaseSpirit(self, amount):
        self.spiritualStrength += amount
        
    def decreaseSpirit(self, amount):
        self.spiritualStrength -= amount
        
    def heal(self, healNumber):
        self.health += healNumber    
        
    def takeDamage(self, damageNumber):
        self.health -= damageNumber
        if self.health <= 0:
            print "You have died. Returning to the main menu...\n"
            mainMenu()
        return "You are " + self.getCondition() + "."
        
    def increaseIntox(self, amount):
        self.intoxication += amount
        self.setDodgeChance(self.calcDodgeChance())
        
    def decreaseIntox(self, amount):
        self.intoxication -= amount
        self.setDodgeChance(self.calcDodgeChance())
        
    def setDodgeChance(self, dodgeChance):
        self.dodgeChance = dodgeChance
        
    def addItem(self, itemToAdd):
        self.inventory[itemToAdd.keywords] = itemToAdd
        
    def removeItem(self, itemToRemove):
        if self.mainHand == itemToRemove:
            self.mainHand = None
        if self.offHand == itemToRemove:
            self.offHand = None
        if self.armor == itemToRemove:
            self.armor = None
        del self.inventory[itemToRemove.keywords]
        
    def attack(self, enemy):
        try:
            return self.mainHand.attack(enemy)
        except AttributeError:
            return "You are not holding a weapon."
        
    def defend(self):
        self.isDefending = True
        return "You take a defensive stance.", True
        
    def advance(self, enemy):
        if enemy.distanceToPlayer > 1:
            enemy.distanceToPlayer -= 1
            resultString = "You move towards the" + enemy.name, True
        else:
            resultString = "You are already right in front of the enemy."
            
        return resultString
    
    def retreat(self, enemy):
        if enemy.distanceToPlayer < 3:
            enemy.distanceToPlayer += 1
            resultString = "You move away from the" + enemy.name, True
        else:
            resultString = "You are already as far away as you can get."
            
        return resultString
        
    def wait(self):
        return "You wait.", True
        
    def getCondition(self):
        healthString = ""
        if self.health >= 95:
            healthString += "Unhurt"
        elif self.health >= 85:
            healthString += "Bruised and Scratched"
        elif self.health >= 60:
            healthString += "Slightly Injured"
        elif self.health >= 35:
            healthString += "Seriously Injured"
        elif self.health >= 10:
            healthString += "Grievously Wounded"
        elif self.health >= 1:
            healthString += "Dying"
        
        return healthString    

    def calcDodgeChance(self):
        if self.intoxication > 75:
            dodgeChance = -25
        elif self.intoxication > 60:
            dodgeChance = -20
        elif self.intoxication > 40:
            dodgeChance = -15
        elif self.intoxication > 25:
            dodgeChance = -10
        elif self.intoxication > 0:
            dodgeChance = 5
        else:
            dodgeChance = -5
            
        return dodgeChance
        
    def beginTurn(self):
        self.isDefending = False
        
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

def newGame():
    state = GameState()
    Builder.buildWorld(state)
    state.addPlayer(Player(state.areaList[0]))
    return state

def mainMenu():
    
    print "Welcome!\nThis terrible text based game is brought to you by Dylan Kelk and Thomas Protheroe."
    print "Please select an option by entering it's number:"
    
    while True:
        selection = raw_input("1 - Start a New Game\n2 - Continue your last game\n3 - Read the manual(currently unavailable)\n\n")
        
        if selection == "1":
            print "Loading..."
            state = newGame()                       #create a new game state and build the world
            parser = Parser.Parser()                #set up the parser
            parser.loadState(state)
            print Builder.INTRO                     #display the intro
            gameLoop(parser, state)
        
        elif selection == "2":
            if not os.path.isfile(SAVEGAME_FILENAME):
                print "There is no existing saved game."
                continue
            else:
                print "Loading saved game..."
                state = load()
                parser = Parser.Parser()
                parser.loadState(state)
                print "Game loaded"
                gameLoop(parser, state)
        
        elif selection == "3":
            print "Sorry, that feature is not yet available.(learn to read)"
            continue
    
        else:
            print "That is not a valid option."
    
def gameLoop(inputParser, state):
    while True:                                         #This is the main game loop
        print ""
        
        userInput = raw_input()                         #Wait for the user to tell us what they want to do
        
        turnResult = inputParser.parse(userInput)                    #hand the input over to the main parser, which calls the necessary commands
        
        try:
            resultString,turnPassed = turnResult
        except ValueError:
            resultString = turnResult
            turnPassed = False
            
        print resultString
        if turnPassed:
            print enemyAction(state.player)
            state.player.beginTurn()
        
        #print inputParser.command     <--- Debug print commands
        #print inputParser.target
        #print inputParser.recipient
        
def enemyAction(player):
    resultString = ""
    for enemy in player.currentLocation.enemies.itervalues():
        resultString += enemy.takeAction(player) + "\n"
    return resultString

def save(state):
    with open(SAVEGAME_FILENAME, 'w') as savegame:
        savegame.write(jsonpickle.encode(state))
    return "Game saved."
    
def load():
    with open(SAVEGAME_FILENAME, 'r') as savegame:
        state = jsonpickle.decode(savegame.read())
        return state
    
def quit():
    choice = raw_input("Are you sure? (Y/N)")
    choice = choice.lower()
    if (choice == "y") or (choice == "yes"):
        mainMenu()
    return "OK then."
    
mainMenu()