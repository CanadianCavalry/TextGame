'''
Created on Aug 23, 2014

@author: Thomas
'''
import NPCs

#PROLOGUE NPCs

class SecurityGuards102(NPCs.NPC):
    
    def __init__(self):
        name = "Security Guards"
        description = "Big and muscular, they're both dressed in crimson body armour and sport heavy \
looking handguns holstered at their sides that gleam threateningly in the soft \
light of the hallway. On the backs of their armour the logo of a large white \
phoenix with the words \"Phoenix Security Corporation\" can be seen. I can't help \
miss the security the older management use to employ - Officers Brooks and O'Sullivan \
might have been strict, but at least they weren't intimidating."
        seenDescription = "Standing in the middle of the hallway are two security guards engaged in a discussion."
        talkResponse = "They don't seem to mind that I interrupted them. \"Well well, if it isn't Mr. Hunter!\" \
one of them says. \"You and the other residents here are very lucky to have us \
here. Trust us, you\'re in good hands!\""
        keywords = "guard,guards,security guard,security guards,officers"
        super(SecurityGuards102, self).__init__(name, description, seenDescription, talkResponse,keywords)
        self.addDialogue(NPCs.Dialogue("good hands,lucky,security",
"\"Well, of course you're in good hands! Now that we and Dr. Malachi are in charge \
of this superb facility I'd say every one of you junkies and derelicts are going to \
be just fine! And especially since you've been taking your new medication, eh? I bet \
it\'s doing wonders for you all!\""))
        
class Cicero103(NPCs.NPC):
    
    def __init__(self):
        name = "Cicero"
        description = "A small and silver-haired British fellow wearing an elegant, black night-robe with moccasins. Once \
a professor who taught Anthropology with a special focus on myth at Oxford, he suffered a stroke which destroyed his \
illustrious career. Cicero is an absent-minded and oft-tormented man whose profound frustration and sense of defeat \
caused by his stroke drove him to alcoholism. Despite all this, the stroke did not diminish his immense appetite for \
knowledge and he still studies and writes about mythology in his spare time. I find his thinking to be refreshingly \
unique and insightful, and he's one of the most gentle men I've ever met."
        seenDescription = "Cicero is sitting in an armchair in the corner of the room, rocking at a manic pace."
        talkResponse = "He looks up as if noticing you for the first time. \"Jacob, the one God loved! It is good to see \
as always, my friend. I am most unsettled today. The smoke and ash of Mount Vesuvius surrounds. It fills my lungs and \
throat, giving me terrible visions. Mischief! Wickedness! Horror!\" He is quite agitated."
        keywords = "cicero,british man,man,occupant,resident"
        super(Cicero103, self).__init__(name, description, seenDescription, talkResponse, keywords)
        
class Micheal105(NPCs.NPC):
    
    def __init__(self):
        name = "Micheal"
        description = "A long, tall drink of a man, Micheal is middle-aged fellow whose fingernails are greasy and yellowish \
from smoking. He's a former crystal meth addict who often blames his problems on his childhood and the neighborhood he grew up in. \
I find him negative, childish and try to avoid whenever possible."
        seenDescription = "This rooms sole occupant, Micheal, is sitting on his bed, fighting to light a half used cigarette."
        talkResponse = "He stops flicking his empty lighter for a moment and looks up. He briefly looks you over and then resumes his attempts. \
\"Oh, hey Jacob. What d'ya want?\" He coughs violently, his wheezing breath a clear indication of lungs severely damaged by excessive \
smoking. \"Is it just me, or is that junk they've been giving us not doing shit for you today?\""
        keywords = "micheal,man,smoking man,occupant,resident"
        super(Micheal105, self).__init__(name, description, seenDescription, talkResponse, keywords)
        
class Astrid106(NPCs.NPC):
    
    def __init__(self):
        name = "Astrid"
        description = "With hair that flows gracefully down her shoulders like an auburn waterfall and a gorgeous, slender figure, \
Astrid could have any man or woman she wanted if she wasn't so self-centered. The rumor is that she was an extremely successful \
cocaine dealer until she got hooked on her own wares. I find the coldness in her eyes unsettling."
        seenDescription = "Astrid, a tall slender woman, is standing in the bathroom combing her hair."
        talkResponse = "\"Why, hello Jacob!\" she coos. \"Forgive me for already being occupied and not offering you proper hospitality. \
The Rejuvenax they have been giving us seems to have to failed to silence my cravings today. And when the world takes something from \
Astrid, it's only right for Astrid to pamper herself even more than usual, no?\""
        keywords = "astrid,woman,tall woman,slender woman,occupant,resident"
        super(Astrid106, self).__init__(name, description, seenDescription, talkResponse, keywords)