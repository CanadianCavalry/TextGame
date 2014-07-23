import jsonpickle
import Main
import BaseClasses

def go(player, keyword):
    matching = list()
    for key,item in player.currentLocation.connectedAreas.iteritems():
        keyList = key.split(",")
        if keyword in keyList:
            matching.append(item)

    if len(matching) == 0:
        print "You can't go that way."
    elif len(matching) > 1:
        print "You need to be more specific"
    elif len(matching) == 1:
        print matching[0].travel(player)
    return

def use(player, keyword):
    matching = list()
    for key,item in player.inventory.iteritems():
        keyList = key.split(",")
        if keyword in keyList:
            matching.append(item)
            
    if len(matching) > 1:
        print "You need to be more specific"
        return    
        
    for key,item in player.currentLocation.itemsContained.iteritems():
        keyList = key.split(",")
        if keyword in keyList:
            matching.append(item)
            
    if len(matching) == 0:
        print "You do not have any such item."
    elif len(matching) > 1:
        print "You need to be more specific"
    elif len(matching) == 1:
        print matching[0].use()
    return

def useOn(player, targetKeyword, recipientKeyword):
    matchingTarget = list()
    for key,item in player.inventory.iteritems():           #first we find the item to be used, which will be an item
        keyList = key.split(",")
        if targetKeyword in keyList:
            matchingTarget.append(item)
            
    if len(matchingTarget) > 1:
        print "You need to be more specific"
        return
    
    for key,item in player.currentLocation.itemsContained.iteritems():          #didn't find the item in the players inventory, so we
        keyList = key.split(",")                                                #search the room for it
        if targetKeyword in keyList:
            matchingTarget.append(item)
            
    if len(matchingTarget) == 0:
        print "You do not have any such item."
        return
    elif len(matchingTarget) > 1:
        print "You need to be more specific"
        return
    elif len(matchingTarget) == 1:
        target = matchingTarget[0]                                            #by here we have found the item to use if it exists
        
    matching = list()
    for key,item in player.currentLocation.features.iteritems():          #now we find the recipient, which will be a feature or link
        keyList = key.split(",")
        if recipientKeyword in keyList:
            matching.append(item)
            
    if len(matching) > 1:
        print "You need to be more specific."
        return
                                                                            
    for key,item in player.currentLocation.connectedAreas.iteritems():      #Now we search in the links list
        keyList = key.split(",")
        if recipientKeyword in keyList:
            matching.append(item)
            
    if len(matching) == 0:
        print "You do not see anything like that here."
        return
    elif len(matching) > 1:
        print "You need to be more specific"
        return
    elif len(matching) == 1:
        recipient = matching[0]
            
    print target.useOn(recipient)
    return

def get(player, keyword):
    matching = list()
    for key,item in player.currentLocation.itemsContained.iteritems():
        keyList = key.split(",")
        if keyword in keyList:
            matching.append(item)
            holder = player.currentLocation
            
    if len(matching) > 1:
        print "You need to be more specific"
        return
    
    for feature in player.currentLocation.features.itervalues():
        if (isinstance(feature, BaseClasses.Container)) and (feature.isOpen == True):
            for key,item in feature.itemsContained.iteritems():
                keyList = key.split(",")
                if keyword in keyList:
                    matching.append(item)
                    holder = feature
    
    if len(matching) == 0:
        print "You do not see any such item here."
    elif len(matching) > 1:
        print "You need to be more specific"
    elif len(matching) == 1:
        print matching[0].get(holder, player)
    return

def drop(player, keyword):
    matching = list()
    for key,item in player.inventory.iteritems():
        keyList = key.split(",")
        if keyword in keyList:
            matching.append(item)
            
    if len(matching) == 0:
        print "You do not have any such item."
    elif len(matching) > 1:
        print "You need to be more specific"
    elif len(matching) == 1:
        print matching[0].drop(player)
    return

def equip(player, keyword):
    matching = list()
    for key,item in player.inventory.iteritems():
        keyList = key.split(",")
        if keyword in keyList:
            matching.append(item)
            
    if len(matching) == 0:
        print "You do not have any such item."
    elif len(matching) > 1:
        print "You need to be more specific"
    elif len(matching) == 1:
        print matching[0].equip(player)
    return

