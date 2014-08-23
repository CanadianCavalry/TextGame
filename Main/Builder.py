'''
Created on Jun 30, 2014

@author: Thomas
'''
from Main import AreasFeatures
import StandardFeatures
import UniqueFeatures
import StandardItems
import Items
import Enemies
import UniqueNPCs
import NPCs

INTRO = "September 3rd, 2015. You wake up around 10 a.m. as usual, and have already ate and freshened up for the day. You recall that the new Director of the Rehab\n House - Father Malachi - is going to be giving a talk outlining why he and his associates have implemented new policies in House management, and will be\n taking questions afterwards. The architect of many new regulations you find draconian and invasive, this will be the first time the director\n has made an appearance to you and the other residents. You plan to attend the talk to get a better idea of the nature\n of the man who will control much of your life in the forseeable future. The talk is taking place in fifteen minutes, and is located\n in the auditorium of the old church wing. You recall that the easiest way to get there is to simply head north through the residents wing,\n past the courtyard, until you reach the auditorium.<paragraph break> You are currently located in your quarters\n in the resident wing of the house. Like virtually every other service offered by the house, they spared no expense in providing\n the residents with a fine place to live. Your quarters are large, fully furnished, and even come with a personal computer\n and a large plasma TV. Right now, you are craving some alcohol. This is surprising as the new medication, 'Rejuvinax', that\n father Malachi has been providing you with has been practically miraculous in controlling your cravings, to the point of you hardly being aware of them.\nIt's an exquisite longing that is more pronounced than anything you've felt since your time here. Odd. Why would you b experiencing symptoms like this now, completely out of nowhere?"

