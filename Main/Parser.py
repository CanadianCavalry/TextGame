'''
Created on Jun 30, 2014

@author: Thomas
'''

class Parser(object):
    
    def __init__(self):
        self.command = ""
        self.target = ""
        self.recipient = ""
        
    def addRecipient(self, position, inputArray):
        while position < len(inputArray):
            self.recipient += inputArray[position].lower() + " "
            position += 1
        self.recipient = self.recipient.strip()
        return
        
    def parse(self, inputArray):
        self.command = ""
        self.target = ""
        self.recipient = ""
        
        if len(inputArray) < 1:                          #Check for an empty input string
            return None
    
        self.command = inputArray.pop(0).lower()
        
        for word in inputArray:                         #remove unnecessary prepositions from the input
            if word in ("the","of","to","from","at","through"):
                inputArray.remove(word)
        
        if len(inputArray) >= 1:    
            for word in inputArray:
                if (self.command == "use") and (word == "on"):                          #check if the command is a two word command
                    self.command += (" " + word)
                    self.addRecipient(inputArray.index(word) + 1, inputArray)           #Start adding the rest of the words to the recipient, starting with the 
                    break                                                               #position after "on". Then end the loop so we skip the rest of the words
                self.target += word.lower() + " "
            self.target = self.target.strip()
        
        if (self.command == "go") or (self.command == "travel") or (self.command == "move") or (self.command == "walk"):
            self.command = "go"
            return
        elif (self.command == "use") or (self.command == "activate"):
            self.command = "use"
            return
        elif (self.command == "use on"):
            self.command = "use on"
            return
        elif (self.command == "get") or (self.command == "take") or (self.command == "acquire") or (self.command == "grab") or (self.command == "fetch") or (self.command == "procure") or (self.command == "attain"):
            self.command = "get"
            return
        elif (self.command == "open"):
            self.command = "open"
            return
        elif (self.command == "close"):
            self.command = "close"
            return
        elif (self.command == "inventory") or (self.command == "inv") or (self.command == "i") or (self.command == "items") or (self.command == "stuff"):
            self.command = "inventory"
            return
        elif (self.command == "look") or (self.command == "examine") or (self.command == "check") or (self.command == "scrutinize") or (self.command == "analyze") or (self.command == "inspect"):
            self.command = "look"
            return
        elif (self.command == "drop") or (self.command == "discard") or (self.command == "ditch"):
            self.command = "drop"
            return
        return
        