def openThing(player, keyword):
    matching = list()
    for key,item in player.currentLocation.connectedAreas.iteritems():
        keyList = key.split(",")
        if keyword in keyList:
            matching.append(item)
            
    if len(matching) > 1:
        print "You need to be more specific"
        return
        
    for key,item in player.currentLocation.features.iteritems():
        keyList = key.split(",")
        if keyword in keyList:
            matching.append(item)
        
    if len(matching) == 0:
        print "You do not see anything like that here."
    elif len(matching) > 1:
        print "You need to be more specific."
    elif len(matching) == 1:
        print matching[0].open(player)
    return

def closeThing(player, keyword):
    matching = list()
    for key,item in player.currentLocation.connectedAreas.iteritems():
        keyList = key.split(",")
        if keyword in keyList:
            matching.append(item)
            
    if len(matching) > 1:
        print "You need to be more specific"
        return
        
    for key,item in player.currentLocation.features.iteritems():
        keyList = key.split(",")
        if keyword in keyList:
            matching.append(item)
        
    if len(matching) == 0:
        print "You do not see anything like that here."
    elif len(matching) > 1:
        print "You need to be more specific."
    elif len(matching) == 1:
        print matching[0].close(player)
    return

def drink(player, keyword):
    matching = list()
    for key,item in player.inventory.iteritems():
        keyList = key.split(",")
        if keyword in keyList:
            matching.append(item)
    
    if len(matching) > 1:
        print "You need to be more specific"
        return
    
    for key,item in player.currentLocation.itemsContained.iteritems():
        keyList = key.split(",")
        if keyword in keyList:
            matching.append(item)
    
    if len(matching) == 0:
        print "You do not see any such item here."
    elif len(matching) > 1:
        print "You need to be more specific"
    elif len(matching) == 1:
        print matching[0].drink(player)
    return

def inventory(player):
    if len(player.inventory) == 0:
        print "You are not carrying anything."
        return
    
    print "Your current inventory:\n"
    for item in player.inventory.itervalues():
        print item.name.title()
    return

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
        
    print healthString
    print intoxicationString
    print spiritString + "\n"
    print mainHandString
    print offHandString

def look(player, keyword):
    if keyword == "":                                                       #Check if this is a general look command
        print player.currentLocation.lookAt()                               # if it is, describe the room and items in it
        return     
    
    matching = list()
    for key,item in player.currentLocation.features.iteritems():        #Check for features that match
        keyList = key.split(",")
        if keyword in keyList:
            matching.append(item)
            
    if len(matching) > 1:
        print "You need to be more specific"
        return
    
    for key,item in player.currentLocation.connectedAreas.iteritems():        #Check for links that match
        keyList = key.split(",")
        if keyword in keyList:
            matching.append(item)
            
    if len(matching) > 1:
        print "You need to be more specific"
        return
    
    for key,item in player.currentLocation.itemsContained.iteritems():  #Check for items in the room that match
        keyList = key.split(",")
        if keyword in keyList:
            matching.append(item)
            
    if len(matching) > 1:
        print "You need to be more specific"
        return
       
    for key,item in player.inventory.iteritems():               #Check for items in inventory that match
        keyList = key.split(",")
        if keyword in keyList:
            matching.append(item)
            
    if len(matching) > 1:
        print "You need to be more specific"
        return

    for feature in player.currentLocation.features.itervalues():
        if (isinstance(feature, BaseClasses.Container)) and (feature.isOpen == True):
            for key,item in feature.itemsContained.iteritems():
                keyList = key.split(",")
                if keyword in keyList:
                    matching.append(item)

    if len(matching) > 1:
        print "You need to be more specific"
    elif len(matching) == 1:
        print matching[0].lookAt()
    else:
        print "You don't see anything like that here."
    return

def save(state):
    with open(Main.SAVEGAME_FILENAME, 'w') as savegame:
        savegame.write(jsonpickle.encode(state))
    print "Game saved."
    
def load():
    with open(Main.SAVEGAME_FILENAME, 'r') as savegame:
        state = jsonpickle.decode(savegame.read())
        return state