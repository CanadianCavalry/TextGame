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
    
    if len(matching) == 0:
        print "You do not see any such item here."
    elif len(matching) > 1:
        print "You need to be more specific"
    elif len(matching) == 1:
        print matching[0].get(player)
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

def openThing(player, keyword):
    matching = list()
    for key,item in player.currentLocation.connectedAreas.iteritems():
        keyList = key.split(",")
        if keyword in keyList:
            matching.append(item)
            
    if len(matching) > 1:
        print "You need to be more specific"
        
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

def closeThing(player, keyword):
    matching = list()
    for key,item in player.currentLocation.connectedAreas.iteritems():
        keyList = key.split(",")
        if keyword in keyList:
            matching.append(item)
            
    if len(matching) > 1:
        print "You need to be more specific"
        
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


def inventory(player):
    if len(player.inventory) == 0:
        print "You are not carrying anything."
        return
    
    print "Your current inventory:\n"
    for item in player.inventory.itervalues():
        print item.name.title() + "\n"
    return

def look(player, keyword):
    if keyword == "":                                                       #Check if this is a general look command
        print player.currentLocation.name                                   # if it is, describe the room and items in it
        print player.currentLocation.lookAt()
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
    elif len(matching) == 1:
        print matching[0].lookAt()
        return
    else:
        print "You don't see anything like that here."