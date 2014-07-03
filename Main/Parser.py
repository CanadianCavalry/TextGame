'''
Created on Jun 30, 2014

@author: Thomas
'''

class Parser(object):
    
    def __init__(self):
        self.command = ""
        self.target = ""
        
    def parse(self, inputArray):
        if len(inputArray) < 1:                          #Check for an empty string
            return None
    
        self.command = inputArray.pop(0).lower()
        self.target = ""
        
        for word in inputArray:                         #remove unnecessary prepositions from the input
            if word in ("the","of","to","from","at"):
                inputArray.remove(word)
        
        if len(inputArray) >= 1:    
            for line in inputArray:
                self.target += line.lower() + " "
            self.target = self.target.strip()
        
        if (self.command == "go") or (self.command == "travel") or (self.command == "move") or (self.command == "walk"):
            self.command = "go"
            return
        elif (self.command == "get") or (self.command == "take") or (self.command == "acquire") or (self.command == "grab") or (self.command == "fetch") or (self.command == "procure") or (self.command == "attain"):
            self.command = "get"
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
        