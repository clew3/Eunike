import math
from typing import Counter
from .equation_creator import random_equation

###################################################################################################################
# CONSTANTS

COUNT = "Count"
END = "End"
FAIL = "Fail"
MEMES = "Memes"
NO_INPUT = "No Input"
THREE = 3
###################################################################################################################

class Room(object):
    '''
    Fields:
        name (Str)
        type (Str)
        background (Str)
        description (Str)
        paths (dict of Str Room)
        equation (list Str Flo)
        self.image (listof Str)
        self.limit (Nat)
        self.keyword (Str)
    '''
    def __init__(self, n):
        '''
        Constructor: Create a Room object by calling Room(n, b),
        
        __init__: Room Str Str -> None
        '''
        self.name = n
        self.type = n
        self.background = ""
        self.description = ""
        self.paths = {}
        self.equation = random_equation()
        self.image = ""
        self.limit = 100
        self.keyword = "TEST"

    def __repr__(self) -> str:
        s = "Name: {0.name}"
        return s.format(self)

    def go(self, action):
        '''
        Returns the proceeding Room if the choice is close enough
        
        go: Room Str -> Room
        Requires: action in self.paths
        '''

        try:
            x = math.isclose(float(action), self.equation[1],abs_tol=0.01)
        except:
            x = False

        
        if x:
            print(self.paths.get(str(self.equation[1])))
            return self.paths.get(str(self.equation[1]))
        else:
            return self.paths.get(action)
    
    def add_paths(self, paths):
        '''
        Adds paths to self.paths
        add_paths: Room (dictof Str Str) -> None
        '''
        self.paths.update(paths)


###################################################################################################################
# Intro
###################################################################################################################


Intro = Room("Intro")
Intro.background = "/static/scenea.jpg"
Intro.description = \
    '''
    Welcome to the story. It's 6:30 pm, and you're trying to find where CCF Bible Study will be held tonight. Let's go on
    an adventure! Whenever you're ready, type 'yes'.
    '''


###################################################################################################################
# Fail
###################################################################################################################


Fail = Room("...")
Fail.type = FAIL


###################################################################################################################
# MC
###################################################################################################################


MC_scene_1 = Room("Outside the MC Building")
MC_scene_1.background = "/static/flask-logo.png"
MC_scene_1.equation = ['3',3]
MC_scene_1.description = \
    '''
    You find yourself at MC, and you're not too sure on how to proceed. When you enter in, there's an elevator that 
    you can take. Which floor do you want to go to?
    '''


MC_scene_1_wrong = Room("Wrong floor")
MC_scene_1_wrong.background = "/static/flask-logo.png"
MC_scene_1_wrong.type = NO_INPUT
MC_scene_1_wrong.keyword = "Let's try again" #hmm maybe new room?
MC_scene_1_wrong.description = \
    '''
    Hmm there's nothing interesting on this floor. Let's go back.
    '''


MC_scene_2 = Room("MC C&D")
MC_scene_2.type = COUNT
MC_scene_2.limit = THREE
MC_scene_2.equation = ['25 - (2*1.13 + 3*1.41)', "18.51"]
MC_scene_2.description = \
    '''
    You find yourself at the MC C&D on the third floor. Feeling peckish (because you know CCF won't end until late o'clock), 
    you decide to grab a quick bite. You remember the last time you used your WatCard, you had $25.00. Knowing coffees cost 
    $1.13 and donuts cost $1.41, how much money would you have left if you bought two coffees and three donuts?
    '''


MC_scene_2_fail = Fail



MC_scene_3 = Room("Post C&D")
MC_scene_3.background = "/static/flask-logo.png"
MC_scene_3.description = \
    '''
    After acquiring the goods, you check the receipt, and there's a "0" circled on the back. Or that could just be a donut, 
    we're not too sure ourselves. Anyhoo, you feel as if your time at MC has come to an end, so you decide to take the bridge.
    But to where?
    '''
   
    
MC_scene_3_wrong = Room("Locked")
MC_scene_3_wrong.background = "/static/flask-logo.png"
MC_scene_3_wrong.type = NO_INPUT
MC_scene_3_wrong.keyword = "Take me back!"
MC_scene_3_wrong.description = \
    '''
    Hmm the door seems to be locked. Let's backtrack.
    '''


