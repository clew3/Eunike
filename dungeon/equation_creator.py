import random

def random_equation():
    '''
    Returns a tuple of an equation paired with its answer
    random_equation: None -> (listof Str Int)
    '''
    operator = random.choice([' + ', 
                              ' - ', 
                              ' * ',
                              ' / ',
                              ])

    rand1 = str(random.randrange(100))
    rand2 = str(random.randrange(100))
    equation = rand1 + operator + rand2
    return (equation, eval(equation))
