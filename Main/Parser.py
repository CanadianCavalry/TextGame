'''
Created on Jun 30, 2014

@author: Thomas
'''
import Commands

class Parser(object):
    
    def __init__(self):
        self.command = ""
        self.target = ""
        self.recipient = ""
        self.state = None
        
    def loadState(self, state):
        self.state = state
        
    def addRecipient(self, position, inputArray):
        while position < len(inputArray):
            self.recipient += inputArray[position].lower() + " "
            position += 1
        self.recipient = self.recipient.strip()
        return
        
    def parse(self, inputString):
        inputString = inputString.lower()
        inputArray = inputString.split()                 #Break apart their input into the action and the target(or object)
        
        self.command = ""
        self.target = ""
        self.recipient = ""
        
        for word in inputArray:                         #remove unnecessary prepositions from the input
            if word in ("the","of","to","from","at","through"):
                inputArray.remove(word)
        
        if len(inputArray) < 1:                          #Check for an empty input string
            return None
    
        self.command = inputArray.pop(0)
        
        if len(inputArray) >= 1:    
            for word in inputArray:
                if (self.command == "use") and (word == "on"):                          #check if the command is a two word command
                    self.command += (" " + word)
                    self.addRecipient(inputArray.index(word) + 1, inputArray)           #Start adding the rest of the words to the recipient, starting with the 
                    break                                                               #position after "on". Then end the loop so we skip the rest of the words
                self.target += word + " "
            self.target = self.target.strip()
        
        if (self.command == "go") or (self.command == "travel") or (self.command == "move") or (self.command == "walk"):
            Commands.go(self.state.player, self.target)
        elif (self.command == "use") or (self.command == "activate"):
            Commands.use(self.state.player, self.target)
        elif (self.command == "use on"):
            Commands.useOn(self.state.player, self.target, self.recipient)
        elif (self.command == "get") or (self.command == "take") or (self.command == "acquire") or (self.command == "grab") or (self.command == "fetch") or (self.command == "procure") or (self.command == "attain"):
            Commands.get(self.state.player, self.target)
        elif (self.command == "drop") or (self.command == "discard") or (self.command == "ditch"):
            Commands.drop(self.state.player, self.target)
        elif (self.command == "equip"):
            Commands.equip(self.state.player, self.target)
        elif (self.command == "open"):
            Commands.openThing(self.state.player, self.target)
        elif (self.command == "close"):
            Commands.closeThing(self.state.player, self.target)
        elif (self.command == "drink"):
            Commands.drink(self.state.player, self.target)
        elif (self.command == "look") or (self.command == "examine") or (self.command == "check") or (self.command == "scrutinize") or (self.command == "analyze") or (self.command == "inspect"):
            Commands.look(self.state.player, self.target)
        elif (self.command == "inventory") or (self.command == "inv") or (self.command == "i") or (self.command == "items") or (self.command == "stuff"):
            Commands.inventory(self.state.player)
        elif (self.command == "char") or (self.command == "stats"):
            Commands.stats(self.state.player)
        elif (self.command == "save"):
            Commands.save(self.state)
        else:
            print "I don't understand that."
        return
        