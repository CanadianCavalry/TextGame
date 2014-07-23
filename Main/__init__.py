import os
import pyglet
import BaseClasses
import StandardFeatures
import Commands
import Parser
import Builder

global SAVEGAME_FILENAME
SAVEGAME_FILENAME = 'save.json'

def newGame():
    state = BaseClasses.GameState()
    Builder.buildWorld(state)
    state.addPlayer(BaseClasses.Player(state.areaList[0]))
    return state

def main():
    window = pyglet.window.Window()
    document = pyglet.text.document.FormattedDocument("Hello there")
    textBox = pyglet.text.layout.IncrementalTextLayout(document, width = window.width - 50, height = window.height - 50, multiline = True)
    @window.event
    def on_draw():
        window.clear()
        textBox.draw()
        
    pyglet.app.run()
    
    print "Welcome!\nThis terrible text based game is brought to you by Dylan and Thomas."
    print "Please select an option by entering it's number:"
    
    while True:
        selection = raw_input("1 - Start a New Game\n2 - Continue your last game\n3 - Read the manual(currently unavailable\n\n")
        
        if selection == "1":
            print "Loading..."
            state = newGame()                       #create a new game state and build the world
            parser = Parser.Parser()                #set up the parser
            parser.loadState(state)
            print Builder.INTRO                     #display the intro
            gameLoop(parser)
        
        elif selection == "2":
            if not os.path.isfile(SAVEGAME_FILENAME):
                print "There is no existing saved game."
                continue
            else:
                print "Loading saved game..."
                state = Commands.load()
                parser = Parser.Parser()
                parser.loadState(state)
                print "Game loaded"
                gameLoop(parser)
        
        elif selection == "3":
            print "Sorry, that feature is not yet available.(learn to read)"
            continue
    
        else:
            print "That is not a valid option."
    
def gameLoop(inputParser):
    while True:                                         #This is the main game loop
        print ""
        
        userInput = raw_input()                         #Wait for the user to tell us what they want to do
        inputParser.parse(userInput)                    #hand the input over to the main parser, which calls the neccessary commands
        
        #print inputParser.command     <--- Debug print commands
        #print inputParser.target
        #print inputParser.recipient
        
main()