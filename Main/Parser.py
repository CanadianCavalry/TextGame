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
        
        if self.command == "go":
            self.command = "go"
            return
        elif (self.command == "get") or (self.command == "take"):
            self.command = "get"
            return
        elif (self.command == "inventory") or (self.command == "inv") or (self.command == "i"):
            self.command = "inventory"
            return
        elif (self.command == "look") or (self.command == "examine"):
            self.command = "look"
            return
        elif (self.command == "drop"):
            self.command = "drop"
            return
        return
        