###################################################################################################################
# QNC
###################################################################################################################


QNC_scene_1 = Room("QNC 2nd Floor")
QNC_scene_1.type = COUNT
QNC_scene_1.limit = THREE
QNC_scene_1.description = \
    '''
    After taking the bridge over, you make your way to the tables where Dana performed his infamous jump. Hoping to 
    find a clue, you take a closer look but nothing there seems out of the ordinary. But when you take a step back,
    what do you see but this equation on the whiteboard?

    What is {}?
    '''.format(QNC_scene_1.equation[0])


QNC_scene_1_fail = Fail


QNC_scene_2 = Room("QNC Basement")
QNC_scene_2.type = COUNT
QNC_scene_2.limit = THREE
QNC_scene_2.equation = ["52 - 36", "16"]
QNC_scene_2.description = \
    '''
    Moving onwards, you follow the steps down the stairs until you reach the basement, where a tantalizing piano lies
    off to the side. Of course I'm adding a piano to the story, what did you expect from me? Speaking of which, what
    is the difference between the number of white keys and the number of black keys on a standard piano?
    '''


###################################################################################################################
# Foodie Fruitie
###################################################################################################################

Foodie_prep = Room("Walk to Foodie")
Foodie_prep.type = NO_INPUT
Foodie_prep.keyword = "Noice!"
Foodie_prep.description = \
    '''
    You open the lid of the piano, and on middle C, there's a sticky note with a "C" on it. Hmmm, that could be something.
    "What else begins with a 'C'?", you ponder.

    "Chinese"

    "Curry"

    "Chicken"

    And with that, you begin the long arduous trek to Waterloo's premiere culinary establishment: Foodie Fruitie. 
    '''

Foodie = Room("Foodie")
Foodie.type = MEMES
Foodie.keyword = "We goooo"
Foodie.description = \
    '''
    Take a break, take a kit kat
    Here are some dank maymays
    Enjoy!

    Caleb spent a lot of work on this
    Let's all appreciate his effort
    Unless you guys don't like it.
    Eh, whatever that's a you problem

    I think I deserve the adoration,
    So please shower praise upon me

    Haha jkjk... unless?
    '''

###################################################################################################################
# E7
###################################################################################################################


E7_scene_1 = Room("E7 4053")
E7_scene_1.description = \
    '''
    You suddenly remember that oh yeah, Bible Study is happening. Where do most CCFers spend their time? At E7 of 
    course! 
    
    You sprint to the fourth floor, where you espy a bunch of fourth years skipping Bible Study and playing
    a cursed board game instead. You'd love to vote them out, but you for one are a Loyal Servant of Jesus, and that's
    just not cool. Too bad you don't remember the name of the game...
    '''


E7_scene_2 = Room("Chem Lab")
E7_scene_2.description = \
    '''
    Making your way downstairs, you run into the chemical lab, where you see someone leave their chemicals laying
    haphazardly around. Hey here's a chemistry question: What are the two elements that are liquid at room temperature
    and pressure? Answer "____ and ____"
    '''

E7_scene_3 = Room("Gear lab")
E7_scene_3.type = COUNT
E7_scene_3.limit = THREE
E7_scene_3.description = \
    '''
    After cleaning up, you meander yourself into the gear lab (and avoiding the Gear Lab Guy). You see schematics for
    something that you think will be a good idea to print, but you're kinda not sure what it is so let's find out!
    While you're waiting for the 3D-printer to finish, you try solving the following math equation on the board:

    What's {}?
    '''.format(E7_scene_3.equation[0])


E7_scene_3_fail = Fail


E7_end = Room("post Gear Lab")
E7_end.type = NO_INPUT
E7_end.keyword = "aight imma head off"
E7_end.description = \
    '''
    After a while, the printer finally finishes it's last touches, so you grab your new prized posession: a shiny "1".
    That's gotta be a clue; I'm not sure how much more obvious it can be. In the mean time, you realize you left your
    Bible in Icon when you went over there for (insert reason). Well, I guess that'll be our next stop.
    '''


###################################################################################################################
# Icon
###################################################################################################################


