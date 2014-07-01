def go(player, keyword):
    matching = list()
    for key,item in player.currentLocation.connectedAreas.iteritems():
        if keyword in key:
            matching.append(item)

    if len(matching) == 0:
        print "You do not see any such item here."
    elif len(matching) > 1:
        print "You need to be more specific"
    elif len(matching) == 1:
        
        if player.currentLocation.visited == False:     #Next check if this is their first time in this area
            player.currentLocation.visited = True
            look(player, "")
        else:
            print player.currentLocation.name
    return

def get(player, keyword):
    matching = list()
    for key,item in player.currentLocation.itemsContained.iteritems():
        if keyword in key:
            matching.append(item)
    
    if len(matching) == 0:
        print "You do not see any such item here."
    elif len(matching) > 1:
        print "You need to be more specific"
    elif len(matching) == 1:
        player.addItem(matching[0])
        player.currentLocation.removeItem(matching[0])
        print "You pick up the " + keyword
    
    return

def drop(player, keyword):
    matching = list()
    for key,item in player.inventory.iteritems():
        if keyword in key:
            matching.append(item)
            
    if len(matching) == 0:
        print "You do not have any such item."
    elif len(matching) > 1:
        print "You need to be more specific"
    elif len(matching) == 1:
        player.removeItem(matching[0])
        player.currentLocation.addItem(matching[0]) 
        print "You drop the " + matching[0].name

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
    
    matchingFeat = list()
    for key,item in player.currentLocation.features.iteritems():        #Check for features that match
        if keyword in key:
            matchingFeat.append(item)
            
    if len(matchingFeat) > 1:
        print "You need to be more specific"
        return
    elif len(matchingFeat) == 1:
        print matchingFeat[0].description
        return
    
    matchingItems = list()
    for key,item in player.currentLocation.itemsContained.iteritems():  #Check for items in the room that match
        if keyword in key:
            matchingItems.append(item)
            
    if len(matchingItems) > 1:
        print "You need to be more specific"
        return
    elif len(matchingItems) == 1:
        print matchingItems[0].description
        return
       
    matchingInv = list()
    for key,item in player.inventory.iteritems():               #Check for items in inventory that match
        if keyword in key:
            matchingInv.append(item)

    if len(matchingInv) > 1:
        print "You need to be more specific"
        return
    elif len(matchingInv) == 1:
        print matchingInv[0].description
        return
       
    else:
        print "You don't see anything like that here."