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
        self.name = "Where am I..."
        self.description = ["What in God's name has happened to your room? It smells like a dog and the paint on the \
walls is peeling off everywhere! The only source of light comes from a very dim red bulb hanging from the ceiling. It barely \
illuminates your bed and your restraints, the small table next to your bed, your closet, and the door.",
]
        self.roomState = 0          #States:    0 - Enemy is active. Player is restrained. Most actions unavailable
                                    #           1 - Enemy is inactive (fighting NPC). More actions available.
                                    #           2 - Enemy is active(stunned at first). All player actions available.
    
    #Features
        self.addFeature(AreasFeatures.Feature("You suspect the bastard discarded your blankets, pillows and sheets somewhere. \
The mattress is covered in a filthy black mould and reeks of something foul...", "bed,my bed,jacobs bed"))
        self.addFeature(AreasFeatures.Feature("You don't remember having this flimsy metal table in your room. It's been dragged \
so close to your bed it's actually touching the frame. On it you see a scalpal, pliers, fish hooks, a trephine and a long, serrated metal wire.", "table,metal table,small table"))
        self.addFeature(AreasFeatures.Feature("You definitely don't remember having this kind of light in your room. Almost burnt out, \
it flashes on and off periodically.","light,bulb,lightbulb,lamp"))
        self.addFeature(AreasFeatures.Feature("It's closed. The door to the closet is so dilapidated it's almost falling off the hinges. \
Why is everything in your room in such awful shape?", "closet"))
        self.addFeature(UniqueFeatures.tortureTools109("The tools are rusty and smeared with dark stains.", "tools,tool,tray,pliers,hooks,fish hook,wire,serreted wire,trephine"))
    
    #Links
    
     
    #Container
        table201 = StandardFeatures.AlwaysOpenContainer("A shoddy metal table, its covered in dark smears.")
        self.addFeature(table201)
    
    #Items
        scalpal201 = UniqueItems.Scalpal()
    
        table201.addItem(scalpal201) 
    
    #NPCs
    
    #Enemies