Icon_scene_1 = Room("Outside Icon")
Icon_scene_1.description = \
    '''
    When you reach the front door, you realize you don't have a fob with you. Sigh, if only Ferd hadn't graduated yet.
    While you wait for someone to save you, here's a question: how many stories is Icon?
    '''


Icon_scene_1_wrong = Room("Wrong")
Icon_scene_1_wrong.type = NO_INPUT
Icon_scene_1_wrong.keyword = "Let's try again"
Icon_scene_1_wrong.description = \
    '''
    You would think it be like so, but it really don't be like that.
    '''


Icon_scene_2 = Room("Elevator")
Icon_scene_2.type = COUNT
Icon_scene_2.limit = THREE
Icon_scene_2.equation = ["2 + 2 / 2 * 2", "4"]
Icon_scene_2.description = \
    '''
    After some time, you're finally able to get into Icon. Once you get to the elevator, you're stuck because you don't
    remember which floor you should get off of. If only there was an equation that you could solve...


    What is {}?
    '''.format(Icon_scene_2.equation[0])


Icon_scene_2_fail = Fail


Icon_scene_3 = Room("Inside the unit")
Icon_scene_3.type = COUNT
Icon_scene_3.limit = THREE
Icon_scene_3.description = \
    '''
    I'm running out of ideas, just solve this question, idk.

    What is {}? 
    '''.format(Icon_scene_3.equation[0])


Icon_scene_3_fail = Fail


Icon_end = Room("Deus Ex Machina")
Icon_end.type = NO_INPUT
Icon_end.keyword = "Uh okay"
Icon_end.description = \
    '''
    After solving the question, for some reason a "1" falls from the sky. Hey, you can't make these things up (well
    actually...). Then you suddenly sneeze and find yourself teleported to SLC. Crazy right? It's almost as if I'm
    running out of narrative ideas to explore, and have resorted to miraculous teleportation as a story-telling
    device.
    '''


###################################################################################################################
# SLC
###################################################################################################################


SLC_scene_1 = Room("At Timmy's")
SLC_scene_1.type = COUNT
SLC_scene_1.limit = 3
SLC_scene_1.equation = ["3 * (18 // 4) + 3", "15"]
SLC_scene_1.description = \
    '''
    Finding yourself whisked away to the front of SLC, you enter and are greeted by a long lineup at Tim Hortons.
    Well, it has been a couple scenes since you last ate, and I guess you have some money left on your WatCard. But
    looking at the lineup, you count 18 people ahead of you. If it takes 3 minutes to serve each customer, and there
    are four tills open, how minutes will you have to wait to get your food? You may assume that each till turns over 
    at the same time.
    '''

SLC_scene_1_wrong = Room("Wrong")
SLC_scene_1_wrong.type = NO_INPUT
SLC_scene_1_wrong.keyword = "Let's try again"
SLC_scene_1_wrong.description = \
    '''
    You would think it be like so, but it really don't be like that.
    '''


SLC_scene_1_fail = Fail


SLC_scene_2 = Room("Pool")
SLC_scene_2.type = COUNT
SLC_scene_2.limit = THREE
SLC_scene_2.description = \
    '''
    Afterwards, you get distracted by the new pool at the finally renovated PAC, so you go and check it out. Good thing
    you happen to have your swimsuit with you (don't ask me why), and you go jump into the pool. I'm trying really hard 
    to make this into a word problem that involves math, but honestly I'm kinda burnt out at this point, so just solve 
    this math equation and don't ask any questions.

    What is {}?
    '''.format(SLC_scene_2.equation[0])

SLC_scene_3 = Room("Boulder, Colorado")
SLC_scene_3.description = \
    '''
    What's a visit to SLC without checking out the new rock climbing wall (you already KNOW there's going to be a scene
    involving bouldering). There, you spy a shiny new object at the top of the lead wall, so with no regard for personal
    safety, you begin climbing up without a harness. Do you fall?
    '''

SLC_scene_3_wrong = Room("End")
SLC_scene_3_wrong.type = END
SLC_scene_3_wrong.description = \
    '''
    Well your wish is my command. You fall to your death. The end.
    '''

