from Main import AreasFeatures

def go(player, keyword):
    matching = list()
    for key,item in player.currentLocation.connectedAreas.iteritems():
        keyList = key.split(",")
        if keyword in keyList:
            matching.append(item)

    if len(matching) == 0:
        return "You can't go that way."
    elif len(matching) > 1:
        return "You need to be more specific"
    elif len(matching) == 1:
        try:
            return matching[0].travel(player)
        except AttributeError:
            return "I can't do that."

def use(player, keyword):
    matching = list()
    for key,item in player.inventory.iteritems():
        keyList = key.split(",")
        if keyword in keyList:
            matching.append(item)
            
    if len(matching) > 1:
        return "You need to be more specific"
        
    for key,item in player.currentLocation.itemsContained.iteritems():
        keyList = key.split(",")
        if keyword in keyList:
            matching.append(item)
            
    if len(matching) == 0:
        return "You do not have any such item."
    elif len(matching) > 1:
        return "You need to be more specific"
    elif len(matching) == 1:
        try:
            return matching[0].use()
        except AttributeError:
            return "I can't use that."
    return

def useOn(player, targetKeyword, recipientKeyword):
    matchingTarget = list()
    for key,item in player.inventory.iteritems():           #first we find the item to be used, which will be an item
        keyList = key.split(",")
        if targetKeyword in keyList:
            matchingTarget.append(item)
            
    if len(matchingTarget) > 1:
        return "You need to be more specific"
    
    for key,item in player.currentLocation.itemsContained.iteritems():          #didn't find the item in the players inventory, so we
        keyList = key.split(",")                                                #search the room for it
        if targetKeyword in keyList:
            matchingTarget.append(item)
            
    if len(matchingTarget) == 0:
        return "You do not have any such item."
    elif len(matchingTarget) > 1:
        return "You need to be more specific"
    elif len(matchingTarget) == 1:
        target = matchingTarget[0]                                            #by here we have found the item to use if it exists
        
    matching = list()
    for key,item in player.currentLocation.features.iteritems():          #now we find the recipient, which will be a feature or link
        keyList = key.split(",")
        if recipientKeyword in keyList:
            matching.append(item)
            
    if len(matching) > 1:
        return "You need to be more specific."
                                                                            
    for key,item in player.currentLocation.connectedAreas.iteritems():      #Now we search in the links list
        keyList = key.split(",")
        if recipientKeyword in keyList:
            matching.append(item)
            
    if len(matching) == 0:
        return "You do not see anything like that here."
    elif len(matching) > 1:
        return "You need to be more specific"
    elif len(matching) == 1:
        recipient = matching[0]
            
    try:
        return target.useOn(recipient)
    except AttributeError:
        return "You cannot use that in that way."

def get(player, keyword):
    matching = list()
    for key,item in player.currentLocation.itemsContained.iteritems():
        keyList = key.split(",")
        if keyword in keyList:
            matching.append(item)
            holder = player.currentLocation
            
    if len(matching) > 1:
        return "You need to be more specific"
    
    for feature in player.currentLocation.features.itervalues():
        if (isinstance(feature, AreasFeatures.Container)) and (feature.isOpen == True):
            for key,item in feature.itemsContained.iteritems():
                keyList = key.split(",")
                if keyword in keyList:
                    matching.append(item)
                    holder = feature
    
    if len(matching) == 0:
        return "You do not see any such item here."
    elif len(matching) > 1:
        return "You need to be more specific"
    elif len(matching) == 1:
        try:
            return matching[0].get(holder, player)
        except AttributeError:
            return "You can't pick that up."

def drop(player, keyword):
    matching = list()
    for key,item in player.inventory.iteritems():
        keyList = key.split(",")
        if keyword in keyList:
            matching.append(item)
            
    if len(matching) == 0:
        return "You do not have any such item."
    elif len(matching) > 1:
        return "You need to be more specific"
    elif len(matching) == 1:
        try:
            return matching[0].drop(player)
        except AttributeError:
            return "You can't drop that right now."

def attack(player, keyword):
    matching = list()
    for key,item in player.currentLocation.enemies.iteritems():
        keyList = key.split(",")
        if keyword in keyList:
            matching.append(item)
            
    if len(matching) > 1:
        return "You need to be more specific"
    
    for key,item in player.currentLocation.NPCs.iteritems():
        keyList = key.split(",")
        if keyword in keyList:
            matching.append(item)
            
    if len(matching) == 0:
        return "There is nothing like that here."
    elif len(matching) > 1:
        return "You need to be more specific"
    elif len(matching) == 1:
        try:
            return player.attack(matching[0])
        except AttributeError:
            return "I see no reason to attack that right now."

def defend(player):
    return player.defend()

