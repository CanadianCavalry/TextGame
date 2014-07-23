'''
Created on Jun 30, 2014

@author: Thomas
'''
import BaseClasses
import StandardFeatures
import StandardItems

INTRO = "September 3rd, 2015. You wake up around 10 a.m. as usual, and have already ate and freshened up for the day. You recall that the new Director of the Rehab\n House - Father Malachi - is going to be giving a talk outlining why he and his associates have implemented new policies in House management, and will be\n taking questions afterwards. The architect of many new regulations you find draconian and invasive, this will be the first time the director\n has made an appearance to you and the other residents. You plan to attend the talk to get a better idea of the nature\n of the man who will control much of your life in the forseeable future. The talk is taking place in fifteen minutes, and is located\n in the auditorium of the old church wing. You recall that the easiest way to get there is to simply head north through the residents wing,\n past the courtyard, until you reach the auditorium.<paragraph break> You are currently located in your quarters\n in the resident wing of the house. Like virtually every other service offered by the house, they spared no expense in providing\n the residents with a fine place to live. Your quarters are large, fully furnished, and even come with a personal computer \nand a large plasma TV. Right now, you are craving some alcohol. This is surprising as the new medication, 'Rejuvinax', that\n father Malachi has been providing you with has been practiacally miraculous in controlling your cravings, to the point of you hardly being aware of them. It's an exquisite longing that is more pronounced than anything you've felt since your time here. Odd. Why would you b experiencing symptoms like this now, completely out of nowhere?"

