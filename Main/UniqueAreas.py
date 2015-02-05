'''
Created on Sep 12, 2014

@author: Thomas
'''
import AreasFeatures
import StandardItems
import StandardFeatures
import UniqueNPCs
import UniqueItems
from Main import UniqueFeatures

class interrogationRoom201(AreasFeatures.Area):
    
    def __init__(self):
        self.visited = False
        self.roomState = 0
        self.connectedAreas = {}
        self.features = {}
        self.itemsContained = {}
        self.enemies = {}
        self.NPCs = {}
        self.name = "Where am I..."
        self.description = ["What in God's name has happened to your room? It smells like a dog and the paint on the \
walls is peeling off everywhere! The only source of light comes from a very dim red bulb hanging from the ceiling. It barely \
illuminates your bed and your restraints, the small table next to your bed, your closet, and the door. The door appears to be chained shut, with a heavy padlock securing the chains.",
]
        self.roomState = 0
    
    #Features
        self.addFeature(AreasFeatures.Feature("You suspect the bastard discarded your blankets, pillows and sheets somewhere. \
The mattress is covered in a filthy black mould and reeks of something foul...", "bed,my bed,jacobs bed"))
        self.addFeature(AreasFeatures.Feature("You don't remember having this flimsy metal table in your room. It's been dragged \
so close to your bed it's actually touching the frame. On it you see a scalpal, pliers, fish hooks, a trephine and a long, serrated metal wire.", "table,metal table,small table"))
        self.addFeature(AreasFeatures.Feature("You definitely don't remember having this kind of light in your room. Almost burnt out, \
it flashes on and off periodically.","light,bulb,lightbulb,lamp"))
        self.addFeature(AreasFeatures.Feature("It's closed. The door to the closet is so dilapidated it's almost falling off the hinges. \
Why is everything in your room in such awful shape?", "closet"))
        self.addFeature(AreasFeatures.Feature("They're made of rope and restrain both your wrists and both your ankles to the bedposts. You're tied quite securely, but the rope isn't very thick and you might be able to manoveure your hands and feet about a foot in each direction.",
"bindings,rope,restraints,bonds"))
        self.addFeature(AreasFeatures.Feature("A heavy steel padlock.", "padlock,lock"))
    
    #Links
        door201A = StandardFeatures.StandardOpenDoor("You don't remember your door looking so dilapidated and worn, and you certainly don't recall a padlock on it.", "door,east door, east")
     
    #Container
        table201 = StandardFeatures.AlwaysOpenContainer("A shoddy metal table, its covered in dark smears.", "table,metal table")
        self.addFeature(table201)
    
    #Items
        table201.addItem(UniqueItems.Scalpal201()) 
        table201.addItem(UniqueItems.TortureTools201())
    
    #NPCs
    
    #Enemies