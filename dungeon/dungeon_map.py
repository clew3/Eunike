import math
from .equation_creator import random_equation

class Room(object):
    '''
    Fields:
        name (Str)
        background (Str)
        description (Str)
        paths (dict of Str Room)
        equation (listof Str Flo)
    '''
    def __init__(self, n, b):
        '''
        Constructor: Create a Room object by calling Room(n, b),
        
        __init__: Room Str Str -> None
        '''
        self.name = n
        self.background = b
        self.description = ''
        self.paths = {}
        self.equation = random_equation()

    
    def go(self, action):
        '''
        Returns the proceeding Room 
        
        go: Room Str -> Room
        Requires: action in self.paths
        '''
        try:
            x = math.isclose(float(action), self.equation[1],rel_tol=2)
        except:
            x = False
        print(x)
        if x:
            return self.paths.get(str(self.equation[1]))
         
    
    def add_paths(self, paths):
        '''
        Adds paths to self.paths
        add_paths: Room (dictof Str Str) -> None
        '''
        self.paths.update(paths)


###################################################################################################################
# Scene A
###################################################################################################################


scene_A = Room("Scene A", "/static/scenea.jpg")
scene_A.description = \
    '''
    Scene A

    What is {}?
    '''.format(scene_A.equation[0])


scene_A_option_1 = Room("Death", "")
scene_A_option_1.description = \
    '''
    Scene A, wrong option
    '''

###################################################################################################################
# Scene B
###################################################################################################################


scene_B = Room("Scene B", "/static/flask-logo.png")
scene_B.description = \
    '''
    Scene B

    What is {}?
    '''.format(scene_B.equation[0])


scene_B_wrong = Room("Death", "")
scene_B_wrong.description = \
    '''
    Scene B, wrong option
    '''

###################################################################################################################
# Scene C
###################################################################################################################


scene_C = Room("Scene C", "")
scene_C.description = \
    '''
    Scene C

    What is {}?
    '''.format(scene_C.equation[0])


scene_C_wrong = Room("Death", "")
scene_C_wrong.description = \
    '''
    Scene C, wrong option
    '''

###################################################################################################################
# Scene D
###################################################################################################################


scene_D = Room("Scene D", "")
scene_D.description = \
    '''
    Scene D

    What is {}?
    '''.format(scene_D.equation[0])


###################################################################################################################
# End Scene
###################################################################################################################


the_end_winner = Room("The End", "")
the_end_winner.description = \
    '''
    The End: Nice
    '''

the_end_loser = Room("The End", "")
the_end_loser.description = \
    '''
    The End: Try again, loser
    '''

###################################################################################################################
# Add Paths
###################################################################################################################


scene_A.add_paths({
    str(scene_A.equation[1]): scene_B,
    '*': scene_A_option_1
})

scene_B.add_paths({
    str(scene_B.equation[1]): scene_C,
    '*': scene_B_wrong
})

scene_C.add_paths({
    str(scene_C.equation[1]): scene_D,
    '*': scene_C_wrong
})

scene_D.add_paths({
    str(scene_D.equation[1]): the_end_winner,
    '*': the_end_loser
})

###################################################################################################################


START = 'scene_A'

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