def buildWorld(gameState):
    
    #Combat Test Environment
    combatRoom = AreasFeatures.Area("Combat Simulator", "You are standing in a large, empty colosseum. There are no doors, and the walls are far to high to climb.")    
    
    fireAxe = StandardItems.Axe()
    chefKnife = StandardItems.Knife()
    handgun = StandardItems.Handgun()
    book = StandardItems.Book("A Book", "Its a book", "A book", 1, "book", )
    page1 = StandardItems.Page("This is the first page, its pretty boring.")
    page2 = StandardItems.Page("This is the second page. It's actually super exciting!")
    book.addPage(page1)
    book.addPage(page2)
    
    combatRoom.addItem(fireAxe)
    combatRoom.addItem(chefKnife)
    combatRoom.addItem(handgun)
    combatRoom.addItem(book)
    
    testDemon = Enemies.TestDemon()
    combatRoom.spawnEnemy(testDemon)
   #gameState.addArea(combatRoom)


    #JACOBS ROOM
    jacobsRoom101 = AreasFeatures.Area("Jacob's Room", "This small room is well furnished with all of the comforts \
you could ask for, including a bed, bookshelf, coffee table, dresser, tv and \
chairs.\nIt even contains a personal bathroom. On the far wall hangs a small \
painting next to the single window. Next to these is my closet. There is a door \
to the west leading to the residential wing.")
    
    #Links
    door101A = StandardFeatures.StandardOpenDoor("A hefty blue wooden door.", "east,door,east door,blue door,wood door,hallway")
    
    #NPCs
    
    #Features
    bookshelf101 = AreasFeatures.Feature("This tall, wooden bookshelf is filled with books on a variety of my favorite subjects - notably theology, history and literature. It also includes \na large red bible (NIV version)", "bookshelf,shelf")
    jacobsRoom101.addFeature(bookshelf101)
    painting101 = AreasFeatures.Feature("A beautiful painting by my brother, Fernando. It's of Jesus curing a blind man. The caption underneath reads 'Once I was blind, and now I see'. \nThe look of childlike surprise and utter gratitude on the mans face always fills me with hope.", "painting")
    jacobsRoom101.addFeature(painting101)
    bed101 = AreasFeatures.Feature("A very comfortable queen sized bed. I've been in the habit of making it immediately after waking since I was a very small child.", "bed,queen bed")
    jacobsRoom101.addFeature(bed101)
    dresser101 = AreasFeatures.Feature("Contains my clothes","dresser")
    jacobsRoom101.addFeature(dresser101)
    chairs101 = AreasFeatures.Feature("Two very comfortable armchairs. I often sit here while praying.","chair,chairs,armchair,armchairs")
    jacobsRoom101.addFeature(chairs101)
    bathroom101 = AreasFeatures.Feature("A small, personal bathroom complete with a sink, shower and toilet. Lately I've gotten into the habit of cleaning it on a weekly basis. \nIt often takes my mind off of my cravings.","bathroom,sink,toilet,shower")
    jacobsRoom101.addFeature(bathroom101)
    window101 = UniqueFeatures.JacobRoomWindow()
    jacobsRoom101.addFeature(window101)
    tv101 = AreasFeatures.Feature("This entertainment unit comes with a 42 inch LED, that includes cable and a PVR. On the bottom shelf are a variety of DVD's I've\n taken from The House library, as well as my personal collection of Dr. Who and Star Trek TNG box sets.","tv,entertinment stand,entertainment center")              #Add ability to turn on
    jacobsRoom101.addFeature(tv101)
    
    #Containers
    coffeeTable101 = StandardFeatures.AlwaysOpenContainer("A heavy wood coffee table, about 2 feet high. Oak, if I had to guess. Looks brand new. There are a dozen or so papers and notes scattered across the top of it. ", "coffee table,table")
    jacobsRoom101.addFeature(coffeeTable101)
    closet101 = StandardFeatures.UnlockedContainer("A fairly small closet, but big enough to hold a few sets of clothes. I haven't had much use for it since I've been here. Don't even remember what I put in it.", "closet", "The closet opens easily, though a little noisily.", "The door slides closed.")
    jacobsRoom101.addFeature(closet101)
    
    #Items
    notice101 = StandardItems.Note("Notice on New Policies", "A note given to the residents about changes to the facilities policies since Father Malachi took over.", "A notice on house policy changes", 1, "note,policy note,notice,policy notice,changes notice,policy changes notice", "There be changes to the policy, bitches.")
    coffeeTable101.addItem(notice101)
    houseGuide101 = Items.Item("Guide to House Services", "To be filled", "A guide to house services", 1, "guide,house guide,services guide,house services guide")
    coffeeTable101.addItem(houseGuide101)
    rehabGuide101 = Items.Item("Guide to Combating Addiction", "To be filled", "A guide to addiction", 1, "guide,addiction guide")
    coffeeTable101.addItem(rehabGuide101)
    rejuvinaxNote101 = Items.Item("Rejuvinax Note", "To be filled", "A note about Rejuvinax", 1, "note,rejuvinax note,drug note")
    coffeeTable101.addItem(rejuvinaxNote101)
    journal101 = Items.Item("Journal", "To be filled", "My journal", 1, "journal")
    coffeeTable101.addItem(journal101)
    flaskOfScotch101 = StandardItems.Alchohol("Flask of Scotch", "A small silver flask which holds about 4 oz. I received this as a gift from a friend form church before they realized \nI had a problem. I'm sure they regretted giving it to me once they found out.", "A small silver flask of whiskey.", 1, "flask,whiskey,silver flask,flask of whiskey,alcohol,booze", "You unscrew the cap and drain the remaining liquid from the flask. Delicious.",10)
    closet101.addItem(flaskOfScotch101)
    leatherJacket101 = StandardItems.LeatherJacket()
    closet101.addItem(leatherJacket101)
    
    gameState.addArea(jacobsRoom101)
    
    #FIRST FLOOR HALLWAY
    firstFloorHallway102 = AreasFeatures.Area("First Floor Hallway", 
"The Residents wing contains all of the private living spaces for House residents. It includes 3 \
floors with ten rooms each. Featuring a  gingerbread-coloured carpet and vermillion walls with fancy, five-bulbed lamps set \
into them, the hallway is large and airy with an upper-class feel. Rooms 101-105 are on the east side of the hallway and Rooms \
106-110 are on the west. Room 106 is my room, and the door to Room 104 is ajar. A set of stairs that leads up to the second \
floor of the Residents wing can be accessed through this hallway. To the SOUTH is a door that leads into the Main Lobby, and another \
door to the NORTH leads into the Essential Services area of the Residents Wing.")
    
    #Links
    door102A = StandardFeatures.StandardOpenDoor("A hefty blue wooden door. The room number is 106.", "west,door,west door,blue door,room 106,106,door 106,jacobs door,jacob door,my room")
    door102A.makeSibling(door101A)
    jacobsRoom101.connect(firstFloorHallway102, door101A)
    firstFloorHallway102.connect(jacobsRoom101, door102A)
    door102B = StandardFeatures.StandardOpenDoor("A hefty blue wooden door. The room number is 104.", "east,door,east door,blue door,room 104,104,door 104")
    door102C = StandardFeatures.StandardOpenDoor("A set of thick metal double doors. The sign above them reads \"Main Lobby\".", "south,door,south door,metal door,double doors,lobby,main lobby")
    door102D = StandardFeatures.StandardOpenDoor("A fairly ordinary wooden door. The sign above it reads \"Essential Services\".", "north,door,north door,essential services door,essential services")
    stairs102A = StandardFeatures.StandardUpwardStairs("A wide, well lit staircase which double back up to the second floor.", "up,upstairs,up stairs,up staircase,staircase,stairs,stairway")
    
    #NPCs
    securityGuards102 = UniqueNPCs.SecurityGuards102()
    firstFloorHallway102.addNPC(securityGuards102)
    
    #Features
    
    #Containers
    
    #Items
    
    #ROOM 104
    cicerosRoom103 = AreasFeatures.Area("Room 104",
    "This room belongs to a rather odd resident named Cicero, who I have developed something of a friendship  with recently. The books, \
pages, and  trinkets scattered all over the room are a testimony to Cicero's tendency to place all his focus on his personal projects \
and ignore everything else. It seems all the books are about mythology, and the pages are either notes of his or clips of papers \
he wrote at Oxford long ago. The trinkets are various curiousities owned by Cicero, some which of he's told me are valuable historical \
artifacts. The door to the hallway is to the west.")
    
    #Links
    door103A = StandardFeatures.StandardOpenDoor("A hefty blue wooden door.", "west,door,west door,blue door,hallway")
    door103A.makeSibling(door102B)
    firstFloorHallway102.connect(cicerosRoom103, door102B)
    cicerosRoom103.connect(firstFloorHallway102, door103A)
    
    #NPCs
    cicero103 = UniqueNPCs.Cicero103()
    cicerosRoom103.addNPC(cicero103)
    
    #Features
    
    #Containers
    
    #Items
    
    #SECOND FLOOR HALLWAY
    secondFloorHallway104 = AreasFeatures.Area("Second Floor Hallway", 
"This hall is nearly identical to the first floor. Rooms 201-205 are on the east side of the hallway and Rooms \
206-210 are on the west. The door to Rooms 201 and 205 are ajar. Two sets of stairs that lead to the first and third \
floor of the Residents wing can be accessed through this hallway.")
    
    #Links
    door104A = StandardFeatures.StandardOpenDoor("A hefty blue wooden door. The room number is 201.", "east,door,east door,blue door,room 201,201,door 201")
    door104B = StandardFeatures.StandardOpenDoor("A hefty blue wooden door. The room number is 205.", "east,door,east door,blue door,room 205,205,door 205")
    
    stairs104A = StandardFeatures.StandardDownwardStairs("A wide, well lit staircase which goes both up to the third floor and down to the first floor.", "down,downstairs,down stairs,down staircase,staircase,stairs,stairway")
    stairs104A.makeSibling(stairs102A)
    firstFloorHallway102.connect(secondFloorHallway104, stairs102A)
    secondFloorHallway104.connect(firstFloorHallway102, stairs104A)
    
    stairs104B = StandardFeatures.StandardUpwardStairs("A wide, well lit staircase which goes both up to the third floor and down to the first floor.", "up,upstairs,up stairs,up staircase,staircase,stairs,stairway")
    
    #NPCs
    
    #Features
    
    #Containers
    
    #Items
    
    #MICHEALS ROOM
    michealsRoom105 = AreasFeatures.Area("Room 201",
"This room is a mess. Bits of old food, dirty laundry, and other things whose origin you would rather not contemplate are scattered over\
every surface. The place reeks of cigarette smoke. So many used cigarette butts are littered over it that you feel like it's a room-sized ashtray. \
The door to the hallway is to the west.")
    
    #Links
    door105A = StandardFeatures.StandardOpenDoor("A hefty blue wooden door.", "west,door,west door,blue door,hallway")
    door105A.makeSibling(door104A)
    secondFloorHallway104.connect(michealsRoom105, door104A)
    michealsRoom105.connect(secondFloorHallway104, door105A)
    
    #NPCs
    micheal105 = UniqueNPCs.Micheal105()
    michealsRoom105.addNPC(micheal105)
    
    #Features
    mess105 = AreasFeatures.Feature("Everything in this room is completely disgusting. I'd really rather not look to closely.", "mess,garbage,cigarettes,butts,cigarette butts,stuff,food,old food,room,things")    
    michealsRoom105.addFeature(mess105)
    
    #Containers
    
    #Items
    
    #ASTRIDS ROOM
    astridsRoom106 = AreasFeatures.Area("Room 205",
"This room belongs to Astrid, a slender, middle aged woman. The place is as immaculate and tidy as ever. Unlike most \
of the other residents in the House, Astrid has completely rearranged the furnishings in her room to suit her needs. \
She even got permission from the management to move out one of the two armchairs that come with every room so she could \
place a tall, gaudy mirror in its place. The centrepiece of the room is a large table upon which pictures of Astrid and \
her various trophies and awards are arranged; I always think of this as Astrid's shrine to herself. The door to the hallway is to the west.")
    
    #Links
    door106A = StandardFeatures.StandardOpenDoor("A hefty blue wooden door.", "west,door,west door,blue door,hallway")
    door106A.makeSibling(door104B)
    secondFloorHallway104.connect(astridsRoom106, door104B)
    astridsRoom106.connect(secondFloorHallway104, door106A)
    
    #NPCs
    astrid106 = UniqueNPCs.Astrid106()
    astridsRoom106.addNPC(astrid106)
    
    #Features
    
    #Containers
    
    #Items
    
    #THIRD FLOOR HALLWAY
    thirdFloorHallway107 = AreasFeatures.Area("Third Floor Hallway", 
"This hall is nearly identical to the first floor. Rooms 301-305 are on the east side of the hallway and Rooms \
206-210 are on the west. The door to Room 308 is ajar. A staircase leads down to the second floor from here.")
    
    #Links
    door107A = StandardFeatures.StandardOpenDoor("A hefty blue wooden door. The room number is 308.", "west,door,west door,blue door,room 308,308,door 308")
    
    stairs107A = stairs104A = StandardFeatures.StandardDownwardStairs("A wide, well lit staircase which goes down to the second floor.", "down,downstairs,down stairs,down staircase,staircase,stairs,stairway")
    stairs107A.makeSibling(stairs104B)
    secondFloorHallway104.connect(thirdFloorHallway107, stairs104B)
    thirdFloorHallway107.connect(secondFloorHallway104, stairs107A)
    
    #NPCs
    
    #Features
    
    #Containers
    
    #Items
    
    #ROSES ROOM
    rosesRoom108 = AreasFeatures.Area("Room 308",
"This room belongs to Astrid, a slender, middle aged woman. The place is as immaculate and tidy as ever. Unlike most \
of the other residents in the House, Astrid has completely rearranged the furnishings in her room to suit her needs. \
She even got permission from the management to move out one of the two armchairs that come with every room so she could \
place a tall, gaudy mirror in its place. The centrepiece of the room is a large table upon which pictures of Astrid and \
her various trophies and awards are arranged; I always think of this as Astrid's shrine to herself. The door to the hallway is to the east.")