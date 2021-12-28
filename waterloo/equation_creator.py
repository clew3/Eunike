import random

def random_equation():
    '''
    Returns a tuple of an equation paired with its answer
    random_equation: None -> (listof Str Str)
    '''
    operator = random.choice([' + ', 
                              ' - ', 
                              ' * ',
                              ' / ',
                              ])

    rand1 = random.randrange(2,100)
    rand2 = random.randrange(1,rand1)
    equation = str(rand1) + operator + str(rand2)
    return (equation, str(eval(equation)))

# Add nuances