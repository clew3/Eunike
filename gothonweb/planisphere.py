class Room(object):

    def __init__(self, name, description):
        self.name = name
        self.description = description
        self.paths = {}
    
    def go(self, direction):
        return self.paths.get(direction, None)
    
    def add_paths(self, paths):
        self.paths.update(paths)


central_corridor = Room("Central Corridor",
'''
The Gothons have invaded your ship. Last surviving member. 
Must grab bomb from armory, put it in the bridge, blow ship up, 
escape in pod.

You're running down the central corridor when you bump into a
Gothon. He's blocking the armory door and will blast you. wyd?

Options: 'shoot' 'dodge' 'tell a joke'
''')


laser_weapon_armory = Room("Laser Weapon Armory",
'''
Luckily, you tell a joke. He bursts out laughing and you zap him.
You find the neutron bomb inside the armory. There's a keypad, and you 
have 10 tries to open the 3 digit lock. wyd?

Options: '0132', '*'
''')


the_bridge = Room("The Bridge",
'''
You grab bomb and run towards the bridge. Bursting onto bridge you 
surprise five Gothons who see your active bomb. wyd?

Options: 'throw the bomb' 'slowly place the bomb'
''')

escape_pod = Room("Escape Pod",
'''
You put bomb under hostage and escape into the pod after placing bomb
on the floor. You reach the escape pod chamber. There are five but some
could be damaged. Can only check one. wyd?
''')

the_end_winner = Room("The End",
'''
You jump into the right pod and escape. You've won!
''')

the_end_loser = Room("The End",
'''
You jump into the wrong pod. Bomb explodes while you're inside.
''')

escape_pod.add_paths({'2': the_end_winner,
                      '*': the_end_loser
})

central_corridor_shoot = Room("death",
'''
Quick on the draw you yank out your blaster and fire it at the Gothon.
He flies into blind rage and blasts you and eats you
''')

central_corridor_dodge = Room("death",
'''
Like a world class boxer you dodge, weave, slip and slide right past him.
You hit your head and he eats you.
''')

laser_weapon_armory_wrong = Room("death",
'''
The lock buzzes one last time and then you hear a sickening
melting sound. You die.
''')

the_bridge_throw = Room("death", 
'''
In a panic you throw the bomb at the group of Gothons and
it goes off.
''')

the_bridge.add_paths({
    'throw the bomb': the_bridge_throw,
    'slowly place the bomb': escape_pod
})

laser_weapon_armory.add_paths({
    '0132': the_bridge,
    '*': laser_weapon_armory_wrong
})

central_corridor.add_paths({
    'shoot': central_corridor_shoot,
    'dodge': central_corridor_dodge,
    'tell a joke': laser_weapon_armory
})

START = 'central_corridor'

def load_room(name):
    return globals().get(name)

def name_room(room):
    for key, value in globals().items():
        if value == room:
            return key

'''
TODO:  don't expose globals (make sure can't jump sequence)
       randomize variables
       mathemzize it
'''