def buildWorld(gameState):
    jacobsRoom101 = BaseClasses.Area("Jacob's Room", "This small room is well furnished with all of the comforts you could ask for, including a bed, bookshelf, coffee table, dresser, tv and chairs.\nIt even contains a personal bathroom. On the far wall hangs a small painting next to the single window. Next to these is my closet. There is a door to the west leading to the residential wing.")
    
    #Links
    door101A = StandardFeatures.StandardOpenDoor("A hefty blue wooden door.", "west,door,west door,blue door,wood door")
    door101B = StandardFeatures.StandardOpenDoor("A hefty blue wooden door. The room number is 102.", "east,door,east door,blue door,wood door")
    door101A.makeSibling(door101B)
    
    #Features
    bookshelf101 = BaseClasses.Feature("This tall, wooden bookshelf is filled with books on a variety of my favorite subjects - notably theology, history and literature. It also includes \na large red bible (NIV version)", "bookshelf,shelf")
    painting101 = BaseClasses.Feature("A beautiful painting by my brother, Fernando. It's of Jesus curing a blind man. The caption underneath reads 'Once I was blind, and now I see'. \nThe look of childlike surprise and utter gratitude on the mans face always fills me with hope.", "painting")
    bed101 = BaseClasses.Feature("A very comfortable queen sized bed. I've been in the habit of making it immediately after waking since I was a very small child.", "bed,queen bed")
    dresser101 = BaseClasses.Feature("Contains my clothes","dresser")
    chairs101 = BaseClasses.Feature("Two very comfortable armchairs. I often sit here while praying.","chair,chairs,armchair,armchairs")
    bathroom101 = BaseClasses.Feature("A small, personal bathroom complete with a sink, shower and toilet. Lately I've gotten into the habit of cleaning it on a weekly basis. \nIt often takes my mind off of my cravings.","bathroom,sink,toilet,shower")
    window101 = BaseClasses.Feature("A large sliding window. The people who designed these rooms know what they were doing. It lets in a lot of light when it's sunny out, and helps my mood.","window")
    tv101 = BaseClasses.Feature("This entertainment unit comes with a 42 inch LED, that includes cable and a PVR. On the bottom shelf are a variety of DVD's I've\n taken from The House library, as well as my personal collection of Dr. Who and Star Trek TNG box sets.","tv,entertinment stand,entertainment center")              #Add ability to turn on
    
    #Containers
    coffeeTable101 = StandardFeatures.AlwaysOpenContainer("A heavy wood coffee table, about 2 feet high. Oak, if I had to guess. Looks brand new. There are a dozen or so papers and notes scattered across the top of it. ", "coffee table,table")
    closet101 = StandardFeatures.UnlockedContainer("A fairly small closet, but big enough to hold a few sets of clothes. I haven't had much use for it since I've been here. Don't even remember what I put in it.", "closet", "The closet opens easily, though a little noisily.", "The door slides closed.")
    
    #Items
    notice101 = BaseClasses.Item("Notice on New Policies", "To be filled later", "A notice on house policy changes", 1, "note,policy note,notice,policy notice,changes notice,policy changes notice")
    houseGuide101 = BaseClasses.Item("Guide to House Services", "To be filled", "A guide to house services", 1, "guide,house guide,services guide,house services guide")
    rehabGuide101 = BaseClasses.Item("Guide to Combating Addiction", "To be filled", "A guide to addiction", 1, "guide,addiction guide")
    rejuvinaxNote101 = BaseClasses.Item("Rejuvinax Note", "To be filled", "A note about Rejuvinax", 1, "note,rejuvinax note,drug note")
    journal101 = BaseClasses.Item("Journal", "To be filled", "My journal", 1, "journal")
    flaskOfScotch101 = StandardItems.Alchohol("Flask of Scotch", "A small silver flask which holds about 4 oz. I received this as a gift from a friend form church before they realized \nI had a problem. I'm sure they regretted giving it to me once they found out.", "A small silver flask of whiskey.", 1, "flask,whiskey,silver flask,flask of whiskey,alcohol,booze", "You unscrew the cap and drain the remaining liquid from the flask. Delicious.",10)
    leatherJacket101 = StandardItems.LeatherJacket()
    
    #Feature Assignment
    jacobsRoom101.addFeature(bookshelf101)
    jacobsRoom101.addFeature(painting101)
    jacobsRoom101.addFeature(bed101)
    jacobsRoom101.addFeature(dresser101)
    jacobsRoom101.addFeature(chairs101)
    jacobsRoom101.addFeature(bathroom101)
    jacobsRoom101.addFeature(window101)
    jacobsRoom101.addFeature(tv101)
    jacobsRoom101.addFeature(coffeeTable101)
    jacobsRoom101.addFeature(closet101)
    
    #Item Assignment
    coffeeTable101.addItem(notice101)
    coffeeTable101.addItem(houseGuide101)
    coffeeTable101.addItem(rehabGuide101)
    coffeeTable101.addItem(rejuvinaxNote101)
    coffeeTable101.addItem(journal101)
    closet101.addItem(flaskOfScotch101)
    closet101.addItem(leatherJacket101)

    gameState.addArea(jacobsRoom101)
    
    hallway102 = BaseClasses.Area("Hallway", "A long boring hallway.")
    
    #Links
    jacobsRoom101.connect(hallway102, door101A)
    hallway102.connect(jacobsRoom101, door101B)
    
    #Features
    
    #Containers
    
    #Items
    
    #Feature Assignment
    
    #Item Assignment
    
    firstRoom = BaseClasses.Area("First Room", "You are standing in a blue room. There is a door to the east and a door to the north.")        #This is test code
    secondRoom = BaseClasses.Area("Second Room", "You are standing in a red room. There is a door to the west. A small nightstand is sitting in the middle of the room for some reason. There is also a heavy looking wooden chest in the corner.")
    thirdRoom = BaseClasses.Area("Third Room", "You are standing in a teal room. There is a door to the south. A large sign is hanging here which reads 'Congratulations, you aren't a moron!")
    
    rustyKey = StandardItems.Key("rusty key", "This key has seen better days. The entire thing is covered in a thick coat of rust.", "An old rusty key.", 1, "key,rusty key,old key", "With some force, the key turns in the lock with a satisfying click.")
    bottleOfVodka = StandardItems.Alchohol("vodka", "A half-full bottle of cheap vodka. The label has long since worn away.", "A bottle of vodka.", 1, "vodka,bottle,alchohol,booze,bottle of vodka", "You eye the bottle suspiciously. Any port in a storm, you suppose. You quickly down the liquid, and immediately feel a slight warmth through your body.", 15)
    silverKey = StandardItems.Key("silver key", "A fine silver key with intricate designs carved into it. It is far to small to be used for a normal door lock.", "An thin silver key.", 1, "key,silver key,small key,engraved key", "You carefully insert the key and turn it slowly, cautious not to break it.")
    fireAxe = StandardItems.Axe()
    chefKnife = StandardItems.Knife()
    
    firstRoom.addItem(fireAxe)
    firstRoom.addItem(chefKnife)
    
    nightStand = StandardFeatures.UnlockedContainer("A small wooden nightstand. The top is littered with a manner of small items such as pens, books and bits of paper.", "nightstand,night stand,drawer", "The drawer slides open easily.", "You close the drawer.")
    nightStand.addItem(bottleOfVodka)
    nightStand.addItem(silverKey)
    
    chest = StandardFeatures.LockedContainer("A oak chest bound in steel. A sticky note has been stuck to the lid which reads 'Please don't open me.", "chest,lid,oak chest,bound chest", "The chest seems to be locked.", "Though the lid is extremely heavy, you manage to get it open.", "You close the chest.", silverKey)
    chest.addItem(rustyKey)
    
    secondRoom.addFeature(nightStand)
    secondRoom.addFeature(chest)
    
    link100A = StandardFeatures.StandardOpenDoor("A fairly flimsy wooden door. It's painted pink.", "east,door,east door,pink door,wood door")
    link100B = StandardFeatures.StandardOpenDoor("A flimsy looking wood door. The pink paint has mostly faded.", "west,door,west door,pink door,wood door")
    link100A.makeSibling(link100B)
    
    link101A = StandardFeatures.StandardLockedDoor("A heavy looking steel door. It's dark grey. The words 'South Side' have been carved into it.", "north,door,north door,grey door,steel door", rustyKey)
    link101B = StandardFeatures.StandardLockedDoor("A heavy looking steel door. It's dark grey. The words 'North Side' have been carved into it.", "south,door,south door,grey door,steel door", rustyKey)
    link101A.makeSibling(link101B)
    
    firstRoom.connect(secondRoom, link100A)
    secondRoom.connect(firstRoom, link100B)
    
    firstRoom.connect(thirdRoom, link101A)
    thirdRoom.connect(firstRoom, link101B)
    
  
