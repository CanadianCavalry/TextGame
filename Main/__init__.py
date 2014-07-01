import sys
import BaseClasses
import World
import Commands
import Parser
import Builder

print "Welcome!\nThis terrible text based game is brought to you by Dylan and Thomas."
print "Please select an option by typing it's number:"

while True:
    selection = raw_input("1 - Start a New Game\n2 - Continue your last game(currently unavailable)\n3 - Read the manual(currently unavailable\n\n")
    
    if selection == "1":
        print "Loading..."
        break
    
    elif selection == "2":
        print "Sorry, that feature is not yet available.(learn to read)"
        continue
    
    elif selection == "3":
        print "Sorry, that feature is not yet available.(learn to read)"
        continue

    else:
        print "That is not a valid option."

print Builder.INTRO

inputParser = Parser.Parser()

while True:                                         #This is the main game loop
    print ""
    userInput = raw_input()                         #Next wait for them to tell us what they want to do
    userInput = userInput.split()                   #Break apart their input into the action and the target(or object)
    
    inputParser.parse(userInput)
    
    if inputParser.command == "go":
        Commands.go(Builder.player, inputParser.target)
    elif (inputParser.command == "get"):
        Commands.get(Builder.player, inputParser.target)
    elif (inputParser.command == "inventory"):
        Commands.inventory(Builder.player)
    elif inputParser.command == "look":
        Commands.look(Builder.player, inputParser.target)
    elif inputParser.command == "drop":
        Commands.drop(Builder.player, inputParser.target)
    else:
        print "I don't understand that."