###################################################################################################################
# End Scene
###################################################################################################################


End_scene = Room("The End")
End_scene.type = COUNT
End_scene.limit = 1
End_scene.description = \
    '''
    You climb to the top and are greeted with a shiny letter "R" (wasaii). Now here comes the hard part: what room are
    CCFers gathering in?
    '''


End_scene_winner = Room("Yay")
End_scene_winner.type = END
End_scene_winner.description = \
    '''
    Congrats, you figured out that the Bible Study would be held in RCH 101! Excitedly, you run through to the theatre,
    ready to learn about the Scriptures. You burst into the lecture hall, and are greeted ... by an empty room? Well
    turns out it took you so long to figure out the clues, that it's 11 and everyone's gone home. Oh well, I'm sure that
    they're all at Foodie. Or are they? If only there was a clue that would tell you where to go next...
    '''


End_scene_fail = Room("Yay")
End_scene_fail.type = END
End_scene_fail.description = \
    '''
    Congrats, you figured out that the Bible Study would be held there! Excitedly, you run through to the theatre,
    ready to learn about the Scriptures. You burst into the lecture hall, and are greeted ... by an empty room? Turns
    out, you did a great job, but "our Bible Study is in another castle". Oh well, time to start all over again.
    '''
    

###################################################################################################################
# Add Paths
###################################################################################################################


Intro.add_paths({
    "yes": MC_scene_1,
    "Yes": MC_scene_1,
})


MC_scene_1.add_paths({
    str(x):MC_scene_1_wrong for x in range(1, 7)
})
MC_scene_1.paths['3'] = MC_scene_2


MC_scene_1_wrong.add_paths({
    "": MC_scene_1,
})


MC_scene_2.add_paths({
     MC_scene_2.equation[1]: MC_scene_3,
})


MC_scene_3.add_paths({
    "QNC": QNC_scene_1,
    "DC": MC_scene_3_wrong,
    "M3": "",
    "SLC": MC_scene_3_wrong,
})


MC_scene_3_wrong.add_paths({
    "": MC_scene_3,
})


QNC_scene_1.add_paths({
    QNC_scene_1.equation[1]: QNC_scene_2,
})


QNC_scene_2.add_paths({
    QNC_scene_2.equation[1]: Foodie_prep,
})

Foodie_prep.add_paths({
    "": Foodie,
})

Foodie.add_paths({
    "": E7_scene_1,
})


E7_scene_1.add_paths({
    "Avalon": E7_scene_2,
})


E7_scene_2.add_paths({
    "Bromine and Mercury": E7_scene_3,
    "Mercury and Bromine": E7_scene_3,
})


E7_scene_3.add_paths({
    E7_scene_3.equation[1]: E7_end,
})


E7_end.add_paths({
    "": Icon_scene_1,
})


Icon_scene_1.add_paths({
    "25": Icon_scene_2,
    "27": Icon_scene_1_wrong,
})


Icon_scene_1_wrong.add_paths({
    "": Icon_scene_1,
})


Icon_scene_2.add_paths({
    Icon_scene_2.equation[1]: Icon_scene_3,
})


Icon_scene_3.add_paths({
    Icon_scene_3.equation[1]: Icon_end,
})


Icon_end.add_paths({
    "": SLC_scene_1,
})


SLC_scene_1.add_paths({
    "12": SLC_scene_1_wrong,
    SLC_scene_1.equation[1]: SLC_scene_2,
})


SLC_scene_1_wrong.add_paths({
    "": SLC_scene_1,
})


SLC_scene_2.add_paths({
    SLC_scene_2.equation[1]: SLC_scene_3,
})


SLC_scene_3.add_paths({
    "Yes": SLC_scene_3_wrong,
    "yes": SLC_scene_3_wrong,
    "No": End_scene,
    "no": End_scene,
})


End_scene.add_paths({
    "RCH 101": End_scene_winner,
})


###################################################################################################################


START = "Intro"

def load_room(name):
    '''
    Returns the requested Room
    load_room: Room -> Room
    '''
    return globals().get(name)

def name_room(room):
    '''
    Grabs the next room to be loaded
    name_room: Room -> Room'''
    for key, value in globals().items():
        if value == room:
            return key