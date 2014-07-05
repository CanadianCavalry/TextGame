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
        if matching[0].travel(player):
            if player.currentLocation.visited == False:     #Next check if this is their first time in this area
                player.currentLocation.visited = True
                look(player, "")
            else:
                print player.currentLocation.name
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
    matchingInv = list()
    for key,item in player.inventory.iteritems():           #first we find the item to be used, which will be an item
        keyList = key.split(",")
        if targetKeyword in keyList:
            matchingInv.append(item)
            
    if len(matchingInv) > 1:
        print "You need to be more specific"
        return
    elif len(matchingInv) == 1:
        target = matchingInv[0]
    else:
        matchingRoom = list()
        for key,item in player.currentLocation.itemsContained.iteritems():          #didn't find the item in the players inventory, so we
            keyList = key.split(",")                                                #search the room for it
            if targetKeyword in keyList:
                matchingRoom.append(item)
                
        if len(matchingRoom) == 0:
            print "You do not have any such item."
            return
        elif len(matchingRoom) > 1:
            print "You need to be more specific"
            return
        elif len(matchingRoom) == 1:
            target = matchingRoom[0]                                            #by here we have found the item to use if it exists
        
    matchingFeatures = list()
    for key,item in player.currentLocation.features.iteritems():          #now we find the recipient, which will be a feature or link
        keyList = key.split(",")
        if recipientKeyword in keyList:
            matchingFeatures.append(item)
            
    if len(matchingFeatures) > 1:
        print "You need to be more specific."
        return
    elif len(matchingFeatures) == 1:
        recipient = matchingFeatures[0]
    else:
        matchingLinks = list()                                                   #didn't find the recipient in the features list, so we
        for key,item in player.currentLocation.connectedAreas.iteritems():      #search in the links list
            keyList = key.split(",")
            if recipientKeyword in keyList:
                matchingLinks.append(item)
                
        if len(matchingLinks) == 0:
            print "You do not see anything like that here."
            return
        elif len(matchingLinks) > 1:
            print "You need to be more specific"
            return
        elif len(matchingLinks) == 1:
            recipient = matchingLinks[0]
            
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

def open(player, keyword):
    matching = list()
    for key,item in player.currentLocation.connectedAreas.iteritems():
        keyList = key.split(",")
        if keyword in keyList:
            matching.append(item)
            
    if len(matching) == 0:
        print "You do not see anything like that here."
    elif len(matching) > 1:
        print "You need to be more specific"
    elif len(matching) == 1:
        print matching[0].open(player)



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
        print player.currentLocation.description
        if player.currentLocation.itemsContained:
            print "Things you see here:"
            for item in player.currentLocation.itemsContained.itervalues():    #Display all the visible items
                print item.seenDescription
        return     
    
    matching = list()
    for key,item in player.currentLocation.features.iteritems():        #Check for features that match
        keyList = key.split(",")
        if keyword in keyList:
            matching.append(item)
            
    if len(matching) > 1:
        print "You need to be more specific"
        return
    elif len(matching) == 1:
        print matching[0].lookAt()
        return
    
    matchingLinks = list()
    for key,item in player.currentLocation.connectedAreas.iteritems():        #Check for features that match
        keyList = key.split(",")
        if keyword in keyList:
            matchingLinks.append(item)
            
    if len(matchingLinks) > 1:
        print "You need to be more specific"
        return
    elif len(matchingLinks) == 1:
        print matchingLinks[0].lookAt()
        return
    
    matchingItems = list()
    for key,item in player.currentLocation.itemsContained.iteritems():  #Check for items in the room that match
        keyList = key.split(",")
        if keyword in keyList:
            matchingItems.append(item)
            
    if len(matchingItems) > 1:
        print "You need to be more specific"
        return
    elif len(matchingItems) == 1:
        print matchingItems[0].lookAt()
        return
       
    matchingInv = list()
    for key,item in player.inventory.iteritems():               #Check for items in inventory that match
        keyList = key.split(",")
        if keyword in keyList:
            matchingInv.append(item)

    if len(matchingInv) > 1:
        print "You need to be more specific"
        return
    elif len(matchingInv) == 1:
        print matchingInv[0].lookAt()
        return
       
    else:
        print "You don't see anything like that here."