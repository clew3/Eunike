import random

def random_equation():
    '''
    Returns a dictionary of an equation paired with its answer
    random_equation: None -> (listof Str Int)
    '''
    operator = random.choice([' + ', ' - ', ' * '])
    rand1 = str(random.randrange(100))
    rand2 = str(random.randrange(100))

    equation = rand1 + operator + rand2
    return [equation, eval(equation)]

class Room(object):

    def __init__(self, name, description):
        self.name = name
        self.description = description
        self.paths = {}
    
    def go(self, direction):
        return self.paths.get(direction)
    
    def add_paths(self, paths):
        self.paths.update(paths)

###################################################################################################################
# Scenes
###################################################################################################################
SCENE_A_EQUATION = random_equation()
SCENE_B_EQUATION = random_equation()
SCENE_C_EQUATION = random_equation()
SCENE_D_EQUATION = random_equation()

scene_A = Room("Scene A",
'''
Scene A

What is {}?
'''.format(SCENE_A_EQUATION[0]))

scene_A_option_1 = Room("death",
'''
Scene A, wrong option
''')

scene_B = Room("Scene B",
'''
Scene B

What is {}?
'''.format(SCENE_B_EQUATION[0]))

scene_B_wrong = Room("death",
'''
Scene B, wrong option
''')

scene_C = Room("Scene C",
'''
Scene C

What is {}?
'''.format(SCENE_C_EQUATION[0]))

scene_C_wrong = Room("death", 
'''
Scene C, wrong option
''')

scene_D = Room("Scene D",
'''
Scene D

What is {}?
'''.format(SCENE_D_EQUATION[0]))

the_end_winner = Room("The End",
'''
The End: Nice
''')

the_end_loser = Room("The End",
'''
The End
''')

###################################################################################################################
# Add Paths
###################################################################################################################

scene_A.add_paths({
    str(SCENE_A_EQUATION[1]): scene_B,
    '*': scene_A_option_1
})

scene_B.add_paths({
    str(SCENE_B_EQUATION[1]): scene_C,
    '*': scene_B_wrong
})

scene_C.add_paths({
    str(SCENE_C_EQUATION[1]): scene_D,
    '*': scene_C_wrong
})

scene_D.add_paths({
    str(SCENE_D_EQUATION[1]): the_end_winner,
    '*': the_end_loser
})

###################################################################################################################

START = 'scene_A'

def load_room(name):
    return globals().get(name)

def name_room(room):
    for key, value in globals().items():
        if value == room:
            return key