def advance(player, keyword):
    matching = list()
    for key,item in player.currentLocation.enemies.iteritems():
        keyList = key.split(",")
        if keyword in keyList:
            matching.append(item)
    
    if len(matching) == 0:
        return "There is nothing like that here."
    elif len(matching) > 1:
        return "You need to be more specific"
    elif len(matching) == 1:
        try:
            return player.advance(matching[0])
        except AttributeError:
            return "That isn't an enemy."
    
def retreat(player, keyword):
    matching = list()
    for key,item in player.currentLocation.enemies.iteritems():
        keyList = key.split(",")
        if keyword in keyList:
            matching.append(item)
            
    if len(matching) == 0:
        return "There is nothing like that here."
    elif len(matching) > 1:
        return "You need to be more specific"
    elif len(matching) == 1:
        try:
            return player.retreat(matching[0])
        except AttributeError:
            return "That isn't an enemy."
            
def equip(player, keyword):
    matching = list()
    for key,item in player.inventory.iteritems():
        keyList = key.split(",")
        if keyword in keyList:
            matching.append(item)
            
    if len(matching) == 0:
        return "You do not have any such item."
    elif len(matching) > 1:
        return "You need to be more specific"
    elif len(matching) == 1:
        try:
            return matching[0].equip(player)
        except AttributeError:
            return "That isn't something you can equip."

def openThing(player, keyword):
    matching = list()
    for key,item in player.currentLocation.connectedAreas.iteritems():
        keyList = key.split(",")
        if keyword in keyList:
            matching.append(item)
            
    if len(matching) > 1:
        return "You need to be more specific"
        
    for key,item in player.currentLocation.features.iteritems():
        keyList = key.split(",")
        if keyword in keyList:
            matching.append(item)
        
    if len(matching) == 0:
        return "You do not see anything like that here."
    elif len(matching) > 1:
        return "You need to be more specific."
    elif len(matching) == 1:
        try:
            return matching[0].open(player)
        except AttributeError:
            return "You can't open that."

def closeThing(player, keyword):
    matching = list()
    for key,item in player.currentLocation.connectedAreas.iteritems():
        keyList = key.split(",")
        if keyword in keyList:
            matching.append(item)
            
    if len(matching) > 1:
        return "You need to be more specific"
        
    for key,item in player.currentLocation.features.iteritems():
        keyList = key.split(",")
        if keyword in keyList:
            matching.append(item)
        
    if len(matching) == 0:
        return "You do not see anything like that here."
    elif len(matching) > 1:
        return "You need to be more specific."
    elif len(matching) == 1:
        try:
            return matching[0].close(player)
        except AttributeError:
            return "You can't close that."

def drink(player, keyword):
    matching = list()
    for key,item in player.inventory.iteritems():
        keyList = key.split(",")
        if keyword in keyList:
            matching.append(item)
    
    if len(matching) > 1:
        return "You need to be more specific"
    
    for key,item in player.currentLocation.itemsContained.iteritems():
        keyList = key.split(",")
        if keyword in keyList:
            matching.append(item)
    
    if len(matching) == 0:
        return "You do not see any such item here."
    elif len(matching) > 1:
        return "You need to be more specific"
    elif len(matching) == 1:
        try:
            return matching[0].drink(player)
        except AttributeError:
            return "You can't drink that."

def wait(player):
    return player.wait()

def read(player, keyword):
    matching = list()
    for key,item in player.inventory.iteritems():
        keyList = key.split(",")
        if keyword in keyList:
            matching.append(item)
    
    if len(matching) > 1:
        return "You need to be more specific"
    
    for key,item in player.currentLocation.itemsContained.iteritems():
        keyList = key.split(",")
        if keyword in keyList:
            matching.append(item)
    
    if len(matching) == 0:
        return "You do not see any such item here."
    elif len(matching) > 1:
        return "You need to be more specific"
    elif len(matching) == 1:
        try:
            return matching[0].read()
        except AttributeError:
            return "That isn't something you can read."
    
def talk(player, keyword):
    matching = list()
    for key,item in player.currentLocation.NPCs.iteritems():
        keyList = key.split(",")
        if keyword in keyList:
            matching.append(item)
    
    if len(matching) > 1:
        return "You need to be more specific"
    elif len(matching) == 0:
        return "You do not see anyone like that here."
    elif len(matching) == 1:
        return matching[0].talk()
    
def ask(player, keyword, dialogueKeyword):
    matching = list()
    for key,item in player.currentLocation.NPCs.iteritems():
        keyList = key.split(",")
        if keyword in keyList:
            matching.append(item)
    
    if len(matching) > 1:
        return "You need to be more specific"
    elif len(matching) == 0:
        return "You do not see anyone like that here."
    elif len(matching) == 1:
        return matching[0].ask(dialogueKeyword)
    
def inventory(player):
    if len(player.inventory) == 0:
        return "You are not carrying anything."
    
    inventoryString = "Your current inventory:\n"
    for item in player.inventory.itervalues():
        inventoryString += item.name.title() + "\n"
    return inventoryString

def stats(player):
    healthString = "Health: "
    if player.health >= 95:
        healthString += "Perfect"
    elif player.health >= 85:
        healthString += "A few scratches"
    elif player.health >= 60:
        healthString += "Minor Injuries"
    elif player.health >= 35:
        healthString += "Major Injuries"
    elif player.health >= 10:
        healthString += "Grievous Wounds"
    elif player.health >= 1:
        healthString += "Dying"
        
    intoxicationString = "Intoxication: "
    if player.intoxication == 0:
        intoxicationString += "Sober"
    elif player.intoxication < 10:
        intoxicationString += "Tipsy"
    elif player.intoxication < 25:
        intoxicationString += "Buzzed"
    elif player.intoxication < 40:
        intoxicationString += "Drunk"
    elif player.intoxication < 60:
        intoxicationString += "Very Drunk"
    elif player.intoxication < 80:
        intoxicationString += "Hammered"
    elif player.intoxication < 90:
        intoxicationString += "Blacked Out"
    elif player.intoxication < 100:
        intoxicationString += "Near Lethal"
        
    spiritString = "Spiritual Strength: "
    if player.spiritualStrength >= 90:
        spiritString += "Saint Like"
    elif player.spiritualStrength >= 75:
        spiritString += "Pious"
    elif player.spiritualStrength >= 68:
        spiritString += "Faithful"
    elif player.spiritualStrength >= 59:
        spiritString += "Good"
    elif player.spiritualStrength >= 50:
        spiritString += "Lukewarm"
    elif player.spiritualStrength >= 40:
        spiritString += "Impure"
    elif player.spiritualStrength >= 30:
        spiritString += "Sinful"
    elif player.spiritualStrength >= 20:
        spiritString += "Evil"
    elif player.spiritualStrength >= 1:
        spiritString += "Diabolical"
    elif player.spiritualStrength == 0:
        spiritString += "Satanic"
        
    mainHandString = "Main hand: "
    if player.mainHand:
        mainHandString += player.mainHand.name
    else:
        mainHandString += "Nothing"
        
    offHandString = "Off hand: "
    if player.offHand:
        offHandString += player.offHand.name
    else:
        offHandString += "Nothing"
        
    armorString = "Armor: "
    if player.armor:
        armorString += player.armor.name
    else:
        armorString += "Nothing"
        
    statString = healthString + "\n"
    statString += intoxicationString + "\n"
    statString += spiritString + "\n"
    statString += mainHandString + "\n\n"
    statString += offHandString + "\n"
    statString += armorString + "\n"
    return statString

def look(player, keyword):
    if keyword == "":                                                       #Check if this is a general look command
        return player.currentLocation.lookAt()                               # if it is, describe the room and items in it     
    
    matching = list()
    for key,item in player.currentLocation.features.iteritems():        #Check for features that match
        keyList = key.split(",")
        if keyword in keyList:
            matching.append(item)
            
    if len(matching) > 1:
        return "You need to be more specific"
    
    for key,item in player.currentLocation.connectedAreas.iteritems():        #Check for links that match
        keyList = key.split(",")
        if keyword in keyList:
            matching.append(item)
            
    if len(matching) > 1:
        return "You need to be more specific"
    
    for key,item in player.currentLocation.itemsContained.iteritems():  #Check for items in the room that match
        keyList = key.split(",")
        if keyword in keyList:
            matching.append(item)
            
    if len(matching) > 1:
        return "You need to be more specific"
       
    for key,item in player.inventory.iteritems():               #Check for items in inventory that match
        keyList = key.split(",")
        if keyword in keyList:
            matching.append(item)
            
    if len(matching) > 1:
        return "You need to be more specific"

    for feature in player.currentLocation.features.itervalues():
        if (isinstance(feature, AreasFeatures.Container)) and (feature.isOpen == True):
            for key,item in feature.itemsContained.iteritems():
                keyList = key.split(",")
                if keyword in keyList:
                    matching.append(item)
                    
    if len(matching) > 1:
        return "You need to be more specific"
    
    for key,item in player.currentLocation.NPCs.iteritems():        #Check for features that match
        keyList = key.split(",")
        if keyword in keyList:
            matching.append(item)
            
    for key,item in player.currentLocation.enemies.iteritems():        #Check for features that match
        keyList = key.split(",")
        if keyword in keyList:
            matching.append(item)
            
    if len(matching) > 1:
        return "You need to be more specific"
    
    if len(matching) == 0:
        return "You don't see anything like that here."
    if len(matching) > 1:
        return "You need to be more specific"
    elif len(matching) == 1:
        try:
            return matching[0].lookAt()
        except AttributeError:
            return "You can't look at that. Apparently something is very wrong with this game."